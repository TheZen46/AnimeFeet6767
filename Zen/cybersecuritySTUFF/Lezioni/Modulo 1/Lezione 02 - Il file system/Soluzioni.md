# Modulo 1 — Lezione 2: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Gli output sono stati verificati con bash 5.2 e GNU coreutils su Linux (ext4); numeri di inode, date e dimensioni saranno diversi sul tuo sistema. I riferimenti `§` rimandano alle sezioni di `Lezione.md`.

## ★ Base

**1.**
```
$ cd /usr/share/doc
$ ls -l /etc/passwd             # assoluto
$ ls -l ../../../etc/passwd     # relativo: doc → share → usr → / , poi etc/passwd
```
Tre percorsi per la home (con utente `hacker`): `/home/hacker`, `~`, `$HOME`; anche `~hacker`, e da `/usr/share/doc` il relativo `../../../home/hacker`. Le prime tre sono la stessa stringa dopo le espansioni della shell (L1 §8.2–8.3); il kernel vede sempre `/home/hacker`.

**2.**
| Richiesta | Dove |
|---|---|
| (a) configurazione del server SSH | `/etc/ssh/sshd_config` |
| (b) log del server web | `/var/log/apache2/` o `/var/log/nginx/` |
| (c) `stdio.h` | `/usr/include/stdio.h` |
| (d) home di root | `/root` |
| (e) versione del kernel come file | `/proc/version` (anche `/proc/sys/kernel/osrelease`) |
| (f) programma installato a mano | `/usr/local/bin` (o `/opt/nome`) |

Il principio: configurazione in `/etc`, dati che cambiano in `/var`, software del sistema in `/usr`, software locale in `/usr/local` o `/opt`, kernel in `/proc` e `/sys` (§2.1).

