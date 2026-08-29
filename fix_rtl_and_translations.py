import os
import json
import re

# Fix CSS in politique-confidentialite.astro
file_path = os.path.join('src', 'pages', '[lang]', 'politique-confidentialite.astro')
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('padding-left: 1.5rem;', 'padding-inline-start: 1.5rem;')
content = content.replace('left: 0;', 'inset-inline-start: 0;')
content = content.replace('border-left: 4px solid', 'border-inline-start: 4px solid')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update Arabic translations
locales_path = os.path.join('src', 'locales', 'ar.json')
with open(locales_path, 'r', encoding='utf-8') as f:
    ar_data = json.load(f)

# The user asked to change: 
# "Le responsable de traitement" -> "المسؤول عن المعالجة"
# "Le sous-traitant" -> "المعالج من الباطن"

# In the JSON for privacy:
# "المراقب للبيانات" was used for "responsable du traitement"
# "مقاولين من الباطن" was used for "sous-traitants"

for section in ar_data['privacy']['sections']:
    section['title'] = section['title'].replace("المراقب للبيانات", "المسؤول عن المعالجة")
    section['content'] = section['content'].replace("المراقب للبيانات", "المسؤول عن المعالجة")
    section['content'] = section['content'].replace("مراقباً للبيانات", "مسؤولاً عن المعالجة")
    
    section['content'] = section['content'].replace("مقاولين من الباطن", "معالجين من الباطن")

with open(locales_path, 'w', encoding='utf-8') as f:
    json.dump(ar_data, f, ensure_ascii=False, indent=2)

print("Fixed CSS and updated Arabic translations.")
