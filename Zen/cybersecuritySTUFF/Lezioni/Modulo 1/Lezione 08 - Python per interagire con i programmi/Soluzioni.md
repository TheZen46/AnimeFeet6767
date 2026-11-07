# Modulo 1 — Lezione 8: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Tutto è stato provato con Python 3.13, pwntools 4.15 e gcc su Linux x86-64. Gli script vanno salvati nella stessa cartella dei programmi con cui dialogano. I riferimenti `§` rimandano alle sezioni di `Lezione.md`. Negli output di pwntools sono state tolte le righe `[+] Starting local process` e `[*] Stopped process`, che cambiano a ogni esecuzione.

## ★ Base

**1.**
(a) `6`: `len` di una `str` conta i **caratteri** (i *code point*, L7 §8.1).
(b) `7`: in UTF-8 la `é` occupa due byte (`c3 a9`, L7 §8.2), quindi la stessa parola è lunga 6 caratteri ma 7 byte.
(c) `66`: indicizzare un `bytes` dà un **intero** (il codice di `B`), non un `bytes` di lunghezza 1.
(d) `b'B'`: una **fetta** di un `bytes` è ancora un `bytes`.
(e) `False`: un `str` e un `bytes` non sono mai uguali, e il confronto **non** dà errore (§3.1). È il bug più silenzioso di tutta la lezione: `if risposta == 'OK':` con `risposta` ricevuta dalla rete non è mai vero.
(f) `b'Hi'`: `bytes` di una lista di interi 0–255.
(g) `[104, 105]`: iterare un `bytes` dà interi.
(h) `b'\x00\x00\x00'`: `bytes(n)` con un intero crea *n* byte a zero (non il byte di valore 3: per quello `bytes([3])`).
(i) `"b'hi'"`: `str` applicato a un `bytes` non decodifica, ne restituisce la **rappresentazione**, con la `b` e gli apici. Per questo `f'Ciao {dati}'` con `dati = b'Zen'` produce `"Ciao b'Zen'"`, e mandato a un server dà una risposta sbagliata che sembra giusta. Al suo posto: `f'Ciao {dati.decode()}'`, oppure, restando nei byte, `b'Ciao ' + dati` o `b'Ciao %s' % dati`.
(l) `b'caff\xe8'`: in Latin-1 ogni carattere fino a U+00FF è un solo byte, e `è` è 0xE8.
(m) `'�'` (il REPL lo mostra come `'�'`): 0xE8 in UTF-8 è l'inizio di una sequenza di tre byte che qui non continua; `errors='replace'` mette il carattere sostitutivo invece di sollevare `UnicodeDecodeError`. È il *mojibake* della L7 §8.4.
(n) `b'ABC'`: `fromhex` ignora gli spazi.
(o) `(31, 31, '0xff', '00000bee')`: `int(..., 16)` accetta il prefisso `0x` (con la base 16 o con la base 0); `hex` restituisce una `str` con prefisso; `%08x` riempie con zeri fino a 8 cifre, senza prefisso (3054 = 0xBEE).

**2.**
(a) `b'\xef\xbe\xad\xde'`: little-endian, il byte meno significativo per primo.
(b) `b'\xde\xad\xbe\xef'`: big-endian.
(c) `b'\xfe\xff\xff\xff'`: −2 in complemento a due a 32 bit è 0xFFFFFFFE (L7 §3.2).
(d) `4294967294`: gli stessi byte letti **senza segno** (`I`).
(e) `-2`: letti **con segno** (`i`). Che cosa li distingue è solo l'interpretazione, la lettera del formato: i bit sono gli stessi (L7 §3.3).
(f) `(10, 16)`: con `<` (e con `>` o `!`) `struct` usa le dimensioni standard **senza allineamento**: 2 + 8 = 10. Senza prefisso usa l'ordine **e l'allineamento nativi** della macchina, come farebbe un compilatore C: dopo l'`H` di 2 byte inserisce 6 byte di riempimento perché il `Q` cominci a un indirizzo multiplo di 8. Un protocollo o un formato di file non hanno "padding nativo" né "ordine nativo": se non scrivi il prefisso, lo script funziona per caso sulla tua macchina e smette di funzionare su un'altra, o legge campi sfasati.
(g) `b'BA'`: 0x4142 little-endian è `42 41`, cioè `B` e `A`.
(h) `16777216`, cioè 0x01000000: letti big-endian, il primo byte è il più significativo.
(i) `(50462976, 117835012)`, cioè `(0x03020100, 0x07060504)`: due interi little-endian da 4 byte, i byte 0–3 e 4–7.

**3.** Una soluzione:

```python
#!/usr/bin/env python3
# hexd.py — un xxd in miniatura (Esercizio 3)
import argparse, sys

def righe(dati):
    for off in range(0, len(dati), 16):
        blocco = dati[off:off + 16]
        esa = ' '.join(f'{b:02x}' for b in blocco[:8])
        if len(blocco) > 8:
            esa += '  ' + ' '.join(f'{b:02x}' for b in blocco[8:])
        testo = ''.join(chr(b) if 0x20 <= b <= 0x7e else '.' for b in blocco)
        yield f'{off:08x}  {esa:<49} |{testo}|'

def main():
    ap = argparse.ArgumentParser(description='dump esadecimale in stile xxd')
    ap.add_argument('file', nargs='?', default='-', help="file da leggere ('-' = standard input)")
    ap.add_argument('-n', type=int, default=None, metavar='N', help='solo i primi N byte')
    a = ap.parse_args()
    try:
        if a.file == '-':
            dati = sys.stdin.buffer.read() if a.n is None else sys.stdin.buffer.read(a.n)
        else:
            with open(a.file, 'rb') as f:
                dati = f.read() if a.n is None else f.read(a.n)
    except OSError as e:
        print(f'hexd.py: {a.file}: {e.strerror}', file=sys.stderr)
        return 1
    for r in righe(dati):
        print(r)
    return 0

if __name__ == '__main__':
    sys.exit(main())
```

```
$ printf 'L8{ciao}\n' > c.txt && python3 hexd.py c.txt
00000000  4c 38 7b 63 69 61 6f 7d  0a                       |L8{ciao}.|
$ python3 hexd.py -n 20 /bin/ls
00000000  7f 45 4c 46 02 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|
00000010  03 00 3e 00                                       |..>.|
$ printf 'ciao' | python3 hexd.py
00000000  63 69 61 6f                                       |ciao|
$ : > vuoto; python3 hexd.py vuoto; echo $?
0
$ python3 hexd.py /non/esiste; echo $?
hexd.py: /non/esiste: No such file or directory
1
```

