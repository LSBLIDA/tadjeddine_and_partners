const ROOT_FOLDER_ID = '1ni0Wj26Tybs1uR9YF2CA421kU7qo22-q';

function doGet() {
  try {
    Logger.log("[doGet] Debut d'execution");
    const payload = getDriveTree(ROOT_FOLDER_ID);

    return ContentService
      .createTextOutput(JSON.stringify({
        success: true,
        timestamp: new Date().toISOString(),
        ...payload
      }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    const errorMessage = error && error.message ? error.message : String(error);
    Logger.log('[doGet] ERREUR: ' + errorMessage);

    return ContentService
      .createTextOutput(JSON.stringify({
        success: false,
        error: errorMessage,
        stack: error && error.stack ? String(error.stack) : 'N/A'
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function getDriveTree(rootFolderId) {
  Logger.log('[getDriveTree] Recherche du dossier: ' + rootFolderId);
  const rootFolder = DriveApp.getFolderById(rootFolderId);

  const rootData = buildFolderPayload(rootFolder, {
    includeNestedFolders: false,
    folderLabel: rootFolder.getName()
  });

  const folders = [];
  const folderIterator = rootFolder.getFolders();

  while (folderIterator.hasNext()) {
    const folder = folderIterator.next();
    Logger.log('[getDriveTree] Traitement dossier: ' + folder.getName());
    folders.push(buildFolderPayload(folder));
  }

  folders.sort(compareByName);

  return {
    rootFolder: {
      id: rootFolder.getId(),
      name: rootFolder.getName(),
      webViewLink: rootFolder.getUrl()
    },
    rootFiles: rootData.files,
    folders: folders
  };
}

function buildFolderPayload(folder, options) {
  const opts = options || {};
  const allFiles = [];
  const fileIterator = folder.getFiles();

  while (fileIterator.hasNext()) {
    allFiles.push(fileIterator.next());
  }

  const jsonFiles = allFiles.filter(isVideoJsonFile);

  let extraVideoLinks = [];
  for (let i = 0; i < jsonFiles.length; i++) {
    try {
      const parsed = parseJsonFileToItems(jsonFiles[i], folder.getName());
      Logger.log('[buildFolderPayload] parsed ' + parsed.length + ' items from ' + jsonFiles[i].getName());
      extraVideoLinks = extraVideoLinks.concat(parsed);
    } catch (error) {
      Logger.log('[buildFolderPayload] ERREUR parsing ' + jsonFiles[i].getName() + ': ' + error.message);
    }
  }

  const files = [];
  for (let i = 0; i < allFiles.length; i++) {
    const file = allFiles[i];
    if (containsFileId(jsonFiles, file.getId())) {
      continue;
    }

    files.push(toDriveFileItem(file));
  }

  if (extraVideoLinks.length) {
    files.push.apply(files, extraVideoLinks);
  }

  if (opts.includeNestedFolders !== false) {
    const nestedFolders = folder.getFolders();
    while (nestedFolders.hasNext()) {
      const nested = nestedFolders.next();
      files.push({
        id: nested.getId(),
        name: nested.getName(),
        mimeType: 'application/vnd.google-apps.folder',
        modifiedTime: new Date().toISOString(),
        webViewLink: nested.getUrl(),
        downloadLink: nested.getUrl()
      });
    }
  }

  files.sort(compareByName);

  return {
    id: folder.getId(),
    name: opts.folderLabel || folder.getName(),
    webViewLink: folder.getUrl(),
    files: files
  };
}

function isVideoJsonFile(file) {
  const name = normalizeFileName(file.getName());
  const mimeType = file.getMimeType();

  if (name === 'video-links.json') {
    return true;
  }

  if (name.endsWith('.json') && (name.indexOf('video') !== -1 || name.indexOf('link') !== -1)) {
    return true;
  }

  return mimeType === 'application/json' && (
    name.indexOf('video') !== -1 ||
    name.indexOf('link') !== -1
  );
}

function parseJsonFileToItems(file, folderName) {
  Logger.log('[parseJsonFileToItems] Lecture de ' + file.getName() + ' (mime: ' + file.getMimeType() + ')');

  let content = '';
  try {
    const mimeType = file.getMimeType();
    if (mimeType === MimeType.GOOGLE_DOCS || mimeType === 'application/vnd.google-apps.document') {
      content = DocumentApp.openById(file.getId()).getBody().getText();
    } else {
      content = file.getBlob().getDataAsString('UTF-8');
    }
  } catch (error) {
    throw new Error('Erreur lecture du fichier: ' + error.message);
  }

  let items;
  try {
    items = JSON.parse(content);
  } catch (error) {
    throw new Error('JSON invalide dans ' + file.getName() + ': ' + error.message);
  }

  if (!Array.isArray(items)) {
    throw new Error("Le JSON doit etre un tableau d'objets.");
  }

  const output = [];
  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    if (!item || !item.webViewLink) {
      continue;
    }

    output.push({
      id: item.id || ('video-json-' + file.getId() + '-' + i),
      name: item.name || ('Video ' + (i + 1)),
      mimeType: item.mimeType || 'video/youtube',
      modifiedTime: item.modifiedTime || new Date().toISOString(),
      webViewLink: item.webViewLink,
      downloadLink: item.downloadLink || item.webViewLink,
      source: folderName || ''
    });
  }

  Logger.log('[parseJsonFileToItems] renvoye ' + output.length + ' items');
  return output;
}

function toDriveFileItem(file) {
  const updatedAt = file.getLastUpdated();

  return {
    id: file.getId(),
    name: file.getName(),
    mimeType: file.getMimeType(),
    modifiedTime: updatedAt ? updatedAt.toISOString() : new Date().toISOString(),
    webViewLink: file.getUrl(),
    downloadLink: 'https://drive.google.com/uc?export=download&id=' + file.getId()
  };
}

function containsFileId(files, fileId) {
  for (let i = 0; i < files.length; i++) {
    if (files[i].getId() === fileId) {
      return true;
    }
  }
  return false;
}

function compareByName(a, b) {
  return String(a.name || '').localeCompare(String(b.name || ''), 'fr', {
    sensitivity: 'base'
  });
}

function normalizeFileName(name) {
  return String(name || '')
    .toLowerCase()
    .replace(/^\uFEFF/, '')
    .trim();
}
