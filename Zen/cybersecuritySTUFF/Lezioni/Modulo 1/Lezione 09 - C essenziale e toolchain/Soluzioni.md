# Modulo 1 — Lezione 9: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Tutto è stato provato con gcc 13.3, GNU gdb 15.1, glibc 2.39 e Valgrind 3.22 su Linux x86-64. Gli indirizzi e alcuni numeri (offset, righe dei messaggi) cambiano da una macchina all'altra; le idee no. I riferimenti `§` rimandano a `Lezione.md`. Compila sempre con `-Wall -Wextra`.

## ★ Base

**1.**
(a) `ciao.i` ha circa **822 righe**: le otto righe del sorgente più il contenuto di `/usr/include/stdio.h` e di tutti gli header che a sua volta include, quasi tutto dichiarazioni (`extern int printf(...)`). (b) La stringa `"Ciao, mondo!\n"` sta nella sezione **`.rodata`** (etichetta `.LC1`); subito sopra, `call printf@PLT`. (c) `nm ciao.o` dà `T main` (definito, in `.text`) e `U printf` (**undefined**: usato, ma da risolvere altrove). (d) Dopo il link, `nm ciao` mostra, oltre a `main`, i simboli aggiunti dalla libreria C: `_start` (il vero punto d'ingresso, §2.5), `_init`, `_fini`, `register_tm_clones`, `frame_dummy`, e `U __libc_start_main`; `_start` chiama `__libc_start_main`, che inizializza la libreria e poi chiama `main`. (e) GCC riconosce che `printf` con una sola stringa costante terminata da `\n` e senza conversioni equivale a `puts`, che è più veloce, e la sostituisce (già a `-O0`): `nm` mostra `U puts`, non `U printf`.

**2.**
(a) `4, 8, 8, 4, 5`. `sizeof('A')` è **4** perché in C un carattere tra apici è un `int` (§4.1); `sizeof("ciao")` è **5**, l'array con il terminatore (§7.2), non la lunghezza.
(b) `(unsigned char)300` = **44** (300 − 256, troncamento modulo 256, §4.3).
(c) `-1 < 1u` è **falso (0)**: la conversione aritmetica usuale porta `-1` a `unsigned`, dove vale 4294967295 (§4.3). GCC avvisa con `-Wextra`.
(d) `(char)200` = **−56** su x86-64, dove `char` ha segno (200 − 256).
(e) Il risultato è un **`int`** e vale **260**: la promozione intera porta `unsigned char` a `int` prima della somma (§4.3), e il risultato non viene rimesso in un `unsigned char`.
(f) `3, -3, -1, 1`: la divisione intera del C tronca **verso zero** (−7/2 = −3, non −4 come il `//` di Python), e il resto ha il segno del **dividendo** (`-7 % 2` = −1, `7 % -2` = 1).
(g) Tranello: `1 << 31` con `1` di tipo `int` (32 bit) sposta un 1 nel bit di segno, ed è **comportamento indefinito** (§4.4). Si scrive `1u << 31` o `(unsigned)1 << 31` per ottenere 2147483648.
(h) `(size_t)0 - 1` = **18446744073709551615** (2⁶⁴ − 1): `size_t` è senza segno e "gira" (§4.3, §4.5). È il bug della riga (8) di `conversioni.c`.

**3.**
(a) Il dinamico è `DYN` (PIE), il punto d'ingresso è un piccolo offset (es. 0x1060, l'indirizzo di `_start`); lo statico è `EXEC`, con un punto d'ingresso assoluto alto (es. 0x401...). (b) `.text` ha i flag `AX` (alloc + eseguibile, **non** scrivibile), `.rodata` `A` (sola lettura), `.data`/`.bss` `WA` (scrivibili, non eseguibili): è la regola W^X/NX (§2.6). (c) `ldd` sul dinamico mostra `linux-vdso`, `libc.so.6` e il *loader* `ld-linux-x86-64.so.2`; sullo statico dice `not a dynamic executable` perché il codice di libreria è già dentro (50 volte più grande, §2.5). (d) `strip` toglie `.symtab`: il binario cala di qualche KB e `nm` dice `no symbols`; `nm -D` mostra ancora i simboli **dinamici** (`puts`, `__libc_start_main`), che servono al *loader* per risolvere le funzioni di libreria e non si possono togliere.

