# Modulo 1 — Lezione 5: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. I comandi sono stati provati con bash 5.2 su Linux 6.x; PID, utenti, orari e processi in esecuzione saranno diversi sul tuo sistema. I riferimenti `§` rimandano alle sezioni di `Lezione.md`.

## ★ Base

**1.**
```
$ echo "PID=$$ PPID=$PPID"
$ p=$$; while [ "$p" -ne 0 ]; do ps -o pid=,ppid=,user=,comm= -p "$p"; p=$(ps -o ppid= -p "$p" | tr -d ' '); done
$ pstree -s -p $$
```
Il ciclo si ferma al PID 1, il cui PPID è 0 (§2.3). Sopra la shell trovi l'emulatore di terminale (`gnome-terminal-server`, `konsole`, `xterm`...) se sei su un desktop, catene di `sshd` se sei collegato da remoto, `login` se sei su una console testuale, `tmux: server` se lavori in tmux, `docker-init` o il programma di avvio del container se sei in un container. Il padre della shell racconta **come** sei entrato nella macchina: è la stessa domanda che si pone un analista forense davanti a una shell sospetta.

**2.** (a) Una shell di login in attesa ha `Ss` (S = in attesa interrompibile, s = leader di sessione). Il comando `ps aux` stesso compare con `R+` (in esecuzione, nel gruppo in primo piano del terminale). I thread del kernel sono quelli tra parentesi quadre con `VSZ` e `RSS` a 0 e `TTY` `?`, ad esempio `[kthreadd]` in stato `S` o `[kworker/...]` in stato `I`.
(b)
```
$ ps -eo pid,user,ni,etime,cmd --sort=-%cpu | head -6
```
(c)
```
$ ps -u root -o pid= | wc -l
$ ps -u "$USER" -o pid= | wc -l
$ ps -eo user= | sort | uniq -c | sort -rn      # tutti gli utenti, in un colpo solo
```
(d) `%CPU` di `ps` è il tempo di CPU usato **diviso l'intera vita** del processo: un processo che ha lavorato al 100% per un minuto e poi ha dormito per un'ora mostra circa 1,6%. `top` calcola invece la percentuale **nell'ultimo intervallo** di aggiornamento (§5.1, §6.1).

**3.**
```
$ sleep 1000 &
$ p=$!
$ grep -E '^(Name|State|PPid|Uid):' /proc/$p/status    # Uid: reale effettivo salvato fs
$ tr '\0' ' ' < /proc/$p/cmdline; echo
$ readlink /proc/$p/cwd /proc/$p/exe
$ ls /proc/$p/fd | wc -l; ls -l /proc/$p/fd
$ tr '\0' '\n' < /proc/$p/environ | grep '^HOME='
$ kill $p
```
Di solito `sleep` ha tre descrittori, 0, 1 e 2, che puntano al terminale (`/dev/pts/N`), ereditati dalla shell. Se lanci `sleep` da uno script con le redirezioni, vedrai i file delle redirezioni (L4 §1.3).

**4.**
```
$ sleep 1000 & p=$!
$ kill -STOP $p; ps -o pid,stat,cmd -p $p        # STAT = T
$ kill -CONT $p; ps -o pid,stat,cmd -p $p        # STAT = S
$ kill -TERM $p; wait $p; echo $?                # 143
$ sleep 1000 & p=$!; kill -KILL $p; wait $p; echo $?   # 137
$ sleep 1000 & p=$!; kill -INT $p; wait $p; echo $?    # 130 (in una shell interattiva)
$ for n in 130 137 139 143; do echo "$n = $(kill -l $n)"; done
130 = INT
137 = KILL
139 = SEGV
143 = TERM
```
`kill -l` accetta direttamente lo stato di uscita: sottrae 128 se il numero supera 128. In uno script il `kill -INT` non avrebbe effetto, perché i processi in background di una shell non interattiva ignorano `SIGINT` (§9.5).