I punti che contano: `'rb'` e `sys.stdin.buffer` (non `sys.stdin`, che è testo e crollerebbe con `UnicodeDecodeError` sui byte di `/bin/ls`); `OSError` è la classe comune di `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, quindi un solo `except` copre tutti i casi in cui il file non si può leggere, senza ingoiare gli errori di programmazione (§2.6); il codice di uscita esce da `sys.exit(main())`. La riga piena è lunga 8 + 2 + 48 + 2 + 18 = 78 caratteri, esattamente come quella di `hexdump -C`: il campo esadecimale va riempito a larghezza fissa (`:<49`, più lo spazio prima di `|`) perché la colonna di destra resti allineata anche nell'ultima riga, più corta. Il file vuoto non stampa niente, come `xxd` (`hexdump -C` stampa invece solo l'offset finale `00000000`). Per file molto grandi converrebbe leggere a blocchi di 16 byte invece che tutto insieme: è una buona estensione.

**4.**

```python
>>> import subprocess
>>> int(subprocess.run(['id', '-u'], capture_output=True, text=True, check=True).stdout)     # (a)
1000
>>> r = subprocess.run(['ls', '/non/esiste'], capture_output=True, text=True)                # (b)
>>> r.returncode, r.stderr
(2, "ls: cannot access '/non/esiste': No such file or directory\n")
>>> subprocess.run(['ls', '/non/esiste'], capture_output=True, check=True)                   # (c)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command '['ls', '/non/esiste']' returned non-zero exit status 2.
>>> subprocess.run(['tr', 'a-z', 'A-Z'], input=b'ciao', capture_output=True).stdout          # (d)
b'CIAO'
>>> subprocess.run(['sleep', '5'], timeout=1)                                                # (e)
Traceback (most recent call last):
  ...
subprocess.TimeoutExpired: Command '['sleep', '5']' timed out after 1 seconds
```

(a) `int` tollera il `\n` finale. (b) Il messaggio di `ls` è sullo **standard error** (`r.stderr`), lo standard output è vuoto; il codice 2 di `ls` significa "problema grave" (per GNU `ls`, 1 = problema minore, 2 = argomento inaccessibile). Senza `check`, `run` non solleva niente: tocca a te guardare `returncode`. (c) `subprocess.CalledProcessError`, con gli attributi `returncode`, `cmd`, `stdout` e `stderr` (questi ultimi pieni se hai catturato l'output). (d) `input=` scrive i dati sullo standard input del figlio e lo chiude, così `tr` riceve EOF e termina; senza `text=True` entrano ed escono `bytes`. (e) Scaduto il limite, `run` **uccide** il figlio con `SIGKILL` (L5 §8), aspetta che termini (niente zombie) e poi solleva `subprocess.TimeoutExpired`.

La funzione `saluta` passa la stringa a `/bin/sh -c`: `saluta('Zen; id')` stampa `Ciao Zen` e poi **esegue `id`**; `saluta('$(whoami)')` esegue `whoami` e stampa `Ciao zen` (il tuo nome utente). È l'iniezione di comandi, **CWE-78** (§5.2, L4 §14.2). La versione corretta non usa la shell, così il nome arriva a `echo` come un solo argomento, intatto:

```python
def saluta(nome):
    subprocess.run(['printf', 'Ciao %s\n', nome])
```

Anche `['echo', 'Ciao', nome]` qui va bene, perché `echo` riconosce le opzioni solo all'inizio e il primo argomento è `Ciao`; ma se il nome fosse il primo argomento, `-n` o `-e` diventerebbero opzioni, ed è per questo che il formato fisso di `printf` è la scelta robusta in generale. Con `shell=True` non c'è modo semplice di "ripulire" il nome: `shlex.quote(nome)` esiste ed è corretto per `sh`, ma la regola è non passare dalla shell quando non serve.

**5.**
(a) `[[1], [1], [1]]`: `[[]] * 3` crea una lista con **tre riferimenti allo stesso** oggetto lista, non tre liste. Si scrive `[[] for _ in range(3)]`.
(b) `[1, 2] [1, 2]`: il valore predefinito `[]` viene creato **una volta**, quando si esegue `def`, e condiviso da tutte le chiamate; inoltre `print` riceve due volte lo stesso oggetto, quindi entrambe le stampe mostrano lo stato finale. Versione corretta:

```python
def aggiungi(a, lista=None):
    if lista is None:
        lista = []
    lista.append(a)
    return lista
```

(c) `b'ciao!' b'ciao'`: i `bytes` sono **immutabili**, quindi `a += b'!'` costruisce un oggetto nuovo e lega a esso il nome `a`; `b` continua a riferirsi al vecchio.
(d) `[1, 2, 3] [1, 2, 3]`: le liste sono mutabili e `+=` su una lista è `extend`, una modifica **sul posto**: `l` e `m` sono lo stesso oggetto e la modifica si vede da entrambi. Stesso operatore, comportamento opposto: dipende dal tipo dell'oggetto, non dal nome.
(e) `65 66`: iterare `bytes` dà interi; `for c in 'AB'` darebbe le stringhe `'A'` e `'B'`. Con i dati binari è la cosa giusta: vuoi fare aritmetica e operazioni sui bit sui valori dei byte (`c ^ 0x20`, `c < 0x20`), e un intero è esattamente questo.
(f) `False`: 0.1 e 0.2 non sono rappresentabili esattamente in binario (L7 §6), e la somma dà `0.30000000000000004`. Per confrontare numeri non interi si usa una tolleranza (`math.isclose`); nelle sfide di calcolo, se i dati sono interi, si resta negli interi (`//`, non `/`).

## ★★ Intermedio

**6.**
(a) L'output del client ingenuo:

```
2 29 5 b'Benve'
2 28277 5 b'to al'
2 8307 5 b'erviz'
```

Il server spedisce il primo pacco, `00 1d` + `Benvenuto al servizio pacchi.`, in pezzi di sette byte: `00 1d B e n v e`, poi `n u t o ␠ a l`, poi `␠ s e r v i z`, e così via. Riga 1: `recv(2)` prende i due byte di lunghezza, 29, e `recv(29)` restituisce **solo i 5 byte già arrivati** (il resto del primo pezzo): `recv(n)` vuol dire "al massimo *n*", non "esattamente *n*" (§6.2). Riga 2: il client crede che il messaggio sia finito e legge come lunghezza i due byte successivi, `nu` = 0x6e75 = 28277, poi altri 5 byte. Riga 3: stessa cosa con ` s` = 0x2073 = 8307. Da quel momento il client ha perso il **sincronismo** con il protocollo e tutto ciò che legge è spazzatura; con un protocollo binario (lunghezze, indirizzi) l'errore non si vede nemmeno.

(b)

```python
#!/usr/bin/env python3
# es6.py — client corretto per pacchi.py
import socket

def recvn(s, n):
    """Restituisce esattamente n byte, o solleva EOFError."""
    dati = b''
    while len(dati) < n:
        pezzo = s.recv(n - len(dati))
        if not pezzo:                             # b'': il server ha chiuso
            raise EOFError(f'chiuso dopo {len(dati)} byte su {n}')
        dati += pezzo
    return dati

with socket.create_connection(('127.0.0.1', 9006)) as s:
    while True:
        try:
            n = int.from_bytes(recvn(s, 2), 'big')
        except EOFError:
            break                                 # fine regolare: chiusura tra un messaggio e l'altro
        m = recvn(s, n)                           # qui invece una chiusura è un errore, e lo lasciamo salire
        print(n, m[:60])
```

```
$ python3 es6.py
29 b'Benvenuto al servizio pacchi.'
3000 b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
50 b'Il terzo e ultimo: L8{la_lunghezza_prima_dei_dati}'
```

Nota la distinzione tra una chiusura **tra** due messaggi (fine normale) e una **dentro** un messaggio (errore). Per un messaggio molto lungo, accumulare con `+=` copia i dati a ogni giro; per messaggi grandi si usa un `bytearray` o una lista di pezzi da unire alla fine con `b''.join`, ma per qualche kilobyte non conta.

