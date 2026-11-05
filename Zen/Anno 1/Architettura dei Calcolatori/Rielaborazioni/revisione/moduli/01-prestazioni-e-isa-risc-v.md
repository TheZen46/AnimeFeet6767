---
corso: Architettura dei Calcolatori
modulo: 1
titolo: Astrazione, prestazioni e l'ISA RISC-V
programma: [ADC-01, ADC-02]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 1 · Astrazione, prestazioni e l'ISA RISC-V

**In questo modulo.** Servono le reti logiche (porte, registri, rappresentazione dei numeri in complemento a 2). Si parte dall'idea che regge tutta la materia, i livelli di astrazione con le loro interfacce, e dal modello di von Neumann. Poi si impara a misurare le prestazioni di un calcolatore con l'equazione del tempo di CPU e con la legge di Amdahl. La seconda parte presenta l'insieme di istruzioni (ISA) del processore RISC-V: registri, memoria, formati di codifica, istruzioni aritmetiche, di accesso alla memoria e di salto. Alla fine del modulo si sa confrontare due macchine con l'equazione delle prestazioni, e codificare e decodificare a mano un'istruzione RISC-V.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (Introduzione, RISC-V Instruction Set Architecture), articolo di Smith e Nair "The Architecture of Virtual Machines" (*IEEE Computer*, 2005), rapporto di von Neumann sull'EDVAC (1945); Patterson e Hennessy, *Struttura e progetto dei calcolatori*, edizione RISC-V (ADC-01, ADC-02)
> Gli appunti a mano del corso coprono solo il datapath con pipeline (modulo 4): questo modulo è scritto in revisione dal materiale del corso.

## 1.1 Livelli di astrazione e interfacce

Un calcolatore moderno è troppo complesso per essere pensato tutto insieme. Lo si divide in **livelli**, ognuno dei quali offre a quello sopra un insieme di servizi attraverso un'**interfaccia** ben definita e nasconde i dettagli di come li realizza. Dal basso verso l'alto: i transistori e le porte logiche; le reti (sommatori, registri, memorie); la **microarchitettura**, cioè l'organizzazione dei blocchi che eseguono le istruzioni; l'**insieme di istruzioni** (ISA, *instruction set architecture*), che è il confine fra hardware e software; il sistema operativo; i linguaggi e le applicazioni.

L'ISA è l'interfaccia più importante. Descrive tutto ciò che un programmatore in linguaggio macchina deve sapere: quali istruzioni esistono, come si codificano, quali registri ci sono, come si accede alla memoria. Non dice come le istruzioni vengono eseguite: due processori con la stessa ISA (per esempio due generazioni della stessa famiglia) eseguono gli stessi programmi anche se dentro sono molto diversi. È il motivo per cui il software sopravvive a molte generazioni di hardware.

Il prezzo delle interfacce è la rigidità: un programma compilato per un'ISA funziona solo sull'hardware che la realizza, e un sistema operativo solo sull'ISA per cui è scritto. La **virtualizzazione** supera questo limite inserendo uno strato di software che realizza un'interfaccia su un'altra. Una **macchina virtuale di processo** offre a un singolo programma un ambiente diverso da quello reale: la macchina virtuale Java, o un emulatore che esegue codice per un'altra ISA. Una **macchina virtuale di sistema** offre un'intera macchina, su cui gira un sistema operativo completo: è il caso degli *hypervisor* che fanno girare più sistemi operativi sullo stesso server.

## 1.2 Il modello di von Neumann

Quasi tutti i calcolatori seguono lo schema descritto da von Neumann nel 1945: un'**unità centrale** (CPU) con un'unità aritmetico-logica e un'unità di controllo, una **memoria** che contiene sia i dati sia le istruzioni, e i dispositivi di **ingresso e uscita**, collegati da un sistema di interconnessione (i bus). L'idea decisiva è il **programma memorizzato**: le istruzioni sono numeri come i dati, stanno nella stessa memoria, e la macchina si riprogramma cambiando il contenuto della memoria, non i collegamenti.

La CPU esegue le istruzioni con un ciclo che si ripete sempre uguale:

