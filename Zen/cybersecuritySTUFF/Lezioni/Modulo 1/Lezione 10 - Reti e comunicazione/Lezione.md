# Modulo 1 — Lezione 10: Reti e comunicazione

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 10 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 13).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. descrivere il modello a livelli di Internet (il *TCP/IP stack*), dire che cosa fa ciascun livello e come un dato viene incapsulato scendendo e spacchettato salendo;
2. leggere e scrivere indirizzi IPv4 e IPv6, riconoscere reti e maschere (CIDR), e sapere che cosa sono gli indirizzi privati, il *loopback* e il *broadcast*;
3. spiegare che cosa sono le **porte**, la differenza tra **TCP** e **UDP**, e che cosa succede, pacchetto per pacchetto, quando si apre e si chiude una connessione TCP;
4. usare i **socket** dal C e da Python per scrivere un client e un server TCP e UDP, collegando il tutto alle chiamate di sistema della Lezione 9;
5. usare `nc`, `curl`, `ss`/`netstat`, `ping` dalla riga di comando per esplorare servizi, fare richieste e diagnosticare una connessione;
6. descrivere il **DNS**: che cosa risolve, i tipi di record principali, come si interroga con `dig`/`host`/`getent`, e perché è un bersaglio e uno strumento nelle CTF;
7. costruire e leggere una richiesta e una risposta **HTTP** a mano, e capire che cosa fa `curl` sotto il cofano, incluse intestazioni, metodi, codici di stato e cookie;
8. catturare e leggere il traffico di rete con `tcpdump` e Wireshark, seguire un flusso TCP, ed estrarre dati da una cattura (`.pcap`), che è una categoria di sfide a sé.

**Prerequisiti:** tutte le lezioni precedenti. In particolare: i descrittori di file e le chiamate di sistema `read`/`write` (L4 §1, L9 §10), il buffering (L4 §3), i processi (L5), la rappresentazione dei numeri, l'endianness e le codifiche (L7), Python e i socket di base con pwntools (L8 §6), il C, i puntatori e le `struct` (L9). Questa lezione unisce tutto il modulo: il socket è un descrittore (L4, L9), i byte che ci passano sono quelli della Lezione 7, e il dialogo è quello della Lezione 8.

**Tempo:** circa 4–5 ore di lettura e prove, 4 ore di esercizi. Molte prove si fanno in **locale**, su `127.0.0.1`, con due terminali (un server e un client): non serve una rete vera, e soprattutto non si attacca mai una macchina che non è la propria.

**Strumenti.** `nc` (netcat), `curl`, `ss` (o `netstat`), `ping`, `dig`/`host` (pacchetto `dnsutils`/`bind-utils`), `tcpdump` e **Wireshark**. Su Debian/Ubuntu/Kali: `sudo apt install netcat-openbsd curl iproute2 dnsutils tcpdump wireshark`. Gli esempi di rete di questa lezione sono stati provati su `127.0.0.1` con Python 3.13, gcc 13.3, `nc` OpenBSD e `curl` 8.5; `tcpdump` e Wireshark si usano sulla tua macchina, con i permessi per catturare.

**Ripasso dalle lezioni precedenti.**
- Nella Lezione 8 hai aperto connessioni con pwntools (`remote`, §6) e hai imparato che `recv` **non** restituisce messaggi ma byte, e che i confini li ricostruisci tu. Oggi capisci **perché**: è TCP a essere un flusso di byte, e lo vedrai dal basso.
- Nella Lezione 9 hai visto un programma C aprire un descrittore e fare `read`/`write`. Un socket è un descrittore come gli altri: le stesse `read` e `write`, più qualche chiamata di sistema in più per stabilire la connessione.
- Nella Lezione 7 hai imparato l'endianness. La rete ha un suo ordine dei byte, il *network byte order* (big-endian), e vedrai le funzioni `htons`/`ntohl` che convertono: è lì che l'endianness smette di essere teoria.

**Convenzione tipografica.** `$` è il prompt della shell. Dove servono due terminali, li indico con `# term. 1` e `# term. 2`. Gli indirizzi di esempio usano `127.0.0.1` (la tua macchina) e la documentazione RFC (`192.0.2.0/24`, `example.com`).

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. Come è fatta la rete | 1–3 | A livelli, indirizzi, porte: come viaggia un dato? |
| II. TCP, UDP e i socket | 4–6 | Come si apre una connessione, e come la si programma? |
| III. Gli strumenti | 7–8 | `nc`, `curl`, `ss`: come si esplora e si diagnostica? |
| IV. I protocolli applicativi | 9–10 | DNS e HTTP: che cosa dicono davvero i messaggi? |
| V. Guardare il traffico | 11 | `tcpdump` e Wireshark: che cosa passa sul filo? |
| VI. La pratica | 12–17 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — Come è fatta la rete

## 1. Il modello a livelli

### 1.1 Perché a livelli

Far comunicare due programmi su due macchine diverse è un problema enorme: bisogna trovare l'altra macchina in una rete di miliardi, portarci i dati attraverso cavi, fibre e radio di tecnologie diverse, gestire la perdita di pezzi, metterli in ordine, e infine consegnarli al programma giusto tra le centinaia in esecuzione. Nessuno risolve tutto questo in un pezzo solo. La soluzione, vecchia di cinquant'anni, è dividerlo in **livelli** (*layer*): ciascuno risolve un sotto-problema e offre un servizio al livello sopra, usando il servizio del livello sotto, senza sapere come gli altri funzionano dentro. Un programma che usa TCP non sa se sotto c'è fibra o Wi-Fi; una scheda di rete non sa se trasporta una pagina web o una e-mail.

Il modello teorico classico è l'**OSI** a sette livelli, utile come vocabolario (si parla di "attacco al livello 7" per dire "a livello applicativo"). Quello che Internet usa davvero è il modello **TCP/IP**, a quattro livelli:

| # | Livello (TCP/IP) | Che cosa fa | Unità di dati | Indirizzo | Esempi |
|---|---|---|---|---|---|
| 4 | **Applicazione** | il protocollo del programma | messaggio | — | HTTP, DNS, SSH, TLS |
| 3 | **Trasporto** | consegna al programma giusto, affidabilità | segmento (TCP) / datagramma (UDP) | **porta** | TCP, UDP |
| 2 | **Rete** (*Internet*) | instradamento da una rete all'altra | pacchetto | **indirizzo IP** | IP (v4, v6), ICMP |
| 1 | **Collegamento** (*Link*) | trasmissione sul mezzo fisico locale | frame | indirizzo MAC | Ethernet, Wi-Fi |

