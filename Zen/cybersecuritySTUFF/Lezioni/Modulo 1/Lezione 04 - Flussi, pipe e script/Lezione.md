# Modulo 1 — Lezione 4: Flussi, pipe e script

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 4 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 14).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. spiegare che cos'è un descrittore di file, come il kernel lo collega a un file aperto, e perché i descrittori 0, 1 e 2 hanno un ruolo speciale;
2. usare e **prevedere** ogni forma di redirezione di bash, compreso l'effetto dell'ordine (`>f 2>&1` contro `2>&1 >f`), here-document e here-string, descrittori aggiuntivi aperti con `exec`;
3. spiegare il buffering dell'output e perché un programma si comporta diversamente su un terminale e in una pipe;
4. descrivere che cosa fa il kernel quando la shell crea una pipe (`pipe`, `fork`, `dup2`, `execve`), e da qui spiegare EOF, `SIGPIPE`, il codice di uscita di una pipeline e il problema di `echo x | read v`;
5. usare `tee`, `xargs`, la sostituzione di processo, le named pipe e i coprocessi;
6. scrivere script bash corretti e robusti: argomenti, condizioni, cicli, funzioni, array, lettura sicura dell'input, gestione degli errori con `trap`;
7. riconoscere i difetti di sicurezza tipici degli script (variabili non quotate, `eval`, file temporanei, script eseguiti con privilegi) e correggerli;
8. scrivere uno script che **dialoga** con un programma interattivo, la competenza alla base di quasi tutte le sfide *pwn* e *misc* con un servizio remoto.

**Prerequisiti:** Lezioni 1–3. In particolare: `argv`, espansioni e divisione in parole (L1 §6–8), codice di uscita (L1 §11), ambiente (L1 §12), inode e `/proc/<PID>/fd` (L2 §7–8, §12.2), i filtri della Lezione 3.

**Tempo:** circa 4–5 ore di lettura e prove, 4 ore di esercizi. È la lezione che trasforma i comandi in programmi: vale la pena andare piano.

**Ripasso dalle lezioni precedenti.**
- Un processo riceve dal padre `argv`, ambiente e **file aperti** (L1 §10.2). Oggi scopriamo che cosa sono, esattamente, quei file aperti.
- In `/proc/<PID>/fd` ogni file aperto compare come link (L2 §8.3, §12.2): li useremo per **vedere** le redirezioni.
- I filtri della Lezione 3 leggono lo standard input e scrivono sullo standard output: questa lezione spiega che cosa siano e come si collegano.

**Convenzione tipografica.** Come nelle lezioni precedenti. Gli script completi sono scritti in blocchi che iniziano con `#!/usr/bin/env bash`: salvali in un file e lanciali con `bash nomefile.sh`.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. I descrittori di file | 1–3 | Da dove legge e dove scrive un programma? Come lo cambio? |
| II. Le pipe e gli strumenti di flusso | 4–6 | Che cosa succede davvero in `a | b`? Come si costruiscono flussi complessi? |
| III. Script bash | 7–13 | Come si scrive un programma in bash, in modo corretto? |
| IV. Sicurezza | 14 | Quali errori negli script diventano vulnerabilità? |
| V. La pratica | 15–20 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — I descrittori di file

## 1. Che cos'è un descrittore di file

### 1.1 Tre livelli

Quando un programma apre un file con la chiamata di sistema `open`, il kernel non gli restituisce il file, ma un **numero intero piccolo**: il **descrittore di file** (*file descriptor*, *fd*). Da quel momento il programma usa quel numero in ogni operazione: `read(fd, ...)`, `write(fd, ...)`, `close(fd)`. Dietro il numero ci sono tre livelli di strutture del kernel (`man 2 open`, *open file descriptions*; OSTEP cap. 39):

```
  processo A                          kernel                               file system
 ┌────────────────────┐    ┌──────────────────────────────┐         ┌────────────────┐
 │ tabella dei fd     │    │ tabella dei file aperti      │         │                │
 │  0 ──────────────────▶  │ /dev/pts/0, lettura/scrittura│ ──────▶ │ inode del PTY  │
 │  1 ──────────────────▶  │   (stesso oggetto per 0,1,2) │         │                │
 │  2 ──────────────────▶  │                              │         │                │
 │  3 ──────────────────▶  │ log.txt, scrittura, offset=812│ ──────▶ │ inode 680100   │
 └────────────────────┘    └──────────────────────────────┘         └────────────────┘
```

1. la **tabella dei descrittori** del processo: per ogni numero, un puntatore;
2. la **descrizione del file aperto** (*open file description*), nel kernel: modalità di apertura (lettura, scrittura, aggiunta in coda), e soprattutto la **posizione corrente** (*offset*) di lettura e scrittura;
3. l'**inode** del file (L2 §7).

Due descrittori possono puntare alla stessa descrizione (dopo un `dup` o un `fork`): allora **condividono l'offset**. Questo dettaglio spiegherà tra poco perché `cmd >f 2>&1` funziona e `cmd >f 2>f` no.

### 1.2 Le tre convenzioni: 0, 1, 2

Per convenzione Unix, ogni programma si aspetta di trovare già aperti tre descrittori:

| fd | Nome | Uso | In C | In Python |
|---|---|---|---|---|
| 0 | **standard input** (stdin) | da qui legge i dati | `stdin` | `sys.stdin` |
| 1 | **standard output** (stdout) | qui scrive i risultati | `stdout` | `sys.stdout`, `print` |
| 2 | **standard error** (stderr) | qui scrive errori e diagnostica | `stderr` | `sys.stderr` |

Non c'è nulla di magico: sono semplicemente i descrittori 0, 1 e 2, che il programma **eredita** dal processo padre. In una shell interattiva tutti e tre puntano al terminale (il PTY, L1 §2.2), ed è per questo che vedi sullo schermo sia i risultati sia gli errori, e che il programma legge da tastiera. La separazione tra 1 e 2 esiste perché i risultati possano essere mandati a un file o a un altro programma **senza** mescolarsi con i messaggi d'errore, che restano sullo schermo.

```
$ ls -l /proc/$$/fd           # i descrittori della shell corrente ($$ = il suo PID)
lrwx------ 1 hacker hacker 64 Nov  7 18:16 0 -> /dev/pts/0
lrwx------ 1 hacker hacker 64 Nov  7 18:16 1 -> /dev/pts/0
lrwx------ 1 hacker hacker 64 Nov  7 18:16 2 -> /dev/pts/0
lrwx------ 1 hacker hacker 64 Nov  7 18:16 255 -> /dev/pts/0
```

(Il 255 è un descrittore che bash tiene aperto per uso interno.)

### 1.3 Ereditarietà

I descrittori aperti sono **ereditati** da `fork` e **sopravvivono** a `execve` (L1 §10.2), salvo quelli segnati *close-on-exec* (`O_CLOEXEC`). È il meccanismo su cui si basano tutte le redirezioni: la shell, nel processo figlio, **dopo** `fork` e **prima** di `execve`, sistema i descrittori 0, 1, 2 come le hai chiesto; poi esegue il programma, che li trova già pronti e non sa nemmeno che sono stati cambiati.

Questo ha anche un risvolto di sicurezza: un programma privilegiato che lascia aperto per errore un descrittore su un file riservato, e poi esegue un programma scelto dall'utente, gli consegna quel file aperto (CWE-403, *Exposure of File Descriptor to an Unintended Control Sphere*). Lo rivedremo nel Modulo 4.

## 2. Le redirezioni

### 2.1 Le forme di base

Una redirezione è un'istruzione alla shell: "prima di eseguire il comando, collega il descrittore *n* a …". Il manuale di bash le descrive nella sezione *REDIRECTION*.

| Forma | Effetto | Chiamata equivalente nel figlio |
|---|---|---|
| `cmd > f` | stdout (1) su `f`, troncato o creato | `fd = open(f, O_WRONLY|O_CREAT|O_TRUNC); dup2(fd, 1)` |
| `cmd >> f` | stdout in **aggiunta** in coda a `f` | `open(f, O_WRONLY|O_CREAT|O_APPEND)` |
| `cmd < f` | stdin (0) da `f` | `open(f, O_RDONLY); dup2(fd, 0)` |
| `cmd 2> f` | stderr (2) su `f` | |
| `cmd n> f`, `cmd n< f` | qualunque descrittore n | |
| `cmd 2>&1` | 2 diventa una **copia** di 1, cioè punta dove punta 1 **in quel momento** | `dup2(1, 2)` |
| `cmd &> f` (bash) | stdout e stderr su `f` | come `> f 2>&1` |
| `cmd &>> f` (bash) | entrambi in aggiunta | |
| `cmd n>&-` | chiude il descrittore n | `close(n)` |
| `cmd <> f` | apre `f` in lettura **e** scrittura sul descrittore 0 | |
| `cmd >| f` | sovrascrive anche se è attivo `set -o noclobber` | |

