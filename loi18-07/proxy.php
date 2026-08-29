<?php
// Proxy pour contourner les restrictions CORS
// Ce script récupère les données du Google Apps Script côté serveur avec gestion des redirections

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, OPTIONS');

// URL du Google Apps Script
$apps_script_url = 'https://script.google.com/macros/s/AKfycbwAxwjbBkjXb5bbg_VpO3l2txuZL4ebTamVtcG5AEmloseIVjINjbWSyEY4lLsMicj8sg/exec';

try {
    // Utiliser cURL pour mieux gérer les redirections
    if (!extension_loaded('curl')) {
        throw new Exception('Extension cURL non disponible');
    }
    
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $apps_script_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_MAXREDIRS, 5);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36');
    
    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $curl_error = curl_error($ch);
    curl_close($ch);
    
    if ($curl_error) {
        throw new Exception('Erreur cURL: ' . $curl_error);
    }
    
    if ($response === false) {
        throw new Exception('Impossible de récupérer le contenu de l\'URL (HTTP ' . $http_code . ')');
    }
    
    // Vérifier si c'est du JSON valide
    if (strpos($response, '{') !== 0) {
        // La réponse ne commence pas par {, c'est probablement du HTML
        throw new Exception('Réponse non-JSON reçue (probablement une page de login). Le script Google Apps Script n\'est pas configuré correctement. Vérifiez qu\'il retourne du JSON dans la fonction doGet().');
    }
    
    $data = json_decode($response, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception('Réponse JSON invalide: ' . json_last_error_msg());
    }
    
    echo json_encode($data);
    
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Erreur proxy: ' . $e->getMessage()
    ]);
}
?>
