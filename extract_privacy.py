import os
import json

locales_dir = os.path.join('src', 'locales')

translations = {
    "fr": {
        "privacy": {
            "page_title": "Politique de Confidentialité - Tadjeddine & Partners",
            "title": "Politique de Confidentialité",
            "company_name": "TADJEDDINE AND PARTNERS",
            "back_to_home": "Retour à l'accueil",
            "sections": [
                {
                    "title": "1. Identité du responsable du traitement",
                    "content": "<p>Conformément aux dispositions de la loi n° 18-07 du 10 juin 2018 relative à la protection des données à caractère personnel, le responsable du traitement des données collectées est <strong>TADJEDDINE AND PARTNERS</strong>, société immatriculée au Registre du Commerce sous le numéro 10B0981001, dont le siège social est situé à Cité Naimi, Rue G N° 1, Zabana, Blida, représentée par son gérant légal M. Tadjeddine BACHIR.</p><p>En sa qualité de responsable du traitement, TADJEDDINE AND PARTNERS s'engage à se conformer à l'ensemble des obligations légales et réglementaires applicables en matière de protection des données à caractère personnel.</p>"
                },
                {
                    "title": "2. Données collectées",
                    "content": "<p>Dans le cadre de ses activités commerciales, TADJEDDINE AND PARTNERS collecte et traite les données suivantes concernant ses prospects :</p><ul class=\"data-list\"><li>Nom et prénom</li><li>Adresse e-mail</li><li>Numéro de téléphone</li><li>Nom de l'entreprise</li><li>Fonction / Poste</li><li>Site web</li></ul>"
                },
                {
                    "title": "3. Finalités du traitement",
                    "content": "<p>Les données collectées sont traitées exclusivement aux fins suivantes :</p><ul class=\"purpose-list\"><li>Répondre aux demandes de contact ou d'information formulées par les prospects</li><li>Adresser des offres commerciales adaptées aux besoins exprimés</li><li>Assurer le suivi de la relation commerciale précontractuelle</li><li>Réaliser des analyses et des statistiques commerciales internes</li></ul>"
                },
                {
                    "title": "4. Destinataires des données",
                    "content": "<p>Les données à caractère personnel sont traitées exclusivement par le personnel habilité de TADJEDDINE AND PARTNERS et ne font l'objet d'aucune cession ni vente à des tiers.</p><p>Toute transmission éventuelle à des sous-traitants techniques (notamment prestataires d'envoi d'e-mails) est encadrée par un contrat intégrant des obligations strictes de confidentialité et de conformité aux dispositions de la loi n° 18-07.</p>"
                },
                {
                    "title": "5. Durée de conservation",
                    "content": "<p>Les données collectées sont conservées pendant une durée maximale de trois (3) ans à compter du dernier contact ou de la dernière interaction de la part du prospect, sauf opposition ou retrait de consentement exercé conformément aux dispositions légales.</p>"
                },
                {
                    "title": "6. Mesures de sécurité",
                    "content": "<p>TADJEDDINE AND PARTNERS met en place toutes les mesures techniques et organisationnelles appropriées pour garantir la confidentialité, l'intégrité et la disponibilité des données à caractère personnel traitées.</p>"
                },
                {
                    "title": "7. Droits des personnes concernées",
                    "content": "<p>Conformément aux articles 7 et 34 à 36 de la loi n° 18-07, toute personne concernée bénéficie des droits suivants :</p><ul class=\"rights-list\"><li>Droit d'accès à ses données à caractère personnel</li><li>Droit de rectification des données inexactes ou incomplètes</li><li>Droit d'opposition au traitement pour motifs légitimes</li><li>Droit de retrait du consentement à tout moment</li></ul><p><strong>Pour exercer ces droits, toute demande peut être adressée :</strong></p><div class=\"contact-methods\"><p><strong>Par courrier électronique</strong> à l'adresse suivante : <a href=\"mailto:info@tadjeddine-partners.com\" class=\"email-link\">info@tadjeddine-partners.com</a></p><p><strong>Par voie postale</strong> à l'adresse du siège social : TADJEDDINE AND PARTNERS, Cité Naimi, Rue G N° 1, Zabana, Blida.</p></div>"
                },
                {
                    "title": "8. Transferts internationaux de données",
                    "content": "<p>Aucun transfert de données à caractère personnel vers l'étranger n'est effectué sans l'obtention des autorisations préalables requises par la loi n° 18-07.</p>"
                },
                {
                    "title": "9. Mise à jour de la politique",
                    "content": "<p>TADJEDDINE AND PARTNERS se réserve le droit de modifier la présente politique de confidentialité à tout moment, notamment pour tenir compte de toute évolution législative ou réglementaire. La version actualisée est tenue à disposition sur demande ou via les canaux de communication habituels.</p>"
                }
            ]
        }
    },
    "en": {
        "privacy": {
            "page_title": "Privacy Policy - Tadjeddine & Partners",
            "title": "Privacy Policy",
            "company_name": "TADJEDDINE AND PARTNERS",
            "back_to_home": "Back to Home",
            "sections": [
                {
                    "title": "1. Identity of the Data Controller",
                    "content": "<p>In accordance with the provisions of Law No. 18-07 of June 10, 2018, relating to the protection of personal data, the data controller for the collected data is <strong>TADJEDDINE AND PARTNERS</strong>, a company registered in the Commercial Register under the number 10B0981001, whose head office is located at Cité Naimi, Rue G N° 1, Zabana, Blida, represented by its legal manager Mr. Tadjeddine BACHIR.</p><p>In its capacity as data controller, TADJEDDINE AND PARTNERS is committed to complying with all applicable legal and regulatory obligations regarding the protection of personal data.</p>"
                },
                {
                    "title": "2. Collected Data",
                    "content": "<p>As part of its commercial activities, TADJEDDINE AND PARTNERS collects and processes the following data concerning its prospects:</p><ul class=\"data-list\"><li>First and last name</li><li>Email address</li><li>Phone number</li><li>Company name</li><li>Job title / Position</li><li>Website</li></ul>"
                },
                {
                    "title": "3. Purposes of Processing",
                    "content": "<p>The collected data is processed exclusively for the following purposes:</p><ul class=\"purpose-list\"><li>Responding to contact or information requests made by prospects</li><li>Sending commercial offers tailored to expressed needs</li><li>Following up on pre-contractual commercial relationships</li><li>Conducting internal commercial analysis and statistics</li></ul>"
                },
                {
                    "title": "4. Data Recipients",
                    "content": "<p>Personal data is processed exclusively by authorized personnel of TADJEDDINE AND PARTNERS and is neither transferred nor sold to third parties.</p><p>Any potential transmission to technical subcontractors (notably email service providers) is governed by a contract including strict obligations of confidentiality and compliance with the provisions of Law No. 18-07.</p>"
                },
                {
                    "title": "5. Retention Period",
                    "content": "<p>Collected data is kept for a maximum period of three (3) years from the last contact or interaction from the prospect, unless opposition or withdrawal of consent is exercised in accordance with legal provisions.</p>"
                },
                {
                    "title": "6. Security Measures",
                    "content": "<p>TADJEDDINE AND PARTNERS implements all appropriate technical and organizational measures to ensure the confidentiality, integrity, and availability of processed personal data.</p>"
                },
                {
                    "title": "7. Rights of Data Subjects",
                    "content": "<p>In accordance with articles 7 and 34 to 36 of Law No. 18-07, any data subject has the following rights:</p><ul class=\"rights-list\"><li>Right of access to their personal data</li><li>Right of rectification of inaccurate or incomplete data</li><li>Right to object to processing for legitimate reasons</li><li>Right to withdraw consent at any time</li></ul><p><strong>To exercise these rights, any request can be addressed:</strong></p><div class=\"contact-methods\"><p><strong>By email</strong> to the following address: <a href=\"mailto:info@tadjeddine-partners.com\" class=\"email-link\">info@tadjeddine-partners.com</a></p><p><strong>By postal mail</strong> to the head office address: TADJEDDINE AND PARTNERS, Cité Naimi, Rue G N° 1, Zabana, Blida.</p></div>"
                },
                {
                    "title": "8. International Data Transfers",
                    "content": "<p>No transfer of personal data abroad is made without obtaining the prior authorizations required by Law No. 18-07.</p>"
                },
                {
                    "title": "9. Policy Updates",
                    "content": "<p>TADJEDDINE AND PARTNERS reserves the right to modify this privacy policy at any time, particularly to account for any legislative or regulatory developments. The updated version is made available upon request or through usual communication channels.</p>"
                }
            ]
        }
    },
    "ar": {
        "privacy": {
            "page_title": "سياسة الخصوصية - Tadjeddine & Partners",
            "title": "سياسة الخصوصية",
            "company_name": "TADJEDDINE AND PARTNERS",
            "back_to_home": "العودة إلى الصفحة الرئيسية",
            "sections": [
                {
                    "title": "1. هوية المراقب للبيانات",
                    "content": "<p>وفقًا لأحكام القانون رقم 18-07 المؤرخ 10 يونيو 2018 المتعلق بحماية البيانات الشخصية، فإن المراقب للبيانات المجمعة هو <strong>TADJEDDINE AND PARTNERS</strong>، شركة مسجلة في السجل التجاري تحت رقم 10B0981001، ويقع مقرها الرئيسي في حي نعيمي، شارع ج رقم 1، زبانا، البليدة، ويمثلها مديرها القانوني السيد تاج الدين بشير.</p><p>بصفتها مراقباً للبيانات، تلتزم TADJEDDINE AND PARTNERS بالامتثال لجميع الالتزامات القانونية والتنظيمية المعمول بها فيما يتعلق بحماية البيانات الشخصية.</p>"
                },
                {
                    "title": "2. البيانات المجمعة",
                    "content": "<p>في إطار أنشطتها التجارية، تقوم TADJEDDINE AND PARTNERS بجمع ومعالجة البيانات التالية المتعلقة بعملائها المحتملين:</p><ul class=\"data-list\"><li>الاسم واللقب</li><li>عنوان البريد الإلكتروني</li><li>رقم الهاتف</li><li>اسم الشركة</li><li>الوظيفة / المنصب</li><li>الموقع الإلكتروني</li></ul>"
                },
                {
                    "title": "3. أغراض المعالجة",
                    "content": "<p>تتم معالجة البيانات المجمعة حصريًا للأغراض التالية:</p><ul class=\"purpose-list\"><li>الرد على طلبات الاتصال أو المعلومات المقدمة من العملاء المحتملين</li><li>إرسال عروض تجارية تتناسب مع الاحتياجات المعبر عنها</li><li>متابعة العلاقات التجارية قبل التعاقدية</li><li>إجراء تحليلات وإحصاءات تجارية داخلية</li></ul>"
                },
                {
                    "title": "4. مستلمو البيانات",
                    "content": "<p>تتم معالجة البيانات الشخصية حصريًا من قبل الموظفين المصرح لهم في TADJEDDINE AND PARTNERS ولا تخضع لأي تنازل أو بيع لأطراف ثالثة.</p><p>يخضع أي نقل محتمل إلى مقاولين من الباطن تقنيين (لا سيما مزودي خدمة البريد الإلكتروني) لعقد يتضمن التزامات صارمة بالسرية والامتثال لأحكام القانون رقم 18-07.</p>"
                },
                {
                    "title": "5. فترة الاحتفاظ",
                    "content": "<p>يتم الاحتفاظ بالبيانات المجمعة لمدة أقصاها ثلاث (3) سنوات من آخر اتصال أو تفاعل من العميل المحتمل، ما لم يتم ممارسة المعارضة أو سحب الموافقة وفقًا للأحكام القانونية.</p>"
                },
                {
                    "title": "6. التدابير الأمنية",
                    "content": "<p>تضع TADJEDDINE AND PARTNERS جميع التدابير التقنية والتنظيمية المناسبة لضمان سرية وسلامة وتوافر البيانات الشخصية المعالجة.</p>"
                },
                {
                    "title": "7. حقوق أصحاب البيانات",
                    "content": "<p>وفقًا للمواد 7 و 34 إلى 36 من القانون رقم 18-07، يتمتع أي صاحب بيانات بالحقوق التالية:</p><ul class=\"rights-list\"><li>حق الوصول إلى بياناته الشخصية</li><li>حق تصحيح البيانات غير الدقيقة أو غير المكتملة</li><li>حق الاعتراض على المعالجة لأسباب مشروعة</li><li>حق سحب الموافقة في أي وقت</li></ul><p><strong>لممارسة هذه الحقوق، يمكن توجيه أي طلب:</strong></p><div class=\"contact-methods\"><p><strong>عن طريق البريد الإلكتروني</strong> إلى العنوان التالي: <a href=\"mailto:info@tadjeddine-partners.com\" class=\"email-link\">info@tadjeddine-partners.com</a></p><p><strong>عن طريق البريد</strong> إلى عنوان المقر الرئيسي: TADJEDDINE AND PARTNERS، حي نعيمي، شارع ج رقم 1، زبانا، البليدة.</p></div>"
                },
                {
                    "title": "8. نقل البيانات الدولي",
                    "content": "<p>لا يتم إجراء أي نقل للبيانات الشخصية إلى الخارج دون الحصول على التراخيص المسبقة المطلوبة بموجب القانون رقم 18-07.</p>"
                },
                {
                    "title": "9. تحديث السياسة",
                    "content": "<p>تحتفظ TADJEDDINE AND PARTNERS بالحق في تعديل سياسة الخصوصية هذه في أي وقت، ولا سيما لأخذ أي تطورات تشريعية أو تنظيمية في الاعتبار. النسخة المحدثة متاحة عند الطلب أو عبر قنوات الاتصال المعتادة.</p>"
                }
            ]
        }
    }
}