**5.**
```
$ sleep 300            # poi Ctrl-Z
[1]+  Stopped                 sleep 300
$ sleep 400 &
[2] 6012
$ cat &
[3] 6013
[3]+  Stopped                 cat
$ jobs -l
[1]-  6010 Stopped                 sleep 300
[2]   6012 Running                 sleep 400 &
[3]+  6013 Stopped (tty input)     cat
$ bg %1
[1]- sleep 300 &
$ fg %3                # cat in primo piano: scrivi qualcosa, poi Ctrl-D
$ kill %1 %2
```
`cat` senza argomenti legge dal terminale; essendo in background, il driver del terminale gli manda `SIGTTIN` appena prova a leggere, e il job si ferma (§9.2). `fg` lo mette nel gruppo in primo piano e gli manda `SIGCONT`.

## ★★ Intermedio

**6.** (a)
```
$ bash -c 'sleep 1 & exec sleep 60' &
$ sleep 2; ps -eo pid,ppid,stat,cmd | awk '$3 ~ /^Z/'
   7101    7100 Z    [sleep] <defunct>
$ kill -9 7101; ps -o stat= -p 7101
Z
$ kill 7100            # uccido il padre (che ora esegue "sleep 60")
$ ps -o stat= -p 7101  # nessun output: lo zombie è stato adottato e raccolto da init
```
Il filtro è sullo stato che **inizia** per `Z`. `kill -9` non ha effetto perché il processo è già morto: resta solo il suo stato di uscita, in attesa di una `wait` che il padre (ora diventato il programma `sleep`) non farà mai. Uccidendo il padre, lo zombie diventa orfano; il nuovo padre (init o un *subreaper*) chiama `wait` e lo elimina.
(b)
```
$ bash -c 'sleep 60 & echo $!'
7150
$ ps -o pid,ppid,cmd -p 7150
$ ps -o pid,cmd -p "$(ps -o ppid= -p 7150)"
```
Su un server o in un container il PPID diventa 1. Su un desktop moderno spesso diventa il PID di `systemd --user`, che si è registrato come *subreaper* con `prctl(PR_SET_CHILD_SUBREAPER)` per raccogliere gli orfani dei processi della sessione utente (§4.5). Il secondo comando `ps` mostra proprio chi è il nuovo padre.

**7.**
```
$ x=1; ( x=2; echo "sub: $x $BASHPID" ); echo "shell: $x $BASHPID"; echo $$ | { read y; echo "y=$y"; }; echo "fuori: [$y]"
sub: 2 803
shell: 1 802
y=802
fuori: []
```
- `( ... )` è una subshell, cioè un `fork` della shell: ha una **copia** di `x`, la modifica, e la modifica muore con lei. `$BASHPID` mostra che è un processo diverso (803).
- La shell principale vede ancora `x=1`.
- Nella pipeline, il gruppo `{ read y; echo ... }` gira in un figlio (L4 §4.4): legge `802` (il `$$` espanso dalla shell principale prima di creare la pipeline) e lo stampa, ma la variabile `y` esiste solo nel figlio.
- Fuori, `y` è vuota.
Copiato: tutte le variabili, la directory, i descrittori. Non condiviso: niente torna dal figlio al padre, se non lo stato di uscita e ciò che il figlio scrive su un descrittore che il padre legge.

