# Stratégie et architecture SEO : AMS Multiservices 24/7

- **Site :** https://www.sosserruriergeneve247.ch
- **Date :** 11 novembre 2026
- **Étape 2 :** proposition d'architecture. Rien n'est encore modifié sur le site.
- **Statut :** en attente. Le 11 novembre, vous avez demandé de ne pas modifier le site : ce plan n'est pas exécuté.
- **Base :** l'audit `AUDIT-SEO.md` et vos réponses du 11 novembre.

## En bref

Le site passe de trois types de pages sans lien entre eux à trois silos reliés à l'accueil :

| | Aujourd'hui | Proposé |
|---|---|---|
| Accueil | 1 | 1, étoffé |
| Pages services | 0 | 10, plus la page tarifs |
| Pages zones | 55 pages de 183 mots | 1 sommaire et 54 pages réécrites |
| Articles | 87, redondants | 30 guides, chacun rattaché à un service |
| Pages de confiance | 3 pages légales | 3 pages légales, À propos, Contact |
| **Total indexable** | **148** | **environ 100** |

Moins de pages, mais chacune a une requête, un contenu propre et des liens vers les autres. L'accueil reste la seule page qui vise « serrurier Genève ».

Trois choses dépendent de vous avant l'exécution : la liste des services que vous proposez réellement, votre accord pour dépublier l'ancien site, et votre feu vert sur ce plan (section 9).

## 1. Le principe : trois silos

```
Accueil : « serrurier Genève »
├── Services (10 pages) + Tarifs
│     └── Guides du même sujet (30 au total)
├── Zones : sommaire /serrurier
│     └── 54 pages commune ou quartier
└── Confiance : À propos, Contact, mentions légales
```

Trois règles tiennent l'ensemble :

1. **Une requête, une page.** Deux pages ne visent jamais la même recherche.
2. **Chaque page renvoie vers le haut.** Un guide pointe vers son service, un service et une zone pointent vers l'accueil.
3. **Tout est à deux clics de l'accueil au plus.** Vous demandiez trois clics au maximum.

## 2. L'accueil

**Requêtes visées :** serrurier Genève, serrurier geneve, serrurier urgence Genève, dépannage serrurier Genève, serrurier 24h/24 Genève. Ces variantes désignent toutes le même besoin : elles se traitent sur l'accueil, pas sur des pages séparées.

**Title et H1 :** inchangés, ils sont bons.

**Ce qui s'ajoute**, sans toucher aux blocs d'appel, de prix et d'avis :

| Section | Contenu | Pourquoi |
|---|---|---|
| Nos services de serrurerie à Genève | 10 cartes de 40 à 60 mots, chacune liée à sa page | Aujourd'hui aucun service n'est décrit ; 7 des 9 concurrents du panel ont ce bloc |
| Qui sommes-nous | 120 à 150 mots : entreprise inscrite au registre du commerce, base à Chêne-Bougeries, qui intervient | Preuve de réalité, lien vers À propos |
| Zones d'intervention | Les 20 zones prioritaires et un lien vers le sommaire | 55 liens d'un coup diluent le poids de chacun |
| Conseils | 4 guides : porte claquée, prix, arnaques, effraction | L'accueil ne fait aujourd'hui de lien vers aucun article |
| Titres de section | « Tarifs d'un serrurier à Genève », « Zones d'intervention dans le canton de Genève », « Questions fréquentes sur le dépannage » | Les H2 actuels ne décrivent pas le métier |

Longueur visée : 1 200 à 1 400 mots, la médiane du panel étant de 1 117.

## 3. Le silo services

### Les pages

