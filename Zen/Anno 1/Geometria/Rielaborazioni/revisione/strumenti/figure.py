"""Figure dei moduli di Geometria (matplotlib, SVG con testo in tracciati).

Uso: python3 figure.py   -> scrive ../figure/N-k.svg
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "figure"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"svg.fonttype": "path", "font.size": 10, "font.family": "DejaVu Sans"})
ACC = "#1f5fa8"
GR = "#888888"


def fig_1_1():
    """Radici seste di -4i nel piano di Gauss."""
    r = 2 ** (1 / 3)
    ang = [np.pi / 4 + k * np.pi / 3 for k in range(6)]
    fig, ax = plt.subplots(figsize=(3.8, 3.8))
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(r * np.cos(t), r * np.sin(t), color=GR, lw=0.8, ls=":")
    xs = [r * np.cos(a) for a in ang] + [r * np.cos(ang[0])]
    ys = [r * np.sin(a) for a in ang] + [r * np.sin(ang[0])]
    ax.plot(xs, ys, color=ACC, lw=1)
    for k, a in enumerate(ang):
        ax.plot([0, r * np.cos(a)], [0, r * np.sin(a)], color="black", lw=0.6)
        ax.plot(r * np.cos(a), r * np.sin(a), "o", color=ACC, ms=5)
        ax.text(1.22 * r * np.cos(a), 1.22 * r * np.sin(a), f"$w_{k}$", ha="center", va="center")
    ax.annotate("", xy=(1.8, 0), xytext=(-1.8, 0), arrowprops=dict(arrowstyle="->", color=GR))
    ax.annotate("", xy=(0, 1.8), xytext=(0, -1.8), arrowprops=dict(arrowstyle="->", color=GR))
    ax.text(1.75, -0.18, "Re", fontsize=8, color=GR)
    ax.text(0.06, 1.7, "Im", fontsize=8, color=GR)
    ax.set_aspect("equal")
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.9, 1.9)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUT / "1-1.svg")
    plt.close(fig)


def fig_1_2():
    """Prodotto vettoriale: parallelogramma e vettore ortogonale (vista assonometrica)."""
    def p(v):  # proiezione obliqua semplice
        x, y, z = v
        return np.array([x - 0.5 * y, z - 0.35 * y])
    v = np.array([2.0, 0.0, 0.0])
    w = np.array([0.8, 1.8, 0.0])
    n = np.cross(v, w) / 1.6
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    poly = np.array([p(np.zeros(3)), p(v), p(v + w), p(w)])
    ax.fill(poly[:, 0], poly[:, 1], color=ACC, alpha=0.15)
    for vec, lab, col in ((v, "$v$", "black"), (w, "$w$", "black"), (n, r"$v \wedge w$", ACC)):
        a, b = p(np.zeros(3)), p(vec)
        ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=col, lw=1.4))
        ax.text(b[0] + 0.08, b[1] + 0.05, lab, color=col)
    c = p((v + w) / 2)
    ax.text(c[0] - 0.55, c[1] - 0.05, "area $= \\|v \\wedge w\\|$", fontsize=8)
    ax.set_xlim(-0.6, 2.9)
    ax.set_ylim(-0.9, 2.6)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUT / "1-2.svg")
    plt.close(fig)


if __name__ == "__main__":
    fig_1_1()
    fig_1_2()
    print("figure scritte in", OUT)
