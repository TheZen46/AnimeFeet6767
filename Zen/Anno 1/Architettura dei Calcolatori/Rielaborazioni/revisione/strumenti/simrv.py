"""Simulatore minimo di RV32I (con mul) per provare i frammenti dei moduli.

Legge il testo assembly dei moduli: etichette, istruzioni e pseudo-istruzioni usate.
"""
import re

NOMI = {"zero": 0, "ra": 1, "sp": 2, "gp": 3, "tp": 4, "t0": 5, "t1": 6, "t2": 7, "s0": 8, "fp": 8, "s1": 9}
NOMI.update({f"a{i}": 10 + i for i in range(8)})
NOMI.update({f"s{i}": 16 + i for i in range(2, 12)})
NOMI.update({f"t{i}": 25 + i for i in range(3, 7)})
NOMI.update({f"x{i}": i for i in range(32)})
M32 = 0xFFFFFFFF


def s32(v):
    v &= M32
    return v - (1 << 32) if v & 0x80000000 else v


class RV:
    def __init__(self, testo):
        self.prog, self.lab = [], {}
        for riga in testo.splitlines():
            riga = riga.split("#")[0].strip()
            while ":" in riga:
                et, riga = riga.split(":", 1)
                self.lab[et.strip()] = len(self.prog)
                riga = riga.strip()
            if riga:
                op, *arg = riga.replace(",", " ").split()
                self.prog.append((op, arg))
        self.x = [0] * 32
        self.mem = {}
        self.chiamate = 0

    def r(self, n):
        return self.x[NOMI[n]]

    def w(self, n, v):
        if NOMI[n]:
            self.x[NOMI[n]] = s32(v)

    def ea(self, a):
        m = re.match(r"(-?\d+)\((\w+)\)", a)
        return int(m.group(1)) + self.r(m.group(2))

    def lw(self, ind):
        return s32(sum(self.mem.get(ind + k, 0) << (8 * k) for k in range(4)))

    def sw(self, ind, v):
        for k in range(4):
            self.mem[ind + k] = (v >> (8 * k)) & 0xFF

    def esegui(self, etichetta, passi=10**6, conta=None):
        RET = -1
        self.x[1] = RET
        self.x[2] = 0x8000
        pc = self.lab[etichetta]
        for _ in range(passi):
            if pc == RET:
                return self.r("a0")
            op, a = self.prog[pc]
            pc += 1
            if conta and op == "jal" and a[-1] == conta:
                self.chiamate += 1
            if op in ("add", "sub", "mul", "and", "or", "xor", "slt"):
                u, v = self.r(a[1]), self.r(a[2])
                self.w(a[0], {"add": u + v, "sub": u - v, "mul": u * v, "and": u & v, "or": u | v,
                              "xor": u ^ v, "slt": int(u < v)}[op])
            elif op in ("addi", "andi", "slli"):
                u, k = self.r(a[1]), int(a[2], 0)
                self.w(a[0], u + k if op == "addi" else (u & k if op == "andi" else u << k))
            elif op == "li":
                self.w(a[0], int(a[1], 0))
            elif op == "mv":
                self.w(a[0], self.r(a[1]))
            elif op == "lw":
                self.w(a[0], self.lw(self.ea(a[1])))
            elif op == "sw":
                self.sw(self.ea(a[1]), self.r(a[0]))
            elif op == "lbu":
                self.w(a[0], self.mem.get(self.ea(a[1]), 0))
            elif op == "sb":
                self.mem[self.ea(a[1])] = self.r(a[0]) & 0xFF
            elif op in ("beq", "bne", "blt", "bge"):
                u, v = self.r(a[0]), self.r(a[1])
                if {"beq": u == v, "bne": u != v, "blt": u < v, "bge": u >= v}[op]:
                    pc = self.lab[a[2]]
            elif op == "j":
                pc = self.lab[a[0]]
            elif op == "jal":
                self.w(a[0], pc)
                pc = self.lab[a[1]]
            elif op == "ret":
                pc = self.r("ra")
            else:
                raise ValueError(op)
        raise RuntimeError("troppi passi")


def blocchi(md):
    """Restituisce i blocchi ```text dei moduli, tolti i '> ' delle citazioni."""
    righe = [r[2:] if r.startswith("> ") else (r[1:] if r.startswith(">") else r) for r in md.splitlines()]
    return re.findall(r"```text\n(.*?)```", "\n".join(righe), re.S)
