"""Verifica degli esercizi aggiunti nell'ampliamento di novembre 2026 (moduli 1-5).

Usa sympy per limiti, derivate, sviluppi; i conti sugli insiemi sono controllati
numericamente sui primi termini.
"""
from itertools import product
from fractions import Fraction as F
import math
import sympy as sp

x, y, n, k, a, b = sp.symbols("x y n k a b", real=True)
ok = 0


def eq(u, v, nome):
    global ok
    assert sp.simplify(u - v) == 0, (nome, u, v)
    ok += 1


def lim(expr, punto, atteso, nome, dir="+-"):
    global ok
    r = sp.limit(expr, x, punto, dir) if dir != "+-" else sp.limit(expr, x, punto)
    assert r == atteso or sp.simplify(r - atteso) == 0, (nome, r, atteso)
    ok += 1


# ---- modulo 1
imp = lambda p, q: (not p) or q  # noqa: E731
assert all(imp(p and imp(p, q), q) for p, q in product([True, False], repeat=2))
assert not all(imp(q and imp(p, q), p) for p, q in product([True, False], repeat=2))
assert all(sum(2 * i - 1 for i in range(1, m + 1)) == m * m for m in range(1, 50))
assert all((7**m - 1) % 6 == 0 for m in range(30))
assert all(sum(i * i for i in range(1, m + 1)) == m * (m + 1) * (2 * m + 1) // 6 for m in range(1, 60))
assert 40**2 + 40 + 41 == 41**2
A = [F(m - 1, m + 1) for m in range(1, 2000)]
assert min(A) == 0 and max(A) < 1 and 1 - max(A) < F(1, 900)
B = [(-1) ** m * (F(3, m) + F(1, m * m)) for m in range(1, 500)]
assert max(B) == F(7, 4) and min(B) == -4
Ag = [(-1) ** m + F(1, m) for m in range(1, 2000)]
assert max(Ag) == F(3, 2) and min(Ag) > -1 and min(Ag) + 1 < F(1, 1000)
eq(sp.solve(sp.Eq(y, x + sp.sqrt(x**2 + 4)), x)[0], (y**2 - 4) / (2 * y), "inversa")
for yy in [sp.Rational(1, 3), 2, 7]:
    xx = (yy**2 - 4) / (2 * yy)
    eq(xx + sp.sqrt(xx**2 + 4), yy, "inversa verifica")
eq((2 + sp.sqrt(y + 1) - 2) ** 2 - 1, y, "inversa parabola")
eq(sp.solve(sp.Eq(sp.log(x - 1), 1), x)[0], 1 + sp.E, "zero log")
ok += 6

# ---- modulo 2
lim((3 * x + 1) / (x + 2), sp.oo, 3, "def")
assert abs(F(3 * 499 + 1, 501) - 3) < F(1, 100)
lim((x**2 + x * sp.sin(x)) / (3 * x**2 + 1), sp.oo, sp.Rational(1, 3), "seno limitato")
lim((2**x + x**3) / (3**x - x), sp.oo, 0, "gerarchia")
lim(sp.sqrt(x**2 + 3 * x) - x, sp.oo, sp.Rational(3, 2), "razionalizza")
lim((1 + 2 / x) ** x, sp.oo, sp.exp(2), "e^2")
lim((sp.exp(3 * x) - 1) / sp.sin(2 * x), 0, sp.Rational(3, 2), "notevole 1")
lim(sp.log(1 + x**2) / (1 - sp.cos(x)), 0, 2, "notevole 2")
lim(x * (sp.log(x + 1) - sp.log(x)), sp.oo, 1, "notevole 3")
lim(((x + 2) / (x - 1)) ** x, sp.oo, sp.exp(3), "1^inf")
lim(x**x, 0, 1, "0^0", "+")
ap = sp.symbols("ap", positive=True)
assert sp.simplify(sp.limit(sp.sqrt(x**2 + ap * x) - x, x, sp.oo) - ap / 2) == 0
lim(sp.sqrt(x**2 + 2 * x) - x, -sp.oo, sp.oo, "a -inf")
lim(sp.cos(x) ** (1 / x**2), 0, sp.exp(-sp.Rational(1, 2)), "cos")
s = [(m**2 * 2**m + math.factorial(m)) / (3**m + math.factorial(m + 1)) for m in (10, 40, 80)]
assert s[0] > s[1] > s[2] and s[2] < 0.02
ok += 1

# ---- modulo 3
assert set(sp.solve(sp.Eq(1 + a, a**2 - 1), a)) == {2, -1}
sol = sp.solve([sp.Eq(3 * a + b, 6), sp.Eq(4 * a + b, b)], [a, b])
assert sol == {a: 0, b: 6}
lim(sp.sin(x) / sp.Abs(x), 0, 1, "salto+", "+")
lim(sp.sin(x) / sp.Abs(x), 0, -1, "salto-", "-")
lim(sp.exp(1 / x), 0, sp.oo, "seconda specie", "+")
assert math.exp(0) + 0 - 3 < 0 < math.e + 1 - 3 and math.sqrt(math.e) - 2.5 < 0
lim(x**2 / (sp.Abs(x) + 2) - x, sp.oo, -2, "obliquo+")
lim(x**2 / (sp.Abs(x) + 2) + x, -sp.oo, -2, "obliquo-")
for e_, ordn, c in [(sp.sqrt(1 + x) - 1, 1, sp.Rational(1, 2)), (1 - sp.cos(2 * x), 2, 2),
                    (sp.log(1 + x**3), 3, 1), ((sp.exp(x**2) - 1) * sp.sin(x), 3, 1),
                    ((1 - sp.cos(x)) * sp.log(1 + 2 * x), 3, 1)]:
    lim(e_ / x**ordn, 0, c, "ordine")
lim(sp.sqrt(x**4 + x) / x**2, sp.oo, 1, "infinito")
lim(x**3 / (x**2 - 4) - x, sp.oo, 0, "obliquo razionale")
lim(x**3 / (x**2 - 4), 2, sp.oo, "vert", "+")

# ---- modulo 4
d = sp.diff
eq(d(x**2 * sp.exp(-x), x), (2 * x - x**2) * sp.exp(-x), "d1")
eq(d(sp.log(x + sp.sqrt(x**2 + 1)), x), 1 / sp.sqrt(x**2 + 1), "d2")
eq(d(sp.atan(1 / x), x), -1 / (x**2 + 1), "d3")
xp = sp.symbols("xp", positive=True)
eq(d(xp**xp, xp), xp**xp * (sp.log(xp) + 1), "d4")
eq(d(sp.sin(3 * x) ** 2, x), 3 * sp.sin(6 * x), "d5")
assert sp.solve([sp.Eq(a + b, 1), sp.Eq(2 * a, 1)], [a, b]) == {a: sp.Rational(1, 2), b: sp.Rational(1, 2)}
lim(x * sp.Abs(x) / x, 0, 0, "x|x|")
eq(d(sp.log(1 + x**2), x).subs(x, 1), 1, "tangente")
eq(1 / d(x**3 + x + 1, x).subs(x, 1), sp.Rational(1, 4), "inversa 1")
eq(1 / d(sp.exp(x) + x, x).subs(x, 0), sp.Rational(1, 2), "inversa 2")
lim((x - sp.sin(x)) / x**3, 0, sp.Rational(1, 6), "hopital 1")
lim(sp.log(x) / sp.sqrt(x), sp.oo, 0, "hopital 2")
lim(x * sp.log(x), 0, 0, "hopital 3", "+")
eq(d(sp.asin(x), x), 1 / sp.sqrt(1 - x**2), "arcsin")
p5 = x**5 + x - 1
assert p5.subs(x, 0) < 0 < p5.subs(x, 1) and len(sp.real_roots(p5)) == 1
ok += 1

# ---- modulo 5
ser = lambda e_, o: sp.series(e_, x, 0, o).removeO()  # noqa: E731
eq(ser(sp.exp(sp.sin(x)), 4), 1 + x + x**2 / 2, "e^sin")
eq(ser(sp.exp(k * x) - sp.sqrt(1 + 2 * x), 3), (k - 1) * x + (k**2 + 1) / 2 * x**2, "parametro k")
lim((sp.exp(x) - sp.sqrt(1 + 2 * x)) / x**2, 0, 1, "k=1")
assert sp.simplify(sp.limit(((1 + x) ** (a / x) - sp.exp(a)) / x, x, 0) + a * sp.exp(a) / 2) == 0
g = x**2 * sp.log(x)
eq(d(g, x), x * (2 * sp.log(x) + 1), "g'")
eq(d(g, x, 2), 2 * sp.log(x) + 3, "g''")
eq(g.subs(x, sp.exp(-sp.Rational(1, 2))), -1 / (2 * sp.E), "min g")
eq(g.subs(x, sp.exp(-sp.Rational(3, 2))), -3 / (2 * sp.E**3), "flesso g")
lim(d(g, x), 0, 0, "g' in 0", "+")
fe = x * sp.exp(-x)
assert max(fe.subs(x, v) for v in (0, 1, 3)) == sp.exp(-1)
f3 = sp.exp(x) - 1 - x + sp.sin(x) ** 2
eq(d(f3, x, 2).subs(x, 0), 3, "f3''")
eq(ser(sp.log(1 + x**2) - sp.sqrt(1 + x**2), 3), -1 + x**2 / 2, "mclaurin")
lim((x**2 / 2) * (x - sp.sin(x)) / x**5, 0, sp.Rational(1, 12), "ordine 5")
eq(ser(x + sp.sqrt(x**2 + 4), 3), 2 + x + x**2 / 4, "P")
lim((sp.log(1 + sp.sin(x)) - x) / (1 - sp.cos(x)), 0, -1, "limite composto")
fx = x * sp.exp(1 / x)
eq(d(fx, x), sp.exp(1 / x) * (x - 1) / x, "f'")
eq(d(fx, x, 2), sp.exp(1 / x) / x**3, "f''")
lim(fx - x, sp.oo, 1, "obliquo")
lim(fx, 0, 0, "sinistra", "-")
lim(d(fx, x), 0, 0, "f' sinistra", "-")
sa = sp.series(sp.sin(x) - x * sp.cos(a * x), x, 0, 7).removeO()
eq(sa.coeff(x, 3), a**2 / 2 - sp.Rational(1, 6), "coeff 3")
eq(sa.coeff(x, 5).subs(a**2, sp.Rational(1, 3)).subs(a, 1 / sp.sqrt(3)), sp.Rational(1, 270), "coeff 5")
lim(d(sp.log(1 + x), x, 2), 0, -1, "f'' sinistra")
An = [(-1) ** m * F(m, m + 1) for m in range(1, 3000)]
assert max(An) < 1 and min(An) > -1 and 1 - max(An) < F(1, 2000) and min(An) + 1 < F(1, 2000)
ok += 1
print("verifica ampliamento Analisi 1A: %d controlli superati" % ok)
