# Modulo 1 — Lezione 7: Rappresentare i dati

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 7 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 14).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. convertire a mente e con gli strumenti tra basi 2, 8, 10 e 16, e spiegare perché i programmatori usano l'esadecimale;
2. dire che cosa sono bit, byte e parole, quali valori può contenere un intero di 8, 16, 32 e 64 bit, con e senza segno, e che cosa succede quando un calcolo esce da quell'intervallo;
3. spiegare il **complemento a due**, calcolare la rappresentazione di un numero negativo e riconoscere a colpo d'occhio valori come `0xffffffff` e `0x80000000`;
4. usare gli operatori sui bit (AND, OR, XOR, NOT, scorrimenti) e le maschere, e conoscere le proprietà dello XOR che userai in crittografia;
5. spiegare l'**ordine dei byte** (*endianness*), leggere correttamente un intero in un dump esadecimale di una macchina x86, e convertire tra ordine della macchina e ordine della rete;
6. descrivere ASCII, Unicode, UTF-8 e UTF-16, riconoscere un problema di codifica (*mojibake*, NUL sparsi, BOM) e risolverlo;
7. usare le codifiche di trasporto (esadecimale, base64, base32, codifica URL) e distinguerle dalla cifratura e dall'hash;
8. ispezionare qualunque file a livello di byte con `xxd`, `od`, `file`, `strings`, `iconv`, Python, e riconoscere i formati dai loro **numeri magici**;
9. riconoscere quando un dato è stato interpretato nel modo sbagliato (base, segno, ordine dei byte, codifica) e correggere l'interpretazione.

**Prerequisiti:** Lezioni 1–5. In particolare: aritmetica di bash `$(( ))` (L4 §9.2), `printf` (L4 §12.3), `tr` e i filtri (L3), le pipe (L4). Non serve matematica oltre le quattro operazioni e le potenze.

**Tempo:** circa 4 ore di lettura e prove, 4 ore di esercizi. È una lezione da fare **con carta e penna**: le conversioni vanno fatte a mano almeno qualche volta, prima di affidarle agli strumenti. In una gara non avrai tempo di aprire un convertitore per riconoscere che `0x41` è `A`.

**Ripasso dalle lezioni precedenti.**
- Nella Lezione 2 abbiamo detto che un file è una sequenza di byte, e che "testo" e "binario" sono solo modi di interpretarla (L2 §2). Oggi studiamo quei modi.
- Nella Lezione 3 abbiamo usato `tr` per il rot13 e `base64` per decodificare (L3 §5, §13). Oggi capiamo che cosa fanno davvero.
- Nella Lezione 5 abbiamo letto le maschere dei segnali in esadecimale, bit per bit (L5 §8.6). Era un'anteprima di questa lezione.

**Convenzione tipografica.** Come nelle lezioni precedenti. Per indicare la base di un numero usiamo i prefissi del linguaggio C: `0x` per l'esadecimale (`0x41`), `0b` per il binario (`0b1000001`), `0` iniziale o `0o` per l'ottale (`0101`, `0o101`); senza prefisso il numero è decimale. Quando serve chiarezza scriviamo la base in pedice: 65₁₀ = 41₁₆ = 1000001₂.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. I numeri | 1–6 | Come si scrive un numero in byte? Che cosa succede ai bordi? |
| II. Il testo | 7–9 | Come diventa byte una lettera? Perché a volte esce spazzatura? |
| III. Codifiche e strumenti | 10–12 | Come si trasportano byte qualunque in un testo? Come si guarda dentro un file? |
| IV. La pratica | 13–18 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — I numeri

## 1. Sistemi di numerazione posizionali

### 1.1 L'idea

Scriviamo i numeri con un sistema **posizionale**: il valore di una cifra dipende dalla sua posizione. In base 10, la scrittura 2024 significa

2·10³ + 0·10² + 2·10¹ + 4·10⁰ = 2000 + 0 + 20 + 4.

Non c'è niente di speciale nel 10 (probabilmente lo usiamo perché abbiamo dieci dita). In una **base** *b* qualunque si usano le cifre da 0 a *b*−1, e una scrittura *dₙ...d₁d₀* vale

*dₙ·bⁿ + ... + d₁·b¹ + d₀·b⁰*.

Le basi che contano in informatica sono quattro:

| Base | Nome | Cifre | Perché si usa |
|---|---|---|---|
| 2 | binario | 0 1 | è la base dell'hardware: un bit è un circuito acceso o spento |
| 8 | ottale | 0–7 | ogni cifra rappresenta 3 bit: comodo per i permessi Unix (`chmod 755`) |
| 10 | decimale | 0–9 | è quella che usiamo noi |
| 16 | esadecimale | 0–9, A–F | ogni cifra rappresenta **4 bit**: due cifre fanno un byte |

### 1.2 Il binario

In base 2 le cifre sono 0 e 1, e le posizioni valgono 1, 2, 4, 8, 16, 32, 64, 128, ... Conviene conoscere a memoria le potenze di 2 almeno fino a 2¹⁶:

| n | 2ⁿ | n | 2ⁿ | n | 2ⁿ |
|---|---|---|---|---|---|
| 0 | 1 | 6 | 64 | 12 | 4096 |
| 1 | 2 | 7 | 128 | 13 | 8192 |
| 2 | 4 | 8 | 256 | 14 | 16384 |
| 3 | 8 | 9 | 512 | 15 | 32768 |
| 4 | 16 | 10 | 1024 | 16 | 65536 |
| 5 | 32 | 11 | 2048 | 32 | 4294967296 |

Da binario a decimale si sommano le potenze corrispondenti agli 1:

0b1011 0110 = 128 + 32 + 16 + 4 + 2 = 182.

Da decimale a binario ci sono due metodi.

- **Sottrazioni successive** (comodo a mente): trova la potenza di 2 più grande che non supera il numero, scrivi 1 in quella posizione, sottrai, ripeti. 182: 128 ci sta (resta 54), 64 no, 32 sì (resta 22), 16 sì (resta 6), 8 no, 4 sì (resta 2), 2 sì (resta 0), 1 no → 1011 0110.
- **Divisioni successive** (meccanico, funziona in ogni base): dividi per 2 e annota il resto, finché il quoziente è 0; i resti letti **dal basso verso l'alto** sono le cifre. 182 → 91 r 0 → 45 r 1 → 22 r 1 → 11 r 0 → 5 r 1 → 2 r 1 → 1 r 0 → 0 r 1: letti dal basso, 10110110.

Il secondo metodo funziona perché ogni divisione per *b* "stacca" la cifra meno significativa: il resto è *d₀*, il quoziente è il numero con le cifre spostate di una posizione a destra.

### 1.3 L'esadecimale

In base 16 servono sedici cifre: 0–9 e poi A=10, B=11, C=12, D=13, E=14, F=15 (maiuscole o minuscole indifferentemente). La ragione per cui l'esadecimale è ovunque in informatica è una sola: **16 = 2⁴**, quindi ogni cifra esadecimale corrisponde **esattamente** a 4 bit (un *nibble*), e la conversione tra binario ed esadecimale si fa **per gruppi**, senza calcoli:

| Hex | Bin | Hex | Bin | Hex | Bin | Hex | Bin |
|---|---|---|---|---|---|---|---|
| 0 | 0000 | 4 | 0100 | 8 | 1000 | C | 1100 |
| 1 | 0001 | 5 | 0101 | 9 | 1001 | D | 1101 |
| 2 | 0010 | 6 | 0110 | A | 1010 | E | 1110 |
| 3 | 0011 | 7 | 0111 | B | 1011 | F | 1111 |

Questa tabella va imparata. Con essa:

- 0b1011 0110 → B 6 → **0xB6**;
- 0xDEADBEEF → 1101 1110 1010 1101 1011 1110 1110 1111.

Da esadecimale a decimale si usa la formula posizionale: 0xB6 = 11·16 + 6 = 182. Per numeri grandi è più comodo passare dagli strumenti (§1.5).

Due cifre esadecimali descrivono un byte (8 bit, da 0x00 a 0xFF = 255); otto cifre un intero a 32 bit; sedici un intero o un indirizzo a 64 bit. Per questo gli indirizzi di memoria che abbiamo visto in `/proc/<PID>/maps` (L5 §7.4) sono scritti in esadecimale: `7ffd8a1f3000` sono 12 cifre, cioè 48 bit, la dimensione effettiva degli indirizzi virtuali su x86-64.

