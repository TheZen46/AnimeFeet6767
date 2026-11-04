# Figure di Reti Logiche, ridisegnate (nessuna figura del docente o del libro).
# uso: python3 figure.py <cartella-uscita> [nome ...]   (ANTEPRIMA=1 salva anche i PNG)
import sys, os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.fonttype"] = "path"
matplotlib.rcParams["font.family"] = "DejaVu Sans"
import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic
import schemdraw.flow as flow

schemdraw.use("matplotlib")
schemdraw.config(fontsize=11, lw=1.3)
OUT = sys.argv[1] if len(sys.argv) > 1 else "figure"
os.makedirs(OUT, exist_ok=True)
FIG = {}


def fig(nome):
    def reg(f):
        FIG[nome] = f
        return f
    return reg


def salva(d, nome):
    d.save(os.path.join(OUT, nome + ".svg"))
    if os.environ.get("ANTEPRIMA"):
        d.save(os.path.join(OUT, "_" + nome + ".png"), dpi=90)


def onda(segnali, nome, hscale=1.0, grid=False):
    """segnali: lista di dict in stile wavedrom."""
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=11)
        d += logic.TimingDiagram({"signal": segnali, "config": {"hscale": hscale}},
                                 ygap=0.35, risetime=0.12, grid=grid, color="black", namecolor="black")
    salva(d, nome)



def W(d, *pts, **kw):
    """filo per punti assoluti"""
    for a, b in zip(pts, pts[1:]):
        d += logic.Line(**kw).at(a).to(b)


def P(d, p):
    d += logic.Dot(radius=0.07).at(p)


def T(d, p, s, loc="center", fs=10, **kw):
    ha = {"left": "right", "right": "left", "center": "center", "top": "center", "bottom": "center"}[loc]
    va = {"top": "bottom", "bottom": "top"}.get(loc, "center")
    d += elm.Label().at(p).label(s, fontsize=fs, halign=ha, valign=va, **kw)


def box(d, x, y, w, h, testo="", fs=10, **kw):
    W(d, (x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y), **kw)
    if testo:
        T(d, (x + w / 2, y + h / 2), testo, fs=fs)


def trap(d, x, y, w, h, sl=0.5, testo="", fs=9):
    """MUX: lato sinistro alto h, destro h - 2 sl"""
    W(d, (x, y), (x + w, y + sl), (x + w, y + h - sl), (x, y + h), (x, y))
    if testo:
        T(d, (x + w / 2, y + h / 2), testo, fs=fs)

# ---------------------------------------------------------------- modulo 1
@fig("1-1")
def porte():
    with schemdraw.Drawing(show=False) as d:
        x = 0
        for nome, el in [("AND", logic.And()), ("OR", logic.Or()), ("NOT", logic.Not()),
                         ("NAND", logic.Nand()), ("NOR", logic.Nor()),
                         ("XOR", logic.Xor()), ("XNOR", logic.Xnor())]:
            d += el.at((x, 0)).right().label(nome, loc="bottom", ofst=0.5)
            x += 3.2
    salva(d, "1-1")


@fig("1-2")
def nand_complete():
    def nandnot(d, x, y):
        g = d.add(logic.Nand().anchor("in1").at((x, y)))
        m = ((g.in1[0] - 0.35), (g.in1[1] + g.in2[1]) / 2)
        W(d, g.in1, (m[0], g.in1[1]), (m[0], g.in2[1]), g.in2)
        P(d, m)
        return g, m
    with schemdraw.Drawing(show=False) as d:
        g, m = nandnot(d, 1.0, 0.25)
        W(d, (0, m[1]), m); T(d, (0, m[1]), "A", "left")
        W(d, g.out, (g.out[0] + 0.6, g.out[1])); T(d, (g.out[0] + 0.6, g.out[1]), r"$\overline{A}$", "right")
        T(d, (1.8, -1.3), "NOT")
        g1 = d.add(logic.Nand().anchor("in1").at((5.5, 0.5)))
        W(d, (4.6, g1.in1[1]), g1.in1); T(d, (4.6, g1.in1[1]), "A", "left")
        W(d, (4.6, g1.in2[1]), g1.in2); T(d, (4.6, g1.in2[1]), "B", "left")
        g2, m2 = nandnot(d, g1.out[0] + 0.9, g1.out[1] + 0.25)
        W(d, g1.out, m2)
        W(d, g2.out, (g2.out[0] + 0.6, g2.out[1])); T(d, (g2.out[0] + 0.6, g2.out[1]), "AB", "right")
        T(d, (7.3, -1.3), "AND")
        n1, a = nandnot(d, 13.0, 1.4)
        n2, b = nandnot(d, 13.0, -0.6)
        W(d, (12.2, a[1]), a); T(d, (12.2, a[1]), "A", "left")
        W(d, (12.2, b[1]), b); T(d, (12.2, b[1]), "B", "left")
        g3 = d.add(logic.Nand().anchor("out").at((n1.out[0] + 3.0, (n1.out[1] + n2.out[1]) / 2)))
        xm = n1.out[0] + 0.6
        W(d, n1.out, (xm, n1.out[1]), (xm, g3.in1[1]), g3.in1)
        W(d, n2.out, (xm, n2.out[1]), (xm, g3.in2[1]), g3.in2)
        W(d, g3.out, (g3.out[0] + 0.6, g3.out[1])); T(d, (g3.out[0] + 0.6, g3.out[1]), "A+B", "right")
        T(d, (15.0, -2.2), "OR")
    salva(d, "1-2")


