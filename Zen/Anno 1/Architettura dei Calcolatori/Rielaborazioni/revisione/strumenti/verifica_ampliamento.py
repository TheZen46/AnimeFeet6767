"""Verifica dei moduli di Architettura dei Calcolatori (codifiche, conti, programmi)."""
from pathlib import Path
import struct
from itertools import product
from rv import R, I, S, B, campi
from simrv import RV, blocchi

ok = 0
MOD = Path(__file__).resolve().parent.parent / "moduli"


def v(a, b, tol=6e-3):
    global ok
    assert abs(a - b) <= tol * max(1, abs(b)), (a, b)
    ok += 1


# ---- modulo 1
assert R(0, 21, 20, 0, 9) == 0x015A04B3 and R(0x20, 7, 6, 0, 5) == 0x407302B3
assert I(-12, 6, 0, 5) == 0xFF430293 and I(8, 2, 2, 10, 0x03) == 0x00812503
assert S(12, 10, 2, 2) == 0x00A12623 and B(16, 6, 5, 0) == 0x00628863
c = campi(0x40B50533); assert (c["op"], c["f3"], c["f7"], c["rd"], c["rs1"], c["rs2"]) == (0x33, 0, 0x20, 10, 10, 11)
c = campi(0x00C58593); assert (c["op"], c["f3"], c["rd"], c["rs1"], 0x00C58593 >> 20) == (0x13, 0, 11, 11, 12)
v((2 * 1 + 1 * 2 + 1 * 3) / 4, 1.75); v((4 + 2 + 3) / 6, 1.5)
cA = .5 * 1 + .2 * 5 + .1 * 3 + .2 * 2; cB = .5 + .2 * 2 + .1 * 2 + .2 * 2; v(cA, 2.2); v(cB, 1.5); v((cA / 2) / (cB / 1.5), 1.1)
v(1 / (0.6 + 0.4 / 10), 1.5625); v(1 / 0.6, 1.667)
assert (0x12345 << 12) + 0x678 == 0x12345678
v(1.2 * 10 * 2e9 / 6 / 1e9, 4.0)
assert struct.unpack("<4B", struct.pack("<I", 0xA1B2C3D4)) == (0xD4, 0xC3, 0xB2, 0xA1) and 0xD4 - 256 == -44
ok += 6
# ---- modulo 2: si eseguono i programmi scritti nel modulo
md = (MOD / "02-programmazione-assembly-risc-v.md").read_text()
src = "\n".join(blocchi(md))


def prova(etichetta, args, mem=None, conta=None):
    import re as _re
    blocco = [b for b in blocchi(md) if _re.search(r"(?m)^\s*" + etichetta + r":", b)][0]
    m = RV(blocco)
    for ind, val in (mem or {}).items():
        if isinstance(val, int):
            m.sw(ind, val)
        else:
            for k, ch in enumerate(val):
                m.mem[ind + k] = ch
    for k, a in enumerate(args):
        m.x[10 + k] = a
    return m.esegui(etichetta, conta=conta), m


def vettore(base, valori):
    return {base + 4 * k: x for k, x in enumerate(valori)}


assert prova("somma", [0x100, 5], vettore(0x100, [1, 2, 3, 4, 5]))[0] == 15
assert prova("strlen", [0x200], {0x200: b"architettura\0"})[0] == 12
assert prova("max", [0x100, 4], vettore(0x100, [3, -2, 9, 4]))[0] == 9
assert prova("traccia", [0x100, 3], vettore(0x100, list(range(1, 10))))[0] == 15
assert prova("fact", [5])[0] == 120 and prova("fact", [1])[0] == 1
r, m = prova("fib", [10], conta="fib"); assert r == 55 and m.chiamate + 1 == 177
assert prova("somma_quadrati", [3, 4])[0] == 25
assert prova("f", [0x300, 0x200], {0x200: b"ciao\0"})[1].mem.get(0x303) == ord("o")
# il guidato 1 (somma dei pari) è il blocco che contiene "andi"
pari = [b for b in blocchi(md) if "andi t4" in b][0]
mp = RV(pari)
for k, x in enumerate([1, 2, 3, 4, -6]):
    mp.sw(0x100 + 4 * k, x)
mp.x[10], mp.x[11] = 0x100, 5
mp.lab["_s"] = 0
assert mp.esegui("_s") == 0
# reverse coding (esercizio 3): il blocco con L1
rc = [b for b in blocchi(md) if b.strip().startswith("li   t0, 0\n        li   t1, 0\nL1:")][0]
mr = RV(rc)
for k, x in enumerate([3, -1, -7, 0, -2]):
    mr.sw(0x100 + 4 * k, x)
