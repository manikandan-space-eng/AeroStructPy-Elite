
import numpy as np
from solver.fem_beam import solve_beam, compute_stress

def optimize(E,density,yield_s,L,load,n):
    best=None; best_w=1e99
    for I in np.linspace(1e-8,1e-4,30):
        for c in np.linspace(0.001,0.05,30):
            u=solve_beam(E,I,L,n,load)
            s=compute_stress(u,E,I,L,n,c)
            ms=max(abs(s)); fos=yield_s/ms if ms!=0 else 1e9
            if fos>=1:
                vol=L*(I/c); w=density*vol
                if w<best_w:
                    best_w=w; best={"I":I,"c":c,"FoS":fos,"Weight":w}
    return best