@fig("2-1")
def mux_porte():
    with schemdraw.Drawing(show=False) as d:
        a1 = d.add(logic.And().anchor("out").at((5.5, 1.2)))
        a2 = d.add(logic.And().anchor("out").at((5.5, -1.2)))
        o = d.add(logic.Or().anchor("out").at((8.5, 0)))
        W(d, a1.out, (6.4, a1.out[1]), (6.4, o.in1[1]), o.in1)
        W(d, a2.out, (6.4, a2.out[1]), (6.4, o.in2[1]), o.in2)
        W(d, o.out, (o.out[0] + 0.6, 0)); T(d, (o.out[0] + 0.6, 0), "U", "right")
        W(d, (0, a1.in1[1]), a1.in1); T(d, (0, a1.in1[1]), "$S_0$", "left")
        W(d, (0, a2.in1[1]), a2.in1); T(d, (0, a2.in1[1]), "$S_1$", "left")
        n = d.add(logic.Not().up().anchor("in1").at((1.4, a2.in1[1] + 0.3)).scale(0.7))
        W(d, (0, -2.8), (1.4, -2.8), (1.4, a2.in2[1]), a2.in2); T(d, (0, -2.8), "SEL", "left")
        P(d, (1.4, a2.in2[1]))
        W(d, (1.4, a2.in2[1]), n.in1)
        W(d, n.out, (1.4, a1.in2[1]), a1.in2)
    salva(d, "2-1")


@fig("2-2")
def mux_da_mux():
    with schemdraw.Drawing(show=False) as d:
        for (x, y, a, b) in [(1, 1.5, "$I_0$", "$I_1$"), (1, -2.5, "$I_2$", "$I_3$")]:
            trap(d, x, y, 1.6, 2.4, 0.5, "MUX\n2→1")
            W(d, (0, y + 1.6), (x, y + 1.6)); T(d, (0, y + 1.6), a, "left"); T(d, (x + 0.15, y + 1.6), "0", "right", fs=8)
            W(d, (0, y + 0.8), (x, y + 0.8)); T(d, (0, y + 0.8), b, "left"); T(d, (x + 0.15, y + 0.8), "1", "right", fs=8)
        trap(d, 5, -0.5, 1.6, 2.4, 0.5, "MUX\n2→1")
        T(d, (5.15, 1.1), "0", "right", fs=8); T(d, (5.15, 0.3), "1", "right", fs=8)
        W(d, (2.6, 2.7), (3.6, 2.7), (3.6, 1.1), (5, 1.1))
        W(d, (2.6, -1.3), (4.0, -1.3), (4.0, 0.3), (5, 0.3))
        W(d, (6.6, 0.7), (7.4, 0.7)); T(d, (7.4, 0.7), "U", "right")
        W(d, (0, -3.6), (1.8, -3.6), (1.8, -2.25)); T(d, (0, -3.6), "$S_0$", "left"); P(d, (1.8, -3.6))
        W(d, (1.8, -3.6), (3.0, -3.6), (3.0, 0.9), (1.8, 0.9), (1.8, 1.75))
        W(d, (0, -4.2), (5.8, -4.2), (5.8, -0.25)); T(d, (0, -4.2), "$S_1$", "left")
    salva(d, "2-2")


@fig("2-3")
def xor_mux():
    with schemdraw.Drawing(show=False) as d:
        trap(d, 1, 0, 2.0, 4.0, 0.6, "MUX\n4→1")
        for k, v in enumerate("0110"):
            y = 3.4 - k * 0.9
            W(d, (0, y), (1, y)); T(d, (0, y), v, "left"); T(d, (1.15, y), f"$I_{k}$", "right", fs=8)
        W(d, (3, 2.0), (3.8, 2.0)); T(d, (3.8, 2.0), r"$A \oplus B$", "right")
        W(d, (1.6, 0.18), (1.6, -0.6)); T(d, (1.6, -0.6), "$S_1 = A$", "bottom", fs=9)
        W(d, (2.5, 0.45), (2.5, -1.1)); T(d, (2.6, -1.1), "$S_0 = B$", "bottom", fs=9)
    salva(d, "2-3")


