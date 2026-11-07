# Modulo 1 — Lezione 9: C essenziale e toolchain

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 9 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 14).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. descrivere le quattro fasi con cui `gcc` trasforma un sorgente C in un eseguibile (preprocessore, compilatore, assemblatore, linker), fermarti a ciascuna e leggerne il prodotto;
2. riconoscere che cosa contiene un file oggetto e un eseguibile ELF (sezioni, simboli, rilocazioni, dipendenze dinamiche) con `file`, `nm`, `readelf`, `objdump`, `ldd`;
3. usare con precisione i tipi interi del C, le loro dimensioni sul tuo sistema (`sizeof`, il modello LP64, `<stdint.h>`) e le conversioni implicite, distinguendo l'overflow definito degli `unsigned` dal **comportamento indefinito** dei `signed`;
4. ragionare sui **puntatori**: indirizzi, dereferenziazione, aritmetica, relazione con gli array, puntatori a puntatori (`argv`), `void *` e conversioni, e disegnare la memoria di un piccolo programma;
5. spiegare come è fatta una **stringa C**, perché il terminatore `\0` è la fonte di metà delle vulnerabilità che studieremo nel Modulo 4, e quali funzioni di `<string.h>` sono pericolose e perché;
6. descrivere lo **spazio di indirizzi** di un processo (codice, dati, BSS, heap, librerie, stack) e dire in quale zona vive ogni variabile di un programma;
7. usare `malloc`, `calloc`, `realloc` e `free` correttamente, e riconoscere *memory leak*, *use-after-free*, *double free* e *off-by-one*, anche con l'aiuto di AddressSanitizer e Valgrind;
8. chiamare dal C le chiamate di sistema `open`, `read`, `write`, `close`, gestire `errno`, e spiegare la differenza tra queste e le funzioni bufferizzate di `<stdio.h>`;
9. usare `gdb` per eseguire un programma passo per passo, fermarlo su un punto, leggere variabili, memoria e registri, e capire che cosa fa un programma di cui **non** hai il sorgente.

**Prerequisiti:** Lezioni 1–8. In particolare: processi, descrittori di file e chiamate di sistema (L4 §1–2, L5 §4), il buffering di `stdio` (L4 §3, L8 Esempio 4), la rappresentazione degli interi, il complemento a due, l'endianness, ASCII (L7 §2–5, §7), lo spazio di indirizzi visto da `/proc/<PID>/maps` (L5 §7.4). Non serve aver già programmato in C: la lezione parte dall'inizio, ma va veloce sulle parti che il C ha in comune con Python (cicli, condizioni, funzioni) e si ferma a lungo su quelle che Python ti nascondeva.

**Tempo:** circa 5 ore di lettura e prove, 4–5 ore di esercizi. Come per la Lezione 8, questa lezione si impara **scrivendo e compilando**: tieni aperto un terminale e prova ogni esempio, e quando un risultato ti sorprende, chiediti quale sezione lo spiega prima di andare avanti.

**Strumenti.** Ti servono `gcc`, `make`, `gdb`, `binutils` (`objdump`, `readelf`, `nm`), e conviene avere `valgrind`. Su Debian, Ubuntu e Kali: `sudo apt install build-essential gdb valgrind`. Gli esempi di questa lezione sono stati provati con gcc 13.3, GNU gdb 15 e glibc 2.39 su Linux x86-64: con versioni diverse cambiano alcuni dettagli (indirizzi, numeri di riga dei messaggi, nomi delle funzioni interne), mai le idee.

**Ripasso dalle lezioni precedenti.**
- Nella Lezione 5 abbiamo visto un processo dall'esterno: il suo PID, i suoi descrittori in `/proc/<PID>/fd`, la sua memoria in `/proc/<PID>/maps`, le chiamate di sistema con `strace`. Oggi lo guardiamo dall'**interno**: il programma che, compilato, diventa quel processo.
- Nella Lezione 7 abbiamo imparato che un byte non ha un solo significato: dipende da chi lo legge e come. Il C è il linguaggio in cui questa ambiguità è **visibile**: lo stesso pezzo di memoria può essere un `int`, quattro `char` o un indirizzo, a seconda del tipo con cui lo guardi.
- Nella Lezione 8 abbiamo dialogato con programmi C "dall'esterno", e ci siamo scontrati con `setvbuf`, il buffering e un indirizzo che trapelava in 6 byte. Oggi apriamo quei programmi e capiamo il perché di ognuna di queste cose.

**Convenzione tipografica.** `$` è il prompt della shell, `(gdb)` quello del debugger. I blocchi senza prompt che cominciano con un commento `// nome.c` sono **file** da salvare con quel nome. Le opzioni di compilazione degli esempi sono sempre scritte per intero: se non specificato, si compila con `gcc -Wall -Wextra -g -o nome nome.c`.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. Dal sorgente all'eseguibile | 1–2 | Che cosa fa davvero `gcc`, e che cosa c'è in un eseguibile? |
| II. Il linguaggio | 3–5 | Come si scrive un programma C corretto, e come sono fatti i suoi tipi? |
| III. La memoria | 6–9 | Che cosa sono puntatori, array, stringhe, strutture, heap e stack? |
| IV. Il C e il sistema | 10–11 | Come parla un programma C con il kernel, e come lo si osserva con `gdb`? |
| V. La pratica | 12–17 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — Dal sorgente all'eseguibile

## 1. Perché il C

### 1.1 Il linguaggio dei sistemi

Il C nasce tra il 1969 e il 1973 ai Bell Labs, dove Dennis Ritchie lo progetta come evoluzione del linguaggio B di Ken Thompson, con uno scopo preciso: riscrivere **Unix** (L1 §2) in un linguaggio di alto livello invece che in assembly. Nel 1973 il kernel di Unix è in C, ed è questa scelta che rende Unix *portabile*: per portarlo su una nuova macchina basta un compilatore C per quella macchina, non una riscrittura. Nel 1978 Brian Kernighan e Dennis Ritchie pubblicano *The C Programming Language*, il "K&R", che per dieci anni è stato la definizione di fatto del linguaggio; nel 1989 arriva lo standard ANSI (poi ISO C90), seguito da C99, C11, C17 e C23.

Cinquant'anni dopo, il C è ancora il linguaggio di quasi tutto ciò che sta **sotto** i programmi che usi: il kernel Linux, la libreria C (`glibc`, `musl`), gli interpreti di Python, Perl e PHP, i server web (nginx, Apache), le librerie crittografiche (OpenSSL), i firmware di router e dispositivi, i sistemi embedded. Anche il C++, il Rust e il Go, che lo sostituiscono in molti progetti nuovi, parlano con il sistema operativo attraverso interfacce definite in C.

### 1.2 Perché in sicurezza

Per chi fa sicurezza, il C è importante per un motivo che ha poco a che fare con la sua eleganza: è un linguaggio che **si fida del programmatore**. Non controlla che un indice stia dentro un array, non controlla che un puntatore punti a memoria valida, non inizializza le variabili, non libera la memoria da solo. Quando il programmatore sbaglia, il programma non solleva un'eccezione come in Python (L8 §2.6): continua, con la memoria in uno stato che nessuno aveva previsto. Lo standard chiama queste situazioni **comportamento indefinito** (*undefined behavior*, §4.6), e significa letteralmente che il linguaggio non garantisce più niente.

Un attaccante vive in quello spazio. Le categorie più importanti di vulnerabilità del software, quelle che studierai nel Modulo 4, sono quasi tutte errori di memoria del C: scrivere oltre la fine di un buffer (*buffer overflow*, CWE-120, CWE-121, CWE-122), leggere oltre la fine (CWE-125), usare memoria già liberata (*use-after-free*, CWE-416), liberarla due volte (CWE-415), interpretare dati dell'utente come una stringa di formato (CWE-134), sbagliare di uno un confine (CWE-193). Nell'elenco **CWE Top 25** dei difetti più pericolosi pubblicato ogni anno da MITRE, la scrittura fuori dai limiti (CWE-787) è stabilmente nelle prime posizioni. Microsoft e Google hanno stimato, ciascuna per i propri prodotti, che circa il **70%** delle vulnerabilità gravi corrette sono errori di sicurezza della memoria.

Le sfide *pwn* e *reverse* delle CTF (Moduli 3 e 4) sono quasi sempre programmi C compilati. Per attaccarli devi saper leggere il C, sapere come il compilatore lo traduce, e sapere dove finiscono in memoria le sue variabili. Questa lezione costruisce esattamente queste tre capacità, senza ancora attaccare niente: prima si capisce come funziona, poi come si rompe.

### 1.3 Il C e Python, a confronto

Avendo appena studiato Python (L8), conviene fissare le differenze che contano.

| | Python | C |
|---|---|---|
| Esecuzione | interpretato (il sorgente diventa *bytecode* eseguito da una macchina virtuale) | **compilato** in codice macchina, eseguito direttamente dal processore |
| Tipi | dinamici: il tipo è dell'oggetto, un nome può riferirsi a oggetti di tipo diverso | **statici**: il tipo è della variabile, deciso alla compilazione, e determina quanti byte occupa e come si interpretano |
| Interi | precisione arbitraria (L8 §2.2) | dimensione fissa (8, 16, 32, 64 bit): **overflow** (§4.5) |
| Memoria | gestita: oggetti creati e distrutti dall'interprete (*garbage collection*) | **manuale**: variabili automatiche sullo stack, memoria dinamica con `malloc`/`free` |
| Errori | eccezioni, controlli su indici e tipi | nessun controllo: codice di ritorno ed `errno`, oppure comportamento indefinito |
| Stringhe | oggetti `str` con la loro lunghezza | array di `char` terminati da `\0` (§8) |
| Velocità | lento | veloce, vicino all'hardware |

La riga più importante per noi è la quinta. In Python `l[10]` su una lista di 3 elementi è un `IndexError`; in C `a[10]` su un array di 3 elementi legge (o scrive) **quello che c'è** 7 posizioni dopo la fine dell'array: un'altra variabile, un indirizzo di ritorno, niente di sensato, oppure memoria non mappata, e allora il processo riceve `SIGSEGV` (L5 §8).

## 2. La toolchain: da `ciao.c` a `ciao`

### 2.1 Quattro programmi dietro un comando

Partiamo dal programma più piccolo che faccia qualcosa:

```c
// ciao.c — il primo programma
#include <stdio.h>

#define SALUTO "Ciao"

int main(void) {
    printf("%s, mondo!\n", SALUTO);
    return 0;
}
```

```
$ gcc -o ciao ciao.c
$ ./ciao
Ciao, mondo!
```

Il comando `gcc` sembra fare una cosa sola, ma è un **driver**: un programma che ne lancia altri, nell'ordine, passando a ciascuno il prodotto del precedente. Con `-v` (*verbose*) lo si vede fare:

```
$ gcc -v -o ciao ciao.c 2>&1 | grep -E 'cc1 |as |collect2' | cut -c1-80
 /usr/libexec/gcc/x86_64-linux-gnu/13/cc1 -quiet -v -imultiarch x86_64-linux-gnu
 as -v --64 -o /tmp/cc44NXIK.o /tmp/ccWoIdkH.s
 /usr/libexec/gcc/x86_64-linux-gnu/13/collect2 -plugin /usr/libexec/gcc/x86_64-l
```

Le fasi sono quattro, e conviene impararne i nomi, le opzioni con cui ci si ferma a ciascuna e i prodotti, perché nel *reverse engineering* (Modulo 3) lavorerai proprio sui prodotti delle ultime due.

| Fase | Programma | Ingresso → uscita | Fermarsi qui |
|---|---|---|---|
| 1. Preprocessore | `cc1` (in modalità `-E`) | `ciao.c` → `ciao.i`: C senza direttive `#` | `gcc -E` |
| 2. Compilatore | `cc1` | `ciao.i` → `ciao.s`: **assembly** in testo | `gcc -S` |
| 3. Assemblatore | `as` (GNU binutils) | `ciao.s` → `ciao.o`: codice macchina, **file oggetto** ELF *rilocabile* | `gcc -c` |
| 4. Linker | `collect2` → `ld` | `ciao.o` + librerie → `ciao`: **eseguibile** ELF | (il default) |

Con `-save-temps` `gcc` conserva tutti i file intermedi nella directory corrente, con i nomi `ciao.i`, `ciao.s`, `ciao.o`: è il modo più rapido di guardarli tutti insieme. (Il preprocessore, in GCC, è integrato in `cc1`; storicamente era un programma separato, `cpp`, che esiste ancora come comando.)

### 2.2 Il preprocessore

Il preprocessore lavora sul **testo** del sorgente, prima che il compilatore veda una sola riga di C, ed esegue le **direttive**: le righe che cominciano con `#`. Non sa niente del linguaggio: copia, sostituisce, elimina testo.

```
$ gcc -E ciao.c -o ciao.i
$ wc -l ciao.i
822 ciao.i
$ tail -5 ciao.i
# 6 "ciao.c"
int main(void) {
    printf("%s, mondo!\n", "Ciao");
    return 0;
}
```

Due cose sono successe. `#include <stdio.h>` è stato sostituito dal **contenuto** del file `/usr/include/stdio.h` e di tutti i file che a sua volta include: otto righe sono diventate 822, quasi tutte dichiarazioni come `extern int printf (const char *__restrict __format, ...);`. E `SALUTO` è stato sostituito, come testo, da `"Ciao"`. Le righe `# 6 "ciao.c"` sono **marcatori di riga**: dicono al compilatore da quale file e riga viene il testo che segue, così che i messaggi d'errore indichino `ciao.c:7` e non `ciao.i:819`.

Le direttive che userai:

- **`#include <file.h>`** cerca il file nelle directory di sistema (`/usr/include` e quelle che stampa `gcc -v` alla voce `#include <...> search starts here`); **`#include "file.h"`** cerca prima nella directory del sorgente. Si includono gli *header* (file `.h`), che contengono **dichiarazioni**: il prototipo di una funzione, la definizione di un tipo, una costante. Le **definizioni** (il corpo delle funzioni) stanno nei file `.c` (§2.6).
- **`#define NOME testo`** definisce una **macro**: da quel punto, ogni occorrenza di `NOME` come parola intera viene sostituita da `testo`. Con parametri, `#define MAX(a, b) ((a) > (b) ? (a) : (b))`. Si può definire anche dalla riga di comando: `gcc -DDEBUG=1` equivale a `#define DEBUG 1` in cima al file.
- **`#if`, `#ifdef`, `#ifndef`, `#else`, `#endif`** includono o escludono pezzi di testo: `#ifdef DEBUG ... #endif` compila il codice di debug solo con `-DDEBUG`. È così che lo stesso sorgente si adatta a Linux, Windows e macOS.
- **`#ifndef X_H` / `#define X_H` / ... / `#endif`** in un header è la **guardia di inclusione**: evita che il contenuto venga incluso due volte nello stesso file, cosa che causerebbe definizioni duplicate.

Poiché il preprocessore sostituisce testo e non valori, le macro con parametri hanno trappole famose. Prova:

```c
// macro.c — le macro sostituiscono testo, non valori
#include <stdio.h>
#define QUADRATO(x) x * x
#define QUADRATO2(x) ((x) * (x))
int main(void) {
    int i = 3;
    printf("%d %d\n", QUADRATO(1 + 2), QUADRATO2(1 + 2));
    printf("%d\n", 100 / QUADRATO2(5));
    printf("%d\n", QUADRATO2(i++));
    printf("i=%d\n", i);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o macro macro.c
macro.c: In function 'main':
macro.c:8:31: warning: operation on 'i' may be undefined [-Wsequence-point]
$ ./macro
5 9
4
12
i=5
```

`QUADRATO(1 + 2)` diventa `1 + 2 * 1 + 2`, cioè 5: per questo ogni parametro va tra parentesi. `100 / QUADRATO2(5)` dà 4 solo grazie alle parentesi **esterne**: con `(x) * (x)` sarebbe `100 / (5) * (5)`, cioè 100. E `QUADRATO2(i++)` diventa `((i++) * (i++))`: `i` viene incrementata **due volte**, e l'ordine delle due modifiche non è definito dal linguaggio, tanto che il compilatore avvisa (§4.6). Una funzione non ha nessuno di questi problemi: il C moderno usa le macro per le costanti e la compilazione condizionale, e funzioni (eventualmente `static inline`) per i calcoli.

### 2.3 Il compilatore

Il compilatore vero e proprio traduce il C preprocessato in **assembly**, il linguaggio testuale che corrisponde una a una alle istruzioni del processore:

```
$ gcc -S -fno-asynchronous-unwind-tables ciao.c -o ciao.s
$ cat ciao.s
	.file	"ciao.c"
	.text
	.section	.rodata
.LC0:
	.string	"Ciao"
.LC1:
	.string	"%s, mondo!\n"
	.text
	.globl	main
	.type	main, @function
main:
	endbr64
	pushq	%rbp
	movq	%rsp, %rbp
	leaq	.LC0(%rip), %rax
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	popq	%rbp
	ret
	...
```

