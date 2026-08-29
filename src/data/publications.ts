export interface Publication {
  slug: string;
  title: string;
  meta_title?: string;
  date_mise_en_ligne: string;
  display_date?: string;
  image_couverture: string;
  description: string[];
  excerpt?: string;
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
    meta_title: "ABIX – Étude sectorielle : Analyse du secteur bancaire algérien 2025",
    date_mise_en_ligne: "2026-08-01",
    display_date: "Août 2026",
    image_couverture: "/uploads/abix-2026.jpg",
    description: [
      "L’édition 2026 d’ABIX propose une analyse approfondie des performances 2025 du secteur bancaire algérien, avec comparaisons entre banques, ratios financiers, classements, tendances sectorielles et perspectives."
    ],
    excerpt: "L’édition 2026 d’ABIX propose une analyse approfondie des performances 2025 du secteur bancaire algérien, avec comparaisons entre banques, ratios financiers, classements, tendances sectorielles et perspectives.",
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
    meta_title: "Étude sectorielle – Analyse du secteur bancaire algérien 2024",
    date_mise_en_ligne: "2025-08-18",
    image_couverture: "/uploads/Couverture_cc225420d6.png",
    description: [
      "Cette étude fournit une vision complète et structurée du secteur bancaire algérien, issue de l'exploitation et de l'analyse approfondie des données financières et réglementaires.",
      "Pour accéder à la présentation détaillée de l'étude sectorielle bancaire 2025, veuillez consulter notre page dédiée."
    ],
    excerpt: "Cette étude fournit une vision complète et structurée du secteur bancaire algérien, issue de l’exploitation et de l’anal",
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
    meta_title: "e-Gouvernement en Algérie : état des lieux, obstacles et solutions",
    date_mise_en_ligne: "2025-08-14",
    image_couverture: "/uploads/egov_livre_3223790e91.png",
    description: [
      "Contenu de la quatrième de couverture pour vous donner un aperçu des raisons qui m'ont motivé à écrire ce livre ainsi que des objectifs que j'espère atteindre à travers lui :",
      "\"Allah ne change rien en un peuple tant que celui-ci n'a pas changé ce qui est en lui\", ce verset coranique énonce un principe immuable qui s'applique à tous, croyants ou non croyants. Pour mettre notre pays sur la voie du progrès, il est essentiel que chacun s'implique activement plutôt que de compter uniquement sur l'État. C'est dans cet esprit que j'ai rédigé ce livre, avec l'espoir que cette contribution à l'effort collectif puisse avoir un impact positif sur le développement de notre nation.",
      "Ce livre est destiné à toutes les personnes intéressées par la transformation numérique de l’administration publique en Algérie, ainsi que celles désirant approfondir leur connaissance des enjeux et des défis liés à l’e-gouvernement.",
      "Il est destiné aux décideurs, aux journalistes, aux professionnels des secteurs public et privé, aux chercheurs, aux étudiants et à toute personne souhaitant comprendre comment les technologies de l’information peuvent améliorer les services publics, la gouvernance et la participation citoyenne.",
      "Durant mon mandat de président du GAAN (Groupement Algérien des Acteurs du Numérique 2020-2022), j’ai été régulièrement sollicité par les médias pour donner mon avis sur l’état de l’e-gouvernement en Algérie. Cependant, j’ai constaté que ce sujet était souvent mal compris par le grand public en raison de sa technicité. Ce livre vise donc à offrir une présentation exhaustive et accessible de l'e-governement en Algérie, en expliquant les concepts, les avantages et les défis rencontrés dans la mise en place de ce système.\""
    ],
    excerpt: "Contenu de la quatrième de couverture pour vous donner un aperçu des raisons qui m'ont motivé à écrire ce livre ainsi qu",
    prix: 2000,
    is_free: false,
    apercu_url: "/uploads/apercudulivre_avec_4eme_de_couverture_0982bfedeb.pdf",
    fichier_url: null,
    lien_achat: "/livre/"
  },
  {
    slug: "e-gouvernement-algerie-enquete-nations-unies-2022",
    title: "L'e-Gouvernement en Algérie selon l'enquête des Nations Unies 2022",
    meta_title: "L'e-Gouvernement en Algérie selon l'enquête des Nations Unies 2022",
    date_mise_en_ligne: "2022-10-15",
    image_couverture: "/uploads/754668_7e9ba9d0a7.jpg",
    description: [
      "Le département des affaires économiques et affaires sociales des Nations Unies vient de publier la 12ème édition de son rapport sur le développement des e-Gouvernements dans les 193 pays membres. C’est une enquête qui classe les pays selon l’Indice de Développement du E-Gouvernement EGDI et l’indice de participation électronique EPI.",
      "L’Algérie a gagné 8 places par rapport à 2020 avec un indice de développement du e-gouvernement EGDI égal à 0,5611 en se classant 112ème sur 193 pays et 9ème sur le continent africain. Le Danemark, la Finlande et la Corée du Sud sont en tête de liste. Les Emirats Arabes Unis sont l'un des pays les plus développés du monde arabe avec un EGDI de 0,901.",
      "L'indice de participation électronique (EPI) est une mesure complémentaire à l’EGDI, il classe les pays en fonction de leur utilisation des technologies de l'information et de la communication (TIC) pour engager les citoyens dans le processus démocratique. Même si l’Algérie a gagné 35 places entre 2020 et 2022, elle n'est toujours pas performante sur ce tableau, l'enquête la classe à la 148ème place sur 193 avec un score EPI de 0,2273, ce qui est très en dessous de la moyenne mondiale et même africaine.",
      "Le GAAN a réalisé pour vous une analyse détaillée de cette étude avec un focus sur l’Algérie."
    ],
    excerpt: "Le département des affaires économiques et affaires sociales des Nations Unies vient de publier la 12ème édition de son ",
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
