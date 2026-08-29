<?php
// Script de diagnostic pour tester l'API Google Apps Script

$google_url = 'https://script.google.com/macros/s/AKfycbwAxwjbBkjXb5bbg_VpO3l2txuZL4ebTamVtcG5AEmloseIVjINjbWSyEY4lLsMicj8sg/exec';

echo '<h1>Test API Google Apps Script</h1>';
echo '<pre>';

// Vérifier si on peut accéder à l'URL
echo "URL testée: " . $google_url . "\n";
echo "---\n";

// Options pour file_get_contents
$context_options = [
    'http' => [
        'method' => 'GET',
        'timeout' => 10,
        'User-Agent' => 'Mozilla/5.0'
    ],
    'https' => [
        'method' => 'GET',
        'timeout' => 10,
        'verify_peer' => false,
        'verify_peer_name' => false,
        'User-Agent' => 'Mozilla/5.0'
    ]
];

try {
    $context = stream_context_create($context_options);
    $response = file_get_contents($google_url, false, $context);
    
    if ($response === false) {
        echo "❌ Impossible de récupérer l'URL\n";
        echo "Erreur: " . error_get_last()['message'] . "\n";
    } else {
        echo "✅ Réponse reçue (première 1000 caractères):\n\n";
        echo htmlspecialchars(substr($response, 0, 1000));
        echo "\n\n---\n";
        echo "Longueur totale: " . strlen($response) . " caractères\n\n";
        
        // Essayer de parser en JSON
        $data = json_decode($response, true);
        if ($data === null) {
            echo "❌ La réponse n'est PAS du JSON valide\n";
            echo "Erreur JSON: " . json_last_error_msg() . "\n";
        } else {
            echo "✅ JSON valide!\n";
            echo "Structure:\n";
            echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
        }
    }
} catch (Exception $e) {
    echo "❌ Exception: " . $e->getMessage() . "\n";
}

echo '</pre>';
?>