**4.** Il `Makefile` è quello del §2.8.
(a) Il secondo `make` dice `make: 'vocali' is up to date` e non ricompila niente: nessun prerequisito è più recente del bersaglio. (b) `touch conta.c` ricompila **solo** `conta.o` (e poi rilinka); `touch conta.h` ricompila **entrambi** i `.o`, perché tutti e due lo includono e dipendono da esso: è il motivo per cui le dipendenze dagli header vanno dichiarate. (c) Si aggiunge `pulisci` (già presente) e, per esempio, `vocali-asan: CFLAGS += -fsanitize=address` con la stessa regola, o un bersaglio separato. (d) Con gli spazi al posto della tabulazione, `make` si ferma con `*** missing separator. Stop.`: le ricette **devono** cominciare con una tabulazione.

**5.**

```c
// apri.c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
int main(int argc, char *argv[]) {
    if (argc != 2) { fprintf(stderr, "uso: %s FILE\n", argv[0]); return 2; }
    int fd = open(argv[1], O_RDONLY);
    if (fd < 0) { perror(argv[1]); return 1; }
    printf("aperto, fd = %d\n", fd);
    close(fd);
    return 0;
}
```

File esistente: `aperto, fd = 3`. File inesistente: `errno == ENOENT` (`No such file or directory`). File `chmod 000` (da utente non privilegiato): `errno == EACCES` (`Permission denied`); se provi da root, l'apertura riesce lo stesso, perché root salta i controlli di permesso (L6). Directory aperta `O_RDONLY`: **riesce** (aprire una directory in lettura è lecito; è `read` su di essa a dare `EISDIR`). `strace -e trace=openat ./apri FILE` mostra la `openat` con il flag e il valore di ritorno (il descrittore o `-1 ENOENT`).

## ★★ Intermedio

**6.**

```c
#include <limits.h>
int somma_sicura(long a, long b, long *r) {
    if (b > 0 && a > LONG_MAX - b) return -1;     // controllo PRIMA dell'operazione
    if (b < 0 && a < LONG_MIN - b) return -1;
    *r = a + b;
    return 0;
}
int somma_builtin(long a, long b, long *r) {
    return __builtin_add_overflow(a, b, r) ? -1 : 0;
}
```

```
LONG_MAX + 1: sicura=-1 builtin=-1     (overflow rilevato, niente scritto)
LONG_MIN + -1: sicura=-1 builtin=-1
3 + 4: 0 (7)
-5 + 2: 0 (-3)
```

(a)–(b) Entrambe rilevano l'overflow e **non** scrivono il risultato in quel caso. (d) `if (a + b < a)` calcola `a + b`: se va in overflow con segno è **comportamento indefinito** (§4.5), e il compilatore può eliminare il controllo (come in `ub.c`). Per `unsigned long` il "wraparound" è definito modulo 2⁶⁴, quindi `a + b < a` è un test di overflow valido; per i tipi con segno no, e serve il controllo preventivo con `LONG_MAX`/`LONG_MIN` o `__builtin_add_overflow`.

**7.**

```c
size_t mia_strlen(const char *s) { const char *p = s; while (*p) p++; return p - s; }

char *mia_strcpy(char *d, const char *s) { char *r = d; while ((*d++ = *s++)) ; return r; }

char *mia_strncpy(char *d, const char *s, size_t n) {     // garantisce SEMPRE il terminatore
    size_t i = 0;
    for (; i < n - 1 && s[i]; i++) d[i] = s[i];
    if (n) d[i] = '\0';
    return d;
}

char *giunta(char **p, int n) {                           // dimensione esatta
    size_t t = 1;                                         // 1 per il '\0' finale
    for (int i = 0; i < n; i++) t += mia_strlen(p[i]) + (i ? 1 : 0);  // +1 per ogni separatore
    char *r = malloc(t);
    r[0] = '\0';
    for (int i = 0; i < n; i++) { if (i) strcat(r, "-"); strcat(r, p[i]); }
    return r;
}
```