**8.**
```bash
#!/usr/bin/env bash
# maschere.sh — mostra i segnali ignorati, intercettati, bloccati e pendenti di un processo
[[ $# -eq 1 && -r /proc/$1/status ]] || { echo "uso: $0 PID (di un processo esistente)" >&2; exit 2; }
decodifica() {
  local m=$((16#$1)) n out=()
  for ((n = 1; n <= 64; n++)); do
    (( (m >> (n - 1)) & 1 )) && out+=("$(kill -l "$n" 2>/dev/null || echo "$n")")
  done
  echo "${out[*]:-nessuno}"
}
while IFS=$':\t ' read -r chiave valore; do
  case $chiave in
    SigIgn) echo "ignorati:     $(decodifica "$valore")" ;;
    SigCgt) echo "intercettati: $(decodifica "$valore")" ;;
    SigBlk) echo "bloccati:     $(decodifica "$valore")" ;;
    SigPnd|ShdPnd) [[ $valore != 0000000000000000 ]] && echo "pendenti:     $(decodifica "$valore")" ;;
  esac
done < "/proc/$1/status"
```
Risultati tipici:
- **shell interattiva** (`bash maschere.sh $$`): ignorati `QUIT TERM TSTP TTIN TTOU` (una shell interattiva non si fa uccidere da `kill` senza opzioni né sospendere da Ctrl-Z), intercettati `INT CHLD WINCH` e altri;
- **`nohup sleep 100 &`**: ignorati `HUP` (`SigIgn` 0x1, §8.6), intercettati nessuno: `sleep` non installa gestori;
- **`sleep 100 &` da uno script**: ignorati `INT QUIT` (0x6, §9.5);
- **processo dell'Esempio 4**: ignorati `QUIT TERM`, intercettati `INT USR2 CHLD`.
Il `read` con `IFS=$':\t '` separa la chiave dal valore spezzando su due punti, tabulazione e spazio.

**9.**
```bash
#!/usr/bin/env bash
# risposta.sh
trap 'echo "USR1 alle $(date +%T)"' USR1
trap 'echo chiusura; exit 0' TERM
trap '' INT
echo "PID $$"
modo=${1:-ciclo}
case $modo in
  ciclo)    while :; do sleep 1; done ;;
  lungo)    sleep 60 ;;
  attesa)   while :; do sleep 60 & wait $!; echo "wait ha restituito $?"; done ;;
esac
```
(a) Con `bash risposta.sh ciclo` e `kill -USR1 PID` dall'altro terminale, la riga compare entro un secondo: bash esegue il gestore appena `sleep 1` finisce.
(b) Con `lungo`, la riga compare solo dopo 60 secondi (o quando `sleep` termina): bash non interrompe un comando in primo piano per eseguire un `trap` (§8.5).
(c) Con `attesa`, la riga compare subito, seguita da `wait ha restituito 138`: 138 = 128 + 10, cioè `wait` è stato interrotto dal segnale 10 (`USR1`). Il `sleep 60` in background però è ancora vivo: il ciclo ne lancerà un altro, quindi in un programma vero conviene ucciderlo o riattenderlo (`wait $!` di nuovo). Nota infine che `trap '' INT` rende lo script immune a Ctrl-C, ma il `sleep` figlio eredita `INT` ignorato (perché le disposizioni ignorate passano attraverso `exec`), mentre i gestori di `USR1` e `TERM` **non** passano al `sleep`: un `kill -USR1` mandato al PID di `sleep` lo uccide.

**10.**
```
$ # (a) ignorato dopo exec
$ bash -c "trap '' USR1; exec sleep 100" & sleep 0.2; grep SigIgn /proc/$!/status
SigIgn:	0000000000000200          # bit 9 = segnale 10 = USR1
$ kill -USR1 $!; ps -o stat= -p $!     # ancora vivo
$ kill $!
$ # (b) il gestore non sopravvive
$ bash -c "trap 'echo x' USR1; exec sleep 100" & sleep 0.2; grep SigCgt /proc/$!/status
SigCgt:	0000000000000000
$ kill -USR1 $!; sleep 0.2; ps -o stat= -p $!      # nessun output: ucciso da USR1 (azione Term)
$ # (c) descrittore ereditato
$ exec 3< /etc/hostname; sleep 100 & ls -l /proc/$!/fd/3; kill $!; exec 3<&-
$ # (d) umask e directory
$ (umask 077; cd /tmp; sleep 100 & grep Umask /proc/$!/status; readlink /proc/$!/cwd; kill $!)
Umask:	0077
/tmp
$ # (e) variabile non esportata
$ SEGRETO=abc; bash -c 'echo "figlio: [$SEGRETO]"'; set | grep '^SEGRETO='
figlio: []
SEGRETO=abc
```
Il valore esatto di `SigIgn` in (a) dipende dal contesto: da una shell interattiva è 0x200, solo `USR1`; se lanci la prova da uno script si aggiungono 0x6 (`INT` e `QUIT`, §9.5), da cui 0x206.

