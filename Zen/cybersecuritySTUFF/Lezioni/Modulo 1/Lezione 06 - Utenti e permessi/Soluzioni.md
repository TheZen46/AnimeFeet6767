# Modulo 1 — Lezione 6: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. I comandi sono stati provati con bash 5.2 su Linux 6.x; UID, nomi utente e orari saranno diversi sul tuo sistema. I riferimenti `§` rimandano alle sezioni di `Lezione.md`. Dove serve un secondo utente, si suppone `prova`, membro del gruppo `prova` ed eventualmente di `team`/`revisori` dove indicato.

## ★ Base

**1.** Traduzione e lettura.

| Stringa | Ottale | Lettura |
|---|---|---|
| `-rwsr-xr-x` | `4755` | file setuid: proprietario rwx **+ setuid**, gruppo e altri r-x. Eseguito, gira come il proprietario. Nessun bit sprecato. |
| `drwxrwxrwt` | `1777` | directory con tutti i permessi a tutti **+ sticky**: ognuno crea file suoi ma non cancella quelli degli altri (è `/tmp`). |
| `-rw-r-----` | `640` | file di dati: proprietario legge/scrive, gruppo legge, altri niente (è `/etc/shadow`). |
| `drwx--x--x` | `711` | directory attraversabile ma non elencabile: entri in `dir/file` se ne conosci il nome, ma non puoi fare `ls` (home con `public_html`). |
| `-r-Sr--r--` | `4544` | setuid **maiuscolo**: il bit setuid c'è ma il proprietario non ha `x`. Bit **sprecato**: il programma non è eseguibile dal proprietario, e il setuid non si applica (serve `x` per il proprietario). Probabile errore. |

**2.** Conversioni.

```
chmod u=rwx,g=rx,o=        → chmod 750
chmod u=rw,go=             → chmod 600
chmod a=r,u+w              → chmod 644
chmod u=rwx,g=rx,o=rx,g+s  → chmod 2755
```
E il contrario:
```
640  → u=rw,g=r,o=       (o: a=r,u+w,g-w... la prima è più chiara)
4755 → u=rwxs,g=rx,o=rx  (oppure: chmod 755 f; chmod u+s f)
1777 → a=rwx,o+t          (oppure +t su 777)
2750 → u=rwx,g=rxs,o=     (oppure: chmod 750 f; chmod g+s f)
```

**3.** umask.

| umask | file | directory |
|---|---|---|
| `022` | `644` | `755` |
| `077` | `600` | `700` |
| `002` | `664` | `775` |
| `027` | `640` | `750` |
| `026` | `640` | `751` |
| `017` | `660` | `760` |

Con `017` un file nasce `660`, non `661`: la umask `017` toglierebbe anche il bit `x` agli altri, ma il file è stato **richiesto** `666` (senza `x`), quindi su quel bit non c'è niente da togliere. La umask può solo spegnere bit accesi, non accenderne (§8.2). La directory, richiesta `777`, diventa invece `760` perché l'`x` degli altri c'era.

**4.** Proprietario contro gruppo, file `406` (`r-----rw-`), gruppo `prova`.
```
$ echo dati > f; sudo chgrp prova f; chmod 406 f; ls -l f
-r-----rw- 1 zen prova 5 ...
$ cat f        # da proprietario: OK, i bit del proprietario sono r--
dati
$ echo x >> f  # da proprietario: FALLISCE, il proprietario non ha w
bash: f: Permission denied
```
L'algoritmo (§6.2) sceglie la **prima** classe applicabile: sei il proprietario, quindi conta `r--`, e **solo** quello, anche se "altri" avrebbero `rw-`. L'utente `prova` è nel **gruppo**: per lui conta `---`, quindi non legge né scrive (e non ricade su "altri"). Un terzo utente, né proprietario né nel gruppo, usa i bit "altri" `rw-`: legge e scrive. È il paradosso del §6.2: il proprietario ha meno diritti di uno sconosciuto.

