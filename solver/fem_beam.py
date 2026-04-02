
import numpy as np

def beam_k(E,I,L):
    return (E*I/L**3)*np.array([
    [12,6*L,-12,6*L],
    [6*L,4*L**2,-6*L,2*L**2],
    [-12,-6*L,12,-6*L],
    [6*L,2*L**2,-6*L,4*L**2]])

def assemble(n,E,I,L):
    dof=2*(n+1); K=np.zeros((dof,dof)); Le=L/n
    for i in range(n):
        k=beam_k(E,I,Le); idx=2*i
        K[idx:idx+4,idx:idx+4]+=k
    return K

def solve_beam(E,I,L,n,load):
    K=assemble(n,E,I,L)
    dof=2*(n+1); F=np.zeros(dof)
    F[-2]=-load
    for d in [0,1]:
        K[d,:]=0;K[:,d]=0;K[d,d]=1;F[d]=0
    return np.linalg.solve(K,F)

def compute_stress(u,E,I,L,n,c):
    Le=L/n; s=[]
    for i in range(n):
        th1=u[2*i+1]; th2=u[2*i+3]
        curv=(th2-th1)/Le
        s.append(E*curv*c)
    return np.array(s)
