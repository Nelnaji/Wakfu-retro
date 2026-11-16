# 🟫 [Retro] — un thème Wakfu aux couleurs de Dofus Retro

> L'âme de **Dofus Retro**, la modernité de **Wakfu**.

**[Retro]** est un thème d'interface pour **WAKFU** qui fusionne deux univers :
la palette chaleureuse et la lisibilité de Dofus Retro (parchemin, bruns, orange vif),
et la finition moderne de Wakfu (relief, ornements, textures, pictos détaillés).

Ce n'est **pas une copie** de Dofus Retro : les formes, la disposition et les polices de
Wakfu sont conservées. Seules les **couleurs** et les **images** de l'interface changent,
comme le permet le système de thèmes officiel d'Ankama.

<p align="center">
  <img src="docs/images/reference-dofus-retro-inventaire.png" alt="Interface de Dofus Retro : l'inventaire" width="720">
  <br>
  <em>La référence : l'interface de Dofus Retro (inventaire). Parchemin, panneaux bruns, orange vif.</em>
</p>

<!-- Image à venir : la fenêtre des aptitudes avec le thème [Retro]
<p align="center">
  <img src="docs/images/retro-aptitudes.png" alt="La fenêtre des aptitudes avec le thème [Retro]" width="720">
  <br>
  <em>Le résultat dans Wakfu : la fenêtre des aptitudes.</em>
</p>
-->

---

## ✨ Ce que le thème change

| Élément                                      | Dans [Retro]                                                                  |
| -------------------------------------------- | ----------------------------------------------------------------------------- |
| 💬 **Chat**                                  | Fond parchemin clair, couleurs des canaux inspirées de Retro (version pastel) |
| 🗨️ **Bulles de dialogue**                    | Texte foncé, contour aux couleurs du canal (privé, guilde…)                   |
| 🎯 **Sélection**                             | Contours orange façon Retro                                                   |
| 🔘 **Boutons principaux**                    | Orange Retro                                                                  |
| 📊 **Jauges Wakfu / Stasis / XP**            | Couleurs d'origine conservées                                                 |
| 🪟 **Fenêtres, onglets, champs, infobulles** | 🚧 En cours : passage progressif en thème clair, écran par écran              |

---

## 💬 Les couleurs du chat

Wakfu dessine un **contour sombre** autour des lettres du chat. Ce n'est pas un hasard : le
chat peut devenir transparent, et le texte doit rester lisible sur n'importe quelle partie
de la carte. Les couleurs de Retro ont donc été **éclaircies** là où c'était nécessaire, pour
ressortir avec ce contour aussi bien sur le fond parchemin que sur la carte. Certaines
(informations, erreurs, Discussion Ankama) gardent leur couleur Retro d'origine.

Ces couleurs servent aussi au **contour des bulles de dialogue**.

| Canal               | Identifiant                    | Couleur                                | Inspiration Retro            |
| ------------------- | ------------------------------ | -------------------------------------- | ---------------------------- |
| Général (proximité) | `vicinityChannelColor`         | `#d6d6d6` gris clair                   | le texte général             |
| Privé               | `privateChannelColor`          | `#0066ff` bleu vif                     | bleu vif                     |
| Groupe              | `partyChannelColor`            | `#53c6ff` bleu ciel                    | bleu du groupe               |
| Guilde              | `guildChannelColor`            | `#a655f8` violet                       | violet                       |
| Commerce            | `tradeChannelColor`            | `#e06e10` orange brûlé                 | brun du commerce             |
| Communauté          | `frCommunityChannelColor`…     | une couleur par langue (voir plus bas) | —                            |
| Recrutement         | `frRecruitmentChannelColor`…   | la couleur de la langue, en plus pâle  | gris                         |
| Politique / nation  | `politicChannelColor`          | `#ffc400` jaune d'or                   | orange de l'alignement       |
| Zone PvP            | `battlegroundChannelColor`     | `#ff3c00` rouge-orangé                 | orange de l'alignement       |
| Discussion Ankama   | `intergameChannelColor`        | `#a3005a` framboise                    | framboise des « rencontres » |
| Informations        | `informationChannelColor`      | `#009900` vert Retro                   | vert                         |
| Combat              | `fightInformationChannelColor` | `#009900` vert Retro                   | vert                         |
| Erreurs             | `errorChannelColor`            | `#bd0000` rouge Retro                  | rouge des alertes            |

**Une couleur par communauté.** Les canaux _Communauté_ et _Recrutement_ existent dans
chaque langue. Chaque langue a sa propre teinte : franche pour la Communauté, et la même
en plus pâle pour le Recrutement. On reconnaît ainsi la langue d'un message d'un coup d'œil.

| Langue | Teinte | Communauté            | Recrutement            |
| ------ | ------ | --------------------- | ---------------------- |
| 🇫🇷 FR  | bleu   | `#679bfd` bleu clair  | `#bacff8` bleu pâle    |
| 🇬🇧 EN  | violet | `#936ef8` violet-bleu | `#c8b5fc` lavande pâle |
| 🇪🇸 ES  | rouge  | `#fc7e7e` corail      | `#ffc0c0` rose pâle    |
| 🇵🇹 PT  | vert   | `#d0ff78` vert-jaune  | `#e9ffbf` vert pâle    |

---

## 🛠️ Comment le thème est fabriqué

### Les images : un outil de recoloration

L'interface de Wakfu compte plus de 600 images. Elles ne sont pas redessinées à la main :
elles sont **recolorées automatiquement** par un script Python
([`outils/recolorer_theme.py`](outils/recolorer_theme.py)), à partir du modèle de thème officiel d'Ankama.

