"""Ricalcolo di tutti i numeri usati negli esempi dei moduli di Statistica.

Uso: python3 verifica.py   (richiede sympy e scipy)
Ogni controllo stampa OK o ERRORE; alla fine il conteggio.
"""
from fractions import Fraction as Fr
from math import comb, factorial, exp, sqrt, log, pi, isclose
import sympy as sp
from scipy import stats

errori = 0


def ok(nome, valore, atteso, tol=None):
    global errori
    if tol is None:
        giusto = valore == atteso
    else:
        giusto = abs(float(valore) - float(atteso)) <= tol
    print(("OK     " if giusto else "ERRORE ") + nome, valore, "atteso", atteso)
    if not giusto:
        errori += 1


# ---------------- Modulo 1: statistica descrittiva ----------------
corso = {"G": (127, 7), "I": (101, 10), "A": (6, 2)}
n = sum(a + b for a, b in corso.values())
ok("M1 studenti totali", n, 253)
ok("M1 gestionale", sum(corso["G"]), 134)
ok("M1 f gestionale", round(134 / 253, 3), 0.530)
ok("M1 italiani", sum(v[0] for v in corso.values()), 234)
ok("M1 profilo stranieri G", round(7 / 19, 2), 0.37)
ok("M1 profilo colonna A stranieri", Fr(2, 8), Fr(1, 4))
occhi = {"F": (5, 8, 7), "M": (4, 6, 20)}
ok("M1 occhi colonne", tuple(a + b for a, b in zip(*occhi.values())), (9, 14, 27))
ok("M1 profilo riga M castani", round(20 / 30, 2), 0.67)
ok("M1 profilo colonna F verdi", round(8 / 14, 2), 0.57)
# test diagnostico
malati, sani = 10, 990
vp, fn = 8, 2
fp, vn = 99, 891
ok("M1 falsi positivi 10%", fp, round(0.10 * sani))
ok("M1 malato dato positivo", round(vp / (vp + fp), 3), 0.075)
# media e mediana
dati = list(range(1, 11))
ok("M1 media 1..10", Fr(sum(dati), 10), Fr(11, 2))
dati2 = list(range(1, 10)) + [100]
ok("M1 media con 100", Fr(sum(dati2), 10), Fr(145, 10))
# percentili con la definizione del corso
v = [1, 4, 5, 8, 9, 10, 12, 15]
f = [Fr(1, 6), Fr(1, 6), Fr(1, 12), Fr(1, 6), Fr(1, 12), Fr(1, 6), Fr(1, 12), Fr(1, 12)]
ok("M1 somma frequenze", sum(f), 1)


def quantile(q):
    c = 0
    for vi, fi in zip(v, f):
        c += fi
        if c >= q:
            return vi