(c) Senza i pezzi e le pause, ogni pacco viene scritto con un solo `sendall`, e su `127.0.0.1` arriva quasi sempre tutto insieme, prima ancora che il client chiami `recv`: il client ingenuo legge per caso i confini giusti. Su una rete vera i segmenti TCP hanno una dimensione massima (circa 1460 byte di dati su Ethernet, lo vedrai nella Lezione 10), i pacchetti arrivano a intervalli, e il messaggio da 3000 byte arriva **sicuramente** in più pezzi. Un client che funziona in locale "quasi sempre" è un client che fallisce sul server della gara.

(d) `io.recvn(n)` di pwntools (§9.4), che usa il buffer del tube; e, per il caso "fino a una marca", `recvuntil`.

**7.**
(a) Tra `Ecco: ` e il `\n` ci sono **6 byte**, per esempio `09 72 7f 1b 94 55`. Un indirizzo dello spazio utente su Linux x86-64 sta sotto 0x0000_8000_0000_0000 (47 bit), e quelli di un eseguibile PIE cominciano tipicamente con 0x55 o 0x56: gli 8 byte little-endian sono quindi `xx xx xx xx xx 55 00 00`, e `fputs`, che scrive fino al primo byte 00 (una stringa C, L7 §9.1), si ferma dopo sei. Il primo byte è sempre `09` e la cifra bassa del secondo è sempre `2`, perché `main`, con il compilatore usato per queste prove, si trova all'offset 0x1209 dell'eseguibile (con il tuo potrebbe essere un altro, ma sarà fisso da un'esecuzione all'altra) e il caricamento avviene a un indirizzo multiplo di 4096 (0x1000): gli ultimi 12 bit non sono casuali. Lo rivedrai nel Modulo 4: è il motivo per cui un indirizzo trapelato basta a calcolare tutti gli altri.

(b)–(c)

```python
#!/usr/bin/env python3
# es7.py — leggere un indirizzo trapelato come byte grezzi
from pwn import *

def tenta():
    io = process('./perde')
    io.recvuntil(b'Ecco: ')
    grezzi = io.recvuntil(b'\nE in esadecimale? ', drop=True)
    if len(grezzi) != 6:                          # un byte 00 dentro l'indirizzo ha fermato fputs
        log.warning(f'trapelati solo {len(grezzi)} byte ({grezzi.hex()}): riprovo')
        io.close()
        return None
    a = u64(grezzi.ljust(8, b'\x00'))
    log.info(f'main è a {a:#x}')
    io.sendline(hex(a).encode())
    risposta = io.recvline().decode().strip()
    io.close()
    return risposta

while (r := tenta()) is None:
    pass
log.success(r)
```

```
$ gcc -o perde perde.c && python3 es7.py
[*] main è a 0x55c5638e5209
[+] Giusto: L8{sei_byte_bastano}
```

Senza il controllo sulla lunghezza, su duecento esecuzioni si vede di solito qualche fallimento, e i byte ricevuti in quei casi sono troppo pochi, per esempio `09 52 ff` o `09 e2`: l'indirizzo conteneva un byte **00 nel mezzo**, e `fputs` si è fermato lì. I byte 2, 3 e 4 dell'indirizzo sono casuali (l'ASLR, Modulo 4), ognuno vale 00 con probabilità 1/256, quindi la probabilità che almeno uno lo sia è 1 − (255/256)³ ≈ 1,2%: due o tre fallimenti su duecento, come si osserva. Un indirizzo ricostruito da 3 byte "riempiti" con `ljust` è sbagliato senza che niente te lo segnali: per questo si **controlla la lunghezza** e si riprova (Esempio 6), invece di fidarsi. Nelle sfide vere spesso la scelta giusta è proprio questa: rilanciare finché l'indirizzo non contiene byte scomodi.

(d) `recvline()` si ferma al primo `\n`, cioè al byte **0x0a**. Se uno dei byte casuali dell'indirizzo vale 0x0a (di nuovo circa l'1,2% delle volte), `recvline` restituisce un indirizzo troncato, e il resto dei byte viene letto come se fosse la riga successiva. `recvuntil` con la marca **lunga** `\nE in esadecimale? ` è robusto: un 0x0a dentro l'indirizzo non è seguito da quel testo. In generale: per separare byte binari, usa come marca il testo che li **segue**, il più lungo e specifico possibile.

**8.**

```python
>>> flat(b'A' * 4, 0xdeadbeef)                    # (a)
b'AAAA\xef\xbe\xad\xde'
>>> context.arch = 'amd64'
>>> flat(b'A' * 4, 0xdeadbeef)                    # (b)
b'AAAA\xef\xbe\xad\xde\x00\x00\x00\x00'
>>> flat(b'ciao', p32(1), 2)                      # (c)
b'ciao\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'
>>> flat({16: 0x401136}, filler=b'B')             # (d)
b'BBBBBBBBBBBBBBBB6\x11@\x00\x00\x00\x00\x00'
>>> flat({8: b'X'}, length=12)                    # (e)
b'aaaabaaaXaaa'
>>> cyclic(12), cyclic_find(b'faaa')              # (f)
(b'aaaabaaacaaa', 20)
```

(a) e (b): `flat` impacchetta gli interi con la dimensione di parola di `context` (§11.1). Il valore predefinito di `context.arch` è `i386`, 32 bit: 4 byte; con `amd64` diventano 8, e la lunghezza passa da 8 a 12. È l'errore classico di chi dimentica `context.arch` (o `context.binary`, che lo imposta leggendo l'ELF) in uno script per un binario a 64 bit: ogni indirizzo è lungo la metà del dovuto e tutto il messaggio è sfasato. (c) I `bytes` entrano così come sono (anche quelli prodotti da `p32`), gli interi vengono impacchettati a 8 byte: 4 + 4 + 8 = 16. (d) **24** byte: 16 di riempimento e l'intero a 8 byte; 0x401136 little-endian è `36 11 40 00 00 00 00 00`, e il REPL mostra 0x36 come `6` e 0x40 come `@` perché sono stampabili. (e) Senza `filler`, `flat` riempie con la sequenza di **`cyclic`** (de Bruijn, §10.4): i buchi non sono byte tutti uguali ma pezzi riconoscibili. Se nel Modulo 4 un programma crolla con il registro `rip` che vale `0x61616166` (`faaa`), `cyclic_find` ti dice subito che quella parte veniva dall'offset 20 del tuo input: riempire con `cyclic` invece che con `A` rende ogni byte "firmato".

**9.**

```python
>>> from pwn import *
>>> c = bytes.fromhex('5f0fbbbd7b5ea1a87668a3b16143a181705ea6ac7245a9b14c53a5bc7c5ba5a3')
>>> xor(c[:3], b'L8{')                            # (a) chiaro ^ cifrato = chiave
b'\x137\xc0'
>>> len(c), (len(c) - 1) % 4                      # (b) l'ultimo byte usa il byte 3 della chiave
(32, 3)
>>> k = xor(c[:3], b'L8{') + xor(c[-1:], b'}')
>>> k.hex()
'1337c0de'
>>> xor(c, k)                                     # (c)
b'L8{chiave_corta_cifrario_debole}'
```

