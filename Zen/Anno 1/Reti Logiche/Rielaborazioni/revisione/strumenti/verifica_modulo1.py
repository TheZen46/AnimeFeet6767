"""Controllo per tabella di verita' delle sintesi del modulo 1. Uso: python verifica_modulo1.py"""
from itertools import product
ok=True
def chk(nome, f, g, n, dc=lambda *v: False):
    global ok
    for v in product([0,1], repeat=n):
        if dc(*v): continue
        if bool(f(*v)) != bool(g(*v)):
            print("ERRORE", nome, v, f(*v), g(*v)); ok=False; return
    print("ok", nome)
N=lambda x: 1-x
# 1.3 esempi
chk("Y1", lambda A,B,C: N(A)&N(B)&N(C) | N(A)&B&N(C) | A&B&N(C), lambda A,B,C: N(C)&(N(A)|B), 3)
chk("Y2", lambda A,B,C: N(A)&N(B)&N(C) | N(A)&B&N(C) | N(A&B&N(C)), lambda A,B,C: N(A)|N(B)|C, 3)
# consenso
chk("consenso", lambda A,B,C: A&B | N(A)&C | B&C, lambda A,B,C: A&B | N(A)&C, 3)
chk("consenso duale", lambda A,B,C: (A|B)&(N(A)|C)&(B|C), lambda A,B,C: (A|B)&(N(A)|C), 3)
chk("distrib", lambda A,B,C: A|(B&C), lambda A,B,C: (A|B)&(A|C), 3)
# Shannon 2 variabili POS su tutte le 16 funzioni
for k in range(16):
    f=lambda a,b,k=k: (k>>(3-(2*a+b)))&1
    chk("shannon POS f%d"%k, f, lambda a,b,f=f: (a|b|f(0,0))&(a|N(b)|f(0,1))&(N(a)|b|f(1,0))&(N(a)|N(b)|f(1,1)), 2)
# esempio forme
y=lambda A,B,C: int((A,B,C) in [(0,0,0),(0,0,1),(1,0,0),(1,1,0)])
chk("y SOP", y, lambda A,B,C: N(A)&N(B) | A&N(C), 3)
chk("y POS", y, lambda A,B,C: (A|N(B))&(N(A)|N(C)), 3)
# mappe
u=lambda A,B,C: int((A,B,C) in [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(1,0,1)])
chk("U1", u, lambda A,B,C: N(B) | N(A)&N(C), 3)
u=lambda A,B,C: int((A,B,C) in [(0,0,1),(0,1,0),(1,0,0),(1,1,0)])
chk("U2", u, lambda A,B,C: N(A)&N(B)&C | A&N(C) | B&N(C), 3)
u=lambda A,B,C: (A^B)|(B&C)
chk("U3a", u, lambda A,B,C: A&N(B)|N(A)&B|B&C, 3)
chk("U3b", u, lambda A,B,C: A&N(B)|N(A)&B|A&C, 3)
chk("U3pos", u, lambda A,B,C: (A|B)&(N(A)|N(B)|C), 3)
u=lambda A,B,C,D: int((8*A+4*B+2*C+D) in [0,1,2,5,8,9,10])
chk("U4", u, lambda A,B,C,D: N(B)&N(C) | N(B)&N(D) | N(A)&N(C)&D, 4)
chk("parita", lambda x,y,z: N(x^y^z), lambda x,y,z: (x|y|N(z))&(x|N(y)|z)&(N(x)|y|z)&(N(x)|N(y)|N(z)), 3)
# 1.6 indifferenze: righe AC, colonne BD
rows=[(0,0),(0,1),(1,1),(1,0)]; cols=rows
M=[[1,1,1,1],[0,None,0,0],[0,1,0,0],[1,None,0,0]]
tab={}
for i,(a,c) in enumerate(rows):
    for j,(b,d) in enumerate(cols): tab[(a,b,c,d)]=M[i][j]
f=lambda A,B,C,D: tab[(A,B,C,D)] or 0
dc=lambda A,B,C,D: tab[(A,B,C,D)] is None
chk("ind SOP", f, lambda A,B,C,D: N(A)&N(C)|N(B)&N(C)|N(B)&D, 4, dc)
chk("ind POS", f, lambda A,B,C,D: (N(A)|N(B))&(N(C)|D)&(N(B)|N(C)), 4, dc)
# variabili riportate
f=lambda A,B,I: [[1,I],[1,0]][A][B]
chk("VR I", f, lambda A,B,I: N(B)|I&N(A), 3)
def f2(A,B,C,x,y):
    r0={ (0,0):1,(0,1):1,(1,1):y,(1,0):y}; r1={(0,0):1,(0,1):x,(1,1):0,(1,0):0}
    return (r0 if A==0 else r1)[(B,C)]
chk("VR xy", f2, lambda A,B,C,x,y: N(A)&N(B)|N(B)&N(C)|x&N(B)|y&N(A), 5)
# esercizio F
chk("es1", lambda A,B,C,D: A&C&D | N(C)&(N(A)&D | A&(B|D)), lambda A,B,C,D: A&D|N(C)&D|A&B&N(C), 4)
# la forma degli appunti senza AB'C' deve differire (in ABCD = 1100)
F=lambda A,B,C,D: A&C&D | N(C)&(N(A)&D | A&(B|D)); G=lambda A,B,C,D: A&D|N(C)&D
assert F(1,1,0,0)==1 and G(1,1,0,0)==0; print("ok es1: la forma degli appunti sbaglia in 1100")
# esercizio 2 righe X colonne YZ
M={(0,0,0):1,(0,0,1):0,(0,1,1):1,(0,1,0):0,(1,0,0):1,(1,0,1):0,(1,1,1):0,(1,1,0):1}
f=lambda X,Y,Z: M[(X,Y,Z)]
chk("es2 SOP", f, lambda X,Y,Z: N(Y)&N(Z)|X&N(Z)|N(X)&Y&Z, 3)
chk("es2 POS", f, lambda X,Y,Z: (Y|N(Z))&(N(X)|N(Z))&(X|N(Y)|Z), 3)
# NAND
chk("nand sop", lambda A,B,C,D: A&B|C&D, lambda A,B,C,D: N(N(A&B)&N(C&D)), 4)
chk("nor pos", lambda A,B,C,D: (A|B)&(C|D), lambda A,B,C,D: N(N(A|B)|N(C|D)), 4)
print("TUTTO OK" if ok else "CI SONO ERRORI")
