#!/usr/bin/env bash
# Prepara la sfida della Lezione 8 in ~/l8_sfida. Non leggere oltre: esegui e basta.
# Crea solo ~/l8_sfida/servizio.py e LEGGIMI.txt. Il servizio, se lo avvii con --porta,
# ascolta soltanto su 127.0.0.1 (la tua macchina) e non è raggiungibile dall'esterno.
set -e
D="$HOME/l8_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
command -v python3 >/dev/null || { echo "serve python3"; exit 1; }
mkdir -p "$D"; cd "$D"
cat > servizio.py <<'PY'
#!/usr/bin/env python3
# Servizio della sfida L8. Non leggere il codice: parlaci.
import base64, os, random, socketserver, sys, time

P = ['TDh7cHl0aG9uXw==', 'cGFybGFfY29uXw==', 'aV9wcm9ncmFtbWlf', 'YWxfcG9zdG9fdHVvfQ==']
def pezzo(i): return base64.b64decode(P[i]).decode()

def gioco(r, w):
    def scrivi(s):
        w.write(s.encode() if isinstance(s, str) else s); w.flush()
    def riga():
        l = r.readline()
        if not l: raise EOFError
        return l.rstrip(b'\r\n').decode(errors='replace')
    rnd = random.SystemRandom()
    scrivi('=== Sportello della Lezione 8 ===\n')
    scrivi('Prova 1: trenta calcoli in dieci secondi.\n')
    t0 = time.monotonic()
    for i in range(30):
        a, b = rnd.randint(100, 9999), rnd.randint(2, 99)
        op = rnd.choice('+-*')
        giusto = {'+': a + b, '-': a - b, '*': a * b}[op]
        scrivi(f'[{i + 1}/30] Quanto fa {a} {op} {b}?\n> ')
        try:
            ok = int(riga()) == giusto
        except ValueError:
            ok = False
        if not ok:
            scrivi('Sbagliato. Arrivederci.\n'); return
        if time.monotonic() - t0 > 10:
            scrivi('Troppo lento. Un essere umano? Arrivederci.\n'); return
    scrivi(f'Bravo. Pezzo 1: {pezzo(0)}\n')
    n = rnd.randint(0x01000000, 0x7fffffff)
    scrivi(f'Prova 2: mandami il numero {n} come intero a 32 bit little-endian: 4 byte grezzi, poi a capo.\n> ')
    dati = r.read(5)
    if dati[:4] != n.to_bytes(4, 'little'):
        scrivi(f'Ho ricevuto {dati[:4].hex()}, mi aspettavo altro. Arrivederci.\n'); return
    scrivi(f'Perfetto. Pezzo 2: {pezzo(1)}\n')
    segreto = os.urandom(12)
    scrivi(f'Prova 3: questo è base64: {base64.b64encode(segreto).decode()}\nRimandami gli stessi byte in esadecimale.\n> ')
    if riga().strip().lower() != segreto.hex():
        scrivi('No. Arrivederci.\n'); return
    scrivi(f'Esatto. Pezzo 3: {pezzo(2)}\n')
    codice = os.urandom(8).hex()
    scrivi('Prova 4: ora ti parlo molto. Ricorda il codice.\n')
    righe = [f'rumore {rnd.getrandbits(64):016x}' for _ in range(300)]
    righe.insert(rnd.randint(50, 250), f'CODICE: {codice}')
    scrivi('\n'.join(righe) + '\n')
    scrivi('Qual era il codice? Hai due secondi.\n> ')
    t1 = time.monotonic()
    risposta = riga().strip()
    if risposta != codice or time.monotonic() - t1 > 2:
        scrivi('No. Arrivederci.\n'); return
    scrivi(f'Ottimo. Pezzo 4: {pezzo(3)}\n')

class Gestore(socketserver.StreamRequestHandler):
    def handle(self):
        try: gioco(self.rfile, self.wfile)
        except (EOFError, ConnectionError, BrokenPipeError): pass

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--porta':
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        with socketserver.ThreadingTCPServer(('127.0.0.1', int(sys.argv[2])), Gestore) as s:
            print(f'In ascolto su 127.0.0.1:{sys.argv[2]} (Ctrl-C per fermare)')
            s.serve_forever()
    else:
        try: gioco(sys.stdin.buffer, sys.stdout.buffer)
        except (EOFError, BrokenPipeError): pass
PY
chmod +x servizio.py
cat > LEGGIMI.txt <<'X'
servizio.py è uno sportello con quattro prove. Ogni prova superata dà un pezzo della flag L8{...}.
Si può usare in due modi:
  python3 servizio.py                 (parla sullo standard input e output)
  python3 servizio.py --porta 4444    (in ascolto su 127.0.0.1:4444; collegati con nc o con pwntools)
A mano non ce la farai: le prove sono troppo veloci o vogliono byte non digitabili.
Scrivi uno script Python che parla al posto tuo. Non leggere il codice del servizio.
X
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
