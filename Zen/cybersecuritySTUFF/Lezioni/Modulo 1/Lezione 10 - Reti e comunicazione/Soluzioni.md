# Modulo 1 — Lezione 10: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Tutto è stato provato su `127.0.0.1` con Python 3.13, gcc 13.3, `nc` OpenBSD e `curl` 8.5 su Linux x86-64. Le prove che richiedono una rete o DNS veri (Esercizio 5) vanno fatte su una macchina con accesso a Internet. I riferimenti `§` rimandano a `Lezione.md`. Fai tutto solo sulle tue macchine o su bersagli autorizzati.

## ★ Base

**1.**
(a) `192.168.1.130` = `11000000 10101000 00000001 10000010`.
(b) `/24`: 256 indirizzi, di cui 254 assegnabili agli host (`.0` è la rete, `.255` il broadcast); broadcast `192.168.1.255`. `192.168.1.130` e `192.168.1.200` hanno lo stesso prefisso `192.168.1`, quindi **sì**, stessa rete.
(c) `/26` = 26 bit di rete, 6 di host → blocchi di 64 indirizzi: `.0–.63`, `.64–.127`, `.128–.191`, `.192–.255`. `192.168.1.130` cade in **`192.168.1.128/26`** (host `.128–.191`, broadcast `.191`); `192.168.1.200` cade in `192.168.1.192/26`: con la `/26` **non** sono più sulla stessa sottorete.
(d) `127.0.0.1` è il *loopback*, "questa macchina"; lo stack di rete riconosce `127.0.0.0/8` e gestisce i pacchetti internamente, senza passarli a una scheda fisica.
(e) Privati: `10.0.0.5` (`10/8`), `172.20.1.1` (`172.16/12`), `192.168.0.1` (`192.168/16`); pubblico: `8.8.8.8`.

**2.**
(a) 22 SSH, 53 DNS, 80 HTTP, 443 HTTPS, 3306 MySQL.
(b) `struct.pack('>H', 1337).hex()` = `'0539'` (big-endian); `struct.pack('<H', 1337).hex()` = `'3905'` (little-endian). Sul filo va il **big-endian** (`05 39`), il *network byte order* (§2.2).
(c) `socket.htons(1337)` = **13829**: su x86 (little-endian) inverte i due byte, e `0x3905` = 13829; è lo stesso valore letto "al contrario" rispetto a 1337 = `0x0539`.
(d) Perché due endpoint possono avere più connessioni insieme: ciò che distingue una connessione è la quadrupla (IP origine, porta origine, IP destinazione, porta destinazione). Il browser apre più connessioni allo stesso sito (stessa destinazione) usando una **porta effimera** diversa per ognuna (§3).

**3.**
(a) Chat bidirezionale: ciò che scrivi su un lato appare sull'altro. (b) Se chiudi il server con Ctrl-C, il client riceve la chiusura (la sua `recv` dà 0 / `nc` esce); se chiudi il client con Ctrl-D, manda EOF/FIN e (con `-N`) chiude il socket, e il server lo vede chiudersi. (c)

```bash
for p in $(seq 7770 7780); do nc -z -w1 127.0.0.1 "$p" 2>/dev/null && echo "$p aperta"; done
```

(d) Porta **chiusa**: nessun server in ascolto, il sistema risponde con un **RST** e `nc -z` fallisce subito; porta **filtrata**: un firewall scarta il SYN senza rispondere, e `nc -z` fallisce solo allo scadere del timeout (`-w1`). La differenza è "risposta immediata (RST)" contro "silenzio fino al timeout".

**4.**
(a) Le righe `>` sono la richiesta (`GET / HTTP/1.1`, `Host:`, `User-Agent:`, `Accept:`), le `<` la risposta (`HTTP/1.0 200 OK`, le intestazioni, il corpo); stato **200**. (b) `curl -I` usa il metodo **HEAD**: il server manda solo le intestazioni, nessun corpo. (c) Un file inesistente dà **404 Not Found**. (d) Nella richiesta catturata con `nc` si vedono: la riga `POST /invia HTTP/1.1`, `Host: 127.0.0.1:8086`, l'intestazione `X-Prova: ciao`, `Content-Length: 7`, `Content-Type: application/x-www-form-urlencoded`, una riga vuota, e il corpo `a=1&b=2`.

