# Architettura dei Calcolatori · notazione comune

| Oggetto | Notazione nei moduli | Nelle slide |
|---|---|---|
| Registri | `x0`…`x31` e nomi ABI (`zero`, `ra`, `sp`, `a0`…`a7`, `t0`…`t6`, `s0`…`s11`) | anche `$1`, `$t0`, `$s1` (MIPS) |
| Campi dei registri | `rd`, `rs1`, `rs2` | anche `Rd`, `Rs`, `Rt` |
| Numeri | decimali; esadecimale con `0x`; binario con pedice 2 o in tabella | uguale |
| Unità | 1 KB = 1024 byte nelle cache; $10^3$ dove è detto (esercizio 9 del modulo 5) | uguale |
| Stadi della pipeline | IF, ID, EX, MEM, WB | anche IFetch, Dec, Exec |
| Segnali di forwarding | ForwardA, ForwardB = 00, 10, 01 | uguale |
| Eccezioni | SEPC e SCAUSE (RISC-V) | EPC e Cause (MIPS) |
| Prestazioni | CPI, IPC, $T_c$, AMAT, miss rate $m$, miss penalty $P$ | uguale |

Nei frammenti di codice i commenti sono in italiano; gli indirizzi dei salti sono sempre etichette.

## Convenzioni degli schemi

- Dati in nero, segnali di controllo in blu tratteggiato, parti aggiunte rispetto allo schema precedente in arancio.
- Nomi dei segnali del Patterson-Hennessy (ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp, PCSrc, ForwardA/B, PCWrite, IF/IDWrite, IF.Flush), come nelle slide del corso.
- Ingressi dei multiplexer numerati come il valore del segnale di selezione; i multiplexer di propagazione hanno gli ingressi 00 (registro ID/EX), 10 (EX/MEM), 01 (MEM/WB).