**5.** Directory.
```
$ mkdir -p ~/l6/d; echo s > ~/l6/d/segreto; chmod 644 ~/l6/d/segreto; chmod 711 ~/l6/d
# da un altro utente:
$ ls ~zen/l6/d
ls: cannot open directory '.../d': Permission denied      # manca r: non si legge la tabella
$ cat ~zen/l6/d/segreto
s                                                          # c'è x (attraverso) + segreto è 644
```
`ls` ha bisogno di `r` sulla directory (leggere i nomi); `cat d/segreto` ha bisogno di `x` sulla directory (attraversarla) e di `r` sul file. Con `711` c'è `x` ma non `r`: puoi raggiungere ciò di cui conosci il nome, non elencare (§6.4). Con `744` (`rwxr--r--`) dall'esterno `x` sparisce per gli altri (resta `r--` = `4`): ora `ls` dà i nomi ma `cat d/segreto` fallisce, perché senza `x` non si attraversa la directory per raggiungere l'inode del file. Le due prove mostrano che `r` e `x` su una directory sono indipendenti.

**6.** passwd e shadow.
```
(a) $ getent passwd | awk -F: '$3>=1000 && $3<60000 {print $1, $7}'
(b) $ getent passwd | awk -F: '{print $7}' | sort | uniq -c | sort -rn
(c) $ awk -F: '$3==0 {print $1}' /etc/passwd        # deve uscire solo "root"
(d) $ sudo awk -F: '$1=="zen"{print $2}' /etc/shadow | cut -c1-3
    $y$    → yescrypt   ($6$ = sha512, $2b$ = bcrypt, $1$ = MD5 debole)
```

## ★★ Intermedio

**7.** Lista nera. Un file leggibile da tutti tranne il gruppo `blocco`:
```
$ echo contenuto > f
$ sudo chgrp blocco f
$ chmod 704 f            # u=rwx, g=---, o=r--
$ ls -l f
-rwx---r-- 1 zen blocco 10 ...
```
Chi è nel gruppo `blocco` incontra la classe "gruppo" (`---`) e si ferma lì; chi non c'è usa "altri" (`r--`) e legge. Verifica con un utente in `blocco` e uno fuori.
Perché è fragile, almeno due modi: (1) **copia indiretta** — un utente fuori da `blocco` legge il file e ne fa una copia leggibile da tutti; da quel momento il contenuto è fuori controllo. (2) Chi è in `blocco` può comunque ottenere il contenuto se esiste un **altro percorso** allo stesso inode (un link fisico fatto da chi poteva leggerlo) o se il file viene mai dato in pasto a un programma che ne mostra il contenuto a tutti. (3) In generale, la lista nera non sopravvive a `tar`, backup, invii: appena il dato esce dal file originale, i suoi permessi non lo seguono. Per questo si protegge con una **lista bianca** (dare accesso solo a chi serve), non con una nera.

**8.** Cartella condivisa senza ACL.
```
$ sudo mkdir /srv/t && sudo chgrp team /srv/t && sudo chmod 2770 /srv/t
# anna (umask 002):
anna$ umask 002; echo a > /srv/t/fa; ls -l /srv/t/fa     # -rw-rw-r-- anna team
# zen (umask 002): può modificare fa perché è team e il file è rw per il gruppo
zen$  umask 002; echo z >> /srv/t/fa && echo ok          # ok
# ma se anna ha umask 077:
anna$ umask 077; echo a2 > /srv/t/fa2; ls -l /srv/t/fa2  # -rw------- anna team
zen$  echo z >> /srv/t/fa2                                # Permission denied!
```
Il setgid garantisce il **gruppo** giusto (`team`) su ogni file, ma **non** i permessi: quelli dipendono dalla umask di chi crea. Con `077` il gruppo non ha `w` (anzi, niente), e la collaborazione si rompe. Aggiungendo l'ACL predefinita:
```
$ sudo setfacl -m d:g:team:rwX /srv/t
anna$ umask 077; echo a3 > /srv/t/fa3; getfacl /srv/t/fa3 | grep team
group:team:rwx
```
Ora i file nascono con `rwx` (meno la mask) per `team` **indipendentemente dalla umask**, perché quando c'è un'ACL predefinita la umask non viene applicata (§10.4): al suo posto valgono i permessi dell'ACL predefinita intersecati con quelli richiesti. È la ragione per cui l'ACL predefinita è il modo robusto di costruire cartelle condivise.

