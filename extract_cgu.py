import os
import json

locales_dir = os.path.join('src', 'locales')

translations = {
    "fr": {
        "cgu": {
            "title": "Conditions Générales d'Utilisation (CGU)",
            "page_title": "Conditions Générales d'Utilisation",
            "sections": [
                {
                    "title": "1. Objet",
                    "content": "Les présentes Conditions Générales d'Utilisation (CGU) régissent l'accès et l'utilisation du site <strong>Tadjeddine & Partners</strong>, cabinet de conseil en stratégie, organisation et transformation digitale. En accédant au site, l’utilisateur accepte sans réserve les présentes CGU."
                },
                {
                    "title": "2. Accès au site",
                    "content": "Le site est accessible gratuitement à tout utilisateur disposant d’un accès Internet. Tous les frais liés à la connexion (matériel, logiciel, abonnement, etc.) sont à la charge de l’utilisateur."
                },
                {
                    "title": "3. Services proposés",
                    "content": "<strong>Tadjeddine & Partners</strong> met à disposition des informations sur ses prestations de conseil, ses publications, ainsi que des formulaires de contact pour les demandes d’information ou de devis. Les contenus ont une vocation informative et ne constituent pas un engagement contractuel."
                },
                {
                    "title": "4. Obligations de l'utilisateur",
                    "content": "L’utilisateur s’engage à utiliser le site conformément à la législation en vigueur et à ne pas porter atteinte aux droits de <strong>Tadjeddine & Partners</strong> ou de tiers. Il lui est interdit de publier des contenus illicites, diffamatoires, ou portant atteinte à la vie privée."
                },
                {
                    "title": "5. Propriété intellectuelle",
                    "content": "L’ensemble du contenu du site (textes, images, logos, chartes graphiques, etc.) est protégé par le droit de la propriété intellectuelle et appartient à <strong>Tadjeddine & Partners</strong>. Toute reproduction ou diffusion non autorisée est strictement interdite."
                },
                {
                    "title": "6. Limitation de responsabilité",
                    "content": "Les informations diffusées sur le site sont fournies à titre indicatif. <strong>Tadjeddine & Partners</strong> ne saurait être tenue responsable en cas d’inexactitudes, omissions ou indisponibilité temporaire du site."
                },
                {
                    "title": "7. Protection des données personnelles",
                    "content": "Les données collectées via le site sont traitées conformément à la loi 18-07 relative à la protection des données personnelles. Pour plus d’informations, veuillez consulter notre <a href='/{lang}/politique-confidentialite'>Politique de confidentialité</a>."
                },
                {
                    "title": "8. Modification des CGU",
                    "content": "<strong>Tadjeddine & Partners</strong> se réserve le droit de modifier à tout moment les présentes CGU. La version applicable est celle publiée sur le site à la date de consultation."
                },
                {
                    "title": "9. Droit applicable",
                    "content": "Les présentes CGU sont régies par le droit algérien. Tout litige sera soumis à la compétence exclusive des tribunaux compétents."
                }
            ]
        }
    },
    "en": {
        "cgu": {
            "title": "Terms of Use (TOU)",
            "page_title": "Terms of Use",
            "sections": [
                {
                    "title": "1. Purpose",
                    "content": "These Terms of Use (TOU) govern the access and use of the <strong>Tadjeddine & Partners</strong> website, a consulting firm in strategy, organization, and digital transformation. By accessing the site, the user accepts these TOU without reservation."
                },
                {
                    "title": "2. Access to the Site",
                    "content": "The site is accessible free of charge to any user with internet access. All costs related to the connection (hardware, software, subscription, etc.) are the responsibility of the user."
                },
                {
                    "title": "3. Services Offered",
                    "content": "<strong>Tadjeddine & Partners</strong> provides information on its consulting services, its publications, as well as contact forms for information or quote requests. The contents are informative and do not constitute a contractual commitment."
                },
                {
                    "title": "4. User Obligations",
                    "content": "The user agrees to use the site in accordance with current legislation and not to infringe on the rights of <strong>Tadjeddine & Partners</strong> or third parties. It is strictly forbidden to publish illicit, defamatory, or privacy-infringing content."
                },
                {
                    "title": "5. Intellectual Property",
                    "content": "All site content (texts, images, logos, graphics, etc.) is protected by intellectual property rights and belongs to <strong>Tadjeddine & Partners</strong>. Any unauthorized reproduction or distribution is strictly prohibited."
                },
                {
                    "title": "6. Limitation of Liability",
                    "content": "Information on the site is provided for indicative purposes. <strong>Tadjeddine & Partners</strong> cannot be held responsible for inaccuracies, omissions, or temporary unavailability of the site."
                },
                {
                    "title": "7. Protection of Personal Data",
                    "content": "Data collected via the site is processed in accordance with Law 18-07 on the protection of personal data. For more information, please consult our <a href='/{lang}/politique-confidentialite'>Privacy Policy</a>."
                },
                {
                    "title": "8. Modification of the TOU",
                    "content": "<strong>Tadjeddine & Partners</strong> reserves the right to modify these TOU at any time. The applicable version is the one published on the site on the date of consultation."
                },
                {
                    "title": "9. Applicable Law",
                    "content": "These TOU are governed by Algerian law. Any dispute will be subject to the exclusive jurisdiction of the competent courts."
                }
            ]
        }
    },
    "ar": {
        "cgu": {
            "title": "شروط الاستخدام العامة (CGU)",
            "page_title": "شروط الاستخدام العامة",
            "sections": [
                {
                    "title": "1. الغرض",
                    "content": "تنظم شروط الاستخدام العامة هذه (CGU) الوصول إلى موقع <strong>Tadjeddine & Partners</strong> واستخدامه، وهو مكتب استشارات في الاستراتيجية والتنظيم والتحول الرقمي. من خلال الدخول إلى الموقع، يقبل المستخدم هذه الشروط دون تحفظ."
                },
                {
                    "title": "2. الوصول إلى الموقع",
                    "content": "الموقع متاح مجانًا لأي مستخدم لديه إمكانية الوصول إلى الإنترنت. يتحمل المستخدم جميع التكاليف المتعلقة بالاتصال (الأجهزة، البرمجيات، الاشتراك، إلخ)."
                },
                {
                    "title": "3. الخدمات المقدمة",
                    "content": "توفر <strong>Tadjeddine & Partners</strong> معلومات حول خدماتها الاستشارية ومنشوراتها، بالإضافة إلى نماذج اتصال لطلبات المعلومات أو عروض الأسعار. المحتويات ذات طابع إعلامي ولا تشكل التزامًا تعاقديًا."
                },
                {
                    "title": "4. التزامات المستخدم",
                    "content": "يلتزم المستخدم باستخدام الموقع وفقًا للقوانين المعمول بها وعدم المساس بحقوق <strong>Tadjeddine & Partners</strong> أو أطراف ثالثة. يُمنع منعًا باتًا نشر محتوى غير قانوني أو تشهيري أو ينتهك الخصوصية."
                },
                {
                    "title": "5. الملكية الفكرية",
                    "content": "جميع محتويات الموقع (النصوص والصور والشعارات والرسومات وما إلى ذلك) محمية بموجب حقوق الملكية الفكرية وتعود ملكيتها إلى <strong>Tadjeddine & Partners</strong>. يُحظر تمامًا أي استنساخ أو توزيع غير مصرح به."
                },
                {
                    "title": "6. حدود المسؤولية",
                    "content": "يتم توفير المعلومات المنشورة على الموقع لأغراض إعلامية. لا يمكن تحميل <strong>Tadjeddine & Partners</strong> المسؤولية في حالة وجود عدم دقة أو سهو أو عدم توفر مؤقت للموقع."
                },
                {
                    "title": "7. حماية البيانات الشخصية",
                    "content": "تتم معالجة البيانات التي يتم جمعها عبر الموقع وفقًا للقانون 18-07 المتعلق بحماية البيانات الشخصية. لمزيد من المعلومات، يرجى الرجوع إلى <a href='/{lang}/politique-confidentialite'>سياسة الخصوصية</a> الخاصة بنا."
                },
                {
                    "title": "8. تعديل شروط الاستخدام",
                    "content": "تحتفظ <strong>Tadjeddine & Partners</strong> بالحق في تعديل شروط الاستخدام هذه في أي وقت. النسخة المعمول بها هي تلك المنشورة على الموقع في تاريخ الاستشارة."
                },
                {
                    "title": "9. القانون المعمول به",
                    "content": "تخضع شروط الاستخدام هذه للقانون الجزائري. يخضع أي نزاع للاختصاص الحصري للمحاكم المختصة."
                }
            ]
        }
    }
}

for lang in ["fr", "en", "ar"]:
    file_path = os.path.join(locales_dir, f"{lang}.json")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['cgu'] = translations[lang]['cgu']
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated CGU translations.")