ok("M1 Q1", quantile(Fr(1, 4)), 4)
ok("M1 Q2", quantile(Fr(1, 2)), 8)
ok("M1 Q3", quantile(Fr(3, 4)), 10)
ok("M1 10 perc", quantile(Fr(1, 10)), 1)
ok("M1 30 perc", quantile(Fr(3, 10)), 4)
ok("M1 90 perc", quantile(Fr(9, 10)), 12)
media = sum(vi * fi for vi, fi in zip(v, f))
ok("M1 media tabella", media, Fr(29, 4))
# voti: due studenti
s2 = [18] * 5 + [30] * 5
m2 = Fr(sum(s2), 10)
sig2 = sum((x - m2) ** 2 for x in s2) / 10
ok("M1 media voti", m2, 24)
ok("M1 sigma^2 voti", sig2, 36)
ok("M1 s^2 voti", sig2 * 10 / 9, 40)
ok("M1 CV voti", sig2 ** 0.5 / 24, 0.25, 1e-12)
# tabella X,Y di Lezione 4
tab = {(1, -1): 1, (1, 0): 2, (1, 1): 3, (2, -1): 3, (2, 0): 1, (2, 1): 0}
N = sum(tab.values())
mx = Fr(sum(x * c for (x, y), c in tab.items()), N)
my = Fr(sum(y * c for (x, y), c in tab.items()), N)
mxy = Fr(sum(x * y * c for (x, y), c in tab.items()), N)
vx = Fr(sum(x * x * c for (x, y), c in tab.items()), N) - mx ** 2
vy = Fr(sum(y * y * c for (x, y), c in tab.items()), N) - my ** 2
cov = mxy - mx * my
ok("M1 media x", mx, Fr(7, 5))
ok("M1 media y", my, Fr(-1, 10))
ok("M1 media xy", mxy, Fr(-2, 5))
ok("M1 cov", cov, Fr(-13, 50))
ok("M1 var x", vx, Fr(6, 25))
ok("M1 var y", vy, Fr(69, 100))
rho = float(cov) / sqrt(float(vx) * float(vy))
ok("M1 rho", round(rho, 3), -0.639)
m_retta = cov / vx
ok("M1 pendenza retta", m_retta, Fr(-13, 12))
q_retta = my - m_retta * mx
ok("M1 intercetta", q_retta, Fr(85, 60))
ok("M1 R^2", round(rho ** 2, 3), 0.408)
# R^2 = 1 - SSres/SStot
ssres = sum(c * (y - (m_retta * x + q_retta)) ** 2 for (x, y), c in tab.items())
sstot = sum(c * (y - my) ** 2 for (x, y), c in tab.items())
ok("M1 R^2 da residui", round(float(1 - ssres / sstot), 3), 0.408)
ok("M1 somma residui", sum(c * (y - (m_retta * x + q_retta)) for (x, y), c in tab.items()), 0)
# Simpson (esempio inventato): due reparti
A = {"uomini": (80, 100), "donne": (18, 20)}    # reparto facile
B = {"uomini": (5, 20), "donne": (30, 100)}     # reparto difficile
ok("M1 Simpson A donne > uomini", Fr(18, 20) > Fr(80, 100), True)
ok("M1 Simpson B donne > uomini", Fr(30, 100) > Fr(5, 20), True)
tot_u = Fr(85, 120)
tot_d = Fr(48, 120)
ok("M1 Simpson totale uomini", tot_u, Fr(17, 24))
ok("M1 Simpson totale donne", tot_d, Fr(2, 5))
ok("M1 Simpson inversione", tot_u > tot_d, True)

# ---------------- Modulo 2: probabilità e variabili aleatorie ----------------
ok("M2 somma 7 due dadi", Fr(sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == 7), 36), Fr(1, 6))
ok("M2 somma 11", Fr(sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == 11), 36), Fr(1, 18))
tre = [(a, b, c) for a in range(1, 7) for b in range(1, 7) for c in range(1, 7)]
ok("M2 tre dadi 9", Fr(sum(1 for t in tre if sum(t) == 9), 216), Fr(25, 216))
ok("M2 tre dadi 10", Fr(sum(1 for t in tre if sum(t) == 10), 216), Fr(1, 8))


def compleanni(k):
    p = Fr(1)
    for i in range(k):
        p *= Fr(365 - i, 365)
    return 1 - p