**5.** (Con DNS reale.)
(a) `A` dà l'indirizzo IPv4, `AAAA` l'IPv6 (§9.2). (b) Un record `MX` indica il server di posta del dominio, con una priorità. (c) I record `TXT` contengono testo libero (verifiche di dominio, SPF/DKIM per la posta, e nelle CTF spesso flag o indizi): sono un nascondiglio classico. (d) `/etc/hosts` è la tabella statica locale nome→indirizzo, consultata **prima** del DNS (lo stabilisce `/etc/nsswitch.conf`): è così che `localhost` risolve senza rete, e come si può forzare un nome a un indirizzo per le prove. (e) `gethostbyname('localhost')` → `'127.0.0.1'`; `getaddrinfo('localhost', 80, type=SOCK_STREAM)` → una lista di tuple `(famiglia, tipo, proto, '', (ip, porta))`, una per ogni indirizzo (IPv4 e, se c'è, IPv6).

## ★★ Intermedio

**6.**

```python
# client.py IP PORTA — manda una riga e legge tutta la risposta
import socket, sys
try:
    s = socket.create_connection((sys.argv[1], int(sys.argv[2])), timeout=5)
except ConnectionRefusedError:
    sys.exit("connessione rifiutata: nessun server in ascolto lì")
s.sendall(sys.stdin.buffer.readline())
risposta = b''
while (c := s.recv(4096)):          # leggo fino alla chiusura (TCP è un flusso)
    risposta += c
s.close()
sys.stdout.buffer.write(risposta)
```

(a) Contro il server echo del §6 rimanda la riga in maiuscolo. (b) Mandando `GET / HTTP/1.0\r\n\r\n` a `http.server`, ricevi la risposta HTTP completa (stato, intestazioni, corpo). (c) Un solo `recv` può restituire solo il primo pezzo: TCP è un flusso e la risposta può arrivare in più segmenti (L8 §6.2, §4); il ciclo `while recv` legge fino all'EOF. (d) `ECONNREFUSED` (in Python `ConnectionRefusedError`) significa che nessun processo è in ascolto su quella porta: il sistema remoto ha risposto con un RST (§5).

**7.**
(a) Con il server a una connessione per volta, il secondo client resta bloccato nell'handshake finché il primo non chiude. (b) In Python, la via più semplice:

```python
import socketserver
class Eco(socketserver.StreamRequestHandler):
    def handle(self):
        while (dati := self.request.recv(1024)):
            self.request.sendall(dati.upper())
socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('127.0.0.1', 7777), Eco) as s:
    s.serve_forever()
```

In C, dopo `accept`: `pid_t p = fork(); if (p == 0) { close(s); /* gestisci c */ _exit(0); } close(c);` nel padre. (c) Due client vengono serviti insieme. (d) Con `fork` il figlio eredita **tutti** i descrittori aperti (L5 §4, L9): il figlio non usa il socket in ascolto `s` e lo chiude; il padre non usa il socket della connessione `c` e lo chiude, altrimenti la connessione non si chiuderebbe davvero finché anche il padre non rilascia il suo riferimento (il *reference count* del descrittore), e si accumulerebbero descrittori (CWE-775).

**8.**

```python
# udp_rovescia.py — server UDP che rimanda il datagramma invertito
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9010))
while True:
    dati, mittente = s.recvfrom(1024)
    s.sendto(dati[::-1], mittente)
```

(a) Si prova con `nc -u 127.0.0.1 9010` o con un client UDP (`sendto`/`recvfrom`). (b) Niente `listen`/`accept`/`connect`: UDP non ha connessioni; si usa `recvfrom` (che dà anche il mittente) e `sendto` (a cui dai la destinazione). (c) Due datagrammi arrivano come **due** `recvfrom` distinti: UDP conserva i confini (§4). (d) Mandando a un server UDP spento **non** ricevi un errore immediato come con TCP: UDP è senza connessione, quindi `sendto` riesce comunque (il datagramma parte); al massimo, più tardi, arriva un messaggio ICMP *port unreachable*, che un `recvfrom` successivo può tradurre in `ECONNREFUSED` solo se avevi fatto `connect` sul socket UDP.

**9.**

```python
# micurl.py URL — un mini-curl: GET HTTP/1.0 con redirect
import socket, sys
from urllib.parse import urlparse

def scarica(url, salti=5):
    u = urlparse(url)
    host, porta, percorso = u.hostname, u.port or 80, u.path or '/'
    s = socket.create_connection((host, porta), timeout=5)
    s.sendall(f'GET {percorso} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode())
    risp = b''
    while (c := s.recv(4096)): risp += c
    s.close()
    testa, _, corpo = risp.partition(b'\r\n\r\n')
    righe = testa.decode(errors='replace').split('\r\n')
    stato = int(righe[0].split()[1])
    intest = dict(r.split(': ', 1) for r in righe[1:] if ': ' in r)
    if 300 <= stato < 400 and 'Location' in intest and salti > 0:
        return scarica(intest['Location'], salti - 1)     # segui il redirect
    return stato, intest, corpo

stato, intest, corpo = scarica(sys.argv[1])
print('STATO:', stato)
print('INTESTAZIONI:', intest)
print('CORPO:', len(corpo), 'byte')
```

(a)–(b) Contro un server locale funziona e segue i 3xx. (c) Devi leggere fino alla chiusura (con `Connection: close`/HTTP 1.0 il server chiude dopo la risposta) o interpretare `Content-Length`: un solo `recv` può dare solo il primo segmento (§4, L8). (d) Per HTTPS servirebbe uno strato **TLS** tra TCP e HTTP: in Python si avvolge il socket con `ssl.create_default_context().wrap_socket(...)`; è più complicato perché TLS negozia cifrari, verifica il certificato del server e cifra tutto il traffico (§8, §11).

**10.**
(a) `ss -tlnp` mostra una riga `LISTEN ... 127.0.0.1:7777 ... users:(("server_tcp",pid=...,fd=3))`: ascolta su `127.0.0.1`, porta 7777, processo `server_tcp`. (b) `ss -tnp` con un client connesso mostra lo stato `ESTAB` e le quattro coordinate (il tuo lato `127.0.0.1:7777`, il peer `127.0.0.1:<porta effimera>`). (c) Con `0.0.0.0:7777` la riga di `ss` mostra l'ascolto su tutte le interfacce: su una macchina in rete, chiunque può collegarsi, il che per un servizio di prova (spesso vulnerabile) è pericoloso (L8, Esercizio 11). (d) `TIME-WAIT` è lo stato in cui resta, per qualche minuto, il lato che ha chiuso attivamente la connessione, per assorbire eventuali pacchetti in ritardo; impedisce di rilegare subito la stessa porta, e `SO_REUSEADDR` dice al sistema di permetterlo lo stesso (§6.2).

## ★★★ Sfida

**11. Lo sportello di rete.** La flag è **`L10{le_reti_parlano_a_voce_alta_dal_filo}`**:

```
$ bash setup_sfida.sh && cd ~/l10_sfida
$ python3 servizio.py --porta 8100
in ascolto: TCP 8100 (banner), HTTP 8101, UDP 8102; cattura.pcap creato

# Pezzo 1 — nc sulla porta TCP (banner)
$ nc 127.0.0.1 8100
=== Sportello di rete della Lezione 10 ===
Pezzo 1: L10{le_reti_
...

# Pezzo 2 — segui il redirect della pagina web
$ curl -s -D - http://127.0.0.1:8101/ -o /dev/null | grep -i location
Location: /segreto-9f3a
$ curl -s http://127.0.0.1:8101/segreto-9f3a          # (oppure: curl -sL http://127.0.0.1:8101/)
Pezzo 2: parlano_

# Pezzo 3 — lo sportello UDP vuole il datagramma "apri"
$ python3 -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); \
s.sendto(b'apri', ('127.0.0.1', 8102)); print(s.recvfrom(1024)[0].decode())"
Pezzo 3: a_voce_alta_
# (equivalente: printf 'apri' | nc -u -w1 127.0.0.1 8102)

# Pezzo 4 — dentro la cattura
$ tcpdump -r cattura.pcap -A 2>/dev/null | grep Pezzo
Pezzo 4: dal_filo}
# (senza tcpdump/Wireshark:  strings cattura.pcap | grep Pezzo)
```

Per ogni pezzo, lo strumento e il perché: **(1)** `nc` — il servizio TCP manda un banner alla connessione, lo leggi collegandoti (§7.1). **(2)** `curl` con `-v`/`-D -` — la radice risponde **302** con `Location: /segreto-9f3a`; seguire i redirect (a mano o con `-L`) è pane quotidiano del web (§8, §10.2). **(3)** un socket **UDP** o `nc -u` — lo sportello è senza connessione, gli mandi un datagramma e ne ricevi uno (§4, §6.4). **(4)** Wireshark/`tcpdump` (o `strings` come ripiego) — il pezzo viaggia in chiaro dentro una cattura, e si legge seguendo il flusso TCP (§11). La flag dice la morale: le reti parlano "a voce alta", e con gli strumenti giusti si ascolta tutto ciò che non è cifrato.

**12. Network forensics.**
(a) `tcpdump -r cattura.pcap -n` elenca i pacchetti; l'handshake è la sequenza `[S]`, `[S.]`, `[.]` (§5). (b) Con `-A` si legge il payload in chiaro: la riga `GET /flag HTTP/1.0` e la risposta `HTTP/1.0 200 OK` con il pezzo. (c) In Wireshark, filtro `http` e *Follow → TCP Stream* ricostruiscono il dialogo richiesta/risposta. (d) Se la connessione fosse **HTTPS**, vedresti l'handshake TCP, l'handshake TLS (i messaggi `Client Hello`/`Server Hello`), e poi solo *Application Data* cifrati: gli indirizzi, le porte, le dimensioni e i tempi sì, il contenuto no (serve la chiave, §11.2).

**13. Protocollo testuale.** Esempio di protocollo (tre righe di specifica):
- comandi, uno per riga terminata da `\n`: `PING`, `SOMMA <a> <b>`, `QUIT`;
- risposte, una riga: `PONG`; il risultato della somma; per `QUIT` il server chiude; per un comando ignoto o argomenti errati, `ERRORE <motivo>`;
- la fine di un messaggio è il `\n` (è un protocollo a righe, come SMTP o HTTP nelle intestazioni).

```python
# server13.py — serve più client (un thread per connessione)
import socketserver
class H(socketserver.StreamRequestHandler):
    def handle(self):
        for riga in self.rfile:                       # legge riga per riga
            parti = riga.decode(errors='replace').split()
            if not parti: continue
            cmd = parti[0].upper()
            if cmd == 'PING':   r = 'PONG'
            elif cmd == 'QUIT': return
            elif cmd == 'SOMMA' and len(parti) == 3:
                try: r = str(int(parti[1]) + int(parti[2]))
                except ValueError: r = 'ERRORE argomenti non numerici'
            else: r = 'ERRORE comando sconosciuto'
            self.wfile.write((r + '\n').encode()); self.wfile.flush()
socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('127.0.0.1', 7000), H) as s:
    s.serve_forever()
```

(a) Specifica sopra. (b) Gli errori (`int()` che fallisce, numero di argomenti sbagliato, comando ignoto) producono una riga `ERRORE ...` invece di far crollare il server (L8 regola 5). (c) Il server si prova con `nc 127.0.0.1 7000` (un client generico: scrivi `PING`, `SOMMA 3 4`, `QUIT`); un tuo client si prova contro `nc -l 127.0.0.1 7000` (un server generico a cui rispondi a mano). Funzionare con `nc` da entrambi i lati è la prova che il protocollo è ben definito e indipendente dall'implementazione. (d) In una cattura `tcpdump -i lo -A port 7000` i comandi `PING`/`SOMMA 3 4` e le risposte si leggono **in chiaro**: è testo su TCP, come HTTP.

## Domande di autoverifica: punti chiave attesi

1. Applicazione (il protocollo del programma), trasporto (porte, affidabilità), rete (IP, instradamento), collegamento (il mezzo fisico); incapsulamento = ogni livello aggiunge la sua intestazione scendendo (§1).
2. 32 bit in quattro byte decimali; `/24` = 24 bit di rete, 8 di host → 256 indirizzi, broadcast `.255` (§2.1).
3. `127.0.0.1` = loopback (questa macchina); i privati (`10/8`, `172.16/12`, `192.168/16`) non sono instradabili su Internet, usati dietro NAT (§2.1, §2.4).
4. Big-endian dei numeri di rete; `htons`/`htonl` convertono da ordine della macchina a ordine della rete; senza, porte e indirizzi sarebbero invertiti (§2.2).
5. 16 bit che identificano il programma; quattro valori (IP e porta di origine e destinazione) identificano la connessione; ben note 0–1023, effimere assegnate ai client (§3).
6. TCP: connessione, affidabile, ordinato, flusso; UDP: senza connessione, inaffidabile, a datagrammi con confini. HTTP usa TCP, il DNS UDP (§4).
7. SYN → SYN+ACK → ACK; chiusura con FIN per ogni direzione; RST = chiusura brusca, lo ricevi su una porta chiusa (§5).
8. TCP è un flusso senza confini di messaggio, `recv` dà "quanto è arrivato"; UDP conserva i confini, `recvfrom` dà un datagramma intero (§4).
9. Descrittore che rappresenta un endpoint; server `socket`/`bind`/`listen`/`accept`, client `socket`/`connect`; `accept` dà un nuovo descrittore per quella connessione, mentre quello in ascolto resta (§6).
10. `fork` per connessione, un thread per connessione, o `select`/`poll`/`epoll` in un processo solo (§6.2).
11. `nc` client/server/scansione, `ss`/`netstat` chi ascolta e chi è connesso, `ping` raggiungibilità; `nc -z`: riesce (aperta), RST (chiusa), timeout (filtrata) (§7).
12. Mostra richiesta (`>`) e risposta (`<`); `-X POST -d`, `-H`, `-b` per metodo, intestazione, cookie (§8).
13. Database distribuito nomi→indirizzi; A/AAAA (IPv4/IPv6), CNAME (alias), MX (posta), TXT (testo, spesso flag); `dig`/`host`/`getent` (§9).
14. Richiesta: metodo, percorso, versione, intestazioni, riga vuota, corpo; risposta: stato + intestazioni + corpo; `\r\n\r\n` separa; 2xx ok, 3xx redirect, 4xx errore client, 5xx errore server (§10).
15. HTTP è stateless; i cookie (`Set-Cookie`/`Cookie`) portano lo stato di sessione tra richieste (§10.2).
16. Catturano i pacchetti e mostrano le intestazioni annidate; l'handshake è `[S]`/`[S.]`/`[.]`; *Follow TCP Stream* ricostruisce il flusso di una connessione (§11).
17. In chiaro = chi cattura legge tutto, credenziali comprese; in HTTPS vedi indirizzi, porte, dimensioni e tempi, ma non il contenuto (§11.2).
18. Il socket è un descrittore (L4/L9); l'ordine dei byte è l'endianness (L7); `recv` non dà messaggi perché TCP è un flusso (L8): il modulo si tiene insieme così (§17).