1. **prelievo** (*fetch*): legge dalla memoria l'istruzione all'indirizzo contenuto nel **program counter** (PC);
2. **decodifica**: capisce che istruzione è e legge gli operandi dai registri;
3. **esecuzione**: fa l'operazione nell'ALU, oppure calcola un indirizzo;
4. **accesso alla memoria**, se l'istruzione legge o scrive un dato;
5. **scrittura del risultato** in un registro, e aggiornamento del PC (all'istruzione successiva, o a quella di destinazione di un salto).

Il collegamento fra CPU e memoria è anche il limite del modello: ogni istruzione e ogni dato devono passare di lì, e la memoria è molto più lenta della CPU. È il cosiddetto "collo di bottiglia di von Neumann", a cui rispondono le cache del modulo 5.

## 1.3 Le prestazioni

Per confrontare due calcolatori bisogna decidere che cosa misurare. Il **tempo di esecuzione** (o tempo di risposta) di un programma interessa all'utente; il **throughput**, cioè il lavoro svolto per unità di tempo, interessa a chi gestisce un server. Qui si guarda il tempo di CPU di un programma, e una macchina è "$n$ volte più veloce" di un'altra se
$$\frac{\text{Prestazione}_A}{\text{Prestazione}_B} = \frac{T_B}{T_A} = n.$$

Il processore lavora al ritmo di un clock con periodo $T_{clk}$ (e frequenza $f = 1/T_{clk}$). Ogni istruzione richiede un certo numero di cicli; la media su un programma si chiama **CPI** (*cicli per istruzione*). Allora vale l'**equazione delle prestazioni**:
$$T_{CPU} = N_{istr} \times CPI \times T_{clk} = \frac{N_{istr} \times CPI}{f}.$$

I tre fattori dipendono da cose diverse. $N_{istr}$ dipende dal programma, dal compilatore e dall'ISA; il $CPI$ dalla microarchitettura (e dal tipo di istruzioni usate); $T_{clk}$ dalla tecnologia e dalla microarchitettura. Migliorare uno solo di essi peggiorando gli altri può non servire: è l'errore di giudicare un processore solo dalla frequenza.

Se le istruzioni si dividono in classi con CPI diversi, il CPI medio è la media pesata con le frazioni $\phi_i$ di istruzioni di ogni classe:
$$CPI = \sum_i \phi_i \, CPI_i.$$

> [!esempio] Due compilatori
> Un programma compilato con il compilatore 1 esegue 2 milioni di istruzioni di classe A (CPI 1), 1 milione di classe B (CPI 2) e 1 milione di classe C (CPI 3); con il compilatore 2, 4 milioni di A, 1 di B e 1 di C. Cicli: $2 + 2 + 3 = 7$ milioni contro $4 + 2 + 3 = 9$ milioni. CPI medio: $\frac{7}{4} = 1{,}75$ contro $\frac{9}{6} = 1{,}5$. Il secondo compilatore ha il CPI migliore ma produce più istruzioni, e il programma è più lento: a parità di clock conta il prodotto $N_{istr} \times CPI$, non uno dei due.

Per lo stesso motivo il **MIPS** (milioni di istruzioni al secondo) non è una buona misura: dipende dal programma e dall'ISA, e una macchina con istruzioni più semplici ne esegue di più senza essere più veloce.

> [!teorema] Legge di Amdahl
> Se un miglioramento accelera di un fattore $k$ una parte del programma che occupa la frazione $F$ del tempo di esecuzione, il tempo nuovo è
> $$T' = T\left((1 - F) + \frac{F}{k}\right), \qquad S = \frac{T}{T'} = \frac{1}{(1 - F) + F/k}.$$

La conseguenza è che l'accelerazione complessiva è limitata dalla parte non migliorata: anche con $k \to \infty$, $S \to \frac{1}{1 - F}$. Se le moltiplicazioni occupano l'80% del tempo, nessun moltiplicatore, per quanto veloce, rende il programma più di 5 volte più rapido. La regola pratica è "rendere veloce il caso frequente".

## 1.4 L'ISA RISC-V: registri e memoria

RISC-V è un'ISA aperta, progettata a Berkeley a partire dal 2010, di tipo **RISC** (*reduced instruction set computer*): poche istruzioni semplici, tutte della stessa lunghezza (32 bit nella versione base RV32I), con operazioni aritmetiche solo fra registri e accesso alla memoria solo con istruzioni di load e store (architettura **load/store**). Le scelte seguono quattro principi di progetto: la semplicità favorisce la regolarità; più piccolo è più veloce; rendere veloce il caso frequente; un buon progetto richiede buoni compromessi.

