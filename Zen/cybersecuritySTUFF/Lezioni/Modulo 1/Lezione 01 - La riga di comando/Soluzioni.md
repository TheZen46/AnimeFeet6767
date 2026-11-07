# Modulo 1 — Lezione 1: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Gli output sono stati verificati con bash 5.2 su Linux; dettagli come i messaggi d'errore possono variare leggermente tra distribuzioni. I riferimenti `§` rimandano alle sezioni di `Lezione.md`.

## ★ Base

**1.**
```
$ echo Ciao, hacker
$ echo -n Ciao, hacker
```
L'opzione è `-n`. Poiché `echo` di solito è un builtin, la documentazione corretta è `help echo`; `man echo` documenta il programma esterno `/usr/bin/echo`, che si comporta allo stesso modo per `-n`. Saperlo distinguere è il punto dell'esercizio (§10.1, §13.1).

**2.**
| Comando | `type` dice | Categoria |
|---|---|---|
| `cd` | shell builtin | builtin |
| `ls` | aliased to `ls --color=auto` (o `/usr/bin/ls`) | alias, che rimanda a un programma esterno |
| `if` | shell keyword | parola riservata |
| `type` | shell builtin | builtin |
| `cat` | `/usr/bin/cat` | programma esterno |
| `ll` | alias (su Ubuntu/Kali: `ls -alF`) oppure `not found` | alias se definito in `~/.bashrc`, altrimenti inesistente |

L'ultimo caso mostra che gli alias sono configurazione personale, letta solo dalle shell interattive (§4.2): non contarci negli script.

**3.** `man 1 printf` per il comando, `man 3 printf` per la funzione C. Senza numero, `man printf` apre la prima sezione che trova, cioè la 1. `man -k password` restituisce di solito, tra le altre, `passwd (1)` (il comando per cambiare password), `passwd (5)` (il formato del file `/etc/passwd`), `shadow (5)` (il file delle password cifrate), `chpasswd (8)` (comando di amministrazione). Se non restituisce nulla, il database va creato con `sudo mandb` (§13.1).

**4.**
```
$ true; echo $?                    → 0
$ false; echo $?                   → 1
$ ls / >/dev/null; echo $?         → 0
$ ls /non/esiste; echo $?          → 2   (GNU ls: 2 = problema grave, come un file inesistente passato come argomento)
$ comandochenonesiste; echo $?     → 127
```
127 è il valore che la shell stessa usa quando non trova il comando né come alias, né come funzione, né come builtin, né in `PATH` (§10.1, §11.1).

**5.**
```
$ cat -- -flag
$ cat ./-flag
```
`cat -flag` dà `cat: invalid option -- 'f'`: `cat` interpreta `-flag` come le opzioni corte unite `-f -l -a -g` (§6.2), e la prima, `-f`, non esiste. Il codice di uscita è 1. `cat "-flag"` è identico, perché le virgolette vengono rimosse dalla shell (§8.8): `cat` riceve comunque la stringa `-flag`. Le virgolette proteggono dalla **shell**, non dal **programma**.

## ★★ Intermedio

**6.**
```
$ cat "la mia flag.txt"
$ cat 'la mia flag.txt'
$ cat la\ mia\ flag.txt
```
(Anche il completamento con Tab produce la terza forma.) `cat la mia flag.txt` passa a `cat` **tre** argomenti, `la`, `mia` e `flag.txt`, perché gli spazi sono metacaratteri (§5.1); `cat` cerca tre file diversi e dà tre errori `No such file or directory`, a meno che non esistano per caso file con quei nomi.

**7.**
```
$ PARTE=uno
$ bash -c 'echo "[$PARTE]"'           → []
$ PARTE=uno bash -c 'echo "[$PARTE]"' → [uno]   (b: solo per questo comando)
$ export PARTE
$ bash -c 'echo "[$PARTE]"'           → [uno]   (a: da ora in poi per tutti i figli)
```
Attenzione alle virgolette singole attorno allo script di `bash -c`: con le doppie, `$PARTE` verrebbe espansa dalla shell **padre** prima di lanciare il figlio, e l'esperimento non dimostrerebbe nulla. È lo stesso fenomeno che `strace` mostra nel §15.2.

**8.**
```
argc=4
[a]
[b]
[a   b]
[$x]
```
`$x` non quotata viene divisa in due parole (`a`, `b`) e gli spazi multipli spariscono (§8.6); `"$x"` resta una parola con gli spazi originali; `'$x'` è letterale (§7).

