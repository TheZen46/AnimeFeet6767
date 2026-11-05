"""Verifica degli esercizi aggiunti nell'ampliamento di novembre 2026 (moduli 1-4)."""
from math import comb, exp, log, sqrt
import numpy as np
from scipy import stats as st
from scipy.integrate import quad

ok = 0


def v(a, b, tol=6e-3, nome=""):
    global ok
    assert abs(a - b) <= tol * max(1, abs(b)), (nome, a, b)
    ok += 1


# ---- modulo 1
x = np.array([1, 2, 3, 4, 5.]); y = np.array([2.1, 3.9, 6.2, 7.8, 10.0])
m, q = np.polyfit(x, y, 1); r = y - (m * x + q)
v(m, 1.97); v(q, 0.09, 1e-6 + 0.02); v(((y - y.mean())**2).sum(), 38.9); v((r**2).sum(), 0.091)
v(1 - (r**2).sum() / ((y - y.mean())**2).sum(), 0.998, 1e-3); assert np.allclose(r, [0.04, -0.13, 0.2, -0.17, 0.06])
assert 45 / 50 > 212 / 250 and 175 / 250 > 30 / 50 and 220 / 300 < 242 / 300
v(0.5 / 50, 0.01); v(0.1 / 5, 0.02)
x = np.array([2, 4, 6, 8.]); y = np.array([18, 22, 25, 27.]); m, q = np.polyfit(x, y, 1)
v(m, 1.5); v(q, 15.5); v(m * 5 + q, 23)
assert 24 / 80 == 36 / 120 == 60 / 200 and abs(24 / 200 - 0.4 * 0.3) < 1e-12
dati = [0] * 4 + [1] * 8 + [2] * 6 + [3] * 2
v(np.mean(dati), 1.3); v(np.var(dati), 0.81); v(np.var(dati, ddof=1), 0.853); assert np.median(dati) == 1
# ---- modulo 2
v(0.95 * 0.02 / (0.95 * 0.02 + 0.10 * 0.98), 0.1624)
assert comb(40, 5) == 658008 and comb(4, 2) * comb(36, 3) == 42840
v(42840 / 658008, 0.0651); v(0.25 - 1 / 16, 3 / 16)
u = np.random.default_rng(1).uniform(size=200000); yy = -0.5 * np.log(u)
v(yy.mean(), 0.5, 0.02); v((2 * u - 1)[np.abs(2 * u - 1)**2 <= 0.25].size / u.size, 0.5, 0.02)
v(0.006 / 0.017, 0.353); v(0.005 / 0.017, 0.294)
assert sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == 7 and a == 3) == 1
v(quad(lambda t: 1 / (3 * sqrt(t)), 0, 1)[0] + quad(lambda t: 1 / (6 * sqrt(t)), 1, 4)[0], 1.0)
# ---- modulo 3
pN = {1: .5, 2: .25, 3: .125, 4: .125}
EN = sum(n * p for n, p in pN.items()); VN = sum(n * n * p for n, p in pN.items()) - EN**2
v(EN, 15 / 8); v(VN, 71 / 64); v(0.6 * EN, 1.125)
px2 = sum(p * comb(n, 2) * .6**2 * .4**(n - 2) for n, p in pN.items() if n >= 2)
v(px2, 0.1872); v(pN[4] * comb(4, 2) * .36 * .16 / px2, 0.2308)
v(1 - st.norm.cdf(2.5)**50, 0.268); assert st.norm.cdf(2.5)**111 > 0.5 > st.norm.cdf(2.5)**112
v(st.norm.sf((9 - 4) / 5), 0.1587)
J = np.array([[.1, .2, .2], [.2, .1, .2]]); Y = np.array([-1, 0, 2]); X = np.array([0, 1])
v((J.sum(0) * Y).sum(), 0.5); v((J[1] / J[1].sum() * Y).sum(), 0.4)
v((X[:, None] * Y[None, :] * J).sum() - 0.5 * 0.5, -0.05, 1e-9)
v(st.norm.cdf(1) - st.norm.cdf(-1), 0.683); v(exp(-1), 0.368)
v(st.binom.cdf(1, 500, .004), 0.4055, 1e-3); v(exp(-2) * 3, 0.4060, 1e-3)
v(quad(lambda t: t**2 / 9, 0, 3)[0], 1); v(quad(lambda t: t**3 / 9, 0, 3)[0], 9 / 4)
v(quad(lambda t: t**4 / 9, 0, 3)[0] - (9 / 4)**2, 27 / 80)
v(st.norm.sf(2), 0.0228); v(170 + st.norm.ppf(.9) * 8, 180.3, 1e-3)
v(st.norm.cdf((25.5 - 30) / sqrt(21)), 0.164); v(st.binom.cdf(25, 100, .3), 0.163); v(st.norm.cdf(-5 / sqrt(21)), 0.138)
# ---- modulo 4
n = np.array([50, 80, 120, 150, 200, 260, 300, 400, 500, 640]); d = np.array([6, 4, 10, 18, 14, 34, 21, 30, 70, 36])
p = d.sum() / n.sum(); v(p, 0.09, 1e-9); z = (d / n - p) / np.sqrt(p * (1 - p) / n)
assert z[8] > 3.09 and 1.96 < z[5] < 3.09 and -3.09 < z[9] < -1.96 and all(abs(z[[0, 1, 2, 3, 4, 6, 7]]) < 1.96)
v(sqrt(.09 * .91 / 500), 0.0128); v(z[8], 3.9, 0.02)
v(st.norm.cdf(-2), 0.023, 0.02)
t = 0.4 / (0.9 / sqrt(10)); v(t, 1.41); v(st.t.ppf(.975, 9), 2.262); v(2 * st.t.sf(t, 9), 0.19, 0.03)
sp2 = (11 * 36 + 9 * 25) / 20; se = sqrt(sp2) * sqrt(1 / 12 + 1 / 10); t = 6 / se
v(sp2, 31.05); v(se, 2.39); v(t, 2.51); v(st.t.ppf(.975, 20), 2.086); v(2 * st.t.sf(t, 20), 0.021, 0.03)
v(6 - 2.086 * se, 1.0, 0.03); v(6 + 2.086 * se, 11.0, 0.01)
dd = np.array([3, 5, -1, 4, 2, 5]); t = dd.mean() / (dd.std(ddof=1) / sqrt(6))
v(dd.var(ddof=1), 5.2); v(t, 3.22); v(st.t.ppf(.95, 5), 2.015); v(st.t.sf(t, 5), 0.012, 0.03)
o = np.array([25, 17, 15, 23, 24, 16]); v(((o - 20)**2 / 20).sum(), 5.0); v(st.chi2.ppf(.95, 5), 11.07); v(st.chi2.sf(5, 5), 0.42, 0.01)
F = st.f_oneway([10, 12, 11, 13], [14, 15, 13, 16], [11, 10, 12, 11]); v(F.statistic, 10.75); v(F.pvalue, 0.004, 0.05); v(st.f.ppf(.95, 2, 9), 4.26)
v(((st.norm.ppf(.95) + st.norm.ppf(.9)) * 100 / 20)**2, 214.1)
z = 0.04 / sqrt(.25 / 1000); v(z, 2.53); v(st.norm.sf(z), 0.006, 0.05); v(st.norm.ppf(.99), 2.326)
pb = 45 / 540; zz = [(r_ - pb) / sqrt(pb * (1 - pb) / m_) for r_, m_ in [(3 / 40, 40), (12 / 100, 100), (30 / 400, 400)]]
v(zz[0], -0.19, 0.03); v(zz[1], 1.33); v(zz[2], -0.60, 0.02)
c = 2 * 7.5**2 / 52.5 + 2 * 7.5**2 / 47.5; v(c, 4.51); v(st.chi2.ppf(.95, 1), 3.841); v(st.chi2.sf(c, 1), 0.034, 0.02)
print("verifica ampliamento Statistica: %d controlli superati" % ok)
