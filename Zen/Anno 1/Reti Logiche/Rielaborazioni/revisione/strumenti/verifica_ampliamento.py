"""Verifica degli esercizi aggiunti nell'ampliamento di novembre 2026 (moduli 1-4).

Ogni controllo confronta l'espressione scritta nel modulo con la specifica,
su tutte le combinazioni degli ingressi (induzione perfetta), oppure simula
le sequenze fronte per fronte.
"""
from itertools import product
import struct

N = lambda x: 1 - x  # noqa: E731
X = lambda a, b: a ^ b  # noqa: E731
ok = 0


def chk(nome, spec, expr, n, dc=lambda *v: False):
    global ok
    for v in product([0, 1], repeat=n):
        if dc(*v):
            continue
        assert int(bool(spec(*v))) == int(bool(expr(*v))), (nome, v)
    ok += 1


# ---- modulo 1
chk("es4 xor", lambda A, B: A ^ B, lambda A, B: N(A & B) & (A | B), 2)
chk("es5 err", lambda d2, d1, d0, rp: (d2 + d1 + d0 + rp) % 2 == 0,
    lambda d2, d1, d0, rp: (lambda c1, c2: c1 & c2 | N(c1) & N(c2))(
        d2 & N(d1) | N(d2) & d1, d0 & N(rp) | N(d0) & rp), 4)
f6 = lambda x, y, z: (x, y, z) in [(0, 0, 1), (0, 1, 0), (1, 1, 1)]  # noqa: E731
chk("es6 sop", f6, lambda x, y, z: N(x) & N(y) & z | N(x) & y & N(z) | x & y & z, 3)
chk("es6 pos", f6, lambda x, y, z: (y | z) & (N(x) | y) & (N(x) | z) & (x | N(y) | N(z)), 3)


def pg(F1, F0, A, B):
    return {(0, 0): N(A | B), (0, 1): N(A ^ B), (1, 0): N(A & B)}.get((F1, F0), 0)


chk("es7", pg, lambda F1, F0, A, B: N(A) & N(B) | F1 & N(A) | F1 & N(B) | F0 & A & B, 4,
    lambda F1, F0, A, B: F1 == 1 and F0 == 1)


def f8(x, y, z, t):
    if x == 0:
        return (y, z, t) in [(0, 0, 0), (0, 1, 0), (0, 1, 1), (1, 1, 1)]
    return (y, z, t) == (0, 0, 1)


chk("es8", f8, lambda x, y, z, t: z & t | x & N(y) | N(y) & N(t), 4,
    lambda x, y, z, t: x == 1 and (y, z, t) not in [(0, 0, 1), (1, 0, 1)])
chk("g1 sop", lambda A, B, C: 4 * A + 2 * B + C in (2, 3, 5, 7), lambda A, B, C: N(A) & B | A & C, 3)
chk("g1 pos", lambda A, B, C: 4 * A + 2 * B + C in (2, 3, 5, 7), lambda A, B, C: (A | B) & (N(A) | C), 3)
chk("g1 nand", lambda A, B, C: N(A) & B | A & C, lambda A, B, C: N(N(N(A) & B) & N(A & C)), 3)
seg = lambda A, B, C, D: 8 * A + 4 * B + 2 * C + D in (0, 2, 3, 5, 6, 7, 8, 9)  # noqa: E731
chk("g2 seg a", seg, lambda A, B, C, D: A | C | B & D | N(B) & N(D), 4,
    lambda A, B, C, D: 8 * A + 4 * B + 2 * C + D > 9)
chk("g3", lambda A, B, C: N((N(A) | B) & N(C)) | A & N(B) & C, lambda A, B, C: A & N(B) | C, 3)

# ---- modulo 2
chk("es5 mux consenso", lambda s, i0, i1: i1 if s else i0,
    lambda s, i0, i1: N(s) & i0 | s & i1 | i0 & i1, 3)
