# -*- coding: utf-8 -*-
"""
RECOLORER UN THÈME WAKFU — script du thème [Retro] (version 4.0)
=================================================================

Ce script prend les images officielles d'un thème Wakfu (dossier « images » du
modèle officiel d'Ankama) et produit une copie recolorée, sans changer :
  - la taille des images (aucun redimensionnement, aucun recadrage) ;
  - la transparence (le canal alpha est recopié tel quel) ;
  - la qualité (sortie en PNG, format sans perte).

PRINCIPE
--------
Pour chaque pixel, on mesure sa teinte, sa saturation et sa luminosité, puis on
le range dans une catégorie (gris / bleu nuit, turquoise, rose, autre).
Chaque catégorie a une PALETTE : un dégradé qui associe une luminosité (0 = noir,
1 = blanc) à une nouvelle couleur. Un pixel sombre prend donc la couleur
« sombre » de la palette, un pixel clair la couleur « claire » : les reliefs,
ombres et textures sont conservés, seule la teinte change.

INSTALLATION (Windows)
----------------------
1. Installer Python 3 depuis https://www.python.org (cocher « Add Python to PATH »).
2. Ouvrir l'invite de commandes et taper :
       pip install pillow numpy scipy

UTILISATION
-----------
Recolorer tout un dossier d'images :
    python recolorer_theme.py  "C:\\chemin\\theme_officiel\\images"  "C:\\chemin\\sortie\\images"

Tester sur une seule image :
    python recolorer_theme.py  --fichier  "...\\textures\\NP-window-1.png"  "test.png"

Le dossier de sortie ne contient QUE les images modifiées ; le jeu utilise ses
images par défaut pour tout le reste. Placez ensuite ce dossier « images » dans
   themes\\theme_Retro-Wakfu\\theme\\images
puis en jeu : « Recharger le thème » (et relancer le jeu si des images ne se
mettent pas à jour).

POUR MODIFIER LE RENDU
----------------------
Tout se règle dans la partie « RÉGLAGES » juste en dessous :
  - les PALETTES (couleurs) ;
  - les LISTES DE FICHIERS (quels fichiers suivent quelle règle).
Les noms de fichiers acceptent le joker * (ex. "Header*" = tous les fichiers
qui commencent par Header).
"""

import os
import sys
import fnmatch

import numpy as np
from PIL import Image
from scipy import ndimage


# ============================================================================
#  RÉGLAGES — PALETTES
# ============================================================================
# Une palette = une liste de (luminosité, couleur).
# La luminosité va de 0.0 (pixel noir dans l'original) à 1.0 (pixel blanc).
# Entre deux points, la couleur est calculée en dégradé.
# Exemple : (0.0, "#2a251d") veut dire « les pixels noirs deviennent #2a251d ».

PALETTES = {
    # Grands fonds sombres (fenêtres, panneaux) -> brun chaud
    "FOND": [(0.0, "#2a251d"), (0.10, "#3e3628"), (0.22, "#4a4236"), (1.0, "#4a4236")],

    # Traits clairs posés SUR un fond (bordures, ornements) -> beige / taupe
    "TRAITS_SUR_FOND": [(0.0, "#4a4236"), (0.22, "#5a5040"), (0.6, "#a39a7c"), (1.0, "#d5cfaa")],

    # Petits détails gris (icônes, traits, contours isolés) -> dégradé brun → crème
    "DETAILS": [(0.0, "#14110c"), (0.20, "#3a3328"), (0.40, "#6b6250"),
                (0.60, "#a39a7c"), (0.80, "#d5cfaa"), (1.0, "#f6f1dc")],

    # Turquoise / bleu saturé (sélections, lueurs) -> orange Retro
    "TURQUOISE_VERS_ORANGE": [(0.0, "#2e1a04"), (0.25, "#784b01"), (0.50, "#d97a1e"),
                              (0.75, "#f5a94f"), (1.0, "#ffe3b8")],

    # En-têtes de fenêtre (turquoise à l'origine) -> brun foncé
    "ENTETES": [(0.0, "#1c1913"), (0.25, "#2a251d"), (0.45, "#332d23"), (0.7, "#4a4236"), (1.0, "#6b6250")],

    # Infobulles, popups, chat -> noir chaud Retro
    "NOIR_CHAUD": [(0.0, "#141210"), (0.3, "#211d16"), (0.6, "#3a3428"), (1.0, "#524a3c")],

    # Boutons principaux (« Valider »), dorés à l'origine -> orange Retro
    "BOUTON_ORANGE": [(0.0, "#5e2a00"), (0.5, "#9a4000"), (0.7, "#c4560f"), (0.85, "#d9631a"), (1.0, "#ee7a22")],

    # Contours de sélection (crème / doré à l'origine) -> orange vif
    "SELECTION": [(0.0, "#7a3000"), (0.5, "#e0600a"), (0.8, "#ff8a2a"), (1.0, "#ffc080")],
}

