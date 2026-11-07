# Modulo 1 — Lezione 8: Python per interagire con i programmi

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 8 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 14).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. scrivere ed eseguire programmi Python 3 corretti, usando con sicurezza i tipi fondamentali, il controllo di flusso, le funzioni, le eccezioni e i moduli;
2. spiegare il modello dei dati di Python (oggetti, nomi, riferimenti, mutabilità) quanto basta per non cadere negli errori più comuni;
3. lavorare con i **byte** senza esitazioni: `bytes` e `str`, codifica e decodifica, `bytearray`, `struct`, `int.to_bytes`, e leggere e scrivere file binari;
4. scrivere script da riga di comando con argomenti, standard input e output, codici di uscita;
5. eseguire altri programmi da Python con `subprocess`, sapendo quando e perché un dialogo con un processo si blocca;
6. aprire una connessione TCP con il modulo `socket`, e capire perché `recv` non restituisce "messaggi";
7. usare **pwntools** per dialogare con un programma locale o con un servizio remoto: `process`, `remote`, `recvuntil`, `sendlineafter`, `interactive`, e gli strumenti per i dati `p32`, `p64`, `u32`, `u64`, `flat`, `xor`;
8. organizzare uno script risolutivo per una sfida in modo che funzioni sia in locale sia sul server della gara, e fare il debug di un dialogo che non va.

**Prerequisiti:** Lezioni 1–5 e 7. In particolare: processi, `fork`/`exec`/`wait` e descrittori (L4 §1–4, L5 §4), il buffering dell'output (L4 §3), il dialogo con un programma interattivo in bash con `coproc` e FIFO (L4 §5.4–5.5, Esempio 6), i byte, l'endianness e le codifiche (L7). Se non hai mai scritto Python, nessun problema: la Parte I parte dall'inizio, ma va più veloce di un corso introduttivo.

**Tempo:** circa 4–5 ore di lettura e prove, 4 ore di esercizi. Questa lezione si impara **scrivendo**: tieni aperto un interprete Python accanto al testo e prova ogni esempio.

**Ripasso dalle lezioni precedenti.**
- Nella Lezione 4 abbiamo fatto dialogare uno script bash con un programma che fa domande (`indovina.sh`), usando un coprocesso. Abbiamo visto che funziona, ma è fragile: bash non è fatta per leggere "fino a questa parola" o mandare byte non stampabili. Oggi rifacciamo la stessa cosa con lo strumento giusto.
- Nella Lezione 5 abbiamo visto che cosa sono un processo figlio, i suoi descrittori e i suoi segnali. `subprocess` e `pwntools` non fanno altro che `fork`, `pipe`, `dup2`, `execve` per conto tuo.
- Nella Lezione 7 abbiamo usato Python per convertire basi, codifiche e ordini dei byte (`bytes.fromhex`, `struct`, `int.from_bytes`). Oggi diamo a quei frammenti una struttura.

**Convenzione tipografica.** `$` è il prompt della shell. `>>>` è il prompt dell'**interprete interattivo** di Python (il *REPL*): le righe che seguono senza prompt sono il risultato. I blocchi senza prompt sono **file** da salvare con il nome indicato nel commento iniziale ed eseguire con `python3 nomefile.py`.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. Python come strumento | 1–5 | Come si scrive un programma Python che lavora con file, byte e processi? |
| II. Parlare in rete | 6–7 | Come si apre una connessione e perché un dialogo si blocca? |
| III. pwntools | 8–11 | Come si dialoga con una sfida in poche righe? |
| IV. Buone abitudini | 12 | Come si scrive uno script di gara affidabile, e che cosa non fare? |
| V. La pratica | 13–18 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — Python come strumento

## 1. Perché Python, e come si usa

### 1.1 Il linguaggio della sicurezza

Python è il linguaggio più usato da chi lavora in sicurezza informatica, e il motivo non è la velocità (è molto più lento del C), ma la **velocità di scrittura**: un'idea si traduce in uno script funzionante in pochi minuti, la libreria standard copre file, rete, processi, codifiche, crittografia di base, espressioni regolari, e attorno al linguaggio esiste un ecosistema enorme di strumenti specifici: **pwntools** (sfide *pwn* e interazione), **requests** (web), **scapy** (pacchetti di rete), **pycryptodome** (crittografia), **angr** (analisi dei binari), **z3** (risolutori di vincoli). Justin Seitz e Tim Arnold, in *Black Hat Python* (cap. 1), lo dicono senza mezzi termini: per chi fa attacco e difesa, Python è il linguaggio con cui si costruiscono gli strumenti propri.

In questa lezione impariamo Python 3 (Python 2 è morto nel 2020: se trovi script vecchi con `print "ciao"` senza parentesi, sono Python 2, e vanno adattati).

### 1.2 Interprete, REPL e script

Python è un linguaggio **interpretato**: il programma `python3` legge il sorgente, lo traduce in un codice intermedio (*bytecode*, salvato nei file `.pyc` della cartella `__pycache__`) e lo esegue con una macchina virtuale. Ci sono tre modi di usarlo:

```
$ python3                         # REPL: scrivi un'istruzione, vedi il risultato
>>> 2 ** 64
18446744073709551616
>>> exit()
$ python3 -c 'print(0x41, chr(0x41))'    # una riga dalla shell, come awk (L3)
65 A
$ python3 script.py arg1 arg2            # un file
```

Il REPL è il tuo laboratorio: lo userai per provare una conversione, una funzione di una libreria, un frammento di codice prima di metterlo in uno script. Due funzioni del REPL valgono oro: `help(oggetto)` mostra la documentazione, `dir(oggetto)` elenca i suoi attributi e metodi. `ipython`, se installato, è un REPL più comodo, con completamento e colori.

Uno script si rende eseguibile come qualunque altro (L1 §10):

```python
#!/usr/bin/env python3
# saluta.py — il primo script
import sys
nome = sys.argv[1] if len(sys.argv) > 1 else 'mondo'
print(f'Ciao, {nome}!')
```

```
$ chmod +x saluta.py; ./saluta.py Zen
Ciao, Zen!
```

### 1.3 Pacchetti e ambienti virtuali

Le librerie esterne si installano con **pip** dal *Python Package Index* (PyPI). Sulle distribuzioni moderne (Debian 12, Ubuntu 23.04 e successive) `pip install` nel Python di sistema è **bloccato** (errore `externally-managed-environment`, PEP 668), per non rompere i pacchetti del sistema. La soluzione corretta è un **ambiente virtuale**: una directory con una copia isolata dell'interprete e dei suoi pacchetti.

```
$ python3 -m venv ~/venv-ctf                  # crea l'ambiente (una volta)
$ source ~/venv-ctf/bin/activate              # lo attiva: il prompt mostra (venv-ctf)
(venv-ctf) $ pip install pwntools             # installa pwntools e le sue dipendenze
(venv-ctf) $ python -c 'import pwnlib; print(pwnlib.version)'
4.15.0
(venv-ctf) $ deactivate                       # torna al Python di sistema
```

`activate` non fa magie: modifica il `PATH` della shell (L1 §12) mettendo `~/venv-ctf/bin` davanti, così che `python` e `pip` siano quelli dell'ambiente. Senza attivarlo, puoi usare direttamente `~/venv-ctf/bin/python script.py`. Su pwn.college pwntools è già installato.

## 2. Il linguaggio, in modo rigoroso

