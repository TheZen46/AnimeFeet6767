---
corso: Architettura dei Calcolatori
modulo: 3
titolo: L'ALU e l'aritmetica del calcolatore
programma: [ADC-03]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 3 · L'ALU e l'aritmetica del calcolatore

**In questo modulo.** Si usano il sommatore e il complemento a 2 delle reti logiche e le istruzioni del modulo 1 (*Astrazione, prestazioni e l'ISA RISC-V*). Si costruisce passo per passo l'unità aritmetico-logica che esegue le istruzioni RISC-V: prima un bit, poi 32, con la sottrazione, il confronto `slt`, il test di zero e il rilevamento dell'overflow. Poi si vede come rendere veloce la somma con il calcolo anticipato del riporto, e come si fanno in hardware la moltiplicazione (anche con l'algoritmo di Booth) e la divisione. La terza parte è la virgola mobile IEEE 754, con gli algoritmi di somma e prodotto. Chiudono i codici di Hamming, che proteggono i dati in memoria dagli errori. Alla fine del modulo si sanno eseguire a mano tutti gli algoritmi e spiegare l'hardware che li realizza.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (Arithmetic Logic Unit, Codici di Hamming); Patterson e Hennessy, *Struttura e progetto dei calcolatori*, edizione RISC-V, cap. 3 e appendice A (ADC-03)
> Il modulo è scritto in revisione dal materiale del corso; ogni algoritmo è svolto su un esempio controllato con `strumenti/verifica_ampliamento.py`.

## 3.1 L'ALU a un bit

L'ALU deve eseguire le operazioni dell'ISA sugli interi: `and`, `or`, somma, sottrazione, confronto. Si comincia da un solo bit. Con gli ingressi $a$ e $b$ si calcolano in parallelo $a \cdot b$, $a + b$ (OR) e la somma con un full adder, che ha anche il riporto in ingresso $c_{in}$ e quello in uscita $c_{out}$. Un multiplexer comandato dal segnale **Operation** sceglie quale risultato portare in uscita.

La sottrazione non richiede un circuito nuovo: in complemento a 2, $a - b = a + \bar b + 1$. Si aggiunge un multiplexer che sceglie fra $b$ e $\bar b$ (segnale **Binvert**), e per il "+1" si mette a 1 il riporto in ingresso del bit 0. Con un secondo multiplexer su $a$ (**Ainvert**) e le leggi di De Morgan si ottiene anche la NOR: $\overline{a + b} = \bar a \cdot \bar b$.

## 3.2 L'ALU a 32 bit

Mettendo in fila 32 ALU a un bit, con il $c_{out}$ di ognuna collegato al $c_{in}$ della successiva, si ottiene un sommatore a propagazione del riporto (*ripple carry*) che sa anche fare AND, OR, NOR e sottrazione. Servono tre aggiunte.

**`slt`.** Il risultato è 1 se $a < b$ e 0 altrimenti, cioè un numero con tutti i bit a 0 tranne forse il bit 0. Si calcola $a - b$: se il risultato è negativo, $a < b$. Ogni ALU a un bit ha un ingresso in più, **Less**, selezionato come quarta scelta del multiplexer: per i bit da 1 a 31 Less vale 0; per il bit 0 Less è collegato al bit di segno della sottrazione calcolato dall'ALU del bit 31 (un'uscita apposita, **Set**). Attenzione: se la sottrazione va in overflow il bit di segno è sbagliato, e il valore giusto è $\text{Set} \oplus \text{Overflow}$.

**Zero.** Per i salti `beq` e `bne` serve sapere se $a - b = 0$: è la NOR di tutti i 32 bit del risultato, $\text{Zero} = \overline{r_{31} + \dots + r_0}$.

**Overflow.** In complemento a 2 c'è overflow quando il riporto che entra nel bit di segno è diverso da quello che ne esce, $V = c_{31} \oplus c_{32}$: succede solo sommando due numeri dello stesso segno (o sottraendo numeri di segno opposto). RISC-V non segnala l'overflow con un'eccezione: se serve, il programma lo controlla con un confronto.

Il controllo dell'ALU usa quattro bit: Ainvert, Binvert (che comanda anche il riporto in ingresso del bit 0) e i due bit di Operation.

| Controllo ALU | Funzione |
|---|---|
| 0000 | AND |
| 0001 | OR |
| 0010 | somma |
| 0110 | sottrazione |
| 0111 | `slt` |
| 1100 | NOR |

