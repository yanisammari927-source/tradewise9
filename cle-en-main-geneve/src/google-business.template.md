# Fiche Google Business Profile : contenu prêt à copier

<!-- Fichier GÉNÉRÉ par src/build.py à partir de src/google-business.template.md : modifiez le modèle, pas ce fichier. -->

À créer sur <https://business.google.com/create>, connecté avec le compte Google de l'entreprise.
Durée : environ 15 minutes, plus la vérification par Google (vidéo, code ou appel, selon ce que Google propose).

> Règle d'or : **nom, téléphone et site doivent être identiques** sur la fiche et sur le site.
> Ne mettez pas « serrurier Genève » dans le nom : Google sanctionne le bourrage de mots-clés dans le nom.

## ⚠️ Avant de commencer : l'adresse doit être réelle

Google vérifie l'adresse, de plus en plus souvent **par vidéo** : il faut filmer en continu l'extérieur (rue, numéro, enseigne ou boîte aux lettres), puis l'intérieur, ainsi que des preuves d'activité (véhicule, outillage, documents de l'entreprise).

- Utilisez **{ADDRESS}** seulement si c'est une adresse réelle de l'entreprise : un local, ou le domicile du serrurier **avec son accord**.
- **N'utilisez jamais** une adresse de domiciliation, une boîte postale, un espace de coworking où vous n'êtes pas présent, ni l'adresse de quelqu'un d'autre sans son accord. Google refuse la vérification ou suspend la fiche, souvent sans possibilité de recours rapide.
- Même si l'adresse est masquée sur la fiche (entreprise qui se déplace chez le client), Google la contrôle.
- L'adresse indiquée sur la fiche doit correspondre à celle des mentions légales du site.

---

## 1. Informations de base

| Champ | À saisir |
|---|---|
| Nom de l'entreprise | `Clé en Main Genève` |
| Catégorie principale | `Serrurier` |
| Catégories secondaires (facultatif) | `Service de dépannage serrurerie` ou `Service de serrurerie d'urgence`, si Google les propose ; sinon laissez vide |
| Avez-vous un lieu où les clients peuvent se rendre ? | **Non** (vous vous déplacez chez eux : l'adresse ne sera pas affichée) |
| Adresse demandée pour la vérification | l'adresse complète et réelle à {ADDRESS} (rue et numéro), non publiée — voir l'avertissement ci-dessus |
| Téléphone | `+41 79 942 95 44` |
| Site web | l'adresse définitive du site, ex. `https://www.cle-en-main-geneve.ch` |

## 2. Zones desservies

Ajoutez une par une (20 zones maximum) :

```
Genève
Carouge
Vernier
Lancy
Meyrin
Onex
Thônex
Chêne-Bougeries
Plan-les-Ouates
Versoix
Le Grand-Saconnex
Bernex
Nyon
Coppet
Gland
```

## 3. Horaires

{HOURS_GBP}

## 4. Description ({DESC_LEN} caractères, limite 750)

```
Clé en Main Genève est un serrurier qui intervient [[7j/7 et 24h/24||{DISPO_LONG}]] dans le canton de Genève et sur La Côte vaudoise (Nyon, Coppet, Gland). Porte claquée, clé perdue ou cassée, serrure bloquée, cylindre à changer, porte à sécuriser ou à remettre en état après une effraction : on vous écoute au téléphone, on vous explique la méthode prévue et on vous donne un devis gratuit avant toute intervention. Rien n'est fait sans votre accord. Nous cherchons d'abord la solution qui abîme le moins votre porte et vous proposons seulement ce qui est nécessaire. On vous répond en français, en anglais et en espagnol. Appartements, maisons, commerces et entreprises.
```

## 5. Services (onglet « Services »)

| Service | Description (300 caractères max) |
|---|---|
| Ouverture de porte | Porte claquée ou fermée à clé, clés à l'intérieur ou perdues. Nous cherchons d'abord la méthode qui abîme le moins. Devis gratuit par téléphone avant intervention. |
| Changement de serrure | Remplacement du cylindre ou de la serrure complète après une perte de clé, un emménagement, une clé cassée ou un cylindre usé. Devis gratuit par téléphone. |
| Sécurisation et blindage | Cylindre haute sécurité, protège-cylindre, serrure multipoints, renforts et blindage de porte. Diagnostic et devis gratuit, rien n'est posé sans votre accord. |
| Après effraction | Mise en sécurité provisoire, remplacement du cylindre ou de la serrure forcés, facture détaillée pour l'assurance. [[7j/7, 24h/24.||Horaires : {DISPO}.]] |
| Changement de serrure de boîte aux lettres | Remplacement de la serrure de boîte aux lettres par un modèle compatible avec l'immeuble. |

Ne remplissez **pas** le champ prix (pour rester cohérent avec le site).

## 6. Attributs (si Google les propose)

- Langues : français, anglais, espagnol
[[- Service d'urgence / Ouvert 24h/24
||]]
## 7. Photos

- **Logo** : `public/img/logo-512.png`
- **Couverture** : `public/img/og-image.jpg`
- Ensuite, ajoutez de **vraies photos** : véhicule, outillage, une porte que vous avez réparée (avec l'accord du client et sans adresse visible). Google valorise les photos authentiques. N'utilisez jamais de photos de banque d'images présentées comme « notre équipe ».

## 8. Premiers posts (onglet « Ajouter une actualité »)

**Post 1**
```
Porte claquée, clé perdue, serrure bloquée ? Clé en Main Genève intervient [[7j/7, 24h/24||{DISPO_LONG}]] à Genève et sur La Côte. Devis gratuit par téléphone avant intervention. On vous répond en FR, EN, ES.
```
Bouton : **Appeler**

**Post 2**
```
Vous venez d'emménager ? Vous ne savez pas combien de clés de votre logement circulent. Changer le cylindre vous assure d'être les seuls à pouvoir ouvrir. Pensez à prévenir votre régie. Devis gratuit par téléphone.
```
Bouton : **Appeler**

## 9. Après la vérification

- Activez les **messages** (en option, seulement si vous pouvez y répondre rapidement).
- Demandez un avis aux **vrais clients** après une intervention réussie, avec le lien « Demander des avis » de la fiche. N'achetez jamais d'avis et ne les rédigez pas vous-même : c'est interdit et Google supprime les fiches concernées.
- Répondez à chaque avis, positif ou négatif, poliment.
