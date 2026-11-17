# Charte de couleurs — thème [Retro]

> Document de référence : les couleurs du thème, leur rôle, et les règles pour les choisir.
> Mis à jour au fil de la cartographie de `colors.xml`.

## 1. Règles

1. **Texte avec contour** (titres, onglets, chat, champs de saisie, texte principal) → couleur **claire**.
   Le contour sombre de Wakfu le rend lisible sur n'importe quel fond.
2. **Texte sans contour** (gouverneur, bulles de dialogue, valeurs de la fiche perso…) → couleur **foncée**, sur fond clair.
3. **Le texte principal (`mainTextLightColor`) est blanc.** Partout où il apparaît, le fond doit être assez foncé (brun, taupe, orange).
4. **États d'un élément cliquable** : même famille de couleur, on joue sur la clarté.
   Normal → base · Survol → plus clair · Appuyé → plus foncé · Désactivé → pâle et grisé.
5. **Orange = action et sélection.** Pas d'orange pour les grands fonds (« pas de la carotte »).
6. **Le bleu du Wakfu reste bleu** (jauge W, univers de la série).

## 1 bis. Les deux systèmes de lignes de liste

- **Interfaces récentes** : `marketTable…` sont des **voiles transparents** (5 %) posés sur le fond. Rendu sur le parchemin de la fiche : ≈ `#a8a388` (paires) / `#9b967c` (impaires).
- **Autres listes** (`evenCell…`, `darkEvenCell…`, `scrollEvenCell…`, `fightReport…`, `craftFee…`) : couleurs **opaques**. On leur donne ces deux mêmes teintes pour que toutes les listes se ressemblent.

## 2. Palette

### Fonds
| Rôle | Code |
|---|---|
| Parchemin (fond de fenêtre clair) | `#d5cfaa` |
| Parchemin clair | `#e2dcbb` |
| Lignes de liste (paires / impaires) | `#c9bf9d` / `#bdb594` |
| Survol de ligne | `#a39a7c` |
| Brun Retro (en-têtes, boutons, onglets) | `#514a3c` |
| Brun foncé (panneaux) | `#3e3628` |
| Noir chaud (infobulles, chat) | `#181612` |

### Accents
| Rôle | Code |
|---|---|
| Orange Retro (bouton, onglet actif) | `#d9631a` |
| Orange brûlé (appuyé) | `#c4560f` |
| Orange vif (barre d'XP) | `#ff6a00` |
| Orange clair (reflet, survol) | `#ffa040` |

### Textes
| Rôle | Code |
|---|---|
| Blanc (texte à contour) | `#ffffff` |
| Crème (texte à contour secondaire) | `#f2ead0` |
| Chocolat (texte long sans contour) | `#4a2c17` |
| Brun foncé (texte sans contour) | `#2e2416` |
| Brun moyen (titres de section) | `#5a4630` |

### Valeurs (sur fond clair)
| Rôle | Code |
|---|---|
| Positif (`characStandardColor`, vérifié : valeurs de la fiche) | `#2f7d12` |
| Négatif | `#b8281e` |
| Feu / Eau / Terre / Air | `#c4570f` / `#1b7fa8` / `#6b8a00` / `#9b3fb5` |

### Couleurs de gameplay : conservées telles quelles
Vie en rouge, PA en bleu, PM en vert, PW, éléments, armure, résistances, raretés…
Ces codes existent depuis des années et les joueurs les connaissent : **on n'y touche pas**
(`HPColor`, `APColor`, `MPColor`, `WPColor`, `SPColor`, `QBColor`, `…LightColor`, `ArmorColor`,
`heartHPColor`, `heartArmorColor`, `levelColor`, `fightResistances…`, `fire/water/earth/airColor`, `…GradientColor`).

**Raretés d'objets** (`old…`, `common…`, `rare…`, `mythic…`, `legendary…`, `relic…`, `souvenir…`, `epic…`, `adminRarityColor`) :
vérifié en jeu, elles colorent le **texte** et les **dégradés transparents** de rareté. **Pour le moment, valeurs d'origine.**
Chantier futur : les assombrir ou les éclaircir, **avec leurs textures** (`itemsRarityBorders/`), et tester ce qui se marie le mieux au thème clair.

**Carte, nations, serveurs et taxes** : couleurs d'origine conservées
(`…TerritoryMapColor`, `friendlyNationColor`, `enemyNationColor`, `territoryNameColor`, `server…`).
**Taxes de mise en vente (HDV)** : `lowTaxColor` / `mediumTaxColor` / `highTaxColor`, vérifiées, **assombries** pour le parchemin : `#2f7d12` / `#b06a00` / `#b8281e`.
`guildPointsColor` (points de guilde, vérifié) : d'origine `#DD6800`, déjà un orange doré.
`gainLaurelLawColor` / `lossLaurelLawColor` : d'origine pour le moment, **peut-être à adapter plus tard**.

**Couleurs génériques et alertes, assombries pour le parchemin** (sens conservé) :
`marketValidSublimationColor` `#1f9e1f` · `warningIconColor` `#c9a000` · `errorColor` `#a81414` · `redInvalidBuildColor` `#b8281e` ·
`redColor` `#b8281e` · `lightRedColor` `#b84040` · `greenColor` `#1f9e1f` · `yellowColor` `#c9a000` · `orangeTransColor` `#c4560fcc` · `yellowScoreColor` `#b08a00`

**Combat (cases, portées, placement, timeline, scores) et couleurs d'équipe** (`fight…`, `team…`, `playerTeamHPColor`, `enemyTeamHPColor`,
`battleground…Score`) : identiques à Dofus Retro, **on n'y touche pas**. Chantier possible plus tard.