@fig("2-4")
def alea_not():
    onda([{"name": "IN", "wave": "1...0...."},
          {"name": "IN negato", "wave": "0....1..."},
          {"name": "OUT ideale", "wave": "1........"},
          {"name": "OUT reale", "wave": "1...01..."}], "2-4", hscale=1)


@fig("2-5")
def consenso():
    with schemdraw.Drawing(show=False) as d:
        a1 = d.add(logic.And().at((3, 2.2)).right())
        a2 = d.add(logic.And().at((3, 0)).right())
        a3 = d.add(logic.And().at((3, -2.2)).right().color("#b8860b"))
        o = d.add(logic.Or(inputs=3).at((6.2, 0)).right().anchor("in2"))
        d += logic.Wire("-|").at(a1.out).to(o.in1)
        d += logic.Line().at(a2.out).to(o.in2)
        d += logic.Wire("-|").at(a3.out).to(o.in3).color("#b8860b")
        d += logic.Line().at(o.out).right(0.5).label("U", "right")
        d += logic.Line().at(a1.in1).left(1.2).label(r"$\overline{A}$", "left")
        d += logic.Line().at(a1.in2).left(1.2).label("B", "left")
        d += logic.Line().at(a2.in1).left(1.2).label("A", "left")
        d += logic.Line().at(a2.in2).left(1.2).label("C", "left")
        d += logic.Line().at(a3.in1).left(1.2).label("B", "left")
        d += logic.Line().at(a3.in2).left(1.2).label("C", "left")
        d += elm.Label().at((a3.out[0] + 0.3, -3.3)).label("termine di consenso BC", fontsize=9, color="#b8860b")
    salva(d, "2-5")


@fig("2-6")
def adder():
    with schemdraw.Drawing(show=False) as d:
        x1 = d.add(logic.Xor().anchor("in1").at((1.5, 1.2)))
        a1 = d.add(logic.And().anchor("in1").at((1.5, -0.8)))
        W(d, (0, x1.in1[1]), x1.in1); T(d, (0, x1.in1[1]), "A", "left")
        W(d, (0, x1.in2[1]), x1.in2); T(d, (0, x1.in2[1]), "B", "left")
        P(d, (0.5, x1.in1[1])); W(d, (0.5, x1.in1[1]), (0.5, a1.in1[1]), a1.in1)
        P(d, (0.9, x1.in2[1])); W(d, (0.9, x1.in2[1]), (0.9, a1.in2[1]), a1.in2)
        W(d, x1.out, (x1.out[0] + 0.5, x1.out[1])); T(d, (x1.out[0] + 0.5, x1.out[1]), "S", "right")
        W(d, a1.out, (a1.out[0] + 0.5, a1.out[1])); T(d, (a1.out[0] + 0.5, a1.out[1]), "C", "right")
        T(d, (2.5, -2.3), "half adder")
        ox = 7.0
        xa = d.add(logic.Xor().anchor("in1").at((ox + 1.6, 2.0)))
        W(d, (ox, xa.in1[1]), xa.in1); T(d, (ox, xa.in1[1]), "A", "left")
        W(d, (ox, xa.in2[1]), xa.in2); T(d, (ox, xa.in2[1]), "B", "left")
        xo = xa.out[0]
        xb = d.add(logic.Xor().anchor("in1").at((xo + 1.6, xa.out[1])))
        W(d, xa.out, xb.in1)
        cy = xa.in2[1] - 1.0
        W(d, (ox, cy), (xo + 1.0, cy), (xo + 1.0, xb.in2[1]), xb.in2); T(d, (ox, cy), "$C_{in}$", "left")
        W(d, xb.out, (xb.out[0] + 0.5, xb.out[1])); T(d, (xb.out[0] + 0.5, xb.out[1]), "S", "right")
        b1 = d.add(logic.And().anchor("in1").at((xo + 1.6, cy - 1.0)))
        b2 = d.add(logic.And().anchor("in1").at((xo + 1.6, cy - 2.6)))
        P(d, (xo + 1.0, cy)); W(d, (xo + 1.0, cy), (xo + 1.0, b1.in1[1]), b1.in1)
        P(d, (xo + 0.4, xa.out[1])); W(d, (xo + 0.4, xa.out[1]), (xo + 0.4, b1.in2[1]), b1.in2)
        P(d, (ox + 0.4, xa.in1[1])); W(d, (ox + 0.4, xa.in1[1]), (ox + 0.4, b2.in1[1]), b2.in1)
        P(d, (ox + 0.8, xa.in2[1])); W(d, (ox + 0.8, xa.in2[1]), (ox + 0.8, b2.in2[1]), b2.in2)
        o = d.add(logic.Or().anchor("out").at((b1.out[0] + 2.4, (b1.out[1] + b2.out[1]) / 2)))
        xm = b1.out[0] + 0.5
        W(d, b1.out, (xm, b1.out[1]), (xm, o.in1[1]), o.in1)
        W(d, b2.out, (xm, b2.out[1]), (xm, o.in2[1]), o.in2)
        W(d, o.out, (o.out[0] + 0.5, o.out[1])); T(d, (o.out[0] + 0.5, o.out[1]), "$C_{out}$", "right")
        T(d, (ox + 4.0, b2.in2[1] - 1.0), "full adder")
    salva(d, "2-6")


