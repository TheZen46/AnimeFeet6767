$\begin{array}{l}\text{RV-32I}&\text{32-bit integer instruction set}\\\text{RV-32E}&\text{32-bit integer instruction set for embedded systems}\\\text{RV-64I}&\text{64-bit integer instruction set}\\\text{RV-128I}&\text{128-bit integer instruction set}\end{array}$

Sono anche presenti estensioni

|                 |                    | $xxxxxxxxxxxxxxaa$ | $\text{16-bit }(aa\ne11)$                 |
| --------------- | ------------------ | ------------------ | ----------------------------------------- |
| $\dots xxxx$    | $xxxxxxxxxxxxxxxx$ | $xxxxxxxxxxxbbb11$ | $\text{32-bit }(bb\ne111)$                |
| $\dots xxxx$    | $xxxxxxxxxxxxxxxx$ | $xxxxxxxxxx011111$ | $\text{48-bit}$                           |
| $\dots xxxx$    | $xxxxxxxxxxxxxxxx$ | $xxxxxxxxx0111111$ | $\text{64-bit}$                           |
| $\dots xxxx$    | $xxxxxxxxxxxxxxxx$ | $xnnnxxxxx1111111$ | $(80+16\cdot nnn)\text{-bit},\ nnn\ne111$ |
| $\dots xxxx$    | $xxxxxxxxxxxxxxxx$ | $x111xxxxx1111111$ | $\text{Reserved for }\ge\text{192-bits}$  |
| $\text{base}+4$ | $\text{base}+2$    | $\text{base}$      | $\leftarrow\text{Byte Address}$           |


| $31-25$             | $24-20$      | $19-15$      | $14-12$         | $11-7$            | $6-0$           |                 |
| ------------------- | ------------ | ------------ | --------------- | ----------------- | --------------- | --------------- |
| $\text{funct7}$     | $\text{rs2}$ | $\text{rs1}$ | $\text{funct3}$ | $\text{rd}$       | $\text{opcode}$ | $\text{R-type}$ |
| $\text{imm(11:0)}$  | <            | $\text{rs1}$ | $\text{funct3}$ | $\text{rd}$       | $\text{opcode}$ | $\text{I-type}$ |
| $\text{imm(11:5)}$  | $\text{rs2}$ | $\text{rs1}$ | $\text{funct3}$ | $\text{imm(4:0)}$ | $\text{opcode}$ | $\text{S-type}$ |
| $\text{imm(31:12)}$ | <            | <            | <               | $\text{rd}$       | $\text{opcode}$ | $\text{U-type}$ |

| $\text{Instruction}$ | $\text{Name}$ | $\text{Description}$ |
| -------------------- | ------------- | -------------------- |
| $\text{add}$         | $\text{ADD}$  | $rd=rs1+rs2$         |
| $\text{sub}$         | $\text{SUB}$  | $rd=rs1-rs2$         |
| $\text{xor}$         | $\text{XOR}$  | $rd=rs1\oplus rs2$   |
|                      |               | $rd=rs1\|rs2$        |
|                      |               | $rd=rs1&rs2$         |

| $\underset{\text{offset}}{\text{imm(11:0)}}$ | <            | $\text{rs1}$ | $010$ | $\text{rd}$       | $0000011$ | LW (load)  |
| -------------------------------------------- | ------------ | ------------ | ----- | ----------------- | --------- | ---------- |
| $\underset{\text{offset}}{\text{imm(11:5)}}$ | $\text{rs2}$ | $\text{rs1}$ | $010$ | $\text{imm(4:0)}$ | $0100011$ | SW (store) |