mux8 = lambda dati: (lambda C, B, A: dati[4 * C + 2 * B + A])  # noqa: E731
chk("es8 maggioranza", mux8([0, 0, 0, 1, 0, 1, 1, 1]), lambda C, B, A: A & B | A & C | B & C, 3)
u8 = lambda C, B, A: C & N(A) | B & N(C) & A | N(B) & N(A) & N(C)  # noqa: E731
chk("es8 dati", mux8([1, 0, 0, 1, 1, 0, 1, 0]), u8, 3)
chk("es8 mux4", u8, lambda C, B, A: [N(A), A, N(A), N(A)][2 * C + B], 3)
v = lambda a1, a0: 2 * a1 + a0  # noqa: E731
chk("es9 G", lambda a1, a0, b1, b0: v(a1, a0) > v(b1, b0),
    lambda a1, a0, b1, b0: a1 & N(b1) | a1 & a0 & N(b0) | a0 & N(b1) & N(b0), 4)
chk("es9 L", lambda a1, a0, b1, b0: v(a1, a0) < v(b1, b0),
    lambda a1, a0, b1, b0: N(a1) & b1 | b1 & b0 & N(a0) | b0 & N(a1) & N(a0), 4)
chk("es9 E", lambda a1, a0, b1, b0: v(a1, a0) == v(b1, b0),
    lambda a1, a0, b1, b0: N(a1 ^ b1) & N(a0 ^ b0), 4)
P = lambda k: (lambda a1, a0, b1, b0: (v(a1, a0) * v(b1, b0) >> k) & 1)  # noqa: E731
chk("es10 P0", P(0), lambda a1, a0, b1, b0: a0 & b0, 4)
chk("es10 P3", P(3), lambda a1, a0, b1, b0: a1 & a0 & b1 & b0, 4)
chk("es10 P2", P(2), lambda a1, a0, b1, b0: a1 & b1 & N(a0) | a1 & b1 & N(b0), 4)
chk("es10 P1", P(1), lambda a1, a0, b1, b0: a0 & b1 & N(a1) | a0 & b1 & N(b0) | a1 & b0 & N(a0) | a1 & b0 & N(b1), 4)
for k, g in [(1, lambda a1, a0, b1, b0: (a1 & b0) ^ (a0 & b1)),
             (2, lambda a1, a0, b1, b0: (a1 & b1) ^ (a1 & b0 & a0 & b1)),
             (3, lambda a1, a0, b1, b0: a1 & b1 & a1 & b0 & a0 & b1)]:
    chk("es10 multilivello P%d" % k, P(k), g, 4)
assert 3 * 2 == 0b0110
c2 = lambda a, b, c: 4 * a + 2 * b + c - 8 * a  # noqa: E731
dc11 = lambda a, b, c: (a, b, c) == (1, 0, 0)  # noqa: E731
chk("es11 Y0", lambda a, b, c: abs(c2(a, b, c)) & 1, lambda a, b, c: c, 3, dc11)
chk("es11 Y1", lambda a, b, c: abs(c2(a, b, c)) >> 1 & 1, lambda a, b, c: b & N(c) | N(a) & b | a & N(b), 3, dc11)
chk("es11 Y1 xor", lambda a, b, c: abs(c2(a, b, c)) >> 1 & 1, lambda a, b, c: b ^ (a & c), 3, dc11)
chk("es11 ERR", lambda a, b, c: c2(a, b, c) == -4, lambda a, b, c: a & N(b) & N(c), 3)
assert 0b101 ^ 0b111 == 0b010 and 0b010 + 1 == 3
S = lambda k: (lambda a1, a0, b1, b0: (v(a1, a0) + v(b1, b0) >> k) & 1)  # noqa: E731
chk("es12 S0", S(0), lambda a1, a0, b1, b0: a0 ^ b0, 4)
chk("es12 S2", S(2), lambda a1, a0, b1, b0: a1 & b1 | a1 & a0 & b0 | a0 & b1 & b0, 4)
chk("es12 S1", S(1), lambda a1, a0, b1, b0: a1 & N(b1) & N(a0) | a1 & N(b1) & N(b0) | N(a1) & b1 & N(a0)
    | N(a1) & b1 & N(b0) | N(a1) & N(b1) & a0 & b0 | a1 & b1 & a0 & b0, 4)