def blocco(d, xy, w, h, testo, fs=10):
    box(d, xy[0], xy[1], w, h, testo, fs)


@fig("2-7")
def ripple():
    with schemdraw.Drawing(show=False) as d:
        for i in range(4):
            x = (3 - i) * 3.0
            blocco(d, (x, 0), 2.0, 1.6, "FA")
            d += logic.Line().at((x + 0.6, 1.6)).up(0.8).label(f"$A_{i}$", "top")
            d += logic.Line().at((x + 1.4, 1.6)).up(0.8).label(f"$B_{i}$", "top")
            d += logic.Line().at((x + 1.0, 0)).down(0.8).label(f"$S_{i}$", "bottom")
            if i < 3:
                d += elm.Arrow().at((x, 0.8)).left(1.0)
        d += elm.Arrow().at((12.0, 0.8)).left(1.0).label("$C_{in}=0$", "top", ofst=0.1)
        d += elm.Arrow().at((0, 0.8)).left(1.0).label("$C_{out}$", "top", ofst=0.1)
        d += elm.Label().at((7.0, -1.9)).label("il riporto attraversa gli stadi da destra a sinistra", fontsize=9)
    salva(d, "2-7")


@fig("2-8")
def alu():
    with schemdraw.Drawing(show=False) as d:
        ys = [2.0, 0.0, -2.0]
        for y, t in zip(ys, ["ADD", "MULT", "CMP"]):
            box(d, 2.0, y, 1.8, 1.2, t)
            W(d, (0.6, y + 0.9), (2.0, y + 0.9)); P(d, (0.6, y + 0.9))
            W(d, (1.1, y + 0.3), (2.0, y + 0.3)); P(d, (1.1, y + 0.3))
            W(d, (3.8, y + 0.6), (5.5, y + 0.6))
        W(d, (0.6, 3.6), (0.6, -1.1)); T(d, (0.6, 3.6), "A", "top")
        W(d, (1.1, 3.6), (1.1, -1.7)); T(d, (1.1, 3.6), "B", "top")
        trap(d, 5.5, -2.2, 1.6, 5.6, 0.6, "MUX")
        for k, y in enumerate(ys):
            T(d, (5.62, y + 0.6), str(k), "right", fs=8)
        W(d, (7.1, 0.6), (7.9, 0.6)); T(d, (7.9, 0.6), "risultato", "right")
        W(d, (6.0, -2.01), (6.0, -2.8)); T(d, (6.0, -2.8), "$S_1$", "bottom")
        W(d, (6.6, -1.79), (6.6, -2.8)); T(d, (6.6, -2.8), "$S_0$", "bottom")
    salva(d, "2-8")


# ---------------------------------------------------------------- modulo 3
@fig("3-1")
def latch_nor():
    with schemdraw.Drawing(show=False) as d:
        n1 = d.add(logic.Nor().anchor("out").at((5, 1.6)))
        n2 = d.add(logic.Nor().anchor("out").at((5, -1.6)))
        W(d, (0.5, n1.in1[1]), n1.in1); T(d, (0.5, n1.in1[1]), "R", "left")
        W(d, (0.5, n2.in2[1]), n2.in2); T(d, (0.5, n2.in2[1]), "S", "left")
        W(d, n1.out, (6.6, 1.6)); T(d, (6.6, 1.6), "Q", "right")
        W(d, n2.out, (6.6, -1.6)); T(d, (6.6, -1.6), r"$\overline{Q}$", "right")
        P(d, (5.6, 1.6)); W(d, (5.6, 1.6), (5.6, 0.4), (n2.in1[0] - 0.5, -0.4), (n2.in1[0] - 0.5, n2.in1[1]), n2.in1)
        P(d, (6.0, -1.6)); W(d, (6.0, -1.6), (6.0, -0.4), (n1.in2[0] - 0.9, 0.4), (n1.in2[0] - 0.9, n1.in2[1]), n1.in2)
    salva(d, "3-1")


@fig("3-2")
def sr_onde():
    onda([{"name": "S", "wave": "010....1.0."},
          {"name": "R", "wave": "0...10.1.0."},
          {"name": "Q", "wave": "x1..0....x."},
          {"name": "Q negato", "wave": "x0..1..0.x."}], "3-2")


