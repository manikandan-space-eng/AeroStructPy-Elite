
import matplotlib.pyplot as plt, numpy as np
def plot_stress(s,L):
    x=np.linspace(0,L,len(s))
    sc=plt.scatter(x,s,c=s)
    plt.colorbar(sc); plt.title("Stress Contour")
    plt.xlabel("L"); plt.ylabel("Stress")
    plt.grid(); plt.savefig("stress.png"); plt.show()
