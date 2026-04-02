
import matplotlib.pyplot as plt
def plot_truss(nodes,els,disp=None,scale=1):
    for a,b in els:
        plt.plot([nodes[a][0],nodes[b][0]],[nodes[a][1],nodes[b][1]])
    if disp is not None:
        dn=[]
        for i,(x,y) in enumerate(nodes):
            dn.append((x+disp[2*i]*scale,y+disp[2*i+1]*scale))
        for a,b in els:
            plt.plot([dn[a][0],dn[b][0]],[dn[a][1],dn[b][1]],'--')
    plt.axis('equal'); plt.grid(); plt.show()