## 3. Couleurs cartographiées et consignes

| Identifiant | Où (constaté en jeu) | Consigne | Code prévu |
|---|---|---|---|
| `mainTextLightColor` | texte principal (fenêtres, en-têtes, infobulles d'objets, quantités) | blanc | `#ffffff` |
| `secondTextLightColor` | titres de section, texte secondaire, en-têtes de colonnes (classement donjons), « Niv. » | blanc (texte à contour, testé) | `#ffffff` |
| `mainTextTitleColor` | cases cochées, onglets inactifs, champs de saisie, kamas | crème | `#f2ead0` |
| `defaultLightColor` | infobulles d'aide, PV du cœur | blanc | `#ffffff` |
| `mainTextDarkColor` | petites étiquettes claires (rareté, « Actif ») | brun foncé | — |
| `defaultDarkColor` | bulles de dialogue, texte du gouverneur, en-têtes de colonnes de la guilde | chocolat | `#4a2c17` |
| `defaultBlackColor` | interface du gouverneur, fond d'une barre d'XP | brun foncé (≠ chocolat) | `#2e2416` |
| `whiteColor` | texte au-dessus des havre-sacs, texte du guide, menus | blanc | `#ffffff` |
| `mecanicBlueColor` | sélection des héros, texte de la guilde | blanc | `#ffffff` |
| `mecanicDarkBlueColor` | nom du métier (page métiers), texte des nations / champ de bataille (sans contour) | brun foncé | `#3e2a1a` |
| `secondaryLight` | chiffre et picto d'XP (fiche perso), XP des quêtes | orange (comme l'XP du perso) | `#c4560f` |
| `defaultDisabledColor` | boutons « Appliquer » et « Ajouter un grade » (guilde) | orange | `#c4560f` |
| `loadingTextColor` | texte de chargement avant l'entrée sur le serveur | beige clair | `#e2dcbb` |
| `evenCellColor` | lignes paires : guilde, champ de bataille, métiers | comme la fiche perso | `#a8a388` |
| `oddCellColor` | lignes impaires : guilde, champ de bataille, métiers | comme la fiche perso | `#9b967c` |
| `mouseOverCellColor` | survol de ces lignes | nettement distinct | `#bdb594` |
| `selectedCellColor` | ligne sélectionnée | orange (sélection) | `#c4560f` |
| `pressedLightColor` | élément surligné du menu déroulant (champ de bataille) | orange, comme les autres menus | `#c55913` |
| `marketTableEvenCellColor` | **toutes les listes internes des interfaces récentes** (stats de la fiche, aptitudes, effets des infobulles, HDV…), lignes paires | voile clair d'origine | `#ffffff0d` |
| `marketTableOddCellColor` | idem, lignes impaires | voile sombre d'origine | `#0000000d` |
| `fightReportEvenCellColor` | lignes paires : fin de combat | comme les autres listes (provisoire) | `#a8a388` |
| `fightReportOddCellColor` | lignes impaires : fin de combat | comme les autres listes (provisoire) | `#9b967c` |
| `craftFeeTextEditorBackgroundEvenColor` | champs de prix, lignes paires : frais d'artisanat | comme les autres listes (provisoire) | `#a8a388` |
| `craftFeeTextEditorBackgroundOddColor` | champs de prix, lignes impaires : frais d'artisanat | comme les autres listes (provisoire) | `#9b967c` |
| `lightGreyTransparentColor` · `chalkboardBackgroundColor` · `chalkboardBorderColor` | certains messages (« tableau noir ») | **plus tard** : fond beige, texte noir | — |
| `heroGradientFirstColor` → `heroGradientSecondColor` | dégradé des vignettes de **héros** (haut → bas) | tons chauds : orange → brun | `#e0701a` → `#7a3a10` |
| `companionGradientFirstColor` → `companionGradientSecondColor` | dégradé des vignettes de **compagnons** | tons chauds, distincts des héros : or → bronze | `#e0b84a` → `#7a5a20` |
| `enabledHeroSlotColor` | bas des emplacements où un héros / compagnon peut être ajouté | orange | `#e0701a80` |
| `disabledHeroSlotColor` | bas des emplacements bloqués (pas en mode booster) | orange grisâtre | `#9c8a7a80` |
| `xpColor` | barre d'XP de fin de combat, rang de la compagnie | orange | `#e0701a` |
| `xpColorCompanion` | barre d'XP des compagnons | un orange différent | `#f5a623` |
| `xpPremiumColor` · `ogrestColor` *(non trouvées)* | sans doute anciennes interfaces | orangé, au lieu du bleuté | `#ffa040` · `#c4560f` |
| `wakfuColor` *(non trouvée)* | sans doute la couleur du Wakfu | **garder le bleu** (règle 6) | `#47dbd3` |
| `loadingWheelColor` | roue de chargement avant la connexion | beige clair | `#e2dcbb` |
| `loginGradientColor` *(non trouvée)* | écran de connexion | beige clair | `#e2dcbb` |
| `craftActionProgressBarColor` · `craftBackgroundProgressBarColor` *(non trouvées)* | barre de progression d'artisanat | tons orangés | `#e0701a` · `#5a4030` |
| `protectorColor` | jauges de plantation (écosystème) | garder d'origine | `#62be25` |
| `wakfuBarColor` · `stasisJaugeColor` · `progressBarDefaultColor` *(non trouvées)* | jauges | garder d'origine | `#4C4C4C` · `#FC2DEF` · `#E5E5E5` |
| `webShopOgrineAmountColor` | solde d'Ogrines (boutique) | garder d'origine | `#2fb1be` |
| `webShopNotEnoughOgrinePriceColor` | prix en Ogrines quand le solde est insuffisant | lisible sur fond brun : rouge clair | `#ff7a6a` |
| `webShopNotEnoughOgrinePriceBackgroundColor` | fond de ce prix | brun Retro | `#514a3c` |
| `webShopBackgroundColor` · `webShopHighlightColor` · `webShopMoneyPrice…` · `webShopPriceBackgroundColor` | boutique (€, bannière, prix) | voir proposition, à confirmer | — |
| `listHighlightColor` | élément sélectionné dans **tous les menus déroulants** des interfaces récentes (famille 1) | orange, comme avant | `#e0701a` |
| `darkOddCellColor` | lignes impaires : interface des nations (politique) | comme la fiche perso | `#9b967c` |
| `darkEvenCellColor` | lignes paires : nations (politique), encadré « Trésorerie dilapidée » | comme la fiche perso | `#a8a388` |
| `scrollEvenCellColor` | lignes paires : classement Joueur contre Joueur (passeport) | comme la fiche perso | `#a8a388` |
| `scrollOddCellColor` | lignes impaires : classement Joueur contre Joueur (passeport) | comme la fiche perso | `#9b967c` |
| `passportTitleColor` | titres de l'interface du passeport | brun de titre | `#5a4630` |
| *(inconnu, piste : `wakfuColor`)* | bouton « Accepter » des objectifs de guilde (cyan) | orange foncé | `#c4560f` |
| `blackColor` | libellés du gouverneur ? *(à confirmer)* | — | — |
| `...ChannelColor` | chat et contour des bulles | voir README | — |

