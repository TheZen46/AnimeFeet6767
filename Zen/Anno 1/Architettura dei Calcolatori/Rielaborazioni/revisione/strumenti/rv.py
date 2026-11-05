"""Codifica e decodifica di istruzioni RISC-V RV32I usate negli esercizi."""


def R(f7, rs2, rs1, f3, rd, op=0x33):
    return (f7 << 25) | (rs2 << 20) | (rs1 << 15) | (f3 << 12) | (rd << 7) | op


def I(imm, rs1, f3, rd, op=0x13):
    return ((imm & 0xFFF) << 20) | (rs1 << 15) | (f3 << 12) | (rd << 7) | op


def S(imm, rs2, rs1, f3, op=0x23):
    imm &= 0xFFF
    return ((imm >> 5) << 25) | (rs2 << 20) | (rs1 << 15) | (f3 << 12) | ((imm & 0x1F) << 7) | op


def B(imm, rs2, rs1, f3, op=0x63):
    imm &= 0x1FFF
    return (((imm >> 12) & 1) << 31) | (((imm >> 5) & 0x3F) << 25) | (rs2 << 20) | (rs1 << 15) | (f3 << 12) \
        | (((imm >> 1) & 0xF) << 8) | (((imm >> 11) & 1) << 7) | op


def campi(w):
    return dict(op=w & 0x7F, rd=(w >> 7) & 31, f3=(w >> 12) & 7, rs1=(w >> 15) & 31, rs2=(w >> 20) & 31, f7=w >> 25)


if __name__ == "__main__":
    for nome, w in [("add x9,x20,x21", R(0, 21, 20, 0, 9)), ("sub x5,x6,x7", R(0x20, 7, 6, 0, 5)),
                    ("addi x5,x6,-12", I(-12, 6, 0, 5)), ("lw x10,8(x2)", I(8, 2, 2, 10, 0x03)),
                    ("sw x10,12(x2)", S(12, 10, 2, 2)), ("beq x5,x6,16", B(16, 6, 5, 0))]:
        print(f"{nome:18s} 0x{w:08X} {w:032b}")
    print(campi(0x40B50533), campi(0x00C58593))
