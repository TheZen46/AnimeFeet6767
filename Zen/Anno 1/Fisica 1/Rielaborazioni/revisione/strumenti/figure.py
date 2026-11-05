"""Figure dei moduli di Fisica Generale 1 (matplotlib, SVG con testo in tracciati).

Uso: python3 figure.py   -> scrive ../figure/N-k.svg
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "figure"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"svg.fonttype": "path", "font.size": 10, "font.family": "DejaVu Sans",
                     "axes.spines.top": False, "axes.spines.right": False})
G = 9.8


def fig_1_1():
    """Traiettorie di un proiettile con v0 = 20 m/s e angoli diversi."""
    v0 = 20.0
    fig, ax = plt.subplots(figsize=(5.8, 2.8))
    stili = {15: ("#888888", "--"), 30: ("#1f5fa8", "-"), 45: ("black", "-"), 60: ("#1f5fa8", ":"), 75: ("#888888", "-.")}
    for ang, (col, ls) in stili.items():
        th = np.radians(ang)
        tv = 2 * v0 * np.sin(th) / G
        t = np.linspace(0, tv, 200)
        x = v0 * np.cos(th) * t
        y = v0 * np.sin(th) * t - 0.5 * G * t**2
        ax.plot(x, y, color=col, ls=ls, lw=1.4, label=f"{ang}°")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_ylim(0, 24)
    ax.legend(frameon=False, fontsize=8, ncol=5, loc="upper center")
    fig.tight_layout()
    fig.savefig(OUT / "1-1.svg")
    plt.close(fig)


def fig_4_1():
    """Piano inclinato: forze su un corpo che rotola."""
    th = np.radians(25)
    fig, ax = plt.subplots(figsize=(4.6, 2.8))
    L = 5.0
    ax.plot([0, L * np.cos(th), L * np.cos(th), 0], [0, 0, L * np.sin(th), 0], color="black", lw=1)
    s = 2.6
    R = 0.45
    px, py = s * np.cos(th), s * np.sin(th)
    cx, cy = px - R * np.sin(th), py + R * np.cos(th)
    circ = plt.Circle((cx, cy), R, fill=False, lw=1.2, color="#1f5fa8")
    ax.add_patch(circ)
    def freccia(x0, y0, dx, dy, lab, off=(0.05, 0.05), col="black"):
        ax.annotate("", xy=(x0 + dx, y0 + dy), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.2))
        ax.text(x0 + dx + off[0], y0 + dy + off[1], lab, color=col)
    freccia(cx, cy, 0, -1.1, "$Mg$", (0.05, -0.15))
    freccia(px, py, -0.9 * np.sin(th) * 1.2, 0.9 * np.cos(th) * 1.2, "$N$", (-0.25, 0.05))
    freccia(px, py, 0.9 * np.cos(th), 0.9 * np.sin(th), "$F_A$", (0.0, 0.08), "#c0392b")
    ax.text(0.9, 0.12, r"$\theta$")
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUT / "4-1.svg")
    plt.close(fig)


if __name__ == "__main__":
    fig_1_1()
    fig_4_1()
    print("figure scritte in", OUT)
