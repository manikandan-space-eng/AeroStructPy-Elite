
import numpy as np
def solve_truss(nodes,elements,E,A,forces,fixed):
    dof=2*len(nodes); K=np.zeros((dof,dof))
    for n1,n2 in elements:
        x1,y1=nodes[n1]; x2,y2=nodes[n2]
        L=((x2-x1)**2+(y2-y1)**2)**0.5
        c=(x2-x1)/L; s=(y2-y1)/L
        k=(E*A/L)*np.array([[c*c,c*s,-c*c,-c*s],[c*s,s*s,-c*s,-s*s],
                            [-c*c,-c*s,c*c,c*s],[-c*s,-s*s,c*s,s*s]])
        m=[2*n1,2*n1+1,2*n2,2*n2+1]
        for i in range(4):
            for j in range(4):
                K[m[i],m[j]]+=k[i,j]
    F=np.array(forces)
    for d in fixed:
        K[d,:]=0;K[:,d]=0;K[d,d]=1;F[d]=0
    return np.linalg.solve(K,F)
