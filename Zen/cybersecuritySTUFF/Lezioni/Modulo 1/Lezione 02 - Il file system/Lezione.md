# Modulo 1 — Lezione 2: Il file system

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 2 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 14).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. spiegare che cos'è un file system, come Linux ne combina molti in un unico albero (montaggio) e che ruolo ha il VFS del kernel;
2. orientarti nella gerarchia standard delle directory (FHS) e sapere dove cercare programmi, configurazioni, dati degli utenti, log, file temporanei;
3. scrivere e risolvere a mente percorsi assoluti e relativi, compresi `.`, `..`, link e casi limite;
4. leggere ogni colonna dell'output di `ls -l` e di `stat`;
5. descrivere che cos'è un inode, che cosa contiene e che cosa **non** contiene;
6. creare e distinguere hard link e link simbolici, prevederne il comportamento quando si sposta o si cancella qualcosa, e spiegare i rischi di sicurezza dei link;
7. riconoscere il vero tipo di un file dai suoi primi byte, indipendentemente dall'estensione;
8. usare i file speciali di `/dev` e le informazioni di `/proc`, compreso il recupero di un file cancellato ma ancora aperto;
9. cercare file con globbing avanzato e con `find`, in modo sicuro anche con nomi ostili.

**Prerequisiti:** Lezione 1 (shell, `argv`, virgolette, espansioni, codice di uscita, `man`).

**Tempo:** circa 4 ore di lettura e prove al terminale, 3–4 ore di esercizi.

**Ripasso dalla Lezione 1.** Tre fatti che useremo continuamente.
- Il programma riceve `argv` già espanso: il **globbing** è fatto dalla shell, che confronta i modelli con i nomi del file system (L1 §8.7).
- Un nome di file che inizia con `-` può essere scambiato per un'opzione: si protegge con `--` o `./` (L1 §6.2).
- La directory corrente è una proprietà del **processo**, per questo `cd` è un builtin (L1 §10.1).

**Convenzione tipografica.** Come nella Lezione 1: `$ ` indica un comando da digitare, le righe senza prefisso sono output. Numeri di inode, date e dimensioni negli esempi saranno diversi sul tuo sistema.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. Il modello | 1–3 | Che cos'è un file system e com'è organizzato l'albero di Linux? |
| II. Percorsi e operazioni | 4–6 | Come si indica un file, come si elenca, si crea, si sposta, si elimina? |
| III. Sotto il cofano | 7–11 | Inode, hard link, link simbolici, date, tipi di file |
| IV. File speciali e ricerca | 12–15 | `/dev`, `/proc`, globbing avanzato, `find`, spazio su disco |
| V. La pratica | 16–21 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — Il modello

## 1. Che cos'è un file system

### 1.1 Due astrazioni: file e directory

Un disco, visto dal basso, è solo una lunga sequenza di **blocchi** numerati, tipicamente da 4096 byte. Nessuno vuole ricordare che la propria tesi occupa i blocchi 81.920–82.047. Il **file system** è lo strato di software, e il formato dei dati sul disco, che costruisce sopra i blocchi due astrazioni (OSTEP, cap. 39, *Files and Directories*):

- il **file**: una sequenza lineare di byte, che si può leggere e scrivere. Per il kernel un file non ha "tipo" né struttura interna: un'immagine, un programma, un testo sono tutti byte. La struttura la dà il programma che li legge;
- la **directory**: un file speciale che contiene un elenco di coppie **(nome, numero di inode)**. È ciò che collega i nomi leggibili dagli umani agli oggetti veri e propri, gli **inode** (§7).

Le directory possono contenere altre directory, e così nasce l'albero. Come dice il docente nella trascrizione pwn.college *Linux Luminarium 2 — The File System*: scatole dentro scatole dentro scatole, con un file alla fine.

### 1.2 "Tutto è un file"

Uno dei principi fondanti di Unix è che quasi ogni risorsa si presenta come un file: i dischi (`/dev/sda`), i terminali (`/dev/pts/0`, che hai visto con `tty` nella Lezione 1), una sorgente di numeri casuali (`/dev/urandom`), le informazioni sui processi (`/proc`), perfino le connessioni di rete, che si usano con le stesse chiamate `read` e `write`. Il vantaggio è enorme: gli stessi strumenti (`cat`, `grep`, le redirezioni) funzionano su tutto. In una sfida CTF, quando non sai come leggere una cosa, chiediti dove si trova come file.

### 1.3 Molti file system, un solo albero: il VFS

Esistono molti formati di file system, ognuno con i suoi compromessi:

| Tipo | Dove lo trovi | Note |
|---|---|---|
| `ext4` | la maggior parte delle installazioni Linux | erede di ext2/ext3, con *journaling* |
| `xfs`, `btrfs` | server, Fedora, openSUSE | btrfs ha snapshot e checksum |
| `vfat`, `exfat` | chiavette USB, partizione di avvio UEFI | niente permessi Unix, nomi non sensibili alle maiuscole |
| `ntfs` | Windows | leggibile da Linux |
| `iso9660` | CD e immagini ISO | sola lettura |
| `tmpfs` | `/dev/shm`, spesso `/tmp` e `/run` | vive in **RAM**: sparisce al riavvio |
| `proc`, `sysfs` | `/proc`, `/sys` | **virtuali**: nessun dato su disco, il kernel genera il contenuto quando lo leggi |
| `overlay` | container Docker | sovrappone più strati di directory |

Il kernel Linux nasconde queste differenze dietro il **VFS** (*Virtual File System*): un'interfaccia comune (aprire, leggere, scrivere, elencare) che ogni file system implementa a modo suo. Per questo `cat` funziona allo stesso modo su un file ext4, su una chiavetta FAT e su `/proc/cpuinfo`, che non esiste su nessun disco.

### 1.4 Il montaggio

Windows assegna a ogni disco una lettera (`C:`, `D:`). Unix, e quindi Linux, ha invece **un unico albero** con una sola radice, `/`. Gli altri file system vengono **montati** (*mount*) su una directory dell'albero, il *punto di montaggio*: da quel momento il contenuto della directory è il contenuto di quel file system. È ciò che ricorda la trascrizione: le altre unità "vengono attaccate" in punti dell'albero, come `/media/...`.

```
$ findmnt -n -o TARGET,SOURCE,FSTYPE /
/      /dev/vda1   ext4
$ df -h /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda1        50G  8.5G   39G  18% /
$ mount | grep -E ' /proc | /tmp '
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
```

`findmnt` mostra l'albero dei montaggi in modo leggibile; `df` lo spazio di ogni file system; `mount` senza argomenti li elenca con le opzioni. Alcune opzioni di montaggio sono **difese di sicurezza** che incontreremo nel Modulo 4: `nosuid` (ignora i bit setuid, Lezione 6), `noexec` (vieta l'esecuzione di programmi da quel file system), `nodev` (ignora i file di dispositivo), `ro` (sola lettura).

In WSL2 il disco di Windows è montato in `/mnt/c`: `C:\Users\Zen` diventa `/mnt/c/Users/Zen`.

## 2. La gerarchia standard: FHS

### 2.1 Le directory principali

La posizione delle directory non è casuale: la stabilisce il **Filesystem Hierarchy Standard** (FHS 3.0, Linux Foundation), seguito con piccole varianti da tutte le distribuzioni. Conoscerlo significa sapere **dove guardare**, che è metà del lavoro in una sfida su una macchina sconosciuta.

| Directory | Contenuto | Interesse in gara |
|---|---|---|
| `/` | radice; su pwn.college contiene anche `/flag` e `/challenge` | primo posto dove cercare |
| `/bin`, `/sbin` | comandi essenziali (`sbin`: amministrazione). Oggi spesso link a `/usr/bin` e `/usr/sbin` | |
| `/usr` | la gran parte del software installato: `/usr/bin`, `/usr/lib`, `/usr/share`, `/usr/include` (header C), `/usr/local` (software installato a mano) | versioni dei programmi, sorgenti degli header |
| `/etc` | **configurazione** di sistema, file di testo: `passwd`, `group`, `shadow`, `hosts`, `ssh/`, `crontab` | utenti, servizi, password (Lezione 6) |
| `/home` | directory personali degli utenti, `/home/nome` | file degli utenti, `.bash_history`, chiavi `.ssh/` |
| `/root` | home dell'utente root | di solito non leggibile |
| `/var` | dati **variabili**: `/var/log` (log), `/var/www` (siti web), `/var/spool` (code), `/var/lib` (dati dei servizi), `/var/tmp` | log, sorgenti di applicazioni web |
| `/tmp` | file temporanei, scrivibile da tutti, spesso svuotata al riavvio | file lasciati da altri utenti o da un servizio |
| `/dev` | file di dispositivo (§12) | |
| `/proc`, `/sys` | file system virtuali del kernel: processi e parametri (§12) | ambiente e argomenti di altri processi |
| `/run` | dati di esecuzione dall'avvio (PID, socket), in RAM | |
| `/boot` | kernel e bootloader | |
| `/lib`, `/lib64` | librerie condivise (anche queste spesso link a `/usr/lib`) | versione di libc (Modulo 4) |
| `/opt` | pacchetti software esterni, autosufficienti | applicazioni delle sfide |
| `/srv` | dati serviti da un server | |
| `/mnt`, `/media` | punti di montaggio temporanei e per supporti rimovibili | dischi aggiuntivi |