**Registri.** Ci sono 32 registri interi da 32 bit, `x0` … `x31`. `x0` vale sempre 0: scriverci non ha effetto, e serve a ottenere costanti e operazioni utili senza istruzioni apposite. Gli altri hanno un nome "di convenzione" (ABI) che dice a che cosa servono nelle chiamate di procedura (modulo 2):

| Registro | Nome | Uso |
|---|---|---|
| `x0` | `zero` | costante 0 |
| `x1` | `ra` | indirizzo di ritorno |
| `x2` | `sp` | puntatore alla cima dello stack |
| `x3`, `x4` | `gp`, `tp` | puntatore globale, puntatore al thread |
| `x5`–`x7`, `x28`–`x31` | `t0`–`t6` | temporanei (non preservati dalle chiamate) |
| `x8`, `x9`, `x18`–`x27` | `s0`–`s11` | salvati (preservati dalle chiamate); `s0` è anche il frame pointer `fp` |
| `x10`–`x17` | `a0`–`a7` | argomenti; `a0` e `a1` anche valori di ritorno |

**Memoria.** La memoria è un vettore di byte, ciascuno con il suo indirizzo (memoria **indirizzata al byte**). Una parola (*word*) è di 4 byte, e i dati di 4 byte di solito stanno a indirizzi multipli di 4 (**allineamento**). RISC-V è **little endian**: in una parola il byte meno significativo sta all'indirizzo più basso. La parola `0x12345678` scritta all'indirizzo 100 occupa i byte 100 (`0x78`), 101 (`0x56`), 102 (`0x34`), 103 (`0x12`).

## 1.5 I formati delle istruzioni

Tutte le istruzioni RV32I sono lunghe 32 bit e ricadono in sei formati. I campi che compaiono in più formati stanno sempre negli stessi bit, così la decodifica è semplice: l'**opcode** (bit 6-0) dice il formato e la famiglia di istruzioni, `rd` (bit 11-7) è il registro di destinazione, `rs1` (19-15) e `rs2` (24-20) sono i registri sorgente, `funct3` (14-12) e `funct7` (31-25) distinguono le istruzioni con lo stesso opcode.

| Formato | 31-25 | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 | Esempi |
|---|---|---|---|---|---|---|---|
| R | funct7 | rs2 | rs1 | funct3 | rd | opcode | `add`, `sub`, `and`, `slt`, `sll` |
| I | imm[11:0] (12 bit) | | rs1 | funct3 | rd | opcode | `addi`, `lw`, `jalr`, `slli` |
| S | imm[11:5] | rs2 | rs1 | funct3 | imm[4:0] | opcode | `sw`, `sb` |
| B | imm[12, 10:5] | rs2 | rs1 | funct3 | imm[4:1, 11] | opcode | `beq`, `bne`, `blt`, `bge` |
| U | imm[31:12] (20 bit) | | | | rd | opcode | `lui`, `auipc` |
| J | imm[20, 10:1, 11, 19:12] | | | | rd | opcode | `jal` |

Gli **immediati** sono costanti scritte nell'istruzione. Hanno 12 bit nei formati I, S e B, e si estendono con il segno a 32 bit prima dell'uso: un immediato I va da $-2048$ a $2047$. Nel formato S l'immediato è spezzato in due pezzi per lasciare `rs2` al suo posto; nei formati B e J l'immediato è un **offset** rispetto al PC, in multipli di 2 byte (il bit 0 non si scrive perché vale sempre 0), e i suoi bit sono rimescolati per riusare gli stessi fili dell'hardware degli altri formati. Per costanti di 32 bit si combinano `lui` (carica i 20 bit alti) e `addi` (aggiunge i 12 bassi).

> [!esempio] Codificare `add x9, x20, x21`
> È di tipo R: opcode `0110011`, funct3 `000`, funct7 `0000000`. I registri sono `rd` = 9 (`01001`), `rs1` = 20 (`10100`), `rs2` = 21 (`10101`). Mettendo i campi in ordine, dal bit 31 al bit 0:
> $$\underbrace{0000000}_{funct7}\ \underbrace{10101}_{rs2}\ \underbrace{10100}_{rs1}\ \underbrace{000}_{funct3}\ \underbrace{01001}_{rd}\ \underbrace{0110011}_{opcode}$$
> cioè, a gruppi di quattro bit, `0000 0001 0101 1010 0000 0100 1011 0011` = `0x015A04B3`.

