from itertools import product
N=lambda x:1-x
ok=True
def jk_next(q,j,k): return (j&N(q))|(N(k)&q)
def check_machine(nome, nvar, ninp, nxt, eqD=None, eqJK=None, used=None):
    """nxt(state_tuple, inp_tuple) -> next tuple or None (dc)"""
    global ok
    for s in product([0,1],repeat=nvar):
        for i in product([0,1],repeat=ninp):
            t=nxt(s,i)
            if t is None: continue
            if eqD:
                got=tuple(f(*s,*i) for f in eqD)
                if got!=t: print("ERR D",nome,s,i,t,got); ok=False
            if eqJK:
                got=tuple(jk_next(s[b], eqJK[b][0](*s,*i), eqJK[b][1](*s,*i)) for b in range(nvar))
                if got!=t: print("ERR JK",nome,s,i,t,got); ok=False
    print("verificato", nome)
# luci: stati XYZ a000 b001 c010 d011 e100 f101
seq={(0,0,0):(0,0,1),(0,0,1):(0,1,0),(0,1,0):(0,1,1),(0,1,1):(1,0,0),(1,0,0):(1,0,1),(1,0,1):(0,0,0)}
check_machine("luci",3,0,lambda s,i: seq.get(s),
  eqD=[lambda X,Y,Z: X&N(Z)|Y&Z, lambda X,Y,Z: Y&N(Z)|N(X)&N(Y)&Z, lambda X,Y,Z: N(Z)],
  eqJK=[(lambda X,Y,Z: Y&Z, lambda X,Y,Z: Z),(lambda X,Y,Z: N(X)&Z, lambda X,Y,Z: Z),(lambda X,Y,Z:1, lambda X,Y,Z:1)])
outs={(0,0,0):(0,0,0),(0,0,1):(1,0,0),(0,1,0):(1,1,0),(0,1,1):(1,1,1),(1,0,0):(0,1,1),(1,0,1):(0,0,1)}
for s,o in outs.items():
    X,Y,Z=s
    assert (Y|N(X)&Z, Y|X&N(Z), X|Y&Z)==o, s
print("uscite luci ok")
# stati non usati luci
for s in [(1,1,0),(1,1,1)]:
    X,Y,Z=s; print("luci da",s,"->",(X&N(Z)|Y&Z, Y&N(Z)|N(X)&N(Y)&Z, N(Z)))
# Es9: stati XY a00 b01 c10, ingresso IN
def es9(s,i):
    X,Y=s; IN,=i
    if s==(0,0): return (0,1) if IN else (0,0)
    if s==(0,1): return (1,0) if IN else (0,0)
    if s==(1,0): return (1,0)
    return None
check_machine("es9",2,1,es9, eqD=[lambda X,Y,IN: X|IN&Y, lambda X,Y,IN: IN&N(X)&N(Y)],
  eqJK=[(lambda X,Y,IN: IN&Y, lambda X,Y,IN: 0),(lambda X,Y,IN: IN&N(X), lambda X,Y,IN: 1)])
# JX sbagliato degli appunti
try_ok=all(jk_next(s[0], i[0]&N(s[0]), 0)==es9(s,i)[0] for s in [(0,0),(0,1),(1,0)] for i in [(0,),(1,)])
print("JX = IN·X' corretto?", try_ok)
# ENB/SEL: a00, b01 HLT, c10 GO
def es10(s,i):
    X,Y=s; ENB,SEL=i
    if s==(0,0): return ((1,0) if SEL else (0,1)) if ENB else (0,0)
    if s==(0,1): return (0,1) if ENB else (0,0)
    if s==(1,0): return (1,0) if ENB else (0,0)
    return None
check_machine("enb/sel",2,2,es10, eqD=[lambda X,Y,E,S: E&(X|S&N(Y)), lambda X,Y,E,S: E&(Y|N(S)&N(X))])
# L10 analisi: contatore con reset sincrono R
def l10(s,i):
    X1,X0=s; R,=i
    if R: return (0,0)
    n=(2*X1+X0+1)%4; return (n>>1,n&1)
check_machine("L10",2,1,l10, eqD=[lambda X1,X0,R: N(R)&(X0^X1), lambda X1,X0,R: N(R)&N(X0)])
# lavatrice: XYZ wait000 LL001 L1010 L2011 L3100 stop101
def lav(s,i):
    START,L=i
    m={(0,0,1):(0,1,0),(0,1,0):(0,1,1),(0,1,1):(1,0,0),(1,0,0):(1,0,1),(1,0,1):(1,0,1)}
    if s==(0,0,0):
        if not START: return (0,0,0)
        return (0,0,1) if L else (0,1,0)
    return m.get(s)
check_machine("lavatrice JK",3,2,lav, eqJK=[
  (lambda X,Y,Z,S,L: Y&Z, lambda X,Y,Z,S,L: 0),
  (lambda X,Y,Z,S,L: N(X)&Z | N(X)&S&N(L), lambda X,Y,Z,S,L: Z),
  (lambda X,Y,Z,S,L: X|Y|S&L, lambda X,Y,Z,S,L: N(X))])
check_machine("lavatrice JY appunti",3,2,lav, eqJK=[
  (lambda X,Y,Z,S,L: Y&Z, lambda X,Y,Z,S,L: 0),
  (lambda X,Y,Z,S,L: N(X)&Z | S&N(L)&N(X)&N(Z), lambda X,Y,Z,S,L: Z),
  (lambda X,Y,Z,S,L: X|Y|S&L, lambda X,Y,Z,S,L: N(X))])
louts={(0,0,0):(0,0,0),(0,0,1):(1,0,0),(0,1,0):(1,0,0),(0,1,1):(0,1,0),(1,0,0):(0,0,1),(1,0,1):(0,0,0)}
for s,o in louts.items():
    X,Y,Z=s; assert (Y&N(Z)|N(X)&N(Y)&Z, Y&Z, X&N(Z))==o, s
print("uscite lavatrice ok")
# rilevatore di fronti Mealy: X+ = IN, OUT = IN xor X
print("TUTTO OK" if ok else "ERRORI")
