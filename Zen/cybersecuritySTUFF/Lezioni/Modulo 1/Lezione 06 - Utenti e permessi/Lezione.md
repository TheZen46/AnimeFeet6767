# Modulo 1 — Lezione 6: Utenti e permessi

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 6 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 15).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. formulare il problema del **controllo d'accesso** in termini di soggetti, oggetti e operazioni, descrivere la matrice di accesso e le sue due realizzazioni (liste di controllo d'accesso e liste di capability), e distinguere controllo **discrezionale** (DAC) e **obbligatorio** (MAC);
2. spiegare che cosa sono per il kernel un **utente** e un **gruppo** (numeri, non nomi), leggere campo per campo `/etc/passwd`, `/etc/shadow`, `/etc/group`, e riconoscere il formato di un hash di password;
3. descrivere le **credenziali di un processo**: UID e GID reale, effettivo e salvato, gruppi supplementari, e come cambiano durante il login, con `su`, con `sudo` e con l'esecuzione di un programma *setuid*;
4. leggere e scrivere i permessi `rwx` in notazione simbolica e ottale, applicare a mente l'**algoritmo di controllo** del kernel (proprietario → gruppo → altri, senza ricaduta), e spiegare il significato diverso di `r`, `w`, `x` su un file e su una directory;
5. calcolare i permessi di un file appena creato a partire dalla **umask**;
6. spiegare i bit **setuid**, **setgid** e **sticky** su file e su directory, quando vengono ignorati o azzerati, e perché sono il punto più delicato dell'intero modello;
7. usare le **ACL POSIX**, gli attributi `chattr` e le **capability** di Linux, e sapere quando ognuno di essi si sovrappone ai bit tradizionali;
8. fare l'**audit** dei permessi di una macchina: trovare file scrivibili da tutti, programmi setuid e capability superflue, regole `sudo` troppo larghe, file di configurazione esposti, e correggerli; riconoscere le stesse configurazioni sbagliate quando, in una CTF, sono la strada verso la flag.

**Prerequisiti:** Lezioni 1–5. In particolare: inode e metadati, `ls -l`, `stat`, link fisici e simbolici (L2 §4–7), `find` con i suoi predicati (L2 §11), le credenziali di un processo come le abbiamo intraviste in `/proc/<PID>/status` (L5 §7.3), `fork`/`execve` e che cosa passa da padre a figlio (L5 §4, §12), `PATH` e la ricerca dei comandi (L1 §11).

**Tempo:** circa 4–5 ore di lettura e prove, 3–4 ore di esercizi. Per molte prove ti servono **due utenti**. Su una macchina virtuale tua (mai su una macchina che non amministri) crea un utente di prova:

```
$ sudo useradd -m -s /bin/bash prova
$ sudo passwd prova
```

e tieni aperto un secondo terminale con `su - prova`. Alla fine della lezione puoi eliminarlo con `sudo userdel -r prova`. Se lavori su WSL o in un container in cui sei già root, crea comunque l'utente: **da root quasi nessun controllo di permesso si applica**, e molti esperimenti di oggi non mostrerebbero niente.

**Ripasso dalle lezioni precedenti.**
- Nella Lezione 2 abbiamo visto che un file è un inode, e che l'inode contiene, tra l'altro, un UID proprietario, un GID e un campo `mode` di 16 bit (L2 §4.2). Abbiamo letto `-rw-r--r--` senza spiegarlo davvero. Oggi lo spieghiamo bit per bit.
- Nella Lezione 2 abbiamo anche detto che cancellare un file vuol dire togliere un nome da una directory (L2 §5). Oggi ne trarremo la conseguenza più sorprendente: per cancellare un file **non serve alcun permesso sul file**.
- Nella Lezione 5 abbiamo letto in `/proc/self/status` la riga `Uid:` con quattro numeri e la riga `Cap...` con cinque maschere esadecimali, promettendo di spiegarle (L5 §7.3). Oggi manteniamo la promessa.
- Nella Lezione 5 abbiamo visto che `execve` sostituisce il programma ma mantiene l'identità del processo (L5 §4.2). Oggi vediamo l'unica grande eccezione: l'`execve` di un file setuid **cambia** l'identità.

**Piano della lezione.**
- *Parte I — Chi è chi* (§1–5): il problema del controllo d'accesso, utenti e gruppi, i file che li descrivono, le credenziali di un processo, `su` e `sudo`.
- *Parte II — I permessi tradizionali* (§6–9): il modello `rwx`, la notazione, `umask`, i bit speciali.
- *Parte III — Oltre `rwx`* (§10–13): ACL, attributi del file system, capability, controllo obbligatorio.
- *Parte IV — Sicurezza* (§14–16): le configurazioni sbagliate più comuni, come trovarle e correggerle, i permessi nelle CTF.
- *Parte V — La pratica* (§17–22): esempi svolti, esercizi, autoverifica, riepilogo, fonti.

Una nota di metodo prima di cominciare. Questa è la prima lezione del corso in cui parliamo di sicurezza in senso stretto. Il punto di vista è quello di chi **amministra e difende** un sistema: capire esattamente che cosa il kernel permette e perché, così da poter riconoscere una configurazione pericolosa e correggerla. Le CTF di categoria *misc* e *pwn* ti chiederanno la stessa cosa dall'altro lato: su una macchina costruita apposta, trovare l'errore che l'autore ha lasciato. Le competenze sono identiche; quello che cambia è soltanto chi ha messo l'errore e chi ti ha dato il permesso di cercarlo. Ogni esperimento di oggi va fatto sulla tua macchina virtuale o sulle piattaforme di allenamento.

---

# Parte I — Chi è chi

## 1. Il problema del controllo d'accesso

### 1.1 Soggetti, oggetti, operazioni

Ogni sistema multiutente deve rispondere migliaia di volte al secondo alla stessa domanda: **questo soggetto può eseguire questa operazione su questo oggetto?** Le tre parole hanno un significato tecnico preciso.

- Il **soggetto** è chi agisce. In un sistema operativo non è mai una persona: è un **processo**, che agisce *per conto* di qualcuno. La persona entra in gioco solo indirettamente, attraverso l'identità che il processo porta con sé.
- L'**oggetto** è la risorsa: un file, una directory, un dispositivo, una porta di rete, un altro processo (a cui mandare un segnale o di cui leggere la memoria), una zona di memoria condivisa.
- L'**operazione** è che cosa il soggetto vuole fare: leggere, scrivere, eseguire, cancellare, cambiare il proprietario, mandare un segnale.