La chiamata di sistema chiave è **`dup2(vecchio, nuovo)`** (`man 2 dup2`): fa sì che il descrittore `nuovo` punti alla stessa descrizione di file aperto di `vecchio`. Tutte le redirezioni sono `open` più `dup2`.

Le redirezioni possono stare in qualunque punto del comando semplice (L1 §5.2): `> f echo ciao` e `echo > f ciao` sono equivalenti a `echo ciao > f`. La convenzione leggibile è metterle in fondo.

Il file viene troncato **prima** che il comando parta. Per questo `sort f > f` **svuota** `f`: la shell apre e tronca `f` per l'output, poi `sort` legge un file ormai vuoto. Si usa un file temporaneo, oppure `sort -o f f`, oppure `sponge` (pacchetto `moreutils`).

### 2.2 L'ordine conta: un'analisi esatta

Le redirezioni sono applicate **da sinistra a destra**, una dopo l'altra. Con il modello di `dup2` si può prevedere esattamente il risultato di ogni combinazione.

**Caso A: `ls /tmp /nonesiste > out 2>&1`**

| Passo | Operazione | fd 1 | fd 2 |
|---|---|---|---|
| inizio | | terminale | terminale |
| `> out` | `open(out)`, `dup2(…, 1)` | `out` | terminale |
| `2>&1` | `dup2(1, 2)`: 2 punta dove punta 1 **ora** | `out` | `out` |

Risultato: tutto in `out`. E poiché 1 e 2 condividono la **stessa** descrizione di file aperto, condividono l'offset: le righe di output ed errore si susseguono senza sovrascriversi.

**Caso B: `ls /tmp /nonesiste 2>&1 > out`**

| Passo | Operazione | fd 1 | fd 2 |
|---|---|---|---|
| inizio | | terminale | terminale |
| `2>&1` | `dup2(1, 2)`: 2 punta dove punta 1 **ora**, cioè al terminale | terminale | terminale |
| `> out` | `dup2(…, 1)` | `out` | terminale |

Risultato: l'output va in `out`, l'errore resta sul **terminale**. `2>&1` non è un collegamento permanente ("2 segue 1"): è una **copia istantanea**.

**Caso C: `cmd > out 2> out`** apre `out` **due volte**, con due descrizioni indipendenti e due offset indipendenti, entrambi a zero: output ed errori si sovrascrivono a vicenda, e il file finale è un miscuglio. Mai farlo; si usa il caso A o `&>`.

**Caso D: scambiare stdout e stderr**: `cmd 3>&1 1>&2 2>&3 3>&-`. Si salva 1 in 3, si sposta 1 su 2, si mette in 2 il vecchio 1 salvato in 3, si chiude 3. È lo stesso schema dello scambio di due variabili con una terza.

Applicazione tipica in gara: **filtrare solo gli errori** con una pipe. La pipe collega solo lo stdout, quindi `cmd 2>&1 >/dev/null | grep x` fa passare a `grep` gli errori e butta via l'output normale (caso B applicato con intenzione).

### 2.3 Here-document e here-string

Un **here-document** fornisce lo stdin di un comando direttamente nello script, fino a una riga che contiene solo il delimitatore:

```
$ cat <<FINE
casa $HOME $((1+1))
FINE
casa /home/hacker 2
$ cat <<'FINE'
casa $HOME $((1+1))
FINE
casa $HOME $((1+1))
```

- Con il delimitatore **non quotato**, nel testo avvengono le espansioni di parametri, di comando e aritmetiche (come tra virgolette doppie).
- Con il delimitatore **quotato** (`'FINE'` o `"FINE"`), il testo è **letterale**: è la forma giusta per scrivere un altro script, un file di configurazione, o un programma che contiene `$`.
- Con `<<-FINE` vengono tolte le **tabulazioni** iniziali di ogni riga (non gli spazi), così il testo si può indentare dentro uno script.

Un **here-string** passa una sola stringa, seguita da un a capo: `tr a-z A-Z <<< "ciao"`. È più efficiente e più corretto di `echo "ciao" | tr a-z A-Z` (niente pipe, niente subshell, nessuna ambiguità di `echo` sulle opzioni).

### 2.4 Redirezioni permanenti con `exec`

`exec` senza un comando applica le redirezioni **alla shell stessa**, in modo permanente:

```
$ exec 3> log.txt          # apre log.txt in scrittura sul descrittore 3
$ echo "prima riga" >&3    # >&3 è un'abbreviazione di 1>&3
$ echo "seconda" >&3
$ exec 3>&-                # chiude il 3
$ cat log.txt
prima riga
seconda
```

Il file viene aperto una volta sola, e l'offset avanza a ogni scrittura: è più efficiente di cento `>> log.txt`. Negli script si usa per mandare tutto lo stdout e lo stderr a un log da un certo punto in poi: `exec >> script.log 2>&1`. Con `exec 3< file` si apre un file in lettura e lo si legge una riga alla volta con `read -u 3` o `read <&3`.

### 2.5 File speciali utili nelle redirezioni

| Nome | Uso |
|---|---|
| `/dev/null` | `cmd > /dev/null` scarta l'output; `cmd < /dev/null` dà un input vuoto (L2 §12.1) |
| `/dev/stdin`, `/dev/stdout`, `/dev/stderr` | link ai descrittori 0, 1, 2 (L2 §12.1), per i programmi che vogliono un **nome** di file |
| `/dev/fd/N` | il descrittore N del processo stesso |
| `/dev/tcp/host/porta`, `/dev/udp/host/porta` | **non esistono** nel file system: bash li riconosce in una redirezione e apre una connessione di rete. `exec 3<>/dev/tcp/example.com/80` apre un socket TCP sul descrittore 3. Lo useremo nella Lezione 10 |

## 3. Il buffering

### 3.1 Perché esiste