ok("M2 compleanni 3", round(float(compleanni(3)), 4), 0.0082)
ok("M2 compleanni 23", round(float(compleanni(23)), 3), 0.507)
ok("M2 compleanni 23 approx", round(1 - exp(-23 * 22 / 730), 3), 0.500)
ok("M2 compleanni 50", round(float(compleanni(50)), 3), 0.970)
ok("M2 stesso mio 23", round(1 - (364 / 365) ** 23, 3), 0.061)
ok("M2 urna 2R2B", round(comb(12, 2) * comb(8, 2) / comb(20, 4), 3), 0.381)
ok("M2 terno secco", Fr(comb(87, 2), comb(90, 5)), Fr(1, 11748))
ok("M2 doppia coppia", comb(13, 2) * comb(4, 2) ** 2 * 11 * 4, 123552)
ok("M2 doppia coppia p", round(123552 / comb(52, 5), 4), 0.0475)
ok("M2 full", 13 * 12 * comb(4, 3) * comb(4, 2), 3744)
ok("M2 full p", round(3744 / comb(52, 5), 5), 0.00144)
ok("M2 monomi", (comb(8, 2), comb(5, 2)), (28, 10))
ok("M2 scala reale", round(4 / comb(52, 5) * 1e6, 2), 1.54)
ok("M2 scala reale dato asso cuori", round(1 / comb(51, 4) * 1e6, 2), 4.0)
ok("M2 cabine", Fr(factorial(10) * 2 ** 10, factorial(20)), Fr(1, 19 * 17 * 15 * 13 * 11 * 9 * 7 * 5 * 3))
ok("M2 cabine valore", round(factorial(10) * 2 ** 10 / factorial(20) * 1e9, 2), 1.53)
print("   cabine:", factorial(10) * 2 ** 10 / factorial(20))
# dado e moneta
pF = Fr(1, 6) * sum(Fr(comb(i, 4), 2 ** i) for i in range(1, 7))
ok("M2 4 teste", pF, Fr(29, 384))
ok("M2 Bayes dado 5", Fr(1, 6) * Fr(5, 32) / pF, Fr(10, 29))
ok("M2 exit poll", Fr(40 * 45, 40 * 45 + 30 * 55), Fr(12, 23))
ok("M2 prima fiori dato seconda", Fr(12, 51) * Fr(1, 4) / Fr(1, 4), Fr(4, 17))
ok("M2 truccata 2T1C", 3 * Fr(2, 3) ** 2 * Fr(1, 3), Fr(4, 9))
# densità
x, y, a = sp.symbols('x y a', real=True)
ok("M2 mx", sp.solve(sp.integrate(a * x, (x, 0, 1)) - 1, a), [2])
ok("M2 P|X|>=1/2", sp.integrate(2 * x, (x, sp.Rational(1, 2), 1)), sp.Rational(3, 4))
ok("M2 Cauchy", sp.solve(sp.integrate(a / (1 + x ** 2), (x, -sp.oo, sp.oo)) - 1, a), [1 / sp.pi])
# trasformazioni
FY = 1 - ((1 - y) / 3) ** 2
ok("M2 f_Y -3X+1", sp.simplify(sp.diff(FY, y) - sp.Rational(2, 9) * (1 - y)), 0)
FY2a = sp.Rational(2, 3) * sp.sqrt(y)
FY2b = (1 + sp.sqrt(y)) / 3
ok("M2 (3X-1)^2 continuita in 1", FY2a.subs(y, 1), FY2b.subs(y, 1))
ok("M2 (3X-1)^2 F(4)", FY2b.subs(y, 4), 1)
ok("M2 gioco 11 euro", sorted({k ** 2 - 2 * k - 3 for k in range(5)}), [-4, -3, 0, 5])
leggeY = {}
for k in range(5):
    leggeY[k * k - 2 * k - 3] = leggeY.get(k * k - 2 * k - 3, 0) + Fr(comb(4, k), 16)
ok("M2 legge Y", leggeY, {-3: Fr(7, 16), -4: Fr(4, 16), 0: Fr(4, 16), 5: Fr(1, 16)})
ok("M2 E gioco", sum(k * p for k, p in leggeY.items()), -2)

# ---------------- Modulo 3: valori attesi e leggi notevoli ----------------
ok("M3 E esponenziale", sp.integrate(x / 3 * sp.exp(-x / 3), (x, 0, sp.oo)), 3)
ok("M3 E 2x", sp.integrate(2 * x * x, (x, 0, 1)), sp.Rational(2, 3))
ok("M3 E sin", sp.integrate(sp.sin(x) / sp.pi, (x, 0, sp.pi)), 2 / sp.pi)
p = sp.symbols('p', positive=True)
ok("M3 E cos/(1+Y)", sp.simplify(((1 - p) - p) * ((1 - p) + p / 2) - (1 - 2 * p) * (1 - p / 2)), 0)
ok("M3 urna monete", 3 * Fr(1, 2) * Fr(3, 5) + 3 * Fr(1, 3) * Fr(2, 5), Fr(13, 10))
ok("M3 var uniforme discreta n=6", Fr(sum(k * k for k in range(1, 7)), 6) - Fr(7, 2) ** 2, Fr(35, 12))
# congiunta L14
cong = {(0, 0): 0, (0, 1): Fr(1, 16), (1, 0): Fr(1, 8), (1, 1): Fr(1, 8), (2, 0): Fr(1, 4), (2, 1): Fr(1, 8),
        (3, 0): Fr(1, 16), (3, 1): Fr(3, 16), (4, 0): Fr(1, 16), (4, 1): 0}