**11.**
```
$ sleep 500 | sleep 501 &
$ setsid sleep 502 &
$ ps -o pid,ppid,pgid,sid,tpgid,tty,stat,cmd -C sleep
    PID    PPID    PGID     SID   TPGID TT       STAT CMD
   7301    4200    7301    4200    7330 pts/0    S    sleep 500
   7302    4200    7301    4200    7330 pts/0    S    sleep 501
   7303    7299    7303    7303      -1 ?        Ss   sleep 502
$ kill -- -7301
```
I due `sleep` della pipeline sono nello stesso gruppo (PGID 7301, il PID del primo), nella sessione della shell (4200), con il terminale `pts/0`, e non hanno `+` perché il gruppo in primo piano è un altro (quello di `ps`, 7330). `setsid sleep 502` è leader di una **nuova** sessione e di un nuovo gruppo (`PGID = SID = PID`, modificatore `s`), senza terminale (`?`, TPGID -1). (Il suo PPID può essere quello di un processo intermedio o 1: `setsid`, se è già leader di gruppo, fa un `fork` prima di chiamare `setsid()`.) `kill -- -7301` manda `SIGTERM` all'intero gruppo; il `--` serve perché `-7301` non sia scambiato per un'opzione.
Chiudendo il terminale, la shell riceve `SIGHUP` e lo inoltra ai suoi job: i due `sleep` della pipeline muoiono. `sleep 502` non appartiene alla sessione del terminale e non è un job della shell: sopravvive.

**12.**
```
$ ( ulimit -f 10; head -c 20000 /dev/zero > f ); echo "rc=$?"
File size limit exceeded
rc=153
$ ls -l f            # 10240 byte: 10 blocchi da 1024
$ ( ulimit -n 5; exec 5< /etc/passwd )
bash: 5: Bad file descriptor
$ ( ulimit -n 6; exec 5< /etc/passwd && echo ok )
ok
$ ( ulimit -Hn 100; ulimit -Sn 50; ulimit -Sn 100; echo "soft=$(ulimit -Sn)"; ulimit -Hn 200 )
soft=100
bash: ulimit: open files: cannot modify limit: Operation not permitted
```
(a) Il kernel manda `SIGXFSZ` (segnale 25, azione predefinita *Core*): 128 + 25 = 153. Il file contiene esattamente il limite, 10 × 1024 byte.
(b) Con `-n 5` i descrittori validi sono 0–4: aprire il numero 5 fallisce con `EBADF`. Con `-n 6` il 5 diventa disponibile. Il limite è sul **numero massimo di descrittore più uno**, non sul conteggio dei file aperti.
(c) Il soft si può alzare e abbassare liberamente fino all'hard; l'hard, una volta abbassato, può essere rialzato solo da root (con `CAP_SYS_RESOURCE`). Da root il messaggio dell'ultimo comando non compare. Per questo le prove si fanno in una subshell.

## ★★★ Sfida

