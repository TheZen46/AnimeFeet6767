"""Ricalcolo degli esempi dei moduli di Geometria (sympy).

Uso: python3 verifica.py
"""
import sympy as sp
from sympy import I, sqrt, pi, Matrix, Rational as R, symbols, simplify, eye

errori = 0


def ok(nome, valore, atteso):
    global errori
    if isinstance(valore, sp.MatrixBase) and isinstance(atteso, sp.MatrixBase):
        giusto = valore.shape == atteso.shape and sp.simplify(valore - atteso).is_zero_matrix
    elif isinstance(valore, (bool, list, tuple, dict, set, sp.MatrixBase)):
        giusto = valore == atteso
    else:
        giusto = sp.simplify(sp.sympify(valore) - sp.sympify(atteso)) == 0
    print(("OK     " if giusto else "ERRORE ") + nome, valore, "atteso", atteso)
    if not giusto:
        errori += 1


# ---------- Modulo 1: numeri complessi, polinomi, geometria analitica ----------
z1, z2 = 2 + 3*I, 1 - 4*I
ok("M1 somma", sp.expand(z1 + z2), 3 - I)
ok("M1 prodotto", sp.expand(z1 * z2), 14 - 5*I)
ok("M1 quoziente", sp.simplify((1 - I) / (2 + I)), R(1, 5) - R(3, 5)*I)
ok("M1 modulo sqrt3+i", sp.Abs(sqrt(3) + I), 2)
ok("M1 argomento sqrt3+i", sp.arg(sqrt(3) + I), pi/6)
ok("M1 (2+2i)^100", sp.expand((2 + 2*I)**100), -2**150)
w = [2**R(1, 3) * sp.exp(I*(pi/4 + k*pi/3)) for k in range(6)]
ok("M1 radici seste di -4i", all(sp.simplify(sp.expand_complex(x**6) + 4*I) == 0 for x in w), True)
x = symbols('x')
P = x**5 - 2*x**4 + 2*x**3 - 2*x**2 + 4*x - 4
ok("M1 P(1+i)", sp.expand(P.subs(x, 1 + I)), 0)
ok("M1 fattorizzazione", sp.expand((x**2 - 2*x + 2)*(x**3 - 2) - P), 0)
ok("M1 radici quadrate 3+4i", sp.expand((2 + I)**2), 3 + 4*I)
ok("M1 i^2025", I**2025, I)
ok("M1 radici cubiche unita", sp.expand(((-1 + sqrt(3)*I)/2)**3), 1)
# vettori
v, vp = Matrix([2, -2, 1]), Matrix([0, 1, -1])
ok("M1 cos angolo", v.dot(vp) / (v.norm()*vp.norm()), -1/sqrt(2))
a, b = Matrix([1, 1, 1]), Matrix([2, 1, 1])
c = a.cross(b)
ok("M1 prodotto vettoriale", c, Matrix([0, 1, -1]))
ok("M1 vettori di norma 2", (sqrt(2)*c).norm(), 2)
A, B = Matrix([1, 0, 2]), Matrix([3, 1, 0])
t = symbols('t', real=True)
C = Matrix([0, 0, t])
area = (B - A).cross(C - A).norm() / 2
sol = sp.solve(sp.Eq(area**2, 100), t)
ok("M1 vertice sull'asse z", sorted(sol), sorted([(14 - sqrt(1991))/5, (14 + sqrt(1991))/5]))
print("   C = (0, 0, t) con t in", sol, [sp.N(s, 4) for s in sol])
v1, v2 = Matrix([-2, -7, -4]), Matrix([-1, -1, 2])
ok("M1 normale piano", v1.cross(v2), Matrix([-18, 8, -5]))
X, Y, Zs = symbols('x y z')
lam, mu = 2, 3
pf = sp.expand(lam*(X + Y + Zs - 3) + mu*(X - Y - Zs - 2))
ok("M1 fascio", pf, 5*X - Y - Zs - 12)
ok("M1 fascio parallelo a (1,2,3)", 5*1 - 2 - 3, 0)
# distanza punto-piano e sfera
ok("M1 distanza punto-piano", sp.Abs(2*1 - 1*1 + 2*3 - 1) / 3, 2)
sfera = X**2 + Y**2 + Zs**2 - 2*X + 4*Y - 6*Zs + 5
ok("M1 sfera centro raggio", sp.expand((X - 1)**2 + (Y + 2)**2 + (Zs - 3)**2 - 9 - sfera), 0)
# distanza del centro dal piano x + 2y + 2z = 7 e raggio della circonferenza
dC = sp.Abs(1 - 4 + 6 - 7) / 3
ok("M1 distanza centro-piano", dC, R(4, 3))
ok("M1 raggio circonferenza", sqrt(9 - dC**2), sqrt(65)/3)
# rette sghembe: r: (1,0,0)+t(1,1,0), s: (0,1,1)+u(0,1,1)? distanza
P0, d1 = Matrix([1, 0, 0]), Matrix([1, 1, 0])
Q0, d2 = Matrix([0, 0, 3]), Matrix([0, 1, 1])
n = d1.cross(d2)
ok("M1 sghembe: non parallele", n != Matrix([0, 0, 0]), True)
dist = sp.Abs((Q0 - P0).dot(n)) / n.norm()
ok("M1 distanza sghembe", dist, 2/sqrt(3))