**3.**
- `/usr/bin/su`: `-` file regolare; permessi `rwsr-xr-x` (la `s` al posto della `x` del proprietario è il bit **setuid**, Lezione 6: il programma gira con i privilegi del proprietario, root); 1 link; proprietario e gruppo `root`; 55680 byte; modificato il 19 agosto (anno corrente, perché mostra l'ora); nome.
- `/tmp`: `d` directory; `rwxrwxrwt`, scrivibile da tutti, con la `t` finale dello **sticky bit** (§9.5, Lezione 6); **9 link** = 2 + 7 sottodirectory (§7.3); 4096 byte, la dimensione della tabella dei nomi, non del contenuto.
- `/dev/pts/0`: `c` dispositivo a caratteri, il tuo pseudo-terminale (L1 §2.2); il proprietario è `hacker` (chi ha la sessione), il gruppo `tty`; `136, 0` sono numero **maggiore** (driver degli pseudo-terminali) e **minore** (il terminale numero 0) al posto della dimensione (§12.1).

**4.**
```
$ mkdir -p progetto/{src,doc,test}       # graffe (L1 §8.1) + -p (§6.1)
$ touch progetto/src/main.c
$ rmdir progetto
rmdir: failed to remove 'progetto': Directory not empty
$ cp -r progetto copia1
$ cp -a progetto copia2
$ ls -l --full-time progetto/src/main.c copia1/src/main.c copia2/src/main.c
```
`rmdir` elimina solo directory vuote (§6.4). `copia1/src/main.c` ha come data l'istante della copia; `copia2/src/main.c` conserva la data dell'originale, perché `-a` preserva i metadati (§6.2).

**5.**
```
$ file vacanze.jpg leggimi.txt script.sh
vacanze.jpg: PDF document, version 1.4
leggimi.txt: ELF 64-bit LSB                (l'intestazione è incompleta: file non può dire di più)
script.sh:   gzip compressed data, from Unix
$ od -A x -t x1z -N 8 vacanze.jpg
000000 25 50 44 46 2d 31 2e 34                          >%PDF-1.4<
```
I primi byte corrispondono alle firme della tabella del §11: `25 50 44 46 2d` (`%PDF-`), `7f 45 4c 46` (`\x7fELF`), `1f 8b` (gzip). L'estensione non ha alcun ruolo. Per `leggimi.txt` il messaggio esatto varia con la versione di `file`, perché abbiamo scritto solo i primi 7 byte di un'intestazione ELF che ne richiederebbe 64: `file` riconosce la firma ma non può interpretare il resto.

## ★★ Intermedio

**6.**
(a) Anche `f` ha permessi `600`: i permessi sono nell'inode, e `f` e `g` sono lo stesso inode (§7.1, §8.1).
(b) `/dev/shm` è un altro file system (tmpfs), e un hard link non può attraversare file system: `ln: failed to create hard link '/dev/shm/g' => 'f': Invalid cross-device link`, errore `EXDEV` (§8.2).
(c) `ln: progetto: hard link not allowed for directory`: gli hard link alle directory creerebbero cicli e renderebbero ambiguo `..` (§8.2).

**7.**
```
$ ln -s "$PWD/a.txt" abs.txt      # $PWD rende il percorso assoluto
$ mv abs.txt d/; cat d/abs.txt    # funziona: il percorso assoluto non dipende dalla posizione del link
ciao
$ cd ~; mv ~/l2 ~/l2_spostata
$ cat ~/l2_spostata/d/s.txt       # il link relativo (../a.txt) funziona ancora
ciao
$ cat ~/l2_spostata/d/abs.txt     # quello assoluto punta ancora a ~/l2/a.txt, che non esiste più
cat: /home/hacker/l2_spostata/d/abs.txt: No such file or directory
```
È esattamente il compromesso descritto nella trascrizione e nel §9.3: i relativi sopravvivono allo spostamento dell'**intero** albero e si rompono se si sposta il solo link; gli assoluti il contrario.

**8.**
(a) `cat scorciatoia/../a.txt` → **errore** `No such file or directory`. È il kernel a risolvere il percorso: `scorciatoia` diventa `d/sub1`, `..` sale fisicamente a `d`, e `d/a.txt` non esiste (§4.2).
(b) `cd scorciatoia && cat ../a.txt` → **errore**, per lo stesso motivo: `cat` passa `../a.txt` al kernel, che parte dalla directory corrente fisica `d/sub1`.
(c) `cd scorciatoia && cd .. && cat a.txt` → `ciao`. `cd ..` è logico: la shell torna a `w1` (§4.3).
La regola da ricordare: `..` dentro un percorso passato a un programma è sempre fisico; solo `cd` (e `pwd`) ragionano in modo logico.

**9.** `nuova` con tre sottodirectory ha **5** link: 2 + 3 (§7.3). Creare un **file** non cambia il numero, perché un file non contiene una voce `..`. Una quarta sottodirectory lo porta a 6.

**10.**
```
$ touch prova; touch -d '2001-09-09' prova; chmod 600 prova
$ stat -c 'mtime=%y | ctime=%z' prova
mtime=2001-09-09 00:00:00.000000000 +0000 | ctime=2026-11-07 17:38:02.856465985 +0000
```
mtime dice 2001, ctime dice oggi. Poiché ogni modifica del contenuto aggiorna **anche** ctime, un file modificato davvero l'ultima volta nel 2001 e mai più toccato avrebbe anche ctime nel 2001. Un ctime molto più recente di mtime indica che i metadati sono stati cambiati dopo: con `touch -d` (*timestomping*), con un `chmod`, un `chown`, una rinomina. ctime non si può impostare con le normali chiamate di sistema (§10), quindi è più affidabile di mtime. In una timeline forense, il disaccordo tra le due date è un indizio da indagare, non una prova da sola.

**11.**
```
$ find /etc -maxdepth 1 -type f -name '*.conf'          # (a)
$ find ~ -type f -mmin -30                              # (b)
$ find /usr/bin -type f -size +1M                       # (c)
$ find /tmp -type f -empty 2>/dev/null                  # (d)
$ find /usr/bin -type l | wc -l                         # (e)
$ find /etc -type f -size -100c 2>/dev/null             # (f)
```
In (a) le virgolette su `'*.conf'` sono indispensabili: senza, se nella directory corrente ci fosse un file `x.conf`, la shell espanderebbe il modello prima di `find` (L1 §8.7), e `find` riceverebbe `-name x.conf`. In (f), `-size -1k` troverebbe solo i file vuoti, perché `find` arrotonda per eccesso: 5 byte contano come 1 KiB, e 1 non è minore di 1 (§14.2). Con l'unità `c` (byte) non c'è arrotondamento.

**12.**
```
$ touch ' ' -- --help $'a\nb'      # oppure: touch ' ' ./--help $'a\nb'
$ ls -b
\ \   --help  a\nb
$ ls -Q
" "  "--help"  "a\nb"
$ rm ' '
$ rm -- --help                     # oppure rm ./--help
$ rm $'a\nb'                       # oppure rm a?b : il ? del glob corrisponde anche all'a capo
```
Attenzione al primo `touch`: `touch --help` stamperebbe l'aiuto invece di creare il file. Con `--` messo prima, tutto ciò che segue è un nome. L'alternativa `rm a?b` è istruttiva: il globbing confronta i nomi byte per byte, e `?` corrisponde a un carattere qualsiasi, a capo compreso (§13). Il completamento con Tab funziona anche qui e inserisce lui le protezioni.

## ★★★ Sfida

**13.**
```
$ echo "dato prezioso" > orig.txt; ls -i orig.txt
680100 orig.txt
$ bash -c 'exec 3<orig.txt; sleep 600' &
[1] 5151
$ rm orig.txt
$ ls -l /proc/5151/fd/3
lr-x------ 1 hacker hacker 64 ... /proc/5151/fd/3 -> /home/hacker/l2/orig.txt (deleted)
$ cp /proc/5151/fd/3 recuperato.txt; cat recuperato.txt
dato prezioso
$ ls -i recuperato.txt
680107 recuperato.txt
$ kill %1
```
Nota: il PID da usare è quello di `bash -c`, mostrato da `[1] 5151` (o da `$!`, L1 §9.2). `cp` crea un **nuovo** inode e vi copia i byte (§6.2): l'inode originale 680100 resta in uso solo finché il processo lo tiene aperto, e viene liberato da `kill %1`, quando l'ultimo riferimento sparisce (§8.3). Non è possibile "ridare un nome" all'inode originale con `ln` dalla riga di comando su ext4: si può solo copiarne il contenuto.

**14.** Flag: `L2{tutto_e_un_file_anche_quando_non_c_e}`

```
$ cd ~/l2_sfida; cat LEGGIMI.txt; ls -la
```
1. **Il labirinto.** Le 41 note hanno lo stesso nome; una sola ha una data di anni fa (impostata con `touch -d`, §10).
   ```
   $ find labirinto -name nota.txt -mtime +365
   labirinto/1/0/41/nota.txt          (il percorso esatto è casuale)
   $ cat "$(find labirinto -name nota.txt -mtime +365)"
   L2{tutto_
   ```
   In alternativa `ls -lt --full-time $(find labirinto -name nota.txt) | tail -1`, o `find labirinto -name nota.txt -not -newermt 2020-01-01`. La sostituzione di comando è tra virgolette per sicurezza (L1 §7).
2. **La foto.**
   ```
   $ file foto.png
   foto.png: gzip compressed data, from Unix, original size modulo 2^32 10
   $ zcat < foto.png
   e_un_file_
   ```
   (§11, Esempio 5.)
3. **La porta.**
   ```
   $ cat ingresso/porta
   cat: ingresso/porta: No such file or directory
   $ ls -l ingresso/porta
   lrwxrwxrwx 1 hacker hacker 15 ... ingresso/porta -> archivio/p3.txt
   ```
   Il link è relativo e si interpreta dalla directory del link, `ingresso/`: punta a `ingresso/archivio/p3.txt`, che non esiste (§9.3). Il file che l'autore intendeva è `archivio/p3.txt`, accanto a `ingresso`:
   ```
   $ cat archivio/p3.txt
   anche_quando_
   ```
   (Riparazione corretta: `ln -sfr archivio/p3.txt ingresso/porta`, oppure a mano `ln -sf ../archivio/p3.txt ingresso/porta`.)
4. **Il guardiano.** Il file `.ultimo_pezzo` è stato cancellato da un processo che lo tiene aperto (§8.3, Esempio 6):
   ```
   $ find /proc/[0-9]*/fd -lname '*ultimo_pezzo*' 2>/dev/null
   /proc/862/fd/3
   $ cat /proc/862/fd/3
   non_c_e}
   $ tr '\0' ' ' < /proc/862/cmdline; echo
   guardiano 7200
   ```
   Il processo si chiama `guardiano` solo perché il suo `argv[0]` è stato impostato con `exec -a` (L1 §6.1); è in realtà `sleep 7200`, come mostra `readlink /proc/862/exe`. Se il processo è già terminato (dopo due ore, o dopo un riavvio) il pezzo è perso: rinomina o elimina `~/l2_sfida` e riesegui lo script.

Il titolo della flag riassume la lezione: in Linux tutto è un file (§1.2), anche un file che non c'è più in nessuna directory.

**15.**
```
1:  a.txt
2:  a.txt b.TXT
3:  1x 2y
4:  *.pdf
5:  a.txt b.TXT
6:  .nascosto.txt a.txt b.TXT
7:  .nascosto.txt a.txt b.TXT d/e.txt
8:  1x 2y b.TXT d
9:  1x 2y
```
Spiegazioni: (1) `*` non corrisponde a `.nascosto.txt` (nascosto) né a `b.TXT` (maiuscole). (2) le classi `[tT]` accettano entrambe le forme. (3) classe POSIX delle cifre. (4) nessuna corrispondenza: il modello resta letterale (L1 §8.7). (5) `nocaseglob` ignora le maiuscole. (6) `dotglob` aggiunge i nascosti. (7) `globstar` fa scendere `**` nelle sottodirectory, con le opzioni 5 e 6 ancora attive. (8) disattivate le due opzioni, `!(*.txt)` è "tutto ciò che non finisce in `.txt`" sensibile alle maiuscole, quindi `b.TXT` è incluso; i nascosti no. (9) `+([0-9])` è una o più cifre, poi una lettera minuscola. Perché uno script: `!(...)` richiede `extglob` già attivo quando la riga viene **analizzata**, e in uno script la riga 8 viene letta dopo l'esecuzione di `shopt -s extglob` (§13).

**16.** Risposta modello.
(a) L'utente crea in anticipo `/tmp/report.txt` come link simbolico a un file che non potrebbe modificare, per esempio un file di configurazione di sistema. Di notte il programma, che gira come root, apre `/tmp/report.txt` in scrittura: il kernel segue il link e il rapporto sovrascrive il file bersaglio con i privilegi di root. Il difetto è *Link Following*, **CWE-59**; l'uso di un nome prevedibile in una directory condivisa è anche *Insecure Temporary File*, **CWE-377**. Se il programma controllasse prima che il percorso non sia un link e lo aprisse dopo, resterebbe vulnerabile a una **TOCTOU** (**CWE-367**).
(b) `/tmp` ha lo sticky bit (`drwxrwxrwt`). Con `fs.protected_symlinks=1` il kernel, in una directory scrivibile da tutti con lo sticky bit, segue un link simbolico solo se chi lo segue ne è il proprietario, o se il proprietario del link coincide con quello della directory. Il link appartiene all'utente attaccante, la directory a root, e chi lo segue è root: il kernel rifiuta (`EACCES`) e l'attacco fallisce.
(c) La variante con hard link crea `/tmp/report.txt` come secondo nome dell'inode bersaglio (stesso file system). `fs.protected_hardlinks=1` vieta di creare un hard link a un file di cui non sei proprietario e che non puoi leggere e scrivere: l'attaccante non riesce nemmeno a preparare la trappola.
(d) Correzioni nel programma: usare `mkstemp`/`mktemp`, che crea un file con nome casuale e lo apre in modo esclusivo (`O_CREAT|O_EXCL`, fallisce se il nome esiste già, link compresi); aprire con `O_NOFOLLOW` per rifiutare un link nell'ultima componente; meglio ancora, scrivere il rapporto in una directory non scrivibile da altri utenti (per esempio `/var/lib/nomeprogramma/`, di proprietà di root con permessi 700).

**17.** Risposta modello.
(a) Nella stessa partizione, `mv` usa `rename()`: toglie la voce (nome → inode) da una directory e la aggiunge a un'altra. I 10 GiB di dati non vengono toccati (§6.3). Verso la chiavetta, che è un altro file system con i propri inode, `rename()` fallisce con `EXDEV`, e `mv` deve leggere e riscrivere tutti i 10 GiB, poi eliminare l'originale.
(b) `rename()` è atomica: un altro programma vede il vecchio nome o il nuovo, mai uno stato intermedio. La copia tra file system crea il nuovo file e lo riempie poco alla volta: chi lo apre durante la copia legge un file incompleto.
(c) Il VFS uniforma le operazioni, ma non può inventare informazioni che il formato del disco non registra. FAT non ha permessi Unix, né proprietario per file, né hard link: il driver mostra permessi e proprietario fissi, decisi dalle opzioni di montaggio (`uid=`, `umask=`), e quelli originali sono andati perduti nella copia (§1.3).

## Domande di autoverifica: punti chiave attesi

1. È il software, con il formato su disco, che trasforma blocchi in file e directory. Il VFS è l'interfaccia comune del kernel a tutti i file system; il montaggio attacca un file system a una directory dell'albero unico che parte da `/` (§1).
2. Nessun `/` (separa le componenti) e nessun byte zero (termina le stringhe in C) (§3).
3. Tipo, permessi, UID e GID, dimensione, numero di link, date, puntatori ai blocchi. Non contiene il nome, che sta nella directory (§7.1).
4. L'hard link è un altro nome dello stesso inode; il simbolico è un file che contiene un percorso. Il simbolico attraversa file system, può puntare a directory e a cose inesistenti, si rompe se il bersaglio sparisce; l'hard link no (§9.2).
5. Rispetto alla directory che **contiene** il link (§9.3).
6. Quando il numero di link è 0 e nessun processo lo tiene aperto. Si recupera da `/proc/<PID>/fd/<n>` (§8.3).
7. mtime: contenuto; ctime: inode (metadati e contenuto); atime: lettura. ctime non si imposta con `touch` e rivela manipolazioni successive (§10).
8. Nello stesso file system usa `rename()` e sposta solo il nome; tra file system diversi copia e cancella (§6.3).
9. Dai primi byte del contenuto, le firme del formato; `file` le confronta con un database, `od` le mostra (§11).
10. `/dev/null` scarta tutto ciò che vi si scrive e in lettura è vuoto; `/proc/self` è la directory del processo che lo legge. Utili: `cmdline`, `environ`, `fd/`, `cwd`, `exe`, `maps`, `status` (§12).
11. Perché un percorso può contenere spazi e a capo ma mai il byte zero: separare con lo zero, o non passare affatto da una riga di testo, è l'unico modo corretto per ogni nome (§14.4).
12. Un programma privilegiato scrive in un nome prevedibile in `/tmp`, dove un altro utente ha messo un link; lo impediscono `protected_symlinks` con lo sticky bit, `protected_hardlinks`, e nel programma `mkstemp`, `O_EXCL`, `O_NOFOLLOW` (§9.5).