mr.x[10], mr.x[11] = 0x100, 5
mr.lab["_s"] = 0
assert mr.esegui("_s") == 3
ok += 11


# tracce della prova scritta (esercizi 5-8): risultato, sp ripristinato, registri s preservati
def traccia(etichetta, args, mem):
    import re as _re
    blocco = [b for b in blocchi(md) if _re.search(r"(?m)^\s*" + etichetta + r":", b)][0]
    m = RV(blocco)
    for ind, val in mem.items():
        m.sw(ind, val)
    for k, a in enumerate(args):
        m.x[10 + k] = a
    sent = {r: 1000 + r for r in [8, 9] + list(range(18, 28))}
    for r, val in sent.items():
        m.x[r] = val
    r = m.esegui(etichetta)
    assert m.x[2] == 0x8000 and all(m.x[k] == val for k, val in sent.items()), etichetta
    return r, m


def leggi(m, base, n):
    return [m.lw(base + 4 * k) for k in range(n)]


import random as _rnd
_rnd.seed(7)
casi = [[5, 1, 4, 2, 8], [7, 2, 9, 4, 3, 8, 1], [38, 27, 43, 3, 9, 82, 10], [1], [2, 2, 1, -3, 0, 2]]
casi += [[_rnd.randint(-50, 50) for _ in range(_rnd.randint(2, 12))] for _ in range(20)]
for c in casi:
    n = len(c)
    _, m = traccia("bubble", [0x100, n], vettore(0x100, c)); assert leggi(m, 0x100, n) == sorted(c)
    _, m = traccia("quicksort", [0x100, 0, n - 1], vettore(0x100, c)); assert leggi(m, 0x100, n) == sorted(c)
    _, m = traccia("mergesort", [0x100, 0x400, 0, n - 1], vettore(0x100, c)); assert leggi(m, 0x100, n) == sorted(c)
    ok += 3
w = [1, 3, 5, 7, 9, 11, 13]
assert traccia("cerca", [0x100, 0, 6, 11], vettore(0x100, w))[0] == 5
assert traccia("cerca", [0x100, 0, 6, 4], vettore(0x100, w))[0] == -1
for x in range(0, 15):
    assert traccia("cerca", [0x100, 0, 6, x], vettore(0x100, w))[0] == (w.index(x) if x in w else -1)
ok += 17

# ---- modulo 3: ALU e aritmetica
def bits(x, n=4):
    return [(x >> i) & 1 for i in range(n)]


a_, b_ = bits(0b1011), bits(0b0110)
g = [x & y for x, y in zip(a_, b_)]; p = [x | y for x, y in zip(a_, b_)]
c = [0]
for i in range(4):
    c.append(g[i] | (p[i] & c[i]))
assert g == bits(0b0010) and p == bits(0b1111) and c == [0, 0, 1, 1, 1]
s_ = sum((a_[i] ^ b_[i] ^ c[i]) << i for i in range(4)) + (c[4] << 4)
assert s_ == 17


def shift_add(m, q, n=4):
    reg, passi = q, []
    for _ in range(n):
        if reg & 1:
            reg += m << n
        reg >>= 1
        passi.append(reg)
    return reg, passi


r, passi = shift_add(6, 5)
assert r == 30 and passi == [0b00110010, 0b00011001, 0b00111100, 0b00011110]


def booth(m, q, n=4):
    mask = (1 << n) - 1
    A, Q, q1, passi = 0, q & mask, 0, []
    for _ in range(n):
        coppia = (Q & 1, q1)
        if coppia == (1, 0):
            A = (A - m) & mask
        elif coppia == (0, 1):
            A = (A + m) & mask
        q1 = Q & 1
        Q = ((Q >> 1) | ((A & 1) << (n - 1))) & mask
        A = ((A >> 1) | (A & (1 << (n - 1)))) & mask
        passi.append((coppia, A, Q, q1))
    v = (A << n) | Q
    return v - (1 << 2 * n) if v >> (2 * n - 1) else v, passi


