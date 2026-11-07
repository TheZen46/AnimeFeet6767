# Modulo 1 — Lezione 4: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Gli script sono stati eseguiti con bash 5.2 su Linux; date, PID e contenuto delle directory saranno diversi sul tuo sistema. I riferimenti `§` rimandano alle sezioni di `Lezione.md`.

## ★ Base

**1.**
```
$ ls /etc/passwd /nonesiste > out.txt 2> err.txt                       # (a)
$ ls /etc/passwd /nonesiste > tutto.txt 2>&1                           # (b) forma POSIX
$ ls /etc/passwd /nonesiste &> tutto.txt                               # (b) forma bash
$ ls /etc/passwd /nonesiste > /dev/null 2>&1                           # (c)
$ ls /etc/passwd /nonesiste > f 2> f; cat -A f                         # (d)
/etc/passwd$
ccess '/nonesiste': No such file or directory$
```
(d) è il caso C del §2.2: `f` viene aperto **due volte**, con due offset indipendenti, entrambi a 0. `ls` scrive prima l'errore (56 byte, `ls: cannot access '/nonesiste': ...`) dal descrittore 2, poi `/etc/passwd\n` (12 byte) dal descrittore 1, **a partire dall'inizio**: i primi 12 byte dell'errore vengono sovrascritti, e resta la coda `ccess '/nonesiste'...`. L'ordine esatto può variare con il programma; il risultato è comunque un miscuglio.

**2.**
| Comando | Sul terminale | Nel file / nella pipe |
|---|---|---|
| (a) `2>&1 > f` | l'errore | `f`: `/etc/passwd` |
| (b) `> f 2>&1` | niente | `f`: errore e `/etc/passwd` |
| (c) `2>/dev/null | wc -l` | `1` | nella pipe solo `/etc/passwd` |
| (d) `2>&1 | wc -l` | `2` | nella pipe entrambe le righe |
| (e) `2>&1 >/dev/null | wc -l` | `1` | nella pipe **solo l'errore** |

(a) e (e) sono lo stesso meccanismo: `2>&1` copia nel 2 ciò che l'1 è in quel momento (terminale in (a), la pipe in (e)), poi l'1 viene spostato altrove. Nota che la pipe viene collegata **prima** delle redirezioni scritte nel comando: per la shell, `|` è già lo stdout iniziale del comando.

**3.**
```
$ cat > config.txt <<FINE
home=$HOME
FINE
$ cat > script.sh <<'FINE'
echo "$HOME"
FINE
$ cat config.txt script.sh
home=/home/hacker
echo "$HOME"
$ rev <<< segreto
oterges
```

**4.**
```
$ cat /nonesiste | sort | wc -l; echo "${PIPESTATUS[@]}"
cat: /nonesiste: No such file or directory
0
1 0 0
$ set -o pipefail; cat /nonesiste | sort | wc -l; echo $?
...
1
$ set +o pipefail; yes | head -n 1; echo "$? ${PIPESTATUS[@]}"
y
0 141 0
$ set -o pipefail; yes | head -n 1; echo $?
y
141
```
Senza `pipefail` il codice è quello di `wc` (0) anche se `cat` è fallito; con `pipefail` è quello di `cat` (1). Il 141 è 128 + 13 (`SIGPIPE`): `yes` è stato terminato quando ha scritto in una pipe il cui lettore, `head`, era già uscito (§4.2). Con `pipefail` questo diventa un "errore", ed è uno dei motivi per cui `pipefail` va usato con giudizio (§7.3).

