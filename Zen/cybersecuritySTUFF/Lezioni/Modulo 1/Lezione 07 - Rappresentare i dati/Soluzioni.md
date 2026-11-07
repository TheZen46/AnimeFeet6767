# Modulo 1 — Lezione 7: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. I comandi sono stati provati con bash 5.2 e Python 3 su Linux x86-64. Dove compare `xxd`, se non lo hai installato usa `od -A x -t x1z` (dump) o Python (`bytes.fromhex`) come nel §10.2. I riferimenti `§` rimandano alle sezioni di `Lezione.md`.

## ★ Base

**1.**
(a) 0b1101 0110 = 128 + 64 + 16 + 4 + 2 = **214**; per gruppi: 1101 = D, 0110 = 6 → **0xD6**.
(b) 0xC4 = 12·16 + 4 = **196**; C = 1100, 4 = 0100 → **0b1100 0100**.
(c) 201 = 128 + 64 + 8 + 1 → **0b1100 1001** → 0xC9; in ottale, gruppi di 3 da destra: 11 001 001 → **0o311**.
(d) 0o755 → 111 101 101 → `rwxr-xr-x`: il proprietario legge, scrive ed esegue; gruppo e altri leggono ed eseguono (lo vedrai in dettaglio nella Lezione 6).
(e) 61 < 0x3F = 0b111111 = 0o77 = **63**: gli ultimi tre sono lo stesso numero scritto in tre basi.
```
$ echo $((16#D6)) $((2#11010110)); printf '%d %x %o\n' 201 201 201; echo $((0x3F)) $((2#111111)) $((8#77))
214 214
201 c9 311
63 63 63
```

**2.**
(a) `C` è la terza lettera: 0x41 + 2 = **0x43**; `c` = 0x43 + 0x20 = **0x63**; `7` = 0x30 + 7 = **0x37**; `{` = **0x7B** (subito dopo `z` = 0x7A); spazio = **0x20**.
(b) 0x6A = 0x61 + 9 → la decima lettera minuscola: **`j`**. 0x2D è nella punteggiatura: **`-`**.
(c) `L7` = **4C 37**.
(d)
```
$ for c in C c 7 '{' ' '; do printf '%s=0x%x\n' "$c" "'$c"; done
C=0x43
c=0x63
7=0x37
{=0x7b
 =0x20
```
Il trucco `"'C"` in `printf` (una virgoletta semplice davanti al carattere) chiede il codice numerico del carattere: è definito da POSIX.

