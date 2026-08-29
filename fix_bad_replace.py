import os

slug_path = os.path.join('src', 'pages', '[lang]', 'publications', '[slug].astro')
with open(slug_path, 'r', encoding='utf-8') as f:
    slug_content = f.read()

# Fix the injected code:
bad_inject = """// Inject logic to replace '/fr/' with '/${lang}/' for external links
const redirect_url = redirect_url ? redirect_url.replace('/fr/', `/${lang}/`) : null;
const lien_achat = lien_achat && lien_achat.includes('algeriabankingindex.com') 
    ? lien_achat.replace('/fr/', `/${lang}/`) 
    : lien_achat;"""

good_inject = """// Inject logic to replace '/fr/' with '/${lang}/' for external links
const redirect_url = publication.redirect_url ? publication.redirect_url.replace('/fr/', `/${lang}/`) : null;
const lien_achat = publication.lien_achat && publication.lien_achat.includes('algeriabankingindex.com') 
    ? publication.lien_achat.replace('/fr/', `/${lang}/`) 
    : publication.lien_achat;"""

slug_content = slug_content.replace(bad_inject, good_inject)

with open(slug_path, 'w', encoding='utf-8') as f:
    f.write(slug_content)

print("Fixed publications/[slug].astro")
