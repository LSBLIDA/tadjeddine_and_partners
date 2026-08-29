import os
import json

locales_dir = os.path.join('src', 'locales')

translations = {
    "fr": {
        "mentions": {
            "title": "Mentions légales",
            "page_title": "Mentions légales",
            "sections": [
                {
                    "title": "Éditeur du site",
                    "content": "<strong>eurl Tadjeddine & Partners au capital de 20.000.000 DA</strong><br />Adresse : Rue G N° 1, Cité Naimi Centre Zabana, Blida – Algérie<br />RC : 10B0981001 - NIF : 001016098100195 - AI : 09010399908<br />Email : <a href='mailto:info@tadjeddine-partners.com'>info@tadjeddine-partners.com</a><br />Téléphone : 05.60.403.405 / 05.60.349.059<br />Gérant : TADJEDDINE BACHIR"
                },
                {
                    "title": "Hébergement",
                    "content": "Djezzy Cloud<br />Route de wilaya, Lot n°37/4, Dar El Beida, Alger, Algérie<br />Email : contact@djezzy.dz"
                },
                {
                    "title": "Propriété intellectuelle",
                    "content": "L'ensemble des contenus présents sur le site (textes, images, vidéos, logos, etc.) sont la propriété exclusive de <strong>eurl Tadjeddine & Partners</strong>, sauf mention contraire. Toute reproduction, distribution ou réutilisation, totale ou partielle, est strictement interdite sans autorisation écrite préalable."
                },
                {
                    "title": "Protection des données personnelles",
                    "content": "Pour en savoir plus sur la collecte et le traitement de vos données, veuillez consulter notre <a href='/{lang}/politique-confidentialite'>Politique de confidentialité</a>."
                },
                {
                    "title": "Conditions d'utilisation",
                    "content": "L'utilisation du site implique l'acceptation pleine et entière des conditions générales d'utilisation (CGU). L’éditeur se réserve le droit de modifier ces conditions à tout moment."
                },
                {
                    "title": "Liens hypertextes",
                    "content": "Des liens vers d'autres sites peuvent être proposés. <strong>Tadjeddine & Partners</strong> décline toute responsabilité quant aux contenus externes accessibles depuis ces liens."
                },
                {
                    "title": "Droit applicable",
                    "content": "Les présentes mentions légales sont régies par le droit algérien. En cas de litige, les tribunaux du ressort de Blida sont seuls compétents."
                }
            ]
        }
    },
    "en": {
        "mentions": {
            "title": "Legal Mentions",
            "page_title": "Legal Mentions",
            "sections": [
                {
                    "title": "Site Publisher",
                    "content": "<strong>eurl Tadjeddine & Partners with a capital of 20,000,000 DA</strong><br />Address: Rue G N° 1, Cité Naimi Centre Zabana, Blida – Algeria<br />CR: 10B0981001 - TIN: 001016098100195 - AI: 09010399908<br />Email: <a href='mailto:info@tadjeddine-partners.com'>info@tadjeddine-partners.com</a><br />Phone: 05.60.403.405 / 05.60.349.059<br />Manager: TADJEDDINE BACHIR"
                },
                {
                    "title": "Hosting",
                    "content": "Djezzy Cloud<br />Route de wilaya, Lot n°37/4, Dar El Beida, Algiers, Algeria<br />Email: contact@djezzy.dz"
                },
                {
                    "title": "Intellectual Property",
                    "content": "All contents on the site (texts, images, videos, logos, etc.) are the exclusive property of <strong>eurl Tadjeddine & Partners</strong>, unless otherwise noted. Any total or partial reproduction, distribution, or reuse is strictly prohibited without prior written authorization."
                },
                {
                    "title": "Protection of Personal Data",
                    "content": "To learn more about the collection and processing of your data, please consult our <a href='/{lang}/politique-confidentialite'>Privacy Policy</a>."
                },
                {
                    "title": "Terms of Use",
                    "content": "Use of the site implies full acceptance of the general terms of use (TOU). The publisher reserves the right to modify these terms at any time."
                },
                {
                    "title": "Hyperlinks",
                    "content": "Links to other sites may be provided. <strong>Tadjeddine & Partners</strong> declines all responsibility for external content accessible from these links."
                },
                {
                    "title": "Applicable Law",
                    "content": "These legal mentions are governed by Algerian law. In the event of a dispute, the courts of Blida have exclusive jurisdiction."
                }
            ]
        }
    },
    "ar": {
        "mentions": {
            "title": "إشعارات قانونية",
            "page_title": "إشعارات قانونية",
            "sections": [
                {
                    "title": "ناشر الموقع",
                    "content": "<strong>eurl Tadjeddine & Partners برأس مال 20,000,000 دينار جزائري</strong><br />العنوان: شارع ج رقم 1، حي نعيمي وسط زبانا، البليدة – الجزائر<br />السجل التجاري: 10B0981001 - رقم التعريف الجبائي: 001016098100195 - رقم التعريف الإحصائي: 09010399908<br />البريد الإلكتروني: <a href='mailto:info@tadjeddine-partners.com'>info@tadjeddine-partners.com</a><br />الهاتف: 05.60.403.405 / 05.60.349.059<br />المدير: تاج الدين بشير"
                },
                {
                    "title": "الاستضافة",
                    "content": "Djezzy Cloud<br />طريق الولاية، القطعة رقم 37/4، الدار البيضاء، الجزائر العاصمة، الجزائر<br />البريد الإلكتروني: contact@djezzy.dz"
                },
                {
                    "title": "الملكية الفكرية",
                    "content": "جميع المحتويات الموجودة على الموقع (نصوص، صور، مقاطع فيديو، شعارات، إلخ) هي ملك حصري لـ <strong>eurl Tadjeddine & Partners</strong>، ما لم يذكر خلاف ذلك. يمنع منعاً باتاً أي استنساخ أو توزيع أو إعادة استخدام كلي أو جزئي دون إذن كتابي مسبق."
                },
                {
                    "title": "حماية البيانات الشخصية",
                    "content": "لمعرفة المزيد حول جمع ومعالجة بياناتك، يرجى الرجوع إلى <a href='/{lang}/politique-confidentialite'>سياسة الخصوصية</a> الخاصة بنا."
                },
                {
                    "title": "شروط الاستخدام",
                    "content": "استخدام الموقع يعني القبول التام لشروط الاستخدام العامة (CGU). يحتفظ الناشر بالحق في تعديل هذه الشروط في أي وقت."
                },
                {
                    "title": "روابط نصية",
                    "content": "قد يتم توفير روابط لمواقع أخرى. لا تتحمل <strong>Tadjeddine & Partners</strong> أي مسؤولية عن المحتويات الخارجية التي يمكن الوصول إليها من هذه الروابط."
                },
                {
                    "title": "القانون المعمول به",
                    "content": "تخضع هذه الإشعارات القانونية للقانون الجزائري. في حالة وجود نزاع، يكون لمحاكم البليدة الاختصاص الحصري."
                }
            ]
        }
    }
}