**3.**
```
$ printf 'Flag: L7{...}\nriga2\r\n\t fine' > prova.txt
$ od -c prova.txt
0000000   F   l   a   g   :       L   7   {   .   .   .   }  \n   r   i
0000020   g   a   2  \r  \n  \t       f   i   n   e
0000033
$ cat -A prova.txt
Flag: L7{...}$
riga2^M$
^I fine
$ wc -c -l prova.txt
 2 27 prova.txt
```
Caratteri di controllo: `\n` = 0x0A (due volte), `\r` = 0x0D, `\t` = 0x09. Il file è di **27 byte** (l'ultimo offset di `od` è 033 in ottale = 27). `wc -l` conta i caratteri `\n`, non le "righe": l'ultima riga, ` fine`, non termina con `\n` e non viene contata, quindi `wc -l` dice 2 anche se le righe visibili sono 3. `cat -A` mostra `^M` per il CR e `^I` per la tabulazione (Ctrl-M = 0x0D, Ctrl-I = 0x09, §7.2).

**4.**
(a)
```
$ printf 'Modulo 1' | base64
TW9kdWxvIDE=
$ printf 'Modulo 1' | od -A n -t x1 | tr -d ' \n'; echo
4d6f64756c6f2031
```
(b) `aGFja2luZw==` → `hacking`; `0x70776e` → i byte 70 77 6e → **`pwn`**.
```
$ echo aGFja2luZw== | base64 -d; echo; python3 -c 'print(bytes.fromhex("70776e"))'
hacking
b'pwn'
```
(c) `U0VHUkVUTw==` → `SEGRETO`. "Nascondere" è la parola sbagliata perché il base64 è una **codifica** pubblica e senza chiave: chiunque la riconosce (alfabeto, lunghezza multipla di 4, `==` finale) e la inverte in un istante. Non dà alcuna riservatezza (§10.6).
(d)
```
$ python3 -c 'import urllib.parse as u; print(u.quote("a=1 & b=2/3"), u.quote("a=1 & b=2/3", safe=""))'
a%3D1%20%26%20b%3D2/3 a%3D1%20%26%20b%3D2%2F3
```
Per default `quote` lascia intatta la `/` (perché negli URL separa i percorsi); con `safe=""` codifica anche quella.

**5.** Letto in **little-endian** il primo byte è il meno significativo: `44 33 22 11` → **0x11223344**. In **big-endian**: **0x44332211**.
```
$ printf '\x44\x33\x22\x11' > e.bin
$ od -A n -t x4 e.bin; od -A n -t x4 --endian=big e.bin
 11223344
 44332211
$ printf '\x04\x03\x02\x01' > le.bin; od -A n -t x4 le.bin      # 0x01020304 in little-endian
 01020304
```

## ★★ Intermedio

**6.**
(a) −1 = **1111 1111** (0xFF); −128 = **1000 0000** (0x80); −64: 64 = 0100 0000 → 1011 1111 + 1 = **1100 0000** (0xC0); −50: 50 = 0011 0010 → 1100 1101 + 1 = **1100 1110** (0xCE).
(b) 0xB0 = 1011 0000 → −128 + 32 + 16 = **−80**. 0x7F = 0111 1111 = **127**, il massimo positivo.
(c) +128 richiederebbe 0b1000 0000, che in 8 bit con segno è già −128: l'intervallo è asimmetrico (§3.2). Infatti, applicando la regola, −(−128): 1000 0000 → 0111 1111 + 1 = 1000 0000, cioè di nuovo −128.
(d) −1 = **0xFFFFFFFF**, −256 = **0xFFFFFF00**.
```
$ printf '%x %x\n' $(( -1 & 0xFFFFFFFF )) $(( -256 & 0xFFFFFFFF ))
ffffffff ffffff00
```

**7.**
(a) `0xA5 & 0x0F` = 1010 0101 & 0000 1111 = **0x05**; `0xA5 | 0x50` = 1010 0101 | 0101 0000 = **0xF5**; `0xA5 ^ 0xFF` = **0x5A** (lo XOR con tutti 1 inverte); `~0xA5` in 8 bit = **0x5A** (stesso risultato, per la stessa ragione).
(b)
```
$ c=$(printf '%d' "'A")
$ printf "\\$(printf '%03o' $(( c | 0x20 )))\n"     # minuscola
a
$ c=$(printf '%d' "'q"); printf "\\$(printf '%03o' $(( c ^ 0x20 )))\n"   # scambia
Q
```
`printf '\NNN'` vuole il codice in **ottale**: per questo si passa prima per `%03o`.
(c) `(0x11223344 >> 16) & 0xFF` = **0x22**: i byte, contando da 0 a destra, sono 0x44 (0), 0x33 (1), 0x22 (2), 0x11 (3).

**8.**
(a) `'A'` = 0100 0001, 0x20 = 0010 0000 → 0110 0001 = 0x61 = `'a'`.
(b)
```python
>>> c = bytes(x ^ 0x42 for x in b'ciao'); c.hex()
'212b232d'
>>> bytes(x ^ 0x42 for x in c)
b'ciao'
```
(c) Chiave = chiaro ⊕ cifrato: 0x16 ⊕ `'L'` (0x4C) = **0x5A**; 0x6D ⊕ `'7'` (0x37) = **0x5A**. Le due posizioni danno la stessa chiave, quindi è plausibile una chiave di un byte ripetuto, 0x5A:
```python
>>> bytes(x ^ 0x5a for x in bytes.fromhex('166d3531'))
b'L7ok'
```

**9.**
(a)
```
$ printf 'Perché?\n' > p.txt; od -c p.txt
0000000   P   e   r   c   h 303 251   ?  \n
```
`é` occupa due byte, `303 251` in ottale = **C3 A9**.
(b)
```
$ iconv -f UTF-8 -t LATIN1 p.txt > p1.txt; od -A n -t x1 p1.txt
 50 65 72 63 68 e9 3f 0a
```
In Latin-1 `é` è un solo byte, **E9**, cioè proprio il suo punto di codice U+00E9.
(c)
```python
>>> rotto = 'città'.encode('utf-8').decode('latin-1'); rotto
'cittÃ\xa0'
>>> rotto.encode('latin-1').decode('utf-8')
'città'
```
I due byte UTF-8 di `à` (C3 A0) letti come Latin-1 diventano `Ã` e lo spazio non separabile (U+00A0). Ricodificare in Latin-1 restituisce i byte originali, che si rileggono come UTF-8.
(d) In UTF-16 ogni carattere ASCII è seguito (in little-endian) da un byte 00: i byte del file sono `c 00 i 00 t 00 ...`, e la sequenza `città` codificata in UTF-8 non vi compare. Bisogna convertire prima (`iconv -f UTF-16 -t UTF-8 file | grep città`) oppure cercare la sequenza UTF-16 (§8.3).

**10.** `FF D8 FF` è la firma di un **JPEG**; `E0` e poi `4A 46 49 46` (`JFIF`) indicano la variante JFIF.
```
$ printf '\xff\xd8\xff\xe0\x00\x10JFIF' > img.bin
$ printf '\xaa' | dd of=img.bin bs=1 seek=2 count=1 conv=notrunc      # il terzo byte ha offset 2
$ od -A n -t x1 img.bin
 ff d8 aa e0 00 10 4a 46 49 46
$ tail -c +7 img.bin          # dal 7° byte (offset 6) in poi
JFIF
$ dd if=img.bin bs=1 skip=6 2>/dev/null        # equivalente con dd
JFIF
```
Attenzione alle due convenzioni: `dd seek`/`skip` contano da 0 (offset), `tail -c +N` conta da 1.

**11.**
```bash
#!/usr/bin/env bash
# tipo.sh — riconosce alcuni formati dai primi byte, senza usare file(1)
[[ -r ${1-} ]] || { echo "uso: $0 FILE" >&2; exit 2; }
h=$(head -c 8 "$1" | od -A n -t x1 | tr -d ' \n')
case $h in
  89504e470d0a1a0a*) echo PNG ;;
  ffd8ff*)           echo JPEG ;;
  474946383[79]61*)  echo GIF ;;
  255044462d*)       echo PDF ;;
  504b0304*)         echo "ZIP (o docx, xlsx, jar, apk)" ;;
  7f454c46*)         echo ELF ;;
  1f8b*)             echo gzip ;;
  2321*)             echo "script (#!)" ;;
  *)                 echo "sconosciuto: $h" ;;
esac
```
```
$ bash tipo.sh /bin/ls
ELF
$ bash tipo.sh "$(ls /usr/share/doc/*/changelog*.gz | head -1)"
gzip
```
Il confronto avviene sulla stringa esadecimale, quindi i modelli di `case` (L4 §9.4) si scrivono in minuscolo come li produce `od`.

**12.**
(a) `G` = 0x47 = 0100 0111, `o` = 0x6F = 0110 1111, `!` = 0x21 = 0010 0001. Concatenati: 010001 110110 111100 100001 → 17, 54, 60, 33 → `R`, `2`, `8`, `h` (17 = R; 54 = 52 + 2 → `2`; 60 = 52 + 8 → `8`; 33 = 26 + 7 → `h`). Risultato: **`R28h`**.
```
$ printf 'Go!' | base64
R28h
```
(b) 1000 byte = 333 gruppi completi di 3 più 1 byte avanzato: 333·4 + 4 = **1336 caratteri**, l'ultimo gruppo con `==`. Il comando `base64`, per default, va a capo ogni 76 caratteri, e così i caratteri totali diventano 1354; con `-w 0` restano 1336.
(c) Un `=`: l'ultimo gruppo aveva 2 byte (16 bit → 3 caratteri + riempimento). Due `=`: aveva 1 byte (8 bit → 2 caratteri + riempimento).
(d) `TDd7YWJjfQ==` ha 12 caratteri → 3 gruppi → al massimo 9 byte, meno 2 per i `==`: **7 byte**. Inizia con `TDd7`, quindi con `L7{` (§10.3). Infatti è `L7{abc}`.

## ★★★ Sfida

**13.**
```python
def a_senza_segno(x, bit):
    return x & ((1 << bit) - 1)            # tiene solo i 'bit' bit bassi

def a_con_segno(x, bit):
    x = a_senza_segno(x, bit)
    return x - (1 << bit) if x >> (bit - 1) else x   # bit alto a 1: vale x − 2^bit

print(a_con_segno(0xFF, 8), a_con_segno(0x80000000, 32), a_senza_segno(-1, 16))
print(a_senza_segno(200 + 100, 8), a_con_segno(0x7FFFFFFF + 1, 32))
```
```
-1 -2147483648 65535
44 -2147483648
```
La seconda funzione applica direttamente la definizione del §3.2: se il bit più alto vale 1, il suo peso è −2ⁿ⁻¹ invece di +2ⁿ⁻¹, cioè il valore senza segno va diminuito di 2ⁿ. In Python `&` con un numero negativo funziona come in complemento a due con infiniti bit, per questo `a_senza_segno(-1, 16)` dà 65535. Queste due funzioni sono esattamente ciò che fanno `ctypes.c_int8`, `c_uint16`, ecc., e ciò che fa `struct` con le lettere minuscole e maiuscole.

**14.** Soluzione della mini-CTF.
```
$ bash setup_sfida.sh
$ cd ~/l7_sfida; cat LEGGIMI.txt
```
*Pezzo 1, strati.txt.* Il contenuto, `NGMzNzdiNjk1ZjYyNzk3NDY1NWY=`, ha l'aspetto del base64 (alfabeto, lunghezza 28, `=`). Decodificato dà `4c377b695f627974655f`: solo cifre esadecimali, lunghezza pari. Decodificato di nuovo:
```
$ base64 -d strati.txt | xxd -r -p; echo
L7{i_byte_
$ base64 -d strati.txt | python3 -c 'import sys; print(bytes.fromhex(sys.stdin.read()).decode())'   # senza xxd
L7{i_byte_
```
L'ordine giusto è "prima il base64, poi l'esadecimale": lo strato esterno è l'ultimo applicato.

*Pezzo 2, numeri.bin.* "Interi senza segno a 32 bit nell'ordine della rete" = **big-endian** (§5.2). Il dump lo conferma: `00 00 00 6e 00 00 00 6f ...`, cioè tre zeri e poi un byte ASCII.
```
$ od -A n -t x1 numeri.bin | head -1
 00 00 00 6e 00 00 00 6f 00 00 00 6e 00 00 00 5f
$ od -A n -t u4 --endian=big numeri.bin | tr -s ' ' '\n' | grep . |
    while read n; do printf "\\$(printf '%03o' "$n")"; done; echo
non_hanno_
$ python3 -c 'import struct; b=open("numeri.bin","rb").read(); print("".join(chr(x) for x in struct.unpack(">%dI" % (len(b)//4), b)))'
non_hanno_
```
Con `od -t u4` senza `--endian=big`, su x86 avresti letto 0x6e000000 = 1 845 493 760: il numero "enorme e rotondo" che segnala l'ordine sbagliato (§5.4).

*Pezzo 3, bit.txt.* Gruppi di 8 simboli fatti di `o` e `I`: sono bit, `o` = 0 e `I` = 1 (il primo simbolo di ogni gruppo è sempre `o`, come il bit più alto di un carattere ASCII).
```
$ for b in $(tr 'oI' '01' < bit.txt); do printf "\\$(printf '%03o' $((2#$b)))"; done; echo
un_solo_
```
*Pezzo 4, ultimo.txt.* `cat` lo mostra quasi normale, `grep` no: `od -c` rivela `377 376` all'inizio (il BOM `FF FE`) e un NUL dopo ogni lettera. È **UTF-16 little-endian** (§8.3).
```
$ file ultimo.txt
ultimo.txt: Unicode text, UTF-16, little-endian text
$ iconv -f UTF-16 -t UTF-8 ultimo.txt
significato}
```

**Flag:** `L7{i_byte_non_hanno_un_solo_significato}`

**15.**
(a) Se il chiaro inizia con una parola nota lunga almeno quanto la chiave, XOR tra quei byte di chiaro e i primi byte del cifrato dà la chiave ripetuta, e la ripetizione stessa ne rivela la lunghezza. In una prova con la chiave `13 37 42` e il testo che inizia con `Benvenuti`:
```python
>>> bytes(c[i] ^ b"Benvenuti"[i] for i in range(9)).hex()
'133742133742133742'
```
Lo schema si ripete ogni 3 byte: la chiave è `13 37 42`. Poi si decifra tutto con `bytes(x ^ k[i % len(k)] for i, x in enumerate(c))`.
(b) Senza un inizio noto, il metodo classico ha due passi.
1. **Lunghezza della chiave.** Per ogni lunghezza candidata *L* si divide il cifrato in *L* colonne (i byte in posizione *j*, *j*+*L*, *j*+2*L*...): con la *L* giusta ogni colonna è stata cifrata con **un solo** byte di chiave, quindi conserva la distribuzione delle frequenze del testo. Si sceglie la *L* che rende le colonne più "simili a un testo"; due misure usate sono l'indice di coincidenza e la distanza di Hamming media tra blocchi consecutivi di lunghezza *L* (che è minima per la lunghezza giusta).
2. **I byte della chiave.** Ogni colonna è uno XOR con un byte singolo: si provano i 256 valori e si sceglie quello che produce il testo più plausibile. Una scorciatoia: in un testo il carattere più frequente è quasi sempre lo spazio (0x20), quindi il byte più frequente della colonna, XOR 0x20, dà probabilmente il byte della chiave.

Con un testo breve la scorciatoia può sbagliare qualche byte: nella prova sopra, con un centinaio di caratteri e *L* = 3, ha trovato due byte su tre, e il terzo si corregge a mano guardando il testo parzialmente decifrato. Con un testo più lungo funziona quasi sempre. È lo stesso ragionamento che si usa per il cifrario di Vigenère, e lo riprenderemo nel Modulo 5.

**16.**
```python
# scrivi.py
import struct
nome = b"zen"
dati = b"CTF1" + struct.pack(">I", len(nome)) + nome + struct.pack("<H", 1337)
open("record.bin", "wb").write(dati)
```
```python
# leggi.py
import struct, sys
b = open(sys.argv[1], "rb").read()
if b[:4] != b"CTF1":
    sys.exit("non è un file CTF1")
(n,) = struct.unpack(">I", b[4:8])
nome = b[8:8 + n].decode("ascii")
(punti,) = struct.unpack("<H", b[8 + n:10 + n])
(sbagliato,) = struct.unpack(">H", b[8 + n:10 + n])
print(f"nome={nome} punteggio={punti} (letto in big-endian: {sbagliato})")
```
```
$ python3 scrivi.py; od -A x -t x1 record.bin
000000 43 54 46 31 00 00 00 03 7a 65 6e 39 05
$ python3 leggi.py record.bin
nome=zen punteggio=1337 (letto in big-endian: 14597)
```
Nel dump si leggono tutti i campi: `43 54 46 31` (`CTF1`), `00 00 00 03` (3, big-endian), `7a 65 6e` (`zen`), `39 05` (1337 = 0x0539, little-endian). Letto in big-endian, `39 05` diventa 0x3905 = 14 597. Il programma di lettura controlla il numero magico prima di fidarsi del resto: è la prima regola di ogni parser.

**17.** Tracce per le risposte.
(a) Oggi la memoria si indirizza a byte di 8 bit e le parole sono di 16, 32, 64 bit: tutti multipli di 4, quindi l'esadecimale (4 bit per cifra) li divide esattamente, mentre l'ottale (3 bit) no (un byte sono 2 cifre ottali e 2 bit avanzati). L'ottale era naturale sulle macchine degli anni '60 con parole di 12, 18 o 36 bit, ed è sopravvissuto nei permessi Unix perché quei 9 bit sono proprio tre gruppi da tre (`rwx`).
(b) È compatibile con ASCII (un testo ASCII è già UTF-8, e i byte sotto 0x80 non compaiono mai dentro un carattere multi-byte, quindi i programmi che cercano `/` o `\n` non sbagliano); non ha problemi di ordine dei byte (le unità sono singoli byte, niente BOM necessario); è autosincronizzante (da qualunque punto si ritrova l'inizio di un carattere); copre tutto Unicode senza code page e senza dover dichiarare una tabella per regione; è compatta per i testi in caratteri latini, la maggioranza dei protocolli e del codice.
(c) **Codificare** trasforma in un formato diverso, in modo pubblico: errore tipico, "proteggere" una password con base64 (chiunque la decodifica). **Cifrare** rende i dati illeggibili senza chiave, ed è reversibile con la chiave: errore tipico, conservare le password degli utenti cifrate, con la chiave sullo stesso server (chi ruba il database ruba anche la chiave e le ottiene tutte). **Fare l'hash** è irreversibile e serve a verificare senza conservare: errore tipico, usare un hash veloce e senza sale (SHA-256 nudo), che permette di provare miliardi di password al secondo e di riconoscere le password uguali. Per le password si usa un hash **lento e con sale** (bcrypt, yescrypt, Argon2).
