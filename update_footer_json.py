import json
import os

locales_dir = os.path.join('src', 'locales')

translations = {
    'fr': {
        'footer': {
            'desc': 'Cabinet de conseil spécialisé en protection des données personnelles, conformité à la loi 18-07 et transformation digitale.',
            'nav': 'Navigation',
            'legal': 'Légal',
            'contact': 'Contact',
            'legal_mentions': 'Mentions légales',
            'privacy': 'Politique de confidentialité',
            'cgu': 'CGU',
            'country': 'Algérie',
            'rights': '© 2025 Tadjeddine & Partners. Tous droits réservés. | Transformer les idées en résultats concrets grâce à une expertise pluridisciplinaire.'
        }
    },
    'en': {
        'footer': {
            'desc': 'Consulting firm specialized in personal data protection, compliance with Law 18-07, and digital transformation.',
            'nav': 'Navigation',
            'legal': 'Legal',
            'contact': 'Contact',
            'legal_mentions': 'Legal Mentions',
            'privacy': 'Privacy Policy',
            'cgu': 'TOS',
            'country': 'Algeria',
            'rights': '© 2025 Tadjeddine & Partners. All rights reserved. | Transforming ideas into concrete results through multidisciplinary expertise.'
        }
    },
    'ar': {
        'footer': {
            'desc': 'شركة استشارية متخصصة في حماية البيانات الشخصية، والامتثال للقانون 18-07، والتحول الرقمي.',
            'nav': 'التنقل',
            'legal': 'قانوني',
            'contact': 'اتصل بنا',
            'legal_mentions': 'إشعارات قانونية',
            'privacy': 'سياسة الخصوصية',
            'cgu': 'شروط الاستخدام',
            'country': 'الجزائر',
            'rights': '© 2025 Tadjeddine & Partners. جميع الحقوق محفوظة. | تحويل الأفكار إلى نتائج ملموسة من خلال خبرة متعددة التخصصات.'
        }
    }
}

for lang in ['fr', 'en', 'ar']:
    file_path = os.path.join(locales_dir, f'{lang}.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data['footer'] = translations[lang]['footer']
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated locales with footer.")