# ---------- Modulo 2: matrici, sistemi, determinanti ----------
A2 = Matrix([[3, -1], [-5, 2]])
ok("M2 inversa 2x2", A2.inv(), Matrix([[2, 1], [5, 3]]))
ok("M2 non invertibile", Matrix([[1, 2], [-1, -2]]).det(), 0)
A3 = Matrix([[0, 1, -1], [1, 3, 2], [1, -4, 1]])
ok("M2 det A3", A3.det(), 8)
ok("M2 con 4 al posto di -4 e singolare", Matrix([[0, 1, -1], [1, 3, 2], [1, 4, 1]]).det(), 0)
print("   inversa A3:", A3.inv(), "det", A3.det())
ok("M2 inversa 3x3", A3 * A3.inv(), eye(3))
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
sis = [x3 + x4 - 1, 2*x1 + 2*x2 + x3 - 5*x4 - 5, 3*x1 + 3*x2 - x3, x1 + x2 - x4 - 1]
s = sp.solve(sis, [x1, x3, x4], dict=True)
ok("M2 sistema", s, [{x1: R(1, 2) - x2, x3: R(3, 2), x4: R(-1, 2)}])
M4 = Matrix([[0, 1, 2, 4], [-1, 1, 2, 0], [3, 1, 0, 4], [0, 1, 1, 1]])
ok("M2 det 4x4", M4.det(), -6)
Ac = Matrix([[-1, 2, 3], [0, 0, 1], [1, 1, 4]])
ok("M2 det cofattori", Ac.det(), 3)
ok("M2 inversa cofattori", Ac.inv(), Matrix([[-1, -5, 2], [1, -7, 1], [0, 3, 0]]) / 3)
Mr = Matrix([[1, 2, 0, -1], [0, 1, 1, -1], [1, 1, -1, 0], [1, 0, -2, 1]])
ok("M2 rango 2", Mr.rank(), 2)
Acr = Matrix([[2, 0, -1], [1, 1, -1], [1, 2, 1]])
bcr = Matrix([1, 2, 5])
ok("M2 det Cramer", Acr.det(), 5)
solc = Acr.LUsolve(bcr)
print("   Cramer:", solc.T)
ok("M2 Cramer x1", Matrix.hstack(bcr, Acr[:, 1], Acr[:, 2]).det() / 5, solc[0])
l = symbols('lambda')
Aug = Matrix([[1, l, 1], [1, 2, l - 1], [2, l**2, l]])
ok("M2 det completa", sp.factor(Aug.det()), sp.factor(-(l + 1)*(l - 2)**2))
for val in (-1, 2, 0):
    Al = Matrix([[1, l], [1, 2], [2, l**2]]).subs(l, val)
    print("   lambda =", val, "rk A =", Al.rank(), "rk (A|b) =", Aug.subs(l, val).rank())
# non commutativita e divisori dello zero
P1, P2 = Matrix([[1, 1], [0, 1]]), Matrix([[1, 0], [1, 1]])
ok("M2 AB != BA", P1*P2 != P2*P1, True)
N1, N2 = Matrix([[1, -1], [-1, 1]]), Matrix([[1, 1], [1, 1]])
ok("M2 divisori dello zero", N1*N2, Matrix([[0, 0], [0, 0]]))

