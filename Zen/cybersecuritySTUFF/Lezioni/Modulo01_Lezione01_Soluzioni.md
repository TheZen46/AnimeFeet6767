# Modulo 1 — Lezione 1: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Gli output sono stati verificati con bash 5 su Linux; dettagli come i messaggi d'errore possono variare leggermente tra distribuzioni.

## ★ Base

**1.**
```
$ echo Ciao, hacker
$ echo -n Ciao, hacker
```
L'opzione è `-n`. Poiché `echo` di solito è un builtin, la documentazione corretta è `help echo`; `man echo` documenta invece il programma esterno `/usr/bin/echo`, che si comporta allo stesso modo per `-n`.

**2.**
| Comando | `type` dice | Categoria |
|---|---|---|
| `cd` | shell builtin | builtin |
| `ls` | aliased to `ls --color=auto` (o `/usr/bin/ls`) | alias, che rimanda a un programma esterno |
| `if` | shell keyword | parola chiave |
| `type` | shell builtin | builtin |
| `cat` | `/usr/bin/cat` | programma esterno |
| `ll` | alias (su Ubuntu/Kali: `ls -alF`) oppure `not found` | alias se definito in `~/.bashrc`, altrimenti inesistente |

L'ultimo caso mostra che gli alias sono configurazione personale, non parte del sistema: non contarci negli script.

**3.** `man 1 printf` per il comando, `man 3 printf` per la funzione C. Senza numero, `man printf` apre la prima sezione che trova, cioè la 1. Con `man -k printf` vedi tutte le pagine correlate e le loro sezioni.

**4.**
```
$ true; echo $?                    → 0
$ false; echo $?                   → 1
$ ls / >/dev/null; echo $?         → 0
$ ls /non/esiste; echo $?          → 2   (GNU ls: 2 = problema grave, come un file inesistente passato come argomento)
$ comandochenonesiste; echo $?     → 127
```
127 è il valore che la shell stessa usa quando non trova il comando né come builtin, né come funzione, né in `PATH`.

## ★★ Intermedio

**5.**
```
$ cat -- -flag
$ cat ./-flag
```
`cat -flag` dà `cat: invalid option -- 'f'`: `cat` interpreta `-flag` come le opzioni corte unite `-f -l -a -g`, e la prima, `-f`, non esiste. Il codice di uscita è 1.

**6.**
```
$ cat "la mia flag.txt"
$ cat 'la mia flag.txt'
$ cat la\ mia\ flag.txt
```
(Anche il completamento con Tab produce la terza forma.) `cat la mia flag.txt` passa a `cat` **tre** argomenti, `la`, `mia` e `flag.txt`, e quindi cerca tre file diversi: dà tre errori `No such file or directory`, a meno che non esistano per caso file con quei nomi.

**7.**
```
$ PARTE=uno
$ bash -c 'echo "[$PARTE]"'           → []
$ PARTE=uno bash -c 'echo "[$PARTE]"' → [uno]   (b: solo per questo comando)
$ export PARTE
$ bash -c 'echo "[$PARTE]"'           → [uno]   (a: da ora in poi per tutti i figli)
```
Attenzione alle virgolette singole attorno allo script di `bash -c`: con le doppie, `$PARTE` verrebbe espansa dalla shell **padre** prima di lanciare il figlio, e l'esperimento non dimostrerebbe nulla.

**8.**
```
argc=4
[a]
[b]
[a   b]
[$x]
```
`$x` non quotata viene divisa in due parole (`a`, `b`) e gli spazi multipli spariscono; `"$x"` resta una parola con gli spazi originali; `'$x'` è letterale.

**9.**
```
$ mkdir -p ~/bin
$ printf '#!/bin/bash\necho "ciao dal mio PATH"\n' > ~/bin/saluta
$ chmod +x ~/bin/saluta
$ export PATH="$HOME/bin:$PATH"
$ saluta
ciao dal mio PATH
```
Per renderlo permanente si aggiunge la riga `export PATH=...` a `~/.bashrc` (molte distribuzioni aggiungono già `~/bin` se esiste, al login successivo). Con `~/bin` messo **all'inizio** di `PATH` vince il tuo `saluta`; se lo avessi aggiunto alla fine (`PATH="$PATH:$HOME/bin"`) vincerebbe `/usr/bin/saluta`. Per verificarlo: `type -a saluta` elenca tutte le corrispondenze nell'ordine di ricerca; la prima è quella che viene eseguita. Nota: bash ricorda i percorsi già trovati (`hash`); dopo aver cambiato `PATH` o aggiunto programmi, `hash -r` svuota questa memoria.