## 3.3 Il calcolo anticipato del riporto

Nel sommatore ripple il riporto attraversa tutti gli stadi, e il ritardo cresce con il numero di bit. Per rendere la somma veloce bisogna calcolare i riporti senza aspettare. Dalla tabella del full adder, $c_{i+1} = a_i b_i + (a_i + b_i)c_i$. Si definiscono per ogni bit

$$g_i = a_i b_i \quad \text{(generazione)}, \qquad p_i = a_i + b_i \quad \text{(propagazione)},$$

perché lo stadio $i$ *genera* un riporto se $a_i = b_i = 1$, qualunque sia $c_i$, e *propaga* il riporto in arrivo se almeno uno dei due bit vale 1. Allora $c_{i+1} = g_i + p_i c_i$, e sostituendo all'indietro:
$$c_1 = g_0 + p_0 c_0, \qquad c_2 = g_1 + p_1 g_0 + p_1 p_0 c_0,$$
$$c_3 = g_2 + p_2 g_1 + p_2 p_1 g_0 + p_2 p_1 p_0 c_0, \qquad c_4 = g_3 + p_3 g_2 + p_3 p_2 g_1 + p_3 p_2 p_1 g_0 + p_3 p_2 p_1 p_0 c_0.$$
Ogni riporto è una rete a due livelli in $g$, $p$ e $c_0$: tutti i riporti sono pronti dopo lo stesso tempo (**carry lookahead**). Il prezzo è che le espressioni crescono rapidamente; per 32 bit si raggruppano i bit a blocchi di 4, ciascuno con il suo $G$ e $P$ di blocco ($P_0 = p_3 p_2 p_1 p_0$, $G_0 = g_3 + p_3 g_2 + p_3 p_2 g_1 + p_3 p_2 p_1 g_0$), e si applica lo stesso schema ai blocchi.

## 3.4 La moltiplicazione

Il prodotto di due numeri di $n$ bit ha fino a $2n$ bit. L'algoritmo è quello in colonna: per ogni bit a 1 del moltiplicatore si somma il moltiplicando spostato. L'hardware delle slide del corso (*add and right shift*) usa un registro prodotto di $2n$ bit: all'inizio la metà alta vale 0 e la metà bassa contiene il moltiplicatore. A ogni passo, se il bit meno significativo del registro è 1 si somma il moltiplicando alla metà alta; poi si sposta tutto il registro di un bit a destra. Dopo $n$ passi il registro contiene il prodotto. Serve un solo sommatore di $n$ bit.