(a) Lo XOR è la sua inversa: se `c = p ^ k`, allora `k = p ^ c` (L7 §4.3). Tre byte di chiaro noti danno tre byte di chiave: `13 37 c0` (il REPL scrive 0x37 come `7`). (b) L'altra cosa nota è che la flag **finisce** con `}`. Il byte di posizione *i* del chiaro è cifrato con il byte *i* mod 4 della chiave; l'ultimo ha posizione 31, e 31 mod 4 = 3: è proprio il byte mancante, `c[31] ^ ord('}')` = 0xde. (c) La chiave è `13 37 c0 de` e la flag `L8{chiave_corta_cifrario_debole}`. (d) I tre byte iniziali coprono le posizioni 0, 1, 2 della chiave (se *k* ≥ 3), l'ultimo la posizione (*n* − 1) mod *k*. La chiave è determinata se *k* ≤ 3, oppure se *k* = 4 e (*n* − 1) mod 4 = 3. Per chiavi più lunghe servono altri frammenti di chiaro noto (il formato della flag, parole probabili come `_the_` o `_di_`), oppure l'analisi statistica dell'Esercizio 15 della Lezione 7: trovare la lunghezza della chiave e attaccare ogni colonna come uno XOR a un byte, scegliendo il byte che rende la colonna "più simile a un testo".

**10.** L'output:

```
predefinito  Nome:False Età:True fine:b'Ciao Zen, 30 anni\n'
stdout=PIPE  Nome:False Età:True fine:b'Ciao Zen, 30 anni\n'
stdin=PTY    Nome:False Età:True fine:b'Ciao Zen, 30 anni\n'
PIPE + -u    Nome:True Età:True fine:b'Ciao Zen, 30 anni\n'
PIPE+stdbuf  Nome:False Età:True fine:b'Ciao Zen, 30 anni\n'
```

(a) Le due righe diverse dal caso C dell'Esempio 4 sono **`stdin=PTY`** e **`stdbuf`**, che con il programma C funzionavano e con Python no. Il motivo è che Python **non usa** lo `stdio` della libreria C per `sys.stdout`: ha un proprio buffer, nell'oggetto `io.TextIOWrapper`. Quindi: `stdbuf` agisce sulle impostazioni dello `stdio` della libreria C (tramite una libreria precaricata, L4 §3.3), che Python ignora; e lo svuotamento automatico dello standard output "prima di leggere da un terminale" è un comportamento della libreria C, non di Python, che svuota il buffer a righe solo quando scrive un `\n` (se lo standard output è un terminale), quando il buffer è pieno, all'uscita, o quando glielo chiedi con `flush`. Resta l'opzione `-u`, che rende Python non bufferizzato, oppure il `flush=True` dal lato di chi scrive il programma.

(b) `Età? ` arriva sempre perché `input` scrive il prompt e poi **svuota** lo standard output prima di leggere: la documentazione lo dice esplicitamente. È per questo che, scrivendo un servizio in Python, `input('> ')` funziona dietro una pipe e `print('> ', end='')` + `sys.stdin.readline()` no. Nota anche che `Età? ` svuota il buffer intero, quindi in quei casi arriva anche il `Nome? ` rimasto indietro, in ritardo.

(c) Per togliere dall'ambiente del figlio **`PYTHONUNBUFFERED`**: se è impostata (a qualunque valore non vuoto), ha lo stesso effetto di `-u`, e allora tutte e cinque le righe direbbero `Nome:True`. Alcuni ambienti (contenitori Docker, servizi di sviluppo) la impostano di proposito, e un esperimento sul buffering condotto lì darebbe risultati "impossibili". Lo stesso vale per i servizi di gara: se l'autore l'ha impostata nel `Dockerfile`, il programma Python non avrà problemi di buffering anche senza `flush`.

(d) Il saluto arriva comunque perché il programma non è bloccato: aspetta noi. Dopo il timeout di due secondi lo script manda `Zen` lo stesso, il programma lo legge (era nel buffer della pipe di ingresso) e prosegue. Ma lo script ha perso due secondi e, peggio, ha mandato una risposta **senza sapere a che cosa** stava rispondendo: se il programma avesse chiesto altro, o avesse svuotato l'input prima di leggere, il dialogo sarebbe andato fuori sincronia senza un errore visibile. La regola 2 del §12.2 ha questa sola eccezione consapevole (Esempio 4): un servizio remoto con il buffering rotto che non puoi aggiustare.

**11.**
(a) Per ogni connessione, `socketserver` dà al gestore un socket, che nel processo è un **descrittore** come un altro (L4 §1). `Popen` fa `fork`; nel figlio, prima di `execve`, fa `dup2(fd, 0)`, `dup2(fd, 1)`, `dup2(fd, 2)` (L5 §4), così i descrittori 0, 1 e 2 del programma pubblicato si riferiscono al socket. Il programma legge e scrive con `read`/`write` sui suoi soliti descrittori, e il kernel inoltra i byte sulla connessione TCP: per lui la rete non esiste. È esattamente ciò che fanno `socat TCP-LISTEN:9011,reuseaddr,fork EXEC:'python3 oracolo.py'`, `xinetd` e i *wrapper* usati nelle gare (spesso dentro un contenitore Docker per ogni connessione).

(b) Sì: con `nc 127.0.0.1 9011` vedi `Indovina il codice: ...` e `Tentativo 1> ` come in locale, perché `oracolo.py` fa `flush=True` dopo ogni messaggio.

(c)

```python
#!/usr/bin/env python3
# es11.py — l'oracolo dell'Esercizio 16 nello scheletro del §12.1
from pwn import *
HOST, PORT = '127.0.0.1', 9011
LOCALE = ['python3', 'oracolo.py']

def avvia():
    if args.REMOTE:
        return remote(args.HOST or HOST, int(args.PORT or PORT))
    return process(LOCALE)

def risolvi(io):
    noto = ''
    while True:
        for c in '0123456789abcdef':
            io.sendlineafter(b'> ', (noto + c).ljust(8, 'g').encode())
            r = io.recvline().decode()
            if 'Esatto' in r:
                return r.strip()
            if int(r.split(':')[1]) > len(noto):
                noto += c
                log.info(f'noto: {noto}')
                break
        else:
            raise RuntimeError('nessuna cifra va bene')

if __name__ == '__main__':
    context.timeout = 10
    io = avvia()
    log.success(risolvi(io))
    io.close()
```

```
$ python3 pubblica.py 9011 python3 oracolo.py &
python3 oracolo.py pubblicato su 127.0.0.1:9011
$ python3 es11.py REMOTE
[+] Opening connection to 127.0.0.1 on port 9011: Done
[*] noto: 7
...
[*] noto: 7557f6c
[+] Esatto in 77 tentativi: L8{un_oracolo_alla_volta}
[*] Closed connection to 127.0.0.1 port 9011
```

`python3 es11.py` dà lo stesso risultato in locale, e `REMOTE PORT=9011 DEBUG` mostra ogni byte scambiato. Attenzione: con `SILENT` non vedi nemmeno la flag, perché `SILENT` porta il livello a `error` e `log.success` è sotto quella soglia; se vuoi silenzio ma la flag, stampala con `print`.

(d) Un giocatore vedrebbe esattamente il problema dell'Esempio 4, ma peggiorato: dietro un socket lo standard output del programma C **non** è un terminale, quindi è bufferizzato a blocchi, e la domanda (anzi, tutto l'output) arriverebbe solo alla fine o quando il buffer da 4096 byte si riempie. L'opzione `pty` di `socat` (`EXEC:./domanda,pty,raw,echo=0`) mette tra il socket e il programma uno pseudo-terminale: il programma vede un terminale, usa il buffering a righe e, prima di leggere, svuota lo standard output. `raw,echo=0` servono a non far rielaborare i byte dal terminale (niente eco di ciò che mandi, niente traduzione di `\n` in `\r\n`, nessun carattere di controllo interpretato).

