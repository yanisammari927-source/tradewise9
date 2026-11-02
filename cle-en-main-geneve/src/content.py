# -*- coding: utf-8 -*-
"""Contenus éditoriaux du site Clé en Main Genève.

Règles : aucun prix, aucun faux avis, aucune fausse statistique.
Chaque commune a un texte rédigé pour elle (pas de modèle avec le nom remplacé).
Le HTML simple (<a>, <strong>) est autorisé dans les textes.
"""

# --------------------------------------------------------------------------
# SERVICES
# --------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "ouverture-de-porte-geneve",
        "name": "Ouverture de porte",
        "short": "Porte claquée ou fermée à clé, clés à l'intérieur ou perdues : on ouvre en cherchant d'abord la méthode qui abîme le moins.",
        "img": "service-ouverture",
        "img_alt": "Illustration d'une porte rouge entrouverte et d'une clé",
        "title": "Ouverture de porte Genève – Serrurier 7j/7 | Clé en Main Genève",
        "desc": "Porte claquée ou clés perdues à Genève ? Ouverture de porte 7j/7, 24h/24. Devis gratuit par téléphone avant intervention : +41 79 942 95 44.",
        "h1": "Serrurier Genève : ouverture de porte claquée ou fermée à clé",
        "lead": "Vous êtes sur le palier, les clés sont de l'autre côté de la porte. Appelez-nous : on vous pose quelques questions, on vous donne un devis gratuit par téléphone, et on ne commence rien sans votre accord.",
        "sections": [
            ("Porte claquée ou porte fermée à clé : pas la même intervention", [
                "Une <strong>porte claquée</strong> n'est retenue que par le pêne demi-tour, celui qui s'enclenche tout seul quand la porte se ferme. Dans de nombreux cas, elle peut s'ouvrir avec des outils adaptés, sans toucher à la serrure.",
                "Une <strong>porte fermée à clé</strong> (verrou engagé, un ou plusieurs tours) est plus délicate. Selon le cylindre et la porte, il faut parfois neutraliser ou percer le cylindre puis le remplacer. Si c'est le cas, on vous le dit au téléphone, avant de se déplacer, et on vous le redit sur place avant de commencer.",
            ]),
            ("Ce qu'on vous demande au téléphone", [
                "<ul><li>L'adresse exacte, l'étage et le code de l'allée s'il y en a un ;</li><li>si la porte est claquée ou fermée à clé ;</li><li>le type de porte : standard, blindée, porte d'immeuble, porte de commerce ;</li><li>si une clé est restée dans la serrure côté intérieur.</li></ul>",
                "Avec ces informations, on vous annonce la méthode prévue, un délai réaliste et le devis. Gratuitement, et sans engagement.",
            ]),
            ("Danger à l'intérieur ? Appelez d'abord les secours", [
                "Si un enfant seul, une personne vulnérable ou un animal est enfermé, ou si une plaque de cuisson ou un bain est resté allumé, appelez immédiatement le <strong>118</strong> (pompiers) ou le <strong>144</strong> (urgences sanitaires). Les secours passent avant le serrurier.",
            ]),
            ("Une vérification simple, pour votre sécurité", [
                "Une fois la porte ouverte, nous vous demandons un justificatif montrant que vous habitez bien le logement (pièce d'identité avec l'adresse, bail, courrier à votre nom). C'est une précaution normale : elle protège aussi votre domicile contre quelqu'un qui se ferait passer pour vous.",
                "Si le cylindre a dû être remplacé, on peut poser le nouveau dans la foulée : voir notre page <a href=\"/changement-de-serrure-geneve/\">changement de serrure</a>.",
            ]),
        ],
        "faq": [
            ("Pouvez-vous ouvrir sans abîmer la porte ?", "Pour une porte simplement claquée, c'est souvent possible. Pour une porte verrouillée à clé ou une porte blindée, cela dépend du modèle. On vous explique la méthode prévue au téléphone, avant de venir."),
            ("Combien coûte une ouverture de porte ?", "Nous ne publions pas de tarifs : chaque porte et chaque situation sont différentes. Vous recevez un devis gratuit par téléphone avant l'intervention, et rien n'est fait sans votre accord."),
            ("Je suis locataire, dois-je prévenir ma régie ?", "Pour une simple ouverture, ce n'est en général pas nécessaire. Si le cylindre doit être changé et qu'il fait partie d'un système de clés de l'immeuble (clé de passe), mieux vaut informer la régie : on vous explique comment."),
        ],
    },
    {
        "slug": "changement-de-serrure-geneve",
        "name": "Changement de serrure",
        "short": "Clé perdue ou volée, emménagement, cylindre usé ou clé cassée dedans : remplacement du cylindre ou de la serrure complète.",
        "img": "service-serrure",
        "img_alt": "Illustration d'un cylindre de serrure et d'une clé rouge",
        "title": "Changement de serrure Genève – Serrurier 7j/7 | Clé en Main Genève",
        "desc": "Changement de cylindre ou de serrure à Genève après perte de clé, emménagement ou usure. Devis gratuit par téléphone avant intervention.",
        "h1": "Changement de serrure et de cylindre : serrurier Genève 7j/7",
        "lead": "Dans la plupart des cas, on ne change pas toute la serrure : on remplace le cylindre, la partie où entre la clé. On vous explique ce qui est nécessaire, et seulement ce qui est nécessaire.",
        "sections": [
            ("Quand faut-il changer le cylindre ?", [
                "<ul><li><strong>Clés perdues ou volées</strong>, surtout si elles étaient avec un document portant votre adresse ;</li><li><strong>emménagement</strong> : vous ne savez pas combien de doubles circulent ;</li><li><strong>clé cassée</strong> dans la serrure, ou clé qui force et qu'il faut « chercher » ;</li><li><strong>séparation, départ d'un colocataire ou d'un employé</strong> qui n'a pas rendu sa clé ;</li><li>après une <a href=\"/apres-effraction-geneve/\">tentative d'effraction</a>.</li></ul>",
            ]),
            ("Cylindre ou serrure complète ?", [
                "Le cylindre est la pièce amovible qui reçoit la clé. Si la serrure elle-même (le boîtier dans la porte) fonctionne bien, changer le cylindre suffit et c'est plus simple.",
                "On remplace la serrure complète quand le mécanisme est cassé, quand la porte se bloque malgré une clé neuve, ou quand vous voulez passer à une <a href=\"/securisation-blindage-geneve/\">serrure multipoints</a> plus résistante.",
            ]),
            ("Clés protégées et carte de propriété", [
                "Beaucoup de cylindres posés à Genève sont livrés avec une <strong>carte de propriété</strong> : sans elle, on ne peut pas faire refaire de clé. C'est une vraie protection contre les copies sauvages. Gardez cette carte à part, pas sur le trousseau.",
            ]),
            ("Immeubles avec clé de passe", [
                "Dans de nombreux immeubles, une même clé ouvre votre appartement, l'allée et la cave : c'est un système de clés organisé par la régie ou la copropriété (PPE). Remplacer un cylindre dans ce cas demande de respecter ce système. En dépannage, on peut poser un cylindre provisoire et vous indiquer la marche à suivre avec la régie.",
            ]),
        ],
        "faq": [
            ("Combien de temps prend un changement de cylindre ?", "Si le cylindre adapté est disponible, l'intervention elle-même est en général courte. Le délai complet vous est annoncé au téléphone avec le devis gratuit."),
            ("En tant que locataire, puis-je changer le cylindre ?", "Oui, en général, à condition de prévenir la régie et de conserver l'ancien cylindre pour le remettre en place à votre départ. En cas de doute, demandez-nous : on vous explique avant d'intervenir."),
            ("Combien de clés recevrai-je ?", "Cela dépend du cylindre choisi. On vous l'indique avec le devis, par téléphone, avant toute intervention."),
        ],
    },
    {
        "slug": "securisation-blindage-geneve",
        "name": "Sécurisation et blindage",
        "short": "Cylindre haute sécurité, protège-cylindre, serrure multipoints, blindage de porte : on renforce le point faible, pas plus.",
        "img": "service-blindage",
        "img_alt": "Illustration d'un bouclier jaune et rouge avec un trou de serrure",
        "title": "Blindage de porte Genève – Serrurier 7j/7 | Clé en Main Genève",
        "desc": "Sécurisation et blindage de porte à Genève : cylindre haute sécurité, serrure multipoints, protections anti-arrachement. Devis gratuit avant intervention.",
        "h1": "Sécurisation et blindage de porte : serrurier Genève",
        "lead": "Aucune porte n'est inviolable. L'objectif est de ralentir une tentative d'intrusion assez longtemps pour qu'elle soit abandonnée. On commence par regarder où est vraiment le point faible.",
        "sections": [
            ("On commence par un diagnostic", [
                "Au téléphone, puis si besoin sur place, on regarde la porte, le cadre, la serrure, le cylindre et les autres accès (porte de service, porte de cave, porte-fenêtre de plain-pied). Renforcer une porte d'entrée ne sert pas à grand-chose si la porte du garage s'ouvre d'un coup d'épaule.",
            ]),
            ("Les solutions possibles", [
                "<ul><li><strong>Cylindre haute sécurité</strong>, résistant au crochetage et au perçage, avec carte de propriété ;</li><li><strong>protège-cylindre</strong> (rosace) contre l'arrachement ;</li><li><strong>serrure multipoints</strong> qui verrouille la porte sur plusieurs points de la hauteur ;</li><li><strong>cornières et renforts</strong> côté paumelles et côté serrure, contre les pieds-de-biche ;</li><li><strong>blindage</strong> de la porte existante, ou remplacement par un bloc-porte certifié selon les classes de résistance (norme EN 1627).</li></ul>",
                "On vous propose ce qui répond à votre situation, pas le catalogue complet.",
            ]),
            ("Copropriété (PPE), régie et assurance", [
                "En immeuble, la face extérieure de la porte palière peut être soumise au règlement de copropriété ou à l'accord du bailleur. Renseignez-vous avant de lancer des travaux visibles. Côté assurance ménage, certains contrats tiennent compte du niveau de protection : demandez à votre assureur ce qu'il exige.",
            ]),
        ],
        "faq": [
            ("Une porte blindée est-elle inviolable ?", "Non, et méfiez-vous de qui vous le promet. Une bonne porte retarde l'intrusion et décourage la plupart des tentatives. C'est déjà beaucoup."),
            ("Faut-il changer toute la porte ?", "Pas forcément. Souvent, un bon cylindre, un protège-cylindre et des renforts suffisent à corriger le point faible. Le devis est gratuit et vous choisissez."),
            ("Pouvez-vous venir voir la porte avant le devis ?", "Oui. Pour un projet de sécurisation, on en parle d'abord au téléphone, puis on peut passer voir la porte. Rien n'est posé sans votre accord."),
        ],
    },
    {
        "slug": "apres-effraction-geneve",
        "name": "Après effraction",
        "short": "Serrure forcée, porte endommagée : mise en sécurité, remplacement du cylindre ou de la serrure, renforcement.",
        "img": "service-effraction",
        "img_alt": "Illustration d'une porte fissurée et barrée",
        "title": "Serrurier après effraction Genève – 7j/7 | Clé en Main Genève",
        "desc": "Cambriolage ou tentative d'effraction à Genève ? Mise en sécurité de la porte, remplacement de serrure, 7j/7. Devis gratuit par téléphone avant intervention.",
        "h1": "Serrurier Genève après effraction : remettre votre porte en sécurité",
        "lead": "Après un cambriolage ou une tentative, on n'a qu'une envie : pouvoir refermer chez soi. On vous aide à le faire vite, sans vous faire perdre ce dont la police et l'assurance auront besoin.",
        "sections": [
            ("Les premiers réflexes", [
                "<ol><li>N'entrez pas si vous pensez que quelqu'un est encore à l'intérieur : appelez le <strong>117</strong> (police).</li><li>Ne touchez à rien avant le passage de la police et prenez des photos de la porte, de la serrure et des dégâts.</li><li>Déposez plainte et gardez le numéro de dossier.</li><li>Prévenez votre assurance ménage (et votre régie si vous êtes locataire).</li></ol>",
            ]),
            ("Ce qu'on fait sur place", [
                "<ul><li><strong>Mise en sécurité</strong> : si la porte ne peut pas être réparée tout de suite, on la referme de façon provisoire pour que vous puissiez dormir tranquille ;</li><li><strong>remplacement du cylindre</strong> ou de la serrure forcés ;</li><li>remise en état de la gâche ou du cadre quand c'est possible ;</li><li>propositions de <a href=\"/securisation-blindage-geneve/\">renforcement</a> pour la suite, sans obligation.</li></ul>",
                "Vous recevez une facture détaillée, que vous pourrez transmettre à votre assurance.",
            ]),
        ],
        "faq": [
            ("Dois-je attendre la police avant de vous appeler ?", "Vous pouvez nous appeler tout de suite pour qu'on organise l'intervention. En revanche, on ne touche pas à la porte avant que la police ait fait ses constatations, si elle doit passer."),
            ("L'assurance va-t-elle rembourser ?", "Cela dépend de votre contrat. Gardez la facture détaillée et les photos, et contactez votre assureur rapidement."),
            ("Pouvez-vous fermer provisoirement une porte très abîmée ?", "Oui, c'est l'un des cas les plus fréquents après une effraction. On vous explique la solution provisoire et la réparation définitive, avec un devis gratuit pour chacune."),
        ],
    },
]

