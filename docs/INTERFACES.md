# Les familles d'interfaces de Wakfu

> Classement établi en jeu par Naofel. Chaque famille est dessinée par des fichiers différents
> et se travaille à part.

## 1. Interfaces récentes (refonte) — ✅ homogènes

Fiche personnage, inventaire, aptitudes, carnet de bord (quêtes, exploits), donjons (classement),
ensembles de cosmétiques, répertoire, encyclopédie, croupiers, hôtel de vente, options, zaap,
échanges, coffres du havre-sac, récompenses de la boutique, écran de connexion (en partie).

- **Signe distinctif :** une **en-tête** (barre de titre brune).
- **Dessinées par :** le dossier `images/textures/` (`NP-window-*`, `Header*`, `NP-Tab`, boutons `NP-*`…).
- **Couleurs :** toutes répondent aux mêmes identifiants de `colors.xml`. Facile à modifier.

## 2. Interfaces anciennes (pas encore refaites par Ankama) — 🚧 à homogénéiser

Guilde, métiers, artisanat, héros et compagnons, champs de bataille, politique (nation, gouverneur),
passeport, attitudes et smileys, boutique, écosystème, climat.

- **Signe distinctif :** un **titre blanc sans en-tête**.
- **Dessinées par :** les **planches** de la racine de `images/`
  (`themeDefault*`, `themeSimple*`, `themeOver*`, `themePressed*`, `themeDisabled*`, `selectedTheme*`).
  Le dessin vient du design de Ymoka (Nightflow), repris dans la version lisse d'EvaUnit-01 (Dranathilus).
- **Couleurs :** en général les mêmes identifiants, mais chaque interface a ses particularités.
- **En cours :** fond des fenêtres, fonds intérieurs et socles faits ; le reste avance morceau par morceau.

## 3. Guide

Un peu à part, proche de la famille 2. Son cadre et son fond viennent de la case **E4** de `themeSimple3`.

## 4. Entrée des donjons

À part : cadre illustré, panneau d'options, jauge de Stasis (dans `themeSimple3`).

## 5. Carte du monde

À part : garde le format de **plateau** (cadre en relief), avec des éléments de la famille 1
(boutons Pions / Filtres, légende).

---

# Cartographie des textures (diagnostics en jeu)

Résultats des tests « couleur flash » : chaque fichier de `images/textures/` a été rempli d'une couleur
vive pour voir où il apparaît. ⚠️ = fichier partagé par plusieurs écrans, à modifier avec prudence.

| Fichier | Où il apparaît | État dans le thème |
|---|---|---|
| `OnboardingBackground` (572×884) | Panneau de sélection des personnages, uniquement | Beige `#d7d1ad` |
| `NP-window-Medium` ⚠️ | Boutons retour et paramètres et encadré Booster (connexion), infobulles des aptitudes, menu des canaux du chat, bandeau et barre Pions / Filtres de la carte, légende de la carte, menu « Trier par », fenêtre « Copier vers un autre build » | Brun `#555142` (doit rester foncé : texte blanc) |
| `NP-window-DarkSmall` ⚠️ | Fond des grandes fenêtres : menu Échap, inventaire, zaaps… | Beige `#d7d1ad` |
| `NP-minus1` ⚠️ | Fond intérieur de presque toutes les interfaces récentes : aptitudes, sorts, équipements, options, donjons, recherche, barre de kamas, « Emplacement libre », cases de « Copier vers un autre build » | Noir 25 % (d'origine) |
| `NP-minus2` ⚠️ | Blocs d'en-tête : filtres de recherche (Niveau, Rareté…), carte du donjon, liste et cases des raccourcis | Blanc 5 % et bordure (d'origine) |
| `NP-minus3`, `NP-minus4` | Non trouvés | D'origine |
| `ornateFrame1` à `4` | Cadres en filigrane autour des blocs (sorts actifs, passifs, mécanique, équipement, angle des fenêtres de confirmation) | Beige foncé `#8c8368` à ~35 % |
| `ornateFrame5` | Idem | D'origine (choix) |
| `Tooltip-Gradient` | Lueur en haut à gauche des infobulles d'objet | D'origine |
| `TooltipBG-Default` | Infobulle d'objet **ouverte ou épinglée** (avec ses boutons œil et fermer) | Beige-taupe, gardé (lisible) |
| `TooltipBG-Over` | Infobulle **de survol** (objets, sorts) | Beige-taupe, gardé (lisible) |
| `TooltipBG-Heroes`, `NP-ToolTip-1` | Non trouvés | — |
| `Fighter-Gradient` | Dégradé en combat | D'origine |
| `LeftGradient`, `NP-White-*`, `NP-Listelement-Button-1` | Rien de visible lors des tests | D'origine |
| `DialogueMain`, `DialogueTitle`, `DialogueOrnament` | Dialogues avec les PNJ | Dessin Wakfu en teintes chaudes (noir chaud, bandeau orange brûlé) |