### Inutilisées (absentes du code du jeu, preuve par scan)
`greyColor` · `scroolfleshcolor` · `timelineOrangeOverlayColor` · `timelineRedOverlayColor`

### Potentiellement plus utilisées (cherchées en jeu, jamais trouvées — laissées par défaut)
> Testées avec une couleur vive : aucun changement visible, y compris aux endroits suggérés par leur nom.
> Le guide d'Ankama prévient que certaines couleurs ne sont plus utilisées. Utile pour les futurs créateurs de thèmes.
> ⚠️ Le scan montre pourtant que certaines sont lues par le code (ex. `questObjectiveColor` : 13 fichiers). Elles servent peut-être dans des écrans rares.

`neutralStateColor` · `positiveStateColor` · `negativeStateColor` · `mecanicLightBlueColor` ·
`achievementCategoryCompleteColor` · `importantTextColor` · `descriptionPopupColor` · `questObjectiveColor` ·
`informationMessageTitleColor` · `tooltipLinkColor` ·
`darkSelectedCellColor` · `darkMouseOverCellColor` · `scrollSelectedCellColor` · `scrollMouseOverCellColor` ·
`detailedCellColor` · `listFilterColor` ·
`craftFeeDefined…` · `craftFeeInherited…` · `craftFeeNonDefined…` (prix des frais d'artisanat, piste : saisir un prix dans le tableau des frais) ·
`spellDeckHighlightColor` · `dungeonLadderSeparatorColor` · `tooltipBackgroundColor` · `tooltipBorderColor` · `mecanicBlueForHoverColor` · `previewButtonBorderColor` · `legacyCharacStandardColor` (sans doute les anciennes interfaces) · `scrollTitleBackgroundColor` · `scrollTitleBackgroundColorLight` · `dungeonLadderRankingColor` · `dungeonLadderNoRankColor` ·
`tableCellBorderColor` (5 fichiers) · `defaultDarkGreyColor` (22 fichiers : forcément utilisée quelque part) · `fleaEvenCellColor` · `fleaOddCellColor`

### À cartographier en priorité (les plus répandues dans le code)
`disabledTextColor` (158 fichiers) · `lightRedColor` (69) · `defaultDarkGreyColor` (22) · `errorColor` (18) · `black75` (15) · `redColor` (15) · `scrollFleshColor` (14) · `questObjectiveColor` (13)