Per i numeri con segno si può moltiplicare i valori assoluti e sistemare il segno alla fine, oppure usare l'**algoritmo di Booth**. L'idea è che una sequenza di 1 nel moltiplicatore si può sostituire con una sottrazione e una somma: $0110 = 1000 - 0010$, quindi $m \times 0110 = m \times 1000 - m \times 0010$. Si guarda la coppia formata dal bit corrente del moltiplicatore e dal bit alla sua destra (all'inizio un bit aggiuntivo $q_{-1} = 0$):

| $q_0\ q_{-1}$ | Operazione | Significato |
|---|---|---|
| 1 0 | $A = A - M$ | inizio di una sequenza di 1 |
| 1 1 | nessuna | in mezzo alla sequenza |
| 0 1 | $A = A + M$ | fine della sequenza |
| 0 0 | nessuna | in mezzo a una sequenza di 0 |

e dopo ogni operazione si fa uno shift **aritmetico** a destra (che conserva il segno) di $A$, $Q$ e $q_{-1}$ insieme. Funziona direttamente in complemento a 2.

In RISC-V la moltiplicazione è nell'estensione M: `mul rd, rs1, rs2` dà i 32 bit bassi del prodotto, `mulh` (con segno) e `mulhu` (senza segno) quelli alti; per sapere se un prodotto sta in 32 bit si guarda la parte alta.

## 3.5 La divisione

La divisione si fa con sottrazioni e shift, come quella in colonna: $\text{dividendo} = \text{quoziente} \times \text{divisore} + \text{resto}$, con $0 \le \text{resto} < \text{divisore}$. A ogni passo si prova a sottrarre il divisore (allineato) dal resto parziale: se il risultato è $\ge 0$ il bit del quoziente è 1 e si tiene la sottrazione; se è negativo il bit è 0 e si ripristina il resto (algoritmo *restoring*). In hardware il divisore sta nella metà alta di un registro di $2n$ bit e scorre a destra di un bit a ogni passo, mentre il quoziente si forma a sinistra. A differenza della moltiplicazione, i passi non si possono fare in parallelo, perché ognuno dipende dal segno del precedente: per questo la divisione è l'operazione intera più lenta. In RISC-V: `div`, `divu`, `rem`, `remu`; la divisione per zero non genera eccezioni ma dà un risultato convenzionale (quoziente con tutti i bit a 1).

## 3.6 La virgola mobile

Il formato IEEE 754 è spiegato nel modulo 2 di Reti Logiche; qui si ricorda l'essenziale e si vedono le operazioni. Un numero normalizzato in singola precisione è
$$(-1)^s \times (1 + F) \times 2^{E - 127},$$
con 1 bit di segno, 8 di esponente in eccesso 127 e 23 di frazione $F$ (il bit 1 prima della virgola è nascosto). In doppia precisione l'esponente ha 11 bit (eccesso 1023) e la frazione 52. Si ha **overflow** quando l'esponente supera il massimo rappresentabile, **underflow** quando un numero diverso da 0 è più piccolo del minimo normalizzato; i valori con esponente tutto a 0 e tutto a 1 sono riservati a zero, denormalizzati, infiniti e NaN.

**Somma.** (1) Si confrontano gli esponenti e si sposta a destra la mantissa del numero con l'esponente minore, finché gli esponenti sono uguali. (2) Si sommano le mantisse (con il segno). (3) Si normalizza il risultato, spostando la mantissa e correggendo l'esponente, e si controlla overflow o underflow. (4) Si arrotonda ai bit disponibili; se l'arrotondamento denormalizza il risultato, si torna al passo 3.

**Prodotto.** (1) Si sommano gli esponenti *veri*: con gli esponenti in eccesso bisogna togliere un 127, perché $(E_1 + 127) + (E_2 + 127) = (E_1 + E_2 + 127) + 127$. (2) Si moltiplicano le mantisse. (3) Si normalizza e si controlla overflow e underflow. (4) Si arrotonda. (5) Il segno è lo XOR dei segni.

Per arrotondare bene l'hardware tiene, durante i calcoli, due bit in più a destra (**guard** e **round**) e un bit **sticky** che vale 1 se qualcuno dei bit scartati era 1. Il modo di arrotondamento standard è al più vicino, e in caso di pareggio al pari.

## 3.7 Rilevare e correggere gli errori: i codici di Hamming

Un bit in memoria o su un canale può cambiare per un disturbo. La **distanza di Hamming** fra due sequenze di bit della stessa lunghezza è il numero di posizioni in cui differiscono: $d(1011, 1110) = 2$. La distanza di un codice è la minima distanza fra due parole valide. Con distanza $d$ si possono rilevare fino a $d - 1$ errori, oppure correggerne fino a $\left\lfloor \frac{d - 1}{2} \right\rfloor$: con $d = 2$ (il bit di parità) si rileva un errore singolo, con $d = 3$ lo si corregge, con $d = 4$ si corregge un errore e se ne rilevano due.

Per correggere un errore su $M$ bit di dati si aggiungono $K$ bit di controllo, che insieme devono indicare se non c'è errore o in quale delle $M + K$ posizioni è avvenuto. Servono quindi
$$2^K \ge M + K + 1.$$
Per $M = 4$ basta $K = 3$ (codice di Hamming (7, 4)); per $M = 8$, $K = 4$; per $M = 16$, $K = 5$; per $M = 32$, $K = 6$; per $M = 64$, $K = 7$. La frazione di bit di controllo diminuisce al crescere di $M$.

**Costruzione.** Si numerano le posizioni da 1: i bit di controllo vanno nelle posizioni potenze di 2 (1, 2, 4, 8, …), i dati nelle altre. Il bit di controllo in posizione $2^j$ è la parità (pari) delle posizioni il cui numero, in binario, ha il bit $j$ a 1: il bit 1 controlla le posizioni 1, 3, 5, 7, …; il bit 2 le posizioni 2, 3, 6, 7, …; il bit 4 le posizioni 4, 5, 6, 7, … Chi riceve ricalcola le tre parità: i risultati, letti come numero binario (la **sindrome**), valgono 0 se non c'è errore, e altrimenti danno proprio la posizione del bit sbagliato, che basta invertire. Aggiungendo un bit di parità su tutta la parola si ottiene il codice **SECDED** (correzione di un errore, rilevazione di due), usato nelle memorie ECC.

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle slide (ALU, Codici di Hamming); soluzioni controllate con `strumenti/verifica_ampliamento.py` (ADC-03)

**Esercizio 1. I riporti anticipati di una somma a 4 bit.** $a = 1011$, $b = 0110$, $c_0 = 0$.

$g = a \cdot b$ bit per bit $= 0010$, $p = a + b = 1111$. Quindi $c_1 = g_0 = 0$; $c_2 = g_1 + p_1 g_0 = 1$; $c_3 = g_2 + p_2 g_1 + p_2 p_1 g_0 = 0 + 1 + 0 = 1$; $c_4 = g_3 + p_3 g_2 + p_3 p_2 g_1 + \dots = 0 + 0 + 1 = 1$. Le somme sono $s_i = a_i \oplus b_i \oplus c_i$: $s_0 = 1$, $s_1 = 0$, $s_2 = 0$, $s_3 = 0$, e il risultato è $1\,0001$, cioè $11 + 6 = 17$. Il riporto finale nasce in $g_1$ e viaggia attraverso $p_2$ e $p_3$: nel ripple impiegherebbe tre stadi, con il lookahead è pronto subito.

**Esercizio 2. Moltiplicazione con l'hardware add and right shift.** $6 \times 5$ con 4 bit: moltiplicando $M = 0110$, registro prodotto iniziale $0000\,0101$.

| Passo | Bit basso | Dopo l'eventuale somma | Dopo lo shift |
|---|---|---|---|
| 1 | 1 | $0110\,0101$ | $0011\,0010$ |
| 2 | 0 | – | $0001\,1001$ |
| 3 | 1 | $0111\,1001$ | $0011\,1100$ |
| 4 | 0 | – | $0001\,1110$ |

Il risultato è $0001\,1110 = 30$. A ogni passo il moltiplicatore "esce" a destra e il prodotto parziale "entra" da sinistra: lo stesso registro contiene entrambi.

**Esercizio 3. Booth con un moltiplicatore negativo.** $3 \times (-2)$ con 4 bit: $M = 0011$, $Q = 1110$, $q_{-1} = 0$, $A = 0000$.

| Passo | $q_0\,q_{-1}$ | Operazione | $A$ dopo lo shift | $Q$ dopo lo shift | $q_{-1}$ |
|---|---|---|---|---|---|
| 1 | 0 0 | nessuna | 0000 | 0111 | 0 |
| 2 | 1 0 | $A = A - M = 1101$ | 1110 | 1011 | 1 |
| 3 | 1 1 | nessuna | 1111 | 0101 | 1 |
| 4 | 1 1 | nessuna | 1111 | 1010 | 1 |

Il prodotto è $A\,Q = 1111\,1010 = -6$ in complemento a 2. Il moltiplicatore $1110$ è una sola sequenza di 1 che arriva fino al bit di segno: c'è una sola sottrazione e nessuna somma, perché la sequenza non "finisce".

**Esercizio 4. Divisione in binario.** $1011 \div 0011$ ($11 \div 3$).

Si procede come in colonna, abbassando un bit alla volta: $1 < 11$, quoziente 0; $10 < 11$, quoziente 0; $101 \ge 11$, quoziente 1 e resto $101 - 11 = 10$; si abbassa l'ultimo bit, $101 \ge 11$, quoziente 1 e resto $10$. Quoziente $0011 = 3$, resto $10 = 2$, e infatti $3 \cdot 3 + 2 = 11$.

**Esercizio 5. Somma in virgola mobile.** $1{,}75 + 0{,}3125$.

$1{,}75 = 1{,}11_2 \times 2^0$ e $0{,}3125 = 1{,}01_2 \times 2^{-2}$. (1) Si allinea il secondo all'esponente 0: $0{,}0101_2 \times 2^0$. (2) Somma: $1{,}1100 + 0{,}0101 = 10{,}0001_2$. (3) Normalizzazione: $1{,}00001_2 \times 2^1$. (4) Con 23 bit di frazione non serve arrotondare. Il risultato è $2 + \frac{2}{32} = 2{,}0625$.

**Esercizio 6. Prodotto in virgola mobile.** $1{,}5 \times (-2{,}25)$ in singola precisione.

$1{,}5 = 1{,}1_2 \times 2^0$ (campo esponente 127), $-2{,}25 = -1{,}001_2 \times 2^1$ (campo 128). (1) Esponente: $127 + 128 - 127 = 128$, cioè $E = 1$. (2) Mantisse: $1{,}1 \times 1{,}001 = 1{,}1011_2$. (3) Già normalizzata. (5) Segno: $0 \oplus 1 = 1$. Il risultato è $-1{,}1011_2 \times 2^1 = -3{,}375$.

**Esercizio 7. Un codice di Hamming (7, 4).** Codificare i dati $1011$ e correggere la parola ricevuta se il bit in posizione 6 si altera.

I dati vanno nelle posizioni 3, 5, 6, 7: $b_3 = 1$, $b_5 = 0$, $b_6 = 1$, $b_7 = 1$. Parità: $b_1 = b_3 \oplus b_5 \oplus b_7 = 0$, $b_2 = b_3 \oplus b_6 \oplus b_7 = 1$, $b_4 = b_5 \oplus b_6 \oplus b_7 = 0$. La parola trasmessa, dalla posizione 1 alla 7, è $0\,1\,1\,0\,0\,1\,1$. Se si altera $b_6$ si riceve $0\,1\,1\,0\,0\,0\,1$. Il ricevitore calcola $s_1 = b_1 \oplus b_3 \oplus b_5 \oplus b_7 = 0$, $s_2 = b_2 \oplus b_3 \oplus b_6 \oplus b_7 = 1$, $s_4 = b_4 \oplus b_5 \oplus b_6 \oplus b_7 = 1$: la sindrome $s_4 s_2 s_1 = 110 = 6$ indica la posizione sbagliata, e invertendo $b_6$ si ritrova la parola giusta.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni controllate con `strumenti/verifica_ampliamento.py` (ADC-03)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. L'overflow dell'ALU.** Con 8 bit, l'ALU calcola $100 + 50$ e $(-100) - 50$. In quali casi segnala overflow e che cosa dà `slt` per $a = 100$, $b = -100$?

*Passo 1.* $100 + 50 = 150 > 127$: il risultato $1001\,0110$ ha segno negativo; i riporti nel e dal bit di segno sono $c_7 = 1$, $c_8 = 0$, diversi: overflow.

*Passo 2.* $(-100) - 50 = -150 < -128$: overflow anche qui, con risultato $0110\,1010$ apparentemente positivo.

*Passo 3: `slt` di $100$ e $-100$.* $100 - (-100) = 200$ va in overflow, e il bit di segno della sottrazione è 1, come se $100 < -100$. Il valore giusto di Set è il bit di segno XOR overflow: $1 \oplus 1 = 0$, quindi `slt` dà 0, correttamente.

**Guidato 2. Quanti bit di controllo?** Si vuole correggere un errore singolo su parole di 32 bit, e rilevarne due.

*Passo 1: la disuguaglianza.* $2^K \ge 32 + K + 1$.

*Passo 2: provare.* $K = 5$: $32 \ge 38$, no. $K = 6$: $64 \ge 39$, sì.

*Passo 3: SECDED.* Per rilevare anche gli errori doppi si aggiunge un bit di parità globale: 7 bit di controllo su 32 di dati, una parola di 39 bit.

*Passo 4: il confronto.* Per 64 bit di dati bastano $K = 7$ più 1, cioè 8: è il formato delle memorie ECC, con 72 bit per ogni 64.

**Guidato 3. Somma in virgola mobile con numeri di segno diverso.** $0{,}5 + (-0{,}4375)$ con 4 bit di mantissa.

*Passo 1: i numeri.* $0{,}5 = 1{,}000_2 \times 2^{-1}$; $-0{,}4375 = -1{,}110_2 \times 2^{-2}$.

*Passo 2: allineare.* Il secondo diventa $-0{,}111_2 \times 2^{-1}$.

*Passo 3: sommare.* $1{,}000 - 0{,}111 = 0{,}001_2$, con esponente $-1$.

*Passo 4: normalizzare.* $0{,}001_2 \times 2^{-1} = 1{,}000_2 \times 2^{-4}$: lo shift è a sinistra di tre posti, e l'esponente scende di 3.

*Passo 5: risultato.* $2^{-4} = 0{,}0625$. La differenza di due numeri vicini perde cifre significative: è la **cancellazione**, il principale motivo di errore nei calcoli in virgola mobile.

## Riepilogo

L'ALU a un bit sceglie con un multiplexer fra AND, OR e somma; con Binvert e il riporto iniziale a 1 sottrae, con Ainvert fa la NOR. L'ALU a 32 bit aggiunge l'ingresso Less per `slt`, l'uscita Zero per i salti e il rilevamento dell'overflow con $c_{31} \oplus c_{32}$. Il calcolo anticipato del riporto rende i riporti reti a due livelli nei segnali di generazione e propagazione, e si applica a blocchi. La moltiplicazione si fa con somme e shift su un registro di $2n$ bit; l'algoritmo di Booth sostituisce le sequenze di 1 con una sottrazione e una somma e lavora in complemento a 2. La divisione si fa con sottrazioni di prova e ripristini, un passo alla volta. In virgola mobile la somma richiede allineamento, somma, normalizzazione e arrotondamento; il prodotto somma gli esponenti togliendo l'eccesso e moltiplica le mantisse. I codici di Hamming con distanza 3 correggono un errore con $K$ bit di controllo tali che $2^K \ge M + K + 1$, e la sindrome indica la posizione dell'errore.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (ADC-03)

### Interi

$$a - b = a + \bar b + 1, \qquad V = c_{n-1} \oplus c_n, \qquad \text{Zero} = \overline{r_{31} + \dots + r_0}, \qquad \text{Set}_{slt} = s_{31} \oplus V.$$

$$g_i = a_i b_i, \quad p_i = a_i + b_i, \quad c_{i+1} = g_i + p_i c_i, \quad P = p_3 p_2 p_1 p_0, \quad G = g_3 + p_3 g_2 + p_3 p_2 g_1 + p_3 p_2 p_1 g_0.$$

| Algoritmo | Regola del passo |
|---|---|
| Add and right shift | se il bit basso è 1, somma $M$ alla metà alta; poi shift a destra |
| Booth | $10$: $A - M$; $01$: $A + M$; $00$, $11$: niente; poi shift aritmetico a destra |
| Divisione restoring | sottrai; se negativo ripristina e il bit è 0, altrimenti il bit è 1 |

### Virgola mobile

$$N = (-1)^s (1 + F) 2^{E - bias}, \quad bias = 127 \text{ (32 bit)}, 1023 \text{ (64 bit)}; \qquad E_{prodotto} = E_1 + E_2 - bias.$$

Somma: allinea, somma, normalizza, arrotonda. Prodotto: esponenti, mantisse, normalizza, arrotonda, segno. Bit di arrotondamento: guard, round, sticky.

### Hamming

$d$ = distanza minima: rileva $d - 1$ errori, ne corregge $\lfloor (d - 1)/2 \rfloor$. Bit di controllo: $2^K \ge M + K + 1$ (SECDED: $K + 1$). Bit di controllo nelle posizioni $1, 2, 4, 8, \dots$; il bit $2^j$ è la parità delle posizioni con il bit $j$ a 1; la sindrome dà la posizione dell'errore.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Ripple carry | riporto che si propaga stadio per stadio |
| Carry lookahead | riporti calcolati in anticipo con generazione e propagazione |
| Algoritmo di Booth | moltiplicazione con somme e sottrazioni secondo le coppie di bit del moltiplicatore |
| Shift aritmetico | shift a destra che ripete il bit di segno |
| Normalizzazione | portare la mantissa nella forma $1{,}F$ |
| Guard, round, sticky | bit extra per arrotondare correttamente |
| Distanza di Hamming | numero di bit in cui differiscono due parole |
| Sindrome | risultato dei controlli di parità, posizione dell'errore |
| SECDED | corregge un errore singolo e rileva quelli doppi |

### Domande che tornano spesso

- Costruire l'ALU a un bit e poi a 32 bit; come si realizzano sottrazione, `slt`, Zero e overflow?
- Perché il ripple carry è lento? Ricavare le equazioni del carry lookahead.
- Descrivere l'hardware della moltiplicazione e l'algoritmo di Booth, con un esempio.
- Perché la divisione è più lenta della moltiplicazione?
- Algoritmi di somma e prodotto in virgola mobile; perché nel prodotto si toglie il bias?
- Codici di Hamming: distanza, numero di bit di controllo, sindrome; che cos'è il SECDED?
