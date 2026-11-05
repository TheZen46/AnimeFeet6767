"""Piccola libreria per disegnare in SVG gli schemi del corso (datapath, memorie, ALU).

Le figure si generano con `python3 strumenti/figure.py`; ogni figura e' una funzione.
Convenzioni: dati in nero, controllo in blu tratteggiato, parti nuove in arancio.
"""
from xml.sax.saxutils import escape

NERO, BLU, ARANCIO, GRIGIO = "#1f2328", "#1f5fbf", "#c0561b", "#e6e8eb"
FONT = "DejaVu Sans, Arial, Helvetica, sans-serif"
MONO = "DejaVu Sans Mono, Consolas, monospace"


class Fig:
    def __init__(self, w, h):
        self.w, self.h, self.el = w, h, []

    # --- forme
    def box(self, x, y, w, h, t=None, fill="#fff", r=3, size=12, col=NERO, dash=False, lw=1.4, tcol=None):
        d = ' stroke-dasharray="5 3"' if dash else ""
        self.el.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{col}" stroke-width="{lw}"{d}/>')
        if t:
            righe = t.split("\n")
            y0 = y + h / 2 - (len(righe) - 1) * size * 0.6
            for i, r_ in enumerate(righe):
                self.t(x + w / 2, y0 + i * size * 1.2 + size * .36, r_, size, "middle", col=tcol or col)

    def ell(self, cx, cy, rx, ry, t=None, size=11, col=NERO, fill="#fff", tcol=None):
        self.el.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{col}" stroke-width="1.4"/>')
        if t:
            righe = t.split("\n")
            y0 = cy - (len(righe) - 1) * size * 0.6
            for i, r_ in enumerate(righe):
                self.t(cx, y0 + i * size * 1.2 + size * .36, r_, size, "middle", col=tcol or col)

    def mux(self, x, y, h, ins=("0", "1"), w=20, col=NERO, fill="#fff", ys=None):
        """Multiplexer verticale: ingressi a sinistra, uscita a destra. Restituisce le y degli ingressi e l'uscita."""
        k = min(10, h / 5)
        self.el.append(f'<polygon points="{x},{y} {x + w},{y + k} {x + w},{y + h - k} {x},{y + h}" fill="{fill}" stroke="{col}" stroke-width="1.4"/>')
        n = len(ins)
        ys = ys or [y + h * (i + 1) / (n + 1) for i in range(n)]
        for yy, s in zip(ys, ins):
            self.t(x + 4, yy + 3.5, s, 9.5, col=col)
        return ys, (x + w, y + h / 2)

    def alu(self, x, y, w, h, t="ALU", size=12, col=NERO, simbolo=False, fill="#fff"):
        p = [(x, y), (x + w, y + h * .3), (x + w, y + h * .7), (x, y + h), (x, y + h * .58), (x + w * .28, y + h / 2), (x, y + h * .42)]
        pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in p)
        self.el.append(f'<polygon points="{pts}" fill="{fill}" stroke="{col}" stroke-width="1.4"/>')
        if t:
            self.t(x + w * .62, y + h / 2 + size * .35, t, size, "middle", bold=not simbolo, col=col)
        return (x, y + h * .21), (x, y + h * .79), (x + w, y + h / 2)

    def gate_and(self, x, y, w=24, h=20, col=NERO):
        r = h / 2
        self.el.append(f'<path d="M{x},{y} h{w - r} a{r},{r} 0 0 1 0,{h} h{-(w - r)} z" fill="#fff" stroke="{col}" stroke-width="1.4"/>')
        return (x, y + h * .28), (x, y + h * .72), (x + w, y + h / 2)

    def gate_or(self, x, y, w=26, h=20, col=NERO):
        self.el.append(f'<path d="M{x},{y} Q{x + w * .55},{y} {x + w},{y + h / 2} Q{x + w * .55},{y + h} {x},{y + h} Q{x + w * .3},{y + h / 2} {x},{y} z" fill="#fff" stroke="{col}" stroke-width="1.4"/>')
        return (x + 4, y + h * .28), (x + 4, y + h * .72), (x + w, y + h / 2)

    def gate_nor(self, x, y, w=26, h=20, col=NERO):
        a, b, o = self.gate_or(x, y, w, h, col)
        self.el.append(f'<circle cx="{x + w + 3.5}" cy="{y + h / 2}" r="3.5" fill="#fff" stroke="{col}" stroke-width="1.3"/>')
        return a, b, (x + w + 7, y + h / 2)

    def gate_not(self, x, y, w=16, h=14, col=NERO):
        self.el.append(f'<polygon points="{x},{y} {x + w},{y + h / 2} {x},{y + h}" fill="#fff" stroke="{col}" stroke-width="1.3"/>')
        self.el.append(f'<circle cx="{x + w + 3}" cy="{y + h / 2}" r="3" fill="#fff" stroke="{col}" stroke-width="1.3"/>')
        return (x, y + h / 2), (x + w + 6, y + h / 2)

    def preg(self, x, y, h, t, w=14, col=NERO):
        self.box(x, y, w, h, None, fill=GRIGIO, r=1, col=col)
        self.t(x + w / 2, y - 6, t, 10.5, "middle", bold=True, col=col)

    # --- linee e testi
    def wire(self, pts, arrow=True, ctrl=False, col=None, lw=1.3, dash=None):
        col = col or (BLU if ctrl else NERO)
        mk = {NERO: "a", BLU: "b", ARANCIO: "c"}.get(col, "a")
        d = ' stroke-dasharray="4 3"' if (ctrl or dash) else ""
        p = " ".join(f"{a},{b}" for a, b in pts)
        m = f' marker-end="url(#{mk})"' if arrow else ""
        self.el.append(f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{lw}"{d}{m}/>')

    def dot(self, x, y, col=NERO):
        self.el.append(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{col}"/>')

    def t(self, x, y, s, size=11, anchor="start", it=False, col=NERO, bold=False, rot=None, mono=False, base=False):
        st = ' font-style="italic"' if it else ""
        st += ' font-weight="bold"' if bold else ""
        fam = MONO if mono else FONT
        tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
        bl = ' dominant-baseline="middle"' if base else ""
        self.el.append(f'<text x="{x}" y="{y}" font-size="{size}" font-family="{fam}" text-anchor="{anchor}" fill="{col}"{st}{bl}{tr}>{escape(s)}</text>')

    def raw(self, s):
        self.el.append(s)

    def svg(self):
        defs = "".join(
            f'<marker id="{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,1 L10,5 L0,9 z" fill="{c}"/></marker>'
            for k, c in (("a", NERO), ("b", BLU), ("c", ARANCIO)))
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}">'
                f'<defs>{defs}</defs><rect width="100%" height="100%" fill="#fff"/>' + "\n".join(self.el) + "</svg>\n")

    def salva(self, percorso):
        with open(percorso, "w", encoding="utf-8") as f:
            f.write(self.svg())
