# 🟫 Wakfu-Retro — Wakfu, style Dofus Retro

> L'âme de **Dofus Retro**, la modernité de **Wakfu**.

**Wakfu-Retro** (affiché **[Retro]** dans les options du jeu) est un thème d'interface pour **WAKFU**
qui fusionne deux univers : la palette chaleureuse et la lisibilité de Dofus Retro (parchemin,
bruns, orange vif), et la finition moderne de Wakfu (relief, ornements, textures, pictos détaillés).

Ce n'est **pas une copie** de Dofus Retro : les formes, la disposition et les polices de
Wakfu sont conservées. Seules les **couleurs** et les **images** de l'interface changent,
comme le permet le système de thèmes officiel d'Ankama.

**Version 4.1** · compatible **Wakfu 1.93** · 🧪 en phase de test

<p align="center">
  <img src="docs/images/reference-dofus-retro-inventaire.png" alt="Interface de Dofus Retro : l'inventaire" width="720">
  <br>
  <em>La référence : l'interface de Dofus Retro (inventaire). Parchemin, panneaux bruns, orange vif.</em>
</p>

<p align="center">
  <img src="docs/images/avancement-fiche-aptitudes.png" alt="Fiche personnage et aptitudes avec le thème Wakfu-Retro" width="900">
  <br>
  <em>Fiche personnage, aptitudes, HUD et chat avec Wakfu-Retro.</em>
</p>

---

## ✨ L'idée

| Élément | Dans Wakfu-Retro |
|---|---|
| 🪟 **Fenêtres** | Fonds parchemin et bruns chauds à la place du gris-bleu |
| 🟧 **Actions et sélection** | **L'orange signale ce qui est actif** : survol des boutons, onglets actifs, éléments sélectionnés, ascenseurs |
| 💬 **Infobulles** | Fond sombre et chaud, texte blanc |
| 💎 **Raretés** | Cadres et étiquettes recolorés, lisibles (y compris pour les daltoniens) |
| 💬 **Chat** | Fond parchemin presque opaque, couleurs des canaux douces pour les yeux |
| 📊 **Jauges Wakfu / Stasis, couleurs d'équipe** | Couleurs d'origine conservées |

---

## 🗺️ Avancement

La majorité des fenêtres principales ont été retravaillées : **tout ce qui est accessible depuis le menu**.

- [x] Chat, bulles de dialogue
- [x] Fiche personnage, aptitudes, HUD
- [x] HDV et inventaire
- [x] Atelier d'enchantement (effets, châsses, sublimations)
- [x] Croupier
- [x] Guilde, compagnons et héros
- [x] Politique, classement JcJ
- [x] Écosystème, climat, gestion de zone
- [x] Guide
- [x] Sélection des personnages, liste des builds
- [x] Boutons d'interaction sur la carte
- [x] Raretés des objets
- [ ] Artisanat, butin, coffres de havre-sac
- [ ] Donjons
- [ ] Dialogues (relecture)

### 🧪 Aidez-moi à tester !