(`-fno-asynchronous-unwind-tables` toglie le direttive `.cfi_...`, che servono ai debugger e alle eccezioni e qui sarebbero rumore.) Imparerai a leggere l'assembly x86-64 nel Modulo 3; per ora basta riconoscere i pezzi. Le due stringhe stanno in una **sezione** chiamata `.rodata` (*read-only data*), con le etichette `.LC0` e `.LC1`. Il codice sta in `.text`. `main` è dichiarata `.globl`, cioè visibile agli altri file. Le istruzioni mettono l'indirizzo di `"Ciao"` nel registro `rsi` e quello del formato nel registro `rdi`: sono il secondo e il primo argomento della chiamata, secondo la **convenzione di chiamata** System V di Linux x86-64 (argomenti interi e puntatori, nell'ordine, in `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`; valore di ritorno in `rax`). `movl $0, %eax` prima di `call printf` dice a `printf`, che ha un numero variabile di argomenti, che non ci sono argomenti in virgola mobile nei registri vettoriali; l'altro `movl $0, %eax` prima di `ret` è il `return 0`.

Le opzioni del compilatore che userai sempre:

- **`-Wall -Wextra`**: attivano la maggior parte degli avvisi utili. Un avviso del compilatore C è quasi sempre un bug; nei tuoi programmi tienili tutti a zero, e con `-Werror` trasformali in errori. Nelle sfide, gli avvisi su un sorgente fornito sono spesso un **indizio**: `warning: format not a string literal and no format arguments` indica una vulnerabilità di formato (CWE-134, Modulo 4).
- **`-g`**: aggiunge le informazioni di debug (formato DWARF): nomi delle variabili, tipi, corrispondenza tra istruzioni e righe del sorgente. Servono a `gdb` (§12). Non cambiano il codice generato.
- **`-O0`, `-O1`, `-O2`, `-O3`, `-Os`**: il livello di **ottimizzazione**. A `-O0` (il default) il compilatore traduce in modo letterale, ogni variabile ha il suo posto in memoria, ed è il livello più facile da leggere e da seguire con il debugger; a `-O2` il codice è più veloce ma riordinato, le variabili possono vivere solo nei registri o sparire. I binari delle sfide sono compilati a livelli diversi: riconoscere il codice ottimizzato è una competenza del Modulo 3.
- **`-std=c17`** (o `c99`, `c11`, `c23`, oppure `gnu17` con le estensioni GNU, che è il default di GCC 13): lo standard del linguaggio.

Il compilatore può cambiare le chiamate di libreria che conosce. Se scrivi `printf("Ciao, mondo!\n")`, senza argomenti di formato e con il `\n` finale, GCC lo sostituisce con `puts("Ciao, mondo!")`, che fa la stessa cosa più velocemente, anche a `-O0`: guardando i simboli del file oggetto troverai `puts` e non `printf`. Sapere che succede evita di cercare una `printf` che nel binario non c'è.

### 2.4 L'assemblatore e il file oggetto

L'assemblatore traduce l'assembly in **codice macchina** e produce un **file oggetto**:

```
$ gcc -c ciao.c -o ciao.o
$ file ciao.o
ciao.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
$ nm ciao.o
0000000000000000 T main
                 U printf
```

Il formato è **ELF** (*Executable and Linkable Format*), lo stesso degli eseguibili e delle librerie su Linux (i primi quattro byte, `7f 45 4c 46`, sono il suo numero magico: L7 §12.1). `LSB` vuol dire little-endian. *Relocatable* (rilocabile) significa che il file non è ancora eseguibile: contiene il codice di `main`, ma non sa ancora **dove** si troveranno in memoria le stringhe e la funzione `printf`.

`nm` elenca i **simboli**, cioè i nomi che il file definisce o usa. La lettera dice il tipo: `T` è un simbolo definito nella sezione di codice (*text*), `U` un simbolo **non definito** (*undefined*), usato qui ma che dovrà fornire qualcun altro. Altre lettere che incontrerai: `D` e `d` dati inizializzati (`.data`), `B` e `b` dati non inizializzati (`.bss`), `R` e `r` dati in sola lettura (`.rodata`). La maiuscola indica un simbolo **globale** (visibile agli altri file), la minuscola uno **locale** (§2.6).

I "buchi" che il linker dovrà riempire si vedono nel codice disassemblato e nella tabella delle **rilocazioni**:

```
$ objdump -d ciao.o
0000000000000000 <main>:
   0:	f3 0f 1e fa          	endbr64
   4:	55                   	push   %rbp
   5:	48 89 e5             	mov    %rsp,%rbp
   8:	48 8d 05 00 00 00 00 	lea    0x0(%rip),%rax        # f <main+0xf>
   f:	48 89 c6             	mov    %rax,%rsi
  12:	48 8d 05 00 00 00 00 	lea    0x0(%rip),%rax        # 19 <main+0x19>
  19:	48 89 c7             	mov    %rax,%rdi
  1c:	b8 00 00 00 00       	mov    $0x0,%eax
  21:	e8 00 00 00 00       	call   26 <main+0x26>
  26:	b8 00 00 00 00       	mov    $0x0,%eax
  2b:	5d                   	pop    %rbp
  2c:	c3                   	ret
$ readelf -r ciao.o
Relocation section '.rela.text' at offset 0x1b0 contains 3 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
00000000000b  000300000002 R_X86_64_PC32     0000000000000000 .rodata - 4
000000000015  000300000002 R_X86_64_PC32     0000000000000000 .rodata + 1
000000000022  000500000004 R_X86_64_PLT32    0000000000000000 printf - 4
```

A sinistra ci sono gli offset in `main`, al centro i byte delle istruzioni, a destra la loro forma leggibile. I quattro byte `00 00 00 00` agli offset 0xb, 0x15 e 0x22 sono **segnaposto**: la tabella delle rilocazioni dice al linker di scriverci, rispettivamente, la distanza dalla stringa `"Ciao"` (all'inizio di `.rodata`), dalla stringa di formato (5 byte più avanti: `"Ciao"` più il suo `\0`) e da `printf`. Gli indirizzi sono **relativi** alla posizione dell'istruzione (`%rip` è il registro che contiene l'indirizzo della prossima istruzione, da cui il `- 4`): è ciò che permette al codice di funzionare a qualunque indirizzo venga caricato (§2.5).

### 2.5 Il linker

Il linker (`ld`, lanciato da GCC attraverso `collect2`) unisce uno o più file oggetto e le librerie in un eseguibile. Fa due lavori:

1. **Risoluzione dei simboli.** Per ogni simbolo `U` di un file oggetto cerca **una** definizione, in un altro file oggetto o in una libreria. Se non ne trova nessuna, l'errore è `undefined reference`; se ne trova due globali con lo stesso nome, `multiple definition`.
2. **Rilocazione.** Decide dove andrà ogni sezione nell'eseguibile, e riempie i segnaposto con gli indirizzi giusti.

Gli errori del linker si riconoscono perché arrivano **dopo** la compilazione, con il nome di un simbolo e senza il numero di riga di un errore di sintassi:

```
$ gcc -o m m.c                       # m.c usa sqrt() di <math.h>
/usr/bin/ld: /tmp/ccPzYBrO.o: in function `main':
m.c:(.text+0x2b): undefined reference to `sqrt'
collect2: error: ld returned 1 exit status
$ gcc -o m m.c -lm                   # -lm: collega la libreria matematica libm
```

L'opzione **`-lNOME`** chiede al linker di cercare la libreria `libNOME.so` (dinamica) o `libNOME.a` (statica) nelle directory delle librerie; `-L DIR` aggiunge una directory. La libreria C, `libc`, è collegata automaticamente; quella matematica, per ragioni storiche, no. (Se `sqrt` è chiamata con una costante, GCC calcola il risultato alla compilazione e la chiamata sparisce: per questo l'errore si vede solo quando l'argomento dipende dall'esecuzione.) L'**ordine** conta: i file oggetto e le librerie si elencano dopo i file che ne usano i simboli, perché `ld` legge gli argomenti da sinistra a destra.

**Collegamento statico e dinamico.** Il nostro `ciao` è collegato **dinamicamente**: il codice di `printf` non è dentro l'eseguibile, ma nella libreria condivisa `libc.so.6`, che viene caricata in memoria quando il programma parte.

```
$ file ciao
ciao: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked,
interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4246...a26, for GNU/Linux 3.2.0, not stripped
$ ldd ciao
	linux-vdso.so.1 (0x00007fbe6161a000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fbe61200000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fbe6161c000)
$ gcc -static -o ciao_static ciao.c
$ ls -l ciao ciao_static | awk '{print $5, $9}'
15960 ciao
785328 ciao_static
```

Un eseguibile dinamico contiene il nome di un **interprete**, il *dynamic loader* `ld-linux-x86-64.so.2`: quando chiami `execve` (L5 §4.2), il kernel carica in memoria il programma **e** il loader, e dà il controllo al loader, che carica le librerie elencate, risolve i simboli come `printf` e solo allora salta all'inizio del programma. `ldd` mostra le librerie che il loader caricherebbe (con gli indirizzi, che cambiano a ogni esecuzione: è l'ASLR, Modulo 4), e `linux-vdso.so.1` è una piccola libreria che il kernel stesso mappa in ogni processo per rendere più veloci alcune chiamate come `gettimeofday`. L'eseguibile statico, al contrario, contiene una copia di tutto il codice di libreria che usa: è 50 volte più grande, ma funziona anche su un sistema con una `libc` diversa o assente. (`ldd` su un eseguibile non fidato è pericoloso: con alcune versioni può eseguirne il codice. Per un binario sconosciuto si usa `readelf -d`, che legge e basta.)

Il collegamento dinamico è la ragione di due strutture che incontrerai in ogni sfida *pwn*: la **PLT** (*Procedure Linkage Table*, la sezione `.plt`) e la **GOT** (*Global Offset Table*, `.got`). La chiamata `call printf@PLT` dell'assembly salta a un piccolo pezzo di codice nella PLT, che a sua volta salta all'indirizzo scritto in una casella della GOT; il loader scrive in quella casella l'indirizzo vero di `printf` dentro `libc`. Una tabella di indirizzi di funzioni, in memoria scrivibile, usata da ogni chiamata di libreria: si capisce perché, nel Modulo 4, sarà uno dei primi bersagli.

**Da `_start` a `main`.** `main` non è la prima funzione eseguita. Il punto di ingresso dell'eseguibile (*entry point*, che `readelf -h` mostra) è `_start`, un pezzo di codice fornito dalla libreria C (il file `crt1.o`, che il linker aggiunge da solo). `_start` prepara gli argomenti e chiama `__libc_start_main`, che inizializza la libreria (lo `stdio`, i costruttori, le variabili d'ambiente) e poi chiama `main(argc, argv, envp)`. Quando `main` ritorna, il suo valore di ritorno viene passato a `exit`, che svuota i buffer di `stdio` e chiama la chiamata di sistema `exit_group` (L5 §4). È per questo che `return 0` da `main` e `exit(0)` si equivalgono, e che il buffering di `stdio` si svuota all'uscita ma non se il processo viene ucciso da un segnale.

```
$ nm ciao | grep -E ' (T|U) '
                 U __libc_start_main@GLIBC_2.34
0000000000001178 T _fini
0000000000001000 T _init
0000000000001060 T _start
0000000000001149 T main
                 U printf@GLIBC_2.2.5
$ readelf -h ciao | grep -E 'Type|Entry'
  Type:                              DYN (Position-Independent Executable file)
  Entry point address:               0x1060
```

Il punto di ingresso, 0x1060, è proprio l'indirizzo di `_start`. I simboli `U` portano ora una **versione** (`@GLIBC_2.34`): la `libc` offre versioni diverse della stessa funzione, e il programma chiede quella con cui è stato compilato. Gli indirizzi come 0x1149 sono **offset** rispetto alla base a cui il programma verrà caricato: `DYN` e `pie` indicano un eseguibile **indipendente dalla posizione** (*PIE*), che il kernel carica a un indirizzo casuale a ogni esecuzione. È quello che hai visto nella Lezione 8 (Esercizio 7): l'indirizzo di `main` cambiava ogni volta, ma finiva sempre con le stesse tre cifre esadecimali.

### 2.6 L'eseguibile ELF: sezioni e segmenti

Un file ELF si può guardare in due modi. Per il linker è fatto di **sezioni** (`readelf -S`): `.text` (codice), `.rodata` (costanti), `.data` (variabili globali inizializzate), `.bss` (variabili globali non inizializzate, che nel file non occupano spazio: si sa solo quanto sono grandi), `.plt` e `.got`, `.dynamic` (le informazioni per il loader), `.symtab` (la tabella dei simboli), e altre. Per il kernel, che lo carica, è fatto di **segmenti** (`readelf -l`), ciascuno con dei permessi: un segmento leggibile ed eseguibile per il codice, uno di sola lettura per le costanti, uno leggibile e scrivibile per i dati. Sono esattamente le righe con permessi `r-xp`, `r--p` e `rw-p` che hai visto in `/proc/<PID>/maps` (L5 §7.4), e su cui torneremo nel §9.

```
$ readelf -S -W ciao | grep -E '\.(text|rodata|data|bss|plt|got|interp) '
  [ 1] .interp           PROGBITS        0000000000000318 000318 00001c 00   A  0   0  1
  [13] .plt              PROGBITS        0000000000001020 001020 000020 10  AX  0   0 16
  [16] .text             PROGBITS        0000000000001060 001060 000116 00  AX  0   0 16
  [18] .rodata           PROGBITS        0000000000002000 002000 000015 00   A  0   0  4
  [24] .got              PROGBITS        0000000000003fb8 002fb8 000048 08  WA  0   0  8
  [25] .data             PROGBITS        0000000000004000 003000 000010 00  WA  0   0  8
  [26] .bss              NOBITS          0000000000004010 003010 000008 00  WA  0   0  1
```

Le colonne sono: nome, tipo, indirizzo (rispetto alla base di caricamento), offset nel file, dimensione, e i **flag**: `A` (*alloc*, va in memoria), `X` (eseguibile), `W` (scrivibile). Il codice è `AX` ma non `W`, la GOT e i dati sono `WA` ma non `X`: la regola "una zona di memoria è scrivibile **oppure** eseguibile, mai entrambe" (detta W^X, o NX) è una delle protezioni del Modulo 4. `.rodata` è lunga 0x15 = 21 byte: 4 byte di intestazione (una costante della `libc`) più le nostre due stringhe con i loro terminatori, 5 + 12.

**I simboli e `strip`.** Le informazioni sui nomi delle funzioni non servono per eseguire il programma: `strip` le toglie.

```
$ strip -o ciao_s ciao && ls -l ciao_s | awk '{print $5}'; nm ciao_s
14472
nm: ciao_s: no symbols
```

Molti binari delle sfide *reverse* sono *stripped*: `nm` non mostra niente e `gdb` non sa dov'è `main`. I nomi delle funzioni di libreria però restano (servono al loader, nella sezione `.dynsym`, che `nm -D` mostra): anche in un binario senza simboli vedrai che usa `strcmp` o `puts`, ed è spesso il primo indizio.

### 2.7 Le protezioni attive per default

Le distribuzioni moderne compilano con alcune protezioni contro gli errori di memoria già attive. Con `gcc -v` si vedono le opzioni che Ubuntu aggiunge da sola:

```
$ gcc -v -o ciao ciao.c 2>&1 | grep ' cc1 ' | tr ' ' '\n' | grep -E '^-f(stack|cf|PIE)|^-W'
-fstack-protector-strong
-Wformat
-Wformat-security
-fstack-clash-protection
-fcf-protection
```

In breve, perché le studierai una per una nel Modulo 4: `-fstack-protector-strong` mette un valore casuale (il *canary*) tra le variabili locali e l'indirizzo di ritorno di ogni funzione con un array, e controlla prima di ritornare che non sia stato sovrascritto; `-fstack-clash-protection` impedisce che uno stack molto grande "salti" oltre la pagina di guardia; `-fcf-protection` aggiunge l'istruzione `endbr64` che hai visto all'inizio di `main` (per la protezione del flusso di controllo di Intel CET); la generazione di eseguibili PIE è attiva per default (`-fPIE` e `-pie`); con `-O1` o superiore viene definito anche `_FORTIFY_SOURCE=3`, che sostituisce funzioni come `strcpy` e `memcpy` con versioni che controllano le dimensioni quando sono note alla compilazione. Nelle sfide e negli esercizi del Modulo 4 queste protezioni verranno tolte di proposito, con opzioni come `-fno-stack-protector`, `-no-pie`, `-z execstack`: sapere che esistono, e che cosa fa ciascuna, ti dirà quale tecnica serve.

### 2.8 Programmi su più file, e `make`

Un programma vero è diviso in **moduli**: ogni file `.c` si compila separatamente in un `.o`, e il linker li unisce. Il "contratto" tra i moduli è l'header:

```c
// conta.h — l'interfaccia del modulo conta.c
#ifndef CONTA_H
#define CONTA_H
#include <stddef.h>
size_t conta_vocali(const char *s);
extern int chiamate;              // definita in conta.c
#endif
```

```c
// conta.c — l'implementazione
#include "conta.h"
int chiamate = 0;                 // visibile agli altri file
static const char VOCALI[] = "aeiouAEIOU";   // static: visibile solo qui
static int e_vocale(char c) {
    for (const char *v = VOCALI; *v; v++)
        if (*v == c) return 1;
    return 0;
}
size_t conta_vocali(const char *s) {
    size_t n = 0;
    chiamate++;
    for (; *s; s++) n += e_vocale(*s);
    return n;
}
```

```c
// principale.c — usa il modulo conta
#include <stdio.h>
#include "conta.h"
int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++)
        printf("%s: %zu vocali\n", argv[i], conta_vocali(argv[i]));
    printf("chiamate: %d\n", chiamate);
    return 0;
}
```

Due parole chiave regolano la visibilità tra file. **`extern`** in una dichiarazione dice "questa variabile esiste, ma è definita altrove": l'header la **dichiara**, `conta.c` la **definisce** (una sola volta). **`static`** davanti a una funzione o a una variabile globale la rende **locale al file**: nessun altro modulo può vederla, e il suo nome non entra in conflitto con nomi uguali altrove. Nei simboli si vede la differenza:

```
$ nm conta.o
0000000000000000 r VOCALI
0000000000000000 B chiamate
0000000000000044 T conta_vocali
0000000000000000 t e_vocale
```

`chiamate` e `conta_vocali` sono maiuscole (globali), `VOCALI` ed `e_vocale` minuscole (locali, per `static`). `chiamate` è in `B` (BSS), perché inizializzata a zero: non serve scrivere lo zero nel file. Se un altro file definisse anche lui `int chiamate = 7;`, il linker si fermerebbe con `multiple definition of 'chiamate'`.

Compilare a mano è noioso e soggetto a errori: se cambi `conta.h`, devi ricompilare **entrambi** i file che lo includono. È il lavoro di **`make`**, che legge un `Makefile` con delle **regole** nella forma "un *bersaglio* dipende da questi *prerequisiti*, e si costruisce con questa *ricetta*", e ricostruisce solo ciò che è più vecchio dei suoi prerequisiti (confrontando le date di modifica, la `mtime` della Lezione 2):

```make
# Makefile — compila vocali da due file sorgente
CC      = gcc
CFLAGS  = -Wall -Wextra -g
OGGETTI = principale.o conta.o

vocali: $(OGGETTI)
	$(CC) $(CFLAGS) -o $@ $^

principale.o: principale.c conta.h
conta.o: conta.c conta.h

.PHONY: pulisci
pulisci:
	rm -f vocali $(OGGETTI)
```

```
$ make
gcc -Wall -Wextra -g   -c -o principale.o principale.c
gcc -Wall -Wextra -g   -c -o conta.o conta.c
gcc -Wall -Wextra -g -o vocali principale.o conta.o
$ ./vocali ciao aiuola xyz
ciao: 3 vocali
aiuola: 5 vocali
xyz: 0 vocali
chiamate: 3
$ make
make: 'vocali' is up to date.
$ touch conta.h && make           # tutti e due i .o dipendono da conta.h: si ricompila tutto
```