# Couleur unique qui remplace le rose / magenta (survols) — en gardant la luminosité
ROSE_VERS = "#ff6600"


# ============================================================================
#  RÉGLAGES — QUELS FICHIERS SUIVENT QUELLE RÈGLE
# ============================================================================
# Ces listes s'appliquent au dossier images/textures (sauf mention contraire).

# Fichiers laissés EXACTEMENT comme l'original (couleurs qui ont un sens :
# Dofus, raretés, jauges Wakfu/Stasis/XP, alliés/ennemis, illustrations…)
GARDER_ORIGINAL = [
    "Dofus-*", "StatSlots*", "statSlot*", "Tooltip-Borders-*", "NeoMap*", "DungeonStasis*",
    "ornateFrame*White*", "Ally-*", "Enemy-*", "PSGradient*", "PWGradient*", "Stasis*", "WakfuBarGlow*",
    "NP-Green-100*", "NP-Red-100*", "NP-ItemRarity*", "NP-AllyBackground*", "NP-EnemyBackground*",
    "Notif*", "heartGauge*", "PreviewBase*", "NP-White-*", "OnboardingBackground*",
    "NP-VelocityBar*", "VelocityGauge*", "Tex-Indicator*", "NP-XPBar*", "HudXpBar*",
    # boutons et onglets secondaires : déjà bruns à l'origine, texte clair lisible
    "NP-SecondaryLargeButton*", "NP-SecondaryMediumButton*", "SecondarySmallButton*", "SecondaryXSButton*",
    "SecondaryFloatingButton*", "NP-ToggleSecondary*", "NP-Tab*",
]

# En-têtes de fenêtre -> palette ENTETES
ENTETES = ["Header*", "Tex-Bar-*", "DialogueTitle*"]

# Panneaux en dégradé (gris -> turquoise) : une seule règle pour tout le panneau
PANNEAUX_DEGRADE = ["DialogueMain*"]

# Fonds en noir chaud (infobulles, popups, aide, chat) -> palette NOIR_CHAUD
NOIR_CHAUD = ["TooltipBG-*", "PopupBackground*", "NP-window-Medium*",
              "NP-Gray-50*", "ChatBackground*", "ChatBottomBackground*", "ChatTab*", "ChatTextEditor*"]

# Boutons principaux (4 états empilés : normal / survol / appuyé / désactivé)
BOUTONS_PRINCIPAUX = ["NP-PrimaryLargeButton*", "NP-PrimaryMediumButton*", "PrimarySmallButton*"]

# Éléments dont le contour crème/doré (état sélectionné ou actif) passe en orange
CONTOUR_SELECTION = ["Tooltip-Borders-Selector*", "TextEditor*", "ChatTextEditor*", "NP-SearchBar-*", "Companion-Circle*"]

# Images à la racine de images/ qui sont traitées (les autres = illustrations, logos…)
RACINE_A_TRAITER = ["theme*", "selectedTheme*", "iconesMru*", "passeport*", "ladder_donjon_empty*",
                    "filterBackground*", "mapButtons*", "minimap_options*", "landMarkFilter9*",
                    "socle_reward*", "havreSacDecor*", "informations*", "parcho*"]

# Dossier images/pictos : True = recolorer, False = garder les pictos d'origine
TRAITER_PICTOS = False


# ============================================================================
#  RÉGLAGES AVANCÉS — DÉTECTION
# ============================================================================
SEUIL_SOMBRE = 0.22        # en dessous de cette luminosité, un gris est « sombre »
TAILLE_MIN_FOND = 11       # un fond = zone sombre où tient un carré de 11 x 11 pixels
TEINTE_BLEUE = (160, 265)  # plage de teinte (en degrés) considérée comme bleu / turquoise
TEINTE_ROSE = (285, 345)   # plage de teinte considérée comme rose / magenta
SATURATION_GRIS = 0.15     # en dessous : le pixel est considéré comme gris
SATURATION_VIVE = 0.35     # au-dessus (dans les bleus) : turquoise vif ; en dessous : bleu nuit grisé


