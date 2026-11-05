"""Verifica degli esercizi aggiunti nell'ampliamento di novembre 2026 (moduli 1-4)."""
import sympy as sp

a, h, k, t, s, x, y, z = sp.symbols("a h k t s x y z")
M = sp.Matrix
ok = 0


def eq(u, v, nome):
    global ok
    assert sp.simplify(u - v) == 0, (nome, u, v)
    ok += 1


# ---- modulo 1
w = 1 - sp.sqrt(3) * sp.I
eq(sp.Abs(w), 2, "modulo"); eq(sp.arg(w), -sp.pi / 3, "arg"); eq(sp.expand(w**6), 64, "w^6")
for kk in range(3):
    r = 2 ** sp.Rational(1, 3) * sp.exp(sp.I * (-sp.pi / 9 + 2 * kk * sp.pi / 3))
    eq(sp.expand(sp.simplify(r**3 - w), complex=True), 0, "radice")
assert set(sp.solve(z**2 - 2 * sp.I * z - 2, z)) == {1 + sp.I, -1 + sp.I}
eq(sp.expand((x**2 - 2 * x + 2) * (x**2 + 2 * x + 2)), x**4 + 4, "x^4+4")
assert all(sp.expand((sp.sqrt(2) * (e1 + e2 * sp.I)) ** 4) == -16 for e1 in (1, -1) for e2 in (1, -1))
R0, d, P = M([0, 1, 2]), M([1, -1, 2]), M([1, 2, 0]); n = d.cross(P - R0)
assert n == M([0, 4, 2]) and (M([0, 2, 1]).dot(P), M([0, 2, 1]).dot(R0)) == (4, 4)
Q, nn = M([1, 2, 3]), M([1, -1, 2]); ss = sp.solve((Q + t * nn).dot(nn) - 1, t)[0]; H = Q + ss * nn
assert ss == -sp.Rational(2, 3) and H == M([sp.Rational(1, 3), sp.Rational(8, 3), sp.Rational(5, 3)])
assert 2 * H - Q == M([-sp.Rational(1, 3), sp.Rational(10, 3), sp.Rational(1, 3)])
C = M([2, -1, 0]); assert abs(C.dot(M([1, 2, 2])) - 3) / 3 == 1
assert C + sp.Rational(1, 3) * M([1, 2, 2]) == M([sp.Rational(7, 3), -sp.Rational(1, 3), sp.Rational(2, 3)])
c = M([1, 1, 0]).cross(M([0, 1, 1])); eq(abs(M([-1, 0, 2]).dot(c)) / c.norm(), 1 / sp.sqrt(3), "sghembe")
A_, B_, C_ = M([1, 0, 1]), M([2, 1, 1]), M([1, 2, 3]); nr = (B_ - A_).cross(C_ - A_)
assert nr == M([2, -2, 2]) and all(v[0] - v[1] + v[2] == 2 for v in (A_, B_, C_)); eq(nr.norm() / 2, sp.sqrt(3), "area")
assert M([1, 1, 1]).cross(M([1, -1, 0])) == M([1, 1, -2])
ok += 8
# ---- modulo 2
A = M([[1, 1, 1], [1, a, 1], [1, 1, a]]); eq(A.det(), (a - 1) ** 2, "det sistema")
sol = A.LUsolve(M([1, a, a**2])); assert sp.simplify(sol - M([-a - 1, 1, a + 1])) == sp.zeros(3, 1)
B = M([[1, h, 0], [0, 1, h], [h, 0, 1]]); eq(B.det(), 1 + h**3, "det h")
assert B.subs(h, 1).inv() == M([[1, -1, 1], [1, 1, -1], [-1, 1, 1]]) / 2
Ck = M([[1, 2, k], [2, 4, 2], [k, 2, 1]]); eq(Ck.det(), -4 * (k - 1) ** 2, "rango"); assert Ck.subs(k, 1).rank() == 1
Bi = M([[1, 0, 0], [2, -1, 0], [3, 0, -1]]); assert Bi**2 == sp.eye(3) and Bi.det() == 1
assert M([[2, 1], [5, 3]]).inv() == M([[3, -1], [-5, 2]])
assert M([[1, 2, 0, 1], [2, 4, 1, 3], [0, 1, 1, 0], [1, 2, 0, 2]]).det() == -1
assert M([[1, 2], [2, 4]]).rank() == 1 and M([[1, 2, 3], [2, 4, 6]]).rank() == 1
ok += 6
# ---- modulo 3
V = [M([1, 0, 1, 0]), M([0, 1, 1, -1])]; W = [M([1, 0, 1, 0]), M([1, 1, 0, 0])]
assert all(v[0] + v[1] - v[2] == 0 and v[1] + v[3] == 0 for v in V)
assert M.hstack(*V, *W).rank() == 3
nv = M([-1, 1, 1, 2]); assert all(nv.dot(v) == 0 for v in V + W) and nv.dot(M([1, 0, 1, 3])) == 6
Af = M([[1, 1, 0], [0, 1, -1], [1, 0, 1]]); PF = M([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
assert PF.inv() * Af == M([[0, 1, -1], [1, 0, 1], [0, 0, 0]]) and Af.nullspace()[0] == M([-1, 1, 1])
assert M([1, 1, 0]).cross(M([1, 0, 1])) == M([1, -1, -1])
Mf = M([[0, 2, 1], [1, 0, 0], [-1, 2, 1]]); assert Mf * PF[:, 0] == M([2, 1, 1]) and Mf * PF[:, 1] == M([1, 1, 0]) and Mf * M([0, 0, 1]) == M([1, 0, 1])
assert Mf * M([0, 1, -2]) == sp.zeros(3, 1) and Mf.rank() == 2
Na = M([[1, 2, 1], [0, a, 1], [1, 2, a]]); eq(Na.det(), a * (a - 1), "nucleo param")
assert Na.subs(a, 0) * M([-2, 1, 0]) == sp.zeros(3, 1)
U = [M([1, 1, 0, 1]), M([0, 1, 1, 0])]; assert all(u[0] - u[1] + u[2] == 0 and u[0] - u[3] == 0 for u in U)
Pp = M([[1, 1], [0, 1]]); assert Pp.inv() * M([[2, 1], [0, 3]]) * Pp == M([[2, 0], [0, 3]])
F4 = M([[1, 0, 1, 2], [0, 1, 1, 1], [1, 1, 2, 3]]); assert F4.rank() == 2
assert F4 * M([-1, -1, 1, 0]) == sp.zeros(3, 1) and F4 * M([-2, -1, 0, 1]) == sp.zeros(3, 1)
ok += 10
# ---- modulo 4
Q2 = M([[5, 2], [2, 2]]); assert set(Q2.eigenvals()) == {1, 6}
assert Q2 * M([-1, 2]) == M([-1, 2]) and Q2 * M([2, 1]) == 6 * M([2, 1])
assert sp.diag(Q2, -6).det() == -36
S3 = M([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
Pq = M.hstack(M([-1, 1, 0]) / sp.sqrt(2), M([-1, -1, 2]) / sp.sqrt(6), M([1, 1, 1]) / sp.sqrt(3))
assert sp.simplify(Pq.T * Pq) == sp.eye(3) and sp.simplify(Pq.T * S3 * Pq) == sp.diag(2, 2, 5)
lam = sp.symbols("lam")
eq(sp.factor(M([[0, -1, 0], [1, 0, 0], [0, 0, 2]]).charpoly(lam).as_expr()), (lam - 2) * (lam**2 + 1), "complessa")
Ck = M([[1, k, 1], [0, 1, 0], [0, 0, 2]]); assert (Ck.subs(k, 0) - sp.eye(3)).rank() == 1 and (Ck.subs(k, 5) - sp.eye(3)).rank() == 2
Abar = M([[1, -2, 1], [-2, 1, 1], [1, 1, 0]]); assert Abar.det() == -6 and Abar[:2, :2].det() == -3
A2 = M([[4, 1], [2, 3]]); Pd = M([[1, 1], [-2, 1]]); assert A2 * Pd == Pd * sp.diag(2, 5)
At = M([[1, t], [t, 1]]); eq(sp.diag(At, -1).det(), -(1 - t**2), "famiglia")
assert At * M([1, 1]) == (1 + t) * M([1, 1]) and At * M([1, -1]) == (1 - t) * M([1, -1])
ok += 8
print("verifica ampliamento Geometria: %d controlli superati" % ok)
