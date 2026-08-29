import fs from 'fs';
import path from 'path';

function fixLayout(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Replace path extraction logic
  const oldLogic = `// Dterminer le chemin sans la langue pour le slecteur de langue
const currentPath = Astro.url.pathname;
const pathWithoutLang = currentPath.replace(new RegExp(\`^/\\\${lang}\`), '') || '/';`;

  const newLogic = `// Extraire de manière robuste le chemin sans la langue
const currentPath = Astro.url.pathname;
let pathWithoutLang = currentPath;
const langs = ['fr', 'en', 'ar'];
for (const l of langs) {
  if (pathWithoutLang.startsWith(\`/\${l}/\`)) {
    pathWithoutLang = pathWithoutLang.substring(l.length + 1);
    break;
  } else if (pathWithoutLang === \`/\${l}\`) {
    pathWithoutLang = '/';
    break;
  }
}
if (!pathWithoutLang.startsWith('/')) {
  pathWithoutLang = '/' + pathWithoutLang;
}`;

  // Replace with a slightly more flexible regex matching in case encoding messed up the previous replace
  // Just rewrite it entirely safely
  content = content.replace(/\/\/ D.*?terminer le chemin sans la langue pour le s.*?lecteur de langue\s*const currentPath = Astro\.url\.pathname;\s*const pathWithoutLang = currentPath\.replace\(new RegExp\(`\^\/\\\${lang}`\), ''\) \|\| '\/';/, newLogic);
  
  // Actually, wait, let's just use string replace for the exact code
  content = content.replace(`// D\uFFFDterminer le chemin sans la langue pour le s\uFFFDlecteur de langue\nconst currentPath = Astro.url.pathname;\nconst pathWithoutLang = currentPath.replace(new RegExp(\`^/\\\${lang}\`), '') || '/';`, newLogic);
  
  // If the above replace fails due to encoding, let's use a regex
  content = content.replace(/\/\/ D[^\n]*\nconst currentPath = Astro\.url\.pathname;\nconst pathWithoutLang = [^\n]*;/m, newLogic);
  
  // Also, check if there are other hardcoded links in Layout.astro
  content = content.replace(/href=\{`\/\${lang}\/services`\}/g, "href={`/${lang}/services`}"); // just to be sure it's valid

  fs.writeFileSync(filePath, content);
  console.log("Fixed Layout path extraction.");
}

fixLayout(path.join('src', 'layouts', 'Layout.astro'));