| Adresse | État | Requête visée | Title proposé |
|---|---|---|---|
| `/serrurier-geneve-ouverture-porte` | à rétablir | ouverture de porte Genève | Ouverture de porte à Genève 24h/24 \| AMS Multiservices |
| `/serrurier-geneve-porte-claquee` | nouvelle | porte claquée Genève | Porte claquée à Genève : ouverture sans dégât \| AMS |
| `/serrurier-geneve-installation-serrure` | à rétablir | changement de serrure Genève, changement de cylindre | Changement de serrure et de cylindre à Genève \| AMS |
| `/serrurier-geneve-depannage-serrure` | à rétablir | dépannage serrure Genève, serrure bloquée | Dépannage de serrure à Genève : serrure bloquée \| AMS |
| `/serrurier-geneve-cle-perdue` | nouvelle | clé perdue Genève, clé cassée | Clé perdue ou cassée à Genève : intervention 24h/24 \| AMS |
| `/serrurier-geneve-securisation-effraction` | à rétablir | serrurier après effraction Genève | Sécurisation après effraction à Genève 24h/24 \| AMS |
| `/serrurier-geneve-blindage-porte` | nouvelle | blindage de porte Genève, porte blindée | Blindage de porte à Genève : porte blindée, renforts \| AMS |
| `/serrurier-geneve-coffre-fort` | à rétablir | ouverture coffre-fort Genève | Coffre-fort à Genève : ouverture, dépannage, pose \| AMS |
| `/serrurier-geneve-controle-acces` | à rétablir | contrôle d'accès Genève | Contrôle d'accès à Genève : badges et digicodes \| AMS |
| `/vitrier-geneve` | à rétablir | vitrier Genève | Vitrier à Genève 24h/24 : vitre cassée en urgence \| AMS |
| `/serrurier-geneve-tarifs` | existante, à étoffer | tarifs serrurier Genève, prix serrurier Genève | Tarifs serrurier Genève : prix par intervention \| AMS |

Tous les titles font 60 caractères au plus.

Les 7 adresses « à rétablir » existaient jusqu'au 31 octobre. Je les garde telles quelles pour récupérer leur historique dans Google, y compris `/serrurier-geneve-installation-serrure`, qui devient la page du changement de serrure : l'adresse compte beaucoup moins que le title et le contenu.

### Comment elles ne se marchent pas dessus

| Paire à risque | Partage |
|---|---|
| Ouverture de porte et porte claquée | La première couvre tous les cas : porte fermée à clé, porte blindée, clé restée à l'intérieur. La seconde ne traite que la porte claquée : méthode sans dégât, prix, délai. Chacune renvoie à l'autre. |
| Ouverture de porte et clé perdue | L'ouverture répond à « je suis dehors ». La page clé perdue répond à « quelqu'un peut avoir ma clé » : changement de cylindre, régie, assurance. |
| Changement de serrure et blindage | Le changement est un remplacement, souvent urgent. Le blindage est un projet de renfort : porte blindée, cornières, serrure multipoints. |
| Dépannage de serrure et accueil | « Dépannage de serrure » est une réparation. « Dépannage serrurier » est une demande d'urgence : elle reste sur l'accueil. |
| Tarifs et guides de prix | Un seul guide de prix subsiste, sur le changement de serrure. Tout le reste est fusionné dans la page tarifs. |

### Le gabarit d'une page service

800 à 1 200 mots, dans cet ordre :

1. H1 avec le service et « à Genève », deux phrases, boutons d'appel et WhatsApp.
2. Dans quels cas nous appeler : les situations réelles.
3. Comment nous intervenons : la méthode, ce qui est fait sans dégât et ce qui ne peut pas l'être.
4. Prix de ce service, avec lien vers la page tarifs.
5. Ce qu'il faut préparer ou vérifier : pièce d'identité, régie, assurance.
6. Questions fréquentes, 4 à 6, propres au service.
7. Liens : 2 services voisins, 3 à 5 guides du même sujet, 6 zones.

Les textes de l'ancien site, sauvegardés dans `audit-seo-donnees/ancien-site/`, servent de base pour les 7 pages rétablies.

### À confirmer par vous

