import fs from 'fs';
import path from 'path';

function fixArticlesPublications(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Fix hardcoded 'fr' translation
  content = content.replace(/const t = useTranslations\('fr'\);/, `const t = useTranslations(lang);`);

  // Fix hardcoded links
  content = content.replace(/href=\{`\/articles\//g, 'href={`/${lang}/articles/');
  content = content.replace(/href=\{`\/publications\//g, 'href={`/${lang}/publications/');

  fs.writeFileSync(filePath, content);
  console.log("Fixed " + filePath);
}

fixArticlesPublications(path.join('src', 'pages', '[lang]', 'articles.astro'));
fixArticlesPublications(path.join('src', 'pages', '[lang]', 'publications.astro'));