Il componente che risponde alla domanda si chiama, nella letteratura classica, **reference monitor** (*monitor dei riferimenti*, rapporto Anderson del 1972 per l'aviazione statunitense). Per essere degno di fiducia deve avere tre proprietà, che ritroverai in ogni testo di sicurezza:

1. **mediazione completa**: ogni accesso passa dal monitor, nessuno escluso;
2. **resistenza alla manomissione**: il soggetto controllato non può modificare il monitor;
3. **verificabilità**: il monitor è abbastanza piccolo e semplice da poter essere analizzato e provato corretto.

In Linux il reference monitor è il **kernel**. Un processo non può aprire un file se non chiedendolo al kernel con una chiamata di sistema (`open`, `openat`), e il kernel, prima di restituire un descrittore, esegue il controllo. È per questo che nella Lezione 5 abbiamo insistito sulla separazione fra modalità utente e modalità kernel (L5 §1.5): la seconda proprietà del monitor dipende interamente da quella separazione. Vale la pena notare subito una conseguenza della prima proprietà: il controllo si fa **all'apertura**, non a ogni lettura. Se un processo ha già un descrittore aperto in lettura e tu tolgi i permessi al file, il processo continua a leggere. Il descrittore è, a tutti gli effetti, un *diritto* già concesso (torneremo su questa idea fra un momento, e poi di nuovo nel §14.7).

### 1.2 La matrice di accesso

Il modo più generale di descrivere *chi può fare che cosa* è la **matrice di accesso** introdotta da Butler Lampson nel 1971 e formalizzata da Harrison, Ruzzo e Ullman nel 1976. Le righe sono i soggetti, le colonne gli oggetti, e ogni cella contiene l'insieme delle operazioni permesse:

```
               /etc/passwd   /etc/shadow   /home/zen/note   stampante
  root         r w           r w           r w              usa
  zen          r             -             r w              usa
  www-data     r             -             -                -
```

La matrice è un modello, non una struttura dati: in un sistema reale con migliaia di utenti e milioni di file sarebbe enorme e quasi tutta vuota. Ci sono due modi naturali di memorizzarla in modo compatto.

- **Per colonne**: a ogni oggetto si attacca la lista di chi può fare che cosa su di esso. È una **ACL** (*Access Control List*, lista di controllo d'accesso). Rispondere a "chi può leggere `/etc/shadow`?" è facile; rispondere a "che cosa può leggere zen?" richiede di scorrere tutti i file.
- **Per righe**: a ogni soggetto si dà l'elenco degli oggetti a cui può accedere, sotto forma di gettoni non falsificabili chiamati **capability** (in questo senso classico la parola indica un *riferimento più diritti*). Rispondere a "che cosa può fare zen?" è facile; revocare un diritto è difficile, perché bisogna ritrovare tutti i gettoni distribuiti.

Unix usa sostanzialmente il primo modello, in una forma molto compressa: invece di una lista arbitraria per ogni file, tre sole voci (proprietario, gruppo, tutti gli altri). Ma c'è anche un pezzo del secondo modello, ed è proprio il **descrittore di file**: una volta che il kernel te l'ha dato, il descrittore è un gettone che porta con sé il diritto (lettura, scrittura) e che puoi persino passare a un altro processo, per eredità o tramite un socket Unix. Infine, attenzione al nome: le **capability di Linux** (§12) sono un'altra cosa ancora, cioè privilegi del superutente divisi in pezzi. La coincidenza di nome confonde tutti, la prima volta.

### 1.3 Discrezionale e obbligatorio

La seconda grande distinzione riguarda **chi decide** il contenuto della matrice.

- Nel controllo **discrezionale** (DAC, *Discretionary Access Control*) è il **proprietario** dell'oggetto a decidere chi vi accede. Se un file è tuo, puoi renderlo leggibile a tutti con un `chmod`, e il sistema non ha niente da obiettare. Il modello Unix tradizionale è DAC.
- Nel controllo **obbligatorio** (MAC, *Mandatory Access Control*) è una **politica di sistema**, decisa dall'amministratore e non modificabile dagli utenti, a stabilire che cosa è permesso. Anche se un file è tuo, la politica può impedirti di passarlo a un processo di un livello diverso. Esempi in Linux: SELinux e AppArmor (§13).

Il difetto strutturale del DAC è la sua stessa definizione: un proprietario può essere ingannato. Se un programma che esegui come te è malevolo (un *cavallo di Troia*), può fare tutto quello che puoi fare tu, compreso rendere i tuoi file leggibili a tutti, e il DAC non ha modo di accorgersene perché quella operazione è perfettamente legittima per il proprietario. Il MAC nasce proprio per porre un limite che neanche il proprietario può superare. I modelli classici sono due e conviene conoscerli per nome:

- **Bell–LaPadula** (1973), pensato per la **riservatezza** nei sistemi militari: livelli di classificazione ordinati (non classificato, riservato, segreto...), con le regole *no read up* (non leggere oggetti di livello superiore al tuo) e *no write down* (non scrivere su oggetti di livello inferiore, per non far trapelare informazioni verso il basso).
- **Biba** (1977), il duale per l'**integrità**: *no read down* (non fidarti di dati meno affidabili di te) e *no write up* (non corrompere dati più affidabili di te).

### 1.4 I principi di progettazione

Nel 1975 Jerome Saltzer e Michael Schroeder pubblicarono *The Protection of Information in Computer Systems*, un articolo che elenca otto principi di progettazione ancora oggi alla base di ogni discussione seria sul tema. Quattro di essi ci accompagneranno per tutta la lezione, e conviene averli in testa fin d'ora perché ogni errore di configurazione che vedremo nella Parte IV ne viola almeno uno.

- **Minimo privilegio** (*least privilege*): ogni programma e ogni utente deve operare con l'insieme minimo di privilegi necessari al suo compito. Un server web non ha bisogno di poter leggere `/etc/shadow`; un programma che deve solo aprire una porta bassa non ha bisogno di tutti i poteri di root.
- **Impostazioni predefinite sicure** (*fail-safe defaults*): la decisione di base è il rifiuto; l'accesso si concede esplicitamente. Un file appena creato non dovrebbe essere scrivibile da tutti (è il compito della `umask`, §8).
- **Mediazione completa** (*complete mediation*): ogni accesso deve essere controllato. Il caso del descrittore già aperto (§1.1) è un compromesso consapevole su questo principio.
- **Economia del meccanismo** (*economy of mechanism*): il meccanismo deve essere il più semplice possibile. I nove bit `rwx` di Unix sono un esempio estremo di economia, con tutti i limiti che ne derivano.

Gli altri quattro sono il *progetto aperto* (la sicurezza non deve dipendere dalla segretezza del meccanismo), la *separazione dei privilegi* (un'operazione critica richiede più condizioni indipendenti), il *meccanismo meno comune* (minimizzare le risorse condivise fra utenti, come `/tmp`) e l'*accettabilità psicologica* (se il meccanismo è scomodo, gli utenti lo aggirano: pensa a chi fa `chmod 777` per "far funzionare le cose").

## 2. Utenti e gruppi

### 2.1 Per il kernel un utente è un numero

La prima idea da fissare è che il kernel **non conosce i nomi degli utenti**. Conosce soltanto numeri interi a 32 bit: lo **UID** (*user identifier*) e il **GID** (*group identifier*). Nell'inode di ogni file c'è un UID e un GID; nelle credenziali di ogni processo ci sono UID e GID. Il controllo d'accesso confronta numeri con numeri.

I nomi (`zen`, `root`, `www-data`) esistono solo nello **spazio utente**: sono una tabella di traduzione mantenuta in file di testo (§3) e consultata da programmi come `ls`, `ps`, `id` quando devono mostrarti qualcosa di leggibile. Lo vedi bene così:

```
$ ls -ln /etc/passwd          # -n: mostra i numeri invece dei nomi
-rw-r--r-- 1 0 0 2847 ott 12 09:14 /etc/passwd
$ touch x; sudo chown 4242:4242 x; ls -l x
-rw-r--r-- 1 4242 4242 0 nov  7 19:30 x
```

Un UID che non corrisponde a nessun nome viene semplicemente mostrato come numero. È una situazione comune dopo aver estratto un archivio `tar` creato su un'altra macchina, o dopo aver cancellato un utente senza cancellarne i file: quei file restano di proprietà di un numero "orfano", e se in futuro crei un nuovo utente che riceve lo stesso UID, **erediterà quei file**. È un piccolo problema di sicurezza reale, e il motivo per cui `find / -nouser -o -nogroup` fa parte di ogni audit (§15).

Lo stesso vale per i container: dentro un container il processo con UID 0 si chiama `root`, e sul sistema ospite lo stesso numero 0 si chiama ancora `root`, a meno di usare i *namespace utente* che rimappano gli UID. È uno dei motivi per cui "sono root nel container" e "sono root sulla macchina" sono affermazioni pericolosamente vicine.

### 2.2 Gli intervalli di UID

Per convenzione (non per regola del kernel) gli UID sono divisi in intervalli, definiti in `/etc/login.defs`:

| UID | Chi | Esempi |
|---|---|---|
| 0 | il **superutente** | `root` |
| 1–99 | account di sistema statici, assegnati dalla distribuzione | `daemon` (1), `bin` (2), `sys` (3) |
| 100–999 | account di sistema dinamici, creati dai pacchetti per i servizi | `www-data`, `sshd`, `systemd-network`, `postgres` |
| 1000–60000 | utenti **umani** | il primo utente creato all'installazione ha di solito 1000 |
| 65534 | `nobody`, l'utente senza privilegi | usato da NFS e da servizi che vogliono "nessuna identità" |

```
$ grep -E '^(UID|GID|SYS_UID)_(MIN|MAX)' /etc/login.defs
UID_MIN                  1000
UID_MAX                 60000
SYS_UID_MIN              100
SYS_UID_MAX              999
```

Gli **account di servizio** esistono per applicare il principio del minimo privilegio: invece di far girare il server web come root, lo si fa girare come `www-data`, un utente che possiede solo i file di cui il server ha bisogno. Se il server viene compromesso, l'attaccante ottiene i poteri di `www-data`, non quelli di root. In una CTF di categoria web, quando ottieni l'esecuzione di comandi sul server, la prima cosa che vedi con `id` è quasi sempre proprio `uid=33(www-data)`.

### 2.3 Root: un numero speciale

Lo UID 0 è l'unico numero che il kernel tratta in modo speciale. Tradizionalmente, un processo con UID effettivo 0 **salta quasi tutti i controlli di permesso**: legge e scrive qualunque file a prescindere dai bit `rwx`, cambia il proprietario di qualunque file, manda segnali a qualunque processo, carica moduli del kernel, cambia l'ora. Nel Linux moderno questa onnipotenza è stata scomposta in una quarantina di **capability** (§12), e "essere root" significa, più precisamente, "avere tutte le capability". Ma per ora la semplificazione regge.

Il nome `root` non conta nulla. Se in `/etc/passwd` aggiungi una riga `pippo:x:0:0::/root:/bin/bash`, chiunque entri come `pippo` è a tutti gli effetti il superutente. Per questo uno dei primi controlli di un audit è cercare **tutti** gli utenti con UID 0, non solo `root`:

```
$ awk -F: '$3 == 0 {print $1}' /etc/passwd
root
```

Una sola riga deve uscire. Due o più sono quasi sempre il segno di una compromissione (una *backdoor* classica) o di una pessima idea di qualche amministratore.

Un'osservazione importante: alcuni controlli valgono **anche per root**. Il bit di esecuzione è uno di questi: root può eseguire un file solo se **almeno uno** dei tre bit `x` è attivo (un file `rw-r--r--` non è eseguibile neppure da root, mentre uno `---------x` lo è). Gli attributi `chattr +i` (§11) fermano anche root. E un file system montato in sola lettura resta in sola lettura per tutti.

### 2.4 I gruppi

Un **gruppo** è un insieme di utenti con un nome e un GID, che serve a concedere un permesso a molte persone insieme senza concederlo a tutti. Ogni utente ha:

- un **gruppo primario**, scritto nel suo record in `/etc/passwd`. È il gruppo che viene assegnato ai file che crea (salvo il caso delle directory setgid, §9.3). Sulle distribuzioni moderne, per ogni utente si crea un gruppo omonimo e privato (*User Private Group*, UPG): l'utente `zen` ha come gruppo primario `zen`, con lo stesso numero;
- zero o più **gruppi supplementari**, elencati in `/etc/group`. Servono a dare accesso a risorse condivise.

```
$ id
uid=1000(zen) gid=1000(zen) groups=1000(zen),4(adm),24(cdrom),27(sudo),100(users)
$ id -Gn prova
prova
$ groups
zen adm cdrom sudo users
```

Alcuni gruppi supplementari hanno un significato speciale, ed è importante saperlo perché **appartenere a certi gruppi equivale, o quasi, a essere root**:

| Gruppo | Che cosa concede | Perché è delicato |
|---|---|---|
| `sudo` (Debian/Ubuntu), `wheel` (Red Hat, Arch) | usare `sudo` per diventare root | è il modo previsto di amministrare |
| `adm` | leggere i log in `/var/log` | i log contengono indirizzi, nomi utente, a volte password digitate per errore |
| `shadow` | leggere `/etc/shadow` | permette l'attacco a dizionario sugli hash |
| `disk` | leggere e scrivere i dispositivi a blocchi (`/dev/sda`) | si può leggere qualunque file direttamente dal disco, aggirando i permessi: equivale a root |
| `docker` | parlare con il demone Docker | si può avviare un container che monta `/` dell'ospite: equivale a root |
| `lxd`, `libvirt` | gestire container e macchine virtuali | stesso problema di `docker` |
| `video`, `input` | accedere allo schermo e alla tastiera | si può catturare quello che gli altri utenti vedono o digitano |

L'appartenenza ai gruppi viene letta **al login** e fissata nelle credenziali del processo (§4). Se aggiungi un utente a un gruppo con `usermod -aG docker zen`, la shell già aperta di `zen` non se ne accorge: bisogna uscire e rientrare, oppure avviare una nuova shell con `newgrp docker` o `su - zen`. Questo dettaglio fa perdere ore a molti amministratori, e il motivo è proprio che i gruppi sono una proprietà del processo, non dell'utente.

Nota infine l'opzione `-a` di `usermod -aG`: senza di essa, `-G` **sostituisce** l'intera lista dei gruppi supplementari, e l'utente perde tutti gli altri, compreso `sudo`. È uno dei modi più rapidi per chiudersi fuori dalla propria macchina.

## 3. I file che descrivono utenti e gruppi

### 3.1 `/etc/passwd`

È il registro degli utenti: una riga per utente, sette campi separati da due punti. Il file è leggibile da **tutti** (`-rw-r--r-- root root`), perché qualunque programma deve poter tradurre un UID in un nome.

```
zen:x:1000:1000:Zen,,,:/home/zen:/bin/bash
 1  2  3    4     5        6        7
```

1. **nome** dell'utente (*login name*), quello che digiti al login;
2. **password**: oggi quasi sempre `x`, che significa "la password è in `/etc/shadow`". Storicamente qui c'era l'hash, ed era leggibile da tutti; vedi §3.2;
3. **UID**;
4. **GID** del gruppo primario;
5. **GECOS**: un campo di commento libero, di solito nome completo, stanza, telefono separati da virgole. Il nome curioso viene dal *General Electric Comprehensive Operating System*, a cui i primi sistemi Unix dei Bell Labs spedivano lavori di stampa;
6. **directory home**;
7. **shell di login**: il programma che `login` avvia dopo l'autenticazione. Per gli account di servizio è `/usr/sbin/nologin` o `/bin/false`, che rifiutano l'accesso interattivo: `nologin` stampa un messaggio ed esce con 1, `false` esce con 1 senza dire niente.

Alcune osservazioni da tenere a mente.

- Il campo 2 può contenere un hash vero anche oggi, se qualcuno lo ha scritto lì: in quel caso **è usato** al posto di quello in `shadow`. Se il campo 2 è **vuoto**, l'utente non ha password e su molti sistemi si entra premendo Invio. Entrambe sono configurazioni da cercare in un audit (§15.2).
- Se `/etc/passwd` è **scrivibile** da un utente non privilegiato, quell'utente può aggiungere una riga con UID 0 e diventare root. È l'errore di configurazione più grave che esista su questo file, ed è un classico delle macchine di allenamento.
- `/etc/passwd` non è l'unica fonte. Il sistema chiede gli utenti attraverso la **NSS** (*Name Service Switch*), configurata in `/etc/nsswitch.conf`: la riga `passwd: files systemd ldap` dice di cercare prima nei file, poi nel servizio di systemd, poi in un server LDAP. Per questo il modo corretto di interrogare il database non è `grep` sul file, ma `getent`:

```
$ getent passwd zen
zen:x:1000:1000:Zen,,,:/home/zen:/bin/bash
$ getent passwd 0
root:x:0:0:root:/root:/bin/bash
$ getent group sudo
sudo:x:27:zen
```

In un'azienda in cui gli utenti stanno in Active Directory o LDAP, `grep zen /etc/passwd` non trova niente, mentre `getent passwd zen` funziona.

Per contare gli utenti umani e vedere quali shell usano, è il caso di ripescare `awk` dalla Lezione 3:

```
$ awk -F: '$3 >= 1000 && $3 < 60000 {print $1, $7}' /etc/passwd
zen /bin/bash
prova /bin/bash
$ awk -F: '{print $7}' /etc/passwd | sort | uniq -c | sort -rn
     22 /usr/sbin/nologin
      3 /bin/bash
      1 /bin/sync
```

### 3.2 `/etc/shadow`

Negli anni '70 e '80 gli hash delle password stavano in `/etc/passwd`, leggibile da tutti. Il ragionamento era che un hash non si può invertire. Il ragionamento era sbagliato: un hash non si inverte, ma si può **indovinare** la password provando milioni di candidati e confrontando gli hash (attacco a dizionario, o forza bruta). Il celebre articolo di Morris e Thompson del 1979, *Password Security: A Case History*, mostrava già che una frazione enorme delle password reali si trovava in poche ore. La soluzione fu spostare gli hash in un file separato, leggibile solo da root e dal gruppo `shadow`:

```
$ ls -l /etc/shadow
-rw-r----- 1 root shadow 1453 ott 12 09:14 /etc/shadow
$ sudo grep zen /etc/shadow
zen:$y$j9T$Kd8...$Qp3...:20380:0:99999:7:::
 1          2               3   4   5   6 789
```

I nove campi sono:

1. **nome**;
2. **hash della password**, oppure un marcatore (vedi sotto);
3. data dell'**ultimo cambio** della password, in giorni dal 1° gennaio 1970;
4. età **minima**: giorni che devono passare prima di poterla cambiare di nuovo;
5. età **massima**: dopo quanti giorni la password scade (99999 = mai);
6. giorni di **preavviso** prima della scadenza;
7. giorni di **inattività** concessi dopo la scadenza, prima che l'account sia bloccato;
8. data di **scadenza dell'account**, in giorni dal 1970;
9. campo riservato.

I campi 3–8 si leggono comodamente con `chage -l zen`. Il campo 2 merita attenzione. Se inizia con `!` o `*`, nessuna password può corrispondere: l'account è **bloccato** per l'accesso con password (ma può ancora entrare con una chiave SSH, se ne ha una: bloccare la password non è disattivare l'account). `!` è quello che mette `passwd -l`; `*` è il valore tipico degli account di servizio, che non hanno mai avuto una password. Un campo **vuoto** significa "nessuna password richiesta".

Se il campo contiene un hash, ha il formato **crypt modulare**: `$id$parametri$sale$hash`. L'identificativo dice quale algoritmo è stato usato:

| Prefisso | Algoritmo | Note |
|---|---|---|
| (nessuno, 13 caratteri) | DES crypt | storico, usa solo i primi 8 caratteri della password: rompibile in pochi minuti |
| `$1$` | MD5-crypt | anni '90, oggi debole |
| `$2a$`, `$2b$`, `$2y$` | bcrypt | usato da BSD e da molte applicazioni web |
| `$5$` | SHA-256-crypt | |
| `$6$` | SHA-512-crypt | il predefinito su molte distribuzioni fino al 2021 circa |
| `$y$` | yescrypt | predefinito su Debian 11+, Ubuntu 22.04+, Fedora 35+ |

Il **sale** (*salt*) è una stringa casuale diversa per ogni utente, che viene combinata con la password prima di calcolare l'hash. Ha due scopi: due utenti con la stessa password hanno hash diversi, e diventa inutile precalcolare tabelle di hash per tutte le password possibili (le *rainbow table*), perché bisognerebbe farne una per ogni sale. Gli algoritmi moderni sono inoltre **lenti di proposito**: SHA-512-crypt applica di default 5000 iterazioni, yescrypt e bcrypt sono progettati per essere costosi anche in memoria, così che chi tenta milioni di password debba pagare milioni di volte quel costo. Nel Modulo 5 (crittografia) studieremo queste funzioni di derivazione delle chiavi in dettaglio; per ora basta saper riconoscere il formato, che in una CTF ti dice subito con quale modalità lanciare uno strumento come `john` o `hashcat`.

Puoi generare un hash a mano per vedere il formato:

```
$ openssl passwd -6 -salt abcdefgh segreto
$6$abcdefgh$...
$ mkpasswd -m yescrypt segreto       # pacchetto whois su Debian
$y$j9T$...
```

Se `/etc/shadow` è **leggibile** da un utente non privilegiato, l'attaccante ottiene gli hash e può tentarne la rottura con calma su un'altra macchina. Se è **scrivibile**, può sostituire l'hash di root con uno di cui conosce la password. Entrambe sono configurazioni da controllare.

### 3.3 `/etc/group` e `/etc/gshadow`

`/etc/group` ha quattro campi:

```
sudo:x:27:zen,anna
 1   2 3   4
```

nome del gruppo, password del gruppo (quasi sempre `x`, inutilizzata), GID, e l'elenco dei **membri supplementari** separati da virgole. Attenzione: un utente che ha questo gruppo come **primario** (campo 4 di `passwd`) ne fa parte anche se non compare nell'elenco. Per sapere chi appartiene davvero a un gruppo bisogna guardare entrambi i file:

```
$ g=sudo; gid=$(getent group $g | cut -d: -f3)
$ { getent group $g | cut -d: -f4 | tr , '\n'; awk -F: -v g="$gid" '$4==g{print $1}' /etc/passwd; } | sort -u
```

`/etc/gshadow` contiene le password di gruppo (usate dal raro comando `newgrp` per entrare in un gruppo di cui non si è membri) e gli **amministratori** del gruppo, che possono aggiungere e togliere membri con `gpasswd`. È leggibile solo da root e da `shadow`.

### 3.4 Gli strumenti di gestione

Non si modificano questi file con un editor qualunque: se due programmi li scrivono contemporaneamente, o se l'editor si interrompe a metà, si rischia di corrompere il database e restare senza root. Gli strumenti dedicati prendono un **lock** (i file `/etc/passwd.lock`, `/etc/shadow.lock`) e scrivono in modo atomico.

| Comando | Effetto |
|---|---|
| `useradd -m -s /bin/bash -G sudo anna` | crea l'utente, la home (`-m`), sceglie la shell, aggiunge ai gruppi |
| `adduser anna` | front-end interattivo di Debian/Ubuntu |
| `usermod -aG docker anna` | aggiunge un gruppo supplementare (con `-a`!) |
| `usermod -L anna` / `-U` | blocca / sblocca la password (aggiunge o toglie `!`) |
| `usermod -s /usr/sbin/nologin anna` | toglie la shell interattiva |
| `userdel -r anna` | cancella l'utente e la sua home |
| `groupadd team`, `gpasswd -a anna team`, `gpasswd -d anna team` | gestione dei gruppi |
| `passwd`, `passwd anna`, `passwd -l anna`, `passwd -S anna` | cambia, blocca, mostra lo stato |
| `chage -M 90 -W 7 anna`, `chage -l anna` | politica di scadenza |
| `vipw`, `vigr`, `vipw -s` | modifica manuale con lock e controllo di coerenza |
| `pwck`, `grpck` | verifica la coerenza dei file |

`useradd` legge i valori predefiniti da `/etc/default/useradd` e da `/etc/login.defs`, e copia nella nuova home il contenuto di `/etc/skel` (i file `.bashrc`, `.profile` iniziali). Se `/etc/skel` contiene qualcosa di pericoloso, tutti i nuovi utenti lo ricevono: un altro punto da guardare.

### 3.5 Come funziona il login

Mettiamo insieme i pezzi seguendo un login su una console testuale. È la stessa sequenza, con varianti, per `sshd` e per il login grafico.

1. Un processo di root (`agetty`) apre il terminale, stampa `login:` e legge il nome. Poi fa `execve` di `/bin/login`, che gira ancora come root.
2. `login` delega l'autenticazione a **PAM** (*Pluggable Authentication Modules*): una libreria che legge `/etc/pam.d/login` e chiama in sequenza dei moduli. `pam_unix` legge l'hash da `/etc/shadow` (può farlo perché `login` è root), calcola l'hash della password digitata con lo stesso sale e confronta. Altri moduli possono controllare l'ora, il numero di tentativi falliti (`pam_faillock`), un secondo fattore, impostare la umask (`pam_umask`), creare la home se manca.
3. Se l'autenticazione riesce, `login` deve **diventare** l'utente. Lo fa con tre chiamate, in quest'ordine preciso:
   - `initgroups("zen", 1000)`: legge `/etc/group` e imposta i **gruppi supplementari** del processo;
   - `setgid(1000)`: imposta il GID;
   - `setuid(1000)`: imposta lo UID. Questa chiamata, eseguita da root, cambia **tutti e tre** gli UID (reale, effettivo, salvato) ed è **irreversibile**: dopo, il processo non ha più alcun modo di tornare root.
4. Cambia directory nella home, imposta `HOME`, `SHELL`, `USER`, `LOGNAME`, `PATH`, e fa `execve` della shell di login, con `argv[0]` che inizia con un trattino (`-bash`): è così che bash sa di essere una shell di login e deve leggere `/etc/profile` e `~/.profile` (L1 §12.3).

L'ordine delle chiamate al punto 3 non è un dettaglio. Se un programma facesse prima `setuid` e poi `setgid`, la seconda chiamata fallirebbe (un utente normale non può cambiare il proprio GID a piacere) e il processo resterebbe con il **GID di root**. Se dimenticasse `initgroups`, resterebbe con i **gruppi supplementari di root**. Entrambi sono errori reali trovati in programmi reali, catalogati come CWE-271 (*Privilege Dropping / Lowering Errors*). E chi non controlla il valore di ritorno di `setuid` rischia di continuare come root se la chiamata fallisce (per esempio per il limite `RLIMIT_NPROC` su vecchi kernel): CWE-273.

Da questo momento ogni processo che la shell crea con `fork` eredita le stesse credenziali (L5 §12.1). L'identità passa di padre in figlio, ed è questo il filo che lega ogni processo sulla macchina alla persona che si è autenticata.

## 4. Le credenziali di un processo

### 4.1 Tre UID, non uno

Nella Lezione 5 abbiamo letto in `/proc/self/status`:

```
$ grep -E '^(Uid|Gid|Groups)' /proc/self/status
Uid:	1000	1000	1000	1000
Gid:	1000	1000	1000	1000
Groups:	4 24 27 100 1000
```

I quattro numeri di `Uid:` sono, nell'ordine, lo UID **reale**, **effettivo**, **salvato** e quello **del file system**. Lo stesso per i GID. Per un processo normale sono tutti uguali, e per questo di solito non ci si pensa. Ma hanno ruoli distinti.

- Lo **UID reale** (*real UID*, `ruid`) dice **chi ha avviato** il processo, cioè per conto di chi lavora. Determina, ad esempio, a chi un processo può mandare segnali e a chi va il conteggio dei processi per il limite `RLIMIT_NPROC`.
- Lo **UID effettivo** (*effective UID*, `euid`) è quello che il kernel usa nei **controlli di permesso**: apertura di file, creazione di file (il nuovo file prende l'`euid` come proprietario), e così via. È l'identità *con cui* il processo agisce.
- Lo **UID salvato** (*saved set-user-ID*, `suid`) è una copia di riserva dell'UID effettivo al momento dell'`execve`. Serve a un programma privilegiato per **abbassare temporaneamente** i propri privilegi e poi riprenderli.
- Lo **UID del file system** (`fsuid`) è una particolarità di Linux, nata per i server NFS: è quello usato per i controlli sui file. Segue automaticamente l'UID effettivo e quasi nessun programma lo cambia; per il resto della lezione lo puoi considerare uguale all'`euid`.

Accanto agli ID ci sono i **gruppi supplementari** (riga `Groups:`), che partecipano al controllo d'accesso esattamente come il GID effettivo: un processo "appartiene" a un gruppo se quel gruppo è il suo GID effettivo **oppure** è nella lista supplementare.

Da shell li vedi con `id`, che mostra reale ed effettivo quando differiscono:

```
$ id
uid=1000(zen) gid=1000(zen) groups=1000(zen),27(sudo)
$ ps -o pid,ruser,euser,suser,fuser,comm -p $$
    PID RUSER    EUSER    SUSER    FUSER    COMMAND
   2214 zen      zen      zen      zen      bash
```

### 4.2 Le regole del cambiamento

Che cosa può fare un processo con i propri UID? Le regole, semplificate ma corrette per i casi che contano:

- un processo **privilegiato** (UID effettivo 0, o più precisamente con la capability `CAP_SETUID`) può impostare i propri UID a qualunque valore. Con `setuid(n)` li imposta **tutti e tre** a `n`, e perde il privilegio per sempre (è quello che fa `login`);
- un processo **non privilegiato** può impostare il proprio UID effettivo solo a uno dei valori che ha già, cioè al proprio UID **reale** o al proprio UID **salvato**. Non può inventare un UID nuovo.

La seconda regola è quella che rende utile lo UID salvato. Immagina un programma che gira con `ruid=1000` e `euid=suid=0`. Può fare `seteuid(1000)`: ora agisce come l'utente, e se viene ingannato ad aprire un file, il controllo avviene con i permessi dell'utente. Quando gli serve di nuovo il privilegio, fa `seteuid(0)`, permesso perché 0 è ancora nello UID salvato. Se invece vuole rinunciare per sempre, fa `setresuid(1000, 1000, 1000)` e anche la copia di riserva sparisce.

Le chiamate di sistema sono `setuid`, `seteuid`, `setreuid` e `setresuid` (con le corrispondenti per i GID). La loro semantica storica è un groviglio, tanto che nel 2002 Chen, Wagner e Dean hanno scritto un articolo intero, *Setuid Demystified*, per ricostruirla con un modello formale e mostrare quante differenze ci fossero fra un sistema Unix e l'altro. La raccomandazione pratica che ne viene, e che trovi anche nella pagina `credentials(7)`, è: **usare `setresuid` e `setresgid`**, che impostano esplicitamente tutti e tre i valori, e **verificare sempre** il risultato con `getresuid` dopo la chiamata.

### 4.3 Come cambiano le credenziali con `execve`

Normalmente `execve` **non** tocca le credenziali: il nuovo programma gira con la stessa identità del vecchio (L5 §4.2). Le eccezioni sono tre:

1. se il file eseguito ha il bit **setuid** (§9.1), lo UID **effettivo** diventa il proprietario del file;
2. se ha il bit **setgid**, il GID **effettivo** diventa il gruppo del file;
3. se ha delle **file capability** (§12.4), il processo acquista quelle capability.

In tutti i casi lo UID **reale** non cambia: il processo continua a "ricordare" chi l'ha avviato. E in tutti i casi, al termine dell'`execve`, lo UID salvato viene posto uguale al nuovo UID effettivo. Quindi un utente con UID 1000 che esegue `/usr/bin/passwd` (proprietario root, setuid) ottiene un processo con `ruid=1000`, `euid=0`, `suid=0`. Lo puoi vedere direttamente: in un terminale lancia `passwd` e lascialo fermo alla richiesta della password; nell'altro:

```
$ ps -o pid,ruser,euser,suser,comm -C passwd
    PID RUSER    EUSER    SUSER    COMMAND
   3120 zen      root     root     passwd
$ grep Uid /proc/3120/status
Uid:	1000	0	0	0
```

È così che `passwd`, eseguito da te, riesce a scrivere `/etc/shadow`, che tu non puoi neanche leggere. E sapendo che il suo UID reale è il tuo, il programma sa **di chi** cambiare la password: se lanci `passwd anna` senza essere root, `passwd` confronta lo UID reale con quello di `anna` e rifiuta. Tutta la sicurezza dell'operazione dipende dal fatto che `passwd` faccia quel controllo correttamente.

Ci sono anche casi in cui il kernel **rifiuta** di applicare il bit setuid pur trovandolo sul file. I tre principali: il file sta su un file system montato con l'opzione `nosuid`; il processo ha attivato il flag `no_new_privs` (§12.6); il processo è tracciato con `ptrace` da un debugger non privilegiato. L'ultimo caso è importante per le CTF: se avvii un programma setuid dentro `gdb` o `strace` da utente normale, il programma **gira senza privilegi**, altrimenti chiunque potrebbe modificarne la memoria e il comportamento attraverso il debugger. È anche il motivo per cui sui server di pwn.college, quando esegui una sfida con `gdb`, la sfida non riesce a leggere `/flag`.

## 5. Cambiare identità: `su`, `sudo` e affini

### 5.1 `su`

`su` (*substitute user*, spesso letto come "super user") avvia una shell con l'identità di un altro utente, root se non ne specifichi uno. Chiede la **password dell'utente di destinazione** (salvo che tu sia già root). È un programma setuid root: deve poterlo essere, perché per diventare un altro utente serve il privilegio di cambiare UID.

```
$ su prova            # shell come prova, ma ambiente quasi tutto ancora tuo
$ su - prova          # shell di login: ambiente pulito, directory home di prova
$ su -c 'id' prova    # esegue un solo comando
$ su -s /bin/bash www-data -c id    # forza una shell per un utente con nologin (solo da root)
```

La differenza fra `su` e `su -` (o `su -l`) è la stessa fra una shell normale e una di login (L1 §12): con il trattino l'ambiente viene ripulito, `PATH`, `HOME`, `USER` sono quelli del nuovo utente e si leggono i suoi file di profilo. **Senza** il trattino molte variabili restano le tue, compreso a volte il `PATH`. Da root, eseguire un `su` senza trattino verso un utente non fidato è il modo classico per esporsi a un file `~/.bashrc` preparato dall'utente; e viceversa diventare root con `su` senza trattino significa usare come root il `PATH` di un utente normale, che potrebbe contenere directory scrivibili da altri. Regola: **sempre `su -`**.

### 5.2 `sudo`

`sudo` (*superuser do*) rovescia la logica di `su`: chiede la **tua** password, e consulta un file di politica, `/etc/sudoers`, per decidere se puoi eseguire **quel comando** come **quell'utente**. I vantaggi rispetto a `su` sono tre: non serve condividere la password di root; si può concedere solo un sottoinsieme di comandi (minimo privilegio); ogni uso viene registrato nei log, con il nome di chi l'ha fatto (responsabilità).

```
$ sudo id                  # un comando come root
$ sudo -u www-data id      # come un altro utente
$ sudo -i                  # shell di login di root (come su -)
$ sudo -s                  # shell di root, ambiente meno ripulito
$ sudo -l                  # che cosa posso fare? (la domanda più importante)
$ sudo -k                  # dimentica l'autenticazione recente
```

Dopo che hai inserito la password, `sudo` per un certo tempo (15 minuti di default, opzione `timestamp_timeout`) non la richiede più, per quel terminale. Comodo, ma significa anche che un programma lanciato da te in quei minuti può chiamare `sudo` senza che tu te ne accorga.

### 5.3 Il file `sudoers`

Il file si modifica **solo** con `visudo`, che prende un lock e controlla la sintassi prima di salvare: un errore di sintassi in `sudoers` blocca `sudo` per tutti, e se root non ha una password sei chiuso fuori. Le distribuzioni moderne includono la directory `/etc/sudoers.d/`, dove ogni pacchetto o amministratore mette un file separato (`visudo -f /etc/sudoers.d/backup`).

La forma generale di una regola è:

```
CHI   DOVE = (COME_CHI:COME_GRUPPO) [OPZIONI:] COMANDI
```

Esempi letti uno per uno:

```
root    ALL=(ALL:ALL) ALL
%sudo   ALL=(ALL:ALL) ALL
anna    ALL=(root) /usr/bin/systemctl restart nginx
backup  ALL=(root) NOPASSWD: /usr/bin/rsync
web     ALL=(www-data) /usr/bin/php /srv/app/manutenzione.php
Defaults        env_reset
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Defaults        use_pty
```

- `root` può fare tutto, su qualunque macchina (`ALL` prima dell'uguale è il nome dell'host, utile quando lo stesso file è distribuito a molte macchine), come qualunque utente e gruppo.
- `%sudo`: il `%` indica un **gruppo**. Tutti i membri di `sudo` possono fare tutto. È la riga che rende amministratore il primo utente di Ubuntu.
- `anna` può eseguire come root **solo** quel comando con **quegli** argomenti. Se in `sudoers` un comando è scritto con argomenti, solo quegli argomenti sono accettati; se è scritto senza, sono accettati **tutti**; se è seguito da `""`, nessun argomento.
- `backup` può eseguire `rsync` come root **senza password** (`NOPASSWD:`) e con qualunque argomento. Vedremo nel §14.4 perché questa riga è, in pratica, una concessione di root completa.
- `Defaults env_reset` ripulisce l'ambiente prima di eseguire il comando, lasciando solo poche variabili. `secure_path` sostituisce il `PATH` con uno fidato. `use_pty` esegue il comando in un nuovo pseudo-terminale, così un comando in background non può iniettare caratteri nel tuo terminale dopo la fine di `sudo`.

Esistono anche alias (`User_Alias`, `Cmnd_Alias`, `Host_Alias`), negazioni con `!`, e l'opzione `env_keep` che conserva variabili specifiche. Quest'ultima è delicata: `env_keep += "LD_PRELOAD"` o `env_keep += "PYTHONPATH"` permettono a chi lancia `sudo` di iniettare codice nel processo di root (abbiamo visto `LD_PRELOAD` nella Lezione 5, §12.2). Lo stesso vale per l'opzione `SETENV:` su una regola, che consente all'utente di passare variabili arbitrarie.

L'output di `sudo -l` è la prima cosa da guardare, sia in un audit sia in una CTF:

```
$ sudo -l
Matching Defaults entries for anna on server:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User anna may run the following commands on server:
    (root) /usr/bin/systemctl restart nginx
```

### 5.4 Altri meccanismi

- `doas` (da OpenBSD, disponibile anche su Linux) è un'alternativa minimale a `sudo`, con un file di configurazione `/etc/doas.conf` di poche righe. È l'applicazione diretta del principio di economia del meccanismo: `sudo` ha centinaia di migliaia di righe di codice e ha avuto vulnerabilità gravi (ad esempio *Baron Samedit*, CVE-2021-3156, un overflow nel parsing degli argomenti che dava root a qualunque utente locale, anche senza alcuna regola in `sudoers`).
- `pkexec` fa parte di **polkit**, il sistema che gestisce le autorizzazioni dei servizi desktop ("inserisci la password per installare gli aggiornamenti"). Anch'esso è setuid root, e anch'esso ha avuto il suo momento di celebrità con *PwnKit* (CVE-2021-4034), un errore nel trattamento di `argc == 0` presente da dodici anni.
- `newgrp gruppo` avvia una nuova shell con il GID effettivo cambiato in quel gruppo (se ne sei membro, o se conosci la password del gruppo); `sg gruppo -c comando` fa lo stesso per un solo comando. Servono soprattutto dopo essere stati aggiunti a un gruppo, per non dover rifare il login.
- `runuser` è la versione di `su` per root che non passa da PAM: usata negli script di avvio.
- `setpriv` (util-linux) è un coltellino svizzero per lanciare un programma con credenziali, gruppi e capability scelte con precisione; lo useremo nel §12.

La morale comune a tutti questi programmi: sono il **confine** fra un utente e un altro, girano con privilegi e leggono input controllato dall'utente (argomenti, ambiente, file di configurazione). Per questo sono storicamente fra i bersagli preferiti, e per questo un amministratore deve tenerli aggiornati e averne installati il meno possibile.

---

# Parte II — I permessi tradizionali

## 6. Il modello `rwx`

### 6.1 Il campo `mode`

Nell'inode di ogni file c'è un campo di 16 bit chiamato `mode` (lo hai visto nell'output di `stat`, L2 §4.2). I 4 bit alti indicano il **tipo** di file (regolare, directory, link simbolico, dispositivo a caratteri o a blocchi, FIFO, socket). I 12 bit bassi sono i **permessi**, organizzati così:

```
  bit:  11   10    9  |  8 7 6  |  5 4 3  |  2 1 0
        suid sgid stk |  r w x  |  r w x  |  r w x
                      | utente  | gruppo  |  altri
                      | (owner) | (group) | (other)
```

Tre gruppi di tre bit, `r` (*read*, lettura), `w` (*write*, scrittura), `x` (*execute*, esecuzione), per tre **classi** di soggetti: il proprietario del file (*user*, `u`), i membri del gruppo del file (*group*, `g`), tutti gli altri (*other*, `o`). Sopra, i tre bit speciali che vedremo nel §9.

Già da qui si vede la compressione rispetto alla matrice di accesso: per ogni oggetto, invece di una colonna con una cella per ogni utente del sistema, ci sono tre celle. Ci sono cose che questo modello **non può esprimere**: per esempio "anna può leggere, bruno può scrivere, carla niente, tutti gli altri leggono" richiede almeno quattro classi. Quando servono, si usano le ACL (§10).

### 6.2 L'algoritmo di controllo

Quando un processo chiede di aprire un file, il kernel esegue un algoritmo preciso. È fondamentale impararlo **esattamente**, perché il suo comportamento in un caso particolare sorprende quasi tutti.

1. Se il processo ha UID effettivo 0 (più precisamente, le capability `CAP_DAC_OVERRIDE` o `CAP_DAC_READ_SEARCH`, §12), l'accesso in lettura e scrittura è **concesso** senza guardare i bit. Per l'esecuzione serve comunque almeno un bit `x` (§2.3).
2. Altrimenti, se l'UID effettivo del processo è uguale all'UID proprietario del file, si usano **i bit del proprietario**, e solo quelli.
3. Altrimenti, se il GID effettivo del processo o uno dei suoi gruppi supplementari è uguale al GID del file, si usano **i bit del gruppo**, e solo quelli.
4. Altrimenti si usano **i bit degli altri**.

L'accesso è concesso se, nella classe scelta, sono attivi **tutti** i bit richiesti dall'operazione (per un'apertura in lettura e scrittura servono sia `r` sia `w`).

La parola importante è "solo". Le classi non si sommano e **non c'è ricaduta**: se sei il proprietario, contano i bit del proprietario anche se quelli del gruppo o degli altri sarebbero più generosi. Prova:

```
$ echo segreto > f
$ chmod 047 f          # proprietario ---, gruppo r--, altri rwx
$ ls -l f
----r--rwx 1 zen zen 8 nov  7 20:01 f
$ cat f
cat: f: Permission denied
```

Tutti gli utenti della macchina possono leggere e scrivere `f`, tranne il suo proprietario. Il modello è strano ma coerente: l'algoritmo trova la prima classe che si applica a te e si ferma. Questo ha un'applicazione pratica, la **lista nera**: con `chmod 705 f` e il gruppo del file impostato a `stagisti`, tutti possono leggere `f` tranne i membri di `stagisti`. In pratica la si usa poco, perché è fragile (basta copiare il file per aggirarla, e chi è nel gruppo può comunque leggere una copia fatta da altri), ma all'esame si chiede spesso.

Naturalmente il proprietario, anche con permessi `000`, può sempre **ridarsi** i permessi con `chmod`, perché cambiare i permessi non richiede alcun permesso sul file: richiede solo di esserne il proprietario. Il primo pezzo della sfida di oggi gioca proprio su questo.

### 6.3 Che cosa significano `r`, `w`, `x` su un file

Su un **file regolare** il significato è quello intuitivo:

- `r`: si può aprire il file in lettura (`open` con `O_RDONLY`), quindi leggerne il contenuto, copiarlo, mapparlo in memoria;
- `w`: si può aprire in scrittura, quindi modificarlo, troncarlo (`> file` lo svuota), aggiungervi in coda;
- `x`: si può chiederne l'esecuzione con `execve`.

Tre conseguenze da sapere.

- **`w` non basta per cancellare**, e non serve: la cancellazione dipende dalla directory (§6.4). Con `w` sul file puoi però svuotarlo completamente con `: > file`, che per molti scopi è come cancellarlo.
- **`x` su uno script non basta**. Per eseguire un programma binario il kernel legge il file da sé, quindi basta `x` (un binario `--x--x--x` è eseguibile da tutti, ma nessuno può copiarlo: è un modo, debole, di proteggere un binario dalla lettura). Per uno **script**, invece, il kernel legge la riga `#!` e avvia l'interprete passandogli il **percorso** del file; l'interprete, che gira con la tua identità, deve poi **aprire e leggere** lo script. Quindi uno script richiede sia `r` sia `x`. Uno script `--x` fallisce con `Permission denied` detto dall'interprete; uno script `r--` si può comunque eseguire con `bash script.sh`, perché in quel caso è bash a essere eseguito e lo script è solo un file di dati.
- **`x` senza `r` non protegge un segreto in un binario** da un utente determinato: il processo che ne risulta è tuo, e lo puoi leggere da `/proc/<PID>/mem` o con un debugger se le politiche di `ptrace` lo consentono (L5 §13.2). Su Linux, per questo motivo, il kernel marca come non scaricabile in memoria (*non-dumpable*) un processo il cui eseguibile non è leggibile.

### 6.4 Che cosa significano `r`, `w`, `x` su una directory

Qui l'intuizione inganna, e serve ripartire dalla Lezione 2: una directory è un file speciale che contiene una **tabella di voci** (nome → numero di inode). I tre bit si riferiscono a operazioni su quella tabella.

- `r`: si può **leggere la tabella**, cioè elencare i nomi (`ls`, i glob `*` della shell). Solo i nomi: per sapere tipo, dimensione, proprietario di ogni voce bisogna raggiungerne l'inode, e per quello serve `x`.
- `x`: si può **attraversare** la directory (*search permission*), cioè usarla come tappa di un percorso: accedere a `dir/file` sapendone il nome, fare `cd dir`, fare `stat` su una voce. Senza `x` su una directory, nulla al suo interno è raggiungibile, qualunque siano i permessi dei file.
- `w`: si può **modificare la tabella**, cioè creare, cancellare, rinominare voci. Ma per modificare la tabella bisogna anche poterla attraversare, quindi in pratica `w` serve solo **insieme a `x`**.

Le combinazioni che contano:

| Permessi | `ls dir` | `ls -l dir` | `cat dir/f` (se conosci il nome) | `touch dir/nuovo`, `rm dir/f` |
|---|---|---|---|---|
| `r--` | elenca i nomi, con errori | nomi con `?????????` | no | no |
| `--x` | no | no | **sì** (se `f` lo permette) | no |
| `r-x` | sì | sì | sì | no |
| `-wx` | no | no | sì | **sì** |
| `rw-` | nomi, con errori | `?????????` | no | **no** |
| `rwx` | sì | sì | sì | sì |

Due righe meritano un commento.

La riga `--x` è la base della "directory segreta": una directory che si può attraversare ma non elencare. Se il nome di un file al suo interno è difficile da indovinare, solo chi lo conosce lo raggiunge. Le home directory sono spesso `drwx--x--x`, così che il server web possa raggiungere `~/public_html` senza che gli altri utenti possano elencare il resto della home. È una forma di sicurezza basata sulla segretezza di un nome, quindi debole, ma in combinazione con nomi casuali lunghi funziona.

La riga `-wx` contiene la conseguenza che avevamo annunciato nella Lezione 2: **chi ha `w` e `x` su una directory può cancellare qualunque file al suo interno, anche se il file è di root e ha permessi `000`**. La cancellazione è un'operazione sulla directory, non sul file. Lo stesso vale per la rinomina, e quindi per la **sostituzione**: chi può scrivere nella directory può cancellare un file e crearne un altro con lo stesso nome e un contenuto diverso. Se quel file è uno script eseguito da root (un lavoro di `cron`, uno script di avvio), la directory scrivibile equivale a un accesso di root (§14.3). L'unica eccezione a questa regola è lo **sticky bit** (§9.4), inventato apposta per `/tmp`.

```
$ mkdir d; echo dati > d/f; chmod 000 d/f; chmod 300 d     # d: -wx------
$ ls d
ls: cannot open directory 'd': Permission denied
$ rm -f d/f && echo cancellato
cancellato
```

### 6.5 Il percorso intero

Il controllo non riguarda solo l'ultimo componente del percorso. Per aprire `/home/anna/progetti/relazione.txt` il kernel deve attraversare `/`, `home`, `anna`, `progetti`, e su **ognuna** di queste directory serve il permesso `x` per la tua classe. Basta che una sola manchi perché il file sia irraggiungibile, qualunque siano i suoi permessi. È per questo che rendere privata una home con `chmod 700 ~` protegge in un colpo solo tutti i file al suo interno, anche quelli con permessi `644`.

Il rovescio della medaglia è il caso del descrittore e del link fisico. Se un file `644` sta in una directory `700`, chi ha già un descrittore aperto continua a leggerlo; e se qualcuno ne ha fatto un link fisico in una directory accessibile, il file è raggiungibile da quell'altro percorso (§9.5 per la protezione del kernel contro questo caso).

Quando un accesso fallisce e non capisci perché, `namei -l` mostra i permessi di ogni componente:

```
$ namei -l /home/anna/progetti/relazione.txt
f: /home/anna/progetti/relazione.txt
drwxr-xr-x root root /
drwxr-xr-x root root home
drwx------ anna anna anna
                     progetti - Permission denied
```

### 6.6 Chi può cambiare che cosa

Le operazioni sui metadati hanno regole proprie, che non dipendono dai bit `rwx` del file:

- **`chmod`** (cambiare i permessi): solo il **proprietario** del file o root.
- **`chown`** (cambiare il proprietario): **solo root** (precisamente: chi ha `CAP_CHOWN`). Su Linux un utente non può "regalare" un proprio file a un altro. Il motivo è storico e di sicurezza: se potessi regalare file, potresti aggirare le quote disco (i file contano per il proprietario) e, peggio, regalare un programma setuid. Alcuni vecchi Unix System V lo permettevano, e azzeravano i bit setuid per limitare il danno.
- **`chgrp`** (cambiare il gruppo): il proprietario può assegnare il file a **uno dei gruppi a cui appartiene**; root a qualunque gruppo.
- **`touch`** per impostare un orario arbitrario: il proprietario; per impostare l'orario attuale basta il permesso di scrittura.

`chown` e `chgrp` hanno un effetto collaterale che vedremo nel §9: azzerano i bit setuid e setgid.

## 7. Leggere e scrivere i permessi

### 7.1 La stringa di `ls -l`

```
-rwxr-x--- 1 anna team 16712 nov  7 20:15 analisi
│└┬┘└┬┘└┬┘ │  │    │
│ │  │  │  │  │    └ gruppo del file
│ │  │  │  │  └ proprietario
│ │  │  │  └ numero di link fisici
│ │  │  └ altri: nessun permesso
│ │  └ gruppo: lettura ed esecuzione
│ └ proprietario: lettura, scrittura, esecuzione
└ tipo: - file, d directory, l link simbolico, c/b dispositivo, p FIFO, s socket
```

Dopo i dieci caratteri può comparire un undicesimo: `.` indica un contesto SELinux, `+` indica che il file ha una **ACL** (§10). Vedere un `+` e ignorarlo è un errore classico: i bit visibili non raccontano più tutta la storia.

Per i **link simbolici** `ls -l` mostra sempre `lrwxrwxrwx`: i permessi di un link simbolico non sono usati da Linux, contano quelli del file a cui punta.

### 7.2 La notazione ottale

Ogni gruppo di tre bit è un numero da 0 a 7, con pesi `r` = 4, `w` = 2, `x` = 1. Quindi tre cifre ottali descrivono i nove bit, e una quarta cifra, davanti, i bit speciali (setuid = 4, setgid = 2, sticky = 1).

| Ottale | Binario | Simbolico | Uso tipico |
|---|---|---|---|
| 0 | 000 | `---` | |
| 1 | 001 | `--x` | directory attraversabile ma non elencabile |
| 2 | 010 | `-w-` | raro |
| 3 | 011 | `-wx` | directory "cassetta delle lettere" (si depositano file senza vedere gli altri) |
| 4 | 100 | `r--` | file in sola lettura |
| 5 | 101 | `r-x` | programmi, directory leggibili |
| 6 | 110 | `rw-` | file di dati |
| 7 | 111 | `rwx` | tutto |

Combinazioni da riconoscere a colpo d'occhio:

| Modo | Stringa | Dove lo trovi |
|---|---|---|
| `644` | `rw-r--r--` | file normali, `/etc/passwd` |
| `640` | `rw-r-----` | `/etc/shadow` (gruppo `shadow`), configurazioni con segreti |
| `600` | `rw-------` | chiavi private SSH, `~/.ssh/authorized_keys` |
| `755` | `rwxr-xr-x` | programmi, directory |
| `700` | `rwx------` | home private, `~/.ssh` |
| `750` | `rwxr-x---` | directory di un gruppo di lavoro |
| `1777` | `rwxrwxrwt` | `/tmp`, `/var/tmp`, `/dev/shm` |
| `4755` | `rwsr-xr-x` | programmi setuid (`passwd`, `sudo`) |
| `2775` | `rwxrwsr-x` | directory condivise con setgid |
| `777` | `rwxrwxrwx` | quasi sempre un errore |

`stat` mostra le due forme insieme, ed è il modo più rapido per passare dall'una all'altra:

```
$ stat -c '%a %A %U:%G %n' /etc/passwd /etc/shadow /tmp /usr/bin/passwd
644 -rw-r--r-- root:root /etc/passwd
640 -rw-r----- root:shadow /etc/shadow
1777 drwxrwxrwt root:root /tmp
4755 -rwsr-xr-x root:root /usr/bin/passwd
```

Il motivo profondo per cui si usa l'ottale e non l'esadecimale è che i permessi sono raggruppati a tre bit, e una cifra ottale è esattamente tre bit. Nella Lezione 7 vedremo le basi numeriche in modo sistematico; per ora basta saper convertire una cifra alla volta.

### 7.3 `chmod`

`chmod` accetta due sintassi.

La **sintassi ottale** imposta **tutti** i permessi in un colpo, sostituendo quelli precedenti:

```
$ chmod 640 rapporto.txt
$ chmod 0755 script.sh       # lo 0 iniziale = nessun bit speciale
$ chmod 4755 programma       # setuid
```

Attenzione a un dettaglio di GNU `chmod`: sulle **directory** una modalità ottale a tre o quattro cifre **non azzera** i bit setuid e setgid esistenti (per non rompere le directory condivise per sbaglio); per toglierli serve la forma simbolica (`chmod g-s dir`) o cinque cifre (`chmod 00755 dir`).

La **sintassi simbolica** modifica solo ciò che indichi. La forma è `[chi][operatore][permessi]`, dove *chi* è una combinazione di `u`, `g`, `o`, `a` (tutti), l'operatore è `+` (aggiungi), `-` (togli), `=` (imposta esattamente), e i permessi sono `r`, `w`, `x`, `X`, `s`, `t`, oppure `u`, `g`, `o` per copiare i permessi di un'altra classe.

```
$ chmod u+x script.sh              # aggiungi esecuzione al proprietario
$ chmod go-w file                  # togli scrittura a gruppo e altri
$ chmod a=r file                   # tutti solo lettura (= 444)
$ chmod u=rwx,g=rx,o= dir          # 750, più leggibile
$ chmod g=u file                   # il gruppo riceve gli stessi permessi del proprietario
$ chmod +x script.sh               # senza "chi": come a+x, ma filtrato dalla umask!
$ chmod -R u+rwX,go-rwx progetto/  # vedi sotto
```

Due finezze.

- Se ometti *chi* (`chmod +x`), il risultato è come `a+x` ma **senza** i bit che la umask (§8) escluderebbe. Con umask `077`, `chmod +w file` aggiunge `w` solo al proprietario. Per evitare sorprese negli script, specifica sempre `u`, `g`, `o` o `a`.
- La `X` maiuscola significa "esecuzione, ma solo se il file è una directory o se ha già almeno un bit `x`". Serve nel caso più comune di `chmod -R`: vuoi rendere attraversabili tutte le directory di un albero, senza rendere eseguibili tutti i file di dati. `chmod -R a+x` farebbe diventare eseguibili anche le foto; `chmod -R a+X` no.

Per applicare permessi diversi a file e directory di un albero, il modo più preciso è `find` (L2 §11):

```
$ find progetto -type d -exec chmod 750 {} +
$ find progetto -type f -exec chmod 640 {} +
```

### 7.4 `chown` e `chgrp`

```
$ sudo chown anna file                 # cambia proprietario
$ sudo chown anna:team file            # proprietario e gruppo
$ sudo chown :team file                # solo il gruppo (come chgrp)
$ chgrp team file                      # da proprietario, se sei in team
$ sudo chown -R www-data:www-data /srv/sito
$ sudo chown --reference=modello file  # copia proprietario e gruppo da un altro file
```

Due trappole di `chown -R`. La prima: per default **non** segue i link simbolici incontrati nell'albero, ma se un link è passato **sulla riga di comando** cambia il file a cui punta. La seconda, più grave: se un utente controlla una directory che root sta per sottoporre a `chown -R`, può inserirvi un link fisico a un file di sistema (se le protezioni del §9.5 non sono attive) e farselo regalare. Per questo `chown -R` eseguito da root su directory di utenti non fidati è un'operazione da fare con attenzione.

### 7.5 La copia, lo spostamento, gli archivi

Che fine fanno i permessi quando copi o sposti un file?

- `mv` all'interno dello stesso file system rinomina soltanto: lo stesso inode, gli stessi permessi, lo stesso proprietario.
- `cp` crea un **nuovo** file, di proprietà di **chi copia**, con i permessi del sorgente filtrati dalla umask e **senza** i bit setuid e setgid (GNU `cp` li toglie sempre, a meno di `-p`). Con `cp -p` (o `cp -a`) si tenta di conservare permessi, proprietario e orari, ma conservare il proprietario riesce solo a root.
- `tar` salva permessi e proprietari nell'archivio. All'estrazione, un utente normale ottiene file propri con i permessi registrati meno la umask; **root** invece ripristina anche i proprietari e i bit speciali (`--same-owner` e `-p` sono il default per root). Estrarre da root un archivio non fidato può quindi creare programmi setuid sulla macchina: un motivo in più per estrarre da utente normale.

Il caso di `cp` merita un esperimento, perché è alla base del primo pezzo della sfida: se puoi **leggere** un file di un altro, puoi copiarlo, e la copia è **tua**, con tutto ciò che ne consegue. Il permesso di lettura è, di fatto, il permesso di fare una copia che il proprietario originale non controlla più.

## 8. La `umask`

### 8.1 Il problema

Quando un programma crea un file, chiama `open(percorso, O_CREAT | ..., modo)` o `mkdir(percorso, modo)`, e il terzo argomento indica i permessi **richiesti**. Quasi tutti i programmi chiedono il massimo ragionevole: `0666` per i file (lettura e scrittura a tutti; l'esecuzione non si chiede, perché un file di dati non deve essere eseguibile) e `0777` per le directory. Sarebbe una pessima impostazione predefinita, contraria al principio dei *fail-safe defaults*. Il correttivo è la **umask** (*user file-creation mode mask*): una maschera, proprietà di ogni processo ed ereditata dai figli (L5 §12.1), che elenca i bit da **togliere** a ogni file creato.

```
permessi finali = permessi richiesti AND (NOT umask)
```

### 8.2 Il calcolo

La formula usa un AND bit a bit, **non** una sottrazione. Per i casi comuni il risultato coincide, ed è per questo che molti la imparano come sottrazione e poi sbagliano nei casi limite.

| umask | file (da 666) | directory (da 777) | Significato |
|---|---|---|---|
| `022` | `644` `rw-r--r--` | `755` `rwxr-xr-x` | default classico: tutti leggono, solo io scrivo |
| `002` | `664` `rw-rw-r--` | `775` `rwxrwxr-x` | default con gruppi privati (UPG): il gruppo scrive |
| `027` | `640` `rw-r-----` | `750` `rwxr-x---` | il gruppo legge, gli altri niente |
| `077` | `600` `rw-------` | `700` `rwx------` | solo io: per server e utenti attenti alla riservatezza |
| `033` | `644` | `744` | qui la sottrazione darebbe `633` per i file, che è **sbagliato** |

Prendiamo l'ultima riga e facciamo il conto bit per bit, sul gruppo:

```
richiesto (6)   1 1 0      rw-
umask (3)       0 1 1      -wx
NOT umask       1 0 0      r--
AND             1 0 0      r--   → 4, non 6-3 = 3
```

La umask toglie solo i bit che ci sono; non può togliere `x` a un file che non l'ha mai chiesto. La sottrazione darebbe `3` (`-wx`), aggiungendo un permesso di esecuzione che nessuno ha richiesto.

Due conseguenze della formula:

- la umask può solo **togliere**: se un programma chiede `0600` (come fa `ssh-keygen` per la chiave privata), con umask `000` il file resta `600`;
- il programma può sempre cambiare i permessi **dopo** la creazione con `chmod`, e la umask non c'entra più. La umask regola solo il momento della nascita.

### 8.3 Leggerla e impostarla

```
$ umask
0022
$ umask -S
u=rwx,g=rx,o=rx
$ umask 077          # da ora, in questa shell e nei suoi figli
$ touch nuovo; mkdir nuovadir; ls -ld nuovo nuovadir
-rw------- 1 zen zen    0 nov  7 20:31 nuovo
drwx------ 2 zen zen 4096 nov  7 20:31 nuovadir
$ ( umask 002; touch condiviso )     # solo nella subshell
$ grep Umask /proc/$$/status
Umask:	0077
```

`umask -S` mostra i permessi **lasciati**, non quelli tolti: è il complemento. La umask è un builtin, perché deve cambiare la umask della shell stessa (un programma esterno cambierebbe solo la propria, L1 §8).

L'impostazione predefinita viene da più posti, nell'ordine in cui vengono applicati al login: il valore `UMASK` di `/etc/login.defs` (applicato da `pam_umask` o da `login`), poi `/etc/profile`, poi `~/.profile` o `~/.bashrc`. Per i **servizi** avviati da systemd la umask si imposta nel file di unità con `UMask=0027`; per default è `0022`.

### 8.4 Perché importa per la sicurezza

Un servizio che scrive file di log, file temporanei o file caricati dagli utenti con umask `000` produce file scrivibili da chiunque sulla macchina. Un utente che lavora con umask `002` in una directory condivisa con gruppo `users` (a cui appartengono tutti) rende scrivibili a tutti i suoi file. Uno script di backup che crea l'archivio con umask `022` crea un archivio **leggibile da tutti** che contiene, magari, una copia di `/etc/shadow`. In tutti questi casi nessuno ha fatto un `chmod` sbagliato: il problema è nato alla creazione. È la classe di errori CWE-276 (*Incorrect Default Permissions*), e in un audit si trova cercando i file appena creati con permessi larghi (§15).

C'è poi una finestra temporale da conoscere. Uno script che fa

```
echo "$PASSWORD" > /etc/app/segreto
chmod 600 /etc/app/segreto
```

con umask `022` crea per un istante un file `644`. Un processo che in quell'istante lo apre in lettura ottiene un descrittore, e lo conserva anche dopo il `chmod` (§1.1). La forma corretta imposta la umask **prima**:

```
( umask 077; echo "$PASSWORD" > /etc/app/segreto )
```

oppure usa `install -m 600 /dev/null /etc/app/segreto` per creare il file vuoto con i permessi giusti e poi scriverci.

## 9. I bit speciali: setuid, setgid, sticky

### 9.1 Setuid

Torniamo al problema di `passwd`. Un utente deve poter cambiare la propria password, che sta in `/etc/shadow`, un file che non può neppure leggere. Le soluzioni possibili erano due: un servizio sempre attivo, di root, a cui chiedere il cambio (oggi si fa così per molte cose); oppure un modo per far girare un programma con i privilegi del **suo proprietario** invece che di chi lo lancia. Dennis Ritchie scelse la seconda e la brevettò nel 1979 (US 4.135.240, *Protection of data file contents*): è il bit **set-user-ID**, o **setuid**.

Se un file eseguibile ha il bit setuid, l'`execve` imposta lo UID **effettivo** del processo al proprietario del file (§4.3). In `ls -l` il bit compare al posto della `x` del proprietario:

- `s` minuscola: setuid **e** esecuzione per il proprietario (`rwsr-xr-x`, 4755);
- `S` maiuscola: setuid **senza** esecuzione per il proprietario (`rwSr--r--`, 4644). È quasi sempre un errore: il bit è lì ma non serve a niente (o serve agli altri, se hanno `x`).

```
$ ls -l /usr/bin/passwd /usr/bin/sudo /usr/bin/su /usr/bin/mount
-rwsr-xr-x 1 root root  64152 mag 30  2024 /usr/bin/passwd
-rwsr-xr-x 1 root root 282032 ott  6 13:51 /usr/bin/sudo
-rwsr-xr-x 1 root root  55680 ago 19 16:47 /usr/bin/su
-rwsr-xr-x 1 root root  51600 apr  9  2024 /usr/bin/mount
```

Il setuid non riguarda solo root: un programma setuid di proprietà di `games` gira come `games` (si usava per far scrivere a tutti i giocatori la tabella dei punteggi, scrivibile solo da `games`). Ma il caso che conta è quello di root, perché un programma **setuid root** è un pezzo di codice che chiunque può avviare e che gira con i pieni poteri. Ogni suo errore è un errore di root. Per questo:

- deve fidarsi il meno possibile dell'ambiente che riceve (variabili, argomenti, descrittori aperti, directory corrente, umask, limiti, segnali ignorati: tutto ciò che passa attraverso `execve`, L5 §12.1, è controllato dall'utente che lo lancia);
- il linker dinamico, quando avvia un programma setuid, entra in **modalità sicura** (*secure-execution mode*, segnalata dal valore `AT_SECURE` nel vettore ausiliario, L5 §12.3): ignora `LD_PRELOAD` e `LD_LIBRARY_PATH` (salvo librerie in percorsi di sistema a loro volta setuid) e varie altre variabili. Senza questa regola, bastarebbe `LD_PRELOAD=./mia.so passwd` per eseguire codice come root;
- non deve mai chiamare altri programmi per nome affidandosi al `PATH` (§14.2).

Il bit setuid si attiva con `chmod u+s` o con la cifra 4 davanti all'ottale. Un utente normale può attivarlo **solo sui propri file**: un programma setuid tuo gira come te, quindi non ti dà niente di nuovo (lo può dare agli **altri**, che lanciandolo agiscono come te: un modo per condividere un accesso, e un rischio se il programma è scritto male).

### 9.2 Quando il setuid viene ignorato o tolto

Il kernel ignora o rimuove il bit in diversi casi, tutti pensati per chiudere una scappatoia.

- **Script**: Linux **ignora** il setuid sugli script con `#!`. Il motivo è una race condition storica: il kernel apre lo script per leggere la riga `#!`, poi l'interprete lo riapre per nome; nel frattempo un attaccante può sostituire il file (o il link simbolico con cui è stato invocato) con un altro script, che verrebbe eseguito con i privilegi. Alcuni Unix risolvono con `/dev/fd/N`; Linux ha scelto di non supportare affatto gli script setuid. Se vuoi che uno script giri come root, lo si mette in `sudoers` o si scrive un piccolo programma C che lo lancia con un ambiente controllato.
- **Scrittura**: quando un utente non privilegiato **scrive** su un file setuid o setgid, il kernel azzera quei bit. Altrimenti chi può scrivere su un programma setuid altrui potrebbe sostituirne il codice mantenendo i privilegi.
- **Cambio di proprietario**: `chown` e `chgrp` azzerano setuid e setgid (anche se eseguiti da root, per i file eseguibili). Un file setuid di `anna` regalato a root non deve diventare setuid root.
- **`nosuid`**: su un file system montato con questa opzione i bit setuid e setgid sono ignorati. Si usa per le chiavette USB, le partizioni `/tmp`, `/home`, `/var/tmp`, le condivisioni di rete: posti dove un utente potrebbe portare un programma setuid preparato su un'altra macchina (dove era root).
- **Debugger e `no_new_privs`**: visti nel §4.3.

Puoi verificare i primi tre in pochi secondi:

```
$ cp /bin/true t; chmod 4755 t; ls -l t
-rwsr-xr-x 1 zen zen 26936 nov  7 20:40 t
$ echo >> t; ls -l t                       # scrittura: bit azzerato
-rwxr-xr-x 1 zen zen 26937 nov  7 20:40 t
$ printf '#!/bin/sh\nid -u\n' > s.sh; sudo chown root s.sh; sudo chmod 4755 s.sh
$ ./s.sh                                    # stampa il TUO uid, non 0
1000
```

### 9.3 Setgid su file e su directory

Il bit **set-group-ID** (cifra 2, `s` al posto della `x` del gruppo) ha due significati completamente diversi.

**Su un file eseguibile** è l'analogo del setuid per il gruppo: il processo prende come GID effettivo il gruppo del file. Esempi tipici: programmi che devono leggere un file di un gruppo specifico. Su Debian, `/usr/bin/chage` e `/usr/bin/expiry` sono setgid `shadow` (devono leggere `/etc/shadow` ma non scriverlo); `ssh-agent` e `crontab` possono essere setgid su certe distribuzioni. Il setgid è un privilegio minore del setuid root, ma non trascurabile: un programma setgid `shadow` con un errore permette di leggere gli hash di tutti.

**Su una directory** cambia il gruppo dei file creati al suo interno: invece del gruppo primario di chi crea il file, prendono il **gruppo della directory**. E le sottodirectory create al suo interno ereditano anche il bit setgid stesso. È il meccanismo con cui si costruiscono le cartelle di lavoro condivise:

```
$ sudo mkdir /srv/progetto
$ sudo chgrp team /srv/progetto
$ sudo chmod 2770 /srv/progetto            # rwxrws---
$ touch /srv/progetto/a; mkdir /srv/progetto/d
$ ls -l /srv/progetto
-rw-rw-r-- 1 zen team    0 nov  7 20:45 a
drwxrwsr-x 2 zen team 4096 nov  7 20:45 d
```

Senza il setgid, il file `a` sarebbe stato del gruppo `zen` e gli altri membri del team non avrebbero potuto modificarlo. Con il setgid e una umask `002`, tutto ciò che ognuno crea è automaticamente leggibile e scrivibile dal team. È il motivo per cui le distribuzioni con gruppi privati per ogni utente usano `002` come umask predefinita: il gruppo privato non contiene nessun altro, quindi `002` non espone niente, ma nelle directory setgid permette la collaborazione.

Una nota storica: su vecchi sistemi un file con setgid ma **senza** `x` per il gruppo (`S` maiuscola, ad esempio `2644`) indicava il *mandatory locking*. Linux ha rimosso il supporto nel 2021 (kernel 5.15); se lo vedi, è un residuo.

### 9.4 Lo sticky bit

Il terzo bit speciale (cifra 1, `t` al posto della `x` degli altri; `T` maiuscola se gli altri non hanno `x`) ha anch'esso una storia doppia. In origine, sui file eseguibili, chiedeva al kernel di tenere il programma in memoria di *swap* dopo la fine ("appiccicoso", *sticky*) per riavviarlo più in fretta. Su Linux non ha alcun effetto sui file.

Oggi conta **solo sulle directory**, e risolve il problema del §6.4: in una directory scrivibile da tutti, chiunque potrebbe cancellare o rinominare i file degli altri. Con lo sticky bit, un file può essere cancellato o rinominato **solo** dal proprietario del file, dal proprietario della directory o da root. È esattamente la configurazione di `/tmp`:

```
$ ls -ld /tmp /var/tmp /dev/shm
drwxrwxrwt 18 root root  4096 nov  7 20:50 /tmp
drwxrwxrwt  7 root root  4096 nov  7 19:02 /var/tmp
drwxrwxrwt  2 root root    60 nov  7 19:02 /dev/shm
```

Con un secondo utente puoi verificare:

```
anna$ echo ciao > /tmp/di_anna; chmod 666 /tmp/di_anna
zen$  rm -f /tmp/di_anna
rm: cannot remove '/tmp/di_anna': Operation not permitted
zen$  echo aggiunta >> /tmp/di_anna && echo scritto
scritto
```

Lo sticky bit protegge il **nome**, non il **contenuto**: `zen` non può cancellare il file, ma i suoi permessi `666` gli consentono di scriverci. Il messaggio è diverso, e la differenza è istruttiva: `Operation not permitted` (`EPERM`) indica una regola di politica come lo sticky bit; `Permission denied` (`EACCES`) indica un controllo sui bit `rwx` fallito.

Una directory scrivibile da tutti **senza** sticky bit (`drwxrwxrwx`) è una delle configurazioni da cercare in un audit: chiunque può sostituire i file che contiene.

### 9.5 Le protezioni del kernel per le directory condivise

Le directory come `/tmp` sono pericolose per un motivo più sottile: sono un posto dove un utente può **preparare** dei nomi prima che un altro (spesso root) li usi. Gli attacchi classici sono tre, e Linux ha aggiunto, nel tempo, tre protezioni regolate da `sysctl`:

```
$ sysctl fs.protected_symlinks fs.protected_hardlinks fs.protected_regular fs.protected_fifos
fs.protected_symlinks = 1
fs.protected_hardlinks = 1
fs.protected_regular = 2
fs.protected_fifos = 1
# valori tipici di Ubuntu; il default del kernel per le ultime due è 0, systemd imposta 1
```

- **Link simbolici** (`protected_symlinks`): l'attaccante crea `/tmp/report.txt` come link simbolico a `/etc/shadow`; uno script di root scrive in `/tmp/report.txt` e così sovrascrive `/etc/shadow`. Con la protezione attiva, in una directory sticky e scrivibile da tutti, un link simbolico viene seguito solo se il suo proprietario è quello che lo segue o coincide con il proprietario della directory.
- **Link fisici** (`protected_hardlinks`): l'attaccante crea un link fisico a un file setuid root vulnerabile, per conservarlo anche dopo che l'amministratore ha aggiornato il pacchetto (l'aggiornamento crea un nuovo inode, il vecchio sopravvive finché ha nomi); oppure a un file che root modificherà. Con la protezione, un utente può creare un link fisico solo a file suoi, o a file che può leggere e scrivere e che non sono setuid o setgid eseguibili.
- **File e FIFO preesistenti** (`protected_regular`, `protected_fifos`): l'attaccante crea in anticipo `/tmp/lavoro.log`, di sua proprietà; uno script di root lo apre con `O_CREAT` senza `O_EXCL`, pensando di crearlo, e invece scrive in un file controllato dall'attaccante. Con la protezione, in una directory sticky, l'apertura con `O_CREAT` di un file esistente che appartiene a un altro utente viene rifiutata.

Queste protezioni sono un ottimo esempio di **difesa in profondità**: non correggono i programmi difettosi, ma rendono innocui molti difetti. La correzione vera resta scrivere bene: creare i file temporanei con `mktemp` (che usa `O_CREAT | O_EXCL` e un nome casuale), mai con un nome fisso in `/tmp`. Su alcuni ambienti (container, sistemi minimali) queste protezioni possono essere disattivate: controllale.

### 9.6 Riepilogo dei bit speciali

| Bit | Ottale | `ls` | Su un file eseguibile | Su una directory |
|---|---|---|---|---|
| setuid | 4000 | `s`/`S` nella `x` del proprietario | euid = proprietario del file | nessun effetto su Linux |
| setgid | 2000 | `s`/`S` nella `x` del gruppo | egid = gruppo del file | i nuovi file prendono il gruppo della directory; le nuove directory ereditano il bit |
| sticky | 1000 | `t`/`T` nella `x` degli altri | nessun effetto su Linux | solo il proprietario del file (o della directory, o root) può cancellare o rinominare |

Per trovarli con `find`, il predicato `-perm` ha tre forme (L2 §11.3) che qui diventano indispensabili:

```
$ find /usr/bin -perm -4000          # -: TUTTI i bit indicati sono attivi (setuid, qualunque resto)
$ find /usr/bin -perm /6000          # /: ALMENO UNO dei bit indicati (setuid o setgid)
$ find . -perm 644                   # senza prefisso: esattamente 644
$ find / -xdev -type d -perm -0002 ! -perm -1000    # directory scrivibili da tutti senza sticky
```

---

# Parte III — Oltre `rwx`

## 10. Le ACL POSIX

### 10.1 Il limite delle tre classi

Il modello del §6 non sa dire "anna legge, bruno legge e scrive, gli altri del gruppo no". Le **ACL** (*Access Control List*) POSIX estendono il modello aggiungendo a un file un elenco di voci per **utenti e gruppi specifici**. Furono definite in una bozza di standard (POSIX 1003.1e, mai approvata e ritirata nel 1997) che tutti però hanno implementato; su Linux sono memorizzate negli **attributi estesi** del file (`system.posix_acl_access`) e funzionano su ext4, XFS, Btrfs e quasi tutti i file system moderni. Gli strumenti stanno nel pacchetto `acl` (`sudo apt install acl`).

### 10.2 Leggere e scrivere un'ACL

```
$ touch piano.txt
$ setfacl -m u:anna:r piano.txt         # -m: modifica; anna può leggere
$ setfacl -m u:bruno:rw piano.txt
$ setfacl -m g:revisori:r piano.txt
$ ls -l piano.txt
-rw-rw-r--+ 1 zen zen 0 nov  7 21:00 piano.txt
$ getfacl piano.txt
# file: piano.txt
# owner: zen
# group: zen
user::rw-
user:anna:r--
user:bruno:rw-
group::r--
group:revisori:r--
mask::rw-
other::r--
```

Le voci sono di sei tipi: `user::` (il proprietario, corrisponde ai bit `u`), `user:nome:` (un utente specifico), `group::` (il gruppo del file), `group:nome:` (un gruppo specifico), `mask::` (vedi sotto), `other::` (corrisponde ai bit `o`). Il `+` in fondo alla stringa di `ls -l` avverte che l'ACL c'è.

Altri comandi utili:

```
$ setfacl -x u:bruno piano.txt          # toglie una voce
$ setfacl -b piano.txt                  # toglie tutta l'ACL estesa
$ setfacl -R -m g:team:rwX progetto/    # ricorsivo, con la X del §7.3
$ getfacl -R progetto > acl.bak         # salva
$ setfacl --restore=acl.bak             # ripristina
```

### 10.3 La maschera e l'algoritmo esteso

Con un'ACL l'algoritmo del §6.2 diventa:

1. se sei il proprietario, contano i permessi `user::`;
2. altrimenti, se c'è una voce `user:tu:`, contano quei permessi **intersecati con la maschera**;
3. altrimenti, se uno dei tuoi gruppi corrisponde al gruppo del file o a una voce `group:nome:`, l'accesso è concesso se **almeno una** di quelle voci, intersecata con la maschera, contiene i permessi richiesti; se nessuna li contiene, l'accesso è negato (non si passa a `other`);
4. altrimenti contano i permessi `other::`.

La **maschera** (`mask::`) è il limite massimo dei permessi che possono concedere le voci "di mezzo": gli utenti nominati, il gruppo proprietario, i gruppi nominati. Il proprietario e `other` non ne sono toccati. La complicazione nasce per compatibilità: quando un file ha un'ACL estesa, i tre bit del **gruppo** mostrati da `ls -l` e modificati da `chmod g...` **sono la maschera**, non i permessi del gruppo proprietario. Così un programma vecchio che fa `chmod 600 file` per renderlo privato ottiene davvero quell'effetto: la maschera va a `---` e tutte le voci nominate smettono di valere.

```
$ chmod g-w piano.txt
$ getfacl piano.txt | grep -E 'bruno|mask'
user:bruno:rw-			#effective:r--
mask::r--
```

`getfacl` mostra il permesso **effettivo** dopo la maschera. Una conseguenza di sicurezza: guardando solo `ls -l` non sai chi ha accesso a un file con il `+`. Un file che sembra `-rw-r-----` può essere leggibile da dieci utenti nominati.

### 10.4 Le ACL predefinite

Una directory può avere, oltre alla propria ACL, un'**ACL predefinita** (*default ACL*): non controlla l'accesso alla directory, ma viene **copiata** su ogni file e sottodirectory creati al suo interno. È il modo più robusto per costruire una cartella condivisa, più del setgid con la umask, perché non dipende dalla umask di chi crea il file:

```
$ setfacl -m d:g:team:rwX /srv/progetto     # d: = default
$ getfacl /srv/progetto | grep default
default:user::rwx
default:group::r-x
default:group:team:rwx
default:mask::rwx
default:other::r-x
```

Quando c'è un'ACL predefinita, la umask **non viene applicata** al nuovo file; al suo posto si usano i permessi dell'ACL predefinita, intersecati con quelli richiesti dal programma.

## 11. Attributi del file system: `chattr` e `lsattr`

Ext4 e altri file system hanno degli **attributi** per file, indipendenti dai permessi, che si leggono con `lsattr` e si modificano con `chattr`. Due di essi contano per la sicurezza, perché valgono **anche per root**:

- `i` (*immutable*): il file non può essere modificato, cancellato, rinominato, né gli si possono creare link. Neppure root può farlo finché non toglie l'attributo, e per toglierlo serve la capability `CAP_LINUX_IMMUTABLE`.
- `a` (*append only*): il file si può aprire solo in aggiunta. Pensato per i log: un intruso che diventa root non può cancellare le righe che lo riguardano senza prima togliere l'attributo, cosa che lascia una traccia e richiede un privilegio specifico.

```
$ sudo chattr +i /etc/resolv.conf
$ sudo rm /etc/resolv.conf
rm: cannot remove '/etc/resolv.conf': Operation not permitted
$ lsattr /etc/resolv.conf
----i---------e------- /etc/resolv.conf
$ sudo chattr -i /etc/resolv.conf
```

Altri attributi (`e` per gli *extent*, `c` compressione, `s` cancellazione sicura, `u` recupero) hanno usi diversi o sono ignorati da ext4. Gli attributi `i` e `a` sono usati sia dai difensori (proteggere un file di configurazione critico) sia dagli intrusi (rendere difficile la rimozione di una backdoor): in un'analisi forense, `lsattr` sui file sospetti è un controllo d'obbligo, e in una CTF di tipo *King of the Hill* `chattr +i` è il modo più comune di "difendere" un file conquistato.

## 12. Le capability di Linux

### 12.1 Dividere root

Il modello "UID 0 può tutto, gli altri niente" viola il minimo privilegio in modo estremo. Un programma come `ping` deve aprire un socket di rete "grezzo" (*raw socket*), operazione riservata a root, e per questo per decenni è stato setuid root: un programma di migliaia di righe che legge argomenti dall'utente con **tutti** i poteri, quando gliene serviva uno solo. Le **capability** di Linux (dal kernel 2.2, 1999, ispirate alla bozza POSIX 1003.1e) dividono i privilegi di root in unità separate, che si possono concedere singolarmente a un processo o a un file. Oggi sono una quarantina; `man 7 capabilities` le elenca tutte. Quelle che devi conoscere:

| Capability | Che cosa permette | Perché è pericolosa se data male |
|---|---|---|
| `CAP_CHOWN` | cambiare proprietario a qualunque file | ci si regala `/etc/shadow` |
| `CAP_DAC_OVERRIDE` | ignorare i permessi `rwx` in lettura, scrittura ed esecuzione | si scrive in `/etc/passwd` |
| `CAP_DAC_READ_SEARCH` | ignorare i permessi in lettura e attraversamento | si legge `/etc/shadow` e qualunque chiave privata |
| `CAP_FOWNER` | agire come proprietario di qualunque file (`chmod` incluso) | `chmod 4755` su una shell |
| `CAP_SETUID`, `CAP_SETGID` | cambiare arbitrariamente UID e GID | diventare root con una chiamata |
| `CAP_NET_BIND_SERVICE` | aprire porte TCP/UDP sotto la 1024 | quasi innocua: il caso d'uso tipico |
| `CAP_NET_RAW` | socket grezzi (ping, sniffer) | intercettare traffico locale |
| `CAP_NET_ADMIN` | configurare interfacce, firewall, routing | redirigere il traffico |
| `CAP_SYS_PTRACE` | tracciare qualunque processo | iniettare codice in un processo di root |
| `CAP_SYS_MODULE` | caricare moduli del kernel | codice arbitrario nel kernel |
| `CAP_SYS_ADMIN` | un insieme enorme (montare file system, namespace, molto altro) | "la nuova root": quasi sempre equivalente a root |
| `CAP_KILL` | mandare segnali a qualunque processo | interrompere servizi |
| `CAP_LINUX_IMMUTABLE` | togliere e mettere `chattr +i`/`+a` | cancellare log protetti |

Una regola empirica, che viene da un articolo del 2011 di Brad Spengler (grsecurity), *False Boundaries and Arbitrary Code Execution*, è che **più di metà** delle capability permettono, con un po' di lavoro, di ottenere tutte le altre. Dare una di queste a un programma equivale a renderlo setuid root.

### 12.2 I cinque insiemi di un processo

Ogni thread ha cinque insiemi di capability, rappresentati come maschere di 64 bit. Sono le cinque righe che hai visto in `/proc/self/status`:

```
$ grep Cap /proc/self/status
CapInh:	0000000000000000
CapPrm:	0000000000000000
CapEff:	0000000000000000
CapBnd:	000001ffffffffff
CapAmb:	0000000000000000
```

- **Effettivo** (*effective*, `CapEff`): le capability che il kernel controlla davvero in questo momento. È l'analogo dell'UID effettivo.
- **Permesso** (*permitted*, `CapPrm`): il limite superiore dell'insieme effettivo. Un processo può spostare capability dal permesso all'effettivo e viceversa, ma non può aggiungerne di nuove al permesso. È l'analogo dello UID salvato.
- **Ereditabile** (*inheritable*, `CapInh`): le capability che possono sopravvivere a un `execve`, ma solo se anche il file eseguito le ha nel suo insieme ereditabile.
- **Delimitante** (*bounding*, `CapBnd`): un limite assoluto. Una capability che non sta in questo insieme non può essere ottenuta in alcun modo, neppure eseguendo un programma setuid root. Si può solo restringere. Un utente normale ha qui tutto attivo, perché il limite è pensato per i container e i servizi, che lo restringono.
- **Ambiente** (*ambient*, `CapAmb`, dal kernel 4.3): capability che passano a un `execve` di un programma **senza** file capability, un modo semplice per dare una capability a uno script o a un interprete senza modificarne il file.

Un processo di root ha tutte le capability negli insiemi permesso ed effettivo; un processo di un utente normale non ne ha nessuna. Le maschere si decodificano con `capsh`:

```
$ capsh --decode=0000000000003000
0x0000000000003000=cap_net_admin,cap_net_raw
$ grep CapEff /proc/1/status          # da root: PID 1 ha tutto
CapEff:	000001ffffffffff
```

### 12.3 Root e capability

Per compatibilità, essere root e avere capability sono legati da regole automatiche. Quando un processo con UID 0 esegue un programma, riceve tutte le capability (limitate dall'insieme delimitante). Quando un processo con UID effettivo 0 lo cambia in un UID diverso da zero, perde le capability effettive; quando tutti e tre gli UID diventano diversi da zero, perde anche quelle permesse. Ecco perché `login` dopo `setuid(1000)` non ha più alcun privilegio: le capability sono sparite insieme allo UID 0.

È possibile anche il contrario: un processo che **non** è root ma ha delle capability. Lo si vede nei servizi avviati da systemd con `AmbientCapabilities=CAP_NET_BIND_SERVICE` e `User=www-data`: un server web che apre la porta 80 senza mai essere stato root.

### 12.4 Le file capability

Le capability possono essere attaccate a un **file eseguibile**, in un attributo esteso (`security.capability`). Quando il file viene eseguito, il processo acquista quelle capability, indipendentemente da chi lo lancia. È la versione a grana fine del setuid. È così che `ping`, su molte distribuzioni, non è più setuid:

```
$ getcap /usr/bin/ping
/usr/bin/ping cap_net_raw=ep
$ ls -l /usr/bin/ping
-rwxr-xr-x 1 root root 89768 apr  8  2024 /usr/bin/ping
```

`ls -l` non mostra niente di speciale: le file capability sono **invisibili** ai comandi abituali, ed è un motivo in più per cercarle esplicitamente in un audit. Le lettere dopo il `=` sono gli insiemi del file: `e` (*effective*: attiva subito le capability come effettive), `p` (*permitted*: aggiungile all'insieme permesso), `i` (*inheritable*).

```
$ sudo setcap cap_net_bind_service=ep ./mioserver   # aggiungi
$ getcap ./mioserver
./mioserver cap_net_bind_service=ep
$ sudo setcap -r ./mioserver                        # togli
$ getcap -r / 2>/dev/null                           # cerca in tutto il sistema
```

Come per il setuid, una **scrittura** sul file rimuove le sue capability, e il linker dinamico entra in modalità sicura anche per i programmi con file capability.

Il caso pericoloso da riconoscere: un **interprete** con capability. Se a `python3`, `perl`, `node`, `vim` o `tar` è stata data `cap_setuid+ep` (spesso da un amministratore che voleva far funzionare uno script e non ha capito che la capability vale per **tutto** ciò che quell'interprete esegue), chiunque può scrivere una riga che chiama `setuid(0)` e diventa root. Lo puoi verificare in laboratorio, sulla tua macchina virtuale, con una **copia** di perl:

```
$ cp /usr/bin/perl /tmp/perlcap
$ sudo setcap cap_setuid+ep /tmp/perlcap
$ /tmp/perlcap -e '$< = $> = 0; exec "id"'
uid=0(root) gid=1000(zen) groups=1000(zen),27(sudo)
$ sudo rm /tmp/perlcap
```

L'UID è 0 e il GID è ancora il tuo: la capability concedeva di cambiare l'UID, non il GID. Precisione utile quando si legge un output del genere.

### 12.5 Strumenti

- `getcap`, `setcap` (pacchetto `libcap2-bin`): file capability;
- `capsh --print`: le capability della shell corrente; `capsh --decode=MASCHERA`: decodifica;
- `getpcaps PID`: le capability di un processo;
- `setpriv --dump`: tutte le credenziali del processo corrente; `setpriv --reuid=1000 --regid=1000 --init-groups --inh-caps=-all comando`: lancia un comando con credenziali scelte;
- `pscap` (pacchetto `libcap-ng-utils`): elenca i processi con capability.

### 12.6 `no_new_privs`

Un processo può impostare su se stesso il flag `PR_SET_NO_NEW_PRIVS` (chiamata `prctl`). Da quel momento, per lui e per tutti i suoi discendenti, `execve` **non concede mai nuovi privilegi**: i bit setuid e setgid e le file capability sono ignorati. Il flag non si può togliere. È il presupposto per i filtri *seccomp* (che limitano le chiamate di sistema disponibili, li incontreremo nel Modulo 4) e un'ottima difesa per i servizi: systemd lo attiva con `NoNewPrivileges=yes`, Docker con `--security-opt no-new-privileges`. Lo vedi nella riga `NoNewPrivs:` di `/proc/<PID>/status`:

```
$ setpriv --no-new-privs sudo id
sudo: The "no new privileges" flag is set, which prevents sudo from running as root.
```

## 13. Il controllo obbligatorio: SELinux e AppArmor

Tutto quello che abbiamo visto finora è DAC: il proprietario decide. Linux offre un'infrastruttura, i **Linux Security Modules** (LSM), che permette di aggiungere ai controlli tradizionali un secondo livello, deciso da una politica dell'amministratore. Il controllo LSM viene **dopo** quello DAC e può solo **negare**: un accesso deve passare entrambi. Due implementazioni dominano.

- **SELinux** (sviluppato dalla NSA, nel kernel dal 2003; predefinito su Red Hat, Fedora, CentOS, Android). Assegna a ogni processo e a ogni file un **contesto** (`utente:ruolo:tipo:livello`, ad esempio `system_u:system_r:httpd_t:s0` per il processo del server web e `system_u:object_r:httpd_sys_content_t:s0` per i file del sito) e una politica dice quali tipi di processo possono fare quali operazioni su quali tipi di file (*type enforcement*). Il server web compromesso, anche se diventa root, gira ancora nel tipo `httpd_t` e non può leggere file di tipo `shadow_t`. Comandi: `getenforce`, `sestatus`, `ls -Z`, `ps -Z`, `id -Z`; i rifiuti finiscono in `/var/log/audit/audit.log`.
- **AppArmor** (predefinito su Ubuntu, Debian, SUSE). Più semplice: invece di etichettare i file, assegna a ogni programma un **profilo** che elenca i percorsi a cui può accedere e con quali permessi. Comandi: `aa-status`, `aa-enforce`, `aa-complain`; i profili stanno in `/etc/apparmor.d/`.

Entrambi hanno una modalità "permissiva" (o *complain*) in cui registrano le violazioni senza bloccarle, utile per scrivere la politica. Il consiglio di sempre, spesso ignorato, è di non disattivarli quando qualcosa non funziona, ma di leggere il log e correggere la politica.

Per le CTF il MAC conta poco nelle categorie classiche, ma è utile riconoscerlo: se un'operazione che i permessi consentirebbero fallisce con `Permission denied` anche da root, il primo sospetto è un LSM. Più spesso incontrerai i **namespace** e **seccomp** dei container, che vedremo nei moduli successivi.

---

# Parte IV — Sicurezza: trovare e correggere i permessi sbagliati

Questa parte è scritta dal punto di vista di chi **amministra e difende** una macchina. L'obiettivo è imparare a fare l'*audit* dei permessi: passare in rassegna un sistema, riconoscere le configurazioni che indeboliscono il controllo d'accesso, e correggerle. Le stesse configurazioni, quando le incontri su una macchina di allenamento costruita apposta, sono ciò che una CTF ti chiede di notare; ma qui il filo conduttore è la **messa in sicurezza**, non lo sfruttamento. Per ogni classe di problema diamo: perché è un problema, con quale comando lo si trova, come lo si corregge.

## 14. Le configurazioni che indeboliscono il controllo d'accesso

Il principio che le riassume tutte è uno: **un processo privilegiato non deve dipendere da un oggetto che un utente meno privilegiato può modificare**. L'oggetto può essere un file di configurazione, uno script, un programma, una libreria, una directory nel `PATH`. Il lavoro dell'audit è seguire queste catene di fiducia e tagliarle dove sono invertite. Il riferimento MITRE è CWE-732 (*Incorrect Permission Assignment for Critical Resource*).

### 14.1 File sensibili con permessi troppo larghi

I file che custodiscono segreti o che governano l'identità del sistema devono avere permessi stretti. I più importanti, con il valore corretto:

| File | Corretto | Perché |
|---|---|---|
| `/etc/shadow`, `/etc/gshadow` | `640 root:shadow` (o `600`) | contengono gli hash delle password |
| `/etc/passwd`, `/etc/group` | `644 root:root` | devono essere leggibili, mai scrivibili da altri |
| `/etc/sudoers`, `/etc/sudoers.d/*` | `440 root:root` | la politica di `sudo` |
| `~/.ssh/id_*` (chiavi private) | `600` | SSH rifiuta di usare una chiave troppo aperta |
| `~/.ssh/authorized_keys` | `600` | chi la scrive entra come te |
| `~/.ssh`, `~` | `700`, `755` o `750` | SSH ignora le chiavi se la home è scrivibile da altri |
| `/etc/ssh/ssh_host_*_key` | `600 root:root` | la chiave privata del server |
| file `.env`, `config.php`, backup di database | `600` o `640` | contengono credenziali di applicazioni |

Il controllo di base cerca i file di sistema scrivibili da "altri" e i segreti leggibili da chi non dovrebbe:

```
$ find /etc -type f -perm -o+w -ls 2>/dev/null          # file di /etc scrivibili da tutti
$ ls -l /etc/shadow /etc/passwd /etc/sudoers            # devono corrispondere alla tabella
$ sudo find /home -name 'id_*' ! -name '*.pub' -perm /077 -ls   # chiavi private troppo aperte
$ find / -xdev -type f -name '*.bak' -o -name '*.env' 2>/dev/null | xargs ls -l 2>/dev/null
```

La correzione è un `chmod`/`chown` al valore della tabella. Il caso più grave è `/etc/passwd` o `/etc/shadow` scrivibili da altri (`chmod o-w`), o `/etc/shadow` leggibile da altri (`chmod 640`). Se trovi queste condizioni su una macchina di produzione, trattala come già compromessa: ripristina i permessi e indaga chi li ha cambiati e quando.

### 14.2 La ricerca dei comandi e il `PATH`

Abbiamo visto nella Lezione 1 (§11) che la shell cerca i comandi scorrendo le directory di `PATH` da sinistra a destra. Un programma privilegiato che invoca un altro programma **per nome** (per esempio uno script di root che chiama `cat` invece di `/bin/cat`) userà la ricerca nel `PATH`. Se in quel `PATH` compare una directory scrivibile da un utente, o il carattere `.` (la directory corrente), un utente può mettervi un file di nome `cat` che viene eseguito al posto di quello vero, con i privilegi del processo.

La difesa ha due parti, e sono entrambe a carico di chi scrive il codice e di chi configura il sistema:

- **negli script privilegiati**, usare percorsi assoluti (`/usr/bin/find`) o impostare un `PATH` fidato all'inizio (`PATH=/usr/sbin:/usr/bin:/sbin:/bin; export PATH`);
- **nella configurazione**, assicurarsi che `PATH` non contenga `.` né directory scrivibili da altri; per `sudo`, lasciare attivo `secure_path` in `sudoers` (§5.3), che sostituisce il `PATH` dell'utente con uno fidato.

```
$ echo "$PATH" | tr ':' '\n' | grep -nE '^$|^\.$|^:' ; echo '-- directory del PATH scrivibili:'
$ IFS=:; for d in $PATH; do [ -d "$d" ] && find "$d" -maxdepth 0 -perm -o+w 2>/dev/null; done
```

### 14.3 Script e directory scrivibili usati da processi di root

Questo è il caso più comune nelle macchine di allenamento, e un errore reale frequente. Un lavoro pianificato (`cron`, `systemd timer`) o un servizio esegue, come root, uno script che si trova in una directory scrivibile da un utente, o che è esso stesso scrivibile da un utente. Chi può scrivere lo script, o sostituirlo nella directory (§6.4), decide che cosa root eseguirà.

Dove guardare e come correggere:

```
$ ls -la /etc/cron.d /etc/cron.daily /etc/cron.hourly /etc/cron.weekly /etc/cron.monthly
$ cat /etc/crontab; sudo ls -l /var/spool/cron/crontabs
$ # per ogni script lanciato, controllane permessi e directory:
$ find /etc/cron* -type f -perm /022 -ls       # script di cron scrivibili da gruppo o altri
$ systemctl list-timers --all
```

Gli script eseguiti da root devono essere di proprietà di root, non scrivibili da altri (`644` o `755`, `root:root`), e stare in directory a loro volta di root e non scrivibili da altri. La correzione: `chown root:root`, `chmod go-w`, e spostare lo script fuori da qualunque directory condivisa. Un buon audit elenca ogni lavoro pianificato e, per ciascuno, verifica l'intera catena di directory fino allo script.

### 14.4 Regole `sudo` più larghe del necessario

`sudo` è sicuro quanto le sue regole. Una regola che sembra ristretta può concedere molto più di quanto si creda, perché molti programmi, pensati per un compito preciso, offrono anche un modo per eseguire comandi arbitrari o leggere file arbitrari. Alcuni esempi che ogni amministratore deve riconoscere:

- un editor (`vi`, `vim`, `nano` con certe opzioni), un *pager* (`less`, `more`, `man`) o qualunque programma che può lanciare una shell o eseguire comandi al suo interno: se è concesso con `sudo`, vale una shell di root;
- un interprete (`python`, `perl`, `awk`, persino `find -exec`) concesso con `sudo`: esegue qualunque cosa;
- un programma che **scrive file** come root (`tee`, `dd`, `cp`), o che li **legge** (`cat`, `rsync` con certe opzioni): permette di leggere o alterare qualunque file, compreso `/etc/shadow` o `/etc/sudoers`;
- `sudo` con l'opzione `env_keep` per `LD_PRELOAD` o `PYTHONPATH` (§5.3).

Lo strumento di riferimento per sapere, dato un programma, in quali modi "esce dal suo seminato" è il progetto **GTFOBins** (gtfobins.github.io): un catalogo, pensato sia per chi difende sia per chi fa penetration test autorizzato, che per centinaia di binari elenca come possono essere usati per leggere file, scrivere file, o ottenere una shell quando sono eseguibili con privilegi. Per l'amministratore è una **checklist difensiva**: dopo aver scritto una regola `sudo`, si cerca il programma su GTFOBins; se compare nella sezione "Sudo", la regola è più larga di quanto sembra e va ristretta (vincolando gli argomenti, scegliendo un programma più specifico, o sostituendo `sudo` con un servizio dedicato).

```
$ sudo -l                               # la prima cosa da leggere su ogni macchina
$ sudo grep -rE 'NOPASSWD|ALL' /etc/sudoers /etc/sudoers.d/ 2>/dev/null
```

La correzione è sempre nella direzione del minimo privilegio: concedere il comando più specifico possibile, con gli argomenti fissati, preferire `NOPASSWD` solo quando indispensabile, e verificare che il programma concesso non abbia vie di fuga.

### 14.5 Programmi setuid e capability non necessari

Ogni programma setuid root e ogni file con capability è una superficie d'attacco: se ha un difetto, è un difetto di root. La difesa è il **minimo**: avere solo quelli indispensabili, tenerli aggiornati, e togliere il bit a quelli che non servono. L'elenco "normale" di programmi setuid root su un sistema Debian/Ubuntu è corto e conviene conoscerlo a memoria, così da notare le aggiunte:

`su`, `sudo`, `passwd`, `chsh`, `chfn`, `newgrp`, `gpasswd`, `mount`, `umount`, e poco altro (`pkexec`, `fusermount`, qualche helper). Tutto ciò che è setuid root **oltre** a questi va giustificato.

```
$ find / -xdev -perm -4000 -type f 2>/dev/null          # tutti i setuid root (e non)
$ find / -xdev -perm -2000 -type f 2>/dev/null          # setgid
$ sudo getcap -r / 2>/dev/null                          # tutte le file capability
```

Confronta l'elenco con quello atteso. Un `find`, un `cp`, un `vim`, un `bash`, un `python` setuid root non sono mai normali: sono il segno di un errore o di una backdoor, e vanno tolti (`chmod u-s`) dopo aver capito chi li ha creati. Per le capability vale lo stesso: `cap_setuid`, `cap_dac_override`, `cap_dac_read_search`, `cap_sys_admin`, `cap_sys_ptrace` su un interprete o su un programma generico sono da rimuovere (`setcap -r file`). Dove serve un privilegio, si preferisce la capability specifica (per esempio `cap_net_bind_service` per aprire una porta bassa) al setuid root completo. Strumenti come `lynis`, `tiger` e i *benchmark* del **CIS** automatizzano buona parte di questi controlli e vanno eseguiti periodicamente.

### 14.6 File e directory scrivibili da tutti, e file "orfani"

Un file scrivibile da tutti (`-o+w`) può essere alterato da chiunque; una directory scrivibile da tutti senza sticky bit (§9.4) permette di sostituire i file che contiene. I file senza proprietario (§2.1) sono spesso il residuo di un utente cancellato e possono finire in mano a un nuovo utente che riceva lo stesso UID.

```
$ find / -xdev \( -type f -o -type d \) -perm -o+w ! -type l -ls 2>/dev/null
$ find / -xdev -type d -perm -0002 ! -perm -1000 -ls 2>/dev/null   # dir scrivibili senza sticky
$ find / -xdev -nouser -o -nogroup 2>/dev/null                     # file orfani
```

Correzione: togliere `w` agli altri dove non serve (`chmod o-w`), aggiungere lo sticky bit alle directory condivise che devono restarlo (`chmod +t`), assegnare un proprietario ai file orfani (`chown`). Su `/tmp` e simili lo sticky bit deve esserci sempre.

### 14.7 Il descrittore già aperto e la finestra temporale

Due problemi più sottili, utili per capire i limiti del modello.

Il primo l'abbiamo incontrato nel §1.1: il controllo si fa all'apertura. Togliere i permessi a un file **non** chiude i descrittori già aperti. Se un processo di un altro utente sta leggendo un file e tu lo rendi `000`, quel processo continua a leggerlo. Per interrompere davvero un accesso bisogna agire sul processo, non solo sui bit. È un motivo per cui, dopo aver scoperto una compromissione, ripristinare i permessi non basta: bisogna identificare e terminare i processi coinvolti (`lsof` sul file, L5 §7.5).

Il secondo è la **race condition tempo-di-controllo/tempo-di-uso** (*TOCTOU*, CWE-367): un programma privilegiato controlla un file (`access()`, o uno `stat`) e poi lo usa (`open()`), e fra i due istanti un utente cambia ciò che il nome indica (sostituendolo con un link simbolico). È un difetto di codice, non di configurazione, e lo studieremo nel Modulo 4; qui basti sapere che è il motivo per cui la funzione `access()` è considerata insicura per questo scopo, e per cui esistono le protezioni del §9.5.

### 14.8 Una lista di controllo

Mettendo insieme il tutto, un audit minimo dei permessi di una macchina Linux:

1. **Account**: un solo UID 0 (`awk -F: '$3==0' /etc/passwd`); nessun account con password vuota; appartenenze ai gruppi sensibili (`sudo`, `adm`, `shadow`, `disk`, `docker`) giustificate.
2. **File di sistema**: `/etc/passwd 644`, `/etc/shadow 640`, `/etc/sudoers 440`; nessun file in `/etc` scrivibile da altri.
3. **`sudo`**: leggere `sudo -l` per ogni utente con regole; nessuna via di fuga; `secure_path` e `env_reset` attivi.
4. **Setuid/setgid/capability**: solo quelli attesi; nessun interprete o programma generico tra essi.
5. **Lavori pianificati**: ogni script di `cron`/timer è di root e non scrivibile da altri, in directory non scrivibili da altri.
6. **`PATH`**: nessun `.` né directory scrivibile da altri, nei profili e nei servizi.
7. **Scrivibili da tutti e orfani**: niente directory `0777` senza sticky; niente file di sistema `-o+w`; nessun file senza proprietario.
8. **Home e chiavi**: home non scrivibili da altri; chiavi private `600`.

Ognuno di questi punti si verifica con un comando visto sopra. Automatizzarli in uno script è un ottimo esercizio (Esercizio 14), ed è esattamente ciò che fanno strumenti come `lynis` in grande.

## 15. I permessi nelle CTF

Nelle competizioni, i permessi compaiono in due vesti.

La prima è una **sfida a sé**, di categoria *misc* o nei moduli introduttivi di piattaforme come pwn.college, HackTheBox o OverTheWire (il gioco *Bandit* è quasi interamente su questo tema). La macchina è costruita così che la flag sia leggibile solo da un certo utente, o protetta da un permesso, e il percorso per arrivarci passa dal riconoscere e usare una delle configurazioni di questa lezione. L'autore ha messo l'errore apposta; il tuo compito è trovarlo, con lo stesso occhio dell'auditor. La sfida di questa lezione (§17, Esercizio 15) è di questo tipo.

La seconda è un **anello di una catena più lunga**: in una sfida *pwn* o *web* ottieni l'esecuzione di comandi come un utente poco privilegiato (`www-data`) e devi arrivare a root per leggere `/flag` o `/root/flag.txt`. Questa fase si chiama *privilege escalation* locale, ed è lo stesso lavoro dell'audit, svolto però per trovare **una** via che l'autore ha lasciato aperta, invece di chiuderle tutte. I primi comandi che si eseguono sono quelli che già conosci: `id`, `sudo -l`, la ricerca dei setuid, delle capability, dei lavori pianificati, dei file scrivibili. Esistono script che li raccolgono (`LinPEAS`, `linux-smart-enumeration`): sono, parola per parola, la lista di controllo del §14.8, eseguita automaticamente. Capire *perché* ogni voce è lì — che è lo scopo di questa lezione — è ciò che distingue chi sa leggere l'output di quegli script da chi li lancia a caso.

In entrambi i casi vale una regola deontologica che ripetiamo da §0: questi strumenti e queste tecniche si usano **solo** su macchine di competizione, di laboratorio o che hai l'autorizzazione esplicita a testare. La differenza fra un professionista della sicurezza e un criminale non sta nelle conoscenze, che sono le stesse, ma nel perimetro dell'autorizzazione.

---

# Parte V — La pratica

## 16. Esempi svolti

Prova a risolverli da solo prima di leggere la soluzione. Lavora sulla tua macchina virtuale, in una directory di prova, con un secondo utente `prova` dove serve.

### Esempio 1 — Leggere i quattro UID di un processo in corsa

*Obiettivo: osservare come un programma setuid cambia l'identità.* In un terminale lancia `passwd` e fermati alla richiesta della password. In un altro, trova il suo PID e leggi la riga `Uid:`.

```
$ pgrep -x passwd
3120
$ grep -E '^(Uid|Gid|Groups)' /proc/3120/status
Uid:	1000	0	0	0
Gid:	1000	1000	1000	1000
Groups:	27 100 1000
```

Lettura: l'UID reale è 1000 (sei stato tu ad avviarlo), ma l'UID effettivo, salvato e del file system sono 0, perché `/usr/bin/passwd` è setuid root. Il GID invece è rimasto 1000: `passwd` non è setgid. È grazie all'euid 0 che `passwd` può aprire `/etc/shadow`; è grazie al ruid 1000 che sa di quale utente cambiare la password. Chiudi con Ctrl-C.

### Esempio 2 — Calcolare a mente permessi e umask

*Obiettivo: automatismo nella conversione.* Senza eseguire niente, di': con `umask 027`, che permessi avranno un file e una directory appena creati? E quanto vale `chmod u=rw,g=r,o= file` in ottale? E che cosa mostra `ls -l` per `2750`?

Soluzione. File: richiesto `666`, umask `027` → `640` (`rw-r-----`). Directory: `777 AND NOT 027` → `750` (`rwxr-x---`). `u=rw,g=r,o=` = `640`. `2750` = setgid + `rwxr-x---` → `rwxr-s---` (la `s` minuscola perché il gruppo ha anche `x`). Verifica:

```
$ ( umask 027; touch f; mkdir d; stat -c '%a %A %n' f d )
640 -rw-r----- f
750 drwxr-x--- d
```

### Esempio 3 — Costruire una cartella di gruppo che funziona davvero

*Obiettivo: mettere insieme setgid, umask e ACL predefinita.* Vuoi una cartella `/srv/team` in cui i membri del gruppo `team` possano leggere e modificare i file degli altri, e in cui i nuovi file nascano già condivisi, qualunque umask abbia chi li crea.

```
$ sudo groupadd team; sudo gpasswd -a anna team; sudo gpasswd -a zen team
$ sudo mkdir /srv/team && sudo chgrp team /srv/team
$ sudo chmod 2770 /srv/team                         # setgid: i file ereditano il gruppo team
$ sudo setfacl -m d:g:team:rwX /srv/team            # ACL predefinita: niente dipende dalla umask
$ sudo setfacl -m d:o::--- /srv/team
```

Il setgid dà ai nuovi file il gruppo `team`; l'ACL predefinita dà loro i permessi `rwX` per il gruppo **senza** passare dalla umask di chi crea. Senza l'ACL, un membro con umask `077` creerebbe file che il resto del team non può leggere. Verifica entrando come `anna` e come `zen` e creando file a turno: ciascuno deve poter modificare quelli dell'altro.

### Esempio 4 — Riconoscere un hash e stabilire quanto è forte

*Obiettivo: leggere `/etc/shadow` da amministratore.* Su una macchina che amministri, guarda con quali algoritmi sono protette le password e se qualche account è senza password o con un hash debole.

```
$ sudo awk -F: '
  $2=="" {print $1": NESSUNA PASSWORD"; next}
  $2 ~ /^[!*]/ {next}                         # bloccati: li saltiamo
  {
    t=$2
    if (t ~ /^\$y\$/) a="yescrypt"
    else if (t ~ /^\$6\$/) a="sha512"
    else if (t ~ /^\$2[aby]\$/) a="bcrypt"
    else if (t ~ /^\$1\$/) a="MD5 (debole)"
    else a="DES/altro (debole)"
    print $1": "a
  }' /etc/shadow
```

Gli algoritmi `MD5` e `DES` sono da sostituire: basta far reimpostare la password all'utente, perché il nuovo hash userà l'algoritmo predefinito del sistema (`ENCRYPT_METHOD` in `/etc/login.defs`). Un account senza password va bloccato (`passwd -l`) o dotato di password. Questo stesso script, in una CTF, ti dice con quale `--format` lanciare `john` sugli hash che hai ottenuto; qui lo usiamo per sapere che cosa correggere.

### Esempio 5 — Dare a un programma solo la capability che gli serve

*Obiettivo: sostituire un setuid root con il minimo privilegio.* Hai un piccolo server che deve ascoltare sulla porta 443. La tentazione è farlo girare da root. Meglio dargli solo `CAP_NET_BIND_SERVICE`.

```
$ sudo setcap 'cap_net_bind_service=+ep' /usr/local/bin/mioserver
$ getcap /usr/local/bin/mioserver
/usr/local/bin/mioserver cap_net_bind_service=ep
```

Ora un utente normale può avviarlo e legarsi alla porta 443, ma il processo non ha nessun altro potere di root: se viene compromesso, l'attaccante ottiene solo la capacità di aprire porte basse, non la macchina. In un'unità systemd lo stesso si ottiene con `AmbientCapabilities=CAP_NET_BIND_SERVICE` e `User=mioserver`, senza toccare il file. È l'opposto esatto dell'errore del §12.4 (la capability su un interprete): qui il privilegio minimo va a un programma con un compito unico.

### Esempio 6 — Un audit dei setuid in una riga

*Obiettivo: confrontare i setuid presenti con quelli attesi.* Prepara una "lista bianca" dei programmi setuid root normali e segnala tutto il resto.

```
$ attesi='/usr/bin/su /usr/bin/sudo /usr/bin/passwd /usr/bin/chsh /usr/bin/chfn
/usr/bin/newgrp /usr/bin/gpasswd /usr/bin/mount /usr/bin/umount /usr/bin/pkexec
/usr/bin/fusermount3 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/polkit-1/polkit-agent-helper-1 /usr/lib/openssh/ssh-keysign'
$ find / -xdev -perm -4000 -type f 2>/dev/null | grep -vFf <(printf '%s\n' $attesi)
```

Qualunque riga in uscita è un setuid root inatteso: va esaminato. Un `/usr/bin/find`, un `/home/zen/.local/bin/bash` o simili sono quasi sempre il segno di un problema. Questo è il cuore di un audit; `lynis` fa questo e altre centinaia di controlli, ma saperlo fare a mano è ciò che ti permette di capire i suoi risultati.

## 17. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire `Soluzioni.md`. Lavora sulla tua macchina virtuale, in `~/l6`, con un secondo utente `prova` quando serve. Ricorda: molti esperimenti non mostrano nulla se li fai da root; crea e usa l'utente `prova`.

### ★ Base

1. **Lettura.** Senza eseguire comandi, traduci in ottale e descrivi a parole: `-rwsr-xr-x`, `drwxrwxrwt`, `-rw-r-----`, `drwx--x--x`, `-r-Sr--r--`. Per ognuno, di' chi può fare che cosa e se qualche bit è "sprecato".

2. **Conversioni.** Scrivi il comando `chmod` ottale equivalente a: `chmod u=rwx,g=rx,o=`; `chmod u=rw,go=`; `chmod a=r,u+w`; `chmod u=rwx,g=rx,o=rx,g+s`. Poi il contrario: esprimi `640`, `4755`, `1777`, `2750` in forma simbolica.

3. **umask.** Per ciascuna di queste umask, di' che permessi avranno un nuovo file e una nuova directory: `022`, `077`, `002`, `027`, `026`, `017`. Verifica quelle che ti sembrano strane con `( umask N; touch f; mkdir d; stat -c '%a %n' f d )`. Perché con `017` un file nasce `660` e non `661`?

4. **Proprietario contro gruppo.** Crea un file, mettilo nel gruppo `prova` (`sudo chgrp`), poi dagli permessi `chmod 406` (proprietario `r--`, gruppo `---`, altri `rw-`). Da proprietario, riesci a scriverci? A leggerlo? Spiega con l'algoritmo del §6.2. Poi come utente `prova` (che è nel gruppo): riesce a leggerlo? E un terzo utente?

5. **Directory.** Crea `~/l6/d` con dentro un file `segreto` con permessi `644`. Metti la directory a `711` (`rwx--x--x`). Da un altro utente: può fare `ls d`? Può fare `cat d/segreto`? Perché la risposta alle due domande è diversa? Poi metti la directory a `744` e ripeti.

6. **`/etc/passwd` e `/etc/shadow`.** Con `getent` e `awk`: (a) elenca nome e shell di tutti gli utenti con UID ≥ 1000; (b) conta quanti utenti hanno ogni shell; (c) verifica che ci sia un solo UID 0; (d) con `sudo`, trova a mano l'algoritmo dell'hash di un utente leggendo il prefisso del campo 2 di `shadow`.

### ★★ Intermedio

7. **Lista nera con i gruppi.** Costruisci una situazione in cui un file è leggibile da tutti **tranne** i membri di un gruppo `blocco`. (Suggerimento: §6.2, l'algoritmo si ferma alla prima classe che corrisponde.) Verifica con un utente nel gruppo e uno fuori. Poi spiega perché questa "lista nera" è fragile: trova almeno due modi in cui un membro di `blocco` può comunque arrivare al contenuto.

8. **Cartella condivisa.** Ricrea l'Esempio 3 ma **senza ACL**, usando solo setgid e umask. Mostra con due utenti che la collaborazione funziona se entrambi hanno umask `002`, e si rompe se uno ha umask `022` o `077`. Poi aggiungi l'ACL predefinita e mostra che il problema sparisce. Spiega esattamente perché.

9. **I bit speciali alla prova.** Dimostra con esperimenti: (a) scrivere su un file setuid ne azzera il bit; (b) `chown` azzera setuid e setgid; (c) Linux ignora il setuid su uno script `#!` (crea uno script setuid root e mostra che stampa il tuo UID, non 0); (d) lo sticky bit su una directory condivisa impedisce a un utente di cancellare il file di un altro ma non di modificarne il contenuto se i permessi lo consentono. Per ogni punto, indica quale scappatoia il kernel sta chiudendo.

10. **Lo script `permspiega`.** Scrivi `permspiega PERCORSO` che, dato un file, stampa: la forma ottale e simbolica; chi è proprietario e gruppo; per un terzo utente generico, se può leggere/scrivere/eseguire; se ha bit speciali, ACL (`+`) o capability, e che cosa significano. Provalo su `/usr/bin/passwd`, `/etc/shadow`, `/tmp`, `/etc/sudoers`, un file tuo con un'ACL.

11. **umask e la finestra temporale.** Scrivi uno script che crea un file di "credenziali" nel modo sbagliato (`echo segreto > f; chmod 600 f` con umask `022`) e uno nel modo giusto (`( umask 077; echo segreto > f )` oppure `install -m 600`). Con un secondo terminale e un ciclo `while` che tenta di aprire il file, dimostra che nel primo caso esiste un istante in cui un altro utente può aprirlo, e nel secondo no. Spiega il ruolo del descrittore già aperto (§14.7).

12. **ACL complete.** Su un file `piano.txt`: dai a `anna` lettura, a `bruno` lettura e scrittura, al gruppo `revisori` lettura; poi fai `chmod g-w piano.txt` e osserva con `getfacl` come cambia la maschera e i permessi **effettivi** di `bruno`. Spiega perché `ls -l` da solo non basta per sapere chi ha accesso al file. Infine togli tutta l'ACL con un comando.

### ★★★ Sfida

13. **Le credenziali che cambiano.** Senza scrivere codice C, osserva il ciclo di vita delle credenziali: (a) con `sudo`, confronta le righe `Uid`, `Gid`, `Groups`, `CapEff`, `NoNewPrivs` di `/proc/self/status` per: la tua shell; `sudo cat /proc/self/status`; `setpriv --reuid=1000 --regid=1000 --init-groups cat /proc/self/status`. (b) Spiega perché un `sudo` a un programma e un file setuid root portano entrambi a euid 0 ma con insiemi di capability diversi. (c) Mostra con `capsh --decode` che cosa contiene `CapBnd` della tua shell e perché contiene quasi tutto anche se non sei root.

14. **Un auditor dei permessi.** Scrivi `audit_permessi.sh` che esegue, in sola lettura, i controlli della lista del §14.8 e stampa un rapporto con una riga per ogni problema trovato, suddiviso per gravità: UID 0 multipli, password vuote, `/etc/shadow` o `/etc/passwd` con permessi sbagliati, setuid root inattesi (rispetto a una lista bianca), capability su interpreti, directory `0777` senza sticky, file di sistema scrivibili da altri, `.` nel `PATH`. Lo script **non deve modificare niente**: solo segnalare. Provalo sulla tua macchina e spiega ogni riga che produce. (È la versione "a mano" di `lynis`.)

15. **La mini-CTF: "I permessi raccontano".** Esegui `bash setup_sfida.sh`: crea la cartella `~/l6_sfida` con quattro prove, ognuna delle quali custodisce un quarto della flag `L6{...}` usando un aspetto diverso di questa lezione. Nessun pezzo è "nascosto" nel senso classico: sono tutti protetti, o scritti, dai permessi. Il file `LEGGIMI.txt` ti guida. In sintesi:
    - **chiuso.txt** è `000`: non puoi leggerlo. Ma ne sei il proprietario — e il proprietario può sempre ridarsi i permessi (§6.2, §6.6).
    - **archivio/** è `444`: leggibile ma non attraversabile. Puoi elencare i nomi dei file ma non aprirli (§6.4). Uno dei nomi è il messaggio.
    - **firme/** contiene trenta file; conta solo chi ha il bit **setuid**, in ordine di nome (§9.1, `find -perm -4000`).
    - **codice/** contiene file vuoti: il messaggio è nei loro **permessi**, letti in ottale come codici ASCII (§7.2). `stat -c '%a'` dà i numeri; traducili.
    Rimetti insieme i quattro pezzi nell'ordine 1-2-3-4. Alla fine, come dice il `LEGGIMI`, ridai a te stesso i permessi su tutto (`chmod -R u+rwx ~/l6_sfida`) così da poter cancellare la cartella. La soluzione completa, comando per comando, è in `Soluzioni.md`.

### Allenamento esterno

- **pwn.college**, dojo *Linux Luminarium*, moduli **Perceiving Permissions** e **Untangling Users**, e il dojo **Access Control** del corso CSE 365: sono la fonte diretta di questa lezione e offrono decine di sfide con verifica automatica.
- **OverTheWire**, gioco **Bandit**: moltissimi livelli sono esercizi di permessi, setuid e lettura di file protetti; è il miglior allenamento graduale che esista per i contenuti di oggi.
- **GTFOBins** (gtfobins.github.io): studia, per cinque o sei binari comuni (`find`, `vim`, `less`, `tar`, `python`), la sezione "Sudo" e "SUID", per capire *perché* una regola `sudo` troppo larga è pericolosa. Usalo come strumento difensivo: dopo aver scritto una regola, controlla il binario.

## 18. Domande di autoverifica

1. Perché il kernel conosce gli utenti come numeri e non come nomi? Dove avviene la traduzione?
2. Che differenza c'è fra UID reale, effettivo e salvato? A che cosa serve ciascuno, e quale usa il kernel per decidere se puoi aprire un file?
3. Enuncia l'algoritmo di controllo dei permessi `rwx`. Perché un file `047` non è leggibile dal suo proprietario?
4. Che cosa significano `r`, `w`, `x` su una **directory**? Perché per cancellare un file non serve alcun permesso sul file?
5. Con umask `027`, che permessi ha un file appena creato? E una directory? Perché si usa un AND e non una sottrazione?
6. Che cosa fa il bit setuid? Perché Linux lo ignora sugli script? Perché viene azzerato quando si scrive sul file o se ne cambia il proprietario?
7. Che differenza c'è fra setgid su un file e setgid su una directory?
8. A che cosa serve lo sticky bit? Qual è la differenza fra l'errore `EPERM` e `EACCES` che hai osservato?
9. Che cosa aggiungono le ACL al modello a tre classi? Che cos'è la maschera e perché `chmod g-w` può togliere l'accesso a utenti nominati?
10. Che cosa sono le capability di Linux? Perché dare `cap_setuid` a `python3` equivale a renderlo setuid root?
11. Perché un programma setuid root entra in "modalità sicura" per il linker dinamico? Che cosa succederebbe altrimenti con `LD_PRELOAD`?
12. Elenca cinque controlli di un audit dei permessi e, per ognuno, il comando che lo esegue e la correzione.

## 19. Riepilogo

- Il controllo d'accesso risponde a "questo soggetto può fare questa operazione su questo oggetto?". In Linux il soggetto è un **processo** con un'identità, l'oggetto è di solito un file, e l'arbitro è il **kernel**. Il modello Unix è **discrezionale** (il proprietario decide); SELinux e AppArmor aggiungono un livello **obbligatorio**.
- Per il kernel un utente è un **numero** (UID), un gruppo un numero (GID). I nomi vivono in `/etc/passwd`, `/etc/group` e nelle fonti di NSS, e si interrogano con `getent`. Gli hash delle password stanno in `/etc/shadow`, leggibile solo da root, nel formato `$id$sale$hash`.
- Un processo porta **UID reale, effettivo, salvato** (e del file system) e i **gruppi supplementari**. L'effettivo decide i permessi; il reale dice chi ha avviato; il salvato permette di abbassare e rialzare i privilegi. `login`, `su` e `sudo` sono i punti in cui l'identità cambia, ed `execve` di un file **setuid** è l'unico caso in cui `execve` cambia l'identità.
- I permessi sono **nove bit** `rwx` in tre classi (proprietario, gruppo, altri) più tre bit speciali. L'algoritmo sceglie **una sola** classe, senza ricaduta. Su una directory, `r` elenca, `x` attraversa, `w`+`x` modifica la tabella: da qui il fatto che si cancella un file senza permessi sul file.
- La **umask** toglie bit ai file alla creazione (`permessi AND NOT umask`). I bit **setuid/setgid** cambiano l'identità dei programmi (e il gruppo dei file nelle directory setgid); lo **sticky bit** protegge i nomi nelle directory condivise come `/tmp`.
- Oltre ai nove bit: le **ACL** per permessi a utenti e gruppi specifici (attenzione alla maschera e al `+` di `ls -l`), gli attributi **`chattr +i/+a`** che fermano anche root, e le **capability** che spezzano i poteri di root in unità concedibili a processi e file.
- La sicurezza dei permessi è, in pratica, un **audit**: un solo UID 0, file sensibili stretti, `sudo -l` senza vie di fuga, solo i setuid e le capability attesi, nessuno script o directory scrivibile da altri usato da root, `PATH` pulito, niente scrivibili da tutti o file orfani. Le stesse voci, lette "al contrario", sono ciò che si cerca in una *privilege escalation* di CTF — da fare solo dove sei autorizzato.

## 20. Fonti

- **OccupyTheWeb**, *Linux Basics for Hackers*, cap. 5 (gestione dei permessi: `chmod`, numeri, setuid/setgid, sticky) e cap. 1, 10 (utenti, file di sistema). È la trattazione più diretta e orientata alla sicurezza fra i libri della tua cartella.
- **R. Anderson**, *Security Engineering*, 3ª ed., cap. 6 (*Access Control*): matrice di accesso, ACL e capability, DAC e MAC, i modelli Bell–LaPadula e Biba, il reference monitor. Il riferimento concettuale per tutta la Parte I.
- **D. A. Curry**, e più in generale la documentazione Unix classica, per il modello dei permessi; **M. Kerrisk**, *The Linux Programming Interface*, cap. 8–9 (utenti e gruppi, credenziali di un processo), 15.3–15.4 (permessi dei file, umask), 17 (ACL), 39 (capability): la fonte più precisa e completa in assoluto, da consultare per capitoli.
- **W. R. Stevens, S. Rago**, *Advanced Programming in the UNIX Environment*, cap. 4 (file e directory: permessi, setuid, sticky, `chmod`, `chown`).
- **J. H. Saltzer, M. D. Schroeder**, *The Protection of Information in Computer Systems*, Proc. IEEE, 1975: gli otto principi di progettazione (§1.4).
- **R. Morris, K. Thompson**, *Password Security: A Case History*, CACM, 1979; **H. Chen, D. Wagner, D. Dean**, *Setuid Demystified*, USENIX Security, 2002 (la semantica di `setuid` e perché usare `setresuid`).
- **pwn.college**, dojo *Linux Luminarium* (moduli *Perceiving Permissions*, *Untangling Users*) e corso CSE 365 (modulo *Access Control*): l'ossatura di questa lezione.
- **Pagine di manuale**: `credentials(7)`, `capabilities(7)`, `chmod(1)`, `chmod(2)`, `umask(2)`, `acl(5)`, `setfacl(1)`, `getfacl(1)`, `chattr(1)`, `sudoers(5)`, `passwd(5)`, `shadow(5)`, `path_resolution(7)`, `inode(7)`, `namei(1)`.
- **MITRE CWE**: CWE-732 (*Incorrect Permission Assignment for Critical Resource*), CWE-276 (*Incorrect Default Permissions*), CWE-271/272/273 (*Privilege Dropping/Lowering Errors*), CWE-250 (*Execution with Unnecessary Privileges*), CWE-367 (*TOCTOU*).
- **Progetti pratici**: GTFOBins (gtfobins.github.io), *LinPEAS* e *linux-smart-enumeration* (come checklist di audit), *lynis* e i *CIS Benchmarks* (hardening automatizzato).

## 21. Prossima lezione

**Lezione 7 — Rappresentare i dati**: bit e byte, i sistemi di numerazione binario ed esadecimale (di cui oggi abbiamo usato l'ottale per i permessi e il modo), interi con e senza segno, il complemento a due, l'*endianness*, le codifiche del testo (ASCII, UTF-8) e Base64 (che abbiamo già incrociato in `setup_sfida.sh`), gli strumenti `xxd` e `hexdump`, e CyberChef. È la lezione che apre la categoria *crypto* e serve da fondamenta a tutto il Modulo 2 sull'architettura: imparerai finalmente a "vedere" un byte in tutte le sue facce.