**5.**
```bash
#!/usr/bin/env bash
# info.sh — informazioni su utente, macchina e una directory
if (( $# != 1 )); then
    echo "uso: $0 DIRECTORY" >&2
    exit 2
fi
if [[ ! -d $1 ]]; then
    echo "$0: '$1' non è una directory" >&2
    exit 1
fi
shopt -s dotglob nullglob          # il glob include i nascosti e sparisce se non c'è niente
voci=("$1"/*)
echo "utente:    $(id -un)"
echo "macchina:  $(hostname)"
echo "directory: $PWD"
echo "voci in $1: ${#voci[@]}"
```
Contare con un array e un glob (L2 §13) è più corretto di `ls -A "$1" | wc -l`, che conterebbe due volte un nome con un a capo. `nullglob` fa sì che una directory vuota dia 0 e non 1 (L1 §8.7). Verifica: `bash info.sh; echo $?` → messaggio su stderr e 2; `bash info.sh /nonesiste` → 1.

## ★★ Intermedio

**6.**
```bash
#!/usr/bin/env bash
exec 3>> log.txt                                    # aggiunta in coda
for i in 1 2 3; do echo "$(date '+%F %T') riga $i" >&3; done
ls -l /proc/$$/fd | grep log.txt                    # il 3 è aperto (l-wx: sola scrittura)
exec 3>&-                                           # chiuso
exec 4< log.txt
read -r -u 4 prima
read -r -u 4 seconda                                # la seconda read continua dall'offset della prima
exec 4<&-
echo "1: $prima"
echo "2: $seconda"
```
La seconda `read` legge la seconda riga perché il descrittore 4 mantiene la **posizione** (l'offset) tra una lettura e l'altra (§1.1). Con due `read ... < log.txt` separati, ogni `read` aprirebbe il file da capo e leggerebbe sempre la prima riga.

**7.** In `echo 42 | read n` entrambi i lati della pipe girano in processi figli (§4.1): `read` imposta `n` nel **suo** processo, che poi termina; la shell principale non viene toccata (§4.4). Correzioni:
```
$ read n <<< 42; echo "$n"                 # here-string
$ read n < <(echo 42); echo "$n"           # sostituzione di processo
$ n=$(echo 42); echo "$n"                  # sostituzione di comando
```
(Quarta, solo negli script: `shopt -s lastpipe`.)

**8.**
```
$ while read l; do echo $l; done < difficile.txt
spazi davanti
backslash
                          (niente: la riga "-n" è diventata echo -n)
$ while IFS= read -r l || [ -n "$l" ]; do printf '[%s]\n' "$l"; done < difficile.txt
[  spazi davanti]
[back\slash]
[-n]
[ultima senza a capo]
```
Le differenze, una per una (§10.3): (1) senza `IFS=`, `read` toglie gli spazi iniziali; e senza virgolette, `echo $l` li toglierebbe comunque per la divisione in parole; (2) senza `-r`, il backslash viene interpretato e sparisce; (3) `echo $l` con `l=-n` diventa `echo -n`, che stampa niente; (4) l'ultima riga senza `\n` fa restituire a `read` un fallimento e il ciclo esce senza stamparla. `|| [ -n "$l" ]` la recupera.

**9.**
```bash
#!/usr/bin/env bash
for f in "$@"; do
    if [[ -L $f ]]; then
        echo "$f: link simbolico -> $(readlink -- "$f")"
    elif [[ ! -e $f ]]; then
        echo "$f: non esiste"
    elif [[ -d $f ]]; then
        echo "$f: directory"
    elif [[ -x $f ]]; then
        echo "$f: eseguibile"
    elif [[ ! -s $f ]]; then
        echo "$f: vuoto"
    else
        case $f in
            *.zip|*.tar.gz|*.tgz) echo "$f: archivio" ;;
            *)                    echo "$f: file" ;;
        esac
    fi
done
```
Il link va controllato **per primo** perché quasi tutti i test (`-e`, `-d`, `-x`, `-s`) **seguono** il link e guardano il bersaglio (L2 §9.4): un link pendente risulterebbe "non esiste", e `/bin` (link a `usr/bin`, L2 §2.2) risulterebbe "directory". `-L` è uno dei pochi test che guarda il link stesso. Poi l'ordine va dal più specifico al più generale: una directory è anche "eseguibile" (il bit `x` sulle directory significa attraversamento, Lezione 6), quindi `-d` deve precedere `-x`.

**10.**
```bash
#!/usr/bin/env bash
massimo() {
    local i m
    (( $# > 0 )) || { echo "massimo: nessun argomento" >&2; return 1; }
    for i in "$@"; do
        [[ $i =~ ^-?[0-9]+$ ]] || { echo "massimo: '$i' non è un intero" >&2; return 1; }
    done
    m=$1
    for i in "$@"; do (( i > m )) && m=$i; done
    echo "$m"
}
i=fuori
massimo 3 -7 42 5        # → 42
echo "i=$i"              # → i=fuori: local i ha protetto la variabile dello script
```
La convalida con una regex ancorata **prima** di qualunque uso aritmetico non è solo pulizia: senza, un argomento come `a[$(comando)]` verrebbe eseguito da `(( i > m ))` (§14.3). Togliendo `i` dalla riga `local`, alla fine lo script stamperebbe `i=5`.

**11.**
```
$ comm -23 <(ls /bin | sort) <(ls /sbin | sort)                         # (a)
$ find /etc -name '*.conf' -type f -print0 2>/dev/null | xargs -0 cat 2>/dev/null | wc -l   # (b)
$ tr -cs '[:alpha:]' '\n' < /etc/services | tee parole.txt | sort | uniq -c | sort -rn | head   # (c)
$ touch 'nome con spazio'
$ printf '%s\n' 'nome con spazio' | xargs ls                            # (d) tre argomenti: errore
ls: cannot access 'nome': No such file or directory
ls: cannot access 'con': No such file or directory
ls: cannot access 'spazio': No such file or directory
$ printf '%s\0' 'nome con spazio' | xargs -0 ls                         # un argomento: funziona
nome con spazio
```
(a) Su sistemi con *usrmerge* `/bin` e `/sbin` sono link (L2 §2.2), ma il confronto funziona lo stesso. (b) `cat` di tutti i file e poi un solo `wc -l` dà il totale direttamente; con `xargs -0 wc -l` otterresti un totale **per ogni gruppo** di argomenti se i file sono tantissimi (xargs può lanciare `wc` più volte). (c) `tee` salva la lista delle parole, una per riga, mentre la catena continua (§5.1).

**12.** La correzione: `python3 -u ...` oppure `PYTHONUNBUFFERED=1 python3 ...`; dentro il programma, `print(..., flush=True)`. Nella catena con `tail -f`, `grep` scrive in una pipe e quindi usa il buffer pieno: le righe trovate restano nel buffer di `grep` finché non si accumulano alcuni KiB, e `awk` non riceve nulla. Si risolve con `grep --line-buffered`, oppure `stdbuf -oL grep ...` (§3.2). `awk` alla fine scrive sul terminale, quindi è già a righe; se anche il suo output andasse in una pipe, servirebbe `fflush()` in awk.

## ★★★ Sfida

**13.**
(a) Ogni tentativo dimezza l'intervallo possibile: dopo k tentativi restano al più 1.000.000 / 2^k numeri. Poiché 2^20 = 1.048.576 > 1.000.000, dopo 20 tentativi resta al più un numero, che è quello giusto: ⌈log₂ 1.000.000⌉ = 20.
(b) Con una FIFO, il ciclo è: `gioco` legge dalla FIFO e scrive nella pipe; il risolutore legge dalla pipe e scrive nella FIFO.
```bash
#!/usr/bin/env bash
mkfifo risposte
bash indovina.sh < risposte | {
    IFS= read -r intro; echo "$intro" >&2
    lo=1; hi=1000000
    while (( lo <= hi )); do
        mid=$(( (lo + hi) / 2 ))
        echo "$mid"                                  # stdout del gruppo = la FIFO
        IFS= read -r r || break                      # stdin del gruppo = l'output del gioco
        echo "$mid -> $r" >&2
        case $r in
            "più alto")  lo=$((mid + 1)) ;;
            "più basso") hi=$((mid - 1)) ;;
            giusto*)     break ;;
        esac
    done
} > risposte
```
```
                   ┌──────────── pipe ─────────────┐
  indovina.sh ─────┘                               ▼
      ▲  stdin                              { risolutore }
      └───────────── FIFO "risposte" ◀──────── stdout
```
I messaggi di avanzamento vanno su stderr perché lo stdout del risolutore è occupato dalla FIFO. Attenzione all'ordine di apertura: `< risposte` blocca finché qualcuno non apre la FIFO in scrittura, e `> risposte` fa esattamente questo, quindi i due lati si sbloccano a vicenda (§5.4).
(c) Un programma C che scrive su una pipe usa il buffer pieno (§3.2): la frase iniziale e le risposte resterebbero nel suo buffer, il risolutore aspetterebbe in `read` e il gioco aspetterebbe un numero: **stallo**. Rimedi: lanciarlo con `stdbuf -oL ./gioco` (funziona se il programma usa la stdio del C senza impostare il buffer da sé), oppure in un pseudo-terminale (`script -q -c ./gioco /dev/null`, `unbuffer`), oppure con gli strumenti della Lezione 8 (`pwntools` può usare un PTY).

**14.** Flag: `L4{flussi_e_pipe_cicli_e_coprocessi}`

```
$ cd ~/l4_sfida; cat LEGGIMI.txt
```
1. **porta1**: 5000 righe false su stdout, la vera su stderr (§1.2).
   ```
   $ ./porta1 > /dev/null
   L4{flussi_
   ```
   (Equivalente: `./porta1 2>&1 >/dev/null`.)
2. **porta2**: vuole la chiave su un descrittore diverso da 0, 1, 2. Il messaggio d'errore lo dice; il numero più naturale è 3 (§2.1).
   ```
   $ ./porta2
   porta2: mi serve la chiave su un descrittore che non è né 0, né 1, né 2
   $ ./porta2 3< chiave.txt
   e_pipe_
   ```
   Funziona anche `./porta2 3<<< apriti`.
3. **oracolo**: un ciclo da 0 a 999, scartando i "no" che vanno su stderr. Le risposte buone non hanno a capo, quindi si concatenano da sole.
   ```
   $ for i in {0..999}; do ./oracolo "$i"; done 2>/dev/null; echo
   cicli_
   ```
4. **porta4**: 50 somme in 10 secondi. Con un coprocesso (§5.5):
   ```bash
   #!/usr/bin/env bash
   coproc P { ./porta4; }
   while IFS= read -r riga <&"${P[0]}"; do
       echo "$riga"
       if [[ $riga =~ quanto\ fa\ ([0-9]+)\ \+\ ([0-9]+) ]]; then
           echo $(( BASH_REMATCH[1] + BASH_REMATCH[2] )) >&"${P[1]}"
       fi
   done
   ```
   ```
   ...
   Domanda 50 di 50: quanto fa 49 + 302?
   Bravo: e_coprocessi}
   ```
   Oppure con una FIFO, come nell'Esercizio 13:
   ```
   $ mkfifo f
   $ ./porta4 < f | while IFS= read -r r; do echo "$r" >&2; [[ $r =~ ([0-9]+)\ \+\ ([0-9]+) ]] && echo $(( BASH_REMATCH[1] + BASH_REMATCH[2] )); done > f
   ```
   Il `+` nella regex va protetto con il backslash perché in ERE è un quantificatore (L3 §4.2). Dentro `$(( ))` gli elementi di `BASH_REMATCH` sono già stati convalidati dalla regex (solo cifre), quindi non c'è rischio di iniezione aritmetica (§14.3).

**15.**
(a) Vedi §14.3: `(( x == 1 ))` con `x='a[$(echo ESEGUITO >&2)]'` stampa `ESEGUITO`.
(b)
```bash
controlla_pin() {
    local pin=$1
    if [[ $pin == 1234 ]]; then echo ok; else echo no; return 1; fi
}
```
La soluzione più sicura è non usare affatto l'aritmetica: un PIN è una **stringa** di cifre, e il confronto di stringhe con `[[ == ]]` (con il lato destro letterale) non valuta nulla. Se servisse un confronto numerico, prima la convalida: `[[ $pin =~ ^[0-9]{1,8}$ ]] || return 1`, poi `(( 10#$pin == 1234 ))`; `10#` forza la base 10, altrimenti `0123` verrebbe letto in ottale (L1 §8.5). Nota la differenza di comportamento: con il confronto numerico `01234` è accettato, con quello di stringa no.
(c) `[` è un comando normale (§9.1): riceve la stringa e la converte in intero con le regole del C, quindi `a[$(...)]` è solo un errore *integer expression expected*. `[[ ]]` e `(( ))` sono costrutti della shell, che con `-eq` valuta entrambi gli operandi come **espressioni aritmetiche** di bash: un nome di variabile viene risolto, un indice di array valutato, e la sostituzione di comando dentro l'indice eseguita.

**16.** Problemi (almeno sei) e correzioni:

| # | Problema | Classe |
|---|---|---|
| 1 | il file è `rwxrwxrwx`: **chiunque** può modificarlo, e cron lo esegue come root | CWE-732 |
| 2 | `/tmp/backup_DATA` è prevedibile: un utente può crearlo prima, come directory propria o link simbolico, e ricevere i backup di tutti, o far scrivere root dove vuole | CWE-377, CWE-59 |
| 3 | `$DEST`, `$u` non quotati: divisione in parole e globbing | CWE-88 (iniezione di argomenti) |
| 4 | `for u in $(ls /home)`: si rompe con nomi con spazi o caratteri speciali (§10.1) | |
| 5 | `eval` con il contenuto di `/etc/backup_note`: chi controlla quel file esegue comandi come root | CWE-95, CWE-78 |
| 6 | password in chiaro nello script **e** negli argomenti di `curl`, visibile in `/proc/<PID>/cmdline` a tutti mentre gira | CWE-798, CWE-214 |
| 7 | FTP trasmette credenziali e dati in chiaro | CWE-319 |
| 8 | `PATH` non impostato e nessun controllo degli errori; `#!/bin/sh` con dash (qui non è un bug di sintassi, ma limita gli strumenti disponibili) | |
| 9 | i backup in `/tmp` sono creati con l'`umask` di default, quindi probabilmente leggibili da tutti | CWE-276 |

Versione corretta (il file va reso di proprietà di root con permessi `700`: `chown root:root backup.sh; chmod 700 backup.sh`):
```bash
#!/usr/bin/env bash
set -euo pipefail
PATH=/usr/sbin:/usr/bin:/sbin:/bin
umask 077                                        # file creati leggibili solo da root

dest=$(mktemp -d /var/backups/backup.XXXXXX)     # directory privata, nome imprevedibile
for home in /home/*/; do
    u=$(basename -- "$home")
    tar -czf "$dest/$u.tgz" -C /home -- "$u"
done

nota=$(cat /etc/backup_note)                     # trattata come dato, mai eseguita
printf 'backup completato in %s per %s\n' "$dest" "$nota"

for f in "$dest"/*.tgz; do
    # credenziali in un file 600 di root (formato .netrc), protocollo cifrato
    curl --netrc-file /root/.backup_netrc -T "$f" "sftp://backup.interno/"
done
```

**17.**
(a) Un lettore riceve EOF solo quando **ogni** descrittore aperto sull'estremità di scrittura della pipe è stato chiuso, in tutti i processi (§4.2). Dopo `pipe()` entrambe le estremità esistono nel padre; `fork` ne crea copie in ogni figlio (§1.3). Se il processo lettore, prima di `execve`, non chiude la **sua** copia dell'estremità di scrittura, quella copia resta aperta per tutta la vita del lettore stesso: quando lo scrittore finisce e chiude la sua, rimane comunque uno scrittore (il lettore stesso), e la `read` del lettore aspetta per sempre dati che nessuno manderà. Per questo la shell, dopo ogni `dup2`, chiude esplicitamente le estremità originali in ogni figlio e nel padre.
(b) Per eseguire uno script, il kernel apre il file, legge lo shebang, e lancia l'interprete passandogli il **nome** dello script; l'interprete poi **riapre** il file per nome. Tra le due aperture c'è un intervallo di tempo in cui il nome può cambiare significato. Se il kernel concedesse i privilegi setuid all'interprete, un utente potrebbe creare un link simbolico al vero script setuid, lanciarlo, e nell'intervallo sostituire il link con un link al **proprio** script: l'interprete, con i privilegi del proprietario, eseguirebbe il codice dell'attaccante. È una TOCTOU (CWE-367, L2 §9.5). In più, gli interpreti sono sensibili all'ambiente (`IFS`, `ENV`, `BASH_ENV`, `PATH`), che chi lancia lo script controlla. Linux quindi ignora il bit, e i privilegi per uno script si concedono con `sudo`.
(c) La redirezione `>> /etc/file` è eseguita dalla **tua** shell, senza privilegi, prima di lanciare `sudo echo x`; `sudo` dà i privilegi solo a `echo`, che non ne ha bisogno. Il file viene aperto senza privilegi e l'operazione fallisce con *Permission denied*. Modi corretti: `echo x | sudo tee -a /etc/file > /dev/null` (è `tee`, con privilegi, ad aprire il file, §5.1), oppure `sudo sh -c 'echo x >> /etc/file'` (la redirezione è fatta da una shell che ha già i privilegi).

## Domande di autoverifica: punti chiave attesi

1. Un intero, indice nella tabella dei descrittori del processo, che punta a una descrizione di file aperto del kernel (modalità e offset), che punta all'inode. Due descrittori che puntano alla stessa descrizione avanzano insieme (§1.1).
2. Perché eredita già aperti i descrittori 0, 1 e 2, sistemati dalla shell tra `fork` ed `execve` (§1.2–1.3).
3. Le redirezioni si applicano da sinistra a destra e `2>&1` è `dup2(1, 2)`, una copia istantanea: nel primo caso 2 copia un 1 già spostato su `f`, nel secondo copia l'1 ancora sul terminale (§2.2).
4. Here-document con espansioni; letterale; con le tabulazioni iniziali tolte; here-string di una riga (§2.3).
5. stdout a righe su un terminale, a buffer pieno su file e pipe; stderr senza buffer. In una pipe lo stdout esce a blocchi (§3).
6. `pipe`, due `fork`, `dup2` dell'estremità giusta su 1 o su 0 in ciascun figlio, chiusura delle estremità, `execve`; il padre attende entrambi. Sono due processi indipendenti, collegati dal buffer del kernel (§4.1–4.2).
7. Quando tutti gli scrittori hanno chiuso; lo scrittore riceve `SIGPIPE`, codice 141 (§4.2).
8. `read` gira in una subshell. `read v <<< x`, `read v < <(cmd)`, `v=$(cmd)` (§4.4).
9. `[ ]` è un comando POSIX soggetto a divisione in parole; `[[ ]]` è sintassi di bash, sicura sulle variabili, con glob e regex; `(( ))` è aritmetica. Stringhe e file con `[[ ]]`, numeri **convalidati** con `(( ))` (§9.2, §14.3).
10. `while IFS= read -r riga || [ -n "$riga" ]; do ...; done < file` (§10.3).
11. Un codice di uscita da 0 a 255; i dati si stampano e si catturano con `$(...)` (§11).
12. Non interviene nelle condizioni e dopo `!`; `((c++))` con `c=0` termina lo script; `local x=$(cmd)` nasconde l'errore (§7.3).
13. Pulire sempre, anche in caso d'errore; creare file temporanei con nomi imprevedibili e in modo esclusivo (§13.1).
14. Variabili non quotate (`"$x"`, `--`); `eval` (array, `${!nome}`); iniezione aritmetica (convalida con regex); file temporanei (`mktemp`); segreti negli argomenti (file, stdin); script scrivibili eseguiti da root (permessi) (§14).
