"""Genera gli schemi in figure/ (python3 strumenti/figure.py [nome ...])."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from disegno import Fig, BLU, ARANCIO, GRIGIO, NERO  # noqa: E402

QUI = os.path.join(os.path.dirname(__file__), "..", "figure")
FIG = {}


def figura(nome):
    def dec(f):
        FIG[nome] = f
        return f
    return dec


def ctrl(f, x, y, nome, verso="giu", lun=22, dx=0, anchor="start"):
    """Segnale di controllo: freccia tratteggiata corta con il nome."""
    if verso == "giu":
        f.wire([(x, y - lun), (x, y)], ctrl=True)
        f.t(x + 3 + dx, y - lun - 3, nome, 10, anchor, it=True, col=BLU)
    elif verso == "su":
        f.wire([(x, y + lun), (x, y)], ctrl=True)
        f.t(x + 3 + dx, y + lun + 10, nome, 10, anchor, it=True, col=BLU)
    elif verso == "sx":
        f.wire([(x - lun, y), (x, y)], ctrl=True)
        f.t(x - lun - 3, y + 3.5, nome, 10, "end", it=True, col=BLU)


def ciclo_singolo(f, ox=0, oy=0, evid=()):
    """Datapath a ciclo singolo (RV32I ridotto: R, lw, sw, beq). Restituisce i punti utili."""
    X = lambda x: x + ox  # noqa: E731
    Y = lambda y: y + oy  # noqa: E731
    # PC e PC+4
    f.box(X(30), Y(270), 40, 60, "PC")
    f.wire([(X(70), Y(300)), (X(120), Y(300))])
    f.dot(X(90), Y(300))
    a, b, o = f.alu(X(115), Y(50), 40, 70, "+", 16, simbolo=True)
    f.wire([(X(90), Y(300)), (X(90), Y(65)), a])
    f.t(X(96), Y(109), "4", 12, "end")
    f.wire([(X(100), b[1]), b])
    # memoria istruzioni
    f.box(X(120), Y(250), 105, 110, "Memoria\nistruzioni", size=11.5)
    f.t(X(124), Y(296), "ind.", 9)
    f.t(X(221), Y(296), "istr.", 9, "end")
    f.wire([(X(225), Y(300)), (X(255), Y(300))], arrow=False)
    # bus dell'istruzione
    f.wire([(X(255), Y(120)), (X(255), Y(500))], arrow=False)
    for yy, et in ((120, "[6:0]"), (270, "[19:15]"), (310, "[24:20]"), (350, "[11:7]"), (460, "[31:0]"), (500, "[30,14:12]")):
        f.dot(X(255), Y(yy))
        f.t(X(260), Y(yy - 4), et, 9, mono=True)
    # controllo
    f.ell(X(345), Y(120), 42, 34, "Unità di\ncontrollo", 11, col=BLU)
    f.wire([(X(255), Y(120)), (X(303), Y(120))])
    f.wire([(X(387), Y(120)), (X(410), Y(120))], ctrl=True)
    for i, r in enumerate(("Branch, MemRead,", "MemtoReg, ALUOp,", "MemWrite, ALUSrc,", "RegWrite")):
        f.t(X(414), Y(100 + 13 * i), r, 9, it=True, col=BLU)
    # banco dei registri
    f.box(X(320), Y(250), 125, 150, None)
    f.t(X(382), Y(325), "Banco dei", 11.5, "middle")
    f.t(X(382), Y(340), "registri", 11.5, "middle")
    for yy, et in ((270, "rs1"), (310, "rs2"), (350, "rd"), (385, "dato da scrivere")):
        f.t(X(325), Y(yy + 4), et, 9)
    f.t(X(440), Y(284), "dato 1", 9, "end")
    f.t(X(440), Y(354), "dato 2", 9, "end")
    for yy in (270, 310, 350):
        f.wire([(X(255), Y(yy)), (X(320), Y(yy))])
    ctrl(f, X(382), Y(250), "RegWrite")
    # generatore immediati
    f.ell(X(385), Y(460), 38, 22, "Gener.\nimmediati", 10)
    f.wire([(X(255), Y(460)), (X(347), Y(460))])
    # ALUSrc
    ys, mo = f.mux(X(490), Y(325), 85, ys=[Y(350), Y(385)])
    f.wire([(X(445), Y(350)), (X(490), ys[0])])
    f.dot(X(468), Y(350))
    f.wire([(X(423), Y(460)), (X(475), Y(460)), (X(475), ys[1]), (X(490), ys[1])])
    f.dot(X(475), Y(385))
    ctrl(f, X(500), Y(404), "ALUSrc", "su", 18)
    # ALU
    ia, ib, oa = f.alu(X(540), Y(240), 75, 160)
    f.wire([(X(445), Y(280)), (X(540), Y(280))])
    f.wire([mo, (X(530), mo[1]), (X(530), ib[1]), ib])
    f.t(X(612), Y(296), "Zero", 9, "end")
    f.t(X(612), Y(336), "risultato", 9, "end")
    # controllo ALU
    f.ell(X(578), Y(470), 38, 20, "Controllo\nALU", 9.5, col=BLU)
    f.wire([(X(255), Y(500)), (X(560), Y(500)), (X(560), Y(489))], ctrl=True)
    f.wire([(X(578), Y(450)), (X(578), Y(388))], ctrl=True)
    f.t(X(582), Y(430), "op. ALU (4 bit)", 9, it=True, col=BLU)
    ctrl(f, X(605), Y(482), "ALUOp", "su", 22, dx=-3)
    # salto: shift e sommatore
    f.ell(X(475), Y(195), 26, 15, "<< 1", 10)
    f.wire([(X(475), Y(385)), (X(475), Y(210))])
    a2, b2, o2 = f.alu(X(555), Y(110), 40, 80, "+", 16, simbolo=True)
    f.wire([(X(501), Y(195)), (X(540), Y(195)), (X(540), b2[1]), b2])
    f.wire([(X(90), Y(65)), (X(90), Y(30)), (X(535), Y(30)), (X(535), a2[1]), a2], arrow=True)
    f.dot(X(90), Y(65))
    # PCSrc
    ys2, mo2 = f.mux(X(680), Y(45), 85)
    f.wire([o, (X(170), Y(85)), (X(170), Y(15)), (X(660), Y(15)), (X(660), ys2[0]), (X(680), ys2[0])])
    f.wire([o2, (X(640), o2[1]), (X(640), ys2[1]), (X(680), ys2[1])])
    # Branch AND Zero
    g1, g2, go = f.gate_and(X(650), Y(200))
    f.wire([oa[0:1] + (Y(286),), (X(632), Y(286)), (X(632), g2[1]), g2])
    f.wire([(X(615), Y(286)), (X(632), Y(286))], arrow=False)
    f.wire([(X(622), g1[1]), g1], ctrl=True)
    f.t(X(588), g1[1] + 4, "Branch", 10, it=True, col=BLU)
    f.wire([go, (X(690), go[1]), (X(690), Y(122))], ctrl=True)
    f.t(X(694), Y(170), "PCSrc", 10, it=True, col=BLU)
    f.wire([mo2, (X(715), mo2[1]), (X(715), Y(5)), (X(15), Y(5)), (X(15), Y(300)), (X(30), Y(300))])
    # memoria dati
    f.box(X(700), Y(270), 105, 130, "Memoria\ndati", size=11.5)
    f.t(X(704), Y(316), "ind.", 9)
    f.t(X(704), Y(381), "dato da", 9)
    f.t(X(704), Y(391), "scrivere", 9)
    f.t(X(801), Y(326), "letto", 9, "end")
    f.wire([oa, (X(700), oa[1])])
    f.dot(X(660), oa[1])
    f.wire([(X(468), Y(350)), (X(468), Y(420)), (X(680), Y(420)), (X(680), Y(385)), (X(700), Y(385))])
    ctrl(f, X(752), Y(270), "MemWrite")
    ctrl(f, X(752), Y(400), "MemRead", "su", 20)
    # MemtoReg
    ys3, mo3 = f.mux(X(840), Y(295), 75, ("1", "0"))
    f.wire([(X(805), Y(320)), (X(840), ys3[0])])
    f.wire([(X(660), oa[1]), (X(660), Y(440)), (X(825), Y(440)), (X(825), ys3[1]), (X(840), ys3[1])])
    ctrl(f, X(850), Y(295), "MemtoReg", "giu", 36, dx=-6, anchor="end")
    f.wire([mo3, (X(880), mo3[1]), (X(880), Y(520)), (X(300), Y(520)), (X(300), Y(385)), (X(320), Y(385))])
    return {}


@figura("4-1")
def f4_1():
    f = Fig(900, 535)
    ciclo_singolo(f)
    return f


def pipeline(f, evid=False):
    """Datapath a pipeline di base (P&H, senza propagazione). Coordinate fisse."""
    # registri di pipeline
    for x, n in ((255, "IF/ID"), (520, "ID/EX"), (760, "EX/MEM"), (930, "MEM/WB")):
        f.preg(x, 75, 490, n)
    for x0, x1, n in ((20, 255, "IF"), (269, 520, "ID"), (534, 760, "EX"), (774, 930, "MEM"), (944, 1070, "WB")):
        f.t((x0 + x1) / 2, 650, n, 12, "middle", bold=True, col="#57606a")
    # IF
    ys, mo = f.mux(35, 285, 70, ys=[305, 335])
    f.box(70, 290, 38, 60, "PC")
    f.wire([mo, (70, 320)])
    f.wire([(108, 320), (135, 320)])
    f.dot(122, 320)
    a, b, o = f.alu(140, 85, 40, 70, "+", 15, simbolo=True)
    f.wire([(122, 320), (122, a[1]), a])
    f.t(131, b[1] - 4, "4", 11, "middle")
    f.wire([(127, b[1]), b])
    f.dot(122, 165)
    f.wire([(122, 165), (255, 165)])
    f.box(135, 270, 100, 100, "Memoria\nistruzioni", size=11)
    f.wire([(235, 320), (255, 320)])
    f.wire([o, (200, o[1]), (200, 40), (12, 40), (12, 305), (35, 305)])
    # ID
    f.wire([(269, 320), (285, 320)], arrow=False)
    f.wire([(285, 150), (285, 540)], arrow=False)
    for yy, et in ((150, "[6:0]"), (290, "[19:15]"), (330, "[24:20]"), (470, "[31:0]"), (510, "[30,14:12]"), (540, "[11:7]")):
        f.dot(285, yy)
        f.t(289, yy - 4, et, 8.5, mono=True)
    f.ell(370, 150, 38, 28, "Controllo", 10.5, col=BLU)
    f.wire([(285, 150), (332, 150)])
    f.box(335, 265, 115, 155, None)
    f.t(392, 340, "Banco dei", 11, "middle")
    f.t(392, 354, "registri", 11, "middle")
    for yy, et in ((290, "rs1"), (330, "rs2"), (370, "rd"), (400, "dato")):
        f.t(339, yy + 4, et, 9)
        if yy < 360:
            f.wire([(285, yy), (335, yy)])
    f.wire([(450, 300), (520, 300)])
    f.wire([(450, 360), (520, 360)])
    f.ell(390, 470, 36, 20, "Gener.\nimmediati", 9.5)
    f.wire([(285, 470), (354, 470)])
    f.wire([(426, 470), (520, 470)])
    f.wire([(285, 510), (520, 510)])
    f.wire([(285, 540), (520, 540)])
    f.wire([(269, 165), (520, 165)])
    # EX
    f.wire([(534, 165), (640, 165)])
    f.ell(575, 230, 22, 13, "<< 1", 9.5)
    a2, b2, o2 = f.alu(640, 150, 40, 70, "+", 15, simbolo=True)
    f.wire([(597, 230), (615, 230), (615, b2[1]), b2])
    f.wire([o2, (760, o2[1])])
    ia, ib, oa = f.alu(650, 268, 60, 150)
    f.wire([(534, 300), (650, 300)])
    ys2, mo2 = f.mux(595, 345, 70, ys=[360, 395])
    f.wire([(534, 360), ys2 and (595, 360)])
    f.dot(560, 360)
    f.wire([(534, 470), (575, 470), (575, 395), (595, 395)])
    f.dot(575, 395)
    f.wire([(575, 395), (575, 244)])
    f.wire([mo2, (630, mo2[1]), (630, ib[1]), ib])
    f.wire([(560, 360), (560, 455), (760, 455)])
    f.t(707, 318, "Zero", 8.5, "end")
    f.wire([(710, 318), (760, 318)])
    f.wire([oa, (760, oa[1])])
    f.ell(680, 500, 34, 18, "Controllo\nALU", 9, col=BLU)
    f.wire([(534, 510), (646, 510)], ctrl=True)
    f.wire([(680, 482), (680, 405)], ctrl=True)
    ctrl(f, 605, 414, "ALUSrc", "su", 10)
    ctrl(f, 700, 518, "ALUOp", "su", 18)
    f.wire([(534, 540), (760, 540)])
    # MEM
    f.box(810, 300, 95, 150, "Memoria\ndati", size=11)
    f.wire([(774, oa[1]), (810, oa[1])])
    f.dot(790, oa[1])
    f.wire([(774, 455), (795, 455), (795, 440), (810, 440)])
    f.t(814, 437, "dato", 8.5)
    f.wire([(905, 330), (930, 330)])
    f.t(901, 327, "letto", 8.5, "end")
    f.wire([(790, oa[1]), (790, 480), (930, 480)])
    ctrl(f, 857, 300, "MemWrite")
    ctrl(f, 857, 450, "MemRead", "su", 18)
    g1, g2, go = f.gate_and(830, 225)
    f.wire([(774, 318), (800, 318), (800, g2[1]), g2])
    f.wire([(812, g1[1]), g1], ctrl=True)
    f.t(810, g1[1] - 6, "Branch", 9.5, "end", it=True, col=BLU)
    f.wire([go, (870, go[1]), (870, 22), (45, 22), (45, 292)], ctrl=True)
    f.t(875, 200, "PCSrc", 10, it=True, col=BLU)
    f.wire([(774, o2[1]), (785, o2[1]), (785, 10), (24, 10), (24, 335), (35, 335)])
    f.wire([(774, 540), (930, 540)])
    # WB
    ys3, mo3 = f.mux(985, 310, 190, ("1", "0"), ys=[330, 480])
    f.wire([(944, 330), (985, 330)])
    f.wire([(944, 480), (985, 480)])
    ctrl(f, 995, 314, "MemtoReg", "giu", 20, dx=2)
    f.wire([mo3, (1040, mo3[1]), (1040, 610), (300, 610), (300, 400), (335, 400)])
    f.wire([(944, 540), (960, 540), (960, 590), (310, 590), (310, 370), (335, 370)])
    # controllo che viaggia
    f.wire([(408, 150), (430, 150), (430, 100), (520, 100)], ctrl=True)
    f.wire([(534, 100), (760, 100)], ctrl=True)
    f.wire([(774, 100), (930, 100)], ctrl=True)
    f.t(470, 94, "EX M WB", 9.5, "middle", it=True, col=BLU)
    f.t(650, 94, "M WB", 9.5, "middle", it=True, col=BLU)
    f.t(850, 94, "WB", 9.5, "middle", it=True, col=BLU)
    f.wire([(944, 100), (1060, 100), (1060, 52), (392, 52), (392, 265)], ctrl=True)
    f.t(398, 255, "RegWrite (da MEM/WB)", 9, it=True, col=BLU)


@figura("4-2")
def f4_3():
    f = Fig(1080, 665)
    pipeline(f)
    return f


def mux3(f, x, y, ins=("00", "10", "01"), col=NERO):
    return f.mux(x, y, 80, ins, w=24, col=col, ys=[y + 20, y + 40, y + 60])


@figura("4-3")
def f4_4():
    """Propagazione (forwarding) nello stadio EX."""
    f = Fig(770, 500)
    for x, n in ((60, "ID/EX"), (470, "EX/MEM"), (650, "MEM/WB")):
        f.preg(x, 40, 420, n)
    O = ARANCIO
    ya, oa_ = mux3(f, 150, 80, col=O)
    yb, ob = mux3(f, 150, 170, col=O)
    f.wire([(74, 100), (150, 100)]); f.t(80, 96, "dato 1", 9)
    f.wire([(74, 190), (150, 190)]); f.t(80, 186, "dato 2", 9)
    ys, mo = f.mux(215, 200, 65, ys=[215, 250])
    f.wire([ob, (195, ob[1]), (195, 215), (215, 215)])
    f.wire([(74, 268), (205, 268), (205, 250), (215, 250)]); f.t(80, 264, "imm.", 9)
    ia, ib, oalu = f.alu(285, 82.2, 60, 180)
    f.wire([oa_, (285, ia[1])])
    f.wire([mo, (260, mo[1]), (260, ib[1]), ib])
    f.dot(195, 215)
    f.wire([(195, 215), (195, 292), (470, 292)]); f.t(380, 288, "dato da scrivere (sw)", 9, "middle")
    f.wire([oalu, (470, oalu[1])])
    # MEM e WB
    f.box(525, 60, 90, 75, "Memoria\ndati", size=10.5)
    f.dot(500, 170)
    f.wire([(484, 170), (650, 170)])
    f.wire([(500, 170), (500, 98), (525, 98)])
    f.wire([(484, 292), (510, 292), (510, 120), (525, 120)])
    f.wire([(615, 98), (650, 98)])
    ys3, mo3 = f.mux(690, 75, 115, ("1", "0"), ys=[98, 170])
    f.wire([(664, 98), (690, 98)]); f.wire([(664, 170), (690, 170)])
    # ritorni verso i multiplexer
    f.wire([(500, 170), (500, 462), (135, 462), (135, 120), (150, 120)], col=O)
    f.dot(500, 170, O); f.dot(135, 210, O)
    f.wire([(135, 210), (150, 210)], col=O)
    f.wire([mo3, (740, mo3[1]), (740, 478), (120, 478), (120, 140), (150, 140)], col=O)
    f.dot(120, 230, O)
    f.wire([(120, 230), (150, 230)], col=O)
    f.t(300, 458, "risultato in EX/MEM (istruzione precedente)", 9, "middle", col=O)
    f.t(300, 492, "risultato in MEM/WB (due istruzioni prima)", 9, "middle", col=O)
    # unità di propagazione
    f.box(250, 330, 140, 55, "Unità di\npropagazione", size=10.5, col=O, tcol=O)
    f.wire([(74, 342), (250, 342)]); f.t(80, 338, "rs1", 9, mono=True)
    f.wire([(74, 372), (250, 372)]); f.t(80, 368, "rs2", 9, mono=True)
    f.wire([(74, 440), (650, 440)]); f.t(80, 436, "rd", 9, mono=True)
    f.dot(530, 440); f.wire([(530, 440), (530, 350), (390, 350)])
    f.t(398, 346, "EX/MEM.rd", 9, mono=True)
    f.wire([(664, 440), (680, 440), (680, 372), (390, 372)])
    f.t(398, 368, "MEM/WB.rd", 9, mono=True)
    f.t(400, 398, "+ i due RegWrite", 9, it=True, col=BLU)
    f.wire([(262, 330), (262, 62), (162, 62), (162, 82)], ctrl=True, col=O)
    f.t(168, 58, "ForwardA", 9.5, it=True, col=O)
    f.wire([(250, 357), (230, 357), (230, 315), (162, 315), (162, 247)], ctrl=True, col=O)
    f.t(166, 312, "ForwardB", 9.5, it=True, col=O)
    return f


@figura("4-5")
def f4_5():
    """IF e ID: salto deciso in ID, rilevamento dei conflitti (stallo) ed eccezioni."""
    f = Fig(880 + 40, 590)
    f.raw('<g transform="translate(40,0)">')
    O = ARANCIO
    f.preg(280, 60, 440, "IF/ID")
    f.preg(660, 60, 440, "ID/EX")
    f.t(150, 580, "IF", 12, "middle", bold=True, col="#57606a")
    f.t(470, 580, "ID", 12, "middle", bold=True, col="#57606a")
    # IF
    ys, mo = f.mux(40, 210, 100, ("0", "1", "2"), ys=[230, 260, 290])
    f.box(80, 230, 38, 60, "PC")
    f.wire([mo, (80, 260)])
    f.box(145, 215, 100, 90, "Memoria\nistruzioni", size=10.5)
    f.wire([(118, 260), (145, 260)])
    f.dot(130, 260)
    a, b, o = f.alu(150, 80, 40, 70, "+", 15, simbolo=True)
    f.wire([(130, 260), (130, a[1]), a])
    f.t(141, b[1] - 4, "4", 11, "middle"); f.wire([(137, b[1]), b])
    f.dot(130, 180); f.wire([(130, 180), (280, 180)])
    f.wire([(245, 260), (280, 260)])
    f.wire([o, (210, o[1]), (210, 45), (20, 45), (20, 230), (40, 230)])
    f.t(4, 280, "gestore", 8.5, "end", col=O)
    f.t(4, 291, "delle", 8.5, "end", col=O)
    f.t(4, 302, "eccezioni", 8.5, "end", col=O)
    f.wire([(8, 290), (40, 290)], col=O)
    # ID
    f.wire([(294, 260), (305, 260)], arrow=False)
    f.wire([(305, 140), (305, 470)], arrow=False)
    f.box(380, 200, 105, 120, None)
    f.t(432, 262, "Banco dei", 10.5, "middle"); f.t(432, 276, "registri", 10.5, "middle")
    for yy, et in ((220, "rs1"), (250, "rs2")):
        f.dot(305, yy); f.wire([(305, yy), (380, yy)]); f.t(384, yy + 4, et, 9)
    f.wire([(485, 225), (550, 225), (550, 245), (560, 245)])
    f.wire([(485, 300), (550, 300), (550, 275), (560, 275)])
    f.dot(520, 225); f.dot(520, 300)
    f.wire([(520, 225), (520, 230), (660, 230)], arrow=False)
    f.wire([(520, 300), (520, 310), (660, 310)])
    f.wire([(520, 225), (520, 230)], arrow=False)
    f.box(560, 235, 40, 50, "=", size=18)
    f.ell(410, 420, 34, 18, "Gener.\nimmediati", 9)
    f.dot(305, 420); f.wire([(305, 420), (376, 420)])
    f.wire([(444, 420), (660, 420)])
    f.dot(470, 420)
    f.ell(470, 360, 22, 12, "<< 1", 9)
    f.wire([(470, 420), (470, 373)])
    a2, b2, o2 = f.alu(560, 90, 40, 70, "+", 15, simbolo=True)
    f.wire([(294, 180), (330, 180), (330, 104.7), a2])
    f.dot(330, 180); f.wire([(330, 180), (660, 180)])
    f.wire([(492, 360), (520, 360), (520, 345), (535, 345), (535, b2[1]), b2])
    f.wire([o2, (620, o2[1]), (620, 30), (28, 30), (28, 260), (40, 260)])
    # decisione del salto
    g1, g2, go = f.gate_and(610, 330)
    f.wire([(600, 260), (612, 260), (612, 300), (600, 300), (600, g1[1]), g1], ctrl=True)
    f.t(604, 258, "uguali", 8.5, it=True, col=BLU)
    f.wire([(588, g2[1]), g2], ctrl=True); f.t(585, g2[1] + 4, "Branch", 9, "end", it=True, col=BLU)
    f.wire([go, (645, go[1]), (645, 20), (50, 20), (50, 212)], ctrl=True)
    f.t(648, 330, "PCSrc", 9.5, it=True, col=BLU)
    f.dot(645, 40, BLU)
    f.wire([(645, 40), (305, 40), (305, 72), (296, 72)], ctrl=True)
    f.t(310, 54, "IF.Flush (azzera IF/ID)", 9, it=True, col=BLU)
    # controllo e bolla
    f.ell(400, 460, 34, 18, "Controllo", 9.5, col=BLU)
    f.dot(305, 460); f.wire([(305, 460), (366, 460)], ctrl=True)
    ys4, mo4 = f.mux(560, 440, 60, ("0", "1"), col=O, ys=[455, 485])
    f.wire([(434, 460), (520, 460), (520, 485), (560, 485)], ctrl=True)
    f.t(545, 459, "0", 10, "end", col=O); f.wire([(548, 455), (560, 455)], col=O)
    f.wire([mo4, (660, mo4[1])], ctrl=True)
    # unità di rilevamento
    f.box(380, 505, 140, 42, "Rilevamento\ndei conflitti", size=10, col=O, tcol=O)
    f.wire([(305, 470), (305, 520), (380, 520)])
    f.t(312, 516, "rs1, rs2", 8.5, mono=True)
    f.wire([(674, 530), (700, 530)], arrow=False)
    f.wire([(700, 530), (700, 535), (520, 535)])
    f.t(704, 527, "ID/EX.rd", 8.5, mono=True); f.t(704, 538, "ID/EX.MemRead", 8.5, mono=True)
    f.wire([(380, 540), (99, 540), (99, 290)], ctrl=True, col=O)
    f.t(104, 554, "PCWrite", 9, it=True, col=O)
    f.wire([(380, 512), (360, 512), (360, 525), (287, 525), (287, 502)], ctrl=True, col=O)
    f.t(225, 520, "IF/IDWrite", 9, it=True, col=O)
    f.wire([(520, 512), (570, 512), (570, 497)], ctrl=True, col=O)
    f.t(574, 520, "bolla", 9, it=True, col=O)
    # eccezioni
    f.box(720, 380, 80, 34, "SEPC", size=10.5, col=O, tcol=O)
    f.box(720, 440, 80, 34, "SCAUSE", size=10.5, col=O, tcol=O)
    f.wire([(674, 180), (760, 180), (760, 380)], col=O)
    f.t(764, 300, "PC dell'istruzione", 8.5, col=O); f.t(764, 311, "che ha causato", 8.5, col=O)
    f.t(764, 322, "l'eccezione", 8.5, col=O)
    f.t(805, 461, "causa", 8.5, col=O)
    f.raw("</g>")
    return f


def fasi(f, x0, y, cicli, col_w=52, h=22, nomi=None, grigio=()):
    """Disegna in riga le fasi: cicli = lista di (ciclo, nome)."""
    for c, n in cicli:
        x = x0 + (c - 1) * col_w
        fill = GRIGIO if n in grigio or n == "bolla" else "#fff"
        f.box(x + 3, y, col_w - 6, h, n, fill=fill, r=2, size=10)


@figura("4-4")
def f4_2():
    """Diagramma temporale con conflitto load-use, stallo e propagazione."""
    W, x0 = 52, 170
    f = Fig(x0 + 9 * W + 20, 230)
    for c in range(1, 10):
        f.t(x0 + (c - .5) * W, 22, str(c), 10, "middle", col="#57606a")
    f.t(x0 - 10, 22, "ciclo", 10, "end", col="#57606a")
    righe = [
        ("lw  x2, 20(x1)", [(1, "IF"), (2, "ID"), (3, "EX"), (4, "MEM"), (5, "WB")]),
        ("and x4, x2, x5", [(2, "IF"), (3, "ID"), (4, "ID"), (5, "EX"), (6, "MEM"), (7, "WB")]),
        ("or  x8, x2, x6", [(3, "IF"), (4, "IF"), (5, "ID"), (6, "EX"), (7, "MEM"), (8, "WB")]),
        ("add x9, x4, x2", [(5, "IF"), (6, "ID"), (7, "EX"), (8, "MEM"), (9, "WB")]),
    ]
    ys = [40, 80, 150, 190]
    for (istr, cc), y in zip(righe, ys):
        f.t(x0 - 10, y + 15, istr, 11, "end", mono=True)
        fasi(f, x0, y, cc)
    # bolla
    f.t(x0 - 10, 130, "(bolla)", 10, "end", it=True, col="#57606a")
    fasi(f, x0, 115, [(4, "bolla"), (5, "bolla"), (6, "bolla")])
    f.box(x0 + 3 * W + 3, 80, W - 6, 22, "ID", fill="#fbe3d6", r=2, size=10, col=ARANCIO, tcol=ARANCIO)
    f.box(x0 + 3 * W + 3, 150, W - 6, 22, "IF", fill="#fbe3d6", r=2, size=10, col=ARANCIO, tcol=ARANCIO)
    # propagazioni
    f.wire([(x0 + 4 * W - 3, 62), (x0 + 4 * W + 3, 80 + 11)], col=ARANCIO, lw=1.8)
    f.wire([(x0 + 6 * W - 3, 102), (x0 + 6 * W + 3, 190 + 11)], col=ARANCIO, lw=1.8)
    f.t(x0 + 9 * W, 225, "in arancio: lo stallo e le propagazioni (MEM/WB → EX)", 9.5, "end", col=ARANCIO)
    return f


@figura("4-6")
def f4_6():
    """Predittore a due bit (contatore saturato)."""
    f = Fig(720, 230)
    xs = [90, 270, 450, 630]
    nomi = [("11", "forte", "preso"), ("10", "debole", "preso"), ("01", "debole", "non preso"), ("00", "forte", "non preso")]
    for x, (b, a, p) in zip(xs, nomi):
        col = NERO if p == "preso" else "#57606a"
        f.raw(f'<circle cx="{x}" cy="115" r="42" fill="{"#eef3fb" if p == "preso" else "#fff"}" stroke="{col}" stroke-width="1.5"/>')
        f.t(x, 106, b, 13, "middle", bold=True, mono=True)
        f.t(x, 122, a, 9.5, "middle")
        f.t(x, 134, p, 9.5, "middle")
    for i in range(3):
        x1, x2 = xs[i], xs[i + 1]
        f.raw(f'<path d="M{x1 + 30},{85} Q{(x1 + x2) / 2},{40} {x2 - 30},{85}" fill="none" stroke="#1f2328" stroke-width="1.3" marker-end="url(#a)"/>')
        f.t((x1 + x2) / 2, 55, "N", 11, "middle", bold=True)
        f.raw(f'<path d="M{x2 - 30},{145} Q{(x1 + x2) / 2},{190} {x1 + 30},{145}" fill="none" stroke="#1f2328" stroke-width="1.3" marker-end="url(#a)"/>')
        f.t((x1 + x2) / 2, 185, "P", 11, "middle", bold=True)
    f.raw('<path d="M60,85 C20,40 0,120 48,118" fill="none" stroke="#1f2328" stroke-width="1.3" marker-end="url(#a)"/>')
    f.t(16, 70, "P", 11, "middle", bold=True)
    f.raw('<path d="M660,85 C700,40 720,120 672,118" fill="none" stroke="#1f2328" stroke-width="1.3" marker-end="url(#a)"/>')
    f.t(704, 70, "N", 11, "middle", bold=True)
    f.t(360, 222, "P = salto preso, N = non preso. Nei due stati a sinistra si prevede «preso».", 10, "middle", col="#57606a")
    return f


@figura("4-7")
def f4_7():
    """Branch target buffer e tabella della storia letti in IF."""
    f = Fig(790, 330)
    f.box(30, 140, 50, 50, "PC")
    f.dot(105, 165)
    f.wire([(80, 165), (105, 165)], arrow=False)
    # tabella
    x, y, w = 200, 60, 330
    cols = [("tag (PC del salto)", 140), ("destinazione", 120), ("storia", 70)]
    xx = x
    for n, cw in cols:
        f.t(xx + cw / 2, y - 8, n, 9.5, "middle", bold=True)
        for r in range(6):
            f.box(xx, y + r * 26, cw, 26, None, fill=GRIGIO if r == 2 else "#fff", r=0, lw=1)
        xx += cw
    f.t(x + 70, y + 2 * 26 + 17, "0x0040 01", 9.5, "middle", mono=True)
    f.t(x + 200, y + 2 * 26 + 17, "0x0040 0040", 9.5, "middle", mono=True)
    f.t(x + 295, y + 2 * 26 + 17, "11", 9.5, "middle", mono=True)
    f.wire([(105, 165), (105, 112), (200, 112)])
    f.t(115, 107, "bit bassi: indice", 9)
    f.wire([(105, 165), (105, 250), (250, 250)])
    f.t(115, 245, "bit alti", 9)
    f.box(250, 232, 36, 36, "=", size=16)
    f.wire([(270, 216), (268, 232)])
    f.box(400, 232, 46, 36, "&", size=14)
    f.wire([(286, 250), (400, 250)])
    f.t(330, 245, "trovato", 9, "middle", it=True, col=BLU)
    f.wire([(495, 216), (495, 242), (446, 242)], ctrl=True)
    f.t(500, 236, "prevede preso?", 9, it=True, col=BLU)
    # mux del PC
    ys, mo = f.mux(620, 120, 90, ("0", "1"), ys=[145, 185])
    f.wire([(400, 216), (400, 225), (590, 225), (590, 185), (620, 185)])
    f.t(560, 219, "", 9)
    f.wire([(105, 165), (105, 300), (600, 300), (600, 145), (620, 145)])
    f.t(330, 295, "PC + 4", 9.5, "middle")
    f.wire([(446, 250), (630, 250), (630, 203)], ctrl=True)
    f.wire([mo, (720, mo[1])])
    f.t(724, 158, "prossimo", 9.5)
    f.t(724, 170, "PC", 9.5)
    f.t(380, 25, "tutto nello stadio IF, in parallelo con la lettura dell'istruzione", 10, "middle", it=True, col="#57606a")
    return f


@figura("4-8")
def f4_8():
    """Processore superscalare con esecuzione fuori ordine."""
    f = Fig(830, 360)
    f.box(230, 20, 300, 44, "Prelievo e decodifica\n(in ordine)", size=11)
    xs = [40, 220, 400, 580]
    fu = ["Intera", "Intera", "Virgola mobile", "Load / store"]
    for x, n in zip(xs, fu):
        f.wire([(380, 64), (380, 80), (x + 70, 80), (x + 70, 110)])
        f.box(x, 110, 140, 36, "Stazione di\nprenotazione", size=9.5, fill=GRIGIO)
        f.wire([(x + 70, 146), (x + 70, 168)])
        f.box(x, 168, 140, 40, n, size=11)
        f.wire([(x + 70, 208), (x + 70, 240)])
    f.box(130, 240, 500, 50, "Unità di completamento con buffer di riordino\n(scrive registri e memoria in ordine)", size=10.5)
    f.wire([(380, 290), (380, 320)])
    f.t(380, 335, "registri e memoria", 10.5, "middle")
    for x in xs:
        f.dot(x + 70, 224, ARANCIO)
    f.wire([(650, 224), (20, 224), (20, 128), (40, 128)], col=ARANCIO)
    f.t(26, 218, "i risultati tornano anche alle stazioni che li aspettano", 9, col=ARANCIO)
    f.t(775, 46, "in ordine", 9.5, "middle", it=True, col="#57606a")
    f.t(775, 190, "fuori ordine", 9.5, "middle", it=True, col=ARANCIO)
    f.t(775, 268, "in ordine", 9.5, "middle", it=True, col="#57606a")
    return f


def indirizzo(f, x, y, campi, h=24):
    """Barra di un indirizzo: campi = [(nome, larghezza, bit)]."""
    xx = x
    for n, w, b in campi:
        f.box(xx, y, w, h, n, r=0, size=10, fill="#fff")
        f.t(xx + w / 2, y - 5, b, 8.5, "middle", mono=True, col="#57606a")
        xx += w
    return xx


@figura("5-1")
def f5_1():
    f = Fig(700, 300)
    liv = [("registri", "< 1 ns", "centinaia di byte"), ("cache L1", "~1 ns", "decine di KiB"),
           ("cache L2 e L3", "3-20 ns", "MiB"), ("memoria principale (DRAM)", "50-100 ns", "GiB"),
           ("memoria di massa (SSD, disco)", "0,1-10 ms", "TB")]
    for i, (n, t, c) in enumerate(liv):
        y = 20 + i * 52
        half = 70 + i * 55
        x1, x2 = 330 - half, 330 + half
        k = 27
        f.raw(f'<polygon points="{x1 + k},{y} {x2 - k},{y} {x2},{y + 46} {x1},{y + 46}" fill="{"#eef3fb" if i < 3 else "#fff"}" stroke="#1f2328" stroke-width="1.3"/>')
        f.t(330, y + 27, n, 11, "middle", bold=True)
        f.t(x2 + 8, y + 22, t, 9.5)
        f.t(x2 + 8, y + 35, c, 9.5, col="#57606a")
    f.wire([(18, 270), (18, 25)], col="#57606a")
    f.t(26, 30, "più veloce, più cara per bit", 9.5, col="#57606a")
    f.t(26, 272, "più grande", 9.5, col="#57606a")
    return f


@figura("5-2")
def f5_2():
    """Cache a mappatura diretta: 1024 blocchi da una parola."""
    f = Fig(640, 420)
    end = indirizzo(f, 140, 30, [("tag", 220, "31 … 12"), ("indice", 110, "11 … 2"), ("off.", 40, "1 0")])
    f.t(130, 47, "indirizzo", 10, "end", it=True)
    tx, ty = 170, 110
    cols = [("V", 30), ("tag", 130), ("dato (32 bit)", 170)]
    xx = tx
    for n, cw in cols:
        f.t(xx + cw / 2, ty - 6, n, 10, "middle", bold=True)
        xx += cw
    righe = ["0", "1", "2", "…", "i", "…", "1022", "1023"]
    for r, et in enumerate(righe):
        xx = tx
        for n, cw in cols:
            f.box(xx, ty + r * 24, cw, 24, None, fill=GRIGIO if et == "i" else "#fff", r=0, lw=1)
            xx += cw
        f.t(tx - 8, ty + r * 24 + 16, et, 9.5, "end", mono=True)
    f.wire([(415, 54), (415, 80), (120, 80), (120, 214), (170, 214)])
    f.t(422, 74, "l'indice seleziona la riga", 9, it=True)
    # confronto
    f.wire([(250, 54), (250, 70), (110, 70), (110, 340), (225, 340)])
    f.wire([(235, 302), (235, 330)])
    f.box(225, 330, 40, 30, "=", size=15)
    g1, g2, go = f.gate_and(320, 340)
    f.wire([(185, 302), (185, 385), (300, 385), (300, g2[1]), g2])
    f.wire([(265, 345), (320, 345)])
    f.wire([go, (380, go[1])])
    f.t(386, 354, "hit", 11, bold=True)
    f.wire([(415, 302), (415, 400)])
    f.t(420, 400, "dato", 10)
    f.t(560, 214, "B = 4 byte, N = 1024", 9.5, "middle", col="#57606a")
    f.t(560, 230, "indice = (ind. / B) mod N", 9.5, "middle", col="#57606a")
    f.t(560, 246, "tag = ind. / (B · N)", 9.5, "middle", col="#57606a")
    return f


@figura("5-4")
def f5_3():
    """Cache associativa a due vie."""
    f = Fig(720, 430)
    indirizzo(f, 170, 25, [("tag", 230, "31 … 11"), ("indice", 100, "10 … 2"), ("off.", 40, "1 0")])
    for v, x0 in ((0, 60), (1, 380)):
        f.t(x0 + 140, 92, "via %d" % v, 11, "middle", bold=True)
        xx = x0
        for n, cw in (("V", 26), ("tag", 110), ("dato", 140)):
            f.t(xx + cw / 2, 112, n, 9.5, "middle")
            for r in range(5):
                f.box(xx, 118 + r * 22, cw, 22, None, fill=GRIGIO if r == 2 else "#fff", r=0, lw=1)
            xx += cw
        f.box(x0 + 60, 260, 40, 30, "=", size=15)
        f.wire([(x0 + 80, 228), (x0 + 80, 260)])
        g1, g2, go = f.gate_and(x0 + 130, 300)
        f.wire([(x0 + 13, 228), (x0 + 13, 345), (x0 + 120, 345), (x0 + 120, g2[1]), g2])
        f.wire([(x0 + 80, 290), (x0 + 80, g1[1]), g1])
        f.wire([(x0 + 206, 228), (x0 + 206, 375), (x0 + 206 + (60 if v == 0 else -60) * 0 , 375)], arrow=False)
    f.wire([(450, 49), (450, 70), (30, 70), (30, 162), (60, 162)])
    f.wire([(360, 162), (380, 162)])
    f.wire([(30, 162), (30, 162)], arrow=False)
    f.wire([(450, 70), (360, 70), (360, 162)], arrow=False)
    f.t(36, 66, "indice: stessa riga nelle due vie", 9, it=True)
    f.wire([(285, 49), (285, 60), (20, 60), (20, 275), (120, 275)])
    f.wire([(285, 60), (690, 60), (690, 275), (480, 275)])
    # mux e OR
    ys, mo = f.mux(330, 360, 50, ("0", "1"), ys=[375, 395])
    f.wire([(266, 375), (330, 375)])
    f.wire([(586, 375), (600, 375), (600, 410), (320, 410), (320, 395), (330, 395)])
    f.wire([mo, (380, mo[1])]); f.t(385, 389, "dato", 10)
    f.wire([(214, 310), (240, 310), (240, 330), (340, 330), (340, 365)], ctrl=True)
    f.wire([(534, 310), (560, 310), (560, 330), (345, 330)], ctrl=True, arrow=False)
    f.t(360, 326, "hit 0 / hit 1 scelgono il dato", 9, it=True, col=BLU)
    f.t(620, 360, "hit = hit 0 OR hit 1", 9.5, "middle", col="#57606a")
    return f


@figura("5-3")
def f5_4():
    """Dove può andare il blocco 12 in una cache da 8 blocchi."""
    f = Fig(720, 170)
    tipi = [("mappatura diretta", [4], "riga 12 mod 8 = 4"), ("associativa a 2 vie", [0, 1], "insieme 12 mod 4 = 0"),
            ("completamente associativa", list(range(8)), "ovunque")]
    for k, (n, ok, nota) in enumerate(tipi):
        x0 = 15 + k * 240
        f.t(x0 + 100, 22, n, 10.5, "middle", bold=True)
        for c in range(8):
            f.box(x0 + c * 25, 40, 25, 50, None, fill="#c9d6ee" if c in ok else "#fff", r=0, lw=1)
            f.t(x0 + c * 25 + 12.5, 105, str(c), 9, "middle", mono=True, col="#57606a")
        if k == 1:
            for c in range(4):
                f.raw(f'<rect x="{x0 + c * 50}" y="38" width="50" height="54" fill="none" stroke="#1f2328" stroke-width="2"/>')
                f.t(x0 + c * 50 + 25, 120, "ins. %d" % c, 8.5, "middle", col="#57606a")
        f.t(x0 + 100, 148, nota, 10, "middle", it=True)
    return f


@figura("5-5")
def f5_5():
    """Organizzazione di un chip DRAM."""
    f = Fig(640, 400)
    x0, y0, n = 200, 40, 10
    for r in range(n):
        for c in range(n):
            f.box(x0 + c * 22, y0 + r * 18, 22, 18, None, fill="#c9d6ee" if r == 4 else "#fff", r=0, lw=0.8)
    f.box(150, y0, 34, n * 18, None)
    f.t(167, y0 + 90, "decodificatore di riga", 9.5, "middle", rot=-90)
    f.wire([(40, y0 + 90), (150, y0 + 90)])
    f.t(40, y0 + 84, "indirizzo di riga (RAS)", 9.5)
    f.box(x0, 240, 220, 26, "buffer di riga", size=10, fill=GRIGIO)
    f.wire([(x0 + 110, 220), (x0 + 110, 240)])
    f.t(x0 + 118, 234, "tutta la riga", 8.5, it=True)
    f.raw(f'<polygon points="{x0 + 30},290 {x0 + 190},290 {x0 + 165},320 {x0 + 55},320" fill="#fff" stroke="#1f2328" stroke-width="1.3"/>')
    f.t(x0 + 110, 309, "selezione colonna", 9.5, "middle")
    f.wire([(x0 + 110, 266), (x0 + 110, 290)])
    f.wire([(560, 305), (x0 + 178, 305)])
    f.t(470, 298, "indirizzo di colonna (CAS)", 9.5)
    f.wire([(x0 + 110, 320), (x0 + 110, 355)])
    f.t(x0 + 110, 372, "dati", 10, "middle")
    f.t(450, 80, "cella = 1 transistor", 9.5, col="#57606a")
    f.t(450, 94, "+ 1 condensatore:", 9.5, col="#57606a")
    f.t(450, 108, "va rinfrescata", 9.5, col="#57606a")
    f.t(450, 122, "periodicamente", 9.5, col="#57606a")
    f.t(450, 160, "più colonne della stessa", 9.5, col="#57606a")
    f.t(450, 174, "riga: accessi veloci", 9.5, col="#57606a")
    f.t(450, 188, "(modalità a burst)", 9.5, col="#57606a")
    return f


@figura("5-6")
def f5_6():
    """Traduzione di un indirizzo virtuale con TLB e tabella delle pagine."""
    f = Fig(780, 370)
    indirizzo(f, 60, 30, [("numero di pagina virtuale", 260, "31 … 12"), ("offset", 120, "11 … 0")])
    f.t(55, 47, "virtuale", 10, "end", it=True)
    f.box(60, 110, 200, 70, "TLB\n(cache delle traduzioni)", size=10.5, fill="#eef3fb")
    f.wire([(160, 54), (160, 110)])
    f.box(360, 110, 200, 150, None)
    f.t(460, 102, "tabella delle pagine (in memoria)", 10, "middle", bold=True)
    for r in range(6):
        f.box(360, 110 + r * 25, 30, 25, "1" if r != 3 else "0", r=0, lw=1, size=9.5)
        f.box(390, 110 + r * 25, 170, 25, None if r == 3 else "pagina fisica", r=0, lw=1, size=9, fill=GRIGIO if r == 1 else "#fff")
    f.t(475, 201, "su disco", 9, "middle", it=True, col="#57606a")
    f.t(375, 274, "V", 9.5, "middle")
    f.wire([(260, 147), (360, 147)])
    f.t(268, 141, "miss", 9, it=True, col=BLU)
    f.box(610, 110, 130, 40, "registro della\ntabella (satp)", size=9.5)
    f.wire([(610, 130), (585, 130), (585, 105), (560, 105), (560, 112)])
    f.wire([(560, 197), (610, 197), (610, 225)], col=ARANCIO)
    f.t(615, 240, "V = 0: page fault,", 9.5, col=ARANCIO)
    f.t(615, 253, "interviene il sistema", 9.5, col=ARANCIO)
    f.t(615, 266, "operativo", 9.5, col=ARANCIO)
    indirizzo(f, 60, 320, [("numero di pagina fisica", 180, "29 … 12"), ("offset", 120, "11 … 0")])
    f.t(55, 337, "fisico", 10, "end", it=True)
    f.wire([(110, 180), (110, 320)])
    f.t(116, 240, "hit", 9, it=True, col=BLU)
    f.wire([(475, 260), (475, 285), (200, 285), (200, 320)])
    f.dot(200, 285)
    f.wire([(200, 285), (200, 182)], dash=True)
    f.t(206, 230, "aggiorna", 9, it=True, col="#57606a")
    f.t(206, 241, "il TLB", 9, it=True, col="#57606a")
    f.wire([(380, 54), (380, 75), (760, 75), (760, 300), (300, 300), (300, 320)])
    f.t(600, 70, "l'offset non si traduce", 9, it=True)
    return f


@figura("3-1")
def f3_1():
    """ALU da un bit con Ainvert, Binvert e Less."""
    f = Fig(560, 340)
    # Ainvert
    f.t(20, 64, "a", 13, bold=True); f.wire([(32, 60), (60, 60)], arrow=False)
    ysa, moa = f.mux(110, 40, 50, ("0", "1"), ys=[52, 78])
    f.dot(60, 60); f.wire([(60, 60), (60, 52), (110, 52)])
    na, no_ = f.gate_not(70, 71)
    f.wire([(60, 60), (60, 78), na], arrow=False)
    f.wire([no_, (110, 78)])
    ctrl(f, 120, 44, "Ainvert", "giu", 18)
    f.t(20, 154, "b", 13, bold=True); f.wire([(32, 150), (60, 150)], arrow=False)
    ysb, mob = f.mux(110, 130, 50, ("0", "1"), ys=[142, 168])
    f.dot(60, 150); f.wire([(60, 150), (60, 142), (110, 142)])
    nb, nob = f.gate_not(70, 161)
    f.wire([(60, 150), (60, 168), nb], arrow=False)
    f.wire([nob, (110, 168)])
    ctrl(f, 120, 186, "Binvert", "su", 18)
    # porte
    g1, g2, go = f.gate_and(220, 40)
    g3, g4, go2 = f.gate_or(220, 95)
    f.dot(170, 65); f.dot(185, 155)
    f.wire([moa, (170, 65), (170, g1[1]), g1])
    f.wire([(170, 65), (170, g3[1]), g3])
    f.wire([mob, (185, 155), (185, g2[1]), g2])
    f.wire([(185, 155), (185, g4[1]), g4])
    # sommatore
    f.box(215, 160, 45, 60, "+", size=17)
    f.wire([(170, 101), (170, 175), (215, 175)])
    f.wire([(185, 155), (185, 205), (215, 205)])
    f.wire([(237, 130), (237, 160)]); f.t(242, 140, "CarryIn", 9.5, it=True)
    f.wire([(237, 220), (237, 255)]); f.t(242, 252, "CarryOut", 9.5, it=True)
    # Less
    f.t(160, 274, "Less", 11, it=True); f.wire([(190, 270), (330, 270), (330, 250), (360, 250)])
    # mux del risultato
    ys, mo = f.mux(360, 30, 240, ("0", "1", "2", "3"), w=26, ys=[50, 105, 190, 250])
    f.wire([go, (360, 50)]); f.wire([go2, (300, 105), (360, 105)])
    f.wire([(260, 190), (360, 190)])
    f.wire([mo, (450, mo[1])]); f.t(455, 154, "Result", 11, it=True)
    ctrl(f, 373, 36, "Operation", "giu", 20)
    f.t(300, 44, "AND", 9, col="#57606a"); f.t(300, 99, "OR", 9, col="#57606a"); f.t(272, 184, "somma", 9, col="#57606a")
    f.t(20, 315, "Per la sottrazione: Binvert = 1 e CarryIn del bit 0 = 1 (a − b = a + not b + 1).", 9.5, col="#57606a")
    f.t(20, 330, "NOR: Ainvert = Binvert = 1 e Operation = AND (De Morgan).", 9.5, col="#57606a")
    return f


@figura("3-2")
def f3_2():
    """ALU a 32 bit a propagazione del riporto, con slt, Zero e Overflow."""
    f = Fig(600, 430)
    ys_ = [40, 120, 200, 320]
    nomi = ["ALU 0", "ALU 1", "ALU 2", "ALU 31"]
    for i, (y, n) in enumerate(zip(ys_, nomi)):
        f.box(150, y, 90, 56, n, size=11)
        k = n.split()[1]
        f.t(140, y + 16, f"a{k}", 9.5, "end", mono=True); f.wire([(142, y + 12), (150, y + 12)])
        f.t(140, y + 36, f"b{k}", 9.5, "end", mono=True); f.wire([(142, y + 32), (150, y + 32)])
        f.t(140, y + 52, "Less", 8.5, "end", it=True); f.wire([(142, y + 48), (150, y + 48)])
        f.wire([(240, y + 22), (420, y + 22)], arrow=False); f.t(300, y + 18, f"Result{k}", 9.5, mono=True)
        f.wire([(420, y + 22), (440, y + 22)], arrow=False)
    for y1, y2 in ((40, 120), (120, 200)):
        f.wire([(195, y1 + 56), (195, y2)])
    f.wire([(195, 256), (195, 270)], arrow=False); f.t(195, 296, "⋮", 14, "middle")
    f.wire([(195, 300), (195, 320)])
    f.t(201, 110, "CarryOut → CarryIn", 8.5, it=True)
    f.wire([(60, 20), (195, 20), (195, 40)], ctrl=True)
    f.t(64, 16, "Bnegate (= Binvert e CarryIn del bit 0)", 9.5, it=True, col=BLU)
    f.wire([(240, 366), (265, 366), (265, 395), (40, 395), (40, 88), (142, 88)], col=ARANCIO)
    f.t(246, 362, "Set", 9.5, it=True, col=ARANCIO)
    f.t(48, 412, "il bit di segno di a − b torna su Less del bit 0 (slt); Less = 0 negli altri bit", 9, col=ARANCIO)
    f.wire([(240, 352), (520, 352)]); f.t(525, 356, "Overflow", 9.5, it=True)
    a, b, o = f.gate_nor(480, 165, 30, 60)
    for y, yy in zip(ys_, (172, 186, 204, 218)):
        f.wire([(440, y + 22), (460, y + 22), (460, yy), (484, yy)])
    f.wire([o, (580, o[1])]); f.t(580, 188, "Zero", 10, "end", it=True)
    return f

@figura("3-3")
def f3_3():
    """Somma a 16 bit con anticipo del riporto su due livelli."""
    f = Fig(680, 270)
    for k in range(4):
        x = 50 + k * 155
        f.box(x, 40, 120, 60, f"sommatore 4 bit\nbit {4 * k + 3}…{4 * k}", size=10)
        f.wire([(x + 40, 100), (x + 40, 170)])
        f.wire([(x + 80, 100), (x + 80, 170)])
        f.t(x + 36, 140, f"P{k}", 9.5, "end", mono=True)
        f.t(x + 84, 140, f"G{k}", 9.5, mono=True)
        if k:
            f.wire([(x - 15, 170), (x - 15, 70), (x, 70)], col=ARANCIO)
            f.t(x - 19, 130, f"c{4 * k}", 9.5, "end", mono=True, col=ARANCIO)
    f.wire([(10, 70), (50, 70)]); f.t(12, 64, "c0", 9.5, mono=True)
    f.wire([(25, 70), (25, 190), (40, 190)]); f.dot(25, 70)
    f.box(40, 170, 610, 40, "unità di anticipo del riporto:  c(i+1) = Gi + Pi · ci, svolta in due livelli di porte", size=10.5, fill="#eef3fb")
    f.wire([(560, 210), (560, 235)], col=ARANCIO); f.t(566, 232, "c16", 9.5, mono=True, col=ARANCIO)
    f.t(340, 20, "ogni blocco calcola Pi = p3 p2 p1 p0 e Gi = g3 + p3 g2 + p3 p2 g1 + p3 p2 p1 g0", 9.5, "middle", col="#57606a")
    f.t(340, 260, "tutti i riporti dei blocchi sono pronti insieme, senza attraversare i blocchi precedenti", 9.5, "middle", col=ARANCIO)
    return f

@figura("3-4")
def f3_4():
    """Moltiplicatore «somma e scorri» con il registro del prodotto da 64 bit."""
    f = Fig(600, 300)
    f.box(150, 20, 200, 36, "Moltiplicando (32 bit)", size=10.5)
    a, b, o = f.alu(150, 80, 90, 110, "ALU", 11)
    f.t(205, 162, "32 bit", 9, "middle")
    f.wire([(200, 56), (200, 64), (130, 64), (130, b[1]), b])
    f.box(150, 220, 400, 40, None)
    f.raw('<line x1="350" y1="220" x2="350" y2="260" stroke="#1f2328" stroke-width="1.2"/>')
    f.t(250, 245, "prodotto, metà alta", 10, "middle")
    f.t(450, 245, "metà bassa (all'inizio: moltiplicatore)", 9.5, "middle")
    f.t(350, 282, "Prodotto (64 bit): scorre a destra di 1 bit a ogni passo", 9.5, "middle", col="#57606a")
    f.wire([(190, 220), (190, 206), (115, 206), (115, a[1]), a])
    f.wire([o, (300, o[1]), (300, 220)])
    f.box(420, 90, 110, 50, "Controllo\n(guarda il bit 0)", size=9.5, col=BLU, tcol=BLU)
    f.wire([(540, 220), (540, 115), (530, 115)], ctrl=True)
    f.t(545, 200, "bit 0", 9, it=True, col=BLU)
    f.wire([(420, 105), (330, 105), (330, 120), (218, 120)], ctrl=True)
    f.t(335, 100, "somma sì/no", 9, it=True, col=BLU)
    f.wire([(475, 140), (475, 218)], ctrl=True)
    f.t(480, 180, "scorri, scrivi", 9, it=True, col=BLU)
    return f

@figura("3-5")
def f3_5():
    """Formati IEEE 754 in singola e doppia precisione."""
    f = Fig(700, 150)
    f.t(10, 47, "singola", 10.5, bold=True)
    indirizzo(f, 80, 30, [("s", 24, "31"), ("esponente (8)", 150, "30 … 23"), ("frazione F (23)", 420, "22 … 0")])
    f.t(10, 117, "doppia", 10.5, bold=True)
    indirizzo(f, 80, 100, [("s", 24, "63"), ("esponente (11)", 190, "62 … 52"), ("frazione F (52)", 380, "51 … 0")])
    f.t(80, 145, "valore = (−1)^s × (1 + F) × 2^(esponente − 127)   [doppia: − 1023]", 10, col="#57606a")
    return f


@figura("3-6")
def f3_6():
    """Somma in virgola mobile: i passi dell'hardware."""
    f = Fig(690, 450)
    f.box(60, 20, 220, 30, "A: segno · esponente · frazione", size=10)
    f.box(360, 20, 220, 30, "B: segno · esponente · frazione", size=10)
    passi = ["1. confronta gli esponenti (piccola ALU: differenza d)",
             "2. scorri a destra di d posizioni la frazione con l'esponente minore",
             "3. somma le frazioni (ALU grande)",
             "4. normalizza: scorri e correggi l'esponente; overflow? underflow?",
             "5. arrotonda ai bit disponibili (guard, round, sticky)"]
    for i, t in enumerate(passi):
        y = 85 + i * 70
        f.box(130, y, 380, 36, t, size=10, fill="#eef3fb" if i in (0, 2) else "#fff")
        if i:
            f.wire([(320, y - 34), (320, y)])
    f.wire([(170, 50), (170, 85)]); f.wire([(470, 50), (470, 85)])
    f.wire([(560, 50), (560, 240), (510, 240)])
    f.t(566, 150, "frazioni", 9, it=True)
    f.wire([(320, 401), (320, 432)]); f.t(330, 430, "risultato", 10)
    f.wire([(130, 103), (90, 103)], arrow=False)
    f.wire([(90, 103), (90, 312), (130, 312)])
    f.t(84, 210, "esponente maggiore", 9, "middle", it=True, rot=-90)
    f.wire([(510, 380), (590, 380), (590, 300), (510, 300)], col=ARANCIO)
    f.t(596, 340, "se ora non è", 9, col=ARANCIO)
    f.t(596, 352, "normalizzato", 9, col=ARANCIO)
    return f