# Étapes d'intervention (communes aux pages services)
STEPS = [
    ("Vous appelez", "Un serrurier décroche, en français, en anglais ou en espagnol, et vous pose quelques questions pour comprendre la situation."),
    ("Devis gratuit par téléphone", "On vous annonce la méthode, le délai et le devis avant de se déplacer. Vous décidez, sans engagement."),
    ("Intervention", "Sur place, on vous redit ce qu'on va faire avant de commencer. S'il y a une surprise, on vous demande votre accord avant d'aller plus loin."),
]

# --------------------------------------------------------------------------
# FAQ ACCUEIL (balisée FAQPage)
# --------------------------------------------------------------------------
HOME_FAQ = [
    ("Intervenez-vous la nuit, le week-end et les jours fériés ?", "Oui. Clé en Main Genève répond 7 jours sur 7, 24 heures sur 24, y compris les week-ends et les jours fériés."),
    ("Combien coûte un serrurier à Genève ?", "Nous n'affichons pas de prix en ligne, car chaque porte et chaque situation sont différentes. Vous recevez un devis gratuit par téléphone avant l'intervention, et rien n'est fait sans votre accord."),
    ("Dans quelles communes intervenez-vous ?", "Dans le canton de Genève (Genève, Carouge, Vernier, Lancy, Meyrin, Onex, Thônex, Chêne-Bougeries, Plan-les-Ouates, Versoix, Le Grand-Saconnex, Bernex) et sur La Côte vaudoise (Nyon, Coppet, Gland). Pour une autre commune proche, appelez-nous."),
    ("Pouvez-vous ouvrir ma porte sans la casser ?", "Une porte simplement claquée peut souvent être ouverte sans dégât. Pour une porte fermée à clé ou blindée, cela dépend du modèle : on vous explique la méthode au téléphone, avant de venir."),
    ("Dans quelles langues pouvez-vous me répondre ?", "On vous répond en français, en anglais et en espagnol."),
    ("Que dois-je préparer avant votre arrivée ?", "L'adresse exacte, l'étage, le code d'accès de l'immeuble si besoin, et un justificatif de domicile (pièce d'identité, bail ou courrier) que nous vous demanderons après l'ouverture."),
]

