import os
import json

file_path = os.path.join('src', 'data', 'publications.ts')

content = r"""export interface Publication {
  slug: string;
  title: string;
  title_en?: string;
  title_ar?: string;
  meta_title?: string;
  date_mise_en_ligne: string;
  display_date?: string;
  image_couverture: string;
  description: string[];
  description_en?: string[];
  description_ar?: string[];
  excerpt?: string;
  excerpt_en?: string;
  excerpt_ar?: string;
  prix?: number | string;
  is_free?: boolean;
  apercu_url?: string | null;
  fichier_url?: string | null;
  lien_achat?: string | null;
  redirect_url?: string | null;
}

export const publications: Publication[] = [
  {
    slug: "abix-etude-sectorielle-analyse-secteur-bancaire-algerien-2025",
    title: "ABIX – Étude sectorielle : Analyse du secteur bancaire algérien 2025",
    title_en: "ABIX – Sectoral Study: Analysis of the Algerian Banking Sector 2025",
    title_ar: "ABIX – دراسة قطاعية: تحليل القطاع المصرفي الجزائري 2025",
    meta_title: "ABIX – Étude sectorielle : Analyse du secteur bancaire algérien 2025",
    date_mise_en_ligne: "2026-08-01",
    display_date: "Août 2026",
    image_couverture: "/uploads/abix-2026.jpg",
    description: [
      "L’édition 2026 d’ABIX propose une analyse approfondie des performances 2025 du secteur bancaire algérien, avec comparaisons entre banques, ratios financiers, classements, tendances sectorielles et perspectives."
    ],
    description_en: [
      "The 2026 edition of ABIX offers an in-depth analysis of the 2025 performances of the Algerian banking sector, with comparisons between banks, financial ratios, rankings, sectoral trends, and perspectives."
    ],
    description_ar: [
      "تقدم نسخة 2026 من ABIX تحليلًا متعمقًا لأداء القطاع المصرفي الجزائري لعام 2025، مع مقارنات بين البنوك، والنسب المالية، والتصنيفات، والاتجاهات القطاعية، والآفاق المستقبلية."
    ],
    excerpt: "L’édition 2026 d’ABIX propose une analyse approfondie des performances 2025 du secteur bancaire algérien, avec comparaisons entre banques, ratios financiers, classements, tendances sectorielles et perspectives.",
    excerpt_en: "The 2026 edition of ABIX offers an in-depth analysis of the 2025 performances of the Algerian banking sector, with comparisons between banks, financial ratios, rankings, sectoral trends, and perspectives.",
    excerpt_ar: "تقدم نسخة 2026 من ABIX تحليلًا متعمقًا لأداء القطاع المصرفي الجزائري لعام 2025، مع مقارنات بين البنوك، والنسب المالية، والتصنيفات، والاتجاهات القطاعية، والآفاق المستقبلية.",
    prix: "À partir de 84 000 DA HT",
    is_free: false,
    apercu_url: null,
    fichier_url: null,
    lien_achat: "https://algeriabankingindex.com/fr/editions/2026/",
    redirect_url: "https://algeriabankingindex.com/fr/editions/2026/"
  },
  {
    slug: "etude-sectorielle-analyse-secteur-bancaire-algerien-2024",
    title: "Étude sectorielle – Analyse du secteur bancaire algérien 2024",
    title_en: "Sectoral Study – Analysis of the Algerian Banking Sector 2024",
    title_ar: "دراسة قطاعية – تحليل القطاع المصرفي الجزائري 2024",
    meta_title: "Étude sectorielle – Analyse du secteur bancaire algérien 2024",
    date_mise_en_ligne: "2025-08-18",
    image_couverture: "/uploads/Couverture_cc225420d6.png",
    description: [
      "Cette étude fournit une vision complète et structurée du secteur bancaire algérien, issue de l'exploitation et de l'analyse approfondie des données financières et réglementaires.",
      "Pour accéder à la présentation détaillée de l'étude sectorielle bancaire 2025, veuillez consulter notre page dédiée."
    ],
    description_en: [
      "This study provides a comprehensive and structured view of the Algerian banking sector, derived from the exploitation and in-depth analysis of financial and regulatory data.",
      "To access the detailed presentation of the 2025 banking sectoral study, please visit our dedicated page."
    ],
    description_ar: [
      "توفر هذه الدراسة رؤية شاملة ومنظمة للقطاع المصرفي الجزائري، مستمدة من استغلال والتحليل المتعمق للبيانات المالية والتنظيمية.",
      "للوصول إلى العرض التفصيلي للدراسة القطاعية المصرفية لعام 2025، يرجى زيارة صفحتنا المخصصة."
    ],
    excerpt: "Cette étude fournit une vision complète et structurée du secteur bancaire algérien, issue de l'exploitation et de l'anal",
    excerpt_en: "This study provides a comprehensive and structured view of the Algerian banking sector, derived from the exploitation...",
    excerpt_ar: "توفر هذه الدراسة رؤية شاملة ومنظمة للقطاع المصرفي الجزائري، مستمدة من استغلال والتحليل...",
    prix: 84000,
    is_free: false,
    apercu_url: "/uploads/apercu_etude_bancaire_2025_4b9a425b5b.pdf",
    fichier_url: "/uploads/Analyse_du_secteur_bancaire_edition_2025_modifs_apportees_155eaaf6fd.pdf",
    lien_achat: "https://algeriabankingindex.com/fr/editions/2025/",
    redirect_url: "https://algeriabankingindex.com/fr/editions/2025/"
  },
  {
    slug: "e-gouvernement-en-algerie-etat-des-lieux-obstacles-et-solutions",
    title: "e-Gouvernement en Algérie : état des lieux, obstacles et solutions",
    title_en: "e-Government in Algeria: Current Status, Obstacles, and Solutions",
    title_ar: "الحكومة الإلكترونية في الجزائر: الوضع الحالي، العقبات، والحلول",
    meta_title: "e-Gouvernement en Algérie : état des lieux, obstacles et solutions",
    date_mise_en_ligne: "2025-08-14",
    image_couverture: "/uploads/egov_livre_3223790e91.png",
    description: [
      "Contenu de la quatrième de couverture pour vous donner un aperçu des raisons qui m'ont motivé à écrire ce livre ainsi que des objectifs que j'espère atteindre à travers lui :",
      "\"Allah ne change rien en un peuple tant que celui-ci n'a pas changé ce qui est en lui\", ce verset coranique énonce un principe immuable qui s'applique à tous, croyants ou non croyants. Pour mettre notre pays sur la voie du progrès, il est essentiel que chacun s'implique activement plutôt que de compter uniquement sur l'État. C'est dans cet esprit que j'ai rédigé ce livre, avec l'espoir que cette contribution à l'effort collectif puisse avoir un impact positif sur le développement de notre nation.",
      "Ce livre est destiné à toutes les personnes intéressées par la transformation numérique de l’administration publique en Algérie, ainsi que celles désirant approfondir leur connaissance des enjeux et des défis liés à l’e-gouvernement.",
      "Il est destiné aux décideurs, aux journalistes, aux professionnels des secteurs public et privé, aux chercheurs, aux étudiants et à toute personne souhaitant comprendre comment les technologies de l’information peuvent améliorer les services publics, la gouvernance et la participation citoyenne.",
      "Durant mon mandat de président du GAAN (Groupement Algérien des Acteurs du Numérique 2020-2022), j’ai été régulièrement sollicité par les médias pour donner mon avis sur l’état de l’e-gouvernement en Algérie. Cependant, j’ai constaté que ce sujet était souvent mal compris par le grand public en raison de sa technicité. Ce livre vise donc à offrir une présentation exhaustive et accessible de l'e-governement en Algérie, en expliquant les concepts, les avantages et les défis rencontrés dans la mise en place de ce système."
    ],
    description_en: [
      "Back cover content to give you an overview of the reasons that motivated me to write this book and the goals I hope to achieve through it:",
      "\"Allah does not change the condition of a people until they change what is in themselves\", this Quranic verse states an immutable principle that applies to everyone, believers or non-believers. To put our country on the path of progress, it is essential that everyone actively participates rather than relying solely on the state. It is in this spirit that I wrote this book, with the hope that this contribution to the collective effort can have a positive impact on the development of our nation.",
      "This book is intended for anyone interested in the digital transformation of public administration in Algeria, as well as those wishing to deepen their knowledge of the issues and challenges related to e-government.",
      "It is intended for decision-makers, journalists, professionals in the public and private sectors, researchers, students, and anyone wanting to understand how information technologies can improve public services, governance, and citizen participation.",
      "During my tenure as president of GAAN (Algerian Group of Digital Actors 2020-2022), I was regularly asked by the media to give my opinion on the state of e-government in Algeria. However, I noticed that this subject was often misunderstood by the general public due to its technical nature. This book therefore aims to offer a comprehensive and accessible presentation of e-government in Algeria, explaining the concepts, benefits, and challenges encountered in the implementation of this system."
    ],
    description_ar: [
      "محتوى الغلاف الخلفي لإعطائك لمحة عن الأسباب التي دفعتني لتأليف هذا الكتاب والأهداف التي آمل تحقيقها من خلاله:",
      "\"إن الله لا يغير ما بقوم حتى يغيروا ما بأنفسهم\"، هذه الآية القرآنية تنص على مبدأ ثابت ينطبق على الجميع، مؤمنين كانوا أم غير مؤمنين. لوضع بلادنا على طريق التقدم، من الضروري أن يشارك الجميع بفعالية بدلاً من الاعتماد فقط على الدولة. بهذه الروح كتبت هذا الكتاب، على أمل أن يكون لهذه المساهمة في الجهد الجماعي تأثير إيجابي على تنمية أمتنا.",
      "هذا الكتاب موجه لكل المهتمين بالتحول الرقمي للإدارة العامة في الجزائر، وكذلك لأولئك الذين يرغبون في تعميق معرفتهم بالقضايا والتحديات المتعلقة بالحكومة الإلكترونية.",
      "إنه موجه لصناع القرار والصحفيين والمهنيين في القطاعين العام والخاص والباحثين والطلاب وأي شخص يرغب في فهم كيف يمكن لتقنيات المعلومات تحسين الخدمات العامة والحوكمة والمشاركة المدنية.",
      "خلال فترة ولايتي كرئيس لـ GAAN (المجموعة الجزائرية للفاعلين الرقميين 2020-2022)، طلب مني الإعلام بانتظام إبداء رأيي حول حالة الحكومة الإلكترونية في الجزائر. ومع ذلك، لاحظت أن هذا الموضوع كان غالباً ما يُساء فهمه من قبل عامة الناس بسبب طبيعته التقنية. لذلك يهدف هذا الكتاب إلى تقديم عرض شامل وسهل الفهم للحكومة الإلكترونية في الجزائر، موضحاً المفاهيم والفوائد والتحديات التي تمت مواجهتها في تنفيذ هذا النظام."
    ],
    excerpt: "Contenu de la quatrième de couverture pour vous donner un aperçu des raisons qui m'ont motivé à écrire ce livre ainsi qu",
    excerpt_en: "Back cover content to give you an overview of the reasons that motivated me to write this book and the goals I hope to achieve...",
    excerpt_ar: "محتوى الغلاف الخلفي لإعطائك لمحة عن الأسباب التي دفعتني لتأليف هذا الكتاب والأهداف التي آمل تحقيقها...",
    prix: 2000,
    is_free: false,
    apercu_url: "/uploads/apercudulivre_avec_4eme_de_couverture_0982bfedeb.pdf",
    fichier_url: null,
    lien_achat: "/livre/"
  },
  {
    slug: "e-gouvernement-algerie-enquete-nations-unies-2022",
    title: "L'e-Gouvernement en Algérie selon l'enquête des Nations Unies 2022",
    title_en: "e-Government in Algeria according to the 2022 United Nations Survey",
    title_ar: "الحكومة الإلكترونية في الجزائر حسب مسح الأمم المتحدة لعام 2022",
    meta_title: "L'e-Gouvernement en Algérie selon l'enquête des Nations Unies 2022",
    date_mise_en_ligne: "2022-10-15",
    image_couverture: "/uploads/754668_7e9ba9d0a7.jpg",
    description: [
      "Le département des affaires économiques et affaires sociales des Nations Unies vient de publier la 12ème édition de son rapport sur le développement des e-Gouvernements dans les 193 pays membres. C’est une enquête qui classe les pays selon l’Indice de Développement du E-Gouvernement EGDI et l’indice de participation électronique EPI.",
      "L’Algérie a gagné 8 places par rapport à 2020 avec un indice de développement du e-gouvernement EGDI égal à 0,5611 en se classant 112ème sur 193 pays et 9ème sur le continent africain. Le Danemark, la Finlande et la Corée du Sud sont en tête de liste. Les Emirats Arabes Unis sont l'un des pays les plus développés du monde arabe avec un EGDI de 0,901.",
      "L'indice de participation électronique (EPI) est une mesure complémentaire à l’EGDI, il classe les pays en fonction de leur utilisation des technologies de l'information et de la communication (TIC) pour engager les citoyens dans le processus démocratique. Même si l’Algérie a gagné 35 places entre 2020 et 2022, elle n'est toujours pas performante sur ce tableau, l'enquête la classe à la 148ème place sur 193 avec un score EPI de 0,2273, ce qui est très en dessous de la moyenne mondiale et même africaine.",
      "Le GAAN a réalisé pour vous une analyse détaillée de cette étude avec un focus sur l’Algérie."
    ],
    description_en: [
      "The United Nations Department of Economic and Social Affairs has just published the 12th edition of its report on e-Government development in the 193 member states. It is a survey that ranks countries according to the E-Government Development Index (EGDI) and the e-Participation Index (EPI).",
      "Algeria gained 8 places compared to 2020 with an EGDI of 0.5611, ranking 112th out of 193 countries and 9th on the African continent. Denmark, Finland, and South Korea top the list. The United Arab Emirates is one of the most developed countries in the Arab world with an EGDI of 0.901.",
      "The e-Participation Index (EPI) is a complementary measure to the EGDI, ranking countries based on their use of information and communication technologies (ICTs) to engage citizens in the democratic process. Although Algeria gained 35 places between 2020 and 2022, it still underperforms in this area; the survey ranks it 148th out of 193 with an EPI score of 0.2273, which is well below the global and even African average.",
      "GAAN has produced a detailed analysis of this study for you, with a focus on Algeria."
    ],
    description_ar: [
      "نشرت إدارة الشؤون الاقتصادية والاجتماعية التابعة للأمم المتحدة للتو النسخة الثانية عشرة من تقريرها حول تنمية الحكومة الإلكترونية في الدول الأعضاء الـ 193. إنه مسح يصنف البلدان وفقاً لمؤشر تنمية الحكومة الإلكترونية (EGDI) ومؤشر المشاركة الإلكترونية (EPI).",
      "كسبت الجزائر 8 مراتب مقارنة بعام 2020 بمؤشر تنمية الحكومة الإلكترونية EGDI يساوي 0.5611 محتلة المرتبة 112 من أصل 193 دولة والمرتبة 9 في القارة الأفريقية. وتتصدر الدنمارك وفنلندا وكوريا الجنوبية القائمة. وتعد الإمارات العربية المتحدة من أكثر الدول تطوراً في العالم العربي بـ EGDI يبلغ 0.901.",
      "مؤشر المشاركة الإلكترونية (EPI) هو مقياس مكمل لـ EGDI، يصنف الدول بناءً على استخدامها لتقنيات المعلومات والاتصالات (ICTs) لإشراك المواطنين في العملية الديمقراطية. على الرغم من أن الجزائر تقدمت 35 مركزاً بين عامي 2020 و 2022، إلا أنها لا تزال غير فعالة في هذا المجال، حيث يصنفها المسح في المرتبة 148 من أصل 193 بدرجة EPI تبلغ 0.2273، وهو أقل بكثير من المتوسط العالمي وحتى الأفريقي.",
      "لقد قام GAAN بإجراء تحليل مفصل لهذه الدراسة مع التركيز على الجزائر."
    ],
    excerpt: "Le département des affaires économiques et affaires sociales des Nations Unies vient de publier la 12ème édition de son ",
    excerpt_en: "The United Nations Department of Economic and Social Affairs has just published the 12th edition of its report on e-Government development...",
    excerpt_ar: "نشرت إدارة الشؤون الاقتصادية والاجتماعية التابعة للأمم المتحدة للتو النسخة الثانية عشرة من تقريرها حول تنمية الحكومة الإلكترونية...",
    prix: 0,
    is_free: true,
    apercu_url: null,
    fichier_url: "/uploads/Le_e_gouvernement_en_Algerie_enquete_de_l_onu_2022_1_39953dc1ec.pdf",
    lien_achat: null
  }
];

export function getPublicationBySlug(slug: string): Publication | undefined {
  return publications.find(publication => publication.slug === slug);
}
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated publications.ts safely.")