@fig("3-3")
def latch_d():
    with schemdraw.Drawing(show=False) as d:
        g1 = d.add(logic.Nand().anchor("out").at((4.5, 1.6)))
        g2 = d.add(logic.Nand().anchor("out").at((4.5, -1.6)))
        W(d, (0, g1.in1[1]), g1.in1); T(d, (0, g1.in1[1]), "D", "left")
        P(d, (0.6, g1.in1[1]))
        n = d.add(logic.Not().down().anchor("in1").at((0.6, g1.in1[1] - 0.4)).scale(0.7))
        W(d, (0.6, g1.in1[1]), n.in1)
        W(d, n.out, (0.6, g2.in2[1]), g2.in2)
        ey = 0.0
        W(d, (0, ey), (1.6, ey)); T(d, (0, ey), "EN", "left"); P(d, (1.6, ey))
        W(d, (1.6, ey), (1.6, g1.in2[1]), g1.in2)
        W(d, (1.6, ey), (1.6, g2.in1[1]), g2.in1)
        box(d, 6.0, -2.4, 2.6, 4.8, "latch SR\n(NAND)", fs=9)
        W(d, g1.out, (6.0, 1.6)); T(d, (6.15, 1.6), r"$\overline{S}$", "right", fs=9)
        W(d, g2.out, (6.0, -1.6)); T(d, (6.15, -1.6), r"$\overline{R}$", "right", fs=9)
        W(d, (8.6, 1.6), (9.4, 1.6)); T(d, (9.4, 1.6), "Q", "right")
        W(d, (8.6, -1.6), (9.4, -1.6)); T(d, (9.4, -1.6), r"$\overline{Q}$", "right")
    salva(d, "3-3")


def frecciad(d, x0, x1, y, testo):
    d += elm.Line(arrow="<->").at((x0, y)).to((x1, y))
    T(d, ((x0 + x1) / 2, y + 0.05), testo, "top", fs=10)


@fig("3-4")
def tempi():
    with schemdraw.Drawing(show=False) as d:
        h = 0.8
        # CK
        W(d, (0, 4), (4, 4), (4, 4 + h), (7, 4 + h), (7, 4), (10, 4), (10, 4 + h), (11.5, 4 + h))
        T(d, (-0.3, 4.4), "CK", "left")
        # D
        W(d, (0, 2), (2.4, 2), (2.6, 2 + h), (8.4, 2 + h), (8.6, 2), (11.5, 2))
        T(d, (-0.3, 2.4), "D", "left")
        # Q
        W(d, (0, 0), (4.7, 0), (4.9, h), (11.5, h))
        T(d, (-0.3, 0.4), "Q", "left")
        for x, y0, y1 in [(4, -0.3, 4 + h), (2.5, 2, 3.3), (5.4, 1.6, 2 + h)]:
            d += elm.Line(ls=":").at((x, y0)).to((x, y1))
        frecciad(d, 2.5, 4, 3.1, "$t_s$")
        frecciad(d, 4, 5.4, 1.5, "$t_h$")
        frecciad(d, 4, 4.8, -0.5, "$t_p$")
        frecciad(d, 4, 7, 5.2, "$t_w$")
        frecciad(d, 4, 10, 6.2, "$T_{CK} \\geq T_{min}$")
        d += elm.Line(ls=":").at((10, 4)).to((10, 6.2))
        d += elm.Line(ls=":").at((4, 4 + h)).to((4, 6.2))
    salva(d, "3-4")


def ff(d, x, y, ing="D", nome="", w=1.4, h=2.0, ck=True):
    box(d, x, y, w, h)
    T(d, (x + 0.12, y + 1.5), ing, "right", fs=9)
    T(d, (x + w - 0.12, y + 1.5), "Q", "left", fs=9)
    if ck:
        W(d, (x, y + 0.35), (x + 0.25, y + 0.5), (x, y + 0.65))
    if nome:
        T(d, (x + w / 2, y - 0.1), nome, "bottom", fs=8)
    return (x, y + 1.5), (x + w, y + 1.5), (x, y + 0.5)


@fig("3-5")
def siso():
    with schemdraw.Drawing(show=False) as d:
        xs = [1.5, 4.5, 7.5, 10.5]
        prev = None
        for i, x in enumerate(xs):
            din, q, ck = ff(d, x, 0, "D")
            if prev is None:
                W(d, (0, din[1]), din); T(d, (0, din[1]), "$S_{in}$", "left")
            else:
                W(d, prev, din)
            P(d, (q[0] + 0.5, q[1])); W(d, (q[0] + 0.5, q[1]), (q[0] + 0.5, q[1] + 1.0)); T(d, (q[0] + 0.5, q[1] + 1.0), f"$Q_{3 - i}$" if False else f"$Q_{i}$", "top", fs=9)
            W(d, (x - 0.4, -1.0), (x - 0.4, ck[1]), ck); P(d, (x - 0.4, -1.0))
            prev = (q[0] + 0.5, q[1])
        W(d, q, (13.6, q[1])); T(d, (13.6, q[1]), "$S_{out}$", "right")
        W(d, (0, -1.0), (xs[-1] - 0.4, -1.0)); T(d, (0, -1.0), "CK", "left")
    salva(d, "3-5")