# ============================================================================
#  OUTILS
# ============================================================================
def hex_vers_rgb(code):
    """'#a1b2c3' -> tableau [161, 178, 195]"""
    code = code.lstrip("#")
    return np.array([int(code[i:i + 2], 16) for i in (0, 2, 4)], float)


def palette_vers_table(points):
    """Transforme une palette en table de 256 couleurs (une par niveau de luminosité)."""
    xs = np.array([p[0] for p in points])
    couleurs = np.array([hex_vers_rgb(p[1]) for p in points])
    t = np.linspace(0, 1, 256)
    return np.stack([np.interp(t, xs, couleurs[:, k]) for k in range(3)], 1)


TABLES = {nom: palette_vers_table(pts) for nom, pts in PALETTES.items()}


def correspond(nom_fichier, motifs):
    return any(fnmatch.fnmatch(nom_fichier, m) for m in motifs)


def teinte_saturation_valeur(rgb):
    """Calcule teinte (0-360°), saturation (0-1) et valeur (0-1) pour chaque pixel."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx = rgb.max(-1); mn = rgb.min(-1); d = mx - mn
    h = np.zeros_like(mx); m = d > 1e-6
    rr = m & (mx == r); gg = m & (mx == g) & ~rr; bb = m & ~rr & ~gg
    h[rr] = ((g - b)[rr] / d[rr]) % 6
    h[gg] = (b - r)[gg] / d[gg] + 2
    h[bb] = (r - g)[bb] / d[bb] + 4
    s = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0)
    return h * 60, s, mx


def analyser(a):
    """Classe chaque pixel de l'image (tableau RGBA) en catégories."""
    rgb = a[..., :3] / 255.0
    alpha = a[..., 3]
    h, s, v = teinte_saturation_valeur(rgb)
    lum = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]   # luminosité perçue
    visible = alpha > 0
    bleuté = (h >= TEINTE_BLEUE[0]) & (h <= TEINTE_BLEUE[1])
    rose = (h >= TEINTE_ROSE[0]) & (h <= TEINTE_ROSE[1]) & (s > SATURATION_VIVE) & visible
    turquoise = bleuté & (s >= SATURATION_VIVE) & visible
    gris = visible & ~turquoise & ~rose & ((s < SATURATION_GRIS) | (bleuté & (s < SATURATION_VIVE)))
    indice = np.clip((lum * 255).round().astype(int), 0, 255)   # position dans les tables
    return dict(alpha=alpha, v=v, lum=lum, rose=rose, turquoise=turquoise, gris=gris, indice=indice)


def appliquer(sortie, masque, table, indice):
    """Remplace la couleur des pixels du masque par la table, selon leur luminosité."""
    sortie[..., :3][masque] = table[indice][masque]