Alcuni valori esadecimali "parlanti" compaiono così spesso che vale la pena riconoscerli: `0xDEADBEEF`, `0xCAFEBABE` (l'inizio di ogni file `.class` di Java), `0xFEEDFACE` (Mach-O), `0x41414141` (`AAAA`, il riempitivo classico degli exploit), `0x90` (l'istruzione NOP di x86), `0xCC` (l'istruzione INT3, il breakpoint dei debugger).

### 1.4 L'ottale

In base 8 ogni cifra corrisponde a **3 bit**. Oggi l'ottale sopravvive quasi solo in due posti: i **permessi di Unix**, dove i nove bit `rwxr-xr-x` si dividono naturalmente in tre gruppi da tre (`111 101 101` = `755`), e le **sequenze di escape** dei caratteri (`\101` = 65 = `A` in `printf` e in C). Attenzione a una trappola di molti linguaggi: in C, in bash e in vecchie versioni di JavaScript, un numero che inizia con 0 è **ottale**: `010` vale 8. In bash `$((010))` è 8 e `$((09))` è un errore (`value too great for base`), il che causa errori sorprendenti con orari e date (`$((08 + 1))`). La soluzione è forzare la base: `$((10#08 + 1))`.

### 1.5 Gli strumenti

```
$ echo $((16#B6)) $((2#10110110)) $((8#266)) $((0xB6)) $((0266))   # da una base qualunque a decimale
182 182 182 182 182
$ printf '%x %X %o %d\n' 182 182 182 0xB6                        # da decimale a hex, ottale
b6 B6 266 182
$ printf '%08x\n' 182                                             # con zeri davanti, 8 cifre
000000b6
$ echo 'obase=2; 182' | bc                                        # in binario (bash non ha %b per i numeri)
10110110
$ echo 'ibase=16; obase=2; B6' | bc                               # da hex a binario (ibase in MAIUSCOLO)
10110110
$ python3 -c 'print(bin(182), hex(182), oct(182), int("b6", 16), int("10110110", 2))'
0b10110110 0xb6 0o266 182 182
```

Con `bc` attenzione all'ordine: se imposti prima `ibase=16`, il successivo `obase=10` viene letto **in base 16** e vale 16. Imposta sempre prima `obase`, poi `ibase`.

## 2. Bit, byte e interi senza segno

### 2.1 Le unità

Un **bit** è una cifra binaria. Un **byte** è un gruppo di **8 bit**, l'unità minima che il processore indirizza: ogni indirizzo di memoria indica un byte. (Storicamente il byte non è sempre stato di 8 bit; oggi lo è ovunque, e gli standard di rete, per essere precisi, parlano di **ottetto**.) Una **parola** (*word*) è la dimensione "naturale" dei dati per un processore: 64 bit sulle macchine moderne. Purtroppo la terminologia è confusa: nella documentazione Intel, per ragioni storiche, una *word* è di 16 bit, una *doubleword* (`dword`) di 32 e una *quadword* (`qword`) di 64. Li ritroverai nell'assembly del Modulo 2 e in `gdb` (`x/4wx` mostra 4 *word* da 4 byte).

Per le quantità grandi esistono due sistemi di multipli, e confonderli è un errore frequente:

| Prefisso SI (potenze di 10) | Prefisso IEC (potenze di 2) |
|---|---|
| kB = 1000 byte | KiB (*kibibyte*) = 1024 byte |
| MB = 10⁶ | MiB = 2²⁰ = 1 048 576 |
| GB = 10⁹ | GiB = 2³⁰ |
| TB = 10¹² | TiB = 2⁴⁰ |

Un disco da "1 TB" ha 10¹² byte, che il sistema operativo mostra come circa 931 GiB. `ls -lh` e `df -h` usano le potenze di 2 (anche se scrivono "K", "M", "G"); `df -H` le potenze di 10. I bit si indicano con la *b* minuscola: una connessione da 100 Mbit/s trasferisce al massimo 12,5 MB/s.

### 2.2 Gli interi senza segno

Con *n* bit si scrivono 2ⁿ valori diversi. Se li interpretiamo come numeri **senza segno** (*unsigned*), vanno da 0 a 2ⁿ − 1:

| Bit | Tipo C tipico | Massimo senza segno | In esadecimale |
|---|---|---|---|
| 8 | `uint8_t`, `unsigned char` | 255 | `0xFF` |
| 16 | `uint16_t` | 65 535 | `0xFFFF` |
| 32 | `uint32_t`, `unsigned int` | 4 294 967 295 | `0xFFFFFFFF` |
| 64 | `uint64_t`, `size_t` (su 64 bit) | 18 446 744 073 709 551 615 | `0xFFFFFFFFFFFFFFFF` |

Il massimo è sempre "tutti i bit a 1". Una regola pratica utile: 2¹⁰ ≈ 10³, quindi 2³² ≈ 4·10⁹ ("quattro miliardi") e 2⁶⁴ ≈ 1,8·10¹⁹.

### 2.3 L'aritmetica modulare e l'overflow

Che cosa succede se a un intero senza segno di 8 bit che vale 200 aggiungiamo 100? Il risultato vero, 300, non sta in 8 bit (300 = 0b1 0010 1100, 9 bit). Il processore tiene solo gli 8 bit bassi e scarta il riporto: il risultato è 0b0010 1100 = **44**. In generale, l'aritmetica su interi senza segno di *n* bit è **aritmetica modulo 2ⁿ**: il risultato è il resto della divisione per 2ⁿ. Si dice che il valore "fa il giro" (*wraps around*), come il contachilometri di un'auto che dopo 99999 torna a 00000.

```
$ echo $(( (200 + 100) & 0xFF ))    # & 0xFF tiene solo gli 8 bit bassi: simula un uint8
44
$ echo $(( (0 - 1) & 0xFF ))        # e all'indietro: 0 - 1 = 255
255
```

Questo comportamento (CSAPP, cap. 2.3.1) è **definito** per i tipi senza segno in C, e va sempre tenuto presente quando si calcolano dimensioni e lunghezze: il Modulo 4 è dedicato agli errori che ne derivano.

## 3. Gli interi con segno

### 3.1 Il problema

Come rappresentare i numeri negativi con soli bit? Le idee storiche sono tre (CSAPP, cap. 2.2).

1. **Modulo e segno** (*sign-magnitude*): il bit più a sinistra indica il segno (0 positivo, 1 negativo), gli altri il valore assoluto. In 8 bit, +5 = 0000 0101 e −5 = 1000 0101. È intuitivo, ma ha due zeri (0000 0000 e 1000 0000) e le somme richiedono circuiti diversi a seconda dei segni. Sopravvive nei numeri in virgola mobile (§6).
2. **Complemento a uno**: il negativo si ottiene invertendo tutti i bit. −5 = 1111 1010. Ha ancora due zeri.
3. **Complemento a due** (*two's complement*): quello che usano **tutti** i processori moderni, e che il C impone dallo standard C23.

### 3.2 Il complemento a due

L'idea è semplice e geniale: in *n* bit, il bit più significativo non vale +2ⁿ⁻¹, ma **−2ⁿ⁻¹**. Tutti gli altri bit mantengono il loro peso positivo. In 8 bit i pesi sono:

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Peso | **−128** | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Quindi:

- 0111 1111 = 64+32+16+8+4+2+1 = **127**, il massimo positivo;
- 1000 0000 = **−128**, il minimo;
- 1111 1111 = −128 + 127 = **−1**;
- 1111 1011 = −128 + 64+32+16+8+2+1 = −128 + 123 = **−5**.

L'intervallo di un intero con segno di *n* bit è da **−2ⁿ⁻¹ a 2ⁿ⁻¹ − 1**: in 8 bit da −128 a 127, in 32 bit da −2 147 483 648 a 2 147 483 647. Un solo zero, e un negativo in più dei positivi: l'intervallo è asimmetrico.

**Come si nega un numero.** La regola pratica: **inverti tutti i bit e aggiungi 1**. +5 = 0000 0101 → invertito 1111 1010 → +1 → 1111 1011 = −5. Funziona anche al contrario: −5 = 1111 1011 → 0000 0100 → +1 → 0000 0101 = +5.

**Perché funziona, e perché piace all'hardware.** In complemento a due, la sequenza di bit che rappresenta −*x* in *n* bit è la stessa che rappresenta, senza segno, 2ⁿ − *x*. Quindi i numeri negativi sono semplicemente i numeri "dall'altra parte" del giro dell'aritmetica modulare: −1 ≡ 255 (mod 256). Di conseguenza **la somma, la sottrazione e la moltiplicazione sono identiche** per numeri con e senza segno: il processore usa lo stesso circuito, e solo l'**interpretazione** del risultato cambia. È per questo che nessuno usa più gli altri sistemi.

### 3.3 Stessi bit, valori diversi

Il punto da fissare è questo: **una sequenza di bit non ha un valore finché non si decide come interpretarla**. Gli stessi 32 bit `0xFFFFFFFF` valgono 4 294 967 295 come `unsigned int` e −1 come `int`. Gli stessi 8 bit `0x80` valgono 128 o −128. Questa è anche la frase che dà il titolo alla flag di oggi.

| Bit (32) | Senza segno | Con segno |
|---|---|---|
| `0x00000000` | 0 | 0 |
| `0x7FFFFFFF` | 2 147 483 647 | 2 147 483 647 (massimo `int`, `INT_MAX`) |
| `0x80000000` | 2 147 483 648 | −2 147 483 648 (minimo `int`, `INT_MIN`) |
| `0xFFFFFFFE` | 4 294 967 294 | −2 |
| `0xFFFFFFFF` | 4 294 967 295 | −1 |

In bash gli interi sono a **64 bit con segno**, e lo si vede bene:

```
$ printf '%x\n' -1                          # −1 visto come 64 bit senza segno
ffffffffffffffff
$ echo $(( 0x7fffffffffffffff + 1 ))        # il massimo più uno fa il giro sul minimo
-9223372036854775808
$ echo $(( -128 & 0xFF ))                   # gli 8 bit bassi di −128
128
```

In una sfida di *reversing* o di *pwn* questo si traduce in un riflesso: quando in un debugger vedi `0xffffffff` o `0xfffffffffffffff0`, pensa subito "−1" e "−16".

### 3.4 Cambiare dimensione: estensione e troncamento

Quando un valore passa da un tipo più piccolo a uno più grande, va **esteso**:

- un valore **senza segno** si estende con zeri a sinistra (*zero extension*): `0xFB` (251) in 16 bit diventa `0x00FB`;
- un valore **con segno** si estende **copiando il bit di segno** (*sign extension*): `0xFB` (−5) in 16 bit diventa `0xFFFB`, che vale ancora −5.

Quando invece un valore passa a un tipo più piccolo, viene **troncato**: si tengono i bit bassi, gli altri si perdono. 300 (`0x012C`) troncato a 8 bit diventa `0x2C` = 44; un `long` che vale 4 294 967 297 (`0x1_0000_0001`) troncato a 32 bit diventa 1. Il troncamento non dà errori: semplicemente cambia il valore. Ne parleremo nel Modulo 4.

In assembly x86 ci sono istruzioni distinte per le due estensioni (`movzx` e `movsx`): saperlo ti farà capire subito, nel Modulo 3, se il programma che stai leggendo tratta un valore come con segno o senza.

## 4. Le operazioni sui bit

### 4.1 Gli operatori

Oltre all'aritmetica, i processori offrono operazioni che lavorano **bit per bit**, indipendentemente in ogni posizione. In C, in bash (dentro `$(( ))`) e in Python si scrivono allo stesso modo:

| Operatore | Nome | Regola per ogni bit | Esempio (8 bit) |
|---|---|---|---|
| `a & b` | AND | 1 se **entrambi** sono 1 | `1100 1010 & 0000 1111 = 0000 1010` |
| `a \| b` | OR | 1 se **almeno uno** è 1 | `1100 1010 \| 0000 1111 = 1100 1111` |
| `a ^ b` | XOR (*or esclusivo*) | 1 se sono **diversi** | `1100 1010 ^ 0000 1111 = 1100 0101` |
| `~a` | NOT | inverte | `~1100 1010 = 0011 0101` |
| `a << k` | scorrimento a sinistra | sposta i bit di *k* posizioni, entrano zeri a destra | `0000 0101 << 2 = 0001 0100` |
| `a >> k` | scorrimento a destra | sposta di *k* a destra | `1001 0100 >> 2 = 0010 0101` (logico) |

Non confonderli con gli operatori **logici** `&&`, `||`, `!`, che lavorano su valori di verità interi (0 è falso, tutto il resto vero): `2 & 1` vale 0, ma `2 && 1` vale 1.

Gli scorrimenti hanno un significato aritmetico: `x << k` moltiplica per 2ᵏ (finché non si esce dai bit disponibili), `x >> k` divide per 2ᵏ arrotondando verso il basso. Per lo scorrimento a destra esistono due versioni: **logico**, che fa entrare zeri (usato per i senza segno), e **aritmetico**, che fa entrare copie del bit di segno, così che un negativo resti negativo (−8 >> 1 = −4). In C la scelta dipende dal tipo; bash e Python usano sempre quello aritmetico (bash lavora su interi con segno):

```
$ echo $(( 5 << 2 )) $(( 20 >> 2 )) $(( -8 >> 1 ))
20 5 -4
```

### 4.2 Le maschere

Le operazioni sui bit servono soprattutto a leggere e modificare **singoli bit o gruppi di bit** dentro un intero, usando una **maschera** (*mask*): un valore con 1 nelle posizioni che ci interessano.

| Obiettivo | Espressione | Esempio |
|---|---|---|
| leggere il bit *k* | `(x >> k) & 1` | il bit 14 di una maschera di segnali (L5 §8.6) |
| accendere il bit *k* | `x \| (1 << k)` | |
| spegnere il bit *k* | `x & ~(1 << k)` | |
| invertire il bit *k* | `x ^ (1 << k)` | |
| tenere gli *n* bit bassi | `x & ((1 << n) - 1)` | `x & 0xFF` = il byte basso |
| estrarre il byte *i* | `(x >> (8*i)) & 0xFF` | |

Ne abbiamo già visto un uso: i permessi Unix sono una maschera di 12 bit, e `chmod g+w` accende un bit. Un altro, molto bello, viene dalla tabella ASCII (§7.2): lettere maiuscole e minuscole differiscono solo per il bit 5 (0x20). `'A'` = 0x41 = 0100 0001, `'a'` = 0x61 = 0110 0001. Quindi `c | 0x20` rende minuscola una lettera, `c & ~0x20` la rende maiuscola, `c ^ 0x20` scambia maiuscole e minuscole.

### 4.3 Le proprietà dello XOR

Lo XOR merita un paragrafo a parte, perché è l'operazione più importante della crittografia simmetrica (Modulo 5) e compare in un'infinità di sfide. Le sue proprietà, per ogni *a*, *b*, *c*:

1. *a* ⊕ 0 = *a* (lo zero è neutro);
2. *a* ⊕ *a* = 0 (ogni valore è l'inverso di sé stesso);
3. *a* ⊕ *b* = *b* ⊕ *a*, e (*a* ⊕ *b*) ⊕ *c* = *a* ⊕ (*b* ⊕ *c*) (commutativa e associativa);
4. quindi (*a* ⊕ *k*) ⊕ *k* = *a*: **applicare due volte la stessa chiave riporta l'originale**.

La proprietà 4 è il principio di una cifratura elementare: dato un messaggio *m* e una chiave *k*, il testo cifrato è *c* = *m* ⊕ *k*, e si decifra con lo stesso XOR, *m* = *c* ⊕ *k*. Se *k* è casuale, lunga quanto il messaggio e usata una volta sola, è il **one-time pad**, l'unico cifrario dimostrabilmente perfetto. Se invece la chiave è corta e ripetuta, è debolissima: e c'è una conseguenza ancora più utile in una CTF. Dalla proprietà 4 segue che *m* ⊕ *c* = *k*: **se conosci un pezzo del messaggio in chiaro e il cifrato corrispondente, ottieni il pezzo di chiave**. Poiché le flag iniziano con un prefisso noto (`flag{`, `L7{`, `CTF{`), un cifrato prodotto con uno XOR a chiave corta si rompe quasi sempre così (Esercizio 15).

Un piccolo esempio a mano con un byte: *m* = `'L'` = 0x4C = 0100 1100, *k* = 0x2A = 0010 1010 → *c* = 0110 0110 = 0x66 = `'f'`. E 0x66 ⊕ 0x2A = 0x4C: si torna a `'L'`.

## 5. L'ordine dei byte (endianness)

### 5.1 Il problema

Un intero di 32 bit occupa 4 byte. La memoria è una sequenza di byte, ciascuno con un indirizzo. In quale **ordine** vanno messi i 4 byte di un intero? Prendiamo il valore 0x12345678: il suo byte più significativo è 0x12, il meno significativo 0x78. Le scelte possibili sono due (CSAPP, cap. 2.1.3).

- **Big-endian** ("prima l'estremità grande"): il byte più significativo all'indirizzo più basso. In memoria, dall'indirizzo *a* in su: `12 34 56 78`. È l'ordine in cui scriviamo i numeri sulla carta.
- **Little-endian** ("prima l'estremità piccola"): il byte **meno** significativo all'indirizzo più basso. In memoria: `78 56 34 12`.

```
indirizzo:        a     a+1   a+2   a+3
big-endian:      12    34    56    78
little-endian:   78    56    34    12
```

I nomi vengono dai *Viaggi di Gulliver* di Swift, dove due popoli si fanno la guerra per decidere da quale estremità si debba rompere un uovo sodo; li introdusse Danny Cohen nel 1980 in un articolo dal titolo *On Holy Wars and a Plea for Peace*, proprio per sottolineare che la scelta è arbitraria. Ma una volta fatta, conta moltissimo.

### 5.2 Chi usa che cosa

- **x86 e x86-64** (Intel e AMD): **little-endian**. Le macchine su cui lavori e quasi tutti i binari delle sfide *pwn* e *reversing*.
- **ARM** e **RISC-V**: *bi-endian* in teoria, **little-endian** in pratica (Android, iPhone, Mac con Apple Silicon, Raspberry Pi).
- **Big-endian**: i vecchi PowerPC e SPARC, molti processori MIPS (router), IBM z/Architecture.
- **I protocolli di rete**: per convenzione **big-endian**, detto per questo *network byte order*. I numeri di porta e gli indirizzi IP nelle intestazioni TCP/IP sono scritti con il byte più significativo per primo (Lezione 10). In C esistono le funzioni `htons`, `htonl` (*host to network short/long*) e `ntohs`, `ntohl` per convertire.
- **I formati di file**: ognuno sceglie. PNG e JPEG usano big-endian; i formati nati su Windows (BMP, WAV, il formato PE degli eseguibili) e ELF su x86 usano little-endian.

L'ordine riguarda solo i **multi-byte** interpretati come numeri. Una stringa di testo è una sequenza di byte singoli, e sta in memoria nell'ordine in cui la leggi in qualunque architettura.

### 5.3 Vederlo con gli strumenti

`od` (L2 §2.3) legge i byte e li può interpretare come interi della macchina:

```
$ printf '\x78\x56\x34\x12' | od -A n -t x1      # byte per byte, nell'ordine del file
 78 56 34 12
$ printf '\x78\x56\x34\x12' | od -A n -t x4      # come intero a 32 bit, ordine della macchina (x86)
 12345678
$ printf '\x78\x56\x34\x12' | od -A n -t x4 --endian=big
 78563412
```

Python offre due strumenti: i metodi `int.to_bytes`/`int.from_bytes` e il modulo `struct`, dove `<` indica little-endian e `>` big-endian, e le lettere indicano il tipo (`B` 1 byte senza segno, `H` 2 byte, `I` 4 byte, `Q` 8 byte; le minuscole `b`, `h`, `i`, `q` sono con segno):

```python
>>> import struct
>>> struct.pack('<I', 0x12345678).hex()
'78563412'
>>> struct.pack('>I', 0x12345678).hex()
'12345678'
>>> int.from_bytes(b'\x78\x56\x34\x12', 'little')
305419896
>>> hex(305419896)
'0x12345678'
>>> struct.unpack('<i', b'\xff\xff\xff\xff')     # con segno: −1
(-1,)
```

### 5.4 Perché conta nelle CTF

Tre situazioni ricorrenti:

1. **Leggere la memoria in un debugger.** Se in `gdb` esamini 8 byte a partire da un indirizzo con `x/8bx` vedi i byte nell'ordine della memoria; con `x/2wx` li vedi raggruppati in due interi da 4 byte, e quindi **rovesciati** a gruppi di quattro. Una stringa `"ABCD"` in memoria è `41 42 43 44`, ma letta come intero a 32 bit su x86 vale 0x44434241. Quando nel Modulo 3 vedrai un programma che confronta un registro con `0x67616c66`, dovrai riconoscere al volo `"flag"` scritto alla rovescia.
2. **Scrivere un indirizzo in un exploit.** Per sovrascrivere un puntatore con l'indirizzo 0x401136 su x86-64 devi mandare i byte `36 11 40 00 00 00 00 00`. La libreria `pwntools` (Lezione 8) ha le funzioni `p32`, `p64` (e `u32`, `u64` per l'operazione inversa) che lo fanno per te; ma devi sapere che cosa fanno.
3. **Interpretare un formato binario.** Un file o un pacchetto di rete contiene campi numerici; leggerli con l'ordine sbagliato dà valori assurdi (una lunghezza di 16 777 216 invece di 1). Se un numero letto da un file sembra enorme e "rotondo" in esadecimale (0x01000000, 0x00010000), probabilmente lo stai leggendo nell'ordine sbagliato.

## 6. I numeri non interi, in breve

I numeri con la virgola si rappresentano con lo standard **IEEE 754** (CSAPP, cap. 2.4). Un `double` (64 bit) è diviso in tre campi: 1 bit di **segno**, 11 bit di **esponente**, 52 bit di **mantissa** (la parte frazionaria), e rappresenta il numero (−1)^segno × 1,mantissa × 2^(esponente − 1023). È la notazione scientifica, in base 2. Un `float` (32 bit) ha 1 + 8 + 23 bit.

La conseguenza che tutti devono conoscere: **molti numeri decimali "semplici" non sono rappresentabili esattamente**. 0,1 in binario è periodico (0,000110011001100...₂), come 1/3 in decimale, e viene arrotondato. Da qui il risultato famoso:

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
>>> (0.1).hex()                 # la rappresentazione esatta: 1,999...₁₆ × 2⁻⁴
'0x1.999999999999ap-4'
```

Per questo i soldi non si contano mai con i `float` (si usano interi in centesimi o tipi decimali), e i confronti tra numeri in virgola mobile si fanno con una tolleranza. IEEE 754 ha anche valori speciali: +∞ e −∞, **NaN** (*Not a Number*, il risultato di 0/0, che è diverso da ogni valore compreso sé stesso), e due zeri, +0 e −0. Nelle CTF i numeri in virgola mobile compaiono soprattutto nel *reversing* (istruzioni SSE, registri `xmm`) e in qualche sfida di *misc* che sfrutta gli arrotondamenti.

---

# Parte II — Il testo

## 7. ASCII

### 7.1 Un codice per i caratteri

Per conservare un testo in byte serve una **codifica dei caratteri** (*character encoding*): una tabella che associa a ogni carattere un numero, e una regola per scrivere quel numero in byte. La più importante della storia è **ASCII** (*American Standard Code for Information Interchange*, 1963): 128 caratteri, numerati da 0 a 127, cioè 7 bit. Ogni sistema moderno la contiene come sottoinsieme, e la tabella completa è sempre a un comando di distanza: `man ascii`.

### 7.2 La struttura della tabella

La tabella ASCII non è disordinata: è costruita con un criterio che vale la pena conoscere, perché permette di ricordarla quasi tutta.

| Intervallo | Contenuto |
|---|---|
| 0x00–0x1F (0–31) | **caratteri di controllo**, non stampabili |
| 0x20 (32) | lo **spazio** |
| 0x21–0x2F | punteggiatura `! " # $ % & ' ( ) * + , - . /` |
| 0x30–0x39 (48–57) | le **cifre** `0`–`9` |
| 0x3A–0x40 | `: ; < = > ? @` |
| 0x41–0x5A (65–90) | le **maiuscole** `A`–`Z` |
| 0x5B–0x60 | `[ \ ] ^ _ `` ` `` |
| 0x61–0x7A (97–122) | le **minuscole** `a`–`z` |
| 0x7B–0x7E | `{ | } ~` |
| 0x7F (127) | DEL, di controllo |

I punti di riferimento da memorizzare sono quattro: **0x20 spazio, 0x30 `'0'`, 0x41 `'A'`, 0x61 `'a'`**. Da questi si ricava il resto:

- la cifra *n* ha codice 0x30 + *n*: il valore di un carattere cifra è `c - '0'`, l'operazione che fa ogni funzione `atoi`;
- la *n*-esima lettera maiuscola (contando da 0) ha codice 0x41 + *n*: `'L'` è la dodicesima lettera, 0x41 + 11 = 0x4C;
- minuscola = maiuscola + 0x20, cioè lo stesso codice con il bit 5 acceso (§4.2);
- le parentesi graffe della flag, `{` e `}`, sono 0x7B e 0x7D.

I caratteri di controllo che incontrerai più spesso:

| Codice | Nome | Escape in C/bash | Note |
|---|---|---|---|
| 0x00 | NUL | `\0` | il terminatore delle stringhe C (§9.1) |
| 0x07 | BEL | `\a` | fa suonare il terminale |
| 0x08 | BS | `\b` | backspace |
| 0x09 | TAB | `\t` | tabulazione orizzontale |
| 0x0A | LF | `\n` | *line feed*: la fine della riga in Unix |
| 0x0D | CR | `\r` | *carriage return*: riporta il cursore a inizio riga |
| 0x1B | ESC | `\e`, `\033` | inizia le **sequenze di escape** del terminale (colori, movimento del cursore) |
| 0x04 | EOT | — | Ctrl-D: chi lo digita sul terminale chiede la fine dell'input (L5 §9.2) |

Il legame tra Ctrl e i caratteri di controllo è un'altra operazione sui bit: Ctrl più una lettera dà il codice della lettera con i bit 5 e 6 spenti, cioè `lettera & 0x1F`. Ctrl-C = `'C'` (0x43) & 0x1F = 0x03; Ctrl-D = 0x04; Ctrl-[ = 0x1B = ESC; Ctrl-J = 0x0A = a capo. Per questo il terminale mostra i caratteri di controllo come `^C`, `^D`, `^[` (L2 §2.3, `cat -A`).

### 7.3 Le estensioni a 8 bit

ASCII usa 7 bit, ma un byte ne ha 8: restavano libere 128 posizioni, da 0x80 a 0xFF. Negli anni '80 e '90 ogni regione le riempì a modo suo, producendo decine di codifiche incompatibili chiamate **code page**. Le più note in Europa occidentale sono **ISO-8859-1** (*Latin-1*), che contiene le lettere accentate dell'italiano (`è` = 0xE8, `à` = 0xE0), la sua variante **ISO-8859-15** (che aggiunge `€`), e **Windows-1252**, la versione Microsoft, che usa anche l'intervallo 0x80–0x9F per simboli come `€` (0x80) e le virgolette tipografiche. Lo stesso byte 0xE8 è `è` in Latin-1, `č` in Latin-2 (Europa centrale) e la lettera cirillica `Х` in KOI8-R (russo). Un file di testo, da solo, **non dice** in quale codifica è scritto. È la radice di tutti i problemi del §8.4.

## 8. Unicode, UTF-8 e UTF-16

### 8.1 Unicode: un numero per ogni carattere

**Unicode** risolve il problema alla radice: un unico catalogo di **tutti** i caratteri di tutte le scritture, più simboli, emoji e caratteri di controllo. A ogni carattere assegna un numero chiamato **punto di codice** (*code point*), scritto `U+` seguito da almeno quattro cifre esadecimali. I primi 128 punti coincidono con ASCII (`U+0041` è `A`), i primi 256 con Latin-1 (`U+00E9` è `é`). Lo spazio va da `U+0000` a `U+10FFFF`: poco più di un milione di posizioni, diviso in 17 **piani** da 65 536; il piano 0, il *Basic Multilingual Plane* (BMP), contiene quasi tutti i caratteri delle lingue moderne; le emoji, ad esempio `😀` = `U+1F600`, stanno nel piano 1.

Unicode dice **quale numero** ha un carattere, non **come** scriverlo in byte. Per questo esistono diverse **forme di codifica** (*encoding forms*): UTF-8, UTF-16, UTF-32.

### 8.2 UTF-8

**UTF-8**, inventata da Ken Thompson e Rob Pike nel 1992, è oggi la codifica di quasi tutto il testo del mondo: la usano Linux, il Web (oltre il 98% delle pagine), i file sorgente, i protocolli moderni. Usa da **1 a 4 byte** per carattere secondo questo schema (RFC 3629):

| Punti di codice | Byte | Schema dei bit |
|---|---|---|
| U+0000 – U+007F | 1 | `0xxxxxxx` |
| U+0080 – U+07FF | 2 | `110xxxxx 10xxxxxx` |
| U+0800 – U+FFFF | 3 | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10000 – U+10FFFF | 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

Le `x` sono i bit del punto di codice, distribuiti da sinistra a destra. Le proprietà che rendono UTF-8 così riuscita si leggono direttamente nella tabella:

1. **è compatibile con ASCII**: un testo ASCII è già un testo UTF-8 valido, byte per byte, e nessun byte di un carattere multi-byte è minore di 0x80. Un programma che cerca `/` o `\n` o NUL non può sbagliarsi;
2. **si sincronizza da sola**: il primo byte di un carattere inizia con `0` o `11`, i byte di continuazione con `10`; partendo da un byte qualunque si trova l'inizio del carattere successivo;
3. **la lunghezza è scritta nel primo byte**: il numero di 1 iniziali dice quanti byte ha il carattere.

Esempio a mano: `é` = U+00E9 = 1110 1001 (8 bit significativi) → serve la forma a 2 byte, che ha 11 bit disponibili: 000 1110 1001 → `110 00011` `10 101001` → **0xC3 0xA9**. E `€` = U+20AC = 0010 0000 1010 1100 → forma a 3 byte → `1110 0010` `10 000010` `10 101100` → **0xE2 0x82 0xAC**. Verifica con Python:

```python
>>> for s in ['A', 'é', '€', '😀']:
...     print(s, hex(ord(s)), s.encode('utf-8').hex(' '))
A 0x41 41
é 0xe9 c3 a9
€ 0x20ac e2 82 ac
😀 0x1f600 f0 9f 98 80
```

Una conseguenza pratica: in UTF-8 **il numero di byte non è il numero di caratteri**. `Città` sono 5 caratteri e 6 byte. `wc -c` conta i byte, `wc -m` i caratteri (ma solo se la *locale* del sistema è UTF-8: `locale` lo dice; con la locale `C` i due conteggi coincidono). In C `strlen` conta i byte; in Python `len` di una `str` conta i punti di codice, `len` di `bytes` i byte.

### 8.3 UTF-16, UTF-32 e il BOM

**UTF-16** usa unità da **2 byte**: i caratteri del BMP occupano un'unità, gli altri due (una **coppia surrogata**, *surrogate pair*, nell'intervallo riservato U+D800–U+DFFF). È la codifica interna di Windows, Java, JavaScript e .NET; per questo in JavaScript `"😀".length` vale 2. **UTF-32** usa sempre 4 byte per carattere: semplice ma dispendiosa, usata quasi solo internamente.

Poiché UTF-16 e UTF-32 usano unità di più byte, hanno il problema dell'ordine dei byte (§5): esistono UTF-16LE e UTF-16BE. Per distinguerle, un file può iniziare con il **BOM** (*Byte Order Mark*), il carattere U+FEFF, che in UTF-16LE si scrive `FF FE` e in UTF-16BE `FE FF`. Anche UTF-8 ha un "BOM", `EF BB BF`, inutile (UTF-8 non ha problemi di ordine) ma aggiunto da alcuni programmi Windows: è la causa di misteriosi errori di sintassi in script che "sembrano" iniziare con `#!` ma in realtà iniziano con tre byte invisibili.

Un testo ASCII scritto in UTF-16LE è riconoscibile a colpo d'occhio in un dump: **un byte NUL dopo ogni lettera**.

```
$ od -c ultimo.txt | head -1
0000000 377 376   s  \0   i  \0   g  \0   n  \0 ...
```

`cat` lo mostra quasi normalmente (il terminale ignora i NUL), ma `grep` non trova la parola cercata, perché i byte di `s\0i\0g\0n` non contengono la sequenza `sign`. È esattamente il quarto pezzo della mini-CTF. Si converte con **`iconv`**:

```
$ iconv -f UTF-16 -t UTF-8 ultimo.txt         # UTF-16 con BOM: l'ordine lo legge dal BOM
$ iconv -f UTF-16LE -t UTF-8 file.txt         # senza BOM, l'ordine va detto
$ iconv -f LATIN1 -t UTF-8 vecchio.txt
$ iconv -l | head                             # le codifiche supportate
$ file ultimo.txt                             # file prova a indovinare la codifica
ultimo.txt: Unicode text, UTF-16, little-endian text
```

Sui sistemi Windows le stringhe UTF-16 sono ovunque, anche negli eseguibili: per cercarle con `strings` serve l'opzione `-e l` (§11.3).

### 8.4 Quando la codifica è sbagliata: il *mojibake*

Se un testo viene scritto in una codifica e letto in un'altra, appare spazzatura, con un nome giapponese: **mojibake** (文字化け, "caratteri trasformati"). Il caso più comune in Italia: un testo UTF-8 letto come Latin-1 o Windows-1252. `è` (`C3 A8`) diventa `Ã¨`; `à` (`C3 A0`) diventa `Ã` seguito da uno spazio non separabile; `€` (`E2 82 AC`) diventa `â‚¬`. Il caso opposto, Latin-1 letto come UTF-8, produce il carattere sostitutivo `�` (U+FFFD), perché `E8` da solo non è una sequenza UTF-8 valida.

Riconoscere questi schemi permette di **ricostruire** il testo originale: se vedi `Ã¨`, la diagnosi è "UTF-8 interpretato come Latin-1", e la cura è ricodificare all'indietro:

```python
>>> 'CittÃ\xa0'.encode('latin-1').decode('utf-8')
'Città'
```

### 8.5 Caratteri uguali e diversi

Unicode introduce un problema che ASCII non aveva: **due sequenze diverse di punti di codice possono rappresentare lo stesso testo visibile**, e **due caratteri diversi possono sembrare identici**.

- **Composizione.** `é` si può scrivere come un solo punto di codice (U+00E9) o come `e` seguita dall'accento combinante (U+0065 U+0301). A schermo sono identiche; per un confronto di byte sono diverse. Per confrontare testo Unicode si **normalizza** prima (forme NFC, NFD, NFKC, NFKD):
  ```python
  >>> import unicodedata
  >>> a, b = 'é', 'é'
  >>> a == b, unicodedata.normalize('NFC', a) == b
  (False, True)
  ```
- **Omoglifi.** La `а` cirillica (U+0430) e la `a` latina (U+0061) sono indistinguibili in quasi tutti i caratteri tipografici. Un nome di dominio come `pаypal.com` scritto con la `а` cirillica è un indirizzo **diverso** da quello vero, e serve per il *phishing* (attacco *IDN homograph*). I browser lo mostrano nella forma *punycode* (`xn--...`) per difendersi.
- **Caratteri invisibili e di controllo della direzione.** Lo spazio a larghezza zero (U+200B), il *right-to-left override* (U+202E), e simili, alterano come un testo appare senza cambiarne il significato per un programma, o viceversa. Nel 2021 l'attacco *Trojan Source* (CVE-2021-42574) ha mostrato come nascondere codice malevolo in un sorgente che a un revisore umano sembra innocuo.

Per questo i programmi che confrontano testo Unicode (nomi utente, domini, parole chiave) devono normalizzarlo prima del confronto: `ａｄｍｉｎ`, scritto con lettere a larghezza piena, diventa `admin` dopo la normalizzazione NFKC.

## 9. Stringhe, righe e byte non stampabili

### 9.1 Come un programma sa dove finisce una stringa

Una stringa in memoria è una sequenza di byte. Per sapere dove finisce, i linguaggi usano due strategie.

- **Terminatore**: il C mette dopo l'ultimo carattere un byte **NUL** (0x00). `"ciao"` occupa 5 byte: `63 69 61 6f 00`. Ogni funzione che lavora sulle stringhe (`strlen`, `strcpy`, `printf("%s")`) procede finché non trova lo zero. Ne seguono due conseguenze fondamentali per la sicurezza: una stringa **non può contenere** un byte NUL (verrebbe troncata lì), e una stringa a cui **manca** il terminatore fa leggere o copiare oltre la fine del buffer. Nel Modulo 4, molti exploit falliscono perché l'indirizzo da scrivere contiene un byte `00`, che `strcpy` interpreta come la fine.
- **Lunghezza esplicita**: Python, Java, Go, Rust e la maggior parte dei formati binari conservano la lunghezza accanto ai dati. Queste stringhe possono contenere qualunque byte, NUL compreso.

Quando un programma scritto in un linguaggio con lunghezza esplicita passa una stringa a una funzione C, un NUL interno la **tronca**: le due parti del programma vedono stringhe diverse.

### 9.2 La fine della riga

Anche "andare a capo" ha più rappresentazioni, eredità delle telescriventi, dove il ritorno del carrello (CR) e l'avanzamento della carta (LF) erano due movimenti distinti:

| Sistema | Fine riga | Byte |
|---|---|---|
| Unix, Linux, macOS moderno | LF | `0A` |
| Windows, molti protocolli di rete (HTTP, SMTP) | CR LF | `0D 0A` |
| Mac OS classico (fino al 2001) | CR | `0D` |

Un file di testo creato su Windows, visto su Linux, ha un `\r` invisibile alla fine di ogni riga. Gli effetti tipici: uno script che fallisce con `/bin/bash^M: bad interpreter`, un confronto `[[ $riga == "ok" ]]` che non riesce mai (perché la riga è `ok\r`), un output che si sovrascrive da solo (perché `\r` riporta il cursore a inizio riga). Si diagnostica con `cat -A` (mostra `^M$`) o `file` (*with CRLF line terminators*), e si corregge con `dos2unix` o `tr -d '\r'` o `sed -i 's/\r$//'`.

```
$ printf 'riga1\r\nriga2\r\n' | od -c
0000000   r   i   g   a   1  \r  \n   r   i   g   a   2  \r  \n
```

Nelle sfide con un servizio di rete (Lezione 8) il CR è una trappola frequente: il server risponde con righe che finiscono in `\r\n`, e il tuo script che confronta con una stringa senza `\r` non trova mai una corrispondenza.

---

# Parte III — Codifiche e strumenti

## 10. Le codifiche di trasporto

### 10.1 Il problema: byte qualunque in un canale di testo

Molti canali accettano solo **testo stampabile**: un'email, un URL, un file di configurazione, un campo JSON, la riga di comando, un QR code, la chat di una gara. Ma spesso vogliamo trasportare **byte arbitrari**: un'immagine, una chiave, un binario, un dato cifrato. Una **codifica di trasporto** (*binary-to-text encoding*) trasforma una sequenza qualunque di byte in una sequenza di caratteri sicuri, in modo **reversibile** e **senza chiave**. Le principali sono quattro.

### 10.2 Esadecimale

La più semplice: ogni byte diventa due cifre esadecimali. Raddoppia la dimensione (efficienza 50%), ma si legge a occhio, ed è la forma in cui si scrivono hash, chiavi, indirizzi e *shellcode*.

```
$ printf 'Ciao' | xxd -p                 # da byte a hex
4369616f
$ echo 4369616f | xxd -r -p              # da hex a byte
Ciao
$ printf 'Ciao' | od -A n -t x1 | tr -d ' \n'; echo     # senza xxd
4369616f
$ python3 -c 'print(b"Ciao".hex(), bytes.fromhex("4369616f"))'
4369616f b'Ciao'
```

`xxd` fa parte del pacchetto di `vim` e non è installato ovunque (manca, ad esempio, nella macchina su cui sono stati provati questi esempi). Se non c'è, `od` e Python lo sostituiscono, come sopra; e per tornare dai byte esadecimali al testo basta anche `printf` con le sequenze `\x`: `printf "$(sed 's/../\\x&/g' <<< 4369616f)"`.

Varianti da riconoscere: `\x43\x69\x61\x6f` (stringa in C o Python), `%43%69` (codifica URL, §10.5), `0x43, 0x69` (array in C), `43:69:61:6f` (impronte di certificati e indirizzi MAC).

### 10.3 Base64

**Base64** (RFC 4648) usa un alfabeto di **64 caratteri**: `A–Z` (valori 0–25), `a–z` (26–51), `0–9` (52–61), `+` (62), `/` (63). Poiché 64 = 2⁶, ogni carattere porta **6 bit**. L'algoritmo:

1. prendi i byte a **gruppi di 3** (24 bit);
2. dividi i 24 bit in **4 gruppi da 6**;
3. sostituisci ogni gruppo con il carattere corrispondente dell'alfabeto.

Tre byte diventano quattro caratteri: la dimensione cresce di un terzo (efficienza 75%). Esempio a mano con `L7{`:

```
byte:     L          7          {
hex:      4C         37         7B
bit:      01001100   00110111   01111011
gruppi:   010011 | 000011 | 011101 | 111011
valori:   19       3        29       59
caratteri: T        D        d        7
```

`printf 'L7{' | base64` stampa infatti `TDd7`, ed è per questo che ogni flag `L7{...}` codificata in base64 inizia con `TDd7`, ogni `flag{` con `ZmxhZ3`, ogni `CTF{` con `Q1RGe`. Riconoscere questi inizi è un trucco da gara.

Se il numero di byte non è multiplo di 3, l'ultimo gruppo si completa con bit zero e il risultato si allunga con il carattere di **riempimento** `=`: un `=` finale significa che l'ultimo gruppo aveva 2 byte, `==` che ne aveva 1.

```
$ printf 'L7{' | base64; printf 'L7' | base64; printf 'L' | base64
TDd7
TDc=
TA==
```

Come riconoscere il base64 "a occhio": solo lettere, cifre, `+` e `/`; lunghezza multipla di 4; eventuali `=` solo alla fine. Esiste una variante **URL-safe** (`base64url`) che usa `-` e `_` al posto di `+` e `/` (che negli URL hanno un significato) e spesso omette il riempimento: è quella dei token JWT del Modulo 6.

```
$ printf 'Ciao, CTF!' | base64          # codifica
Q2lhbywgQ1RGIQ==
$ echo 'Q2lhbywgQ1RGIQ==' | base64 -d   # decodifica
Ciao, CTF!
$ base64 -w 0 immagine.png              # senza a capo ogni 76 caratteri
$ python3 -c 'import base64; print(base64.urlsafe_b64encode(b"\xfb\xff\xfe"), base64.b64encode(b"\xfb\xff\xfe"))'
b'-__-' b'+//+'
```

### 10.4 Base32 e altre

**Base32** usa 32 caratteri (`A–Z` e `2–7`), quindi 5 bit per carattere, gruppi di 5 byte in 8 caratteri, riempimento con `=` fino a sei. È meno efficiente (62,5%) ma non distingue maiuscole e minuscole ed evita caratteri ambigui: si usa dove una persona deve dettare o digitare il dato, ad esempio i segreti delle app di autenticazione a due fattori (TOTP).

```
$ printf 'Ciao, CTF!' | base32
INUWC3ZMEBBVIRRB
```

Riconoscerlo: solo maiuscole e cifre da 2 a 7, lunghezza multipla di 8, spesso molti `=`. Esistono anche **base85** (o Ascii85, più efficiente, usato nei PDF e in Git), **base58** (usato da Bitcoin, senza caratteri ambigui come `0`, `O`, `I`, `l`), **base36**, **base62**. Nelle sfide di *misc* capita di trovare una catena di codifiche diverse una dentro l'altra: lo strumento più comodo per provarle è **CyberChef** (§11.4).

### 10.5 La codifica URL

Negli URL alcuni caratteri hanno un significato speciale (`/`, `?`, `&`, `=`, `#`, lo spazio) e altri non sono ammessi. La **codifica percentuale** (*percent-encoding*, RFC 3986) sostituisce ogni byte "non sicuro" con `%` seguito da due cifre esadecimali: lo spazio diventa `%20`, `&` diventa `%26`, `è` (in UTF-8 `C3 A8`) diventa `%C3%A8`. Nei moduli HTML lo spazio si codifica anche come `+`.

```python
>>> import urllib.parse
>>> urllib.parse.quote('a b&c=d/è?')
'a%20b%26c%3Dd/%C3%A8%3F'
>>> urllib.parse.quote_plus('a b&c=d/è?')
'a+b%26c%3Dd%2F%C3%A8%3F'
>>> urllib.parse.unquote('%3Cscript%3E')
'<script>'
```

La userai continuamente nel Modulo 6 (sicurezza web). Attenzione alla **doppia codifica**: `%253C` decodificato una volta dà `%3C`, decodificato due volte dà `<`; un programma deve decodificare un numero di volte ben definito.

### 10.6 Codificare non è cifrare

È il punto concettuale più importante della Parte III, e vale la pena dirlo in modo netto: **una codifica non protegge niente**. Esadecimale, base64, base32, codifica URL, rot13: sono trasformazioni **pubbliche e senza chiave**, che chiunque può invertire in un istante. Tre operazioni vanno tenute distinte:

| Operazione | Reversibile? | Serve una chiave? | Scopo | Esempi |
|---|---|---|---|---|
| **codifica** | sì, da chiunque | no | trasportare o rappresentare | base64, hex, UTF-8, URL |
| **cifratura** | sì, solo con la chiave | sì | segretezza | AES, ChaCha20, RSA |
| **hash** | no | no (o sì, per un MAC) | integrità, impronte, password | SHA-256, yescrypt (L6) |

Un errore frequente nei programmi reali, e un'occasione nelle CTF, è trovare una password o un token "protetti" con base64: nell'autenticazione HTTP *Basic*, ad esempio, l'intestazione `Authorization: Basic emVuOnNlZ3JldG8=` contiene semplicemente `zen:segreto` in base64. Senza HTTPS, chiunque intercetti la richiesta legge la password. Le CWE corrispondenti sono la **CWE-261** (*Weak Encoding for Password*) e la **CWE-311** (*Missing Encryption of Sensitive Data*).

## 11. Gli strumenti per guardare dentro i file

### 11.1 Dump esadecimali: `xxd`, `od`, `hexdump`

Un **dump esadecimale** mostra il contenuto di un file byte per byte. Il formato canonico, quello di `xxd` e di `hexdump -C`, ha tre colonne: l'**offset** (la posizione nel file, in esadecimale), **16 byte** in esadecimale, e gli stessi byte come caratteri ASCII, con un punto al posto dei non stampabili.

```
$ printf 'ciao\0mondo\0\x01\x02segreto\n' | xxd
00000000: 6369 616f 006d 6f6e 646f 0001 0273 6567  ciao.mondo...seg
00000010: 7265 746f 0a                             reto.
```

Le opzioni di `xxd` da conoscere: `-l N` (solo N byte), `-s OFFSET` (da quella posizione; `-s -32` gli ultimi 32), `-c N` (N byte per riga), `-g N` (raggruppa a N byte), `-e` (little-endian, raggruppa e rovescia), `-p` (solo esadecimale continuo), `-r` (operazione inversa: da dump a byte), `-i` (output come array C), `-b` (in binario invece che in esadecimale).

Un uso potente di `xxd -r` è la **modifica di un file binario**: produci il dump, cambialo con un editor di testo o con `sed`, e ricostruisci il file.

```
$ xxd programma > dump.txt        # modifica dump.txt (attenzione a non cambiare la lunghezza)
$ xxd -r dump.txt > programma_patch
```

`od` (*octal dump*, L2 §2.3) è sempre presente, anche dove `xxd` non c'è; le sue opzioni principali: `-A x|d|o|n` (base dell'offset, o nessun offset), `-t x1` (byte in esadecimale), `-t c` (caratteri, con gli escape del C), `-t u4`, `-t d2`, `-t x8` (interi di 4, 2, 8 byte senza o con segno, nell'ordine della macchina), `--endian=big|little`, `-j N` (salta N byte), `-N N` (leggi N byte), `-v` (non comprimere le righe ripetute, che altrimenti diventano `*`). `hexdump -C` produce il formato canonico ed è comune su BSD e macOS.

### 11.2 `file`: che cos'è questo file?

`file` (L2 §2.4) non guarda l'estensione: legge i primi byte e li confronta con un database di **firme**, i *numeri magici* del §12. Opzioni utili: `-b` (solo la descrizione, senza il nome), `-i` (tipo MIME e codifica: `text/plain; charset=utf-8`), `-z` (guarda dentro i file compressi), `-s` (legge anche dispositivi a blocchi).

### 11.3 `strings`: il testo dentro i binari

`strings` stampa tutte le sequenze di almeno 4 caratteri stampabili consecutivi di un file. È spesso il primo comando da lanciare su un binario sconosciuto in una sfida di *reversing*: messaggi d'errore, nomi di funzioni, percorsi, a volte la flag stessa o un suo indizio.

```
$ strings programma | grep -i flag
$ strings -n 8 programma           # solo sequenze di almeno 8 caratteri
$ strings -t x programma           # con l'offset in esadecimale
$ strings -e l programma.exe       # stringhe UTF-16LE (Windows)
$ strings -a file                  # tutto il file, non solo alcune sezioni (default nelle versioni recenti)
```

Il limite di `strings` è evidente: trova solo il testo **in chiaro**. Una flag codificata in base64 compare come stringa (riconoscibile); una flag costruita carattere per carattere dal programma, o cifrata con uno XOR, no. Gli autori delle sfide lo sanno, e "la flag non è in `strings`" è la norma dalle sfide di livello intermedio in su.

### 11.4 Python e CyberChef

Per tutto ciò che va oltre una conversione, lo strumento è Python, che nella Lezione 8 diventerà il nostro linguaggio di lavoro. Le operazioni di base:

```python
>>> b = open('numeri.bin', 'rb').read()     # 'rb': byte, non testo
>>> b[:8]
b'\x00\x00\x00n\x00\x00\x00o'
>>> b[3], hex(b[3]), chr(b[3])               # un elemento di bytes è un intero
(110, '0x6e', 'n')
>>> s = 'Città'; s.encode('utf-8')           # str -> bytes
b'Citt\xc3\xa0'
>>> b'Citt\xc3\xa0'.decode('utf-8')          # bytes -> str
'Città'
>>> bytes(x ^ 0x2A for x in b'ciao')         # XOR byte per byte
>>> int('ff', 16), format(255, '08b'), f'{255:#x}'
(255, '11111111', '0xff')
```

La distinzione tra `str` (testo, una sequenza di punti di codice Unicode) e `bytes` (una sequenza di interi da 0 a 255) è il concetto più importante di Python 3 per chi lavora in sicurezza: i socket, i file binari e i processi parlano in `bytes`, e ogni conversione in `str` richiede una codifica esplicita.

**CyberChef** (gchq.github.io/CyberChef), sviluppato dall'agenzia britannica GCHQ, è un'applicazione web che concatena decine di operazioni (codifiche, decodifiche, XOR, compressione, hash, analisi) in una "ricetta" visuale. La sua funzione *Magic* prova automaticamente le codifiche più comuni. È lo strumento più usato per le sfide di codifica nelle gare; impara però a fare le stesse cose dalla riga di comando, perché non sempre avrai un browser, e perché uno script si può ripetere e automatizzare.

## 12. I formati dei file e i numeri magici

### 12.1 I numeri magici

Quasi ogni formato binario inizia con una sequenza fissa di byte, il **numero magico** (*magic number*) o **firma** (*file signature*), che permette di riconoscerlo indipendentemente dal nome. Quelli che devi riconoscere a colpo d'occhio in un dump:

| Formato | Primi byte (hex) | Come appaiono in ASCII |
|---|---|---|
| ELF (eseguibili Linux) | `7F 45 4C 46` | `.ELF` |
| PE (eseguibili Windows) | `4D 5A` | `MZ` |
| Mach-O (macOS, 64 bit) | `CF FA ED FE` | |
| script | `23 21` | `#!` |
| PNG | `89 50 4E 47 0D 0A 1A 0A` | `.PNG....` |
| JPEG | `FF D8 FF` | |
| GIF | `47 49 46 38 37 61` / `...39 61` | `GIF87a` / `GIF89a` |
| PDF | `25 50 44 46 2D` | `%PDF-` |
| ZIP (anche `.docx`, `.xlsx`, `.jar`, `.apk`) | `50 4B 03 04` | `PK..` |
| gzip | `1F 8B` | |
| bzip2 | `42 5A 68` | `BZh` |
| xz | `FD 37 7A 58 5A 00` | `.7zXZ.` |
| 7-Zip | `37 7A BC AF 27 1C` | `7z....` |
| tar | `75 73 74 61 72` all'offset 257 | `ustar` |
| classe Java | `CA FE BA BE` | |
| SQLite | `53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33 00` | `SQLite format 3.` |
| pcap (catture di rete) | `D4 C3 B2 A1` (little-endian) | |

```
$ head -c 4 /bin/ls | od -A n -t x1
 7f 45 4c 46
```

Molti formati hanno anche una **coda** riconoscibile: un PNG finisce con il blocco `IEND` (`49 45 4E 44 AE 42 60 82`), un JPEG con `FF D9`, uno ZIP con il record `PK\x05\x06` (la "directory centrale").

### 12.2 Perché conta nelle CTF

Nelle sfide di *forensics* e *misc* (Modulo 7) i numeri magici sono lo strumento principale, in tre situazioni tipiche:

1. **file con l'estensione sbagliata o senza estensione**: `file` o i primi byte rivelano che `documento.txt` è in realtà uno ZIP;
2. **firma danneggiata di proposito**: un PNG il cui primo byte è stato cambiato non si apre; riconoscere che il resto è un PNG e correggere la firma con un editor esadecimale lo rende di nuovo leggibile;
3. **file dentro altri file**: dati aggiunti dopo la fine di un'immagine, o un archivio nascosto dentro un altro file. Cercare le firme in tutto il file (`grep -obUaP '\x50\x4b\x03\x04' file` stampa l'offset di ogni inizio di ZIP; lo strumento `binwalk` lo fa in modo sistematico) e ritagliare con `dd` o `tail -c +OFFSET` permette di estrarli.

