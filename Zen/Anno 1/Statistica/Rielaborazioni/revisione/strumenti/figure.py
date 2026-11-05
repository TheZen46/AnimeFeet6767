"""Figure dei moduli di Statistica (matplotlib, SVG con testo in tracciati).

Uso: python3 figure.py   -> scrive ../figure/N-k.svg
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

OUT = Path(__file__).resolve().parent.parent / "figure"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "svg.fonttype": "path", "font.size": 10, "axes.spines.top": False,
    "axes.spines.right": False, "font.family": "DejaVu Sans",
})
ACC = "#1f5fa8"
GR = "#888888"


def salva(fig, nome):
    fig.tight_layout()
    fig.savefig(OUT / f"{nome}.svg")
    plt.close(fig)


def fig_1_1():
    """Boxplot dei dati 1, ..., 9, 100 con i quartili del corso."""
    dati = list(range(1, 10)) + [100]
    q1, q2, q3 = 3, 5, 8
    iqr = q3 - q1
    sup = q3 + 1.5 * iqr
    baffo_sup = max(x for x in dati if x <= sup)
    fig, ax = plt.subplots(figsize=(6.2, 1.9))
    y = 0
    ax.add_patch(plt.Rectangle((q1, y - 0.3), q3 - q1, 0.6, fill=False, lw=1.4, ec="black"))
    ax.plot([q2, q2], [y - 0.3, y + 0.3], color=ACC, lw=2)
    ax.plot([1, q1], [y, y], color="black", lw=1)
    ax.plot([q3, baffo_sup], [y, y], color="black", lw=1)
    for xb in (1, baffo_sup):
        ax.plot([xb, xb], [y - 0.15, y + 0.15], color="black", lw=1)
    ax.plot(dati[:-1], [y - 0.55] * 9, "|", color=GR, ms=8)
    ax.plot([17.3], [y], "o", mfc="white", mec="black")
    ax.text(17.3, 0.3, "100", ha="center", fontsize=8)
    ax.text(16.6, -0.05, "//", ha="center", fontsize=9, color=GR)
    ax.plot([sup, sup], [-0.8, 0.8], ls=":", color=GR)
    ax.text(sup - 0.2, 0.62, r"$Q_3 + \frac{3}{2}\,\mathrm{IQR} = 15{,}5$", ha="right", fontsize=8)
    for v, t in ((q1, "$Q_1$"), (q2, "$Q_2$"), (q3, "$Q_3$")):
        ax.text(v, -0.95, t, ha="center", fontsize=9)
    ax.set_xlim(0, 18)
    ax.set_ylim(-1.1, 1.0)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks(range(0, 18, 2))
    salva(fig, "1-1")


def fig_1_2():
    """Dati della tabella a due vie e retta dei minimi quadrati."""
    tab = {(1, -1): 1, (1, 0): 2, (1, 1): 3, (2, -1): 3, (2, 0): 1}
    fig, ax = plt.subplots(figsize=(4.2, 3.0))
    for (x, y), c in tab.items():
        ax.scatter([x], [y], s=120 * c, color=ACC, alpha=0.35, ec=ACC)
        ax.text(x + 0.07, y + 0.12, str(c), fontsize=9)
    xx = np.linspace(0.7, 2.3, 10)
    ax.plot(xx, -13 / 12 * xx + 17 / 12, color="black", lw=1.4)
    ax.plot([1.4], [-0.1], "+", color="black", ms=10)
    ax.text(1.43, -0.32, r"$(\bar x, \bar y)$", fontsize=9)
    ax.set_xlim(0.6, 2.4)
    ax.set_ylim(-1.6, 1.6)
    ax.set_xticks([1, 2])
    ax.set_yticks([-1, 0, 1])
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    salva(fig, "1-2")


def fig_2_1():
    """Densità e probabilità come area."""
    f = stats.gamma(a=3, scale=1).pdf
    x = np.linspace(0, 10, 400)
    fig, ax = plt.subplots(figsize=(5.0, 2.4))
    ax.plot(x, f(x), color="black")
    a, b = 1.5, 4
    xs = np.linspace(a, b, 100)
    ax.fill_between(xs, f(xs), color=ACC, alpha=0.3)
    ax.text(2.75, 0.07, r"$P[a \leq X \leq b]$", ha="center", fontsize=9)
    ax.set_xticks([a, b])
    ax.set_xticklabels(["$a$", "$b$"])
    ax.set_yticks([])
    ax.text(6.5, 0.15, r"$y = f(x)$", fontsize=9)
    ax.set_ylim(0, 0.32)
    salva(fig, "2-1")


def fig_3_1():
    """Normale standard: densità con l'area fra -1 e 1, e funzione di ripartizione."""
    z = np.linspace(-3.5, 3.5, 400)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.4))
    a1.plot(z, stats.norm.pdf(z), color="black")
    zs = np.linspace(-1, 1, 100)
    a1.fill_between(zs, stats.norm.pdf(zs), color=ACC, alpha=0.3)
    a1.text(0, 0.12, "68,3%", ha="center", fontsize=9)
    a1.set_xticks([-2, -1, 0, 1, 2])
    a1.set_yticks([0, 0.2, 0.4])
    a1.set_title(r"densità $\phi(z)$", fontsize=10)
    a2.plot(z, stats.norm.cdf(z), color="black")
    for zz in (-1, 0, 1):
        v = stats.norm.cdf(zz)
        a2.plot([zz, zz], [0, v], ls=":", color=GR)
        a2.plot([-3.5, zz], [v, v], ls=":", color=GR)
    a2.set_yticks([0, 0.16, 0.5, 0.84, 1])
    a2.set_yticklabels(["0", "0,16", "0,5", "0,84", "1"])
    a2.set_xticks([-2, -1, 0, 1, 2])
    a2.set_title(r"ripartizione $\Phi(z)$", fontsize=10)
    salva(fig, "3-2")