@figura("1-1")
def f1_1():
    """I sei formati delle istruzioni RV32I."""
    u, x0 = 19, 40
    f = Fig(x0 + 32 * u + 20, 330)
    formati = [
        ("R", [("funct7", 7, 0), ("rs2", 5, 0), ("rs1", 5, 0), ("funct3", 3, 0), ("rd", 5, 0), ("opcode", 7, 0)]),
        ("I", [("imm[11:0]", 12, 1), ("rs1", 5, 0), ("funct3", 3, 0), ("rd", 5, 0), ("opcode", 7, 0)]),
        ("S", [("imm[11:5]", 7, 1), ("rs2", 5, 0), ("rs1", 5, 0), ("funct3", 3, 0), ("imm[4:0]", 5, 1), ("opcode", 7, 0)]),
        ("B", [("imm[12|10:5]", 7, 1), ("rs2", 5, 0), ("rs1", 5, 0), ("funct3", 3, 0), ("imm[4:1|11]", 5, 1), ("opcode", 7, 0)]),
        ("U", [("imm[31:12]", 20, 1), ("rd", 5, 0), ("opcode", 7, 0)]),
        ("J", [("imm[20|10:1|11|19:12]", 20, 1), ("rd", 5, 0), ("opcode", 7, 0)]),
    ]
    for b, xb in ((31, 0), (25, 6), (24, 7), (20, 11), (19, 12), (15, 16), (14, 17), (12, 19), (11, 20), (7, 24), (6, 25), (0, 31)):
        f.t(x0 + xb * u + u / 2, 22, str(b), 8.5, "middle", mono=True, col="#57606a")
    for i, (n, campi) in enumerate(formati):
        y = 32 + i * 46
        f.t(x0 - 14, y + 19, n, 13, "middle", bold=True)
        xx = x0
        for c, w, imm in campi:
            f.box(xx, y, w * u, 28, c, fill="#e3e8f0" if imm else "#fff", r=0, size=9.5 if len(c) < 14 else 8.5, lw=1.1)
            xx += w * u
    f.t(x0, 318, "In grigio l'immediato. rs1, rs2 e rd stanno sempre negli stessi bit; il bit di segno dell'immediato è sempre il 31.", 9, col="#57606a")
    return f


