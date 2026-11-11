# Audit SEO : AMS Multiservices 24/7

- **Site audité :** https://www.sosserruriergeneve247.ch
- **Date :** 11 novembre 2026
- **Objectif :** entrer dans les dix premiers résultats organiques de Google sur « serrurier Genève » et « serrurier Geneve »
- **Périmètre :** étape 1, audit seul. Aucun site n'a été modifié.
- **Mise à jour :** 11 novembre 2026, après vos réponses (section 10). Le code du site a été retrouvé, quatre décisions sont prises.

## Verdict

Le site est techniquement irréprochable. Il obtient 100 sur 100 sur mobile, affiche son contenu principal en 1,5 seconde et pèse 149 Ko. Un seul des douze concurrents mesurés fait aussi bien. La vitesse n'explique donc pas son classement.

Ce qui le freine vient de la refonte mise en ligne le 1er novembre 2026 et de l'organisation des contenus :

1. Les 7 pages services ont été supprimées et redirigées vers l'accueil. Le site n'a plus de page pour « ouverture de porte Genève » ni pour « changement de serrure Genève ».
2. Les 55 pages zones font 183 mots en médiane, dont 57 % sont identiques d'une page à l'autre. C'est un schéma proche de ce que Google appelle des pages satellites.
3. L'ancien site est resté publié et indexable sur une adresse wixsite.com, avec 87 articles identiques et un numéro de téléphone qui n'est pas le vôtre. Son blog automatique continue d'y publier.
4. Le blog compte 87 articles et 106 744 mots, mais n'envoie presque aucun lien vers les pages à classer. Il pointe en revanche vers cinq domaines qui n'existent pas et vers un concurrent.

Sur les requêtes que j'ai pu tester, le site ressort sur la longue traîne (2e sur « serrurier Genève dépannage 24h/24 ouverture de porte ») mais pas dans les dix premiers sur « serrurier Genève » ni sur « serrurier geneve ». Ces tests viennent d'un moteur qui n'est pas Google.ch : voir les limites à la section 2.

Trois corrections ne dépendent d'aucune décision et peuvent être faites cette semaine : rétablir les pages services (C1), dépublier l'ancien site (C3) et supprimer les liens fautifs du blog (F4).

Deux données manquent pour conclure, et vous seul pouvez les fournir : le classement réel sur Google.ch et les liens entrants (section 10).

## 1. Où est la refonte ?

Vous m'avez demandé de vérifier d'abord si une refonte codée se trouve dans ce dossier. Trois sites sont en ligne, et un seul a son code ici.

| Site | Marque et téléphone | État | Code source |
|---|---|---|---|
| www.sosserruriergeneve247.ch | AMS Multiservices 24/7, 077 243 69 43 | En ligne. C'est déjà une refonte codée : site Wix « sans éditeur » créé le 1er novembre 2026, pages de 34 Ko. | Retrouvé chez Wix le 11 novembre, voir ci-dessous |
| amsmultiservice247.wixsite.com/my-site | AMS, 022 557 75 87 et 077 243 69 43 | En ligne et indexable. C'est l'ancien site Wix, créé le 27 mars 2024, resté publié quand le domaine a été rattaché au nouveau site. | Éditeur Wix |
| cle-en-main-geneve.netlify.app | Clé en Main Genève, 079 942 95 44 | En ligne et indexable, 22 pages. Site distinct d'AMS d'après vous : hors périmètre. | `cle-en-main-geneve/` |

Où est le code du site AMS :

- Il a été construit dans votre session « Maquette site serrurier Genève » (28 octobre au 1er novembre), qui n'avait pas de dépôt Git. Le générateur d'origine (`build.py`) n'existe que là-bas.
- Wix conserve le projet publié : révision `1c2868c5`, du 1er novembre à 11 h 17 UTC. Je l'ai téléchargé le 11 novembre sans rien modifier : une enveloppe Astro, les 149 pages HTML générées, la table des routes et des redirections (`src/routes.json`), le plan de site.
- L'étape 3 peut donc se faire directement sur ce code, puis par une nouvelle publication sur Wix. La version actuelle reste récupérable.

## 2. Méthode et limites

Mesures faites le 11 novembre 2026 :