Je n'écrirai une page que pour un service que vous proposez vraiment. Dites-moi si l'un de ceux-ci est à retirer : **blindage de porte**, **coffre-fort**, **contrôle d'accès**, **vitrerie**.

## 4. Le silo zones

### Le sommaire

`/serrurier` devient une vraie page, alors qu'elle redirige aujourd'hui vers l'accueil. Elle liste les 54 zones par secteur :

| Secteur | Zones |
|---|---|
| Genève-ville | Acacias, Champel, Charmilles, Cornavin, Eaux-Vives, Jonction, Pâquis, Petit-Saconnex, Plainpalais, Rue du Rhône, Saint-Jean, Servette |
| Rive gauche | Anières, Chêne-Bougeries, Chêne-Bourg, Choulex, Collonge-Bellerive, Cologny, Corsier, Gy, Hermance, Jussy, Meinier, Presinge, Thônex, Vandœuvres, Veyrier |
| Sud du canton | Bardonnex, Bernex, Carouge, Confignon, Lancy, Onex, Perly-Certoux, Plan-les-Ouates, Troinex |
| Champagne | Aire-la-Ville, Avully, Avusy, Cartigny, Laconnex, Soral |
| Rive droite | Avanchets, Bellevue, Collex-Bossy, Grand-Saconnex, Meyrin, Pregny-Chambésy, Russin, Satigny, Vernier, Versoix |
| La Côte vaudoise | Nyon, Gland |

Title : « Zones d'intervention : canton de Genève et La Côte | AMS ». Cette page ne vise pas « serrurier Genève ».

`/serrurier/geneve` est redirigée vers l'accueil, qui est la page de Genève.

### Deux vagues de réécriture

Vous desservez toutes ces zones : les 54 adresses sont conservées. C'est l'ordre de réécriture qui change.

| Vague | Zones | Critère |
|---|---|---|
| 1 | Carouge, Lancy, Vernier, Meyrin, Onex, Thônex, Chêne-Bougeries, Chêne-Bourg, Plan-les-Ouates, Versoix, Grand-Saconnex, Cologny, Bernex, Veyrier, Eaux-Vives, Plainpalais, Pâquis, Champel, Servette, Jonction | Les communes que vous avez citées, les autres communes les plus peuplées et les grands quartiers de la ville |
| 2 | Les 34 autres | Communes plus petites et quartiers secondaires |

### Le gabarit d'une page zone

500 à 900 mots, dont rien n'est repris d'une autre page :

| Bloc | Contenu propre à la zone | Source |
|---|---|---|
| Délai | Distance par la route depuis Chêne-Bougeries et temps de trajet hors heures de pointe | Calcul d'itinéraire, que vous validez |
| Bâti et serrures | Type d'immeubles, de portes et de serrures du lieu | Connaissance du terrain, relue par vous |
| Cas fréquents | Les 3 ou 4 pannes typiques du lieu | Vos interventions. Sans exemple réel de votre part, j'écris « cas fréquents », jamais un faux récit daté |
| Accès | Stationnement, codes d'immeuble, zones piétonnes | Terrain |
| Prix | Tranche de déplacement de la zone, lien vers les tarifs | Votre grille |
| Questions locales | 2 ou 3 questions | Propres au lieu |
| Liens | 3 services, 3 ou 4 zones voisines, sommaire, accueil | Plan de maillage |

Le title est différencié par zone, par exemple « Serrurier Carouge 24h/24 : Vieux-Carouge, Fontenette | AMS ».

La promesse « 15 à 30 minutes » partout disparaît. Chaque page affiche une fourchette fondée sur sa distance réelle.

## 5. Le silo conseils

### Le principe

Les 87 articles deviennent 30 guides. Pour chaque sujet, le meilleur article reste à son adresse, reçoit les passages utiles des autres, et ceux-ci sont redirigés vers lui en 301.