(e) Con `''` o `'0.0.0.0'` il server ascolterebbe su **tutte** le interfacce, quindi sarebbe raggiungibile da chiunque possa raggiungere la tua macchina (la rete locale, la rete dell'università, Internet se la macchina ha un indirizzo pubblico). Pubblicare così un programma qualunque significa regalare a chiunque il suo input: se il programma ha una vulnerabilità (ed è proprio per trovarle che lo stiamo studiando), chi si collega esegue codice **con il tuo utente**, sulla tua macchina. Per gli esperimenti: sempre `127.0.0.1`, e se ti serve davvero la rete, una macchina virtuale isolata.

**12.** Una soluzione:

```python
#!/usr/bin/env python3
# tubo.py — un "tube" minimo con la sola libreria standard (Esercizio 12)
import os, socket, subprocess

class Tubo:
    """Un flusso di byte con buffer di ricezione: da un socket o da un processo."""
    def __init__(self, leggi, scrivi, chiudi):
        self._leggi, self._scrivi, self._chiudi = leggi, scrivi, chiudi
        self.buffer = b''                         # dati ricevuti ma non ancora consegnati

    @classmethod
    def rete(cls, host, porta, timeout=10):
        s = socket.create_connection((host, porta), timeout=timeout)
        return cls(lambda: s.recv(4096), s.sendall, s.close)

    @classmethod
    def processo(cls, argv):
        p = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=0)
        def chiudi():
            p.stdin.close(); p.stdout.close(); p.wait()
        return cls(lambda: os.read(p.stdout.fileno(), 4096), p.stdin.write, chiudi)

    def _riempi(self):
        pezzo = self._leggi()                     # bloccante; socket.timeout se il server tace
        if not pezzo:
            raise EOFError(f'flusso chiuso; nel buffer restavano {self.buffer!r}')
        self.buffer += pezzo

    def recvuntil(self, marca, drop=False):
        inizio = 0
        while (i := self.buffer.find(marca, inizio)) < 0:
            inizio = max(0, len(self.buffer) - len(marca) + 1)   # la marca può stare a cavallo
            self._riempi()
        fine = i + len(marca)
        dati, self.buffer = self.buffer[:fine], self.buffer[fine:]
        return dati[:i] if drop else dati

    def recvline(self):
        return self.recvuntil(b'\n')

    def recvn(self, n):
        while len(self.buffer) < n:
            self._riempi()
        dati, self.buffer = self.buffer[:n], self.buffer[n:]
        return dati

    def send(self, dati):
        self._scrivi(dati)

    def sendline(self, dati):
        self.send(dati + b'\n')

    def sendafter(self, marca, dati):
        r = self.recvuntil(marca); self.send(dati); return r

    def sendlineafter(self, marca, dati):
        return self.sendafter(marca, dati + b'\n')

    def close(self):
        self._chiudi()
```

La classe non sa da dove vengono i byte: riceve tre funzioni (leggere un pezzo, scrivere, chiudere), e i due costruttori le preparano per un socket o per un processo. È la stessa idea dei tube di pwntools (§8.3), in piccolo.

(a) `p.stdout` è un oggetto file **bufferizzato**: `read(4096)` aspetta di avere 4096 byte (o EOF) prima di restituire, e il dialogo si blocca, perché il programma ha mandato una domanda di 20 byte e aspetta la risposta. `os.read(fd, 4096)` è la chiamata di sistema `read` (L4 §1): restituisce **appena** c'è qualcosa, fino a 4096 byte, come `recv` su un socket. (Esisterebbe anche `p.stdout.read1(4096)`, che fa una sola lettura; con `bufsize=0` `p.stdout` è un `FileIO` non bufferizzato e anche il suo `read` va bene. Per la scrittura `bufsize=0` serve perché `p.stdin.write` arrivi subito al programma senza `flush`.)

(b) Se la marca non c'è, aggiungere un pezzo non può crearne un'occorrenza che **termina** prima della fine dei vecchi dati; può solo crearne una che comincia negli ultimi `len(marca) − 1` byte vecchi e prosegue nel pezzo nuovo. Quindi si riparte da `len(buffer) − len(marca) + 1`. Ripartire da 0 sarebbe **corretto** ma inefficiente: con 300 righe di rumore che arrivano in tanti pezzi, ogni ricerca riscandisce tutto il buffer, e il costo diventa quadratico. Ripartire da `len(buffer)` (cioè "cerco solo nel pezzo nuovo") sarebbe invece **scorretto**: perderebbe la marca spezzata. È l'errore più comune nelle versioni scritte di getto.

(c) Il test, con una lettura finta che restituisce un byte alla volta:

```python
>>> from tubo import Tubo
>>> pezzi = iter([bytes([c]) for c in b'abcFINEdefFI'] + [b'NE\nxyz'])
>>> t = Tubo(lambda: next(pezzi, b''), None, None)
>>> t.recvuntil(b'FINE'), t.recvuntil(b'FINE', drop=True), t.recvline(), t.buffer
(b'abcFINE', b'def', b'\n', b'xyz')
>>> t.recvn(10)
Traceback (most recent call last):
  ...
EOFError: flusso chiuso; nel buffer restavano b'xyz'
```

La prima marca arriva un byte alla volta, la seconda è spezzata tra due pezzi (`FI` e `NE`), l'ultimo pezzo porta con sé dati in più (`\nxyz`) che restano nel buffer per le letture seguenti, e la chiusura produce un `EOFError` informativo. Tre requisiti, quattro righe di test, e nessun processo né rete: scrivere il codice in modo che la sorgente dei byte sia **sostituibile** è anche ciò che lo rende verificabile.

## ★★★ Sfida

**13.**

```python
#!/usr/bin/env python3
# es13.py — valutare espressioni aritmetiche senza eval, con il modulo ast
import ast, operator
from pwn import *

OP = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
      ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod}

def valuta(nodo):
    if isinstance(nodo, ast.Expression):
        return valuta(nodo.body)
    if isinstance(nodo, ast.Constant) and type(nodo.value) is int:
        return nodo.value
    if isinstance(nodo, ast.BinOp) and type(nodo.op) in OP:
        return OP[type(nodo.op)](valuta(nodo.left), valuta(nodo.right))
    if isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, ast.USub):
        return -valuta(nodo.operand)
    raise ValueError(f'nodo non ammesso: {type(nodo).__name__}')

def calcola(testo):
    if len(testo) > 1000:
        raise ValueError('espressione troppo lunga')
    return valuta(ast.parse(testo, mode='eval'))   # analizza, non esegue

io = process(['python3', 'espressioni.py'])
for _ in range(20):
    io.recvuntil(b': ')
    e = io.recvline().strip().decode()
    try:
        risposta = str(calcola(e))
    except (ValueError, SyntaxError, ZeroDivisionError) as err:
        log.warning(f'rifiuto {e[:40]}...: {err}')
        risposta = 'RIFIUTO'
    io.sendlineafter(b'? ', risposta.encode())
log.success(io.recvline().decode().strip())
```

```
$ python3 es13.py
[!] rifiuto __import__('os').system('echo HO ESEGUIT...: nodo non ammesso: Call
[+] Venti su venti: L8{ast_non_esegue_niente}
```

Il punto è la **lista bianca**: la funzione non cerca di riconoscere ciò che è pericoloso (impossibile: i modi di scrivere codice Python sono infiniti), ma accetta solo ciò che conosce. `type(nodo.value) is int` esclude anche `True` (che è un `int`, §2.2) e i `float`. (a) La trappola è una **chiamata** di funzione: `ast.parse` produce un nodo `Call` (con dentro un `Attribute` e un altro `Call` per `__import__`), che non è in nessuno dei casi ammessi e arriva al `raise` finale, già al primo livello. Nota che `ast.parse` sulla trappola **non esegue niente**: costruisce solo l'albero. (b) Il server genera lui le espressioni, quindi il suo `eval` valuta solo testo scritto da lui; il tuo `eval` valuterebbe testo scritto da **un altro**, che può essere qualunque cosa: è l'iniezione di codice, CWE-95. In una gara, un server dispettoso (o compromesso da un'altra squadra) è una possibilità reale, e il tuo script gira sulla tua macchina con i tuoi permessi. (c) No: Python arrotonda la divisione intera **verso meno infinito** e dà al resto il segno del divisore, il C tronca **verso zero** e dà al resto il segno del dividendo. `-7 // 2` vale −4 in Python, `-7 / 2` vale −3 in C; `-7 % 2` vale 1 in Python e −1 in C. Il server è scritto in Python e calcola con le regole di Python, quindi conviene calcolare in Python; se il servizio fosse un programma C, con interi a 32 bit, dovresti imitare il C: troncamento verso zero, e maschere per l'overflow (L7, Esercizio 13). (d) Un `BinOp` con operatore `ast.Pow`: se lo aggiungessi, dovresti controllare gli operandi **prima** di calcolare (per esempio esponente al massimo 64 e base limitata, o un limite sul numero di bit del risultato con `int.bit_length`), oltre al limite sulla lunghezza del testo, che ferma anche le espressioni enormemente annidate (che farebbero esaurire la ricorsione).

**14.** Dopo `bash setup_sfida.sh` e `cd ~/l8_sfida`, il primo passo è a mano:

```
$ python3 servizio.py
=== Sportello della Lezione 8 ===
Prova 1: trenta calcoli in dieci secondi.
[1/30] Quanto fa 1128 - 58?
> 1070
[2/30] Quanto fa 7395 * 41?
> ...
```

Da qui le marche: `Quanto fa `, `?`, `> `. Uno script costruito una prova alla volta, sullo scheletro del §12.1:

```python
#!/usr/bin/env python3
# es14.py — risolutore della mini-CTF della Lezione 8 (pwntools)
import base64, re
from pwn import *
HOST, PORT = '127.0.0.1', 4444
LOCALE = ['python3', 'servizio.py']

def avvia():
    if args.REMOTE:
        return remote(args.HOST or HOST, int(args.PORT or PORT))
    return process(LOCALE)

def prova1(io):
    for _ in range(30):
        io.recvuntil(b'Quanto fa ')
        a, op, b = io.recvuntil(b'?', drop=True).decode().split()
        a, b = int(a), int(b)
        risultato = {'+': a + b, '-': a - b, '*': a * b}[op]   # KeyError se l'operatore è nuovo
        io.sendlineafter(b'> ', str(risultato).encode())
    return io.recvline_contains(b'Pezzo 1').split(b': ', 1)[1]

def prova2(io):
    io.recvuntil(b'il numero ')
    n = int(io.recvuntil(b' ', drop=True))
    io.sendafter(b'> ', p32(n) + b'\n')                        # 4 byte grezzi + a capo
    return io.recvline_contains(b'Pezzo 2').split(b': ', 1)[1]

def prova3(io):
    io.recvuntil(b'base64: ')
    segreto = base64.b64decode(io.recvline().strip())
    io.sendlineafter(b'> ', segreto.hex().encode())
    return io.recvline_contains(b'Pezzo 3').split(b': ', 1)[1]

def prova4(io):
    rumore = io.recvuntil(b'Hai due secondi.\n')
    codice = re.search(rb'CODICE: ([0-9a-f]{16})', rumore).group(1)
    io.sendlineafter(b'> ', codice)
    return io.recvline_contains(b'Pezzo 4').split(b': ', 1)[1]

if __name__ == '__main__':
    context.timeout = 10
    io = avvia()
    pezzi = [prova(io).strip() for prova in (prova1, prova2, prova3, prova4)]
    io.close()
    log.success(b''.join(pezzi).decode())
```

```
$ python3 es14.py
[+] L8{python_parla_con_i_programmi_al_posto_tuo}
$ python3 servizio.py --porta 4444 &
In ascolto su 127.0.0.1:4444 (Ctrl-C per fermare)
$ python3 es14.py REMOTE
[+] Opening connection to 127.0.0.1 on port 4444: Done
[*] Closed connection to 127.0.0.1 port 4444
[+] L8{python_parla_con_i_programmi_al_posto_tuo}
$ python3 es14.py REMOTE DEBUG          # funziona anche così, in meno di un secondo
```

La flag è **`L8{python_parla_con_i_programmi_al_posto_tuo}`**. Le quattro prove:
1. **Velocità**: trenta calcoli in dieci secondi, impossibili a mano e banali per uno script (circa 0,2 secondi per tutta la sfida). Si risolve con l'analisi rigida della domanda (regola 5: tre pezzi, un operatore tra quelli noti) e **senza `eval`** (regola 6, Esempio 2). Il `KeyError` su un operatore sconosciuto è voluto: meglio fermarsi con un errore chiaro che rispondere a caso.
2. **Byte grezzi**: il numero va mandato come 4 byte little-endian (`p32`, §10.1), che dalla tastiera non si possono digitare (spesso contengono byte non stampabili). Il servizio legge **esattamente 5 byte**: per questo si usa `sendafter` con `p32(n) + b'\n'`, e non conviene un `sendline` "di testo". Nessuna conversione `str` di mezzo: `str(p32(n))` darebbe la rappresentazione `"b'...'"` (Esercizio 1i).
3. **Codifiche**: base64 in ingresso, esadecimale in uscita (§3, L7 §10): `base64.b64decode` poi `.hex()`. I byte decodificati sono casuali e non sono testo: non vanno mai decodificati in `str`.
4. **Rumore e tempo**: 300 righe da cui estrarre il codice, entro due secondi. `recvuntil` fino alla domanda raccoglie tutto il rumore in una sola lettura (il buffer del tube, §9.1), e una regex precisa (`[0-9a-f]{16}`) estrae il codice. Leggere riga per riga con `recvline` in un ciclo funzionerebbe, ma è più lento e più fragile.

Se lo script funziona in locale e non in rete, o viceversa, le cause tipiche sono: marche copiate male che per caso combaciano in un caso e non nell'altro (`\r\n` contro `\n`, spazi finali), un `sleep` usato al posto di una marca, o la lettura di dati "che sono già arrivati" in locale e non ancora in rete (il §7 e l'Esercizio 6). Con le marche giuste e solo letture "fino a", lo script è identico nei due modi, ed è il risultato da ottenere.

**15.**

```python
#!/usr/bin/env python3
# es15.py — la mini-CTF senza pwntools: solo libreria standard e tubo.py
import base64, re, sys
from tubo import Tubo

def riga_con(io, parola):
    while parola not in (r := io.recvline()):
        pass
    return r.split(b': ', 1)[1].strip()

def risolvi(io):
    pezzi = []
    for _ in range(30):
        io.recvuntil(b'Quanto fa ')
        a, op, b = io.recvuntil(b'?', drop=True).decode().split()
        a, b = int(a), int(b)
        io.sendlineafter(b'> ', str({'+': a + b, '-': a - b, '*': a * b}[op]).encode())
    pezzi.append(riga_con(io, b'Pezzo 1'))
    io.recvuntil(b'il numero ')
    n = int(io.recvuntil(b' ', drop=True))
    io.sendafter(b'> ', n.to_bytes(4, 'little') + b'\n')
    pezzi.append(riga_con(io, b'Pezzo 2'))
    io.recvuntil(b'base64: ')
    io.sendlineafter(b'> ', base64.b64decode(io.recvline().strip()).hex().encode())
    pezzi.append(riga_con(io, b'Pezzo 3'))
    rumore = io.recvuntil(b'Hai due secondi.\n')
    io.sendlineafter(b'> ', re.search(rb'CODICE: ([0-9a-f]{16})', rumore).group(1))
    pezzi.append(riga_con(io, b'Pezzo 4'))
    return b''.join(pezzi).decode()

if __name__ == '__main__':
    if len(sys.argv) == 3:                        # python3 es15.py HOST PORTA
        io = Tubo.rete(sys.argv[1], int(sys.argv[2]))
    else:
        io = Tubo.processo([sys.executable, 'servizio.py'])
    try:
        print(risolvi(io))
    finally:
        io.close()
```

```
$ python3 es15.py
L8{python_parla_con_i_programmi_al_posto_tuo}
$ python3 es15.py 127.0.0.1 4444
L8{python_parla_con_i_programmi_al_posto_tuo}
$ env -u PYTHONUNBUFFERED python3 es15.py
L8{python_parla_con_i_programmi_al_posto_tuo}
```

Il dialogo (`risolvi`) è praticamente identico a quello dell'Esercizio 14: stesse marche, stesse chiamate, perché `Tubo` ha la stessa interfaccia. Cambiano: `p32(n)` diventa `n.to_bytes(4, 'little')`; `recvline_contains` diventa una funzione di tre righe; la scelta tra locale e remoto è fatta a mano con `sys.argv` invece che con `args`. Che cosa ti dava pwntools in più: il PTY per il processo (qui le pipe), il timeout configurabile su ogni lettura anche per i processi (qui solo il socket ha un timeout: un processo che tace blocca `os.read` per sempre), la modalità `DEBUG`, `interactive`, i messaggi `log`, e la robustezza di dieci anni di uso in gara.

La versione locale funziona anche con `env -u PYTHONUNBUFFERED` perché il **servizio** svuota il proprio buffer dopo ogni messaggio (nel suo codice c'è un `flush` dopo ogni scrittura: è ciò che fa qualunque servizio di gara ben scritto). Dietro le pipe, la tua versione dipende interamente da questo: se il servizio non facesse `flush`, con `Tubo.processo` resteresti bloccato alla prima domanda (§5.3), e dovresti avviarlo con `python3 -u`, o impostare `PYTHONUNBUFFERED=1` nel suo ambiente, oppure usare uno pseudo-terminale con il modulo `pty`: esattamente le soluzioni dell'Esercizio 10.

**16.**
(a) 16⁸ = 2³² ≈ 4,3 miliardi di codici; provando a caso ne servono in media metà, circa 2 miliardi, e il servizio ne concede 150. La regola 10 dice: se la forza bruta richiede un numero di tentativi impossibile, non è la soluzione prevista, e stai cercando nel posto sbagliato. Qui la soluzione è l'informazione in più che l'oracolo ti dà.

(b)

```python
#!/usr/bin/env python3
# es16.py — ricostruire il codice una cifra alla volta
from pwn import *

def risolvi():
    io = process(['python3', 'oracolo.py'])
    noto = ''
    while True:
        for c in '0123456789abcdef':
            prova = (noto + c).ljust(8, 'g')       # 'g' non è mai una cifra giusta
            io.sendlineafter(b'> ', prova.encode())
            r = io.recvline().decode()
            if 'Esatto' in r:
                io.close()
                return r.strip()
            if int(r.split(':')[1]) > len(noto):
                noto += c
                break
        else:
            raise RuntimeError('nessuna cifra va bene: il protocollo non è quello che credo')

with context.local(log_level='error'):
    print(risolvi())
```

```
$ python3 es16.py
Esatto in 67 tentativi: L8{un_oracolo_alla_volta}
```

Il riempimento deve essere un carattere che **non può** essere giusto: con `0`, se la cifra successiva del codice fosse proprio 0, l'oracolo conterebbe anche quella e ti direbbe "2 giuste" quando ne stai provando una: lo script, che controlla `> len(noto)`, funzionerebbe lo stesso, ma uno script che controllasse `== len(noto) + 1` sbaglierebbe. `g` non è una cifra esadecimale e toglie ogni ambiguità. Il ramo `else` del `for` (§2.4) scatta se nessuna delle 16 cifre fa avanzare: non può succedere se hai capito il protocollo, ed è proprio per questo che deve fermare lo script con un errore chiaro.

(c) Per ognuna delle prime sette cifre servono da 1 a 16 tentativi, uniformemente: in media 8,5. Per l'ultima, si prova finché non arriva `Esatto`: ancora da 1 a 16, in media 8,5. Massimo 8 · 16 = **128**, media 8 · 8,5 = **68**. Su duecento partite si misura una media di circa 68 (nella prova: minimo 30, massimo 96, media 67,7). I 150 tentativi bastano **sempre**, perché 128 < 150: l'autore ha scelto il limite apposta.

(d) Il difetto comune è che il sistema rivela un'informazione **parziale** sul segreto (quanto di esso è giusto), che permette di attaccarlo un pezzo alla volta: il costo passa da *b*ⁿ (tutte le combinazioni) a *n* · *b* (ogni pezzo separatamente). Nei casi reali l'informazione non è scritta in chiaro come qui: è il **tempo** di risposta di un confronto che si ferma al primo carattere diverso (CWE-208), la differenza tra "pagina vuota" e "pagina con risultati" di un'iniezione SQL cieca, il messaggio d'errore diverso di un *padding* valido o non valido. Il rimedio è che la verifica sia **tutto o niente**, anche nei tempi: confrontare tutto il segreto sempre, in tempo costante. In Python, `hmac.compare_digest(a, b)` confronta due stringhe di byte impiegando un tempo che non dipende da **dove** si trova la prima differenza.

**17.**

```python
#!/usr/bin/env python3
# es17.py — indovina.sh della Lezione 4, con la ricerca binaria
from pwn import *

def gioca():
    io = process(['bash', 'indovina.sh'])
    io.recvline()                                 # "Ho pensato un numero..."
    basso, alto = 1, 1_000_000                    # invariante: il segreto è in [basso, alto]
    while True:
        medio = (basso + alto) // 2
        io.sendline(str(medio).encode())
        r = io.recvline().decode().strip()
        if r == 'più alto':
            basso = medio + 1
        elif r == 'più basso':
            alto = medio - 1
        elif r.startswith('giusto'):
            io.close()
            return medio, int(r.split()[2])
        else:
            raise RuntimeError(f'risposta inattesa: {r!r}')

with context.local(log_level='error'):
    print(gioca())
    n = [gioca()[1] for _ in range(300)]
    print(max(n), sum(n) / len(n))
```

```
$ python3 es17.py
(515078, 18)
20 19.01
```

(a) Invariante: il segreto *s* è sempre nell'intervallo chiuso [`basso`, `alto`]. All'inizio è vero per costruzione; se la risposta è `più alto`, *s* > `medio`, quindi *s* ∈ [`medio` + 1, `alto`], e analogamente per `più basso`. A ogni giro l'intervallo si **dimezza almeno** (perde `medio` e una delle due metà), quindi dopo un numero finito di passi o si trova *s* o l'intervallo conterrebbe un solo elemento, che è necessariamente *s*: il ciclo termina sempre con `giusto`. (b) Il massimo è ⌈log₂(1 000 001)⌉ = **20**, perché 2²⁰ = 1 048 576 > 1 000 000; la media misurata è circa 19, molto vicina al massimo (metà dei valori si trova solo all'ultimo livello dell'albero di ricerca). 25 bastano sempre. (c) Il programma risponde sempre con **una riga** completa, quindi `recvline` è la lettura esatta del protocollo: un messaggio, una riga. Non c'è prompt perché il programma usa `read` della bash, che non stampa niente prima di leggere. Il buffering non è un problema: `echo` di bash scrive ogni riga con una chiamata `write` immediata. (d) Il ramo `else` solleva un'eccezione con la risposta ricevuta: con `non è un numero` lo script si ferma subito e ti dice perché, invece di continuare a bisecare su informazioni sbagliate. (e) Lo script Python è più corto e si legge come l'algoritmo; la versione bash della Lezione 4 deve gestire il coprocesso, i suoi due descrittori e le redirezioni di ogni lettura e scrittura. Se il programma scrivesse le risposte **senza** `\n`, bash resterebbe bloccata in `read` (che legge fino a fine riga), e anche `recvline` di pwntools: ma in Python basta cambiare la lettura (per esempio `recvuntil` sulle parole finali delle tre risposte possibili, o `recvregex`), mentre in bash serve `read -d` con un delimitatore o `read -n`, e il codice diventa fragile in fretta.

## Domande di autoverifica: punti chiave attesi

1. Una variabile è un **nome** legato a un oggetto; `b = a` lega un secondo nome allo stesso oggetto. Se l'oggetto è mutabile e lo si modifica sul posto (`append`, `+=` su liste), la modifica si vede da entrambi i nomi; se è immutabile (`int`, `str`, `bytes`), ogni "modifica" crea un oggetto nuovo e lega a esso solo il nome a sinistra (§2.1).
2. `str` = testo Unicode, `bytes` = sequenza di valori 0–255. `encode` trasforma testo in byte secondo una codifica, `decode` il contrario. Si chiamano al **confine**: prima di mandare, dopo aver ricevuto, se serve testo. `'A' == b'A'` è `False`, senza errori (§3.1).
3. `b'ABC'[0]` è `65` (un `int`), `b'ABC'[0:1]` è `b'A'` (un `bytes`). Scorrendo dati binari ottieni interi su cui fare aritmetica; confrontare `dati[0] == b'A'` è sempre falso (§3.2).
4. `(0x401136).to_bytes(8, 'little')`, `struct.pack('<Q', 0x401136)`, `p64(0x401136)`; dai 6 byte trapelati: `u64(b.ljust(8, b'\x00'))` o `int.from_bytes(b, 'little')` (§3.3, §10.1).
5. Senza prefisso `struct` usa ordine e allineamento **nativi**, che inseriscono byte di riempimento e cambiano da macchina a macchina; un formato di file o di rete li fissa (Esercizio 2f).
6. In modalità testo Python decodifica (UTF-8 di solito) e traduce i fine riga: su un binario solleva `UnicodeDecodeError` o altera i dati. `'rb'` restituisce i byte esatti (§4.1).
7. Con la lista, ogni elemento arriva al programma come un argomento di `execve`, senza shell; con `shell=True` la stringa è interpretata da `/bin/sh`, e `;`, `$(...)`, `|` nel dato diventano comandi: CWE-78 (§5.2).
8. Buffering: il figlio, dietro una pipe, tiene l'output nel buffer e la domanda non arriva; stallo: entrambe le pipe piene, ognuno aspetta che l'altro legga (§5.3).
9. TCP è un flusso di byte: `recv` restituisce ciò che è arrivato, al massimo *n* byte, senza confini di messaggio. *n* byte esatti: ciclo finché non li hai (Esercizio 6); fino a una marca: buffer + ricerca + conservazione dell'eccedenza (§9.1, Esercizio 12).
10. Un oggetto con un buffer di ricezione e un'interfaccia uniforme di lettura e scrittura. `process` e `remote` sono intercambiabili: lo stesso dialogo funziona in locale e sul server (§8.3).
11. Leggere fino a una marca, fino a `\n`, esattamente *n* byte; mandare con `\n`; aspettare una marca e poi mandare; passare il controllo alla tastiera. `drop=True` toglie la marca dal risultato (§9.4–9.6).
12. Con un PTY il programma C vede un terminale e usa il buffering a righe; con `stdin=PTY` la libreria C svuota anche l'output prima di leggere, e le domande senza `\n` arrivano. Python gestisce il proprio buffer e non fa quello svuotamento: serve `-u`, `PYTHONUNBUFFERED`, o `flush` dal lato del programma (§9.2, Esempio 4, Esercizio 10).
13. Impacchettare/spacchettare interi a 32/64 bit; costruire messaggi binari da pezzi misti; XOR a chiave ripetuta; sequenze di de Bruijn e ricerca dell'offset. `p32(-1)` è fuori dall'intervallo senza segno: serve `sign=True` o una maschera (§10).
14. Le impostazioni globali (architettura, ordine dei byte, dimensione di parola, timeout, livello di log). Con `amd64` gli interi in `flat` diventano 8 byte invece di 4 (Esercizio 8).
15. Lo scheletro del §12.1: `avvia()` sceglie `remote` con `REMOTE`, altrimenti `process`; `HOST=` e `PORT=` cambiano il bersaglio; `DEBUG` mostra ogni byte (§11.3).
16. `eval` esegue qualunque codice Python: il server sceglie che cosa esegui sulla tua macchina (CWE-95). Si analizza il testo (`split`, regex) o si visita l'albero di `ast.parse` ammettendo solo numeri e operatori (Esercizio 13).
17. Il tempo necessario non è noto: in locale basta, sul server no, o il contrario rende lo script lentissimo. Si legge fino a un segnale con `recvuntil`, con un timeout come rete di sicurezza (regola 3).
18. Dove si è fermato (Ctrl-C, traceback); che cosa è passato (`DEBUG`); il programma ha scritto (buffering)?; il terminatore; i tempi; ridurre il problema (§12.3).
19. Quando la riuscita dipende da un valore casuale che non puoi controllare (un indirizzo con byte scomodi, un'estrazione). Con probabilità di successo *p*, servono in media 1/*p* tentativi, e la probabilità di fallirne *k* di fila è (1 − *p*)ᵏ: se 1/*p* è nell'ordine delle decine va bene, se è nell'ordine dei miliardi la strada è sbagliata (Esempio 6, Esercizio 16).