**9.**
```
$ mkdir -p ~/bin
$ printf '#!/bin/bash\necho "ciao dal mio PATH"\n' > ~/bin/saluta
$ chmod +x ~/bin/saluta
$ export PATH="$HOME/bin:$PATH"
$ saluta
ciao dal mio PATH
```
Per renderlo permanente si aggiunge la riga `export PATH=...` a `~/.bashrc` (molte distribuzioni aggiungono già `~/bin` al `PATH` se esiste, tramite `~/.profile`, dal login successivo). Con `~/bin` **all'inizio** di `PATH` vince il tuo `saluta`; se lo avessi aggiunto alla fine (`PATH="$PATH:$HOME/bin"`) vincerebbe `/usr/bin/saluta`. Per verificarlo: `type -a saluta` elenca tutte le corrispondenze nell'ordine di ricerca, e la prima è quella eseguita. Se avevi già lanciato `saluta` prima di cambiare `PATH`, bash potrebbe ricordare il vecchio percorso nella tabella hash: `hash -r` (§10.1).

**10.**
```
$ p=/var/log/nginx/access.log.2.gz
$ echo "${p##*/}"    → access.log.2.gz         (a: toglie il prefisso più lungo fino all'ultima /)
$ echo "${p%/*}"     → /var/log/nginx          (b: toglie il suffisso più corto dall'ultima /)
$ echo "${p##*.}"    → gz                      (c: toglie il prefisso più lungo fino all'ultimo .)
$ echo "${p%.gz}"    → /var/log/nginx/access.log.2   (d)
$ echo "${p%%.*}"    → /var/log/nginx/access   (e: toglie il suffisso più lungo dal primo .)
```
Attenzione al caso (e): funziona solo perché nessuna directory del percorso contiene un punto. Con `/home/a.b/file.txt`, `${p%%.*}` darebbe `/home/a`. Nella pratica si combina: prima `${p##*/}`, poi `%%.*` sul solo nome.

**11.**
```
$ echo $((0x1337))                      → 4919
$ echo $((2#11111111))                  → 255
$ printf '%x\n' $((0x401000 + 0x2a8))   → 4012a8
$ echo $((08))
bash: 08: value too great for base (error token is "08")
```
Un numero che inizia con `0` è letto in **ottale** (§8.5), e in base 8 la cifra 8 non esiste. Lo stesso errore capita leggendo ore o giorni come `08` da `date`: si risolve con `$((10#08))`, che forza la base 10. Il calcolo `0x401000 + 0x2a8` è tipico del Modulo 3: indirizzo base di un programma più un offset.

## ★★★ Sfida

**12.** Flag: `L1{la_shell_non_mente_mai}`

Percorso risolutivo:
```
$ cd ~/l1_sfida
$ ls -a
-parte1  .  ..  .strumenti  .suggerimento  'parte 2 di 3'
$ cat ./-parte1                     → L1{la_shell_
$ cat "parte 2 di 3"                → non_mente_
$ cat .suggerimento                 → La chiave si chiama CHIAVE e vale: apriti
$ ls -a .strumenti                  → rivela
$ .strumenti/rivela                 → la CHIAVE non e' nel mio ambiente   (codice di uscita 3)
$ CHIAVE=apriti .strumenti/rivela   → mai}
```
L'ordine dell'elenco dipende dalla *locale* (Lezione 3): quello sopra è l'ordine per byte della locale `C`, dove `-` (0x2d) viene prima di `.` (0x2e); con una locale come `it_IT.UTF-8` l'ordine può cambiare, perché le regole di collazione non confrontano i byte ma "lettere" con pesi diversi per la punteggiatura. Per un ordine prevedibile: `LC_ALL=C ls -a`. Le virgolette attorno a `'parte 2 di 3'` non fanno parte del nome: GNU `ls`, quando scrive su un terminale, cita i nomi che contengono spazi o caratteri speciali proprio perché tu possa copiarli in un comando (stile di quoting `shell-escape`, Lezione 2); con `ls -N` o in una pipe le virgolette spariscono.

