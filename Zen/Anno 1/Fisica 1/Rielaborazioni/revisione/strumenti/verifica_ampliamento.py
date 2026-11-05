"""Verifica degli esercizi aggiunti nell'ampliamento di novembre 2026 (moduli 1-4)."""
from math import sqrt, sin, cos, tan, atan, acos, radians, degrees, pi
from scipy.optimize import brentq

g = 9.81
ok = 0


def v(a, b, tol=6e-3, nome=""):
    global ok
    assert abs(a - b) <= tol * max(1, abs(b)), (nome, a, b)
    ok += 1


# ---- modulo 1
t = sqrt(240 / g); v(t, 4.95); v(7 / t, 1.4, 0.02)
h = brentq(lambda h: sqrt(2 * h / g) + h / 340 - 4.8, 1, 200); v(h, 99.6); v(sqrt(h), 9.98); v(0.5 * g * 4.8**2, 113, 0.01)
x1 = 2000 * 3 / 5; vm = sqrt(4 * x1); v(x1, 1200); v(vm, 69.3); v(vm / 2 + vm / 3, 57.7)
dv = 60 / 3.6; v(dv**2 / 8, 34.7)
u, w = 3, 4
x = lambda t: u * t * (1 - 2 * sin(w * t))  # noqa: E731
vel = lambda t: u * (1 - 2 * sin(w * t)) - 2 * u * t * w * cos(w * t)  # noqa: E731
acc = lambda t: -4 * u * w * cos(w * t) + 2 * u * t * w * w * sin(w * t)  # noqa: E731
t1 = pi / 24; v(x(t1), 0, 1e-12); v(x(1), 7.54); v(x(.5), -1.23); v((x(1) - x(.5)) / .5, 17.5); v(vel(.75), 20.0); v(acc(t1), -35.3)
assert all(abs(3 * r - (r * r + 2)) < 1e-12 for r in (1, 2))
v(pi / 4, 0.785); v(sin(pi / 4), sqrt(2) / 2)
vx, vy = 15 * cos(radians(30)), 15 * sin(radians(30)); tv = (vy + sqrt(vy**2 + 2 * g * 20)) / g
v(tv, 2.92); v(vx * tv, 38.0); v(sqrt(vx**2 + (vy - g * tv)**2), 24.8); v(sqrt(225 + 2 * g * 20), 24.8)
v(degrees(atan(20 / 8)), 68, 0.01)
# ---- modulo 2
a0 = atan(0.3); a2 = 2 * a0; aa = g * (sin(a2) - 0.2 * cos(a2)); s = 2 / sin(a2)
v(degrees(a0), 16.7); v(aa, 3.76); v(s, 3.63); v(sqrt(2 * s / aa), 1.39)
v(5 * 2.25 * 5, 56.25); ct = g / (2.25 * 5); v(degrees(acos(ct)), 29.3); v(5 * sqrt(1 - ct**2), 2.45)
v(sqrt(2 * 0.5 / 0.05), 4.47); v(sqrt(2 * 0.125 / 0.05), 2.24); v(sqrt(2 * 0.25 / 0.05), 3.16)
om = 2 * pi / 0.5; l = 50 * 0.1 / (50 - 0.2 * om**2); v(l, 0.271); v(l - 0.1, 0.171)
v(0.5 * 0.2 * (om * l)**2 + 25 * (l - 0.1)**2, 1.90); v(0.2 * l * l * om, 0.185)
v(5 * g * 0.5 + 0.5 * 5 * g * cos(radians(30)), 45.8); ag = (10 * g - 5 * g * 0.5 - 0.3 * 5 * g * cos(radians(30))) / 15
v(ag, 4.06); v(10 * (g - ag), 57.5)
v(degrees(atan(400 / (100 * g))), 22.2); v(2 * pi * sqrt(0.8 / g), 1.79)
# ---- modulo 3
v(-60 * 0.1**3, -0.06); v(60 * 0.1**3 / 2, 0.03); v(18 * 3 * 1.5 - 18 * 0.5, 72)
v1 = sqrt(2 * g * 0.5 * (1 - cos(radians(30)))); v2 = 4 / 3 * v1; hh = v2**2 / (2 * g)
v(v1, 1.15); v(v2, 1.53); v(hh, 0.119); v(degrees(acos(1 - hh / 0.2)), 66, 0.01)
v(sqrt(9 + 25 + 2 * 15 * cos(radians(60))), 7); v(0.5 * 0.01 * 15, 0.075)
V = 0.058 * sqrt(100 / 3); v(V, 0.335); v(3 * V, 1.00)
m = 0.4; Ek = 2 - m * g * 0.5 * 0.2 - 0.15 * m * g * cos(radians(30)) * 0.2
v(m * g * 0.5 * 0.2, 0.392); v(0.15 * m * g * cos(radians(30)) * 0.2, 0.102); v(Ek, 1.506); v(sqrt(2 * Ek / m), 2.74)
v(2 / (m * g * 0.5 + 0.15 * m * g * cos(radians(30))), 0.81)
v(0.5 * 2 * 9 - 0.5 * 3 * 4, 3); v(sqrt(6 / 600), 0.1)
# ---- modulo 4
R2 = 2 * g / 2 + 0.5 * g / 3; v(R2, 11.45); v(2.5 * g - R2, 13.08); v(degrees(atan(0.2)), 11.3)
a = 2 * g / 7; vv = sqrt(2 * a * 2); v(a, 2.80); v(vv, 3.35); v(vv / 0.5, 6.70)
ad = 2 / 3 * g * sin(radians(45)); v(ad, 4.62); v(ad / 0.5, 9.25); v(g * sin(radians(45)) * 2 / 3, 4.62); v(degrees(atan(1.5)), 56.3)
v(g / 30, 0.327); v(2 * pi * sqrt(6 / 30), 2.81)
v0 = 1.5 / 0.17; vf = 5 / 7 * v0; v(v0, 8.82); v(vf, 6.30); v(vf / 0.0285, 221); v(0.7 * 0.17 * vf**2 - 0.5 * 0.17 * v0**2, -1.89)
w0 = sqrt(3 * g); wp = (1 / 3) / (1 / 3 + 0.5) * w0; K = 0.5 * (1 / 3 + 0.5) * wp**2
v(w0, 5.42); v(wp, 2.17); v(K, 1.96); v(degrees(acos(1 - K / g)), 36.9)
v(sqrt(10 / 7 * g), 3.74); v(sqrt(2 * g), 4.43); v(g * tan(radians(40)), 8.23)
v(0.5 - (1 / 32 + 1 / 16), 13 / 32)
print("verifica ampliamento Fisica 1: %d controlli superati" % ok)