| Décision | Articles |
|---|---|
| Conservés comme guides | 30 |
| Fusionnés dans un guide | 42 |
| Redirigés vers une page service, tarifs, zone ou accueil | 15 |

Avant d'exécuter, je vérifie dans la Search Console qu'aucun article à fusionner ne reçoit de visites. Si c'est le cas, c'est lui qui devient le guide conservé.

### Les 30 guides

| N° | Guide | Adresse conservée | Page parente | Articles fusionnés |
|---|---|---|---|---|
| G1 | Porte claquée : que faire, et que ne pas faire | `/post/comment-ouvrir-une-porte-claquée-sans-dégâts` | porte claquée | 3 |
| G2 | Porte de garage bloquée : qui appeler | `/post/porte-de-garage-bloquée-qui-appeler-à-genève` | dépannage | 0 |
| G3 | Prix d'un changement de serrure ou de cylindre | `/post/combien-coûte-un-changement-de-serrure` | changement de serrure | 1 |
| G4 | Quand changer sa serrure ou son cylindre | `/post/changer-le-cylindre-d-une-porte-d-entrée-quand-agir` | changement de serrure | 4 |
| G5 | Cylindre et serrure : la différence | `/post/différence-cylindre-et-serrure-le-vrai-rôle` | changement de serrure | 0 |
| G6 | Locataire ou propriétaire : qui paie le serrurier | `/post/serrurier-locataire-propriétaire-qui-paie` | changement de serrure | 1 |
| G7 | Quelle serrure choisir pour sa porte d'entrée | `/post/choisir-les-meilleures-serrures-haute-sécurité` | changement de serrure | 3 |
| G8 | Serrure multipoints : fonctionnement et pose | `/post/installer-une-serrure-multipoints-chez-soi` | changement de serrure | 0 |
| G9 | Serrure connectée ou biométrique : utile ou non | `/post/serrure-biométrique-sécurité-limites-et-choix` | changement de serrure | 1 |
| G10 | Serrure bloquée : que faire tout de suite | `/post/serrure-bloquée-que-faire-tout-de-suite` | dépannage | 1 |
| G11 | Serrure qui tourne dans le vide : causes et solutions | `/post/pourquoi-une-serrure-tourne-t-elle-dans-le-vide` | dépannage | 0 |
| G12 | Clé cassée dans la serrure : que faire | `/post/clé-cassée-dans-serrure-que-faire-vite` | clé perdue | 2 |
| G13 | Clé perdue : les bons réflexes | `/post/comment-faire-face-à-une-clé-perdue` | clé perdue | 1 |
| G14 | Reconnaître un serrurier fiable et éviter les arnaques | `/post/trouver-un-serrurier-genève-fiable-en-urgence` | accueil | 0 |
| G15 | Délai d'intervention d'un serrurier : à quoi s'attendre | `/post/combien-de-temps-pour-un-serrurier-à-genève` | accueil | 0 |
| G16 | En attendant le serrurier : préparer l'intervention | `/post/préparer-une-intervention-de-serrurier-en-urgence` | ouverture de porte | 2 |
| G17 | Assurance ménage : le serrurier est-il remboursé | `/post/assurance-couvre-un-serrurier-en-urgence` | effraction | 0 |
| G18 | Après une effraction : que faire, dans l'ordre | `/post/que-faire-après-une-effraction` | effraction | 5 |
| G19 | Reconnaître une tentative d'effraction | `/post/signes-de-tentative-d-effraction-à-reconnaître` | effraction | 0 |
| G20 | Sécuriser sa porte d'entrée | `/post/comment-sécuriser-une-porte-d-entrée-efficacement` | blindage | 2 |
| G21 | Porte blindée ou serrure renforcée : que choisir | `/post/porte-blindée-ou-serrure-renforcée-que-choisir` | blindage | 0 |
| G22 | Blinder une porte d'appartement | `/post/guide-blindage-porte-appartement-en-7-points` | blindage | 1 |
| G23 | Sécuriser une porte de cave | `/post/comment-sécuriser-une-porte-de-cave-efficacement` | blindage | 0 |
| G24 | Normes de serrures et de portes en Suisse | `/post/normes-suisses-de-serrure-et-sécurité-à-genève` | blindage | 2 |
| G25 | Sécuriser un commerce ou un bureau | `/post/cas-de-sécurisation-de-commerce-à-genève` | contrôle d'accès | 7 |
| G26 | Contrôle d'accès en entreprise : bien choisir | `/post/guide-contrôle-d-accès-entreprise-bien-choisir` | contrôle d'accès | 2 |
| G27 | Immeuble : badge ou digicode | `/post/badge-ou-digicode-immeuble-que-choisir` | contrôle d'accès | 2 |
| G28 | Coffre-fort bloqué : l'ouvrir sans dégât | `/post/ouvrir-un-coffre-fort-bloqué-sans-dégâts` | coffre-fort | 0 |
| G29 | Installer et ancrer un coffre-fort | `/post/installer-un-coffre-fort-maison-7-règles` | coffre-fort | 2 |
| G30 | Vitre cassée après une effraction : que faire | `/post/vitrier-urgence-après-effraction-à-genève` | vitrier | 0 |