- Crawl complet du site AMS : 149 URL issues du plan de site et des liens internes, avec un robot identifié qui respecte robots.txt. Pour chaque page : statut, redirections, title, meta description, H1 à H3, canonical, balise robots, hreflang, données structurées, liens, images, nombre de mots du contenu principal.
- Similarité entre pages, calculée sur les séquences de cinq mots.
- Lighthouse 12.2.1 en profil mobile sur 7 pages AMS (l'accueil trois fois) et sur la page classée de 12 concurrents.
- Rendu mobile à 390 px de large, vérifié sur capture d'écran.
- Crawl échantillon de 22 sites concurrents : robots.txt, plans de site, page classée et jusqu'à six pages types par site.
- Dates d'enregistrement des domaines (registre .ch), registre du commerce (Zefix), annuaire search.ch.
- Ancien site Wix et compte Wix : état de publication, pages, articles.

Ce qui n'a pas pu être mesuré :

| Donnée | Pourquoi | Conséquence |
|---|---|---|
| Classement réel sur Google.ch | Nouvelle tentative le 11 novembre, à votre demande : Google répond par son contrôle anti-robot, que je ne contourne pas. Les concurrents ont été identifiés avec l'outil de recherche intégré, dont l'index n'est pas celui de Google et qui interroge depuis les États-Unis. | Le panel de la section 7 est représentatif du marché, mais ce n'est pas un top 10 certifié. L'ordre des sites n'est pas un classement. |
| Liens entrants | Pas d'accès à un outil de liens ni à la Search Console. | Le facteur probablement le plus discriminant sur ce mot-clé n'est pas mesuré. |
| Core Web Vitals de terrain | L'API PageSpeed Insights a refusé les requêtes (quota épuisé). | LCP et CLS sont des mesures de laboratoire. L'INP ne se mesure que sur de vrais visiteurs. |
| Search Console | Pas d'accès. | Pages réellement indexées, requêtes, positions et anciennes URL connues de Google : inconnues. |
| Fiche Google Business Profile | Hors périmètre et non consultable. | La cohérence du nom et du téléphone avec la fiche reste à vérifier par vous. |
| Redirection HTTP vers HTTPS | Le port 80 n'est pas joignable depuis cette session. | L'en-tête HSTS est présent ; la redirection elle-même n'est pas testée. |

## 3. Le site en chiffres

| Indicateur | Valeur |
|---|---|
| URL crawlées | 149 : 148 en statut 200, 1 en 404 |
| URL dans le plan de site (`/plan-du-site.xml`) | 148, toutes en 200 et indexables |
| Répartition | 1 accueil, 1 page tarifs, 1 index de blog, 55 pages zones, 87 articles, 3 pages légales |
| Pages services | 0 (7 jusqu'au 31 octobre 2026) |
| Pages de moins de 300 mots | 61 sur 148, soit 41 % : les 55 zones, la page tarifs, les 3 pages légales, 2 articles |
| Longueur des pages zones | 159 à 211 mots, médiane 183 |
| Part identique entre pages zones | 57 % en médiane (51 à 61 %) |
| Articles | 87, médiane 1 328 mots, 106 744 mots au total, 13 avec une image |
| Rythme de publication | 80 articles entre le 4 juillet et le 31 octobre 2026, soit deux tous les trois jours |
| Title | 40 à 59 caractères, aucun doublon |
| Meta description | 116 à 153 caractères, aucune vide, aucun doublon |
| H1 | exactement un par page, aucun doublon |
| Canonical | présente et auto-référente sur les 148 pages |
| Balise robots | `index, follow` sur les 148 pages |
| hreflang | aucune (site monolingue, `lang="fr-CH"`) |
| Pages orphelines | aucune. 51 pages n'ont qu'un seul lien interne entrant : 49 articles, Champel et Jonction |
| Liens internes cassés | 1 |
| Redirections en chaîne | aucune |
| Images | 20 balises `<img>` sur 148 pages, toutes avec un attribut alt, dont 4 en anglais |
| Performance mobile (Lighthouse) | 99 à 100 sur les 7 pages testées |
| Domaine | enregistré le 27 mars 2024 |

Le détail page par page est dans `audit-seo-donnees/crawl-ams.tsv`.

## 4. Problèmes classés par impact

| N° | Problème | Pages concernées | Effort |
|---|---|---|---|
| C1 | Pages services supprimées et redirigées vers l'accueil | 7 URL | moyen |
| C2 | Pages zones minces et quasi identiques | 55 URL | élevé |
| C3 | Ancien site toujours publié et indexable | tout l'ancien site | faible |
| C4 | Deux sites sur le même mot-clé : tranché, Clé en Main Genève est hors périmètre | Clé en Main Genève | aucun |
| F1 | Neuf pages visent « serrurier Genève » | 9 URL | faible |
| F2 | Accueil moins complet que ceux des concurrents | `/` | moyen |
| F3 | Blog produit en série, redondant, sans liens vers les pages à classer | 87 articles | élevé |
| F4 | Liens vers cinq domaines inexistants et vers un concurrent | 7 articles | faible |
| F5 | Identité de l'entreprise variable selon les sources | site, annuaires, registre | faible |
| F6 | Anciennes adresses en anglais en erreur 404 | `/en/…` | faible |
| F7 | Aucune preuve d'expertise ni de réalité de l'entreprise | accueil, pages à créer | moyen |
| F8 | Autorité du domaine non mesurée | domaine | à mesurer |
| M1 | Données structurées en retrait par rapport à l'ancien site | toutes | faible |
| M2 | Page tarifs mince et concurrencée par cinq articles | `/serrurier-geneve-tarifs` | moyen |
| M3 | Maillage interne qui ne décrit pas les pages | toutes | moyen |
| M4 | Peu d'images, aucune identifiable, quatre alt en anglais | toutes | moyen |
| M5 | Aucune mesure des appels | toutes | faible |
| M6 | Tarif de nuit non chiffré | accueil, tarifs, zones | faible |
| M7 | Un lien interne cassé | 1 article | faible |
| M8 | Réglages Wix en anglais et en dollars | compte Wix | faible |
| L1 à L9 | Neuf points mineurs | voir tableau | faible |

### Critique

#### C1. Les pages services ont été supprimées et redirigées vers l'accueil

**Constat.** Jusqu'au 31 octobre, le site avait 7 pages services de 759 à 1 158 mots, balisées `Service` et `FAQPage`. Elles sont encore visibles sur l'ancien site. Sur le nouveau, leurs 7 adresses renvoient une redirection 301 vers l'accueil. Plus aucune page ne vise « ouverture de porte Genève », « changement de serrure Genève », « dépannage serrure », « coffre-fort » ou « vitrier Genève ». Seuls des articles de blog traitent ces sujets.

**Pages.** `/serrurier-geneve-ouverture-porte`, `/serrurier-geneve-depannage-serrure`, `/serrurier-geneve-installation-serrure`, `/serrurier-geneve-coffre-fort`, `/serrurier-geneve-controle-acces`, `/serrurier-geneve-securisation-effraction`, `/vitrier-geneve`.

**Pourquoi ça pèse sur le classement.** Une recherche de service appelle une page de service : un article « comment ouvrir une porte claquée » répond à une question, pas à « ouverture de porte Genève ». Une redirection vers l'accueil depuis une page au sujet précis est souvent traitée par Google comme une erreur « soft 404 », et l'historique de l'ancienne page n'est alors pas transmis. Enfin, ce sont les pages services qui, par leurs liens, renforcent l'accueil sur « serrurier Genève ».

**Qui le fait déjà.** 7 des 9 sites du panel de tête ont des pages services. Longueurs relevées sur deux pages par site : hugodubois.ch 1 950 mots, depannage-serrurier.ch 1 380, serrurier-geneve-multisecu.ch 740, sos-serrurier-geneve.ch 730, copserrurier.ch 410, serrurier-secours.ch 405.

**Correction.** Remettre ces 7 adresses en ligne avec un statut 200, aux mêmes URL, en supprimant les 7 règles de redirection. Partir du contenu de l'ancien site, à copier avant de le dépublier (C3). Sur chaque page : title et H1 propres, balisage `Service` et `BreadcrumbList`, lien depuis un bloc « services » de l'accueil, liens depuis les articles du même thème. À faire dans les jours qui viennent : ces adresses étaient en ligne il y a onze jours, Google les a probablement encore dans son index. La liste complète des pages services (changement de cylindre, porte claquée, clés perdues, blindage) relève de l'étape 2.

#### C2. Les 55 pages zones sont minces et quasi identiques

**Constat.** 55 pages `/serrurier/<lieu>` de 159 à 211 mots. En médiane, 57 % des séquences de cinq mots d'une page se retrouvent sur au moins neuf pages zones sur dix. La partie propre à chaque lieu tient en une phrase de vingt à trente mots, suivie d'une liste d'interventions tirée de six modèles. Le bloc de prix est identique partout, et la promesse « 15 à 30 minutes » figure sur 53 pages, de Gy aux Pâquis. Ces pages représentent 37 % des pages indexables. Avant la refonte, la page Carouge faisait 415 mots.

**Pages.** Les 55 URL `/serrurier/…`, listées dans `audit-seo-donnees/crawl-ams.tsv`.

**Pourquoi ça pèse sur le classement.** Les règles antispam de Google donnent comme exemples de pages satellites les « pages sensiblement similaires » et les pages « qui ciblent des régions ou des villes spécifiques ». Le risque est double : des pages explorées mais non indexées, et un signal de faible qualité qui pèse sur tout le site. Sans contenu propre, ces pages ne peuvent pas non plus se classer sur « serrurier Carouge ».

**Qui le fait déjà.** Pages zones du panel de tête : 2 000 mots chez depannage-serrurier.ch, 925 à 1 030 chez serrurier-geneve-multisecu.ch, 481 chez copserrurier.ch, 400 à 450 chez sos-serrurier-geneve.ch. Seul serrurerie-silva.ch a des pages aussi courtes (234 mots), sur un domaine enregistré en 2006.

**Correction.**

Vous m'avez confirmé que vous desservez réellement toutes les zones affichées. Les 55 adresses sont donc conservées, et c'est leur contenu qui change.

1. Réécrire toutes les pages zones en deux vagues : d'abord 20 zones prioritaires (les communes que vous avez citées et les quartiers de Genève-ville), puis les 34 autres. Viser 500 à 900 mots réellement propres au lieu : distance et temps de trajet depuis Chêne-Bougeries, type de bâti et de serrures, cas d'intervention fréquents, repères, contraintes d'accès, questions locales.
2. Ne pas désindexer les pages en attente : elles existent depuis 2024 et la réécriture peut être faite en quelques semaines.
3. Créer une vraie page `/serrurier` qui liste les zones. Aujourd'hui cette adresse redirige vers `/#zone`.
4. Remplacer « 15 à 30 minutes » par une fourchette propre à chaque zone, calculée sur la distance réelle, que vous validez.

#### C3. L'ancien site est toujours publié et indexable

**Constat.** `amsmultiservice247.wixsite.com/my-site` sert encore tout l'ancien site : accueil, 7 pages services, tarifs, 54 pages zones, 93 articles. Aucune balise noindex, canonical sur lui-même, exploration autorisée par robots.txt. Les 87 articles du nouveau site s'y trouvent à l'identique : 94 % et 96 % du texte en commun sur les deux articles comparés. Son blog automatique continue : cinq articles y ont été publiés depuis la refonte, les 2, 4, 6, 8 et 10 novembre, et n'existent que là. Il affiche deux numéros, 022 557 75 87 et 077 243 69 43. Vous m'avez confirmé que le 022 n'est pas le vôtre : l'ancien site publie donc un numéro erroné.

Je n'ai pas trouvé cette adresse dans l'index que je peux interroger. Son indexation par Google reste à vérifier avec la recherche `site:amsmultiservice247.wixsite.com`.

**Pourquoi ça pèse sur le classement.** Deux adresses se déclarent chacune version de référence du même contenu : Google doit en choisir une et peut retenir la mauvaise. Les nouveaux articles renforcent le site qui ne doit pas se classer. Les deux numéros brouillent l'identité de l'entreprise (F5).

**Correction.** Dans cet ordre :

1. Copier le contenu des 7 pages services et des articles publiés depuis le 1er novembre. C'est fait : voir `audit-seo-donnees/ancien-site/`.
2. Arrêter la publication automatique d'articles sur ce site.
3. Dépublier le site « AMS Serrurerie 24/7 » dans le tableau de bord Wix. Je peux le faire par la connexion Wix dès que vous me le confirmez.

#### C4. Deux sites sur le même mot-clé : tranché

**Constat.** `cle-en-main-geneve.netlify.app` est en ligne et indexable, avec le title « Serrurier Genève – Dépannage 7j/7 | Clé en Main Genève », la commune 1224 Chêne-Bougeries et le 079 942 95 44.

**Décision du 11 novembre.** Vous m'avez indiqué que ce n'est pas du tout le même site et que seul www.sosserruriergeneve247.ch compte. Clé en Main Genève sort donc de cet audit et de la suite du travail.

**À garder en tête.** Les deux sites visent la même requête depuis la même commune. Pour qu'ils ne se gênent pas, ils ne doivent partager ni adresse postale, ni numéro, ni liens entre eux.

### Fort

#### F1. Neuf pages visent « serrurier Genève » dans leur title et leur H1

| Page | Title | Mots |
|---|---|---|
| `/` | Serrurier Genève 24h/24 et 7j/7 – AMS Multiservices 24/7 | 812 |
| `/serrurier/geneve` | Serrurier à Genève-ville 24h/24 – AMS Multiservices | 192 |
| `/serrurier-geneve-tarifs` | Tarifs serrurier Genève : prix d'ouverture de porte | 258 |
| `/blog` | Conseils serrurier Genève – Blog AMS Multiservices | 1 102 |
| `/post/serrurier-geneve-24-7` | Serrurier Genève 24/7 – Votre expert en sécurité à Genève | 346 |
| `/post/serrurier-genève-urgence` | Serrurier Genève urgence : votre sécurité, notre priorité | 174 |
| `/post/trouver-un-serrurier-genève-fiable-en-urgence` | Trouver un serrurier Genève fiable en urgence | 1 176 |
| `/post/combien-de-temps-pour-un-serrurier-à-genève` | Combien de temps pour un serrurier à Genève ? | 1 384 |
| `/post/tarif-ouverture-porte-serrurier-à-genève` | Tarif ouverture porte serrurier à Genève | 1 133 |

**Pourquoi ça pèse sur le classement.** Quand plusieurs pages d'un site sont candidates à la même requête, leurs signaux se dispersent et Google peut alterner entre elles. L'accueil doit être la seule page optimisée pour le mot-clé principal.

**Qui le fait déjà.** hugodubois.ch : une page par intention, rangée sous `/serrurier/geneve/`.

**Correction.**

- `/serrurier/geneve` : redirection 301 vers `/`. L'accueil est la page de Genève ; les quartiers gardent leurs pages.
- `/post/serrurier-geneve-24-7` et `/post/serrurier-genève-urgence` : redirection 301 vers `/`. Ce sont deux textes courts de 2025, sans contenu propre.
- `/blog` : title « Conseils serrurerie et sécurité – Blog AMS Multiservices », H1 « Conseils de serrurerie et de sécurité ».
- `/post/tarif-ouverture-porte-serrurier-à-genève` : fusion dans la page tarifs (M2).
- Les deux autres articles : un title centré sur leur question, par exemple « Comment reconnaître un serrurier fiable » et « Délai d'intervention d'un serrurier : à quoi s'attendre », avec un lien vers l'accueil sur l'ancre « serrurier à Genève ».
- `/serrurier-geneve-tarifs` garde « tarifs serrurier Genève » : c'est une autre intention.

#### F2. L'accueil couvre moins le sujet que ceux des concurrents

**Constat.** 812 mots, dont environ 250 d'avis clients et 55 noms de lieux. Le mot « serrurier » y figure 7 fois et « Genève » 7 fois. La médiane du panel de tête est de 1 117 mots, avec 18 et 17 occurrences. Aucun bloc ne présente les services : « changement de serrure », « blindage », « coffre-fort » et « dépannage » n'apparaissent pas. Les H2 ne décrivent pas le métier (« Ce qu'en disent nos clients », « Nos prix, sans astérisque »). Le premier paragraphe ne contient pas « Genève ». L'accueil ne fait de lien vers aucun article.

**Pourquoi ça pèse sur le classement.** Google classe la page qui couvre le mieux les attentes derrière la requête : services, prix, zones, délais, preuves. Les liens de l'accueil sont aussi les plus forts du site, et ils ne servent aujourd'hui que les pages zones.

**Qui le fait déjà.** serrurier-secours.ch (8 services, zones, FAQ), serrurier-romand.ch (8 prestations, FAQ), depannage-serrurier.ch (services, quartiers, codes postaux, grille tarifaire, FAQ), hugodubois.ch (11 sections).

**Correction.** Ajouter, sans toucher aux blocs de conversion :

1. Une section « Nos services de serrurerie à Genève » : 7 ou 8 cartes de 40 à 60 mots, chacune liée à sa page service.
2. Un paragraphe « Qui sommes-nous » de 120 à 150 mots : entreprise inscrite au registre du commerce, base à Chêne-Bougeries, qui intervient.
3. Des H2 descriptifs : « Tarifs d'un serrurier à Genève », « Zones d'intervention dans le canton de Genève », « Questions fréquentes sur le dépannage ».
4. « à Genève » dans la première phrase.
5. Trois ou quatre liens vers les meilleurs guides.

Cible : 1 200 à 1 400 mots, au niveau du panel, sans chercher une densité de mots-clés.

#### F3. Le blog est produit en série, redondant, et n'alimente pas les pages à classer

**Constat.** 80 des 87 articles ont été publiés entre le 4 juillet et le 31 octobre 2026, à raison de deux tous les trois jours, tous d'une longueur voisine (médiane 1 328 mots). 13 ont une image. Beaucoup traitent le même sujet : 9 sur l'effraction, 8 sur le changement de serrure ou de cylindre, 6 sur les prix (tableau en section 6). 86 articles sur 87 ne font aucun lien vers une page zone, aucun ne peut en faire vers une page service, et l'accueil ne reçoit aucun lien depuis le corps d'un article. 49 articles n'ont qu'un seul lien entrant, celui de l'index du blog.

**Pourquoi ça pèse sur le classement.** Les règles antispam de Google visent le « contenu à grande échelle » produit d'abord pour le classement, quel que soit l'outil ; une cadence régulière et des sujets qui se recoupent en sont les marques. Des articles concurrents entre eux se neutralisent. Et 106 744 mots qui ne transmettent rien aux pages commerciales sont un actif inutilisé.

**Qui le fait déjà.** serrurier-geneve-multisecu.ch publie des articles courts qui répondent chacun à une question précise, rangés sous `/serrurerie-a-geneve/`. depannage-serrurier.ch a une page tarifs et une page FAQ plutôt que cinq articles sur les prix. serrurier-romand.ch a peu de pages, mais un lexique de 6 666 mots.

**Correction.**

1. Arrêter la publication automatique.
2. Par sujet, garder le meilleur article et y fusionner les autres avec une redirection 301. Objectif : 25 à 30 guides. Le plan de fusion article par article relève de l'étape 2.
3. Dans chaque guide conservé : un lien vers la page service correspondante et un lien vers l'accueil ou les tarifs, avec des ancres variées.
4. Signer les guides du nom du serrurier, avec une date de mise à jour et une photo réelle.

#### F4. Liens vers cinq domaines inexistants et vers un concurrent

**Constat.** 9 liens répartis dans 6 articles pointent vers 5 domaines absents du DNS et non enregistrés au registre .ch (vérifié le 11 novembre 2026). 2 autres liens, suivis par les moteurs, pointent avec l'ancre « sos serrurier genève » vers sos-serrurier-geneve.ch (022 886 02 12), un site du panel de tête.

| Article | Lien vers |
|---|---|
| `/post/réponses-professionnelles-pour-vos-urgences-serrurerie-serrurier-réparation-rapide` | ams-multiservices.ch/urgence-serrurier |
| `/post/trouver-un-vitrier-rapide-à-genève-assistance-vitrerie-immédiate` | ams-multiservices.ch (2 liens) |
| `/post/services-de-serrurerie-24-7-à-genève-serrurerie-assistance-genève` | ams-serrurerie-24-7-geneve.ch |
| `/post/services-24-7-de-ams-serrurerie-serrurier-chêne-bougeries-24h` | ams-serrurerie.ch |
| `/post/interventions-express-pour-dépannage-vitrage-cassé-à-genève` | sosvitrerierapidegeneve.ch (2 liens) |
| `/post/ams-vitrier-genève-votre-expert-vitrier-disponible-24-7` | ams-vitrier.ch (2 liens) |
| `/post/artisan-serrurier-urgence-votre-allié-pour-toutes-vos-urgences-à-genève` | sos-serrurier-geneve.ch (2 liens) |

**Pourquoi ça pèse sur le classement.** Un lien mort est un signal de négligence et une impasse pour le lecteur. Un domaine libre peut être acheté par n'importe qui, qui recevrait alors vos liens. Un lien suivi vers un concurrent, sur votre mot-clé, travaille pour lui.

**Correction.** Supprimer ces 11 liens, ou les faire pointer vers vos propres pages : l'accueil, ou `/vitrier-geneve` une fois rétablie. Vous m'avez confirmé que sos-serrurier-geneve.ch n'est pas à vous : c'est bien un lien vers un concurrent.

#### F5. L'identité de l'entreprise varie d'une source à l'autre

**Constat.** Cinq variantes du nom, deux numéros de téléphone, un numéro IDE qui existe mais n'est affiché nulle part, une adresse Gmail. Le détail est en section 8.

**Pourquoi ça pèse sur le classement.** Google identifie une entreprise locale en recoupant nom, adresse et téléphone entre le site, les annuaires et le registre. Chaque variante affaiblit ce recoupement. Dans un métier connu pour ses arnaques, une entité vérifiable est aussi un signal de confiance pour l'internaute.

**Qui le fait déjà.** travaux-depannage.ch, serruriersschweizer.ch et sos-serrures24.ch affichent leur numéro IDE.

**Correction.** Arrêter un format unique (étape 4) et l'appliquer partout. Afficher dans les mentions légales et le pied de page la raison sociale inscrite, le titulaire et le numéro CHE-417.859.085. Le seul numéro valable est le 077 243 69 43 (+41 77 243 69 43) : retirer le 022 557 75 87 partout où il subsiste, à commencer par l'ancien site, et vérifier la fiche Google. Remplacer l'adresse Gmail par une adresse au nom de domaine.

#### F6. Les anciennes adresses en anglais renvoient une erreur 404

**Constat.** L'ancien site avait une version anglaise. `/en/serrurier/satigny` et `/en/serrurier/troinex` figurent encore dans un index de recherche et renvoient 404, comme `/en` et `/en/blog`.

**Pourquoi ça pèse sur le classement.** Une adresse indexée qui renvoie 404 perd son historique et les liens qu'elle a pu recevoir.

**Correction.** Rediriger en 301 `/en/<chemin>` vers `/<chemin>`, et `/en` vers `/`. Avant de figer le plan de redirection, extraire de la Search Console la liste des anciennes URL (rapports Pages et Liens) : je n'ai pas pu la reconstituer entièrement.

#### F7. Rien ne prouve l'expertise ni la réalité de l'entreprise

**Constat.** Pas de page À propos ni de page contact : `/a-propos` et `/contact` renvoient 404. Personne n'est présenté, alors que les avis cités sur l'accueil nomment le serrurier. Le visuel d'accueil a l'aspect d'une image de banque d'images et ne porte aucune métadonnée. Deux affirmations ne sont pas étayées : « Serrurier agréé par toutes les assurances ménage » et « 15 à 30 minutes » sur toutes les zones.

**Pourquoi ça pèse sur le classement.** Les critères de qualité de Google (expérience, expertise, autorité, fiabilité) comptent davantage pour un service d'urgence à domicile, où l'internaute confie l'accès à son logement.

**Qui le fait déjà.** serrurerie-silva.ch a une galerie et une page presse, depannage-serrurier.ch une page À propos, hugodubois.ch une section « Nos artisans à Genève ».

**Correction.** Créer `/a-propos` : qui intervient, depuis quand, numéro du registre du commerce, assurance responsabilité civile, marques posées, photos du véhicule et d'interventions à Genève. Remplacer le visuel d'accueil par une photo réelle. Reformuler les deux affirmations en faits vérifiables, par exemple « facture détaillée acceptée par les assurances ménage ».

#### F8. L'autorité du domaine n'est pas mesurée

**Constat.** Le domaine date du 27 mars 2024. Six des neuf sites du panel de tête ont été enregistrés entre 2000 et 2017. Je n'ai aucune donnée sur vos liens entrants ni sur ceux des concurrents. Seule citation vérifiée : la fiche search.ch et local.ch.

**Pourquoi ça pèse sur le classement.** À contenu comparable, ce sont les liens et les citations locales qui départagent les sites sur un mot-clé principal. L'âge n'est pas un obstacle en soi : serrurier-geneve-multisecu.ch, enregistré en avril 2025, figure dans le panel.

**Correction.** Me transmettre le rapport Liens de la Search Console. Le plan de citations et de liens locaux relève de l'étape 4.

### Moyen

#### M1. Données structurées en retrait par rapport à l'ancien site

**Constat.** Présents : `Locksmith`, `WebSite`, `WebPage`, `BreadcrumbList`, `BlogPosting`. Absents : `Service` et `OfferCatalog`, que l'ancien site avait ; `FAQPage`, alors que l'accueil a une FAQ de 4 questions ; les coordonnées `geo` ; `sameAs`. Dans `BlogPosting`, l'auteur est l'entreprise et l'image est le visuel d'accueil pour les 87 articles.

**Pourquoi ça compte.** Ces balises n'améliorent pas directement le classement. Elles lèvent les ambiguïtés sur l'entreprise et ses services. Pour la FAQ, n'attendez pas d'affichage enrichi : depuis août 2023, Google le réserve aux sites gouvernementaux et de santé.

**Qui le fait déjà.** `FAQPage` : hugodubois.ch, travaux-depannage.ch, serruriersschweizer.ch, urgence-serrurerie-geneve.ch. Coordonnées géographiques : serrurier-secours.ch, depannage-serrurier.ch.

**Correction.** Sur `Locksmith` : `geo`, `hasMap`, `sameAs` (fiche Google, local.ch, search.ch), raison sociale et numéro IDE. `Service` sur chaque page service, `FAQPage` là où une FAQ est visible, auteur `Person` sur les guides.

#### M2. La page tarifs est mince et concurrencée par cinq articles

**Constat.** `/serrurier-geneve-tarifs` fait 258 mots, composés de blocs déjà présents sur l'accueil (simulateur, tableau, étapes). L'ancienne page tarifs faisait 724 mots avec une FAQ. Cinq articles visent des requêtes de prix.

**Pourquoi ça compte.** « Prix serrurier Genève » est une requête à part entière. Une page unique et complète la capte mieux que six pages partielles.

**Qui le fait déjà.** serruriersschweizer.ch a une page tarifs de 1 512 mots, depannage-serrurier.ch une « grille tarifaire 2026 ».

**Correction.** En faire la seule page de prix : tarif par prestation (les fourchettes figurent déjà dans vos articles), ce qui fait varier le prix, tarif de nuit chiffré, exemples de factures. Y fusionner par redirection 301 `/post/tarif-ouverture-porte-serrurier-à-genève` et `/post/combien-coûte-l-ouverture-d-une-porte-à-genève`.

#### M3. Le maillage interne ne décrit pas les pages

**Constat.** Les ancres de navigation sont « Prix », « Avis », « Zone », « FAQ ». L'accueil ne reçoit aucune ancre descriptive. Les pages zones reçoivent 1 à 10 liens, Champel et Jonction un seul. 49 articles n'en reçoivent qu'un.

**Pourquoi ça compte.** L'ancre d'un lien indique à Google le sujet de la page visée, et le nombre de liens entrants répartit le poids entre les pages.

**Qui le fait déjà.** depannage-serrurier.ch : 620 liens internes sur sa page Genève, vers ses services, ses quartiers et les communes voisines. hugodubois.ch : 88, avec un fil d'Ariane.

**Correction.** Bloc services sur l'accueil et dans le pied de page, page `/serrurier` comme sommaire des zones, liens contextuels dans les guides, fil d'Ariane visible. Le plan détaillé relève de l'étape 2.

#### M4. Peu d'images, aucune identifiable, quatre textes alternatifs en anglais

**Constat.** 20 images sur 148 pages. 13 articles sur 87 en ont une, aucune page zone. Quatre attributs alt sont en anglais, par exemple « Eye-level view of a locksmith working on a door lock ».

**Pourquoi ça compte.** Des photos réelles appuient la crédibilité (F7) et peuvent ressortir dans Google Images. Un alt en anglais sur une page en français est incohérent.

**Qui le fait déjà.** serrurerie-silva.ch a une galerie de réalisations ; l'accueil de serrurier-geneve-multisecu.ch compte 106 images.

**Correction.** Une photo réelle par page service et par zone prioritaire, alt descriptif en français, format WebP.

#### M5. Aucune mesure des appels

**Constat.** Le site ne charge aucun script tiers. C'est excellent pour la vitesse, mais rien ne compte les clics sur « Appeler » et « WhatsApp ».

**Pourquoi ça compte.** Ce n'est pas un facteur de classement. Sans cette mesure, impossible de savoir quelles pages rapportent des appels ni de piloter la suite.

**Correction.** Valider la propriété dans la Search Console et y soumettre `/plan-du-site.xml`. Compter les clics sur les liens `tel:` et WhatsApp avec un outil léger et sans cookies.

#### M6. Le tarif de nuit n'est pas chiffré

**Constat.** Le tableau et le simulateur indiquent « tarif de nuit » dès 18 h, sans montant.

**Pourquoi ça compte.** La transparence des prix est votre avantage : 7 sites sur 20 seulement affichent des prix. Un tarif caché l'affaiblit.

**Qui le fait déjà.** depannage-serrurier.ch annonce une majoration de 50 % la nuit et le dimanche.

**Correction.** Indiquer le montant ou la majoration de nuit sur l'accueil, la page tarifs et les pages zones.

#### M7. Un lien interne cassé

**Page.** `/post/comment-faire-face-à-une-clé-perdue` : l'ancre « Appeler un super-héros des serrures » pointe vers `/post/www.sosserruriergeneve247.ch`, qui renvoie 404.

**Correction.** Remplacer la cible par `tel:+41772436943`.

#### M8. Les réglages Wix du nouveau site sont en anglais et en dollars

**Constat.** Langue `en`, région `US`, fuseau `America/New_York`, devise `USD`.

**Pourquoi ça compte.** Ces réglages n'apparaissent pas dans les pages, qui sont bien en `fr-CH`. Ce sont en revanche eux que Wix transmet aux assistants IA par le point d'accès annoncé dans `/llms.txt`.

**Correction.** Dans le tableau de bord Wix : français, Suisse, Europe/Zurich, CHF, et remplir les informations de l'entreprise.

### Faible

| N° | Constat | Page | Pourquoi | Correction |
|---|---|---|---|---|
| L1 | `/sitemap.xml` renvoie 404 : cette adresse est réservée par Wix. Le plan de site est à `/plan-du-site.xml`, déclaré dans robots.txt | racine | Les outils qui testent l'adresse standard ne trouvent rien | Soumettre `/plan-du-site.xml` dans la Search Console. Rien d'autre à corriger |
| L2 | Sur mobile, le numéro n'est pas écrit en haut de l'accueil : la barre fixe dit « Appeler », le bouton « Appeler maintenant » | `/` | Conversion : certains visiteurs veulent voir ou noter le numéro | Écrire « 077 243 69 43 » dans la barre fixe ou sur le bouton |
| L3 | La bulle de la mascotte recouvre le bouton « Confirmer par téléphone » | `/`, `/serrurier-geneve-tarifs` | Conversion : un bouton d'appel masqué | Masquer la bulle quand elle passe sur un bouton d'appel |
| L4 | Les 5 fichiers de police pèsent 111 Ko, soit 75 % du poids de la page | toutes | Marge de vitesse sur réseau lent | Passer à 3 fichiers |
| L5 | `sizes="108vw"` fait charger l'image de 1 600 px aux téléphones haute densité | `/` | Marge de vitesse sur réseau lent | Ajouter une variante de 1 200 px |
| L6 | Ni icône `apple-touch-icon` ni manifeste | toutes | Sans effet sur le classement ; finition | Les ajouter |
| L7 | Les 55 titles de zones suivent le même gabarit ; ceux de l'ancien site étaient différenciés | `/serrurier/…` | Taux de clic dans les résultats | Les différencier quand le contenu le sera |
| L8 | 75 adresses contiennent des accents (`/mentions-légales`, `/post/…-à-genève`) | 75 URL | Chaque accent crée des variantes d'encodage de la même adresse | Ne pas les changer : une URL modifiée coûte plus qu'elle ne rapporte. Écrire les nouvelles sans accents |
| L9 | Plus de page en anglais ; copserrurier.ch glisse « Emergency locksmith Geneva » dans sa meta description | à créer | Demande anglophone réelle à Genève, hors de l'objectif principal | Une page anglaise avec hreflang, une fois le reste traité |

## 5. Mesures techniques

Lighthouse 12.2.1, profil mobile, réseau et processeur bridés par simulation. Ce sont des mesures de laboratoire.

| Page AMS | Performance | LCP | TBT | CLS | Poids | Requêtes |
|---|---|---|---|---|---|---|
| Accueil (3 mesures) | 99 à 100 | 1,5 à 1,6 s | 0 à 4 ms | 0,015 | 149 à 155 Ko | 9 |
| `/serrurier/carouge` | 100 | 1,4 s | 0 ms | 0,015 | 124 Ko | 8 |
| `/serrurier-geneve-tarifs` | 100 | 1,2 s | 0 ms | 0,015 | 124 Ko | 8 |
| Article de blog | 100 | 1,2 s | 0 ms | 0,015 | 127 Ko | 8 |
| `/blog` | 100 | 1,3 s | 0 ms | 0,015 | 127 Ko | 8 |

Les scores SEO, accessibilité et bonnes pratiques sont à 100 sur les 7 mesures.

| Site (page classée) | Performance | LCP | Poids |
|---|---|---|---|
| **AMS** | **100** | **1,5 s** | **149 Ko** |
| urgence-serrurerie-geneve.ch | 100 | 0,9 s | 11 Ko |
| serruriersschweizer.ch | 96 | 2,4 s | 384 Ko |
| travaux-depannage.ch | 92 | 3,0 s | 649 Ko |
| hugodubois.ch | 86 | 1,6 s | 365 Ko |
| serrurerie-silva.ch | 84 | 4,2 s | 443 Ko |
| serrurier-geneve-multisecu.ch | 81 | 3,9 s | 567 Ko |
| copserrurier.ch | 68 | 5,9 s | 586 Ko |
| serrurier-romand.ch | 68 | 9,6 s | 1 249 Ko |
| serrurier-genève.ch | 64 | 7,3 s | 1 187 Ko |
| sos-serrurier-geneve.ch | 57 | 9,0 s | 2 615 Ko |
| serrurier-secours.ch | 48 | 9,8 s | 1 016 Ko |
| depannage-serrurier.ch | 19 | 8,5 s | 1 073 Ko |
| meier-serrurerie.ch | 19 | 16,1 s | 2 037 Ko |

Le panel de tête a un score médian de 68 et un LCP médian de 7,3 secondes. Des sites lents tiennent donc les positions : la vitesse est acquise pour AMS et ne demande plus de travail.

Autres vérifications :

- **HTTPS :** actif, en-tête HSTS d'un an. Le domaine sans www redirige en 301 vers www.
- **robots.txt :** tout autorisé, plan de site déclaré.
- **Plan de site :** 148 URL avec date de modification, toutes en 200.
- **Redirections :** barre oblique finale et `/index.html` redirigées en 301, sans chaîne.
- **Erreurs 404 :** une adresse inconnue renvoie un vrai statut 404.
- **Paramètres d'URL :** `?x=1` et `/blog?page=2` portent une canonical vers l'adresse propre.
- **JavaScript :** un seul fichier de 3 Ko, différé. Aucun script bloquant, aucun script tiers.
- **CSS :** 18,5 Ko en ligne dans la page.
- **Polices :** hébergées sur le site, préchargées, avec polices de repli ajustées, d'où un CLS de 0,015.
- **Image d'accueil :** WebP avec `srcset`, 22 Ko dans le test mobile.
- **INP :** non mesurable en laboratoire. Avec 0 à 4 ms de blocage et 3 Ko de JavaScript, le risque est faible. À confirmer dans la Search Console, rapport Signaux Web essentiels.
- **Rendu mobile :** aucun débordement horizontal, barre fixe « WhatsApp » et « Appeler » en bas d'écran.

## 6. Ciblage par page et cannibalisation

| Type de page | Nombre | Mot-clé visé | État |
|---|---|---|---|
| Accueil | 1 | serrurier Genève | Bonne cible : title et H1 corrects. Contenu à étoffer (F2). |
| Zone Genève-ville | 1 | serrurier Genève-ville | Concurrence directe de l'accueil (F1). |
| Autres zones | 54 | serrurier + lieu | Lieu présent dans le title, le H1, l'URL et le premier paragraphe. Pages minces et similaires (C2). |
| Tarifs | 1 | tarifs serrurier Genève | Intention distincte, page mince (M2). |
| Index du blog | 1 | conseils serrurier Genève | Reprend le mot-clé principal (F1). |
| Articles | 87 | questions et guides | 23 titles contiennent « Genève ». Redondants (F3). |
| Pages légales | 3 | aucun | Mentions légales incomplètes (F5). |
| Services | 0 | ouverture de porte, changement de serrure… | Supprimées le 1er novembre (C1). |

Pages dont le title ou le H1 porte le même thème :

| Thème | Pages | Détail |
|---|---|---|
| serrurier Genève | 9 | accueil, tarifs, index du blog, zone Genève-ville, 5 articles |
| effraction, cambriolage | 9 | 9 articles |
| changement de serrure ou de cylindre | 8 | 8 articles |
| prix, tarif | 6 | page tarifs et 5 articles |
| contrôle d'accès, badge, digicode | 6 | 6 articles |
| vitrerie | 6 | 6 articles |
| clé cassée ou perdue | 5 | 5 articles |
| ouverture de porte, porte claquée | 5 | page tarifs et 4 articles |
| coffre-fort | 4 | 4 articles |
| blindage | 3 | 3 articles |

Aucun bourrage de mots-clés : sur l'accueil, « serrurier » représente 0,9 % des mots, contre 0,9 à 4,4 % dans le panel de tête.

## 7. Concurrence

J'ai lancé six recherches. Les sites sortis sur « serrurier Genève » et « serrurier geneve » forment le panel de tête : neuf sites actifs, l'annuaire local.ch et un domaine qui n'existe plus (serrurierageneve.ch). Treize autres sites sont sortis sur les requêtes d'urgence et de prix.

Position d'AMS dans ces recherches :

| Requête | AMS |
|---|---|
| serrurier Genève | absent des 10 résultats |
| serrurier geneve | absent des 10 résultats |
| serrurier Genève dépannage 24h/24 ouverture de porte | 2e |
| serrurier geneve urgence | 6e |
| changement de serrure cylindre Genève serrurier prix | 4e, avec l'article « Combien coûte un changement de serrure ? » |

### Panel de tête : structure et contenu

| Site | Domaine | Pages | Structure | Page classée | Page zone | Page service |
|---|---|---|---|---|---|---|
| **AMS** | **2024** | **148** | **55 zones, 0 service, 87 articles** | **812 mots** | **183 mots** | **aucune** |
| copserrurier.ch | 2000 | 68 | 50 zones, 4 services | 611 | 481 | 404 à 421 |
| serrurerie-silva.ch | 2006 | 30 | 24 zones, galerie, presse | 257 | 234 | aucune |
| serrurier-genève.ch | 2015 | 3 | page unique | 518 | aucune | aucune |
| sos-serrurier-geneve.ch | 2016 | 17 | 10 zones, 6 services | 661 | 400 à 450 | 687 à 774 |
| depannage-serrurier.ch | 2016 | 56 730 | annuaire national : services, villes, tarifs, FAQ | 2 039 | 2 000 | 1 357 à 1 395 |
| serrurier-secours.ch | 2017 | 59 | 8 zones, 13 services | 1 174 | 455 à 1 214 | 376 à 434 |
| serrurier-romand.ch | 2020 | 53 | page Genève, prestations, lexique de 6 666 mots | 1 117 | 543 | page prestations |
| hugodubois.ch | 2022 | 1 439 | multi-métiers : page Genève, services, zones | 2 331 | 47 à 1 640 | 1 949 à 1 952 |
| serrurier-geneve-multisecu.ch | 2025 | 67 | 44 zones, 8 services, 6 articles | 1 283 | 925 à 1 030 | 734 à 746 |

Les longueurs de pages zones et services viennent de deux pages testées par site.

### Panel de tête : signaux

| Site | Liens internes de la page | Données structurées | Prix affichés | FAQ | Dernière mise à jour |
|---|---|---|---|---|---|
| **AMS** | **61** | **Locksmith** | **oui** | **oui, sans balisage** | **nov. 2026** |
| copserrurier.ch | 61 | Organization | oui | non | nov. 2026 |
| serrurerie-silva.ch | 32 | Organization | non | non | déc. 2024 |
| serrurier-genève.ch | 3 | aucune | non | non | févr. 2022 |
| sos-serrurier-geneve.ch | 14 | WebSite | non | non | mars 2024 |
| depannage-serrurier.ch | 620 | Locksmith, géo, AggregateRating | oui | oui | nov. 2026 |
| serrurier-secours.ch | 22 | Locksmith, géo | oui | oui | août 2026 |
| serrurier-romand.ch | 21 | Organization, AggregateRating | non | oui | oct. 2026 |
| hugodubois.ch | 88 | Locksmith, Service, FAQPage, géo | oui | oui | nov. 2026 |
| serrurier-geneve-multisecu.ch | 17 | Organization | non | non | juin 2025 |

La dernière mise à jour est la date de modification la plus récente déclarée dans le plan de site de chaque concurrent.

### Ce qu'ils ont et qu'AMS n'a pas

1. **Des pages services.** 7 sites sur 9. AMS en avait 7 jusqu'au 31 octobre.
2. **Une page principale plus complète.** Médiane de 1 117 mots contre 812, avec un bloc de services partout sauf chez serrurier-genève.ch.
3. **Des pages zones plus longues.** De 234 à 2 000 mots, médiane proche de 690. AMS est le plus bas du panel avec 183.
4. **De l'ancienneté.** Six domaines sur neuf ont entre 9 et 26 ans.
5. **Un numéro fixe genevois.** serrurier-secours.ch, serrurerie-silva.ch, serrurier-genève.ch et sos-serrurier-geneve.ch affichent un 022. AMS n'en a pas : celui de l'ancien site n'était pas le bon. Un 022 renvoyé sur le mobile serait un plus, sans urgence.
6. **Des liens entrants**, probablement. Non mesuré.

### Ce qu'AMS a et qu'ils n'ont pas

- La vitesse : 100 contre une médiane de 68.
- Des prix affichés : 4 sites du panel de tête sur 9 seulement le font.
- Une base technique sans défaut : canonical, title et description uniques sur toutes les pages.

### Deux enseignements

- **La fraîcheur ne tient pas les positions.** Trois sites du panel n'ont pas été mis à jour depuis 2022, mars 2024 et décembre 2024. Publier un article tous les deux jours n'est pas ce qui les a classés.
- **Le marché est attaqué par des sites récents.** Cinq sites sortis sur les requêtes d'urgence et de prix ont été enregistrés depuis août 2025 : urgence-serrurerie-geneve.ch, depanne-moi.ch, travaux-depannage.ch, depannage-serrurier-geneve-rapide.ch, serruriersschweizer.ch. Les plus aboutis ont des pages de plus de 2 000 mots, une grille de prix et leur numéro IDE affiché.

Le détail des 22 sites est dans `audit-seo-donnees/concurrents.tsv`.

## 8. E-E-A-T et cohérence NAP

### Nom, adresse, téléphone selon la source

| Source | Nom | Adresse | Téléphone |
|---|---|---|---|
| Site, données structurées et mentions légales | AMS Multiservices 24/7 | Chemin de la Montagne 96, 1224 Chêne-Bougeries | 077 243 69 43 |
| Site, en-tête | AMS MULTISERVICES · Serrurerie · Vitrerie · Genève | non indiquée | 077 243 69 43 |
| Articles du blog | AMS Serrurerie 24/7, AMS Vitrier | non indiquée | 077 243 69 43 |
| Ancien site, toujours en ligne | AMS, AMS Multiservices 24/7 Serrurerie Vitrerie Genève | Chemin de la Montagne 96, 1224 Chêne-Bougeries | 077 243 69 43, et 022 557 75 87 qui n'est pas le vôtre |
| search.ch et local.ch | Ams Multiservices 24/7 Serrurerie Vitrerie Genève | Chemin de la Montagne 96, Chêne-Bougeries | 077 243 69 43 |
| Registre du commerce | Ammari Ams Multiservices, entreprise individuelle, CHE-417.859.085, publiée le 4 novembre 2024 | siège à Chêne-Bougeries | non indiqué |
| Nom de domaine | sosserruriergeneve247 | sans objet | sans objet |
L'adresse est cohérente partout. Le nom ne l'est pas, et un numéro erroné subsiste sur l'ancien site.

### Signaux de confiance

| Élément | AMS | Dans les 20 sites concurrents lisibles |
|---|---|---|
| Adresse complète affichée | oui : pied de page, mentions légales, données structurées | 5 sites |
| Numéro IDE affiché | non, alors qu'il existe | 3 sites : travaux-depannage.ch, serruriersschweizer.ch, sos-serrures24.ch |
| Titulaire ou personne nommée | non | hugodubois.ch (« Nos artisans à Genève ») |
| Page À propos | non (404) | depannage-serrurier.ch, depannage-serrurier-geneve-rapide.ch |
| Page contact | non (404) | copserrurier.ch, serrurier-secours.ch, serrurerie-silva.ch, serrurier-geneve-multisecu.ch |
| Mentions légales | oui, 119 mots, sans titulaire ni IDE | non relevé |
| Prix affichés | oui | 7 sites |
| Photos réelles | aucune identifiable | serrurerie-silva.ch (galerie) |
| Preuves : assurance, marques, ancienneté | aucune | serrurerie-silva.ch (« + de 20 ans d'expérience », presse), serrurier-geneve-multisecu.ch (partenaires) |
| Adresse e-mail au nom de domaine | non, Gmail | non relevé |
| Numéro fixe 022 | aucun : celui de l'ancien site n'était pas le bon | au moins 7 sites |

## 9. Ce qui est bon et qu'il ne faut pas casser

- La vitesse et la légèreté : aucune dépendance externe, 9 requêtes.
- Title, meta description et H1 uniques et de bonne longueur sur les 148 pages.
- Canonical auto-référente partout, y compris sur les adresses avec paramètres.
- Un vrai statut 404, des redirections propres, aucun contenu bloqué.
- Le balisage `Locksmith` avec adresse, horaires et zone desservie.
- Les prix affichés et le simulateur.
- Les boutons d'appel et WhatsApp sur chaque page, et la barre fixe sur mobile.
- Les adresses des pages zones et des articles, conservées lors de la refonte.

## 10. Décisions prises et points ouverts

Vos réponses du 11 novembre :

| Question | Votre réponse | Conséquence |
|---|---|---|
| AMS et Clé en Main Genève sont-ils la même entreprise ? | Non, ce n'est pas du tout le même site. Seul www.sosserruriergeneve247.ch compte. | Clé en Main sort du périmètre (C4). |
| Où est le code du site ? | Vous ne savez pas : à chercher dans les autres sessions. | Retrouvé et téléchargé depuis Wix (section 1). |
| Le 022 557 75 87 est-il actif ? | Ce n'est pas le bon numéro. Le seul valable est le +41 77 243 69 43. | Le 022 est à retirer partout (C3, F5). |
| L'ancien site doit-il être dépublié ? | N'utiliser que le site actuellement en ligne. | Je le dépublie dès que vous me le confirmez (C3). |
| sos-serrurier-geneve.ch est-il à vous ? | Non. | C'est un concurrent : liens à supprimer (F4). |
| Quelles zones desservez-vous vite ? | Toutes les villes et tous les lieux affichés sur le site. | Les 55 pages zones sont conservées et réécrites (C2). |
| Export Search Console et capture Google ? | À regarder moi-même sur Google. | Google bloque les visites automatisées depuis ce serveur (section 2). |

Ce qui reste ouvert :

1. **Deux ou trois captures d'écran de Google** sur votre téléphone, après avoir tapé « serrurier Genève ». C'est le seul moyen d'avoir le vrai classement vu depuis Genève.
2. **Votre accord pour dépublier l'ancien site** « AMS Serrurerie 24/7 », qui affiche un numéro erroné.
3. **Qui, ou quel outil, publie un article tous les deux jours** sur l'ancien site ? Il faut l'arrêter.
4. **Un accès ou un export de la Search Console**, si vous en avez une : requêtes, pages et liens.

## Annexes

- `audit-seo-donnees/crawl-ams.tsv` : les 149 URL du site AMS avec statut, title, longueurs, H1, nombre de mots, liens entrants, canonical, données structurées, images.
- `audit-seo-donnees/concurrents.tsv` : les 22 sites concurrents avec date d'enregistrement, nombre et type de pages, longueur des pages, données structurées, prix, scores Lighthouse.
- `audit-seo-donnees/ancien-site/` : le texte des 7 pages services, de la page tarifs, de l'accueil, de la page Carouge et des 5 derniers articles de l'ancien site, copiés le 11 novembre avant sa dépublication.

## Sources

Sites et registres consultés :

- [AMS Multiservices 24/7](https://www.sosserruriergeneve247.ch/)
- [Ancien site AMS sur wixsite.com](https://amsmultiservice247.wixsite.com/my-site)
- [Clé en Main Genève](https://cle-en-main-geneve.netlify.app/)
- [Registre du commerce de Genève, extrait CHE-417.859.085](http://app2.ge.ch/ecohrcinternet/extract?lang=FR&companyOfsUid=CHE-417.859.085)
- [Fiche search.ch d'AMS](https://search.ch/tel/?was=ams+multiservices)
- [Annuaire local.ch, serrurerie à Genève](https://www.local.ch/fr/q/geneve/serrurerie)
- [Registre des domaines .ch (RDAP)](https://rdap.nic.ch/domain/sosserruriergeneve247.ch)

Documentation Google :

- [Règles concernant le spam dans la recherche : pages satellites et contenu à grande échelle](https://developers.google.com/search/docs/essentials/spam-policies?hl=fr)
- [Modifications apportées aux résultats enrichis HowTo et FAQ, août 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes?hl=fr)
- [Consignes relatives à la représentation de votre établissement sur Google](https://support.google.com/business/answer/3038177?hl=fr)

Concurrents analysés :

- Panel de tête : [copserrurier.ch](https://copserrurier.ch/), [serrurerie-silva.ch](https://serrurerie-silva.ch/), [serrurier-genève.ch](https://www.xn--serrurier-genve-6mb.ch/), [sos-serrurier-geneve.ch](https://www.sos-serrurier-geneve.ch/), [depannage-serrurier.ch](https://depannage-serrurier.ch/serrurier-geneve), [serrurier-secours.ch](https://www.serrurier-secours.ch/), [serrurier-romand.ch](https://www.serrurier-romand.ch/serrurier-geneve/), [hugodubois.ch](https://hugodubois.ch/serrurier/geneve/), [serrurier-geneve-multisecu.ch](https://serrurier-geneve-multisecu.ch/)
- Autres : [urgence-serrurerie-geneve.ch](https://urgence-serrurerie-geneve.ch/), [travaux-depannage.ch](https://travaux-depannage.ch/serrurier/serrurier-geneve/), [serruriersschweizer.ch](https://serruriersschweizer.ch/serrurier-geneve/), [depannage-geneve.ch](https://depannage-geneve.ch/serrurier-en-urgence/), [sos-serrurier24.com](https://sos-serrurier24.com/), [meier-serrurerie.ch](https://meier-serrurerie.ch/), [serrurierspeed.ch](https://www.serrurierspeed.ch/web/), [depanne-moi.ch](https://www.depanne-moi.ch/), [sos-serrures24.ch](https://sos-serrures24.ch/), [super-serrurier.ch](https://super-serrurier.ch/), [depannage-serrurier-geneve-rapide.ch](https://depannage-serrurier-geneve-rapide.ch/)