```
$ grep -obUaP 'PK\x03\x04' immagine.png      # -o solo la corrispondenza, -b offset, -U binario, -a come testo, -P regex Perl
40213:PK
$ tail -c +40214 immagine.png > nascosto.zip   # tail conta da 1: offset + 1
$ file nascosto.zip
nascosto.zip: Zip archive data, at least v2.0 to extract
```

---

# Parte IV — La pratica

## 13. Esempi svolti

### Esempio 1 — Una conversione completa a mano

Convertiamo 2024 in binario, esadecimale e ottale, e verifichiamo.

*Binario, per divisioni successive:* 2024 → 1012 r 0 → 506 r 0 → 253 r 0 → 126 r 1 → 63 r 0 → 31 r 1 → 15 r 1 → 7 r 1 → 3 r 1 → 1 r 1 → 0 r 1. Letti dal basso: **111 1110 1000**.

*Esadecimale, per gruppi di 4 bit da destra:* 0111 1110 1000 → 7 E 8 → **0x7E8**. Verifica: 7·256 + 14·16 + 8 = 1792 + 224 + 8 = 2024.

*Ottale, per gruppi di 3 bit da destra:* 011 111 101 000 → 3 7 5 0 → **03750**. Verifica: 3·512 + 7·64 + 5·8 = 1536 + 448 + 40 = 2024.