## 1.6 Le istruzioni principali

**Aritmetiche e logiche.** `add rd, rs1, rs2` ($rd = rs1 + rs2$), `sub`, `and`, `or`, `xor`; le versioni con immediato `addi`, `andi`, `ori`, `xori` (non esiste `subi`: basta `addi` con un immediato negativo). Gli shift `sll`, `srl` (logico, entra 0) e `sra` (aritmetico, entra il bit di segno), e `slli`, `srli`, `srai`: uno shift a sinistra di $k$ moltiplica per $2^k$. `slt rd, rs1, rs2` mette 1 in `rd` se $rs1 < rs2$ (con segno) e 0 altrimenti; `sltu` fa il confronto senza segno. Non c'è un registro di flag: gli esiti dei confronti finiscono in registri normali.

**Accesso alla memoria.** `lw rd, offset(rs1)` carica la parola all'indirizzo $rs1 + offset$; `sw rs2, offset(rs1)` la scrive. Per i byte: `lb` (estende con il segno), `lbu` (estende con zeri), `sb`; per le mezze parole `lh`, `lhu`, `sh`. L'unico modo di indirizzamento della memoria è registro base più spiazzamento.

**Salti condizionati.** `beq rs1, rs2, etichetta` salta se i registri sono uguali, `bne` se diversi, `blt` e `bge` (con segno), `bltu` e `bgeu` (senza segno). L'assemblatore traduce l'etichetta nell'offset rispetto al PC dell'istruzione di salto.

**Salti incondizionati.** `jal rd, etichetta` salva in `rd` l'indirizzo dell'istruzione successiva ($PC + 4$) e salta; `jalr rd, offset(rs1)` salta all'indirizzo $rs1 + offset$, salvando anch'esso $PC + 4$ in `rd`. Con `rd` = `ra` sono le istruzioni di chiamata di procedura; con `rd` = `x0` sono salti semplici.

**Pseudo-istruzioni.** L'assemblatore accetta istruzioni che non esistono in hardware e le traduce: `li rd, c` (carica una costante, con `addi` o `lui` più `addi`), `mv rd, rs` (`addi rd, rs, 0`), `nop` (`addi x0, x0, 0`), `j etichetta` (`jal x0, …`), `ret` (`jalr x0, 0(ra)`), `la rd, simbolo` (carica un indirizzo), `bgt`, `ble` (con gli operandi scambiati), `neg`, `not`.

**Modi di indirizzamento.** Riassumendo: *immediato* (l'operando è nell'istruzione: `addi`), *registro* (`add`), *base più spiazzamento* (`lw`, `sw`), *relativo al PC* (salti, `auipc`).

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle slide del corso; codifiche controllate con `strumenti/rv.py` e conti con `strumenti/verifica_ampliamento.py` (ADC-01, ADC-02)

**Esercizio 1. Codificare quattro istruzioni.** Scrivere in esadecimale (a) `sub x5, x6, x7`, (b) `addi x5, x6, -12`, (c) `lw x10, 8(x2)`, (d) `sw x10, 12(x2)`.

(a) Tipo R con funct7 `0100000` (è il bit che distingue `sub` da `add`), rs2 = 7, rs1 = 6, funct3 `000`, rd = 5, opcode `0110011`: `0x407302B3`.

(b) Tipo I, opcode `0010011`, funct3 `000`. L'immediato $-12$ su 12 bit in complemento a 2 è `111111110100`. Con rs1 = 6 e rd = 5: `0xFF430293`. Le prime tre cifre esadecimali, `FF4`, sono proprio l'immediato.

(c) Tipo I con opcode `0000011` e funct3 `010` (parola): immediato 8, rs1 = 2, rd = 10: `0x00812503`.

(d) Tipo S, opcode `0100011`, funct3 `010`. L'immediato 12 = `000000001100` si spezza: imm[11:5] = `0000000` nei bit 31-25, imm[4:0] = `01100` nei bit 11-7. Con rs2 = 10 (il dato da scrivere) e rs1 = 2 (la base): `0x00A12623`.

**Esercizio 2. Decodificare.** Che istruzioni sono `0x40B50533` e `0x00C58593`?

`0x40B50533` = `0100 0000 1011 0101 0000 0101 0011 0011`. Opcode `0110011`: tipo R. funct3 = `000`, funct7 = `0100000`: è una `sub`. rd = bit 11-7 = `01010` = 10, rs1 = `01010` = 10, rs2 = `01011` = 11. È `sub x10, x10, x11`, cioè `sub a0, a0, a1`.