`mia_strcpy` sfrutta che l'assegnamento è un'espressione il cui valore è quello assegnato: il ciclo copia fino al `\0` incluso e si ferma quando copia lo zero (falso). (c) La `strncpy` dello standard, se `src` è lungo almeno `n`, **non** mette il terminatore: lascia una stringa non terminata, un difetto. La nostra copia al massimo `n − 1` caratteri e mette sempre il `\0`. (d) `giunta` calcola la dimensione esatta (lunghezze + `n − 1` separatori + 1 terminatore); sotto `-fsanitize=address` non segnala niente, a conferma che il conto è giusto (dimentica il `+1` finale, e ASan trova subito un `heap-buffer-overflow` nel `strcat`).

**8.** È il programma `memoria.c` del §8.
(a) Ordinando gli indirizzi: codice (`main`, `0x...1xx`), `.rodata` (`const`, stringhe), `.data`/`.bss` (globali e `static`), heap (`malloc`, molto più in alto ma sotto lo stack), stack (`0x7fff...`, il più alto). Combaciano con le righe `r-x`, `r--`, `rw-`, `[heap]`, `[stack]` di `/proc/self/maps`. (b) Cambiano a ogni esecuzione gli indirizzi di stack, heap e (su un PIE) anche di codice e dati, perché il programma è caricato a una base casuale (ASLR, §8); le **distanze** interne restano fisse. (c) Scrivere in una stringa letterale fa crollare il programma con `SIGSEGV`, perché `.rodata` è mappata in sola lettura (flag `A` senza `W`, §2.6).

**9.**

```c
#include <stdlib.h>
typedef struct { int *dati; size_t n, capacita; } Vettore;
Vettore vettore_nuovo(void) { return (Vettore){NULL, 0, 0}; }
int vettore_aggiungi(Vettore *v, int x) {
    if (v->n == v->capacita) {
        size_t nc = v->capacita ? v->capacita * 2 : 4;
        int *nd = realloc(v->dati, nc * sizeof *nd);
        if (!nd) return -1;                       // in overflow non ha riassegnato: v->dati resta valido
        v->dati = nd; v->capacita = nc;
    }
    v->dati[v->n++] = x;
    return 0;
}
int vettore_get(const Vettore *v, size_t i, int *out) {
    if (i >= v->n) return -1;                     // controllo dei limiti
    *out = v->dati[i];
    return 0;
}
void vettore_libera(Vettore *v) { free(v->dati); v->dati = NULL; v->n = v->capacita = 0; }
```

(a) Con un `vettore_libera` alla fine, `-fsanitize=address` non segnala *leak*. (b) Se dimentichi `v->dati = nd`, continui a usare il vecchio blocco, che `realloc` può aver liberato: ASan segnala `heap-use-after-free`. (c) `vettore_get` con `i >= n` leggerebbe fuori dai limiti (`heap-buffer-overflow`); il controllo `if (i >= v->n)` lo previene. (d) Per un vettore di `void *`, `dati` diventa `void **`, `vettore_aggiungi` prende un `void *`, `vettore_get` lo restituisce: così contiene puntatori a elementi di qualunque tipo, come fa, in sostanza, una lista di Python.

**10.**

```c
// mio_cat.c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
static int versa(int fd) {
    char buf[4096]; ssize_t r;
    while ((r = read(fd, buf, sizeof buf)) > 0) {
        ssize_t w = 0;
        while (w < r) { ssize_t k = write(1, buf + w, r - w); if (k < 0) { perror("write"); return -1; } w += k; }
    }
    return r < 0 ? -1 : 0;
}
int main(int argc, char *argv[]) {
    if (argc == 1) return versa(0) < 0;
    for (int i = 1; i < argc; i++) {
        int fd = open(argv[i], O_RDONLY);
        if (fd < 0) { perror(argv[i]); return 1; }
        if (versa(fd) < 0) return 1;
        close(fd);
    }
    return 0;
}
```