Concetti usati: file nascosti (`ls -a`, §8.7); `./` o `--` per il nome con il trattino (Esempio 3); virgolette per il nome con gli spazi (§7); un programma in una directory che non è in `PATH` va lanciato con un percorso che contiene una `/`, quindi senza ricerca in `PATH` (§10.1); una variabile d'ambiente passata solo a un comando (§12.1). Anche `export CHIAVE=apriti` funziona, ma lascia la variabile nella shell. Il codice di uscita 3, visibile con `echo $?`, indica che il programma ha "rifiutato" consapevolmente, non che è andato in crash (§11.1). Anche `CHIAVE=apriti bash -c .strumenti/rivela` funziona; `CHIAVE=apriti; .strumenti/rivela` (con il punto e virgola) **no**, perché così `CHIAVE` è solo una variabile di shell, non esportata.

Le stringhe codificate nello script sono in Base64: le decodificheremo a mano nella Lezione 7.

**13.**
```
$ A=1; B='$A'; C="$B"
$ echo $A $B $C "$C" '$C'
1 $A $A $A $C
$ echo "$(echo '$A')" $((A+41))
$A 42
```
Il punto sottile: l'espansione delle variabili avviene **una sola volta**, e il suo risultato non viene riesaminato per altre espansioni di variabile (solo per divisione in parole e globbing, §8). `B` contiene il testo `$A`; con `C="$B"`, `C` riceve quel testo, che **non** viene espanso di nuovo. La sostituzione di comando stampa `$A` letterale perché dentro ci sono le virgolette singole. L'espansione aritmetica legge invece il valore di `A` per nome, e dà 42. (Per forzare una seconda valutazione esiste `eval`, che negli script è pericoloso proprio per questo: esegue come codice dei dati.)

**14.**
```
$ conta "$@"   → 3    tre parole: "a", "b c", "" (anche la stringa vuota è un argomento)
$ conta "$*"   → 1    una sola parola: "a b c " (uniti con il primo carattere di IFS, uno spazio)
$ conta $@     → 3    senza virgolette: divisione in parole → a, b, c; la stringa vuota sparisce
$ conta $*     → 3    stesso risultato di $@ senza virgolette
```
Il terzo caso dà 3 "per caso": gli argomenti originali erano `a`, `b c`, `""`, quelli ricevuti sono `a`, `b`, `c`. Il conteggio coincide ma i valori no. Solo `"$@"` preserva esattamente gli argomenti originali, ed è per questo che si usa sempre negli script che inoltrano argomenti a un altro comando (§9.2).

**15.** Con `HOME` = la directory che contiene `a.txt` e `b.txt` (qui `/tmp/esempio`):
```
execve("/usr/bin/ls", ["ls", "-l", "/tmp/esempio/a.txt", "/tmp/esempio/b.txt", "x y"], ...) = 0
```
`"$HOME"` è espansa e protetta dalle virgolette, `/*.txt` è fuori dalle virgolette e quindi soggetto a globbing: un modello diventa **due** argomenti, in ordine alfabetico. `'x y'` resta un solo argomento con lo spazio.

Con `HOME=/root` (nessun file `.txt` lì, o nessun permesso di leggere la directory):
```
execve("/usr/bin/ls", ["ls", "-l", "/root/*.txt", "x y"], ...) = 0
```
Il modello non corrisponde a niente e resta **letterale** (§8.7): `ls` riceve un argomento che contiene davvero un asterisco, e risponde `cannot access '/root/*.txt'`. È `ls` a lamentarsi, non la shell, perché la shell non considera un errore il globbing senza corrispondenze (a meno di `failglob`).

**16.** Un insieme possibile:
```
$ true; echo $?                           → 0     successo
$ false; echo $?                          → 1     errore generico
$ ls /non/esiste; echo $?                 → 2     errore grave di ls (vedi man ls, EXIT STATUS)
$ touch x; ./x; echo $?                   → 126   trovato ma senza permesso di esecuzione
$ comandochenonesiste; echo $?            → 127   non trovato
$ sleep 100 (poi Ctrl-C); echo $?         → 130   128 + 2 (SIGINT)
$ bash -c 'sleep 5 & kill $!; wait $!'; echo $?        → 143   128 + 15 (SIGTERM, il segnale predefinito di kill)
$ bash -c 'kill -SEGV $$'; echo $?        → 139   128 + 11 (SIGSEGV); bash stampa anche "Segmentation fault"
```
Nell'ultimo, `$$` è il PID della shell interna, che si manda da sola il segnale: il risultato è indistinguibile, per il padre, da un vero accesso alla memoria non valido. Nell'esempio con `wait`, `wait` restituisce lo stato del processo in background, e `bash -c` termina con quel valore.