def fig_3_2():
    """Binomiale Bin(100; 0,05) e Poisson(5)."""
    k = np.arange(0, 15)
    fig, ax = plt.subplots(figsize=(5.4, 2.4))
    ax.bar(k - 0.18, stats.binom.pmf(k, 100, 0.05), width=0.36, color=GR, label="Bin(100; 0,05)")
    ax.bar(k + 0.18, stats.poisson.pmf(k, 5), width=0.36, color=ACC, label="Poisson(5)")
    ax.set_xticks(range(0, 15, 2))
    ax.set_xlabel("$k$")
    ax.legend(frameon=False, fontsize=8)
    salva(fig, "3-1")


def fig_4_1():
    """Venti intervalli di confidenza al 90% da campioni simulati."""
    rng = np.random.default_rng(7)
    mu, sigma, n = 500, 100, 100
    z = stats.norm.ppf(0.95)
    d = z * sigma / np.sqrt(n)
    fig, ax = plt.subplots(figsize=(5.8, 2.8))
    for i in range(20):
        m = rng.normal(mu, sigma, n).mean()
        fuori = abs(m - mu) > d
        ax.plot([m - d, m + d], [i, i], color=("#c0392b" if fuori else "black"), lw=1.4)
        ax.plot([m], [i], "o", ms=3, color=("#c0392b" if fuori else "black"))
    ax.axvline(mu, color=ACC, lw=1.2)
    ax.text(mu + 1, 20.2, r"$\mu$", color=ACC)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("peso (g)")
    salva(fig, "4-1")


def fig_4_2():
    """Densità t di Student e normale; densità chi-quadro."""
    x = np.linspace(-4, 4, 400)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.4))
    a1.plot(x, stats.norm.pdf(x), color="black", label="$N(0, 1)$")
    a1.plot(x, stats.t.pdf(x, 3), color=ACC, label="$t_3$")
    a1.plot(x, stats.t.pdf(x, 1), color=GR, ls="--", label="$t_1$")
    a1.legend(frameon=False, fontsize=8)
    a1.set_yticks([])
    w = np.linspace(0.01, 20, 400)
    for k, st in ((2, ":"), (4, "--"), (8, "-")):
        a2.plot(w, stats.chi2.pdf(w, k), color="black", ls=st, label=fr"$\chi^2_{{{k}}}$")
    a2.legend(frameon=False, fontsize=8)
    a2.set_yticks([])
    a2.set_ylim(0, 0.5)
    salva(fig, "4-2")



def fig_4_3():
    """Funnel plot dei dieci ospedali del paragrafo 4.9."""
    n = np.array([50, 80, 120, 150, 200, 260, 300, 400, 500, 640])
    d = np.array([6, 4, 10, 18, 14, 34, 21, 30, 70, 36])
    p = d.sum() / n.sum()
    xs = np.linspace(40, 700, 300)
    se = np.sqrt(p * (1 - p) / xs)
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    ax.axhline(p, color="black", lw=1)
    for z, ls in [(1.96, "--"), (3.09, ":")]:
        ax.plot(xs, p + z * se, color=GR, ls=ls, lw=1.2)
        ax.plot(xs, np.clip(p - z * se, 0, None), color=GR, ls=ls, lw=1.2)
    ax.scatter(n, d / n, color=ACC, zorder=3, s=22)
    for lab, x, y in zip("ABCDEFGHIJ", n, d / n):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(5, 3), fontsize=9)
    ax.set_xlabel("numero di interventi $n_i$")
    ax.set_ylabel("tasso $\\hat p_i$")
    ax.set_ylim(0, 0.23)
    ax.text(690, p + 0.004, "$\\bar p = 0{,}09$", ha="right", fontsize=9)
    ax.text(700, p + 1.96 * np.sqrt(p * (1 - p) / 700) + 0.003, "95%", ha="right", fontsize=8, color=GR)
    ax.text(700, p + 3.09 * np.sqrt(p * (1 - p) / 700) + 0.003, "99,8%", ha="right", fontsize=8, color=GR)
    salva(fig, "4-3")

if __name__ == "__main__":
    for f in (fig_1_1, fig_1_2, fig_2_1, fig_3_1, fig_3_2, fig_4_1, fig_4_2, fig_4_3):
        f()
    print("figure scritte in", OUT)