(b) `mio_wc` conta byte (il totale dei `read`), righe (i byte `\n`) e parole (le transizioni da spazio a non-spazio), scorrendo il buffer. (c) `strace -c` conta le chiamate: il tuo `cat` fa circa una `read` ogni 4096 byte e una `write` per blocco; il `cat` di sistema usa buffer più grandi (spesso 128 KB) e quindi meno chiamate. (d) `./mio_cat grande | head -1` fa chiudere la pipe da `head` dopo la prima riga; la `write` successiva riceve `SIGPIPE`, e il programma termina (L4 §4.2). Lo vedi con `echo $?` (141 = 128 + 13, il numero di `SIGPIPE`).

**11.**
(a) Con `fib(5)` la ricorsione scende fino a `fib(1)`/`fib(0)`: il `backtrace` più profondo ha circa 5 *frame* di `fib` più `main`. (b) `info args` a ogni livello mostra `n` che cala. (c) `watch` su una variabile ferma il programma quando cambia (è un *watchpoint*). (d) A `-O2` il compilatore riordina il codice, tiene variabili nei registri e ne elimina alcune: `gdb` le mostra `<optimized out>` e le righe non seguono il sorgente. Per questo si fa debug a `-O0`. (e) A `-O2` il codice di `fib` è più corto e in parte iterativo: `disassemble` mostra una sola `call fib` (una delle due ricorsioni è stata trasformata), contro le due di `-O0`.

## ★★★ Sfida

**12. La cassaforte.** La flag è **`L9{la_toolchain_racconta_piu_del_sorgente}`**, ricomposta dai quattro pezzi:

```
$ bash setup_sfida.sh && cd ~/l9_sfida && make
gcc -g -O0 -no-pie -fno-stack-protector -o cassaforte cassaforte.c

# Pezzo 1 — strings (Lezione 7)
$ strings cassaforte | grep L9
Pezzo 1: L9{la_toolchain_

# Pezzo 2 — la password, letta con gdb. Ci si ferma nella funzione di controllo,
# si esegue lo snprintf e si legge la variabile locale 'atteso':
$ gdb -q -batch -ex 'break controlla' -ex 'run x' -ex 'next 2' \
      -ex 'printf "%s\n", atteso' cassaforte
47471-apriti
$ ./cassaforte 47471-apriti
Pezzo 1: L9{la_toolchain_
Accesso!
Pezzo 2: racconta_
Pezzo 3: piu_del_

# Pezzo 3 — (già ottenuto sopra con la password; o, senza password, da gdb dopo la decodifica)
$ gdb -q -batch -ex 'break main' -ex run -ex 'call (void)decodifica(p3, 0x5a)' \
      -ex 'printf "%s\n", p3' cassaforte              # NB: main decodifica già p3 da sé
piu_del_

# Pezzo 4 — funzione 'regalo', mai chiamata da main: la chiami tu
$ nm cassaforte | grep regalo
0000000000401...  T regalo
$ gdb -q -batch -ex 'break main' -ex run -ex 'call (void)regalo()' \
      -ex 'call (void)fflush(0)' cassaforte
Pezzo 4: sorgente}
```

Per ogni pezzo, lo strumento e il perché: **(1)** `strings` — il pezzo è una stringa letterale in `.rodata`, in chiaro; è sempre il primo tentativo. **(2)** `gdb` — la password non è una stringa nel binario, è costruita a runtime da un numero (`chiave = (2026*31) ^ 0x4c39 = 47471`) e una parola; fermandosi dopo lo `snprintf` e leggendo `atteso` (o leggendo la globale `chiave` con `print chiave` e aggiungendo `-apriti`) la si ottiene senza tentativi. **(3)** `gdb` dopo la decodifica — il pezzo è offuscato con XOR e diventa testo solo in memoria; `strings` sul binario mostrerebbe byte non stampabili, quindi bisogna leggerlo **a programma avviato**. **(4)** `nm`/`objdump` + `gdb` — `regalo` è codice morto (nessun `call regalo` nel disassembly di `main`); si invoca a mano con `call`, o ci si salta con `set $pc = regalo`. La morale è nella flag: la toolchain racconta più del sorgente, perché mostra il programma com'è davvero in memoria, non come è scritto.