(Il modello OSI spezza l'applicazione in tre, 5–7, e il collegamento in due, 1–2; i numeri "L3", "L4", "L7" che sentirai vengono da OSI. Per lavorare basta il modello a quattro.)

### 1.2 L'incapsulamento

Un dato che scende attraverso i livelli viene **incapsulato**: ogni livello aggiunge davanti ai dati che riceve la propria **intestazione** (*header*), come una busta dentro una busta dentro una busta. Quando apri una pagina, il tuo browser produce un messaggio HTTP; TCP gli mette davanti la propria intestazione (con le porte) formando un **segmento**; IP mette davanti la sua (con gli indirizzi) formando un **pacchetto**; Ethernet mette la sua (con i MAC) formando un **frame**, che viaggia sul cavo. Sulla macchina di destinazione il processo è inverso: ogni livello toglie la propria intestazione e passa il resto a quello sopra. In uno schema:

```
          mittente                                   destinatario
  [ HTTP: GET / ... ]                           [ HTTP: GET / ... ]
  [ TCP | HTTP ]                                [ TCP | HTTP ]
  [ IP | TCP | HTTP ]                           [ IP | TCP | HTTP ]
  [ Eth | IP | TCP | HTTP | FCS ]  ---------->  [ Eth | IP | TCP | HTTP | FCS ]
                                   sul filo
```

Questo è esattamente ciò che vedrai in Wireshark (§11): una cattura mostra, per ogni pacchetto, le intestazioni annidate una dentro l'altra, dal frame Ethernet fino al messaggio applicativo. Capire l'incapsulamento è capire che cosa stai guardando.

## 2. Indirizzi IP

### 2.1 IPv4

Un indirizzo **IPv4** è un numero a 32 bit (L7 §2), scritto come quattro byte in decimale separati da punti (*dotted decimal*): `192.0.2.235` sono i quattro byte `11000000 00000000 00000010 11101011`. Ci sono quindi circa 4,3 miliardi di indirizzi (2³²), troppo pochi per il mondo di oggi: è il motivo di IPv6 (§2.3) e del NAT (§2.4).

Un indirizzo si divide in due parti: un **prefisso di rete** e un **identificatore di host** dentro quella rete. Quanti bit spettano alla rete lo dice la **maschera**, scritta in notazione **CIDR** come `/n`: `192.0.2.0/24` significa "i primi 24 bit (`192.0.2`) identificano la rete, gli ultimi 8 l'host", quindi la rete contiene gli indirizzi da `192.0.2.0` a `192.0.2.255` (256 indirizzi, di cui il primo è l'indirizzo di rete e l'ultimo il *broadcast*). Una `/16` ha 16 bit di host (65 536 indirizzi), una `/8` ne ha 24. La maschera `/24` equivale alla maschera di bit `255.255.255.0`: fare l'AND bit a bit (L7 §4.2) tra un indirizzo e la maschera dà l'indirizzo di rete. Due host sono "sulla stessa rete locale" (si raggiungono senza passare da un router) se hanno lo stesso prefisso di rete.

Alcuni indirizzi hanno un significato speciale:
- **`127.0.0.0/8`** è il *loopback*: `127.0.0.1` è "questa stessa macchina". Un pacchetto per `127.0.0.1` non esce mai dalla scheda di rete; è dove farai quasi tutte le prove.
- Gli indirizzi **privati** (RFC 1918), non instradabili su Internet, usati nelle reti locali dietro un NAT: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. Il tuo computer di casa ha quasi certamente un indirizzo `192.168.x.y`.
- **`0.0.0.0`**: "qualunque indirizzo", usato da un server per dire "ascolta su tutte le interfacce" (§6.3).
- L'ultimo indirizzo di una rete è il **broadcast** (`192.0.2.255` per una `/24`): raggiunge tutti gli host della rete locale.

### 2.2 L'ordine dei byte della rete

Qui l'endianness della Lezione 7 (§5) smette di essere teoria. I protocolli di rete mettono i numeri a più byte (porte, indirizzi, lunghezze) in **big-endian**, che per questo si chiama anche *network byte order*. Le macchine x86, invece, sono little-endian. Un programma che costruisce un'intestazione deve quindi **convertire**, e il C offre quattro funzioni (da `<arpa/inet.h>`): `htons` (*host to network short*, 16 bit), `htonl` (32 bit), e le inverse `ntohs`, `ntohl`. Le vedrai nel server del §6: `htons(7777)` mette la porta 7777 nell'ordine giusto. Dimenticarle è un bug classico: su x86 la porta 7777 (`0x1e61`) diventerebbe `0x611e` = 24862, e il programma ascolterebbe sulla porta sbagliata.

### 2.3 IPv6, in breve

IPv6 usa indirizzi a **128 bit**, scritti come otto gruppi di quattro cifre esadecimali separati da `:` (`2001:0db8:0000:0000:0000:0000:0000:0001`), con due abbreviazioni: gli zeri iniziali di ogni gruppo si omettono, e **una** sequenza di gruppi tutti a zero si sostituisce con `::` (l'indirizzo sopra diventa `2001:db8::1`). Il loopback è `::1`. 128 bit sono abbastanza indirizzi da non doverli mai più razionare. Nelle CTF e nel lavoro quotidiano incontrerai ancora soprattutto IPv4, ma i socket moderni e gli strumenti (`curl`, `ss`, `getaddrinfo`) parlano entrambi.

### 2.4 Un cenno su NAT e routing

Poiché gli indirizzi IPv4 pubblici scarseggiano, le reti domestiche e aziendali usano indirizzi privati all'interno e un solo indirizzo pubblico verso Internet: il router fa **NAT** (*Network Address Translation*), riscrivendo indirizzi e porte dei pacchetti in uscita e tenendo una tabella per instradare le risposte. È il motivo per cui, da casa, puoi collegarti a un server esterno ma un server esterno non può collegarsi direttamente a te (serve una regola di *port forwarding*). L'**instradamento** (*routing*) è il meccanismo con cui ogni pacchetto, di router in router, trova la strada verso la rete di destinazione, guardando l'indirizzo IP e una tabella di instradamento; a ogni salto il *TTL* (*time to live*) del pacchetto cala di uno, e un pacchetto che gira a vuoto viene scartato quando arriva a zero (è il meccanismo su cui si basa `traceroute`).

## 3. Le porte e il modello client-server

Un indirizzo IP identifica una **macchina**; ma su una macchina girano decine di programmi che usano la rete. La **porta** identifica il programma: è un numero a 16 bit (0–65535), e la coppia (indirizzo IP, porta) identifica un **endpoint** di comunicazione. Una connessione TCP è individuata da **quattro** valori: IP e porta di origine, IP e porta di destinazione (la *socket pair*). È per questo che il tuo browser può avere dieci connessioni aperte verso lo stesso sito: hanno la stessa destinazione, ma porte di origine diverse.

Le porte si dividono per convenzione in: **ben note** (0–1023), riservate ai servizi di sistema e che richiedono privilegi per essere aperte in ascolto (su Linux, essere root o avere una capability); **registrate** (1024–49151); **dinamiche o effimere** (49152–65535), che il sistema assegna automaticamente alla porta di origine di un client. Alcune porte ben note da ricordare: **22** SSH, **53** DNS, **80** HTTP, **443** HTTPS, **25** SMTP, **21** FTP, **3306** MySQL, **6379** Redis. Nelle sfide, una scansione delle porte (§7) dice subito quali servizi offre una macchina, e le porte "strane" sono spesso dove sta la sfida.

Quasi tutta la comunicazione in rete segue il modello **client-server**: il **server** apre una porta e **aspetta** connessioni (è "passivo"); il **client** sa dove sta il server (indirizzo e porta) e **inizia** la connessione (è "attivo"). Il server di solito serve molti client. In una CTF, il "servizio della sfida" (L8) è un server, e tu scrivi il client. Nel §6 scriverai entrambi.

---

# Parte II — TCP, UDP e i socket

## 4. TCP e UDP

Al livello di trasporto, due protocolli si dividono quasi tutto il traffico, con filosofie opposte.

**TCP** (*Transmission Control Protocol*) offre un **flusso di byte affidabile e ordinato** tra due endpoint. "Affidabile" significa che TCP ritrasmette i pezzi persi, scarta i duplicati, e consegna i byte **nell'ordine** in cui sono stati inviati; se la consegna è impossibile, segnala un errore. Per farlo, TCP mantiene uno **stato** per ogni connessione (numeri di sequenza, finestra, timer), e la connessione va **aperta** e **chiusa** con una procedura. È il protocollo di HTTP, SSH, e di quasi tutte le sfide: quando in una CTF leggi `nc host porta`, è TCP.

**UDP** (*User Datagram Protocol*) offre invece una consegna **a datagrammi, senza connessione e senza garanzie**: spedisci un pacchetto e speri che arrivi. Non c'è apertura, non c'è ordine, non c'è ritrasmissione; un datagramma può perdersi, arrivare in ritardo o doppio. In cambio è più leggero e senza latenza di handshake: è il protocollo del DNS (una domanda, una risposta), del tempo (NTP), dello streaming e dei giochi, dove una ritrasmissione tardiva è inutile. Il confronto:

| | TCP | UDP |
|---|---|---|
| Connessione | sì (handshake, §5) | no |
| Affidabilità | ritrasmette, mette in ordine | nessuna garanzia |
| Unità | flusso di byte (niente confini di messaggio) | datagrammi (confini preservati) |
| Stato | per connessione | nessuno |
| Intestazione | 20+ byte | 8 byte |
| Usi | HTTP, SSH, TLS, la maggior parte delle CTF | DNS, NTP, streaming, giochi |

Una differenza conta per chi programma, ed è quella della Lezione 8: TCP è un **flusso di byte**, e una `recv` restituisce "quanto è arrivato", che può essere mezzo messaggio o due messaggi insieme (L8 §6.2); i confini li ricostruisci tu. UDP, invece, **conserva i confini**: una `recvfrom` restituisce esattamente un datagramma, quello che un `sendto` ha spedito.

## 5. L'handshake e la chiusura di TCP

L'intestazione TCP contiene, oltre alle due porte, dei **flag** (bit) che controllano la connessione: i più importanti sono **SYN** (sincronizza, "voglio aprire"), **ACK** (conferma, "ho ricevuto"), **FIN** (fine, "ho finito di mandare"), **RST** (reset, "chiudi subito, errore").

Aprire una connessione richiede tre pacchetti, il **three-way handshake**:

```
  client                              server
    |  --- SYN (seq=x) ----------------->  |   "voglio aprire, il mio numero di sequenza è x"
    |  <-- SYN (seq=y), ACK (x+1) -------   |   "ok, il mio è y, ho ricevuto fino a x"
    |  --- ACK (y+1) ------------------->   |   "ho ricevuto fino a y: connessione aperta"
    |                                       |
    |  <======= flusso di byte =========>   |   (dati, ciascuno confermato da ACK)
```

Dopo l'handshake la connessione è stabilita, e i due possono scambiarsi byte in entrambe le direzioni; ogni byte ricevuto viene confermato con un ACK, e ciò che non è confermato entro un timeout viene ritrasmesso. Chiudere richiede uno scambio di **FIN** e **ACK** (ciascuna direzione si chiude per conto suo: puoi aver finito di mandare ma continuare a ricevere). È l'EOF della Lezione 8: quando il server manda FIN, la tua `recv` restituisce 0 (in pwntools, `EOFError`). Un **RST**, invece, chiude bruscamente: lo ricevi, per esempio, quando ti colleghi a una porta su cui **non** c'è nessun server in ascolto (è così che una scansione, §7, distingue una porta chiusa da una aperta). Vedrai questi pacchetti, uno per uno, in `tcpdump` e Wireshark (§11): riconoscere `[S]`, `[S.]`, `[.]`, `[F.]`, `[R]` nell'output di `tcpdump` è saper leggere lo stato di una connessione.

## 6. I socket

### 6.1 Che cos'è un socket

Un **socket** è l'astrazione con cui un programma usa la rete: un **descrittore di file** (L4 §1, L9 §10) che rappresenta un endpoint di comunicazione. Una volta stabilita la connessione, ci leggi e ci scrivi con `read`/`write` o con le varianti `recv`/`send`, esattamente come su un file o una pipe. Tutta la differenza sta nelle poche chiamate di sistema che servono a **creare** il socket e a **stabilire** la connessione. È ciò che pwntools (L8) e il modulo `socket` di Python fanno per te; ora lo scrivi a mano.

Le chiamate di sistema dei socket, nell'ordine in cui le usa un server e un client:

| | Server (passivo) | Client (attivo) |
|---|---|---|
| 1 | `socket()` crea il socket | `socket()` |
| 2 | `bind()` lo lega a (IP, porta) | |
| 3 | `listen()` lo mette in ascolto | |
| 4 | `accept()` attende e accetta una connessione (restituisce un **nuovo** socket) | `connect()` avvia la connessione |
| 5 | `recv()`/`send()` sul socket della connessione | `recv()`/`send()` |
| 6 | `close()` | `close()` |

`accept` è il punto sottile: il socket in ascolto resta ad accettare altre connessioni, e ogni connessione accettata è un **nuovo** descrittore, con cui si dialoga. È così che un server serve molti client (spesso facendo `fork`, L5 §4, o un thread per connessione).

### 6.2 Un server TCP in C

Mettiamo insieme la Lezione 9 e la rete: un server che accetta una connessione e rimanda ogni riga in maiuscolo (un *echo* che trasforma).

```c
// server_tcp.c — un server TCP che rimanda in maiuscolo ogni riga (echo)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <arpa/inet.h>
int main(int argc, char *argv[]) {
    int porta = argc > 1 ? atoi(argv[1]) : 7777;
    int s = socket(AF_INET, SOCK_STREAM, 0);          // 1. crea il socket (IPv4, TCP)
    int uno = 1; setsockopt(s, SOL_SOCKET, SO_REUSEADDR, &uno, sizeof uno);
    struct sockaddr_in indirizzo = {0};
    indirizzo.sin_family = AF_INET;
    indirizzo.sin_addr.s_addr = htonl(INADDR_LOOPBACK);   // 127.0.0.1
    indirizzo.sin_port = htons(porta);                    // porta in network byte order
    if (bind(s, (struct sockaddr *)&indirizzo, sizeof indirizzo) < 0) { perror("bind"); return 1; }  // 2
    if (listen(s, 8) < 0) { perror("listen"); return 1; }    // 3. ascolta (coda di 8)
    printf("in ascolto su 127.0.0.1:%d\n", porta); fflush(stdout);
    for (;;) {
        struct sockaddr_in cliente; socklen_t len = sizeof cliente;
        int c = accept(s, (struct sockaddr *)&cliente, &len);   // 4. accetta
        if (c < 0) { perror("accept"); continue; }
        char ip[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &cliente.sin_addr, ip, sizeof ip);   // indirizzo -> testo
        printf("connesso %s:%d\n", ip, ntohs(cliente.sin_port)); fflush(stdout);
        char buf[1024]; ssize_t n;
        while ((n = recv(c, buf, sizeof buf, 0)) > 0) {         // 5. ricevi (flusso!)
            for (ssize_t i = 0; i < n; i++) buf[i] = toupper((unsigned char)buf[i]);
            send(c, buf, n, 0);                                 // 6. invia
        }
        close(c);                                               // 7. chiudi la connessione
        if (argc > 2) break;                                    // "una sola connessione", per i test
    }
    close(s);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o server_tcp server_tcp.c
# term. 1:
$ ./server_tcp 7777
in ascolto su 127.0.0.1:7777
connesso 127.0.0.1:53558
# term. 2:
$ printf 'ciao mondo\n' | nc -N 127.0.0.1 7777
CIAO MONDO
```

Le cose da notare, tutte verificabili con `strace ./server_tcp` (L5): la struttura `struct sockaddr_in` descrive un indirizzo IPv4 + porta, con la porta e l'indirizzo in *network byte order* (da cui `htons`/`htonl`, §2.2); `SO_REUSEADDR` permette di riavviare subito il server sulla stessa porta senza aspettare che il sistema liberi la vecchia (senza, otterresti `bind: Address already in use`); `recv` in un ciclo, perché TCP è un flusso e un messaggio può arrivare in più pezzi (L8); `inet_ntop`/`inet_pton` convertono tra l'indirizzo binario e la sua forma testuale (sono i successori dei vecchi `inet_ntoa`/`inet_aton`, e gestiscono anche IPv6). Questo server serve **una connessione per volta**: per servirne molte insieme, dopo `accept` si fa `fork` (il figlio gestisce `c`, il padre torna ad `accept`), oppure si usa un thread, oppure `select`/`poll`/`epoll` per gestire tutto in un processo solo.

### 6.3 Un client TCP in C

Il client è più corto: niente `bind`/`listen`/`accept`, solo `connect`.

```c
// client_tcp.c — un client TCP: manda una riga e stampa la risposta
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
int main(int argc, char *argv[]) {
    if (argc < 3) { fprintf(stderr, "uso: %s IP PORTA [messaggio]\n", argv[0]); return 2; }
    int s = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in srv = {0};
    srv.sin_family = AF_INET;
    srv.sin_port = htons(atoi(argv[2]));
    if (inet_pton(AF_INET, argv[1], &srv.sin_addr) != 1) { fprintf(stderr, "IP non valido\n"); return 1; }
    if (connect(s, (struct sockaddr *)&srv, sizeof srv) < 0) { perror("connect"); return 1; }
    const char *msg = argc > 3 ? argv[3] : "ciao\n";
    send(s, msg, strlen(msg), 0);
    char buf[1024];
    ssize_t n = recv(s, buf, sizeof buf - 1, 0);
    if (n > 0) { buf[n] = '\0'; printf("risposta: %s", buf); }
    close(s);
    return 0;
}
```

```
$ gcc -Wall -Wextra -o client_tcp client_tcp.c
$ ./client_tcp 127.0.0.1 7777 'salve rete
'
risposta: SALVE RETE
```

Un client che si collega a un indirizzo (invece di legarsi come il server) non specifica la propria porta: il sistema gliene assegna una **effimera** (§3). `connect` fa il three-way handshake (§5) e torna quando la connessione è stabilita, o fallisce con `ECONNREFUSED` se nessuno è in ascolto (il server ha mandato un RST) o `ETIMEDOUT` se l'host non risponde.

### 6.4 Gli stessi, in Python

In Python il modulo `socket` è un involucro sottile sulle stesse chiamate di sistema, ed è quello che pwntools (L8 §8) usa sotto. Lo stesso echo, molto più corto:

```python
# echo.py server|client — l'equivalente Python del §6.2–6.3
import socket, sys
if sys.argv[1] == 'server':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 7779)); s.listen()
    print('in ascolto', flush=True)
    c, chi = s.accept()
    with c:
        while (dati := c.recv(1024)):
            c.sendall(dati.upper())
else:
    c = socket.create_connection(('127.0.0.1', 7779))
    c.sendall(b'ciao da python\n')
    print(c.recv(1024))
    c.close()
```

```
# term. 1:  python3 echo.py server
# term. 2:
$ python3 echo.py client
b'CIAO DA PYTHON\n'
```

`socket.create_connection((host, porta))` fa `socket` + `connect` in una riga, e accetta anche un **nome** al posto di un IP (fa la risoluzione DNS, §9, con `getaddrinfo`, e sceglie IPv4 o IPv6). `sendall` insiste finché tutti i byte sono partiti (a differenza di `send`, che può mandarne meno). È letteralmente ciò che c'è sotto `remote()` di pwntools: quando nella Lezione 8 scrivevi `io = remote('host', 1337)`, succedeva questo.

Per **UDP** si usa `SOCK_DGRAM`, e le funzioni cambiano: niente `connect`/`accept`, ma `sendto(dati, (ip, porta))` e `dati, mittente = recvfrom(n)`, perché ogni datagramma porta con sé il proprio mittente:

```python
# udp.py — eco UDP
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9009))
dati, mittente = s.recvfrom(1024)        # un datagramma intero, con il suo mittente
s.sendto(dati.upper(), mittente)
```

Un `recvfrom` restituisce **esattamente** un datagramma (i confini sono conservati, §4): è la differenza pratica più visibile con TCP.

---

# Parte III — Gli strumenti dalla riga di comando

## 7. `nc`, `ss`, `ping`: esplorare e diagnosticare

### 7.1 `nc` (netcat): il coltellino svizzero

`nc` apre o accetta una connessione TCP (o UDP con `-u`) e collega i suoi standard input e output al socket: tutto ciò che scrivi va al socket, tutto ciò che arriva finisce sul tuo terminale. È il programma con cui ti sei collegato ai servizi nella Lezione 8. Gli usi principali:

```
$ nc 127.0.0.1 7777            # client: collegati e parla (scrivi righe, leggi le risposte)
$ nc -l 7777                   # server: ascolta sulla porta 7777 (il tuo "servizio")
$ nc -l 127.0.0.1 7777         # ascolta solo sul loopback (più sicuro delle prove)
$ printf 'GET / HTTP/1.0\r\n\r\n' | nc example.com 80    # manda una richiesta e stampa la risposta
$ nc -z -w1 127.0.0.1 7777     # -z: prova solo la connessione, non manda dati (per scansione)
```

Due `nc` su due terminali sono una **chat**: `nc -l 7777` su uno, `nc 127.0.0.1 7777` sull'altro, e ciò che scrivi su uno appare sull'altro. È il modo più rapido di capire client e server senza scrivere codice. L'opzione **`-N`** chiude il socket (manda FIN) quando il tuo input finisce, utile negli script; **`-w1`** mette un timeout di un secondo; **`-u`** usa UDP. (Esistono più versioni di `nc` con opzioni leggermente diverse: quella di Debian/Ubuntu è OpenBSD netcat; `ncat` di Nmap ne è una variante più ricca.)

Una scansione delle porte "povera", per sapere quali servizi offre una macchina (**solo sulle tue, o su bersagli autorizzati**):

```
$ for p in 22 80 443 8080; do nc -z -w1 127.0.0.1 $p && echo "$p aperta"; done
```

`nc -z` prova la connessione: se riesce (handshake completato), la porta è aperta; se riceve un RST (§5), è chiusa; se non risponde nulla entro il timeout, è filtrata da un firewall. Per un lavoro serio si usa **`nmap`**, che fa lo stesso in modo molto più veloce e intelligente, riconosce i servizi e le loro versioni, ed è lo strumento del Modulo 7; ma il principio è questo, ed è utile saperlo fare anche a mano.

### 7.2 `ss` e `lsof`: chi ascolta, chi è connesso

Per vedere quali porte sono in ascolto sulla **tua** macchina e quali connessioni sono aperte, si usa `ss` (il successore di `netstat`):

```
$ ss -tlnp            # TCP (-t), in ascolto (-l), numerico (-n), con il processo (-p)
State   Recv-Q  Send-Q  Local Address:Port  Peer Address:Port  Process
LISTEN  0       128     127.0.0.1:7777      0.0.0.0:*          users:(("server_tcp",pid=1234,fd=3))
$ ss -tnp            # le connessioni TCP stabilite (senza -l)
$ ss -ulnp           # le porte UDP in ascolto
```

Le colonne dicono: lo stato (`LISTEN` in ascolto, `ESTAB` connessione stabilita, `TIME-WAIT` appena chiusa), l'indirizzo e la porta locali, quelli del peer (`*` = qualunque, per un socket in ascolto), e il processo. `127.0.0.1:7777` significa "ascolto solo sul loopback"; `0.0.0.0:7777` (o `*:7777`) "ascolto su tutte le interfacce", raggiungibile dalla rete — il che, per un servizio di prova, è di solito un errore (L8, Esercizio 11). Dove `ss` non c'è, `netstat -tlnp` fa lo stesso, e `lsof -i :7777` elenca i processi che usano quella porta. Sono i primi comandi quando un servizio "non risponde": è davvero in ascolto? su quale indirizzo? quale processo?

### 7.3 `ping` e `traceroute`

`ping host` manda pacchetti **ICMP** *echo request* e misura se e in quanto tempo tornano le risposte: dice se un host è raggiungibile e la latenza. `traceroute host` sfrutta il TTL (§2.4) per elencare i router attraversati fino alla destinazione. Sono diagnostici di livello rete: se `ping` funziona ma una connessione TCP no, il problema è più in alto (un firewall sulla porta, un servizio spento); se nemmeno `ping` funziona, il problema è di raggiungibilità. (Molti host e firewall bloccano ICMP, quindi un `ping` che non risponde non significa sempre "spento".)

## 8. `curl`: parlare HTTP senza un browser

`curl` è il client da riga di comando per HTTP (e decine di altri protocolli). È lo strumento con cui esplorerai i servizi web del Modulo 6, e il modo più diretto di vedere che cosa fa una richiesta HTTP.

```
$ curl http://esempio.test/                  # GET: scarica e stampa il corpo
$ curl -s -o pagina.html http://.../          # -s silenzioso, -o salva su file
$ curl -I http://.../                         # solo le intestazioni della risposta (HEAD)
$ curl -v http://.../                         # verbose: mostra richiesta (>) e risposta (<)
$ curl -L http://.../                         # segui i redirect (3xx)
$ curl -X POST -d 'nome=zen&x=1' http://.../  # POST con dati di form
$ curl -H 'Authorization: Bearer XYZ' http://.../   # aggiungi un'intestazione
$ curl -b 'sessione=abc' http://.../          # manda un cookie
$ curl -k https://.../                        # -k: non verificare il certificato TLS (per le prove)
```

L'opzione più istruttiva è **`-v`**, che mostra la conversazione riga per riga, con `>` per ciò che `curl` manda e `<` per ciò che riceve:

```
$ curl -v http://127.0.0.1:8085/
*   Trying 127.0.0.1:8085...
* Connected to 127.0.0.1 port 8085
> GET / HTTP/1.1
> Host: 127.0.0.1:8085
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.13.18
< Content-type: text/html; charset=utf-8
< Content-Length: 457
<
... (il corpo) ...
```

Tutto quello che vedi dopo `Connected` è **testo** che viaggia su una normale connessione TCP: `curl` ha fatto `connect`, mandato le righe `>` e letto le righe `<`. Potresti farlo a mano con `nc` (o con un socket, come nell'Esempio 2), ed è esattamente ciò che fa il §9 del protocollo HTTP. Per HTTPS c'è in più uno strato di cifratura (TLS) tra TCP e HTTP, che `curl` gestisce da sé; `-k` salta la verifica del certificato, comodo per i server di prova con certificati auto-firmati.

---

# Parte IV — I protocolli applicativi

## 9. Il DNS

### 9.1 A che cosa serve

Gli esseri umani usano **nomi** (`example.com`), le macchine **indirizzi** (`93.184.216.34`). Il **DNS** (*Domain Name System*) è l'enorme database distribuito che traduce i primi nei secondi. Quando scrivi un nome in un browser, o passi un nome a `curl` o a `socket.create_connection`, la prima cosa che succede è una **risoluzione DNS**: una domanda "qual è l'indirizzo di questo nome?" e una risposta, quasi sempre su UDP porta 53. La funzione C e Python che la fa è `getaddrinfo`, ed è il motivo per cui `connect` può prendere un nome al posto di un IP.

Il DNS è **gerarchico**: la radice conosce i server dei domini di primo livello (`.com`, `.it`, ...), che conoscono i server dei domini (`example.com`), che conoscono i record dei nomi (`www.example.com`). Il tuo computer di solito non interroga questa gerarchia direttamente, ma un **resolver** (quello del provider, o pubblici come `8.8.8.8`, `1.1.1.1`) che lo fa per lui e mette in cache le risposte per un tempo (il **TTL** del record).

### 9.2 I tipi di record

Una zona DNS contiene **record** di vari tipi; i principali:

| Tipo | Che cosa mappa | Esempio |
|---|---|---|
| **A** | nome → indirizzo IPv4 | `example.com. A 93.184.216.34` |
| **AAAA** | nome → indirizzo IPv6 | `example.com. AAAA 2606:2800:...` |
| **CNAME** | nome → altro nome (alias) | `www.example.com. CNAME example.com.` |
| **MX** | dominio → server di posta | `example.com. MX 10 mail.example.com.` |
| **NS** | dominio → server DNS autoritativi | `example.com. NS a.iana-servers.net.` |
| **TXT** | nome → testo libero | verifiche, SPF, e... flag nelle CTF |
| **PTR** | indirizzo → nome (DNS inverso) | `34.216.184.93.in-addr.arpa. PTR ...` |

### 9.3 Interrogare il DNS

Lo strumento principale è **`dig`**; `host` è più conciso, e `getent hosts` usa la risoluzione del sistema (che non è solo DNS: consulta anche `/etc/hosts`).

```
$ dig +short example.com A           # solo le risposte
93.184.216.34
$ dig example.com MX                 # i server di posta
$ dig +short example.com TXT         # i record di testo (occhio: a volte ci nascondono le flag)
$ host example.com                    # forma breve: indirizzi e mail server
$ dig -x 93.184.216.34               # DNS inverso (record PTR)
$ getent hosts example.com            # la risoluzione del sistema (DNS + /etc/hosts)
$ cat /etc/hosts                      # le corrispondenze statiche locali, consultate per prime
```

In Python, la stessa risoluzione del sistema:

```python
>>> import socket
>>> socket.gethostbyname('localhost')
'127.0.0.1'
>>> socket.getaddrinfo('localhost', 80, type=socket.SOCK_STREAM)
[(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('127.0.0.1', 80))]
```

### 9.4 Il DNS in sicurezza

Il DNS è, al tempo stesso, un bersaglio e uno strumento. Un bersaglio, perché è stato pensato senza autenticazione: chi può rispondere prima del server vero può mandarti all'indirizzo sbagliato (*DNS spoofing*/*cache poisoning*), ed è il motivo di DNSSEC e del DNS cifrato (DoH/DoT). Uno strumento, perché nelle sfide: i record **TXT** sono un nascondiglio classico per flag e indizi; l'elenco dei sottodomini (`dev.`, `admin.`, `backup.`) di un bersaglio è spesso il primo passo della ricognizione (*subdomain enumeration*); e l'*exfiltrazione via DNS* (nascondere dati nelle query DNS, che spesso escono anche da reti molto chiuse) è una tecnica sia d'attacco sia di CTF. Per ora ti basti saper interrogare il DNS e sapere che cosa risponde.

## 10. HTTP

### 10.1 La forma di una richiesta e di una risposta

**HTTP** (*HyperText Transfer Protocol*) è il protocollo del web, ed è, nella sua forma classica (1.0 e 1.1), **testo** che viaggia su TCP (porta 80; su TLS è HTTPS, porta 443). Una transazione è una **richiesta** del client e una **risposta** del server. La richiesta:

```
GET /pagina.html HTTP/1.1          <- riga di richiesta: METODO percorso VERSIONE
Host: example.com                  <- intestazioni: Nome: valore, una per riga
User-Agent: curl/8.5.0
Accept: */*
                                   <- una riga vuota: fine delle intestazioni
```

(Un POST avrebbe, dopo la riga vuota, un **corpo** con i dati, e le intestazioni `Content-Length` e `Content-Type` a descriverlo.) La risposta ha la stessa struttura:

```
HTTP/1.1 200 OK                    <- riga di stato: VERSIONE codice messaggio
Content-Type: text/html; charset=utf-8
Content-Length: 457
Server: ...
                                   <- riga vuota
<!doctype html> ...                <- il corpo (lungo Content-Length byte)
```

Ogni riga finisce con `\r\n` (CR LF, L7 §9.2), e la riga vuota (`\r\n\r\n`) separa le intestazioni dal corpo: è la marca che cerchi con `recvuntil(b'\r\n\r\n')` quando parli HTTP a mano (L8). Lo vedi puntuale facendo la richiesta con un socket, come nell'Esempio 2.

### 10.2 Metodi, codici di stato, intestazioni

I **metodi** dicono che cosa fare: **GET** (richiedi una risorsa, senza effetti), **POST** (invia dati, con effetti), **PUT**/**DELETE** (crea/elimina), **HEAD** (come GET ma solo le intestazioni). I **codici di stato** sono a tre cifre, raggruppati per la prima:

| Classe | Significato | Esempi |
|---|---|---|
| **1xx** | informativo | 100 Continue |
| **2xx** | successo | **200** OK, 201 Created, 204 No Content |
| **3xx** | redirezione | **301** Moved Permanently, 302 Found, 304 Not Modified |
| **4xx** | errore del client | **400** Bad Request, **401** Unauthorized, **403** Forbidden, **404** Not Found |
| **5xx** | errore del server | **500** Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

Le **intestazioni** portano i metadati: `Host` (quale sito, indispensabile in HTTP/1.1 perché più siti condividono un IP), `Content-Type` (il formato del corpo: `text/html`, `application/json`), `Content-Length` (quanti byte), `User-Agent` (il programma client), `Location` (dove reindirizza un 3xx), `Authorization` (le credenziali), `Set-Cookie`/`Cookie` (lo stato di sessione). I **cookie** sono il modo in cui HTTP, che di per sé non ha memoria tra una richiesta e l'altra (*stateless*), tiene traccia di una sessione: il server manda `Set-Cookie: sessione=abc`, e il browser lo rimanda a ogni richiesta successiva con `Cookie: sessione=abc`. Manipolare metodi, intestazioni e cookie è metà del Modulo 6; qui ti basti riconoscerli in una richiesta che costruisci a mano. HTTP/2 e HTTP/3 cambiano la codifica sul filo (binaria, e su UDP per HTTP/3), ma i concetti — metodi, stati, intestazioni — restano.

---

# Parte V — Guardare il traffico

## 11. `tcpdump` e Wireshark

### 11.1 Catturare

Finora abbiamo guardato la rete dal punto di vista di un programma. Gli **analizzatori di pacchetti** la guardano dal filo: catturano i frame che passano su un'interfaccia e li mostrano, intestazione per intestazione (§1.2). È una competenza centrale per la difesa e per una categoria di sfide (*network forensics*): ti danno una cattura, un file `.pcap`, e la flag è nascosta nel traffico.

**`tcpdump`** è lo strumento da riga di comando (serve essere root o avere i permessi di cattura):

```
$ sudo tcpdump -i lo -n port 7777            # cattura sul loopback, porta 7777, senza risolvere i nomi
$ sudo tcpdump -i eth0 -n host 192.0.2.10    # tutto il traffico da/verso un host
$ sudo tcpdump -i lo -w cattura.pcap port 80 # salva su file, da aprire poi con Wireshark
$ tcpdump -r cattura.pcap -n -A              # rileggi un file, mostra il payload in ASCII (-A)
```

L'output di `tcpdump` per il three-way handshake del §5 è qualcosa come:

```
IP 127.0.0.1.53558 > 127.0.0.1.7777: Flags [S], seq 12345, ...        <- SYN
IP 127.0.0.1.7777 > 127.0.0.1.53558: Flags [S.], seq 67890, ack 12346 <- SYN+ACK
IP 127.0.0.1.53558 > 127.0.0.1.7777: Flags [.], ack 67891             <- ACK
IP 127.0.0.1.53558 > 127.0.0.1.7777: Flags [P.], ... length 11        <- dati ("ciao mondo\n")
IP 127.0.0.1.7777 > 127.0.0.1.53558: Flags [P.], ... length 11        <- risposta ("CIAO MONDO\n")
IP 127.0.0.1.53558 > 127.0.0.1.7777: Flags [F.], ...                  <- FIN
```

`[S]` è SYN, `[S.]` SYN+ACK (il punto è l'ACK), `[.]` solo ACK, `[P.]` dati (PUSH+ACK), `[F.]` FIN, `[R]` RST. Riconoscere questa sequenza è leggere lo stato di una connessione a occhio: hai appena visto "dal filo" l'handshake del §5 e l'echo del §6.

### 11.2 Leggere con Wireshark

**Wireshark** è l'analizzatore grafico, e per leggere una cattura è insostituibile. Quello che devi saper fare:
- **aprire un `.pcap`** e scorrere i pacchetti, ognuno con le sue intestazioni annidate (Ethernet, IP, TCP, e il protocollo applicativo), che corrispondono all'incapsulamento del §1.2;
- **filtrare**: `tcp.port == 80`, `ip.addr == 192.0.2.10`, `http`, `dns`, `tcp.flags.syn == 1` — i filtri di Wireshark sono il modo di trovare l'ago nel pagliaio di una cattura grande;
- **seguire un flusso** (*Follow → TCP Stream*): Wireshark ricostruisce il flusso di byte di una connessione (ricordi: TCP è un flusso, i pacchetti sono solo il trasporto), e te lo mostra come un dialogo, client e server a colori diversi. È qui che la flag di una sfida *pcap* salta fuori: una password in chiaro in una richiesta HTTP, un file trasferito, un comando;
- **esportare oggetti** (*File → Export Objects → HTTP*): estrae i file trasferiti via HTTP dalla cattura.

La regola della *network forensics*: un protocollo in **chiaro** (HTTP, FTP, Telnet, DNS) mostra tutto a chi cattura — credenziali comprese. È il motivo per cui oggi quasi tutto è cifrato (HTTPS, SSH), e in una cattura di traffico cifrato vedrai gli indirizzi, le porte e i tempi, ma non il contenuto. Molte sfide usano di proposito un protocollo in chiaro, o ti danno la chiave per decifrare il TLS.

---

# Parte VI — La pratica

## 12. Esempi svolti

### Esempio 1 — Una chat con due `nc`

Il modo più rapido di toccare con mano client e server, senza scrivere codice. Su un terminale fai il server, sull'altro il client, e scrivi:

```
# term. 1 (server)                       # term. 2 (client)
$ nc -l 127.0.0.1 7777                    $ nc 127.0.0.1 7777
ciao dal client   <----------------       ciao dal client
ciao dal server    ---------------->       ciao dal server
```

Ogni riga che scrivi su un terminale appare sull'altro: è una connessione TCP bidirezionale, e `nc` collega il tuo standard input e output al socket. **Che cosa imparare.** Il server **aspetta** (`-l`), il client **inizia** (§3); una volta connessi, sono simmetrici. Se chiudi un lato con Ctrl-D (EOF), l'altro riceve la chiusura (FIN, §5) e la sua `recv` dà 0. È lo stesso dialogo che in Python facevi con pwntools, qui senza una riga di codice.

### Esempio 2 — HTTP a mano, con un socket

`curl` fa comodo, ma HTTP è solo testo su TCP. Scriviamo la richiesta a mano, con un socket Python, per vederlo:

```python
# http_grezzo.py — una richiesta HTTP con un socket, senza librerie HTTP
import socket, sys
host, percorso = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else '/')
s = socket.create_connection((host, 80))
richiesta = f'GET {percorso} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n'
s.sendall(richiesta.encode())
risposta = b''
while (c := s.recv(4096)):          # TCP è un flusso: leggo finche' il server non chiude
    risposta += c
s.close()
testa, _, corpo = risposta.partition(b'\r\n\r\n')     # la riga vuota separa testa e corpo
righe = testa.split(b'\r\n')
print('STATO:', righe[0].decode())
print('INTESTAZIONI:', len(righe) - 1)
print('CORPO:', len(corpo), 'byte')
```

```
# contro un server locale (python3 -m http.server 8080):   (adatta la porta nel codice)
STATO: HTTP/1.0 200 OK
INTESTAZIONI: 4
CORPO: 281 byte
```

**Che cosa imparare.** Una richiesta HTTP è un pugno di righe terminate da `\r\n`, più una riga vuota; la risposta ha la stessa forma, e `\r\n\r\n` separa le intestazioni dal corpo — la marca che cercavi con `recvuntil` nella Lezione 8. `Connection: close` dice al server di chiudere dopo la risposta, così il `recv` finisce con un EOF e non devo interpretare `Content-Length` per sapere quando fermarmi (che è invece ciò che serve per leggere più risposte sulla stessa connessione). È, in venti righe, quello che `curl` fa per te — e quello che farai nel Modulo 6.

### Esempio 3 — L'endianness della rete, vista

Il *network byte order* (§2.2) non è teoria: si vede impacchettando una porta. In Python, con `struct` (L7, L8 §3.3):

```
>>> import struct
>>> struct.pack('>H', 7777).hex()      # big-endian (rete): il byte alto per primo
'1e61'
>>> struct.pack('<H', 7777).hex()      # little-endian (x86): invertito
'611e'
>>> import socket
>>> socket.htons(7777)                  # host-to-network short: su x86 inverte
24862
>>> hex(24862)
'0x611e'
```

**Che cosa imparare.** La porta 7777 è `0x1e61`. Sul filo deve viaggiare big-endian (`1e 61`); una macchina x86, che è little-endian, la tiene in memoria come `61 1e`. `htons` converte da "ordine della macchina" a "ordine della rete": su x86 inverte i due byte (e `htons(7777)` restituisce 24862, che sono gli stessi byte letti al contrario), su una macchina big-endian non farebbe nulla. È il motivo di `htons(porta)` nel server del §6.2: senza, ascolteresti sulla porta 24862.

### Esempio 4 — Vedere una connessione dal filo

Avvia il server del §6.2 e cattura il traffico mentre un client si collega (serve `tcpdump` e i permessi di cattura):

```
# term. 1:  ./server_tcp 7777
# term. 2:  sudo tcpdump -i lo -n port 7777
# term. 3:  printf 'ciao\n' | nc -N 127.0.0.1 7777
```

`tcpdump` mostra, nell'ordine: `Flags [S]` (il SYN del client), `Flags [S.]` (SYN+ACK del server), `Flags [.]` (ACK del client: handshake finito, §5), poi `Flags [P.] ... length 5` (il client manda "ciao\n"), un altro `[P.] length 5` in senso inverso (il server risponde "CIAO\n"), e infine `[F.]` (la chiusura). **Che cosa imparare.** Hai appena visto, pacchetto per pacchetto, tutto ciò che il §5 e il §6 descrivono: l'apertura in tre tempi, lo scambio di dati, la chiusura. Aprendo la stessa cattura in Wireshark e facendo *Follow TCP Stream*, rivedi gli stessi byte come il dialogo `ciao`/`CIAO`. È il ponte tra "come funziona TCP" e "che cosa c'è sul filo".

## 13. Esercizi

Tre livelli. I **★ Base** si fanno con `nc`, `curl`, `dig`, `ss` e un po' di `struct`. Gli **★★ Intermedio** ti fanno scrivere client e server. Gli **★★★ Sfida** sono analisi e la mini-CTF. Fai tutte le prove su `127.0.0.1` o su bersagli che hai il permesso di toccare: scansionare o collegarsi a macchine altrui senza autorizzazione è illegale (§3, e la regola di fondo del corso). Le soluzioni, provate su loopback con Python 3.13, gcc 13.3, `nc` e `curl`, sono in `Soluzioni.md`.

### ★ Base

**1. Indirizzi e maschere.** Senza strumenti, poi verifica: (a) scrivi i quattro byte di `192.168.1.130` in binario. (b) Per la rete `192.168.1.0/24`: quanti host? qual è il broadcast? `192.168.1.130` e `192.168.1.200` sono sulla stessa rete? (c) E per `/26` (maschera `255.255.255.192`)? In quale sottorete `/26` cade `192.168.1.130`? (d) Che cos'è `127.0.0.1`, e perché i pacchetti verso di esso non escono dalla scheda di rete? (e) `10.0.0.5`, `172.20.1.1`, `192.168.0.1`, `8.8.8.8`: quali sono privati e quali pubblici?

**2. Porte e ordine dei byte.** (a) A quali servizi corrispondono le porte 22, 53, 80, 443, 3306? (b) Con `struct` in Python, impacchetta la porta 1337 in big-endian e in little-endian, e mostra i byte in esadecimale. Quale va "sul filo"? (c) Che cosa fa `socket.htons(1337)`, e perché restituisce quel numero su una macchina x86? (d) Perché una connessione TCP è identificata da **quattro** valori e non da due? Come fa il tuo browser ad avere più connessioni verso lo stesso sito?

**3. Esplorare con `nc`.** (a) Avvia `nc -l 127.0.0.1 9999` su un terminale e collegati con `nc 127.0.0.1 9999` sull'altro: scrivi righe nei due sensi. (b) Che cosa succede, dal lato client, se chiudi il server con Ctrl-C? E se chiudi il client con Ctrl-D? (c) Con `nc -z -w1`, scrivi un ciclo di shell che prova le porte da 7770 a 7780 su `127.0.0.1` e stampa quelle aperte (avvia prima un `nc -l` su una di esse per avere un "aperto"). (d) Prova `nc -z -w1 127.0.0.1 1` (porta quasi certamente chiusa): come distingue `nc` una porta chiusa (RST) da una filtrata (nessuna risposta)?

**4. `curl` e HTTP.** Avvia un server locale con `python3 -m http.server 8080`. (a) `curl -v http://127.0.0.1:8080/`: quali righe sono la richiesta (`>`) e quali la risposta (`<`)? Qual è il codice di stato? (b) `curl -I`: che cosa cambia, e quale metodo HTTP usa? (c) Chiedi un file che non esiste: che codice di stato ottieni? (d) Con `nc -l 127.0.0.1 8086` su un terminale e `curl -X POST -d 'a=1&b=2' -H 'X-Prova: ciao' http://127.0.0.1:8086/invia` sull'altro, guarda la **richiesta** che `curl` ha mandato: trova la riga di richiesta, l'intestazione `Host`, la tua `X-Prova`, `Content-Length` e il corpo.

**5. DNS.** (Serve la risoluzione dei nomi; se la tua macchina di prova non ha rete, usa `/etc/hosts` e `localhost`.) (a) `dig +short <un dominio> A` e `AAAA`: che differenza c'è? (b) `dig <dominio> MX`: a che cosa serve un record MX? (c) `dig +short <dominio> TXT`: che cosa c'è di solito nei record TXT, e perché nelle CTF conviene guardarli? (d) `getent hosts localhost` e `cat /etc/hosts`: che cos'è `/etc/hosts`, e perché viene consultato **prima** del DNS? (e) In Python, `socket.gethostbyname('localhost')` e `socket.getaddrinfo('localhost', 80)`: che cosa restituiscono?

### ★★ Intermedio

**6. Un client TCP.** Scrivi, in Python o in C, un client che si collega a un indirizzo e a una porta dati, manda una riga letta dallo standard input, stampa la risposta e chiude. (a) Provalo contro il server echo del §6. (b) Falso contro `python3 -m http.server 8080` mandando `GET / HTTP/1.0\r\n\r\n`: che cosa ricevi? (c) Aggiungi la lettura "fino alla chiusura" (come l'Esempio 2): perché un solo `recv` potrebbe non bastare (L8 §6.2, §4)? (d) Gestisci il caso in cui la connessione è rifiutata (`ECONNREFUSED`): che cosa significa?

**7. Un server TCP che serve più client.** Parti dal server echo del §6.2 (C) o §6.4 (Python). (a) Verifica che, mentre un client è connesso, un secondo client resta in attesa (il server serve uno per volta). (b) Modificalo per servirne molti insieme: in C con `fork` dopo `accept` (il figlio gestisce la connessione, il padre torna ad `accept`, L5 §4); in Python con un thread per connessione, o con `socketserver.ThreadingTCPServer`. (c) Prova con due client contemporanei. (d) Perché il server deve chiudere, nel padre, il descrittore della connessione dopo il `fork` (e il figlio quello in ascolto)? Che cosa succede ai descrittori con `fork` (L5 §4, L9)?

**8. Un server UDP.** Scrivi un server UDP che riceve un datagramma, e risponde al mittente con il datagramma invertito (byte al contrario). (a) Provalo con un client UDP tuo e con `nc -u`. (b) Che cosa cambia rispetto a TCP nelle chiamate che usi (niente `connect`/`accept`/`listen`; `recvfrom`/`sendto`)? (c) Manda due datagrammi di fila: arrivano come due `recvfrom` distinti o si fondono? Perché (§4)? (d) Che cosa succede se il client manda un datagramma e il server non è avviato: ricevi un errore come con TCP? Perché no?

**9. Il tuo mini-`curl`.** Scrivi `micurl.py URL` che: estrae host, porta (default 80) e percorso dall'URL; apre una connessione; manda una richiesta `GET` HTTP/1.0 con l'intestazione `Host`; legge tutta la risposta; separa intestazioni e corpo sulla riga vuota; e stampa il codice di stato, le intestazioni come dizionario, e la lunghezza del corpo. (a) Provalo contro un server locale. (b) Aggiungi il supporto ai **redirect**: se lo stato è 3xx, segui l'intestazione `Location` (come `curl -L`). (c) Perché devi leggere **fino alla chiusura** (o interpretare `Content-Length`), e non puoi fidarti di un solo `recv`? (d) Che cosa dovresti aggiungere per gestire HTTPS, e perché è molto più complicato (un accenno: TLS tra TCP e HTTP)?

**10. Leggere lo stato della rete.** Sul tuo sistema: (a) avvia il server del §6 e, con `ss -tlnp` (o `netstat -tlnp`, o `lsof -i`), trova la riga del tuo server: su quale indirizzo e porta ascolta? Quale processo? (b) Mentre un client è connesso, con `ss -tnp` trova la connessione: quali sono le quattro coordinate (IP e porta di origine e destinazione)? (c) Modifica il server perché ascolti su `0.0.0.0` invece che su `127.0.0.1`: come cambia la riga di `ss`, e perché su una macchina in rete sarebbe pericoloso (L8, Esercizio 11)? (d) Che cosa significa lo stato `TIME-WAIT` che vedi dopo aver chiuso una connessione, e perché `SO_REUSEADDR` aiuta a riavviare subito il server (§6.2)?

### ★★★ Sfida

**11. Mini-CTF: lo sportello di rete.** Esegui `bash setup_sfida.sh`: crea `~/l10_sfida/` con `servizio.py` e `LEGGIMI.txt`. Avvia il servizio con `python3 servizio.py --porta 8100`: apre **tre** servizi (su 8100, 8101, 8102) e crea un file `cattura.pcap`. La flag `L10{...}` è in quattro pezzi:
- **Pezzo 1**: collegati con `nc` alla porta TCP 8100 e leggi quello che ti dice.
- **Pezzo 2**: c'è una pagina web sulla porta 8101. La radice `/` non ha il pezzo, ma ti **reindirizza** altrove: segui il redirect (guarda l'intestazione `Location` con `curl -v` o `-I`, oppure usa `curl -L`).
- **Pezzo 3**: c'è uno sportello **UDP** sulla porta 8102. Mandagli il datagramma giusto (ti dice lui che cosa vuole) e leggi la risposta. Usa un socket UDP in Python o `nc -u`.
- **Pezzo 4**: è nel file `cattura.pcap`. Aprilo con Wireshark (*Follow TCP Stream*) o leggilo con `tcpdump -r cattura.pcap -A`; se non hai nessuno dei due, `strings cattura.pcap` basta per questo caso.

Scrivi, per ogni pezzo, lo strumento usato e perché, e ricomponi la flag. Poi, per approfondire: mentre risolvi i pezzi 1–3, cattura il traffico con `tcpdump -i lo -n` e riconosci l'handshake e i dati di ciascuno.

**12. Network forensics su una cattura.** Prendi la `cattura.pcap` della sfida (o creane una tua con `tcpdump -i lo -w mia.pcap` mentre fai una richiesta HTTP a un server locale). (a) Con `tcpdump -r ... -n`, conta i pacchetti e identifica l'handshake (`[S]`, `[S.]`, `[.]`). (b) Con `-A`, trova il payload in chiaro: la richiesta e la risposta HTTP. (c) In Wireshark, usa *Follow TCP Stream* e il filtro `http`: ricostruisci il dialogo. (d) Spiega perché, se la cattura fosse di una connessione **HTTPS**, non vedresti il contenuto, e che cosa vedresti comunque (indirizzi, porte, dimensioni, tempi).

**13. Un servizio e il suo client, dall'inizio.** Progetta un piccolo protocollo testuale a righe su TCP (per esempio: il client manda `SOMMA 3 4`, il server risponde `7`; `PING` → `PONG`; `QUIT` → chiude) e scrivi **sia** il server (serve più client, Esercizio 7) **sia** il client. (a) Documenta il protocollo in tre righe (quali comandi, quali risposte, come si riconosce la fine di un messaggio). (b) Gestisci gli errori: comando sconosciuto, argomenti mancanti (il server non deve crollare, L8 regola 5). (c) Prova il tuo server con `nc` (è un client generico!) e il tuo client contro `nc -l` (un server generico): è la prova che il protocollo è ben definito e indipendente dall'implementazione. (d) Cattura una sessione con `tcpdump` e ritrova i tuoi comandi nel traffico: sono in chiaro?

### Allenamento

Questa lezione apre i Moduli 6 (web) e 7 (reti e traffico). Su pwn.college, i moduli *Talking Web* e *Intercepting Communication* del percorso CSE 365 ti fanno costruire richieste HTTP a mano e analizzare il traffico; il modulo di networking insegna i socket a basso livello. Installa **Wireshark** e prendi l'abitudine di catturare il traffico delle tue stesse prove: vedere ciò che fai è il modo più rapido di capirlo. Fuori da pwn.college, su picoCTF le categorie *Web Exploitation* (a partire da `curl`, intestazioni e cookie) e *Forensics* (le sfide `.pcap`, da aprire in Wireshark) sono il terreno naturale di questa lezione; e TryHackMe/HackTheBox hanno interi percorsi introduttivi di *networking*. La regola, come sempre: queste tecniche solo sulle tue macchine, sui laboratori di allenamento, e sui bersagli di una gara.

## 14. Domande di autoverifica

1. Quali sono i quattro livelli del modello TCP/IP, e che cosa fa ciascuno? Che cos'è l'incapsulamento?
2. Com'è fatto un indirizzo IPv4? Che cosa dice la notazione `/24`? Quanti host ha una `/24`, e qual è il suo broadcast?
3. Che cosa sono `127.0.0.1` e gli indirizzi privati (`10/8`, `172.16/12`, `192.168/16`)? Perché esistono?
4. Che cos'è il *network byte order*? A che cosa servono `htons`/`ntohl`? Che cosa succede se le dimentichi?
5. Che cos'è una porta? Perché una connessione TCP è identificata da quattro valori? Che cosa sono le porte ben note e quelle effimere?
6. Differenze tra TCP e UDP: connessione, affidabilità, ordine, confini dei messaggi. Quale usa HTTP, quale il DNS, e perché?
7. Descrivi il three-way handshake con i flag SYN/ACK. Come si chiude una connessione (FIN)? Che cos'è un RST, e quando lo ricevi?
8. Perché una `recv` su TCP può restituire mezzo messaggio o due messaggi insieme, mentre una `recvfrom` su UDP restituisce esattamente un datagramma?
9. Che cos'è un socket? Elenca le chiamate di sistema di un server (`socket`, `bind`, `listen`, `accept`, ...) e di un client (`socket`, `connect`, ...). Perché `accept` restituisce un **nuovo** descrittore?
10. Come fa un server a servire più client contemporaneamente? (Tre modi.)
11. A che cosa servono `nc`, `ss`/`netstat`, `ping`? Come si fa una scansione di porte "povera" con `nc -z`, e come distingue aperta/chiusa/filtrata?
12. Che cosa fa `curl -v`? Come riconosci la richiesta e la risposta? Come mandi un POST, un'intestazione, un cookie?
13. Che cos'è il DNS? Che cosa mappano i record A, AAAA, CNAME, MX, TXT? Con quali comandi li interroghi? Perché i record TXT interessano nelle CTF?
14. Com'è fatta una richiesta HTTP? E una risposta? Che cosa separa le intestazioni dal corpo? Che cosa indicano i codici 2xx, 3xx, 4xx, 5xx?
15. Che cosa sono i cookie e perché esistono (HTTP è *stateless*)? Quali intestazioni li portano?
16. Che cosa fanno `tcpdump` e Wireshark? Come riconosci l'handshake nell'output di `tcpdump`? Che cos'è *Follow TCP Stream*?
17. Perché un protocollo "in chiaro" (HTTP, FTP, Telnet) è un problema in una cattura di traffico? Che cosa vedi, e che cosa no, in una cattura di traffico cifrato (HTTPS)?
18. Collega: un socket è un descrittore (quale lezione?); i byte sul filo hanno un ordine (quale?); un `recv` non dà messaggi (quale?). Come si tiene tutto insieme?

## 15. Riepilogo

- La rete è organizzata in **livelli** (TCP/IP: applicazione, trasporto, rete, collegamento); ogni livello aggiunge la sua intestazione scendendo (**incapsulamento**) e la toglie salendo. È ciò che vedi in Wireshark.
- Un **indirizzo IPv4** è 32 bit in *dotted decimal*; la **maschera `/n`** divide rete e host (`/24` = 256 indirizzi); `127.0.0.1` è il loopback, `10/8`/`172.16/12`/`192.168/16` sono privati. IPv6 ha 128 bit (`::1` il loopback). I numeri di rete sono in **big-endian** (*network byte order*): `htons`/`htonl` convertono.
- Una **porta** (16 bit) identifica il programma; la coppia (IP, porta) un endpoint, e una connessione TCP i **quattro** valori di origine e destinazione. Porte ben note (0–1023), registrate, effimere. Modello **client-server**: il server ascolta, il client inizia.
- **TCP** = flusso di byte affidabile e ordinato, con handshake (SYN/SYN-ACK/ACK) e chiusura (FIN); un **RST** chiude bruscamente. È un **flusso**: `recv` dà "quanto è arrivato", i confini li ricostruisci tu (L8). **UDP** = datagrammi senza connessione né garanzie, ma con i confini conservati; è del DNS, NTP, streaming.
- Un **socket** è un descrittore di file (L4, L9). Server: `socket`, `bind`, `listen`, `accept` (nuovo descrittore per ogni connessione), `recv`/`send`, `close`. Client: `socket`, `connect`, `recv`/`send`, `close`. In Python, `socket` e `create_connection` (ciò che c'è sotto pwntools); UDP usa `SOCK_DGRAM`, `sendto`/`recvfrom`. Più client: `fork`, thread, o `select`/`poll`/`epoll`.
- Strumenti: **`nc`** (client/server/chat/scansione), **`curl`** (HTTP, con `-v` per vedere la conversazione), **`ss`**/`netstat`/`lsof` (chi ascolta, chi è connesso), **`ping`**/`traceroute` (raggiungibilità, percorso).
- Il **DNS** traduce nomi in indirizzi (UDP 53); gerarchico, con cache (TTL); record **A**/**AAAA**/**CNAME**/**MX**/**NS**/**TXT**/**PTR**; si interroga con `dig`/`host`/`getent` e, in Python, `getaddrinfo`. È bersaglio (spoofing) e strumento (TXT, enumerazione, exfiltrazione) nelle CTF.
- **HTTP** è testo su TCP (porta 80; HTTPS su TLS, 443): richiesta (metodo, percorso, intestazioni, riga vuota, corpo) e risposta (stato, intestazioni, corpo), righe con `\r\n`, `\r\n\r\n` tra testa e corpo. Metodi (GET, POST, ...), codici (2xx/3xx/4xx/5xx), intestazioni (`Host`, `Content-Type`, `Location`, `Set-Cookie`). I **cookie** danno memoria a un protocollo *stateless*.
- **`tcpdump`** e **Wireshark** catturano i pacchetti e mostrano le intestazioni annidate; si riconoscono i flag TCP (`[S]`, `[S.]`, `[.]`, `[F.]`, `[R]`), si filtra, si **segue un flusso**. I protocolli in chiaro mostrano tutto a chi cattura (il motivo della cifratura); le sfide `.pcap` sono una categoria a sé.
- Tutto il Modulo 1 si tiene qui: il socket è il descrittore di L4/L9, i byte sul filo sono quelli di L7, il dialogo è quello di L8. Da qui si va al web (Modulo 6) e alle reti (Modulo 7).

## 16. Fonti

- **W. Richard Stevens, Kevin R. Fall**, *TCP/IP Illustrated, Volume 1: The Protocols*: il riferimento classico, che mostra i protocolli attraverso catture reali (lo spirito del §11). Per i socket, **Stevens, Fenner, Rudoff**, *UNIX Network Programming, Vol. 1*.
- **Andrew S. Tanenbaum, David J. Wetherall**, *Computer Networks*, o **Kurose, Ross**, *Computer Networking: A Top-Down Approach*: due testi universitari standard per il modello a livelli, IP, TCP/UDP, DNS, HTTP (§1–10).
- **Chris Sanders**, *Practical Packet Analysis* (con Wireshark): il libro indicato nel programma del modulo, dedicato proprio a catturare e leggere il traffico (§11).
- **Justin Seitz, Tim Arnold**, *Black Hat Python*, cap. 2–3: socket TCP/UDP in Python, un *netcat* e un proxy scritti da sé — l'equivalente in codice del §6.
- **Le RFC**: 791 (IPv4), 793/9293 (TCP), 768 (UDP), 1035 (DNS), 9110/9112 (HTTP), 1918 (indirizzi privati). Sono le definizioni ufficiali; si leggono quando un dettaglio conta davvero.
- **Documentazione degli strumenti**: `man nc`, `man curl` (e `curl --manual`), `man ss`, `man tcpdump`, `man dig`; la *Socket Programming HOWTO* di Python e il modulo `socket`; la Wireshark User's Guide e la *Wireshark Wiki* (i filtri di visualizzazione).
- **pwn.college**, CSE 365, i moduli *Talking Web* e *Intercepting Communication*, e le trascrizioni 139/142/145/147 (*Intercepting Communications*); per il traffico, i tutorial di Wireshark di *Malware-Traffic-Analysis.net*.
- **MITRE CWE/ATT&CK**: CWE-319 (trasmissione di dati sensibili in chiaro), CWE-311 (mancanza di cifratura); le tecniche ATT&CK di *Network Sniffing* (T1040), *Exfiltration Over Alternative Protocol* / DNS (T1048), *Adversary-in-the-Middle* (T1557).

## 17. La fine del Modulo 1 e la simulazione di gara

Con questa lezione il **Modulo 1 — Fondamenti** è completo. In dieci lezioni hai costruito le fondamenta di tutto il resto del corso: la riga di comando e il file system (1–2), la manipolazione del testo (3), i flussi, i processi e l'ambiente (4–5), utenti e permessi (6), la rappresentazione dei dati (7), l'interazione automatizzata con i programmi in Python e pwntools (8), il C e la toolchain (9), e le reti (10). Sono le competenze che le gare danno per scontate e che i moduli successivi useranno in continuazione: il *reverse engineering* (Modulo 3) parte dal C e da `gdb` della Lezione 9; lo sfruttamento della memoria (Modulo 4) dallo stack e dagli overflow che hai già intravisto; la crittografia (Modulo 5) dai byte e dallo XOR della Lezione 7; il web (Modulo 6) da HTTP e `curl`; le reti (Modulo 7) da questa lezione.

**Il prossimo passo è la simulazione di gara** (Lezione 11): tre ore, dieci-dodici sfide in stile *jeopardy* che combinano gli argomenti del modulo — *misc* (navigazione, scripting, manipolazione di testo), *encoding* (hex, base64, XOR), interazione con i programmi (pwntools), e rete (`nc`, `curl`, una cattura `.pcap`). È il momento in cui le competenze separate diventano la capacità di risolvere un problema vero sotto tempo. Prima di affrontarla, vale la pena rifare le mini-CTF delle lezioni (le flag `L1{...}`–`L10{...}`) senza guardare le soluzioni: se le risolvi tutte in scioltezza, sei pronto.