**9.** I bit speciali (tutti gli esperimenti provati; da **utente normale**, non root).
```
(a) $ cp /bin/true t; chmod 4755 t; ls -l t     # -rwsr-xr-x
    $ echo >> t; ls -l t                          # -rwxr-xr-x  → setuid azzerato dalla scrittura
    Scappatoia chiusa: sostituire il codice di un programma setuid mantenendone i privilegi.
(b) $ chmod 4755 t; sudo chown root t; ls -l t   # -rwxr-xr-x  → chown azzera setuid/setgid
    Scappatoia chiusa: far "regalare" a root un eseguibile setuid altrui.
(c) $ printf '#!/bin/sh\nid -u\n' > s.sh; sudo chown root s.sh; sudo chmod 4755 s.sh
    $ ./s.sh                                       # stampa il TUO uid (es. 1000), non 0
    Scappatoia chiusa: la race condition sugli script setuid (il kernel li ignora del tutto).
(d) $ sudo mkdir /srv/pub; sudo chmod 1777 /srv/pub
    anna$ echo x > /srv/pub/fa; chmod 666 /srv/pub/fa
    zen$  rm /srv/pub/fa        # EPERM: lo sticky impedisce di cancellare il file di un altro
    zen$  echo y >> /srv/pub/fa # OK: i permessi 666 consentono la scrittura del contenuto
    Scappatoia chiusa: cancellare/sostituire i file altrui in una directory condivisa.
```

**10.** `permspiega`. Una versione:
```bash
#!/usr/bin/env bash
# permspiega PERCORSO — descrive i permessi di un file
f="$1"
[ -e "$f" ] || { echo "non esiste: $f" >&2; exit 1; }
read -r oct sym own grp <<<"$(stat -c '%a %A %U %G' "$f")"
echo "file:        $f"
echo "ottale:      $oct      simbolico: $sym"
echo "proprietario: $own    gruppo: $grp"
# bit per un terzo utente (classe 'altri' = ultime 3 cifre di sym)
o="${sym:7:3}"
echo "un terzo utente: r=$([[ $o == r* ]] && echo sì || echo no) \
w=$([[ ${o:1:1} == w ]] && echo sì || echo no) \
x=$([[ ${o:2:1} =~ [xt] ]] && echo sì || echo no)"
# bit speciali
[[ $sym =~ ^...[sS] ]] && echo ">> setuid: eseguito, gira come $own"
[[ $sym =~ ^......[sS] ]] && echo ">> setgid: gira come gruppo $grp (file) / eredita gruppo (dir)"
[[ $sym =~ [tT]$ ]] && echo ">> sticky: solo il proprietario del file può cancellarlo (dir)"
# ACL
[[ $sym == *+ ]] && { echo ">> ha una ACL (+). Dettaglio:"; getfacl -p "$f" | sed 's/^/     /'; }
# capability
c=$(getcap "$f" 2>/dev/null); [ -n "$c" ] && echo ">> capability: $c"
```
Provato su `/usr/bin/passwd` (setuid root), `/etc/shadow` (640, un terzo utente niente), `/tmp` (sticky), `/etc/sudoers` (440), e un file con ACL creato nell'Es. 12.

**11.** La finestra temporale.
```bash
# vittima_sbagliata.sh
umask 022
echo "SEGRETO" > cred; chmod 600 cred      # per un istante è 644
# vittima_giusta.sh
( umask 077; echo "SEGRETO" > cred )        # mai leggibile da altri
# oppure: install -m 600 /dev/null cred; echo SEGRETO > cred
```
Con un secondo utente in ciclo stretto:
```
altro$ while :; do cat ~zen/l6/cred 2>/dev/null && { echo RUBATO; break; }; done
```
Lanciando ripetutamente `vittima_sbagliata.sh` dall'utente `zen`, prima o poi l'altro terminale stampa `RUBATO`: ha aperto il file nell'istante fra `>` e `chmod`. Con `vittima_giusta.sh` non succede mai. Nota (§14.7): se l'attaccante è riuscito ad **aprire** il file in quell'istante, il descrittore resta valido anche dopo il `chmod 600`; chiudere la finestra a posteriori non basta. La soluzione è non aprirla: impostare la umask (o i permessi) **prima** di scrivere il contenuto.

**12.** ACL complete.
```
$ touch piano.txt
$ setfacl -m u:anna:r,u:bruno:rw,g:revisori:r piano.txt
$ ls -l piano.txt                     # -rw-rw-r--+  (il + segnala l'ACL)
$ chmod g-w piano.txt                 # tocca la MASCHERA, non il gruppo proprietario
$ getfacl piano.txt
...
user:bruno:rw-			#effective:r--   ← la maschera r-- declassa bruno a sola lettura
mask::r--
...
$ setfacl -b piano.txt                # rimuove tutta l'ACL estesa
```
`chmod g-w` su un file con ACL abbassa la **maschera** a `r--`: tutte le voci "di mezzo" (utenti nominati, gruppo proprietario, gruppi nominati) vengono limitate, quindi `bruno` resta con `r--` effettivo pur avendo la voce `rw-`. Per questo `ls -l` non basta: mostra `rw-` nel campo gruppo (che è la maschera), ma non dice che esistono voci per `anna`, `bruno`, `revisori`. Solo `getfacl` rivela chi ha davvero accesso. È un punto cieco classico negli audit: un file con `+` va sempre esaminato con `getfacl`.

