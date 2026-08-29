import fs from 'fs';
import path from 'path';

function localizePubs(filePath, isSlug) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Helper function injected? We can just do inline: pub[\`title_\${lang}\`] || pub.title
  if (isSlug) {
    // In [slug].astro, the variable is \`publication\`
    content = content.replace(/\{publication\.title([^}]*)\}/g, "{publication[`title_${lang}` as keyof typeof publication] || publication.title$1}");
    content = content.replace(/\{publication\.excerpt([^}]*)\}/g, "{publication[`excerpt_${lang}` as keyof typeof publication] || publication.excerpt$1}");
    
    // For description, it's an array and mapped over
    content = content.replace(/publication\.description\.map/g, "(publication[`description_${lang}` as keyof typeof publication] || publication.description).map");
    // Also meta_title
    content = content.replace(/publication\.meta_title \|\| publication\.title/g, "publication.meta_title || (publication[`title_${lang}` as keyof typeof publication] as string) || publication.title");
    
    // In <head> meta tags:
    content = content.replace(/content=\{publication\.excerpt([^}]*)\}/g, 'content={publication[`excerpt_${lang}` as keyof typeof publication] || publication.excerpt$1}');
  } else {
    // In publications.astro, the variable is \`pub\` inside map
    content = content.replace(/\{pub\.title([^}]*)\}/g, "{pub[`title_${lang}` as keyof typeof pub] || pub.title$1}");
    content = content.replace(/\{pub\.excerpt([^}]*)\}/g, "{pub[`excerpt_${lang}` as keyof typeof pub] || pub.excerpt$1}");
    content = content.replace(/pub\.description\?\.\[0\]/g, "(pub[`description_${lang}` as keyof typeof pub] || pub.description)?.[0]");
  }

  // Handle TS errors by adding \`@ts-ignore\` or type assertion, actually Astro compiles with esbuild so it strips types, but in .astro files it's fine.
  
  fs.writeFileSync(filePath, content);
  console.log("Updated " + filePath);
}

localizePubs(path.join('src', 'pages', '[lang]', 'publications.astro'), false);
localizePubs(path.join('src', 'pages', '[lang]', 'publications', '[slug].astro'), true);
