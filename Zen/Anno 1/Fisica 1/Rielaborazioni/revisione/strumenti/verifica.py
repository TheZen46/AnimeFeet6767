"""Ricalcolo degli esempi dei moduli di Fisica Generale 1.

Uso: python3 verifica.py   (richiede sympy)
"""
from math import sqrt, pi, sin, cos, tan, radians, isclose
import sympy as sp

g = 9.8
errori = 0


def ok(nome, valore, atteso, tol=0.0):
    global errori
    giusto = abs(valore - atteso) <= tol if tol else valore == atteso
    print(("OK     " if giusto else "ERRORE ") + nome, valore, "atteso", atteso)
    if not giusto:
        errori += 1


t, w, x, A, phi = sp.symbols('t omega x A phi', real=True)
# ---------- Modulo 1: strumenti e cinematica ----------
xs = A * sp.cos(w * t + phi)
ok("M1 oscillatore risolve x''=-w^2 x", sp.simplify(sp.diff(xs, t, 2) + w**2 * xs), 0)
a0, v0, x0 = sp.symbols('a0 v0 x0')
xm = a0 * t**2 / 2 + v0 * t + x0
ok("M1 MRUA x''", sp.diff(xm, t, 2), a0)
ok("M1 frenata tempo", 30 / 5, 6.0)
ok("M1 frenata spazio", 30 * 6 - 5 * 36 / 2, 90.0)
ok("M1 v^2 = v0^2 + 2a dx", 30**2 - 2 * 5 * 90, 0)
th = radians(30)
ok("M1 proiettile tempo di volo", round(2 * 20 * sin(th) / g, 2), 2.04)
ok("M1 proiettile gittata", round(20**2 * sin(2 * th) / g, 1), 35.3)
ok("M1 proiettile altezza massima", round((20 * sin(th))**2 / (2 * g), 2), 5.10)
om = 2 * 2 * pi
ok("M1 circolare omega", round(om, 2), 12.57)
ok("M1 circolare v", round(om * 0.5, 2), 6.28)
ok("M1 circolare ac", round(om**2 * 0.5, 1), 79.0)
ok("M1 barca modulo", sqrt(3**2 + 4**2), 5.0)
ok("M1 barca tempo", 60 / 3, 20.0)
ok("M1 barca deriva", 4 * 20, 80)

# ---------- Modulo 2: dinamica ----------
ok("M2 auto forza", round(1500 * (100 / 3.6) / 20), 2083)
ok("M2 due scatole a", 10 / (2 + 3), 2.0)
ok("M2 due scatole T", 3 * 10 / 5, 6.0)
ok("M2 piano liscio", round(g * sin(th), 2), 4.9)
ok("M2 piano scabro", round(g * (sin(th) - 0.2 * cos(th)), 2), 3.20)
ok("M2 angolo limite mu=0.5", round(sp.deg(sp.atan(0.5)).evalf(), 1), 26.6, 0.05)
ok("M2 giro della morte", round(sqrt(g * 1), 2), 3.13)
ok("M2 tensione in alto v=4", round(0.5 * 4**2 / 1 - 0.5 * g, 2), 3.1)
ok("M2 pendolo periodo", round(2 * pi * sqrt(1 / g), 2), 2.01)
ok("M2 molla omega", sqrt(200 / 0.5), 20.0)
ok("M2 molla periodo", round(2 * pi / 20, 3), 0.314)
# piano inclinato e massa appesa (m1 sul piano scabro, m2 appesa)
m1, m2, mud = 4.0, 3.0, 0.2
a = (m2 * g - m1 * g * sin(th) - mud * m1 * g * cos(th)) / (m1 + m2)
ok("M2 piano e carrucola a", round(a, 2), 0.43)
T = m2 * (g - a)
ok("M2 piano e carrucola T", round(T, 1), 28.1)

# ---------- Modulo 3: lavoro, energia, quantita di moto ----------
ok("M3 lavoro molla", 0.5 * 200 * 0.1**2, 1.0, 1e-12)
ok("M3 caduta libera v", round(sqrt(2 * g * 5), 2), 9.9)
ok("M3 molla lancia blocco v", round(sqrt(200 / 0.5) * 0.1, 2), 2.0)
U = x**3 - 3 * x
eq = sp.solve(sp.diff(U, x), x)
ok("M3 equilibri", sorted(eq), [-1, 1])
ok("M3 stabile in 1", sp.diff(U, x, 2).subs(x, 1) > 0, True)
ok("M3 instabile in -1", sp.diff(U, x, 2).subs(x, -1) < 0, True)
ok("M3 potenza", 500 * 20, 10000)
ok("M3 rinculo", -0.01 * 400 / 4, -1.0)
vf = (2 * 3 + 1 * 0) / 3
ok("M3 anelastico vf", vf, 2.0)
ok("M3 anelastico energia persa", 0.5 * 2 * 9 - 0.5 * 3 * vf**2, 3.0)
v1p, v2p = (2 - 1) / 3 * 3, 2 * 2 / 3 * 3
ok("M3 elastico v1'", v1p, 1.0)
ok("M3 elastico v2'", v2p, 4.0)
ok("M3 elastico energia", 0.5 * 2 * v1p**2 + 0.5 * 1 * v2p**2, 9.0)
l, al, lam = sp.symbols('l alpha lambda0', positive=True)
M = sp.integrate(lam * (1 + al * x), (x, 0, l))
xc = sp.simplify(sp.integrate(lam * (1 + al * x) * x, (x, 0, l)) / M)
ok("M3 CM asta", sp.simplify(xc - l * (3 + 2 * al * l) / (3 * (2 + al * l))), 0)
ok("M3 CM omogenea", sp.limit(xc, al, 0), l / 2)
# pendolo balistico
mp, Mb, vp = 0.01, 2.0, 300.0
V = mp * vp / (mp + Mb)
ok("M3 pendolo balistico V", round(V, 3), 1.493)
ok("M3 pendolo balistico h", round(V**2 / (2 * g), 3), 0.114)

