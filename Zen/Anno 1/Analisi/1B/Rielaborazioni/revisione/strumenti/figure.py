"""Figure di Analisi 1B (ridisegnate). Uso: python figure.py <cartella>"""
import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams.update({"svg.fonttype": "path", "font.size": 10, "font.family": "DejaVu Sans"})
import matplotlib.pyplot as plt
OUT = sys.argv[1] if len(sys.argv) > 1 else "figure"; os.makedirs(OUT, exist_ok=True)
BLU, ROSSO = "#1f5f9e", "#b5452b"

def salva(fig, nome):
    fig.savefig(os.path.join(OUT, nome + ".svg"), bbox_inches="tight"); plt.close(fig)

# 1-1 somme inferiori e superiori
f = lambda x: 1 + 0.8 * np.sin(1.3 * x) + 0.15 * x
xs = np.linspace(0.3, 4.3, 400); P = np.linspace(0.6, 4.0, 6)
fig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
for ax, tipo in zip(axs, ["inferiori", "superiori"]):
    ax.plot(xs, f(xs), color="black", lw=1.4)
    for a, b in zip(P[:-1], P[1:]):
        t = np.linspace(a, b, 100); h = f(t).min() if tipo == "inferiori" else f(t).max()
        ax.add_patch(plt.Rectangle((a, 0), b - a, h, fill=True, alpha=0.25,
                     color=BLU if tipo == "inferiori" else ROSSO, ec="black", lw=0.6))
    ax.set_xticks(P); ax.set_xticklabels([f"$x_{i}$" for i in range(len(P))])
    ax.set_yticks([]); ax.set_title("somma " + tipo); ax.spines[["top", "right"]].set_visible(False)
    ax.set_ylim(0, 2.6)
salva(fig, "1-1")

# 2-1 criterio integrale
fx = lambda x: 1 / x**1.3
xs = np.linspace(1, 8.5, 400)
fig, ax = plt.subplots(figsize=(6, 3))
for nn in range(1, 8):
    ax.add_patch(plt.Rectangle((nn, 0), 1, fx(nn), fill=True, alpha=0.18, color=ROSSO, ec=ROSSO, lw=0.8))
    ax.add_patch(plt.Rectangle((nn, 0), 1, fx(nn + 1), fill=True, alpha=0.35, color=BLU, ec=BLU, lw=0.8))
ax.plot(xs, fx(xs), color="black", lw=1.5, label="$y = f(x)$")
ax.set_xticks(range(1, 9)); ax.set_xticklabels(["$n_0$"] + [f"$n_0+{i}$" for i in range(1, 8)], fontsize=8)
ax.set_yticks([]); ax.spines[["top", "right"]].set_visible(False)
ax.text(5.2, 0.55, "rettangoli di altezza $f(n)$: sopra il grafico\nrettangoli di altezza $f(n+1)$: sotto il grafico", fontsize=8)
salva(fig, "2-1")

# 3-1 curve di livello di paraboloide e cono
X, Y = np.meshgrid(np.linspace(-2, 2, 300), np.linspace(-2, 2, 300))
fig, axs = plt.subplots(1, 2, figsize=(7, 3.5))
for ax, Z, tit in [(axs[0], X**2 + Y**2, "$f = x^2 + y^2$ (paraboloide)"), (axs[1], np.sqrt(X**2 + Y**2), "$f = \\sqrt{x^2 + y^2}$ (cono)")]:
    lv = [0.5 * i for i in range(1, 8)] if "sqrt" in tit else [0.5 * i for i in range(1, 8)]
    cs = ax.contour(X, Y, Z, levels=lv, colors=BLU, linewidths=1)
    ax.clabel(cs, fontsize=7, fmt="%.1f")
    ax.set_aspect("equal"); ax.set_title(tit, fontsize=9); ax.set_xticks([]); ax.set_yticks([])
    ax.axhline(0, color="gray", lw=0.5); ax.axvline(0, color="gray", lw=0.5)
salva(fig, "3-1")
print("figure fatte")