Le principe :

- chaque pixel est classé selon sa teinte, sa saturation et sa luminosité (gris, bleu nuit, turquoise, rose…) ;
- chaque catégorie suit une **palette** : un dégradé qui associe une luminosité d'origine à une nouvelle couleur ;
- comme la correspondance se fait par luminosité, **les reliefs, ombres et textures de Wakfu sont conservés**, seule la teinte change ;
- **la taille et la transparence ne sont jamais modifiées**, et les images sont enregistrées en PNG, sans perte ;
- les grands aplats (fonds de fenêtres) sont distingués des petits détails (icônes, traits), pour que chacun reçoive la bonne couleur ;
- certaines images restent d'origine : Dofus, raretés, jauges, couleurs alliés/ennemis, illustrations.

Toutes les couleurs et les règles se règlent en haut du script, dans la partie **RÉGLAGES**.

```bash
pip install pillow numpy scipy
python outils/recolorer_theme.py  chemin/vers/theme_officiel/images  sortie/images
```

### Les couleurs de texte : `colors.xml`

Les couleurs de texte, des listes et du chat se règlent dans `theme/colors/colors.xml`.
Un **thème de diagnostic** (une couleur vive différente par identifiant) a permis de
vérifier en jeu à quoi sert chaque couleur importante :

| Identifiant             | Utilisation vérifiée en jeu                                                      |
| ----------------------- | -------------------------------------------------------------------------------- |
| `mainTextLightColor`    | Texte principal : fenêtres, titres des en-têtes, infobulles d'objets, quantités  |
| `secondTextLightColor`  | Titres de section (« Combat », « Jouabilité »), texte secondaire                 |
| `mainTextTitleColor`    | Texte du champ du chat, cases cochées, onglets inactifs, champs de saisie, kamas |
| `defaultLightColor`     | Infobulles d'aide, PV dans le cœur                                               |
| `defaultDarkColor`      | Texte des bulles de dialogue                                                     |
| `mainTextDarkColor`     | Étiquettes claires (rareté, « Actif »)                                           |
| `defaultLightGoldColor` | Jets améliorés dans les infobulles                                               |
| `...ChannelColor`       | Texte du chat **et** contour des bulles (voir plus haut)                         |

> 💡 **Bon à savoir pour les créateurs de thèmes.** Les couleurs des canaux du chat ne sont pas
> présentes dans le `colors.xml` par défaut, mais **le jeu les accepte si on les ajoute**.
> Liste complète des identifiants reconnus par le client :
>
> `vicinityChannelColor` · `privateChannelColor` · `partyChannelColor` · `guildChannelColor` ·
> `tradeChannelColor` · `politicChannelColor` · `battlegroundChannelColor` · `intergameChannelColor` ·
> `informationChannelColor` · `fightInformationChannelColor` · `errorChannelColor` ·
> `frCommunityChannelColor` · `enCommunityChannelColor` · `esCommunityChannelColor` · `ptCommunityChannelColor` ·
> `frRecruitmentChannelColor` · `enRecruitmentChannelColor` · `esRecruitmentChannelColor` · `ptRecruitmentChannelColor`

---

## 📦 Installation

0. Téléchargez la dernière version dans la page **[Releases](../../releases)** : le zip ne contient que le dossier du thème.
1. En jeu : **Options → Interface → Ouvrir le dossier** des thèmes
   (ou, depuis le launcher : _Paramètres du jeu → Répertoire du jeu → Ouvrir le dossier des logs → `themes`_).
2. Copiez le dossier **`theme_Retro-Wakfu`** dans ce dossier `themes`.
3. En jeu : **Actualiser la liste**, choisissez **[Retro]**, puis **Recharger le thème**.
4. Si certaines images ne se mettent pas à jour, **relancez complètement le jeu**.

```
themes/
└── theme_Retro-Wakfu/
    ├── theme.xml
    └── theme/
        ├── colors/colors.xml
        └── images/
            └── textures/ …
```

---

## 🗺️ Avancement

Le thème avance **écran par écran**, une étape testée en jeu à la fois.

- [x] Chat : fond parchemin et couleurs des canaux
- [x] Bulles de dialogue
- [x] Jauges Wakfu / Stasis / XP d'origine
- [ ] Fonds de fenêtres en clair
- [ ] Onglets
- [ ] Champs de saisie
- [ ] Infobulles
- [ ] Fenêtre des aptitudes

---

## 🙏 Crédits

- **[Ankama](https://www.ankama.com)** : WAKFU, Dofus Retro, et le **modèle de thème officiel** qui sert de base au projet. Toutes les images d'origine leur appartiennent.
- **Nightflow**, par **Ymoka et l'équipe WAKFU** : le `colors.xml` de ce thème a servi de point de départ au projet.
- **Ailten et KockaColHa** : leur thème Dofus Retro pour Wakfu (2022) a servi de référence et d'inspiration.
- **Naofel** : création, tests en jeu, direction artistique et couleurs du chat.

---

## 🤖 Utilisation d'IA

**Oui**, l'IA a été utilisée pour ce projet, pour :

- générer divers scripts, dont l'outil de recoloration ;
- modifier les images de l'interface (recoloration).
- l'écriture de cette doc...

La direction artistique, les choix de couleurs et les tests en jeu ont été faits à la main.

---

## ⚖️ Mentions

Projet de fan, **non officiel**, sans lien avec Ankama.
WAKFU, DOFUS et DOFUS Retro sont des marques d'Ankama ; les images d'interface d'origine sont © Ankama.
Ce thème n'utilise que le système de thèmes officiel du jeu et ne modifie aucun fichier du client.