@fig("3-6")
def contatore_t():
    with schemdraw.Drawing(show=False) as d:
        xs = [1.5, 6.3, 11.1, 15.9]
        rails = [3.8, 4.4, 5.0]
        outs = []
        for i, x in enumerate(xs):
            t, q, ck = ff(d, x, 0, "T")
            outs.append((t, q))
            W(d, (x - 0.4, -1.0), (x - 0.4, ck[1]), ck); P(d, (x - 0.4, -1.0))
            if i < 3:
                W(d, q, (q[0] + 0.3, q[1]), (q[0] + 0.3, rails[i]), (18.8, rails[i]))
                P(d, (q[0] + 0.3, q[1]))
                T(d, (18.8, rails[i]), f"$Q_{i}$", "right", fs=9)
            else:
                W(d, q, (18.8, q[1])); T(d, (18.8, q[1]), "$Q_3$", "right", fs=9)
        W(d, (-0.2, -1.0), (xs[-1] - 0.4, -1.0)); T(d, (-0.2, -1.0), "CK", "left")
        W(d, (0.6, outs[0][0][1]), outs[0][0]); T(d, (0.6, outs[0][0][1]), "1", "left")
        t1 = outs[1][0]
        W(d, (t1[0] - 0.8, rails[0]), (t1[0] - 0.8, t1[1]), t1); P(d, (t1[0] - 0.8, rails[0]))
        for k, ni in [(2, 2), (3, 3)]:
            tk = outs[k][0]
            g = d.add(logic.And(inputs=ni).anchor("out").at((tk[0] - 0.3, 2.6)).scale(0.8))
            W(d, g.out, (tk[0] - 0.3, tk[1]), tk)
            ins = [g.in1, g.in2] + ([g.in3] if ni == 3 else [])
            for j, p in enumerate(ins):
                r = rails[ni - 1 - j]
                xv = p[0] - 0.25 - 0.25 * j
                W(d, (xv, r), (xv, p[1]), p); P(d, (xv, r))
    salva(d, "3-6")


@fig("3-7")
def contatore4_onde():
    with schemdraw.Drawing(show=False) as d:
        d += logic.TimingDiagram({"signal": [
            {"name": "CK", "wave": "P........"},
            {"name": "Q0 = U0", "wave": "010101010"},
            {"name": "Q1 = U1", "wave": "0.1.0.1.0"},
            {"name": "TC", "wave": "0..10..10"},
            {"name": "stato", "wave": "=========", "data": ["0", "1", "2", "3", "0", "1", "2", "3", "0"]}]},
            ygap=0.35, risetime=0.08, color="black", namecolor="black")
    salva(d, "3-7")


@fig("3-8")
def lfsr():
    with schemdraw.Drawing(show=False) as d:
        xs = [3.0, 6.0, 9.0, 12.0]
        nomi = ["D", "C", "B", "A"]
        taps = []
        prev = None
        for i, x in enumerate(xs):
            din, q, ck = ff(d, x, 0, "D")
            if prev is not None:
                W(d, prev, din)
            else:
                first = din
            tp = (q[0] + 0.4, q[1])
            P(d, tp); taps.append(tp)
            W(d, q, tp)
            W(d, tp, (tp[0], -0.6 - 0.0)); T(d, (tp[0], -0.6), nomi[i], "bottom", fs=10)
            W(d, (x - 0.4, -1.6), (x - 0.4, ck[1]), ck); P(d, (x - 0.4, -1.6))
            prev = tp
        W(d, (0.6, -1.6), (xs[-1] - 0.4, -1.6)); T(d, (0.6, -1.6), "CK", "left")
        fx = d.add(logic.Xor().left().anchor("out").at((11.4, 4.0)))
        hi, lo = (fx.in1, fx.in2) if fx.in1[1] > fx.in2[1] else (fx.in2, fx.in1)
        W(d, taps[3], (taps[3][0], lo[1]), lo)
        W(d, taps[2], (taps[2][0], 5.4), (taps[3][0] + 0.6, 5.4), (taps[3][0] + 0.6, hi[1]), hi)
        gx = d.add(logic.Xor().right().anchor("out").at((first[0] - 0.6, first[1])))
        W(d, gx.out, first)
        top, bot = (gx.in1, gx.in2) if gx.in1[1] > gx.in2[1] else (gx.in2, gx.in1)
        W(d, fx.out, (top[0] - 0.4, fx.out[1]), (top[0] - 0.4, top[1]), top)
        W(d, (0.3, bot[1]), bot); T(d, (0.3, bot[1]), "IN", "left")
    salva(d, "3-8")