**13.** Su `/bin/ls` (le risposte precise variano con la distribuzione):
(a) `file /bin/ls` → `ELF 64-bit LSB pie executable, dynamically linked, ... stripped`: è PIE, dinamico, *stripped*. (b) `strings /bin/ls | less` mostra i messaggi d'errore, i nomi delle opzioni lunghe, i formati di data. (c) `nm -D /bin/ls` (o `readelf --dyn-syms`) elenca le funzioni di libreria: `strcmp`, `malloc`, `getenv`, `ioctl`, `readdir`... (d) `objdump -d /bin/ls | grep '@plt'` mostra quali chiama: `opendir`/`readdir` (legge directory), `ioctl` (dimensione del terminale), `strcoll` (ordinamento). (e) `strace ls` mostra le chiamate di sistema (`openat`, `getdents64`, `statx`, `write`); `ltrace`, dove c'è, quelle di libreria. (f) L'ordine `file → strings → nm/readelf → objdump → ltrace/strace → gdb` va dal **colpo d'occhio** (che tipo di file, quali stringhe) al **dettaglio** (quali istruzioni, che cosa fa davvero a runtime): si parte dagli strumenti che costano meno e spesso bastano, e si scende solo quando serve. È l'ordine con cui si apre ogni sfida *reverse*.

**14.** Con `overflow.c` del §7.3 compilato `-g -O0 -fno-stack-protector`:
(a) `gdb`, dopo lo `strcpy`: `p &nome` e `p &ammesso` danno due indirizzi sullo stack a pochi byte di distanza (su questo compilatore `nome` è 8 byte, e `ammesso` lo segue). (b) La lunghezza minima che cambia `ammesso` è **9** byte (8 riempiono `nome`, il 9° invade il primo byte di `ammesso`): con 8 `A` più un byte diverso da zero `ammesso` diventa non nullo. (c) `./overflow "$(printf 'AAAAAAAA\x01')"` scrive 8 `A` in `nome` e il byte `\x01` in `ammesso`, che diventa esattamente 1: il `\0` che `strcpy` aggiunge riempie il resto. (d) Senza `-fno-stack-protector` (il default), un input abbastanza lungo fa abortire il programma con `*** stack smashing detected ***; Aborted`: il *canary* (§2.7) tra le variabili e l'indirizzo di ritorno è stato sovrascritto, e il controllo prima del `ret` lo rileva. (e) Con un input lungo abbastanza da superare l'indirizzo di ritorno, dopo il `SIGSEGV` il `backtrace` mostra il *frame* chiamante come `0x4141414141414141` invece di `main`: l'indirizzo di ritorno è stato sovrascritto con le `A` (0x41), e chi controlla quei byte controlla dove salta il programma — il fondamento del Modulo 4 (§11.4).

**15.**
(a) `massimo` a `-O2` non usa un salto ma `cmpl` seguito da `cmovge` (*conditional move*): copia `b` in `eax` solo se la condizione è vera. Niente salto significa niente *branch misprediction*, ed è anche un dettaglio che conta per la sicurezza (il codice senza salti non ha un tempo dipendente dal dato, L8, Esercizio 16).
(b) Per la convenzione di chiamata (§2.3), `a` arriva in `edi`, `b` in `esi`, e il risultato torna in `eax` (le metà a 32 bit di `rdi`, `rsi`, `rax`).
(c) A `-O0`, `objdump -d` di `fib` mostra **due** `call fib` (le due chiamate ricorsive); a `-O2` ne resta **una**, perché il compilatore trasforma una delle due ricorsioni in un ciclo (e il codice è più corto e veloce).
(d) Le due `call fib` a `-O0` corrispondono a `fib(n-1)` e `fib(n-2)`: il compilatore, senza ottimizzare, traduce letteralmente le due chiamate del sorgente.

