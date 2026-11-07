# Modulo 1 — Lezione 1: La riga di comando

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 1 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 12).

## 0. Obiettivi, prerequisiti, piano della lezione

**Al termine della lezione sarai in grado di:**

1. descrivere i livelli che separano la tastiera dal kernel (terminale, pseudo-terminale, shell, chiamate di sistema) e spiegare che cosa accade tra il tasto Invio e l'output;
2. descrivere il ciclo di vita di una shell e la differenza tra shell interattive e non interattive, di login e non di login, con i relativi file di avvio;
3. scomporre una riga secondo la grammatica di bash: metacaratteri, operatori, comandi semplici, liste;
4. prevedere con esattezza il vettore `argv` che un programma riceverà, applicando nell'ordine giusto le otto espansioni della shell;
5. spiegare come la shell risolve il nome di un comando (alias, parole chiave, funzioni, builtin, `PATH`, tabella hash) e come il kernel esegue un file (`execve`, shebang);
6. interpretare il codice di uscita di un programma, anche quando è stato terminato da un segnale;
7. distinguere variabili di shell, variabili d'ambiente e parametri speciali, e spiegare perché l'ambiente è un input controllato da chi lancia il programma;
8. trovare da solo la documentazione di qualunque comando e leggere correttamente la sezione *SYNOPSIS* di una pagina di manuale;
9. osservare la shell al lavoro con `set -x` e `strace`.

**Prerequisiti:** nessuno. Serve un ambiente Linux con `bash` 4 o successivo: il dojo di pwn.college (dal browser), una macchina virtuale (Debian, Ubuntu, Kali) o WSL2 su Windows.

**Tempo:** circa 4 ore di lettura e prove al terminale, 3–4 ore di esercizi. È la lezione più lunga del modulo perché tutte le successive ne usano il vocabolario.

**Come studiare questa lezione.** Tieni un terminale aperto accanto al testo e digita ogni esempio: la shell si impara con le dita, non con gli occhi. Quando un esempio non dà l'output previsto, fermati e capisci perché prima di andare avanti: nove volte su dieci la differenza è proprio il punto che la sezione vuole insegnare.

**Convenzione tipografica.** Le righe che iniziano con `$ ` sono comandi da digitare senza il `$`; le righe senza prefisso sono output; il testo dopo `#` in un comando è un commento, e la shell lo ignora.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. Il contesto | 1–4 | Che cos'è la shell, da dove viene, come vive? |
| II. La grammatica | 5–9 | Come viene letta e trasformata una riga? |
| III. L'esecuzione | 10–12 | Come diventa un processo, e come ne leggo il risultato? |
| IV. Gli strumenti | 13–15 | Come trovo documentazione, lavoro veloce, osservo cosa accade? |
| V. La pratica | 16–19 | Esempi svolti, esercizi, autoverifica, fonti |

---

# Parte I — Il contesto

## 1. Perché la riga di comando

Le interfacce grafiche sono comode per compiti che si fanno una volta. La riga di comando vince in tre situazioni che, nella sicurezza informatica, sono la norma.

1. **Accesso remoto.** Un server, un container, una macchina compromessa in un laboratorio, il servizio di una sfida CTF raggiunto con `nc` o `ssh`: quasi mai c'è una grafica. C'è un flusso di testo in entrata e uno in uscita.
2. **Composizione.** I programmi Unix sono progettati per essere combinati: l'output di uno diventa l'input del successivo (le *pipe*, Lezione 4). Un compito complesso diventa una riga.
3. **Ripetibilità.** Una riga di comando si può salvare, rileggere, rieseguire su mille file, mettere in uno script. Un clic no.

Doug McIlroy, l'inventore delle pipe, riassunse la cosiddetta *filosofia Unix* in tre regole: scrivi programmi che facciano una cosa sola e la facciano bene; scrivi programmi che lavorino insieme; scrivi programmi che gestiscano flussi di testo, perché è un'interfaccia universale. Ogni strumento che incontrerai in questo modulo (`grep`, `sort`, `xxd`, `nc` …) è costruito così, ed è per questo che si combinano.

**Una nota di etica, prima di cominciare.** Le prime lezioni del corso di pwn.college (trascrizioni 092–095, *Cybersecurity Ethics* e seguenti) insistono su un punto che vale anche qui: le tecniche di questo corso si applicano **solo** a sistemi di tua proprietà, ad ambienti di allenamento come il dojo, e alle infrastrutture delle competizioni, che esistono proprio per essere attaccate. La stessa riga di comando che apre un file in una sfida può causare danni reali su un sistema altrui, ed è un reato anche in Italia (art. 615-ter c.p., accesso abusivo a un sistema informatico).

## 2. Dalla tastiera al kernel: i livelli

### 2.1 Il kernel e le chiamate di sistema

Il processore di un computer moderno funziona in almeno due **modalità di privilegio**. In *modalità kernel* il codice può fare qualunque cosa: accedere a tutta la memoria, programmare le periferiche, gestire le interruzioni. In *modalità utente* il codice è confinato: non può toccare direttamente il disco, la rete o la memoria di altri programmi. Su x86-64 queste modalità corrispondono agli *anelli di protezione* 0 e 3; li studieremo nel Modulo 2.

Il **kernel** è il programma che gira in modalità kernel. Tutti gli altri programmi, compresa la shell, girano in modalità utente e, quando hanno bisogno di qualcosa che non possono fare da soli (aprire un file, creare un processo, scrivere sul terminale), lo chiedono al kernel con una **chiamata di sistema** (*system call*, o *syscall*): un'istruzione speciale del processore che passa il controllo al kernel in un punto d'ingresso prestabilito. Linux offre circa 370 chiamate di sistema su x86-64 (la tabella `asm/unistd_64.h` di un kernel 6.x ne elenca 373; ogni versione ne aggiunge qualcuna, e alcune vecchie restano solo per compatibilità); quelle che conteranno di più in questo corso sono `read`, `write`, `open`, `close`, `fork` (o `clone`), `execve`, `wait4`, `exit`.

Un **processo**, nella definizione del libro OSTEP (cap. 4), è un *programma in esecuzione*: il codice del programma più lo stato che il kernel gli associa, cioè la memoria, i registri, i file aperti, la directory corrente, l'utente per conto del quale gira, l'ambiente. La shell è un processo; ogni comando esterno che lanci diventa un altro processo.

### 2.2 Terminale, TTY e pseudo-terminale