Il m'est impossible de tout tester seul. Si vous tombez sur un écran qui pose problème
(texte illisible, couleur qui jure, élément resté dans les tons d'origine), ouvrez une
**[Issue](../../issues)** en précisant :
- **quel écran** ;
- **comment y accéder** ;
- si possible, une **capture d'écran**.

---

## 🚫 Ce qu'un thème ne peut pas changer

Certaines couleurs sont **inscrites dans le code du jeu**, ou partagées par trop d'écrans
pour être modifiées sans en abîmer d'autres :

- le **contour du texte** dans le chat et dans les titres ;
- l'**effet rouge du niveau inaccessible** (cadenas et chiffre) : le cadenas a été foncé pour rester lisible, mais sa teinte rouge est imposée par le jeu ;
- le **rouge de certains messages sur les objets** (« L'expéditeur ne possède peut-être pas cet objet », « Déjà appris ») ;
- la **teinte orange / bleutée des fiches de combat** (couleur d'équipe appliquée par le jeu) ;
- quelques **couleurs de texte utilisées à divers endroits** : les changer pour un écran les abîmerait ailleurs ;
- les **icônes du jeu** : jetons du croupier, icônes de caractéristiques, bordures néon des sublimations ;
- l'état « modifié » des colonnes de l'atelier d'enchantement s'appuie sur un voile du jeu : il reste plus clair que les autres colonnes.

---

## 📦 Installation

0. Téléchargez la dernière version dans la page **[Releases](../../releases)** : le zip ne contient que le dossier du thème.
1. En jeu : **Options → Interface → Ouvrir le dossier** des thèmes
   (ou, depuis le launcher : *Paramètres du jeu → Répertoire du jeu → Ouvrir le dossier des logs → `themes`*).
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
            ├── textures/ …
            └── pictos/ …
```

---

## 💬 Les couleurs du chat

Wakfu dessine un **contour sombre** autour des lettres du chat, pour que le texte reste
lisible même quand le chat est transparent. Les couleurs des canaux ont donc été choisies
**claires et douces**, pour ressortir avec ce contour sur le fond parchemin comme sur la carte.

Ces couleurs servent aussi au **contour des bulles de dialogue**.

| Canal | Identifiant | Couleur |
|---|---|---|
| Général (proximité) | `vicinityChannelColor` | `#d6d6d6` gris clair |
| Privé | `privateChannelColor` | `#3a88fc` bleu |
| Groupe | `partyChannelColor` | `#53c6ff` bleu ciel |
| Guilde | `guildChannelColor` | `#c082ff` violet clair |
| Commerce | `tradeChannelColor` | `#ff9650` orange doux |
| Politique / nation | `politicChannelColor` | `#fcd450` jaune d'or |
| Zone PvP | `battlegroundChannelColor` | `#ff3c00` rouge-orangé |
| Discussion Ankama | `intergameChannelColor` | `#a3005a` framboise |
| Informations | `informationChannelColor` | `#46cf46` vert |
| Combat | `fightInformationChannelColor` | `#46cf46` vert |
| Erreurs | `errorChannelColor` | `#bd0000` rouge |

**Une couleur par communauté.** Chaque langue a sa teinte : franche pour la *Communauté*,
plus pâle pour le *Recrutement*.

| Langue | Communauté | Recrutement |
|---|---|---|
| 🇫🇷 FR | `#82aeff` bleu clair | `#aab1be` gris-bleu |
| 🇬🇧 EN | `#936ef8` violet-bleu | `#c8b5fc` lavande pâle |
| 🇪🇸 ES | `#fc7e7e` corail | `#ffc0c0` rose pâle |
| 🇵🇹 PT | `#d0ff78` vert-jaune | `#e9ffbf` vert pâle |

---

## 🛠️ Comment le thème est fabriqué

### Les images

L'interface de Wakfu compte plus de 600 images. Elles sont **recolorées à partir des
originales**, sans être redessinées :
- la correspondance se fait par luminosité, donc **les reliefs, ombres et textures de Wakfu sont conservés**, seule la teinte change ;
- **la taille et la transparence ne sont jamais modifiées**, et les images sont enregistrées en PNG, sans perte ;
- chaque écran est vérifié en jeu, et les retouches se font image par image.

Pour retrouver quelle image dessine quel élément, des **thèmes de diagnostic** donnent une
couleur unique à chaque texture, picto, case des planches ou état de bouton : une capture
d'écran suffit alors à identifier le bon fichier.

Un premier outil de recoloration automatique est disponible dans
[`outils/recolorer_theme.py`](outils/recolorer_theme.py) :

```bash
pip install pillow numpy scipy
python outils/recolorer_theme.py  chemin/vers/theme_officiel/images  sortie/images
```

### Les couleurs de texte : `colors.xml`

Les couleurs de texte, des listes et du chat se règlent dans `theme/colors/colors.xml`.
Un **diagnostic des couleurs** (une couleur vive différente par identifiant) a permis de
vérifier en jeu à quoi sert chacune. Elles sont commentées dans le fichier :
`[vérifié]` trouvée en jeu, `[observé]` constatée, `[non trouvée]` cherchée sans succès.

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

## 🙏 Crédits

- **[Ankama](https://www.ankama.com)** : WAKFU, Dofus Retro, et le **modèle de thème officiel** qui sert de base au projet. Toutes les images d'origine leur appartiennent.
- **Nightflow**, par **Ymoka et l'équipe WAKFU** : le `colors.xml` de ce thème a servi de point de départ au projet.
- **Shukrute**, par **Mikkoku** : source d'inspiration.
- **Ailten et KockaColHa** : leur thème Dofus Retro pour Wakfu (2022) a servi de référence et d'inspiration.
- **Naofel** : création, tests en jeu, direction artistique et couleurs.
- Merci à la guilde pour les tests !

---

## 🤖 Utilisation d'IA

**Oui**, l'IA a été utilisée pour ce projet, pour :
- générer divers scripts, dont l'outil de recoloration et les thèmes de diagnostic ;
- modifier les images de l'interface (recoloration).

La direction artistique, les choix de couleurs et les tests en jeu sont faits à la main.

---

## ⚖️ Mentions

Projet de fan, **non officiel**, sans lien avec Ankama.
WAKFU, DOFUS et DOFUS Retro sont des marques d'Ankama ; les images d'interface d'origine sont © Ankama.
Ce thème n'utilise que le système de thèmes officiel du jeu et ne modifie aucun fichier du client.