**17.** Risposta modello.
`system()` passa la stringa a `/bin/sh -c`; la shell vede la parola `tar`, che non contiene `/`, e la cerca nelle directory di `PATH` da sinistra a destra (§10.1). `PATH` fa parte dell'ambiente, che è ereditato da chi lancia il programma (§12.1): se un utente non privilegiato mette in testa a `PATH` una directory che controlla, contenente un proprio eseguibile chiamato `tar`, il programma privilegiato eseguirà quel file invece del vero `tar`, potenzialmente con i propri privilegi. È la classe di difetti *Untrusted Search Path*, **CWE-426**, strettamente legata a **CWE-427** *Uncontrolled Search Path Element*.

Mitigazioni: (1) percorsi assoluti, `/usr/bin/tar`; (2) evitare `system()`, che coinvolge una shell e tutta la sua grammatica, a favore di `execve` (o `posix_spawn`) con un `argv` esplicito; (3) ripulire l'ambiente prima di eseguire altri programmi e impostare un `PATH` fisso e sicuro, come fa `sudo` con `secure_path`.

Perché le difese del §12.3 non bastano: la *secure-execution mode* del caricatore dinamico filtra solo le variabili che interessano il caricatore stesso (`LD_PRELOAD`, `LD_LIBRARY_PATH` e simili); `PATH` non è tra queste, perché è la shell, non il caricatore, a usarla. Quanto alla shell: bash, e le versioni recenti di dash, abbandonano i privilegi se l'utente reale e quello effettivo sono diversi, ma molti programmi privilegiati chiamano prima `setuid(0)` (rendendo reale ed effettivo uguali), e a quel punto la protezione della shell non scatta. L'unica difesa affidabile è nel programma stesso. Riprenderemo il caso concreto, su binari sintetici, nella Lezione 6 e nel Modulo 4.

## Domande di autoverifica: punti chiave attesi

1. Terminale: disegna e riceve tasti. PTY: coppia master/slave del kernel che collega terminale e shell, con la disciplina di linea. Shell: interpreta le righe e lancia i programmi. Kernel: crea i processi e gestisce le risorse. Ctrl-C lo trasforma in `SIGINT` la disciplina di linea, cioè il kernel (§2.2).
2. Riceve `argv` (le parole già divise ed espanse) e l'ambiente. Le virgolette sono rimosse prima. Sì, un argomento può contenere un a capo (per esempio `$'a\nb'`); l'unico byte impossibile è lo zero (§6.1).
3. La directory corrente appartiene al processo: un figlio la cambierebbe solo per sé. Altri: `export`, `exit`, `source`, `umask`, `read` (§10.1).
4. Alias, parole riservate, funzioni, builtin, poi le directory di `PATH` da sinistra a destra; se il nome contiene `/`, nessuna ricerca. La tabella hash memorizza i percorsi già trovati e si svuota con `hash -r` (§10.1).
5. Graffe, tilde, parametri, sostituzione di comando, aritmetica, divisione in parole, globbing, rimozione delle virgolette. `{1..$n}` non funziona perché le graffe vengono espanse prima delle variabili (§8, §8.1).
6. Solo sul risultato di espansioni di parametro, di comando e aritmetiche non racchiuse tra virgolette doppie. La controlla `IFS` (§8.6).
7. Una variabile d'ambiente viene copiata nei processi figli; una di shell no, finché non la esporti. Lo script gira in un processo figlio, e le modifiche di un figlio non risalgono al padre. Si aggira con `source` (§12.1, Esempio 6).
8. 0 successo; 126 trovato ma non eseguibile; 127 non trovato; 130 = 128 + 2, `SIGINT`; 139 = 128 + 11, `SIGSEGV` (§11.1).
9. Legge la prima riga come percorso dell'interprete (più un eventuale argomento) e lancia l'interprete passandogli il nome dello script e gli argomenti (§10.3).
10. Perché lo sceglie interamente chi lancia il programma, come `argv`; variabili come `PATH` o `LD_PRELOAD` cambiano quale codice viene eseguito (§12.3).
11. `help` per i builtin; `man 2 nome` per le chiamate di sistema; `man 5 nome` per i formati di file (§13).