# ---------------------------------------------------------------- modulo 4
@fig("4-1")
def msf():
    with schemdraw.Drawing(show=False) as d:
        box(d, 1.6, 0, 3.0, 2.0, "rete dello\nstato successivo", fs=9)
        box(d, 6.2, 0, 1.6, 2.0, "registro\ndi stato", fs=9)
        box(d, 9.4, 0, 3.0, 2.0, "rete delle\nuscite", fs=9)
        d += elm.Arrow().at((0, 1.3)).to((1.6, 1.3)); T(d, (0, 1.3), "I", "left")
        d += elm.Arrow().at((4.6, 1.0)).to((6.2, 1.0)); T(d, (5.4, 1.05), "$X^+$", "top", fs=9)
        d += elm.Arrow().at((7.8, 1.0)).to((9.4, 1.0)); T(d, (8.6, 1.05), "X", "top", fs=9)
        d += elm.Arrow().at((12.4, 1.0)).to((13.8, 1.0)); T(d, (13.8, 1.0), "U", "right")
        P(d, (8.6, 1.0))
        W(d, (8.6, 1.0), (8.6, 2.8), (1.0, 2.8), (1.0, 1.7))
        d += elm.Arrow().at((1.0, 1.7)).to((1.6, 1.7))
        d += elm.Arrow().at((6.6, -1.0)).to((6.6, 0)); T(d, (6.6, -1.0), "CK", "bottom", fs=9)
        d += elm.Arrow().at((7.4, -1.0)).to((7.4, 0)); T(d, (7.5, -1.0), r"$\overline{RES}$", "bottom", fs=9)
        P(d, (0.6, 1.3))
        d += elm.Line(ls="--").at((0.6, 1.3)).to((0.6, -1.8))
        d += elm.Line(ls="--").at((0.6, -1.8)).to((10.9, -1.8))
        d += elm.Arrow(ls="--").at((10.9, -1.8)).to((10.9, 0))
        T(d, (11.0, -2.0), "solo nella macchina di Mealy", "bottom", fs=8)
    salva(d, "4-1")


def rombo(d, c, w=1.0, h=0.6, testo="", fs=9):
    x, y = c
    W(d, (x - w, y), (x, y + h), (x + w, y), (x, y - h), (x - w, y))
    if testo:
        T(d, c, testo, fs=fs)


def ovale(d, c, w=1.8, h=0.9, testo="", fs=9):
    d += elm.Ellipse(w=w, h=h).at((c[0] - w / 2, c[1])).anchor("W") if False else flow.Ellipse(w=w, h=h).at(c).anchor("center")
    if testo:
        T(d, c, testo, fs=fs)


def stato(d, x, y, w, h, uscite="", nome="", codice="", lato="right"):
    box(d, x, y, w, h, uscite, fs=9)
    if nome:
        if lato == "right":
            T(d, (x + w + 0.25, y + h / 2), nome, "right", fs=10)
        else:
            T(d, (x - 0.25, y + h / 2), nome, "left", fs=10)
    if codice:
        T(d, (x + w - 0.05, y + h + 0.05), codice, "top", fs=8)


def freccia(d, *pts):
    W(d, *pts[:-1])
    d += elm.Arrow().at(pts[-2]).to(pts[-1])


@fig("4-2")
def asm_elementi():
    with schemdraw.Drawing(show=False) as d:
        freccia(d, (1.2, 2.6), (1.2, 2.0))
        stato(d, 0, 1.0, 2.4, 1.0, "U", "a", "00")
        T(d, (1.2, 0.2), "blocco di stato", "bottom", fs=9)
        freccia(d, (5.5, 2.6), (5.5, 2.1))
        rombo(d, (5.5, 1.5), testo="IN")
        W(d, (6.5, 1.5), (7.1, 1.5)); T(d, (6.6, 1.55), "1", "top", fs=8)
        W(d, (5.5, 0.9), (5.5, 0.5)); T(d, (5.6, 0.75), "0", "right", fs=8)
        T(d, (5.5, 0.2), "blocco decisionale", "bottom", fs=9)
        freccia(d, (10.0, 2.6), (10.0, 1.95))
        ovale(d, (10.0, 1.5), testo="OUT")
        W(d, (10.0, 1.05), (10.0, 0.5))
        T(d, (10.0, 0.2), "uscita condizionata", "bottom", fs=9)
        T(d, (1.2, 2.75), "dallo stato precedente", "top", fs=8)
    salva(d, "4-2")


@fig("4-3")
def asm_mod4():
    with schemdraw.Drawing(show=False) as d:
        ys = [6.0, 4.0, 2.0, 0.0]
        usc = ["", "$U_0$", "$U_1$", "$TC\\ U_1\\ U_0$"]
        cod = ["00", "01", "10", "11"]
        for k, y in enumerate(ys):
            stato(d, 0, y, 2.4, 1.0, usc[k], str(k), cod[k])
            if k < 3:
                freccia(d, (1.2, y), (1.2, y - 1.0))
        W(d, (1.2, 0), (1.2, -0.5), (-1.0, -0.5), (-1.0, 7.6), (1.2, 7.6))
        d += elm.Arrow().at((1.2, 7.6)).to((1.2, 7.0))
        P(d, (-0.2, 7.6)); T(d, (-0.2, 7.7), "reset", "top", fs=8)
    salva(d, "4-3")


