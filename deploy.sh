#!/bin/bash
set -e  # stoppe en cas d’erreur

PROJECT_DIR="/www/wwwroot/tadjeddine-partners.com"
PM2_NAME="astro-frontend"   # change si ton process PM2 a un autre nom

echo "🚀 [1/6] Nettoyage des anciens builds..."
rm -rf "$PROJECT_DIR/dist" "$PROJECT_DIR/.astro"
rm -f package-lock.json

echo "🚀 [2/6] Réinstallation des dépendances..."
cd "$PROJECT_DIR"
rm -rf node_modules package-lock.json
npm install

echo "🚀 [3/6] Compilation du projet..."
npm run build

echo "🚀 [4/6] Redémarrage du serveur SSR (PM2)..."
pm2 restart "$PM2_NAME" || pm2 start npm --name "$PM2_NAME" -- run start

echo "🚀 [5/6] Vérification et reload de Nginx..."
nginx -t && systemctl reload nginx

echo "🚀 [6/6] Vérifications rapides..."
curl -I https://tadjeddine-partners.com/vendor/fontawesome/css/all.min.css | head -n 1
curl -I https://tadjeddine-partners.com/_astro/ | head -n 1

echo "✅ Déploiement terminé avec succès !"
