# Clé en Main Genève : site vitrine

Site statique (HTML + CSS, sans framework, sans JavaScript) pour **Clé en Main Genève**, serrurier à Genève et sur La Côte.

- 22 pages : accueil, 4 services, 15 communes, contact, mentions légales (+ page 404)
- SEO local : `<title>`, meta description et H1 uniques, balise canonical, JSON-LD `Locksmith` sur toutes les pages, `FAQPage` sur l'accueil, `BreadcrumbList` sur les pages intérieures, `sitemap.xml`, `robots.txt`
- Lighthouse mobile mesuré en local : Performance 100 · Accessibilité 100 · Bonnes pratiques 100 · SEO 100
- Aucun prix, aucun avis, aucune statistique, aucune photo : les visuels sont des illustrations (WebP)

## Structure

```
cle-en-main-geneve/
├── public/              ← LE SITE À METTRE EN LIGNE (déjà généré)
├── src/
│   ├── content.py       ← tous les textes (services, communes, FAQ)
│   ├── build.py         ← gabarits, CSS, SEO, configuration (adresse, IDE, domaine)
│   ├── google-business.template.md ← modèle de GOOGLE-BUSINESS.md
│   └── images.mjs       ← génère les illustrations WebP et les icônes
├── GOOGLE-BUSINESS.md   ← contenu de la fiche Google (GÉNÉRÉ par build.py)
├── netlify.toml
├── vercel.json
└── README.md
```

## 1. À compléter avant la mise en ligne

Le bloc **CONFIGURATION** se trouve en haut de `src/build.py` :

| Variable   | À remplacer par                                             |
|------------|-------------------------------------------------------------|
| `SITE_URL` | votre domaine final, ex. `https://www.cle-en-main-geneve.ch` |
| `OWNER_NAME` | **à remplir** : prénom et nom du titulaire de l'entreprise individuelle (mentions légales) |
| `HOURS_24_7` | `True` = « 7j/7, 24h/24 » partout (site, JSON-LD, fiche Google). À ne garder que si quelqu'un répond vraiment la nuit. `False` = horaires de `HOURS` |
| `HOURS`    | horaires normaux jour par jour (utilisés si `HOURS_24_7 = False`) |
| `STREET`   | rue et numéro (facultatif ; vide = seulement « 1224 Chêne-Bougeries ») |
| `POSTAL_CODE` / `LOCALITY` | déjà remplis : `1224` / `Chêne-Bougeries`         |
| `IDE`      | vide = non affiché ; à remplir si l'entreprise obtient un numéro IDE, ex. `CHE-123.456.789` |
| `HOSTING`  | déjà rempli : Netlify                                        |

Puis régénérez le site :

```bash
cd cle-en-main-geneve
python3 src/build.py
```

Python 3.8 ou plus récent suffit, sans aucune installation. Le domaine peut aussi être passé sans modifier le fichier :
`SITE_URL=https://www.mondomaine.ch python3 src/build.py`

> ⚠️ Le domaine est utilisé dans les balises canonical, le sitemap, `robots.txt` et les données structurées. **Régénérez toujours le site après avoir changé de domaine.**

Pour modifier un texte, éditez `src/content.py`, puis relancez `python3 src/build.py`.
Pour régénérer les illustrations (facultatif) : `node src/images.mjs`. Il faut Node.js et Playwright.

## 2. Mettre en ligne

### Option A : Netlify (le plus simple)

**Sans compte Git (glisser-déposer)**
1. Créez un compte sur <https://app.netlify.com>.
2. Menu **Sites → Add new site → Deploy manually**.
3. Glissez-déposez le dossier **`public/`**. Le site est en ligne en quelques secondes, sur une adresse `xxx.netlify.app`.

**Avec GitHub (mises à jour automatiques)**
1. **Add new site → Import an existing project → GitHub**, puis choisissez le dépôt.
2. **Base directory** : `cle-en-main-geneve`. **Publish directory** : `public` (déjà prévu dans `netlify.toml`).
3. Déployez. Chaque `git push` met le site à jour.
   Pensez à lancer `python3 src/build.py` en local et à committer `public/` avant de pousser.

### Option B : Vercel