## ★★★ Sfida

**13.** Le credenziali che cambiano.
```
(a) $ grep -E 'Uid|Gid|Groups|CapEff|NoNewPrivs' /proc/self/status
    Uid: 1000 1000 1000 1000   CapEff: 0000000000000000   NoNewPrivs: 0
    $ sudo grep -E 'Uid|CapEff|NoNewPrivs' /proc/self/status
    Uid: 0 0 0 0               CapEff: 000001ffffffffff   NoNewPrivs: 0
    $ setpriv --reuid=1000 --regid=1000 --init-groups grep -E 'Uid|Gid|CapEff' /proc/self/status
    Uid: 1000 1000 1000 1000   CapEff: 0000000000000000
```
(b) Un programma eseguito con `sudo` parte da un processo di root: ha **tutte** le capability negli insiemi permesso ed effettivo (riga `CapEff` piena). Un programma **setuid root** eseguito da un utente ottiene euid 0, e per le regole di compatibilità (§12.3) riceve anch'esso tutte le capability — ma il suo UID **reale** resta quello dell'utente, e se nel codice fa `setuid(getuid())` per abbassarsi perde tutte le capability effettive e permesse insieme allo UID 0. In pratica entrambi arrivano a euid 0, ma `sudo` è pensato per *restare* root, mentre un setuid ben scritto *abbassa* subito i privilegi. La differenza vera si vede in un servizio avviato con `AmbientCapabilities`: lì il processo ha **una sola** capability e non è mai stato root.
(c) `CapBnd` della shell di un utente normale contiene quasi tutte le capability:
```
$ grep CapBnd /proc/self/status
CapBnd: 000001ffffffffff
$ capsh --decode=000001ffffffffff | tr ',' '\n' | head
```
L'insieme **delimitante** non sono le capability che *hai* (quelle sono `CapEff`, a zero), ma il **tetto massimo** di ciò che potresti ottenere eseguendo un programma setuid root. È pieno perché il limite serve a essere *ristretto* dai container e dai servizi (`systemd` con `CapabilityBoundingSet=`), non dagli utenti: per default nessuno lo abbassa, quindi contiene tutto.

**14.** `audit_permessi.sh`. Una versione didattica, in sola lettura:
```bash
#!/usr/bin/env bash
# audit_permessi.sh — controlli di sola lettura sui permessi (versione "a mano" di lynis)
P(){ printf '[%s] %s\n' "$1" "$2"; }   # gravità, messaggio
echo "== Account =="
n=$(awk -F: '$3==0{print $1}' /etc/passwd | wc -l)
[ "$n" -gt 1 ] && P ALTA "più di un UID 0: $(awk -F: '$3==0{print $1}' /etc/passwd | tr '\n' ' ')"
awk -F: '$2==""{print $1}' /etc/passwd | while read u; do P ALTA "passwd vuota in /etc/passwd: $u"; done
if [ -r /etc/shadow ]; then awk -F: '$2==""{print $1}' /etc/shadow | while read u; do P ALTA "shadow vuota: $u"; done; fi
echo "== File di sistema =="
for pair in "/etc/passwd:644" "/etc/shadow:640" "/etc/sudoers:440"; do
  f=${pair%:*}; want=${pair#*:}; have=$(stat -c %a "$f" 2>/dev/null)
  [ -n "$have" ] && [ "$have" != "$want" ] && P MEDIA "$f ha $have, atteso $want"
done
find /etc -xdev -type f -perm -o+w 2>/dev/null | while read f; do P ALTA "scrivibile da tutti: $f"; done
echo "== Setuid inattesi =="
bianca='/usr/bin/su /usr/bin/sudo /usr/bin/passwd /usr/bin/chsh /usr/bin/chfn
/usr/bin/newgrp /usr/bin/gpasswd /usr/bin/mount /usr/bin/umount /usr/bin/pkexec
/usr/bin/fusermount3 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/polkit-1/polkit-agent-helper-1 /usr/lib/openssh/ssh-keysign'
find / -xdev -perm -4000 -type f 2>/dev/null | grep -vFf <(printf '%s\n' $bianca) \
  | while read f; do P ALTA "setuid root inatteso: $f"; done
echo "== Capability su interpreti =="
getcap -r / 2>/dev/null | grep -E 'perl|python|ruby|node|lua|php|vim|awk|tar|zsh|bash|gdb' \
  | while read l; do P ALTA "capability su interprete: $l"; done
echo "== Directory scrivibili senza sticky =="
find / -xdev -type d -perm -0002 ! -perm -1000 2>/dev/null \
  | while read d; do P MEDIA "0777 senza sticky: $d"; done
echo "== PATH =="
echo "$PATH" | tr ':' '\n' | grep -qxE '\.|' && P BASSA "PATH contiene '.' o una voce vuota (= directory corrente)"
echo "== File orfani =="
find / -xdev \( -nouser -o -nogroup \) 2>/dev/null | head | while read f; do P BASSA "senza proprietario: $f"; done
```
Ogni riga di output va letta con la sezione corrispondente del §14: una gravità ALTA (UID 0 multiplo, `/etc/shadow` esposto, setuid inatteso, capability su interprete) è un problema da correggere subito; MEDIA e BASSA sono da valutare. Lo script **non modifica niente**, come richiesto. La correzione, per ogni voce, è nelle rispettive sezioni (§14.1–14.6).

