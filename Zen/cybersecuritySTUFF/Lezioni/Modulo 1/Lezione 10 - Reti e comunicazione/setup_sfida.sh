#!/usr/bin/env bash
# Prepara la mini-CTF della Lezione 10 in ~/l10_sfida. Non leggere oltre: esegui e basta.
# Crea servizio.py e LEGGIMI.txt. Avvia con: python3 servizio.py --porta 8100
# I servizi ascoltano SOLO su 127.0.0.1 (la tua macchina).
set -e
D="$HOME/l10_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
command -v python3 >/dev/null || { echo "serve python3"; exit 1; }
mkdir -p "$D"; cd "$D"
cat > servizio.py <<'PY'
#!/usr/bin/env python3
# Servizio della sfida L10. Non leggere il codice: esploralo con gli strumenti di rete.
import socket, socketserver, struct, sys, threading, os

BASE = int(sys.argv[sys.argv.index('--porta') + 1]) if '--porta' in sys.argv else 8100

# --- Servizio 1: TCP, manda un banner e chiude ---
class Banner(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b'=== Sportello di rete della Lezione 10 ===\n'
                             b'Pezzo 1: L10{le_reti_\n'
                             b'Gli altri pezzi sono altrove: una pagina web su questa porta +1,\n'
                             b'uno sportello UDP su questa porta +2, e una cattura cattura.pcap.\n')

# --- Servizio 2: HTTP, il pezzo e' sotto un percorso rivelato da un redirect ---
class Web(socketserver.BaseRequestHandler):
    def handle(self):
        req = self.request.recv(4096).decode(errors='replace')
        riga = req.split('\r\n', 1)[0]
        percorso = riga.split(' ')[1] if ' ' in riga else '/'
        if percorso == '/':
            corpo = b'Vai dove ti mando.\n'
            self.request.sendall(b'HTTP/1.0 302 Found\r\nLocation: /segreto-9f3a\r\n'
                                 b'Content-Length: %d\r\n\r\n' % len(corpo) + corpo)
        elif percorso == '/segreto-9f3a':
            corpo = b'Pezzo 2: parlano_\n'
            self.request.sendall(b'HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n'
                                 b'Content-Length: %d\r\n\r\n' % len(corpo) + corpo)
        else:
            corpo = b'Non qui.\n'
            self.request.sendall(b'HTTP/1.0 404 Not Found\r\nContent-Length: %d\r\n\r\n' % len(corpo) + corpo)

def udp_server(porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', porta))
    while True:
        dati, mittente = s.recvfrom(1024)
        if dati.strip() == b'apri':
            s.sendto(b'Pezzo 3: a_voce_alta_\n', mittente)
        else:
            s.sendto(b'Manda esattamente: apri\n', mittente)

def scrivi_pcap(nome):
    def pkt(payload, sp, dp):
        eth = struct.pack('>6s6sH', b'\x00'*6, b'\x00'*6, 0x0800)
        tcp = struct.pack('>HHIIBBHHH', sp, dp, 1, 0, 5<<4, 0x18, 65535, 0, 0) + payload
        total = 20 + len(tcp)
        ip = struct.pack('>BBHHHBBH4s4s', 0x45,0,total,0,0,64,6,0,
                         bytes([127,0,0,1]), bytes([127,0,0,1]))
        return eth + ip + tcp
    frames = [(b'GET /flag HTTP/1.0\r\n\r\n', 40000, 8080),
              (b'HTTP/1.0 200 OK\r\n\r\nPezzo 4: dal_filo}\n', 8080, 40000)]
    with open(nome, 'wb') as f:
        f.write(struct.pack('<IHHiIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1))
        for payload, sp, dp in frames:
            raw = pkt(payload, sp, dp)
            f.write(struct.pack('<IIII', 0, 0, len(raw), len(raw)) + raw)

if __name__ == '__main__':
    scrivi_pcap(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])) or '.', 'cattura.pcap'))
    threading.Thread(target=udp_server, args=(BASE + 2,), daemon=True).start()
    socketserver.TCPServer.allow_reuse_address = True
    web = socketserver.TCPServer(('127.0.0.1', BASE + 1), Web)
    threading.Thread(target=web.serve_forever, daemon=True).start()
    ban = socketserver.TCPServer(('127.0.0.1', BASE), Banner)
    print(f'in ascolto: TCP {BASE} (banner), HTTP {BASE+1}, UDP {BASE+2}; cattura.pcap creato', flush=True)
    try:
        ban.serve_forever()
    except KeyboardInterrupt:
        pass
PY
cat > LEGGIMI.txt <<'T'
Mini-CTF della Lezione 10 — lo sportello di rete.

Avvia:  python3 servizio.py --porta 8100
Apre tre servizi su 127.0.0.1 e crea il file cattura.pcap:
  - porta 8100  : un servizio TCP (banner)
  - porta 8101  : una pagina web (HTTP)
  - porta 8102  : uno sportello UDP
  - cattura.pcap: una cattura di traffico

La flag L10{...} è in quattro pezzi. Usa gli strumenti della lezione, NON leggere servizio.py:

  Pezzo 1  collegati con nc alla porta 8100 e leggi:   nc 127.0.0.1 8100
  Pezzo 2  c'è una pagina su 8101; la radice / ti REINDIRIZZA altrove.
           Segui il redirect: curl -v (guarda l'intestazione Location) oppure curl -L.
  Pezzo 3  sportello UDP su 8102: mandagli il datagramma che chiede e leggi la risposta.
           In Python con un socket SOCK_DGRAM, o con:  nc -u 127.0.0.1 8102
  Pezzo 4  è dentro cattura.pcap. Aprilo con Wireshark (Follow TCP Stream) o:
           tcpdump -r cattura.pcap -A      (se non li hai: strings cattura.pcap)

Suggerimento: mentre risolvi 1-3, cattura con  tcpdump -i lo -n  e riconosci l'handshake.
Le soluzioni sono in Soluzioni.md (aprile solo dopo aver provato).
T
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