Le ricette cominciano con un carattere di **tabulazione**, non con spazi (è l'errore più frequente: `missing separator`). `$@` è il bersaglio, `$^` tutti i prerequisiti. Le regole per i `.o` non hanno ricetta: `make` conosce già la regola implicita "un `.o` si fa dal `.c` con `$(CC) $(CFLAGS) -c`", e noi aggiungiamo solo la dipendenza dall'header. `.PHONY` dichiara che `pulisci` non è un file. Molte sfide con il sorgente includono un `Makefile`: leggerlo è il modo più rapido di sapere **con quali opzioni** (e quindi con quali protezioni) è stato compilato il binario.

---

# Parte II — Il linguaggio

## 3. La struttura di un programma e l'I/O

### 3.1 `main`, i suoi argomenti e il suo valore

Ogni programma C ospitato (*hosted*, cioè che gira sopra un sistema operativo) comincia da `main`, che lo standard ammette in due forme, `int main(void)` e `int main(int argc, char *argv[])`; Linux, come tutti gli Unix, ne accetta una terza con l'ambiente:

```c
// argomenti.c — argc, argv ed envp
#include <stdio.h>
int main(int argc, char *argv[], char *envp[]) {
    printf("argc = %d\n", argc);
    for (int i = 0; i < argc; i++)
        printf("argv[%d] = \"%s\"\n", i, argv[i]);
    printf("argv[argc] = %p\n", (void *)argv[argc]);
    int n = 0;
    while (envp[n]) n++;
    printf("%d variabili d'ambiente, la prima: %s\n", n, envp[0]);
    return argc - 1;
}
```

```
$ gcc -Wall -Wextra -o argomenti argomenti.c
$ env -i A=1 B=2 ./argomenti 'uno due' tre; echo "codice: $?"
argc = 3
argv[0] = "./argomenti"
argv[1] = "uno due"
argv[2] = "tre"
argv[argc] = (nil)
2 variabili d'ambiente, la prima: A=1
codice: 2
```

È la stessa struttura che hai visto dal lato della shell (L1 §6.1, L5 §4.2): `execve(percorso, argv, envp)` passa al nuovo programma un array di stringhe per gli argomenti e uno per l'ambiente, entrambi terminati da un puntatore **nullo** (`argv[argc]` è `NULL`, che `printf` con `%p` stampa come `(nil)`). `argv[0]` è il nome con cui il programma è stato invocato, e non è affidabile: lo sceglie chi chiama `execve`. `char *argv[]` si legge "array di puntatori a `char`": cioè un array di stringhe C (§6, §8). Il valore restituito da `main` diventa il **codice di uscita** del processo, quello di `$?` (L4 §8.3): per convenzione 0 è successo, qualunque altro valore un errore, e solo gli 8 bit bassi arrivano al genitore (`return 256` dà 0, L5 §4.4).

Le funzioni `exit(codice)` (da `<stdlib.h>`) e `return codice` da `main` si equivalgono: entrambe svuotano i buffer di `stdio` ed eseguono le funzioni registrate con `atexit`. `_exit(codice)` (da `<unistd.h>`) invece chiama direttamente il kernel, **senza** svuotare i buffer: un `printf` senza `\n` seguito da `_exit` non stampa niente.

### 3.2 Scrivere: `printf` e i suoi formati

`printf(formato, ...)` scrive sullo standard output, sostituendo ogni **conversione** del formato (una sequenza che comincia con `%`) con il valore del prossimo argomento. È una funzione **variadica**: accetta un numero qualunque di argomenti, e non ha modo di sapere né quanti sono né di che tipo. Lo deduce **solo dal formato**. Se il formato e gli argomenti non corrispondono, `printf` legge comunque quello che il formato le dice di leggere, dai registri e dallo stack: è comportamento indefinito, e con un formato scelto dall'utente è la vulnerabilità di formato (CWE-134) del Modulo 4. GCC controlla la corrispondenza quando il formato è una costante (`-Wformat`, attivo con `-Wall`).

```c
// formati.c — le conversioni di printf
#include <stdio.h>
int main(void) {
    int n = 3054; unsigned long big = 0xdeadbeefcafeUL; const char *s = "Lezione9";
    printf("[%d] [%5d] [%-5d|] [%05d] [%+d]\n", 42, 42, 42, 42, 42);
    printf("[%x] [%X] [%#x] [%08x] [%o] [%#o]\n", n, n, n, n, 493, 493);
    printf("[%u] [%d]\n", -1, (int)4294967295u);
    printf("[%lx] [%lu] [%zu]\n", big, big, sizeof big);
    printf("[%c%c] [%s] [%.3s] [%10s] [%-10s|]\n", 'O', 75, s, s, s, s);
    printf("[%f] [%.2f] [%e] [%g]\n", 3.14159, 3.14159, 31415.9, 0.0001);
    printf("[%p] [%%]\n", (void *)s);
    int scritti = printf("ciao\n");
    printf("printf ha scritto %d byte\n", scritti);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o formati formati.c && ./formati
[42] [   42] [42   |] [00042] [+42]
[bee] [BEE] [0xbee] [00000bee] [755] [0755]
[4294967295] [-1]
[deadbeefcafe] [244837814094590] [8]
[OK] [Lezione9] [Lez] [  Lezione9] [Lezione9  |]
[3.141590] [3.14] [3.141590e+04] [0.0001]
[0x55e5e8a69008] [%]
ciao
printf ha scritto 5 byte
```

La forma generale di una conversione è `%[flag][larghezza][.precisione][lunghezza]tipo`:

| Parte | Esempi | Significato |
|---|---|---|
| tipo | `d` `i` (intero con segno), `u` (senza segno), `x` `X` (esadecimale), `o` (ottale), `c` (carattere), `s` (stringa), `f` `e` `g` (virgola mobile), `p` (puntatore), `%` (il carattere `%`) | come interpretare l'argomento |
| lunghezza | `hh` (`char`), `h` (`short`), `l` (`long`), `ll` (`long long`), `z` (`size_t`) | la dimensione dell'argomento intero: `%ld`, `%zu`, `%llx`, `%hhx` |
| larghezza | `%5d`, `%10s`, `%*d` (la larghezza è un argomento) | numero minimo di caratteri |
| precisione | `%.2f` (cifre decimali), `%.3s` (al massimo 3 caratteri della stringa) | |
| flag | `-` (allinea a sinistra), `0` (riempi con zeri), `+` (segno sempre), `#` (prefisso `0x` o `0`), spazio | |

Due righe dell'output meritano attenzione. `[%u]` con `-1` stampa 4294967295: `printf` ha ricevuto gli stessi 32 bit, e il formato dice di leggerli senza segno (L7 §3.3); `%d` con `(int)4294967295u` fa il viaggio inverso. E `%p` stampa un indirizzo: quello della stringa costante, che è in `.rodata` (§2.6) e quindi, in un eseguibile PIE, a un indirizzo che comincia con `0x55` o `0x56` e cambia a ogni esecuzione.

`printf` restituisce il numero di byte scritti. Esistono poi le varianti: `fprintf(stderr, ...)` scrive su un altro flusso (lo standard error, per i messaggi d'errore, L4 §1), `snprintf(buf, n, ...)` scrive in un array **al massimo** `n` byte terminatore compreso (§8.3), `dprintf(fd, ...)` su un descrittore. `puts(s)` scrive una stringa e un `\n`, `putchar(c)` un carattere.

**Una regola, da subito.** Mai `printf(s)` con una stringa `s` che non hai scritto tu: si scrive `printf("%s", s)` (o `fputs(s, stdout)`). Se `s` contiene `%x` o `%n`, `printf` lo interpreterà come formato. Il compilatore te lo dice (`format not a string literal and no format arguments`, attivo per default su Ubuntu con `-Wformat-security`).

### 3.3 Leggere: `fgets`, `scanf` e la conversione dei numeri

Leggere l'input in C è più difficile che scriverlo, e più pericoloso. La regola pratica è: **leggi una riga intera con `fgets`, poi analizzala**.

`fgets(buf, n, flusso)` legge dal flusso fino al `\n` compreso, o fino alla fine del file, ma **al massimo `n − 1` caratteri**, e termina sempre la stringa con `\0`. Restituisce `buf`, oppure `NULL` se non ha letto niente (fine del file o errore). Il `\n` resta nella stringa, e se la riga era più lunga di `n − 1` il resto rimane nel flusso per la lettura successiva. È la funzione che hai visto in tutti i programmi della Lezione 8.

Per convertire il testo in un numero si usano `strtol` (per `long`), `strtoul`, `strtoll`, `strtod`. Non `atoi`: `atoi("abc")` restituisce 0 senza modo di distinguerlo da `atoi("0")`, e il suo comportamento in caso di overflow non è definito. `strtol` invece dice **dove** si è fermata e se il valore era fuori dall'intervallo:

```c
// leggi.c — leggere un numero dall'input in modo robusto
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
int main(void) {
    char riga[64];
    printf("Un numero: ");
    fflush(stdout);
    if (!fgets(riga, sizeof riga, stdin)) {
        fprintf(stderr, "nessun input\n");
        return 1;
    }
    riga[strcspn(riga, "\n")] = '\0';            // toglie il \n finale, se c'è
    char *fine;
    errno = 0;
    long n = strtol(riga, &fine, 10);
    if (fine == riga || *fine != '\0') {
        fprintf(stderr, "\"%s\" non è un numero\n", riga);
        return 1;
    }
    if (errno == ERANGE) {
        fprintf(stderr, "%s è fuori dall'intervallo di long\n", riga);
        return 1;
    }
    printf("hai scritto %ld, il doppio è %ld\n", n, 2 * n);
    return 0;
}
```

```
$ for v in 21 12abc abc "" 99999999999999999999 " 7"; do printf '%s\n' "$v" | ./leggi; echo " [$?]"; done
Un numero: hai scritto 21, il doppio è 42
 [0]
Un numero: "12abc" non è un numero
 [1]
Un numero: "abc" non è un numero
 [1]
Un numero: "" non è un numero
 [1]
Un numero: 99999999999999999999 è fuori dall'intervallo di long
 [1]
Un numero: hai scritto 7, il doppio è 14
 [0]
```

(I messaggi d'errore vanno sullo standard error, quindi in un terminale si mescolano all'output: per separarli, `2>/dev/null`.) `fine` punta al primo carattere non convertito: se è uguale a `riga` non è stato convertito niente, se non è il terminatore c'era altro dopo il numero. `strtol` salta gli spazi iniziali (da cui `" 7"` accettato) e accetta un segno. `strcspn(riga, "\n")` restituisce la lunghezza del prefisso senza `\n`, e lì scriviamo il terminatore: è il modo idiomatico di togliere il `\n` lasciato da `fgets`. `fflush(stdout)` prima di leggere fa arrivare la domanda senza `\n` anche dietro una pipe (L8, Esempio 4). C'è ancora un difetto: `2 * n` può andare in overflow se `n` è molto grande (§4.5); lo correggerai nell'Esercizio 6.

**`scanf`** legge e converte insieme (`scanf("%d", &n)`), e restituisce il numero di conversioni riuscite. È comoda negli esempi, ma ha tre problemi: se l'input non corrisponde si ferma **lasciando l'input nel flusso** (un ciclo `while (scanf("%d", &n) != 1)` con l'input `abc` gira per sempre, perché `abc` non viene mai consumato); `%s` senza larghezza legge una parola **di qualunque lunghezza** in un array di dimensione fissa, cioè un *buffer overflow* (si scrive `%15s` per un array di 16); e mescolare `scanf` e `fgets` lascia `\n` indesiderati nel flusso. La funzione **`gets`**, che legge una riga senza alcun limite, è così pericolosa che lo standard C11 l'ha **eliminata**: compare ancora nelle sfide, proprio perché è l'esempio perfetto di *buffer overflow* (CWE-242, uso di una funzione intrinsecamente pericolosa).

### 3.4 `stdio` e il buffering, dal lato del C

I flussi `stdin`, `stdout` e `stderr` sono oggetti di tipo `FILE *` creati dalla libreria C, ognuno associato a un descrittore (0, 1, 2) e a un **buffer** (L4 §3). Le regole della `glibc`, ora dal lato di chi scrive il programma:

- `stdout` è **bufferizzato a righe** se è un terminale, **a blocchi** (4096 byte, o la dimensione del blocco del file) altrimenti;
- `stderr` non è mai bufferizzato;
- prima di leggere da un flusso bufferizzato a righe o non bufferizzato che deve chiedere dati al kernel, la libreria svuota `stdout` se è bufferizzato a righe: è ciò che fa arrivare la domanda "Come ti chiami? " in un terminale (L8, Esempio 4);
- `fflush(f)` svuota il buffer di `f`; `exit` e il `return` da `main` svuotano tutti i buffer; un processo ucciso da un segnale perde ciò che era nel buffer.

`setvbuf(stdout, NULL, _IONBF, 0)`, all'inizio di `main`, rende `stdout` non bufferizzato: è la riga che gli autori delle sfide aggiungono per evitare a tutti i giocatori i problemi della Lezione 8. Le altre modalità sono `_IOLBF` (a righe) e `_IOFBF` (a blocchi). La differenza tra queste funzioni e le chiamate di sistema `read` e `write`, che non hanno buffer, la vedremo nel §11.

## 4. I tipi e le loro dimensioni

### 4.1 Gli interi: quanto sono grandi?

Il C ha cinque tipi interi standard con segno, ciascuno con il suo gemello senza segno (`unsigned`): `signed char`, `short`, `int`, `long`, `long long`. Lo standard non fissa le loro dimensioni, ma solo dei **minimi** (`short` e `int` almeno 16 bit, `long` almeno 32, `long long` almeno 64) e un ordine (`sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)`). Le dimensioni vere le decide il **modello dei dati** della piattaforma. Linux, macOS e gli altri Unix a 64 bit usano **LP64** (*long and pointer 64*): `int` a 32 bit, `long` e i puntatori a 64. Windows a 64 bit usa **LLP64**: anche `long` è a 32 bit, e solo `long long` e i puntatori a 64. L'operatore `sizeof` restituisce la dimensione in byte di un tipo o di un'espressione, come valore di tipo `size_t`:

```c
// dimensioni.c — quanto occupano i tipi su questa macchina
#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <stddef.h>
int main(void) {
    printf("char        %zu  [%d, %d]\n", sizeof(char), CHAR_MIN, CHAR_MAX);
    printf("short       %zu  [%d, %d]\n", sizeof(short), SHRT_MIN, SHRT_MAX);
    printf("int         %zu  [%d, %d]\n", sizeof(int), INT_MIN, INT_MAX);
    printf("long        %zu  [%ld, %ld]\n", sizeof(long), LONG_MIN, LONG_MAX);
    printf("long long   %zu\n", sizeof(long long));
    printf("unsigned    %zu  [0, %u]\n", sizeof(unsigned), UINT_MAX);
    printf("size_t      %zu  [0, %zu]\n", sizeof(size_t), SIZE_MAX);
    printf("void *      %zu\n", sizeof(void *));
    printf("float %zu, double %zu, long double %zu\n", sizeof(float), sizeof(double), sizeof(long double));
    printf("int32_t %zu, uint64_t %zu, intptr_t %zu\n", sizeof(int32_t), sizeof(uint64_t), sizeof(intptr_t));
    return 0;
}
```

```
$ gcc -Wall -Wextra -o dimensioni dimensioni.c && ./dimensioni
char        1  [-128, 127]
short       2  [-32768, 32767]
int         4  [-2147483648, 2147483647]
long        8  [-9223372036854775808, 9223372036854775807]
long long   8
unsigned    4  [0, 4294967295]
size_t      8  [0, 18446744073709551615]
void *      8
float 4, double 8, long double 16
int32_t 4, uint64_t 8, intptr_t 8
```

Le costanti `INT_MAX`, `UINT_MAX` e simili sono in `<limits.h>`; gli intervalli sono quelli del complemento a due della Lezione 7 (§3.2): da −2ⁿ⁻¹ a 2ⁿ⁻¹ − 1 con segno, da 0 a 2ⁿ − 1 senza.

Tre tipi meritano un discorso a parte.
- **`char`** è il tipo di un byte, e `sizeof(char)` è 1 per definizione. Ma se `char` senza altro abbia segno o no lo decide la piattaforma: su x86-64 ha segno (−128…127), su ARM Linux di solito no (0…255). Per i **byte** come dati si usa `unsigned char` (o `uint8_t`), sempre: è l'equivalente dei `bytes` di Python.
- **`size_t`** (da `<stddef.h>`) è il tipo senza segno delle **dimensioni**: lo restituiscono `sizeof` e `strlen`, lo vogliono `malloc`, `memcpy`, `read`. È a 64 bit su LP64. Il suo gemello con segno, `ssize_t`, è il tipo di ritorno di `read` e `write`, che usano −1 per segnalare un errore (§11).
- I **tipi a dimensione esatta** di `<stdint.h>`, `int8_t`, `uint8_t`, `int16_t`, …, `uint64_t`, hanno la dimensione scritta nel nome su ogni piattaforma, e `intptr_t`/`uintptr_t` sono grandi abbastanza per contenere un puntatore. Per un formato di file, un protocollo di rete, un'intestazione, si usano sempre questi (come i `<I` e `<Q` di `struct` in Python, L8 §3.3). Per stamparli in modo portabile ci sono le macro di `<inttypes.h>`, come `PRIu64`: `printf("%" PRIu64 "\n", x)`.

Le **costanti** hanno anch'esse un tipo: `42` è `int`, `42u` `unsigned`, `42L` `long`, `42UL` `unsigned long`, `0x2a` è un `int` scritto in esadecimale, `052` (con lo zero iniziale!) è un `int` in **ottale** e vale 42, `'A'` è un `int` (in C, non in C++) che vale 65. Una costante troppo grande per `int` prende automaticamente un tipo più grande.

### 4.2 Virgola mobile, booleani, `void`

`float` (32 bit) e `double` (64 bit) sono numeri IEEE 754 (L7 §6), con gli stessi limiti di precisione di Python: `0.1 + 0.2 != 0.3`. Nei programmi di sistema e nelle sfide sono rari. Il C non aveva un tipo booleano fino al C99, che ha introdotto `_Bool` e l'header `<stdbool.h>` con `bool`, `true` e `false` (in C23 sono parole chiave). Una condizione in C è un **intero**: 0 è falso, qualunque altro valore è vero, e gli operatori di confronto (`==`, `<`, `&&`, `!`) restituiscono un `int` che vale 0 o 1. `void` significa "nessun valore": una funzione `void` non restituisce niente, `(void)` nella lista dei parametri dice che la funzione non ne ha, e `void *` è il "puntatore a qualunque cosa" del §6.6.

### 4.3 Le conversioni implicite

Quando un'espressione combina tipi diversi, il C li **converte** in silenzio secondo regole precise, che conviene conoscere perché producono alcuni dei bug di sicurezza più subdoli.

1. **Promozione intera.** Prima di un'operazione aritmetica, ogni valore di tipo più piccolo di `int` (`char`, `short`, e i loro `unsigned`) viene convertito in `int`. Quindi `unsigned char a = 250, b = 10;` e `a + b` vale **260**, non 4: il calcolo avviene in `int`. Diventa 4 solo quando il risultato viene rimesso in un `unsigned char`.
2. **Conversioni aritmetiche usuali.** Se i due operandi hanno tipi diversi, quello "più piccolo" si converte nel "più grande"; e se uno è senza segno e l'altro con segno della stessa dimensione, **vince il senza segno**. È la regola che fa dire al C che `-1 < 1u` è falso: −1 diventa `unsigned` e vale 4294967295.
3. **Assegnamento.** Assegnando un valore a una variabile di tipo più piccolo si tengono i bit bassi (per i tipi senza segno è il modulo 2ⁿ; per quelli con segno il risultato è definito dall'implementazione, e GCC tiene i bit bassi): `unsigned char t = 300` vale 44 (300 − 256), `int k = 3000000000L` vale −1294967296.

```c
// conversioni.c — le conversioni implicite che sorprendono
#include <stdio.h>
#include <string.h>
int main(void) {
    unsigned int u = 1;
    int i = -1;
    printf("(1) -1 < 1u ? %s\n", i < u ? "sì" : "no");
    printf("(2) (unsigned)-1 = %u\n", (unsigned)i);
    char c = 200;
    unsigned char uc = 200;
    printf("(3) char 200 = %d, unsigned char 200 = %d\n", c, uc);
    unsigned char a = 250, b = 10;
    printf("(4) a + b = %d, (unsigned char)(a + b) = %d\n", a + b, (unsigned char)(a + b));
    printf("(5) 7 / 2 = %d, -7 / 2 = %d, -7 %% 2 = %d, 7.0 / 2 = %.1f\n", 7 / 2, -7 / 2, -7 % 2, 7.0 / 2);
    int n = 300; unsigned char t = n;
    printf("(6) unsigned char t = 300 -> %d\n", t);
    long big = 3000000000; int k = big;
    printf("(7) int k = 3000000000 -> %d\n", k);
    printf("(8) strlen(\"\") - 1 = %zu\n", strlen("") - 1);
    printf("(9) sizeof('a') = %zu, sizeof(char) = %zu\n", sizeof('a'), sizeof(char));
    unsigned int x = 0; x--;
    printf("(10) unsigned 0 - 1 = %u\n", x);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o conversioni conversioni.c
conversioni.c:7:36: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
$ ./conversioni
(1) -1 < 1u ? no
(2) (unsigned)-1 = 4294967295
(3) char 200 = -56, unsigned char 200 = 200
(4) a + b = 260, (unsigned char)(a + b) = 4
(5) 7 / 2 = 3, -7 / 2 = -3, -7 % 2 = -1, 7.0 / 2 = 3.5
(6) unsigned char t = 300 -> 44
(7) int k = 3000000000 -> -1294967296
(8) strlen("") - 1 = 18446744073709551615
(9) sizeof('a') = 4, sizeof(char) = 1
(10) unsigned 0 - 1 = 4294967295
```

Riga per riga: (1) la conversione aritmetica usuale, segnalata da `-Wextra`; (2) lo stesso, esplicito con un **cast** (`(tipo)espressione`); (3) 200 non sta in un `char` con segno e diventa 200 − 256 = −56; (4) la promozione intera; (5) la divisione tra interi **tronca verso zero** (−7/2 = −3, a differenza del `//` di Python che dà −4), e il resto ha il segno del dividendo; basta un operando `double` perché la divisione sia in virgola mobile; (6)–(7) il troncamento all'assegnamento; (8) `strlen` restituisce `size_t`, senza segno: 0 − 1 non è −1 ma 2⁶⁴ − 1. Un ciclo `for (size_t i = 0; i < strlen(s) - 1; i++)` su una stringa vuota non termina in tempo utile: è un errore classico, e una vulnerabilità quando quel valore diventa una lunghezza da copiare; (9) un carattere tra apici è un `int`; (10) gli `unsigned` "girano" in modo definito.

La riga (8) è il prototipo di una famiglia di vulnerabilità: un controllo di lunghezza fatto con un tipo con segno e una copia fatta con `size_t`. Se il programma controlla `if (len < 64)` con `int len` letto dall'utente e poi chiama `memcpy(buf, dati, len)`, un `len` negativo supera il controllo e diventa, convertito in `size_t`, un numero enorme (CWE-195, *signed to unsigned conversion error*).

### 4.4 Operatori sui bit e spostamenti

Gli operatori `&`, `|`, `^`, `~`, `<<`, `>>` sono quelli della Lezione 7 (§4), con due avvertenze del C. Lo spostamento a sinistra di un valore con segno che fa uscire un 1 dal bit di segno, e lo spostamento di una quantità **maggiore o uguale** alla larghezza del tipo (`1 << 32` con un `int` a 32 bit), sono comportamento indefinito; e lo spostamento a destra di un valore **negativo** è definito dall'implementazione (GCC replica il bit di segno: spostamento *aritmetico*). Per manipolare bit si usano quindi tipi **senza segno**: `uint32_t`, `1u << n`, `(uint64_t)1 << 40`.

### 4.5 L'overflow

Le operazioni sugli interi **senza segno** sono definite modulo 2ⁿ: `UINT_MAX + 1` è 0, sempre, come hai visto nella riga (10). Quelle sugli interi **con segno** che producono un risultato fuori dall'intervallo (`INT_MAX + 1`) sono invece **comportamento indefinito**. Sull'hardware x86-64 la somma "gira" anche per i numeri con segno, e un `printf` di `INT_MAX + 1` stampa −2147483648; ma il compilatore è autorizzato a **supporre che l'overflow con segno non avvenga mai**, e ottimizza di conseguenza:

```c
// ub.c — l'overflow con segno è comportamento indefinito
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
int piu_grande(int x) { return x + 1 > x; }      // "sempre vero"?
int main(int argc, char *argv[]) {
    int x = argc > 1 ? atoi(argv[1]) : INT_MAX;
    printf("x = %d, x + 1 = %d, x + 1 > x: %d\n", x, x + 1, piu_grande(x));
    return 0;
}
```

```
$ gcc -o ub ub.c && ./ub
x = 2147483647, x + 1 = -2147483648, x + 1 > x: 1
$ gcc -O2 -S -o - ub.c | sed -n '/^piu_grande:/,/ret/p' | grep -v cfi
piu_grande:
.LFB39:
	endbr64
	movl	$1, %eax
	ret
$ gcc -fwrapv -o ub ub.c && ./ub
x = 2147483647, x + 1 = -2147483648, x + 1 > x: 0
```

Il programma stampa contemporaneamente che `x + 1` vale −2147483648 e che `x + 1 > x` è vero. Non è un errore del compilatore: poiché l'overflow "non può avvenire", `x + 1 > x` è sempre vero, e GCC sostituisce l'intera funzione con `return 1` (l'assembly lo mostra: `movl $1, %eax`). Lo fa già a `-O0`, perché questa semplificazione avviene presto, sull'albero del programma. Con `-fwrapv` chiedi a GCC di trattare l'overflow con segno come modulare, e il risultato torna "intuitivo". La conseguenza pratica è seria: un controllo di sicurezza scritto come `if (x + 100 < x) /* overflow! */ return -1;` con `x` di tipo `int` può essere **eliminato** dal compilatore. I controlli si scrivono **prima** dell'operazione, senza farla: `if (x > INT_MAX - 100)`, oppure con le funzioni di GCC `__builtin_add_overflow(a, b, &risultato)`, che restituiscono vero se l'operazione andrebbe in overflow.

Gli **overflow interi** sono una classe di vulnerabilità a sé (CWE-190): una dimensione calcolata come `n * sizeof(elemento)` che va in overflow produce un `malloc` troppo piccolo, e la copia successiva scrive oltre la fine. È uno dei motivi per cui esiste `calloc(n, dimensione)`, che controlla il prodotto (§10).

### 4.6 Il comportamento indefinito

Abbiamo già incontrato il **comportamento indefinito** (*undefined behavior*, UB) tre volte: l'overflow con segno, `i++` due volte nella stessa espressione (§2.2), gli spostamenti troppo grandi. Lo standard C distingue con cura tre categorie:

- **comportamento definito dall'implementazione**: ogni compilatore sceglie, ma deve documentare la scelta (il segno di `char`, la dimensione di `int`, lo spostamento a destra dei negativi);
- **comportamento non specificato**: ci sono più possibilità e il compilatore può sceglierne una qualunque, anche diversa ogni volta, senza documentarla (l'ordine in cui vengono valutati gli argomenti di una funzione);
- **comportamento indefinito**: lo standard non impone **nessun** requisito. Il programma può fare la cosa "ovvia", crollare, produrre risultati assurdi, o comportarsi diversamente cambiando livello di ottimizzazione.

L'elenco dei comportamenti indefiniti dello standard C17 (l'appendice J.2) ne conta quasi duecento. Quelli che incontrerai di continuo: accedere a un array fuori dai limiti, dereferenziare un puntatore nullo o non valido, usare memoria già liberata, leggere una variabile locale non inizializzata, l'overflow con segno, modificare una stringa letterale, chiamare `printf` con argomenti che non corrispondono al formato, modificare due volte la stessa variabile senza un punto di sequenza (`i = i++`). Per la sicurezza il comportamento indefinito è la radice del problema: è lo spazio in cui il programma fa qualcosa che il programmatore non ha scritto, e che un attaccante può scegliere.

Gli strumenti per scovarlo durante lo sviluppo sono i **sanitizer** del compilatore: `-fsanitize=undefined` (UBSan) aggiunge controlli che segnalano, durante l'esecuzione, l'overflow con segno, gli spostamenti illegali, la divisione per zero e altro; `-fsanitize=address` (ASan, §10.5) controlla gli accessi alla memoria. Sul nostro `ub.c`:

```
$ gcc -fsanitize=undefined -o ub ub.c && ./ub
ub.c:8:5: runtime error: signed integer overflow: 2147483647 + 1 cannot be represented in type 'int'
x = 2147483647, x + 1 = -2147483648, x + 1 > x: 1
```

UBSan segnala la somma nella riga 8, ma non quella dentro `piu_grande`: quella non viene più eseguita, perché il compilatore l'ha già eliminata.

## 5. Espressioni, controllo del flusso e funzioni

### 5.1 Quello che sai già da Python

La sintassi del controllo del flusso è quella che Python ha in parte ereditato, con le parentesi graffe al posto dell'indentazione e il punto e virgola alla fine di ogni istruzione:

```c
if (x > 0) {
    puts("positivo");
} else if (x == 0) {
    puts("zero");
} else {
    puts("negativo");
}

for (int i = 0; i < 10; i++) { ... }     // inizializzazione; condizione; passo
while (n > 0) { ... }
do { ... } while (n > 0);                 // il corpo viene eseguito almeno una volta

switch (op) {
case '+': r = a + b; break;
case '-': r = a - b; break;
default:  return -1;
}
```

Le differenze che fanno sbagliare chi viene da Python: le parentesi intorno alla condizione sono obbligatorie; le graffe si possono omettere se il corpo è una sola istruzione, ed è una fonte storica di bug (nel 2014 il *goto fail* di Apple, una riga `goto fail;` duplicata fuori da un `if` senza graffe, disattivava la verifica dei certificati TLS); in uno `switch`, senza `break` l'esecuzione **prosegue** nel caso successivo (*fall-through*); `=` è l'assegnamento e `==` il confronto, e `if (x = 0)` è legale (assegna 0 e la condizione è falsa: `-Wall` avvisa); gli operatori logici sono `&&`, `||`, `!` e, come in Python, `&&` e `||` valutano il secondo operando solo se serve (*cortocircuito*), una proprietà su cui si basa l'idioma `if (p != NULL && p->x > 0)`. `i++` e `++i` incrementano entrambi `i`, ma come espressione il primo vale il valore **prima** dell'incremento, il secondo quello dopo. `break` e `continue` funzionano come in Python; `goto etichetta` salta a un'etichetta nella stessa funzione, ed è usato quasi solo per la gestione degli errori (`goto pulizia;`).

### 5.2 Le funzioni e il passaggio per valore

Una funzione C ha un tipo di ritorno, un nome e dei parametri tipizzati. Deve essere **dichiarata** prima di essere usata: o definita più in alto nel file, o con un **prototipo** (`int somma(int a, int b);`), di solito in un header.

```c
int somma(int a, int b) {
    return a + b;
}
```

In C gli argomenti si passano **sempre per valore**: la funzione riceve una **copia** di ogni argomento, e modificarla non cambia la variabile del chiamante. È diverso da Python, dove si passano riferimenti a oggetti (L8 §2.1). Per permettere a una funzione di modificare una variabile del chiamante, le si passa il suo **indirizzo**, un puntatore (§6.3): è ciò che fa `scanf("%d", &n)`, ed è il motivo della `&`. Gli array sono l'eccezione apparente: un array passato a una funzione "decade" nel puntatore al suo primo elemento (§6.4), quindi la funzione lavora sull'array originale, e non ne conosce la lunghezza. Per questo le funzioni C che lavorano su array ricevono quasi sempre anche la dimensione: `memcpy(dest, src, n)`, `fgets(buf, n, f)`, `read(fd, buf, n)`.

### 5.3 Visibilità e durata delle variabili

Ogni variabile ha un **ambito** (dove il suo nome è visibile) e una **durata di memorizzazione** (quando esiste in memoria). Le combinazioni che contano:

| Dichiarata | Ambito | Durata | Dove vive (§9) | Valore iniziale |
|---|---|---|---|---|
| dentro una funzione o un blocco | il blocco | **automatica**: dall'ingresso all'uscita dal blocco | sullo **stack** (o in un registro) | **indeterminato** |
| dentro una funzione, con `static` | il blocco | **statica**: tutto il programma | `.data` o `.bss` | 0, o quello scritto, una volta sola |
| fuori da ogni funzione | il file (e gli altri file, con `extern`) | statica | `.data` o `.bss` | 0, o quello scritto |
| fuori da ogni funzione, con `static` | solo il file | statica | `.data` o `.bss` | 0, o quello scritto |
| allocata con `malloc` | (non ha nome: la raggiungi con un puntatore) | **allocata**: fino a `free` | nello **heap** | indeterminato (`calloc`: 0) |

La riga più importante per la sicurezza è la prima: una variabile locale **non inizializzata** contiene ciò che c'era prima in quel punto dello stack, cioè i resti di una chiamata precedente, e leggerla è comportamento indefinito (CWE-457). È così che a volte un programma fa trapelare dati che non dovrebbe. La seconda riga, la variabile locale `static`, mantiene il suo valore tra una chiamata e l'altra: è un contatore che sopravvive alla funzione.

Una funzione non deve mai restituire l'indirizzo di una sua variabile automatica: quando la funzione ritorna, quella variabile non esiste più, e la memoria verrà riusata dalla chiamata successiva (*dangling pointer*, CWE-562). GCC avvisa (`function returns address of local variable`), e GCC 13 arriva a sostituire il puntatore restituito con `NULL`, a qualunque livello di ottimizzazione: un programma che lo usa crolla subito, invece di leggere memoria riusata.

---

# Parte III — La memoria

## 6. I puntatori

### 6.1 Che cos'è un puntatore

Un puntatore è una variabile che contiene un **indirizzo di memoria**. La memoria di un processo è un'unica grande sequenza di byte (L7 §2.1), ognuno con il suo numero d'ordine, l'indirizzo. Un `int` sta in quattro byte consecutivi; dire "il puntatore `p` punta a `x`" significa che `p` contiene l'indirizzo del primo di quei quattro byte. Questa è l'astrazione che Python ti nascondeva (i suoi "nomi che si riferiscono a oggetti", L8 §2.1, sono puntatori gestiti dall'interprete): in C i puntatori sono numeri espliciti, e ci puoi fare aritmetica.

Due operatori li collegano a ciò che puntano: `&x` è l'**indirizzo** di `x`; `*p` è il **valore puntato** da `p` (la *dereferenziazione*). Sono inversi: `*&x` è `x`. Il tipo di un puntatore dice a che cosa punta: `int *p` è "puntatore a `int`", e serve perché `*p` sappia quanti byte leggere e come interpretarli, e perché l'aritmetica dei puntatori (§6.3) funzioni.

```c
// puntatori.c — indirizzi, dereferenziazione, aritmetica
#include <stdio.h>
int main(void) {
    int x = 42;
    int *p = &x;                                  // p contiene l'indirizzo di x
    printf("x = %d, &x = %p, p = %p, *p = %d\n", x, (void *)&x, (void *)p, *p);
    *p = 7;                                       // scrive in x attraverso p
    printf("dopo *p = 7: x = %d\n", x);
    printf("sizeof x = %zu, sizeof p = %zu, &p = %p\n", sizeof x, sizeof p, (void *)&p);

    int a[4] = {10, 20, 30, 40};
    int *q = a;                                   // a "decade" in &a[0]
    printf("a = %p, &a[0] = %p, &a[1] = %p\n", (void *)a, (void *)&a[0], (void *)&a[1]);
    printf("q + 1 = %p (+%td byte), *(q + 2) = %d, q[3] = %d, 3[q] = %d\n",
           (void *)(q + 1), (char *)(q + 1) - (char *)q, *(q + 2), q[3], 3[q]);
    printf("sizeof a = %zu, sizeof q = %zu, elementi = %zu\n", sizeof a, sizeof q, sizeof a / sizeof a[0]);

    unsigned char *b = (unsigned char *)&a[1];    // gli stessi byte, visti uno a uno
    printf("i byte di a[1] = 20: %02x %02x %02x %02x\n", b[0], b[1], b[2], b[3]);

    char *s = "ciao";
    char **pp = &s;
    printf("s = %p -> \"%s\", *pp = %p, **pp = '%c'\n", (void *)s, s, (void *)*pp, **pp);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o puntatori puntatori.c && ./puntatori
x = 42, &x = 0x7fff65ed45e4, p = 0x7fff65ed45e4, *p = 42
dopo *p = 7: x = 7
sizeof x = 4, sizeof p = 8, &p = 0x7fff65ed45e8
a = 0x7fff65ed4610, &a[0] = 0x7fff65ed4610, &a[1] = 0x7fff65ed4614
q + 1 = 0x7fff65ed4614 (+4 byte), *(q + 2) = 30, q[3] = 40, 3[q] = 40
sizeof a = 16, sizeof q = 8, elementi = 4
i byte di a[1] = 20: 14 00 00 00
s = 0x5645f0b2412a -> "ciao", *pp = 0x5645f0b2412a, **pp = 'c'
```

Da notare: `p` e `&x` sono lo stesso valore; `*p = 7` cambia `x`, perché scrive nella sua memoria; un puntatore occupa 8 byte (è un indirizzo a 64 bit), **qualunque** sia il tipo a cui punta; `&p` è un altro indirizzo ancora (il puntatore è una variabile e ha a sua volta un indirizzo). Il stampare un indirizzo con `%p` richiede un `void *`, da cui i cast: su un PIE gli indirizzi dello stack cominciano con `0x7fff...` e quelli del codice e delle costanti con `0x55...` o `0x56...`.

### 6.2 Il puntatore nullo

Il valore speciale `NULL` (una macro per `(void *)0`, da `<stddef.h>` e altri header) significa "non punta a niente". Dereferenziarlo è comportamento indefinito: sui sistemi moderni la pagina all'indirizzo 0 non è mappata, quindi `*p` con `p == NULL` fa crollare il processo con `SIGSEGV` (il famigerato *segmentation fault*, L5 §8). Le funzioni che possono fallire restituiscono `NULL` per segnalarlo (`malloc` quando la memoria è esaurita, `fopen` quando il file non si apre, `strchr` quando il carattere non c'è), e il chiamante **deve** controllare prima di dereferenziare: `if (p == NULL) { ... }`, spesso scritto `if (!p)`. Dimenticare il controllo è CWE-476 (*NULL pointer dereference*), e, nel senso opposto, un puntatore che un attaccante riesce a portare a zero dove il programma non se lo aspetta è lo strumento di molti exploit.

### 6.3 L'aritmetica dei puntatori

Sommare un intero a un puntatore non somma byte, ma **elementi**: `q + 1`, con `q` di tipo `int *`, punta all'`int` successivo, cioè 4 byte più avanti; con un `char *` avanzerebbe di 1, con un `double *` di 8. Il compilatore moltiplica l'intero per `sizeof(*q)`. Questo rende l'aritmetica dei puntatori e gli array la stessa cosa (§6.4). La differenza di due puntatori dello stesso tipo dà il numero di **elementi** tra loro (di tipo `ptrdiff_t`, stampato con `%td`). Si possono sommare, sottrarre, confrontare puntatori, ma solo **dentro lo stesso array** (o un elemento oltre la fine): andare altrove è comportamento indefinito, anche solo a calcolare l'indirizzo senza dereferenziarlo.

### 6.4 Puntatori e array

In C array e puntatori sono legati da una regola sola: in quasi tutti i contesti, il nome di un array **decade** nel puntatore al suo primo elemento. Per questo `a` e `&a[0]` sono lo stesso valore, `*(a + i)` e `a[i]` sono la stessa cosa (e, poiché la somma è commutativa, anche `i[a]` e `3[q]` funzionano, per quanto nessuno li scriva), e una funzione che "riceve un array" riceve in realtà un puntatore.

Le due eccezioni, in cui il nome dell'array **non** decade, sono proprio quelle dell'esempio: `sizeof a` dà la dimensione dell'intero array (16 byte per 4 `int`), non del puntatore; e `&a` dà l'indirizzo dell'array (numericamente uguale a `&a[0]`, ma di tipo "puntatore ad array di 4 int"). Da `sizeof a / sizeof a[0]` si ricava il **numero di elementi** di un array — ma solo dove l'array è una vera variabile, non dove è decaduto: dentro una funzione che riceve `int v[]`, `sizeof v` è 8, la dimensione del puntatore, e GCC avvisa.

```c
// decadimento.c — un array passato a una funzione diventa un puntatore
#include <stdio.h>
void azzera(int v[], size_t n) {                  // v è un int *, anche se scritto int v[]
    for (size_t i = 0; i < n; i++) v[i] = 0;
}
void raddoppia(int k) { k *= 2; }                 // modifica una copia
void raddoppia_p(int *k) { *k *= 2; }             // modifica l'originale
int main(void) {
    int a[5] = {1, 2, 3, 4, 5};
    printf("fuori: sizeof a = %zu\n", sizeof a);
    azzera(a, 2);
    printf("a = {%d, %d, %d, %d, %d}\n", a[0], a[1], a[2], a[3], a[4]);
    int k = 21;
    raddoppia(k);    printf("raddoppia(k):    k = %d\n", k);
    raddoppia_p(&k); printf("raddoppia_p(&k): k = %d\n", k);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o decadimento decadimento.c && ./decadimento
fuori: sizeof a = 20
a = {0, 0, 3, 4, 5}
raddoppia(k):    k = 21
raddoppia_p(&k): k = 42
```

`azzera` modifica l'array del chiamante, perché riceve un puntatore ai suoi elementi (gli array "si passano per riferimento" solo in quanto decadono in puntatori); `raddoppia` riceve una **copia** di `k` e non cambia niente; `raddoppia_p` riceve l'indirizzo di `k` e lo modifica. È la differenza del §5.2, ed è il motivo della `&` in `scanf("%d", &n)`: `scanf` deve scrivere nella tua variabile, e in C l'unico modo è darle l'indirizzo.

### 6.5 Puntatori a funzione e `argv`

Anche le funzioni hanno un indirizzo, e un puntatore può contenerlo: `int (*op)(int, int) = somma;` dichiara `op` come puntatore a una funzione che prende due `int` e ne restituisce uno, e `op(3, 4)` la chiama. Servono per le *callback* (una funzione passata a un'altra, come il comparatore di `qsort`) e per le **tabelle di dispatch** (un array di puntatori a funzione indicizzato da un comando). In sicurezza sono un bersaglio: sovrascrivere un puntatore a funzione, o una casella della GOT (§2.5), dirotta l'esecuzione dove vuole l'attaccante.

Il `char *argv[]` di `main` è un array di puntatori a `char`, cioè un array di stringhe; `char **` è la stessa cosa vista come puntatore. Nell'esempio `puntatori.c`, `char **pp = &s` è un puntatore a un puntatore a `char`: `*pp` è `s`, `**pp` è il primo carattere. È la struttura "a due livelli" che ricorre ovunque in C: `argv`, l'ambiente `envp`, gli array di stringhe.

### 6.6 `void *` e `const`

`void *` è un puntatore **senza tipo**: può contenere l'indirizzo di qualunque oggetto, e ci si converte da e verso qualunque altro tipo di puntatore senza cast esplicito. È il tipo che usano `malloc` (restituisce `void *`, che assegni a un puntatore del tipo giusto) e `memcpy`/`memset`/`qsort` (lavorano sui byte, senza sapere il tipo). Non ci si può fare aritmetica né dereferenziarlo, perché non sa quanti byte occupa ciò che punta (GCC, come estensione, tratta `void *` come `char *` per l'aritmetica, ma è meglio essere espliciti).

`const` davanti al tipo puntato (`const char *s`) dice che **non modificherai** ciò che il puntatore punta: `*s = 'x'` non compila. È la promessa che fanno le funzioni che non alterano il loro argomento (`strlen(const char *)`, `printf(const char *, ...)`), ed è obbligatorio per puntare a una stringa letterale, che sta in `.rodata` e modificarla fa crollare il programma. Attenzione alla posizione: `const char *p` è "puntatore a `char` costante" (puoi cambiare `p`, non `*p`), `char *const p` è "puntatore costante a `char`" (puoi cambiare `*p`, non `p`).

## 7. Array, stringhe e `struct`

### 7.1 Gli array

Un array è una sequenza di elementi dello stesso tipo, contigui in memoria. `int a[5];` ne riserva cinque; `a[0]`…`a[4]` sono gli elementi, e `a[5]` è **già fuori**. Il C **non controlla** gli indici: `a[5]`, `a[100]`, `a[-1]` compilano e leggono o scrivono la memoria a quell'offset, qualunque cosa ci sia. È la causa prima dei *buffer overflow* (CWE-125 in lettura, CWE-787 in scrittura), e il motivo per cui in C bisogna sempre portarsi dietro la **lunghezza** di un array insieme al suo puntatore. Un array si inizializza con `int a[5] = {1, 2, 3};` (i restanti a zero), `int a[] = {1, 2, 3};` (la dimensione è dedotta: 3), `int a[100] = {0};` (tutti a zero). Gli array multidimensionali (`int m[3][4]`) sono array di array, contigui per righe.

### 7.2 Le stringhe C

Questa sezione è il cuore della lezione, perché la rappresentazione delle stringhe in C è la fonte di una parte enorme delle vulnerabilità del software. **Una stringa C è un array di `char` che contiene i caratteri seguiti da un byte `\0` (il terminatore, `NUL`).** Non c'è nessuna informazione sulla lunghezza memorizzata da nessuna parte: la lunghezza è *implicita*, ed è la distanza dal primo carattere al primo `\0`. È l'opposto dei `bytes` di Python, che conoscono la propria lunghezza (L8 §3.1), e della L7 §9.1, dove abbiamo visto proprio questa differenza tra stringhe terminate e stringhe con lunghezza esplicita.

```c
// stringhe.c — una stringa C è un array di char terminato da '\0'
#include <stdio.h>
#include <string.h>
int main(void) {
    char s[] = "ciao";                            // 5 byte: 'c','i','a','o','\0'
    printf("sizeof s = %zu, strlen(s) = %zu\n", sizeof s, strlen(s));
    for (size_t i = 0; i <= strlen(s); i++)
        printf("s[%zu] = %3d ('%c')\n", i, s[i], s[i] >= 32 ? s[i] : '.');
    s[2] = '\0';                                  // tronca la stringa a "ci"
    printf("dopo s[2]='\\0': \"%s\", ma i byte dopo ci sono ancora: '%c'\n", s, s[3]);

    char dst[8];
    strcpy(dst, "abc");                           // copia 4 byte (con il \0)
    strcat(dst, "de");                            // aggiunge in coda
    printf("dst = \"%s\", strlen = %zu\n", dst, strlen(dst));
    printf("strcmp(\"abc\",\"abd\") = %d, memcmp = %d\n", strcmp("abc", "abd"), memcmp("abc", "abd", 3));
    char *p = strchr("a=b=c", '=');
    printf("strchr '=' a offset %td; strstr: %s\n", p - "a=b=c", strstr("trova_me_qui", "me"));
    return 0;
}
```

```
$ gcc -Wall -Wextra -o stringhe stringhe.c && ./stringhe
sizeof s = 5, strlen(s) = 4
s[0] =  99 ('c')
...
s[4] =   0 ('.')
dopo s[2]='\0': "ci", ma i byte dopo ci sono ancora: 'o'
dst = "abcde", strlen = 5
strcmp("abc","abd") = -1, memcmp = -1
strchr '=' a offset 1; strstr: me_qui
```

Due fatti da fissare. Primo: `sizeof s` è 5 (l'array, terminatore compreso), `strlen(s)` è 4 (i caratteri). Confonderli è un errore di dimensionamento che porta a scrivere un byte di troppo o di meno. Secondo: scrivere un `\0` in mezzo **accorcia** la stringa per chiunque la legga con le funzioni `str...`, ma i byte successivi restano in memoria: un programma che "cancella" dati scrivendo un terminatore non li ha cancellati affatto, e si possono ancora trovare (è una tecnica di forensics, e un modo in cui trapelano segreti).

Le funzioni di `<string.h>` si dividono in due famiglie: quelle `str...` si fermano al terminatore; quelle `mem...` lavorano su un numero fisso di byte, terminatore o no (per i dati binari si usano queste). Le più comuni: `strlen` (lunghezza), `strcpy`/`strncpy` (copia), `strcat`/`strncat` (concatena), `strcmp`/`strncmp`/`memcmp` (confronto; restituiscono <0, 0, >0, **non** un booleano: `if (strcmp(a, b))` è vero quando sono **diversi**), `strchr`/`strrchr` (cerca un carattere), `strstr` (cerca una sottostringa), `memcpy`/`memmove` (copia byte; `memmove` funziona anche se le aree si sovrappongono), `memset` (riempie con un byte).

### 7.3 Perché `strcpy`, `strcat`, `gets`, `sprintf` sono pericolose

`strcpy(dst, src)` copia da `src` a `dst` **fino al terminatore di `src`**, senza sapere quanto è grande `dst`. Se `src` è più lungo, scrive oltre la fine di `dst`: *buffer overflow*. Lo stesso vale per `strcat` (concatena senza limiti), `sprintf` (formatta senza limiti) e `gets` (legge una riga senza limiti). Vederlo:

```c
// overflow.c — perché il terminatore è un problema di sicurezza
#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[]) {
    volatile int ammesso = 0;                     // volatile: il compilatore non lo ottimizza via
    char nome[8];
    if (argc > 1) strcpy(nome, argv[1]);          // nessun controllo di lunghezza!
    printf("nome = \"%s\", ammesso = %d\n", nome, ammesso);
    if (ammesso) puts(">>> accesso riservato sbloccato! <<<");
    return 0;
}
```

```
$ gcc -Wall -fno-stack-protector -O0 -o overflow overflow.c
$ ./overflow Zen
nome = "Zen", ammesso = 0
$ ./overflow AAAAAAAAAABBBB
nome = "AAAAAAAAAABBBB", ammesso = 1111638337
>>> accesso riservato sbloccato! <<<
$ ./overflow "$(printf 'AAAAAAAA\x01')"
nome = "AAAAAAAA", ammesso = 1
>>> accesso riservato sbloccato! <<<
```

`nome` è lungo 8 byte, e `ammesso` gli è vicino in memoria (su questo compilatore, subito dopo). Scrivere più di 8 caratteri in `nome` **invade** `ammesso` e ne cambia il valore: con 10 `A` e 4 `B`, i byte `BBBB` (0x42424242) finiscono dentro `ammesso`, che diventa diverso da zero, e il controllo `if (ammesso)` passa. L'ultimo caso è "chirurgico": 8 `A` riempiono `nome`, e il byte `\x01` scrive esattamente 1 in `ammesso`. Hai sovrascritto una variabile a cui il programma non ti dava accesso, dando in pasto a `strcpy` una stringa più lunga del previsto. È il cuore del Modulo 4: qui la vittima è una variabile vicina, lì sarà l'**indirizzo di ritorno** della funzione, cioè il controllo dell'esecuzione. (Abbiamo tolto `-fstack-protector` apposta: con la protezione attiva, il programma rileverebbe la modifica e abortirebbe con `*** stack smashing detected ***`.)

Le versioni "sicure" prendono la dimensione della destinazione: `strncpy(dst, src, n)`, `snprintf(dst, n, "%s", src)`, `strncat`, `fgets(buf, n, f)` al posto di `gets`. Non sono però senza insidie: `strncpy`, se `src` è lungo almeno `n`, **non** mette il terminatore, lasciando una stringa non terminata (un'altra fonte di guai); e `n` deve essere la dimensione **vera** della destinazione, non una indovinata. La regola solida è: conosci sempre la dimensione del buffer di destinazione, e usa funzioni a cui la passi.

### 7.4 Le strutture

Una `struct` raggruppa variabili di tipo diverso sotto un nome, come un record. È il mattone con cui si descrivono dati complessi: un pacchetto di rete, un'intestazione di file, una voce di una tabella.

```c
struct punto { int x; int y; };
struct persona {
    char nome[32];
    int eta;
    struct punto posizione;
};

struct persona p = {"Zen", 30, {10, 20}};
p.eta = 31;                        // accesso con il punto
struct persona *pp = &p;
pp->eta = 32;                      // accesso attraverso un puntatore: (*pp).eta
printf("%s, %d\n", pp->nome, pp->eta);
```

I campi si raggiungono con `.` su una struttura e con `->` su un puntatore a struttura (`pp->eta` è una scorciatoia per `(*pp).eta`). Un fatto che conta per chi legge dati binari: il compilatore inserisce **padding** tra i campi per allinearli (un `int` a un indirizzo multiplo di 4, ecc.), come hai visto con `struct.calcsize('HQ')` in Python (L8, Esercizio 2f). Quindi `sizeof(struct persona)` può essere maggiore della somma dei campi, e l'offset di un campo non è la somma delle dimensioni dei precedenti: per saperlo si usa la macro `offsetof(tipo, campo)` di `<stddef.h>`. Per leggere un formato binario "a byte" con una `struct`, o si disattiva il padding (`#pragma pack` o l'attributo `packed`), o si leggono i campi uno a uno: è una scelta che incontrerai nel Modulo 4 e in forensics. `typedef` dà un nome breve a un tipo (`typedef struct punto Punto;` permette di scrivere `Punto` invece di `struct punto`). Esistono anche le `union` (tutti i campi condividono la stessa memoria, uno per volta) e gli `enum` (costanti intere con un nome).

## 8. Lo spazio di indirizzi di un processo

Lo spazio di indirizzi di un processo è la memoria che vede, un'unica sequenza di indirizzi da 0 a 2⁴⁸ − 1 su x86-64, divisa in **regioni** con permessi diversi. È quella che hai guardato dall'esterno in `/proc/<PID>/maps` (L5 §7.4); ora la guardiamo dall'interno, chiedendo a un programma l'indirizzo delle sue variabili.

```c
// memoria.c — dove vive ogni variabile
#include <stdio.h>
#include <stdlib.h>
int globale_init = 1;                             // .data
int globale_zero;                                 // .bss
const int costante = 7;                           // .rodata
int main(int argc, char *argv[]) {
    int locale = argc;                            // stack
    static int statica = 3;                       // .data
    char *testo = "stringa";                      // il puntatore è sullo stack, "stringa" in .rodata
    int *dinamico = malloc(sizeof(int));          // il puntatore è sullo stack, l'int nello heap
    printf("codice   main      %p\n", (void *)main);
    printf("rodata   costante  %p\n", (void *)&costante);
    printf("rodata   \"stringa\" %p\n", (void *)testo);
    printf("data     init      %p\n", (void *)&globale_init);
    printf("data     statica   %p\n", (void *)&statica);
    printf("bss      zero      %p\n", (void *)&globale_zero);
    printf("heap     malloc    %p\n", (void *)dinamico);
    printf("stack    locale    %p\n", (void *)&locale);
    printf("stack    argv[0]   %p\n", (void *)argv[0]);
    free(dinamico);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o memoria memoria.c && ./memoria
codice   main      0x5614cb6991a9
rodata   costante  0x5614cb69a004
rodata   "stringa" 0x5614cb69a008
data     init      0x5614cb69c010
data     statica   0x5614cb69c014
bss      zero      0x5614cb69c01c
heap     malloc    0x5614d7d4e2a0
stack    locale    0x7ffff07089d4
stack    argv[0]   0x7ffff07096af
```

Ordinando gli indirizzi dal più piccolo al più grande si ritrova la mappa della memoria, le stesse righe di `maps` (L5 §7.4):

```
indirizzi bassi
  0x5614cb699xxx   .text      il codice          r-x  (eseguibile, non scrivibile)
  0x5614cb69axxx   .rodata    costanti, stringhe  r--  (sola lettura)
  0x5614cb69cxxx   .data/.bss globali e statiche  rw-  (dati del programma)
  0x5614d7d4exxx   [heap]     malloc              rw-  (cresce verso l'alto)
       ...         librerie   libc, loader        (mappate dal dynamic loader)
  0x7ffff0708xxx   [stack]    variabili locali    rw-  (cresce verso il basso)
indirizzi alti
```

Le cose da fissare. **Codice, costanti e dati** stanno in indirizzi "bassi" (su un PIE, `0x55...`/`0x56...`): sono le sezioni dell'ELF (§2.6), mappate in memoria al caricamento, con i permessi dell'ELF. Il **codice** è `r-x`: eseguibile ma non scrivibile, così un attaccante non può riscriverlo (è la protezione NX/W^X, Modulo 4). Lo **heap** (§9) sta subito dopo i dati e cresce verso indirizzi più alti; lo **stack** sta in cima (`0x7fff...`) e cresce verso indirizzi più **bassi**, verso lo heap. Tra i due ci sono le **librerie condivise** (`libc`, il loader) e le regioni mappate con `mmap`.

Due regioni hanno un ruolo centrale negli attacchi, e le rivedrai in continuazione.

**Lo stack** è la regione dove vivono le variabili locali e dove si tiene traccia delle chiamate di funzione. A ogni chiamata, il processore spinge sullo stack un *frame* (record di attivazione): l'**indirizzo di ritorno** (dove riprendere quando la funzione finisce), i parametri non passati nei registri, le variabili locali, il *canary* se attivo (§2.7). Quando la funzione ritorna, il frame viene rimosso e l'esecuzione riprende dall'indirizzo di ritorno. Il punto cruciale, che hai già intravisto in `overflow.c`: le variabili locali e l'indirizzo di ritorno stanno nello **stesso** stack, a pochi byte di distanza. Un array locale riempito oltre la sua dimensione scrive verso l'indirizzo di ritorno, e chi controlla ciò che viene scritto lì controlla dove il programma salterà. È lo *stack buffer overflow*, l'attacco fondativo del Modulo 4 (lo vedrai "da dentro" con `gdb` nel §11).

**Lo heap** è la regione della memoria dinamica, gestita da `malloc`/`free` (§9). A differenza dello stack, cresce e si frammenta in modo controllato dal programma, e la sua struttura interna (i *chunk*, le liste di blocchi liberi) è a sua volta bersaglio di una famiglia di attacchi (lo *heap exploitation*, più avanti nel corso).

Gli indirizzi dello stack, dello heap e delle librerie **cambiano a ogni esecuzione**: è l'ASLR (*Address Space Layout Randomization*), la protezione che hai già osservato nella Lezione 8 (Esercizio 7), dove l'indirizzo di `main` era diverso ogni volta ma finiva con le stesse tre cifre. È il motivo per cui, in un attacco, spesso il primo passo è far **trapelare** un indirizzo (un *leak*): conoscerne uno permette di calcolare tutti gli altri della stessa regione, perché le distanze interne restano fisse.

## 9. La memoria dinamica: `malloc` e `free`

### 9.1 Le quattro funzioni

Le variabili locali spariscono alla fine della funzione, e la loro dimensione è fissata alla compilazione. Quando serve memoria che **sopravvive** alla funzione, o la cui dimensione si sa solo durante l'esecuzione, si usa lo **heap**, con quattro funzioni di `<stdlib.h>`:

- **`void *malloc(size_t n)`** riserva `n` byte e restituisce un puntatore al loro inizio, oppure `NULL` se non c'è abbastanza memoria. Il contenuto è **indeterminato** (byte a caso).
- **`void *calloc(size_t num, size_t dim)`** riserva `num * dim` byte, **azzerati**, e, a differenza di `malloc(num * dim)`, controlla che il prodotto non vada in overflow (§4.5): è la scelta giusta per un array di cui l'utente fornisce il numero di elementi.
- **`void *realloc(void *p, size_t n)`** cambia la dimensione del blocco puntato da `p` a `n` byte, conservandone il contenuto; può **spostare** il blocco (e allora restituisce un indirizzo diverso e libera il vecchio), quindi il valore restituito va sempre riassegnato, ma a una variabile **nuova** (se `realloc` fallisce restituisce `NULL` senza liberare il vecchio blocco, che altrimenti si perderebbe).
- **`void free(void *p)`** restituisce al sistema il blocco puntato da `p`, che deve essere **esattamente** un indirizzo ricevuto da `malloc`/`calloc`/`realloc` e non ancora liberato. `free(NULL)` non fa niente (è lecito).

La regola d'oro: **ogni `malloc` ha un `free`**, uno solo, e dopo il `free` quel puntatore non si usa più. Un array dinamico che cresce da sé (il modo idiomatico, e il motore delle liste e dei dizionari di Python sotto il cofano):

```c
// dinamica.c — un array che cresce quanto serve
#include <stdio.h>
#include <stdlib.h>
int main(void) {
    size_t cap = 2, n = 0;
    int *v = malloc(cap * sizeof *v);             // sizeof *v = sizeof(int), indipendente dal tipo
    if (!v) { perror("malloc"); return 1; }
    for (int x; scanf("%d", &x) == 1; ) {
        if (n == cap) {
            cap *= 2;
            int *nuovo = realloc(v, cap * sizeof *v);
            if (!nuovo) { free(v); perror("realloc"); return 1; }
            v = nuovo;                            // realloc può spostare il blocco
        }
        v[n++] = x;
    }
    long somma = 0;
    for (size_t i = 0; i < n; i++) somma += v[i];
    printf("%zu numeri, somma %ld, capacità finale %zu\n", n, somma, cap);
    free(v);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o dinamica dinamica.c && echo "3 1 4 1 5 9 2 6" | ./dinamica
8 numeri, somma 31, capacità finale 8
```

Due idiomi da imparare qui. `sizeof *v` invece di `sizeof(int)`: si legge "la dimensione di ciò che `v` punta", e resta corretto anche se cambi il tipo di `v`; raddoppiare la capacità quando è piena (`cap *= 2`) rende l'inserimento di *n* elementi costoso in media come *n* operazioni, non *n*² (è così che crescono le liste di Python). `perror(msg)` stampa `msg` seguito dal messaggio corrispondente a `errno` (§11.2).

### 9.2 I quattro errori classici

Gli errori della memoria dinamica sono quattro, e sono vulnerabilità con un numero CWE ciascuna. Li mostriamo nella loro forma minima; nel §9.3 li scoviamo con lo strumento giusto.

1. **Memory leak** (CWE-401): un `malloc` senza `free`. Il blocco resta riservato ma irraggiungibile. In un programma che gira a lungo (un server), i leak lo fanno crescere finché esaurisce la memoria.

```c
char *p = malloc(100);
/* ... uso p ... */
return 0;                 // dimenticato free(p): 100 byte persi
```

2. **Use-after-free** (CWE-416): usare un blocco dopo averlo liberato. La memoria può essere già stata riassegnata a un altro `malloc`, e la scrittura corrompe dati altrui; è una delle vulnerabilità più sfruttate nei browser e nei kernel.

```c
char *p = malloc(8);
free(p);
p[0] = 'x';               // use-after-free
```

3. **Double free** (CWE-415): liberare due volte lo stesso blocco. Corrompe le strutture interne dell'allocatore, e con esse si costruiscono attacchi allo heap.

```c
free(p);
free(p);                  // double free
```

4. **Off-by-one / heap overflow** (CWE-787, CWE-193): scrivere un byte (o più) oltre la fine del blocco. L'errore "di uno" più comune è dimenticare lo spazio per il terminatore:

```c
char *p = malloc(strlen(s));        // manca +1 per il '\0'
strcpy(p, s);                       // scrive un byte oltre la fine
```

A questi si aggiungono l'uso di memoria **non inizializzata** (CWE-457, i byte casuali di `malloc`, che possono far trapelare dati o decidere a caso un ramo del programma) e il passaggio a `free` di un puntatore che non viene da `malloc`.

### 9.3 Trovarli: AddressSanitizer e Valgrind

Questi errori spesso **non** fanno crollare subito il programma: la memoria "sbagliata" è comunque mappata, e il programma continua con dati corrotti, crollando (o peggio, dando un risultato errato) molto più tardi e altrove. Per questo servono strumenti che controllino ogni accesso.

**AddressSanitizer (ASan)** si attiva alla compilazione con `-fsanitize=address` (e conviene `-g` per avere righe e nomi). Strumenta il programma perché ogni accesso alla memoria sia verificato; quando trova un errore, stampa il tipo, l'indirizzo, e lo *stack trace* del punto in cui è avvenuto e di dove il blocco era stato allocato e liberato. Rallenta il programma di circa due volte, ed è lo strumento che useresti durante lo sviluppo e nei *fuzzer*. Sui quattro bug:

```
$ gcc -g -fsanitize=address -o b b.c     # b.c: strcpy(malloc(8), "0123456789")
b.c:6:3: warning: '__builtin_memcpy' writing 11 bytes into a region of size 8 overflows the destination [-Wstringop-overflow=]
$ ./b
==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x502000000018 ...
SUMMARY: AddressSanitizer: heap-buffer-overflow ... in memcpy

# use-after-free:  ==ERROR: AddressSanitizer: heap-use-after-free ... in main
# double free:     ==ERROR: AddressSanitizer: attempting double-free ...
# leak (a fine programma): ==ERROR: LeakSanitizer: detected memory leaks
#                          SUMMARY: AddressSanitizer: 8 byte(s) leaked in 1 allocation(s).
```

(Nel caso del *buffer overflow*, GCC lo segnala **già alla compilazione** con `-Wstringop-overflow`, perché la lunghezza della stringa letterale è nota: un altro caso in cui l'avviso del compilatore è il bug.)

**Valgrind** fa un lavoro simile **senza ricompilare**: esegue il binario su una CPU simulata e controlla ogni accesso. È più lento (10–30 volte), ma funziona su qualunque eseguibile, anche quando non hai il sorgente, e trova anche l'uso di memoria **non inizializzata**, che ASan non vede:

```
$ gcc -g -o vg vg.c            # vg.c: a=malloc(4 int); a[4]=7; return malloc(8)[0];
$ valgrind -q ./vg
==vg== Invalid write of size 4                       <- a[4], fuori dai limiti
==vg== Syscall param exit_group(status) contains uninitialised byte(s)  <- b[0] non inizializzato
```

Nelle sfide e nel lavoro reale, la regola è: compila sempre con `-Wall -Wextra`, e quando qualcosa si comporta in modo strano, ricompila con `-fsanitize=address,undefined` o lancia sotto Valgrind **prima** di passare ore con il debugger. Metà dei bug di memoria si trova così in un minuto.

# Parte IV — Il C e il sistema

## 10. Le chiamate di sistema

### 10.1 `stdio` contro le chiamate di sistema

Finora per leggere e scrivere abbiamo usato `printf`, `fgets`, `fopen`: sono funzioni della **libreria C**, che aggiungono un **buffer** (L4 §3) sopra i veri canali di comunicazione con il kernel. Sotto di esse ci sono le **chiamate di sistema** (L5 §2): `open`, `read`, `write`, `close`, che lavorano su **descrittori** (interi, L4 §1), senza buffer, e sono l'unico modo in cui un programma chiede un servizio al kernel. La libreria `stdio` non fa altro che chiamare queste, raggruppando tante piccole `printf` in poche `write` grandi.

| | `<stdio.h>` (libreria C) | chiamate di sistema (`<unistd.h>`, `<fcntl.h>`) |
|---|---|---|
| Aprire | `FILE *fopen(nome, modo)` | `int open(nome, flag, [modo])` |
| Leggere | `fread`, `fgets`, `fscanf`, `getchar` | `ssize_t read(fd, buf, n)` |
| Scrivere | `fwrite`, `fprintf`, `fputs`, `putchar` | `ssize_t write(fd, buf, n)` |
| Chiudere | `int fclose(FILE *)` | `int close(fd)` |
| Identità | un puntatore `FILE *` | un intero, il descrittore |
| Buffer | sì (L4 §3) | no: ogni chiamata parla col kernel |

Quale usare? `stdio` per il testo e quando il buffering aiuta (molte piccole scritture); le chiamate di sistema quando vuoi il **controllo esatto** di quanti byte entrano ed escono e quando (dati binari, rete, il momento preciso di una scrittura), ed è quello che fa pwntools (L8) e che farai nelle sfide. Ed è anche la ragione dei problemi di buffering della Lezione 8: `printf` mette i dati in un buffer, e finché non lo svuota, `write` (e quindi la pipe o il socket) non vede niente.

### 10.2 `open`, `read`, `write`, `close` ed `errno`

Un `cp` minimale, scritto con le sole chiamate di sistema, mostra l'uso corretto di tutte e quattro e il trattamento degli errori:

```c
// copia.c — copiare un file con le chiamate di sistema, senza stdio
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
    if (argc != 3) { fprintf(stderr, "uso: %s sorgente destinazione\n", argv[0]); return 2; }
    int in = open(argv[1], O_RDONLY);
    if (in < 0) { perror(argv[1]); return 1; }
    int out = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (out < 0) { perror(argv[2]); close(in); return 1; }
    char buf[4096];
    ssize_t letti;
    while ((letti = read(in, buf, sizeof buf)) > 0) {
        ssize_t scritti = 0;
        while (scritti < letti) {                 // write può scrivere meno del richiesto
            ssize_t k = write(out, buf + scritti, letti - scritti);
            if (k < 0) { perror("write"); return 1; }
            scritti += k;
        }
    }
    if (letti < 0) { perror("read"); return 1; }
    close(in); close(out);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o copia copia.c && ./copia src.txt dst.txt && diff src.txt dst.txt && echo ok
ok
$ ./copia /non/esiste x; echo "rc=$?"
/non/esiste: No such file or directory
rc=1
$ strace -e trace=openat,read,write,close ./copia src.txt dst2.txt
openat(AT_FDCWD, "src.txt", O_RDONLY)   = 3
openat(AT_FDCWD, "dst2.txt", O_WRONLY|O_CREAT|O_TRUNC, 0644) = 4
read(3, "riga uno\nriga due\n", 4096)   = 18
write(4, "riga uno\nriga due\n", 18)    = 18
read(3, "", 4096)                       = 0
```

I dettagli che contano, tutti verificabili con `strace` (L5):
- **`open`** restituisce il descrittore più piccolo libero (3, perché 0, 1, 2 sono i flussi standard, L4 §1) o **−1** in caso di errore. I flag: `O_RDONLY`, `O_WRONLY`, `O_RDWR`; combinati con `|`, `O_CREAT` (crea se non esiste; allora serve il terzo argomento, i permessi, filtrati dalla `umask`, L6), `O_TRUNC` (azzera), `O_APPEND` (scrive in coda).
- **`read(fd, buf, n)`** legge **al massimo** `n` byte e restituisce quanti ne ha letti davvero: può essere meno di `n` (è arrivato meno, o è una pipe o un socket), **0** alla fine del file (EOF), **−1** per errore. È la stessa semantica del `recv` dei socket (L8 §6.2), ed è il motivo per cui si legge sempre in un ciclo.
- **`write(fd, buf, n)`** scrive **al massimo** `n` byte e restituisce quanti ne ha scritti: anche la scrittura può essere parziale (il ciclo interno la completa). Scrivere su una pipe chiusa dà `SIGPIPE`/`EPIPE` (L4 §4.2).
- **`close(fd)`** rilascia il descrittore. I descrittori sono una risorsa limitata: un server che non chiude ciò che apre li esaurisce (CWE-775).

**`errno`** è una variabile globale (per thread) di `<errno.h>` in cui le chiamate di sistema scrivono il **codice** dell'ultimo errore, quando segnalano −1. Non va controllata senza prima aver visto un fallimento (una chiamata riuscita non la azzera). I valori hanno nomi (`ENOENT` file non trovato, `EACCES` permesso negato, `EBADF` descrittore non valido): `perror("msg")` e `strerror(errno)` li traducono nel messaggio leggibile. È il meccanismo di errore del C a basso livello, l'equivalente delle eccezioni di Python (L8 §2.6) ma da controllare a mano a ogni chiamata.

Esistono molte altre chiamate di sistema, che incontrerai lungo il corso: `lseek` (spostarsi in un file), `stat`/`fstat` (le informazioni di un file, L2), `dup`/`dup2` (duplicare un descrittore, L4 §2), `fork`/`execve`/`wait` (i processi, L5 §4), `mmap` (mappare memoria o file), `socket`/`connect`/`recv`/`send` (la rete, Lezione 10). `strace` (L5) mostra, per qualunque programma, esattamente quali chiama e con quali argomenti: è il modo più diretto di capire che cosa fa un binario rispetto al mondo esterno, senza leggerne il codice.

## 11. `gdb`: guardare un programma mentre gira

### 11.1 A che cosa serve

`gdb` (il *GNU Debugger*) esegue un programma sotto il tuo controllo: lo ferma dove vuoi, ti fa leggere e cambiare variabili, memoria e registri, eseguire una riga per volta, e vedere la **catena delle chiamate** quando qualcosa va storto. Per imparare il C serve a *vedere* ciò che finora abbiamo dedotto (dove stanno le variabili, come cambiano); per il *reverse engineering* e il *pwn* (Moduli 3 e 4) è lo strumento principale, perché funziona anche **senza il sorgente**, sul solo codice macchina. Compila con **`-g`** per avere nomi di variabili, tipi e numeri di riga; con `-O0` perché il codice segua il sorgente riga per riga.

### 11.2 I comandi essenziali

| Comando | Abbr. | Effetto |
|---|---|---|
| `run [argomenti]` | `r` | avvia il programma |
| `break posto` | `b` | ferma a una funzione (`b main`), una riga (`b file.c:12`), un indirizzo (`b *0x...`) |
| `continue` | `c` | riprende fino al prossimo *breakpoint* |
| `next` | `n` | esegue la riga corrente, **senza** entrare nelle funzioni chiamate |
| `step` | `s` | esegue la riga, **entrando** nelle funzioni |
| `finish` | | esegue fino al ritorno dalla funzione corrente |
| `print espr` | `p` | stampa una variabile o un'espressione (`p n`, `p a[2]`, `p/x n` in esadecimale) |
| `x/FMT indirizzo` | | esamina la memoria (`x/8xb p` = 8 byte esadecimali, `x/s p` = stringa, `x/4i $pc` = 4 istruzioni) |
| `info args` / `info locals` | | gli argomenti e le variabili locali della funzione corrente |
| `info registers` | `i r` | i registri (`i r rdi rsi`) |
| `backtrace` | `bt` | la catena delle chiamate (chi ha chiamato chi) |
| `list` | `l` | mostra il sorgente intorno al punto corrente |

Si lancia `gdb ./programma` e si lavora interattivamente; per gli esempi qui usiamo la forma non interattiva `gdb -batch -ex 'comando' ...`, che esegue i comandi e esce.

### 11.3 Seguire un programma passo per passo

Prendiamo un fattoriale e fermiamoci dentro la funzione:

```c
// fattoriale.c — per imparare gdb
#include <stdio.h>
#include <stdlib.h>
long fattoriale(int n) {
    long r = 1;
    for (int i = 2; i <= n; i++)
        r *= i;
    return r;
}
int main(int argc, char *argv[]) {
    int n = argc > 1 ? atoi(argv[1]) : 5;
    long f = fattoriale(n);
    printf("%d! = %ld\n", n, f);
    return 0;
}
```

```
$ gcc -g -O0 -o fattoriale fattoriale.c
$ gdb -q -batch -ex 'break fattoriale' -ex 'run 5' -ex 'backtrace' \
      -ex 'info args' -ex 'next' -ex 'next' -ex 'print i' -ex 'print r' ./fattoriale
Breakpoint 1, fattoriale (n=5) at fattoriale.c:5
5	    long r = 1;
#0  fattoriale (n=5) at fattoriale.c:5
#1  0x...e8 in main (argc=2, argv=0x7fffffffadf8) at fattoriale.c:12
n = 5
6	    for (int i = 2; i <= n; i++)
7	        r *= i;
$1 = 2
$2 = 2
```

Il *breakpoint* ferma il programma all'ingresso di `fattoriale`, prima di eseguirne la prima riga. `backtrace` mostra che siamo dentro `fattoriale`, chiamata da `main` alla riga 12. `info args` dà `n = 5`. `next` esegue una riga per volta, e dopo due `next` siamo nel corpo del ciclo, con `i == 2` e `r == 2`. Potresti cambiare un valore (`set var n = 10`) e vedere il programma proseguire con quello: è così che si saltano i controlli o si forza un ramo, durante l'analisi di un binario.

### 11.4 Vedere un overflow da dentro

Ecco il collegamento con il Modulo 4. Prendiamo una funzione con lo stesso difetto di `overflow.c`, ma dove il buffer è vicino all'**indirizzo di ritorno**:

```c
// crash.c
#include <stdio.h>
#include <string.h>
void vittima(char *in) {
    char buf[16];
    strcpy(buf, in);
    printf("%s\n", buf);
}
int main(int argc, char *argv[]) {
    vittima(argc > 1 ? argv[1] : "ciao");
    return 0;
}
```

```
$ gcc -g -O0 -fno-stack-protector -o crash crash.c
$ gdb -q -batch -ex 'run' -ex 'bt' --args ./crash "$(python3 -c 'print("A"*40)')"
Program received signal SIGSEGV, Segmentation fault.
0x000055555555519a in vittima (in=0x7fffffffb631 'A' <repeats 40 times>) at crash.c:7
7	}
#0  0x000055555555519a in vittima (...) at crash.c:7
#1  0x4141414141414141 in ?? ()
#2  0x4141414141414141 in ?? ()
```

Quaranta `A` in un buffer da 16 hanno invaso lo stack fin oltre l'indirizzo di ritorno di `vittima`, sovrascrivendolo con `0x4141414141414141` (`AAAAAAAA` in ASCII, L7 §7). Quando `vittima` prova a ritornare, salta a quell'indirizzo, che non è mappato, e il programma riceve `SIGSEGV`. Il `backtrace` lo dice chiaramente: il *frame* chiamante non è più `main`, è `0x4141...`. **Chi controlla i byte che finiscono lì, controlla dove il programma salta**: mettendo al posto delle `A` l'indirizzo di una funzione utile (o di codice iniettato), si dirotta l'esecuzione. Questo è, in una frase, lo *stack buffer overflow*, e tutto il Modulo 4 è dedicato a trasformare questo `SIGSEGV` in un controllo preciso. Per ora ti basti **vederlo**, e riconoscere nel `0x4141...` del backtrace la firma di un overflow.

Con `x` si guarda la memoria direttamente, e con `info registers` i registri, compreso `$pc` (o `$rip`), l'indirizzo della prossima istruzione, e `$sp` (`$rsp`), la cima dello stack:

```
$ gdb -q -batch -ex 'break vittima' -ex 'run ciao' -ex 'x/s in' \
      -ex 'info registers rdi rsi' -ex 'p $rip' --args ./crash ciao
Breakpoint 1, vittima (in=0x7fffffffb655 "ciao") at crash.c:5
0x7fffffffb655:	"ciao"
rdi            0x7fffffffb655      ...          <- primo argomento: il puntatore a "ciao"
rsi            0x7fffffffae08      ...
$1 = (void (*)()) 0x555555555179 <vittima+16>   <- la prossima istruzione
```

`rdi` contiene il primo argomento di `vittima` (il puntatore a `in`), secondo la convenzione di chiamata (§2.3), e `x/s in` segue quel puntatore e stampa la stringa. Questi comandi — fermarsi, guardare i registri e la memoria, seguire un puntatore — sono il mestiere di base del Modulo 3. Qui li hai usati per **capire** un programma di cui avevi il sorgente; là li userai su binari di cui non ce l'hai.

---

# Parte V — La pratica

## 12. Esempi svolti

### Esempio 1 — Fermarsi a ogni fase della compilazione

Riprendiamo `ciao.c` del §2 e seguiamolo attraverso le quattro fasi, fermandoci a ciascuna, per vedere con gli occhi che cosa produce.

```
$ gcc -save-temps -o ciao ciao.c         # conserva ciao.i, ciao.s, ciao.o
$ wc -l ciao.i                           # il preprocessore ha espanso #include
822 ciao.i
$ grep -c '^#' ciao.i                     # i marcatori di riga
118
$ head -3 ciao.s                          # l'assembly
	.file	"ciao.c"
	.text
	.section	.rodata
$ file ciao.o                             # il file oggetto, non ancora eseguibile
ciao.o: ELF 64-bit LSB relocatable, x86-64, ...
$ nm ciao.o                               # i suoi simboli: main definito, printf da risolvere
0000000000000000 T main
                 U printf
$ file ciao                               # l'eseguibile, dopo il linker
ciao: ELF 64-bit LSB pie executable, ... dynamically linked, ...
```

**Che cosa imparare.** Un solo comando, `gcc`, nasconde quattro programmi. Saperli separare serve quando qualcosa va storto: un errore `undefined reference` viene dal linker (fase 4), non dal compilatore; un `#include` che non si trova viene dal preprocessore (fase 1); un avviso `-Wformat` dal compilatore (fase 2). E nel *reverse engineering* lavorerai proprio sui prodotti delle fasi 3 e 4, il codice macchina, con `objdump` e `gdb`.

### Esempio 2 — Leggere un binario che non hai scritto

Nelle sfide *reverse* ti danno un eseguibile e nessun sorgente. Il primo passo non è mai aprirlo con un debugger: è guardarlo con gli strumenti statici, dal più semplice al più complesso. Prendiamo un `misterioso` che chiede una parola d'ordine (compilato da un sorgente che **non** guardi):

```
$ file misterioso
misterioso: ELF 64-bit LSB pie executable, x86-64, dynamically linked, not stripped
$ strings misterioso | grep -vE '^(/|__)' | head
apriti_sesamo
Benvenuto, L9{strings_e_il_primo_sguardo}
uso: ./misterioso PAROLA
No.
$ nm -D misterioso                        # i simboli dinamici: quali funzioni di libreria usa
                 U puts@GLIBC_2.2.5
                 U strcmp@GLIBC_2.34
$ objdump -d misterioso | grep '@plt' | sort -u
    call   1070 <strcmp@plt>
    call   1060 <puts@plt>
```

Già `strings` (L7 §11) ha quasi risolto la sfida: la parola d'ordine `apriti_sesamo` e la flag sono stringhe in chiaro in `.rodata`. `nm -D` dice che il programma usa `strcmp`: confronta la tua parola con qualcosa. Se la flag non fosse in chiaro, il passo dopo è fermarsi sul confronto con `gdb` e leggere i suoi argomenti:

```
$ gdb -q -batch -ex 'break main' -ex 'run prova' -ex 'break strcmp' -ex 'continue' \
      -ex 'x/s $rdi' -ex 'x/s $rsi' misterioso
0x7fffffffb64f:	"prova"                    <- quello che hai scritto tu (primo argomento, rdi)
0x555555556021:	"apriti_sesamo"            <- quello con cui lo confronta (secondo argomento, rsi)
```

(Prima si ferma `break main`, poi si mette il *breakpoint* su `strcmp` e si fa `continue`: così si salta la `strcmp` che il *loader* usa prima di `main`, e ci si ferma su quella del programma.) Leggere `rdi` e `rsi` — il primo e il secondo argomento, per la convenzione di chiamata del §2.3 — rivela il segreto senza conoscerlo. Lo strumento complementare, dove è installato, è **`ltrace`**, che traccia le chiamate di libreria come `strace` traccia le chiamate di sistema (`ltrace ./misterioso prova` mostrerebbe la riga `strcmp("prova", "apriti_sesamo")`). **Che cosa imparare:** l'ordine di un'analisi statica è `file` → `strings` → `nm -D`/`readelf` → `objdump -d` → `gdb`/`ltrace`, dal colpo d'occhio al dettaglio, ed è lo stesso ordine del Modulo 3.

### Esempio 3 — Lo stesso overflow, visto in tre modi

Un errore di memoria si manifesta in modo diverso a seconda di come compili ed esegui. Prendiamo:

```c
// tre.c
#include <stdio.h>
#include <string.h>
int main(void) {
    char buf[8];
    strcpy(buf, "stringa troppo lunga");    // 21 byte in 8
    printf("%s\n", buf);
    return 0;
}
```

- **Il compilatore**, già senza eseguire, con `-O2` (che attiva `_FORTIFY_SOURCE`): `warning: '__builtin___strcpy_chk' writing 21 bytes into a region of size 8`. L'avviso è il bug.
- **AddressSanitizer** (`gcc -g -fsanitize=address`), all'esecuzione: `ERROR: AddressSanitizer: stack-buffer-overflow`, con la riga esatta e lo *stack trace*.
- **`gdb`** con la protezione dello stack attiva (il default): il programma abortisce con `*** stack smashing detected ***` e `SIGABRT`, perché il *canary* (§2.7) è stato sovrascritto; con `-fno-stack-protector`, invece, `gdb` mostra il `SIGSEGV` al ritorno, con l'indirizzo di ritorno corrotto (§11.4).

**Che cosa imparare.** Durante lo sviluppo, compila con `-Wall -Wextra` e, al minimo dubbio, con `-fsanitize=address,undefined`: tre quarti degli errori di memoria si trovano così, subito e con un messaggio chiaro, invece che con ore di debugger su un crash lontano dalla causa.

### Esempio 4 — Simulare i tipi del C (il ponte con la Lezione 7)

Nella Lezione 7 (Esercizio 13) hai imitato in Python i tipi a dimensione fissa del C, con le maschere. Ora hai l'originale. Questo programma mostra l'overflow e il *wraparound* su cui si costruiscono le vulnerabilità di tipo intero (CWE-190):

```c
// tipi.c
#include <stdio.h>
#include <stdint.h>
int main(void) {
    uint8_t u = 255; u++;                         // gira a 0 (definito)
    int8_t  s = 127; s++;                          // -128 (su x86; con segno è UB in generale)
    uint32_t grande = 0xffffffff;
    printf("uint8: 255+1 = %u\n", u);
    printf("int8:  127+1 = %d\n", s);
    printf("uint32 max + 1 = %u\n", grande + 1);
    size_t len = 4; int richiesti = 10;
    if (richiesti - (int)len < 0) puts("controllo con segno: ok");
    size_t quanti = 3; printf("3 * 2GB in size_t: %zu\n", quanti * (size_t)2000000000 * 2);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o tipi tipi.c && ./tipi
uint8: 255+1 = 0
int8:  127+1 = -128
uint32 max + 1 = 0
controllo con segno: ok
3 * 2GB in size_t: 12000000000
```

**Che cosa imparare.** Gli `unsigned` "girano" in modo definito modulo 2ⁿ; i `signed` in overflow sono comportamento indefinito (§4.5). Un calcolo di dimensione (`numero * dimensione_elemento`) fatto in un tipo troppo stretto va in overflow e produce un buffer troppo piccolo: è la ragione di `calloc` (§9.1), e una classe di bug a sé. Quando leggi il sorgente di una sfida, i punti dove un valore controllato dall'utente entra in un calcolo di dimensione sono i primi da guardare.

### Esempio 5 — Un bug di memoria trovato con i sanitizer

Un programma che costruisce una stringa dinamica, con un classico errore "di uno":

```c
// giunta.c — unisce argv in una sola stringa separata da spazi
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[]) {
    size_t tot = 0;
    for (int i = 1; i < argc; i++) {
        tot += strlen(argv[i]);
        if (i < argc - 1) tot += 1;             // uno spazio tra una parola e l'altra
    }
    char *s = malloc(tot);                      // manca +1 per il '\0' finale!
    s[0] = '\0';
    for (int i = 1; i < argc; i++) {
        strcat(s, argv[i]);
        if (i < argc - 1) strcat(s, " ");
    }
    printf("[%s]\n", s);
    free(s);
    return 0;
}
```

Compilato normalmente, spesso "funziona": il byte di troppo cade in memoria che `malloc` aveva arrotondato per eccesso. Sotto AddressSanitizer il bug salta fuori:

```
$ gcc -g -fsanitize=address -o giunta giunta.c && ./giunta uno due tre
==ERROR: AddressSanitizer: heap-buffer-overflow ... WRITE of size 1
    #0 ... in strcat
    ... allocated by thread T0 here: ... in main giunta.c:11
[uno due tre]
```

Il conto `tot` somma le lunghezze delle parole e **un separatore tra una e l'altra** (`n − 1` spazi in tutto), ma dimentica il byte per il `\0` finale: `strcat` scrive esattamente un byte oltre la fine del blocco. La correzione è `malloc(tot + 1)`. **Che cosa imparare:** gli errori "di uno" sulle stringhe sono quasi sempre il terminatore dimenticato; ASan li trova anche quando il programma sembra funzionare, e questo è precisamente il motivo per usarlo.

## 13. Esercizi

Gli esercizi sono in tre livelli. I **★ Base** fissano la toolchain e i tipi: si fanno con `gcc`, `nm`, `readelf` e un interprete di prova. Gli **★★ Intermedio** ti fanno scrivere programmi C corretti e ragionare su puntatori, memoria e chiamate di sistema. Gli **★★★ Sfida** sono analisi di binari e piccoli programmi completi, inclusa la mini-CTF. Compila sempre con `-Wall -Wextra`; dove un esercizio parla di un "binario della sfida", trattalo come una scatola nera e non leggerne il sorgente. Le soluzioni, provate con gcc 13.3, gdb 15 e glibc 2.39, sono in `Soluzioni.md`.

### ★ Base

**1. Le quattro fasi.** Prendi `ciao.c` del §2. (a) Genera e guarda i quattro prodotti con `gcc -save-temps`. Quante righe ha `ciao.i`, e perché così tante? (b) Nell'assembly `ciao.s`, trova la stringa `"Ciao, mondo!\n"` e la chiamata a `printf`: in quale sezione sta la stringa? (c) Con `nm ciao.o`, quali simboli sono `T` e quali `U`, e che cosa significa? (d) Dopo il link, con `nm ciao | grep ' T '`, quali funzioni ci sono **oltre** a `main`, e da dove vengono (§2.5)? (e) Compila `printf("Ciao, mondo!\n")` senza argomenti e, con `nm`, verifica che la `printf` è diventata `puts`: perché?

**2. Prevedi i tipi.** Senza compilare, scrivi il valore di ciascuna espressione; poi verifica con un breve programma e, per ogni errore, indica la regola del §4. Tutte le variabili sono sul sistema LP64.

```c
sizeof(int), sizeof(long), sizeof(char *), sizeof('A'), sizeof("ciao")    // (a)
(unsigned char)300                                                        // (b)
-1 < 1u                                                                   // (c) con un commento
(char)200                   // su x86-64, dove char ha segno                // (d)
250 + (unsigned char)10     // di che tipo è il risultato, e quanto vale?    // (e)
7 / 2, -7 / 2, -7 % 2, 7 % -2                                             // (f)
1 << 31     // con int a 32 bit                                            // (g) tranello
(size_t)0 - 1                                                             // (h)
```

**3. Leggere un ELF.** Compila un programma qualunque (`gcc -o prog prog.c`) e un secondo con `-static`. Con `file`, `readelf -h`, `readelf -S`, `readelf -l`, `ldd`: (a) qual è il tipo (`DYN`/`EXEC`) e il punto d'ingresso dei due? (b) elenca le sezioni `.text`, `.rodata`, `.data`, `.bss` e i loro flag: quale è eseguibile ma non scrivibile, e quale il contrario? (c) quali librerie carica quello dinamico, e perché quello statico "is not a dynamic executable"? (d) fai `strip` del binario dinamico: di quanto cala, e che cosa non trova più `nm`? Che cosa trova ancora `nm -D`, e perché serve al *loader*?

**4. Un Makefile.** Riprendi il programma su più file del §2.8 (`conta.c`, `conta.h`, `principale.c`). (a) Scrivi il `Makefile` e verifica che `make` due volte di fila ricompili la seconda volta **niente**. (b) `touch conta.c`: che cosa ricompila `make`? E dopo `touch conta.h`? Perché la differenza? (c) Aggiungi un bersaglio `pulisci` e uno che compili con `-fsanitize=address`. (d) Che cosa stampa `make` se togli la **tabulazione** davanti a una ricetta e metti spazi?

**5. `errno` e i codici di uscita.** Scrivi `apri.c` che prova ad aprire con `open` il file passato come argomento in sola lettura, e: se riesce, stampa il descrittore e lo chiude; se fallisce, stampa il messaggio d'errore con `perror` ed esce con codice 1. Provalo su un file che esiste, uno che non esiste, uno senza permesso di lettura (creane uno con `chmod 000`, L6) e una directory. Per ciascuno, che `errno` (nome simbolico) ottieni? Confronta con `strace -e trace=openat ./apri FILE`.

### ★★ Intermedio

**6. Somma con controllo dell'overflow.** Riprendi `leggi.c` del §3.3, che ha il difetto di calcolare `2 * n` senza controllare l'overflow. (a) Scrivi una funzione `int somma_sicura(long a, long b, long *risultato)` che calcola `a + b`, scrive il risultato tramite il puntatore e restituisce 0, oppure restituisce −1 **senza** scrivere se la somma andrebbe in overflow di `long`. Scrivi il controllo **prima** dell'operazione, con `LONG_MAX`/`LONG_MIN` di `<limits.h>` (non `if (a + b < a)`, che è UB, §4.5). (b) Riscrivila con `__builtin_add_overflow`. (c) Verifica entrambe su `LONG_MAX + 1`, `LONG_MIN - 1`, `3 + 4`, `-5 + 2`. (d) Perché `if (a + b < a)` non è un controllo valido per `long` con segno, mentre lo sarebbe per `unsigned long`?

**7. Il tuo `strlen` e il tuo `strcpy`.** Scrivi, con l'aritmetica dei puntatori (non con gli indici): (a) `size_t mia_strlen(const char *s)`; (b) `char *mia_strcpy(char *dst, const char *src)` che copia `src` in `dst` (terminatore compreso) e restituisce `dst`; (c) `char *mia_strncpy(char *dst, const char *src, size_t n)` che copia al massimo `n` byte e garantisce **sempre** il terminatore (a differenza di `strncpy` dello standard: spiega la differenza). (d) Scrivi una funzione `giunta(char **parti, int n)` che unisce `n` stringhe separate da `-` in una nuova stringa allocata con `malloc` della dimensione **esatta** (calcolala), e la restituisce; chi la chiama fa `free`. Provala e verificala con `-fsanitize=address`.

**8. La memoria di un programma.** Scrivi un programma con: una variabile globale inizializzata, una globale non inizializzata, una `const`, una stringa letterale, una `static` locale, una locale, e un blocco allocato con `malloc`. Stampa l'indirizzo di ciascuna (`%p`). (a) Ordina gli indirizzi e assegna ciascuno alla sua regione (`.text`, `.rodata`, `.data`/`.bss`, heap, stack), confrontando con `cat /proc/self/maps` (fai aspettare il programma con `getchar()` e leggi `/proc/<PID>/maps` in un altro terminale, L5 §7.4). (b) Quali indirizzi cambiano a ogni esecuzione e quali no? Perché (ASLR, PIE)? (c) Prova a scrivere nella stringa letterale (`char *p = "x"; p[0] = 'y';`): che cosa succede, e da quale flag di sezione (§2.6) dipende?

**9. Un array dinamico generico.** Scrivi una piccola struttura `Vettore` (un `int *dati`, un `size_t n` e un `size_t capacita`) e le funzioni `vettore_nuovo`, `vettore_aggiungi` (raddoppia la capacità quando è piena, §9.1), `vettore_get`, `vettore_libera`. (a) Verifica con `-fsanitize=address` che non ci siano *leak* né accessi fuori dai limiti. (b) Che cosa succede, e come lo segnala ASan, se `vettore_aggiungi` dimentica di riassegnare il puntatore dopo `realloc`? (c) Che cosa succede se chiami `vettore_get` con un indice `>= n`? Aggiungi un controllo. (d) Trasformalo in un vettore di `void *` per contenere elementi di qualunque tipo: che cosa cambia nella firma delle funzioni?

**10. `cat` e `wc` con le chiamate di sistema.** (a) Scrivi `mio_cat.c` che copia sullo standard output il contenuto dei file passati come argomenti (o lo standard input se non ce ne sono), usando **solo** `open`, `read`, `write`, `close`, con un buffer di 4096 byte e il ciclo di scrittura completo (`write` può scrivere meno del richiesto, §10.2). (b) Scrivi `mio_wc.c` che conta righe, parole e byte dello standard input, leggendo a blocchi con `read`. (c) Confronta l'output con `cat` e `wc`, e il comportamento con `strace -c` (quante `read`/`write` fa il tuo, quante `cat`?). (d) Che cosa succede se fai `./mio_cat file | head -1` e il file è grande: vedi `SIGPIPE`? Perché (L4 §4.2)?

**11. `gdb` per capire.** Compila con `-g -O0` un programma con una funzione ricorsiva (per esempio Fibonacci `fib(n)`). (a) Mettici un *breakpoint* e, con `run 5`, usa `backtrace` a varie profondità della ricorsione: quanti *frame* vedi al massimo? (b) Con `info args` e `print`, segui il valore di `n` scendendo nella ricorsione. (c) Usa `watch` su una variabile e `continue`: `gdb` si ferma quando cambia. (d) Compila lo stesso programma con `-O2` e riprova: perché ora `gdb` fatica a seguire le righe e certe variabili sono `<optimized out>`? (e) Con `disassemble fib`, confronta la lunghezza del codice a `-O0` e `-O2`.

### ★★★ Sfida

**12. Mini-CTF: la cassaforte.** Esegui `bash setup_sfida.sh`: crea `~/l9_sfida/` con `cassaforte.c`, un `Makefile` e `LEGGIMI.txt`. Compila con `make` e ottieni il binario `cassaforte`. La flag `L9{...}` è in **quattro pezzi**, e vanno recuperati **senza** indovinare la password a tentativi e **senza** leggere `cassaforte.c`:
- **Pezzo 1**: si vede subito con uno strumento della Lezione 7. Quale?
- **Pezzo 2**: viene stampato solo con la password giusta. La password è un numero calcolato dal programma, seguito da una parola: recuperala con `gdb`, fermandoti nella funzione che la controlla e leggendo la variabile locale con cui ti confronta (oppure leggendo la variabile globale `chiave`). Poi lancia `cassaforte` con la password.
- **Pezzo 3**: è offuscato e diventa leggibile solo in memoria, a programma avviato. Fermati con `gdb` **dopo** che è stato decodificato e stampane il contenuto.
- **Pezzo 4**: è stampato da una funzione che `main` **non chiama mai** (codice morto). Trovala con `nm`/`objdump`, e chiamala tu da `gdb` (`call`), oppure salta a essa.

Scrivi, per ogni pezzo, quale strumento hai usato e perché, e ricomponi la flag. (Suggerimento per il pezzo 2: `objdump -d` o `gdb` ti mostrano come `chiave` è calcolata; oppure `break` nella funzione di controllo e `print` della variabile locale `atteso` dopo lo `snprintf`.)

**13. Analisi di un binario sconosciuto.** Prendi un eseguibile che **non** hai scritto (per esempio `/bin/true`, `/bin/ls`, o `misterioso` dell'Esempio 2 compilato da un compagno). (a) Con `file`: è PIE? statico o dinamico? *stripped*? (b) Con `strings | less`: trova messaggi, nomi di file, formati. (c) Con `nm -D` o `readelf --dyn-syms`: quali funzioni di libreria usa? (d) Con `objdump -d | grep '@plt'`: quali chiamate di libreria fa, e che cosa ti dicono sul suo comportamento? (e) Con `ltrace` (se c'è) o `strace`: quali chiamate di libreria e di sistema fa davvero quando gira? (f) Metti in ordine questi strumenti dal "colpo d'occhio" al "dettaglio", e spiega perché è l'ordine giusto per iniziare una sfida *reverse*.

**14. Il buffer e il suo vicino.** Compila `overflow.c` del §7.3 con `-g -O0 -fno-stack-protector`. (a) Con `gdb`, metti un *breakpoint* dopo lo `strcpy` e stampa l'indirizzo di `nome` e di `ammesso` (`p &nome`, `p &ammesso`): quanti byte li separano? (b) Qual è la lunghezza minima dell'input che cambia `ammesso`, e perché proprio quella? (c) Costruisci un input che metta in `ammesso` esattamente il valore 1 (usa `printf` della shell per i byte non stampabili, come nell'esempio). (d) Ricompila **senza** `-fno-stack-protector` (il default) e rifai: che messaggio dà il programma, e perché (§2.7)? (e) Con `gdb`, su un input lungo abbastanza da superare l'indirizzo di ritorno, guarda il `backtrace` dopo il crash: che cosa vedi al posto di `main`, e che cosa significa per il Modulo 4 (§11.4)?

**15. Dal C all'assembly e ritorno.** Scrivi una funzione `int massimo(int a, int b)` che restituisce il più grande. (a) Compilala con `gcc -S -O2 -fno-asynchronous-unwind-tables` e leggi l'assembly: come ha tradotto il confronto (c'è un salto, o un'istruzione `cmov`)? (b) In quali registri arrivano `a` e `b`, e in quale torna il risultato (§2.3)? (c) Scrivi `int fib(int n)` ricorsiva, compilala a `-O0` e a `-O2`, e con `objdump -d` conta le istruzioni: a `-O2` la ricorsione c'è ancora, o il compilatore l'ha trasformata? (d) Senza essere esperto di assembly, individua nell'output di `fib` a `-O0` le istruzioni `call fib`: quante sono, e perché?

### Allenamento

Gli esercizi di questa lezione sono il ponte verso i Moduli 3 (*reverse*) e 4 (*pwn*). Su pwn.college, i moduli *Program Misuse* e *Assembly Crash Course* del percorso introduttivo ti fanno eseguire, leggere e modificare programmi a basso livello; il dojo *Debugging* insegna `gdb` a fondo. Installa `pwndbg` o `gef`, due estensioni di `gdb` nate per le CTF, che mostrano registri, stack e disassembly a ogni passo: le userai in tutto il Modulo 4. Fuori da pwn.college, su picoCTF la categoria *Reverse Engineering* comincia esattamente da qui (un binario, `strings`, `gdb`), e *Binary Exploitation* dai *buffer overflow* del §7.3 e §11.4. La regola: per ogni binario, prima gli strumenti statici (`file`, `strings`, `nm`, `objdump`), poi quelli dinamici (`ltrace`, `strace`, `gdb`), sempre in quest'ordine.

## 14. Domande di autoverifica

1. Quali sono le quattro fasi che `gcc` esegue da `.c` a eseguibile, quale programma le compie, e con quale opzione ti fermi a ciascuna?
2. Che differenza c'è tra un file oggetto (`.o`) e un eseguibile? Che cosa aggiunge il linker?
3. Che cosa fa il preprocessore con `#include` e con `#define`? Perché una macro con parametri va scritta con molte parentesi?
4. Che cosa significano `T` e `U` in `nm`? E la maiuscola contro la minuscola? A che cosa servono `extern` e `static`?
5. Collegamento statico e dinamico: differenze in dimensione e in come parte il programma. Che cos'è il *dynamic loader*? E la GOT/PLT?
6. Che cos'è un eseguibile PIE, e perché i suoi indirizzi cambiano a ogni esecuzione?
7. Quanto occupano `int`, `long`, un puntatore, `size_t` su Linux x86-64 (modello LP64)? E su Windows a 64 bit?
8. Quando si usa `unsigned char`/`uint8_t` invece di `char`? Perché per i byte come dati sempre il primo?
9. Che cosa succede in `-1 < 1u`? E assegnando 300 a un `unsigned char`? Enuncia la promozione intera e le conversioni aritmetiche usuali.
10. Differenza tra overflow di un `unsigned` e di un `signed`. Perché il secondo è pericoloso, e come si scrive un controllo di overflow corretto?
11. Che cos'è il comportamento indefinito? Fai tre esempi che incontrerai spesso. Quali strumenti lo scovano?
12. Che cos'è un puntatore? Che cosa fanno `&` e `*`? Perché `*p = 7` cambia `x` se `p == &x`?
13. Che cosa vuol dire che un array "decade" in un puntatore? Quali due contesti fanno eccezione? Perché una funzione che riceve un array ne ignora la lunghezza?
14. Com'è fatta una stringa C? Dove sta la sua lunghezza? Perché `strcpy`, `strcat`, `gets`, `sprintf` sono pericolose, e con che cosa si sostituiscono?
15. Che cosa succede, in memoria, quando scrivi più caratteri di quanti ne contiene un array locale? Perché questo porta al controllo dell'esecuzione (Modulo 4)?
16. Elenca le regioni dello spazio di indirizzi di un processo, dalle più basse alle più alte, e di' quale variabile vive in ciascuna. In che direzione crescono stack e heap?
17. A che cosa servono `malloc`, `calloc`, `realloc`, `free`? Qual è la regola d'oro? Perché `calloc` per un array di cui l'utente dà il numero di elementi?
18. Nomina i quattro errori classici della memoria dinamica, con il loro nome inglese. Come li trovi con ASan e con Valgrind?
19. Differenza tra `printf`/`fgets` e `read`/`write`. Perché le seconde non hanno buffer? Che cos'è `errno`?
20. Che cosa restituisce `read(fd, buf, n)`? Perché si legge sempre in un ciclo? Che cosa significano 0 e −1?
21. A che cosa serve `gdb`? Che cosa fanno `break`, `run`, `next`/`step`, `print`, `x`, `backtrace`, `info registers`? Perché compilare con `-g -O0`?
22. In un `backtrace` dopo un crash vedi `0x4141414141414141`: che cosa è successo, e perché quell'indirizzo preciso?

## 15. Riepilogo

- Il **C** è compilato, con tipi statici e memoria manuale, e non controlla quasi nulla: è veloce e vicino all'hardware, ed è la lingua del kernel, delle librerie e di quasi tutte le sfide *pwn* e *reverse*. La maggior parte delle vulnerabilità gravi sono errori di memoria del C.
- **La toolchain**: `gcc` è un driver per preprocessore (`-E`), compilatore (`-S`, produce assembly), assemblatore (`-c`, produce un `.o` ELF rilocabile) e linker (produce l'eseguibile). Il **preprocessore** espande `#include` e `#define` come testo. Il **linker** risolve i simboli (`undefined reference`, `multiple definition`) e riloca; collega `libc` da sé, le altre con `-lNOME`.
- L'**ELF** è fatto di sezioni (`.text` codice, `.rodata` costanti, `.data`/`.bss` globali, `.plt`/`.got` per il collegamento dinamico) e segmenti con permessi (`r-x`, `r--`, `rw-`). Gli strumenti: `file`, `strings`, `nm`/`nm -D`, `readelf`, `objdump`, `ldd`, `strip`. Un eseguibile **dinamico** carica `libc` a runtime tramite il *loader*; **PIE** = caricato a un indirizzo casuale (ASLR). Protezioni per default: *stack canary*, NX, PIE, FORTIFY.
- **I tipi**: cinque interi con/senza segno, dimensioni date dal modello (LP64 su Linux: `int` 32, `long` e puntatori 64), `sizeof` le dà; `unsigned char`/`uint8_t` per i byte, `size_t` per le dimensioni, `<stdint.h>` per le dimensioni esatte. Le **conversioni implicite** (promozione intera, "vince il senza segno", troncamento all'assegnamento) sono fonte di bug. L'overflow **unsigned** è modulare e definito, quello **signed** è comportamento indefinito.
- Il **comportamento indefinito** (overflow con segno, accessi fuori dai limiti, puntatori non validi, memoria non inizializzata, `printf` con formato sbagliato) è lo spazio in cui vivono gli attacchi; `-fsanitize=undefined`/`address` e `-Wall -Wextra` lo scovano.
- **Puntatori**: contengono indirizzi; `&` prende l'indirizzo, `*` dereferenzia; l'aritmetica conta in elementi; `NULL` non punta a niente e dereferenziarlo è `SIGSEGV`. Gli **array** decadono in puntatori (eccetto `sizeof` e `&`), non portano con sé la lunghezza, e il C non controlla gli indici.
- Una **stringa C** è un array di `char` terminato da `\0`, senza lunghezza memorizzata. È la fonte dei *buffer overflow*: `strcpy`/`strcat`/`gets`/`sprintf` scrivono senza limiti; si usano le versioni con dimensione (`snprintf`, `fgets`) conoscendo sempre la dimensione della destinazione. Le `struct` raggruppano campi (con *padding* di allineamento).
- Lo **spazio di indirizzi**: codice e dati in basso, heap che cresce verso l'alto, librerie, stack in alto che cresce verso il basso. Lo **stack** tiene variabili locali e indirizzo di ritorno vicini: un overflow di un array locale raggiunge l'indirizzo di ritorno e permette di dirottare l'esecuzione. ASLR rende casuali gli indirizzi, e un *leak* ne rivela uno per calcolare gli altri.
- **Memoria dinamica**: `malloc`/`calloc`/`realloc`/`free`, un `free` per ogni `malloc`. Quattro errori: *memory leak*, *use-after-free*, *double free*, *heap overflow*/*off-by-one*. Si trovano con **AddressSanitizer** (ricompilando) e **Valgrind** (anche senza sorgente).
- **Le chiamate di sistema** `open`/`read`/`write`/`close` lavorano su descrittori, senza buffer: `read` e `write` possono fare meno del richiesto (ciclo), `read` dà 0 a EOF e −1 su errore, con il codice in `errno`. `stdio` è un buffer sopra di esse.
- **`gdb`** esegue un programma sotto controllo (`break`, `run`, `next`/`step`, `print`, `x`, `backtrace`, `info registers`), con `-g -O0`; funziona anche senza sorgente, ed è lo strumento del *reverse* e del *pwn*. Un `0x4141...` in un backtrace è la firma di uno *stack overflow*.
- L'ordine per analizzare un binario: **statico** (`file` → `strings` → `nm`/`readelf` → `objdump`) poi **dinamico** (`ltrace`/`strace` → `gdb`), dal colpo d'occhio al dettaglio.

## 16. Fonti

- **Brian W. Kernighan, Dennis M. Ritchie**, *The C Programming Language*, 2ª ed. (ANSI C), 1988: il "K&R", ancora la migliore introduzione al linguaggio, conciso e preciso.
- **Randal E. Bryant, David R. O'Hallaron**, *Computer Systems: A Programmer's Perspective* (CSAPP), 3ª ed.: cap. 1 (il viaggio di un programma attraverso il sistema), cap. 3.1–3.4 (rappresentazione dei programmi, dal C all'assembly), cap. 7 (**linking**, file oggetto, simboli, rilocazione, librerie statiche e dinamiche), cap. 9.9 (memoria dinamica). È il riferimento principale per §1–2 e §8–9.
- **ISO/IEC 9899** (lo standard C, C17/C23) e la sua appendice J.2 (l'elenco dei comportamenti indefiniti); in pratica, la documentazione di glibc (`man` sezioni 2 e 3) e la *C reference* di cppreference.com.
- **Documentazione degli strumenti**: `man gcc` (in particolare le opzioni `-W`, `-O`, `-f`), `info make` (il *GNU Make Manual*), il *Debugging with GDB* (sourceware.org/gdb/documentation), le pagine `man` di `ld`, `nm`, `objdump`, `readelf`, `strings`, `valgrind`; la documentazione di AddressSanitizer (github.com/google/sanitizers).
- **John R. Levine**, *Linkers and Loaders*: per chi vuole capire a fondo il §2.5–2.6.
- **Matt Godbolt, Compiler Explorer** (godbolt.org): per vedere, riga per riga e nel browser, in che assembly GCC traduce un pezzo di C, a vari livelli di ottimizzazione. Insostituibile per il §2.3 e il Modulo 3.
- **pwn.college**, CSE 365 e il percorso *Program Security*: i moduli *Program Misuse*, *Assembly Crash Course*, *Debugging*; la trascrizione 037 (*Syllabus and Program Security*) per l'introduzione.
- **MITRE CWE**: CWE-787 (*out-of-bounds write*) e CWE-125 (lettura), CWE-120/121/122 (*buffer overflow* classico, stack, heap), CWE-416 (*use-after-free*), CWE-415 (*double free*), CWE-401 (*memory leak*), CWE-457 (memoria non inizializzata), CWE-476 (dereferenziazione di NULL), CWE-190/195 (overflow interi e conversione di segno), CWE-134 (stringa di formato), CWE-242/676 (funzioni pericolose come `gets`). Sono il catalogo di ciò che studierai nel Modulo 4.

## 17. Prossima lezione

**Lezione 10 — Reti e comunicazione**: il modello TCP/IP, indirizzi IP e porte, TCP e UDP, i socket visti dal C e dalla riga di comando con `nc`, il DNS, HTTP e `curl`, e come si cattura e si legge il traffico con `tcpdump` e Wireshark. È l'ultima lezione del Modulo 1, quella che chiude il cerchio: nella Lezione 8 hai parlato con un servizio di rete tramite pwntools senza chiederti che cosa ci fosse sotto il socket; nella 9 hai visto come un programma C apre un descrittore e fa `read` e `write`; nella 10 quel descrittore diventa una connessione di rete, e capirai che cosa viaggia davvero sul filo. Dopo la Lezione 10 c'è la **simulazione di gara**, che mette insieme tutto il modulo.