**15.** La mini-CTF "I permessi raccontano". Soluzione completa, pezzo per pezzo. Prima prepara (da utente normale):
```
$ bash setup_sfida.sh && cd ~/l6_sfida && cat LEGGIMI.txt
```

**Pezzo 1 — `chiuso.txt` (§6.2, §6.6).** Il file è `000`, non lo leggi. Ma `ls -l` mostra che ne sei il **proprietario**, e il proprietario può sempre cambiare i permessi di un proprio file, anche con permessi `000` (cambiare i permessi richiede di essere proprietario, non di avere `r`/`w`):
```
$ ls -l chiuso.txt           # ---------- tu tu
$ chmod u+r chiuso.txt
$ cat chiuso.txt
L6{i_permessi_
```

**Pezzo 2 — `archivio/` (§6.4).** La directory è `444` (`r--`): puoi **leggerla** (elencare i nomi) ma non **attraversarla** (manca `x`), quindi non apri i file dentro. Non serve: il messaggio è uno dei **nomi**.
```
$ ls archivio
inventario  protocollo  raccontano_  registro  verbale
```
Il nome fuori posto — l'unico che non è un sinonimo di "documento" e che finisce con `_` — è il pezzo:
```
raccontano_
```
(Se vuoi i file comunque, basta `chmod u+x archivio`, ma non è necessario per la flag.)

**Pezzo 3 — `firme/` (§9.1).** Trenta file; conta **solo** quelli con il bit **setuid**, in ordine di nome. Il contenuto di ciascuno è una sillaba della flag:
```
$ for f in $(ls firme | sort); do [ -u "firme/$f" ] && cat "firme/$f"; done; echo
chi_puo_
# equivalente, con find:
$ find firme -maxdepth 1 -type f -perm -4000 | sort | xargs cat; echo
```
I file con setgid (`2755`) o sticky (`1755`) sono esche: `-u` (ovvero `-perm -4000`) seleziona il bit giusto.

**Pezzo 4 — `codice/` (§7.2).** I file sono vuoti; il messaggio è nei loro **permessi**, letti in ottale come codici ASCII. `stat -c '%a'` dà il numero (es. `146`), che interpretato in **ottale** è un carattere ASCII:
```
$ for f in $(ls codice | sort); do printf "\\$(stat -c %a "codice/$f")"; done; echo
fare_cosa}
```
(`printf "\NNN"` interpreta `NNN` come ottale: `146`→`f`, `141`→`a`, `162`→`r`, `145`→`e`, `137`→`_`, …)

**La flag completa**, pezzi 1-2-3-4 in ordine:
```
L6{i_permessi_raccontano_chi_puo_fare_cosa}
```

**Pulizia.** Come dice il `LEGGIMI`, alcune directory e file hanno permessi stretti; per poter cancellare tutto, ridatti prima i permessi:
```
$ chmod -R u+rwx ~/l6_sfida
$ rm -rf ~/l6_sfida
```

La sfida riassume la lezione: il proprietario comanda sui propri permessi (1), una directory si legge e si attraversa in modo indipendente (2), i bit speciali si selezionano con `find -perm` (3), e i permessi sono solo numeri che si possono leggere come dati (4).