## ★★★ Sfida

**10.**
```
$ A=1; B='$A'; C="$B"
$ echo $A $B $C "$C" '$C'
1 $A $A $A $C
$ echo "$(echo '$A')" $((A+41))
$A 42
```
Il punto sottile: l'espansione delle variabili avviene **una sola volta**. `B` contiene il testo `$A`; quando `C="$B"` viene espansa, `C` riceve quel testo, `$A`, che **non** viene espanso di nuovo. Lo stesso vale per `$B` e `$C` nel comando `echo`. La sostituzione di comando stampa `$A` letterale perché dentro ci sono le virgolette singole. L'espansione aritmetica `$((A+41))` legge invece il valore di `A` per nome, e dà 42.

**11.** Risposta modello.
`system()` passa la stringa a `/bin/sh -c`, che cerca `tar` nelle directory di `PATH` da sinistra a destra (§4). `PATH` fa parte dell'ambiente, ereditato da chi lancia il programma: se un utente non privilegiato mette in testa a `PATH` una directory che controlla, contenente un proprio eseguibile chiamato `tar`, il programma privilegiato eseguirà quel file con i propri privilegi invece del vero `tar`. È la classe di difetti *Untrusted Search Path*, **CWE-426** (affine a CWE-427, *Uncontrolled Search Path Element*). Mitigazioni: (1) usare percorsi assoluti (`/usr/bin/tar`) e preferire `execve` con argomenti espliciti a `system`, che coinvolge anche la shell; (2) ripulire l'ambiente prima di eseguire altri programmi, impostando un `PATH` fisso e sicuro, come fa `sudo` con `secure_path`. Riprenderemo il tema con i programmi setuid nella Lezione 6 e nel Modulo 4.

**12.** Flag: `L1{la_shell_non_mente_mai}`

Percorso risolutivo:
```
$ cd ~/l1_sfida
$ ls -a
.  ..  -parte1  .strumenti  .suggerimento  parte 2 di 3
$ cat ./-parte1                 → L1{la_shell_     (nome che inizia con "-": Esempio 3)
$ cat "parte 2 di 3"            → non_mente_       (nome con spazi: Esercizio 6)
$ cat .suggerimento             → La chiave si chiama CHIAVE e vale: apriti
$ ls -a .strumenti              → rivela
$ .strumenti/rivela             → la CHIAVE non e' nel mio ambiente   (codice di uscita 3)
$ CHIAVE=apriti .strumenti/rivela   → mai}
```
Concetti usati: file nascosti (`ls -a`); fine delle opzioni o `./` per il nome con il trattino; virgolette per il nome con gli spazi; un programma in una directory che non è in `PATH` va lanciato con un percorso (contiene una `/`, quindi niente ricerca in `PATH`); una variabile d'ambiente passata solo a un comando. Anche `export CHIAVE=apriti` funziona, ma lascia la variabile nella shell. Il codice di uscita 3, visibile con `echo $?`, è un indizio in più che il programma ha "rifiutato" e non è andato in crash.

Le stringhe codificate nello script sono in Base64: le decodificheremo a mano nella Lezione 7.

## Domande di autoverifica: punti chiave attesi

1. Il terminale mostra testo e riceve tasti; la shell interpreta le righe e lancia i programmi; il kernel crea i processi e gestisce le risorse (§1).
2. Riceve `argv` (le parole già divise ed espanse) e l'ambiente. Le virgolette sono rimosse prima (§3.1, §5).
3. Perché la directory corrente appartiene al processo: un figlio la cambierebbe solo per sé (§4).
4. Alias, parole chiave, funzioni, builtin, poi le directory di `PATH` da sinistra a destra; se il nome contiene `/`, nessuna ricerca (§4).
5. Una variabile d'ambiente viene ereditata dai processi figli; una di shell no, finché non la esporti (§7).
6. 0 successo, 127 comando non trovato, 130 = 128 + 2, terminato da SIGINT (Ctrl-C) (§6).
7. `help` per i builtin; `man 2 nome` per le chiamate di sistema (§8).