chk("es12 cascata S1", S(1), lambda a1, a0, b1, b0: a1 ^ b1 ^ (a0 & b0), 4)
chk("es12 cascata S2", S(2), lambda a1, a0, b1, b0: a1 & b1 | (a0 & b0) & (a1 | b1), 4)
chk("es13", lambda A, B: A ^ B, lambda A, B: N(N(A | B) | A & B), 2)
chk("es13 mux", lambda A, B: A ^ B, lambda A, B: N(B) if A else B, 2)
chk("g1 mux", lambda A, B, C: 4 * A + 2 * B + C in (1, 2, 6, 7), lambda A, B, C: [C, N(C), 0, 1][2 * A + B], 3)


def add8(a, b):
    s = (a + b) & 0xFF
    c8 = (a + b) >> 8
    c7 = ((a & 0x7F) + (b & 0x7F)) >> 7
    return s, c7, c8


neg = lambda x: (~x + 1) & 0xFF  # noqa: E731
assert neg(50) == 0b11001110 and neg(100) == 0b10011100
assert add8(100, 50) == (0b10010110, 1, 0) and 0b10010110 - 256 == -106
assert add8(100, neg(50)) == (50, 1, 1)
assert add8(neg(100), neg(50)) == (0b01101010, 0, 1) and 0b01101010 == 106
chk("g3 alea", lambda A, B, C: A & N(C) | B & C, lambda A, B, C: A & N(C) | B & C | A & B, 3)
assert [4 * a + 2 * b + c for a, b, c in product([0, 1], repeat=3) if a & N(c) | b & c] == [3, 4, 6, 7]
fl = lambda x: struct.pack(">f", x).hex().upper()  # noqa: E731
assert fl(-6.75) == "C0D80000" and fl(-13.625) == "C15A0000"
assert struct.unpack(">f", bytes.fromhex("41200000"))[0] == 10.0
assert 1.5 + 0.375 == 1.875 and 0.375 == 2**-2 + 2**-3 and 0.625 == 0.5 + 0.125
assert struct.unpack(">f", struct.pack(">f", 2.0**24 + 1))[0] == 2.0**24
assert abs((2 - 2**-23) * 2.0**127 - 3.4028235e38) < 1e31 and abs(2.0**-126 - 1.1754944e-38) < 1e-44
ok += 1

# ---- modulo 3
q = 0
tab = []
for pr, cl, en, d in [(1, 0, 0, 0), (1, 1, 0, 1), (1, 1, 1, 1), (1, 1, 1, 0), (1, 1, 0, 1), (0, 1, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0)]:
    q = 0 if cl == 0 else 1 if pr == 0 else (d if en else q)
    tab.append(q)
assert tab == [0, 0, 1, 0, 0, 1, 1, 0], tab
q = 0
tab = []
for e, d in [(0, 1), (1, 1), (0, 0), (1, 0), (0, 1), (1, 1)]:
    q = e & d | N(e) & q
    tab.append(q)
assert tab == [0, 1, 1, 0, 0, 1]
q = 0
tab = []
for j, k in [(1, 0), (0, 0), (1, 1), (1, 1), (0, 1), (0, 1), (1, 0), (1, 1)]:
    q = j & N(q) | N(k) & q
    tab.append(q)
assert tab == [1, 1, 0, 1, 0, 0, 1, 0]
s = (0, 0, 0)
vals = [0]
for d in [1, 0, 1, 1, 0, 0]:
    s = (d, s[0], s[1])
    vals.append(c2(*s))