ok("M3 somma congiunta", sum(cong.values()), 1)
EX = sum(i * q for (i, j), q in cong.items())
EY = sum(j * q for (i, j), q in cong.items())
EXY = sum(i * j * q for (i, j), q in cong.items())
ok("M3 EX", EX, 2)
ok("M3 EY", EY, Fr(1, 2))
ok("M3 EXY", EXY, Fr(15, 16))
ok("M3 cov", EXY - EX * EY, Fr(-1, 16))
# binomiale
ok("M3 dado 8 volte S=2", round(comb(8, 2) * (1 / 6) ** 2 * (5 / 6) ** 6, 3), 0.260)
ok("M3 dado S>=2", round(1 - (5 / 6) ** 8 - 8 * (1 / 6) * (5 / 6) ** 7, 3), 0.395)
pS2 = 3 * Fr(1, 8) * Fr(7, 10) + 3 * Fr(4, 9) * Fr(1, 3) * Fr(3, 10)
ok("M3 urna 10 monete S=2", pS2, Fr(19, 48))
ok("M3 truccata dato S=2", 3 * Fr(4, 9) * Fr(1, 3) * Fr(3, 10) / pS2, Fr(32, 95))
ok("M3 E S", Fr(3, 2) * Fr(7, 10) + 2 * Fr(3, 10), Fr(33, 20))
ok("M3 lotto 257", round((17 / 18) ** 257 * 1e7, 2), 4.17)
ok("M3 S5=3", Fr(comb(5, 3), 32), Fr(5, 16))
ok("M3 T3=5", Fr(comb(4, 2), 32), Fr(3, 16))
ok("M3 T3<=5", Fr(1, 8) + Fr(3, 16) + Fr(3, 16), Fr(1, 2))
ok("M3 overbooking bin", round(1 - 0.95 ** 100 - 100 * 0.05 * 0.95 ** 99, 4), 0.9629)
ok("M3 overbooking Poisson", round(1 - exp(-5) * 6, 4), 0.9596)
ok("M3 sito P[N>=12]", round(stats.poisson.sf(11, 5) * 1e3, 2), 5.45)
ok("M3 sito P[N=12]", round(stats.poisson.pmf(12, 5) * 1e3, 2), 3.43)
ok("M3 banca P[N=9]", round(stats.poisson.pmf(9, 12), 3), 0.087)
hy = [stats.hypergeom.pmf(k, 1000, 100, 10) for k in range(4)]
bi = [stats.binom.pmf(k, 10, 0.1) for k in range(4)]
ok("M3 iper k=2", round(hy[2], 3), 0.194)
ok("M3 bin k=2", round(bi[2], 3), 0.194)
print("   iper", [round(h, 4) for h in hy], round(1 - sum(hy), 4))
print("   bin ", [round(b, 4) for b in bi], round(1 - sum(bi), 4))
ok("M3 call center 4 min", round(1 - exp(-4 / 5), 3), 0.551)
ok("M3 call center 5|2", round(1 - exp(-3 / 5), 3), 0.451)
Z = stats.norm
ok("M3 P|Z|<=1", round(Z.cdf(1) - Z.cdf(-1), 4), 0.6827)
ok("M3 coda z=1 approx", round(exp(-0.5) / sqrt(2 * pi), 3), 0.242)
ok("M3 coda z=2 approx", round(exp(-2) / (2 * sqrt(2 * pi)), 4), 0.0270)
ok("M3 N(1,0.16)", round(Z.cdf(0.75) - Z.cdf(-1), 4), 0.6147)
ok("M3 N(1,0.16) X>2", round(Z.sf(2.5), 4), 0.0062)
ok("M3 phi 0.9", round(Z.ppf(0.9), 4), 1.2816)
ok("M3 phi 0.05", round(Z.ppf(0.05), 4), -1.6449)
ok("M3 altezze >183", round(Z.sf(1), 4), 0.1587)
ok("M3 atipico", round(2 * Z.cdf(-1.25), 4), 0.2113)
ok("M3 delta 50%", round(8 * Z.ppf(0.75), 2), 5.40)
ok("M3 biscotti", round(486 + Z.ppf(0.99) * 2 * 9, 1), 527.9)
ok("M3 moneta esatta", round(sum(stats.binom.pmf(k, 100, 0.5) for k in range(41, 60)), 3), 0.943)
ok("M3 moneta TLC", round(2 * Z.cdf(2) - 1, 3), 0.954)
ok("M3 n TLC", round((1.645 * 0.5 / 0.01) ** 2), 6765)
ok("M3 ristorante esatto", round(stats.poisson.cdf(200, 225), 3), 0.049)
ok("M3 ristorante TLC", round(Z.cdf(-25 / 15), 3), 0.048)
ok("M3 Poisson(1) P<=1", round(2 * exp(-1), 3), 0.736)