**13.** Output (con `fflush`):
```
ciao [821 figlio di 819]
[822 figlio di 820]
[820 figlio di 819]
[819 figlio di 802]
```
- "ciao" compare **una volta**: viene stampato e svuotato dal buffer prima dei `fork`, quindi i figli non ne ereditano una copia.
- Dopo due `fork` ci sono **4 processi**: l'originale (819), il suo primo figlio (820), il secondo figlio dell'originale (821), il figlio di 820 (822). Ognuno stampa la sua riga tra parentesi.
- Ognuno poi aspetta tutti i suoi figli (`while (wait(NULL) > 0)`) e infine stampa `\n`. Un processo senza figli (821, 822) stampa subito l'a capo; l'originale aspetta 820 e 821, e 820 aspetta 822. Per questo gli a capo arrivano in un ordine che "chiude" le righe dei figli prima di quelle dei padri, ma l'ordine tra 820, 821 e 822 dipende dallo **scheduler** e cambia tra un'esecuzione e l'altra.
- Senza `fflush`: "ciao " resta nel buffer di `stdout` (non c'è un a capo, e in una pipe il buffer è pieno, non a righe), viene **copiato** dai `fork` insieme al resto della memoria, e ognuno dei 4 processi lo svuota alla fine. Risultato: **4 "ciao"**:
```
$ ./f2 | cat
ciao [837 figlio di 834]
ciao [838 figlio di 836]
ciao [836 figlio di 834]
ciao [834 figlio di 802]
```
Nota bene: succede lo stesso anche sul terminale, perché il buffering a righe svuota solo quando trova `\n`, e "ciao " non lo contiene. È la combinazione di copy-on-write (§4.1) e buffering della libreria C (L4 §3).

**14.** Soluzione della mini-CTF.
```
$ bash setup_sfida.sh
$ cd ~/l5_sfida; cat LEGGIMI.txt
```
*Pezzo 1, il custode.* "Porta il pezzo scritto addosso": nella riga di comando.
```
$ ps -eo pid,args | grep '[c]ustode'
   9101 custode[L5{i_processi_] 7200
```
`comm` di questo processo è `sleep`: lo trovi solo cercando nella riga di comando (`pgrep -af custode`), ed è un esempio di `exec -a` (§4.3, §5.3).

*Pezzo 2, il messaggero.* "Lo porta nel suo ambiente".
```
$ tr '\0' '\n' < /proc/$(pgrep -f '^messaggero')/environ | grep PEZZO
PEZZO=parlano_
```
`/proc/PID/environ` è leggibile perché il processo è tuo (§7.2, §13.1).

*Pezzo 3, la sentinella.* "Parla solo se riceve il segnale giusto". Invece di provare a caso (e di ucciderla con il segnale sbagliato), leggi le sue maschere:
```
$ p=$(pgrep -f '^sentinella'); grep -E 'SigIgn|SigCgt' /proc/$p/status
SigIgn:	0000000000000007
SigCgt:	0000000000010a00
```
`SigIgn` 0x7 = bit 0, 1, 2 = `HUP`, `INT`, `QUIT`: `HUP` ignorato da `nohup`, `INT` e `QUIT` perché il processo è stato lanciato in background da uno script (§9.5). `SigCgt` 0x10a00 = bit 9, 11, 16 = segnali 10 (`USR1`), 12 (`USR2`), 17 (`CHLD`, che bash intercetta sempre). Restano due candidati, `USR1` e `USR2`. (Curiosità: lo script della sentinella prova a intercettare anche `HUP`, ma una shell non interattiva **non può** intercettare un segnale che era già ignorato quando è partita: `man bash`, builtin `trap`. È un'altra faccia dell'eredità delle disposizioni.) Provando:
```
$ kill -USR2 $p; sleep 1.5; cat risposta.txt
Non è il segnale giusto.
$ kill -USR1 $p; sleep 1.5; cat risposta.txt
a_chi_sa_
```
(L'attesa serve perché la sentinella esegue il gestore solo quando il suo `sleep 1` termina, §8.5.)

*Pezzo 4, l'ostinato.* "Vive dove è nascosto il pezzo": la sua directory corrente.
```
$ p=$(pgrep -f '^ostinato'); readlink /proc/$p/cwd
/home/zen/l5_sfida/.3fa9c1e07b2d
$ cat "$(readlink /proc/$p/cwd)/pezzo4.txt"
ascoltare}
```
La directory nascosta ha un nome casuale: cercarla con `ls -a` funziona, ma `cwd` la indica senza ambiguità.

**Flag:** `L5{i_processi_parlano_a_chi_sa_ascoltare}`

*Pulizia.*
```
$ pkill -f '^custode\[|^messaggero|^sentinella|^ostinato'
$ pgrep -af '^ostinato'                      # è ancora vivo!
$ grep SigIgn /proc/$(pgrep -f '^ostinato')/status
SigIgn:	0000000000004001                     # TERM (bit 14) e HUP (bit 0, da nohup)
$ pkill -KILL -f '^ostinato'
```
L'ostinato è un `sleep` lanciato da una bash con `trap '' TERM` e poi `exec`: la disposizione *ignorata* è sopravvissuta all'`exec` (§8.3, §12.1). Contro `SIGKILL` non c'è difesa.

**15.** (a)
```bash
#!/usr/bin/env bash
# spia2.sh [-u UTENTE] [SECONDI]
filtro=""
if [[ $1 == -u ]]; then filtro=$(id -u "$2") || exit 2; shift 2; fi
declare -A visto
for d in /proc/[0-9]*; do visto[${d#/proc/}]=1; done
fine=$((SECONDS + ${1:-10}))
while (( SECONDS < fine )); do
  for d in /proc/[0-9]*; do
    p=${d#/proc/}
    [[ -n ${visto[$p]} ]] && continue
    visto[$p]=1
    u=$(stat -c %u "$d" 2>/dev/null) || continue
    [[ -n $filtro && $u != "$filtro" ]] && continue
    c=$(tr '\0' ' ' < "$d/cmdline" 2>/dev/null) || continue
    pp=$(awk '/^PPid:/ {print $2}' "$d/status" 2>/dev/null)
    [[ -n $c ]] && printf '%(%T)T %-8s pid=%-6s ppid=%-6s %s\n' -1 "$(id -nu "$u" 2>/dev/null || echo "$u")" "$p" "$pp" "$c"
  done
  sleep 0.05
done
```
(b) Con il ciclo simulato in background e `bash spia2.sh 15`, ogni 3 secondi compaiono due righe, `bash -c tar czf ...` e `tar czf /tmp/b.tgz /etc/hostname` (più `gzip`, che `tar` lancia come figlio: un buon esempio di albero di processi che non avresti immaginato). Il PPID di `bash -c` è il ciclo `while` in background.
(c) Il lavoro vive pochi decimi di secondo ogni 3 secondi: un `ps` lanciato a mano ha poche probabilità di cadere nell'intervallo giusto. Quando guardi, il ciclo esterno è quasi sempre in stato `S`, dentro `sleep 3` (o meglio: il ciclo è una subshell bash in `S`, in attesa con `wait4` del suo figlio `sleep`).

**16.** Problemi:
1. **Pidfile in `/tmp`** (CWE-377/CWE-379): chiunque può creare `/tmp/servizio.pid` prima del primo avvio o sostituirlo. Mettendoci il PID di un proprio processo, un attaccante fa credere che il servizio sia vivo (DoS); mettendoci un PID qualunque, controlla che cosa lo script "vede".
2. **Riuso dei PID** (CWE-367, §13.3): se il servizio muore e il PID viene riassegnato a un altro processo, `kill -0` ha successo e il servizio non viene mai riavviato. In più, da root `kill -0` funziona con **qualunque** processo, quindi il controllo è debole.
3. **Password sulla riga di comando** (CWE-214, §13.1): `--db-password=Sup3rS3gr3t0` è visibile a ogni utente con `ps aux` finché il servizio è vivo, e il segreto è anche scritto in chiaro nello script.
4. **`$(cat $PIDFILE)` non quotato e senza controllo**: se il file contiene `-1`, `kill -0 -1` riguarda tutti i processi; se contiene più parole, `kill` riceve più argomenti. Da root e con un file controllabile da altri è un'iniezione di argomenti (CWE-88).
5. **`cd` senza controllo** (L4 §13.2): se `/opt/servizio` non esiste, lo script esegue `./servizio` nella directory corrente di `cron`.
6. **Il servizio gira come root**, eredita l'ambiente e i descrittori di `cron`, nessun limite di risorse, niente log; e se `/opt/servizio` o il binario sono scrivibili da altri utenti, lo script esegue come root il codice di chiunque (CWE-732, L4 §14.7).
7. Race tra due esecuzioni: se il servizio impiega più di un minuto a scrivere il pidfile o a partire, `cron` lancia una seconda copia.

Versione corretta "minima":
```bash
#!/usr/bin/env bash
set -euo pipefail
PIDFILE=/run/servizio/servizio.pid           # directory di root, non scrivibile da altri
exec 9> /run/servizio/lock; flock -n 9 || exit 0   # una sola esecuzione per volta
vivo() {
  local p
  [[ -r $PIDFILE ]] || return 1
  p=$(<"$PIDFILE")
  [[ $p =~ ^[0-9]+$ ]] || return 1
  [[ $(readlink "/proc/$p/exe" 2>/dev/null) == /opt/servizio/servizio ]]
}
if ! vivo; then
  cd /opt/servizio || exit 1
  setpriv --reuid=servizio --regid=servizio --init-groups \
    ./servizio --db-password-file=/etc/servizio/db.pass </dev/null >>/var/log/servizio.log 2>&1 &
  echo $! > "$PIDFILE"
fi
```
La soluzione **giusta** però è un'unità di systemd: systemd è il padre del servizio, sa con certezza se è vivo senza pidfile, lo riavvia (`Restart=on-failure`), lo esegue con un utente dedicato (`User=servizio`), passa i segreti in modo sicuro (`LoadCredential=`), raccoglie i log e impone limiti (`TasksMax=`, `MemoryMax=`, `NoNewPrivileges=yes`):
```ini
[Service]
ExecStart=/opt/servizio/servizio --db-password-file=%d/dbpass
LoadCredential=dbpass:/etc/servizio/db.pass
User=servizio
Restart=on-failure
NoNewPrivileges=yes
TasksMax=64
```

**17.** Tracce per le risposte.
(a) Separare `fork` ed `exec` permette di preparare il figlio con le normali chiamate di sistema (redirezioni, directory, utente, limiti, segnali) senza un'interfaccia apposita con decine di parametri (§4.3, OSTEP cap. 5). Le alternative: `vfork` (il figlio condivide la memoria del padre finché non chiama `exec`; veloce ma pericolosa), `posix_spawn` (un'unica chiamata con una lista di "azioni" da eseguire nel figlio: è ciò che usano molti runtime moderni), `clone`/`clone3` con flag scelti. Baumann et al. sostengono che `fork` non è più una buona astrazione: copia uno stato enorme e implicito (thread, buffer, descrittori, mappe di memoria), non è thread-safe (un figlio di un programma multithread ha un solo thread e magari un lock preso da un thread che non esiste più), complica il kernel, e il copy-on-write non lo rende gratuito per processi molto grandi; propongono `posix_spawn` come interfaccia predefinita.
(b) Se ogni segnale si potesse intercettare o ignorare, un programma difettoso o malevolo potrebbe rendersi **impossibile da fermare**: nessuno, nemmeno root, potrebbe terminarlo o sospenderlo senza riavviare. `SIGKILL` e `SIGSTOP` sono gestiti interamente dal kernel, senza eseguire codice del processo, ed è questo che li rende affidabili (eccezione: un processo in stato `D` non li riceve finché l'attesa non finisce).
(c) Un segnale può interrompere il programma in qualunque istruzione. Se in quel momento il programma sta modificando una struttura dati condivisa (ad esempio la lista dei blocchi liberi dentro `malloc`) e il gestore usa la stessa struttura (chiamando `malloc`, `free` o funzioni che le usano, come `syslog`), la struttura viene vista e modificata a metà: è corrotta. "Async-signal-safe" indica le funzioni che non hanno questo problema. In OpenSSH, il gestore di `SIGALRM` chiamava funzioni non sicure; l'attaccante, controllando il momento in cui il timer scadeva (cioè quando il segnale arrivava) e ripetendo migliaia di connessioni, riusciva a far scattare il segnale proprio dentro `free`, e a sfruttare la corruzione dello heap per eseguire codice nel processo `sshd`, che gira come root.