# ============================================================================
#  RÈGLES DE RECOLORATION
# ============================================================================
def regle_generale(a, entete=False):
    """Règle par défaut : fonds, traits, détails, turquoise, rose."""
    p = analyser(a)
    sombre = p["gris"] & (p["lum"] < SEUIL_SOMBRE)
    # 1) Fonds = grandes zones sombres (on garde ce qui peut contenir un carré de TAILLE_MIN_FOND)
    k = TAILLE_MIN_FOND if min(a.shape[:2]) >= 24 else max(3, min(a.shape[:2]) // 3)
    graines = ndimage.binary_opening(sombre & (p["alpha"] >= 20), structure=np.ones((k, k), bool))
    fond = ndimage.binary_propagation(graines, mask=sombre)        # étendu aux bords et aux fondus
    # 2) Traits clairs juste au contact d'un fond
    traits = ndimage.binary_dilation(fond, iterations=3) & p["gris"] & ~fond & (p["lum"] >= SEUIL_SOMBRE)
    # 3) Tout le reste du gris = petits détails
    details = p["gris"] & ~fond & ~traits
    sortie = a.copy()
    appliquer(sortie, fond, TABLES["FOND"], p["indice"])
    appliquer(sortie, traits, TABLES["TRAITS_SUR_FOND"], p["indice"])
    appliquer(sortie, details, TABLES["DETAILS"], p["indice"])
    appliquer(sortie, p["turquoise"], TABLES["ENTETES" if entete else "TURQUOISE_VERS_ORANGE"], p["indice"])
    sortie[..., :3][p["rose"]] = (hex_vers_rgb(ROSE_VERS) * p["v"][..., None])[p["rose"]]
    return sortie


def regle_panneau_degrade(a):
    """Panneau dont le fond passe du gris au turquoise : une seule règle pour tout."""
    p = analyser(a)
    m = p["gris"] | p["turquoise"]
    sombre = m & (p["lum"] < 0.35)
    sortie = a.copy()
    appliquer(sortie, sombre, TABLES["FOND"], p["indice"])
    appliquer(sortie, m & ~sombre, TABLES["TRAITS_SUR_FOND"], p["indice"])
    return sortie


def regle_noir_chaud(a):
    """Infobulles, popups, chat : tout le gris/bleu devient noir chaud."""
    p = analyser(a)
    sortie = a.copy()
    appliquer(sortie, p["gris"] | p["turquoise"], TABLES["NOIR_CHAUD"], p["indice"])
    return sortie


def regle_bouton_principal(a):
    """Boutons à 4 états empilés : les 3 premiers en orange, le 4e (désactivé) reste gris."""
    p = analyser(a)
    sortie = regle_generale(a)
    lignes = np.zeros(p["lum"].shape, bool)
    lignes[: (p["lum"].shape[0] * 3) // 4] = True
    m = (p["alpha"] > 0) & lignes & ~p["turquoise"] & ~p["rose"]
    appliquer(sortie, m, TABLES["BOUTON_ORANGE"], p["indice"])
    return sortie


def contour_selection_orange(sortie, a):
    """Les contours crème / dorés (sélection, champ actif) passent en orange."""
    p = analyser(a)
    h, s, v = teinte_saturation_valeur(a[..., :3] / 255.0)
    m = (a[..., 3] > 0) & (h >= 25) & (h <= 60) & (s >= 0.15) & (v >= 0.6)
    appliquer(sortie, m, TABLES["SELECTION"], p["indice"])
    return sortie


def recolorer_image(chemin, nom, dossier_parent):
    """Choisit la règle selon le nom et le dossier, renvoie l'image recolorée (ou None si inchangée)."""
    if dossier_parent == "textures":
        if correspond(nom, GARDER_ORIGINAL) and not correspond(nom, CONTOUR_SELECTION):
            return None
        a = np.asarray(Image.open(chemin).convert("RGBA")).astype(float)
        if correspond(nom, PANNEAUX_DEGRADE):
            sortie = regle_panneau_degrade(a)
        elif correspond(nom, NOIR_CHAUD):
            sortie = regle_noir_chaud(a)
        elif correspond(nom, BOUTONS_PRINCIPAUX):
            sortie = regle_bouton_principal(a)
        else:
            sortie = regle_generale(a, entete=correspond(nom, ENTETES))
        if correspond(nom, CONTOUR_SELECTION):
            sortie = contour_selection_orange(sortie, a)
        return sortie
    if dossier_parent == "pictos":
        if not TRAITER_PICTOS:
            return None
        a = np.asarray(Image.open(chemin).convert("RGBA")).astype(float)
        return regle_generale(a)
    if dossier_parent == ".":
        if not correspond(nom, RACINE_A_TRAITER):
            return None
        a = np.asarray(Image.open(chemin).convert("RGBA")).astype(float)
        return regle_generale(a)
    return None   # autres sous-dossiers (items, achievementCategories, crown…) : inchangés


def enregistrer(tableau, chemin):
    os.makedirs(os.path.dirname(chemin) or ".", exist_ok=True)
    Image.fromarray(tableau.clip(0, 255).astype(np.uint8), "RGBA").save(chemin, optimize=True)


# ============================================================================
#  PROGRAMME PRINCIPAL
# ============================================================================
def traiter_dossier(source, destination):
    modifiees = inchangees = 0
    for racine, _, fichiers in os.walk(source):
        rel = os.path.relpath(racine, source)
        parent = rel.split(os.sep)[0]
        for nom in sorted(fichiers):
            if not nom.lower().endswith((".png", ".tga")):
                continue
            resultat = recolorer_image(os.path.join(racine, nom), nom, parent)
            if resultat is None:
                inchangees += 1
                continue
            enregistrer(resultat, os.path.join(destination, rel, os.path.splitext(nom)[0] + ".png"))
            modifiees += 1
    print(f"Images recolorées : {modifiees}   |   laissées d'origine : {inchangees}")


def traiter_un_fichier(source, destination):
    nom = os.path.basename(source)
    parent = os.path.basename(os.path.dirname(source))
    if parent not in ("textures", "pictos"):
        parent = "."
    resultat = recolorer_image(source, nom, parent)
    if resultat is None:
        print("Ce fichier est dans une liste « garder l'original » : rien à faire.")
        return
    enregistrer(resultat, destination)
    print("Image recolorée :", destination)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--fichier":
        traiter_un_fichier(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        traiter_dossier(sys.argv[1], sys.argv[2])
    else:
        print(__doc__)