Il **terminale** era in origine un dispositivo fisico: una telescrivente (*teletypewriter*, da cui l'abbreviazione **TTY**), poi un video-terminale come il VT100, collegato al computer da una linea seriale. Oggi è un programma, l'**emulatore di terminale** (GNOME Terminal, Windows Terminal, xterm, la scheda del dojo), che imita quei dispositivi.

Tra l'emulatore e la shell il kernel inserisce uno **pseudo-terminale** (PTY): una coppia di file speciali, il lato *master* tenuto dall'emulatore e il lato *slave* (`/dev/pts/N`) dato alla shell come input e output. Il kernel, in mezzo, applica la **disciplina di linea**: in modalità "canonica" raccoglie i caratteri finché non premi Invio, gestisce il tasto Backspace, e trasforma alcune combinazioni di tasti in **segnali**, per esempio Ctrl-C in `SIGINT` per il programma in primo piano. Per questo Ctrl-C funziona anche con un programma che non lo gestisce: non è il programma a leggere il tasto, è il kernel a interromperlo.

```
$ tty
/dev/pts/0
```

**Rilevanza in gara.** Quando ottieni una shell su una macchina remota attraverso una semplice connessione di rete (una *reverse shell*, nei laboratori), non c'è un PTY: niente Ctrl-C che interrompe il comando, niente completamento, niente editor a pieno schermo. Per questo nei writeup si vede spesso il comando `python3 -c 'import pty; pty.spawn("/bin/bash")'`, che crea un pseudo-terminale. Adesso sai che cosa sta aggiungendo.

### 2.3 La shell

La **shell** è un normale programma in modalità utente, come `ls` o `cat`, con un compito preciso: leggere comandi (dal terminale, da un file o da una stringa), interpretarli secondo la propria grammatica, e farli eseguire. Il nome viene dall'idea di un *guscio* che avvolge il kernel e lo rende usabile. Esistono molte shell: `sh` (standard POSIX; su Debian e Ubuntu è implementata da `dash`, minimale e veloce), `bash` (la più diffusa sui sistemi Linux), `zsh` (predefinita su macOS), `fish`, `ksh`. Questo corso usa `bash`; quando qualcosa è specifico di bash e non vale per `sh`, lo segnaliamo.

Il quadro completo:

```
  tu ──tasti──▶ emulatore di terminale ──▶ PTY master
                                              │  (kernel: disciplina di linea, segnali)
                                           PTY slave /dev/pts/N
                                              │
                                            shell (bash) ──fork/execve──▶ processo del comando
                                              │                                 │
                                              └──────── chiamate di sistema ────┴──▶ KERNEL ──▶ hardware
```

### 2.4 Che cosa succede quando premi Invio

Prendiamo `echo hello hackers`, l'esempio con cui si apre la trascrizione di pwn.college *Linux Luminarium 1 — The Command Line*, e seguiamolo per intero.

1. Digiti i caratteri; l'emulatore li scrive nel PTY; la disciplina di linea li accumula e, al tasto Invio, li rende disponibili alla shell, che li riceve con una `read`.
2. La shell **analizza** la riga (Parte II): la divide in *token*, riconosce un comando semplice, applica le espansioni. Ottiene le parole `echo`, `hello`, `hackers`.
3. La shell **risolve** il nome `echo` (§10): è un builtin, quindi lo esegue lei stessa, senza creare processi. Se il comando fosse esterno, come `cat`, la shell creerebbe un processo figlio (`fork`), e il figlio sostituirebbe se stesso con il programma `/usr/bin/cat` (`execve`), ricevendo le parole come `argv`.
4. Il comando scrive `hello hackers\n` sul descrittore 1 (lo *standard output*), che è collegato al PTY; l'emulatore lo disegna.
5. La shell attende la fine del figlio (`wait`), ne registra il **codice di uscita** (§11) e stampa di nuovo il prompt.

Questi cinque passi sono il filo conduttore della lezione: le sezioni seguenti approfondiscono ciascuno di essi.

## 3. Un po' di storia (con una correzione)

Nella trascrizione di pwn.college il docente ricorda che il termine *shell* nasce con **Multics** e che Linux è nato come progetto amatoriale di Linus Torvalds, presentandolo come una versione amatoriale di Multics. La seconda parte non è esatta. La catena storica corretta è questa.

| Anno | Sistema o programma | Autori | Che cosa ha introdotto |
|---|---|---|---|
| 1964–69 | **Multics** | MIT, Bell Labs, General Electric | sistema a condivisione di tempo; Louis Pouzin vi formalizza l'idea di *shell* come programma separato che interpreta i comandi |
| 1969– | **Unix** | Ken Thompson, Dennis Ritchie (Bell Labs) | sistema volutamente più semplice, nato dopo l'uscita dei Bell Labs da Multics; file system gerarchico, "tutto è un file", processi leggeri |
| 1971 | *Thompson shell* | Ken Thompson | prima shell di Unix; redirezioni `<` e `>` |
| 1973 | pipe | Doug McIlroy, Ken Thompson | l'operatore `|` (Lezione 4) |
| 1979 | **Bourne shell** `sh` | Stephen Bourne | variabili, strutture di controllo, script: la base della sintassi di oggi |
| 1983–88 | progetto GNU, standard POSIX | Richard Stallman; IEEE | strumenti liberi compatibili con Unix; standard comune per shell e utility (POSIX.1, 1988; la shell in POSIX.2, 1992) |
| 1989 | **bash** (*Bourne-Again SHell*) | Brian Fox, poi Chet Ramey | shell GNU compatibile con `sh`, con storia, completamento, array |
| 1991 | **Linux** | Linus Torvalds | un **kernel** scritto da zero, ispirato a Minix (di Andrew Tanenbaum) e compatibile con Unix |

Linux quindi non deriva direttamente da Multics: ne eredita le idee **attraverso Unix**, di cui è una reimplementazione indipendente. Un sistema "Linux" che usi tutti i giorni è il kernel Linux più gli strumenti GNU (bash, coreutils, il compilatore gcc) e molto altro software: per questo alcuni lo chiamano GNU/Linux.

La lezione da trarre, come dice lo stesso docente, è che la riga di comando è un sistema **cresciuto in modo organico**: le convenzioni sono nate in tempi diversi, da persone diverse, per problemi diversi, e poi si sono stratificate. Molte stranezze (perché `--` per le opzioni lunghe? perché `$?`?) non hanno una ragione profonda: vanno conosciute. Lo standard **POSIX** è il tentativo di fissare il nucleo comune; bash lo rispetta e lo estende.

## 4. Il ciclo di vita della shell

### 4.1 Il ciclo leggi–analizza–esegui

Una shell interattiva è, nella sua essenza, un ciclo infinito che il manuale di bash descrive in pochi passi (sezione *SHELL GRAMMAR* e seguenti):

```
ripeti:
    stampa il prompt
    leggi una riga (o più, se il comando non è finito)
    dividi la riga in token (parole e operatori)
    riconosci la struttura (comandi semplici, pipeline, liste, comandi composti)
    applica le espansioni a ogni comando semplice
    esegui le redirezioni
    esegui il comando e attendi il codice di uscita
finché non arriva la fine dell'input (Ctrl-D) o il comando exit
```

Se una riga non è completa (una virgoletta aperta, un `if` senza `fi`, una barra rovesciata finale), la shell stampa il **prompt secondario** `PS2`, per default `> `, e continua a leggere. Se vedi comparire `>` inaspettatamente, quasi sempre hai lasciato aperta una virgoletta: Ctrl-C annulla la riga.

```
$ echo "ciao
> mondo"
ciao
mondo
```

### 4.2 Interattiva o no, di login o no

Due proprietà indipendenti decidono come si comporta una shell e quali file legge all'avvio.

- **Interattiva**: legge i comandi da un terminale e parla con una persona. Mostra il prompt, abilita gli alias, la storia, il completamento, il *job control*. Una shell che esegue uno script (`bash script.sh`) o una stringa (`bash -c '...'`) è **non interattiva**.
- **Di login**: è la prima shell di una sessione (un accesso da console, `ssh`, `su -`, `bash -l`). Per convenzione il suo `argv[0]` inizia con un trattino, come `-bash`.

I file di avvio letti da bash (manuale, sezione *INVOCATION*):

| Tipo di shell | File letti all'avvio |
|---|---|
| di login (interattiva o no) | `/etc/profile`, poi il **primo** che esiste tra `~/.bash_profile`, `~/.bash_login`, `~/.profile`; all'uscita `~/.bash_logout` |
| interattiva, non di login | `~/.bashrc` (su Debian e Ubuntu anche `/etc/bash.bashrc`) |
| non interattiva | nessuno, salvo il file indicato dalla variabile `BASH_ENV` |

Di solito `~/.profile` contiene una riga che carica anche `~/.bashrc`, così le impostazioni valgono in entrambi i casi.

Tre eccezioni alla tabella, che il manuale documenta e che sorprendono spesso:

- **bash lanciata da `sshd` per un comando remoto** (`ssh host 'comando'`): la shell è non interattiva e non di login, eppure bash legge `~/.bashrc`, perché riconosce di avere lo standard input collegato a una connessione di rete. Per questo un `echo` messo in `~/.bashrc` può rompere `scp` e `rsync`, che si aspettano di parlare con il programma remoto senza testo in mezzo;
- **bash invocata come `sh`** (per esempio `/bin/sh` che punta a bash, come su alcune distribuzioni non Debian): bash imita la Bourne shell, entra in *modalità POSIX* dopo la lettura dei file di avvio, legge solo `/etc/profile` e `~/.profile` se è di login, e solo il file indicato da `ENV` se è interattiva;
- **identità reale ed effettiva diverse** (un programma setuid che lancia bash, Lezione 6): bash non legge `BASH_ENV` né `ENV` e, senza l'opzione `-p`, riporta l'identità effettiva a quella reale (§12.3).

L'opzione `--norc` salta `~/.bashrc`, `--noprofile` salta i file di login, `--rcfile file` sostituisce `~/.bashrc`. Una shell "pulita" per gli esperimenti si ottiene con `env -i bash --norc --noprofile`.

Perché conta:

- un **alias** definito in `~/.bashrc` non esiste in uno script: gli script non devono dipendere dagli alias;
- una shell ottenuta in un laboratorio attraverso un exploit è di solito **non interattiva e non di login**: niente prompt, niente `PATH` personalizzato, niente alias. Se un comando "non esiste", controlla `echo $PATH` e usa percorsi assoluti;
- i file di avvio sono eseguiti automaticamente, quindi sono un luogo classico in cui chi analizza una macchina compromessa (forensics, Modulo 7) cerca modifiche sospette. Per la stessa ragione possono contenere informazioni utili in una sfida: la storia dei comandi, variabili, percorsi.

Per sapere in che tipo di shell ti trovi:

```
$ echo $0                       # "-bash" indica una shell di login
-bash
$ [[ $- == *i* ]] && echo interattiva
interattiva
$ shopt -q login_shell && echo login
login
```

La variabile speciale `$-` contiene le opzioni attive della shell, una lettera ciascuna; `i` significa interattiva.

### 4.3 Il prompt

Il prompt è il testo che la shell stampa quando è pronta a ricevere un comando. Una forma tipica è:

```
hacker@dojo:~$
```

- `hacker` è il nome dell'utente, `dojo` il nome della macchina (*hostname*);
- `~` è la directory corrente (`~` abbrevia la tua home, per esempio `/home/hacker`);
- `$` indica un **utente normale**; `#` indica l'utente **root**, l'amministratore, che ha identificativo utente (UID) 0 (Lezione 6).

Il formato è controllato dalla variabile `PS1`, che accetta sequenze speciali:

| Sequenza | Significato |
|---|---|
| `\u` | nome utente |
| `\h` | hostname fino al primo punto |
| `\w` | directory corrente, con `~` per la home |
| `\$` | `#` se l'UID è 0, altrimenti `$` |
| `\t` | ora corrente |

```
$ echo "$PS1"
\u@\h:\w\$
$ PS1='[\t] \w > '
[17:30:12] ~ >
```

La modifica vale solo per la shell corrente: per renderla permanente va scritta in `~/.bashrc`. Nelle trascrizioni e nei writeup il prompt è spesso ridotto a `$` o `#`: quando leggi `# cat flag` il `#` non va digitato, ti dice solo che il comando è eseguito come root. Attenzione al contesto, perché lo stesso `#`, **dentro** un comando, apre un commento.

**Il prompt è un'informazione, non una garanzia.** `PS1` è una variabile come le altre e chiunque può impostarla a `root@server#`. Per sapere davvero chi sei usa `id` o `whoami`, che chiedono l'informazione al kernel.

---

# Parte II — La grammatica

## 5. Come la shell legge una riga: token, operatori, comandi

### 5.1 Metacaratteri e token

Il primo passo dell'analisi è la divisione della riga in **token**. Il manuale di bash (sezione *DEFINITIONS*) definisce:

- **blank**: spazio o tabulazione;
- **metacarattere**: un carattere che, se non è protetto da virgolette, separa le parole. Sono: spazio, tabulazione, a capo, e `|  &  ;  (  )  <  >`;
- **parola** (*word*): una sequenza di caratteri trattata dalla shell come un'unità;
- **operatore di controllo**: un token che ha una funzione di controllo: a capo, `||`, `&&`, `&`, `;`, `;;`, `|`, `|&`, `(`, `)`;
- **operatore di redirezione**: `<`, `>`, `>>`, `2>`, `<<` e simili (Lezione 4).

Conseguenza pratica: gli operatori **non** hanno bisogno di spazi intorno. `echo a;echo b` sono due comandi, perché `;` è un metacarattere. Al contrario `=` non è un metacarattere, ed è per questo che `X = 1` e `X=1` sono cose diverse (§9).

```
$ echo a;echo b
a
b
$ echo a\;echo b      # il ; protetto dal backslash è un carattere normale
a;echo b
```

Il carattere `#` all'inizio di una parola apre un **commento** che arriva fino alla fine della riga; in mezzo a una parola, come in `abc#def`, è un carattere normale.

### 5.2 Comandi semplici

L'unità di base è il **comando semplice**: una sequenza facoltativa di assegnazioni di variabili, seguita da parole e redirezioni, terminata da un operatore di controllo. Nella forma generale:

```
[NOME=valore ...] parola0 [parola1 ...] [redirezioni ...]
```

La prima parola, dopo le espansioni, è il nome del comando; le altre sono gli argomenti. Le assegnazioni iniziali, se c'è un comando, valgono **solo** per quel comando (§12).

### 5.3 Liste: sequenza e condizione

Più comandi si combinano in **liste**:

| Forma | Significato |
|---|---|
| `A ; B` (o `A` a capo `B`) | esegue A, poi B, qualunque sia il risultato di A |
| `A && B` | esegue B solo se A ha successo (codice di uscita 0) |
| `A || B` | esegue B solo se A fallisce (codice diverso da 0) |
| `A &` | esegue A in background e passa subito oltre (Lezione 5) |
| `A | B` | pipeline: l'output di A diventa l'input di B (Lezione 4) |

`&&` e `||` hanno la stessa precedenza e si associano da sinistra: `A && B || C` significa "(A && B) || C", e quindi C viene eseguito anche se A riesce ma B fallisce. Non è un vero "se–allora–altrimenti"; per quello esiste `if` (Lezione 4).

```
$ mkdir prova && cd prova && echo "sono in $PWD"
$ grep -q flag file.txt || echo "nessuna flag qui"
```

### 5.4 Comandi composti (anteprima)

Bash ha anche **comandi composti**: gruppi `{ ...; }` e `( ... )` (quest'ultimo esegue i comandi in una *subshell*, un processo figlio), condizioni `if`, cicli `for` e `while`, `case`, test `[[ ... ]]`, aritmetica `(( ... ))`. Le parole `if`, `then`, `fi`, `for`, `do`, `done`, `{`, `}` sono **parole riservate**: hanno un significato speciale solo in posizione di comando. Li tratteremo con lo scripting nella Lezione 4. Per ora basta un esempio di subshell, che useremo:

```
$ (cd /tmp; pwd); pwd
/tmp
/home/hacker
```

La `cd` dentro le parentesi cambia la directory solo del processo figlio; la shell principale resta dov'era.

## 6. Argomenti, `argv` e opzioni

### 6.1 Il vettore `argv`

Dopo le espansioni, le parole di un comando semplice diventano il **vettore degli argomenti** che il programma riceve. In C lo vedrai come `int main(int argc, char *argv[])` (Lezione 9): `argc` è il numero di elementi, `argv` un array di stringhe terminate da un byte zero.

```
$ echo hello hackers
hello hackers
```

| indice | valore |
|---|---|
| `argv[0]` | `echo` |
| `argv[1]` | `hello` |
| `argv[2]` | `hackers` |
| `argv[3]` | `NULL` (fine del vettore) |

Tre fatti fondamentali.

1. **Il programma non vede la riga di comando.** Vede solo `argv`, già diviso ed espanso, senza virgolette. Non sa se hai scritto `"a b"` o `a\ b`: in entrambi i casi riceve la stringa `a b`. Molti errori, e molte vulnerabilità, nascono dal credere che un programma veda qualcosa di diverso da ciò che vede davvero.
2. **Un argomento può contenere qualunque byte tranne lo zero.** Spazi, a capo, asterischi, trattini, caratteri di controllo: se sono protetti da virgolette, arrivano al programma così come sono. Il byte zero non può esserci perché in C segna la fine della stringa.
3. **`argv[0]` è solo una convenzione.** Di solito è il nome con cui hai chiamato il programma, ma chi lancia un processo con `execve` può metterci qualunque cosa. In bash, `exec -a nomefinto programma` lo dimostra. Per questo un programma non dovrebbe mai fidarsi di `argv[0]` per decidere chi è o dove si trova.

Come ricorda la trascrizione di pwn.college, due comandi che sembrano simili trattano gli argomenti in modo opposto:

```
$ echo flag
flag
$ cat flag
pwn.college{...}
```

`echo` stampa i propri argomenti come testo; `cat` interpreta ogni argomento come il **nome di un file** e ne stampa il contenuto. La shell non sa nulla di questa differenza: è il programma a dare un significato agli argomenti.

### 6.2 Le opzioni e le loro convenzioni

Molti argomenti non sono dati ma **opzioni** (o *flag*) che modificano il comportamento del programma. Le convenzioni sono codificate dallo standard POSIX (*Base Definitions*, cap. 12, *Utility Conventions*) ed estese da GNU:

| Convenzione | Esempio | Origine |
|---|---|---|
| opzione corta: un trattino e una lettera | `ls -l` | POSIX |
| più opzioni corte unite | `ls -la` = `ls -l -a` | POSIX |
| opzione con valore, attaccato o separato | `head -n 5`, `head -n5` | POSIX |
| `--` termina le opzioni | `rm -- -file` | POSIX |
| un solo `-` come nome di file indica lo standard input | `cat -` | convenzione diffusa |
| opzione lunga con due trattini | `ls --all`, `date --utc` | GNU |
| valore di un'opzione lunga | `--width=80` o `--width 80` | GNU |
| abbreviazione di un'opzione lunga, se non ambigua | `ls --hum` = `ls --human-readable`; `ls --al` dà errore perché è ambiguo tra `--all` e `--almost-all` | GNU |
| opzioni anche dopo gli operandi | `ls /tmp -l` | GNU (non POSIX) |

L'ultima riga merita attenzione. La funzione di libreria `getopt` di GNU riordina `argv` in modo che le opzioni vengano riconosciute anche dopo i nomi di file; lo standard POSIX invece dice che la prima parola che non inizia con `-` termina le opzioni. Con la variabile d'ambiente `POSIXLY_CORRECT` impostata, gli strumenti GNU tornano al comportamento POSIX. Ecco perché un comando può funzionare su Linux e non su macOS o su un sistema minimale come BusyBox.

La trascrizione mostra due esempi:

```
$ echo -n hello      # -n: non andare a capo alla fine
hello$
$ date --utc         # data in UTC, Coordinated Universal Time
```

**È il programma, non la shell, a decidere che cosa sia un'opzione.** La shell passa `-n` come qualunque altra parola. Questo produce il problema dei nomi di file che iniziano con un trattino (Esempio 3, Esercizio 5), un classico delle sfide *misc*. In sicurezza esiste una classe di difetti chiamata **argument injection** (CWE-88): un programma costruisce gli argomenti di un altro programma a partire da dati esterni e un nome come `--output=/percorso` viene interpretato come opzione invece che come dato. La difesa è la stessa che userai a mano: `--` prima dei dati, oppure un prefisso `./`.

### 6.3 Leggere un comando sconosciuto

Davanti a un comando mai visto in un writeup, procedi così:

1. individua la prima parola dopo le espansioni: è il programma;
2. separa le opzioni (con i loro valori) dagli operandi;
3. per ogni opzione che non conosci, consulta `man` (§13).

Esempio: `tar -xzvf archivio.tgz -C /tmp`. Programma `tar`; opzioni corte unite `x` (estrai), `z` (gzip), `v` (verboso), `f` con valore `archivio.tgz` (il file); opzione `-C` con valore `/tmp` (la directory di destinazione). Nota che `f` deve essere l'ultima del gruppo, perché la parola successiva è il suo valore.

## 7. Le virgolette

Le virgolette (*quoting*, manuale di bash, sezione *QUOTING*) servono a **togliere il significato speciale** ai caratteri: ai metacaratteri, ai simboli che attivano le espansioni (`$`, `` ` ``, `*`, `?`, `[`, `~`, `{`), alle parole riservate. Bash ne ha quattro forme.

| Forma | Che cosa resta speciale dentro | Esempio | Risultato |
|---|---|---|---|
| `\c` (backslash) | nulla: protegge il solo carattere successivo | `echo a\ \ b \$HOME` | `a  b $HOME` |
| `'...'` (singole) | **nulla**, nemmeno il backslash | `echo '$HOME \n *'` | `$HOME \n *` |
| `"..."` (doppie) | `$`, `` ` ``, `\` (solo davanti a `$`, `` ` ``, `"`, `\`, a capo); nelle shell interattive anche `!` (storia, §14.2) | `echo "$HOME   *"` | `/home/hacker   *` |
| `$'...'` (ANSI-C, bash) | le sequenze di escape del C: `\n`, `\t`, `\xHH`, `\'` | `echo $'a\tb\x41'` | `a	bA` (con una tabulazione) |

Conseguenze da memorizzare:

- **dentro le virgolette singole non si può mettere una virgoletta singola**, nemmeno con il backslash. Si chiude, si aggiunge `\'` o `"'"`, si riapre: `echo 'l'\''hacker'` stampa `l'hacker`. In alternativa `$'l\'hacker'`;
- le virgolette doppie **non** impediscono l'espansione delle variabili, ma impediscono la **divisione in parole** e il **globbing** del risultato (§8.6–8.7). È esattamente ciò che si vuole quasi sempre;
- forme diverse si possono concatenare in una sola parola, senza spazi: `echo "ciao "'$USER'" sono $USER"` produce **un** argomento, `ciao $USER sono hacker`;
- le virgolette **non arrivano al programma**: sono tolte nell'ultimo passo dell'espansione (§8.8).

Il punto chiave: le virgolette decidono **quante parole**, cioè quanti elementi di `argv`, riceverà il programma.

```
$ echo hello      hackers
hello hackers
$ echo "hello      hackers"
hello      hackers
```

Nel primo caso `echo` riceve due argomenti e li stampa separati da un solo spazio, perché è `echo` a inserire uno spazio tra gli argomenti; nel secondo riceve **un solo** argomento che contiene sei spazi.

**Regola pratica:** metti sempre tra virgolette doppie le espansioni di variabili e di comandi (`"$x"`, `"$(cmd)"`), a meno che tu non voglia esplicitamente la divisione in parole. Le espansioni non quotate sono la prima causa di bug negli script e, quando lo script gira con privilegi, di vulnerabilità.

## 8. Le espansioni

Dopo la divisione in token, e prima dell'esecuzione, bash trasforma ogni parola con una serie di **espansioni**, sempre nello stesso ordine (manuale, sezione *EXPANSION*):

| # | Espansione | Sintassi | Esempio | Risultato |
|---|---|---|---|---|
| 1 | graffe | `{a,b}`, `{1..5}` | `echo f{1,2}.txt` | `f1.txt f2.txt` |
| 2 | tilde | `~`, `~utente` | `echo ~root` | `/root` |
| 3 | parametri e variabili | `$x`, `${x}` | `echo $HOME` | `/home/hacker` |
| 4 | sostituzione di comando | `$(cmd)` | `echo $(whoami)` | `hacker` |
| 5 | aritmetica | `$((espr))` | `echo $((6*7))` | `42` |
| 6 | divisione in parole | (automatica) | | |
| 7 | nomi di file (*globbing*) | `*`, `?`, `[...]` | `echo /etc/pass*` | `/etc/passwd` |
| 8 | rimozione delle virgolette | (automatica) | | |

Le espansioni 2–5 avvengono nello stesso passaggio, da sinistra a destra (bash include in questo passaggio anche la *sostituzione di processo* `<(cmd)`, che vedremo nella Lezione 4). L'ordine spiega molti comportamenti che sembrano strani, come vedrai nei paragrafi seguenti.

### 8.1 Graffe

Genera stringhe da un modello. È puramente **testuale**: non controlla se i file esistono, a differenza del globbing.

```
$ echo {a..e} {01..03} pre{x,y}post
a b c d e 01 02 03 prexpost preypost
$ mkdir -p progetto/{src,doc,test}     # tre directory in un comando
$ cp config.txt{,.bak}                 # = cp config.txt config.txt.bak
```

Poiché avviene **prima** delle variabili, `{1..$n}` non funziona: quando le graffe vengono espanse, `$n` non è ancora stato sostituito. Si usa `seq 1 "$n"` o un ciclo aritmetico.

### 8.2 Tilde

Una `~` all'inizio di una parola diventa la home dell'utente corrente (il valore di `HOME`); `~nome` diventa la home dell'utente `nome`, letta dal database degli utenti (`/etc/passwd`, Lezione 6). Tra virgolette non viene espansa: `"~"` resta `~`, per cui negli script si preferisce `"$HOME"`.

### 8.3 Parametri e variabili

`$nome` o `${nome}` sono sostituiti dal valore. Le graffe servono quando il nome è seguito da caratteri che potrebbero farne parte (`${FLAG}college`), e abilitano un piccolo linguaggio di manipolazione delle stringhe molto utile nelle CTF:

| Forma | Effetto | Con `f=/home/hacker/archivio.tar.gz` |
|---|---|---|
| `${#f}` | lunghezza | `28` |
| `${f#*/}` | toglie il prefisso **più corto** che corrisponde al modello | `home/hacker/archivio.tar.gz` |
| `${f##*/}` | toglie il prefisso **più lungo** | `archivio.tar.gz` (come `basename`) |
| `${f%.gz}` | toglie il suffisso più corto | `/home/hacker/archivio.tar` |
| `${f%%.*}` | toglie il suffisso più lungo | `/home/hacker/archivio` |
| `${f/hacker/root}` | sostituisce la prima occorrenza | `/home/root/archivio.tar.gz` |
| `${f//a/A}` | sostituisce tutte le occorrenze | `/home/hAcker/Archivio.tAr.gz` |
| `${f:6:6}` | sottostringa da posizione 6, lunghezza 6 | `hacker` |
| `${x:-predef}` | valore di `x`, oppure `predef` se `x` è vuota o non definita | |
| `${x:=predef}` | come sopra, e in più assegna `predef` a `x` | |
| `${x:?messaggio}` | errore con `messaggio` se `x` è vuota o non definita | |

Un trucco per ricordare `#` e `%`: sulla tastiera americana `#` sta a sinistra di `$` (toglie a sinistra), `%` a destra (toglie a destra).

### 8.4 Sostituzione di comando

`$(comando)` esegue il comando in una subshell e si sostituisce con il suo **output**, tolti gli a capo finali. La forma antica con gli apici inversi `` `comando` `` è equivalente ma non si annida bene: preferisci `$(...)`.

```
$ echo "oggi è $(date +%A) e sono $(whoami)"
oggi è sabato e sono hacker
$ righe=$(wc -l < /etc/passwd); echo "$righe utenti"
```

### 8.5 Aritmetica

`$(( ... ))` valuta un'espressione intera (64 bit con segno) con la sintassi del C: `+ - * / %`, `**` (potenza), confronti, operatori sui bit `& | ^ ~ << >>`, basi diverse con `0x` (esadecimale), `0` (ottale), `base#numero`.

```
$ echo $((0xff)) $((2#1010)) $((1 << 10)) $((7 / 2)) $((7 % 2))
255 10 1024 3 1
```

Dentro `$(( ))` le variabili si possono scrivere senza `$`. La divisione è intera, e un numero che inizia con `0` è letto in ottale: `$((010))` vale 8. Lo userai come calcolatrice veloce per gli offset nel Modulo 3.

### 8.6 Divisione in parole e `IFS`

Il risultato delle espansioni 3–5, **se non è tra virgolette doppie**, viene diviso in parole usando i caratteri della variabile `IFS` (*Internal Field Separator*, per default spazio, tabulazione, a capo). Sequenze di spazi contano come un unico separatore, e gli spazi iniziali e finali spariscono.

```
$ x='a   b'
$ printf '[%s]' $x;   echo      # non quotata: due parole
[a][b]
$ printf '[%s]' "$x"; echo      # quotata: una parola, spazi intatti
[a   b]
$ s='uno:due'; IFS=:; printf '[%s]' $s; echo; unset IFS
[uno][due]
```

(`printf '[%s]'` applica il modello a ogni argomento: è il modo più semplice per vedere quante parole ci sono.) **Attenzione:** la divisione avviene solo sul **risultato** delle espansioni, non sul testo che hai scritto. Gli spazi digitati separano le parole già nella fase dei token (§5.1).

### 8.7 Globbing

Una parola che contiene `*`, `?` o `[` non tra virgolette è trattata come un **modello** e sostituita dall'elenco, in ordine alfabetico, dei nomi di file che corrispondono:

| Modello | Corrisponde a |
|---|---|
| `*` | qualunque stringa, anche vuota |
| `?` | esattamente un carattere |
| `[abc]`, `[a-z]` | un carattere dell'insieme o dell'intervallo |
| `[!abc]` o `[^abc]` | un carattere **non** nell'insieme |

Regole importanti:

- i file che iniziano con `.` (file nascosti) **non** corrispondono a `*` né a `?`, a meno di scrivere il punto esplicitamente (`.*`) o di attivare `shopt -s dotglob`;
- se nessun file corrisponde, il modello resta **letterale**: `echo *.xyz` stampa `*.xyz`. Con `shopt -s nullglob` sparirebbe, con `shopt -s failglob` darebbe errore;
- il globbing opera sui nomi del **file system**, le graffe no: `ls *.{c,h}` prima diventa `ls *.c *.h` (graffe), poi ogni modello viene confrontato con i file (globbing);
- un nome di file prodotto dal globbing può iniziare con `-` ed essere scambiato per un'opzione. Con un file chiamato `-l` nella directory, `ls *` diventa `ls -l ...`. Per questo negli script si scrive `ls -- *` oppure `ls ./*`.

Approfondiremo il globbing con il file system nella Lezione 2 (modulo pwn.college *File Globbing*).

### 8.8 Rimozione delle virgolette

Infine, tutte le virgolette e i backslash che non sono il risultato di un'espansione vengono rimossi. Ciò che resta è l'`argv` definitivo.

### 8.9 Un esempio completo, passo per passo

```
$ n=3; echo ~/f{1,2}_$((n*2)) "$(echo  a   b)" *.nonexist
```

1. graffe: `~/f1_$((n*2))` e `~/f2_$((n*2))`;
2. tilde: `/home/hacker/f1_$((n*2))` e `/home/hacker/f2_$((n*2))`;
3. aritmetica: `/home/hacker/f1_6`, `/home/hacker/f2_6`; sostituzione di comando: `a b` (il comando interno `echo  a   b` riceve due argomenti e li unisce con uno spazio);
4. divisione in parole: non tocca `"a b"`, che è tra virgolette doppie;
5. globbing: `*.nonexist` non corrisponde a nulla e resta letterale;
6. rimozione delle virgolette.

`argv` finale: `echo`, `/home/hacker/f1_6`, `/home/hacker/f2_6`, `a b`, `*.nonexist`. Output: `/home/hacker/f1_6 /home/hacker/f2_6 a b *.nonexist`.

## 9. Variabili e parametri

### 9.1 Assegnazione e uso

```
$ FLAG=pwn          # assegnazione: NESSUNO spazio attorno a =
$ echo $FLAG
pwn
$ echo "${FLAG}college"
pwncollege
```

- `FLAG = pwn`, con gli spazi, **non** è un'assegnazione: la shell cerca un comando chiamato `FLAG` con argomenti `=` e `pwn`, e risponde `FLAG: command not found`;
- il valore è sempre una **stringa**; il contesto aritmetico (§8.5) la interpreta come numero quando serve;
- i nomi contengono lettere, cifre e `_` e non iniziano con una cifra. Per convenzione le variabili d'ambiente e di sistema sono in maiuscolo; per le tue variabili negli script usa il minuscolo, così non ne sovrascrivi una di sistema (scrivere `PATH=...` per sbaglio in uno script rompe tutti i comandi successivi);
- una variabile mai definita si espande alla stringa vuota, senza errori. `set -u` rende questo un errore, ed è consigliato negli script;
- `readonly X=1` rende la variabile non modificabile; `unset X` la elimina; `read X` la legge dalla tastiera o da un input (Lezione 4).

### 9.2 Parametri speciali

Alcuni nomi sono impostati dalla shell stessa e non si possono assegnare:

| Parametro | Significato |
|---|---|
| `$0` | nome della shell o dello script |
| `$1`, `$2` … `${10}` | argomenti posizionali (di uno script o di una funzione) |
| `$#` | numero di argomenti posizionali |
| `"$@"` | tutti gli argomenti, **ciascuno come parola separata** |
| `"$*"` | tutti gli argomenti uniti in **una** parola, separati dal primo carattere di `IFS` |
| `$?` | codice di uscita dell'ultimo comando (§11) |
| `$$` | PID della shell corrente (Lezione 5) |
| `$!` | PID dell'ultimo comando lanciato in background |
| `$-` | opzioni attive della shell |
| `$_` | ultimo argomento del comando precedente |

La differenza tra `"$@"` e `"$*"` è il caso più importante. Con gli argomenti `a` e `b c`, `"$@"` produce due parole (`a`, `b c`), `"$*"` una sola (`a b c`), mentre `$@` senza virgolette ne produce tre (`a`, `b`, `c`) per via della divisione in parole. Negli script quasi sempre serve `"$@"`.

---

# Parte III — L'esecuzione

## 10. Dal nome al programma

### 10.1 L'ordine di risoluzione

Quando la prima parola di un comando semplice è, per esempio, `ls`, bash la risolve in quest'ordine (manuale, sezione *COMMAND EXECUTION*):

1. **alias**: sostituzioni testuali definite con `alias nome='testo'`, applicate solo nelle shell interattive e prima ancora dell'analisi delle espansioni;
2. **parole riservate**: `if`, `for`, `while`, `[[`, `{` …;
3. **funzioni** di shell, definite con `nome() { ...; }`;
4. **builtin**: comandi implementati dentro la shell stessa (`cd`, `echo`, `printf`, `export`, `read`, `type`, `help`, `source` …);
5. **programmi esterni**: se il nome **non contiene `/`**, bash lo cerca nelle directory elencate in `PATH`, separate da `:`, **da sinistra a destra**, e vince il primo file eseguibile trovato. Se il nome contiene una `/` (`./prog`, `/bin/ls`, `bin/prog`) non c'è alcuna ricerca: si esegue esattamente quel file.

Se nulla corrisponde, bash stampa `command not found` e imposta il codice di uscita 127 (prima, se è definita, chiama la funzione `command_not_found_handle`: è lei che su Ubuntu suggerisce quale pacchetto installare).

Una precisazione per chi scrive script portabili: in *modalità POSIX* (`set -o posix`, o bash invocata come `sh`) i **builtin speciali** definiti dallo standard (`break`, `:`, `.`, `continue`, `eval`, `exec`, `exit`, `export`, `readonly`, `return`, `set`, `shift`, `trap`, `unset`) vengono trovati **prima** delle funzioni, e una funzione con lo stesso nome non li può nascondere.

```
$ type cd
cd is a shell builtin
$ type ls
ls is aliased to `ls --color=auto'
$ type if
if is a shell keyword
$ type -a echo
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
$ echo "$PATH"
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

Strumenti per controllare la risoluzione:

| Comando | Effetto |
|---|---|
| `type nome`, `type -a nome` | mostra che cosa verrebbe eseguito (con `-a`, tutte le corrispondenze in ordine) |
| `command -v nome` | stampa il percorso o il nome; è la forma portabile (POSIX) per gli script |
| `which nome` | programma esterno che cerca solo in `PATH`: ignora alias, funzioni e builtin, quindi può mentire |
| `\ls` o `command ls` | salta l'alias (e, con `command`, anche la funzione) |
| `builtin echo` | forza il builtin |
| `/usr/bin/echo` | forza il programma esterno |
| `hash`, `hash -r` | mostra o svuota la tabella in cui bash ricorda i percorsi già trovati |

**La tabella hash.** Per non scorrere `PATH` a ogni comando, bash ricorda dove ha trovato ogni programma. Se poi installi o sposti un programma, bash potrebbe continuare a cercarlo nel vecchio percorso: `hash -r` risolve.

**Perché `cd` deve essere un builtin.** La directory corrente è una proprietà del **processo** (§2.1). Un programma esterno `cd` cambierebbe la directory del proprio processo, che poi termina, lasciando la shell dov'era. Per la stessa ragione sono builtin `export`, `exit`, `source`, `read`, `ulimit`, `umask`: tutti modificano lo stato della shell stessa. Altri, come `echo` e `printf`, sono builtin solo per velocità, ed esiste anche la versione esterna.

### 10.2 Che cosa fa davvero il kernel: `fork` ed `execve`

Per eseguire un programma esterno la shell usa due chiamate di sistema, che studieremo a fondo nella Lezione 5 (e in OSTEP, cap. 5, *Process API*).

1. **`fork()`** (su Linux realizzata con `clone`) crea un processo figlio che è una copia quasi identica della shell: stessa memoria, stessi file aperti, stessa directory corrente, stesso ambiente.
2. Nel figlio la shell applica le redirezioni, poi chiama **`execve(percorso, argv, envp)`**: il kernel **sostituisce** il programma del processo con quello indicato, preparando la nuova memoria con il vettore `argv` e l'ambiente `envp`. Se `execve` riesce non ritorna mai: il codice della shell, in quel processo, non esiste più.
3. Il padre (la shell) chiama **`wait`** e resta in attesa finché il figlio non termina, poi ne legge lo stato.

La firma di `execve` (`man 2 execve`) è la definizione precisa di "lanciare un programma":

```c
int execve(const char *pathname, char *const argv[], char *const envp[]);
```

Tre input, tutti scelti da chi lancia il programma: **quale file**, **quali argomenti**, **quale ambiente**. Tienilo a mente: nei Moduli 3 e 4 analizzeremo i programmi proprio come funzioni di questi tre input.

### 10.3 Il kernel e gli script: lo shebang

Perché `execve` riesca, il file deve avere il permesso di esecuzione (bit `x`, Lezione 6) e un formato che il kernel sa caricare. Il kernel guarda i primi byte:

- se iniziano con `\x7fELF` è un eseguibile **ELF** (il formato dei programmi compilati su Linux, Modulo 2) e il kernel lo carica direttamente;
- se iniziano con `#!` (lo **shebang**), il kernel legge il resto della prima riga come percorso di un **interprete**, più al massimo un argomento, e lancia quello passandogli il nome dello script. Un file `script.sh` che inizia con `#!/bin/bash`, eseguito come `./script.sh arg`, diventa per il kernel `execve("/bin/bash", ["/bin/bash", "./script.sh", "arg"], envp)`.

```
$ printf '#!/bin/bash\necho "sono uno script, argv: $0 $@"\n' > s.sh
$ ./s.sh uno
bash: ./s.sh: Permission denied
$ echo $?
126
$ chmod +x s.sh; ./s.sh uno
sono uno script, argv: ./s.sh uno
$ bash s.sh uno              # anche senza permesso x: è bash a leggere il file
sono uno script, argv: s.sh uno
```

La forma `#!/usr/bin/env python3` usa il programma `env` per cercare `python3` in `PATH`: è più portabile ma, di nuovo, dipende da `PATH`. Il codice di uscita 126 significa "trovato ma non eseguibile".

### 10.4 Collegamento con la sicurezza (teoria)

Ricapitolando: il comportamento di un comando dipende da **alias, funzioni, `PATH`, la tabella hash, lo shebang**, tutte cose che chi lancia il comando può influenzare. Quando un programma **privilegiato** esegue un altro programma per nome (chiama `tar` invece di `/usr/bin/tar`, magari attraverso la funzione C `system()`, che passa la stringa a `/bin/sh -c`), e chi lo lancia controlla `PATH`, la ricerca da sinistra a destra può trovare un programma diverso da quello previsto. È la classe di difetti nota come *untrusted search path* (CWE-426) o *uncontrolled search path element* (CWE-427). Le mitigazioni sono tre: percorsi assoluti; `execve` con argomenti espliciti invece di `system`; un ambiente ripulito e un `PATH` fisso, come fa `sudo` con l'opzione `secure_path`. Riprenderemo questi temi con i programmi setuid nella Lezione 6 e nel Modulo 4, sempre su binari sintetici di laboratorio.

## 11. Il codice di uscita

### 11.1 Convenzioni

Ogni processo, terminando, consegna al padre uno **stato**. Se il programma termina normalmente (chiamando `exit(n)` o ritornando da `main`), lo stato contiene il **codice di uscita** `n`, ridotto a 8 bit: un intero da 0 a 255 (`exit(300)` diventa 44, cioè 300 mod 256). Se il processo è terminato da un **segnale**, lo stato contiene il numero del segnale. Bash riassume entrambi i casi nella variabile `$?`:

| Valore di `$?` | Significato |
|---|---|
| `0` | successo |
| `1`–`125` | errore; il significato dipende dal programma (vedi la sezione *EXIT STATUS* della sua pagina di manuale) |
| `126` | comando trovato ma non eseguibile (permessi, formato) |
| `127` | comando non trovato |
| `128 + n` | terminato dal segnale `n`: `130` = `SIGINT` (2, Ctrl-C), `137` = `SIGKILL` (9), `139` = `SIGSEGV` (11, *segmentation fault*), `143` = `SIGTERM` (15) |

Il 139 lo vedrai spesso nei Moduli 3 e 4: un programma che va in *segmentation fault* ha tentato un accesso alla memoria non valido, e in una sfida pwn è il primo segno che l'input ha raggiunto qualcosa di interessante. `kill -l 11` traduce un numero in nome di segnale.

```
$ true; echo $?
0
$ false; echo $?
1
$ ls /non/esiste; echo $?
ls: cannot access '/non/esiste': No such file or directory
2
$ bash -c 'exit 300'; echo $?
44
$ sleep 100        # poi premi Ctrl-C
^C
$ echo $?
130
```

### 11.2 Vero e falso

Per la shell **0 è vero** (successo) e qualunque altro valore è falso: il contrario del C, dove 0 è falso. Le costruzioni `&&`, `||`, `if`, `while` usano tutte il codice di uscita. I comandi `true` e `false` esistono solo per restituire 0 e 1. L'operatore `!` davanti a un comando ne inverte il risultato.

Il codice di una **pipeline** `A | B` è quello dell'ultimo comando, B; con `set -o pipefail` diventa il primo codice diverso da zero. L'array `PIPESTATUS` contiene i codici di tutti i comandi della pipeline. Il codice di `$(...)` dentro un'assegnazione (`x=$(cmd)`) è quello di `cmd`.

## 12. L'ambiente

### 12.1 Variabili di shell e variabili d'ambiente

Ogni processo ha un **ambiente**: un elenco di stringhe nella forma `NOME=valore`, ricevuto come terzo argomento di `execve` (§10.2), accanto ad `argv`. La shell distingue:

- **variabili di shell**: esistono solo dentro la shell corrente;
- **variabili d'ambiente** (o *esportate*): la shell le copia nell'`envp` di ogni programma che lancia.

Una variabile di shell non fa parte dell'ambiente finché non la esporti:

```
$ SEGRETO=abc
$ bash -c 'echo "figlio vede: [$SEGRETO]"'
figlio vede: []
$ export SEGRETO
$ bash -c 'echo "figlio vede: [$SEGRETO]"'
figlio vede: [abc]
```

L'eredità va **solo dal padre al figlio**, ed è una **copia**: un figlio che modifica una variabile non cambia quella del padre. Per questo uno script che fa `export X=1` non modifica la shell da cui lo lanci; per farlo bisogna eseguirlo **nella** shell corrente con `source script.sh` (o `. script.sh`).

Si può impostare una variabile **solo per un comando**, mettendo l'assegnazione prima del nome (§5.2): `LANG=C ls` esegue `ls` con `LANG=C` nel suo ambiente senza toccare la shell. `env -i comando` lo esegue con un ambiente **vuoto**; `env -u NOME comando` senza una variabile.

Comandi utili: `env` o `printenv` (mostrano l'ambiente), `printenv NOME` (una sola variabile), `set` (anche variabili di shell e funzioni), `declare -p NOME` (attributi e valore), `export -n NOME` (smette di esportare), `unset NOME` (elimina).

### 12.2 Variabili d'ambiente da conoscere

Dal capitolo 7 di *Linux Basics for Hackers* e dal manuale di bash:

| Variabile | Significato |
|---|---|
| `PATH` | directory in cui cercare i programmi (§10.1) |
| `HOME` | directory home; la usano `cd` senza argomenti e la tilde |
| `PWD`, `OLDPWD` | directory corrente e precedente (`cd -` torna a quella precedente) |
| `USER`, `LOGNAME` | nome utente (impostati al login: sono informativi, non affidabili, come `PS1`) |
| `SHELL` | shell di login dell'utente, non necessariamente quella in uso |
| `TERM` | tipo di terminale, usato dai programmi a schermo intero |
| `PS1`, `PS2` | prompt primario e secondario |
| `LANG`, `LC_ALL`, `LC_*` | lingua, codifica dei caratteri, ordinamento; `LC_ALL=C` rende output e ordinamento prevedibili, utile negli script |
| `EDITOR` | editor predefinito |
| `HISTFILE`, `HISTSIZE` | file e dimensione della storia dei comandi (§14) |
| `LD_PRELOAD`, `LD_LIBRARY_PATH` | istruzioni al caricatore dinamico su quali librerie caricare (Modulo 2) |

### 12.3 L'ambiente come input non fidato

Dal punto di vista di un programma, l'ambiente è un **input**, esattamente come `argv` e come ciò che legge da tastiera: lo sceglie chi lancia il programma. Un programma che gira con privilegi più alti di chi lo lancia (un programma *setuid*, Lezione 6) deve quindi trattarlo come ostile. I sistemi moderni hanno difese apposite: quando un programma setuid viene eseguito, il kernel lo segnala al caricatore dinamico (il flag `AT_SECURE`), che entra in *secure-execution mode* e ignora o limita variabili pericolose come `LD_PRELOAD` e `LD_LIBRARY_PATH` (`man 8 ld.so`); bash stessa, se avviata con identità effettiva diversa da quella reale, abbandona i privilegi a meno che non riceva l'opzione `-p`. Queste difese esistono perché, in passato, la loro assenza ha prodotto vulnerabilità reali: le analizzeremo come casi di studio nel Modulo 4.

Nelle CTF l'ambiente è anche un luogo dove cercare: la flag o un indizio possono essere in una variabile, e `env | grep -i flag` è tra i primi comandi da provare su una macchina nuova. L'ambiente di un processo in esecuzione si legge in `/proc/<PID>/environ`, se hai i permessi (Lezione 5).

---

# Parte IV — Gli strumenti

## 13. Trovare la documentazione

Saper trovare da soli la risposta è la competenza più importante di questa lezione: nessuno ricorda tutte le opzioni di tutti i comandi, e in gara non c'è nessuno a cui chiedere.

### 13.1 Le fonti disponibili

| Strumento | Per cosa | Esempio |
|---|---|---|
| `man comando` | manuale completo dei programmi esterni, delle chiamate di sistema, delle funzioni C, dei formati di file | `man ls` |
| `help comando` | documentazione dei **builtin** di bash; `help` da solo li elenca tutti | `help cd`, `help export` |
| `comando --help` | riepilogo rapido delle opzioni (convenzione GNU, non universale) | `ls --help` |
| `man -k parola` (= `apropos`) | cerca la parola nei nomi e nelle descrizioni di tutte le pagine | `man -k password` |
| `whatis comando` | la riga di descrizione di una pagina | `whatis passwd` |
| `info comando` | documentazione GNU estesa, organizzata in nodi | `info coreutils` |
| `/usr/share/doc/` | documentazione dei pacchetti installati | |

Se `man -k` non trova nulla su un sistema appena installato, il database delle pagine non è stato costruito: `sudo mandb` lo crea. Nei container minimali (anche in alcune sfide) le pagine di manuale non sono installate: resta `--help`, oppure la versione online su `man7.org`.

### 13.2 Le sezioni del manuale

Il manuale è diviso in **sezioni** numerate (`man man`):

| Sezione | Contenuto | Esempio |
|---|---|---|
| 1 | comandi utente | `man 1 printf` (il comando) |
| 2 | chiamate di sistema del kernel | `man 2 open`, `man 2 execve` |
| 3 | funzioni di libreria (soprattutto C) | `man 3 printf` (la funzione C) |
| 4 | file speciali, dispositivi | `man 4 null` (`/dev/null`) |
| 5 | formati di file e convenzioni | `man 5 passwd` (il file `/etc/passwd`) |
| 6 | giochi | |
| 7 | panoramiche, standard, varie | `man 7 ascii`, `man 7 signal`, `man 7 environ` |
| 8 | comandi di amministrazione | `man 8 ld.so`, `man 8 mount` |

Quando un testo scrive `printf(3)`, intende "la pagina `printf` della sezione 3". Senza numero, `man` apre la prima sezione che trova; `man -a nome` le apre tutte in sequenza. Le sezioni 2 e 3 diventeranno il tuo pane quotidiano dalla Lezione 9 in poi; la sezione 7 contiene alcune delle migliori introduzioni sintetiche esistenti (prova `man 7 ascii` e `man 7 environ`).

### 13.3 La struttura di una pagina e la sinossi

Ogni pagina segue la stessa struttura: **NAME** (nome e descrizione in una riga), **SYNOPSIS** (come si invoca), **DESCRIPTION**, **OPTIONS**, **EXIT STATUS**, **ENVIRONMENT** (variabili che influenzano il programma), **FILES**, **SEE ALSO**, a volte **BUGS** ed **EXAMPLES**. Per la sicurezza le sezioni più trascurate e più utili sono **ENVIRONMENT** e **FILES**: dicono quali input "nascosti" il programma legge.

La **sinossi** usa una notazione precisa:

| Notazione | Significato |
|---|---|
| **grassetto** | da scrivere esattamente così |
| *corsivo* o sottolineato | da sostituire con un valore |
| `[ ... ]` | facoltativo |
| `...` | ripetibile |
| `a | b` | alternativa: l'uno o l'altro |

Esempio da `man cp`:

```
cp [OPTION]... [-T] SOURCE DEST
cp [OPTION]... SOURCE... DIRECTORY
```

Si legge: "zero o più opzioni, poi un sorgente e una destinazione; oppure zero o più opzioni, uno o più sorgenti e una directory".

### 13.4 Navigare dentro `man`

`man` mostra la pagina con il visualizzatore `less`:

| Tasto | Effetto |
|---|---|
| spazio / `b` | pagina avanti / indietro |
| `/parola` | cerca in avanti; `n` e `N` vanno al risultato successivo e precedente |
| `g` / `G` | inizio / fine |
| `h` | aiuto di `less` |
| `q` | esci |

Trucco: per trovare un'opzione specifica, cerca con il trattino e lo spazio iniziale, per esempio `/^ *-n` (righe che iniziano con spazi e poi `-n`). Il modulo pwn.college *Digesting Documentation* allena proprio queste abilità.

## 14. Lavorare in fretta: storia, editing, completamento

### 14.1 Scorciatoie della riga

Bash usa la libreria **readline**, con scorciatoie in stile Emacs (`set -o vi` attiva quelle in stile vi):

| Tasto | Effetto |
|---|---|
| Tab (una o due volte) | completa comandi, file, variabili; con due Tab mostra le alternative |
| ↑ / ↓ | comando precedente / successivo |
| Ctrl-R | cerca all'indietro nella storia (di nuovo Ctrl-R per il risultato precedente) |
| Ctrl-A / Ctrl-E | inizio / fine della riga |
| Alt-B / Alt-F | parola indietro / avanti |
| Ctrl-W / Ctrl-U / Ctrl-K | cancella la parola precedente / fino a inizio riga / fino a fine riga |
| Ctrl-Y | incolla ciò che hai appena cancellato |
| Ctrl-L | pulisce lo schermo (come `clear`) |
| Ctrl-C | il kernel invia `SIGINT` al programma in primo piano (§2.2); a prompt, annulla la riga |
| Ctrl-D | fine dell'input (EOF); a prompt vuoto chiude la shell |
| Ctrl-Z | sospende il programma in primo piano (`SIGTSTP`, Lezione 5) |

In gara il tempo conta: il completamento con Tab evita anche gli errori di battitura nei nomi di file strani, perché inserisce lui le protezioni necessarie.

### 14.2 La storia dei comandi

Bash conserva i comandi in una lista in memoria e, all'uscita, li salva nel file indicato da `HISTFILE` (per default `~/.bash_history`).

| Forma | Effetto |
|---|---|
| `history` | elenca la storia numerata |
| `!!` | ripete l'ultimo comando (utile: `sudo !!`) |
| `!n` | ripete il comando numero `n` |
| `!stringa` | ripete l'ultimo comando che inizia con `stringa` |
| `!$` | l'ultimo argomento del comando precedente |
| `^vecchio^nuovo` | ripete l'ultimo comando sostituendo `vecchio` con `nuovo` |

L'espansione della storia con `!` è attiva solo nelle shell interattive (si disattiva con `set +H`) e avviene **prima** di tutto il resto, già mentre la riga viene letta, quindi anche dentro le virgolette doppie. Bash la salta solo se `!` è seguito da uno spazio, da un a capo, da `=`, da `(` o dalla virgoletta doppia di chiusura: per questo `echo "ciao!"` funziona, mentre `echo "ciao!mondo"` risponde `bash: !mondo: event not found`, perché bash cerca nella storia un comando che inizi con `mondo`. Tra virgolette singole `!` non è speciale: `echo 'ciao!mondo'` funziona sempre. Una password con un punto esclamativo, digitata tra virgolette doppie in un comando, è il caso classico in cui questo morde.

**Rilevanza in gara e in forensics.** `~/.bash_history` è uno dei primi file da leggere su una macchina da analizzare: rivela che cosa ha fatto l'utente, a volte password digitate per errore come comandi. Nelle sfide di categoria *forensics* o *misc* capita di trovarci la flag. Per lo stesso motivo un comando che inizia con uno spazio non viene salvato se `HISTCONTROL` contiene `ignorespace`: impara a controllare queste variabili prima di trarre conclusioni da una storia "vuota".

## 15. Osservare la shell al lavoro

Due strumenti permettono di **vedere** ciò che abbiamo descritto in teoria. Usali ogni volta che un comando non fa ciò che ti aspetti.

### 15.1 `set -x`: la traccia della shell

Con `set -x` bash stampa, prima di eseguirlo, ogni comando **dopo le espansioni**, preceduto da `+` (il contenuto della variabile `PS4`). È il modo più diretto per vedere l'`argv` effettivo. `set +x` la disattiva.

```
$ x='a   b'
$ set -x
$ echo $x "$x" ~/f*.nonexist
+ echo a b 'a   b' '/home/hacker/f*.nonexist'
a b a   b /home/hacker/f*.nonexist
$ set +x
```

Le virgolette singole nella traccia sono aggiunte da bash solo per mostrarti dove inizia e finisce ogni parola. Per uno script intero: `bash -x script.sh`.

### 15.2 `strace`: le chiamate di sistema

`strace` esegue un programma e stampa ogni chiamata di sistema che fa, con argomenti e risultato. Con `-f` segue anche i processi figli; con `-e trace=execve` mostra solo le esecuzioni di programmi; con `-s 200` mostra le stringhe fino a 200 caratteri (il default è 32, e le stringhe più lunghe compaiono troncate con `...`, un dettaglio che inganna spesso chi legge un `argv`).

```
$ strace -f -s 200 -e trace=execve bash -c 'echo ciao; /bin/echo "a  b" $HOME' 2>&1 | grep -v '^+++'
execve("/usr/bin/bash", ["bash", "-c", "echo ciao; /bin/echo \"a  b\" $HOME"], 0x7ffd... /* 24 vars */) = 0
ciao
execve("/bin/echo", ["/bin/echo", "a  b", "/home/hacker"], 0x5638... /* 24 vars */) = 0
a  b /home/hacker
```

Che cosa si vede, riga per riga:

1. la prima `execve` lancia `bash` con tre argomenti; lo script tra virgolette singole arriva intatto, con `$HOME` ancora letterale, perché lo ha protetto la shell **esterna**. Nota che il primo argomento di `execve` è già `/usr/bin/bash`: la ricerca in `PATH` l'ha fatta chi lancia (qui `strace`), non il kernel, che vuole sempre un percorso;
2. `echo ciao` **non** produce alcuna `execve`: è un builtin, eseguito dentro bash (§10.1);
3. `/bin/echo` produce una `execve` con `argv` = `["/bin/echo", "a  b", "/home/hacker"]`: le virgolette sono sparite, i due spazi sono rimasti dentro un unico argomento, `$HOME` è stata espansa dalla shell **interna**;
4. il terzo argomento di `execve` è l'ambiente, di cui `strace` mostra solo il numero di variabili.

Un dettaglio che vale la pena notare: la seconda `execve` **non** è preceduta da `[pid N]`, cioè avviene nello stesso processo della prima. Bash, quando l'ultimo comando di `bash -c` è un programma esterno, non fa `fork`: chiama direttamente `execve`, perché dopo non avrebbe più nulla da fare. Se inverti l'ordine (`bash -c '/bin/echo "a  b" $HOME; echo fine'`) compaiono la riga `strace: Process N attached` e il prefisso `[pid N]` davanti alla `execve`: ora il figlio esiste davvero, perché la shell deve sopravvivergli per eseguire `echo fine`. È il modello `fork` + `execve` del §10.2 reso visibile.

In quattro righe c'è tutta la Parte II e la Parte III di questa lezione. `strace` sarà uno strumento fondamentale del Modulo 3 (reverse engineering dinamico); se non è installato, `sudo apt install strace`.

---

# Parte V — La pratica

## 16. Esempi svolti

### Esempio 1 — Vedere `argv` con i propri occhi

Definiamo una piccola funzione che stampa quanti argomenti riceve e ognuno tra parentesi quadre. La useremo per tutto il modulo; puoi aggiungerla al tuo `~/.bashrc`.

```
$ args() { printf 'argc=%d\n' "$#"; printf '[%s]\n' "$@"; }
$ args a "b c" 'd $HOME' $HOME e\ f
argc=5
[a]
[b c]
[d $HOME]
[/home/hacker]
[e f]
```

Analisi parola per parola: `a` è una parola semplice; `"b c"` è una parola sola perché lo spazio è tra virgolette; `'d $HOME'` resta letterale perché le virgolette singole bloccano l'espansione; `$HOME` viene espansa e, non contenendo spazi, resta una parola; `e\ f` è una parola sola perché lo spazio è protetto dal backslash. `$#` e `"$@"` sono i parametri speciali del §9.2.

### Esempio 2 — Builtin o programma?

```
$ type -a echo
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
```

Esistono un `echo` interno alla shell e uno o più `echo` su disco (su molte distribuzioni `/bin` è un collegamento a `/usr/bin`, per questo compare due volte). Digitando `echo` vince il builtin (§10.1); per forzare il programma esterno si scrive il percorso, `/usr/bin/echo`. Le due versioni possono differire in dettagli come la gestione di `-e` o di `-n`, e `echo` di `sh` (dash) interpreta i backslash in modo diverso da quello di bash: è uno dei motivi per cui negli script si preferisce `printf`, il cui comportamento è fissato da POSIX.

### Esempio 3 — Il file che si chiama `-n`

Qualcuno ha creato un file chiamato `-n` che contiene la flag.

```
$ cat -n
```

Non succede niente: il cursore resta in attesa. `cat` ha interpretato `-n` come l'opzione "numera le righe" e, senza nomi di file, legge dallo standard input, cioè dalla tastiera (esci con Ctrl-D o Ctrl-C). Le virgolette **non** aiutano: `cat "-n"` è identico, perché le virgolette vengono rimosse prima che `cat` riceva l'argomento (§8.8). Due soluzioni corrette:

```
$ cat -- -n         # "--": fine delle opzioni (§6.2)
$ cat ./-n          # il nome non inizia più con "-"
```

La seconda funziona con qualunque programma, anche con quelli che non supportano `--`.

### Esempio 4 — Ambiente ereditato e codice di uscita insieme

```
$ bash -c 'echo "[$X]"; exit 7'; echo "uscita: $?"
[]
uscita: 7
$ X=ciao bash -c 'echo "[$X]"; exit 7'; echo "uscita: $?"
[ciao]
uscita: 7
$ echo "[$X]"
[]
```

Nel secondo caso `X=ciao` è nell'ambiente **solo** del processo `bash -c` (§12.1): la terza riga dimostra che la shell corrente non è cambiata.

### Esempio 5 — Leggere un comando da un writeup

In un writeup trovi:

```
$ for f in ~/chall/*.enc; do base64 -d "$f" > "${f%.enc}.bin" && echo "ok: ${f##*/}"; done
```

Applichiamo la Parte II. `for ... do ... done` è un ciclo (Lezione 4): per ogni file che corrisponde al modello `~/chall/*.enc` (tilde e globbing) la variabile `f` assume il percorso completo. Per ciascuno: `base64 -d "$f"` decodifica il file (`f` tra virgolette: un nome con spazi resta una parola); `> "${f%.enc}.bin"` scrive l'output in un file con lo stesso nome ma estensione `.bin` (§8.3, tolto il suffisso `.enc`); `&&` stampa il messaggio solo se la decodifica è riuscita; `${f##*/}` è il solo nome del file, senza directory. Una riga, sei concetti di questa lezione.

### Esempio 6 — Eseguire o "sorgere" uno script

```
$ printf 'export LIVELLO=2\ncd /tmp\n' > imposta.sh
$ bash imposta.sh; echo "[$LIVELLO] $PWD"
[] /home/hacker
$ source imposta.sh; echo "[$LIVELLO] $PWD"
[2] /tmp
```

`bash imposta.sh` esegue lo script in un **nuovo processo**: `export` e `cd` cambiano lo stato del figlio, che poi termina. `source` (o `.`) legge ed esegue i comandi **nella shell corrente**, che quindi cambia davvero. È così che `~/.bashrc` modifica la tua shell, ed è il motivo per cui, dopo averlo modificato, si scrive `source ~/.bashrc`.

## 17. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire `Soluzioni.md`. Per gli esercizi che chiedono una previsione, scrivi la risposta su carta e solo dopo verifica al terminale: è il modo più efficace per scoprire che cosa non hai capito.

### ★ Base

1. Usa `echo` per stampare `Ciao, hacker` e poi la stessa frase senza andare a capo. Quale opzione hai usato e dove l'hai trovata documentata?
2. Classifica con `type` i comandi: `cd`, `ls`, `if`, `type`, `cat`, `ll`. Per ognuno indica la categoria (§10.1).
3. Trova la pagina di manuale del **comando** `printf` e quella della **funzione C** `printf`. Che comando hai usato per ciascuna? Poi trova con `man -k` almeno tre pagine che parlano di "password" e indica la loro sezione.
4. Mostra il codice di uscita di `true`, `false`, `ls /`, `ls /non/esiste` e di un comando inesistente, `comandochenonesiste`. Spiega il valore dell'ultimo.
5. Crea un file chiamato `-flag` con il comando `echo segreto > ./-flag`. Leggilo in **due** modi diversi. Poi spiega perché `cat -flag` non funziona, che messaggio d'errore dà, e perché `cat "-flag"` non aiuta.

### ★★ Intermedio

6. Crea un file chiamato `la mia flag.txt` (con gli spazi). Leggilo in **tre** modi diversi (virgolette doppie, virgolette singole, backslash). Che cosa succede con `cat la mia flag.txt` e perché?
7. Imposta `PARTE=uno` senza esportarla. Dimostra con `bash -c` che un processo figlio non la vede; poi rendila visibile in due modi: (a) con `export`; (b) solo per un singolo comando, senza modificare la shell corrente.
8. Usando la funzione `args` dell'Esempio 1, **prevedi** l'output di:
   ```
   $ x='a   b'
   $ args $x "$x" '$x'
   ```
9. Crea la directory `~/bin` e dentro uno script `saluta` che stampa `ciao dal mio PATH` (prima riga `#!/bin/bash`, poi rendilo eseguibile con `chmod +x`). Fai in modo di poterlo lanciare digitando solo `saluta`. Poi rispondi: se esistesse anche `/usr/bin/saluta`, quale verrebbe eseguito, e come puoi verificarlo?
10. Con `p=/var/log/nginx/access.log.2.gz`, ottieni usando **solo** le espansioni di parametro del §8.3: (a) il nome del file `access.log.2.gz`; (b) la directory `/var/log/nginx`; (c) l'ultima estensione `gz`; (d) il percorso senza `.gz`; (e) il percorso senza alcuna estensione.
11. Usando solo bash, calcola: il valore decimale di `0x1337`; il valore di `2#11111111`; e il risultato **in esadecimale** di `0x401000 + 0x2a8` (suggerimento: `printf '%x\n'`). Perché `echo $((08))` dà errore?

### ★★★ Sfida

12. **Mini-CTF.** Nella cartella di questa lezione c'è lo script `setup_sfida.sh`. Eseguilo con `bash setup_sfida.sh`: crea solo file nella directory `~/l1_sfida`. **Non leggerne il contenuto**: è codificato apposta. La flag ha il formato `L1{...}` ed è divisa in tre parti; trovale tutte usando solo ciò che hai imparato in questa lezione. Suggerimento minimo: i file il cui nome inizia con `.` sono nascosti (§8.7); `ls -a` li mostra.
13. **Previsione.** Senza eseguirli, scrivi l'output esatto di questi comandi; poi verifica.
    ```
    $ A=1; B='$A'; C="$B"
    $ echo $A $B $C "$C" '$C'
    $ echo "$(echo '$A')" $((A+41))
    ```
14. **`"$@"` e `"$*"`.** Definisci `conta() { echo $#; }` ed esegui `set -- a "b c" ""` (che imposta gli argomenti posizionali a tre valori, l'ultimo vuoto). Prevedi l'output di `conta "$@"`, `conta "$*"`, `conta $@`, `conta $*`. Spiega ogni risultato.
15. **`strace`.** In una directory con i soli file `a.txt` e `b.txt`, con `HOME` impostata a quella directory, prevedi l'esatto `argv` della `execve` di `ls` per il comando `ls -l "$HOME"/*.txt 'x y'`. Verificalo con `strace -f -e trace=execve`. Poi ripeti con `HOME=/root` (o una directory senza file `.txt`): che cosa cambia e perché?
16. **Tutti i codici.** Scrivi un comando che produca ciascuno dei seguenti valori di `$?`, e spiega perché: 0, 1, 2, 126, 127, 130 o 143, 139. Per gli ultimi due non serve un programma che vada davvero in crash: basta mandare a un processo il segnale giusto (`kill -SEGV`, `kill -TERM`).
17. **Teoria (sicurezza).** Un programma di sistema, eseguito con privilegi elevati, contiene l'istruzione C `system("tar -czf /tmp/backup.tgz /home/data")`. Spiega in 8–12 righe: perché il comportamento dipende da `PATH` di chi lo lancia; quale classe di difetto è (nome e CWE); quali mitigazioni lo eliminano; e perché le difese del caricatore dinamico descritte nel §12.3 **non** bastano a proteggere questo caso. Non serve scrivere codice.

### Allenamento su pwn.college

Nel dojo **Linux Luminarium** completa i moduli *Hello Hackers*, *Digesting Documentation* e *Shell Variables*. Per ogni sfida annota in un file di appunti il comando risolutivo e il concetto della lezione che usa (con il numero di sezione): diventerà il tuo foglio di consultazione per le gare.

## 18. Domande di autoverifica

Rispondi per iscritto in 3–5 righe ciascuna, senza guardare il testo; poi confronta con le sezioni indicate in `Soluzioni.md`.

1. Qual è la differenza tra terminale, pseudo-terminale, shell e kernel? Chi trasforma Ctrl-C in un segnale?
2. Che cosa riceve esattamente un programma quando lo lanci dalla shell? Riceve le virgolette? Può ricevere un argomento che contiene un a capo?
3. Perché `cd` non può essere un programma esterno? Nomina altri due builtin che lo sono per la stessa ragione.
4. In quale ordine bash risolve il nome di un comando? Che ruolo hanno `PATH` e la tabella hash?
5. Elenca nell'ordine le otto espansioni. Perché `{1..$n}` non funziona?
6. In quali casi avviene la divisione in parole? Quale variabile la controlla?
7. Qual è la differenza tra una variabile di shell e una variabile d'ambiente? Perché uno script non può cambiare la directory della shell che lo ha lanciato, e come si aggira?
8. Che cosa indicano i codici di uscita 0, 126, 127, 130 e 139?
9. Che cosa fa il kernel quando esegue un file che inizia con `#!`?
10. Perché l'ambiente va considerato un input non fidato da un programma privilegiato?
11. Dove cerchi la documentazione di un builtin? E di una chiamata di sistema? E del formato di un file di configurazione?

## 19. Riepilogo

- La shell è un programma in modalità utente che legge righe, le trasforma e chiede al kernel di eseguire programmi con `fork` ed `execve`; il terminale è un altro programma, collegato alla shell da un pseudo-terminale gestito dal kernel.
- Una riga viene divisa in token dai metacaratteri, organizzata in comandi semplici e liste, poi trasformata da otto espansioni in ordine fisso.
- Le virgolette decidono quante parole riceverà il programma; non arrivano mai al programma.
- Il programma riceve tre cose, tutte scelte da chi lo lancia: il file eseguito, `argv`, l'ambiente. La sicurezza di un programma privilegiato dipende da come tratta questi tre input.
- Il codice di uscita (0 = successo, 126, 127, 128+n) è il canale con cui un programma riferisce il proprio esito.
- `man`, `help`, `--help` e `apropos` rispondono a quasi ogni domanda; `set -x` e `strace` mostrano ciò che accade davvero.

## 20. Fonti

- **pwn.college**, *Linux Luminarium — 1 The Command Line* (trascrizione 088, `C:\CTF_Transcripts\pwn.college`): prompt, comandi e argomenti, opzioni corte e lunghe, `echo -n`, `date --utc`, storia di Linux (corretta nel §3).
- **pwn.college**, *Introduction* 091–095: che cos'è pwn.college, etica della cybersecurity, che cos'è la cybersecurity (lettura consigliata prima di iniziare).
- **OccupyTheWeb**, *Linux Basics for Hackers*, No Starch Press: cap. 1 (*Getting Started with the Basics*) e cap. 7 (*Managing User Environment Variables*).
- **R. e A. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces* (OSTEP), cap. 4 (*The Abstraction: The Process*) e cap. 5 (*Process API*), per §2.1 e §10.2.
- **Ethical Hacker Italiani** (trascrizioni, cartella `trascrizioni`): video sui comandi base di Linux, utili come ripasso in italiano.
- **GNU Bash Reference Manual** (`man bash`): sezioni *DEFINITIONS*, *SHELL GRAMMAR*, *QUOTING*, *PARAMETERS*, *EXPANSION*, *COMMAND EXECUTION*, *ENVIRONMENT*, *EXIT STATUS*, *INVOCATION*, *HISTORY EXPANSION*.
- **Pagine di manuale**: `execve(2)`, `ld.so(8)`, `environ(7)`, `signal(7)`, `man(1)`, `strace(1)`.
- **POSIX.1-2017** (IEEE Std 1003.1), *Base Definitions* cap. 12 *Utility Conventions*; *Shell & Utilities* cap. 2 *Shell Command Language*.
- **P. H. Salus**, *A Quarter Century of Unix* (1994), per la storia e la citazione di McIlroy nel §1.
- **MITRE CWE**: CWE-88 (*Argument Injection*), CWE-426 (*Untrusted Search Path*), CWE-427 (*Uncontrolled Search Path Element*).

## 21. Prossima lezione

**Lezione 2 — Il file system**: la gerarchia delle directory Linux (standard FHS), percorsi assoluti e relativi, inode, hard link e link simbolici, metadati dei file, file speciali in `/dev` e `/proc`, e il globbing approfondito.