Prova `man 7 hier`: è la descrizione ufficiale della gerarchia, installata su ogni sistema.

### 2.2 `usr` non vuol dire "Unix System Resources" (un'altra correzione)

Nella trascrizione il docente spiega `usr` come *Unix system resource*. È un'interpretazione diffusa ma costruita a posteriori (un *backronym*). Storicamente, nei primi Unix dei Bell Labs, `/usr` conteneva davvero le directory degli **utenti** (*user*). Quando il primo disco si riempì, i programmi di sistema furono in parte spostati sul secondo disco, montato in `/usr`, creando le copie `/usr/bin` e `/usr/lib`; le home si spostarono poi in `/home`. La divisione tra `/bin` e `/usr/bin` nasce quindi da un limite di spazio degli anni '70, non da un principio di progetto. Per questo molte distribuzioni moderne (Fedora, Debian 12, Ubuntu, Arch) hanno fatto lo *usrmerge*: `/bin`, `/sbin`, `/lib` sono diventati link simbolici a `/usr/bin`, `/usr/sbin`, `/usr/lib`.

```
$ ls -ld /bin
lrwxrwxrwx 1 root root 7 Apr 22  2024 /bin -> usr/bin
```

Hai appena visto il primo link simbolico della lezione (§9). È anche il motivo per cui nella Lezione 1 `type -a echo` mostrava sia `/usr/bin/echo` sia `/bin/echo`: sono lo stesso file raggiunto da due percorsi.

## 3. Nomi di file: che cosa è permesso

Su un file system Linux nativo, un nome di file (una singola **componente** di percorso) può contenere **qualunque byte tranne due**: la barra `/`, che separa le componenti, e il byte zero `\0`, che termina le stringhe in C. Tutto il resto è lecito: spazi, a capo, tabulazioni, asterischi, virgolette, caratteri di controllo, byte non validi in UTF-8.

Altri vincoli e convenzioni:

- la lunghezza massima di una componente è di solito **255 byte** (`NAME_MAX`), quella di un percorso passato al kernel **4096 byte** (`PATH_MAX`). Byte, non caratteri: una lettera accentata in UTF-8 ne occupa due;
- i nomi sono **sensibili alle maiuscole**: `Flag`, `flag` e `FLAG` sono tre file diversi (non su FAT e NTFS, né, di default, su macOS);
- l'**estensione** (`.txt`, `.png`) è solo una parte del nome: il kernel la ignora del tutto. Il vero tipo di un file si deduce dal contenuto (§11);
- i nomi che iniziano con `.` sono **nascosti** per convenzione: `ls` e il globbing li saltano (L1 §8.7). Non è una protezione, è solo una regola di visualizzazione;
- `.` e `..` sono voci presenti in ogni directory: `.` è la directory stessa, `..` la directory madre. Nella radice `..` punta alla radice stessa.

Nelle sfide *misc* gli autori sfruttano proprio questa libertà: file che si chiamano `-`, ` ` (uno spazio), `...`, `--help`, nomi con un a capo, nomi quasi uguali con lettere di alfabeti diversi. Le difese sono quelle della Lezione 1 (virgolette, `--`, `./`) più due nuove: `ls -b` o `ls -Q` mostrano i caratteri strani in forma visibile, e `find -print0` con `xargs -0` (§14.4) gestisce qualunque nome.

---

# Parte II — Percorsi e operazioni

## 4. Percorsi

### 4.1 Assoluti e relativi

Un **percorso** (*path*) è una sequenza di componenti separate da `/` che identifica un oggetto nell'albero. La trascrizione lo definisce così: un insieme di directory, con un file alla fine, unite da barre.

- Un percorso **assoluto** inizia con `/` e parte dalla radice: `/home/hacker/flag`. Ha lo stesso significato ovunque ti trovi.
- Un percorso **relativo** non inizia con `/` e parte dalla **directory corrente** (*current working directory*, cwd) del processo: se la cwd è `/home/hacker`, il percorso `flag` indica `/home/hacker/flag` e `../zardus/flag` indica `/home/zardus/flag`.
- `./flag` è relativo e **esplicito**: equivale a `flag`, ma contiene una `/`. Nella Lezione 1 hai visto che per questo la shell non cerca in `PATH` (L1 §10.1) e che un nome che inizia con `-` smette di sembrare un'opzione.

Ogni processo ha la propria cwd, ereditata dal padre: `pwd` la mostra, `cd` la cambia. I moduli pwn.college *Pondering Paths* allenano esattamente questo.

### 4.2 Come il kernel risolve un percorso

Quando un programma apre un percorso, il kernel lo **risolve componente per componente** (`man 7 path_resolution`):

1. sceglie il punto di partenza: la radice se il percorso inizia con `/`, altrimenti la cwd del processo;
2. per ogni componente tranne l'ultima, cerca il nome nella directory corrente della risoluzione; deve esistere, essere una directory (o un link simbolico a una directory, che viene seguito), e il processo deve avere su di essa il permesso di **attraversamento** (il bit `x`, Lezione 6);
3. `.` resta nella stessa directory, `..` sale alla directory madre;
4. l'ultima componente viene cercata e, a seconda dell'operazione, aperta, creata o eliminata.

Conseguenze utili:

- barre multiple contano come una: `///tmp//x` è `/tmp/x`;
- una barra finale impone che l'oggetto sia una directory: `ls file.txt/` dà errore *Not a directory*;
- `..` è risolto **fisicamente** dal kernel, sulla directory reale, anche se ci sei arrivato attraverso un link simbolico. La shell invece, per comodità, tiene traccia del percorso **logico** (§4.3). Questa differenza produce alcune delle sorprese più frequenti con i link (Esempio 4).

### 4.3 `cd` e `pwd` in dettaglio

| Comando | Effetto |
|---|---|
| `cd` (senza argomenti) | va alla home, cioè a `$HOME` |
| `cd ~utente` | va alla home di `utente` (espansione tilde, L1 §8.2) |
| `cd -` | torna alla directory precedente (`$OLDPWD`) e la stampa |
| `cd ..` | sale di un livello, **logicamente**: toglie l'ultima componente dal percorso che la shell ricorda |
| `cd -P dir` | segue i link e usa il percorso fisico |
| `pwd` / `pwd -P` | percorso logico (con i link come li hai attraversati) / percorso fisico (link risolti) |
| `pushd dir`, `popd`, `dirs` | pila di directory: entri in `dir` ricordando da dove venivi |

```
$ ln -s d/sub1 scorciatoia
$ cd scorciatoia
$ pwd
/home/hacker/w1/scorciatoia
$ pwd -P
/home/hacker/w1/d/sub1
$ ls ..            # il kernel risolve .. fisicamente: siamo in d/sub1, quindi .. è d
s.txt  sub1  sub2
$ cd ..            # la shell risolve .. logicamente: toglie "scorciatoia"
$ pwd
/home/hacker/w1
```

Stessa scritta `..`, due risultati diversi, perché in un caso la interpreta la shell (`cd`) e nell'altro il kernel (`ls ..` passa a `ls` la stringa `..`, che il kernel risolve). Il percorso logico è una comodità della shell, non una proprietà del file system.

## 5. Elencare: `ls` in profondità

### 5.1 Le opzioni essenziali