assert vals == [0, -4, 2, -3, -2, 3, 1], vals
for n in range(16):
    q3, q2, q1, q0 = (n >> 3) & 1, (n >> 2) & 1, (n >> 1) & 1, n & 1
    nx = (q3 ^ (q2 & q1 & q0)) << 3 | (q2 ^ (q1 & q0)) << 2 | (q1 ^ q0) << 1 | N(q0)
    assert nx == (n + 1) % 16
st = 0
seq = []
for _ in range(8):
    q2, q1, q0 = st >> 2 & 1, st >> 1 & 1, st & 1
    t2, t1, t0 = q1 & q0 | q2 & q0, N(q2) & q0, 1
    st = st ^ (t2 << 2 | t1 << 1 | t0)
    seq.append(st)
assert seq[:6] == [1, 2, 3, 4, 5, 0]
for start, att in [(6, 7), (7, 2)]:
    q2, q1, q0 = start >> 2 & 1, start >> 1 & 1, start & 1
    assert start ^ ((q1 & q0 | q2 & q0) << 2 | (N(q2) & q0) << 1 | 1) == att
assert 12 + 7 + 6 == 25 and abs(1 / 25e-9 - 40e6) < 1
a = b = 0
tab = []
for x in [1, 1, 0, 0, 1, 0]:
    a, b = x ^ b, a
    tab.append((a, b))
assert tab == [(1, 0), (1, 1), (1, 1), (1, 1), (0, 1), (1, 0)]
ok += 1

# ---- modulo 4
q1 = q0 = 0
tab = []
for x in [1, 1, 0, 1, 1, 1]:
    z = x & q1 & q0
    q1, q0 = q1 ^ (x & q0), q0 ^ x
    tab.append((q1, q0, z))
assert [(a, b) for a, b, _ in tab] == [(0, 1), (1, 0), (1, 0), (1, 1), (0, 0), (0, 1)]
assert [z for *_, z in tab] == [0, 0, 0, 0, 1, 0]
q1 = q0 = 0
tab = []
for x in [1, 1, 1, 0, 1, 0, 1, 1]:
    q1, q0 = x & q0, x
    tab.append((q1, q0))
assert tab == [(0, 1), (1, 1), (1, 1), (0, 0), (0, 1), (0, 0), (0, 1), (1, 1)]
q1 = q0 = 0
tab = []
for dn in [0] * 4 + [1] * 4:
    q1, q0 = q1 ^ (q0 ^ dn), q0 ^ 1
    tab.append(2 * q1 + q0)
assert tab == [1, 2, 3, 0, 3, 2, 1, 0]
# ricevitore: simulazione della tabella degli stati
T = {"I": ("I", "S1"), "S1": ("I", "S2"), "S2": ("B0", "B1"), "B0": ("P0", "E"), "B1": ("P1", "E"),
     "P0": ("V0", "E"), "P1": ("V1", "E"), "V0": ("I", "S1"), "V1": ("I", "S1"), "E": ("I", "E")}


def ricevi(bits):
    s, out = "I", []
    for b_ in bits:
        s = T[s][b_]
        out.append(s)
    return out


r = ricevi([0, 1, 1, 1, 0, 0, 0, 0])
assert r[5] == "V1" and r.count("V0") == 0 and "E" not in r
r = ricevi([1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0])
assert r[4] == "V0" and r[9] == "V1"
assert "E" in ricevi([1, 1, 0, 1, 0]) and ricevi([1, 0, 0])[-1] == "I"
reg = [1, 1, 1, 0, 0, 0]
assert reg[1:6] == [1, 1, 0, 0, 0]  # la falsa rilevazione del registro a scorrimento
# rilevatore 101
for mealy in (False, True):
    q1 = q0 = 0
    zs = []
    for x in [1, 0, 1, 0, 1, 1]:
        if mealy:
            zs.append(q1 & x)
            q1, q0 = q0 & N(x), x
        else:
            q1, q0 = q0 & N(x) | q1 & N(q0) & x, x
            zs.append(q1 & q0)
    assert zs == [0, 0, 1, 0, 1, 0], (mealy, zs)
ok += 1
print("verifica ampliamento: %d controlli superati" % ok)