## Domande di autoverifica: punti chiave attesi

1. Preprocessore (`-E`), compilatore (`-S`, assembly), assemblatore (`-c`, `.o`), linker (eseguibile); i programmi sono `cc1`, `as`, `ld` guidati da `gcc` (§2.1).
2. Il `.o` è rilocabile, con simboli `U` da risolvere e segnaposto; il linker risolve i simboli e riloca, aggiungendo `_start` e le librerie (§2.4–2.5).
3. `#include` incolla un file, `#define` sostituisce testo; le parentesi evitano che la precedenza degli operatori cambi il senso della macro espansa (§2.2).
4. `T` = definito in `.text`, `U` = non definito; maiuscola globale, minuscola locale (`static`); `extern` dichiara, `static` limita al file (§2.4, §2.8).
5. Statico = tutto dentro, grande, autonomo; dinamico = `libc` caricata dal *loader* a runtime, con GOT/PLT per le chiamate (§2.5).
6. PIE = indipendente dalla posizione, caricato a base casuale dall'ASLR: gli indirizzi cambiano, le distanze interne no (§2.5, §8).
7. LP64: `int` 4, `long` 8, puntatore 8, `size_t` 8; Windows 64 (LLP64): `long` 4 (§4.1).
8. `unsigned char`/`uint8_t` per i byte, sempre, perché `char` può avere segno e l'estensione del segno falserebbe i valori ≥ 128 (§4.1).
9. `-1 < 1u` è falso (−1 → unsigned); 300 → `unsigned char` dà 44; promozione a `int`, poi "vince il senza segno" (§4.3).
10. Unsigned modulo 2ⁿ (definito); signed overflow UB (il compilatore lo assume impossibile); controllo prima dell'operazione o `__builtin_add_overflow` (§4.5).
11. UB = nessun requisito dello standard (overflow con segno, accesso fuori dai limiti, puntatore non valido, variabile non inizializzata); `-fsanitize`, `-Wall` (§4.6).
12. Un puntatore contiene un indirizzo; `&` lo prende, `*` lo dereferenzia; `*p = 7` scrive nella memoria di `x` (§6.1).
13. In quasi ogni contesto il nome dell'array è il puntatore al primo elemento; eccezioni `sizeof` e `&`; la funzione riceve un puntatore, non la lunghezza (§6.4).
14. Array di `char` + `\0`, lunghezza implicita; `strcpy`/`strcat`/`gets`/`sprintf` scrivono senza limiti; si usano `snprintf`/`fgets` con la dimensione (§7.2–7.3).
15. Si scrive oltre l'array, verso l'indirizzo di ritorno sullo stack; chi controlla quei byte controlla dove salta il programma (§8, §11.4).
16. Basso→alto: codice, rodata, data/bss, heap (cresce in su), librerie, stack (cresce in giù). Locali sullo stack, globali in data/bss, dinamico nello heap (§8).
17. Allocare, allocare azzerato con controllo del prodotto, ridimensionare, liberare; un `free` per `malloc`; `calloc` perché controlla l'overflow di `n*dim` (§9.1).
18. *Memory leak*, *use-after-free*, *double free*, *heap overflow/off-by-one*; ASan ricompilando, Valgrind anche senza sorgente (§9.2–9.3).
19. `stdio` ha un buffer sopra `read`/`write`, che parlano col kernel senza buffer; `errno` è il codice dell'ultimo errore (§10.1–10.2).
20. `read` restituisce i byte letti (≤ n), 0 a EOF, −1 su errore; si legge in un ciclo perché può dare meno del richiesto (§10.2).
21. `gdb` esegue sotto controllo; `break`/`run`/`next`/`step`/`print`/`x`/`backtrace`/`info registers`; `-g` per i simboli, `-O0` per seguire il sorgente (§11).
22. Lo stack è stato sovrascritto oltre l'indirizzo di ritorno con `0x41` = `'A'`: uno *stack buffer overflow* (§11.4).