# --------------------------------------------------------------------------
# COMMUNES — texte rédigé individuellement pour chaque commune
# --------------------------------------------------------------------------
COMMUNES = [
    {
        "slug": "serrurier-geneve", "name": "Genève", "label": "Genève (Ville)", "canton": "GE",
        "title": "Serrurier Genève Ville – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier en Ville de Genève : Pâquis, Eaux-Vives, Plainpalais, Servette, Champel… Ouverture de porte et changement de serrure 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Genève : dépannage 7j/7 dans tous les quartiers de la Ville",
        "lead": "Des Pâquis à Champel, de Saint-Jean aux Eaux-Vives : un serrurier qui connaît les immeubles genevois et vous donne un devis gratuit par téléphone avant de venir.",
        "intro": [
            "La Ville de Genève, ce sont d'abord des immeubles anciens : façades du XIXᵉ siècle aux Pâquis et aux Eaux-Vives, allées à digicode à Plainpalais, portes palières en bois massif dans la Vieille-Ville. Quand une porte se claque ou qu'une clé reste coincée, la difficulté vient souvent de là : des serrures d'origine, refaites plusieurs fois au fil des locataires, et des cylindres intégrés au système de clés de la régie.",
            "Nous intervenons dans tous les quartiers : Pâquis, Servette, Saint-Jean, Charmilles, Jonction, Plainpalais, Champel, Eaux-Vives, Vieille-Ville, Petit-Saconnex. Que vous ayez cherché « serrurier Genève » ou « serrurier geneve » sur votre téléphone, devant votre porte, vous êtes au bon endroit : appelez, on vous répond.",
        ],
        "situations": [
            ("Porte palière claquée, clés à l'intérieur", "Le cas le plus courant en ville. Une porte seulement claquée s'ouvre souvent sans toucher à la serrure ; on vous dit au téléphone si c'est probablement votre cas."),
            ("Clé cassée dans un vieux cylindre", "Dans les immeubles anciens, les cylindres ont parfois des décennies de service. On extrait le morceau de clé, puis on vérifie si le cylindre peut encore servir ou s'il vaut mieux le remplacer."),
            ("Cylindre lié à la clé de passe de la régie", "Beaucoup d'immeubles genevois fonctionnent avec une clé qui ouvre à la fois l'appartement, l'allée et la cave. En dépannage, on peut poser un cylindre provisoire et vous expliquer comment commander le cylindre définitif auprès de la régie."),
            ("Arcades et commerces", "Serrure de porte vitrée qui refuse de s'ouvrir avant l'ouverture du magasin, clé d'employé non rendue : on intervient aussi pour les commerces, tôt le matin ou le dimanche."),
        ],
        "tip": "Se garer prend parfois du temps en ville, surtout dans la Vieille-Ville et aux Pâquis. Donnez-nous dès l'appel le code de l'allée, l'étage et le nom sur la porte : on évite ainsi d'attendre en bas de l'immeuble.",
        "faq": [
            ("Venez-vous aussi dans la Vieille-Ville, où l'accès en voiture est limité ?", "Oui. On se gare au plus près et on termine à pied avec l'outillage. Ce temps d'accès est pris en compte dans le délai annoncé au téléphone."),
            ("Mon immeuble a une clé de passe gérée par la régie : pouvez-vous changer mon cylindre ?", "On regarde d'abord le type de cylindre. Si le cylindre définitif doit être commandé via la régie, on peut poser un cylindre provisoire pour que vous puissiez fermer chez vous en attendant."),
        ],
        "near": ["serrurier-carouge", "serrurier-lancy", "serrurier-grand-saconnex", "serrurier-chene-bougeries"],
    },
    {
        "slug": "serrurier-carouge", "name": "Carouge", "label": "Carouge", "canton": "GE",
        "title": "Serrurier Carouge – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Carouge : portes anciennes du Vieux-Carouge, ateliers, commerces et immeubles. Ouverture de porte 7j/7, devis gratuit par téléphone avant intervention.",
        "h1": "Serrurier Carouge : portes anciennes, ateliers et appartements",
        "lead": "Du Vieux-Carouge aux immeubles de la Fontenette : ouverture de porte, réparation et changement de serrure, avec un devis gratuit par téléphone.",
        "intro": [
            "Carouge a gardé son plan de ville sarde : rues tracées à angle droit, maisons basses, cours intérieures et ateliers au rez-de-chaussée. Beaucoup de portes sur rue sont anciennes, en bois, avec des serrures qui ont parfois plus d'âge que leurs occupants. On aime ces portes, et on préfère les réparer quand c'est possible plutôt que tout remplacer.",
            "Hors du centre historique, du côté de la Fontenette, de Pinchat ou des tours de Carouge, on retrouve des immeubles plus récents avec des portes palières classiques. Deux mondes différents, et deux manières de travailler : on vous demande au téléphone dans quel type de bâtiment vous vous trouvez.",
        ],
        "situations": [
            ("Vieille serrure qui ne tourne plus", "Les serrures anciennes en applique se grippent avec le temps. Souvent, un nettoyage ou le remplacement d'une pièce suffit. Si un remplacement est nécessaire, on cherche un modèle qui respecte l'allure de la porte."),
            ("Atelier ou boutique bloqué le matin", "Artisans et commerçants ne peuvent pas attendre que la matinée passe. On intervient tôt, avant l'ouverture, 7 jours sur 7."),
            ("Porte de cour ou de passage", "Les portes qui donnent sur les cours intérieures sont partagées entre plusieurs voisins. Changer leur cylindre implique de refaire des clés pour tout le monde : on vous aide à organiser ça avec la régie ou le propriétaire."),
        ],
        "tip": "Le Vieux-Carouge est un site protégé : une modification visible de la façade (nouvelle porte, nouvelle ferrure apparente) peut nécessiter une autorisation. Pour un simple changement de cylindre, aucun souci.",
        "faq": [
            ("Pouvez-vous conserver ma serrure ancienne ?", "Souvent, oui. On regarde si le mécanisme peut être réparé ; si ce n'est pas raisonnable, on vous le dit franchement et on vous propose une alternative, avec un devis gratuit."),
            ("Intervenez-vous pour les commerces carougeois avant l'ouverture ?", "Oui, 7 jours sur 7 et dès tôt le matin. Appelez-nous dès que vous constatez le problème."),
        ],
        "near": ["serrurier-geneve", "serrurier-lancy", "serrurier-plan-les-ouates", "serrurier-thonex"],
    },
    {
        "slug": "serrurier-vernier", "name": "Vernier", "label": "Vernier", "canton": "GE",
        "title": "Serrurier Vernier – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Vernier : Le Lignon, Les Avanchets, Châtelaine, Aïre, Vernier-Village et zones d'activités. Dépannage 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Vernier : du Lignon à Vernier-Village, 7j/7",
        "lead": "Grands ensembles, maisons de village et entreprises : un serrurier pour tout Vernier, avec un devis gratuit par téléphone avant intervention.",
        "intro": [
            "Vernier rassemble des quartiers qui ne se ressemblent pas : la cité du Lignon et ses immeubles qui s'étirent le long du Rhône, les Avanchets, Châtelaine, Aïre, mais aussi Vernier-Village et ses maisons. Sans oublier les zones d'activités, où se trouvent bureaux, ateliers et entrepôts.",
            "Dans les grands immeubles, une porte claquée se règle d'autant plus vite qu'on trouve directement la bonne entrée. Dans les entreprises, les demandes concernent plutôt des portes de locaux techniques, des portes de service ou des cylindres à remplacer après le départ d'un collaborateur.",
        ],
        "situations": [
            ("Porte claquée au Lignon ou aux Avanchets", "Appartement, local à poussettes, cave : on intervient sur les portes privatives. Pour la porte d'entrée de l'immeuble, c'est la régie ou le concierge qui nous mandate."),
            ("Clé de collaborateur non rendue", "Un employé part avec sa clé ? On remplace les cylindres concernés et, si vous avez un système de clés hiérarchisé, on vous explique comment le garder cohérent."),
            ("Maison à Vernier-Village", "Porte d'entrée, porte de garage, porte de jardin : les accès secondaires sont souvent les moins protégés. On peut les regarder avec vous lors d'une intervention."),
        ],
        "tip": "Le Lignon compte de très nombreuses entrées. Donnez-nous le numéro exact de l'adresse (et pas seulement « le Lignon ») : on trouve votre allée du premier coup.",
        "faq": [
            ("Intervenez-vous dans les zones d'activités de Vernier ?", "Oui, pour les entreprises comme pour les particuliers, y compris en dehors des heures de bureau, pour ne pas perturber votre activité."),
            ("Je suis locataire : qui paie l'ouverture de porte ?", "En général, une ouverture après un oubli de clé est à la charge de l'occupant, alors qu'une serrure défectueuse peut relever du bailleur. En cas de doute, vérifiez avec votre régie ; le devis, lui, est gratuit."),
        ],
        "near": ["serrurier-meyrin", "serrurier-geneve", "serrurier-lancy", "serrurier-onex"],
    },
    {
        "slug": "serrurier-lancy", "name": "Lancy", "label": "Lancy", "canton": "GE",
        "title": "Serrurier Lancy – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Lancy : Petit-Lancy, Grand-Lancy, Les Palettes, Pont-Rouge, La Chapelle. Ouverture de porte, cylindres, boîtes aux lettres. Devis gratuit par téléphone.",
        "h1": "Serrurier Lancy : Petit-Lancy, Grand-Lancy et Pont-Rouge",
        "lead": "Villas, immeubles récents et quartiers en plein développement : on intervient partout à Lancy, 7 jours sur 7.",
        "intro": [
            "Lancy s'étend du Petit-Lancy, avec ses villas et ses chemins résidentiels, au Grand-Lancy et aux Palettes, plus denses. Autour de la gare de Lancy-Pont-Rouge et du côté de La Chapelle, de nombreux immeubles neufs sont sortis de terre ces dernières années.",
            "Cette diversité se retrouve dans les serrures : cylindres modernes avec carte de propriété dans les constructions récentes, mécanismes plus anciens dans les villas. On adapte la méthode à ce qu'on trouve, et on vous l'explique avant de commencer.",
        ],
        "situations": [
            ("Immeuble neuf : toutes les clés perdues", "Dans les bâtiments récents, les clés sont protégées : impossible d'en refaire sans la carte de propriété. Si tout est perdu, on ouvre la porte et on pose un nouveau cylindre."),
            ("Villa : serrure multipoints bloquée", "La clé tourne, mais la porte reste coincée : c'est souvent le mécanisme multipoints qui force. On le débloque, on le règle ou on le remplace selon son état."),
            ("Clé de boîte aux lettres perdue", "Une petite serrure, mais un vrai problème quand le courrier s'accumule. On remplace la serrure de boîte aux lettres par un modèle compatible avec la batterie de l'immeuble."),
        ],
        "tip": "Vous habitez un immeuble récent ? Retrouvez la carte de propriété de vos clés, souvent remise à l'entrée dans le logement, et rangez-la ailleurs que sur le trousseau. Elle vous fera gagner beaucoup de temps le jour où une clé manque.",
        "faq": [
            ("J'ai perdu la carte de propriété de mes clés : que faire ?", "Contactez d'abord votre régie ou votre propriétaire : la carte est parfois enregistrée chez eux. Sinon, il faut en général remplacer le cylindre pour obtenir de nouvelles clés protégées."),
            ("Changez-vous les serrures de boîtes aux lettres ?", "Oui, dans la plupart des cas. Dans un immeuble avec des boîtes uniformes, on choisit un modèle compatible ; un accord de la régie peut être demandé."),
        ],
        "near": ["serrurier-onex", "serrurier-carouge", "serrurier-plan-les-ouates", "serrurier-geneve"],
    },
    {
        "slug": "serrurier-meyrin", "name": "Meyrin", "label": "Meyrin", "canton": "GE",
        "title": "Serrurier Meyrin – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Meyrin : cité, Meyrin-Village, écoquartier des Vergers et zone d'activités. Dépannage 24h/24, on répond en FR, EN, ES. Devis gratuit par téléphone.",
        "h1": "Serrurier Meyrin : cité, village et Vergers, 24h/24",
        "lead": "Horaires décalés, retour tardif, locaux d'entreprise : à Meyrin, on répond à toute heure, en français, en anglais ou en espagnol.",
        "intro": [
            "Meyrin a été la première cité satellite de Suisse : dans les années 1960, des immeubles y ont été construits d'un seul élan pour accueillir des milliers d'habitants. Aujourd'hui, la commune réunit cette cité, le village ancien, le nouvel écoquartier des Vergers et une grande zone d'activités, avec le CERN et une partie de l'aéroport sur son territoire.",
            "Beaucoup de Meyrinois travaillent en horaires décalés ou viennent de l'étranger. C'est pour ça qu'on décroche à toute heure, et qu'on vous répond en français, en anglais ou en espagnol.",
        ],
        "situations": [
            ("Retour de nuit, clés restées au travail", "Fin de service à 2 h du matin, clés oubliées dans le casier : ça arrive. On intervient la nuit comme le jour, avec le même principe de devis gratuit par téléphone."),
            ("Logements récents des Vergers", "Les portes neuves sont souvent équipées de serrures multipoints et de cylindres protégés. Si votre immeuble utilise un contrôle d'accès électronique géré par la régie, on vous dit honnêtement au téléphone ce qui relève de nous ou non."),
            ("Locaux d'entreprise en zone d'activités", "Portes de bureaux, d'ateliers, de locaux techniques : ouverture, remplacement de cylindres, renforcement."),
        ],
        "tip": "Pour un site à accès contrôlé (entreprise, bâtiment surveillé), prévenez la réception ou le service de sécurité de notre venue : on évite ainsi d'attendre à l'entrée.",
        "faq": [
            ("Do you speak English?", "Yes. We answer in French, English and Spanish, day and night. The quote is given for free over the phone, before we come."),
            ("Pouvez-vous ouvrir la porte d'entrée de mon immeuble ?", "La porte commune d'un immeuble dépend de la régie ou du concierge : on intervient à leur demande. Pour votre porte d'appartement, appelez-nous directement."),
        ],
        "near": ["serrurier-vernier", "serrurier-grand-saconnex", "serrurier-geneve"],
    },
    {
        "slug": "serrurier-onex", "name": "Onex", "label": "Onex", "canton": "GE",
        "title": "Serrurier Onex – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Onex : appartements de la cité, Onex-Village, caves et cylindres usés. Ouverture de porte 7j/7, devis gratuit par téléphone avant intervention.",
        "h1": "Serrurier Onex : appartements, caves et cylindres fatigués",
        "lead": "Porte claquée, clé qui force, cave à sécuriser : on intervient dans toute la commune d'Onex, avec un devis gratuit par téléphone.",
        "intro": [
            "Onex a beaucoup changé en soixante ans. Le village d'origine a été rejoint dans les années 1960 par la cité nouvelle et ses grands immeubles ; entre les deux, de petits immeubles, des villas et, en contrebas, les bords du Rhône.",
            "Ici, la plupart des appels concernent des appartements : portes claquées en sortant les poubelles, clés perdues sur le chemin de l'école, cylindres usés après des décennies d'allers-retours.",
        ],
        "situations": [
            ("Un enfant rentre de l'école et la porte est fermée", "Si l'enfant est dehors, en sécurité, on vous aide à organiser l'ouverture au plus vite. Si un enfant est seul à l'intérieur et en danger, appelez d'abord le 118 ou le 144."),
            ("Cylindre d'origine qui accroche", "Une clé qu'il faut « chercher » dans la serrure annonce un cylindre usé. Le changer avant qu'une clé ne casse dedans évite une intervention en urgence."),
            ("Porte de cave peu solide", "Les caves sont souvent fermées par une simple porte en bois ou en treillis. Un cylindre correct ou un renfort simple change déjà beaucoup."),
        ],
        "tip": "Ne lubrifiez pas un cylindre avec de l'huile de cuisine ou de la graisse épaisse : elle attire la poussière et finit par bloquer le mécanisme. Un spray adapté aux serrures, ou un appel, c'est mieux.",
        "faq": [
            ("Ma clé tourne mal : faut-il changer toute la serrure ?", "Rarement. Dans la plupart des cas, seul le cylindre est usé. On vous le confirme au téléphone avec le devis gratuit."),
            ("Pouvez-vous sécuriser ma cave ?", "Oui : cylindre, ferrure, renfort de la porte selon ce qui existe. Si la porte appartient à l'immeuble, un accord de la régie peut être nécessaire."),
        ],
        "near": ["serrurier-lancy", "serrurier-bernex", "serrurier-vernier"],
    },
    {
        "slug": "serrurier-thonex", "name": "Thônex", "label": "Thônex", "canton": "GE",
        "title": "Serrurier Thônex – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Thônex et dans les Trois-Chêne : villas, immeubles, quartier de Belle-Terre. Ouverture, réglage et changement de serrure. Devis gratuit par téléphone.",
        "h1": "Serrurier Thônex : villas, immeubles et Belle-Terre",
        "lead": "À la frontière, au cœur des Trois-Chêne : ouverture de porte, réglage et changement de cylindre, 7 jours sur 7.",
        "intro": [
            "Thônex touche la frontière française au niveau de Moillesulaz et forme, avec Chêne-Bourg et Chêne-Bougeries, ce qu'on appelle les Trois-Chêne. La commune mêle villas, petits immeubles et le nouveau quartier de Belle-Terre, construit ces dernières années.",
            "Les journées commencent souvent tôt ici. Une serrure qui bloque à 6 h du matin, au moment de partir travailler, c'est exactement le genre d'appel auquel on répond.",
        ],
        "situations": [
            ("Clés perdues avec un document d'adresse", "Portefeuille, sac ou trousseau avec un badge nominatif : si quelqu'un peut relier vos clés à votre adresse, changez le cylindre sans attendre."),
            ("Porte neuve qui frotte ou ferme mal", "Dans les constructions récentes, une porte peut travailler les premiers mois. Souvent, un réglage de la gâche suffit. Si le bâtiment est encore sous garantie, contactez d'abord le constructeur ou la régie."),
            ("Villa : porte-fenêtre et accès arrière", "Les cambrioleurs passent rarement par la porte d'entrée bien en vue. On peut regarder avec vous les accès côté jardin."),
        ],
        "tip": "Une porte qui ne se ferme qu'en la poussant fort finit par user la serrure. Faites-la régler dès les premiers signes : c'est plus rapide qu'un remplacement.",
        "faq": [
            ("La porte de mon appartement neuf ferme mal : est-ce grave ?", "Généralement non : c'est souvent une question de réglage. Si le logement est encore sous garantie, passez d'abord par la régie ou le constructeur ; sinon, on s'en occupe."),
            ("Intervenez-vous de l'autre côté de la frontière ?", "Notre zone d'intervention est la Suisse : canton de Genève et La Côte vaudoise. Pour un cas particulier, appelez-nous et on vous répond franchement."),
        ],
        "near": ["serrurier-chene-bougeries", "serrurier-geneve", "serrurier-carouge"],
    },
    {
        "slug": "serrurier-chene-bougeries", "name": "Chêne-Bougeries", "label": "Chêne-Bougeries", "canton": "GE",
        "title": "Serrurier Chêne-Bougeries – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Chêne-Bougeries et Conches : sécurisation de villa, portes de service, serrures multipoints, après effraction. Devis gratuit par téléphone.",
        "h1": "Serrurier Chêne-Bougeries : sécuriser une villa, accès par accès",
        "lead": "Grandes maisons, plusieurs entrées, jardins : à Chêne-Bougeries, la sécurité se pense accès par accès. On vous aide à le faire, sans surenchère.",
        "intro": [
            "Chêne-Bougeries est l'une des communes les plus résidentielles du canton : grandes propriétés à Conches, villas avec jardin, chemins calmes, et quelques immeubles vers Grange-Canal et le long de la route de Chêne.",
            "Ici, la demande n'est pas toujours une urgence. Souvent, c'est un propriétaire qui veut savoir si sa porte d'entrée, sa porte de service ou celle du garage tiendraient face à une tentative d'intrusion, et ce qu'il serait raisonnable d'améliorer.",
        ],
        "situations": [
            ("Diagnostic de sécurité d'une maison", "On fait le tour des accès avec vous : porte principale, porte de service, garage, buanderie, porte-fenêtre. Puis on vous dit ce qui mérite d'être renforcé, et ce qui va déjà bien."),
            ("Porte de service ou de garage", "Moins visibles, souvent moins bien équipées : ce sont fréquemment elles qui posent problème. Un bon cylindre et des renforts suffisent parfois."),
            ("Retour de vacances, serrure forcée", "Si vous découvrez une effraction, appelez d'abord la police (117). Ensuite, on remet la porte en sécurité : voir notre page après effraction."),
        ],
        "tip": "Une maison est aussi solide que son accès le plus faible. Avant de blinder la porte d'entrée, vérifiez la porte du garage ou de la buanderie : c'est souvent là qu'on gagne le plus en sécurité.",
        "faq": [
            ("Pouvez-vous venir voir avant de proposer quelque chose ?", "Oui. On en parle d'abord au téléphone, puis on peut passer voir les portes. Le devis est gratuit et rien n'est posé sans votre accord."),
            ("Travaillez-vous avec mon installateur d'alarme ?", "Nous nous occupons des portes, serrures et cylindres. L'alarme reste l'affaire de votre installateur, mais on peut tout à fait coordonner nos interventions."),
        ],
        "near": ["serrurier-thonex", "serrurier-geneve", "serrurier-carouge"],
    },
    {
        "slug": "serrurier-plan-les-ouates", "name": "Plan-les-Ouates", "label": "Plan-les-Ouates", "canton": "GE",
        "title": "Serrurier Plan-les-Ouates – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Plan-les-Ouates : entreprises de la ZIPLO, Saconnex-d'Arve, Arare, La Chapelle-Les Sciers. Dépannage 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Plan-les-Ouates : entreprises de la ZIPLO et logements",
        "lead": "Locaux professionnels et quartiers résidentiels : on intervient à Plan-les-Ouates 7 jours sur 7, y compris en dehors des heures de bureau.",
        "intro": [
            "Plan-les-Ouates est connue pour sa zone industrielle, la ZIPLO, où se sont installées de nombreuses entreprises, notamment dans l'horlogerie. Côté logements, la commune compte le village, Saconnex-d'Arve, Arare et le quartier de La Chapelle-Les Sciers, partagé avec Lancy.",
            "Deux publics, deux rythmes : les entreprises veulent une intervention qui ne perturbe pas la production, les familles veulent pouvoir rentrer chez elles. On s'organise en conséquence, le devis restant toujours gratuit et donné par téléphone.",
        ],
        "situations": [
            ("Local d'archives ou de stockage à protéger", "Pièces de valeur, documents confidentiels : un cylindre haute sécurité avec carte de propriété limite qui peut faire des copies de clés."),
            ("Clé qui tourne dans le vide", "Si la clé tourne sans rien entraîner, la pièce qui actionne la serrure à l'intérieur du cylindre est probablement cassée. L'ouverture demande alors en général de remplacer le cylindre ; on vous l'explique avant."),
            ("Portail ou porte de jardin au village", "Serrures exposées à la pluie et au gel, qui finissent par gripper. On répare ou on remplace par un modèle adapté à l'extérieur."),
        ],
        "tip": "Pour une entreprise, préparez la liste des portes concernées et, si vous en avez un, le plan de vos clés (qui ouvre quoi). Le devis n'en sera que plus précis.",
        "faq": [
            ("Pouvez-vous intervenir en dehors des heures de bureau ?", "Oui, 7 jours sur 7, tôt le matin, le soir ou le week-end, pour ne pas bloquer votre activité."),
            ("Ma clé tourne dans le vide, que se passe-t-il ?", "Le plus souvent, une pièce interne du cylindre est cassée. Il faut alors ouvrir puis remplacer le cylindre. Ne forcez pas : vous pourriez abîmer la serrure elle-même."),
        ],
        "near": ["serrurier-lancy", "serrurier-carouge", "serrurier-bernex", "serrurier-onex"],
    },
    {
        "slug": "serrurier-versoix", "name": "Versoix", "label": "Versoix", "canton": "GE",
        "title": "Serrurier Versoix – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Versoix : bourg, bord du lac, villas et immeubles. Ouverture de porte, réglage, changement de cylindre 7j/7. Délai réaliste et devis gratuit par téléphone.",
        "h1": "Serrurier Versoix : au bord du lac, un délai annoncé honnêtement",
        "lead": "Versoix est au nord du canton : on vous annonce au téléphone un délai réaliste, avec un devis gratuit, plutôt qu'une promesse qu'on ne pourrait pas tenir.",
        "intro": [
            "Au nord du canton, Versoix borde le Léman et touche le canton de Vaud. On y trouve le bourg historique, le port, des quartiers de villas qui montent vers les bois, et des immeubles autour de la gare.",
            "La commune est plus éloignée du centre-ville que d'autres. Plutôt que de vous promettre un temps d'arrivée impossible, on vous indique au téléphone un délai qui tient compte de l'heure et de l'endroit où se trouve le serrurier disponible.",
        ],
        "situations": [
            ("Porte en bois qui gonfle avec l'humidité", "Près du lac, les portes en bois travaillent avec les saisons. La serrure force, la clé devient dure : souvent, un ajustement de la gâche règle le problème avant la casse."),
            ("Maison secondaire ou logement peu occupé", "Un logement souvent vide mérite une attention particulière : cylindre de qualité, protège-cylindre, renfort des accès secondaires."),
            ("Garage et portes annexes", "Clé perdue d'une porte de garage ou d'un local de rangement : on remplace le cylindre, et on peut le faire fonctionner avec la même clé que d'autres portes si vous le souhaitez."),
        ],
        "tip": "Si votre porte en bois devient dure à fermer en hiver ou après de fortes pluies, ne forcez pas sur la clé : faites ajuster la porte avant que la serrure ne casse.",
        "faq": [
            ("Combien de temps pour venir à Versoix ?", "Cela dépend de l'heure et de l'endroit où se trouve le serrurier disponible. On vous annonce un délai réaliste au téléphone, avec le devis gratuit."),
            ("Pouvez-vous ajuster une porte qui frotte ?", "Oui, quand le problème vient de la gâche ou des réglages de la porte. Si la porte elle-même est déformée, on vous le dit et on vous oriente."),
        ],
        "near": ["serrurier-grand-saconnex", "serrurier-coppet", "serrurier-geneve"],
    },
    {
        "slug": "serrurier-grand-saconnex", "name": "Grand-Saconnex", "label": "Le Grand-Saconnex", "canton": "GE",
        "title": "Serrurier Grand-Saconnex – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier au Grand-Saconnex, près de l'aéroport et des organisations internationales. On répond en FR, EN, ES. Dépannage 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Grand-Saconnex : on vous répond en français, English, español",
        "lead": "Près de l'aéroport, de Palexpo et des organisations internationales : un serrurier qui vous explique tout clairement, dans votre langue.",
        "intro": [
            "Entre l'aéroport, Palexpo et le quartier des organisations internationales, Le Grand-Saconnex accueille beaucoup d'habitants venus du monde entier, souvent pour quelques années. On y trouve aussi le vieux village, des villas et des immeubles récents.",
            "Quand on ne connaît pas encore les usages locaux (régie, carte de propriété des clés, clé de passe), une serrure bloquée peut vite devenir compliquée. On vous répond en français, en anglais ou en espagnol, et on vous explique chaque étape avant d'intervenir.",
        ],
        "situations": [
            ("Nouveaux arrivants : faut-il changer le cylindre ?", "Vous ne savez pas combien de clés de votre logement circulent ? Un changement de cylindre vous assure d'être les seuls à pouvoir ouvrir. Pensez à en informer la régie."),
            ("Logement meublé ou de fonction", "Si le logement appartient à votre employeur ou à une agence, leur accord est nécessaire avant de changer le cylindre. On peut ouvrir la porte, puis vous laisser le temps d'obtenir cet accord."),
            ("Retour de voyage tard, clés introuvables", "Vol de nuit, valise ouverte, pas de clé : on intervient à toute heure, 7 jours sur 7."),
        ],
        "tip": "Vous venez d'emménager ? Demandez à votre régie combien de clés existent pour votre logement et notez-le. Si personne ne le sait, changer le cylindre est une précaution raisonnable.",
        "faq": [
            ("Can you help me in English?", "Yes. We answer in French, English and Spanish, 24/7. We explain the method and give you a free quote over the phone before coming."),
            ("Mon logement est fourni par mon employeur : puis-je changer la serrure ?", "Il faut l'accord du propriétaire ou de l'organisme qui gère le logement. En attendant, on peut ouvrir la porte et vous conseiller."),
        ],
        "near": ["serrurier-geneve", "serrurier-meyrin", "serrurier-vernier", "serrurier-versoix"],
    },
    {
        "slug": "serrurier-bernex", "name": "Bernex", "label": "Bernex", "canton": "GE",
        "title": "Serrurier Bernex – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Bernex, Lully, Sézenove, Loëx : maisons anciennes, dépendances, caves et nouveaux quartiers. Dépannage 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Bernex : village, hameaux et nouveaux quartiers",
        "lead": "Maisons de campagne, granges, caves et immeubles neufs : à Bernex, on intervient jusque dans les hameaux, 7 jours sur 7.",
        "intro": [
            "Bernex, c'est encore la campagne genevoise : vignes, champs et hameaux comme Lully, Sézenove ou Loëx. Mais la commune grandit vite, avec de nouveaux quartiers d'habitation autour du terminus du tram.",
            "Les demandes y sont variées : vieilles portes de ferme rénovée, dépendances fermées par des serrures d'un autre âge, appartements neufs avec cylindres protégés. On s'adapte à ce qu'on trouve.",
        ],
        "situations": [
            ("Maison ancienne ou ferme rénovée", "Portes épaisses, serrures anciennes, parfois plusieurs verrous ajoutés au fil du temps. On remet de l'ordre sans dénaturer la porte."),
            ("Granges, caves et dépendances", "Locaux de rangement, cave à vin, atelier : un cylindre fiable ou un renfort simple évite bien des mauvaises surprises."),
            ("Appartement dans un nouveau quartier", "Porte palière claquée, cylindre récent avec carte de propriété : même service qu'en ville, avec un devis gratuit par téléphone."),
        ],
        "tip": "À la campagne, donnez-nous un repère en plus de l'adresse : nom du chemin, couleur du portail, bâtiment voisin. Les adresses des hameaux sont parfois difficiles à trouver de nuit.",
        "faq": [
            ("Venez-vous jusque dans les hameaux ?", "Oui : Lully, Sézenove, Loëx et l'ensemble de la commune. Le délai vous est annoncé au téléphone."),
            ("Pouvez-vous sécuriser une cave à vin ou un local de stockage ?", "Oui : cylindre de qualité, protège-cylindre, renforts de porte selon le local. On vous propose le nécessaire, sans plus."),
        ],
        "near": ["serrurier-onex", "serrurier-plan-les-ouates", "serrurier-lancy", "serrurier-vernier"],
    },
    {
        "slug": "serrurier-nyon", "name": "Nyon", "label": "Nyon", "canton": "VD",
        "title": "Serrurier Nyon – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Nyon (VD) : vieille ville, quartiers résidentiels, entreprises. Ouverture de porte et changement de serrure 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Nyon : vieille ville, pendulaires et entreprises",
        "lead": "Clé en Main Genève intervient aussi à Nyon et sur La Côte : délai et devis annoncés gratuitement au téléphone, avant de prendre la route.",
        "intro": [
            "Ville vaudoise au bord du Léman, Nyon mêle une vieille ville perchée autour de son château, des quartiers résidentiels qui s'étendent vers le Jura et de nombreuses entreprises et organisations, dont le siège de l'UEFA.",
            "Beaucoup de Nyonnais travaillent à Genève et font l'aller-retour chaque jour. Nous intervenons des deux côtés : le délai annoncé au téléphone tient compte de l'heure et de la circulation entre Genève et Nyon.",
        ],
        "situations": [
            ("Vieille ville : portes anciennes, escaliers étroits", "Immeubles anciens, portes en bois, serrures d'époque : on travaille avec soin, et on vous dit si une réparation est possible avant de proposer un remplacement."),
            ("Pendulaire : les clés sont restées au bureau", "Vous rentrez de Genève, les clés sont sur votre bureau. Si personne ne peut vous les ramener, on ouvre la porte de chez vous."),
            ("Locaux professionnels", "Bureaux, commerces, cabinets : ouverture, remplacement de cylindres après départ d'un collaborateur, renforcement."),
        ],
        "tip": "Si vous faites le trajet Genève–Nyon chaque jour, laissez un double chez un voisin ou un proche de confiance à Nyon. C'est souvent la solution la plus rapide, et on préfère vous le dire.",
        "faq": [
            ("Intervenez-vous dans le canton de Vaud ?", "Oui, à Nyon, Coppet, Gland et dans les communes voisines de La Côte. Pour une autre localité, appelez-nous : on vous répond franchement."),
            ("Le déplacement depuis Genève est-il compris dans le devis ?", "Oui. Le devis gratuit donné par téléphone comprend le déplacement : vous savez à quoi vous attendre avant qu'on parte."),
        ],
        "near": ["serrurier-gland", "serrurier-coppet", "serrurier-versoix"],
    },
    {
        "slug": "serrurier-coppet", "name": "Coppet", "label": "Coppet", "canton": "VD",
        "title": "Serrurier Coppet – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Coppet (VD) : maisons de bourg, propriétés, cylindres sur une même clé, sécurisation avant absence. Dépannage 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Coppet : maisons de bourg et propriétés au bord du lac",
        "lead": "Entre Genève et Nyon, on intervient à Coppet pour les urgences comme pour les projets de sécurisation, avec un devis gratuit par téléphone.",
        "intro": [
            "Petite ville vaudoise entre Genève et Nyon, Coppet est connue pour son château, ancienne demeure de Madame de Staël, et pour sa Grand-Rue bordée d'arcades. Autour du bourg, on trouve surtout des villas et des propriétés, au bord du lac ou sur les hauts.",
            "Les maisons y sont souvent anciennes ou spacieuses, avec plusieurs accès. C'est typiquement là qu'un regard d'ensemble sur les portes et les clés est utile, plutôt qu'une intervention au coup par coup.",
        ],
        "situations": [
            ("Maison de bourg dans la Grand-Rue", "Portes anciennes sur rue, serrures d'époque : on privilégie la réparation et des solutions discrètes qui respectent la façade."),
            ("Une seule clé pour toutes les portes", "Entrée, garage, porte de jardin, cave : on peut installer des cylindres qui s'ouvrent tous avec la même clé. Moins de trousseaux, plus de simplicité."),
            ("Avant une longue absence", "Vous partez plusieurs semaines ? C'est le bon moment pour vérifier cylindres, renforts et accès secondaires."),
        ],
        "tip": "Plusieurs portes, plusieurs clés ? Des cylindres sur une même clé simplifient la vie, à condition de garder le nombre de doubles sous contrôle. Notez à qui vous les confiez.",
        "faq": [
            ("Pouvez-vous installer des cylindres qui s'ouvrent avec la même clé ?", "Oui, c'est une demande fréquente pour les maisons avec plusieurs accès. On vous propose les modèles adaptés avec un devis gratuit."),
            ("Intervenez-vous aussi à Founex, Commugny ou Mies ?", "Nous couvrons la région entre Genève et Nyon. Appelez-nous : on vous confirme l'intervention et le délai au téléphone."),
        ],
        "near": ["serrurier-versoix", "serrurier-nyon", "serrurier-gland"],
    },
    {
        "slug": "serrurier-gland", "name": "Gland", "label": "Gland", "canton": "VD",
        "title": "Serrurier Gland – Dépannage 7j/7 | Clé en Main Genève",
        "desc": "Serrurier à Gland (VD) : immeubles récents, villas, serrures multipoints bloquées, contrôle des clés. Dépannage 7j/7, devis gratuit par téléphone.",
        "h1": "Serrurier Gland : immeubles récents, villas et familles",
        "lead": "Entre Nyon et Rolle, on intervient à Gland pour les portes bloquées, les clés perdues et les cylindres à changer, avec un devis gratuit par téléphone.",
        "intro": [
            "Entre Nyon et Rolle, Gland a beaucoup grandi : nouveaux quartiers d'immeubles, zones de villas et plusieurs organisations internationales de protection de la nature qui y ont leur siège.",
            "Beaucoup de jeunes familles, beaucoup de portes récentes : les demandes portent souvent sur des serrures multipoints qui coincent, des clés distribuées un peu trop largement, ou des locaux communs dont il faut gérer l'accès.",
        ],
        "situations": [
            ("La clé tourne, mais la porte ne s'ouvre pas", "Sur les portes récentes à verrouillage multipoints, une tringle peut se bloquer. Ne forcez pas : on débloque, on règle ou on remplace le mécanisme selon son état."),
            ("Trop de clés en circulation", "Nounou, voisins, famille, ancien colocataire : au bout de quelques années, on ne sait plus qui a une clé. Un changement de cylindre remet les compteurs à zéro."),
            ("Local vélos, garage souterrain", "Les locaux communs dépendent de la régie ou de la copropriété (PPE). On intervient à leur demande, ou on vous explique qui contacter."),
        ],
        "tip": "Tenez une petite liste des clés que vous confiez (à qui, quand). Le jour où l'une d'elles manque, vous saurez tout de suite s'il faut changer le cylindre.",
        "faq": [
            ("Gland, ce n'est pas trop loin pour vous ?", "Non, Gland fait partie de notre zone sur La Côte. On vous annonce au téléphone un délai réaliste et un devis gratuit, déplacement compris."),
            ("Que faire si la clé tourne mais la porte reste bloquée ?", "Ne forcez pas sur la clé ni sur la poignée : vous risqueriez de casser le mécanisme. Appelez-nous, on vous guide déjà au téléphone."),
        ],
        "near": ["serrurier-nyon", "serrurier-coppet", "serrurier-versoix"],
    },
]