```
$ printf '%x %o\n' 2024 2024; echo 'obase=2; 2024' | bc
7e8 3750
11111101000
```

### Esempio 2 — Leggere un intero da un dump

Un file contiene questi 8 byte:

```
$ xxd dati.bin
00000000: e807 0000 ffff ffff                      ........
```

Che cosa contiene, se sappiamo che sono due interi a 32 bit scritti da una macchina x86?

- Primi 4 byte, `e8 07 00 00`: in little-endian il byte più significativo è l'ultimo, quindi il valore è 0x000007E8 = **2024** (Esempio 1).
- Secondi 4 byte, `ff ff ff ff`: 0xFFFFFFFF, cioè 4 294 967 295 se senza segno, **−1** se con segno (§3.3).

```
$ od -A n -t u4 dati.bin; od -A n -t d4 dati.bin
       2024 4294967295
       2024         -1
$ python3 -c 'import struct; print(struct.unpack("<Ii", open("dati.bin","rb").read()))'
(2024, -1)
```

Se avessimo letto i primi 4 byte in big-endian avremmo ottenuto 0xE8070000 = 3 892 772 864: il valore "rotondo e enorme" del §5.4 che segnala l'ordine sbagliato.

### Esempio 3 — Il complemento a due di −100 in 8 e 16 bit

