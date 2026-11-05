---
corso: Architettura dei Calcolatori
modulo: 2
titolo: Programmazione in assembly RISC-V
programma: [ADC-02]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 2 · Programmazione in assembly RISC-V

**In questo modulo.** Si usano i registri, i formati e le istruzioni del modulo 1 (*Astrazione, prestazioni e l'ISA RISC-V*), e un po' di C. Si vede come un compilatore traduce in assembly i costrutti del C: espressioni, condizioni, cicli, accessi ad array, matrici e stringhe. Poi si studia il modello di memoria di un programma (codice, dati statici, heap, stack) e il meccanismo delle procedure: passaggio dei parametri, convenzioni sui registri, stack frame, procedure annidate e ricorsive. Infine si fa il percorso inverso, dall'assembly al C. Alla fine del modulo si sanno scrivere e leggere programmi RISC-V con cicli, array e chiamate di funzione, e provarli nel simulatore.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (Gestione chiamate a funzione, Vettori e matrici, Fibonacci, Merge Sort, Reverse coding, Simulatore QtRvSim), programmi di esempio `Simple.s` e `Strlen.s`; Patterson e Hennessy, *Struttura e progetto dei calcolatori*, cap. 2 (ADC-02)
> Il modulo è scritto in revisione dal materiale del corso. Tutti i frammenti di codice sono stati eseguiti con il simulatore di `strumenti/verifica_ampliamento.py`. Nelle slide alcuni esempi usano la notazione MIPS (`$t0`, `$s1`); qui si usa sempre quella RISC-V.

## 2.1 Dal C all'assembly: espressioni e condizioni

Un compilatore assegna le variabili a registri e traduce ogni espressione in una sequenza di istruzioni con risultati intermedi nei temporanei. Con `f`, `g`, `h`, `i`, `j` in `s0`…`s4`, l'istruzione C `f = (g + h) - (i + j);` diventa

```text
add  t0, s1, s2      # t0 = g + h
add  t1, s3, s4      # t1 = i + j
sub  s0, t0, t1      # f = t0 - t1
```

Le condizioni diventano salti condizionati, di solito con la **condizione negata**: si salta oltre il ramo "vero" quando la condizione è falsa. Per `if (i == j) f = g + h; else f = g - h;`:

```text
      bne  s3, s4, Else   # se i != j salta al ramo else
      add  s0, s1, s2     # f = g + h
      j    Fine           # salta oltre il ramo else
Else: sub  s0, s1, s2     # f = g - h
Fine:
```

Un ciclo è un salto all'indietro. `while (v[i] == k) i += 1;`, con `i` in `s3`, `k` in `s5` e l'indirizzo di `v` in `s6`:

```text
Ciclo: slli t1, s3, 2     # t1 = 4 * i (ogni intero occupa 4 byte)
       add  t1, t1, s6    # t1 = indirizzo di v[i]
       lw   t0, 0(t1)     # t0 = v[i]
       bne  t0, s5, Esci  # se v[i] != k esci
       addi s3, s3, 1     # i += 1
       j    Ciclo
Esci:
```

Un `for (i = 0; i < n; i++)` si traduce allo stesso modo: inizializzazione prima del ciclo, controllo con `bge` (uscita se $i \ge n$) all'inizio, incremento e salto all'indietro alla fine.

## 2.2 Array e matrici

L'indirizzo dell'elemento `v[i]` di un array di interi è $\text{base} + 4i$: l'indice va moltiplicato per la dimensione dell'elemento, cioè shiftato a sinistra di 2 (`slli`). Per un array di `char` la dimensione è 1 e lo shift non serve. È la differenza principale fra l'indice del C, che conta elementi, e l'indirizzo, che conta byte.

Una matrice C `int M[R][C]` è memorizzata **per righe** (*row-major*): prima tutta la riga 0, poi la riga 1, e così via. L'elemento `M[i][j]` ha indirizzo
$$\text{base} + (i \cdot C + j) \cdot 4.$$
Se $C$ è una potenza di 2 la moltiplicazione $i \cdot C$ è uno shift; altrimenti si usa `mul` (estensione M di RISC-V) o una somma ripetuta. Scorrendo la matrice con un puntatore che avanza di 4 byte si visitano gli elementi nell'ordine della memoria, riga per riga.

> [!esempio] Somma degli elementi di un array
> La funzione `int somma(int v[], int n)` riceve l'indirizzo di `v` in `a0` e `n` in `a1`, e restituisce il risultato in `a0`.
>
> ```text
> somma:  li   t0, 0          # i = 0
>         li   t1, 0          # s = 0
> ciclo:  bge  t0, a1, fine   # se i >= n esci
>         slli t2, t0, 2      # t2 = 4 * i
>         add  t2, a0, t2     # t2 = &v[i]
>         lw   t3, 0(t2)      # t3 = v[i]
>         add  t1, t1, t3     # s += v[i]
>         addi t0, t0, 1      # i++
>         j    ciclo
> fine:   mv   a0, t1         # risultato in a0
>         ret
> ```

## 2.3 Byte e stringhe

Una stringa C è un array di byte terminato dal carattere nullo (codice 0). Si legge un carattere alla volta con `lbu` (senza segno: i codici vanno da 0 a 255) e si scrive con `sb`. La lunghezza di una stringa si calcola facendo avanzare un puntatore fino allo 0:

```text
strlen: mv   t0, a0         # t0 = puntatore al carattere corrente
loop:   lbu  t1, 0(t0)      # t1 = *t0
        beq  t1, zero, end  # fine della stringa
        addi t0, t0, 1      # carattere successivo
        j    loop
end:    sub  a0, t0, a0     # lunghezza = puntatore finale - iniziale
        ret
```

Qui si usa l'**aritmetica dei puntatori** invece di un indice: invece di calcolare a ogni giro $\text{base} + i$, si incrementa direttamente l'indirizzo, e si risparmiano istruzioni. È la stessa ottimizzazione che fa un compilatore.

## 2.4 Il modello di memoria di un programma

Lo spazio di indirizzamento di un programma RISC-V è diviso in zone, dal basso verso l'alto:

| Zona | Contenuto |
|---|---|
| riservata | indirizzi bassi non usati |
| testo (*text*) | il codice macchina |
| dati statici (*data*) | variabili globali e costanti, raggiunte tramite `gp` |
| heap | memoria allocata dinamicamente (`malloc`, `new`), cresce verso l'alto |
| stack | variabili locali e dati delle chiamate, cresce verso il basso da `sp` |

Heap e stack crescono uno verso l'altro, così lo spazio libero in mezzo può servire all'uno o all'altro. Nel sorgente assembly le zone si scelgono con le **direttive**: `.text` per il codice, `.data` per i dati; `.word 3, 5, 7` riserva e inizializza parole, `.asciz "ciao"` una stringa con lo 0 finale, `.space n` riserva $n$ byte. Nel simulatore QtRvSim del corso il programma comincia all'etichetta `_start` (dichiarata con `.globl _start`), e si possono seguire passo per passo i registri, la memoria e la pipeline; il programma termina con una chiamata di sistema (`ecall`) o con un ciclo infinito di arresto.

## 2.5 Le procedure

Una chiamata di procedura richiede sei passi: (1) il chiamante mette gli argomenti dove la procedura li cerca; (2) trasferisce il controllo; (3) la procedura si procura la memoria che le serve; (4) svolge il suo compito; (5) mette il risultato dove il chiamante lo cerca; (6) restituisce il controllo al punto da cui era stata chiamata.

In RISC-V gli argomenti vanno in `a0`…`a7` (gli altri, se ce ne sono di più, sullo stack), il risultato in `a0` (e `a1`). La chiamata è `jal ra, procedura` (scritta anche `call procedura`), che salva in `ra` l'indirizzo di ritorno; il ritorno è `jalr zero, 0(ra)`, cioè `ret`.

Il problema è che chiamante e procedura usano gli stessi 32 registri. La **convenzione di chiamata** divide il lavoro:

- i registri **salvati** `s0`…`s11`, `sp` e `ra` (dal punto di vista del chiamante) devono avere, al ritorno, lo stesso valore che avevano alla chiamata: se la procedura li usa, li salva sullo stack all'inizio e li ripristina alla fine (*callee-saved*);
- i registri **temporanei** `t0`…`t6` e gli argomenti `a0`…`a7` possono essere modificati dalla procedura: se il chiamante ne ha bisogno dopo la chiamata, è lui a salvarli (*caller-saved*).

Lo **stack** si usa così: per riservare $k$ byte si sottrae $k$ a `sp` (`addi sp, sp, -k`), si salvano i registri con `sw` a offset positivi da `sp`, e alla fine si ripristinano e si rilascia lo spazio (`addi sp, sp, k`). La zona di stack di una chiamata si chiama **stack frame** (o record di attivazione). `sp` resta allineato a 16 byte nella convenzione standard; negli esempi del corso, per semplicità, si riservano solo i byte necessari.

Una procedura che non ne chiama altre (**procedura foglia**) spesso non ha bisogno dello stack: usa i temporanei e non tocca `ra`. Una procedura che ne chiama altre deve salvare almeno `ra`, perché la sua `jal` lo sovrascrive, e i registri che le servono dopo la chiamata.

## 2.6 Procedure ricorsive

Una procedura ricorsiva è una procedura non foglia che chiama sé stessa: ogni chiamata ha il suo stack frame con i suoi valori.

> [!esempio] Fattoriale
> `int fact(int n) { return n < 2 ? 1 : n * fact(n - 1); }`
>
> ```text
> fact:   addi sp, sp, -8     # spazio per ra e n
>         sw   ra, 4(sp)
>         sw   a0, 0(sp)      # salva n
>         li   t0, 2
>         blt  a0, t0, base   # n < 2: caso base
>         addi a0, a0, -1
>         jal  ra, fact       # a0 = fact(n - 1)
>         lw   t1, 0(sp)      # t1 = n (salvato prima della chiamata)
>         mul  a0, a0, t1     # a0 = n * fact(n - 1)
>         j    esci
> base:   li   a0, 1
> esci:   lw   ra, 4(sp)
>         addi sp, sp, 8
>         ret
> ```
>
> Per `fact(3)` lo stack contiene, al momento più profondo, tre frame con $n = 3, 2, 1$ e i rispettivi indirizzi di ritorno; i frame si liberano in ordine inverso mentre si calcolano $1$, $2 \cdot 1$, $3 \cdot 2$.

> [!esempio] Fibonacci
> `int fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }`. Dopo la prima chiamata ricorsiva serve ancora sia $n$ sia $fib(n - 1)$: si tengono in due registri salvati, `s0` e `s1`, che vanno quindi salvati sullo stack.
>
> ```text
> fib:    li   t0, 2
>         blt  a0, t0, fine   # n < 2: restituisce n, che è già in a0
>         addi sp, sp, -12
>         sw   ra, 8(sp)
>         sw   s0, 4(sp)
>         sw   s1, 0(sp)
>         mv   s0, a0         # s0 = n
>         addi a0, s0, -1
>         jal  ra, fib        # a0 = fib(n - 1)
>         mv   s1, a0         # s1 = fib(n - 1)
>         addi a0, s0, -2
>         jal  ra, fib        # a0 = fib(n - 2)
>         add  a0, s1, a0
>         lw   s1, 0(sp)
>         lw   s0, 4(sp)
>         lw   ra, 8(sp)
>         addi sp, sp, 12
> fine:   ret
> ```
>
> Nel caso base la procedura è foglia e non tocca lo stack. Il numero di chiamate cresce come i numeri di Fibonacci stessi: `fib(10)` = 55 richiede 177 chiamate. La versione con un ciclo ne richiede una.

## 2.7 Dall'assembly al C

Leggere un programma assembly vuol dire ricostruire le variabili (a quali registri corrispondono), i cicli (i salti all'indietro) e le condizioni (i salti in avanti, con la condizione negata). Si procede così: si individuano gli argomenti (`a0`, `a1`…) e il valore di ritorno; si cerca il salto all'indietro, che chiude un ciclo, e il salto di uscita; si traduce il corpo istruzione per istruzione; infine si riscrive il tutto in un C leggibile, con i nomi delle variabili e un `for` dove c'è un contatore.

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle slide (Vettori e matrici, Reverse coding, Fibonacci); tutti i programmi eseguiti con il simulatore di `strumenti/verifica_ampliamento.py` (ADC-02)

**Esercizio 1. Il massimo di un array.** Scrivere `int max(int v[], int n)` (con $n \ge 1$).

```text
max:    lw   t1, 0(a0)      # m = v[0]
        li   t0, 1          # i = 1
ciclo:  bge  t0, a1, fine
        slli t2, t0, 2
        add  t2, a0, t2
        lw   t3, 0(t2)      # t3 = v[i]
        bge  t1, t3, avanti # se m >= v[i] non cambia
        mv   t1, t3         # m = v[i]
avanti: addi t0, t0, 1
        j    ciclo
fine:   mv   a0, t1
        ret
```

Con $v = (3, -2, 9, 4)$ restituisce 9. La condizione del C è `if (v[i] > m) m = v[i];`, e il salto la nega: si salta oltre l'assegnamento se $m \ge v[i]$.

**Esercizio 2. La traccia di una matrice.** `M` è una matrice $N \times N$ di interi, con l'indirizzo in `a0` e $N$ in `a1`. Scrivere la somma degli elementi della diagonale.

L'elemento `M[i][i]` è all'indirizzo $\text{base} + (iN + i) \cdot 4 = \text{base} + i(N + 1) \cdot 4$: passando da un elemento della diagonale al successivo l'indirizzo cresce di $4(N + 1)$. Conviene quindi un puntatore che avanza di quel passo:

```text
traccia: addi t2, a1, 1     # t2 = N + 1
         slli t2, t2, 2     # passo = 4(N + 1) byte
         li   t0, 0         # i = 0
         li   t1, 0         # s = 0
ciclo:   bge  t0, a1, fine
         lw   t3, 0(a0)     # M[i][i]
         add  t1, t1, t3
         add  a0, a0, t2    # puntatore al prossimo elemento della diagonale
         addi t0, t0, 1
         j    ciclo
fine:    mv   a0, t1
         ret
```

Per la matrice $3 \times 3$ con elementi $1, \dots, 9$ per righe la traccia è $1 + 5 + 9 = 15$.

**Esercizio 3. Reverse coding.** Che cosa calcola questa funzione, con l'indirizzo di un array in `a0` e la sua lunghezza in `a1`?

```text
        li   t0, 0
        li   t1, 0
L1:     bge  t0, a1, L3
        slli t2, t0, 2
        add  t2, a0, t2
        lw   t3, 0(t2)
        bge  t3, zero, L2
        addi t1, t1, 1
L2:     addi t0, t0, 1
        j    L1
L3:     mv   a0, t1
        ret
```

`t0` parte da 0, cresce di 1 e il ciclo esce quando arriva ad `a1`: è un indice $i$ da 0 a $n - 1$. Il corpo carica `v[i]` e, se **non** è $\ge 0$, cioè se è negativo, incrementa `t1`, che è restituito. In C:

```c
int conta_negativi(int v[], int n) {
    int c = 0;
    for (int i = 0; i < n; i++)
        if (v[i] < 0) c++;
    return c;
}
```

**Esercizio 4. Una procedura che ne chiama un'altra.** Scrivere `int somma_quadrati(int a, int b)` che restituisce $a^2 + b^2$ usando una procedura foglia `quad(x)` che restituisce $x^2$.

```text
quad:   mul  a0, a0, a0     # foglia: niente stack
        ret

somma_quadrati:
        addi sp, sp, -8
        sw   ra, 4(sp)      # la jal sotto sovrascrive ra
        sw   s0, 0(sp)      # s0 serve dopo la chiamata
        mv   s0, a1         # tiene b al sicuro
        jal  ra, quad       # a0 = a^2
        mv   t0, a0
        mv   a0, s0
        mv   s0, t0         # s0 = a^2
        jal  ra, quad       # a0 = b^2
        add  a0, a0, s0
        lw   s0, 0(sp)
        lw   ra, 4(sp)
        addi sp, sp, 8
        ret
```

`b` non può restare in `a1`, perché per la convenzione `quad` potrebbe cambiarlo; e $a^2$ non può restare in `t0` durante la seconda chiamata, per lo stesso motivo. Per questo entrambi passano da `s0`, salvato sullo stack. Con $a = 3$ e $b = 4$ restituisce 25.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; programmi eseguiti con il simulatore di `strumenti/verifica_ampliamento.py` (ADC-02)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Tradurre un ciclo con una condizione.** Tradurre `int s = 0; for (int i = 0; i < n; i++) if (v[i] % 2 == 0) s += v[i];` (somma dei pari), con `v` in `a0`, `n` in `a1`, risultato in `a0`.

*Passo 1: i registri.* `i` in `t0`, `s` in `t1`, temporanei `t2`, `t3`.

*Passo 2: il test di parità senza divisione.* Un numero è pari se il bit meno significativo è 0: `andi t4, t3, 1`.

*Passo 3: la condizione negata.* Il C dice "se è pari somma": si salta oltre la somma se è dispari, `bne t4, zero, avanti`.

*Passo 4: il codice.*

```text
        li   t0, 0
        li   t1, 0
ciclo:  bge  t0, a1, fine
        slli t2, t0, 2
        add  t2, a0, t2
        lw   t3, 0(t2)
        andi t4, t3, 1
        bne  t4, zero, avanti
        add  t1, t1, t3
avanti: addi t0, t0, 1
        j    ciclo
fine:   mv   a0, t1
        ret
```

*Passo 5: il controllo.* Con $v = (1, 2, 3, 4, -6)$ la somma dei pari è $2 + 4 - 6 = 0$. Il test con `andi` funziona anche per i negativi in complemento a 2 ($-6$ = `…11111010`, bit 0 a 0).

**Guidato 2. Disegnare lo stack.** Durante `fact(3)` dell'esempio del paragrafo 2.6, con `sp` = `0x1000` all'inizio, che cosa c'è nello stack quando si raggiunge il caso base?

*Passo 1: la prima chiamata.* `sp` scende a `0x0FF8`; in `0x0FFC` c'è `ra` del chiamante esterno, in `0x0FF8` c'è $n = 3$.

*Passo 2: la seconda.* `sp` = `0x0FF0`; in `0x0FF4` l'indirizzo di ritorno dentro `fact` (l'istruzione dopo la `jal`), in `0x0FF0` $n = 2$.

*Passo 3: la terza, caso base.* `sp` = `0x0FE8`; in `0x0FEC` lo stesso indirizzo di ritorno, in `0x0FE8` $n = 1$. Con $n = 1 < 2$ si va al caso base.

*Passo 4: la risalita.* Ogni ritorno rilascia 8 byte: `sp` torna a `0x0FF0`, `0x0FF8`, `0x1000`, mentre `a0` vale 1, 2, 6.

**Guidato 3. Reverse coding con un puntatore.** Che cosa fa questa funzione, con `a0` e `a1` indirizzi di due stringhe?

```text
f:      lbu  t0, 0(a1)
        sb   t0, 0(a0)
        beq  t0, zero, fine
        addi a0, a0, 1
        addi a1, a1, 1
        j    f
fine:   ret
```

*Passo 1: che cosa si legge e si scrive.* Si legge un byte da `a1` e lo si scrive in `a0`.

*Passo 2: il ciclo.* Si avanza di un byte su entrambe le stringhe finché il byte copiato non è lo 0.

*Passo 3: il C.* `void copia(char *dst, const char *src) { while ((*dst = *src) != 0) { dst++; src++; } }`: è `strcpy`. Lo 0 finale viene copiato prima del test, così la stringa di destinazione è terminata correttamente.

## Riepilogo

Il compilatore assegna le variabili ai registri e traduce condizioni e cicli in salti condizionati con la condizione negata. L'indirizzo di `v[i]` è $\text{base} + 4i$ per gli interi, e una matrice è memorizzata per righe, con `M[i][j]` a $\text{base} + (iC + j) \cdot 4$; scorrere con un puntatore invece che con un indice risparmia istruzioni. La memoria di un programma è divisa in testo, dati statici, heap e stack; le direttive dell'assemblatore scelgono la zona. Nelle procedure gli argomenti passano in `a0`…`a7`, il risultato in `a0`, la chiamata è `jal ra` e il ritorno `jalr zero, 0(ra)`; i registri `s` e `ra` sono preservati da chi li usa, i `t` e gli `a` da chi ne ha bisogno dopo la chiamata. Una procedura non foglia salva `ra` e i registri salvati nel suo stack frame; la ricorsione funziona perché ogni chiamata ha il suo frame.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (ADC-02)

### Schemi di traduzione

| C | RISC-V |
|---|---|
| `if (a == b) X; else Y;` | `bne a, b, Else` · X · `j Fine` · `Else:` Y · `Fine:` |
| `while (cond) X;` | `Ciclo:` salto fuori se non cond · X · `j Ciclo` |
| `for (i = 0; i < n; i++) X;` | `li i, 0` · `Ciclo: bge i, n, Fine` · X · `addi i, i, 1` · `j Ciclo` |
| `v[i]` (int) | `slli t, i, 2` · `add t, base, t` · `lw x, 0(t)` |
| `M[i][j]` (int, $C$ colonne) | indirizzo $\text{base} + (iC + j) \cdot 4$ |
| `c = s[i]` (char) | `add t, base, i` · `lbu c, 0(t)` |

### Convenzione di chiamata

| Chi salva | Registri |
|---|---|
| la procedura chiamata (callee-saved) | `s0`–`s11`, `sp`, `ra` (se ne chiama altre) |
| il chiamante (caller-saved) | `t0`–`t6`, `a0`–`a7` |

Prologo: `addi sp, sp, -k` · `sw ra, …(sp)` · `sw s…, …(sp)`. Epilogo: `lw` in ordine inverso · `addi sp, sp, k` · `ret`.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Procedura foglia | non chiama altre procedure, spesso non usa lo stack |
| Stack frame | zona di stack di una chiamata: registri salvati e variabili locali |
| Indirizzo di ritorno | indirizzo dell'istruzione dopo la chiamata, salvato in `ra` |
| Caller-saved / callee-saved | salvati da chi chiama / da chi è chiamato |
| Row-major | memorizzazione delle matrici riga per riga |
| Aritmetica dei puntatori | avanzare un indirizzo invece di ricalcolarlo da un indice |
| Direttiva | comando per l'assemblatore (`.data`, `.word`, `.asciz`) |

### Domande che tornano spesso

- Quali sono i passi di una chiamata di procedura e come li realizza RISC-V?
- Perché alcuni registri sono preservati e altri no? Che cosa deve salvare una procedura non foglia?
- Disegnare lo stack durante una chiamata ricorsiva.
- Come si calcola l'indirizzo di un elemento di un array e di una matrice?
- Descrivere le zone della memoria di un programma.
- Tradurre in C un frammento assembly assegnato.
