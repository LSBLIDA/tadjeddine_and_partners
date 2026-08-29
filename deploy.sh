#!/bin/bash
# 1. Utiliser set -Eeuo pipefail pour une gestion stricte des erreurs
set -Eeuo pipefail

# 2. Définir les chemins principaux
DEPLOY_DIR="/root/tadjeddine_and_partners_deploy"
PROD_DIR="/www/wwwroot/tadjeddine-partners.com"
NODE_BIN="/www/server/nodejs/v22.23.1/bin"

# 3. Ajouter Node.js au PATH
export PATH="$NODE_BIN:$PATH"

echo "=== DÉBUT DU DÉPLOIEMENT ==="

# Se positionner dans le répertoire de déploiement (le clone Git)
cd "$DEPLOY_DIR"

# 4. Vérifications requises : versions et présence du projet
echo "[1/7] Vérification de l'environnement..."
node -v
npm -v

if [ ! -f "package.json" ]; then
    echo "Erreur critique : package.json introuvable dans $DEPLOY_DIR"
    exit 1
fi

# 6. Installation propre des dépendances et compilation
echo "[2/7] Installation des dépendances (npm ci)..."
npm ci

echo "[3/7] Compilation du projet (npm run build)..."
# 7. Si le build échoue, set -e arrêtera immédiatement l'exécution du script
npm run build

# 8. Vérifier la présence du fichier index.html généré
if [ ! -f "dist/index.html" ]; then
    echo "Erreur critique : Le build a réussi mais dist/index.html est absent."
    exit 1
fi

# 9. Création des identifiants uniques horodatés
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
DIST_NEW="dist.new-$TIMESTAMP"
DIST_BACKUP="dist.backup-$TIMESTAMP"

echo "[4/7] Préparation des répertoires et transfert vers la production..."
# 10. Copier le nouveau build dans le dossier de production sous un nom temporaire (staging)
cp -R dist "$PROD_DIR/$DIST_NEW"

# 11. Préserver les dossiers spécifiques depuis l'ancienne production
echo "[5/7] Préservation des données persistantes..."
if [ -d "$PROD_DIR/dist/.well-known" ]; then
    mkdir -p "$PROD_DIR/$DIST_NEW/.well-known"
    # L'option -n garantit que l'on n'écrase pas un fichier de la nouvelle version
    cp -rn "$PROD_DIR/dist/.well-known/"* "$PROD_DIR/$DIST_NEW/.well-known/" 2>/dev/null || true
fi

if [ -d "$PROD_DIR/dist/uploads" ]; then
    mkdir -p "$PROD_DIR/$DIST_NEW/uploads"
    cp -rn "$PROD_DIR/dist/uploads/"* "$PROD_DIR/$DIST_NEW/uploads/" 2>/dev/null || true
fi

if [ -f "$PROD_DIR/dist/vendor.tar.gz" ]; then
    if [ ! -f "$PROD_DIR/$DIST_NEW/vendor.tar.gz" ]; then
        cp "$PROD_DIR/dist/vendor.tar.gz" "$PROD_DIR/$DIST_NEW/vendor.tar.gz"
    fi
fi

# 12. Appliquer les bonnes permissions pour Nginx
chown -R www:www "$PROD_DIR/$DIST_NEW"

# 13. Vérifier Nginx AVANT de procéder à la bascule
echo "[6/7] Vérification Nginx et bascule de production..."
nginx -t

# 14. Effectuer la bascule (Zero downtime)
cd "$PROD_DIR"
if [ -d "dist" ]; then
    mv dist "$DIST_BACKUP"
fi
mv "$DIST_NEW" dist

# 15. Recharger Nginx suite à la bascule réussie
systemctl reload nginx

# 16. Effectuer des tests HTTP sur des URLs ciblées
echo "[7/7] Tests post-déploiement..."
URLS=(
    "https://tadjeddine-partners.com/"
    "https://tadjeddine-partners.com/articles/"
    "https://tadjeddine-partners.com/publications/"
    "https://tadjeddine-partners.com/banques2025/"
    "https://tadjeddine-partners.com/livre/"
    "https://tadjeddine-partners.com/loi18-07/"
)

TEST_FAILED=0

for url in "${URLS[@]}"; do
    # 17. N'accepter que le code HTTP 200 (sinon, code d'erreur simulé)
    STATUS=$(curl -o /dev/null -s -w "%{http_code}\n" "$url" || echo "000")
    if [ "$STATUS" -ne 200 ]; then
        echo "Erreur détectée : L'URL $url a retourné HTTP $STATUS (200 attendu)."
        TEST_FAILED=1
        break
    else
        echo "Test OK (HTTP 200) : $url"
    fi
done

# 18. Procédure de rollback d'urgence si un test échoue
if [ $TEST_FAILED -eq 1 ]; then
    echo "⚠️ Échec des tests, lancement de la restauration..."
    cd "$PROD_DIR"
    
    if [ -d "$DIST_BACKUP" ]; then
        rm -rf dist
        mv "$DIST_BACKUP" dist
        systemctl reload nginx || true
    fi
    
    echo "ROLLBACK EFFECTUE"
    exit 1
fi

# 19. Message de validation et clôture
echo "======================================"
echo "DEPLOIEMENT REUSSI"
echo "Backup de l'ancienne version conservé sous : $PROD_DIR/$DIST_BACKUP"
echo "======================================"