Les quatre sujets que vous demandiez sont couverts : porte claquée (G1), prix (page tarifs et G3), arnaques (G14), normes suisses (G24).

Le détail des 87 articles, avec la décision et la cible de chacun, est dans `audit-seo-donnees/plan-fusion-blog.tsv`.

### Ce qui change dans chaque guide conservé

- Un nouveau titre, centré sur la question posée, sans « serrurier Genève ».
- Les meilleurs passages des articles fusionnés, sans répétition.
- Un lien vers la page service parente dans les premiers paragraphes, un lien vers l'accueil ou les tarifs, deux liens vers des guides voisins.
- Le nom du serrurier comme auteur, une date de mise à jour, une photo réelle quand vous en avez.
- Plus aucun lien vers les cinq domaines inexistants ni vers sos-serrurier-geneve.ch.

L'index `/blog` prend le title « Conseils serrurerie et sécurité – Blog AMS Multiservices » et classe les guides par service.

La publication automatique s'arrête. Ensuite, un guide par mois suffit, à condition qu'il réponde à une question que vos clients posent vraiment.

## 6. Le plan de maillage

### Profondeur

| Clics depuis l'accueil | Pages |
|---|---|
| 0 | Accueil |
| 1 | 10 services, tarifs, sommaire des zones, 20 zones prioritaires, index du blog, 4 guides, À propos, Contact, pages légales |
| 2 | 34 autres zones, 26 autres guides |

### Qui fait un lien vers qui

| Depuis | Vers |
|---|---|
| En-tête | Services, Tarifs, Zones, Conseils, À propos |
| Accueil | Les 10 services, la page tarifs, le sommaire des zones et les 20 zones prioritaires, 4 guides, À propos |
| Page service | Accueil, tarifs, 2 services voisins, 3 à 5 guides de son sujet, 6 zones |
| Page zone | Accueil, sommaire, 3 services, 3 ou 4 zones voisines, tarifs |
| Guide | Sa page service, l'accueil ou les tarifs, 2 guides voisins |
| Pied de page | Les 10 services, 10 zones, le sommaire, Conseils, À propos, Contact, pages légales |

### Les ancres

Aujourd'hui les liens disent « Prix », « Zone », « FAQ ». Chaque page cible recevra plusieurs ancres descriptives, pour qu'aucune ne soit répétée mécaniquement.

