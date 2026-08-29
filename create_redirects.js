import fs from 'fs';
import path from 'path';

const pagesDir = path.join('src', 'pages');

const staticPages = [
  'accueil.astro', 'apropos.astro', 'articles.astro', 'cgu.astro', 
  'contact.astro', 'livre.astro', 'mentions-legales.astro', 
  'politique-confidentialite.astro', 'publications.astro', 'services.astro'
];

for (const page of staticPages) {
  const pageName = page.replace('.astro', '');
  const content = `---
---
<meta http-equiv="refresh" content={\`0;url=/fr/\${'${pageName}' === 'accueil' ? '' : '${pageName}'}\`} />
`;
  fs.writeFileSync(path.join(pagesDir, page), content);
}

// Recreate articles/[slug].astro for redirection
const articlesDir = path.join(pagesDir, 'articles');
if (!fs.existsSync(articlesDir)) fs.mkdirSync(articlesDir);
const articlesContent = `---
import { articles } from '../../data/articles';

export async function getStaticPaths() {
  return articles.map(a => ({
    params: { slug: a.slug }
  }));
}
const { slug } = Astro.params;
---
<meta http-equiv="refresh" content={\`0;url=/fr/articles/\${slug}\`} />
`;
fs.writeFileSync(path.join(articlesDir, '[slug].astro'), articlesContent);

// Recreate publications/[slug].astro for redirection
const pubsDir = path.join(pagesDir, 'publications');
if (!fs.existsSync(pubsDir)) fs.mkdirSync(pubsDir);
const pubsContent = `---
import { publications } from '../../data/publications';

export async function getStaticPaths() {
  return publications.map(p => ({
    params: { slug: p.slug }
  }));
}
const { slug } = Astro.params;
---
<meta http-equiv="refresh" content={\`0;url=/fr/publications/\${slug}\`} />
`;
fs.writeFileSync(path.join(pubsDir, '[slug].astro'), pubsContent);

console.log("Created redirects for old URLs.");