**Non modifiable :** le survol des lignes de personnages (écran de connexion) n'est ni une image ni une
couleur de `colors.xml`. Le moteur éclaircit lui-même la ligne, presque invisible sur le beige.

## Famille 2 : morceaux de planches identifiés

### Comment ces planches fonctionnent

- Les planches de la racine de `images/` sont de grandes images (1024 ou 2048 px) découpées en
  centaines de morceaux. Le jeu en étire certains (9-patch) pour dessiner des fenêtres entières.
- **Les états partagent les mêmes coordonnées.** Un même morceau existe dans `themeDefault` (repos),
  `themeOver` (survol), `themePressed` (appui ou sélection) et `themeDisabled` (désactivé).
  Pour modifier l'effet de survol d'un bouton, on retouche donc le même endroit dans `themeOver`.
- `selectedTheme*` n'a pas servi pour les éléments testés jusqu'ici (socles de la guilde, etc.).

### Méthode de diagnostic

1. **Quadrillage codé** : chaque case de 1/8 × 1/8 de la planche reçoit une couleur unique et opaque.
   Sur une capture, la couleur mesurée donne la case exacte (A = `themeDefault`, B = `themeDefault2`,
   C = `themeSimple`, D = `themeSimple2`, E = `themeSimple3`, numéros 1 à 64 ligne par ligne).
2. **Remettre une planche à la fois** : on laisse les planches de test en place et on remet
   une seule planche d'origine. Ce qui reprend sa couleur normale vient de celle-là.
3. **Suspects colorés** : quand il reste quelques candidats, chacun reçoit une couleur différente.

### Morceaux identifiés

| Planche | Morceau | Rôle | État |
|---|---|---|---|
| `themeSimple2` | petit carré brun à liseré clair (x 1002-1025, y 14-36) | **Fond de toutes les fenêtres de la famille 2** (boutique, guilde, métiers, climat, politique, havre-mondes, émoticônes, champs de bataille…), étiré par le jeu | Beige clair `#d7d1ad`, liseré crème `#f2ead0` |
| `themeSimple2` | D57/D58, grand carré (x 46-498, y 1709-2032) | Fonds intérieurs et zones de titre : guilde (améliorations, havre-monde), politique, boutique (détail d'article), gestion de la zone, attitudes | Beige plus sombre `#b4ac8d` |
| `themeDefault` / `themeOver` / `themePressed` | socle losange (x 190-270, y 80-150) | Socles des menus latéraux (guilde, politique, écosystème…) : repos / survol / sélection | Repos d'origine ; survol : flanc orange ; sélection : plateau clair et halo orange |
| `themeDefault` | A61, A62, A23 | Boutons de catégories (boutique, guide), bouton « Découvrir » | À traiter |
| `themeDefault` | A2, A3, A10 | Bouton « Quitter la guilde », filtres (« Tout type »), socles au repos | À traiter |
| `themeSimple` | C57 / C64 | Cases d'article de la boutique (repos / survol) | À traiter |
| `themeSimple` | **C11** ⚠️ | Panneau intérieur de la boutique **et** bulles de chat **et** infobulles des croupiers | Doit rester foncé (texte blanc) |
| `themeSimple` | C4 | Infobulle des zaaps | À traiter |
| `themeSimple` | C1 | Bandeau de la guilde, panneau du groupe, ascenseurs | À traiter |
| `themeSimple` | C41 | Cadres des héros (gestion du groupe) | À traiter |
| `themeSimple3` | E4 | Cadre et fond du guide | À traiter |
| `themeDefault2`…`themeDisabled2` | cartes en pierre avec l'œil | Cartes de sélection (héros / défis) | Brun, lueur orange |

**Pas dans les planches :** les émoticônes, le climat et le passeport (`passeport.png`, à part).

---

# Qualité des images

Les anciennes passes de recoloration travaillaient par seuils et avaient **pixelisé** une grande
partie des images (aplats, bords crénelés, gravures tracées en pixels). Toutes les images ont été
refaites à partir de sources lisses, en gardant les couleurs choisies :

| Dossier | Source du dessin |
|---|---|
| `textures/` | originaux du jeu (`gui.jar`) |
| Planches (`theme*`, `selectedTheme*`) | **EvaUnit-01** (Dranathilus), même disposition que Nightflow, sans pixelisation |
| Planches `2`, `newCharacter` | originaux du jeu (`gui.jar`) |
| `pictos/`, `itemsRarityBorders/`, `dungeonGameplay/` | EvaUnit-01 (déjà propres, non retouchés) |

**Méthode (`outils/transfert_qualite.py`)** : pour chaque pixel, le **dessin** (relief, dégradés,
grain, bords doux) vient de la source lisse, et la **couleur** (teinte, saturation, clarté) vient de
l'ancienne version du thème au même endroit. La forme et la transparence du thème sont conservées.

> ⚠️ **Règle à respecter désormais :** ne plus recolorer par seuils. Toute retouche se fait par
> décalage de clarté (relief conservé) ou par rotation de teinte, à partir d'une image lisse.
