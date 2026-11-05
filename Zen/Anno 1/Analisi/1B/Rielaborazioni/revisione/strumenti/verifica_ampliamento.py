"""Verifica degli esercizi aggiunti nell'ampliamento di novembre 2026 (moduli 1-4)."""
import sympy as sp

x, y, t, a, k = sp.symbols("x y t a k", real=True)
xp = sp.symbols("xp", positive=True)
Y = sp.Function("y")
ok = 0


def eq(u, v, nome):
    global ok
    d = sp.simplify(u - v)
    assert d == 0 or (d.free_symbols == set() and abs(float(d)) < 1e-12), (nome, u, v)
    ok += 1


I = sp.integrate
# ---- modulo 1
eq(I(x**3 * sp.sqrt(x**2 - 3), (x, sp.sqrt(3), 2)), sp.Rational(6, 5), "sostituzione")
eq(I((2 * x + 1) / (x - 1) ** 2, (x, 2, 4)), 2 + 2 * sp.log(3), "fratti")
u = sp.symbols("u")
eq(I(sp.exp(u), (u, 0, sp.sqrt(3))), sp.exp(sp.sqrt(3)) - 1, "tangente")
eq(I(x**2 * sp.atan(x), (x, 0, 1)), sp.pi / 12 - sp.Rational(1, 6) + sp.log(2) / 6, "parti")
eq(I(1 / (1 + xp**2), (xp, 0, sp.oo)), sp.pi / 2, "improprio")
eq(sp.limit(sp.Si(x) / x, x, 0), 1, "funz integrale 0")
eq(sp.limit(sp.Si(x) / x, x, sp.oo), 0, "funz integrale inf")
v = I(-2 * xp**2 / xp**sp.Rational(5, 2), (xp, 0, 3)) + I((-4 * xp - 6) / xp**sp.Rational(5, 2), (xp, 3, sp.oo))
eq(v, -64 / (3 * sp.sqrt(3)), "lezione 6")
for xx in [sp.Rational(1, 2), 2, 5]:
    assert abs(xx**2 - 2 * xx - 3) < xx**2 + 2 * xx + 3
eq(I(1 / ((xp + 2) * sp.sqrt(xp + 1)), (xp, 0, 3)), 2 * sp.atan(2) - sp.pi / 2, "radice")
eq(sp.diff(sp.exp(x) * (sp.sin(x) - sp.cos(x)) / 2, x), sp.exp(x) * sp.sin(x), "circolare")
eq(sp.limit((1 - sp.cos(x)) / x**2 * sp.sqrt(x), x, 0, "+"), 0, "guidato 2")
eq(I(2 - 2 * x**2, (x, -1, 1)), sp.Rational(8, 3), "area")
# ---- modulo 2
n = sp.symbols("n", positive=True, integer=True)
for expr, ref, L in [(sp.sqrt(n + 2) * (1 - sp.cos(1 / n)), n**sp.Rational(-3, 2), sp.Rational(1, 2)),
                     (n * (sp.exp(1 / n**2) - 1) * sp.sin(1 / n), n**-2, 1),
                     (sp.log(1 + 1 / n**3) / (1 - sp.cos(1 / n)), 1 / n, 2),
                     (sp.sqrt(n + 2) - sp.sqrt(n), n**sp.Rational(-1, 2), 1),
                     (sp.sqrt(n**2 + 1) - n, 1 / n, sp.Rational(1, 2))]:
    eq(sp.limit(expr / ref, n, sp.oo), L, "asintotico")