# ---------- Modulo 3: spazi vettoriali e applicazioni lineari ----------
a_, b_, c_ = symbols('a b c')
ss = sp.solve([a_ + 2*b_ + c_, a_ + b_ + 2*c_], [a_, b_], dict=True)
ok("M3 combinazioni nulle", ss, [{a_: -3*c_, b_: c_}])
Bm = Matrix([[1, -1, 0], [0, 1, 1], [1, 1, 1]])
ok("M3 base R3 det", Bm.det(), -1)
coord = Bm.LUsolve(Matrix([1, 1, -1]))
print("   coordinate di u:", coord.T)
ok("M3 coordinate", Bm * coord, Matrix([1, 1, -1]))
ok("M3 base R1[x]", Matrix([[2, 3], [1, 2]]).det(), 1)
W1 = Matrix([[1, 1, 2], [1, 0, 1], [0, 0, 0], [1, 0, -1]])
W2 = Matrix([[1, 1], [1, 2], [1, 1], [4, 2]])
ok("M3 dim W1", W1.rank(), 3)
ok("M3 dim W2", W2.rank(), 2)
ok("M3 dim W1+W2", Matrix.hstack(W1, W2).rank(), 4)
ns = Matrix.hstack(W1, -W2).nullspace()
inter = [W1 * v[:3, :] for v in ns]
print("   W1 ∩ W2 generato da", [list(v.T) for v in inter])
ok("M3 Grassmann", 3 + 2 - Matrix.hstack(W1, W2).rank(), len(ns))
Af = Matrix([[1, -2], [2, -4], [0, 1]])
ok("M3 rango f", Af.rank(), 2)
ok("M3 nucleo f", Af.nullspace(), [])
Al = Matrix([[1, l, 0], [0, 1, l], [l, 0, 1]])
ok("M3 det phi", sp.expand(Al.det()), 1 + l**3)
ok("M3 phi2 inversa", Al.subs(l, 2).LUsolve(Matrix([1, 1, 1])), Matrix([R(1, 3)]*3))
ok("M3 phi(-1) nucleo", Al.subs(l, -1).nullspace()[0].T, Matrix([[1, 1, 1]]))
# cambio di base in R1[x]: coordinate di 1 + x rispetto a {2 + x, 3 + 2x}
ok("M3 coordinate polinomio", Matrix([[2, 3], [1, 2]]).LUsolve(Matrix([1, 1])), Matrix([-1, 1]))
# derivata su R2[x] nella base 1, x, x^2
D = Matrix([[0, 1, 0], [0, 0, 2], [0, 0, 0]])
ok("M3 rango derivata", D.rank(), 2)

# ---------- Modulo 4: autovalori, diagonalizzazione, teorema spettrale ----------
Ad = Matrix([[2, 1, -1], [0, 2, 1], [0, 0, 1]])
lt = symbols('t')
ok("M4 polinomio caratteristico", sp.factor((Ad - lt*eye(3)).det()), sp.factor(-(lt - 2)**2*(lt - 1)))
ok("M4 molteplicita geometrica di 2", 3 - (Ad - 2*eye(3)).rank(), 1)
ok("M4 non diagonalizzabile", Ad.is_diagonalizable(), False)
Ad2 = Matrix([[2, 0, 0], [1, 1, 0], [1, 0, 1]])
Pd, Dd = Ad2.diagonalize()
print("   diagonalizzabile:", Dd, Pd)
ok("M4 diagonalizzazione", Pd.inv()*Ad2*Pd, Dd)
S = Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
ok("M4 autovalori simmetrica", S.eigenvals(), {2: 1, -1: 2})
Q = Matrix([[1/sqrt(3), 1/sqrt(2), 1/sqrt(6)], [1/sqrt(3), -1/sqrt(2), 1/sqrt(6)], [1/sqrt(3), 0, -2/sqrt(6)]])
ok("M4 Q ortogonale", sp.simplify(Q.T*Q), eye(3))
ok("M4 Q^T S Q", sp.simplify(Q.T*S*Q), sp.diag(2, -1, -1))
ok("M4 det Q = 1", sp.simplify(Q.det()), 1)
# Gram-Schmidt
u1, u2, u3 = Matrix([1, 1, 0]), Matrix([1, 0, 1]), Matrix([0, 1, 1])
e1 = u1 / u1.norm()
w2 = u2 - u2.dot(e1)*e1
e2 = w2 / w2.norm()
w3 = u3 - u3.dot(e1)*e1 - u3.dot(e2)*e2
e3 = w3 / w3.norm()
ok("M4 GS e2", sp.simplify(e2 - Matrix([1, -1, 2])/sqrt(6)), Matrix([0, 0, 0]))
ok("M4 GS e3", sp.simplify(e3 - Matrix([-1, 1, 1])/sqrt(3)), Matrix([0, 0, 0]))
# Fibonacci
F = Matrix([[1, 1], [1, 0]])
ok("M4 F^10", (F**10)[0, 1], 55)
phi1, phi2 = (1 + sqrt(5))/2, (1 - sqrt(5))/2
ok("M4 Binet n=10", sp.simplify((phi1**10 - phi2**10)/sqrt(5)), 55)
ok("M4 autovalori Fibonacci", set(F.eigenvals().keys()), {phi1, phi2})
th = symbols('theta', real=True)
Rt = Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
ok("M4 polinomio rotazione", sp.expand(sp.simplify((Rt - lt*eye(2)).det())), lt**2 - 2*sp.cos(th)*lt + 1)
# forma quadratica / prodotto scalare definito positivo
G = Matrix([[2, 1], [1, 2]])
ok("M4 definita positiva", all(ev > 0 for ev in G.eigenvals()), True)
print("\nErrori:", errori)