@figura("2-1")
def f2_1():
    """Organizzazione della memoria di un programma RISC-V (convenzione del corso)."""
    f = Fig(520, 375)
    zone = [("stack  ↓", 70, "#eef3fb"), ("", 60, "#fff"), ("heap (dati dinamici)  ↑", 50, "#eef3fb"),
            ("dati statici", 50, "#eef3fb"), ("testo (codice)", 55, "#eef3fb"), ("riservato", 35, GRIGIO)]
    y = 20
    pos = []
    for n, h, c in zone:
        f.box(160, y, 180, h, n, fill=c, r=0, size=10.5)
        pos.append(y)
        y += h
    f.t(350, pos[0] + 14, "← sp (cima dello stack)", 9.5)
    f.t(350, pos[3] + 28, "← gp (dati globali)", 9.5)
    f.t(350, pos[4] + 30, "← pc (all'avvio, _start)", 9.5)
    f.t(350, pos[5] + 30, "indirizzo 0", 9, mono=True, col="#57606a")
    f.t(150, 26, "indirizzi alti", 9, "end", it=True, col="#57606a")
    f.t(250, 366, "lo stack cresce verso il basso, lo heap verso l'alto", 9.5, "middle", col="#57606a")
    return f


@figura("2-2")
def f2_2():
    """Lo stack durante fact(3): un record di attivazione per chiamata."""
    f = Fig(560, 330)
    righe = [("ra (nel main)", "fact(3)"), ("a0 = 3", "fact(3)"), ("ra (in fact)", "fact(2)"), ("a0 = 2", "fact(2)"),
             ("ra (in fact)", "fact(1)"), ("a0 = 1", "fact(1)")]
    y0 = 40
    for i, (c, fr) in enumerate(righe):
        f.box(200, y0 + i * 34, 160, 34, c, r=0, size=10, fill="#eef3fb" if fr == "fact(2)" else "#fff", lw=1.1)
    for k, fr in enumerate(("fact(3)", "fact(2)", "fact(1)")):
        yy = y0 + k * 68
        f.raw(f'<path d="M370,{yy + 3} h8 v62 h-8" fill="none" stroke="#57606a" stroke-width="1.2"/>')
        f.t(386, yy + 38, "record di " + fr, 9.5, col="#57606a")
    f.t(190, y0 - 8, "indirizzi alti", 9, "end", it=True, col="#57606a")
    f.t(190, y0 + 6 * 34 + 24, "indirizzi bassi", 9, "end", it=True, col="#57606a")
    f.wire([(130, y0 + 6 * 34), (198, y0 + 6 * 34)])
    f.t(125, y0 + 6 * 34 + 4, "sp", 11, "end", bold=True, mono=True)
    f.t(280, 300, "ogni chiamata fa addi sp, sp, -8 e salva ra e a0;", 9.5, "middle", col="#57606a")
    f.t(280, 314, "al ritorno li rilegge e fa addi sp, sp, 8", 9.5, "middle", col="#57606a")
    return f


def main(nomi):
    os.makedirs(QUI, exist_ok=True)
    for n in nomi or sorted(FIG):
        f = FIG[n]()
        Fig.salva(f, os.path.join(QUI, n + ".svg"))
        print("figure/%s.svg" % n)


if __name__ == "__main__":
    main(sys.argv[1:])