+100 = 64 + 32 + 4 = 0110 0100. Invertiamo: 1001 1011. Aggiungiamo 1: **1001 1100** = 0x9C. Verifica con i pesi: −128 + 16 + 8 + 4 = −100.

In 16 bit, per estensione del segno: 1111 1111 1001 1100 = **0xFF9C**. Come senza segno, 0x9C = 156 = 256 − 100 e 0xFF9C = 65 436 = 65 536 − 100, come previsto dal §3.2.

```
$ printf '%02x %04x\n' $(( -100 & 0xFF )) $(( -100 & 0xFFFF ))
9c ff9c
$ python3 -c 'print((-100).to_bytes(2, "big", signed=True).hex(), int.from_bytes(b"\x9c", "big", signed=True))'
ff9c -100
```

### Esempio 4 — Codificare a mano in UTF-8

Codifichiamo `ñ` (U+00F1) e `→` (U+2192).

- U+00F1 = 1111 0001, 8 bit significativi: serve la forma a 2 byte (11 bit). 000 1111 0001 → `110 00011` `10 110001` → **C3 B1**.
- U+2192 = 0010 0001 1001 0010, 14 bit: forma a 3 byte (16 bit). 0010 000110 010010 → `1110 0010` `10 000110` `10 010010` → **E2 86 92**.