`0x00C58593` = `0000 0000 1100 0101 1000 0101 1001 0011`. Opcode `0010011` con funct3 `000`: `addi`. rd = `01011` = 11, rs1 = `01011` = 11, immediato = `000000001100` = 12. È `addi a1, a1, 12`.

**Esercizio 3. Il CPI medio e il confronto fra due macchine.** Un programma ha il 50% di istruzioni ALU, il 20% di load, il 10% di store e il 20% di salti. Sulla macchina A i CPI sono 1, 5, 3, 2 e il clock è a 2 GHz; sulla macchina B sono 1, 2, 2, 2 con clock a 1,5 GHz. Quale macchina è più veloce, e di quanto?

$CPI_A = 0{,}5 + 1 + 0{,}3 + 0{,}4 = 2{,}2$; $CPI_B = 0{,}5 + 0{,}4 + 0{,}2 + 0{,}4 = 1{,}5$. Il numero di istruzioni è lo stesso (stessa ISA, stesso programma), quindi si confrontano i tempi per istruzione: $\frac{2{,}2}{2\ \text{GHz}} = 1{,}1$ ns per A, $\frac{1{,}5}{1{,}5\ \text{GHz}} = 1{,}0$ ns per B. B è più veloce di $\frac{1{,}1}{1{,}0} = 1{,}1$ volte, nonostante il clock più lento.

**Esercizio 4. Amdahl.** In un programma i calcoli in virgola mobile occupano il 40% del tempo. Conviene un'unità in virgola mobile 10 volte più veloce o un miglioramento che accelera tutto del 30%?

Con l'unità nuova: $S = \frac{1}{0{,}6 + 0{,}04} = 1{,}5625$. Con l'accelerazione generale, $S = 1{,}3$. Conviene la prima. Anche con un'unità infinitamente veloce, però, non si andrebbe oltre $\frac{1}{0{,}6} = 1{,}67$.

**Esercizio 5. Costanti di 32 bit.** Come si carica `0x12345678` in `t0`?

`lui t0, 0x12345` mette `0x12345000` in `t0`; `addi t0, t0, 0x678` aggiunge i 12 bit bassi. Funziona perché `0x678` ha il bit 11 a 0. Se i 12 bit bassi avessero il bit 11 a 1, `addi` li estenderebbe con il segno come numero negativo, e bisognerebbe caricare con `lui` la parte alta aumentata di 1: è il conto che fa l'assemblatore quando si scrive la pseudo-istruzione `li t0, 0x12345678`.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni controllate con `strumenti/rv.py` e `strumenti/verifica_ampliamento.py` (ADC-01, ADC-02)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Codificare un salto condizionato.** Codificare `beq x5, x6, +16` (il salto va 16 byte avanti).

*Passo 1: il formato.* `beq` è di tipo B, opcode `1100011`, funct3 `000`.

*Passo 2: l'immediato.* L'offset 16 su 13 bit è `0 0000 0001 0000`: imm[12] = 0, imm[11] = 0, imm[10:5] = `000000`, imm[4:1] = `1000`.

*Passo 3: i campi al loro posto.* Bit 31 = imm[12] = 0; bit 30-25 = imm[10:5] = `000000`; rs2 = 6 = `00110`; rs1 = 5 = `00101`; funct3 = `000`; bit 11-8 = imm[4:1] = `1000`; bit 7 = imm[11] = 0; opcode `1100011`.

*Passo 4: il risultato.* `0000 0000 0110 0010 1000 1000 0110 0011` = `0x00628863`.

**Guidato 2. Quanto si guadagna con un clock più veloce?** Un programma impiega 10 s sulla macchina A con clock a 2 GHz. Si vuole una macchina B che lo esegua in 6 s; con un clock più veloce, però, B ha bisogno di 1,2 volte i cicli di A. Che frequenza serve?

*Passo 1: i cicli di A.* $\text{cicli}_A = T \times f = 10 \times 2 \cdot 10^9 = 2 \cdot 10^{10}$.

*Passo 2: i cicli di B.* $1{,}2 \times 2 \cdot 10^{10} = 2{,}4 \cdot 10^{10}$.

*Passo 3: la frequenza.* $f_B = \frac{2{,}4 \cdot 10^{10}}{6\ \text{s}} = 4$ GHz.