Ogni chiamata di sistema `write` ha un costo (il passaggio in modalità kernel, L1 §2.1). Per questo le librerie standard (la `stdio` del C, l'I/O di Python) non chiamano `write` a ogni `printf`, ma accumulano i dati in un **buffer** in memoria e li scrivono a blocchi. Le regole della libreria C (`man 3 setvbuf`), seguite in modo simile da Python e da altri linguaggi:

| Descrittore | Collegato a un terminale | Collegato a file o pipe |
|---|---|---|
| stdout | **a righe** (*line buffered*): scrive a ogni `\n` | **pieno** (*fully buffered*): scrive quando il buffer (tipicamente 4–64 KiB) è pieno, o all'uscita |
| stderr | **senza buffer** | **senza buffer** |

### 3.2 Le conseguenze

```
$ python3 -c "
import sys
print('stdout 1'); sys.stderr.write('stderr 2\n'); print('stdout 3')" 2>&1 | cat
stderr 2
stdout 1
stdout 3
```

Sul terminale l'ordine sarebbe 1, 2, 3. In una pipe lo stdout di Python è a buffer pieno: le due `print` restano in memoria fino all'uscita, mentre lo stderr passa subito. L'output **cambia ordine** a seconda di dove va. Le stesse cause producono due problemi che incontrerai sicuramente:

1. **log fuori ordine**: messaggi d'errore che compaiono "prima" dell'output che li ha causati;
2. **programmi interattivi che sembrano bloccati**: quando un tuo script parla con un programma attraverso una pipe (§6, Lezione 8), il programma può aver scritto la domanda nel **suo** buffer senza mandarla, e il tuo script aspetta una domanda che non arriverà finché il buffer non si riempie. Molte sfide CTF chiamano esplicitamente `setvbuf(stdout, NULL, _IONBF, 0)` all'inizio proprio per evitarlo; quando non lo fanno, è un problema tuo.

Rimedi:

| Strumento | Effetto |
|---|---|
| `python3 -u`, variabile `PYTHONUNBUFFERED=1` | Python senza buffer |
| `stdbuf -oL cmd` | forza lo stdout a righe per programmi che usano la stdio del C (non funziona con tutti) |
| `grep --line-buffered`, `sed -u` | opzioni specifiche degli strumenti |
| `script -q -c cmd /dev/null`, `unbuffer cmd` | eseguono il programma in un **pseudo-terminale**, così si comporta come se fosse interattivo |
| in C: `fflush(stdout)`, `setvbuf` | il programmatore svuota il buffer quando serve |

Nota: i builtin di bash come `echo` e `printf` **non** hanno buffer: ogni comando produce subito la sua `write`. Il problema riguarda i programmi esterni.

---

# Parte II — Le pipe e gli strumenti di flusso

## 4. Che cos'è una pipe

### 4.1 Il meccanismo nel kernel

Una **pipe** è un canale unidirezionale gestito dal kernel: un buffer in memoria con un'estremità di scrittura e una di lettura. La crea la chiamata di sistema `pipe(fd)` (`man 2 pipe`, `man 7 pipe`), che restituisce **due** descrittori: `fd[0]` per leggere, `fd[1]` per scrivere. Ciò che si scrive in `fd[1]` si legge, nello stesso ordine, da `fd[0]`. I dati non toccano mai il disco.

Per eseguire `echo ciao | tr a-z A-Z`, la shell:

1. chiama `pipe()` e ottiene, per esempio, i descrittori 3 (lettura) e 4 (scrittura);
2. crea un primo figlio con `fork`; nel figlio fa `dup2(4, 1)` (lo stdout diventa l'estremità di scrittura), chiude 3 e 4, ed esegue `echo`;
3. crea un secondo figlio; nel figlio fa `dup2(3, 0)` (lo stdin diventa l'estremità di lettura), chiude 3 e 4, ed esegue `tr`;
4. chiude 3 e 4 nel padre, e attende **entrambi** i figli.

Non è una descrizione di comodo: si vede con `strace`.

```
$ strace -f -e trace=pipe2,dup2,execve bash -c 'echo ciao | tr a-z A-Z' 2>&1 | grep -v '^+++'
execve("/usr/bin/bash", ["bash", "-c", "echo ciao | tr a-z A-Z"], ...) = 0
pipe2([3, 4], 0)                        = 0
[pid 7101] dup2(4, 1)                   = 1
[pid 7102] dup2(3, 0)                   = 0
[pid 7102] execve("/usr/bin/tr", ["tr", "a-z", "A-Z"], ...) = 0
CIAO
```

`echo` non compare come `execve` perché è un builtin (L1 §15.2): lo esegue il primo figlio, che è ancora bash.

### 4.2 Le proprietà che ne derivano

1. **I comandi di una pipeline girano in parallelo.** Non è "prima A, poi B": partono insieme, e B elabora i dati man mano che A li produce. Per questo `tail -f log | grep ERROR` funziona su un file che cresce all'infinito.
2. **Il buffer è limitato.** Su Linux una pipe contiene per default 65.536 byte (64 KiB, `man 7 pipe`, *Pipe capacity*). Se chi scrive è più veloce di chi legge, quando il buffer è pieno `write` si **blocca** finché l'altro non legge. Se chi legge trova il buffer vuoto, `read` si blocca finché arrivano dati. Questo regola automaticamente la velocità dei due processi.
3. **EOF arriva quando tutti gli scrittori hanno chiuso.** Un lettore vede la fine dell'input (`read` restituisce 0) solo quando **ogni** descrittore aperto sull'estremità di scrittura è stato chiuso. Se un processo dimentica aperta una copia dell'estremità di scrittura, il lettore aspetterà per sempre: è il motivo per cui la shell, al passo 4, chiude le sue copie. È un errore classico quando si programmano pipe a mano (Lezione 8).
4. **Chi scrive su una pipe senza lettori riceve `SIGPIPE`.** Se il lettore termina prima, la successiva `write` dello scrittore provoca il segnale `SIGPIPE` (13), che per default termina il processo.

```
$ yes | head -n 2
y
y
$ echo "${PIPESTATUS[@]}"
141 0
```

`yes` stamperebbe `y` all'infinito; `head` termina dopo due righe; `yes` riceve `SIGPIPE` e muore con codice 128 + 13 = **141** (L1 §11.1). Non è un errore: è il meccanismo normale con cui una pipeline si ferma quando l'ultimo comando ha finito.

### 4.3 Il codice di uscita di una pipeline

Come anticipato nella Lezione 1 (§11.2), il codice di uscita di `A | B | C` è quello di **C**. Il fallimento di A passa inosservato:

```
$ false | true; echo $?
0
$ set -o pipefail; false | true; echo $?
1
```

Con `set -o pipefail` il codice è quello dell'**ultimo** comando che ha fallito (0 se nessuno ha fallito). L'array **`PIPESTATUS`** contiene i codici di tutti i comandi dell'ultima pipeline, e va letto **subito** dopo, perché il comando successivo lo sovrascrive. Attenzione all'interazione con `SIGPIPE`: con `pipefail`, `yes | head -1` fallisce con 141, anche se tutto è andato come previsto.

### 4.4 Ogni pezzo di una pipeline è una subshell

Poiché ogni comando della pipeline gira in un processo figlio (§4.1), anche un builtin in una pipeline modifica solo il **suo** processo:

```
$ v=iniziale
$ echo nuovo | read v
$ echo "$v"
iniziale
```

`read v` ha letto `nuovo` e impostato `v`, ma in una subshell che poi è terminata (L1 §12.1). È una delle sorprese più frequenti di bash. Soluzioni:

```
$ read v <<< "nuovo"                      # here-string: nessuna pipe
$ read v < <(echo nuovo)                  # sostituzione di processo (§5.3)
$ v=$(echo nuovo)                         # sostituzione di comando
$ shopt -s lastpipe                       # in uno script: l'ultimo comando gira nella shell corrente
```

`lastpipe` funziona solo quando il *job control* è disattivato, cioè negli script (non nella shell interattiva, salvo `set +m`). Lo stesso problema colpisce `cmd | while read ...; do conta=$((conta+1)); done`: alla fine del ciclo `conta` è tornata al valore di prima. Rimedio: `while read ...; do ...; done < <(cmd)`.

## 5. Strumenti di flusso

### 5.1 `tee`: biforcare un flusso

`tee file` copia lo stdin sia sullo stdout sia nel file (il nome viene dai raccordi a T degli idraulici). Serve a salvare un risultato intermedio senza interrompere la catena, o a vedere e registrare insieme l'output di un comando lungo.

```
$ ./scan.sh | tee scan.log | grep OPEN
$ cmd | tee -a log.txt              # -a: in aggiunta
$ echo "riga" | sudo tee -a /etc/file > /dev/null
```

L'ultimo esempio risolve un problema reale: `sudo echo riga >> /etc/file` **non** funziona, perché la redirezione è fatta dalla **tua** shell, senza privilegi, prima di lanciare `sudo`. Con `tee` è il programma eseguito con `sudo` ad aprire il file.

### 5.2 `xargs`: dalle righe agli argomenti

Molti comandi accettano dati come **argomenti** e non dallo stdin (`rm`, `touch`, `ls`, `file`). `xargs cmd` legge lo stdin, lo divide in parole e lancia `cmd` con quelle parole come argomenti, raggruppandole per non superare il limite di lunghezza (L2 §13, `E2BIG`).

| Opzione | Effetto |
|---|---|
| `-n N` | al massimo N argomenti per esecuzione |
| `-I{}` | una esecuzione per riga, con `{}` sostituito dalla riga intera |
| `-0` | input separato da byte zero (con `find -print0`, L2 §14.4) |
| `-d '\n'` (GNU) | separa solo sugli a capo |
| `-P N` | fino a N esecuzioni **in parallelo** |
| `-t` | stampa ogni comando prima di eseguirlo |
| `-r` (GNU) | non esegue nulla se l'input è vuoto |

```
$ printf '%s\n' f1 f2 | xargs -t touch
touch f1 f2
$ printf 'uno\ndue\n' | xargs -I{} echo "file-{}.txt"
file-uno.txt
file-due.txt
$ seq 1 254 | xargs -P 32 -I{} sh -c 'ping -c1 -W1 10.0.0.{} >/dev/null && echo 10.0.0.{}'   # (laboratorio: host attivi nella TUA rete)
```

**La trappola di `xargs`.** Senza `-0` o `-d`, `xargs` divide su spazi **e** a capo, e interpreta virgolette e backslash con regole sue, diverse da quelle della shell:

```
$ echo "'a b' c" | xargs -n1 echo
a b
c
```

Un nome di file con uno spazio o un apostrofo rompe il comando. Le forme sicure sono sempre le stesse: `find ... -print0 | xargs -0 ...` oppure `find ... -exec ... +`.

### 5.3 Sostituzione di processo

`<(comando)` esegue il comando e si sostituisce con il **nome di un file** da cui leggerne l'output; `>(comando)` con il nome di un file su cui scrivere per mandare dati al comando. Il nome è un percorso come `/dev/fd/63`: un descrittore aperto su una pipe (§2.5).

```
$ echo <(true)
/dev/fd/63
$ diff <(sort a.txt) <(sort b.txt)             # confronta due file ordinati senza file temporanei
$ comm -12 <(cut -d: -f1 /etc/passwd | sort) <(ls /home | sort)   # L3 §14.4 in una riga
$ while IFS= read -r l; do n=$((n+1)); done < <(grep x f); echo "$n"   # il conteggio sopravvive (§4.4)
$ cmd > >(tee out.log) 2> >(tee err.log >&2)    # salva stdout e stderr separatamente, vedendoli entrambi
```

È la soluzione quando un comando vuole **file** come argomenti e tu hai **flussi**: `diff`, `comm`, `paste`, `join` ne sono gli utenti tipici.

### 5.4 Named pipe (FIFO)

Una **FIFO** (L2 §12.3) è una pipe con un nome nel file system, creata con `mkfifo`. Processi indipendenti, lanciati in momenti diversi o da shell diverse, possono usarla per comunicare. Aprire una FIFO in lettura **blocca** finché qualcuno non la apre in scrittura, e viceversa.

```
$ mkfifo canale
$ cat canale &                  # il lettore aspetta
$ echo "messaggio" > canale     # lo scrittore sblocca il lettore
messaggio
```

Con una FIFO si costruisce un **ciclo**: l'output di un programma entra in un altro, il cui output torna nel primo. È la tecnica classica per dialogare con un programma interattivo dalla shell (Esempio 6).

### 5.5 Coprocessi

Bash 4 ha una forma integrata dello stesso schema: `coproc NOME { comando; }` lancia il comando in background con **due** pipe, e mette i descrittori nell'array `NOME`: `${NOME[0]}` per leggere il suo output, `${NOME[1]}` per scrivere nel suo input.

```
$ coproc CALC { while read -r a b; do echo $((a + b)); done; }
$ echo "2 3" >&"${CALC[1]}"
$ read -r risultato <&"${CALC[0]}"
$ echo "$risultato"
5
```

È lo strumento più comodo per far "parlare" uno script con un programma che fa domande (Esercizio 14). Nella Lezione 8 faremo la stessa cosa, in modo più robusto, con Python e `pwntools`.

### 5.6 `|&` e il raggruppamento

`cmd1 |& cmd2` è un'abbreviazione di `cmd1 2>&1 | cmd2`: manda nella pipe sia stdout sia stderr. Per redirigere l'output di **più** comandi insieme si usano i gruppi (L1 §5.4):

```
$ { echo "intestazione"; date; ls; } > report.txt     # un solo file, aperto una volta
$ ( cd /tmp && ls ) | wc -l                            # subshell: la cd non cambia la shell corrente
```

Nel gruppo `{ ...; }` lo spazio dopo `{` e il `;` prima di `}` sono obbligatori: `{` e `}` sono parole riservate, non metacaratteri.

## 6. La sostituzione di comando, rivista

`$(cmd)` (L1 §8.4) è in realtà una pipe: la shell crea una pipe, lancia `cmd` in una subshell con lo stdout sulla pipe, e legge tutto fino a EOF. Due dettagli che ora puoi spiegare:

- gli **a capo finali** vengono tolti, tutti: `x=$(printf 'riga\n\n\n')` contiene solo `riga`. Se servono, il trucco è `x=$(cmd; echo .); x=${x%.}`;
- una variabile di bash **non può contenere byte zero**: se l'output di `cmd` ne contiene, bash li scarta (con un avviso). Per dati binari non si usano le variabili ma file, pipe, o strumenti come `xxd` e `base64` (Lezione 7).

---

# Parte III — Script bash

## 7. Che cos'è uno script, e come si scrive bene

### 7.1 Dalla riga al file

Uno **script** è un file di testo che contiene comandi di shell, eseguiti in sequenza da una shell **non interattiva** (L1 §4.2). Tutto ciò che hai imparato vale identico, con tre differenze: niente alias, niente espansione della storia con `!`, e niente prompt.

```bash
#!/usr/bin/env bash
# saluta.sh — saluta l'utente e mostra dove si trova
echo "Ciao $USER, sei in $PWD"
```

Tre modi di eseguirlo, già visti nella Lezione 1 (§10.3, Esempio 6):

| Comando | Che cosa succede |
|---|---|
| `bash saluta.sh` | un nuovo processo bash legge il file; non serve il permesso `x` |
| `chmod +x saluta.sh; ./saluta.sh` | il kernel legge lo shebang e lancia l'interprete |
| `source saluta.sh` | i comandi vengono eseguiti nella **shell corrente** |

**Lo shebang conta.** `#!/bin/sh` non è bash: su Debian e Ubuntu è `dash`, che non ha `[[ ]]`, gli array, `<<<`, `$'...'`, la sostituzione di processo, `{1..5}`. Uno script con funzioni bash e shebang `/bin/sh` fallisce con errori di sintassi apparentemente incomprensibili. Se usi le funzioni di bash, scrivi `#!/usr/bin/env bash` (o `#!/bin/bash`).

### 7.2 Strumenti di controllo

| Strumento | Effetto |
|---|---|
| `bash -n script.sh` | controlla la sintassi senza eseguire |
| `bash -x script.sh`, `set -x` | traccia ogni comando dopo le espansioni (L1 §15.1) |
| `PS4='+ ${LINENO}: '` | aggiunge il numero di riga alla traccia |
| **ShellCheck** (`shellcheck script.sh`, anche online su shellcheck.net) | analisi statica: trova variabili non quotate, errori di confronto, problemi di portabilità. Usalo su ogni script che scrivi: è il miglior insegnante di bash che esista |

### 7.3 La "modalità rigorosa" e i suoi limiti

Molti script iniziano con:

```bash
set -euo pipefail
```

| Opzione | Effetto |
|---|---|
| `-e` (`errexit`) | lo script termina se un comando fallisce |
| `-u` (`nounset`) | usare una variabile non definita è un errore |
| `-o pipefail` | una pipeline fallisce se fallisce un suo comando (§4.3) |

È una buona abitudine, ma `set -e` ha regole complicate che è bene conoscere (manuale di bash, `set -e`):

- **non** interviene sui comandi usati come condizione: in `if cmd`, `while cmd`, `cmd && …`, `cmd || …`, e su ogni comando preceduto da `!`;
- un'espressione aritmetica che vale 0 è un "fallimento": con `c=0`, `((c++))` restituisce 1 (perché il valore **prima** dell'incremento è 0) e termina lo script. Si scrive `c=$((c + 1))` o `((c++)) || true`;
- dentro una funzione chiamata come condizione (`f || echo errore`), `set -e` è disattivato **per tutta la funzione**;
- `local x=$(cmd)` nasconde il fallimento di `cmd`, perché il codice di uscita è quello di `local`, che riesce sempre. Si scrive `local x; x=$(cmd)`.

Conclusione pratica: usa `set -euo pipefail`, ma controlla esplicitamente gli errori che contano (`cmd || { echo "errore" >&2; exit 1; }`), invece di affidarti solo a `-e`.

## 8. Argomenti e codici di uscita

### 8.1 Parametri posizionali

Uno script riceve i suoi argomenti come parametri posizionali (L1 §9.2): `$0` è il nome dello script, `$1`…`$9`, `${10}`… gli argomenti, `$#` il loro numero, `"$@"` l'elenco esatto. `shift` scarta il primo e fa scorrere gli altri; `shift 2` ne scarta due.

```bash
#!/usr/bin/env bash
# conta.sh — conta le righe di ogni file passato
if [ $# -eq 0 ]; then
    echo "uso: $0 FILE..." >&2
    exit 2
fi
for f in "$@"; do
    printf '%6d %s\n' "$(wc -l < "$f")" "$f"
done
```

Tre convenzioni da rispettare sempre:
1. il messaggio d'uso va su **stderr** (`>&2`), non su stdout;
2. il codice di uscita deve dire il vero: 0 per successo, 1 per errore generico, 2 per uso sbagliato (convenzione di molti strumenti GNU);
3. `wc -l < "$f"` (con la redirezione) stampa solo il numero, mentre `wc -l "$f"` stamperebbe anche il nome.

### 8.2 Opzioni con `getopts`

Per opzioni in stile Unix (L1 §6.2) bash ha il builtin `getopts` (`help getopts`):

```bash
#!/usr/bin/env bash
verbose=0; n=10
while getopts "vn:" opt; do         # "n:" = l'opzione -n vuole un valore
    case $opt in
        v) verbose=1 ;;
        n) n=$OPTARG ;;
        *) echo "uso: $0 [-v] [-n NUM] FILE..." >&2; exit 2 ;;
    esac
done
shift $((OPTIND - 1))               # toglie le opzioni già lette: in "$@" restano i file
echo "verbose=$verbose n=$n file: $*"
```

`getopts` gestisce le opzioni unite (`-vn 5`) e `--`, ma non le opzioni lunghe di GNU.

### 8.3 `exit` e `return`

`exit n` termina lo script (o la shell) con codice `n`; senza argomento, con il codice dell'ultimo comando. `return n` fa lo stesso per una **funzione** (§11). In entrambi i casi il valore è ridotto a 8 bit: `return 300` restituisce 44 (L1 §11.1).

## 9. Condizioni

### 9.1 `if` esegue comandi

In bash `if` non valuta espressioni booleane: **esegue un comando** e guarda il suo codice di uscita (L1 §11.2).

```bash
if grep -q '^hacker:' /etc/passwd; then
    echo "esiste"
elif [ -d /home/hacker ]; then
    echo "c'è solo la home"
else
    echo "non esiste"
fi
```

Le parentesi quadre non sono sintassi: `[` è un **comando** (un builtin, ed esiste anche `/usr/bin/[`), sinonimo di `test`, che vuole come ultimo argomento `]`. Per questo gli spazi sono obbligatori: `[ -f x ]`, mai `[-f x]`.

### 9.2 `[ ]`, `[[ ]]` e `(( ))`

| | `[ ... ]` / `test` | `[[ ... ]]` | `(( ... ))` |
|---|---|---|---|
| che cos'è | comando (POSIX) | parola riservata di bash | aritmetica di bash |
| divisione in parole e globbing delle variabili | **sì**: `[ $x = y ]` si rompe se `x` è vuota o contiene spazi | **no**: `[[ $x = y ]]` è sicuro | non rilevante |
| confronto di stringhe | `=`, `!=`, `\<`, `\>` | `==`, `!=`, `<`, `>` | |
| corrispondenza con un modello glob | no | `[[ $f == *.txt ]]` (modello **non** quotato) | |
| regex | no | `[[ $s =~ ^[0-9]+$ ]]`, gruppi in `BASH_REMATCH` | |
| confronto numerico | `-eq -ne -lt -le -gt -ge` | gli stessi | `==`, `<`, `>=` … come in C |
| logica | `-a`, `-o` (sconsigliati), oppure più `[ ]` con `&&` | `&&`, `||`, `!`, parentesi | `&&`, `||`, `!` |

```
$ x=""
$ [ $x = y ]; echo $?
bash: [: =: unary operator expected
2
$ [[ $x = y ]]; echo $?
1
$ [[ 10 > 9 ]] || echo "come stringhe, '10' viene prima di '9'"
come stringhe, '10' viene prima di '9'
$ (( 10 > 9 )) && echo "come numeri, sì"
come numeri, sì
```

Nel primo caso `$x` vuota e non quotata sparisce (L1 §8.6), e `[` riceve `= y ]`: un errore di sintassi. Regole pratiche: in bash usa **`[[ ]]`** per stringhe e file, **`(( ))`** per numeri; se devi scrivere per `sh`, usa `[ ]` e quota **sempre** le variabili.

### 9.3 I test più usati

| Test | Vero se |
|---|---|
| `-e f` / `-f f` / `-d f` / `-L f` | esiste / è un file regolare / è una directory / è un link simbolico (L2 §5.2) |
| `-r f` / `-w f` / `-x f` | il processo può leggere / scrivere / eseguire (Lezione 6) |
| `-s f` | esiste e non è vuoto |
| `f1 -nt f2` | f1 è più recente di f2 (mtime, L2 §10) |
| `-z s` / `-n s` | la stringa è vuota / non è vuota |
| `-t 0` | il descrittore 0 è un terminale: lo script sta parlando con una persona? |
| `-v nome` | la variabile è definita |

### 9.4 `case`

Per confrontare un valore con molti modelli glob:

```bash
case "$file" in
    *.tar.gz|*.tgz) tar -xzf "$file" ;;
    *.zip)          unzip "$file" ;;
    *.gz)           gunzip "$file" ;;
    -*)             echo "nome sospetto: $file" >&2 ;;
    *)              echo "formato sconosciuto: $file" ;;
esac
```

I modelli sono provati in ordine e vince il primo: `*.tar.gz` va prima di `*.gz`. `;;` chiude ogni ramo.

### 9.5 Regex in bash

`[[ stringa =~ regex ]]` usa le regex **ERE** (L3 §4.4), e i gruppi catturati finiscono nell'array `BASH_REMATCH`:

```
$ [[ "2026-11-07" =~ ^([0-9]{4})-([0-9]{2})-([0-9]{2})$ ]] && echo "anno ${BASH_REMATCH[1]}, mese ${BASH_REMATCH[2]}"
anno 2026, mese 11
```

La regex a destra **non** va quotata: tra virgolette diventa una stringa letterale. Per regex complicate conviene metterla in una variabile: `re='^[0-9]+$'; [[ $x =~ $re ]]`. A differenza di `grep`, `=~` lavora sull'**intera** stringa, anche se contiene a capo, quindi è la scelta giusta per convalidare un valore (L3, Esercizio 17).

## 10. Cicli

### 10.1 `for`

```bash
for f in *.txt; do echo "file: $f"; done            # su una lista (qui un glob)
for i in {1..5}; do echo "$i"; done                 # su un intervallo (graffe, L1 §8.1)
for ((i = 0; i < 10; i += 2)); do echo "$i"; done   # stile C
for arg in "$@"; do echo "[$arg]"; done             # sugli argomenti (anche: for arg; do ...)
```

Due trappole:
- **il glob senza corrispondenze resta letterale** (L1 §8.7): se non ci sono `.txt`, il ciclo gira **una volta** con `f='*.txt'`. Rimedio: `shopt -s nullglob`, oppure `[ -e "$f" ] || continue` come prima riga del ciclo;
- **mai** `for f in $(ls)` o `for riga in $(cat file)`: la divisione in parole spezza nomi e righe sugli spazi, e il globbing espande gli asterischi contenuti nei dati. Per i file si usa il glob, per le righe `while read` (§10.3).

### 10.2 `while` e `until`

`while cmd; do ...; done` ripete finché `cmd` ha successo; `until` finché fallisce. `break` esce dal ciclo, `continue` passa all'iterazione successiva (entrambi accettano un numero di livelli: `break 2`).

```bash
n=0
while (( n < 3 )); do echo "giro $n"; n=$((n + 1)); done
until ping -c1 -W1 10.0.0.5 >/dev/null 2>&1; do sleep 1; done; echo "l'host è attivo"
```

### 10.3 Leggere un file riga per riga: la forma corretta

```bash
while IFS= read -r riga; do
    printf '[%s]\n' "$riga"
done < file.txt
```

Ogni pezzo ha una ragione:

| Pezzo | Senza, che cosa succede |
|---|---|
| `IFS=` | `read` toglie spazi e tabulazioni iniziali e finali: `  spazi  ` diventa `spazi` |
| `-r` | `read` interpreta i backslash: `a\tb` perde il backslash, e un `\` finale unisce due righe |
| `< file.txt` alla fine | (con `cat file | while`) il ciclo gira in una subshell e le variabili modificate si perdono (§4.4) |
| `printf` invece di `echo` | una riga come `-n` o `-e` viene presa per un'opzione di `echo` |

C'è un'ultima trappola: se il file **non termina con `\n`** (L3 §1.1), `read` legge l'ultima riga ma restituisce "fallimento", e il ciclo termina **senza elaborarla**. La forma completamente robusta è:

```bash
while IFS= read -r riga || [ -n "$riga" ]; do ...; done < file.txt
```

`read` con `IFS` impostato divide anche in campi: `IFS=: read -r utente x uid gid resto <<< "$riga"` legge una riga di `/etc/passwd` in cinque variabili, e l'ultima riceve tutto il resto. Per i nomi di file prodotti da `find`, la forma che regge qualunque nome è:

```bash
while IFS= read -r -d '' f; do echo "[$f]"; done < <(find . -type f -print0)
```

`-d ''` fa usare a `read` il byte zero come terminatore, in coppia con `-print0` (L2 §14.4).

## 11. Funzioni

```bash
saluta() {
    local nome=${1:-sconosciuto}     # local: la variabile esiste solo dentro la funzione
    echo "Ciao, $nome"
    return 0
}
saluta Zen
msg=$(saluta Anna)                   # l'"output" di una funzione si cattura come quello di un comando
```

Concetti chiave:
- una funzione si comporta come un **comando**: riceve argomenti in `$1`, `$2`, `$@` (quelli dello script sono nascosti mentre gira), scrive su stdout e stderr, e restituisce un codice di uscita con `return`;
- `return` restituisce **solo un codice di uscita** (0–255), non un valore. I dati si restituiscono **stampandoli** e catturandoli con `$(...)`, oppure assegnando una variabile globale;
- senza `local`, ogni variabile assegnata dentro la funzione è **globale** e sovrascrive quelle dello script. Dichiara sempre `local` le variabili di lavoro;
- le funzioni vanno definite **prima** di essere chiamate (lo script è eseguito dall'alto in basso). Una struttura comune è definire tutto e chiamare in fondo una funzione `main "$@"`.

## 12. Array e altri strumenti

### 12.1 Array indicizzati

```
$ a=(uno "due tre" quattro)
$ echo "${#a[@]}"            # numero di elementi
3
$ echo "${a[1]}"             # gli indici partono da 0
due tre
$ a+=(cinque)                # aggiunge in coda
$ printf '[%s]' "${a[@]}"; echo     # tutti gli elementi, ciascuno come parola (come "$@")
[uno][due tre][quattro][cinque]
$ echo "${!a[@]}"            # gli indici
0 1 2 3
```

Gli array sono il modo corretto di conservare una **lista di argomenti** che contengono spazi, per esempio le opzioni da passare a un comando: `opts=(-l --color=never); ls "${opts[@]}"`. Una stringa `opts="-l --color=never"` funzionerebbe solo grazie alla divisione in parole, e si romperebbe al primo valore con uno spazio.

`mapfile -t righe < file` (o `readarray`) legge un file in un array, una riga per elemento; `read -ra parole <<< "$riga"` divide una riga in un array di parole.

### 12.2 Array associativi

```
$ declare -A conteggio
$ conteggio[root]=1; conteggio[hacker]=5
$ for k in "${!conteggio[@]}"; do echo "$k=${conteggio[$k]}"; done
```

Sono l'equivalente bash degli array di awk (L3 §11.3). Vanno dichiarati con `declare -A`.

### 12.3 `printf` invece di `echo`

`echo` ha comportamenti diversi tra shell e versioni (L1, Esempio 2) e non sa stampare in modo sicuro una stringa che inizia con `-`. `printf` è definito da POSIX e fa tutto ciò che serve:

```
$ printf '%s\n' "$x"                   # stampa x così com'è, sempre
$ printf '%-10s|%5d|%x\n' nome 42 255  # colonne, numeri, esadecimale
nome      |   42|ff
$ printf '%q\n' "a b" $'x\ny'          # %q: forma quotata riusabile come input della shell
a\ b
$'x\ny'
```

Ricorda: il formato è il **primo** argomento e non deve mai contenere dati esterni (`printf "$x"` è sbagliato: se `x` contiene `%s` o `%n` il risultato è imprevedibile). Nel Modulo 4 vedremo che lo stesso errore, in C, è una delle classi di vulnerabilità più note: *format string*.

## 13. Errori, pulizia e robustezza

### 13.1 `trap`

`trap 'comandi' SEGNALE...` esegue dei comandi quando la shell riceve un segnale o in situazioni speciali (`help trap`):

| Evento | Quando |
|---|---|
| `EXIT` | all'uscita dello script, in qualunque modo (fine normale, `exit`, errore con `set -e`) |
| `ERR` | quando un comando fallisce (con le stesse eccezioni di `set -e`) |
| `INT`, `TERM`, `HUP` | Ctrl-C, `kill`, chiusura del terminale (Lezione 5) |

L'uso più importante è la **pulizia garantita** dei file temporanei:

```bash
#!/usr/bin/env bash
set -euo pipefail
tmp=$(mktemp -d)                      # directory temporanea con nome casuale (L2 §6.1)
trap 'rm -rf -- "$tmp"' EXIT          # rimossa comunque vada a finire lo script
curl -s https://example.com > "$tmp/pagina.html"
grep -o '<title>[^<]*' "$tmp/pagina.html"
```

Nota le virgolette singole attorno al comando del `trap`: `$tmp` viene espansa quando la trappola **scatta**, non quando viene definita. Con `mktemp` il nome è imprevedibile, e questo evita gli attacchi con link in `/tmp` descritti nella Lezione 2 (§9.5).

### 13.2 Una lista di controllo per ogni script

1. Shebang giusto (`#!/usr/bin/env bash` se usi funzioni di bash).
2. `set -euo pipefail`, conoscendone i limiti (§7.3).
3. **Ogni** espansione tra virgolette doppie: `"$x"`, `"$@"`, `"$(cmd)"`, `"${a[@]}"`.
4. `[[ ]]` e `(( ))` invece di `[ ]`.
5. `--` prima di nomi di file che vengono da fuori; `./` davanti ai glob (L1 §6.2, L2 §14.4).
6. Lettura delle righe con `while IFS= read -r`; nomi di file con `-print0` e `read -d ''`.
7. File temporanei con `mktemp` e `trap ... EXIT`.
8. Messaggi d'errore su stderr, codici di uscita significativi.
9. `shellcheck` prima di considerarlo finito.

---

# Parte IV — Sicurezza

## 14. Gli script come superficie d'attacco

Gli script di shell sono ovunque nei sistemi reali: avvio dei servizi, backup notturni, *cron*, installatori, CGI di vecchi siti web, *hook* di Git, pipeline di integrazione continua. Molti girano con privilegi elevati e ricevono dati dall'esterno: nomi di file, parametri, variabili d'ambiente, contenuto di file. Questa sezione elenca i difetti che, nella pratica e nelle sfide, trasformano uno script in una vulnerabilità. Ognuno ha una correzione precisa.

### 14.1 Variabili non quotate

```bash
rm $file          # con file='* ' o file='-rf /qualcosa', fa ben altro che eliminare un file
```

La divisione in parole e il globbing (L1 §8.6–8.7) trasformano un **dato** in **più argomenti**, magari in opzioni. Correzione: `rm -- "$file"`. È la causa più comune di bug negli script, ed è ciò che ShellCheck segnala per primo.

### 14.2 `eval` e `bash -c` con dati esterni

`eval "stringa"` esegue la stringa come **codice** di shell; lo stesso fanno `bash -c "$x"`, `sh -c`, e la funzione C `system()` (L1 §10.4).

```
$ x="1; echo INIETTATO"
$ eval "echo valore=$x"
valore=1
INIETTATO
```

È un'**iniezione di comandi** (CWE-78; con `eval` anche CWE-95, *Eval Injection*). La correzione quasi sempre è **non usare `eval`**: per scegliere una variabile per nome c'è `${!nome}` o `declare -n`; per costruire un comando con argomenti variabili c'è un array (§12.1). Se un dato deve davvero entrare in un comando per `sh -c`, si passa come **argomento** e non come testo: `sh -c 'grep -- "$1" file' _ "$x"`.

### 14.3 Iniezione aritmetica

Questo è meno noto ed è importante: nel contesto aritmetico di bash (`(( ))`, `$(( ))`, `[[ … -eq … ]]`, gli indici degli array, `let`), il **valore** di una variabile viene valutato a sua volta come espressione, e un indice di array come `a[$(comando)]` esegue la sostituzione di comando.

```
$ x='a[$(echo ESEGUITO >&2)]'
$ (( x == 1 ))
ESEGUITO
$ [[ $x -eq 1 ]]
ESEGUITO
$ [ "$x" -eq 1 ]          # il comando [ non valuta espressioni: solo errore, nessuna esecuzione
```

Un dato esterno che finisce in un confronto numerico può quindi eseguire comandi, anche se è perfettamente quotato. Correzione: **convalidare prima** che sia davvero un numero, con una regex ancorata: `[[ $x =~ ^[0-9]+$ ]] || exit 1`, e solo dopo usarlo in `(( ))`.

### 14.4 File temporanei prevedibili

`tmp=/tmp/backup.$$` sembra unico, ma un PID è indovinabile, e un altro utente può creare il file prima, magari come link simbolico (L2 §9.5, CWE-377). Correzione: `mktemp`, `mktemp -d`, e `trap` per la pulizia (§13.1).

### 14.5 Ambiente e `PATH` negli script privilegiati

Uno script eseguito con privilegi eredita l'ambiente di chi lo lancia, se nessuno lo ripulisce: `PATH`, `IFS`, `BASH_ENV`, `ENV`, variabili di localizzazione (L1 §12.3). Correzione: impostare all'inizio un `PATH` fisso (`PATH=/usr/sbin:/usr/bin:/sbin:/bin`), usare percorsi assoluti per i comandi critici, e lasciare che `sudo` ripulisca l'ambiente (è il suo comportamento predefinito, `env_reset`).

### 14.6 Dati riservati negli argomenti

```bash
mysql -u admin -pSegreto123 ...     # la password è in argv
```

Gli argomenti di ogni processo sono leggibili da **tutti** gli utenti in `/proc/<PID>/cmdline` e con `ps` (L2 §12.2, Lezione 5), finché il processo gira. Lo stesso vale, con meno esposizione, per l'ambiente (`/proc/<PID>/environ`, leggibile dal proprietario). È CWE-214 (*Invocation of Process Using Visible Sensitive Information*). Correzione: passare i segreti attraverso un file con permessi stretti, lo stdin, o un descrittore dedicato. In gara vale il contrario: `ps aux` o un ciclo su `/proc/*/cmdline` possono mostrarti la password che un altro processo ha passato in chiaro.

### 14.7 Script setuid e script scrivibili

Su Linux il kernel **ignora il bit setuid sugli script** con shebang (lo onora solo sugli eseguibili ELF). La ragione è storica e istruttiva: tra il momento in cui il kernel legge lo shebang e il momento in cui l'interprete **riapre lo script per nome**, un attaccante può sostituire il file (ad esempio con un link simbolico verso un altro script): una TOCTOU (L2 §9.5) che per anni ha reso insicuri gli script setuid sui sistemi che li permettevano. Per dare privilegi a uno script si usa invece `sudo` con una regola precisa (Lezione 6).

Il difetto che si trova invece spessissimo nei laboratori di *privilege escalation* è più banale: uno script eseguito da root (da *cron* o da `sudo`) che è **scrivibile** da un utente normale, o che si trova in una directory scrivibile, o che richiama un altro script scrivibile. Chi può modificare lo script decide che cosa esegue root (CWE-732, *Incorrect Permission Assignment for Critical Resource*). Lo analizzeremo con i permessi nella Lezione 6 e nel Modulo 8.

Il filo comune delle tre lezioni precedenti si conferma: **ogni volta che un dato attraversa un confine** (diventa argomento, codice, espressione aritmetica, nome di file, riga di un altro script) bisogna chiedersi se verrà interpretato come dato o come istruzione.

---

# Parte V — La pratica

## 15. Esempi svolti

### Esempio 1 — Vedere le redirezioni nel kernel

```
$ ls -l /proc/self/fd > fd.txt 2>&1 3< /etc/hostname; cat fd.txt
lrwx------ 1 hacker hacker 64 ... 0 -> /dev/pts/0
l-wx------ 1 hacker hacker 64 ... 1 -> /home/hacker/l4/fd.txt
l-wx------ 1 hacker hacker 64 ... 2 -> /home/hacker/l4/fd.txt
lr-x------ 1 hacker hacker 64 ... 3 -> /etc/hostname
lr-x------ 1 hacker hacker 64 ... 4 -> /proc/12345/fd
```

`ls` elenca i **propri** descrittori (`self` è `ls`, L2 §12.2): 1 e 2 puntano a `fd.txt` (caso A del §2.2), 3 a `/etc/hostname` aperto in lettura (`lr-x`: i permessi del link dicono la modalità di apertura), 4 è la directory che `ls` stesso sta leggendo. Ogni redirezione del §2 si può verificare così.

### Esempio 2 — Solo gli errori in una pipe

```
$ find / -name 'passwd' 2>&1 >/dev/null | grep -c 'Permission denied'
37
```

Ordine delle redirezioni (§2.2): prima `2>&1` copia nel 2 la pipe (che in quel momento è l'1), poi `>/dev/null` sposta l'1 su `/dev/null`. Nella pipe arrivano solo gli errori.

### Esempio 3 — Uno script completo e robusto

```bash
#!/usr/bin/env bash
# trovaflag.sh — cerca flag in un albero di directory e le salva, senza duplicati
set -euo pipefail

uso() { echo "uso: $0 [-p PREFISSO] DIRECTORY..." >&2; exit 2; }

prefisso='[A-Za-z0-9_]+'
while getopts "p:" opt; do
    case $opt in
        p) prefisso=$OPTARG ;;
        *) uso ;;
    esac
done
shift $((OPTIND - 1))
(( $# > 0 )) || uso

tmp=$(mktemp)
trap 'rm -f -- "$tmp"' EXIT

for dir in "$@"; do
    if [[ ! -d $dir ]]; then
        echo "salto '$dir': non è una directory" >&2
        continue
    fi
    find "$dir" -type f -print0 |
        xargs -0 grep -aohE -- "${prefisso}\{[^}]*\}" >> "$tmp" || true
done

sort -u -- "$tmp"
```

Che cosa mostra: `getopts` per le opzioni; una funzione `uso` che stampa su stderr ed esce con 2; `(( $# > 0 ))` per gli argomenti obbligatori; `mktemp` e `trap` per il file temporaneo; un controllo sul tipo con `[[ -d ]]`; `find -print0 | xargs -0` per i nomi ostili; `grep -a` per i binari, `-o` per le sole corrispondenze, `-h` per non stampare i nomi dei file, `--` prima del modello; `|| true` perché `grep` restituisce 1 quando non trova nulla, e con `set -e` e `pipefail` questo fermerebbe lo script (§7.3). La pipe può andare a capo dopo `|` senza backslash.

### Esempio 4 — Il conteggio che sparisce

```bash
n=0
grep -o 'x' file | while read -r _; do n=$((n + 1)); done
echo "$n"            # stampa 0: il ciclo girava in una subshell (§4.4)

n=0
while read -r _; do n=$((n + 1)); done < <(grep -o 'x' file)
echo "$n"            # stampa il numero giusto
```

### Esempio 5 — Un "server" e un "client" con una FIFO

```bash
mkfifo richieste
# terminale 1: il "server" legge una riga alla volta e risponde
while IFS= read -r r; do echo "ricevuto: $r"; done < richieste
# terminale 2: il "client"
echo "ciao" > richieste
```

Il server si blocca in `open` finché un client non apre la FIFO in scrittura (§5.4), poi legge fino a EOF, cioè finché l'ultimo scrittore non chiude. Con un solo `echo` il ciclo legge una riga e termina; per un server che resta in ascolto lo si racchiude in un `while true`.

### Esempio 6 — Dialogare con un programma interattivo

Il gioco `indovina.sh`, nella cartella della lezione, pensa un numero tra 1 e 1.000.000 e risponde `più alto` o `più basso` a ogni tentativo, con un massimo di 25. A mano è faticoso; con una **ricerca binaria** servono al massimo 20 tentativi (2^20 > 1.000.000), e con un coprocesso lo script può giocare da solo:

```bash
#!/usr/bin/env bash
coproc G { bash indovina.sh; }
IFS= read -r intro <&"${G[0]}"; echo "$intro"
lo=1; hi=1000000
while (( lo <= hi )); do
    mid=$(( (lo + hi) / 2 ))
    echo "$mid" >&"${G[1]}"                          # scrive nello stdin del gioco
    IFS= read -r risposta <&"${G[0]}" || break        # legge dallo stdout del gioco
    echo "$mid -> $risposta"
    case $risposta in
        "più alto")  lo=$((mid + 1)) ;;
        "più basso") hi=$((mid - 1)) ;;
        giusto*)     break ;;
    esac
done
```

```
...
23734 -> più alto
23738 -> più basso
23736 -> giusto in 19 tentativi
```

È lo schema di tutte le sfide con un servizio da "battere": leggere una domanda, calcolare la risposta, scriverla, ripetere. Funziona perché il gioco è uno script bash, il cui `echo` scrive subito; con un programma C a buffer pieno (§3.2) servirebbe `stdbuf` o un pseudo-terminale. Nella Lezione 8 lo rifaremo con `pwntools`, e nella Lezione 10 attraverso la rete.

## 16. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire `Soluzioni.md`. Lavora in una directory di prova (`mkdir ~/l4 && cd ~/l4`). Per ogni script che scrivi, se puoi, passalo a `shellcheck`.

### ★ Base

1. Con il comando `ls /etc/passwd /nonesiste`: (a) manda l'output in `out.txt` e gli errori in `err.txt`; (b) manda entrambi in `tutto.txt` nel modo corretto, in due forme diverse; (c) butta via tutto; (d) prova `ls /etc/passwd /nonesiste > f 2> f` e spiega il contenuto di `f` con il §2.2.
2. **Previsione.** Per ciascuno di questi comandi, scrivi su carta che cosa compare sul terminale e che cosa finisce nel file o nella pipe; poi verifica.
   (a) `ls /etc/passwd /nonesiste 2>&1 > f`  (b) `ls /etc/passwd /nonesiste > f 2>&1`  (c) `ls /etc/passwd /nonesiste 2>/dev/null | wc -l`  (d) `ls /etc/passwd /nonesiste 2>&1 | wc -l`  (e) `ls /etc/passwd /nonesiste 2>&1 >/dev/null | wc -l`
3. **Here-document.** Con un solo comando `cat` e un here-document, crea `config.txt` che contiene la riga `home=` seguita dalla tua home **espansa**. Con un secondo here-document crea `script.sh` che contiene **letteralmente** la riga `echo "$HOME"`. Poi usa un here-string per passare la parola `segreto` a `rev`.
4. **Pipeline.** Esegui `cat /nonesiste | sort | wc -l` e stampa subito dopo `PIPESTATUS`. Ripeti con `set -o pipefail` e confronta `$?`. Poi esegui `yes | head -n 1` con e senza `pipefail` e spiega il 141.
5. **Primo script.** Scrivi `info.sh` che: (a) se non riceve esattamente un argomento, stampa un messaggio d'uso su stderr ed esce con 2; (b) altrimenti stampa utente, nome della macchina, directory corrente, e quante voci (file nascosti compresi) contiene la directory passata come argomento; (c) esce con 1 se l'argomento non è una directory.

### ★★ Intermedio

6. **Descrittori con `exec`.** Scrivi uno script che apre `log.txt` sul descrittore 3 in **aggiunta**, vi scrive tre righe con data e ora (`date '+%F %T'`), e lo chiude. Poi, nello stesso script, apre `log.txt` in lettura sul descrittore 4 e ne legge **solo** le prime due righe con `read -u 4`. Verifica con `ls -l /proc/$$/fd` (dentro lo script) che i descrittori siano aperti quando ti aspetti.
7. **Il `read` che non funziona.** Dimostra che `echo 42 | read n; echo "$n"` non stampa 42. Spiega il perché in termini di processi, e correggi in **tre** modi diversi.
8. **Leggere davvero tutte le righe.** Crea un file con `printf '  spazi davanti\nback\\slash\n-n\nultima senza a capo' > difficile.txt`. Confronta l'output di `while read l; do echo $l; done < difficile.txt` con quello della forma corretta del §10.3, e spiega **ogni** differenza.
9. **Condizioni.** Scrivi `tipo.sh` che, per ogni argomento, stampa una tra: `non esiste`, `link simbolico -> DESTINAZIONE`, `directory`, `eseguibile`, `vuoto`, `archivio` (se il nome finisce in `.zip`, `.tar.gz`, `.tgz`), `file`. Usa `[[ ]]` per i test e `case` per le estensioni. In quale ordine devono stare i controlli, e perché il controllo del link va fatto per primo?
10. **Funzioni.** Scrivi una funzione `massimo` che stampa il massimo dei suoi argomenti, rifiuta (codice 1, messaggio su stderr) qualunque argomento che non sia un intero, e usa solo variabili `local`. Mostra che una variabile `i` dello script non viene toccata da un ciclo `for i` dentro la funzione.
11. **Strumenti di flusso.** (a) Con la sostituzione di processo, mostra quali file sono in `/bin` ma non in `/sbin` (usa `comm`). (b) Conta il totale delle righe di tutti i file `.conf` in `/etc`, in modo sicuro con qualunque nome. (c) In una catena che conta le parole di `/etc/services`, salva con `tee` la lista intermedia delle parole prima del conteggio. (d) Mostra con un esempio la differenza tra `xargs` e `xargs -0` su un nome di file che contiene uno spazio.
12. **Buffering.** Riproduci l'esempio Python del §3.2. Poi correggilo in due modi. Infine spiega perché `tail -f log | grep ERRORE | awk '{print $1}'` può non mostrare nulla per molto tempo anche se gli errori arrivano, e come si risolve.

### ★★★ Sfida

13. **Il gioco.** Studia l'Esempio 6 e il gioco `indovina.sh`. (a) Spiega perché la ricerca binaria richiede al massimo 20 tentativi. (b) Riscrivi il risolutore **senza** `coproc`, usando una named pipe come nell'ultima parte del §5.4: disegna su carta dove scrive e da dove legge ogni processo. (c) Che cosa succederebbe se il gioco fosse un programma C che usa `printf` senza `fflush`, e come lo risolveresti?
14. **Mini-CTF.** Nella cartella di questa lezione c'è `setup_sfida.sh`. Eseguilo con `bash setup_sfida.sh`: crea `~/l4_sfida` con quattro programmi. **Non leggerne il codice**: usali. Leggi `LEGGIMI.txt` e ricostruisci la flag `L4{...}`. Il quarto pezzo richiede uno script che dialoga con un programma.
15. **Iniezione aritmetica.** (a) Riproduci l'esempio del §14.3. (b) Scrivi una funzione `controlla_pin` che riceve un PIN e stampa `ok` se vale 1234, in modo che **nessun** input possa eseguire comandi. (c) Spiega perché `[ "$x" -eq 1234 ]` non esegue il comando ma `[[ $x -eq 1234 ]]` sì.
16. **Revisione di sicurezza.** Questo script viene eseguito ogni notte da root tramite *cron*, e il file è di proprietà di root con permessi `rwxrwxrwx`. Trova **almeno sei** problemi, indica per ciascuno la classe (CWE dove possibile) e scrivi la versione corretta.
    ```bash
    #!/bin/sh
    # backup.sh
    DEST=/tmp/backup_$(date +%F)
    mkdir $DEST
    for u in $(ls /home); do
        tar czf $DEST/$u.tgz /home/$u
    done
    eval "echo backup completato in $DEST per $(cat /etc/backup_note)"
    curl -u admin:Password123 -T $DEST/*.tgz ftp://backup.interno/
    ```
17. **Teoria.** (a) Spiega, partendo dalle chiamate di sistema `pipe`, `fork`, `dup2`, `close` ed `execve`, perché un lettore di una pipe può restare bloccato per sempre se uno dei processi dimentica di chiudere l'estremità di scrittura. (b) Spiega perché il kernel Linux ignora il bit setuid sugli script, descrivendo la TOCTOU che ne deriverebbe. (c) Spiega in che senso `sudo echo x >> /etc/file` "non usa sudo", e due modi corretti di farlo.

### Allenamento su pwn.college

Nel dojo **Linux Luminarium** completa *Practicing Piping* (tutte le sfide su redirezioni, `tee`, sostituzione di processo, named pipe) e *Shell Variables* nella parte su `read`. Il modulo *Chaining Commands* allena liste e script. Annota per ogni sfida il comando risolutivo e la sezione corrispondente.

## 17. Domande di autoverifica

1. Che cos'è un descrittore di file? Che cosa c'è tra il numero e l'inode, e che cosa vuol dire che due descrittori condividono l'offset?
2. Perché un programma "sa" dove trovare il suo input e dove scrivere il suo output, senza che nessuno glielo dica?
3. Spiega con `dup2` la differenza tra `cmd >f 2>&1` e `cmd 2>&1 >f`.
4. Che cosa fanno `<<EOF`, `<<'EOF'`, `<<-EOF` e `<<<`?
5. Quali sono le regole di buffering di stdout e stderr? Perché un programma si comporta diversamente in una pipe?
6. Descrivi i passi che la shell compie per eseguire `a | b`. Perché i due comandi girano in parallelo?
7. Quando un lettore di una pipe vede EOF? Che cosa succede allo scrittore se il lettore termina prima? Che codice di uscita ne risulta?
8. Perché `echo x | read v` non imposta `v`? Dai due soluzioni.
9. Qual è la differenza tra `[ ]`, `[[ ]]` e `(( ))`? Quando usi ciascuno?
10. Scrivi la forma corretta per leggere un file riga per riga e spiega ogni suo pezzo.
11. Che cosa restituisce `return` in una funzione, e come si restituisce un dato?
12. Quali sono i limiti di `set -e`? Fai due esempi.
13. A che cosa servono `trap ... EXIT` e `mktemp`?
14. Elenca quattro difetti di sicurezza tipici degli script e la correzione di ciascuno.

## 18. Riepilogo

- Un descrittore è un indice nella tabella dei file aperti del processo; 0, 1 e 2 sono stdin, stdout e stderr per convenzione, ereditati dal padre.
- Le redirezioni sono `open` più `dup2`, applicate da sinistra a destra: `2>&1` copia, non collega.
- Lo stdout è a righe su un terminale e a buffer pieno altrove; lo stderr non ha buffer. Questo cambia l'ordine dell'output e può bloccare il dialogo con un programma.
- Una pipe è un buffer del kernel tra due processi che girano in parallelo; EOF arriva quando tutti gli scrittori chiudono; chi scrive senza lettori riceve `SIGPIPE`. Ogni pezzo di una pipeline è una subshell.
- `tee`, `xargs`, la sostituzione di processo, le FIFO e i coprocessi permettono di costruire flussi complessi, fino a dialogare con un programma interattivo.
- Uno script robusto: shebang giusto, `set -euo pipefail` con giudizio, ogni espansione quotata, `[[ ]]` e `(( ))`, `while IFS= read -r`, funzioni con `local`, array per le liste di argomenti, `mktemp` e `trap`.
- Le vulnerabilità degli script nascono quando un dato diventa codice: divisione in parole, `eval`, contesto aritmetico, file temporanei, ambiente, segreti negli argomenti, permessi di scrittura.

## 19. Fonti

- **OccupyTheWeb**, *Linux Basics for Hackers*, cap. 8 (*Bash Scripting*): il primo script, variabili, `read`, `if`, un semplice scanner di porte come esercizio.
- **pwn.college**, *Linux Luminarium*, moduli *Practicing Piping*, *Chaining Commands*, *Shell Variables*; trascrizione 078 *CSE 365 — Data Dealings and Access Control* per l'introduzione alle pipe nel corso.
- **R. e A. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces*, cap. 5 (*Process API*: `fork`, `exec`, e il paragrafo sulla costruzione delle redirezioni e delle pipe nella shell) e cap. 39 (descrittori e tabella dei file aperti).
- **R. E. Bryant, D. R. O'Hallaron**, *Computer Systems: A Programmer's Perspective*, cap. 10 (*System-Level I/O*: descrittori, tabella dei file aperti, `dup2`, buffering dello standard I/O) e cap. 8.4 (controllo dei processi).
- **GNU Bash Reference Manual** (`man bash`): *REDIRECTION*, *Pipelines*, *Coprocesses*, *Process Substitution*, *CONDITIONAL EXPRESSIONS*, *ARITHMETIC EVALUATION*, *Arrays*, `set`, `trap`, `read`, `getopts`, `mapfile`.
- **Pagine di manuale**: `pipe(2)`, `pipe(7)`, `dup2(2)`, `open(2)`, `fifo(7)`, `setvbuf(3)`, `stdbuf(1)`, `xargs(1)`, `tee(1)`, `mktemp(1)`.
- **ShellCheck** (shellcheck.net) e il suo wiki, che spiega ogni avviso con esempi; **BashFAQ** e **BashPitfalls** di Greg Wooledge (mywiki.wooledge.org), in particolare *How can I read a file line-by-line?* e *Why doesn't set -e do what I expected?*.
- **MITRE CWE**: CWE-78, CWE-95, CWE-214, CWE-377, CWE-403, CWE-732.

## 20. Prossima lezione

**Lezione 5 — Processi e ambiente**: PID e PPID, `ps` e `top`, il contenuto di `/proc/<PID>`, i segnali e `kill`, il *job control* (`&`, `fg`, `bg`, Ctrl-Z), il ciclo `fork`/`exec`/`wait` visto dal lato dei processi, e che cosa un figlio eredita dal padre. Tutto ciò che in queste lezioni abbiamo chiamato "processo figlio" diventerà un oggetto da osservare e controllare.