r, passi = booth(3, -2)
assert r == -6 and [x[1:] for x in passi] == [(0, 7, 0), (0b1110, 0b1011, 1), (0b1111, 0b0101, 1), (0b1111, 0b1010, 1)]
assert all(booth(x, y)[0] == x * y for x in range(-7, 8) for y in range(-8, 8))  # M = -8 non si nega in 4 bit
assert divmod(11, 3) == (3, 2)
f32 = lambda x: struct.unpack(">f", struct.pack(">f", x))[0]  # noqa: E731
assert f32(1.75) + f32(0.3125) == 2.0625 and 1.5 * -2.25 == -3.375
assert struct.unpack(">I", struct.pack(">f", -2.25))[0] >> 23 & 0xFF == 128
assert (127 + 128 - 127) == 128 and 0.5 - 0.4375 == 2 ** -4


def hamming(d):           # d = [d3, d5, d6, d7]
    b = [0] * 8
    b[3], b[5], b[6], b[7] = d
    b[1], b[2], b[4] = b[3] ^ b[5] ^ b[7], b[3] ^ b[6] ^ b[7], b[5] ^ b[6] ^ b[7]
    return b[1:]


def sindrome(w):
    b = [0] + w
    return (b[4] ^ b[5] ^ b[6] ^ b[7]) << 2 | (b[2] ^ b[3] ^ b[6] ^ b[7]) << 1 | (b[1] ^ b[3] ^ b[5] ^ b[7])


w = hamming([1, 0, 1, 1]); assert w == [0, 1, 1, 0, 0, 1, 1] and sindrome(w) == 0
w[5] ^= 1; assert w == [0, 1, 1, 0, 0, 0, 1] and sindrome(w) == 6
assert all(sindrome([x ^ (k == j) for j, x in enumerate(hamming(list(dd)))]) == k + 1
           for dd in product([0, 1], repeat=4) for k in range(7))
K = lambda M: next(k for k in range(1, 20) if 2 ** k >= M + k + 1)  # noqa: E731
assert [K(m) for m in (4, 8, 16, 32, 64)] == [3, 4, 5, 6, 7]
s8 = lambda x: (x + 128) % 256 - 128  # noqa: E731
assert s8(100 + 50) == -106 and (150 & 0xFF) == 0b10010110 and (-150) & 0xFF == 0b01101010
assert s8(100 - (-100)) < 0
ok += 12

# ---- modulo 4: pipeline
from pipe import cicli, predittore
A = [("load", 5, [10]), ("load", 6, [10]), ("alu", 7, [5, 6]), ("store", 0, [7, 10]), ("alu", 10, [10])]
A2 = [A[0], A[1], A[4], A[2], A[3]]
Bc = [("alu", 9, [18, 19]), ("alu", 20, [9, 21]), ("alu", 22, [9, 20]), ("alu", 23, [22, 18]), ("store", 0, [23, 10])]
assert cicli(A, False)[0] == 13 and cicli(A, True)[0] == 10 and cicli(A, True)[2] == [2, 3, 5, 6, 7]
assert cicli(A2, True)[0] == 9 and cicli(A2, False)[0] == 12
assert cicli(Bc, False)[0] == 17 and cicli(Bc, True)[0] == 9
assert cicli([("load", 5, [10]), ("branch", 0, [5, 0])])[1] == [0, 2]
assert cicli([("alu", 6, [6]), ("branch", 0, [6, 7])])[1] == [0, 1]
G3 = [("alu", 6, [6]), ("branch", 0, [6, 7]), ("alu", 28, [5, 6])]
assert cicli(G3, presi={1})[0] == 9 and cicli(G3, presi={1})[2][1] == 4
v((850 * 1000) / ((5 + 999) * 250), 3.386); v(1 + .25 * .4 + .15 * .6, 1.19)
v(1 + .1 + .15 * .6 * 3, 1.37); v(1 + .1 + .15 * .1, 1.115)
for esiti, attesi in (([True] * 9 + [False], (8, 9)), ([True] * 3 + [False], (2, 3))):
    for bit, att in zip((1, 2), attesi):
        st = None
        for _ in range(4):
            gg, st = predittore(esiti, bit, st)
        assert gg == att


def vliw(pacchetti, reg, mem):
    """Esegue pacchetti: tutte le letture del pacchetto prima delle scritture."""
    pc = 0
    while True:
        vecchi, scritture, salto = dict(reg), [], None
        for ins in pacchetti[pc]:
            op, *ar = ins
            if op == "lw":
                scritture.append((ar[0], mem[vecchi[ar[2]] + ar[1]]))
            elif op == "sw":
                mem[vecchi[ar[2]] + ar[1]] = vecchi[ar[0]]
            elif op == "addi":
                scritture.append((ar[0], vecchi[ar[1]] + ar[2]))
            elif op == "slli":
                scritture.append((ar[0], vecchi[ar[1]] << ar[2]))
            elif op == "bne":
                salto = vecchi[ar[0]] != vecchi[ar[1]]
        for r_, x_ in scritture:
            reg[r_] = x_
        if salto is None:
            pc += 1
        elif salto:
            pc = 0
        else:
            return mem


