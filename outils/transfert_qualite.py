"""
Recolore une image SANS perte de qualité.

Le dessin (relief, dégradés, grain, bords doux) vient d'une image lisse (original du jeu,
ou EvaUnit-01), et les couleurs viennent d'une image déjà recolorée de même taille.
La forme et la transparence de l'image recolorée sont conservées.

Usage :
    python transfert_qualite.py  image_lisse.png  image_recoloree.png  sortie.png
"""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from teintes import rgb2hls, hls2rgb
from PIL import Image
from scipy import ndimage as nd
def transfert(src,guide,dst,s_teinte=0.7,s_ton=2.5):
    e=np.array(Image.open(src).convert('RGBA')).astype(float)/255
    u=np.array(Image.open(guide).convert('RGBA')).astype(float)/255
    lab,n=nd.label((e[...,3]>0)|(u[...,3]>0),np.ones((3,3)))
    o=e.copy()
    eLr=rgb2hls(e[...,:3])[1]; uLr=rgb2hls(u[...,:3])[1]
    for i,sl in enumerate(nd.find_objects(lab),1):
        if sl is None: continue
        y0,y1=max(sl[0].start-6,0),sl[0].stop+6; x0,x1=max(sl[1].start-6,0),sl[1].stop+6
        S=(slice(y0,y1),slice(x0,x1)); comp=(lab[S]==i)
        w=u[S][...,3]*comp
        if w.sum()<1: continue
        def nc(v,s):
            return nd.gaussian_filter(v*w,s)/np.maximum(nd.gaussian_filter(w,s),1e-6)
        ur=np.stack([nc(u[S][...,c],s_teinte) for c in range(3)],-1)
        uh,_,uS=rgb2hls(np.clip(ur,0,1))
        _,eL,_=rgb2hls(e[S][...,:3])
        dL=nc(uLr[S]-eLr[S],s_ton)
        dLf=nc(uLr[S]-eLr[S],0.5)
        gS=rgb2hls(np.clip(u[S][...,:3],0,1))[2]
        k=np.clip((gS-0.25)/0.25,0,1)
        dL=dL*(1-k)+dLf*k
        rgb=hls2rgb(uh,np.clip(eL+dL,0,1),uS)
        blk=o[S]; blk[...,:3][comp]=rgb[comp]
    o[...,3]=u[...,3]  # forme et transparence de la version Retro (bords déjà propres)
    Image.fromarray((np.clip(o,0,1)*255).round().astype(np.uint8)).save(dst)
if __name__=='__main__': transfert(*sys.argv[1:4])