Questa sezione non sostituisce un corso di Python (per quello, *Automate the Boring Stuff with Python* di Al Sweigart, cap. 1–9, è un'ottima lettura parallela), ma dà le basi con la precisione necessaria a evitare gli errori tipici.

### 2.1 Oggetti, nomi e riferimenti

In Python **tutto è un oggetto**: un numero, una stringa, una lista, una funzione, un modulo. Ogni oggetto ha un **tipo** (`type(x)`), un'**identità** (`id(x)`, in pratica il suo indirizzo in memoria) e un **valore**. Una variabile **non contiene** un oggetto: è un **nome** che si riferisce a un oggetto. L'assegnazione `a = b` non copia niente: fa sì che `a` si riferisca allo stesso oggetto di `b`.

Questo diventa importante con gli oggetti **mutabili** (che si possono modificare dopo la creazione: liste, dizionari, insiemi, `bytearray`) e **immutabili** (numeri, stringhe, tuple, `bytes`):

```python
>>> a = [1, 2, 3]
>>> b = a              # b e a sono lo stesso oggetto
>>> b.append(4)
>>> a
[1, 2, 3, 4]
>>> c = a.copy()       # una copia (superficiale): oggetto nuovo
>>> c.append(5); a
[1, 2, 3, 4]
>>> s = 'ciao'; t = s; t += '!'    # le stringhe sono immutabili: += crea un oggetto nuovo
>>> s, t
('ciao', 'ciao!')
```

Il confronto `==` confronta i **valori**, `is` le **identità**. Si usa `is` solo per `None` (`if x is None:`).

Python è **tipizzato dinamicamente** (i tipi sono degli oggetti, non dei nomi: lo stesso nome può riferirsi prima a un intero e poi a una stringa) ma **fortemente** (non converte i tipi di nascosto: `'3' + 4` è un errore, a differenza di JavaScript o di PHP). È una protezione preziosa: molti errori di tipo emergono subito come eccezioni invece che come risultati sbagliati.

### 2.2 I tipi fondamentali

| Tipo | Esempi | Note |
|---|---|---|
| `int` | `42`, `-7`, `0x41`, `0b1010`, `0o755`, `1_000_000` | **precisione arbitraria**: nessun overflow (L7 §2.3), ma per simulare un tipo C servono le maschere (L7, Esercizio 13) |
| `float` | `3.14`, `1e-9` | IEEE 754 a 64 bit (L7 §6) |
| `bool` | `True`, `False` | sottotipo di `int` (`True + True == 2`) |
| `NoneType` | `None` | "nessun valore": restituito dalle funzioni senza `return` |
| `str` | `'ciao'`, `"ciao"`, `'''più righe'''`, `r'\d+'` | testo Unicode, immutabile (§3) |
| `bytes` | `b'ciao'`, `b'\x00\xff'` | sequenza immutabile di byte (§3) |
| `list` | `[1, 'a', b'x']` | sequenza mutabile, eterogenea |
| `tuple` | `(1, 2)`, `(1,)` | sequenza immutabile; la virgola fa la tupla, non le parentesi |
| `dict` | `{'nome': 'zen', 'uid': 1000}` | dizionario chiave → valore, ordinato per inserimento |
| `set` | `{1, 2, 3}` | insieme senza ripetizioni |

Le operazioni sugli interi da conoscere: `//` divisione intera, `%` resto, `**` potenza, `divmod(a, b)`, `pow(a, b, m)` (potenza modulare, efficientissima: la userai in RSA nel Modulo 5), `abs`, e le conversioni `int('ff', 16)`, `hex()`, `bin()`, `oct()` (L7 §1.5). La divisione `/` restituisce **sempre** un `float`, anche tra interi: `7 / 2` è `3.5`, `6 / 2` è `3.0`. In uno script di gara che calcola indirizzi o lunghezze, una `/` al posto di `//` produce un `float` che poi fa fallire `p64` o `range`.

### 2.3 Sequenze, indici e fette

Stringhe, `bytes`, liste e tuple sono **sequenze**: si indicizzano da 0, con indici negativi che contano dalla fine, e si **affettano** (*slicing*) con `[inizio:fine:passo]`, dove `fine` è escluso:

```python
>>> s = 'L8{python}'
>>> s[0], s[-1], s[3:9], s[:2], s[3:], s[::-1], s[::2]
('L', '}', 'python', 'L8', 'python}', '}nohtyp{8L', 'L{yhn')
>>> len(s), 'py' in s, s.index('{')
(10, True, 2)
```

Le operazioni sulle sequenze che userai di continuo: `len`, `in`, concatenazione `+`, ripetizione `*` (`b'A' * 64`), `sorted`, `reversed`, `min`, `max`, `sum`, e le funzioni che producono sequenze: `range(n)`, `enumerate(seq)` (coppie indice, elemento), `zip(a, b)` (coppie in parallelo).

### 2.4 Controllo di flusso

Python usa l'**indentazione** (4 spazi per convenzione) per delimitare i blocchi: non ci sono parentesi graffe, e un'indentazione sbagliata è un errore di sintassi o, peggio, un errore di logica.

```python
for i, c in enumerate('L8{'):          # for itera su qualunque sequenza
    if c.isdigit():
        print(i, c, 'è una cifra')
    elif c.isalpha():
        print(i, c, 'è una lettera')
    else:
        print(i, c, 'è altro')

n = 0
while n < 3:
    n += 1
else:                                   # l'else dei cicli: eseguito se non c'è stato break
    print('finito senza break')
```

Le **comprensioni** (*comprehension*) costruiscono una lista, un insieme o un dizionario in una riga, ed è il modo idiomatico di trasformare dati:

```python
>>> [ord(c) for c in 'ciao']
[99, 105, 97, 111]
>>> [c for c in 'L8{python}' if c.isalpha()]
['L', 'p', 'y', 't', 'h', 'o', 'n']
>>> {c: ord(c) for c in 'ab'}
{'a': 97, 'b': 98}
>>> bytes(x ^ 0x20 for x in b'Ciao')     # un generatore passato a bytes(): XOR byte per byte (L7 §4.3)
b'cIAO'
```

### 2.5 Funzioni

```python
def xor_ripetuto(dati: bytes, chiave: bytes) -> bytes:
    """Restituisce dati XOR chiave, ripetendo la chiave."""
    return bytes(b ^ chiave[i % len(chiave)] for i, b in enumerate(dati))
```

La stringa tra triple virgolette subito dopo `def` è la **docstring**, che `help()` mostra. Le annotazioni (`: bytes`, `-> bytes`) sono documentazione: Python non le controlla durante l'esecuzione. I parametri possono avere valori predefiniti (`def f(x, base=16)`), si possono passare per nome (`f(x, base=2)`), e una funzione può accettare un numero variabile di argomenti posizionali (`*args`, una tupla) e per nome (`**kwargs`, un dizionario).

Attenzione a un errore classico: un valore predefinito **mutabile** viene creato **una sola volta**, quando la funzione è definita, e condiviso tra tutte le chiamate. `def aggiungi(x, lista=[])` accumula gli elementi da una chiamata all'altra. La forma corretta è `def aggiungi(x, lista=None): if lista is None: lista = []`.

### 2.6 Eccezioni

Gli errori in Python sono **eccezioni**: oggetti che interrompono l'esecuzione e risalgono le chiamate finché qualcuno non li cattura. Se nessuno li cattura, il programma termina stampando il *traceback* (la pila delle chiamate) e il codice di uscita è 1.

```python
try:
    n = int(input('Un numero: '))
    print(100 // n)
except ValueError:
    print('non era un numero')
except ZeroDivisionError:
    print('zero no')
else:
    print('tutto bene')          # se non ci sono state eccezioni
finally:
    print('sempre')              # in ogni caso, anche dopo un return
```

Le eccezioni che incontrerai più spesso: `ValueError` (valore sbagliato, `int('x')`), `TypeError` (tipo sbagliato, `'a' + 1`, o `str` dove serve `bytes`), `KeyError` e `IndexError` (chiave o indice inesistenti), `FileNotFoundError`, `PermissionError`, `UnicodeDecodeError` (byte non validi per la codifica), `EOFError` (fine dell'input: in pwntools significa "il programma ha chiuso la connessione"), `TimeoutError`, `KeyboardInterrupt` (Ctrl-C: è il segnale `SIGINT` di L5 §8, trasformato in eccezione). Un `except Exception:` generico che "ingoia" tutto è quasi sempre un errore: nasconde i bug.

Il costrutto `with` garantisce la chiusura di una risorsa (un file, un socket, un processo) anche in caso di eccezione:

```python
with open('/etc/hostname') as f:
    print(f.read().strip())
# qui f è già chiuso
```

### 2.7 Moduli

Un **modulo** è un file `.py`; un **pacchetto** è una directory di moduli. Si importano con `import`:

```python
import os, sys                    # moduli interi: os.getcwd(), sys.argv
from base64 import b64decode      # un nome da un modulo
import struct as st               # con un altro nome
```

Python cerca i moduli nelle directory di `sys.path`, che inizia con **la directory dello script**. Per questo uno script chiamato `random.py` o `socket.py` nella tua cartella di lavoro "copre" il modulo della libreria standard, e un `import socket` in qualunque script in quella cartella carica il tuo file: è un errore frequentissimo nelle prime settimane, e anche un rischio di sicurezza quando si eseguono script in cartelle di altri (lo stesso principio del `PATH` di L1 §12).

Un file può essere sia uno script sia un modulo importabile. Il blocco

```python
if __name__ == '__main__':
    main()
```

esegue `main()` solo quando il file viene lanciato direttamente, non quando viene importato.

## 3. `bytes` e `str`: la distinzione che conta

### 3.1 Due tipi, due mondi

Nella Lezione 7 (§11.4) abbiamo anticipato la distinzione più importante di Python 3 per chi lavora in sicurezza. Ora la studiamo per bene.

- **`str`** è una sequenza di **punti di codice Unicode** (L7 §8.1): è testo astratto, senza una rappresentazione in byte definita. `len('Città')` è 5.
- **`bytes`** è una sequenza di **interi da 0 a 255**: è ciò che passa davvero in un file, in una pipe, in un socket. `len('Città'.encode())` è 6.

Il passaggio da uno all'altro richiede **sempre** una codifica:

```python
>>> 'Città'.encode('utf-8')           # str -> bytes (utf-8 è il default)
b'Citt\xc3\xa0'
>>> b'Citt\xc3\xa0'.decode('utf-8')   # bytes -> str
'Città'
>>> b'\xff\xfe'.decode('utf-8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
>>> b'\xff\xfe'.decode('utf-8', errors='replace'), b'\xff'.decode('latin-1')
('��', 'ÿ')
```

L'opzione `errors=` decide che cosa fare con i byte non validi: `'strict'` (default, eccezione), `'replace'` (carattere `�`), `'ignore'` (li scarta), `'backslashreplace'` (li mostra come `\xff`). **Latin-1** ha una proprietà utile: ogni byte da 0 a 255 corrisponde a un carattere (U+0000–U+00FF), quindi la decodifica in Latin-1 non fallisce mai ed è perfettamente reversibile. È un trucco per "trasportare" byte arbitrari dentro una `str` quando una libreria lo pretende.

### 3.2 Come si comportano i `bytes`

I `bytes` assomigliano alle stringhe, con alcune differenze decisive:

```python
>>> b = b'ABC\x00\xff'
>>> b[0]                 # un elemento è un INTERO, non un bytes
65
>>> b[0:1]               # una fetta è un bytes
b'A'
>>> list(b)
[65, 66, 67, 0, 255]
>>> bytes([72, 105])     # da una lista di interi
b'Hi'
>>> bytes(4)             # quattro byte a zero (attenzione: non b'4')
b'\x00\x00\x00\x00'
>>> b'A' * 8 + b'\x41\x42'
b'AAAAAAAAAB'
>>> b'ciao'.hex(), bytes.fromhex('63 69 61 6f')
('6369616f', b'ciao')
>>> b'riga\n'.strip(), b'a:b:c'.split(b':'), b'x'.join([b'1', b'2'])
(b'riga', [b'a', b'b', b'c'], b'1x2')
>>> b'flag{abc}'.startswith(b'flag'), b'{' in b'flag{abc}', b'flag{abc}'.find(b'{')
(True, True, 4)
```

Quasi tutti i metodi delle stringhe esistono anche per i `bytes`, ma vogliono argomenti `bytes`: `b'a:b'.split(':')` è un `TypeError`. La regola pratica per gli script di gara: **dentro, lavora in `bytes`**; converti in `str` solo per stampare o per fare calcoli sul testo (`int(b'42')` funziona, perché `int` accetta anche `bytes` che contengono cifre ASCII).

Il modo in cui Python **mostra** un `bytes` merita attenzione: i byte stampabili compaiono come caratteri ASCII, gli altri come `\xNN`, alcuni come `\n`, `\t`, `\r`. Così `b'6\x11@\x00'` sono i byte 0x36, 0x11, 0x40, 0x00: il `6` e la `@` non sono "caratteri" nel senso del programma, sono solo il modo in cui Python visualizza 0x36 e 0x40. Davanti a un output strano, `.hex()` toglie ogni ambiguità.

**`bytearray`** è la versione **mutabile** di `bytes`: utile quando devi modificare un buffer byte per byte (una patch su un file, una decifratura in loco):

```python
>>> buf = bytearray(b'ciao')
>>> buf[0] = 0x43; buf += b'!'
>>> buf, bytes(buf)
(bytearray(b'Ciao!'), b'Ciao!')
```

### 3.3 Numeri e byte: `int.to_bytes`, `struct`

Le due strade per convertire tra interi e sequenze di byte le abbiamo già incontrate (L7 §5.3). Ricapitoliamo con le regole complete:

```python
>>> (0x401136).to_bytes(8, 'little')
b'6\x11@\x00\x00\x00\x00\x00'
>>> int.from_bytes(b'\xff\xff', 'big', signed=True)
-1
>>> (-2).to_bytes(2, 'little', signed=True)
b'\xfe\xff'
>>> (300).to_bytes(1, 'little')
OverflowError: int too big to convert
```

`struct` converte **più campi insieme**, secondo una **stringa di formato**: il primo carattere è l'ordine dei byte (`<` little, `>` big, `!` rete = big, `=` nativo senza allineamento), poi un carattere per campo, eventualmente con un numero di ripetizioni: `x` byte di riempimento, `c` un carattere (bytes di lunghezza 1), `b`/`B` 1 byte con/senza segno, `h`/`H` 2 byte, `i`/`I` 4 byte, `q`/`Q` 8 byte, `f` `float`, `d` `double`, `Ns` una stringa di N byte.

```python
>>> import struct
>>> struct.pack('<HI4s', 7, 0xdeadbeef, b'zen!')
b'\x07\x00\xef\xbe\xad\xdezen!'
>>> struct.unpack('<HI4s', b'\x07\x00\xef\xbe\xad\xdezen!')
(7, 3735928559, b'zen!')
>>> struct.calcsize('<HI4s')
10
```

`unpack` restituisce **sempre** una tupla, anche con un solo campo: `(n,) = struct.unpack('<I', b)` oppure `n = struct.unpack('<I', b)[0]`. Senza il prefisso di ordine (`'HI'` invece di `'<HI'`) `struct` usa l'ordine **e l'allineamento** della macchina, e inserisce byte di riempimento tra i campi come farebbe un compilatore C: `struct.calcsize('HI')` è 8, non 6. Negli script per le sfide specifica sempre l'ordine.

## 4. File, argomenti e flussi standard

### 4.1 Leggere e scrivere file

La funzione `open(percorso, modo)` restituisce un oggetto file. I modi: `'r'` lettura di testo (default), `'w'` scrittura (tronca il file), `'a'` aggiunta in fondo, `'x'` creazione esclusiva (fallisce se il file esiste), `'+'` lettura e scrittura; aggiungere `'b'` per i **file binari** (`'rb'`, `'wb'`). In modo testo, Python decodifica i byte con la codifica della *locale* (quasi sempre UTF-8) e normalizza le fine riga; in modo binario restituisce i byte così come sono.

```python
with open('dati.bin', 'rb') as f:
    intestazione = f.read(16)        # i primi 16 byte
    f.seek(0x40)                     # salta all'offset 0x40 (L2 §7.3)
    blocco = f.read(8)
    resto = f.read()                 # tutto il resto
    print(f.tell())                  # posizione corrente

with open('righe.txt', encoding='utf-8') as f:
    for riga in f:                   # un file di testo si itera per righe (con '\n' finale)
        riga = riga.rstrip('\n')

with open('uscita.bin', 'wb') as f:
    f.write(b'\x7fELF' + bytes(12))
```

Per i casi semplici, il modulo `pathlib` offre una sintassi più compatta: `Path('f.bin').read_bytes()`, `Path('f.txt').read_text()`, `Path('out.bin').write_bytes(dati)`, `Path.home() / 'l8_sfida'`, `Path('.').glob('*.txt')`.

### 4.2 La riga di comando

`sys.argv` è la lista degli argomenti, con `sys.argv[0]` uguale al nome dello script (L1 §10.2). Per script con opzioni, il modulo `argparse` costruisce automaticamente il messaggio d'aiuto e i controlli:

```python
#!/usr/bin/env python3
# decodifica.py — decodifica un file in esadecimale o base64
import argparse, base64, sys

ap = argparse.ArgumentParser(description='Decodifica hex o base64.')
ap.add_argument('file', help='file da decodificare ("-" per lo standard input)')
ap.add_argument('-f', '--formato', choices=['hex', 'b64'], default='b64')
args = ap.parse_args()

dati = sys.stdin.buffer.read() if args.file == '-' else open(args.file, 'rb').read()
try:
    out = bytes.fromhex(dati.decode()) if args.formato == 'hex' else base64.b64decode(dati)
except ValueError as e:
    sys.exit(f'errore: {e}')          # stampa su stderr ed esce con codice 1
sys.stdout.buffer.write(out)
```

```
$ python3 decodifica.py -h
usage: decodifica.py [-h] [-f {hex,b64}] file
...
$ echo Q2lhbw== | python3 decodifica.py -; echo
Ciao
$ echo 4369616f | python3 decodifica.py -f hex -; echo
Ciao
```

Tre dettagli di questo script valgono per ogni strumento da riga di comando:

1. **`sys.stdin.buffer` e `sys.stdout.buffer`** sono le versioni **binarie** dei flussi standard. `sys.stdin.read()` restituisce una `str` decodificata, e fallisce o altera i dati se l'input non è testo valido; per dati binari serve `.buffer`;
2. **`sys.exit(messaggio)`** stampa il messaggio su standard error ed esce con codice 1; `sys.exit(n)` esce con il codice `n`. I codici di uscita seguono le stesse regole di L1 §11, e uno script ben fatto le rispetta, così da poter essere usato in una pipeline o in un `if`;
3. lo script **filtra**: legge dallo standard input e scrive sullo standard output, come i filtri della Lezione 3, ed è quindi componibile con gli altri strumenti.

### 4.3 L'ambiente e il sistema

Il modulo `os` dà accesso alle chiamate di sistema e all'ambiente (L5 §12): `os.environ` (un dizionario con l'ambiente, `os.environ.get('HOME')`), `os.getpid()`, `os.getuid()`, `os.getcwd()`, `os.chdir()`, `os.listdir()`, `os.walk()` (visita ricorsiva di un albero, come `find`), `os.stat()` (i metadati di un file: dimensione, permessi, inode, L2 §6), `os.path.join()`, `os.path.exists()`. Il modulo `shutil` copia e sposta file e alberi, il modulo `glob` espande i caratteri jolly come la shell.

## 5. Eseguire altri programmi: `subprocess`

### 5.1 `subprocess.run`

Il modo moderno di eseguire un programma da Python è la funzione `subprocess.run`. Dietro le quinte fa esattamente ciò che fa la shell (L5 §4): `fork`, eventualmente `pipe` e `dup2` per collegare i flussi, `execve`, `wait`.

```python
>>> import subprocess
>>> r = subprocess.run(['ls', '-d', '/etc', '/nonesiste'], capture_output=True, text=True)
>>> r.returncode, r.stdout, r.stderr
(2, '/etc\n', "ls: cannot access '/nonesiste': No such file or directory\n")
>>> subprocess.run(['tr', 'a-z', 'A-Z'], input=b'ciao\n', capture_output=True).stdout
b'CIAO\n'
>>> subprocess.check_output(['id', '-u'])
b'1000\n'
```

Le opzioni principali:

| Opzione | Effetto |
|---|---|
| `capture_output=True` | cattura stdout e stderr (altrimenti vanno sul terminale) |
| `text=True` | decodifica l'output in `str` (altrimenti `bytes`) |
| `input=dati` | manda `dati` sullo standard input del programma, poi lo chiude |
| `check=True` | se il codice di uscita non è 0, solleva `CalledProcessError` |
| `timeout=secondi` | se il programma non termina in tempo, lo uccide e solleva `TimeoutExpired` |
| `cwd=`, `env=` | directory corrente e ambiente del figlio |
| `stdout=subprocess.DEVNULL` | butta via l'output (come `> /dev/null`) |

Il codice di uscita segue la convenzione di Python, diversa da quella della shell: se il figlio è stato **ucciso da un segnale**, `returncode` vale **−N**, non 128 + N. `subprocess.run(['sh', '-c', 'kill -TERM $$']).returncode` è −15 (L5 §4.4).

### 5.2 Lista di argomenti contro `shell=True`

Il primo argomento di `run` è una **lista**: `['ls', '-d', percorso]`. Ogni elemento diventa un elemento di `argv`, **senza** passare da una shell: niente divisione in parole, niente espansioni, niente caratteri speciali. Esiste l'opzione `shell=True`, che accetta una stringa e la fa interpretare da `/bin/sh -c`:

```python
subprocess.run('ls -l /tmp | wc -l', shell=True)    # comodo per una pipeline...
```

È comoda, ma va evitata ogni volta che la stringa contiene dati che non controlli: un nome di file come `x; rm -rf ~` diventerebbe un comando. È lo stesso problema di `eval` e `bash -c` con dati esterni della Lezione 4 (§14.2, CWE-78). La forma con la lista è sicura per costruzione, perché nessuna shell interpreta gli argomenti.

### 5.3 `Popen` e il dialogo

`run` aspetta che il programma termini. Per **dialogare** con un programma mentre è in esecuzione (mandare una risposta dopo aver letto una domanda) serve la classe `Popen`, che avvia il processo e restituisce subito, lasciandoti i suoi flussi come file:

```python
p = subprocess.Popen(['python3', 'servizio.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
domanda = p.stdout.readline()        # legge una riga dall'output del programma
p.stdin.write(b'42\n'); p.stdin.flush()
risposta = p.stdout.readline()
p.stdin.close(); p.wait()
```

È lo schema del coprocesso della Lezione 4 (§5.5), scritto in Python. E porta con sé gli stessi due pericoli.

**Il buffering.** Quando lo standard output di un programma è una pipe e non un terminale, la libreria C (e quella di Python) lo bufferizzano **a blocchi** (L4 §3): il programma scrive la domanda, ma la domanda resta nel suo buffer e non arriva a te finché il buffer non si riempie o il programma non termina. Il tuo `readline()` aspetta per sempre. Si verifica facilmente (la variabile `PYTHONUNBUFFERED`, se impostata nel tuo ambiente, disattiva il buffering e nasconde il problema, per questo la togliamo con `env -u`):

```python
# buffer.py — il figlio scrive una domanda e aspetta 3 secondi
import subprocess, sys, select
figlio = 'import time\nprint("domanda?")\ntime.sleep(3)'
for opzioni in ([], ['-u']):
    p = subprocess.Popen([sys.executable, *opzioni, '-c', figlio], stdout=subprocess.PIPE)
    pronto, _, _ = select.select([p.stdout], [], [], 1.0)    # c'è qualcosa da leggere entro 1 s?
    print(opzioni, 'dati disponibili dopo 1 s:', bool(pronto))
    p.kill(); p.wait()
```

```
$ env -u PYTHONUNBUFFERED python3 buffer.py
[] dati disponibili dopo 1 s: False
['-u'] dati disponibili dopo 1 s: True
```

Senza `-u` (*unbuffered*), la domanda non arriva finché il figlio non termina. I rimedi, dal lato del programma con cui parli, sono quelli della Lezione 4: `python3 -u`, `stdbuf -o0` per i programmi C che usano la libreria standard, oppure presentare al programma uno **pseudo-terminale** invece di una pipe, così che creda di parlare con una persona e usi il buffering a righe. Le sfide ben fatte chiamano `setvbuf(stdout, NULL, _IONBF, 0)` all'inizio proprio per evitare il problema; le altre no, e pwntools ti offre il terminale finto con un'opzione (§9.2).

**Lo stallo (deadlock).** Se scrivi molti dati sullo standard input del figlio senza leggere il suo output, e il figlio produce molto output, entrambi si bloccano: lui aspetta che tu legga (la sua pipe di uscita è piena, 64 KiB su Linux, L4 §4.2), tu aspetti che lui legga (la tua pipe di ingresso è piena). Per input e output "tutto in una volta" si usa `p.communicate(input=dati)`, che legge e scrive in parallelo; per un vero dialogo si legge e si scrive a turno, rispettando il protocollo. È esattamente il lavoro che pwntools fa per te.

---

# Parte II — Parlare in rete

## 6. I socket

### 6.1 Che cos'è un socket

Un **socket** è l'estremità di un canale di comunicazione tra due processi, eventualmente su macchine diverse. Per il programma è un **descrittore di file** come gli altri (L4 §1): ci si scrive e ci si legge con `send` e `recv` (o `write` e `read`). La Lezione 10 spiegherà la rete in dettaglio (indirizzi IP, porte, TCP, UDP); per ora ci bastano tre idee.

1. Un servizio è identificato da un **indirizzo** e da una **porta**: `127.0.0.1:4444` è la porta 4444 della tua stessa macchina (`127.0.0.1`, il *loopback*, non esce mai dal computer); `chall.esempio.it:31337` è la porta 31337 di un server di gara.
2. **TCP** offre un **flusso di byte** affidabile e ordinato tra due estremità: ciò che una parte scrive, l'altra lo legge, nello stesso ordine, senza perdite. Ma **senza confini tra i messaggi**: è un tubo, come una pipe (L4 §4).
3. Il **client** si collega (`connect`), il **server** aspetta le connessioni (`bind`, `listen`, `accept`). Le sfide di tipo "connettiti a `host porta`" sono server TCP che, per ogni connessione, eseguono il programma della sfida con lo standard input e output collegati al socket.

Lo strumento universale per parlare con un servizio TCP a mano è **`nc`** (*netcat*): `nc host porta` collega il tuo terminale al socket. Prova con il servizio della mini-CTF:

```
$ python3 servizio.py --porta 4444 &          # in ascolto solo su 127.0.0.1
$ nc 127.0.0.1 4444
=== Sportello della Lezione 8 ===
Prova 1: trenta calcoli in dieci secondi.
[1/30] Quanto fa 2404 + 8?
>
```

Rispondere a mano a trenta domande in dieci secondi non è realistico: ci serve un programma.

### 6.2 Un client con il modulo `socket`

```python
>>> import socket
>>> s = socket.create_connection(('127.0.0.1', 4444), timeout=5)
>>> s.recv(4096)
b'=== Sportello della Lezione 8 ===\n'
>>> s.close()
```

Osserva il risultato, perché è la lezione più importante di questa Parte. Abbiamo chiesto **fino a** 4096 byte, e il server aveva già mandato tre righe; eppure `recv` ne ha restituita una sola. `recv(n)` restituisce **ciò che è arrivato finora**, da 1 a *n* byte: magari una riga, magari mezza, magari tre. Dipende da come il server ha scritto (qui con un `flush` dopo ogni riga), da come i dati sono stati divisi in pacchetti, dal momento in cui chiami `recv`. Le regole esatte:

- `recv(n)` si **blocca** finché non c'è almeno un byte, poi restituisce quelli disponibili, al massimo *n*;
- restituisce `b''` (zero byte) quando l'altra parte ha **chiuso** la connessione: è l'EOF dei socket;
- con un `timeout` impostato, se non arriva niente in tempo solleva `TimeoutError` (`socket.timeout` nelle versioni vecchie).

Allo stesso modo, `send(dati)` può inviare **solo una parte** dei dati e restituisce quanti ne ha inviati; `sendall(dati)` ripete finché non li ha inviati tutti. Si usa sempre `sendall`.

Di conseguenza, per seguire un protocollo bisogna costruirsi una funzione che **accumula** fino a trovare un segnale noto, come un a capo o un prompt:

```python
def ricevi_fino(sock, marca: bytes) -> bytes:
    """Legge dal socket finché i dati ricevuti non contengono 'marca'."""
    buf = b''
    while marca not in buf:
        pezzo = sock.recv(4096)
        if not pezzo:
            raise EOFError(buf)            # il server ha chiuso prima della marca
        buf += pezzo
    return buf
```

```python
>>> s = socket.create_connection(('127.0.0.1', 4444), timeout=5)
>>> ricevi_fino(s, b'> ')[-40:]
b'ci secondi.\n[1/30] Quanto fa 785 * 3?\n> '
>>> s.sendall(b'0\n'); ricevi_fino(s, b'\n')
b'Sbagliato. Arrivederci.\n'
>>> s.recv(100)                             # il server ha chiuso
b''
```

Questa versione ha un difetto: se in un `recv` arrivano anche dati **dopo** la marca, li restituisce insieme e la lettura successiva non li troverà più dove li aspetta. Una versione corretta deve conservare l'eccedenza in un buffer per la chiamata seguente. È esattamente ciò che fanno, con cura, i *tube* di pwntools (§9).

### 6.3 Un server minimo

Per provare i tuoi client in locale è utile saper scrivere un piccolo server. Il modulo `socketserver` gestisce `bind`, `listen` e `accept`, e chiama un metodo per ogni connessione:

```python
#!/usr/bin/env python3
# eco.py — un server che risponde in maiuscolo, una riga alla volta
import socketserver

class Gestore(socketserver.StreamRequestHandler):
    def handle(self):                         # self.rfile e self.wfile: il socket come file
        self.wfile.write(b'Scrivi qualcosa:\n')
        for riga in self.rfile:
            self.wfile.write(riga.upper())

socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('127.0.0.1', 5555), Gestore) as srv:
    srv.serve_forever()
```

Un dettaglio importante: il server ascolta su **`127.0.0.1`**, quindi è raggiungibile solo dalla tua macchina. Con `'0.0.0.0'` sarebbe raggiungibile da tutta la rete a cui sei collegato, cosa da evitare per un programma di prova. Il servizio della mini-CTF fa lo stesso.

Un'alternativa senza Python, utile per trasformare in un servizio di rete **qualunque** programma che usa stdin e stdout, è `socat`: `socat TCP-LISTEN:4444,bind=127.0.0.1,reuseaddr,fork EXEC:./programma` è il modo in cui molte sfide vengono pubblicate. Così puoi provare in locale, nelle stesse condizioni del server della gara, un binario che ti è stato dato.

## 7. Che cosa può andare storto in un dialogo

Prima di passare a pwntools, vale la pena fare l'elenco dei problemi che fanno fallire uno script di interazione. Li ritroverai tutti, e sapere che esistono è metà della soluzione.

1. **Leggere troppo presto o troppo poco.** Il caso del §6.2: hai letto la prima riga e credi di avere la domanda. Si risolve leggendo **fino a un segnale noto** (il prompt `> `, la parola `?`), mai "un pezzo e speriamo".
2. **Leggere troppo.** Hai letto fino al prompt, ma il `recv` ha portato con sé anche l'inizio del messaggio successivo, che poi non trovi più. Si risolve con un buffer che conserva l'eccedenza.
3. **Il programma non ha ancora scritto, perché bufferizza.** Il caso del §5.3: dall'altra parte c'è una pipe, e la domanda è ancora nel buffer del programma. Si risolve con uno pseudo-terminale o modificando il buffering del programma. Sui servizi remoti di solito l'autore se n'è già occupato.
4. **Il terminatore sbagliato.** Il programma legge con `fgets`/`input()`/`scanf` e aspetta un `\n` che non hai mandato (`send` invece di `sendline`); oppure il server manda `\r\n` e tu cerchi `\n` (L7 §9.2); oppure il programma legge un numero esatto di byte con `read(0, buf, 8)` e il tuo `\n` finale viene letto come primo byte della risposta successiva.
5. **Il programma legge in un modo, tu scrivi in un altro.** Se il programma fa `read(0, buf, 100)` e tu mandi due righe in rapida successione, una sola `read` può prenderle **entrambe**: dal lato di chi riceve non ci sono confini tra i messaggi (§6.2). Si risolve aspettando il prompt prima di ogni invio.
6. **Le codifiche.** Mandi una `str` dove serve `bytes` (`TypeError`), o confronti `bytes` con `str` (`b'ok' == 'ok'` è `False`, senza errori: il bug più subdolo).
7. **Il tempo.** Il servizio ha un limite di tempo (`alarm`, L5 §8.8), e il tuo script, se stampa troppo o fa calcoli lenti, lo supera. Oppure il tuo `recv` aspetta per sempre una risposta che non arriverà mai: serve un **timeout**.
8. **La chiusura.** Il programma ha terminato (o è crollato) e la connessione si è chiusa: le letture restituiscono EOF, le scritture falliscono con *Broken pipe* (L4 §4.2). In pwntools diventa un `EOFError`: leggere l'output ricevuto fino a quel momento di solito spiega perché.


---

# Parte III — pwntools

## 8. Che cos'è pwntools

### 8.1 Una libreria per le CTF

**pwntools** è una libreria Python scritta da giocatori di CTF per giocatori di CTF. Nasce nel 2013 dal team danese *Gallopsled* come raccolta degli strumenti che ogni squadra riscriveva a ogni gara: aprire una connessione, leggere fino al prompt, trasformare un indirizzo in 8 byte little-endian, generare uno shellcode, collegare `gdb` al processo. Oggi è lo standard di fatto: quasi ogni *writeup* di una sfida *pwn* che leggerai, dalle gare universitarie italiane (OliCyber, CyberChallenge.IT) alle grandi competizioni internazionali, comincia con `from pwn import *`. Anche pwn.college la usa in tutti i suoi moduli, e le macchine del dojo la hanno già installata.

La libreria ha due anime, e conviene tenerle distinte fin dall'inizio:

1. **`pwnlib`**, la libreria vera e propria, divisa in moduli: `pwnlib.tubes` (le connessioni), `pwnlib.util.packing` (i numeri come byte), `pwnlib.context` (le impostazioni globali), `pwnlib.log` (i messaggi), `pwnlib.elf` (la lettura dei file eseguibili), `pwnlib.asm` e `pwnlib.shellcraft` (assembly e shellcode), `pwnlib.gdb` (il debugger), `pwnlib.rop` (le catene ROP) e molti altri. Ogni modulo si può importare da solo.
2. **`pwn`**, un modulo "di comodo" pensato per gli script di gara: `from pwn import *` importa nello spazio dei nomi del tuo script **tutto** quello che serve (le classi `process` e `remote`, le funzioni `p64` e `u64`, l'oggetto `context`, `log`, `args`, `ELF`...), e in più modifica alcune impostazioni del terminale e legge gli argomenti magici della riga di comando (§11.3).

In questa lezione usiamo solo una piccola parte di pwnlib: i *tube*, l'impacchettamento dei dati, `context`, il logging e gli argomenti. Il resto (ELF, assembly, gdb, ROP) arriverà con i moduli di reverse engineering e di sicurezza del software, e troverai già pronto lo stesso modo di lavorare.

### 8.2 Installazione e import

pwntools funziona su Linux (e su macOS, con qualche limite). Su Windows si usa dentro WSL o in una macchina virtuale: è uno dei motivi per cui questo corso lavora su Linux fin dalla Lezione 1. Si installa con `pip` nell'ambiente virtuale del §1.3:

```
$ python3 -m venv ~/venv-ctf
$ source ~/venv-ctf/bin/activate
(venv-ctf) $ pip install pwntools
(venv-ctf) $ python3 -c 'import pwn; print(pwn.version)'
4.15.0
```

L'installazione porta con sé anche alcuni **comandi** da terminale, che sono piccoli programmi costruiti sulla libreria: `pwn checksec`, `pwn cyclic`, `pwn hex`, `pwn unhex`, `pwn asm`, `pwn template` e altri (`pwn --help` li elenca). Ne useremo un paio.

Gli esempi di questa lezione sono stati provati con pwntools 4.15 e Python 3.13. Le versioni 4.x sono compatibili tra loro per tutto ciò che vediamo qui.

**Sull'`import *`.** In un programma normale `from modulo import *` è sconsigliato, perché riempie lo spazio dei nomi di nomi che non hai scelto e che possono nasconderne altri (§2.7). Negli script di gara è invece l'uso universale, perché lo script è breve, usa decine di funzioni della libreria e deve essere scritto in fretta. Due conseguenze pratiche:

- non chiamare una tua variabile con il nome di qualcosa che pwntools esporta (`log`, `context`, `args`, `process`, `remote`, `flat`, `xor`, `sleep`, `read`, `write`...): la sovrascrivi senza alcun avviso. In particolare **`read` e `write` di pwntools non sono quelli del modulo `os`**: sono funzioni che leggono e scrivono file interi;
- `from pwn import *` importa anche, per comodità, moduli della libreria standard come `os`, `sys`, `re`, `time`, `struct`, `subprocess`. Non contarci: scrivi comunque gli `import` che ti servono, così lo script resta leggibile e funziona anche se un giorno importi solo `pwnlib`.

Se preferisci un codice più pulito, usa `import pwn` e scrivi `pwn.process(...)`, `pwn.p64(...)`. È una scelta di stile; in questa lezione usiamo la forma più comune.

**Due effetti collaterali di `from pwn import *`** che sorprendono la prima volta. Primo, pwntools prende il controllo del terminale per disegnare i suoi messaggi animati (`[x] Opening connection...` che diventa `[+] ... Done`): se lo script stampa cose strane in un ambiente senza terminale (un editor, un notebook), aggiungi l'argomento `NOTERM` (§11.3). Secondo, la libreria legge `sys.argv` e **toglie** dalla lista gli argomenti scritti TUTTI IN MAIUSCOLO, come `DEBUG` o `REMOTE`, che interpreta come comandi propri (§11.3).

### 8.3 L'idea centrale: il *tube*

Nella Parte I e nella Parte II hai visto due modi molto diversi di parlare con un programma: con `subprocess.Popen` (due pipe verso un processo figlio) e con `socket` (una connessione TCP verso un processo che può stare dall'altra parte del mondo). Le API sono diverse (`p.stdout.readline()` da una parte, `s.recv(4096)` dall'altra), ma il problema che risolvi è identico: **un flusso di byte che entra e uno che esce**, da cui devi leggere fino a un certo punto e in cui devi scrivere risposte.

pwntools prende questa osservazione sul serio e la trasforma in un'astrazione: il **tube** (letteralmente "tubo"). Un tube è un oggetto con un canale di ingresso e un canale di uscita, e con un unico insieme di metodi (`recv`, `recvline`, `recvuntil`, `send`, `sendline`, `interactive`, `close`...) che funzionano **allo stesso modo** qualunque cosa ci sia dall'altra parte. Le principali classi di tube sono:

| Classe | Dall'altra parte c'è | Equivalente "a mano" |
|---|---|---|
| `process(argv)` | un programma avviato sulla tua macchina | `subprocess.Popen` con pipe e pseudo-terminali |
| `remote(host, porta)` | un servizio TCP (o UDP, o TLS) | `socket.create_connection` |
| `listen(porta)` | un client che si collega a te | `socket.bind` + `listen` + `accept` |
| `ssh(...)` e i suoi `.process()` | un programma su una macchina remota via SSH | `ssh utente@host comando` |
| `serialtube` | una porta seriale | `pyserial` |

Questo ha una conseguenza pratica enorme, che è il motivo principale per cui pwntools è diventato lo standard: **lo stesso script funziona in locale e in gara**. In una sfida tipica ti viene dato il programma (il binario, o il sorgente Python) e l'indirizzo del server su cui gira la versione con la flag vera. Tu sviluppi e provi lo script contro la copia locale con `process`, e quando funziona cambi **una sola riga**, quella che crea il tube, per passare a `remote`. Tutto il resto del dialogo resta identico. È ciò che fa il risolutore di questa lezione (§12.1).

### 8.4 Un primo assaggio

Prima di studiare i dettagli, ecco un esempio completo che ti mostra lo stile. Riprendiamo `indovina.sh` della Lezione 4: il programma pensa un numero tra 1 e 1 000 000, risponde `più alto`, `più basso` o `giusto in N tentativi`, e concede 25 tentativi. In bash, con `coproc`, ci erano servite una ventina di righe e molta attenzione ai descrittori. In Python con pwntools:

```python
#!/usr/bin/env python3
# indovina_pwn.py — ricerca binaria contro indovina.sh della Lezione 4
from pwn import *

io = process(['bash', 'indovina.sh'])
io.recvline()                                  # "Ho pensato un numero tra 1 e 1000000..."
basso, alto = 1, 1_000_000
while True:
    medio = (basso + alto) // 2
    io.sendline(str(medio).encode())
    risposta = io.recvline().decode()
    if risposta.startswith('giusto'):
        log.success(f'{medio}: {risposta.strip()}')
        break
    elif 'alto' in risposta:
        basso = medio + 1
    else:
        alto = medio - 1
io.close()
```

```
$ python3 indovina_pwn.py
[+] Starting local process '/usr/bin/bash': pid 4121
[+] 731942: giusto in 19 tentativi
[*] Stopped process '/usr/bin/bash' (pid 4121)
```

(Il numero e il conteggio cambiano a ogni esecuzione, ma i tentativi non superano mai 20: la ricerca binaria su un milione di valori ne richiede al più ⌈log₂(1 000 001)⌉ = 20.)

Osserva tre cose. Lo script non si occupa di pipe, `fork`, descrittori o buffer: `process` fa tutto. Ogni dato che entra e che esce è di tipo **`bytes`** (`str(medio).encode()` per mandare, `.decode()` per ragionare sul testo ricevuto): è la regola che rende indispensabile il §3. E il dialogo è scritto **come lo faresti a mano**: leggi la domanda, rispondi, leggi l'esito. È questo il segreto di un buon script di interazione: ricalcare il protocollo, un passo alla volta.

## 9. I tube in dettaglio

### 9.1 Il buffer di ricezione: perché `recvuntil` funziona

Nel §6.2 avevamo scritto a mano una funzione che legge da un socket "fino a una marca", e avevamo notato il suo difetto: un `recv` può restituire, insieme alla marca, anche dei byte **successivi**, che una funzione ingenua consegna al chiamante (o butta via), e che la lettura seguente non troverà più. Ogni tube di pwntools risolve questo problema con un **buffer di ricezione** interno, ed è l'idea da cui discende tutto il resto. Vale la pena capire il meccanismo, perché spiega il comportamento di ogni metodo di lettura.

Quando chiedi a un tube di leggere, succede questo:

1. il tube guarda prima nel suo buffer: se i byte che ti servono sono già lì (perché una lettura precedente ne aveva portati più del necessario), te li dà subito, senza toccare il sistema operativo;
2. altrimenti esegue una lettura "di basso livello" (una `read` sulla pipe o sul terminale finto per `process`, una `recv` sul socket per `remote`), che restituisce **quello che c'è**, da 1 a 4096 byte, e lo aggiunge in fondo al buffer;
3. ripete finché la condizione che hai chiesto (n byte, una riga, una marca) è soddisfatta, o finché scade il tempo, o finché l'altra parte chiude;
4. ti consegna **esattamente** i byte fino al punto richiesto e lascia nel buffer l'eccedenza, che sarà la prima cosa letta la volta successiva.

```
          il programma scrive:   "Nome? "  ...  "Età? "
                                      │              │
   read() del sistema operativo:  [ "Nome? Et" ]  [ "à? " ]   ← pezzi arbitrari
                                      │
             buffer del tube:     "Nome? Et"
   recvuntil(b'? ')  restituisce: "Nome? "      e nel buffer resta "Et"
   recvuntil(b'? ')  legge ancora: buffer "Età? "  → restituisce "Età? "
```

Le conseguenze pratiche:

- **I confini dei messaggi non contano più.** Non importa come il sistema operativo spezza il flusso: tu ragioni in termini di "fino a `> `", "una riga", "8 byte". È la soluzione dei problemi 1, 2 e 5 del §7.
- **Nulla si perde.** Ciò che leggi in più resta disponibile. C'è persino un metodo, `unrecv(dati)`, che rimette dei byte **in testa** al buffer, nel caso tu abbia letto qualcosa che vuoi far rileggere a un'altra parte del codice.
- **Una lettura scaduta non consuma niente.** Se `recvuntil(b'> ', timeout=1)` non trova la marca entro un secondo, restituisce `b''` e **rimette nel buffer** quello che aveva letto nel frattempo. Puoi riprovare senza aver perso dati.

```python
>>> p = process(['bash', '-c', 'printf abcdefgh; sleep 1; printf "XYZ\\n> "; read x; echo "[$x]"; exit 3'])
>>> p.recvuntil(b'>', timeout=0.3)     # la marca arriva dopo 1 s: scade e restituisce b''
b''
>>> p.recvn(3)                         # ...ma niente è andato perso
b'abc'
>>> p.recvuntil(b'Z')                  # aspetta il resto
b'defghXYZ'
>>> p.unrecv(b'PRIMA ')                # rimette dei byte in testa al buffer
>>> p.recvline()
b'PRIMA \n'
```

### 9.2 `process`: un programma locale

`process` avvia un programma sulla tua macchina e ti restituisce un tube collegato ai suoi standard input e output. Sotto il cofano fa ciò che hai visto nella Lezione 5: `fork`, collegamento dei descrittori 0, 1 e 2 a pipe o a pseudo-terminali con `dup2`, `execve` del programma. Gli argomenti più utili:

```python
process(argv,                # lista: ['./sfida', 'arg1'] — oppure una stringa con un solo programma: './sfida'
        shell=False,         # True: argv è una riga di comando per /bin/sh (stessi rischi del §5.2)
        cwd=None,            # directory di lavoro del figlio
        env=None,            # dizionario dell'ambiente; None = eredita il tuo
        stdin=PIPE,          # PIPE oppure PTY
        stdout=PTY,          # PTY (il predefinito!) oppure PIPE
        stderr=STDOUT,       # lo standard error finisce nello stesso tube dello standard output
        raw=True,            # se si usa un PTY: modalità "grezza", senza eco e senza traduzioni
        aslr=None,           # False per disattivare la casualizzazione degli indirizzi (Modulo 4)
        timeout=...)         # timeout predefinito di tutte le letture di questo tube
```

**La lista degli argomenti.** Come per `subprocess` (§5.2), il primo argomento è una **lista**: il programma e i suoi argomenti, ciascuno come elemento separato, senza nessuna shell di mezzo. Una stringa singola è accettata, ma viene interpretata come **il nome del programma**, non come una riga di comando: `process('ls -l')` cerca un eseguibile che si chiama letteralmente `ls -l`, non lo trova e solleva un'eccezione (`'./ls -l' does not exist`). Un'altra trappola: per un programma nella directory corrente, `process('sfida')` funziona perché pwntools cerca anche lì, ma scrivi sempre `'./sfida'`, come nella shell (L1 §12). Se il programma non è eseguibile (hai scaricato il binario e il bit `x` si è perso, L6), `process` fallisce con *Permission denied*: rimedio `chmod +x sfida`. Se ti serve davvero la shell (una pipeline, una redirezione), passa `shell=True` con una stringa, sapendo che è il caso del §5.2 e va usato solo con stringhe scritte da te.

**Lo standard output è un terminale finto.** Questo è il dettaglio più importante di `process`, e risolve il problema 3 del §7 senza che tu faccia niente: per impostazione predefinita, pwntools collega lo standard output del figlio a uno **pseudo-terminale** (PTY), non a una pipe. Il programma, chiedendo `isatty(1)`, crede di scrivere su un terminale vero, e la libreria C usa quindi il buffering **a righe** (L4 §3): ogni riga arriva subito. Rifacciamo l'esperimento del §5.3 con pwntools:

```python
# buffer_pwn.py — lo stesso figlio del §5.3, con stdout su PIPE e su PTY
from pwn import *
figlio = ['python3', '-c', 'import time; print("domanda?"); time.sleep(3)']
for so in (PIPE, PTY):
    p = process(figlio, stdout=so)
    log.info(f'stdout={"PIPE" if so == PIPE else "PTY"}: {p.recv(timeout=1)!r}')
    p.kill()
```

```
$ env -u PYTHONUNBUFFERED python3 buffer_pwn.py
[+] Starting local process '/usr/bin/python3': pid 367
[*] stdout=PIPE: b''
[*] Stopped process '/usr/bin/python3' (pid 367)
[+] Starting local process '/usr/bin/python3': pid 368
[*] stdout=PTY: b'domanda?\n'
[*] Stopped process '/usr/bin/python3' (pid 368)
```

Con la pipe, in un secondo non arriva niente; con il terminale finto la domanda arriva subito. Lo standard **input**, invece, resta una pipe: il programma che chiede `isatty(0)` riceve `False`.

**Attenzione al prompt senza a capo.** Il buffering a righe svuota il buffer a ogni `\n`. Ma un prompt come `printf("Come ti chiami? ")` **non contiene** un `\n`: perché allora, in un terminale vero, lo vedi comparire? Perché la libreria C ha una regola in più: quando un programma sta per **leggere** da un flusso collegato a un terminale (o comunque non bufferizzato a blocchi), svuota prima lo standard output bufferizzato a righe. In un terminale vero lo standard input è un terminale, e la regola scatta; con `process`, lo standard input è una **pipe**, la regola non scatta, e il prompt resta nel buffer anche se lo standard output è un PTY. L'Esempio 4 lo mostra con un programma C di tre righe. Il rimedio è `process(argv, stdin=PTY)`: con **entrambi** i flussi su un terminale finto, il programma si comporta esattamente come davanti a una persona. (I programmi Python non hanno il problema: `input()` svuota da solo lo standard output prima di leggere.) Lo stesso `stdin=PTY` serve per i programmi che rifiutano di partire se non sono collegati a un terminale, o che leggono una password con `getpass`.

Con un PTY entra in gioco la **disciplina di linea** del terminale (il "driver" che, in un terminale vero, fa l'eco di ciò che scrivi, trasforma `\n` in `\r\n`, interpreta Ctrl-C e Ctrl-D come segnali e fine file). pwntools la disattiva per default con `raw=True`, perché in uno script vuoi che i byte passino **identici** in entrambe le direzioni. È per questo che un `\x04` (Ctrl-D) mandato a un `process(..., stdin=PTY)` arriva al programma come byte qualunque, e non come fine file. Se ti trovi davanti a `\r\n` inattesi, o vedi tornare indietro l'eco di ciò che hai mandato, la causa è quasi sempre un terminale non in modalità grezza.

**Controllare il processo.** Un tube `process` ha anche i metodi del processo: `p.pid`; `p.poll()` restituisce `None` se il programma è ancora vivo, altrimenti il suo **codice di uscita** (negativo se è stato ucciso da un segnale: `-11` è `SIGSEGV`, il *segmentation fault* che vedrai spessissimo nel Modulo 4, L5 §8); `p.poll(block=True)` aspetta che termini; `p.kill()` lo termina; `p.close()` chiude i canali e il processo. Quando un programma crolla, pwntools lo segnala anche nei messaggi: `[*] Process './sfida' stopped with exit code -11 (SIGSEGV) (pid 4242)`.

### 9.3 `remote` e `listen`: la rete

`remote(host, porta)` apre una connessione TCP, esattamente come `socket.create_connection` del §6.2, e la avvolge in un tube:

```python
io = remote('sfida.esempio.it', 31337)                 # TCP
io = remote('sfida.esempio.it', 443, ssl=True)          # TCP con TLS (servizi "https-like")
io = remote('10.0.0.5', 5353, typ='udp')                # UDP (raro nelle CTF)
```

Se la connessione non riesce, `remote` solleva un'eccezione e pwntools stampa `[ERROR] Could not connect to ...`: controlla l'indirizzo e la porta (spesso le gare danno il comando `nc host porta`, da cui leggi i due valori), e ricorda che molti servizi di gara sono raggiungibili solo dalla VPN della competizione.

`listen(porta)` fa il contrario: si mette in ascolto e aspetta che qualcuno si colleghi. Restituisce subito un oggetto; `wait_for_connection()` aspetta il client e restituisce il tube della connessione. È utile per provare in locale il tuo client, per ricevere una connessione "di ritorno" da un programma che stai analizzando, o per scrivere un piccolo server di prova senza `socketserver`:

```python
>>> l = listen(0, bindaddr='127.0.0.1')     # porta 0: scegli tu una porta libera
>>> l.lport
46799
>>> r = remote('127.0.0.1', l.lport)         # un client, nello stesso script
>>> c = l.wait_for_connection()              # il lato server della connessione
>>> c.sendline(b'ciao dal server')
>>> r.recvline()
b'ciao dal server\n'
```

Come per il server del §6.3, specifica `bindaddr='127.0.0.1'` se non vuoi che la porta sia raggiungibile da altre macchine: per impostazione predefinita `listen` ascolta su tutte le interfacce.

Esiste infine `ssh(user, host, password=...)`, che apre una sessione SSH e da cui puoi lanciare processi remoti con `s.process([...])` (anche loro tube) e copiare file con `s.download()` e `s.upload()`. È il modo in cui si lavora con le sfide in stile *wargame* (OverTheWire), dove il programma vulnerabile va eseguito sulla macchina del server.

### 9.4 Ricevere

I metodi di lettura sono molti, ma si riconducono a poche famiglie. Tutti restituiscono **`bytes`**, tutti accettano un argomento `timeout` (in secondi), e tutti sollevano `EOFError` se l'altra parte ha chiuso e non ci sono abbastanza dati per soddisfare la richiesta.

| Metodo | Restituisce | Note |
|---|---|---|
| `recv(n=4096)` | **quello che c'è**, da 1 a *n* byte | come `socket.recv`: non sai quanto arriva; utile solo per "dammi quello che hai" |
| `recvn(n)` | **esattamente** *n* byte | aspetta finché li ha tutti; per i dati binari di lunghezza nota |
| `recvline(keepends=True)` | una riga, fino al `\n` incluso | `keepends=False` toglie il `\n` |
| `recvlines(k)` | una lista di *k* righe | **senza** `\n` (per default `keepends=False`) |
| `recvuntil(delim, drop=False)` | tutto fino alla marca **inclusa** | `drop=True` la toglie; `delim` può essere una lista di marche: si ferma alla prima che compare |
| `recvline_contains(s)` | la prima riga che contiene `s` | scarta le righe precedenti |
| `recvregex(regex, capture=False)` | tutto fino alla prima corrispondenza | `capture=True` restituisce l'oggetto `Match`, con i gruppi |
| `recvrepeat(t)` / `clean(t)` | tutto ciò che arriva finché non c'è silenzio per *t* secondi | `clean` per svuotare il buffer prima di un nuovo passo |
| `recvall()` | tutto fino alla chiusura (EOF) | per programmi che stampano e terminano |

Qualche commento sui metodi che userai di più.

**`recvuntil` è il metodo principe.** Quasi ogni dialogo si scrive come una successione di "leggi fino al prompt, rispondi". Quando ti serve il dato che **precede** una marca, `drop=True` evita di doverla togliere a mano:

```python
io.recvuntil(b'Quanto fa ')                         # scarta tutto fino a "Quanto fa "
espressione = io.recvuntil(b'?', drop=True)         # b'1234 * 56', senza il "?"
```

È lo schema "leggi fino a A, poi fino a B": il pezzo tra le due marche è il tuo dato. La marca deve essere **abbastanza specifica**: `recvuntil(b':')` si fermerà al primo due punti del messaggio di benvenuto, magari in un orario `12:30`. Copia sempre la marca dall'output reale, inclusi spazi e punteggiatura.

**`recvline` e le righe.** Un servizio orientato alle righe si legge comodamente con `recvline()`, a cui di solito segue `.strip()` (toglie `\n`, `\r`, spazi) e `.decode()` per lavorare con il testo. Attenzione al prompt: se il programma stampa `> ` **senza** a capo e aspetta, un `recvline()` aspetterà per sempre (o fino al timeout) una riga che non arriverà finché non rispondi. È il motivo per cui si legge il prompt con `recvuntil(b'> ')` e non con `recvline()`.

**`recvregex` e la prudenza con le ripetizioni.** `recvregex` legge **un pezzo alla volta** e si ferma **appena** l'espressione regolare trova una corrispondenza nei dati arrivati finora. Con un quantificatore come `+`, questo vuol dire che può fermarsi troppo presto:

```python
>>> m = r.recvregex(rb'codice e: ([0-9a-f]+)', capture=True)   # il server ha mandato "...codice e: 1234abcd. Altre..."
>>> m.group(1)
b'1'
```

La regex era già soddisfatta dopo la prima cifra! Il rimedio è "ancorare" l'espressione con ciò che segue il dato (`rb'codice e: ([0-9a-f]+)\.'`), oppure (più semplice e più robusto) leggere la riga intera con `recvline_contains(b'codice')` o `recvuntil(b'\n')` e applicare la regex con `re.search` al risultato completo. È lo stesso principio dei problemi 1 e 2 del §7: decidi **tu** dove finisce il dato, non i tempi della rete.

**`recvall` e `recvrepeat`.** `recvall()` legge fino a EOF ed è ideale per un programma che stampa tutto e termina (`process(['./sfida', 'arg'])` seguito da `recvall()` è l'equivalente di `subprocess.run(..., capture_output=True)`). Su un servizio che non chiude mai la connessione, `recvall()` non ritorna: in quel caso usa `recvrepeat(1)` o `clean(1)`, che si fermano dopo un secondo di silenzio. Sono utili per "vedere che cosa c'è" mentre sviluppi, ma uno script finito non dovrebbe basarsi su pause e silenzi (§12.2).

**Timeout e EOF: due esiti diversi.** È importante distinguerli:

- **timeout**: i dati attesi non sono arrivati in tempo, ma la connessione è aperta. I metodi di ricezione restituiscono **`b''`** (e conservano nel buffer ciò che hanno letto). Un `b''` inatteso nello script vuol dire quasi sempre "stavo aspettando una marca che non arriverà", cioè una marca sbagliata o un passo del protocollo saltato;
- **EOF**: l'altra parte ha chiuso. I metodi sollevano **`EOFError`**. Il programma ha terminato (forse ti ha detto `Sbagliato. Arrivederci.` e se n'è andato), o è crollato, o il server ti ha disconnesso per un limite di tempo.

Il timeout predefinito è **infinito** (`context.timeout`, §11.1): senza un timeout, una lettura sbagliata blocca lo script per sempre. Puoi impostarlo per tutto lo script (`context.timeout = 5`), per un tube (`process(..., timeout=5)`) o per una singola chiamata (`recvuntil(b'> ', timeout=2)`).

### 9.5 Inviare

I metodi di invio sono quattro, e la loro differenza è tutta nel `\n` e nell'attesa:

| Metodo | Che cosa fa |
|---|---|
| `send(dati)` | scrive i byte così come sono |
| `sendline(dati)` | scrive i byte **più** `context.newline` (per default `b'\n'`) |
| `sendafter(marca, dati)` | `recvuntil(marca)` e poi `send(dati)` |
| `sendlineafter(marca, dati)` | `recvuntil(marca)` e poi `sendline(dati)` |

`sendlineafter` è la forma che userai di più, perché fonde in una riga il passo fondamentale "aspetta la domanda, poi rispondi": `io.sendlineafter(b'> ', b'42')`. Restituisce ciò che ha ricevuto fino alla marca (inclusa), così che puoi ancora esaminare la domanda: `domanda = io.sendlineafter(b'? ', b'Zen')`.

Quale scegliere tra `send` e `sendline` dipende da **come legge il programma** dall'altra parte, ed è il problema 4 del §7:

- un programma che legge **righe** (`input()` in Python, `fgets`, `getline`, `scanf("%d")`, `read` della shell) aspetta il `\n`: usa `sendline`. Con `send` il programma resta in attesa e tu, che aspetti la sua risposta, pure: uno stallo;
- un programma che legge **un numero fisso di byte** (`read(0, buf, 8)` in C, `sys.stdin.buffer.read(8)` in Python) prende esattamente quei byte: usa `send` con la lunghezza giusta. Un `\n` in più verrebbe letto come primo byte della domanda successiva (o rimarrebbe nel buffer del programma e rovinerebbe la lettura seguente);
- i **dati binari** (un intero impacchettato, un indirizzo, uno shellcode) si mandano sempre con `send`, perché possono contenere il byte `0x0a` (`\n`) al loro interno: un programma che legge righe si fermerebbe lì. Se il programma vuole davvero i byte seguiti da un a capo, come la Prova 2 della mini-CTF, aggiungi `b'\n'` a mano: `io.send(p32(n) + b'\n')`.

`send` e `sendline` accettano anche `str` (pwntools le converte, stampando un avviso: `BytesWarning: Text is not bytes; assuming ASCII`). Non contarci: con caratteri non ASCII la conversione fallisce o sbaglia, e l'avviso ti sta dicendo che lo script mescola i due tipi (problema 6 del §7). Abituati a passare sempre `bytes`, convertendo i numeri con `str(n).encode()`.

### 9.6 Dare il controllo a te: `interactive`

`io.interactive()` collega il tube al **tuo** terminale: quello che il programma scrive compare a schermo, quello che digiti viene mandato al programma, riga per riga, finché non premi Ctrl-D (o Ctrl-C) o l'altra parte chiude. Il prompt `$ ` che vedi è di pwntools, non della sfida.

Si usa in due situazioni. La prima, mentre sviluppi: lo script fa automaticamente i passi noiosi (trenta calcoli, un login) e poi ti lascia esplorare a mano il resto. La seconda, in gara, alla fine di un exploit: quando lo script ha ottenuto una shell sul server (l'obiettivo di molte sfide *pwn*, Modulo 4), `interactive()` ti fa usare quella shell per digitare `ls` e `cat flag.txt`.

```python
io = remote('sfida.esempio.it', 31337)
io.sendlineafter(b'Password: ', b'quella-che-ho-trovato')
io.interactive()                    # da qui in poi digiti tu
```

### 9.7 Chiudere, e la fine del flusso

`io.close()` chiude il tube in entrambe le direzioni (e termina il processo, se è un `process`). A volte serve chiudere **solo** la direzione di invio, per dire al programma "non arriverà altro input" senza smettere di leggere ciò che risponde: è l'equivalente di premere Ctrl-D, e con pwntools si scrive `io.shutdown('send')`. Un programma come `cat` o `sort`, che legge fino a EOF prima di rispondere, ne ha bisogno:

```python
>>> q = process(['sort'])
>>> q.send(b'pera\nmela\nbanana\n')
>>> q.shutdown('send')          # EOF sullo standard input di sort
>>> q.recvall()
b'banana\nmela\npera\n'
```

`io.connected()` dice se il tube è ancora aperto. E se uno script termina senza chiudere i tube, pwntools li chiude all'uscita, stampando `[*] Stopped process` o `[*] Closed connection`.

Quando lo script si ferma con un `EOFError`, la prima cosa da fare è chiedersi **che cosa ha detto il programma prima di chiudere**. Con i messaggi di debug (§11.2) lo vedi subito; senza, ricorda che i dati arrivati restano nel buffer, e che puoi catturare l'eccezione e stamparli:

```python
try:
    io.recvuntil(b'Pezzo 1: ')
except EOFError:
    log.failure(f'chiuso; ultime parole: {io.clean()!r}')
    raise
```

## 10. I dati: impacchettare, spacchettare, trasformare

### 10.1 `p32`, `p64`, `u32`, `u64`

Nella Lezione 7 (§6) abbiamo visto che lo stesso intero si scrive in memoria come una sequenza di byte il cui ordine dipende dall'architettura, e che x86 è **little-endian**: l'intero 0x401136 a 64 bit sta in memoria come `36 11 40 00 00 00 00 00`. Nel §3.3 di questa lezione abbiamo fatto la conversione con `int.to_bytes` e `struct.pack('<Q', ...)`. pwntools dà a queste operazioni dei nomi cortissimi, perché in una sfida *pwn* le scriverai decine di volte:

| Funzione | Che cosa fa | Equivalente con la libreria standard |
|---|---|---|
| `p8(x)`, `p16(x)`, `p32(x)`, `p64(x)` | intero → 1, 2, 4, 8 byte (*pack*) | `x.to_bytes(4, 'little')`, `struct.pack('<I', x)` |
| `u8(b)`, `u16(b)`, `u32(b)`, `u64(b)` | byte → intero (*unpack*) | `int.from_bytes(b, 'little')`, `struct.unpack('<I', b)[0]` |

```python
>>> p32(0x41424344)
b'DCBA'                                # il byte meno significativo (0x44 = 'D') per primo
>>> hex(u32(b'DCBA'))
'0x41424344'
>>> p64(0x401136)
b'6\x11@\x00\x00\x00\x00\x00'          # Python mostra come caratteri i byte stampabili: 0x36 = '6', 0x40 = '@'
>>> p16(1, endian='big')
b'\x00\x01'
>>> p64(-1, sign=True)
b'\xff\xff\xff\xff\xff\xff\xff\xff'    # complemento a due (L7 §3.2)
>>> u32(b'\xff\xff\xff\xff', sign=True)
-1
```

Tre dettagli da ricordare, ciascuno causa di molti script sbagliati.

**L'ordine predefinito è little-endian**, perché i bersagli delle CTF sono quasi sempre x86 o ARM in modalità little-endian. L'argomento `endian='big'` (o l'impostazione globale `context.endian`, §11.1) serve per i formati di rete e per le architetture big-endian.

**`u32` e `u64` vogliono esattamente 4 e 8 byte.** Questo è il caso tipico: il programma ti stampa un indirizzo "grezzo" (i suoi byte, così come stanno in memoria) e, siccome gli indirizzi a 64 bit su Linux hanno i due byte alti a zero, e una stringa C si ferma al primo zero (L7 §9.1), ne ricevi solo 6. `u64` di 6 byte fallisce con `struct.error: unpack requires a buffer of 8 bytes`. Il rimedio è riempire a destra con zeri, perché in little-endian i byte mancanti sono quelli **più significativi**:

```python
>>> u64(b'\x36\x11\x40'.ljust(8, b'\x00'))
4198710                                # = 0x401136
```

Lo schema `u64(io.recvn(6).ljust(8, b'\x00'))` (o `u64(io.recvline().strip().ljust(8, b'\x00'))`) è uno dei più frequenti nei *writeup*: impara a riconoscerlo.

**Un valore troppo grande è un errore.** `p32(2**32)` solleva un'eccezione (`'I' format requires 0 <= number <= 4294967295`), e `p32(-1)` pure, a meno di `sign=True`. È una protezione utile: ti accorgi subito di aver passato un indirizzo a 64 bit a una funzione a 32. Se invece vuoi il troncamento del C, applica tu la maschera, `p32(x & 0xffffffff)` (L7, Esercizio 13).

Esistono anche `pack(x, bits)` e `unpack(b, bits)`, che prendono la dimensione come argomento (`pack(0x41, 24)` dà 3 byte), e senza dimensione usano quella di `context.bits` (§11.1).

### 10.2 `flat`: costruire un messaggio binario

Spesso l'input da mandare a un programma è un **pezzo di memoria costruito a mano**: tot byte di riempimento, poi un intero, poi un indirizzo, poi una stringa. Concatenare a mano `b'A' * 40 + p64(x) + p64(y)` funziona, ma `flat` lo fa in modo più leggibile e meno soggetto a errori. Accetta una sequenza di elementi e li "appiattisce" in un unico `bytes`: le stringhe di byte restano come sono, gli interi vengono impacchettati con la dimensione di `context.bits` (o con `word_size=`), le liste vengono appiattite ricorsivamente.

```python
>>> context.arch = 'amd64'                              # parole di 64 bit (§11.1)
>>> flat(b'AAAA', 0xdeadbeef)
b'AAAA\xef\xbe\xad\xde\x00\x00\x00\x00'
>>> flat(1, 2, word_size=32)
b'\x01\x00\x00\x00\x02\x00\x00\x00'
```

La forma più potente è il **dizionario**, in cui le chiavi sono **posizioni** (offset in byte) e i valori sono ciò che va messo lì. Gli spazi vuoti vengono riempiti con il `filler`:

```python
>>> flat({0: b'AAAA', 16: 0xdeadbeef}, filler=b'B')
b'AAAABBBBBBBBBBBB\xef\xbe\xad\xde\x00\x00\x00\x00'
```

Leggilo come una mappa della memoria: "all'offset 0 il mio nome, all'offset 16 il numero". È esattamente il modo in cui ragionerai sullo stack nel Modulo 4, quando saprai che un certo valore sta, per esempio, 40 byte dopo l'inizio di un buffer. Senza `filler`, pwntools riempie i vuoti con la sequenza ciclica del §10.4, il che è voluto: se un byte di riempimento finisce in un posto inatteso, la sequenza ti dice quale. Con `length=` imponi la lunghezza totale (riempiendo in fondo).

Un sinonimo storico di `flat` è `fit`. Nei *writeup* li troverai entrambi.

### 10.3 Trasformazioni di uso comune

pwntools include versioni brevi di molte trasformazioni della Lezione 7. Non fanno nulla che non sapresti fare con la libreria standard, ma accorciano lo script:

| Funzione | Esempio | Standard library |
|---|---|---|
| `xor(a, b, ...)` | `xor(b'ciao', 0x42)` → `b'!+#-'` | ciclo con `^` (L7 §4.3) |
| `enhex(b)` / `unhex(s)` | `enhex(b'\x00\xff')` → `'00ff'` | `b.hex()` / `bytes.fromhex(s)` |
| `b64e(b)` / `b64d(s)` | `b64e(b'L8')` → `'TDg='` | `base64.b64encode` / `b64decode` |
| `urlencode(s)` | `urlencode('a b')` → `'%61%20%62'` | `urllib.parse.quote` (che però codifica solo i caratteri riservati) |
| `bits(x)` / `unbits(l)` | `bits(0x41)` → `[0,1,0,0,0,0,0,1]` | `format(x, '08b')` |
| `hexdump(b)` | dump in stile `xxd`, con i byte ripetuti compressi | — |

`xor` merita due parole: accetta qualunque combinazione di `bytes`, `str` e interi, e **ripete ciclicamente** l'argomento più corto fino alla lunghezza del più lungo. È quindi la funzione dello XOR a chiave ripetuta della Lezione 7: `xor(cifrato, b'k3y')` decifra con la chiave `k3y`, e `xor(cifrato, b'L8{')` ricava i primi tre byte della chiave se sai che il chiaro inizia con `L8{` (L7 §4.3, Esercizio 15).

`hexdump` è il modo più rapido di **guardare** dei dati binari che hai ricevuto, e lo stesso formato è quello dei messaggi di debug (§11.2):

```python
>>> print(hexdump(b'L8{ciao}\x00\x01\x02\xff' + b'A' * 12))
00000000  4c 38 7b 63  69 61 6f 7d  00 01 02 ff  41 41 41 41  │L8{c│iao}│····│AAAA│
00000010  41 41 41 41  41 41 41 41                            │AAAA│AAAA│
00000018
```

### 10.4 Un'anticipazione: `cyclic`

L'ultima funzione di questa sezione la userai sul serio solo nel Modulo 4, ma è così caratteristica di pwntools che vale la pena presentarla ora. `cyclic(n)` genera una stringa di *n* byte in cui **ogni sequenza di 4 byte compare una volta sola** (è una *sequenza di de Bruijn*):

```python
>>> cyclic(20)
b'aaaabaaacaaadaaaeaaa'
>>> cyclic_find(b'faaa')
20
>>> cyclic_find(0x61616166)     # lo stesso, come intero little-endian
20
```

A che cosa serve? Supponi di mandare a un programma un input lungo, e che il programma, a causa di un errore di programmazione, copi una parte di quell'input in un posto della memoria in cui non doveva (è l'idea del *buffer overflow*, Modulo 4). Se l'input è `AAAA...A`, vedrai nel debugger che un certo registro contiene `0x41414141`, ma non saprai **quale** delle tante `A` ci è finita. Se l'input è `cyclic(200)`, il registro conterrà, per esempio, `0x6161616c`, e `cyclic_find(0x6161616c)` ti dirà la posizione esatta nell'input: 44. Con `n=8` (`cyclic(200, n=8)`) le sottosequenze uniche sono di 8 byte, adatte ai registri a 64 bit. Da riga di comando: `pwn cyclic 100` e `pwn cyclic -l 0x6161616c`.

## 11. `context`, logging e argomenti

### 11.1 `context`: le impostazioni globali

`context` è un oggetto unico, globale, che contiene le impostazioni di cui molte funzioni di pwntools hanno bisogno: per quale architettura assemblare, quante byte è una parola, che ordine dei byte usare, quanto aspettare, quanto parlare. Si legge e si scrive come un oggetto qualunque:

| Attributo | Valori tipici | Che cosa influenza |
|---|---|---|
| `context.arch` | `'i386'` (predefinito), `'amd64'`, `'arm'`, `'aarch64'` | assembly e shellcode; imposta anche `bits` |
| `context.bits` | 32, 64 | la dimensione degli interi in `flat` e `pack` senza dimensione |
| `context.endian` | `'little'`, `'big'` | `p32`/`u32` e simili |
| `context.os` | `'linux'` | shellcode, chiamate di sistema |
| `context.log_level` | `'debug'`, `'info'` (predefinito), `'warning'`, `'error'` | quanti messaggi vedi (§11.2) |
| `context.timeout` | secondi; predefinito "infinito" | tutte le letture dei tube |
| `context.newline` | `b'\n'` | il terminatore di `sendline` (e di `recvline`) |
| `context.binary` | `'./sfida'` o un oggetto `ELF` | imposta automaticamente arch, bits, endian **leggendoli dal file** |

La riga che troverai all'inizio di quasi ogni script di gara è proprio l'ultima: `context.binary = elf = ELF('./sfida')`. Legge l'intestazione del file eseguibile (Modulo 3), e da quel momento pwntools sa che il bersaglio è, per esempio, un ELF x86-64 little-endian: `flat` usa parole di 8 byte, l'assembler genera codice a 64 bit, e così via. Per un servizio scritto in Python, come la nostra mini-CTF, non c'è un binario, e `context` resta ai valori predefiniti.

Per cambiare un'impostazione solo in un pezzo di codice c'è `with context.local(...)`: all'uscita dal blocco i valori tornano quelli di prima.

```python
>>> with context.local(endian='big'):
...     p32(1)
b'\x00\x00\x00\x01'
>>> p32(1)
b'\x01\x00\x00\x00'
```

### 11.2 I messaggi: `log` e il livello di debug

pwntools ha un proprio sistema di messaggi, `log`, che stampa su standard error righe con un prefisso colorato:

```python
log.info('collegato')              # [*] collegato
log.success('flag trovata')        # [+] flag trovata
log.warning('risposta strana')     # [!] risposta strana
log.failure('sbagliato')           # [-] sbagliato
log.debug('dettaglio')             # [DEBUG] dettaglio — solo con log_level = 'debug'
log.error('impossibile')           # [ERROR] impossibile — e solleva un'eccezione: lo script si ferma
```

Usarlo invece di `print` ha due vantaggi: i messaggi vanno su standard error, quindi non si mescolano con un eventuale output utile dello script (L4 §2); e il loro volume si regola con un'unica impostazione. Per le operazioni lunghe c'è `log.progress`, che mostra una riga che si aggiorna sul posto:

```python
p = log.progress('Calcoli')
for i in range(30):
    p.status(f'{i + 1}/30')         # [x] Calcoli: 17/30 (riscritta sulla stessa riga)
    ...
p.success('fatti')                  # [+] Calcoli: fatti
```

**Il livello `debug` è il tuo strumento di indagine numero uno.** Con `context.log_level = 'debug'` (o, più comodamente, aggiungendo `DEBUG` alla riga di comando, §11.3), pwntools stampa **ogni byte** che passa nei tube, in entrambe le direzioni, con il formato di `hexdump`:

```
[DEBUG] Received 0x1e bytes:
    b'[1/30] Quanto fa 4521 * 37?\n'
    b'> '
[DEBUG] Sent 0x7 bytes:
    b'167277\n'
```

Quando un dialogo non va, guardare questo registro risponde quasi sempre alla domanda "che cosa è successo davvero?": vedi se la marca che aspettavi è arrivata (e com'era scritta esattamente, con o senza spazio finale, con `\r\n` o `\n`), se hai mandato `\n` o no, se hai mandato `str(n)` o i byte di `p32(n)`, e qual è stata l'ultima cosa che il programma ha detto prima di chiudere. Con i dati binari il registro passa automaticamente alla forma esadecimale. Il rovescio della medaglia è che il registro è voluminoso: per un servizio che stampa 300 righe di rumore (la Prova 4), meglio attivarlo solo intorno al passo che non funziona, con `with context.local(log_level='debug'):`.

Al contrario, `context.log_level = 'error'` silenzia tutti i messaggi di pwntools tranne gli errori, utile per uno script che deve stampare solo il risultato.

### 11.3 Gli argomenti "magici": `args`

Come anticipato nel §8.2, `from pwn import *` esamina la riga di comando dello script e **toglie** da `sys.argv` gli argomenti scritti tutti in maiuscolo, nella forma `NOME` o `NOME=valore`, mettendoli nel dizionario `args`. Alcuni hanno un significato speciale per pwntools:

| Argomento | Effetto |
|---|---|
| `DEBUG` | `context.log_level = 'debug'` |
| `SILENT` | `context.log_level = 'error'` |
| `NOTERM` | niente animazioni né colori (per editor, file, ambienti senza terminale) |
| `LOG_LEVEL=warning` | imposta il livello a piacere |
| `TIMEOUT=5` | imposta `context.timeout` |
| `NOASLR` | per `process`: disattiva la casualizzazione degli indirizzi |

Tutti gli altri restano a disposizione del tuo script: `args.NOME` vale la stringa del valore (o `'1'`/`True` se è scritto senza `=`), e `''` (che è "falso") se l'argomento non c'è. È così che si scrive lo script "locale o remoto" in una riga:

```python
if args.REMOTE:
    io = remote(args.HOST or 'sfida.esempio.it', int(args.PORT or 31337))
else:
    io = process(['python3', 'servizio.py'])
```

```
$ python3 risolvi.py                                  # contro la copia locale
$ python3 risolvi.py REMOTE                           # contro il server della gara
$ python3 risolvi.py REMOTE HOST=127.0.0.1 PORT=4444 DEBUG
```

Gli argomenti in minuscolo, invece, restano in `sys.argv` (e `argparse` funziona normalmente): `python3 risolvi.py ciao DEBUG` lascia `sys.argv == ['risolvi.py', 'ciao']`.

### 11.4 Uno sguardo al resto della libreria

Nei moduli successivi del corso userai altre parti di pwntools. Per ora ti basta sapere che esistono e a che cosa servono, così da riconoscerle nei *writeup*:

- **`ELF('./sfida')`** apre un file eseguibile e ne espone la struttura: `elf.symbols['main']` (l'indirizzo di una funzione), `elf.got`, `elf.plt`, `elf.search(b'/bin/sh')`, `elf.checksec()`. Il comando `pwn checksec ./sfida` stampa le protezioni attive del binario (Modulo 4). Sono temi dei Moduli 2–4.
- **`gdb.debug(['./sfida'])`** e **`gdb.attach(io)`** avviano il programma sotto il debugger, o collegano `gdb` a un `process` già aperto, aprendo una nuova finestra di terminale: lo script prosegue e tu osservi la memoria del programma nel momento esatto in cui gli mandi l'input. Lo useremo dalla Lezione 9 in poi.
- **`asm('mov eax, 1')`**, **`disasm(b'...')`** e **`shellcraft`** assemblano e disassemblano istruzioni e generano shellcode (Moduli 2 e 4).
- **`ROP(elf)`** costruisce automaticamente catene ROP (Modulo 4).
- **`pwn template ./sfida --host h --port p`** scrive per te lo scheletro di uno script, con le funzioni per scegliere fra locale, remoto e debugger. È comodo, ma la prima volta scrivi lo scheletro a mano (§12.1) per sapere che cosa contiene.

La documentazione ufficiale (docs.pwntools.com) è ben fatta e ha esempi per ogni funzione; i suoi *tutorial* (github.com/Gallopsled/pwntools-tutorial) sono un ottimo complemento a questa lezione.

---

# Parte IV — Buone abitudini

## 12. Scrivere uno script di gara affidabile

### 12.1 Lo scheletro

Ecco uno scheletro che puoi copiare all'inizio di ogni sfida di interazione. Non è l'unico possibile, ma contiene tutte le decisioni che contano, e ogni riga ha un motivo.

```python
#!/usr/bin/env python3
# risolvi.py — scheletro per una sfida di interazione
from pwn import *

HOST, PORT = 'sfida.esempio.it', 31337       # dal testo della sfida ("nc sfida.esempio.it 31337")
LOCALE = ['python3', 'servizio.py']          # o ['./sfida'] per un binario

def avvia():
    """Restituisce il tube: remoto con REMOTE, altrimenti locale."""
    if args.REMOTE:
        return remote(args.HOST or HOST, int(args.PORT or PORT))
    return process(LOCALE)

def risolvi(io):
    """Il dialogo, un passo per ogni scambio del protocollo."""
    io.recvuntil(b'Benvenuto')
    io.sendlineafter(b'> ', b'1')
    ...
    return io.recvline().strip()

if __name__ == '__main__':
    context.timeout = 10                     # nessuna lettura aspetta per sempre
    io = avvia()
    flag = risolvi(io)
    log.success(f'Flag: {flag.decode()}')
    io.close()
```

Le scelte che contiene:

- **Una sola riga sceglie tra locale e remoto**, e il dialogo non sa con chi sta parlando (§8.3). Svilupperai il 90% del tempo in locale, dove puoi rilanciare il programma mille volte, leggerne il sorgente, metterlo sotto il debugger, e passerai al server solo alla fine.
- **Il dialogo sta in una funzione** che riceve il tube. Se la sfida richiede più tentativi (un valore casuale da indovinare, un exploit che riesce una volta su sedici), basta un ciclo che chiama `avvia()` e `risolvi()` finché non va.
- **Un timeout globale.** Senza, una marca sbagliata blocca lo script per sempre e tu non sai dove. Con il timeout, la lettura restituisce `b''` o lo script si ferma con un'eccezione che indica la riga esatta.
- **Le costanti in cima.** Indirizzo, porta, nome del programma: cambiano da una sfida all'altra, e averle in un posto solo evita di dimenticarne una.

### 12.2 Dieci regole

1. **Guarda prima a mano.** Prima di scrivere una riga di codice, collegati con `nc host porta` o lancia il programma e leggi esattamente che cosa scrive, che cosa chiede e come reagisce a un input sbagliato. Copia le marche dall'output reale. Uno script scritto "a memoria" del testo della sfida sbaglia uno spazio su due.
2. **Un `recvuntil` prima di ogni `send`.** Non mandare mai la risposta prima di aver letto la domanda. Funziona quasi sempre lo stesso (i dati aspettano nel buffer del programma), ma il giorno in cui il programma svuota il proprio input prima di chiedere, o legge con `read` di dimensione fissa, la tua risposta anticipata va persa o si mescola con la successiva (§7, problema 5). `sendlineafter` rende la regola gratuita.
3. **Mai `sleep` al posto di `recvuntil`.** "Aspetto mezzo secondo e poi leggo tutto" sembra funzionare in locale e fallisce sul server, dove la rete è più lenta, o funziona sul server e rende lo script dieci volte più lento del limite di tempo della sfida. Leggi **fino a un segnale**, non **per un tempo**.
4. **Sempre `bytes`.** Converti al confine: `.encode()` prima di mandare, `.decode()` dopo aver ricevuto, se ti serve il testo. Un confronto tra `bytes` e `str` è sempre falso, senza errori (§3.1).
5. **Analizza l'input in modo rigido.** Se la domanda è `Quanto fa 4521 * 37?`, estrai i tre pezzi con `split()` o con una regex precisa, e controlla che l'operatore sia uno di quelli che conosci. Uno script che "capisce più o meno" il formato produrrà risposte sbagliate nel caso che non avevi previsto, e non saprai perché.
6. **Mai `eval` su dati che arrivano dalla rete.** È la tentazione più forte con le sfide di calcolo: `eval('4521 * 37')` dà la risposta giusta in una riga. Ma `eval` esegue **qualunque** espressione Python, e il server, se è scritto da un autore dispettoso (o se è compromesso), può mandarti al posto del calcolo `__import__('os').system('rm -rf ~')`, che il tuo script eseguirebbe **sulla tua macchina**. È lo stesso errore dell'iniezione di comandi (§5.2, L4 §14.2) a parti invertite: in una CTF sei tu il bersaglio. Nel dubbio, analizza e calcola tu (Esempio 2), oppure usa `ast.literal_eval`, che accetta solo valori letterali.
7. **Prima di tutto il debug.** Quando qualcosa non va, la prima mossa è rilanciare con `DEBUG` e leggere gli ultimi scambi (§11.2). Nove volte su dieci l'errore si vede lì: la marca non è quella che credevi, hai mandato un byte in più, il programma ti aveva già salutato.
8. **Un passo alla volta.** Costruisci lo script incrementalmente: prima la connessione e la prima lettura, poi il primo scambio, controlla che funzioni, poi il secondo. Uno script di cento righe scritto tutto insieme e lanciato una volta sola è un problema di cento righe da indagare.
9. **Fai stampare a te le informazioni utili.** `log.info` dei valori intermedi (il numero ricevuto, la risposta calcolata) costa poco e, quando il server risponde `Sbagliato`, ti dice subito se l'errore è nella lettura o nel calcolo.
10. **Rispetta il servizio.** Il server della gara è condiviso da tutte le squadre. Un ciclo che apre mille connessioni al secondo per forza bruta non è quasi mai la soluzione prevista, può farti escludere dalla gara e rallenta gli altri. E ricorda la regola di fondo del corso: questi strumenti si usano **solo** contro programmi e servizi che hai il permesso di attaccare, cioè le sfide della gara, le tue macchine virtuali, le piattaforme di allenamento.

### 12.3 Quando il dialogo non va: un metodo

Quando lo script si blocca o si ferma con un errore, procedi così, nell'ordine.

1. **Dove si è fermato?** Se è bloccato, interrompilo con Ctrl-C: il *traceback* (§2.6) indica la riga che stava eseguendo, quasi sempre un `recv...` che aspetta una marca che non arriverà. Se si è fermato con `EOFError`, il programma ha chiuso: che cosa aveva scritto prima?
2. **Che cosa è passato davvero?** Rilancia con `DEBUG` e confronta, byte per byte, l'ultima cosa ricevuta con la marca che aspettavi, e l'ultima cosa mandata con quella che il programma si aspettava.
3. **Il programma ha davvero scritto?** Se in modalità debug non arriva niente, mentre a mano (`nc` o il terminale) il programma risponde, sospetta il buffering (§5.3, §9.2): stai usando `stdout=PIPE`? Il programma è dietro un `socat` senza `pty`?
4. **Il terminatore è giusto?** `send` contro `sendline`, `\n` contro `\r\n`, un `read` di dimensione fissa (§9.5).
5. **I tempi.** Il servizio ha un limite di tempo? Lo script stampa troppo (con `DEBUG` attivo, 300 righe di rumore possono costare secondi)? Prova senza `DEBUG`, o attivalo solo nel passo che ti interessa.
6. **Riduci il problema.** Isola lo scambio che non funziona in uno script di cinque righe, oppure fallo a mano con `interactive()` subito prima del punto critico.

### 12.4 Quando pwntools non c'è

A volte pwntools non è disponibile: una macchina di gara senza accesso a Internet, un sistema su cui non puoi installare pacchetti, un ambiente Windows. Ti resta la libreria standard, e la Parte II ti ha dato tutti i pezzi: `socket.create_connection`, un buffer di ricezione con una funzione `recvuntil` scritta da te (Esercizio 12), `subprocess.Popen` con `-u` o `stdbuf` per il buffering. Saper scrivere lo stesso risolutore **senza** pwntools è il modo migliore per capire che cosa fa pwntools, ed è per questo che la mini-CTF di questa lezione si può risolvere in entrambi i modi.

---

# Parte V — La pratica

## 13. Esempi svolti

Tutti gli esempi sono stati eseguiti su Linux x86-64 con Python 3.13, pwntools 4.15 e gcc. Salva i file in una directory di prova (`mkdir ~/l8 && cd ~/l8`), con il nome indicato nel commento iniziale. I numeri casuali e i PID cambieranno a ogni esecuzione.

### Esempio 1 — Lo stesso dialogo, con e senza pwntools

**Il problema.** Il programma `domande.py` chiede il nome e l'età. Vogliamo rispondere `Zen` e `20` con uno script, e leggere la risposta finale.

```python
#!/usr/bin/env python3
# domande.py — chiede nome ed età e risponde
nome = input('Come ti chiami? ')
eta = int(input(f'Ciao {nome}. Quanti anni hai? '))
print(f'Tra dieci anni ne avrai {eta + 10}.')
```

**Ragionamento.** Le due domande finiscono con `? ` e **non** vanno a capo: il programma scrive la domanda e si ferma ad aspettare sulla stessa riga. Quindi non possiamo leggerle con `readline`, che aspetterebbe un `\n` che non arriverà prima della nostra risposta. Dobbiamo leggere **fino alla marca** `? `.

**Con la sola libreria standard.** Il modo più semplice di leggere "fino a una marca" senza rischiare di leggere troppo (§6.2) è leggere un byte alla volta:

```python
# es1_std.py — lo stesso dialogo con la sola libreria standard
import subprocess

def leggi_fino(f, marca):
    dati = b''
    while not dati.endswith(marca):
        c = f.read(1)                     # un byte alla volta: lento, ma non legge mai troppo
        if not c:
            raise EOFError(dati)
        dati += c
    return dati

p = subprocess.Popen(['python3', 'domande.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
leggi_fino(p.stdout, b'Come ti chiami? ')
p.stdin.write(b'Zen\n'); p.stdin.flush()
leggi_fino(p.stdout, b'Quanti anni hai? ')
p.stdin.write(b'20\n'); p.stdin.flush()
print(p.stdout.readline().decode().strip())
p.stdin.close(); p.wait()
```

Funziona perché `input()` di Python svuota da solo lo standard output prima di leggere: con un programma C che non lo fa, `leggi_fino` aspetterebbe per sempre (Esempio 4). Nota anche le due `flush()`: senza, il nostro `Zen\n` resterebbe nel buffer **del nostro** `p.stdin` (§5.3).

**Con pwntools.**

```python
#!/usr/bin/env python3
# es1.py — dialogo con domande.py
from pwn import *
io = process(['python3', 'domande.py'])
io.sendlineafter(b'Come ti chiami? ', b'Zen')
io.sendlineafter(b'Quanti anni hai? ', b'20')
log.info(io.recvline().decode().strip())
io.close()
```

```
$ python3 es1.py
[+] Starting local process '/usr/bin/python3': pid 604
[*] Tra dieci anni ne avrai 30.
[*] Stopped process '/usr/bin/python3' (pid 604)
```

**Che cosa imparare.** La struttura del dialogo è **identica** nei due script: aspetta la domanda, rispondi, ripeti. pwntools elimina la meccanica (pipe, flush, lettura byte per byte, buffer) e lascia solo il protocollo. Nota la marca della seconda domanda: è `Quanti anni hai? `, e non `? `, perché la seconda domanda contiene anche `Ciao Zen.`; con `? ` funzionerebbe lo stesso, ma una marca specifica protegge da sorprese se il testo cambia.

### Esempio 2 — Una raffica di calcoli, senza `eval`

**Il problema.** `calcoli.py` fa dieci domande del tipo `Domanda 3: 516553 / 589 = ` e, alla prima risposta sbagliata, termina. Le divisioni sono sempre esatte.

```python
#!/usr/bin/env python3
# calcoli.py — dieci operazioni in fila
import random
for i in range(10):
    a, b, op = random.randint(1, 999), random.randint(1, 999), random.choice('+-*/')
    if op == '/': a *= b                       # divisione sempre esatta
    r = input(f'Domanda {i + 1}: {a} {op} {b} = ')
    if r != str({'+': a + b, '-': a - b, '*': a * b, '/': a // b}[op]):
        print('Sbagliato!'); exit(1)
print('Bravo: L8{esempio_due}')
```

**Ragionamento.** La scorciatoia sarebbe `eval(b'516553 / 589')`, che però dà `877.0` (un `float`: in Python 3 `/` è la divisione reale) e, soprattutto, viola la regola 6 del §12.2. Analizziamo la domanda con un'espressione regolare **completa**, ancorata alla fine (`= $`), che accetta solo il formato atteso, e calcoliamo con le funzioni del modulo `operator`, scelte da un dizionario: se arriva un operatore che non conosciamo, il `KeyError` ci avverte invece di farci rispondere a caso. Usiamo `log.progress` per vedere a che punto siamo.

```python
#!/usr/bin/env python3
# es2.py — risolve calcoli.py senza eval
from pwn import *
import operator, re

OP = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
FORMATO = re.compile(rb'Domanda (\d+): (-?\d+) ([-+*/]) (-?\d+) = $')

io = process(['python3', 'calcoli.py'])
barra = log.progress('Calcoli')
for _ in range(10):
    domanda = io.recvuntil(b'= ')
    m = FORMATO.search(domanda)
    if not m:
        log.error(f'formato inatteso: {domanda!r}')
    n, a, op, b = m.groups()
    risultato = OP[op.decode()](int(a), int(b))
    barra.status(f'{n.decode()}: {a.decode()} {op.decode()} {b.decode()} = {risultato}')
    io.sendline(str(risultato).encode())
barra.success('fatti')
log.success(io.recvline().decode().strip())
```

```
$ python3 es2.py
[+] Starting local process '/usr/bin/python3': pid 607
[+] Calcoli: fatti
[+] Bravo: L8{esempio_due}
[*] Stopped process '/usr/bin/python3' (pid 607)
```

(Durante l'esecuzione la riga `[x] Calcoli: ...` si aggiorna sul posto; con `NOTERM` vedi invece tutte le righe una sotto l'altra.)

**Che cosa imparare.** Tre dettagli. La regex lavora su `bytes` (`rb'...'`), perché `domanda` è `bytes`: mescolare un pattern `str` con dati `bytes` è un `TypeError`. `int()` accetta direttamente dei `bytes` che contengono cifre ASCII (`int(b'589')` è 589), quindi non serve decodificare i numeri. E `-?\d+` accetta anche i negativi: qui non compaiono come operandi, ma in un servizio che rimanda i risultati intermedi potrebbero, ed è meglio prevederli che scoprire il problema alla domanda 27 di 30.

### Esempio 3 — Byte grezzi: leggere un indirizzo e rimandarlo

**Il problema.** Il programma C seguente stampa l'indirizzo della sua funzione `main` come **byte grezzi** (i 6 byte bassi, così come stanno in memoria) e chiede indietro `main + 0x10` come intero di 8 byte little-endian. È la forma, ridotta all'osso, di una situazione che incontrerai in ogni sfida *pwn* del Modulo 4: il programma "perde" un indirizzo, tu lo leggi, ci fai un calcolo e lo usi.

```c
// indirizzo.c — stampa un indirizzo come byte grezzi e vuole indietro l'indirizzo + 0x10
#include <stdio.h>
#include <stdint.h>
#include <unistd.h>

int main(void) {
    setvbuf(stdout, NULL, _IONBF, 0);            // niente buffering: la sfida è "ben fatta"
    uint64_t indirizzo = (uint64_t)&main, risposta = 0;
    printf("Indirizzo di main: ");
    write(1, &indirizzo, 6);                     // solo i 6 byte bassi, così come stanno in memoria
    printf("\nMandami main + 0x10, 8 byte little-endian: ");
    if (read(0, &risposta, 8) != 8) return 1;
    if (risposta == indirizzo + 0x10) puts("Esatto: L8{esempio_tre}");
    else printf("No: ho ricevuto 0x%lx\n", risposta);
    return 0;
}
```

```
$ gcc -o indirizzo indirizzo.c
```

(Non preoccuparti se il C ti è ancora poco familiare: lo studieremo nella Lezione 9. Qui conta solo il **protocollo**: 6 byte grezzi in uscita, 8 byte grezzi in ingresso letti con `read`.)

**Ragionamento.**
- I 6 byte vanno letti con **`recvn(6)`**, non con `recvline()`: sono byte arbitrari, e uno di essi potrebbe valere `0x0a`. Con `recvline` avremmo un dato troncato una volta ogni tanto, l'errore più difficile da trovare perché "a volte funziona".
- I byte sono in little-endian e mancano i due più significativi (che valgono zero): `u64(grezzo.ljust(8, b'\x00'))` (§10.1).
- Il programma legge **esattamente 8 byte** con `read`: mandiamo `p64(...)` con **`send`**, senza `\n` (§9.5).

```python
#!/usr/bin/env python3
# es3.py — leggere un indirizzo grezzo e rimandarlo modificato
from pwn import *
io = process(['./indirizzo'])
io.recvuntil(b'Indirizzo di main: ')
grezzo = io.recvn(6)                       # 6 byte esatti: NON recvline, potrebbero contenere 0x0a
indirizzo = u64(grezzo.ljust(8, b'\x00'))
log.info(f'byte ricevuti: {grezzo.hex(" ")}  ->  main = {hex(indirizzo)}')
io.sendafter(b'little-endian: ', p64(indirizzo + 0x10))
log.success(io.recvline().decode().strip())
```

```
$ python3 es3.py
[+] Starting local process './indirizzo': pid 623
[*] byte ricevuti: e9 61 27 9a 1d 56  ->  main = 0x561d9a2761e9
[+] Esatto: L8{esempio_tre}
[*] Process './indirizzo' stopped with exit code 0 (pid 623)
```

**Che cosa imparare.** Osserva i byte: `e9 61 27 9a 1d 56` letti al contrario danno `0x561d9a2761e9`. Se rilanci, l'indirizzo cambia (`0x5604c6e381e9`, poi un altro ancora): è la **casualizzazione degli indirizzi** (ASLR, con un eseguibile PIE), una delle protezioni che studieremo nel Modulo 4, e il motivo per cui nelle sfide gli indirizzi vanno letti **durante** l'esecuzione, non scritti a mano nello script. Le ultime tre cifre esadecimali (`1e9`) invece restano uguali: la casualizzazione sposta il programma di un multiplo di 4096 byte (una pagina, 0x1000). Prova a rilanciare con `python3 es3.py NOASLR`: l'indirizzo sarà sempre lo stesso, `0x5555555551e9`, l'indirizzo a cui Linux carica un eseguibile PIE quando la casualizzazione è disattivata.

### Esempio 4 — Il programma che non risponde

**Il problema.** Questo programma C, "mal fatto", non disattiva il buffering:

```c
// domanda.c — un programma "mal fatto": nessun setvbuf
#include <stdio.h>
int main(void) {
    char nome[64];
    printf("Come ti chiami? ");                  // niente \n: resta nel buffer di stdio
    if (!fgets(nome, sizeof nome, stdin)) return 1;
    printf("Ciao, %s", nome);
    return 0;
}
```

Lanciato a mano in un terminale funziona perfettamente. Da uno script, apparentemente no. Proviamo quattro configurazioni, con un timeout di due secondi per non restare bloccati:

```python
#!/usr/bin/env python3
# es4.py — lo stesso dialogo con quattro configurazioni
from pwn import *
prove = [('stdout=PTY (predefinito)', dict(argv=['./domanda'])),
         ('stdout=PIPE',              dict(argv=['./domanda'], stdout=PIPE)),
         ('stdin=PTY, stdout=PTY',    dict(argv=['./domanda'], stdin=PTY)),
         ('PIPE + stdbuf -o0',        dict(argv=['stdbuf', '-o0', './domanda'], stdout=PIPE))]
for nome, opzioni in prove:
    with context.local(log_level='error'):
        io = process(**opzioni)
        domanda = io.recvuntil(b'? ', timeout=2)
    if domanda:
        io.sendline(b'Zen')
        log.success(f'{nome}: {io.recvline().decode().strip()}')
    else:
        log.failure(f'{nome}: nessuna domanda entro 2 s')
    io.close()
```

```
$ gcc -o domanda domanda.c && python3 es4.py        # tolte le righe "[*] Stopped process"
[-] stdout=PTY (predefinito): nessuna domanda entro 2 s
[-] stdout=PIPE: nessuna domanda entro 2 s
[+] stdin=PTY, stdout=PTY: Ciao, Zen
[+] PIPE + stdbuf -o0: Ciao, Zen
```

**Ragionamento.** Analizziamo le quattro righe con la teoria del §9.2 e della Lezione 4 (§3).
1. **Predefinito.** Lo standard output è un PTY, quindi bufferizzato a righe. Ma la domanda non ha `\n`, e lo standard input è una **pipe**: quando `fgets` va a leggere, la libreria C non ha motivo di svuotare lo standard output. La domanda resta nel buffer e il nostro `recvuntil` scade. (Il programma non è bloccato: aspetta noi, e noi aspettiamo lui.)
2. **Pipe.** Ancora peggio: buffering a blocchi da 4096 byte; la domanda arriverebbe solo alla fine del programma.
3. **Entrambi PTY.** Il programma crede di avere davanti una persona: prima di leggere da un terminale, la libreria C svuota lo standard output bufferizzato a righe. La domanda arriva.
4. **`stdbuf -o0`** chiede alla libreria C, prima di avviare il programma, di non bufferizzare affatto lo standard output (L4 §3.3): ogni `printf` viene scritto subito, anche su una pipe. Funziona per i programmi dinamici che usano `stdio`; non per quelli che gestiscono il buffering da sé o sono compilati staticamente.

**Che cosa imparare.** Un `recvuntil` che scade su una domanda che "a mano si vede" è il sintomo tipico del buffering. In locale si risolve con `stdin=PTY` (o `stdbuf`). Su un servizio remoto non puoi intervenire: se l'autore ha pubblicato il programma con `socat` e una pipe (§6.3), il server ha lo stesso problema per **tutti** i giocatori, e di solito se ne accorge e lo corregge con `setvbuf` o con l'opzione `pty` di `socat`. Se non lo fa, la soluzione è mandare la risposta **senza** aspettare la domanda (la regola 2 del §12.2 ha questa sola eccezione, e l'unico modo di saperlo è aver capito il perché).

### Esempio 5 — Un servizio di rete con dati da elaborare

**Il problema.** Il servizio `magazzino.py` ascolta sulla porta 5555 di `127.0.0.1`. Manda tre inventari: per ognuno, un'intestazione con il numero di righe, le righe (nome, quantità, prezzo) e la domanda `Totale? `, a cui va risposto con la somma di quantità × prezzo. Il servizio, come molti server reali, termina le righe con `\r\n`.

```python
#!/usr/bin/env python3
# magazzino.py — un servizio di rete: tre inventari, per ognuno il valore totale
import random, socketserver

class Gestore(socketserver.StreamRequestHandler):
    def handle(self):
        w = lambda s: self.wfile.write(s.encode())
        w('Magazzino. Per ogni inventario dimmi il valore totale (quantità × prezzo).\r\n')
        for giro in range(3):
            righe = [(f'art{random.randrange(10**4):04d}', random.randint(1, 50), random.randint(1, 500))
                     for _ in range(random.randint(5, 15))]
            w(f'--- Inventario {giro + 1} ({len(righe)} righe) ---\r\n')
            for nome, q, p in righe:
                w(f'{nome:<10}{q:>5}{p:>8}\r\n')
            w('Totale? ')
            if self.rfile.readline().strip() != str(sum(q * p for _, q, p in righe)).encode():
                w('Errore.\r\n'); return
        w('Grazie: L8{esempio_cinque}\r\n')

socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('127.0.0.1', 5555), Gestore) as srv:
    srv.serve_forever()
```

Avvialo in un secondo terminale con `python3 magazzino.py` e prova prima a mano con `nc 127.0.0.1 5555` (regola 1 del §12.2).

**Ragionamento.** L'intestazione ci dice **quante** righe seguono: è un'informazione preziosa, perché ci permette di leggere esattamente quelle con `recvlines(n)`, senza indovinare dove finisce la tabella. Estraiamo `n` con una regex sull'intestazione. Le righe finiscono con `\r\n`: `recvlines` toglie il `\n` ma lascia il `\r`, e qui non importa perché `split()` senza argomenti tratta `\r` come spazio. (Se invece confrontassimo la riga con una stringa, o la usassimo come ultima colonna in `int()`, ce ne accorgeremmo: `int(b'215\r')` funziona, perché `int` ignora gli spazi attorno, ma `b'215\r' == b'215'` è falso.)

```python
#!/usr/bin/env python3
# es5.py — client per magazzino.py
from pwn import *
import re

io = remote(args.HOST or '127.0.0.1', int(args.PORT or 5555))
io.recvline()                                              # il benvenuto
for _ in range(3):
    intestazione = io.recvline().decode()                  # "--- Inventario 1 (12 righe) ---"
    n = int(re.search(r'\((\d+) righe\)', intestazione).group(1))
    totale = 0
    for riga in io.recvlines(n):                           # esattamente n righe, senza \n
        nome, q, p = riga.split()
        totale += int(q) * int(p)
    log.info(f'{intestazione.strip()}: totale {totale}')
    io.sendlineafter(b'Totale? ', str(totale).encode())
log.success(io.recvline().strip().decode())
```

```
$ python3 es5.py
[+] Opening connection to 127.0.0.1 on port 5555: Done
[*] --- Inventario 1 (7 righe) ---: totale 63469
[*] --- Inventario 2 (8 righe) ---: totale 42638
[*] --- Inventario 3 (6 righe) ---: totale 64416
[+] Grazie: L8{esempio_cinque}
[*] Closed connection to 127.0.0.1 port 5555
```

**Che cosa imparare.** Rilancia con `DEBUG`: il benvenuto compare in forma di `hexdump`, perché contiene caratteri non ASCII (`à` e `×` in UTF-8, `c3 a0` e `c3 97`, L7 §8.2), mentre le righe della tabella compaiono come testo. Lo script, per com'è scritto, si adatta a inventari di qualunque lunghezza, e **non** usa mai pause né `recv()` "a pezzi". Infine, l'uso di `args.HOST` e `args.PORT` rende lo stesso client utilizzabile contro un altro server senza modificarlo.

### Esempio 6 — Riprovare finché non va

**Il problema.** `fortuna.py` pensa una porta tra 0 e 3 e dà la flag solo a chi la indovina, con un solo tentativo per esecuzione. La probabilità di successo di un tentativo è 1/4: ci serve uno script che **ripete** tutta l'interazione finché non riesce.

```python
#!/usr/bin/env python3
# fortuna.py — una sola possibilità su quattro
import random
segreto = random.randrange(4)
if input('Scegli una porta (0-3): ').strip() == str(segreto):
    print('Fortunato: L8{esempio_sei}')
else:
    print(f'No, era la {segreto}.')
```

**Ragionamento.** È lo schema del §12.1: una funzione `avvia()` che crea un tube nuovo, una funzione `tenta(io)` che fa **un** tentativo e dice se è riuscito, e un ciclo. Due accortezze: chiudere ogni tube con `finally` (altrimenti, in cento giri, si accumulano processi o connessioni aperte), e trattare un `EOFError` come un tentativo fallito, non come un crollo dello script. Silenziamo i messaggi di pwntools durante il ciclo e li riattiviamo per il risultato.

```python
#!/usr/bin/env python3
# es6.py — ripetere un tentativo finché non riesce
from pwn import *
import re

def avvia():
    if args.REMOTE:
        return remote(args.HOST, int(args.PORT))
    return process(['python3', 'fortuna.py'])

def tenta(io):
    """Restituisce la flag, oppure None se il tentativo è fallito."""
    io.sendlineafter(b'(0-3): ', b'2')
    risposta = io.recvline().decode()
    m = re.search(r'L8\{[^}]*\}', risposta)
    return m.group(0) if m else None

context.log_level = 'error'                       # zittisce "Starting local process" a ogni giro
for tentativo in range(1, 101):
    io = avvia()
    try:
        flag = tenta(io)
    except EOFError:
        flag = None                               # il servizio ha chiuso: conta come fallito
    finally:
        io.close()
    if flag:
        break
with context.local(log_level='info'):
    if flag:
        log.success(f'{flag} al tentativo {tentativo}')
    else:
        log.failure('100 tentativi senza successo')
```

```
$ python3 es6.py
[+] L8{esempio_sei} al tentativo 5
$ python3 es6.py
[+] L8{esempio_sei} al tentativo 2
```

**Che cosa imparare.** Il numero di tentativi necessari segue una distribuzione geometrica: con probabilità di successo *p* = 1/4, ne servono in media 1/*p* = 4, e la probabilità di fallire 100 volte di fila è (3/4)¹⁰⁰ ≈ 3·10⁻¹³. Questo calcolo va fatto **sempre** prima di lanciare un ciclo di tentativi contro un server di gara: se la probabilità è 1/16 (un caso tipico nel Modulo 4, quando si indovinano 4 bit di un indirizzo casuale), servono in media 16 connessioni, ed è accettabile; se è 1/2³², la forza bruta non è la soluzione e stai cercando nel posto sbagliato (regola 10 del §12.2). La regex `L8\{[^}]*\}` è il modo standard di riconoscere una flag in un output qualunque: adattala al formato della gara (`flag\{...\}`, `CCIT\{...\}`, ...).

---

## 14. Esercizi

Gli esercizi sono in tre livelli. Quelli **★ Base** controllano che tu abbia capito il linguaggio e i byte: si fanno all'interprete, e la risposta va scritta **prima** di premere Invio, perché indovinare dopo non insegna niente. Quelli **★★ Intermedio** ti fanno scrivere i pezzi di cui è fatto ogni script di interazione: un client di rete, un dialogo con un processo, un messaggio binario, un `recvuntil` scritto da te. Quelli **★★★ Sfida** sono piccole gare: c'è un programma, c'è una flag, e lo script lo scrivi tu da zero. Tutti i programmi da usare sono riportati nel testo: salvali con il nome indicato nel commento iniziale, **senza leggerli più del necessario** quando l'esercizio dice di trattarli come una scatola nera. Le soluzioni, provate con Python 3.13 e pwntools 4.15, sono in `Soluzioni.md`.

### ★ Base

**1. Prevedi l'interprete: byte e testo.** Per ciascuna espressione scrivi il risultato esatto, come lo mostrerebbe il REPL (con `b'...'`, apici e tipo giusti), poi verifica. Accanto a ogni risposta sbagliata annota quale regola del §3 avevi dimenticato.

```python
len('perché')                          # (a)
len('perché'.encode())                 # (b)
b'ABC'[1]                              # (c)
b'ABC'[1:2]                            # (d)
'A' == b'A'                            # (e)
bytes([72, 105])                       # (f)
list(b'hi')                            # (g)
bytes(3)                               # (h)
str(b'hi')                             # (i)
'caffè'.encode('latin-1')              # (l)
b'\xe8'.decode('utf-8', errors='replace')   # (m)
bytes.fromhex('41 42 43')              # (n)
int('0x1f', 16), int('1f', 16), hex(255), '%08x' % 3054    # (o)
```

Poi spiega in due righe perché (i) è una trappola frequente quando si costruisce un messaggio con le f-string (`f'{dati}'` con `dati` di tipo `bytes`), e che cosa si scrive al suo posto.

**2. Prevedi l'interprete: numeri e strutture.** Stesso metodo, per `struct` e `int.to_bytes` (§3.3, L7 §3 e §5).

```python
import struct
struct.pack('<I', 0xdeadbeef)                    # (a)
struct.pack('>I', 0xdeadbeef)                    # (b)
struct.pack('<i', -2)                            # (c)
struct.unpack('<I', b'\xfe\xff\xff\xff')[0]      # (d)
struct.unpack('<i', b'\xfe\xff\xff\xff')[0]      # (e)
struct.calcsize('<HQ'), struct.calcsize('HQ')    # (f)
(0x4142).to_bytes(2, 'little')                   # (g)
int.from_bytes(b'\x01\x00\x00\x00', 'big')       # (h)
struct.unpack('<2I', bytes(range(8)))            # (i)  scrivi i due numeri in esadecimale
```

Per (f) i due valori sono diversi: spiega da dove vengono i byte in più, e perché quando descrivi un protocollo di rete o un formato di file con `struct` devi **sempre** scrivere esplicitamente `<`, `>` o `!`. Per (d) ed (e): gli stessi quattro byte sono due numeri diversi; che cosa li distingue, e dove lo hai già visto (L7 §3.3)?

**3. Un `xxd` in miniatura.** Scrivi `hexd.py`, uno script da riga di comando che stampa il contenuto di un file nel formato

```
00000000  4c 38 7b 63 69 61 6f 7d  0a                       |L8{ciao}.|
```

cioè l'offset in otto cifre esadecimali, sedici byte per riga in esadecimale (con uno spazio in più dopo l'ottavo), e la colonna di destra con i caratteri stampabili ASCII (da 0x20 a 0x7e) e un punto al posto degli altri. Requisiti, tutti dal §4:
- `python3 hexd.py FILE` legge il file; `python3 hexd.py -` o `python3 hexd.py` senza argomenti legge lo **standard input**, in modo che `printf 'ciao' | python3 hexd.py` funzioni;
- l'opzione `-n N` stampa solo i primi `N` byte (usa `argparse`);
- un file inesistente produce un messaggio su **standard error** e il codice di uscita 1, senza *traceback*; il codice di uscita è 0 negli altri casi;
- il file va letto in modalità **binaria**: un file che non è UTF-8 valido (prova con `/bin/ls`) non deve far crollare lo script.

Confronta l'uscita con quella di `xxd` o di `hexdump -C` (L7 §5.3) su tre file: uno di testo, `/bin/ls` con `-n 64`, e un file vuoto.

**4. `subprocess` senza sorprese.** Scrivi, all'interprete o in uno script, le chiamate a `subprocess.run` che:
- (a) eseguono `id -u` e mettono in una variabile di tipo `int` il tuo UID;
- (b) eseguono `ls /non/esiste` senza far crollare lo script, e stampano il codice di uscita e il messaggio d'errore di `ls` (quale flusso?);
- (c) eseguono `ls /non/esiste` in modo che, invece, un fallimento **sollevi** un'eccezione; come si chiama, e quali attributi ha?
- (d) passano a `tr a-z A-Z` la stringa `ciao` sullo standard input e ne leggono il risultato, senza usare la shell;
- (e) eseguono `sleep 5` con un limite di un secondo. Che cosa succede al processo `sleep` quando scade il limite?

Infine, considera questa funzione:

```python
def saluta(nome):
    subprocess.run(f'echo Ciao {nome}', shell=True)
```

Che cosa fa `saluta('Zen; id')`? E `saluta('$(whoami)')`? Riscrivila in modo che qualunque nome, anche quelli, venga stampato tale e quale. Classifica il difetto con il suo CWE (§5.2, L4 §14.2).

**5. Le trappole del modello dei dati.** Prevedi l'output di ciascun frammento (§2.1, §2.5), poi verifica. Per ciascuno, scrivi una riga che spieghi il comportamento in termini di **oggetti e nomi**, non di "variabili che contengono valori".

```python
x = [[]] * 3; x[0].append(1); print(x)                       # (a)

def aggiungi(a, lista=[]):
    lista.append(a); return lista
print(aggiungi(1), aggiungi(2))                                # (b)

a = b'ciao'; b = a; a += b'!'; print(a, b)                     # (c)
l = [1, 2]; m = l; l += [3]; print(l, m)                       # (d)
for c in b'AB': print(c, end=' ')                              # (e)
print(0.1 + 0.2 == 0.3)                                        # (f)
```

Per (c) e (d) l'operatore è lo stesso, `+=`, e il comportamento è opposto: perché? Per (b), scrivi la versione corretta con `lista=None`. Per (e), qual è la differenza con `for c in 'AB'`, e perché è proprio la differenza che serve quando si lavora con dati binari?

### ★★ Intermedio

**6. `recv` non restituisce messaggi.** Questo servizio manda tre messaggi, ognuno preceduto dalla sua lunghezza in **2 byte big-endian**: è il modo più comune, nei protocolli binari, di dire dove finisce un messaggio (L7 §9.1). Per rendere evidente il problema del §6.2, li spedisce a pezzi di sette byte.

```python
#!/usr/bin/env python3
# pacchi.py — messaggi preceduti dalla lunghezza (2 byte, big-endian), spediti a pezzi
import socketserver, time
MESSAGGI = [b'Benvenuto al servizio pacchi.', b'x' * 3000,
            b'Il terzo e ultimo: L8{la_lunghezza_prima_dei_dati}']
class Gestore(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            for m in MESSAGGI:
                pacco = len(m).to_bytes(2, 'big') + m
                for i in range(0, len(pacco), 7):      # sette byte alla volta, con una pausa
                    self.request.sendall(pacco[i:i + 7])
                    time.sleep(0.001)
        except (BrokenPipeError, ConnectionResetError):
            pass                                       # il client se n'è andato prima della fine
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('127.0.0.1', 9006), Gestore) as s:
    s.serve_forever()
```

(a) Avvialo in un terminale. In un altro, prova il client "ingenuo" che chiunque scriverebbe la prima volta, e spiega **riga per riga** l'output che ottieni:

```python
import socket
s = socket.create_connection(('127.0.0.1', 9006))
for _ in range(3):
    h = s.recv(2); n = int.from_bytes(h, 'big'); m = s.recv(n)
    print(len(h), n, len(m), m[:40])
```

(b) Scrivi una funzione `recvn(s, n)` che restituisce **esattamente** `n` byte, chiamando `recv` quante volte serve, e solleva `EOFError` se la connessione si chiude prima. Usala per scrivere il client corretto, che stampa la lunghezza e l'inizio di ogni messaggio e si ferma da solo alla chiusura. (c) Perché il client ingenuo, provato **senza** le pause e i pezzi da sette byte, sembrerebbe funzionare quasi sempre su `127.0.0.1`, e perché questo è un motivo in più per non fidarsene contro un server vero? (d) Quale funzione di pwntools fa lo stesso lavoro di `recvn`?

**7. Sei byte bastano (quasi sempre).** Questo programma fa trapelare (*leak*) l'indirizzo della propria funzione `main` come byte grezzi, nello stesso modo in cui lo fanno molte sfide del Modulo 4, e chiede di rimandarlo in esadecimale.

```c
// perde.c — fa trapelare un indirizzo come byte grezzi
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(void) {
    setvbuf(stdout, NULL, _IONBF, 0);
    uintptr_t a = (uintptr_t)&main;
    printf("Ecco: ");
    fputs((char *)&a, stdout);                  // i byte di a, fino al primo 00
    printf("\nE in esadecimale? ");
    char riga[64];
    if (!fgets(riga, sizeof riga, stdin)) return 1;
    puts(strtoull(riga, NULL, 16) == a ? "Giusto: L8{sei_byte_bastano}" : "No.");
    return 0;
}
```

(a) Compilalo con `gcc -o perde perde.c` e guarda che cosa stampa con `./perde < /dev/null | od -An -tx1 -c`. Quanti byte ci sono tra `Ecco: ` e il `\n`, e perché proprio quel numero (pensa a come è fatto un indirizzo a 64 bit in uno spazio utente Linux, e a che cosa fa `fputs` con il byte 00)? (b) Scrivi uno script pwntools che legge i byte trapelati, li trasforma nell'intero con `u64` (§10.1) e rimanda `hex(a)`. (c) Lancia lo script **duecento** volte in un ciclo e conta i fallimenti. Dovresti vederne qualcuno: trova la causa guardando i byte ricevuti in un caso fallito, calcola la probabilità attesa, e correggi lo script in modo che se ne accorga e riprovi (Esempio 6). (d) Perché, per separare i byte trapelati dal resto, è meglio `recvuntil(b'\nE in esadecimale? ', drop=True)` che `recvline()`? Quale byte dell'indirizzo renderebbe sbagliato `recvline()`?

**8. `flat` e `context`.** Prevedi il risultato, poi verifica. Fai attenzione alla prima riga.

```python
from pwn import *
flat(b'A' * 4, 0xdeadbeef)                       # (a) senza aver impostato context.arch
context.arch = 'amd64'
flat(b'A' * 4, 0xdeadbeef)                       # (b)
flat(b'ciao', p32(1), 2)                         # (c)
flat({16: 0x401136}, filler=b'B')                # (d) quanti byte in tutto?
flat({8: b'X'}, length=12)                       # (e) senza filler: con che cosa riempie?
cyclic(12), cyclic_find(b'faaa')                 # (f)
```

Perché (a) e (b) danno lunghezze diverse? Che cosa ti insegna (e) sul riempimento predefinito di `flat`, e perché è una scelta comoda quando, nel Modulo 4, un programma crollerà e ti dirà quale pezzo del tuo input è finito in un registro (§10.4)?

**9. XOR con un testo noto.** Una flag del formato `L8{...}`, lunga 32 byte, è stata cifrata con lo XOR a chiave ripetuta, con una chiave di **4 byte**. Ecco il cifrato in esadecimale:

```
5f0fbbbd7b5ea1a87668a3b16143a181705ea6ac7245a9b14c53a5bc7c5ba5a3
```

(a) Usando che il chiaro comincia con `L8{`, ricava i primi tre byte della chiave con una sola chiamata a `xor` (§10.3, L7 §4.3). (b) Ti manca un byte. Sai però **un'altra** cosa del chiaro: quale, e in quale posizione? Mostra con un conto modulo 4 che ti dà proprio il byte mancante. (c) Decifra la flag. (d) Generalizza: con una chiave di lunghezza *k* e un chiaro di lunghezza *n* di cui conosci i primi 3 byte e l'ultimo, per quali *k* la chiave è interamente determinata? Che cosa faresti se non lo fosse (pensa all'Esercizio 15 della Lezione 7)?

**10. Il buffering, dal lato di Python.** Questo programma Python fa due domande in due modi diversi:

```python
#!/usr/bin/env python3
# chiedi.py — due modi di fare una domanda
import sys
print('Nome? ', end='')
nome = sys.stdin.readline().strip()
eta = input('Età? ')
print(f'Ciao {nome}, {eta} anni')
```

Lo script seguente prova cinque configurazioni. Per ciascuna, **prevedi** se la marca `Nome? ` arriva entro due secondi, se arriva `Età? `, e se il saluto finale arriva comunque, poi esegui.

```python
#!/usr/bin/env python3
# es10.py — cinque modi di avviare chiedi.py
from pwn import *
prove = [('predefinito', ['python3', 'chiedi.py'], {}),
         ('stdout=PIPE', ['python3', 'chiedi.py'], dict(stdout=PIPE)),
         ('stdin=PTY',   ['python3', 'chiedi.py'], dict(stdin=PTY)),
         ('PIPE + -u',   ['python3', '-u', 'chiedi.py'], dict(stdout=PIPE)),
         ('PIPE+stdbuf', ['stdbuf', '-o0', 'python3', 'chiedi.py'], dict(stdout=PIPE))]
for nome, argv, opzioni in prove:
    with context.local(log_level='error'):
        io = process(argv, env={'PATH': os.environ['PATH']}, **opzioni)
        d1 = io.recvuntil(b'Nome? ', timeout=2)
        io.sendline(b'Zen')
        d2 = io.recvuntil('Età? '.encode(), timeout=2)
        io.sendline(b'30')
        fine = io.recvall(timeout=2)
    print(f'{nome:12} Nome:{bool(d1)} Età:{bool(d2)} fine:{fine!r}')
    io.close()
```

(a) Confronta la tabella con quella dell'Esempio 4 (lo stesso problema con un programma C). Due righe hanno un risultato **diverso** dal caso C: quali, e perché? (Suggerimento: chi gestisce il buffer dello standard output di un programma Python, e che cosa fa la libreria C prima di leggere da un terminale?) (b) Perché `Età? ` arriva in tutte le configurazioni? Leggi la documentazione di `input` per la risposta. (c) Perché lo script passa `env={'PATH': ...}` invece di lasciare l'ambiente com'è? Quale variabile d'ambiente, se fosse impostata nel tuo sistema, renderebbe tutte e cinque le righe uguali (§5.3; la trovi in `python3 --help-env`)? (d) Perché il saluto finale arriva anche quando `Nome? ` non è arrivato, e perché in uno script di gara non devi contare su questo (regola 2 del §12.2)?

**11. Pubblicare un programma in rete, e lo scheletro locale/remoto.** Nelle gare, i programmi interattivi vengono messi in rete con strumenti come `socat` o `xinetd`: per ogni connessione, il server avvia una copia del programma con il **socket** come standard input, output ed errore. Lo puoi fare anche tu, in Python, in dieci righe:

```python
#!/usr/bin/env python3
# pubblica.py PORTA PROGRAMMA [ARG...] — mette un programma interattivo in rete, come socat o xinetd
import socketserver, subprocess, sys
porta, comando = int(sys.argv[1]), sys.argv[2:]
class Gestore(socketserver.BaseRequestHandler):
    def handle(self):
        fd = self.request.fileno()                # il socket diventa stdin, stdout e stderr del figlio
        with subprocess.Popen(comando, stdin=fd, stdout=fd, stderr=fd) as figlio:
            figlio.wait()
socketserver.ThreadingTCPServer.allow_reuse_address = True
socketserver.ThreadingTCPServer.daemon_threads = True
with socketserver.ThreadingTCPServer(('127.0.0.1', porta), Gestore) as s:
    print(f'{" ".join(comando)} pubblicato su 127.0.0.1:{porta}', flush=True)
    s.serve_forever()
```

(a) Spiega, con le parole della Lezione 5 (§4, descrittori ereditati, `fork`, `dup2`, `execve`), che cosa fa `Popen` con `stdin=fd, stdout=fd, stderr=fd`, e perché il programma pubblicato non ha bisogno di sapere niente di reti. (b) Pubblica l'oracolo dell'Esercizio 16 con `python3 pubblica.py 9011 python3 oracolo.py` e collegati con `nc 127.0.0.1 9011`: il programma ti risponde come in locale? (c) Prendi lo scheletro del §12.1 e scrivi uno script che, **senza cambiare una riga del dialogo**, risolve l'oracolo sia in locale (`python3 es11.py`) sia in rete (`python3 es11.py REMOTE`, poi `REMOTE PORT=9011 DEBUG`). (d) Che cosa vedrebbe un giocatore se il programma pubblicato fosse il `domanda.c` dell'Esempio 4, senza `setvbuf`, e perché l'opzione `pty` di `socat` lo aggiusterebbe? (e) `pubblica.py` ascolta solo su `127.0.0.1`: che cosa cambierebbe con `''` o `'0.0.0.0'`, e perché pubblicare così un programma qualunque su una macchina collegata a una rete è una pessima idea?

**12. Un `recvuntil` scritto da te.** Il §6.2 si è chiuso con un `recvuntil` difettoso, e il §12.4 ti ha promesso di scriverne uno corretto. Scrivi, con la sola libreria standard, un modulo `tubo.py` con una classe `Tubo` che offre la stessa interfaccia minima di un tube di pwntools:
- due costruttori: `Tubo.rete(host, porta)` (un socket TCP) e `Tubo.processo(argv)` (un `subprocess.Popen` con le pipe);
- `recvuntil(marca, drop=False)`, `recvline()`, `recvn(n)`, `send(dati)`, `sendline(dati)`, `sendafter(marca, dati)`, `sendlineafter(marca, dati)`, `close()`.

Requisiti: un **buffer di ricezione** conserva i byte arrivati dopo la marca, che devono essere restituiti dalla lettura successiva (§9.1); la marca può arrivare **spezzata** tra due `recv` (la parte iniziale in uno, il resto nel successivo) e va trovata lo stesso; la chiusura del flusso diventa un `EOFError` il cui messaggio mostra che cosa restava nel buffer. Domande: (a) Perché per leggere dal processo non va bene `p.stdout.read(4096)` di un oggetto file bufferizzato, e serve `os.read` sul descrittore (o `bufsize=0`)? (b) Perché il tuo `recvuntil`, quando non trova la marca, non deve ricominciare a cercarla ogni volta dall'inizio del buffer, e da dove deve ripartire? È un problema di correttezza o di efficienza? (c) Scrivi un piccolo test che, con una funzione di lettura finta che restituisce **un byte alla volta**, verifica tutti e tre i requisiti senza bisogno di processi né di rete.

### ★★★ Sfida

**13. Calcolare senza `eval`.** Il servizio seguente manda venti espressioni aritmetiche con parentesi, annidate fino a tre livelli, con gli operatori `+ - * // %`, e vuole il risultato di ciascuna. In una posizione a caso, però, al posto dell'espressione c'è una **trappola**: un pezzo di codice Python che, se eseguito, lancia un comando sulla tua macchina. A quella domanda la risposta giusta è la parola `RIFIUTO`.

```python
#!/usr/bin/env python3
# espressioni.py — venti espressioni con parentesi; una di esse è una trappola
import random, sys
rnd = random.SystemRandom()
def espr(p):
    if p == 0 or rnd.random() < 0.3:
        return str(rnd.randint(1, 999))
    op = rnd.choice(['+', '-', '*', '//', '%'])
    return f'({espr(p - 1)} {op} {espr(p - 1)})'
trappola = rnd.randrange(20)
for i in range(20):
    if i == trappola:
        e = "__import__('os').system('echo HO ESEGUITO UN COMANDO SULLA TUA MACCHINA >&2')"
    else:
        while True:                               # niente divisioni per zero
            e = espr(3)
            try: giusto = eval(e); break          # il server può usare eval: le espressioni le genera lui
            except ZeroDivisionError: pass
    print(f'Espressione {i + 1}: {e}\nRisultato (o RIFIUTO)? ', end='', flush=True)
    r = sys.stdin.readline().strip()
    if i == trappola:
        if r != 'RIFIUTO':
            print('Hai eseguito quello che ti ho mandato? Arrivederci.'); sys.exit(1)
    elif r != str(giusto):
        print(f'Sbagliato: era {giusto}.'); sys.exit(1)
print('Venti su venti: L8{ast_non_esegue_niente}')
```

Scrivi un risolutore che **non usa mai** `eval`, `exec` né `ast.literal_eval` (che non accetta gli operatori). Usa invece il modulo `ast` della libreria standard: `ast.parse(testo, mode='eval')` trasforma il testo in un **albero sintattico** senza eseguirlo, e tu lo visiti con una funzione ricorsiva che accetta **solo** i nodi che conosci (`Expression`, `Constant` con valore intero, `BinOp` con i cinque operatori, eventualmente `UnaryOp` con il meno) e rifiuta tutto il resto con un'eccezione. Domande: (a) Che nodo produce la trappola, e in quale punto della tua funzione viene rifiutata? (b) Perché il server può permettersi `eval` e tu no (regola 6 del §12.2)? (c) Gli operatori `//` e `%` di Python e del C danno lo stesso risultato con i numeri negativi? Fai un esempio, e spiega perché qui conviene calcolare in Python, e perché in una sfida scritta in C dovresti invece imitare il C (L7, Esercizio 13). (d) Supponi che una versione futura del servizio aggiunga l'elevamento a potenza, `**`. Un'espressione come `9**9**9**9` non esegue codice, ma blocca lo stesso il tuo script, che resta a calcolare un numero con miliardi di cifre: quale nodo la produce, e quali due difese aggiungeresti (una sui valori che il nodo riceve, una sulla lunghezza del testo)?

**14. Mini-CTF.** Nella cartella di questa lezione c'è `setup_sfida.sh`. Eseguilo con `bash setup_sfida.sh`: crea `~/l8_sfida/` con un servizio, `servizio.py`, e un file `LEGGIMI.txt`. Il servizio è uno **sportello** con quattro prove, e ogni prova superata dà un pezzo della flag `L8{...}`. Le prove sono pensate per essere impossibili a mano: troppo veloci, o con byte che dalla tastiera non si digitano. Regole del gioco:
- **non leggere il codice di `servizio.py`**: trattalo come il servizio remoto di una gara, di cui conosci solo quello che dice. Il primo passo è collegarsi a mano (regola 1 del §12.2) e copiare le marche esatte;
- il servizio si usa in due modi: `python3 servizio.py` dialoga sullo standard input e output, `python3 servizio.py --porta 4444` resta in ascolto su `127.0.0.1:4444`. Il tuo script deve funzionare **in entrambi**, con lo scheletro del §12.1 (`python3 risolvi.py` e `python3 risolvi.py REMOTE`), e anche con `DEBUG` attivo;
- costruisci lo script una prova alla volta (regola 8): la prova *n* si scrive solo quando la *n* − 1 passa.

Quando hai la flag, rispondi per iscritto: per ciascuna prova, qual era la difficoltà e quale sezione della lezione la risolve? Se lo script funziona in locale ma non in rete (o viceversa), perché?

**15. La stessa mini-CTF, senza pwntools.** Risolvi di nuovo l'Esercizio 14 usando **solo** la libreria standard e il tuo `tubo.py` dell'Esercizio 12, sia sullo standard input del servizio (con `Tubo.processo`) sia in rete (con `Tubo.rete`). È la situazione del §12.4: una macchina senza pwntools. Quando funziona, confronta i due script riga per riga: quali righe sono identiche, quali cambiano, e che cosa ti dava pwntools che hai dovuto scrivere a mano? Prova a lanciare la versione locale con `env -u PYTHONUNBUFFERED`: funziona ancora? Da che cosa dipende, nel codice di un servizio che non devi leggere, che la tua versione con le pipe non si blocchi (§5.3)?

**16. Un oracolo, una cifra alla volta.** Questo servizio custodisce un codice di 8 cifre esadecimali e ti concede 150 tentativi. A ogni tentativo sbagliato ti dice quante cifre sono giuste **a partire dall'inizio**.

```python
#!/usr/bin/env python3
# oracolo.py — un codice di 8 cifre esadecimali; l'oracolo dice quante sono giuste dall'inizio
import os, sys
codice = os.urandom(4).hex()
print('Indovina il codice: 8 cifre esadecimali minuscole. Hai 150 tentativi.', flush=True)
for t in range(1, 151):
    print(f'Tentativo {t}> ', end='', flush=True)
    prova = sys.stdin.readline().strip()
    if prova == codice:
        print(f'Esatto in {t} tentativi: L8{{un_oracolo_alla_volta}}'); sys.exit(0)
    giuste = 0
    for a, b in zip(prova, codice):
        if a != b: break
        giuste += 1
    print(f'Cifre giuste dall\'inizio: {giuste}', flush=True)
print('Tentativi finiti.')
```

(a) Quanti codici possibili ci sono, e quanti tentativi servirebbero in media provando a caso? Che cosa dice la regola 10 del §12.2? (b) Scrivi lo script che ricostruisce il codice **una cifra alla volta**. Quale carattere conviene usare per "riempire" le posizioni che non conosci ancora, e perché non va bene `0`? (c) Calcola il numero **massimo** e il numero **medio** di tentativi del tuo metodo, poi misuralo su duecento partite. I 150 tentativi bastano sempre? (d) Questo schema, "un segreto lungo *n* verificato un pezzo alla volta, con un'informazione su quanti pezzi sono giusti", trasforma un costo esponenziale (16⁸) in uno lineare (8 · 16). Lo ritroverai in forme meno esplicite: un confronto di password che si ferma al primo carattere diverso e quindi impiega **più tempo** quanti più caratteri sono giusti (gli attacchi a tempo, *timing attack*), le iniezioni SQL "alla cieca" del Modulo 6, gli oracoli di *padding* del Modulo 5. Spiega, con le tue parole, qual è il difetto di progetto comune a tutti, e come si scrive un confronto che non lo ha (cerca `hmac.compare_digest`).

**17. La rivincita su `indovina.sh`.** Nella Lezione 4 (Esempio 6) hai fatto giocare un coprocesso bash contro `indovina.sh`, che pensa un numero tra 1 e 1 000 000 e risponde `più alto` o `più basso`. Riscrivi il giocatore in Python con pwntools, usando la **ricerca binaria**. Requisiti e domande: (a) scrivi l'**invariante** del ciclo (che cosa è sempre vero di `basso` e `alto`) e mostra che il ciclo termina; (b) qual è il numero massimo di tentativi della ricerca binaria su un milione di valori, e perché i 25 concessi bastano sempre? Misura massimo e media su trecento partite; (c) il programma non ha un prompt: come fai a sapere quando leggere, e perché qui `recvline` è la scelta giusta? (d) Che cosa fa il tuo script se riceve una risposta che non conosce, per esempio `non è un numero`? Deve fermarsi con un errore chiaro, non continuare a caso (regola 5); (e) confronta il tuo script con la versione bash della Lezione 4: lunghezza, leggibilità, e che cosa succederebbe a ciascuno dei due se il programma scrivesse le risposte senza `\n` finale.

### Allenamento

Le sfide di questa lezione sono quelle che le gare chiamano **misc** o **ppc** (*professional programming challenge*): un servizio che fa domande troppo in fretta per un essere umano. Su pwn.college, il dojo *Playing With Programs* (tra i *Fundamentals*) raccoglie le sfide di interazione con i programmi, e i livelli del vecchio modulo *Program Interaction* (oggi nell'archivio del sito, i livelli *embryoio*) ti chiedono di avviare un programma da bash, da Python e da C con argomenti, ambiente, descrittori e segnali precisi: sono l'allenamento ideale per §4–5 e per la Lezione 5, e ogni livello va risolto **anche** con `subprocess` e con pwntools. Tutti i moduli successivi di pwn.college, a partire da quelli di *reverse engineering* e *memory errors*, presuppongono che tu sappia scrivere in pochi minuti uno script `from pwn import *` che avvia `/challenge/...` e dialoga con esso. Fuori da pwn.college, picoCTF (categoria *General Skills*) e le gare di allenamento di OliCyber e CyberChallenge.IT hanno sempre qualche sfida "di calcolo veloce" o "di conversione a tempo": fanne almeno tre, scrivendo ogni volta lo script con lo scheletro del §12.1 e senza mai usare `eval`.

---

## 15. Domande di autoverifica

1. Che cosa significa che in Python "le variabili sono nomi che si riferiscono a oggetti"? Perché `b = a` seguito da una modifica di `a` a volte cambia anche `b` e a volte no?
2. Qual è la differenza tra `bytes` e `str`? Che cosa fanno `encode` e `decode`, e in quale punto di uno script di interazione vanno chiamati? Che cosa succede se confronti `'A'` con `b'A'`?
3. Che cosa restituisce `b'ABC'[0]`, e che cosa `b'ABC'[0:1]`? Perché la differenza conta quando si scorrono dati binari?
4. Come si trasforma l'intero 0x401136 in 8 byte little-endian, in almeno tre modi (libreria standard e pwntools)? E come si torna indietro da 6 byte trapelati?
5. Perché in `struct` bisogna scrivere sempre `<`, `>` o `!` all'inizio del formato?
6. Perché un file binario va aperto con `'rb'`? Che cosa succede leggendo `/bin/ls` in modalità testo?
7. Perché `subprocess.run(['ls', nome])` è sicuro e `subprocess.run(f'ls {nome}', shell=True)` no? Quale CWE descrive il difetto?
8. Perché un dialogo con un processo attraverso le pipe si può bloccare? Descrivi i due motivi diversi: il buffering e lo stallo (*deadlock*).
9. Perché `recv(1024)` può restituire meno di quanto il server ha mandato, o due messaggi insieme? Come si leggono esattamente *n* byte, e come si legge "fino a una marca"?
10. Che cos'è un *tube* di pwntools? Che cosa hanno in comune `process` e `remote`, e perché è questa la loro qualità più importante?
11. Che cosa fanno `recvuntil`, `recvline`, `recvn`, `sendline`, `sendlineafter`, `interactive`? Che cosa fa `drop=True`?
12. Perché pwntools avvia i processi con lo standard output su un PTY, e quando serve anche `stdin=PTY`? Perché per un programma Python non basta?
13. Che cosa fanno `p32`, `u64`, `flat`, `xor`, `cyclic`? Perché `p32(-1)` dà errore?
14. Che cos'è `context`, e che cosa cambia nei risultati di `flat` e `p...` quando imposti `context.arch = 'amd64'`?
15. Come si scrive uno script che funziona sia in locale sia contro il server della gara? A che cosa servono `REMOTE`, `DEBUG`, `HOST=`?
16. Perché non si deve mai usare `eval` su dati ricevuti dalla rete? Come si calcola un'espressione aritmetica senza eseguire codice?
17. Perché "aspetto mezzo secondo e poi leggo" è sbagliato, e con che cosa si sostituisce?
18. Lo script si blocca. Elenca, in ordine, i passi del metodo del §12.3.
19. Quando ha senso ripetere un tentativo in un ciclo contro un server? Come stimi in anticipo quante connessioni serviranno?

## 16. Riepilogo

- **Python** è lo strumento standard per scrivere in pochi minuti programmi che parlano con altri programmi. Si usa in un **ambiente virtuale** (`python3 -m venv`, `pip install pwntools`), con il REPL accanto per provare ogni riga.
- Il **modello dei dati**: i nomi si riferiscono a oggetti; gli oggetti mutabili (`list`, `dict`, `bytearray`) si modificano sul posto e la modifica si vede da tutti i nomi, quelli immutabili (`int`, `str`, `bytes`, `tuple`) no. Trappole: `[[]] * 3`, argomenti predefiniti mutabili, `is` al posto di `==`.
- **`bytes` e `str`** sono due tipi distinti: i `bytes` sono sequenze di interi 0–255 (indicizzandoli si ottiene un `int`), le `str` sequenze di caratteri Unicode. Si passa dall'uno all'altro solo con `encode`/`decode`, al **confine** del programma. Tutto ciò che entra ed esce da file, pipe e socket è `bytes`.
- Interi e byte: `int.to_bytes`/`int.from_bytes`, e `struct.pack`/`unpack` con un formato che dichiara **sempre** l'ordine (`<` little, `>` big, `!` rete); `bytes.fromhex`, `.hex()`, `base64`.
- **File e riga di comando**: `open(..., 'rb')` per i dati binari, `with` per chiuderli, `sys.argv` e `argparse`, `sys.stdin.buffer` e `sys.stdout.buffer` per i byte, messaggi d'errore su `stderr`, `sys.exit(codice)`.
- **`subprocess`**: `run` con una **lista** di argomenti (mai `shell=True` con dati esterni: CWE-78), `capture_output`, `check`, `input`, `timeout`; `Popen` per il dialogo, con i suoi due pericoli: il **buffering** del programma figlio e lo **stallo** delle pipe piene.
- **Socket**: `socket.create_connection`, `sendall`, `recv`. TCP è un **flusso di byte**, non di messaggi: `recv` restituisce quello che è arrivato, e i confini li ricostruisci tu, leggendo *n* byte o fino a una marca, con un **buffer** che conserva l'eccedenza.
- **pwntools** risolve tutti questi problemi con un'unica astrazione, il **tube**: `process` (locale, con PTY), `remote` (TCP), `listen`, tutti con la stessa interfaccia: `recvuntil`, `recvline`, `recvn`, `recvall`, `clean`, `send`, `sendline`, `sendafter`, `sendlineafter`, `interactive`, `close`; la fine del flusso è un `EOFError`, la lettura che scade restituisce `b''`.
- **I dati in pwntools**: `p32`/`p64`/`u32`/`u64` (con `ljust(8, b'\x00')` per gli indirizzi trapelati a 6 byte), `flat` per costruire messaggi binari (dipende da `context.arch`), `xor` a chiave ripetuta, `enhex`/`unhex`, `b64e`/`b64d`, `hexdump`, `cyclic` e `cyclic_find`.
- **`context`, `log`, `args`**: `context.arch`, `context.timeout`, `context.log_level`; `DEBUG` mostra ogni byte scambiato; gli argomenti in maiuscolo (`REMOTE`, `HOST=`, `PORT=`) scelgono il bersaglio senza cambiare il codice.
- **Lo script di gara**: lo scheletro del §12.1 (costanti in cima, `avvia()` locale/remoto, `risolvi(io)`, timeout globale) e le dieci regole del §12.2: guarda prima a mano, un `recvuntil` prima di ogni `send`, mai `sleep` al posto di una marca, sempre `bytes`, analisi rigida, **mai `eval`**, debug per primo, un passo alla volta, stampa i valori intermedi, rispetta il servizio. Quando non va, il metodo del §12.3.
- Senza pwntools resta la **libreria standard**, che basta: un socket o un `Popen`, un buffer, un `recvuntil` scritto bene (Esercizio 12).

## 17. Fonti

- **Python Software Foundation**, *The Python Tutorial* e *The Python Standard Library* (docs.python.org/3): in particolare le pagine su `bytes` e `bytearray` (*Binary Sequence Types*), `struct`, `subprocess`, `socket` e la *Socket Programming HOWTO*, `socketserver`, `argparse`, `ast`, `hmac.compare_digest`, la funzione `input`; *The Python Language Reference*, cap. 3 (*Data model*) per oggetti, identità e mutabilità.
- **Justin Seitz, Tim Arnold**, *Black Hat Python*, 2ª ed., cap. 1 (l'ambiente di lavoro) e cap. 2 (client e server TCP con `socket`, un `netcat` in Python): il riferimento per Python come strumento di sicurezza.
- **Al Sweigart**, *Automate the Boring Stuff with Python*, cap. 1–9: le basi del linguaggio, per chi parte da zero.
- **Gallopsled**, documentazione di pwntools (docs.pwntools.com), in particolare *Getting Started*, `pwnlib.tubes` (*tubes*, `process`, `remote`, `listen`), `pwnlib.util.packing` (`p32`, `flat`), `pwnlib.util.fiddling` (`xor`, `enhex`, `hexdump`), `pwnlib.util.cyclic`, `pwnlib.context`, `pwnlib.args`; e il repository `Gallopsled/pwntools-tutorial`.
- **pwn.college**, CSE 365, la lezione *Gleaning Challenge Insight* per il metodo di lavoro su una sfida; il dojo *Playing With Programs* e i livelli *embryoio* del modulo *Program Interaction* (archivio).
- **Pagine di manuale**: `python3(1)`, `pty(7)`, `stdbuf(1)`, `setvbuf(3)`, `socket(7)`, `tcp(7)`, `socat(1)`, `nc(1)`.
- **MITRE CWE**: CWE-78 (iniezione di comandi del sistema operativo, `shell=True`), CWE-95 (*eval injection*, regola 6), CWE-208 (*observable timing discrepancy*, Esercizio 16).

## 18. Prossima lezione

**Lezione 9 — C essenziale e toolchain**: dal sorgente all'eseguibile (preprocessore, compilatore, assemblatore, linker, `gcc` passo per passo), tipi e dimensioni, puntatori e array, le stringhe del C e il loro terminatore, `malloc` e `free`, le chiamate di sistema `open`, `read`, `write` viste dal lato del C, e un primo uso di `gdb`. Oggi hai parlato con i programmi dall'esterno; nella prossima lezione li apri e guardi come sono fatti dentro. Molte cose che oggi hai trattato come fatti (`setvbuf` e il buffering, l'indirizzo di `main` che trapela a 6 byte, il `fgets` che legge una riga) avranno la loro spiegazione dal lato di chi scrive il programma.