def latenze(pacchetti):
    """Controlla: ALU usabile dal pacchetto dopo, lw da due pacchetti dopo."""
    pronto = {}
    for k, pk in enumerate(pacchetti):
        for op, *ar in pk:
            letti = ([ar[2]] if op == "lw" else [ar[0], ar[2]] if op == "sw"
                     else ar[:2] if op == "bne" else [ar[1]])
            assert all(pronto.get(r_, 0) <= k for r_ in letti), (k, op)
        for op, *ar in pk:
            if op in ("lw", "addi", "slli"):
                pronto[ar[0]] = k + (2 if op == "lw" else 1)


semplice = [[("addi", "a0", "a0", 4), ("lw", "t0", 0, "a0")], [("addi", "a1", "a1", 4)],
            [("slli", "t0", "t0", 1)], [("bne", "a0", "a2"), ("sw", "t0", -4, "a1")]]
srotolato = [[("addi", "a0", "a0", 8), ("lw", "t0", 0, "a0")], [("addi", "a1", "a1", 8), ("lw", "t1", -4, "a0")],
             [("slli", "t0", "t0", 1)], [("slli", "t1", "t1", 1), ("sw", "t0", -8, "a1")],
             [("bne", "a0", "a2"), ("sw", "t1", -4, "a1")]]
for prog_, ni in ((semplice, 6), (srotolato, 9)):
    latenze(prog_)
    mem0 = {0x100 + 4 * k: k * k - 3 for k in range(6)}
    mem0.update({0x200 + 4 * k: 0 for k in range(6)})
    out = vliw(prog_, {"a0": 0x100, "a1": 0x200, "a2": 0x118, "t0": 0, "t1": 0}, mem0)
    assert [out[0x200 + 4 * k] for k in range(6)] == [2 * (k * k - 3) for k in range(6)]
    assert sum(len(pk) for pk in prog_) == ni
v(6 / 4, 1.5); v(9 / 5, 1.8)
ok += 6

# ---- modulo 5: cache
from cache import simula, campi as campi_c
seq = [0, 8, 32, 0, 40, 8, 64, 32]
assert "".join(simula(seq, 8, 4, 1)) == "MMMMMMMM"
assert "".join(simula(seq, 8, 4, 2)) == "MMMHMHMM"
assert "".join(simula(seq, 8, 4, 8)) == "MMMHMHMH"
assert "".join(simula(list(range(0, 64, 4)), 4, 16, 1)) == "MHHH" * 4
g2 = [0, 4, 16, 64, 68, 0, 20]
assert "".join(simula(g2, 8, 4, 1)) == "M" * 7 and "".join(simula(g2, 2, 16, 1)) == "MHMMHMH"
assert campi_c(0x1234ABCD, 32, 2048) == (0x1234, 1374, 13)
assert 2 ** 11 * (256 + 16 + 1) == 559104 and 559104 / 8 / 1024 == 68.25 and 2 ** 11 * 275 == 563200
assert 2 ** 10 * (128 + 18 + 1) == 147 * 1024
v(1 + .05 * 100, 6); v(1 + .05 * (10 + .4 * 100), 3.5)
v(1.5 + .02 * 120 + .3 * .05 * 120, 5.7); v(1.5 + .035 * 20 + .013 * 120, 3.76)
v(5.7 / (1.5 + .035 * 240) / 2 * 1, 5.7 / 9.9 / 2); v(5.7 / (9.9 / 2), 1.1515)
assert (1 + 8 * 25 + 1, 1 + 25 + 7 * 6 + 1, 1 + 25 + 8) == (202, 69, 34)
v(32 / 202, 0.158); v(32 / 69, 0.464); v(32 / 34, 0.941)
assert 2 ** 20 * 4 == 4 * 2 ** 20 and 30 * 400 == 12000 and 4e6 / 16 * 400 == 1e8
v(4e6 / 16000 * 1500 / 1e9 * 100, 0.0375)
ok += 4
print("verifica Architettura: %d controlli superati" % ok)