# ---------- Modulo 4: corpo rigido ----------
m, R = sp.symbols('m R', positive=True)
ok("M4 due masse I_CM", sp.simplify(2 * m * (l / 2)**2), m * l**2 / 2)
ok("M4 Steiner due masse", sp.simplify(m * l**2 / 2 + 2 * m * (l / 2)**2), m * l**2)
r = sp.symbols('r', positive=True)
ok("M4 asta I_CM", sp.integrate(m / l * x**2, (x, -l / 2, l / 2)), m * l**2 / 12)
ok("M4 asta estremo", sp.integrate(m / l * x**2, (x, 0, l)), m * l**2 / 3)
ok("M4 disco", sp.integrate(m / (sp.pi * R**2) * r**2 * 2 * sp.pi * r, (r, 0, R)), m * R**2 / 2)
th_, ph = sp.symbols('theta varphi')
rho = m / (sp.Rational(4, 3) * sp.pi * R**3)
Isf = sp.integrate(sp.integrate(sp.integrate(rho * (r * sp.sin(th_))**2 * r**2 * sp.sin(th_), (r, 0, R)), (th_, 0, sp.pi)), (ph, 0, 2 * sp.pi))
ok("M4 sfera", sp.simplify(Isf), sp.Rational(2, 5) * m * R**2)
ok("M4 carrucola I", round((0.33 * 15 - 1.1) / 10, 3), 0.385)
ok("M4 palo v", round(sqrt(3 * g * 2.3), 2), 8.22)
for nome, c, att in (("anello", 1.0, 0.5), ("disco", 0.5, 2 / 3), ("sfera", 0.4, 5 / 7)):
    ok("M4 rotolamento " + nome, 1 / (1 + c), att, 1e-12)
ok("M4 mu minimo disco", round(0.5 / 1.5 * tan(th), 3), 0.192)
ok("M4 Atwood a", round((3 - 2) * g / (3 + 2 + 2 / 2), 3), 1.633)
aA = (3 - 2) * g / 6
T1, T2 = 3 * (g - aA), 2 * (g + aA)
ok("M4 Atwood T1-T2 = I a / R^2", round(T1 - T2, 3), round(1.0 * aA, 3))
ok("M4 pattinatrice", 4 * 2 / 1.6, 5.0)
ok("M4 pattinatrice energia", (0.5 * 1.6 * 25) / (0.5 * 4 * 4), 2.5)
R2 = (20 * g * 2 + 30 * g * 1) / 4
ok("M4 trave R2", round(R2, 1), 171.5)
ok("M4 trave R1", round(50 * g - R2, 1), 318.5)
ok("M2 ascensore N", 70 * (g + 2), 826.0, 1e-9)
ok("M2 ascensore kg", round(826 / g, 1), 84.3)
ok("M2 curva vmax", round(sqrt(0.8 * g * 50), 1), 19.8)
ok("M3 attrito ferma blocco", round(1 / (0.2 * 0.5 * g), 2), 1.02)
ok("M4 disco alpha", 4 * 0.1 / (0.5 * 2 * 0.1**2), 40.0, 1e-9)
ok("M4 disco energia", 0.5 * 0.01 * 80**2, 32.0, 1e-9)
ok("M4 disco lavoro", 4 * 0.1 * 0.5 * 40 * 2**2, 32.0, 1e-9)
ok("M4 sasso", round(sqrt(2 * g * 2.3), 2), 6.71)
ok("M4 sfera vs cilindro", (2 / 1.4) > (2 / 1.5), True)
# segno nel teorema del momento angolare: dL/dt = tau - vO x p
vO, vv, rr, rO, FF = (sp.Matrix(sp.symbols(f'{n}1:4')) for n in ('a', 'b', 'c', 'd', 'f'))
mm = sp.symbols('mm')
lhs = (vv - vO).cross(mm * vv) + (rr - rO).cross(FF)
ok("M4 teorema momento angolare", sp.simplify(lhs - ((rr - rO).cross(FF) - vO.cross(mm * vv))), sp.zeros(3, 1))
print("\nErrori:", errori)