1. Créez un compte sur <https://vercel.com>, puis **Add New → Project** et importez le dépôt GitHub.
2. **Root Directory** : `cle-en-main-geneve`. **Framework Preset** : *Other*.
3. `vercel.json` indique déjà que le site se trouve dans `public/`, sans étape de build.
4. **Deploy**.

En ligne de commande, c'est aussi possible : `npx vercel` depuis `cle-en-main-geneve/`.

## 3. Connecter un nom de domaine

### a) Acheter le domaine
Chez un registraire suisse ou international : Infomaniak, Hostpoint, Gandi, OVH… Un `.ch` est recommandé pour le référencement local.

### b) Netlify
1. Dans le site : **Domain management → Add a domain**, puis saisissez `cle-en-main-geneve.ch`.
2. Chez votre registraire, dans la zone DNS :
   - **Option 1, la plus simple** : remplacez les serveurs de noms (nameservers) par ceux que Netlify affiche (`dns1.p0X.nsone.net`…).
   - **Option 2** : gardez votre DNS et créez :
     - un enregistrement `A` pour `@` qui pointe vers l'IP indiquée par Netlify (actuellement `75.2.60.5`) ;
     - un `CNAME` pour `www` qui pointe vers `votre-site.netlify.app`.
3. Le certificat HTTPS (Let's Encrypt) est activé automatiquement, en quelques minutes à quelques heures.
4. Définissez `www.cle-en-main-geneve.ch` (ou la version sans www) comme **Primary domain**. L'autre version redirigera automatiquement.

### c) Vercel
1. **Project → Settings → Domains → Add**, puis saisissez le domaine.
2. Chez le registraire :
   - un `A` pour `@` qui pointe vers `76.76.21.21` ;
   - un `CNAME` pour `www` qui pointe vers `cname.vercel-dns.com`.

   Vercel affiche les valeurs exactes à utiliser : suivez ses indications si elles diffèrent.
3. HTTPS automatique.

> Le domaine principal choisi (avec ou sans `www`) doit être **identique** à `SITE_URL` dans `build.py`.

## 4. Après la mise en ligne (référencement local)

1. **Google Search Console** (<https://search.google.com/search-console>) : ajoutez le domaine, validez-le par un enregistrement DNS TXT, puis soumettez `https://votre-domaine/sitemap.xml`.
2. **Bing Webmaster Tools** : importez directement le site depuis la Search Console.
3. **Fiche Google Business Profile** : c'est indispensable pour apparaître sur Google Maps quand on cherche « serrurier Genève ». Utilisez exactement le même nom, téléphone et adresse que sur le site, avec la catégorie *Serrurier* et une zone desservie.
4. Testez les données structurées : <https://search.google.com/test/rich-results>.
5. Vérifiez la vitesse : <https://pagespeed.web.dev>.

## Pages générées

| URL | Contenu |
|-----|---------|
| `/` | Accueil |
| `/ouverture-de-porte-geneve/` | Service : ouverture de porte |
| `/changement-de-serrure-geneve/` | Service : changement de serrure |
| `/securisation-blindage-geneve/` | Service : sécurisation et blindage |
| `/apres-effraction-geneve/` | Service : après effraction |
| `/serrurier-geneve/`, `/serrurier-carouge/`, `/serrurier-vernier/`, `/serrurier-lancy/`, `/serrurier-meyrin/`, `/serrurier-onex/`, `/serrurier-thonex/`, `/serrurier-chene-bougeries/`, `/serrurier-plan-les-ouates/`, `/serrurier-versoix/`, `/serrurier-grand-saconnex/`, `/serrurier-bernex/`, `/serrurier-nyon/`, `/serrurier-coppet/`, `/serrurier-gland/` | Une page par commune, texte rédigé pour chacune |
| `/contact/` | Contact |
| `/mentions-legales/` | Mentions légales et protection des données (LPD) |

## Notes

- **Polices** : Archivo 900 et Inter sont chargées depuis Google Fonts sans bloquer l'affichage. C'est mentionné dans la page de confidentialité.
- **Barre d'appel** fixe en bas d'écran sur mobile ; numéro visible en haut de chaque page (bandeau rouge et bouton dans l'en-tête).
- **Aucun formulaire** : le site ne collecte aucune donnée. Le contact se fait par téléphone ou SMS.