| Opzione | Effetto |
|---|---|
| `-l` | formato lungo (§5.2) |
| `-a` / `-A` | include i file nascosti; `-A` esclude `.` e `..` |
| `-h` | dimensioni leggibili (K, M, G) con `-l` |
| `-i` | mostra il numero di inode (§7) |
| `-d` | mostra la directory stessa invece del suo contenuto (`ls -ld /tmp`) |
| `-R` | ricorsivo |
| `-t` / `-S` / `-r` | ordina per data di modifica / per dimensione / inverte l'ordine |
| `-F` | aggiunge un indicatore di tipo: `/` directory, `@` link, `*` eseguibile, `|` FIFO, `=` socket |
| `-b` / `-Q` | mostra i caratteri non stampabili con escape / mette i nomi tra virgolette |
| `-N` | mostra i nomi così come sono, senza alcuna citazione |
| `--full-time` | data completa, con secondi e nanosecondi |
| `-1` | un nome per riga (è il default quando l'output non è un terminale) |

Combinazioni da memorizzare: `ls -la` (tutto, con dettagli), `ls -lt | head` (i più recenti), `ls -lS` (i più grandi), `ls -ld dir` (permessi della directory stessa).

**Le virgolette che `ls` aggiunge da sé.** Dalla versione 8.25 di GNU coreutils (2016), quando l'output è un terminale `ls` usa lo stile di citazione `shell-escape`: un file chiamato `parte 2 di 3` compare come `'parte 2 di 3'`, un nome con un a capo come `'a'$'\n''b'`. Le virgolette **non** fanno parte del nome: sono scritte in modo che tu possa copiare il nome così com'è in un comando. Quando l'output va in una pipe o in un file (`ls | cat`), lo stile torna `literal` e i nomi escono senza modifiche, a capo compresi. Lo stile si sceglie con `--quoting-style=` (`literal`, `shell`, `shell-escape`, `c`, `escape`) oppure con la variabile d'ambiente `QUOTING_STYLE`. In gara è un aiuto prezioso: un nome che `ls` cita in modo strano contiene quasi certamente un carattere invisibile.

### 5.2 Leggere `ls -l` colonna per colonna

```
$ ls -l
-rw-r--r-- 2 hacker hacker    5 Nov  7 17:32 a.txt
drwxr-xr-x 4 hacker hacker 4096 Nov  7 17:32 d
lrwxrwxrwx 1 hacker hacker    5 Nov  7 17:32 s.txt -> a.txt
```

| Colonna | Esempio | Significato |
|---|---|---|
| 1, primo carattere | `-`, `d`, `l` | **tipo** del file (tabella sotto) |
| 1, nove caratteri | `rw-r--r--` | **permessi** per proprietario, gruppo, altri (Lezione 6) |
| 2 | `2` | **numero di link** (hard link) all'inode (§8) |
| 3 | `hacker` | utente proprietario |
| 4 | `hacker` | gruppo proprietario |
| 5 | `5` | dimensione in byte (per un link simbolico: la lunghezza del percorso a cui punta, qui 5 = `a.txt`) |
| 6–8 | `Nov  7 17:32` | data di ultima **modifica** del contenuto (mtime, §10); per file più vecchi di sei mesi mostra l'anno al posto dell'ora |
| 9 | `a.txt` | nome; per i link, `-> destinazione` |

La riga `total` che `ls -l` stampa in cima a una directory è lo spazio occupato su disco, in blocchi da 1 KiB, dai file elencati.

I **tipi di file**, come mostra la trascrizione pwn.college *Linux Luminarium 3 — Symbolic Links* parlando del primo carattere di `ls -l`:

| Carattere | Tipo | Esempio |
|---|---|---|
| `-` | file regolare | `/etc/passwd` |
| `d` | directory | `/home` |
| `l` | link simbolico | `/bin` |
| `c` | dispositivo a caratteri | `/dev/null`, `/dev/tty` |
| `b` | dispositivo a blocchi | `/dev/sda` |
| `p` | FIFO (*named pipe*) | creato con `mkfifo` |
| `s` | socket Unix | `/run/...sock` |

Sono **sette** tipi, e il kernel li distingue nell'inode (§7). Il "tipo" nel senso di immagine, testo o programma non c'entra: per il kernel sono tutti file regolari.

## 6. Creare, copiare, spostare, eliminare

### 6.1 Creare

| Comando | Effetto |
|---|---|
| `touch f` | crea `f` vuoto se non esiste; se esiste, ne aggiorna le date (§10) |
| `> f` | crea `f` vuoto, o lo **svuota** se esiste (redirezione, Lezione 4) |
| `mkdir dir` | crea una directory; fallisce se la madre non esiste |
| `mkdir -p a/b/c` | crea tutte le directory mancanti; non dà errore se esistono già |
| `mktemp`, `mktemp -d` | crea un file o una directory temporanea con nome casuale e sicuro, e ne stampa il nome |

`mktemp` merita attenzione già ora: creare file temporanei con nomi prevedibili in `/tmp` (come `/tmp/backup.txt`) è un errore di sicurezza classico, perché un altro utente può crearli prima di te, magari come link simbolici (§9.5).

### 6.2 Copiare: `cp`

`cp sorgente destinazione` crea un **nuovo** file, con un nuovo inode, e vi copia i byte.

| Opzione | Effetto |
|---|---|
| `-r` | copia ricorsiva di directory |
| `-a` | modalità archivio: ricorsiva, conserva permessi, proprietario (se puoi), date, link simbolici come link |
| `-p` | conserva permessi, proprietario e date |
| `-i` / `-n` | chiede prima di sovrascrivere / non sovrascrive mai |
| `-L` / `-P` | segue i link simbolici e copia il file puntato / copia il link come link |

Senza `-p` o `-a`, la copia ha come data di modifica l'istante della copia e come proprietario chi la esegue. Se la destinazione esiste ed è un file, viene **sovrascritta senza chiedere**; se è una directory, il file viene copiato dentro.

### 6.3 Spostare e rinominare: `mv`

`mv` ha due comportamenti molto diversi, e capire quale si applica richiede l'idea di inode (§7):

- **all'interno dello stesso file system**, `mv` non tocca i dati: chiama `rename()`, che toglie una voce (nome → inode) da una directory e la aggiunge in un'altra. È istantaneo anche per file enormi, e l'inode resta lo stesso. `rename()` è inoltre **atomica**: chi osserva vede il vecchio nome o il nuovo, mai uno stato intermedio. Gli editor e i programmi seri salvano i file scrivendo una copia temporanea e poi rinominandola sopra l'originale proprio per questo;
- **tra file system diversi**, `rename()` non può funzionare (gli inode appartengono a un file system), e `mv` ripiega su copia più eliminazione: lento, non atomico, e con un **nuovo** inode.

```
$ ls -i a.txt
679973 a.txt
$ mv a.txt a2.txt; ls -i a2.txt         # stesso file system: stesso inode
679973 a2.txt
$ mv a2.txt /dev/shm/; ls -i /dev/shm/a2.txt   # /dev/shm è tmpfs: un altro file system
34 /dev/shm/a2.txt
```

### 6.4 Eliminare: `rm` e `rmdir`

| Comando | Effetto |
|---|---|
| `rm f` | elimina il **nome** `f` (la chiamata di sistema si chiama `unlink`, e il nome è esatto: §8.3) |
| `rm -i f` | chiede conferma |
| `rm -r dir` | elimina ricorsivamente una directory e tutto il contenuto |
| `rm -f` | non chiede mai e non segnala file inesistenti |
| `rmdir dir` | elimina una directory solo se **vuota** |

Su Linux **non c'è un cestino** a riga di comando: `rm` è definitivo dal punto di vista dell'utente. Dal punto di vista del disco, invece, i blocchi vengono solo segnati come liberi e i dati restano finché non vengono riutilizzati: è ciò che permette agli strumenti di *file carving* di recuperarli, come vedremo nel Modulo 7.

**Due regole di prudenza**, valide sempre e a maggior ragione negli script:

1. non scrivere mai `rm -rf $dir/` con una variabile non protetta: se `dir` è vuota il comando diventa `rm -rf /`. GNU `rm` ha una rete di sicurezza, l'opzione `--preserve-root` attiva per default, che rifiuta di operare ricorsivamente proprio su `/`; ma la rete non copre la variante più comune, `rm -rf $dir/*`, che con `dir` vuota diventa `rm -rf /*`: il globbing produce `/bin`, `/etc`, `/home` … e nessuno di questi è `/`. Usa `rm -rf -- "${dir:?}"/`, dove `${dir:?}` interrompe il comando con un errore se la variabile è vuota (L1 §8.3), e in uno script `set -u` (Lezione 4);
2. prima di un `rm` con un modello, esegui lo stesso modello con `ls` o `echo` per vedere che cosa verrà eliminato: `echo rm *.log`.

---

# Parte III — Sotto il cofano

## 7. L'inode

### 7.1 Che cosa contiene

Ogni oggetto del file system (file regolare, directory, link simbolico, dispositivo …) è descritto da una struttura chiamata **inode** (*index node*), identificata da un numero unico **all'interno di quel file system**. Nei file system Unix classici, come ext4, gli inode sono in una tabella creata quando il disco viene formattato. Un inode contiene (OSTEP, cap. 39–40; `man 7 inode`):

| Campo | Significato |
|---|---|
| tipo | uno dei sette tipi del §5.2 |
| permessi | i bit `rwx` per proprietario, gruppo e altri, più setuid, setgid, sticky (Lezione 6) |
| UID, GID | utente e gruppo proprietari, come **numeri** |
| dimensione | in byte |
| numero di link | quanti nomi (voci di directory) puntano a questo inode |
| date | accesso (atime), modifica del contenuto (mtime), modifica dell'inode (ctime), a volte creazione (btime) (§10) |
| puntatori ai dati | dove si trovano sul disco i blocchi del contenuto (in ext4: *extent*, intervalli di blocchi contigui) |
| numero di blocchi | spazio effettivamente allocato, che può essere minore della dimensione (*file sparsi*) |

E soprattutto, che cosa **non** contiene: il **nome**. Il nome sta nella **directory**, che è una tabella di coppie (nome, numero di inode). Un file, inteso come inode con i suoi dati, non sa come si chiama, né in quale directory si trova, né quanti nomi ha, se non per il contatore dei link.

```
   directory /home/hacker            tabella degli inode               blocchi dati
  ┌──────────────┬────────┐        ┌────────┬─────────────────────┐
  │ .            │ 131074 │        │ 679973 │ tipo=file, 0644,    │ ──▶ "ciao\n"
  │ ..           │ 131073 │        │        │ uid=1000, size=5,   │
  │ a.txt        │ 679973 │ ─────▶ │        │ links=2, date ...   │
  │ b.txt        │ 679973 │ ─────▶ │        │                     │
  │ s.txt        │ 679980 │ ─────▶ │ 679980 │ tipo=symlink        │ ──▶ "a.txt"
  └──────────────┴────────┘        └────────┴─────────────────────┘
```

### 7.2 Vederlo: `stat` e `ls -i`

```
$ stat a.txt
  File: a.txt
  Size: 5         	Blocks: 8          IO Block: 4096   regular file
Device: 254,0	Inode: 679973      Links: 2
Access: (0644/-rw-r--r--)  Uid: ( 1000/  hacker)   Gid: ( 1000/  hacker)
Access: 2026-11-07 17:32:02.729363748 +0000
Modify: 2026-11-07 17:32:02.735086988 +0000
Change: 2026-11-07 17:32:02.735086988 +0000
 Birth: 2026-11-07 17:32:02.729363748 +0000
```

Riga per riga: dimensione 5 byte ma **8 blocchi** da 512 byte allocati (4096 byte: il file system assegna lo spazio a blocchi interi); `Device` identifica il file system (numeri maggiore e minore del dispositivo, §12.1); `Inode` e `Links` sono i campi del §7.1; `Access: (0644/...)` sono i permessi in ottale e simbolici; seguono le quattro date.

`stat -c` permette di scegliere i campi, utile negli script: `stat -c '%i %h %s %F' file` stampa inode, numero di link, dimensione, tipo. `ls -i` mostra il numero di inode accanto al nome; `df -i` quanti inode sono liberi (un file system può esaurire gli inode prima dello spazio, se contiene milioni di file piccoli).

### 7.3 Le directory e il loro contatore di link

Anche una directory è un inode, il cui contenuto è la tabella dei nomi. Sui file system Unix classici (ext2/3/4, xfs, tmpfs) il suo numero di link è **2 + numero di sottodirectory**: un link è il suo nome nella directory madre, uno è la voce `.` dentro sé stessa, e ogni sottodirectory aggiunge una voce `..` che punta a lei. Nell'esempio del §5.2, `d` ha 4 link perché contiene due sottodirectory.

La regola non è una legge del kernel ma una convenzione del formato su disco, e ci sono eccezioni: **btrfs** mostra sempre 1 per le directory, e ext4 smette di contare quando una directory supera circa 65.000 sottodirectory (il contatore viene fissato a 1, che significa "non lo so"). Per questo `find`, che usa il conteggio per risparmiare letture su alcune piattaforme, ha l'opzione `-noleaf` per i file system che non lo rispettano. In un esercizio puoi contarci; in un'analisi forense su un file system sconosciuto, verifica.

## 8. Hard link

### 8.1 Un file, più nomi

Un **hard link** è semplicemente un'ulteriore voce di directory che punta a un inode **già esistente**. Si crea con `ln` (senza opzioni):

```
$ echo ciao > a.txt
$ ln a.txt b.txt
$ ls -li a.txt b.txt
679973 -rw-r--r-- 2 hacker hacker 5 Nov  7 17:32 a.txt
679973 -rw-r--r-- 2 hacker hacker 5 Nov  7 17:32 b.txt
```

Stesso numero di inode, contatore dei link a 2. Non esiste un "originale" e una "copia": `a.txt` e `b.txt` sono **due nomi equivalenti dello stesso file**. Come spiega la trascrizione pwn.college, un hard link punta direttamente agli stessi dati del file originale. Modificando il contenuto attraverso un nome, la modifica si vede attraverso l'altro; cambiando i permessi attraverso uno, cambiano anche per l'altro, perché i permessi stanno nell'inode.

### 8.2 Limiti

- **Non si può attraversare un file system**: il numero di inode ha senso solo dentro un file system. `ln` risponde `Invalid cross-device link` (errore `EXDEV`).
- **Non si possono creare hard link a directory** (`hard link not allowed for directory`): renderebbe possibili cicli nell'albero e ambiguo il significato di `..`. Le uniche eccezioni sono le voci `.` e `..`, gestite dal kernel.
- Su molte distribuzioni il kernel impedisce di creare hard link a file **di cui non sei proprietario** e che non potresti leggere e scrivere: è la protezione `fs.protected_hardlinks` (valore 1 in `/proc/sys/fs/protected_hardlinks`), introdotta proprio contro gli attacchi descritti nel §9.5.

Per trovare tutti i nomi di un inode: `find / -xdev -samefile a.txt` oppure `find / -xdev -inum 679973` (`-xdev` resta sullo stesso file system, l'unico dove possono stare).

### 8.3 Che cosa vuol dire davvero "cancellare"

La chiamata di sistema per eliminare un file si chiama **`unlink`**, e il nome descrive esattamente ciò che fa: toglie **un nome** da una directory e decrementa il contatore dei link dell'inode. Il kernel libera davvero l'inode e i suoi blocchi solo quando sono vere entrambe le condizioni:

1. il contatore dei link è arrivato a **0**;
2. **nessun processo** ha ancora il file aperto.

La seconda condizione ha una conseguenza importante. Se un processo ha aperto un file e qualcuno lo cancella, il file sparisce da ogni directory ma **continua a esistere**, e il processo continua a leggerlo e scriverlo, finché non lo chiude. Su Linux il file resta raggiungibile attraverso `/proc/<PID>/fd/<n>` (§12.2):

```
$ echo segreto > canc.txt
$ bash -c 'exec 3<canc.txt; sleep 300' &        # un processo apre il file sul descrittore 3
[1] 4242
$ rm canc.txt
$ ls -l /proc/4242/fd/ | grep canc
lr-x------ 1 hacker hacker 64 Nov  7 17:32 3 -> /home/hacker/canc.txt (deleted)
$ cat /proc/4242/fd/3
segreto
```

È una tecnica nota in forensics e nelle CTF: un file "cancellato" da un servizio ancora in esecuzione, o un log rimosso da un intruso mentre il demone che lo scriveva è attivo, si recupera così. Lo stesso principio spiega perché `df` a volte mostra un disco pieno anche dopo aver cancellato un file enorme: qualcuno lo tiene ancora aperto (`lsof +L1` elenca questi file).

## 9. Link simbolici

### 9.1 Un file che contiene un percorso

Un **link simbolico** (*symlink*, o *soft link*) è un file di tipo speciale (`l`) il cui contenuto è **un percorso**. Quando il kernel, risolvendo un percorso, incontra un link simbolico, sostituisce quella componente con il percorso contenuto nel link e continua la risoluzione. Come dice la trascrizione: "se mi devi usare, usa invece quest'altro file".

```
$ ln -s a.txt s.txt                    # ln -s DESTINAZIONE NOME_DEL_LINK
$ ls -l s.txt
lrwxrwxrwx 1 hacker hacker 5 Nov  7 17:32 s.txt -> a.txt
$ cat s.txt
ciao
$ readlink s.txt
a.txt
```

Ordine degli argomenti: come in `cp`, prima ciò che esiste (o dovrebbe esistere), poi il nome nuovo. La dimensione del link (5) è la lunghezza della stringa `a.txt`. I permessi `rwxrwxrwx` di un link simbolico sono **ignorati** su Linux: contano quelli del file a cui si arriva.

### 9.2 Differenze rispetto agli hard link

| | Hard link | Link simbolico |
|---|---|---|
| che cos'è | un altro nome per lo stesso inode | un file a sé, con il proprio inode, che contiene un percorso |
| attraversa file system | no | sì |
| può puntare a directory | no | sì |
| può puntare a qualcosa che non esiste | no | sì (link **pendente**, *dangling*) |
| se si cancella o rinomina il bersaglio | il file sopravvive attraverso l'altro nome | il link si rompe |
| `ls -l` | indistinguibile dall'originale, salvo il contatore | tipo `l` e freccia `->` |

### 9.3 Relativi e assoluti: la trappola

Un link simbolico può contenere un percorso assoluto o relativo. Il punto cruciale, sottolineato anche nella trascrizione: un percorso relativo dentro un link è interpretato **rispetto alla directory che contiene il link**, non rispetto alla tua directory corrente né a quella in cui il link è stato creato.

```
$ ln -s a.txt s.txt           # punta a "a.txt", cioè al file accanto al link
$ mv s.txt d/                 # ora il link è in d/, e "a.txt" si cerca in d/
$ cat d/s.txt
cat: d/s.txt: No such file or directory
```

Il docente lo mostra spostando un link da una home a `/tmp`: il link relativo, una volta spostato, punta a un file diverso o inesistente. I link assoluti non hanno questo problema, ma si rompono se si sposta l'intero albero (per esempio copiando una home su un altro server), dove invece i relativi sopravvivono. La scelta dipende dal contesto. Per calcolare un link relativo corretto: `ln -sr destinazione nome` lo fa in automatico.

### 9.4 Seguire o non seguire

Quasi tutte le operazioni **seguono** i link (aprire, leggere, `stat`, `cd`), ma non tutte:

| Operazione | Sul link stesso o sul bersaglio? |
|---|---|
| `cat`, `open()`, `stat`, `cd` | bersaglio |
| `ls -l`, `lstat()`, `readlink` | link stesso |
| `rm link` | elimina il **link**, non il bersaglio |
| `rm -r L` con `L` link a una directory | elimina **solo il link**, la directory puntata resta intatta |
| `rm -r L/` (con la barra finale) | la barra costringe a risolvere il link: GNU `rm` **svuota la directory bersaglio**, poi fallisce con `cannot remove 'L/': Not a directory` perché `L` in sé non è una directory. Il messaggio d'errore arriva quando il danno è già fatto |
| `chmod` | bersaglio (sul link non ha senso) |
| `chown -h` | link stesso |
| `cp` / `cp -P` / `cp -L` | dipende dalle opzioni (§6.2) |
| `find` (default) / `find -L` | non segue / segue |

Strumenti: `readlink link` stampa il contenuto; `readlink -f percorso` e `realpath percorso` risolvono **tutti** i link e restituiscono il percorso canonico assoluto. I link possono puntare ad altri link, ma il kernel si ferma dopo **40** passaggi, per evitare cicli infiniti (`ln -s a b; ln -s b a; cat a` dà *Too many levels of symbolic links*, errore `ELOOP`).

### 9.5 Link e sicurezza (teoria)

I link simbolici sono un ingrediente classico di vulnerabilità perché separano il **nome** che un programma controlla dall'**oggetto** su cui alla fine agisce. Lo schema tipico, studiato nella letteratura come *symlink attack* o *link following* (CWE-59):

1. un programma con privilegi (per esempio uno che gira come root) scrive in un percorso prevedibile in una directory scrivibile da tutti, come `/tmp/report.txt`;
2. un utente non privilegiato crea in anticipo `/tmp/report.txt` come link simbolico a un file importante che non potrebbe modificare;
3. il programma, seguendo il link, scrive con i propri privilegi sul file importante.

Una variante sfrutta il tempo tra un controllo e un uso: il programma verifica che il percorso sia un file innocuo e, un attimo dopo, lo apre; nel frattempo il nome è stato sostituito con un link. È la classe **TOCTOU** (*time of check to time of use*, CWE-367), una *race condition* che riprenderemo nel Modulo 4 (pwn.college dedica un modulo intero alle race conditions).

Le difese sono a più livelli: nei programmi, `mktemp` invece di nomi prevedibili e l'opzione `O_NOFOLLOW` o `openat` per non seguire i link; nel kernel, la protezione `fs.protected_symlinks`, che nelle directory con lo **sticky bit** come `/tmp` (lo vedi nella `t` finale di `drwxrwxrwt`, Lezione 6) impedisce di seguire un link che appartiene a un altro utente. Nei moduli pwn.college di questa parte troverai sfide in cui un programma privilegiato di laboratorio legge un file indicato da te: i link sono lo strumento per fargli leggere `/flag`.

## 10. Le date di un file

Un inode registra più date, e confonderle è un errore frequente, anche nelle analisi forensi.

| Data | Nome | Cambia quando | Mostrata da |
|---|---|---|---|
| **mtime** | *modification time* | si modifica il **contenuto** | `ls -l` (default) |
| **ctime** | *change time* (non *creation*!) | si modifica l'**inode**: contenuto, permessi, proprietario, numero di link, rinomina | `ls -lc`, `stat` |
| **atime** | *access time* | si **legge** il contenuto | `ls -lu`, `stat` |
| **btime** | *birth time* | creazione dell'inode (solo su alcuni file system, come ext4) | `stat` (riga *Birth*) |

Dettagli importanti:

- **atime** costa caro (ogni lettura diventerebbe una scrittura), quindi quasi tutti i sistemi montano con `relatime`: atime viene aggiornato solo se è più vecchio di mtime o di ctime, oppure se risale a più di 24 ore prima. Con `noatime` non viene aggiornato mai. Non è affidabile come prova che un file **non** sia stato letto;
- `touch -d '2020-01-01 12:00' f` imposta mtime e atime a piacere: le date di modifica sono **falsificabili** da chi ha i permessi sul file (*timestomping*);
- **ctime invece non si può impostare** con le normali chiamate di sistema: ogni modifica, compreso un `touch`, la porta all'istante corrente. Si può falsificare solo per vie indirette che richiedono root: spostare l'orologio di sistema prima della modifica, oppure scrivere direttamente sulle strutture del disco smontato (`debugfs` su ext4). Un file con mtime nel 2020 e ctime di oggi è stato manipolato oggi:

```
$ touch -d '2020-01-01 12:00' a.txt
$ stat -c 'mtime=%y | ctime=%z' a.txt
mtime=2020-01-01 12:00:00.000000000 +0000 | ctime=2026-11-07 17:32:21.509910981 +0000
```

Le date sono la materia prima delle **timeline** forensi (Modulo 7) e un criterio di ricerca per `find` (§14): "quali file sono stati modificati nell'ultima ora?" è spesso la domanda giusta su una macchina sconosciuta.

## 11. Il vero tipo di un file: contenuto, non estensione

Il kernel non guarda le estensioni (§3), e neanche molti programmi: un file `foto.txt` può essere un'immagine PNG e `documento.jpg` un PDF. Il tipo reale si riconosce dai primi byte, i **numeri magici** (*magic numbers*) definiti dai rispettivi formati:

| Formato | Primi byte (esadecimale) | Come appaiono in testo |
|---|---|---|
| ELF (programmi Linux) | `7f 45 4c 46` | `\x7fELF` |
| PNG | `89 50 4e 47 0d 0a 1a 0a` | `\x89PNG\r\n\x1a\n` |
| JPEG | `ff d8 ff` | |
| GIF | `47 49 46 38` | `GIF8` |
| PDF | `25 50 44 46 2d` | `%PDF-` |
| ZIP (anche .docx, .jar, .apk) | `50 4b 03 04` | `PK\x03\x04` |
| gzip | `1f 8b` | |
| bzip2 / xz | `42 5a 68` / `fd 37 7a 58 5a 00` | `BZh` / `\xfd7zXZ\0` |
| script | `23 21` | `#!` (L1 §10.3) |

Il comando **`file`** fa questo lavoro per te, confrontando l'inizio del file con un database di firme (`man 5 magic`):

```
$ file /bin/ls doc.jpg x.txt
/bin/ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, ...
doc.jpg: PDF document, version 1.4
x.txt:   gzip compressed data, was "a.txt", ...
```

Per vedere i byte con i tuoi occhi: `head -c 16 file | od -A x -t x1z` (o `xxd file | head`, se `xxd` è installato; lo useremo molto nella Lezione 7).

```
$ od -A x -t x1z -N 16 /bin/ls
000000 7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  >.ELF............<
```

Nelle sfide *misc* e *forensics*, "che cos'è davvero questo file?" è sempre la prima domanda, e `file` la prima risposta. Attenzione però: `file` guarda soprattutto l'inizio, e un file può contenere altri file nascosti più avanti (un archivio ZIP accodato a un'immagine, per esempio). Strumenti come `binwalk` cercano firme in tutto il file; li useremo nel Modulo 7.

---

# Parte IV — File speciali e ricerca

## 12. File speciali: `/dev` e `/proc`

### 12.1 `/dev`: i dispositivi

I file in `/dev` non contengono dati: sono **porte d'accesso a driver del kernel**. Il loro inode ha tipo `c` (dispositivo a caratteri, letto e scritto come flusso di byte) o `b` (dispositivo a blocchi, accessibile a blocchi in posizione arbitraria, come un disco), e al posto della dimensione `ls -l` mostra due numeri: il **maggiore**, che identifica il driver, e il **minore**, che identifica il dispositivo specifico.

```
$ ls -l /dev/null /dev/zero /dev/urandom /dev/tty
crw-rw-rw- 1 root root 1, 3 Nov  7 04:04 /dev/null
crw-rw-rw- 1 root root 1, 5 Nov  7 04:04 /dev/zero
crw-rw-rw- 1 root root 1, 9 Nov  7 04:04 /dev/urandom
crw-rw-rw- 1 root root 5, 0 Nov  7 04:04 /dev/tty
```

| Dispositivo | Lettura | Scrittura | Uso tipico |
|---|---|---|---|
| `/dev/null` | fine del file immediata | scarta tutto | buttare via output: `comando 2>/dev/null` |
| `/dev/zero` | byte `00` all'infinito | scarta | creare file di zeri: `head -c 1M /dev/zero > f` |
| `/dev/urandom` | byte casuali crittograficamente sicuri | (aggiunge entropia) | chiavi, nomi casuali: `head -c 16 /dev/urandom | od -A n -t x1` |
| `/dev/tty` | il terminale del processo | il terminale del processo | parlare all'utente anche se l'output è rediretto |
| `/dev/sda`, `/dev/nvme0n1`, `/dev/vda` | il disco intero, byte per byte | **sovrascrive il disco** | immagini forensi (Modulo 7) |
| `/dev/shm` | directory tmpfs in RAM | | file temporanei veloci |
| `/dev/stdin`, `/dev/stdout`, `/dev/stderr` | link a `/proc/self/fd/0`, `1`, `2` | | passare lo standard input a un programma che vuole un nome di file |

Il comando `2>/dev/null`, che userai in quasi ogni ricerca con `find`, sarà spiegato a fondo nella Lezione 4: per ora sappi che scarta i messaggi d'errore.

### 12.2 `/proc`: il kernel visto come file

`/proc` è un file system **virtuale**: i file non esistono su un disco, il kernel ne genera il contenuto al momento della lettura. Per ogni processo in esecuzione c'è una directory `/proc/<PID>`, e `/proc/self` è un link che punta sempre alla directory del processo che lo legge.

| File | Contenuto |
|---|---|
| `/proc/<PID>/cmdline` | l'`argv` del processo, con gli argomenti separati da byte zero |
| `/proc/<PID>/environ` | l'ambiente iniziale del processo, separato da byte zero (L1 §12.3) |
| `/proc/<PID>/cwd` | link alla directory corrente del processo |
| `/proc/<PID>/exe` | link al file eseguibile |
| `/proc/<PID>/fd/` | un link per ogni descrittore di file aperto (§8.3) |
| `/proc/<PID>/status` | nome, stato, PID, PPID, UID, memoria |
| `/proc/<PID>/maps` | mappa della memoria del processo (Modulo 2, fondamentale nel Modulo 4) |
| `/proc/cpuinfo`, `/proc/meminfo` | processore e memoria |
| `/proc/version` | versione del kernel |
| `/proc/sys/...` | parametri del kernel modificabili (per esempio `fs/protected_symlinks`); si gestiscono con `sysctl` |

```
$ readlink /proc/self/exe /proc/self/cwd
/usr/bin/readlink
/home/hacker
$ tr '\0' ' ' < /proc/self/cmdline; echo
tr \0
$ grep -E '^(Name|Pid|PPid|Uid)' /proc/self/status
Name:	grep
Pid:	756
PPid:	733
Uid:	1000	1000	1000	1000
```

Nota che in ogni esempio `self` è il **comando che legge**: `readlink`, `tr`, `grep`. L'argv di `tr` contiene la stringa `\0` letterale, perché è `tr` stesso a interpretarla. Di solito `cmdline` e `environ` degli altri utenti non sono leggibili (dipende dalle opzioni di montaggio di `/proc` e dai permessi), ma quelli dei **tuoi** processi sì: in una sfida, un processo lanciato con la flag tra gli argomenti o nell'ambiente si tradisce qui. Ne riparleremo nella Lezione 5.

`/sys` (sysfs) è il fratello più ordinato di `/proc`: espone dispositivi, driver e parametri del kernel come un albero di piccoli file.

### 12.3 FIFO e socket, in breve

Gli ultimi due tipi del §5.2 servono alla comunicazione tra processi. Una **FIFO**, creata con `mkfifo nome`, è una pipe con un nome nel file system: un processo vi scrive, un altro legge, e i dati passano dall'uno all'altro senza essere mai salvati su disco. Un **socket Unix** è un punto di comunicazione bidirezionale con un nome di file, usato da molti servizi locali (database, Docker, il server grafico). Li useremo nelle Lezioni 4 e 10.

## 13. Globbing avanzato

Nella Lezione 1 (§8.7) hai visto `*`, `?` e `[...]`. Bash offre altre possibilità, attivabili con `shopt` (`help shopt`):

| Funzione | Attivazione | Esempio | Significato |
|---|---|---|---|
| classi di caratteri | sempre | `[[:digit:]]*`, `[[:upper:]]*`, `[[:alnum:]]`, `[[:space:]]` | nomi che iniziano con una cifra / maiuscola …; non dipendono dalla lingua come gli intervalli `[a-z]` |
| file nascosti | `shopt -s dotglob` | `*` | include i nomi che iniziano con `.` (mai `.` e `..`) |
| ricorsione | `shopt -s globstar` | `**/*.txt` | `**` corrisponde a zero o più directory: tutti i `.txt` dell'albero |
| modelli estesi | `shopt -s extglob` | `!(*.txt)`, `+([0-9])`, `@(a|b)`, `?(x)`, `*(x)` | tutto tranne; una o più ripetizioni; una delle alternative; zero o una; zero o più |
| nessuna corrispondenza | `shopt -s nullglob` / `failglob` | | il modello sparisce / errore, invece di restare letterale |
| maiuscole indifferenti | `shopt -s nocaseglob` | | `*.TXT` trova anche `.txt` |

```
$ shopt -s globstar; echo **/*.txt
a.txt b.txt d/s.txt e.txt
$ shopt -s extglob
$ echo !(*.txt)
d doc.jpg loop1 loop2
```

**Una trappola di `extglob`.** L'opzione deve essere attiva **quando la riga viene analizzata**, perché cambia la grammatica: `shopt -s extglob; echo !(*.txt)` scritto su **una sola** riga dà un errore di sintassi, perché bash analizza l'intera riga prima di eseguire `shopt`. Va attivata in una riga precedente (o all'inizio dello script).

Il globbing ha due limiti che lo rendono inadatto a ricerche serie: lavora solo sui **nomi** (non su dimensione, data, proprietario, tipo) e, su alberi grandi, produce elenchi che possono superare la lunghezza massima della riga di comando (`Argument list too long`, errore `E2BIG`). Per tutto il resto c'è `find`.

## 14. Cercare con `find`

### 14.1 La struttura del comando

`find` percorre ricorsivamente uno o più alberi e valuta, per ogni oggetto incontrato, un'**espressione** fatta di test, operatori e azioni (`man 1 find`):

```
find [punti di partenza ...] [espressione]
```

Senza punto di partenza usa `.`; senza azioni stampa il percorso di ciò che soddisfa l'espressione (`-print`).

```
$ find / -name flag 2>/dev/null
/flag
```

È probabilmente il comando che userai di più all'inizio di ogni sfida su una macchina: "dov'è la flag?". `2>/dev/null` nasconde le centinaia di *Permission denied* sulle directory che non puoi leggere.

### 14.2 I test

| Test | Vero se … | Esempio |
|---|---|---|
| `-name modello` / `-iname` | il **nome** (ultima componente) corrisponde al modello glob, con o senza maiuscole. Metti il modello tra virgolette, o lo espanderà la shell! | `-name '*.conf'` |
| `-path modello` | il percorso intero corrisponde | `-path '*/.git/*'` |
| `-type t` | il tipo è `f` file, `d` directory, `l` link, `c`, `b`, `p`, `s` | `-type f` |
| `-size n[ckMG]` | la dimensione è `n` (`+n` più di, `-n` meno di), in byte `c`, KiB `k`, MiB `M`, GiB `G` | `-size +10M` |
| `-mtime n`, `-mmin n` | modificato `n` giorni / minuti fa (`-n` meno di, `+n` più di) | `-mmin -60` |
| `-newer f` | modificato dopo il file `f` | `-newer /etc/passwd` |
| `-user u`, `-group g` | proprietario | `-user root` |
| `-perm modo` | permessi esattamente `modo`; con `-modo` almeno quei bit; con `/modo` almeno uno di quei bit (Lezione 6) | `-perm -4000` |
| `-empty` | file vuoto o directory vuota | |
| `-inum n`, `-samefile f` | ha quell'inode / è lo stesso inode di `f` (§8.2) | |
| `-readable`, `-writable`, `-executable` | il processo corrente ha quel permesso | `-writable` |
| `-maxdepth n`, `-mindepth n` | limita la profondità (vanno messi all'inizio) | `-maxdepth 1` |
| `-xdev` | non entra in altri file system | |

**Trappola di `-size`:** `find` arrotonda **per eccesso** all'unità richiesta. `-size -1k` significa "meno di 1 unità da 1 KiB, arrotondando per eccesso", quindi trova solo i file **vuoti**: un file di 5 byte conta come 1k. Per "meno di 1024 byte" scrivi `-size -1024c`.

### 14.3 Operatori

Più test uno dopo l'altro sono uniti da un **E** implicito. Esistono anche:

| Operatore | Significato |
|---|---|
| `! test` o `-not test` | negazione |
| `test1 -o test2` | O |
| `\( ... \)` | raggruppamento (le parentesi vanno protette dalla shell, L1 §5.1) |

```
$ find . \( -name '*.txt' -o -name '*.jpg' \) -not -name 'b*'
```

L'**E** ha precedenza sull'**O**, come in algebra: `find . -name '*.c' -o -name '*.h' -print` stampa solo i `.h`, perché si legge "`*.c` O (`*.h` E stampa)". Con le parentesi il problema sparisce.

### 14.4 Le azioni e i nomi ostili

| Azione | Effetto |
|---|---|
| `-print` | stampa il percorso, seguito da un a capo (default) |
| `-print0` | stampa il percorso seguito da un byte **zero** |
| `-ls` | stampa in formato simile a `ls -l` |
| `-exec cmd {} \;` | esegue `cmd` una volta **per ogni** risultato, con `{}` sostituito dal percorso |
| `-exec cmd {} +` | esegue `cmd` una volta con **molti** risultati come argomenti (più veloce) |
| `-delete` | elimina; pericolosissimo se messo prima dei test (l'ordine conta!) |

Perché `-print0`? Nella Lezione 1 hai visto che l'unico byte che non può comparire in un argomento, e quindi in un percorso, è lo zero (L1 §6.1). Un a capo invece può comparire in un nome di file. Se passi l'output di `find` a un altro programma con le righe come separatore, un nome con uno spazio o un a capo viene spezzato:

```
$ find . -name '*.txt' | xargs ls        # SBAGLIATO con nomi che contengono spazi
ls: cannot access './con': No such file or directory
ls: cannot access 'spazio.txt': No such file or directory
$ find . -name '*.txt' -print0 | xargs -0 ls     # CORRETTO con qualunque nome
$ find . -name '*.txt' -exec ls {} +             # CORRETTO anche questo, senza xargs
```

(`xargs` trasforma le righe che riceve in argomenti di un comando: lo vedremo nella Lezione 4, insieme alle pipe.) `-exec` non passa mai dalla shell, quindi non ha problemi di divisione in parole: è la scelta più semplice e sicura.

### 14.5 Ricette per le gare

```
$ find / -name '*flag*' 2>/dev/null                    # tutto ciò che ha "flag" nel nome
$ find / -type f -user hacker 2>/dev/null              # i file di un certo utente
$ find / -type f -newer /etc/hostname 2>/dev/null      # file modificati dopo l'installazione
$ find / -mmin -10 -type f -not -path '/proc/*' 2>/dev/null   # modificati negli ultimi 10 minuti
$ find / -writable -type d 2>/dev/null                 # dove posso scrivere?
$ find / -perm -4000 -type f 2>/dev/null               # programmi setuid (Lezione 6)
$ find . -type f -exec grep -l 'pwn.college{' {} +     # file che contengono una flag (grep: Lezione 3)
```

### 14.6 Alternative più veloci

- `locate nome` (pacchetto `mlocate` o `plocate`) cerca in un database aggiornato periodicamente da `updatedb`: istantaneo, ma non vede i file creati dopo l'ultimo aggiornamento, e spesso non è installato nelle sfide.
- `which` e `command -v` cercano solo programmi in `PATH` (L1 §10.1); `whereis` cerca programma, sorgenti e pagina di manuale in posizioni standard.

## 15. Spazio e occupazione

| Comando | Risponde a |
|---|---|
| `df -h` | quanto spazio c'è su ogni file system montato? |
| `df -i` | quanti inode liberi? |
| `du -sh dir` | quanto occupa `dir`, in totale? |
| `du -ah dir | sort -h | tail` | quali sono i file e le directory più grandi? |
| `ls -lS` | i file più grandi di una directory |

`du` misura lo spazio **allocato** (i blocchi del §7.2), `ls -l` la dimensione **logica**. Possono differire molto: un file *sparso*, creato per esempio con `truncate -s 1G f`, ha dimensione 1 GiB ma occupa zero blocchi, perché le parti mai scritte non sono allocate.

---

# Parte V — La pratica

## 16. Esempi svolti

### Esempio 1 — Orientarsi su una macchina sconosciuta

Hai appena ottenuto una shell in una sfida. Una sequenza di ricognizione ragionata, sezione per sezione:

```
$ pwd; id                        # dove sono e chi sono (L1 §4.3)
$ ls -la ~ /                     # home e radice, file nascosti compresi (§5)
$ ls -la /challenge /opt /srv /var/www 2>/dev/null   # posti tipici per i file di una sfida (§2.1)
$ find / -name '*flag*' -not -path '/proc/*' 2>/dev/null   # ricerca per nome (§14)
$ find / -mmin -30 -type f -not -path '/proc/*' -not -path '/sys/*' 2>/dev/null   # file toccati di recente (§10)
$ file /challenge/* 2>/dev/null  # che cosa sono davvero i file trovati (§11)
```

Ogni riga risponde a una domanda precisa. Imparare la domanda è più importante che imparare il comando.

### Esempio 2 — Un hard link sopravvive alla cancellazione

```
$ echo uno > f
$ ln f g
$ echo due >> g              # aggiunge una riga attraverso il secondo nome
$ cat f
uno
due
$ rm f
$ cat g
uno
due
$ stat -c %h g
1
```

`f` e `g` erano lo stesso inode (§8.1): la riga aggiunta attraverso `g` si vede attraverso `f`. Dopo `rm f` il contatore scende a 1 e il file continua a esistere sotto il nome `g` (§8.3).

### Esempio 3 — Il link relativo che si rompe e come ripararlo

```
$ ln -s a.txt s.txt; mv s.txt d/
$ cat d/s.txt
cat: d/s.txt: No such file or directory
$ readlink d/s.txt                 # il contenuto non è cambiato...
a.txt
$ find . -xtype l                  # ...ma ora è un link pendente
./d/s.txt
$ ln -sfr a.txt d/s.txt            # -r: calcola il percorso relativo giusto; -f: sostituisce il link esistente
$ readlink d/s.txt
../a.txt
$ cat d/s.txt
ciao
```

`readlink` mostra che il link contiene ancora `a.txt`: è la sua **posizione** a essere cambiata, e il percorso relativo si interpreta dalla directory del link (§9.3). `find -xtype l` trova i link pendenti (con `-xtype` il test sul tipo guarda il bersaglio: un link il cui bersaglio è ancora "un link" non è risolvibile).

### Esempio 4 — Due `..` diversi

```
$ ln -s d/sub1 scorciatoia
$ cd scorciatoia; pwd; pwd -P
/home/hacker/w1/scorciatoia
/home/hacker/w1/d/sub1
$ ls ..
s.txt  sub1  sub2
$ cd ..; pwd
/home/hacker/w1
```

È l'esempio del §4.3, ripreso perché è la sorgente di confusione più comune: `ls ..` usa il `..` del **kernel**, fisico, che sale da `d/sub1` a `d`; `cd ..` usa il `..` della **shell**, logico, che toglie l'ultima componente dal percorso che la shell ricorda. Se vuoi che `cd` si comporti come il kernel: `cd -P ..`.

### Esempio 5 — Il file che dice di essere un'immagine

```
$ ls -l foto.png
-rw-r--r-- 1 hacker hacker 30 Nov  7 17:37 foto.png
$ file foto.png
foto.png: gzip compressed data, from Unix, original size modulo 2^32 10
$ od -A x -t x1z -N 4 foto.png
000000 1f 8b 08 00                                      >....<
$ zcat < foto.png
e_un_file_
```

L'estensione mente; i primi due byte `1f 8b` sono la firma di gzip (§11). `zcat` (o `gzip -dc`) decomprime sullo standard output. Usare `zcat < foto.png` invece di `zcat foto.png` evita che `gzip` si lamenti dell'estensione sconosciuta: con la redirezione riceve solo i byte, non il nome.

### Esempio 6 — Trovare tutto ciò che un processo tiene aperto e che è stato cancellato

```
$ find /proc/[0-9]*/fd -lname '*(deleted)' 2>/dev/null
/proc/862/fd/3
$ ls -l /proc/862/fd/3
lr-x------ 1 hacker hacker 64 Nov  7 17:37 /proc/862/fd/3 -> /home/hacker/l2_sfida/.ultimo_pezzo (deleted)
$ tr '\0' ' ' < /proc/862/cmdline; echo
guardiano 7200
$ cp /proc/862/fd/3 recuperato.txt
```

Si combinano quattro idee: il globbing `[0-9]*` sceglie solo le directory dei processi in `/proc` (§13); `find -lname` confronta il **contenuto** di un link simbolico con un modello (§14.2); i link in `/proc/<PID>/fd` mostrano `(deleted)` per i file cancellati ma aperti (§8.3); `cmdline` rivela chi è il processo (§12.2). Il nome `guardiano` è un `argv[0]` scelto da chi ha lanciato il processo (L1 §6.1): il programma vero è `sleep`, come confermerebbe `readlink /proc/862/exe`.

## 17. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire `Soluzioni.md`. Lavora in una directory di prova (`mkdir ~/l2 && cd ~/l2`) per non toccare i tuoi file.

### ★ Base

1. Ti trovi in `/usr/share/doc`. Scrivi il percorso **assoluto** e il percorso **relativo** più corto per raggiungere `/etc/passwd`, e verificali entrambi con `ls -l`. Poi scrivi tre percorsi diversi, tutti validi, che indicano la tua home.
2. **FHS.** Senza cercare in rete, indica in quale directory cercheresti: (a) la configurazione del server SSH; (b) i log di un server web; (c) l'header C `stdio.h`; (d) la home di root; (e) la versione del kernel in esecuzione, come file; (f) un programma installato a mano dall'amministratore. Poi verifica con `ls` e `man 7 hier`.
3. **Leggere `ls -l`.** Spiega ogni campo di queste tre righe:
   ```
   -rwsr-xr-x  1 root   root  55680 Aug 19 16:47 /usr/bin/su
   drwxrwxrwt  9 root   root   4096 Nov  7 17:37 /tmp
   crw--w----  1 hacker tty  136, 0 Nov  7 17:40 /dev/pts/0
   ```
   Che cosa ti dice il numero 9 su `/tmp`? Che cosa sono `136, 0`? (Le lettere `s` e `t` le studieremo nella Lezione 6: per ora basta notarle.)
4. Con **un solo** comando crea la struttura `progetto/src`, `progetto/doc`, `progetto/test`. Crea `progetto/src/main.c` con `touch`. Prova `rmdir progetto` e spiega l'errore. Copia `progetto` in `copia1` con `cp -r` e in `copia2` con `cp -a`, poi confronta le date di `main.c` nelle tre posizioni con `ls -l --full-time`.
5. **Tipi veri.** Crea tre file con nomi ingannevoli:
   ```
   $ printf '%%PDF-1.4\n' > vacanze.jpg
   $ printf '\x7fELF\x02\x01\x01' > leggimi.txt
   $ echo ciao | gzip > script.sh
   ```
   Identificali con `file` e mostrane i primi byte con `od -A x -t x1z -N 8`. Confronta con la tabella del §11.

### ★★ Intermedio

6. **Hard link.** Riproduci l'Esempio 2. Poi rispondi: (a) dopo `ln f g`, se esegui `chmod 600 g`, che permessi ha `f`? Perché? (b) Perché `ln f /dev/shm/g` fallisce? Qual è il nome dell'errore? (c) Che cosa succede con `ln progetto progetto2`?
7. **Link simbolici.** Riproduci l'Esempio 3. Poi crea un link **assoluto** allo stesso file, spostalo in `d/` e verifica che funzioni. Infine sposta l'**intera** directory di lavoro altrove (`mv ~/l2 ~/l2_spostata`) e verifica quale dei due link funziona ancora. Spiega.
8. **Previsione.** Nella directory `w1` dell'Esempio 4 (con `scorciatoia -> d/sub1`, e `a.txt` in `w1`), prevedi il risultato di: (a) `cat scorciatoia/../a.txt`; (b) `cd scorciatoia && cat ../a.txt`; (c) `cd scorciatoia && cd .. && cat a.txt`. Poi verifica.
9. **Contatore delle directory.** Crea `nuova` con tre sottodirectory. Prevedi il numero di link di `nuova` e verifica con `stat -c %h`. Che cosa succede al numero se crei un **file** dentro `nuova`? E se crei un'altra sottodirectory?
10. **Date.** Crea un file, imposta la data di modifica al 9 settembre 2001 con `touch -d`, poi cambiane i permessi con `chmod 600`. Mostra mtime e ctime con `stat`. Spiega perché un analista forense considererebbe sospetta questa combinazione.
11. **`find`.** Scrivi un comando `find` per ciascuna richiesta: (a) i file che finiscono in `.conf` direttamente dentro `/etc` (non nelle sottodirectory); (b) i file della tua home modificati negli ultimi 30 minuti; (c) i file più grandi di 1 MiB in `/usr/bin`; (d) i file vuoti in `/tmp`; (e) quanti link simbolici ci sono in `/usr/bin` (suggerimento: `| wc -l`, Lezione 3); (f) i file in `/etc` più piccoli di 100 byte. Per (f), spiega perché `-size -1k` sarebbe sbagliato.
12. **Nomi ostili.** Crea tre file chiamati, rispettivamente, ` ` (uno spazio), `--help` e `a` a capo `b` (suggerimento: `touch $'a\nb'`, L1 §7). Elencali in modo che i nomi siano riconoscibili, poi eliminali tutti e tre in modo sicuro, uno alla volta.

### ★★★ Sfida

13. **Recupero.** Crea un file con un contenuto a tua scelta, aprilo da un processo in background come nel §8.3, cancellalo, e recuperane il contenuto in un nuovo file `recuperato.txt` usando solo `/proc`. Verifica con `ls -i` che `recuperato.txt` ha un inode **diverso** da quello che aveva il file originale, e spiega perché. Ricorda di terminare il processo alla fine (`kill %1`).
14. **Mini-CTF.** Nella cartella di questa lezione c'è `setup_sfida.sh`. Eseguilo con `bash setup_sfida.sh`: crea la directory `~/l2_sfida` e avvia un processo che si chiude da solo dopo due ore. **Non leggerne il contenuto.** Leggi `~/l2_sfida/LEGGIMI.txt` e trova i quattro pezzi della flag `L2{...}`. Ogni pezzo richiede una parte diversa di questa lezione.
15. **Previsione di globbing.** In una directory vuota esegui `mkdir d; touch a.txt b.TXT .nascosto.txt 1x 2y d/e.txt`. Scrivi su carta l'output di ciascuna riga, eseguendole **in quest'ordine** in uno script (perché in uno script? rileggi la trappola di `extglob` nel §13), poi verifica:
    ```bash
    echo "1: " *.txt
    echo "2: " *.[tT][xX][tT]
    echo "3: " [[:digit:]]*
    echo "4: " *.pdf
    shopt -s nocaseglob; echo "5: " *.txt
    shopt -s dotglob;    echo "6: " *.txt
    shopt -s globstar;   echo "7: " **/*.txt
    shopt -u nocaseglob dotglob; shopt -s extglob
    echo "8: " !(*.txt)
    echo "9: " +([0-9])[a-z]
    ```
16. **Teoria (sicurezza).** Un programma di laboratorio, eseguito come root da un servizio pianificato, scrive ogni notte un rapporto in `/tmp/report.txt` aprendolo in scrittura senza particolari opzioni. In 10–15 righe: (a) descrivi come un utente non privilegiato potrebbe sfruttarlo con un link simbolico e quale CWE descrive il difetto; (b) spiega perché, su un sistema con `fs.protected_symlinks=1`, l'attacco fallisce, e quale ruolo ha lo sticky bit di `/tmp`; (c) spiega perché un attacco analogo con un **hard link** è bloccato da `fs.protected_hardlinks`; (d) proponi due correzioni nel programma stesso, che funzionino anche senza le protezioni del kernel.
17. **Teoria (file system).** Spiega, usando i concetti di inode, `rename()` e VFS: (a) perché `mv` di un file da 10 GiB dentro la stessa partizione è istantaneo e verso una chiavetta USB richiede minuti; (b) perché, durante quel secondo `mv`, un altro programma potrebbe vedere un file incompleto, mentre nel primo caso no; (c) perché, dopo averlo spostato sulla chiavetta FAT, il file ha perso i suoi permessi Unix.

### Allenamento su pwn.college

Nel dojo **Linux Luminarium** completa i moduli *Pondering Paths*, *Comprehending Commands* e *File Globbing*. Come nella Lezione 1, annota per ogni sfida il comando risolutivo e la sezione della lezione da cui viene.

## 18. Domande di autoverifica

Rispondi per iscritto in 3–5 righe ciascuna, senza guardare il testo; poi confronta con i punti chiave in `Soluzioni.md`.

1. Che cos'è un file system? Che cosa sono il VFS e il montaggio, e perché Linux non ha lettere di unità?
2. Quali sono le due sole restrizioni sui byte di un nome di file, e perché proprio quelle?
3. Che cosa contiene un inode? Che cosa **non** contiene?
4. Qual è la differenza tra un hard link e un link simbolico? Dai tre differenze pratiche.
5. Rispetto a che cosa si interpreta il percorso relativo contenuto in un link simbolico?
6. Quando il kernel libera davvero lo spazio di un file? Come si recupera un file cancellato ma ancora aperto?
7. Qual è la differenza tra mtime, ctime e atime? Quale non si può falsificare con `touch`, e perché è utile in forensics?
8. Perché `mv` è a volte istantaneo e a volte lento?
9. Come si riconosce il vero tipo di un file? Che cos'è un numero magico?
10. Che cosa sono `/dev/null` e `/proc/self`? Nomina tre file utili dentro `/proc/<PID>`.
11. Perché in `find` si usano `-print0` e `xargs -0`, o `-exec ... +`, quando si passano i risultati a un altro comando?
12. Che cos'è un attacco con link simbolico in `/tmp`, e quali protezioni lo impediscono?

## 19. Riepilogo

- Il file system trasforma blocchi di disco in file (sequenze di byte) e directory (tabelle nome → inode). Linux monta molti file system diversi, anche virtuali come `/proc`, in un unico albero, uniformati dal VFS.
- La gerarchia FHS dice dove stanno programmi (`/usr/bin`), configurazione (`/etc`), dati variabili (`/var`), utenti (`/home`), file temporanei (`/tmp`): conoscerla è sapere dove cercare.
- I percorsi si risolvono componente per componente, dalla radice o dalla directory corrente del processo; `..` del kernel è fisico, quello di `cd` logico.
- L'inode contiene tutto tranne il nome. Un hard link è un altro nome dello stesso inode; un link simbolico è un file che contiene un percorso, interpretato dalla directory del link.
- Cancellare significa togliere un nome: il file sparisce quando non ha più nomi **e** nessuno lo tiene aperto.
- Le date (mtime, ctime, atime) raccontano la storia di un file; mtime si falsifica, ctime no.
- Il tipo vero di un file è nei suoi primi byte, non nell'estensione: `file` e `od` lo rivelano.
- `/dev` e `/proc` espongono dispositivi e processi come file; `find` cerca per qualunque proprietà, e con `-print0` o `-exec` gestisce qualunque nome.
- Link, nomi prevedibili e il tempo tra controllo e uso sono la base di intere classi di vulnerabilità (CWE-59, CWE-367) che riprenderemo nel Modulo 4.

## 20. Fonti

- **pwn.college**, *Linux Luminarium — 2 The File System* (trascrizione 087, `C:\CTF_Transcripts\pwn.college`): directory annidate, radice, percorsi, directory standard (`/usr`, `/etc`, `/home`, `/tmp`), confronto con Windows e montaggio. Il significato di `usr` è corretto nel §2.2.
- **pwn.college**, *Linux Luminarium — 3 Symbolic Links* (trascrizione 086): tipi di file in `ls -l`, link simbolici relativi e assoluti, il problema dello spostamento, hard link.
- **R. e A. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces*, cap. 39 (*Interlude: Files and Directories*: inode, `unlink`, hard e soft link, `rename` atomica, montaggio) e cap. 40 (*File System Implementation*).
- **OccupyTheWeb**, *Linux Basics for Hackers*, cap. 1 (navigazione, `find`, `locate`, `whereis`) e cap. 10 (*Filesystem and Storage Device Management*: `/dev`, montaggio, `df`).
- **Linux Foundation**, *Filesystem Hierarchy Standard* 3.0; `man 7 hier`.
- **Pagine di manuale**: `path_resolution(7)`, `inode(7)`, `symlink(7)`, `stat(1)`, `ls(1)`, `ln(1)`, `find(1)`, `file(1)`, `magic(5)`, `proc(5)`, `null(4)`, `random(4)`, `mount(8)`.
- **Documentazione del kernel Linux**, `Documentation/admin-guide/sysctl/fs.rst`: `protected_symlinks`, `protected_hardlinks`.
- **D. M. Ritchie e K. Thompson**, *The UNIX Time-Sharing System*, Communications of the ACM, 1974: il modello originale di file, directory e i-node.
- **MITRE CWE**: CWE-59 (*Link Following*), CWE-367 (*Time-of-check Time-of-use Race Condition*), CWE-377 (*Insecure Temporary File*).

## 21. Prossima lezione

**Lezione 3 — Cercare e trasformare testo**: espressioni regolari, `grep`, `sed`, `awk`, `cut`, `tr`, `sort`, `uniq`, `wc`, `strings`. Dopo aver imparato a trovare i file, impareremo a trovare ciò che c'è dentro.
