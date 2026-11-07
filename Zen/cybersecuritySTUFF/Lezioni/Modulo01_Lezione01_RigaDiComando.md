# Modulo 1 — Lezione 1: La riga di comando

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 1 di 10
> Soluzioni degli esercizi: `Modulo01_Lezione01_Soluzioni.md` (da aprire solo dopo aver provato)

## 0. Obiettivi e prerequisiti

**Al termine della lezione sarai in grado di:**

1. distinguere terminale, shell e kernel, e spiegare cosa succede tra il tasto Invio e l'output;
2. scomporre una riga di comando in nome del programma, argomenti e opzioni, e prevedere quali argomenti riceverà il programma;
3. classificare un comando (builtin, esterno, alias, funzione, parola chiave) e spiegare come la shell lo trova tramite `PATH`;
4. usare correttamente virgolette singole, doppie e backslash;
5. creare, leggere ed esportare variabili, e distinguere variabili di shell e d'ambiente;
6. leggere il codice di uscita di un comando;
7. trovare da solo la documentazione di qualunque comando (`man`, `help`, `--help`, `apropos`).

**Prerequisiti:** nessuno. Serve solo un ambiente Linux con `bash`: il dojo di pwn.college, una macchina virtuale o WSL2.

**Tempo:** circa 2 ore di teoria ed esempi, 2–3 ore di esercizi.

---

## 1. Terminale, shell, kernel

Quando "apri il terminale" stai in realtà usando tre componenti diversi, che è bene non confondere.

| Componente | Che cos'è | Esempi |
|---|---|---|
| **Terminale** (emulatore di terminale) | il programma che disegna la finestra, riceve i tasti e mostra il testo. Storicamente era un dispositivo fisico (la *teletype*, da cui il nome `tty`) | GNOME Terminal, Windows Terminal, xterm, la scheda del browser nel dojo |
| **Shell** | un normale programma in spazio utente che legge una riga di testo, la interpreta e chiede al sistema operativo di eseguire i programmi richiesti | `bash`, `sh` (dash), `zsh`, `fish` |
| **Kernel** | il nucleo del sistema operativo: crea i processi, gestisce file, memoria e periferiche. La shell gli parla con le *chiamate di sistema* (system call) | Linux |

Il flusso, semplificato, quando digiti `echo hello hackers` e premi Invio:

1. il terminale passa i caratteri alla shell;
2. la shell divide la riga in parole e applica le espansioni (§5);
3. se il comando è interno alla shell (un *builtin*) lo esegue lei stessa; altrimenti cerca il programma su disco (§4), crea un nuovo processo e gli fa eseguire quel programma (le chiamate `fork` ed `execve`, che studieremo nella Lezione 5);
4. il programma scrive il suo output, che il terminale mostra;
5. la shell attende la fine del programma, ne registra il codice di uscita (§6) e stampa di nuovo il prompt.

**Perché conta per la sicurezza.** Quasi tutte le sfide CTF di categoria *pwn* e *misc* partono da una shell su una macchina remota. Capire esattamente quali argomenti riceve un programma, e da dove viene, è il primo passo per capire come un programma può essere usato in modo non previsto dal suo autore.

### Un po' di storia (con una correzione)

Nella trascrizione di pwn.college (*Linux Luminarium 1 — The Command Line*) il docente ricorda che il termine *shell* nasce con **Multics** e che Linux è nato come progetto amatoriale di Linus Torvalds. La catena storica precisa è questa:

- **Multics** (MIT, Bell Labs, General Electric, anni '60): sistema a condivisione di tempo in cui Louis Pouzin introduce l'idea e il nome di *shell*.
- **Unix** (Ken Thompson e Dennis Ritchie, Bell Labs, dal 1969): sistema più semplice, nato dopo l'abbandono di Multics da parte dei Bell Labs. Ha la sua shell (*Thompson shell*), poi la **Bourne shell** `sh` (1979).
- **Bash** (*Bourne-Again SHell*, Brian Fox per il progetto GNU, 1989): compatibile con `sh`, con molte estensioni.
- **Linux** (Linus Torvalds, 1991): un **kernel** scritto da zero, ispirato a Minix e compatibile con Unix. Linux non deriva direttamente da Multics: ne eredita le idee attraverso Unix. Un sistema "Linux" completo è il kernel più gli strumenti GNU (tra cui bash) e altro software.

La lezione da trarre, come dice lo stesso docente, è che la riga di comando è un sistema **cresciuto in modo organico**, pieno di convenzioni storiche: molte stranezze (perché `--` per le opzioni lunghe?) non hanno una ragione profonda, e vanno semplicemente conosciute.

---

## 2. Il prompt

Il prompt è il testo che la shell stampa quando è pronta a ricevere un comando. Una forma tipica è:

```
hacker@dojo:~$
```

- `hacker` è il nome dell'utente, `dojo` il nome della macchina;
- `~` è la directory corrente (`~` abbrevia la tua home, per esempio `/home/hacker`);
- `$` indica un **utente normale**; `#` indica l'utente **root** (amministratore, UID 0).

Il formato del prompt è controllato dalla variabile `PS1` (prova `echo "$PS1"`). Nelle trascrizioni e nei writeup il prompt è spesso abbreviato a `$` o `#`: quando leggi `# cat flag`, il `#` non va digitato, ti dice solo che il comando è eseguito come root.

**Convenzione di queste lezioni:** le righe che iniziano con `$ ` sono comandi da digitare (senza il `$`); le righe senza prefisso sono l'output.

---

## 3. Anatomia di un comando

### 3.1 Parole, argomenti, `argv`

La shell divide la riga in **parole** usando spazi e tabulazioni come separatori (più spazi consecutivi contano come uno solo). La prima parola è il nome del comando; le successive sono gli **argomenti** (o *parametri*: sono sinonimi, come sottolinea la trascrizione di pwn.college).

```
$ echo hello hackers
hello hackers
```

Il programma `echo` riceve un vettore di stringhe chiamato **`argv`** (*argument vector*):

| indice | valore |
|---|---|
| `argv[0]` | `echo` |
| `argv[1]` | `hello` |
| `argv[2]` | `hackers` |

`argv[0]` è per convenzione il nome del programma. Questo vettore è esattamente ciò che ritroverai nella firma `int main(int argc, char *argv[])` di un programma C (Lezione 9). Il programma **non vede** la riga di comando originale: vede solo `argv`, già diviso e già espanso dalla shell. Questo è un punto fondamentale: molti errori, e molte vulnerabilità, nascono dal credere che un programma veda qualcosa di diverso da ciò che vede davvero.

Due comandi che sembrano simili fanno cose molto diverse:

```
$ echo flag
flag
$ cat flag
pwn.college{...}
```

`echo` stampa i propri argomenti come testo; `cat` interpreta ogni argomento come il **nome di un file** e ne stampa il contenuto.

### 3.2 Opzioni

Molti argomenti non sono dati ma **opzioni** (o *flag*) che cambiano il comportamento del programma. La convenzione, nata con Unix e codificata dallo standard POSIX (*Utility Syntax Guidelines*) e poi estesa da GNU:

- **opzione corta**: un trattino e una lettera, `-n`. Più opzioni corte si possono unire: `ls -l -a` equivale a `ls -la`;
- **opzione lunga** (estensione GNU): due trattini e una parola, `--utc`, `--help`;
- **opzione con valore**: `-o file`, `-ofile`, `--output=file`, `--output file`, a seconda del programma;
- **`--` da solo** significa "fine delle opzioni": tutto ciò che segue è un argomento normale, anche se inizia con `-`.

Esempi dalla trascrizione:

```
$ echo -n hello      # -n: non andare a capo alla fine
hello$
$ date --utc         # data in UTC (Coordinated Universal Time)
```

**Attenzione:** è il **programma**, non la shell, a decidere cosa sia un'opzione. La shell passa `-n` come qualunque altra parola. Questo porta al problema dei file il cui nome inizia con un trattino (Esempio 3 e Esercizio 5), un classico delle sfide *misc*.

---

## 4. Che tipo di comando è? `type` e `PATH`

Quando la prima parola è, ad esempio, `ls`, la shell la risolve in quest'ordine (manuale di bash, sezione *COMMAND EXECUTION*):

1. **alias** (sostituzioni testuali definite con `alias`, attive nelle shell interattive);
2. **parole chiave** della sintassi (`if`, `for`, `while`, `[[` …);
3. **funzioni** di shell;
4. **builtin**: comandi implementati dentro la shell stessa (`cd`, `echo`, `export`, `type`, `help` …);
5. **programmi esterni**, cercati nelle directory elencate nella variabile `PATH`, **da sinistra a destra**. Vince il primo trovato.

Se il nome contiene una `/` (ad esempio `./prog` o `/bin/ls`), la ricerca in `PATH` non avviene: si esegue esattamente quel file.

```
$ type cd
cd is a shell builtin
$ type ls
ls is aliased to `ls --color=auto'
$ type -a echo
echo is a shell builtin
echo is /usr/bin/echo
$ echo "$PATH"
/usr/local/bin:/usr/bin:/bin
```

Perché `cd` deve essere un builtin? Perché la directory corrente è una proprietà del **processo**: un programma esterno cambierebbe la directory del proprio processo figlio, che poi termina, lasciando la shell dov'era.

**Collegamento con la sicurezza (teoria, ripresa nel Modulo 4).** Se un programma privilegiato esegue un altro programma per nome (ad esempio chiama `ls` invece di `/bin/ls`) e chi lo lancia controlla `PATH`, la ricerca da sinistra a destra può trovare un programma diverso da quello previsto. È la classe di difetti nota come *PATH injection* o *untrusted search path* (CWE-426). La mitigazione è usare percorsi assoluti e ripulire l'ambiente; per questo `sudo` imposta un proprio `secure_path`.

---

## 5. Virgolette ed espansioni (introduzione)

Prima di eseguire un comando, bash trasforma la riga con una serie di **espansioni**, in quest'ordine (manuale di bash, sezione *EXPANSION*):

1. espansione delle graffe: `file{1,2}` → `file1 file2`
2. espansione della tilde: `~` → `/home/hacker`
3. espansione di parametri e variabili: `$HOME`, `${USER}`
4. sostituzione di comando: `$(date)`
5. espansione aritmetica: `$((6*7))` → `42`
6. **divisione in parole** (*word splitting*) del risultato delle espansioni 3–5 non tra virgolette
7. espansione dei nomi di file (*globbing*): `*.txt` → elenco dei file corrispondenti
8. rimozione delle virgolette

Le **virgolette** servono a controllare queste trasformazioni:

| Forma | Effetto | Esempio | Risultato |
|---|---|---|---|
| `'...'` (singole) | **nessuna** espansione: tutto è letterale | `echo '$HOME   *'` | `$HOME   *` |
| `"..."` (doppie) | espande `$`, `` ` `` e `\`; **non** divide in parole e **non** fa globbing | `echo "$HOME   *"` | `/home/hacker   *` |
| `\c` (backslash) | rende letterale il solo carattere successivo | `echo a\ \ b` | `a  b` |

Il punto chiave: le virgolette decidono **quante parole**, cioè quanti elementi di `argv`, riceverà il programma.

```
$ echo hello      hackers
hello hackers
$ echo "hello      hackers"
hello      hackers
```

Nel primo caso `echo` riceve due argomenti e li stampa separati da un solo spazio; nel secondo riceve **un solo** argomento che contiene sei spazi. Le virgolette non arrivano al programma: sono rimosse nell'ultimo passo.

**Regola pratica:** metti sempre tra virgolette doppie le variabili (`"$x"`), a meno che tu non voglia esplicitamente la divisione in parole. Le espansioni non quotate sono una fonte classica di bug negli script (riprenderemo il tema nella Lezione 4).

---

## 6. Codice di uscita

Ogni programma, terminando, restituisce al processo padre un intero tra 0 e 255, il **codice di uscita** (*exit status*). La convenzione è:

- `0` = successo;
- qualunque altro valore = errore (il significato dipende dal programma: `man` spesso lo documenta nella sezione *EXIT STATUS*);
- `128 + n` = il programma è stato terminato dal segnale `n` (ad esempio 130 = 128 + 2, interruzione con Ctrl-C; i segnali sono nella Lezione 5);
- `127` = comando non trovato; `126` = trovato ma non eseguibile.

La shell salva il codice dell'ultimo comando nella variabile speciale `$?`:

```
$ true; echo $?
0
$ false; echo $?
1
$ ls /non/esiste; echo $?
ls: cannot access '/non/esiste': No such file or directory
2
```

Gli operatori `&&` ed `||` usano il codice di uscita: `cmd1 && cmd2` esegue `cmd2` solo se `cmd1` ha successo; `cmd1 || cmd2` solo se fallisce. Nota che per la shell "vero" è 0, al contrario del C.

---

## 7. Variabili di shell e variabili d'ambiente

### 7.1 Variabili di shell

```shell
$ FLAG=pwn          # assegnazione: NESSUNO spazio attorno a =
$ echo $FLAG
pwn
$ echo "${FLAG}college"
pwncollege
```

- `FLAG = pwn` (con spazi) **non** è un'assegnazione: la shell cerca un comando chiamato `FLAG` con argomenti `=` e `pwn`.
- `${NOME}` delimita il nome quando è seguito da altre lettere.
- Una variabile mai definita si espande alla stringa vuota, senza errori (usa `set -u` negli script per renderlo un errore).

### 7.2 Ambiente ed `export`

Ogni processo ha un **ambiente**: un elenco di coppie `NOME=valore` che riceve dal padre al momento della creazione, accanto ad `argv`. Una variabile di shell **non** fa parte dell'ambiente finché non la esporti:

```bash
$ SEGRETO=abc
$ bash -c 'echo "figlio vede: [$SEGRETO]"'
figlio vede: []
$ export SEGRETO
$ bash -c 'echo "figlio vede: [$SEGRETO]"'
figlio vede: [abc]
```

Si può anche impostare una variabile **solo per un comando**: `LANG=C ls` esegue `ls` con `LANG=C` nel suo ambiente senza cambiare la shell.

Comandi utili: `env` o `printenv` (mostrano l'ambiente), `set` (mostra anche le variabili di shell e le funzioni), `unset NOME` (elimina).

Variabili d'ambiente da conoscere (*Linux Basics for Hackers*, cap. 7):

| Variabile | Significato |
|---|---|
| `PATH` | directory in cui cercare i programmi (§4) |
| `HOME` | directory home dell'utente |
| `PWD` | directory corrente |
| `USER` | nome utente |
| `SHELL` | shell di login |
| `PS1` | formato del prompt |
| `LANG`, `LC_*` | lingua e codifica dei caratteri |

L'ambiente è un vettore di stringhe passato al programma esattamente come `argv` (in C lo si legge con `getenv` o con il terzo argomento `envp` di `main`). Nelle CTF capita di trovare la flag proprio in una variabile d'ambiente: `env | grep -i flag` è uno dei primi comandi da provare su una macchina nuova.

---

## 8. Trovare la documentazione

Saper trovare da soli la risposta è la competenza più importante di questa lezione: nessuno ricorda tutte le opzioni di tutti i comandi.

| Strumento | Per cosa | Esempio |
|---|---|---|
| `man comando` | manuale completo dei programmi esterni e di molto altro | `man ls` |
| `help comando` | documentazione dei **builtin** di bash | `help cd`, `help export` |
| `comando --help` | riepilogo rapido delle opzioni (convenzione GNU, non universale) | `ls --help` |
| `man -k parola` (= `apropos`) | cerca la parola nei titoli di tutte le pagine di manuale | `man -k password` |
| `info comando` | documentazione GNU estesa | `info coreutils` |

Il manuale è diviso in **sezioni** numerate. Le più importanti:

| Sezione | Contenuto | Esempio |
|---|---|---|
| 1 | comandi utente | `man 1 printf` (il comando) |
| 2 | chiamate di sistema del kernel | `man 2 open`, `man 2 execve` |
| 3 | funzioni di libreria C | `man 3 printf` (la funzione C) |
| 5 | formati di file | `man 5 passwd` |
| 7 | panoramiche e convenzioni | `man 7 ascii`, `man 7 signal` |
| 8 | comandi di amministrazione | `man 8 mount` |

Quando un testo scrive `printf(3)`, intende "la pagina `printf` della sezione 3". Le sezioni 2 e 3 diventeranno essenziali dalla Lezione 9 in poi.

Dentro `man` (che usa il visualizzatore `less`): `/parola` cerca, `n` va al risultato successivo, `q` esce, `h` mostra l'aiuto.

---

## 9. Lavorare in fretta: storia e scorciatoie

| Tasto o comando | Effetto |
|---|---|
| Tab (una o due volte) | completa nomi di comandi e file, o mostra le alternative |
| ↑ / ↓ | scorre i comandi precedenti |
| Ctrl-R | cerca all'indietro nella storia |
| `history`, `!!`, `!n` | elenco della storia, ripeti l'ultimo comando, ripeti il comando numero `n` |
| Ctrl-C | invia il segnale di interruzione (SIGINT) al programma in esecuzione |
| Ctrl-D | fine dell'input (EOF); a prompt vuoto chiude la shell |
| Ctrl-L / `clear` | pulisce lo schermo |
| Ctrl-A / Ctrl-E | inizio / fine della riga |

In gara il tempo conta: il completamento con Tab evita anche gli errori di battitura nei nomi di file strani.

---

## 10. Esempi svolti

### Esempio 1 — Vedere `argv` con i propri occhi

Definiamo una piccola funzione che stampa quanti argomenti riceve e ognuno tra parentesi quadre. La useremo per tutto il modulo.

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

Analisi parola per parola: `a` è una parola semplice; `"b c"` è una parola sola perché lo spazio è tra virgolette; `'d $HOME'` resta letterale perché le virgolette singole bloccano l'espansione; `$HOME` viene espansa; `e\ f` è una parola sola perché lo spazio è protetto dal backslash. (`$#` è il numero di argomenti e `"$@"` è l'elenco degli argomenti, ciascuno come parola separata: li approfondiremo nella Lezione 4.)

### Esempio 2 — Builtin o programma?

```
$ type -a echo
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
```

Esistono un `echo` interno alla shell e uno o più `echo` su disco (su molte distribuzioni `/bin` è un collegamento a `/usr/bin`, per questo compare due volte). Digitando `echo` vince il builtin (§4); per forzare il programma esterno si scrive il percorso, `/usr/bin/echo`. Le due versioni possono differire in dettagli come la gestione di `-e`: è uno dei motivi per cui negli script si preferisce `printf`.

### Esempio 3 — Il file che si chiama `-n`

Qualcuno ha creato un file chiamato `-n` che contiene la flag.

```shell
$ cat -n
```

Non succede niente: il cursore resta in attesa. `cat` ha interpretato `-n` come l'opzione "numera le righe" e, senza nomi di file, legge dalla tastiera (lo standard input; esci con Ctrl-D o Ctrl-C). Due soluzioni corrette:

```shell
$ cat -- -n         # "--": fine delle opzioni
$ cat ./-n          # il nome non inizia più con "-"
```

La seconda funziona con qualunque programma, anche con quelli che non supportano `--`.

### Esempio 4 — Ambiente ereditato e codice di uscita insieme

```shell
$ bash -c 'echo "[$X]"; exit 7'; echo "uscita: $?"
[]
uscita: 7
$ X=ciao bash -c 'echo "[$X]"; exit 7'; echo "uscita: $?"
[ciao]
uscita: 7
```

Nel secondo caso `X=ciao` è nell'ambiente **solo** del processo `bash -c`. Il codice di uscita è un intero su 8 bit: `bash -c 'exit 300'` restituisce 44, cioè 300 mod 256.

---

## 11. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire le soluzioni. Per gli esercizi che chiedono una previsione, scrivi la risposta su carta e solo dopo verifica al terminale.

### ★ Base

1. Usa `echo` per stampare `Ciao, hacker` e poi la stessa frase senza andare a capo. Quale opzione hai usato e dove l'hai trovata documentata?
2. Classifica con `type` i comandi: `cd`, `ls`, `if`, `type`, `cat`, `ll`. Per ognuno indica la categoria (§4).
3. Trova la pagina di manuale del **comando** `printf` e quella della **funzione C** `printf`. Che comando hai usato per ciascuna?
4. Mostra il codice di uscita di `true`, `false`, `ls /`, `ls /non/esiste` e di un comando inesistente, `comandochenonesiste`. Spiega il valore dell'ultimo.

### ★★ Intermedio

5. Crea un file chiamato `-flag` con il comando `echo segreto > ./-flag`. Leggilo in **due** modi diversi. Poi spiega perché `cat -flag` non funziona e che messaggio d'errore dà.
6. Crea un file chiamato `la mia flag.txt` (con gli spazi). Leggilo in **tre** modi diversi (virgolette doppie, virgolette singole, backslash). Che cosa succede con `cat la mia flag.txt` e perché?
7. Imposta `PARTE=uno` senza esportarla. Dimostra con `bash -c` che un processo figlio non la vede; poi rendila visibile in due modi: (a) con `export`; (b) solo per un singolo comando, senza modificare la shell corrente.
8. Usando la funzione `args` dell'Esempio 1, **prevedi** l'output di:
   ```
   $ x='a   b'
   $ args $x "$x" '$x'
   ```
9. Crea la directory `~/bin` e dentro uno script `saluta` che stampa `ciao dal mio PATH` (prima riga `#!/bin/bash`, poi rendilo eseguibile con `chmod +x`). Fai in modo di poterlo lanciare digitando solo `saluta`. Poi rispondi: se esistesse anche `/usr/bin/saluta`, quale verrebbe eseguito, e come puoi verificarlo?

### ★★★ Sfida

10. **Previsione.** Senza eseguirli, scrivi l'output esatto di questi comandi; poi verifica.
    ```
    $ A=1; B='$A'; C="$B"
    $ echo $A $B $C "$C" '$C'
    $ echo "$(echo '$A')" $((A+41))
    ```
11. **Teoria (sicurezza).** Un programma di sistema, eseguito con privilegi elevati, contiene l'istruzione C `system("tar -czf /tmp/backup.tgz /home/data")`. Spiega in 5–8 righe perché il comportamento dipende dalla variabile `PATH` di chi lo lancia, quale classe di difetto è (nome e CWE), e quali due mitigazioni lo eliminano. Non serve scrivere codice.
12. **Mini-CTF.** Salva questo script come `setup_l1.sh` ed eseguilo con `bash setup_l1.sh` (crea solo file nella directory `~/l1_sfida`). **Non leggerne il contenuto**: è codificato apposta. La flag ha il formato `L1{...}` ed è divisa in tre parti; trovale tutte usando solo ciò che hai imparato in questa lezione.
13. ```bash
    #!/usr/bin/env bash
    # Prepara la sfida della Lezione 1 in ~/l1_sfida. Non leggere oltre: esegui e basta.
    set -e
    D="$HOME/l1_sfida"; mkdir -p "$D/.strumenti"
    d(){ printf '%s' "$1" | base64 -d; }
    d 'TDF7bGFfc2hlbGxf' > "$D/-parte1"
    d 'bm9uX21lbnRlXw==' > "$D/parte 2 di 3"
    cat > "$D/.strumenti/rivela" <<'X'
    #!/usr/bin/env bash
    if [ "$CHIAVE" = "apriti" ]; then printf '%s\n' "$(printf 'bWFpfQ==' | base64 -d)"; exit 0
    else echo "la CHIAVE non e' nel mio ambiente" >&2; exit 3; fi
    X
    chmod +x "$D/.strumenti/rivela"
    echo "La chiave si chiama CHIAVE e vale: apriti" > "$D/.suggerimento"
    echo "Sfida pronta in $D"
    ```
Suggerimento minimo: i file il cui nome inizia con `.` sono nascosti; `ls -a` li mostra.

### Allenamento su pwn.college

Nel dojo **Linux Luminarium** completa i moduli *Hello Hackers*, *Digesting Documentation* e *Shell Variables*. Annota per ogni sfida il comando risolutivo: diventerà il tuo foglio di appunti per le gare.

---

## 12. Domande di autoverifica

Rispondi a voce o per iscritto in 2–3 righe ciascuna.

1. Qual è la differenza tra terminale, shell e kernel?
2. Che cosa riceve esattamente un programma quando lo lanci dalla shell? Riceve le virgolette?
3. Perché `cd` non può essere un programma esterno?
4. In quale ordine bash cerca un comando, e che ruolo ha `PATH`?
5. Qual è la differenza tra una variabile di shell e una variabile d'ambiente?
6. Che cosa indicano i codici di uscita 0, 127 e 130?
7. Dove cerchi la documentazione di un builtin? E di una chiamata di sistema?

---

## 13. Fonti

- **pwn.college**, *Linux Luminarium — 1 The Command Line* (trascrizione 088, `C:\CTF_Transcripts\pwn.college`): prompt, comandi e argomenti, opzioni corte e lunghe, `echo -n`, `date --utc`, storia di Linux.
- **pwn.college**, *Introduction* 091–095: che cos'è pwn.college, etica della cybersecurity (lettura consigliata prima di iniziare).
- **OccupyTheWeb**, *Linux Basics for Hackers*, No Starch Press: cap. 1 (*Getting Started with the Basics*) e cap. 7 (*Managing User Environment Variables*).
- **Ethical Hacker Italiani** (trascrizioni, cartella `trascrizioni`): video sui comandi base di Linux, utili come ripasso in italiano.
- **GNU Bash Reference Manual** (`man bash`): sezioni *SHELL GRAMMAR*, *QUOTING*, *EXPANSION*, *COMMAND EXECUTION*, *ENVIRONMENT*, *EXIT STATUS*.
- **POSIX.1-2017**, *Base Definitions*, cap. 12 *Utility Conventions* (sintassi delle opzioni e `--`).
- **MITRE CWE-426**, *Untrusted Search Path* (per l'Esercizio 11).

## 14. Prossima lezione

**Lezione 2 — Il file system**: la gerarchia delle directory Linux, percorsi assoluti e relativi, inode, hard link e link simbolici, file speciali in `/dev` e `/proc`.