*Passo 4: il controllo.* $\frac{2{,}4 \cdot 10^{10}}{4 \cdot 10^9} = 6$ s. Raddoppiare la frequenza non basta a dimezzare il tempo, perché i cicli aumentano.

**Guidato 3. Little endian.** All'indirizzo 200 c'è la parola `0xA1B2C3D4`. Che cosa carica `lbu t0, 201(zero)`? E `lb t1, 200(zero)`?

*Passo 1: i byte in memoria.* Little endian: 200 → `D4`, 201 → `C3`, 202 → `B2`, 203 → `A1`.

*Passo 2: `lbu`.* Carica `0xC3` ed estende con zeri: `t0` = `0x000000C3` = 195.

*Passo 3: `lb`.* Carica `0xD4`, il cui bit 7 è 1, ed estende il segno: `t1` = `0xFFFFFFD4` = $-44$.

## Riepilogo

Un calcolatore si organizza in livelli di astrazione separati da interfacce, la più importante delle quali è l'ISA, il confine fra hardware e software; la virtualizzazione realizza un'interfaccia sopra un'altra. Il modello di von Neumann mette dati e istruzioni nella stessa memoria e le esegue con il ciclo prelievo-decodifica-esecuzione. Il tempo di CPU è il prodotto di numero di istruzioni, CPI e periodo del clock; nessuno dei tre fattori da solo misura le prestazioni, e la legge di Amdahl limita il guadagno di ogni miglioramento parziale. RISC-V è un'ISA load/store con 32 registri (`x0` sempre nullo), memoria indirizzata al byte e little endian, e istruzioni da 32 bit in sei formati (R, I, S, B, U, J) con i campi dei registri sempre negli stessi bit; gli immediati si estendono con il segno, e gli offset dei salti sono relativi al PC.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (ADC-01, ADC-02)

### Prestazioni

$$T_{CPU} = N_{istr} \cdot CPI \cdot T_{clk}, \qquad CPI = \sum_i \phi_i CPI_i, \qquad \frac{\text{Prest}_A}{\text{Prest}_B} = \frac{T_B}{T_A}, \qquad S_{Amdahl} = \frac{1}{(1 - F) + F/k} \le \frac{1}{1 - F}.$$

### Formati RV32I

| Formato | Campi (dal bit 31 al bit 0) |
|---|---|
| R | funct7 · rs2 · rs1 · funct3 · rd · opcode |
| I | imm[11:0] · rs1 · funct3 · rd · opcode |
| S | imm[11:5] · rs2 · rs1 · funct3 · imm[4:0] · opcode |
| B | imm[12, 10:5] · rs2 · rs1 · funct3 · imm[4:1, 11] · opcode |
| U | imm[31:12] · rd · opcode |
| J | imm[20, 10:1, 11, 19:12] · rd · opcode |

Opcode più usati: `0110011` R, `0010011` I aritmetiche, `0000011` load, `0100011` store, `1100011` branch, `1101111` `jal`, `1100111` `jalr`, `0110111` `lui`.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| ISA | insieme di istruzioni, registri e regole che un programma vede |
| Microarchitettura | organizzazione interna che realizza un'ISA |
| Macchina virtuale di processo / di sistema | ambiente per un programma / per un intero sistema operativo |
| Programma memorizzato | istruzioni e dati nella stessa memoria |
| CPI | numero medio di cicli per istruzione |
| RISC | ISA con poche istruzioni semplici e di lunghezza fissa |
| Architettura load/store | solo load e store accedono alla memoria |
| Little endian | il byte meno significativo all'indirizzo più basso |
| Estensione del segno | ripetere il bit di segno per allungare un numero |
| Pseudo-istruzione | istruzione dell'assemblatore tradotta in istruzioni reali |

### Domande che tornano spesso

- Che cos'è l'ISA e perché è un'interfaccia così importante? Che cosa sono le macchine virtuali?
- Descrivere il modello di von Neumann e il ciclo di esecuzione delle istruzioni.
- Ricavare l'equazione delle prestazioni; perché il MIPS è una misura fuorviante?
- Enunciare la legge di Amdahl e spiegarne le conseguenze.
- Descrivere i formati delle istruzioni RISC-V; perché i campi dei registri sono sempre negli stessi bit?
- Perché nei formati B e J l'immediato è "rimescolato" e non contiene il bit 0?