r1 = ((n + 2) ** 2 * 3**(n + 1) / sp.factorial(2 * n + 2)) / ((n + 1) ** 2 * 3**n / sp.factorial(2 * n))
eq(sp.limit(sp.combsimp(r1), n, sp.oo), 0, "rapporto 1")
r2 = (sp.factorial(n) / (9 ** (n + 1) * (n + 2) ** 4)) / (sp.factorial(n - 1) / (9**n * (n + 1) ** 4))
assert sp.limit(sp.combsimp(r2), n, sp.oo) == sp.oo
eq(sp.limit(n**2 * (1 - sp.cos(1 / n)), n, sp.oo), sp.Rational(1, 2), "non infinitesima")
eq(sp.diff(sp.log(xp) / xp, xp), (1 - sp.log(xp)) / xp**2, "monotonia")
eq(sp.summation(1 / (n * (n + 2)), (n, 1, sp.oo)), sp.Rational(3, 4), "telescopica")
assert abs(float(sp.summation(1 / (n * (n + 2)), (n, 1, 10))) - 0.6629) < 1e-3
# ---- modulo 3
assert sp.solve(y + y**2 - 4, y)[0] == -sp.Rational(1, 2) + sp.sqrt(17) / 2
assert sp.Rational(-1, -9) > 0 and sp.Rational(15, 23) > 0 and sp.Rational(-1, 7) < 0
r, th = sp.symbols("r th", positive=True)
pol = lambda e: sp.simplify(e.subs({x: r * sp.cos(th), y: r * sp.sin(th)}))  # noqa: E731
eq(pol(x * y**3 / (x**2 + y**2) ** 2), sp.cos(th) * sp.sin(th) ** 3, "polari c")
eq((x * x**3 / (x**2 + x**2) ** 2), sp.Rational(1, 4), "bisettrice")
g = x**2 * y / (x**4 + y**2)
eq(g.subs(y, x**2), sp.Rational(1, 2), "parabola")
eq(sp.limit(g.subs(y, 3 * x), x, 0), 0, "retta")
f = x**2 - 2 * x * y + y**3
assert set(map(tuple, [list(s) for s in sp.solve([f.diff(x), f.diff(y)], [x, y])])) == {(0, 0), (sp.Rational(2, 3), sp.Rational(2, 3))}
eq(sp.hessian(f, (x, y)).det().subs(y, sp.Rational(2, 3)), 4, "hess")
eq(f.subs({x: sp.Rational(2, 3), y: sp.Rational(2, 3)}), -sp.Rational(4, 27), "valore")
f = x**4 + y**4 - 4 * x * y
assert len(sp.solve([f.diff(x), f.diff(y)], [x, y])) == 3 and f.subs({x: 1, y: 1}) == -2
f = sp.sqrt(x + y**2 + 1)
eq(f.diff(x).subs({x: 0, y: 1}) * sp.Rational(3, 5) + f.diff(y).subs({x: 0, y: 1}) * sp.Rational(4, 5), 11 * sp.sqrt(2) / 20, "direzionale")
f = x * sp.exp(x * y)
assert (f.diff(x).subs({x: 1, y: 0}), f.diff(y).subs({x: 1, y: 0})) == (1, 1)
f = x**3 + y**3 - 3 * x * y
assert sp.hessian(f, (x, y)).det().subs({x: 1, y: 1}) == 27 and f.subs({x: 1, y: 1}) == -1
f = x**2 + y**2 - x - y
assert f.subs({x: sp.Rational(1, 2), y: sp.Rational(1, 2)}) == -sp.Rational(1, 2)
ok += 4
# ---- modulo 4
s = sp.dsolve(sp.Eq(Y(x).diff(x), x * sp.exp(Y(x))), Y(x), ics={Y(0): 0}).rhs
eq(sp.series(s, x, 0, 3).removeO(), x**2 / 2, "taylor sol")
assert all(abs(float((s + sp.log(1 - x**2 / 2)).subs(x, v))) < 1e-12 for v in (0.3, -0.9, 1.2))
ok += 1
s = sp.dsolve(sp.Eq(Y(t).diff(t), Y(t) / t + Y(t) ** 2), Y(t), ics={Y(1): 1}).rhs
eq(s, 2 * t / (3 - t**2), "bernoulli")
lam = sp.symbols("lam")
eq(sp.expand((lam - 2 - 3 * sp.I) * (lam - 2 + 3 * sp.I)), lam**2 - 4 * lam + 13, "k=13")
assert set(sp.solve(lam**2 - 4 * lam - 5, lam)) == {5, -1}
s = sp.dsolve(sp.Eq(Y(x).diff(x, 2) - 5 * Y(x).diff(x) + 6 * Y(x), 3 * sp.exp(3 * x)), Y(x),
              ics={Y(0): 0, Y(x).diff(x).subs(x, 0): 0}).rhs
eq(s, 3 * sp.exp(2 * x) - 3 * sp.exp(3 * x) + 3 * x * sp.exp(3 * x), "risonanza")
y0 = sp.symbols("y0")
cand = -1 + (y0 + 1) * sp.exp(t**3 / 3)
eq(cand.diff(t) - (cand + 1) * t**2, 0, "y0")
yy = sp.Function("w")(x)
fx = (x**2 - yy) / (1 + yy**2)
y2 = sp.diff(fx, x).subs(sp.Derivative(yy, x), fx)
eq(fx.subs(yy, 0).subs(x, 1), 1, "y'(1)")
eq(y2.subs(yy, 0).subs(x, 1), 1, "y''(1)")
A = sp.Matrix([[1, -5], [1, -3]])
assert A.trace() == -2 and A.det() == 2 and set(A.eigenvals()) == {-1 + sp.I, -1 - sp.I}
s = sp.dsolve(sp.Eq(Y(x).diff(x), Y(x) ** 2 * sp.exp(x)), Y(x), ics={Y(0): 1}).rhs
eq(s, 1 / (2 - sp.exp(x)), "guidato 1")
eq(sp.series(s, x, 0, 3).removeO(), 1 + x + sp.Rational(3, 2) * x**2, "guidato 1 taylor")
cand = sp.sin(t) / t**2
eq(cand.diff(t) + 2 / t * cand - sp.cos(t) / t**2, 0, "guidato 2")
X, Yv = sp.symbols("X Yv")
J = sp.Matrix([X - X * Yv, -Yv + X * Yv]).jacobian([X, Yv])
assert set(J.subs({X: 0, Yv: 0}).eigenvals()) == {1, -1} and set(J.subs({X: 1, Yv: 1}).eigenvals()) == {sp.I, -sp.I}
for M, att in [([[-2, 1], [0, -3]], {-2, -3}), ([[1, 2], [-2, 1]], {1 + 2 * sp.I, 1 - 2 * sp.I}), ([[0, 1], [-4, 0]], {2 * sp.I, -2 * sp.I})]:
    assert set(sp.Matrix(M).eigenvals()) == att
ok += 3
print("verifica ampliamento Analisi 1B: %d controlli superati" % ok)
