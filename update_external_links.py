import os
import re

# Fix index.astro
index_path = os.path.join('src', 'pages', '[lang]', 'index.astro')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace(
    'href="https://algeriabankingindex.com/fr/editions/2025/"',
    'href={`https://algeriabankingindex.com/${lang}/editions/2025/`}'
)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)
    
print("Updated index.astro external links")

# Fix publications/[slug].astro
slug_path = os.path.join('src', 'pages', '[lang]', 'publications', '[slug].astro')
with open(slug_path, 'r', encoding='utf-8') as f:
    slug_content = f.read()

const_inject = """
const { lang } = Astro.params;
const { publication } = Astro.props;
const t = useTranslations(lang);

// Inject logic to replace '/fr/' with '/${lang}/' for external links
const redirect_url = publication.redirect_url ? publication.redirect_url.replace('/fr/', `/${lang}/`) : null;
const lien_achat = publication.lien_achat && publication.lien_achat.includes('algeriabankingindex.com') 
    ? publication.lien_achat.replace('/fr/', `/${lang}/`) 
    : publication.lien_achat;
"""

slug_content = slug_content.replace(
    "const { lang } = Astro.params;\nconst { publication } = Astro.props;\nconst t = useTranslations(lang);",
    const_inject
)

slug_content = re.sub(r'publication\.redirect_url', "redirect_url", slug_content)
slug_content = re.sub(r'publication\.lien_achat', "lien_achat", slug_content)

with open(slug_path, 'w', encoding='utf-8') as f:
    f.write(slug_content)

print("Updated publications/[slug].astro external links")
