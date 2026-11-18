"""Outils de teinte (conversion RGB <-> HLS vectorisée) utilisés par transfert_qualite.py."""
import numpy as np,sys
from PIL import Image
def rgb2hls(c):
    mx=c.max(-1);mn=c.min(-1);L=(mx+mn)/2;d=mx-mn
    S=np.where(d==0,0,np.where(L<0.5,d/(mx+mn+1e-9),d/(2-mx-mn+1e-9)))
    r,g,b=c[...,0],c[...,1],c[...,2]
    h=np.where(mx==r,((g-b)/(d+1e-9))%6,np.where(mx==g,(b-r)/(d+1e-9)+2,(r-g)/(d+1e-9)+4))/6
    return np.where(d==0,0,h),L,S
def hls2rgb(h,L,S):
    q=np.where(L<0.5,L*(1+S),L+S-L*S);p=2*L-q
    def f(t):
        t=t%1
        return np.where(t<1/6,p+(q-p)*6*t,np.where(t<1/2,q,np.where(t<2/3,p+(q-p)*(2/3-t)*6,p)))
    return np.stack([f(h+1/3),f(h),f(h-1/3)],-1)
def warm(src,dst,hue=27,sat=1.0,lmul=1.0):
    a=np.array(Image.open(src).convert('RGBA')).astype(float)
    h,L,S=rgb2hls(a[...,:3]/255)
    out=hls2rgb(np.full_like(h,hue/360),np.clip(L*lmul,0,1),np.clip(S*sat,0,1))
    a[...,:3]=out*255
    Image.fromarray(a.round().astype(np.uint8)).save(dst)
if __name__=='__main__':
    warm(sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]))