# ---------------- Modulo 4: inferenza ----------------
z05, z005, z025 = Z.ppf(0.95), Z.ppf(0.995), Z.ppf(0.975)
ok("M4 z_0.05", round(z05, 3), 1.645)
ok("M4 z_0.005", round(z005, 3), 2.576)
ok("M4 pesci 90%", round(z05 * 100 / 10, 2), 16.45)
ok("M4 pesci 99%", round(z005 * 100 / 10, 2), 25.76)
ok("M4 pesci n", round((z005 / z05) ** 2 * 100, 1), 245.2)
ph = 0.6
ok("M4 sigma hat", round(sqrt(ph * (1 - ph)), 3), 0.490)
ok("M4 moneta 90% d2", round(z05 * sqrt(0.24) / 10, 3), 0.081)
ok("M4 moneta 99% d2", round(z005 * sqrt(0.24) / 10, 3), 0.126)
ok("M4 moneta 99% d1", round(z005 * 0.5 / 10, 3), 0.129)
ok("M4 90 teste d2", round(z005 * 0.3 / 10, 3), 0.077)
T = stats.t
C = stats.chi2
ok("M4 t 0.01,8", round(T.ppf(0.99, 8), 3), 2.896)
ok("M4 delta 9 giorni", round(T.ppf(0.99, 8) * 13 / 3, 2), 12.55)
ok("M4 chi 0.99,8", round(C.ppf(0.01, 8), 3), 1.646)
ok("M4 chi 0.01,8", round(C.ppf(0.99, 8), 3), 20.090)
ok("M4 var 9 giorni", (round(8 * 169 / C.ppf(0.99, 8), 1), round(8 * 169 / C.ppf(0.01, 8), 1)), (67.3, 821.1))
ok("M4 t 0.005,80", round(T.ppf(0.995, 80), 3), 2.639)
ok("M4 eps straordinari", round(T.ppf(0.995, 80) * 6 / 9, 3), 1.759)
ok("M4 chi 0.995,80", round(C.ppf(0.005, 80), 3), 51.172)
ok("M4 chi 0.005,80", round(C.ppf(0.995, 80), 3), 116.321)
ok("M4 var straordinari", (round(80 * 36 / C.ppf(0.995, 80), 2), round(80 * 36 / C.ppf(0.005, 80), 2)), (24.76, 56.28))
# test di ipotesi (esempi nuovi)
tstat = (24 - 25.5) / (6 / 9)
ok("M4 test t straordinari", round(tstat, 2), -2.25)
ok("M4 t 0.025,80", round(T.ppf(0.975, 80), 3), 1.990)
ok("M4 p-value straordinari", round(2 * T.cdf(tstat, 80), 3), 0.027)
zs = (0.6 - 0.5) / (0.5 / 10)
ok("M4 test moneta z", zs, 2.0, 1e-12)
ok("M4 p-value moneta", round(2 * Z.sf(2), 4), 0.0455)
chi = 8 * 169 / 100
ok("M4 test varianza", round(chi, 2), 13.52)
ok("M4 chi 0.05,8", round(C.ppf(0.95, 8), 3), 15.507)
# potenza: test z unilaterale mu0=500 vs mu=520, sigma=100, n=100, alpha 5%
pot = Z.sf(z05 - 20 / 10)
ok("M4 potenza", round(pot, 3), 0.639)
# differenza di medie (campioni indipendenti, varianze note)
d = 52 - 48
se = sqrt(36 / 40 + 25 / 50)
ok("M4 diff medie se", round(se, 3), 1.183)
ok("M4 diff medie z", round(d / se, 2), 3.38)
# chi-quadro di indipendenza: genere x colore occhi
oss = [[5, 8, 7], [4, 6, 20]]
chi2, pv, dof, att = stats.chi2_contingency(oss, correction=False)
ok("M4 chi2 occhi", round(chi2, 2), 4.85)
ok("M4 chi2 occhi dof", dof, 2)
ok("M4 chi 0.05,2", round(C.ppf(0.95, 2), 3), 5.991)
print("   attese", att.round(2).tolist(), "p", round(pv, 3))
# ANOVA a una via (dati inventati)
g1, g2, g3 = [20, 22, 24], [25, 27, 26], [21, 23, 22]
Fst, pa = stats.f_oneway(g1, g2, g3)
ok("M4 ANOVA F", round(Fst, 2), 8.0)
ok("M4 F 0.05;2,6", round(stats.f.ppf(0.95, 2, 6), 2), 5.14)
print("   ANOVA p", round(pa, 4))

print("\nErrori:", errori)