```
$ printf 'ñ→' | od -A n -t x1
 c3 b1 e2 86 92
```

Nota che entrambi i caratteri iniziano con un byte ≥ 0xC0 (uno o più 1 seguiti da 0) e proseguono con byte tra 0x80 e 0xBF (`10xxxxxx`): è lo schema che permette di riconoscere UTF-8 in un dump.

### Esempio 5 — Una catena di codifiche

Una sfida fornisce questa stringa: `NDM2OTYxNmYyMDZkNmY2ZTY0NmY=`. Ragioniamo:

1. lettere, cifre, lunghezza 28 (multiplo di 4), `=` finale: è **base64**. Decodifichiamo: `4369616f206d6f6e646f`;
2. solo cifre e lettere da `a` a `f`, lunghezza pari: è **esadecimale**. Decodifichiamo:

```
$ echo NDM2OTYxNmYyMDZkNmY2ZTY0NmY= | base64 -d; echo
4369616f206d6f6e646f
$ echo NDM2OTYxNmYyMDZkNmY2ZTY0NmY= | base64 -d | xxd -r -p; echo
Ciao mondo
```

Il risultato è testo leggibile: ci fermiamo. Il metodo generale è questo: **osserva l'alfabeto e la lunghezza, scegli la codifica più probabile, decodifica, ripeti finché il risultato non è testo sensato** (o un formato riconoscibile dai numeri magici). Con Python la catena si scrive in una riga: `bytes.fromhex(base64.b64decode(s).decode())`.