for lang in ["fr", "en", "ar"]:
    file_path = os.path.join(locales_dir, f"{lang}.json")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['privacy'] = translations[lang]['privacy']
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Privacy translations.")

privacy_path = os.path.join('src', 'pages', '[lang]', 'politique-confidentialite.astro')
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
const sections = t('privacy.sections') || [];
---

<Layout title={t('privacy.page_title')}>
	<div class="privacy-policy">
		<div class="container">
			<div class="privacy-content">
				<h1 class="privacy-title">{t('privacy.title')}</h1>
				<div class="company-name">{t('privacy.company_name')}</div>

				{Array.isArray(sections) && sections.map((section: any) => (
					<section class="privacy-section">
						<h2>{section.title}</h2>
						<div set:html={section.content}></div>
					</section>
				))}

				<div class="back-link">
					<a href={`/${lang}`} class="btn btn-primary">{t('privacy.back_to_home')}</a>
				</div>
			</div>
		</div>
	</div>
</Layout>

<style>
	.privacy-policy {
		padding: 8rem 0 4rem;
		background: #0f0f0f;
		min-height: 100vh;
	}

	.privacy-content {
		max-width: 800px;
		margin: 0 auto;
		background: rgba(31, 41, 55, 0.5);
		backdrop-filter: blur(10px);
		padding: 3rem;
		border-radius: 1rem;
		border: 1px solid rgba(55, 65, 81, 0.5);
	}

	.privacy-title {
		font-size: 2.5rem;
		font-weight: 700;
		text-align: center;
		margin-bottom: 1rem;
		background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}

	.company-name {
		text-align: center;
		font-size: 1.25rem;
		font-weight: 600;
		color: #cbd5e1;
		margin-bottom: 3rem;
		padding-bottom: 1rem;
		border-bottom: 2px solid rgba(203, 213, 225, 0.3);
	}

	.privacy-section {
		margin-bottom: 2.5rem;
	}

	.privacy-section h2 {
		font-size: 1.5rem;
		font-weight: 600;
		color: #f8fafc;
		margin-bottom: 1rem;
		padding-bottom: 0.5rem;
		border-bottom: 1px solid rgba(248, 250, 252, 0.2);
	}

	.privacy-section :global(p) {
		color: #d1d5db;
		line-height: 1.7;
		margin-bottom: 1rem;
	}

	.privacy-section :global(ul) {
		list-style: none;
		padding: 0;
		margin: 1rem 0;
	}

	.privacy-section :global(ul li) {
		color: #d1d5db;
		padding: 0.5rem 0;
		padding-left: 1.5rem;
		position: relative;
	}

	.privacy-section :global(ul li::before) {
		content: '•';
		position: absolute;
		left: 0;
		color: #f8fafc;
		font-weight: bold;
		font-size: 1.2rem;
	}

	.privacy-section :global(.contact-methods) {
		background: rgba(55, 65, 81, 0.3);
		padding: 1.5rem;
		border-radius: 0.5rem;
		margin-top: 1rem;
		border-left: 4px solid #f8fafc;
	}

	.privacy-section :global(.contact-methods p) {
		margin-bottom: 0.75rem;
	}

	.privacy-section :global(.email-link) {
		color: #f8fafc;
		text-decoration: none;
		font-weight: 500;
		transition: color 0.3s ease;
	}

	.privacy-section :global(.email-link:hover) {
		color: #cbd5e1;
	}

	.back-link {
		text-align: center;
		margin-top: 3rem;
		padding-top: 2rem;
		border-top: 1px solid rgba(248, 250, 252, 0.2);
	}

	@media (max-width: 768px) {
		.privacy-policy {
			padding: 6rem 0 3rem;
		}

		.privacy-content {
			padding: 2rem;
			margin: 0 1rem;
		}

		.privacy-title {
			font-size: 2rem;
		}

		.privacy-section :global(.contact-methods) {
			padding: 1rem;
		}
	}
</style>
"""

with open(privacy_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated politique-confidentialite.astro")