| Page visée | Ancres |
|---|---|
| Accueil | serrurier à Genève · serrurier d'urgence à Genève · AMS Multiservices · notre service de dépannage 24h/24 · un serrurier genevois |
| Ouverture de porte | ouverture de porte à Genève · faire ouvrir sa porte · ouverture de porte en urgence |
| Porte claquée | porte claquée · ouvrir une porte claquée sans dégât |
| Changement de serrure | changement de serrure · remplacer le cylindre · faire changer sa serrure à Genève |
| Dépannage | dépannage de serrure · serrure bloquée · réparation de serrure |
| Tarifs | tarifs · prix d'un serrurier à Genève · notre grille de prix |
| Zone | serrurier à Carouge · intervention à Carouge · Carouge |

## 7. Le plan de redirections

| Adresse | Aujourd'hui | Proposé |
|---|---|---|
| 7 anciennes pages services | 301 vers l'accueil | Pages rétablies, statut 200 |
| `/serrurier` | 301 vers `/#zone` | Page sommaire, statut 200 |
| `/serrurier/geneve` | Page de 192 mots | 301 vers `/` |
| `/en` et `/en/…` | 404 | 301 vers l'adresse française équivalente |
| 42 articles fusionnés | Pages | 301 vers leur guide |
| 15 articles redirigés | Pages | 301 vers `/vitrier-geneve` (4), `/` (5), tarifs (3), changement de serrure (1), Chêne-Bougeries (1), À propos (1) |
| `/a-propos`, `/contact` | 404 | Pages nouvelles |

Aucune adresse conservée ne change.

## 8. Données structurées par type de page

| Page | Balisage |
|---|---|
| Toutes | `Locksmith` complété : coordonnées géographiques, raison sociale, numéro IDE, liens vers la fiche Google, local.ch et search.ch |
| Accueil | `WebSite`, `FAQPage` sur la FAQ visible |
| Service | `Service` avec zone desservie, `FAQPage`, `BreadcrumbList` |
| Zone | `Locksmith` avec la zone en `areaServed`, `BreadcrumbList` |
| Guide | `Article` avec un auteur `Person`, dates, image propre, `BreadcrumbList` |
| À propos, Contact | `AboutPage`, `ContactPage` |

Un rappel : le balisage FAQ ne produit plus d'affichage enrichi dans Google pour un site commercial. Il sert à la compréhension de la page, pas au taux de clic.

## 9. La suite

### Comment j'exécute

Le code du site est récupéré depuis Wix. Je modifie les pages, je reconstruis le site, je vérifie tout en local (liens, redirections, balises, Lighthouse), puis je publie sur Wix. La version actuelle reste récupérable.

Ordre proposé, du plus urgent au plus long :

| Lot | Contenu | Corrige |
|---|---|---|
| 1 | Rétablir les 7 pages services, supprimer les 11 liens fautifs et le lien cassé, rediriger `/en`, dépublier l'ancien site | C1, C3, F4, F6, M7 |
| 2 | Accueil étoffé, page tarifs, 3 nouvelles pages services, À propos, Contact, mentions légales, données structurées | F1, F2, F5, F7, M1, M2, M6 |
| 3 | Sommaire des zones et 20 zones prioritaires | C2, M3 |
| 4 | Fusion du blog : 30 guides, 57 redirections | F3 |
| 5 | Les 34 autres zones | C2 |

L'étape 4 (annuaires, liens locaux, format NAP) et la feuille de route sur 90 jours avec les indicateurs à suivre viennent après.

### Ce dont j'ai besoin

1. **Votre feu vert sur ce plan**, ou vos corrections.
2. **Les services à retirer**, s'il y en a, parmi : blindage de porte, coffre-fort, contrôle d'accès, vitrerie.
3. **Votre accord pour dépublier l'ancien site** « AMS Serrurerie 24/7 », qui affiche un numéro qui n'est pas le vôtre.
4. **Le nom à afficher** comme titulaire et comme auteur des guides.
5. **Des captures d'écran de Google** sur « serrurier Genève », et un accès à la Search Console si vous en avez une.
6. **Des photos réelles** si vous en avez : véhicule, outillage, interventions. Ce n'est pas bloquant.