### Esempio 6 — Riconoscere e riparare un file

Un file `foto` non si apre. Guardiamo i primi byte:

```
$ file foto
foto: data
$ xxd -l 16 foto
00000000: 0050 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

`file` non lo riconosce, ma i byte da 1 a 7 sono quelli della firma PNG (§12.1) e subito dopo compare `IHDR`, il primo blocco di ogni PNG. Il primo byte dovrebbe essere `89` ed è stato azzerato. Ripariamolo scrivendo un solo byte all'offset 0, senza toccare il resto (`conv=notrunc` impedisce a `dd` di troncare il file):

```
$ printf '\x89' | dd of=foto bs=1 seek=0 count=1 conv=notrunc
$ file foto
foto: PNG image data, 640 x 480, 8-bit/color RGBA, non-interlaced
```

Le dimensioni 640 × 480 vengono dai campi dell'intestazione `IHDR`: due interi a 32 bit **big-endian** (PNG usa l'ordine della rete) che seguono `IHDR`: `00 00 02 80` = 640 e `00 00 01 e0` = 480.

## 14. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire `Soluzioni.md`. Le prime volte fai le conversioni **a mano** e poi verifica con gli strumenti. Lavora in una directory di prova (`mkdir ~/l7 && cd ~/l7`).

### ★ Base

1. **Conversioni.** A mano, poi verifica: (a) 0b1101 0110 in decimale ed esadecimale; (b) 0xC4 in decimale e binario; (c) 201 in binario, esadecimale e ottale; (d) 0o755 in binario (e che cosa significa come permesso?); (e) ordina dal più piccolo al più grande: 0x3F, 61, 0b111111, 0o77.
2. **ASCII.** Senza consultare la tabella (usa i punti di riferimento del §7.2): (a) qual è il codice esadecimale di `C`, `c`, `7`, `{`, spazio? (b) Che carattere è 0x6A? E 0x2D? (c) Scrivi `L7` come due byte esadecimali. (d) Verifica tutto con `printf '%d' "'C"` e con `man ascii`.
3. **Byte in chiaro.** Crea un file con `printf 'Flag: L7{...}\nriga2\r\n\t fine' > prova.txt`. Mostralo con `od -c`, con `xxd` (o `od -A x -t x1z`), e con `cat -A`. Individua il byte di ogni carattere di controllo. Quanti byte occupa il file? Perché `wc -l` e il numero di `\n` possono non coincidere?
4. **Codifiche.** (a) Codifica `Modulo 1` in base64 e in esadecimale. (b) Decodifica `aGFja2luZw==` e `0x70776e`. (c) La stringa `U0VHUkVUTw==` che cosa nasconde, e perché "nascondere" è la parola sbagliata? (d) Codifica in percentuale la stringa `a=1 & b=2/3`.
5. **Endianness.** Il file di 4 byte `44 33 22 11`: che intero rappresenta letto in little-endian? E in big-endian? Verifica con `od -t x4` e `od -t x4 --endian=big`. Poi crea con `printf` un file che contiene l'intero 0x01020304 scritto in little-endian, e controllalo.

### ★★ Intermedio

6. **Complemento a due.** A mano, in 8 bit: (a) la rappresentazione di −1, −128, −64, −50; (b) che valore con segno rappresenta 0xB0? e 0x7F? (c) perché −128 non ha un opposto rappresentabile in 8 bit? (d) in 32 bit, scrivi in esadecimale −1 e −256, e verifica con `printf '%x' $(( -1 & 0xFFFFFFFF ))`.
7. **Operazioni sui bit.** (a) Calcola a mano `0xA5 & 0x0F`, `0xA5 | 0x50`, `0xA5 ^ 0xFF`, `~0xA5` (in 8 bit). (b) Scrivi un'espressione `$(( ))` che, dato un carattere in `c=$(printf '%d' "'A")`, lo trasformi nella minuscola; un'altra che scambi maiuscolo e minuscolo. (c) Con una maschera, estrai il terzo byte (contando da 0) di 0x11223344.
8. **XOR.** (a) Verifica a mano che `'A' ^ 0x20` dà `'a'`. (b) In Python, cifra la parola `ciao` con la chiave di un byte 0x42 (XOR), mostra il risultato in esadecimale, poi decifralo. (c) Ti do il cifrato (esadecimale) `166d3531` e so che il chiaro inizia con `L7`: ricava i primi due byte della chiave, e se la chiave è di 1 byte ripetuto, l'intero chiaro.
9. **Testo e codifiche.** (a) Scrivi `Perché?` in un file UTF-8 e mostra con `od -c` i byte di `é`. (b) Converti quel file in Latin-1 con `iconv` e confronta i byte. (c) Crea di proposito del *mojibake*: in Python prendi i byte UTF-8 di `città` e decodificali come Latin-1 (`.decode('latin-1')`); poi ricostruisci l'originale come nel §8.4. (d) Perché `grep città` non trova una riga scritta in UTF-16?
10. **Dump e riparazione.** Ti do (nella sfida, o costruiscilo tu con `printf`) un file i cui primi byte sono `FF D8 FF E0 00 10 4A 46 49 46`: che formato è (usa la tabella del §12.1)? Scrivi il comando `dd` che cambierebbe il terzo byte in 0xAA senza alterare la lunghezza, e quello che estrae i byte dal 7° in poi.
11. **I numeri magici.** Scrivi uno script `tipo.sh FILE` che, **senza usare `file`**, legge i primi byte con `od` e stampa il formato probabile tra PNG, JPEG, GIF, PDF, ZIP, ELF, gzip, in base alla firma. Provalo su alcuni file del sistema (`/bin/ls`, un'immagine, un `.gz` in `/usr/share/doc`).
12. **Base64 a mano.** (a) Codifica `Go!` in base64 a mano (3 byte → 4 caratteri), mostrando i gruppi di 6 bit, e verifica. (b) Perché `base64` di un file di 1000 byte produce 1336 caratteri (più un a capo ogni 76, se non usi `-w 0`)? (c) Che cosa significano uno e due `=` alla fine? (d) Dato `TDd7YWJjfQ==`, senza eseguirlo di' da quanti byte è il dato originale e come inizia.

### ★★★ Sfida

13. **Simulare i tipi del C in Python.** Gli interi di Python non hanno limiti, ma spesso serve imitare un tipo a dimensione fissa. (a) Scrivi `a_senza_segno(x, bit)` che restituisce `x` ridotto a `bit` bit (con una maschera). (b) Scrivi `a_con_segno(x, bit)` che interpreta quei bit in complemento a due (se il bit più alto è 1, sottrai 2^bit). (c) Verifica: `a_con_segno(0xFF, 8)` = −1, `a_con_segno(0x80000000, 32)` = −2147483648, `a_senza_segno(-1, 16)` = 65535. (d) Usa le funzioni per mostrare che `200 + 100` in 8 bit dà 44 e che `0x7FFFFFFF + 1` in 32 bit con segno dà il minimo negativo.
14. **Mini-CTF.** Nella cartella di questa lezione c'è `setup_sfida.sh`. Eseguilo con `bash setup_sfida.sh`: crea `~/l7_sfida` con quattro file, ognuno con un pezzo della flag `L7{...}` in una rappresentazione diversa. **Non leggere il codice dello script**: leggi `LEGGIMI.txt` e decodifica ogni pezzo con gli strumenti di questa lezione.
15. **Rompere uno XOR a chiave ripetuta.** Nella sfida (o costruiscilo: cifra un testo italiano lungo con una chiave di 3 byte) ti viene dato un file cifrato con XOR e una chiave di lunghezza ignota ma breve. (a) Sapendo che il testo è ASCII e inizia con una parola nota, ricava la chiave. (b) Se non conosci l'inizio, come stimeresti la lunghezza della chiave e come la ricaveresti, sfruttando il fatto che il byte più frequente di un testo è lo spazio (0x20)? (Non serve il codice completo: descrivi il metodo.)
16. **Un formato binario fatto a mano.** Progetta e scrivi, con `printf` o Python, un file che rispetti questo mini-formato: magic `CTF1` (4 byte), un intero a 32 bit **big-endian** con la lunghezza del nome, il nome (ASCII), un intero a 16 bit **little-endian** con un punteggio. Poi scrivi lo *script di lettura* in Python (`struct.unpack`) che lo ristampa in chiaro. Che cosa succede se leggi il punteggio in big-endian?
17. **Teoria.** Rispondi in modo argomentato: (a) perché l'esadecimale è più usato dell'ottale oggi, mentre i permessi Unix usano l'ottale? (b) Elenca tre proprietà che rendono UTF-8 superiore alle code page e a UTF-16 per il testo di Internet. (c) Spiega a un compagno la differenza tra codificare, cifrare e fare l'hash di una password, con un esempio concreto di errore per ciascuna confusione.

### Allenamento

Le sfide di questa lezione sono soprattutto di tipo **misc** e **crypto introduttivo**. Su pwn.college fai tutti i livelli del modulo *Dealing with Data* del corso CSE 365, che segue le lezioni *Dealing with Data 1–6* su cui è costruita questa lezione; il modulo *Cryptography* inizia proprio dallo XOR. Fuori da pwn.college, cerca sfide di "encoding", "base64", "xor" su piattaforme come picoCTF (categoria *General Skills* e *Cryptography*): sono il terreno ideale per esercitare questa lezione. Tieni aperto **CyberChef** e, accanto, prova a ottenere lo stesso risultato da riga di comando.

## 15. Domande di autoverifica

1. Perché l'esadecimale corrisponde così bene al binario, e l'ottale ai permessi?
2. Quanti valori rappresenta un byte? Qual è il massimo di un intero senza segno a 32 bit, in decimale e in esadecimale?
3. Che cos'è l'aritmetica modulo 2ⁿ? Che cosa succede a un `uint8` che vale 255 e viene incrementato?
4. Spiega il complemento a due. Perché la somma funziona uguale per numeri con e senza segno?
5. Gli stessi 32 bit `0x80000000`: quanto valgono con e senza segno?
6. Che cos'è l'endianness? In che ordine stanno in memoria, su x86, i byte dell'intero 0x41424344?
7. Che cos'è lo XOR e quali sue proprietà lo rendono utile in crittografia? Come si ricava la chiave da chiaro e cifrato noti?
8. Com'è fatta la tabella ASCII? Quali sono i codici di `0`, `A`, `a`, spazio?
9. Come codifica UTF-8 un carattere? Perché è compatibile con ASCII e come si riconosce in un dump?
10. Qual è la differenza tra `str` e `bytes`? Perché `len` può dare un numero diverso dal numero di byte?
11. Come funziona il base64? Perché la dimensione cresce di un terzo? Che cosa indicano gli `=`?
12. Qual è la differenza tra codificare, cifrare e fare l'hash? Perché il base64 non protegge una password?
13. Che cos'è un numero magico? Nomina le firme di ELF, PNG, ZIP, PDF.
14. Quali strumenti usi per: vedere i byte di un file, sapere che formato è, estrarre il testo, convertire una codifica?

## 16. Riepilogo

- Un **numero posizionale** in base *b* usa cifre 0…*b*−1. In informatica contano il **binario** (l'hardware), l'**esadecimale** (4 bit per cifra, per leggere i byte), l'**ottale** (3 bit, per i permessi). Conversioni: a mano per divisioni/sottrazioni successive, con gli strumenti `$(( ))`, `printf`, `bc`, Python.
- Un **byte** sono 8 bit. Un intero senza segno di *n* bit va da 0 a 2ⁿ−1; l'aritmetica è **modulo 2ⁿ** e può fare il **giro** (overflow).
- Il **complemento a due** rappresenta i negativi dando peso −2ⁿ⁻¹ al bit più alto; negare = invertire i bit e aggiungere 1. **Gli stessi bit valgono numeri diversi** secondo l'interpretazione con o senza segno: è il titolo della flag.
- Le **operazioni sui bit** (AND, OR, XOR, NOT, scorrimenti) e le **maschere** leggono e modificano singoli bit. Lo **XOR** è autoinverso: *m*⊕*k*⊕*k* = *m*, e *m*⊕*c* = *k*.
- L'**endianness** è l'ordine dei byte di un numero: x86 è **little-endian**, la rete è **big-endian**. Sbagliarlo dà valori enormi e "rotondi".
- Il **testo** è byte interpretati con una codifica. **ASCII** (7 bit) è la base; **Unicode** dà un numero a ogni carattere; **UTF-8** (1–4 byte, compatibile con ASCII) è lo standard; **UTF-16** (2 byte, NUL sparsi) è di Windows. Problemi tipici: *mojibake*, BOM, CR/LF, caratteri ingannevoli.
- Le **codifiche di trasporto** (hex, base64, base32, URL) portano byte qualunque in un canale di testo, in modo pubblico e reversibile: **non sono cifratura**.
- Gli **strumenti**: `xxd`/`od`/`hexdump` (dump), `file` (formato), `strings` (testo nei binari), `iconv` (codifiche), Python (`bytes`/`str`, `struct`), CyberChef. I **numeri magici** identificano i formati; `binwalk`, `dd` e `tail -c` estraggono file dentro file.

## 17. Fonti

- **R. E. Bryant, D. R. O'Hallaron**, *Computer Systems: A Programmer's Perspective*, cap. 2 (*Representing and Manipulating Information*): bit e byte, interi con e senza segno, complemento a due, overflow, operazioni sui bit, byte order, numeri in virgola mobile. È il riferimento principale di questa lezione.
- **pwn.college**, CSE 365, lezioni *Dealing with Data 1–6* (trascrizioni 079–084: *Binary Data*, *Hex*, *Encoding Text*, *Playing with Encodings*, *Base64*, *Gleaning Challenge Insight*) e il modulo di esercizi *Dealing with Data*; l'inizio del dojo *Cryptography* per lo XOR.
- **Standard e specifiche**: *The Unicode Standard* (sezioni introduttive e sulle forme di codifica); RFC 3629 (UTF-8), RFC 4648 (base16/32/64), RFC 3986 (URI e percent-encoding); IEEE 754 (virgola mobile).
- **Danny Cohen**, *On Holy Wars and a Plea for Peace* (1980), l'articolo che ha dato i nomi *big-endian* e *little-endian*.
- **Joel Spolsky**, *The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets* (2003): l'introduzione a Unicode più citata.
- **Pagine di manuale**: `ascii(7)`, `utf-8(7)`, `charsets(7)`, `od(1)`, `xxd(1)`, `hexdump(1)`, `strings(1)`, `file(1)`, `iconv(1)`, `base64(1)`, `base32(1)`, `printf(1)` e `printf(3)`.
- **Strumenti**: CyberChef (gchq.github.io/CyberChef) e la sua documentazione; `binwalk` per l'analisi dei formati.
- **MITRE CWE**: CWE-261 e CWE-311 (codifica scambiata per protezione), CWE-176 (gestione scorretta dell'Unicode).

## 18. Prossima lezione

**Lezione 8 — Python per interagire con i programmi**: dalla riga di comando allo script, i tipi di Python per la sicurezza (`bytes` contro `str`, numeri, liste, dizionari), leggere e scrivere file binari, eseguire altri programmi, e soprattutto **pwntools**: `process`, `remote`, `recv`/`send`, `p32`/`p64` (che oggi abbiamo anticipato), per dialogare con un servizio locale o remoto. È la lezione che unisce tutto il Modulo 1 e apre la porta alle sfide *pwn*.