for lang in ["fr", "en", "ar"]:
    file_path = os.path.join(locales_dir, f"{lang}.json")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['mentions'] = translations[lang]['mentions']
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Mentions translations.")

mentions_path = os.path.join('src', 'pages', '[lang]', 'mentions-legales.astro')
content = """---
export function getStaticPaths() {
  return [
    { params: { lang: 'fr' } },
    { params: { lang: 'en' } },
    { params: { lang: 'ar' } }
  ];
}
const { lang } = Astro.params;

import Layout from '../../layouts/Layout.astro';
import { useTranslations } from '../../i18n/utils';
const t = useTranslations(lang);
const sections = t('mentions.sections') || [];
---

<Layout title={t('mentions.page_title')}>
  <section class="mentions-legales">
    <div class="container">

      <h1>{t('mentions.title')}</h1>

      {Array.isArray(sections) && sections.map((section: any) => (
        <div class="card">
          <h2>{section.title}</h2>
          <p set:html={section.content.replace('{lang}', lang)}></p>
        </div>
      ))}

    </div>
  </section>

  <style>
    .mentions-legales {
      padding: 60px 0;
      background-color: #0f172a;
      color: #fff;
    }

    .mentions-legales h1 {
      text-align: center;
      margin-bottom: 40px;
    }

    .mentions-legales a {
      color: #ccc;
      text-decoration: underline;
    }

    .container {
      max-width: 900px;
      margin: auto;
    }

    .card {
      background-color: #1e1e2f;
      padding: 20px;
      border-radius: 10px;
      margin-bottom: 20px;
      box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }

    .card h2 {
      margin-top: 0;
      color: #fff;
    }
    .card p :global(a) {
        color: #d4af37;
        text-decoration: none;
    }
    .card p :global(a:hover) {
        text-decoration: underline;
    }
  </style>
</Layout>
"""
with open(mentions_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated mentions-legales.astro")