@fig("4-4")
def asm_updown():
    with schemdraw.Drawing(show=False) as d:
        n = 4
        ys = [12 - 4 * k for k in range(n)]
        usc = ["", "$U_0$", "$U_1$", "$U_1\\ U_0$"]
        for k, y in enumerate(ys):
            stato(d, -1.2, y - 1.0, 2.4, 1.0, usc[k], str(k), "", lato="left")
            freccia(d, (0, y - 1.0), (0, y - 1.4))
            rombo(d, (0, y - 2.0), testo="U/D")
            T(d, (0.1, y - 2.7), "1", "right", fs=8)
            T(d, (1.05, y - 1.95), "0", "top", fs=8)
            if k < n - 1:
                d += elm.Arrow().at((0, y - 2.6)).to((0, ys[k + 1]))
            lane = 2.0 + 0.6 * k
            prev = ys[(k - 1) % n]
            W(d, (1.0, y - 2.0), (lane, y - 2.0), (lane, prev - 0.5))
            d += elm.Arrow().at((lane, prev - 0.5)).to((1.2, prev - 0.5))
        yl = ys[-1] - 2.6
        W(d, (0, yl), (0, yl - 0.5), (-3.0, yl - 0.5), (-3.0, ys[0] + 0.6), (0, ys[0] + 0.6))
        d += elm.Arrow().at((0, ys[0] + 0.6)).to((0, ys[0]))
    salva(d, "4-4")


@fig("4-5")
def fronti_onde():
    onda([{"name": "CK", "wave": "lh" * 10},
          {"name": "IN", "wave": "0...1.......0......."},
          {"name": "stato (Moore)", "wave": "=....=.=.....=.=....", "data": ["a", "b", "c", "d", "a"]},
          {"name": "OUT (Moore)", "wave": "0....1.0.....1.0...."},
          {"name": "OUT (Mealy)", "wave": "0...10......10......"}], "4-5", hscale=0.5)


@fig("4-6")
def moore_mealy():
    onda([{"name": "CK", "wave": "lh" * 7},
          {"name": "IN1", "wave": "0.1..........."},
          {"name": "IN2", "wave": "0...1........."},
          {"name": "OUT (Mealy)", "wave": "0...1........."},
          {"name": "OUT (Moore)", "wave": "0....1........"}], "4-6", hscale=0.5)


@fig("4-7")
def datapath():
    with schemdraw.Drawing(show=False) as d:
        box(d, 0, 3.0, 2.6, 2.0, "FSM-A", fs=10)
        box(d, 7.0, 3.0, 2.6, 2.0, "FSM-B", fs=10)
        box(d, 0, -1.0, 2.6, 1.8, "CNT\n3 bit", fs=10)
        trap(d, 7.6, -1.6, 1.4, 3.0, 0.4, "MUX", fs=9)
        d += elm.Arrow().at((-1.6, 4.4)).to((0, 4.4)); T(d, (-1.6, 4.4), "IN", "left")
        d += elm.Arrow().at((0.8, 3.0)).to((0.8, 0.8)); T(d, (0.7, 1.9), "EN", "left", fs=9)
        d += elm.Arrow().at((1.8, 3.0)).to((1.8, 0.8)); T(d, (1.9, 1.9), "CL", "right", fs=9)
        d += elm.Arrow().at((2.6, 4.6)).to((7.0, 4.6)); T(d, (4.8, 4.65), "TRG", "top", fs=9)
        d += elm.Arrow().at((7.0, 3.6)).to((2.6, 3.6)); T(d, (4.8, 3.65), "ETX", "top", fs=9)
        d += elm.Arrow().at((1.3, 5.0)).to((1.3, 6.0)); T(d, (1.3, 6.0), "BSY", "top", fs=9)
        d += elm.Arrow().at((2.6, -0.1)).to((7.6, -0.1)); T(d, (5.1, -0.05), "$Q_2 Q_1 Q_0$", "top", fs=9)
        T(d, (5.1, -0.75), "e le costanti 1, 0", "top", fs=8)
        d += elm.Arrow().at((8.3, 3.0)).to((8.3, 1.3)); T(d, (8.4, 2.1), "selezione", "right", fs=9)
        d += elm.Arrow().at((9.0, -0.1)).to((10.4, -0.1)); T(d, (10.4, -0.1), "SER", "right")
        T(d, (1.3, -1.6), "datapath", "bottom", fs=8)
        T(d, (4.8, 5.6), "controllori", "top", fs=8)
    salva(d, "4-7")



if __name__ == "__main__":
    nomi = sys.argv[2:] or sorted(FIG)
    for n in nomi:
        FIG[n]()
        print("fatta", n)
