// Serveur proxy simple pour contourner CORS
// Lancé avec: node proxy-server.js

const http = require('http');
const https = require('https');
const url = require('url');

const APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwAxwjbBkjXb5bbg_VpO3l2txuZL4ebTamVtcG5AEmloseIVjINjbWSyEY4lLsMicj8sg/exec';

const server = http.createServer((req, res) => {
  // Headers CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Content-Type', 'application/json');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  if (req.url === '/proxy' && req.method === 'GET') {
    console.log('[Proxy] Récupération de', APPS_SCRIPT_URL);

    https.get(APPS_SCRIPT_URL, (googleRes) => {
      let data = '';

      googleRes.on('data', (chunk) => {
        data += chunk;
      });

      googleRes.on('end', () => {
        try {
          const jsonData = JSON.parse(data);
          console.log('[Proxy] Réponse reçue, statut:', googleRes.statusCode);
          res.writeHead(200);
          res.end(JSON.stringify(jsonData));
        } catch (e) {
          console.error('[Proxy] Erreur parsing JSON:', e.message);
          res.writeHead(500);
          res.end(JSON.stringify({
            success: false,
            error: 'Erreur: réponse JSON invalide du script Google'
          }));
        }
      });
    }).on('error', (err) => {
      console.error('[Proxy] Erreur HTTPS:', err.message);
      res.writeHead(500);
      res.end(JSON.stringify({
        success: false,
        error: 'Erreur réseau: ' + err.message
      }));
    });
  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: 'Route non trouvée' }));
  }
});

server.listen(3001, () => {
  console.log('✅ Proxy serveur lancé sur http://localhost:3001/proxy');
  console.log('📍 Utilisez cette URL dans index.html');
});
