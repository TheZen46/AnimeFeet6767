---
corso: Reti Logiche
modulo: 2
titolo: Reti combinatorie standard, ritardi e aritmetica
programma: [RL-02, RL-03]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-04
---

# 2 · Reti combinatorie standard, ritardi e aritmetica

**In questo modulo.** Si usano le forme canoniche, le mappe di Karnaugh e le variabili riportate del modulo 1 (*Algebra booleana e sintesi delle reti combinatorie*). Si studiano le reti combinatorie che si usano come blocchi già pronti: multiplexer, demultiplexer, decoder, encoder. Poi si guarda che cosa succede nel circuito reale, dove ogni porta ha un ritardo, e come i ritardi producano le alee. L'ultima parte è l'aritmetica binaria: la rappresentazione dei numeri e i codici, la somma, il complemento a 2 per i numeri negativi, le reti che sommano, sottraggono, confrontano e moltiplicano, fino all'unità aritmetico-logica. Alla fine del modulo si sa progettare con i blocchi standard, riconoscere ed eliminare un'alea statica, e fare a mano e con una rete le operazioni sui numeri binari con e senza segno.

## 2.1 Multiplexer

Il **multiplexer** (MUX) è un selettore: ha alcuni ingressi dati, alcuni ingressi di selezione e un'uscita, che copia l'ingresso dati scelto dalla selezione. Il più semplice è il MUX 2→1, con ingressi dati $S_0$ e $S_1$, selezione $SEL$ e uscita $U$. La specifica a parole è: $U = S_0$ se $SEL = 0$, $U = S_1$ se $SEL = 1$.

| $SEL$ | $S_1$ | $S_0$ | $U$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

La prima forma canonica ha quattro mintermini, che si raccolgono a due a due:

$$U = \overline{SEL}\,\bar{S}_1 S_0 + \overline{SEL}\,S_1 S_0 + SEL\,S_1\bar{S}_0 + SEL\,S_1 S_0 = \overline{SEL}\,S_0 + SEL\,S_1.$$

La seconda ha quattro maxtermini, che si raccolgono allo stesso modo: posto $T = SEL + S_0$, i due fattori $(T + S_1)(T + \bar{S}_1)$ danno $T$, e lo stesso vale per gli altri due. Quindi $U = (SEL + S_0)(\overline{SEL} + S_1)$. Con la mappa le due sintesi si trovano subito: righe $SEL$, colonne $S_1 S_0$.

| $SEL \backslash S_1 S_0$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 |

Il circuito della SOP ha due AND e una OR (figura 2.1): $SEL$ entra diretto in una AND e negato nell'altra, quindi una sola delle due AND è "aperta" e lascia passare il suo ingresso dati.

![Figura 2.1](../figure/2-1.svg)

Il MUX 4→1 ha quattro ingressi dati $I_0, \dots, I_3$ e due di selezione $S_1 S_0$, che formano il numero binario dell'ingresso scelto:

| $S_1$ | $S_0$ | $U$ |
|---|---|---|
| 0 | 0 | $I_0$ |
| 0 | 1 | $I_1$ |
| 1 | 0 | $I_2$ |
| 1 | 1 | $I_3$ |

$$U = \bar{S}_1\bar{S}_0\, I_0 + \bar{S}_1 S_0\, I_1 + S_1\bar{S}_0\, I_2 + S_1 S_0\, I_3.$$

In generale un MUX $2^n \to 1$ ha $n$ ingressi di selezione, e la sua uscita è la somma dei prodotti fra ogni mintermine delle selezioni e l'ingresso dati corrispondente. Un MUX grande si costruisce con MUX più piccoli: con tre MUX 2→1 si ottiene un MUX 4→1, facendo scegliere ai primi due con $S_0$ fra $I_0, I_1$ e fra $I_2, I_3$, e all'ultimo con $S_1$ fra le loro uscite (figura 2.2).

![Figura 2.2](../figure/2-2.svg)

Il MUX è una **rete universale**. Se si collegano le $n$ variabili di una funzione agli ingressi di selezione di un MUX $2^n \to 1$ e si mette su ogni ingresso dati la costante 0 o 1 della riga corrispondente della tabella di verità, l'uscita realizza la funzione. Per esempio lo XOR $A \oplus B$ si ottiene da un MUX 4→1 con $A$ su $S_1$, $B$ su $S_0$ e ingressi dati $0, 1, 1, 0$ (figura 2.3).

![Figura 2.3](../figure/2-3.svg)

Il MUX 4→1 si può anche leggere come una mappa a due variabili ($S_1$, $S_0$) con gli ingressi dati nelle celle: è una mappa a variabili riportate. Di qui il legame con il paragrafo 1.6: una funzione di $n$ variabili si realizza anche con un MUX $2^{n-1} \to 1$, mettendo $n - 1$ variabili sulle selezioni e scrivendo negli ingressi dati 0, 1, la variabile rimasta o la sua negazione.

## 2.2 Demultiplexer, decoder, encoder

Il **demultiplexer** (DEMUX) fa l'operazione inversa del MUX: ha un ingresso dati $IN$, $n$ ingressi di selezione e $2^n$ uscite, e porta $IN$ sull'uscita scelta, mentre le altre restano a 0. Per il DEMUX 1→4:

$$U_0 = \bar{S}_1\bar{S}_0\, IN, \quad U_1 = \bar{S}_1 S_0\, IN, \quad U_2 = S_1\bar{S}_0\, IN, \quad U_3 = S_1 S_0\, IN.$$

| $S_1$ | $S_0$ | $U_0$ | $U_1$ | $U_2$ | $U_3$ |
|---|---|---|---|---|---|
| 0 | 0 | $IN$ | 0 | 0 | 0 |
| 0 | 1 | 0 | $IN$ | 0 | 0 |
| 1 | 0 | 0 | 0 | $IN$ | 0 |
| 1 | 1 | 0 | 0 | 0 | $IN$ |

Il **decoder** $n \to 2^n$ ha $n$ ingressi e $2^n$ uscite, e per ogni combinazione degli ingressi porta a 1 una e una sola uscita: l'uscita $U_k$ vale 1 quando gli ingressi formano il numero $k$. Ogni uscita è quindi un mintermine degli ingressi: nel decoder 3→8, $U_0 = \bar{I}_2\bar{I}_1\bar{I}_0$, …, $U_7 = I_2 I_1 I_0$. Un DEMUX è un decoder con un ingresso di abilitazione: se $IN = 0$ tutte le uscite sono a 0, se $IN = 1$ funziona come decoder. Poiché un decoder produce tutti i mintermini, un decoder seguito da una OR degli opportuni mintermini realizza qualsiasi funzione nella prima forma canonica.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-02)
> **Encoder.** L'**encoder** $2^n \to n$ fa l'inverso del decoder: ha $2^n$ ingressi, di cui se ne suppone attivo uno alla volta, e dà in uscita il numero binario dell'ingresso attivo. Se più ingressi possono essere attivi insieme si usa l'**encoder con priorità**, che codifica quello di indice più alto, con un'uscita $V$ che dice se almeno un ingresso è attivo. Per 4 ingressi:
>
> | $I_3$ | $I_2$ | $I_1$ | $I_0$ | $Y_1$ | $Y_0$ | $V$ |
> |---|---|---|---|---|---|---|
> | 0 | 0 | 0 | 0 | – | – | 0 |
> | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
> | 0 | 0 | 1 | – | 0 | 1 | 1 |
> | 0 | 1 | – | – | 1 | 0 | 1 |
> | 1 | – | – | – | 1 | 1 | 1 |
>
> I trattini negli ingressi sono indifferenze sugli ingressi (paragrafo 1.6). Dalla tabella: $Y_1 = I_3 + I_2$, $Y_0 = I_3 + \bar{I}_2 I_1$, $V = I_3 + I_2 + I_1 + I_0$.

> [!esempio] Una porta logica programmabile
> Una rete ha due ingressi di controllo $S_0$, $S_1$ e due ingressi dati $A$, $B$, e deve comportarsi come una porta diversa a seconda del controllo:
>
> | $S_0$ | $S_1$ | $U$ |
> |---|---|---|
> | 0 | 0 | $A \cdot B$ |
> | 0 | 1 | $A + B$ |
> | 1 | 0 | $\bar{A}$ |
> | 1 | 1 | – |
>
> La combinazione $11$ non si usa: è un'indifferenza su tutta la riga. Sulla mappa a quattro variabili (righe $S_0 S_1$, colonne $AB$)
>
> | $S_0 S_1 \backslash AB$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | 00 | 0 | 0 | 1 | 0 |
> | 01 | 0 | 1 | 1 | 1 |
> | 11 | – | – | – | – |
> | 10 | 1 | 1 | 0 | 0 |
>
> la sintesi AND-OR è $U = S_1 A + S_1 B + S_0\bar{A} + \bar{S}_0 AB$ e quella OR-AND è $U = (\bar{S}_0 + \bar{A})(S_0 + S_1 + A)(S_0 + S_1 + B)(A + B + \bar{S}_1)$. L'ultimo fattore copre lo 0 in $S_0 S_1 AB = 0100$ usando l'indifferenza in $1100$; si può scegliere anche $(S_0 + A + B)$, che copre lo stesso 0 insieme a quello in $0000$. Le indifferenze della riga $11$ permettono di scrivere $S_1 A$ invece di $\bar{S}_0 S_1 A$, e $S_0\bar{A}$ invece di $S_0\bar{S}_1\bar{A}$.

## 2.3 Ritardi di propagazione e alee

Nel modulo 1 le porte erano ideali: l'uscita cambiava nello stesso istante degli ingressi. Una porta reale impiega un tempo per rispondere, il **ritardo di propagazione** $t_p$, che è diverso da porta a porta e cambia con la temperatura, con il carico e con il verso della commutazione. Il diagramma temporale reale di una rete combinatoria mostra le uscite che cambiano un po' dopo gli ingressi, e una rete con più livelli accumula i ritardi di tutte le porte che un segnale attraversa.

L'esempio più semplice è $OUT = IN + \overline{IN}$, che per l'algebra vale sempre 1. Nel circuito $IN$ arriva alla OR direttamente, $\overline{IN}$ attraverso un NOT che ritarda di $t_p$. Quando $IN$ scende da 1 a 0, per un tempo pari al ritardo del NOT entrambi gli ingressi della OR sono a 0, e l'uscita fa un impulso a 0 che non dovrebbe esserci (figura 2.4).

![Figura 2.4](../figure/2-4.svg)

> [!definizione] Alea
> Un'**alea** (*hazard*) è una variazione transitoria e indesiderata dell'uscita di una rete combinatoria, dovuta ai diversi ritardi dei percorsi che i segnali seguono dagli ingressi all'uscita. L'alea è **statica** se l'uscita dovrebbe restare costante e invece fa un impulso (alea statica di 1 se dovrebbe restare a 1, di 0 se dovrebbe restare a 0); è **dinamica** se l'uscita dovrebbe cambiare una volta e invece oscilla prima di assestarsi.

Le alee statiche di una rete a due livelli si vedono sulla mappa. Si prenda $U = \bar{A}B + AC$, con $B = C = 1$ e $A$ che scende da 1 a 0: la funzione passa dalla cella $111$ alla cella $011$ e vale 1 in entrambe. Ma le due celle sono coperte da gruppi diversi: in $111$ l'uscita è tenuta a 1 dalla AND di $AC$, in $011$ dalla AND di $\bar{A}B$. Se la prima si spegne prima che la seconda si accenda, cosa che succede perché $\bar{A}$ passa attraverso un NOT in più, l'uscita scende a 0 per un istante.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-02)
> **Il termine di consenso elimina l'alea.** Se si aggiunge alla sintesi il gruppo $BC$, che copre entrambe le celle, durante la transizione la sua AND resta accesa e tiene l'uscita a 1: $U = \bar{A}B + AC + BC$ è la stessa funzione (è la proprietà del consenso del paragrafo 1.3) ma non ha l'alea (figura 2.5). In generale una sintesi SOP è priva di alee statiche di 1 per le variazioni di una sola variabile se ogni coppia di celle adiacenti a 1 è coperta da almeno un gruppo comune. Si paga con porte in più: la sintesi senza alee non è più minima.

![Figura 2.5](../figure/2-5.svg)

Le alee contano quando l'uscita di una rete combinatoria viene usata mentre è ancora in transizione. La soluzione più generale è non guardarla finché non si è assestata: è quello che fa il **clock** nelle reti sincrone del modulo 3, dove le uscite delle reti combinatorie si campionano solo in istanti in cui sono certamente a regime.

## 2.4 Numeri e codici

Un numero naturale si scrive in **notazione posizionale** in base $B$ con le cifre $a_k \dots a_1 a_0$, ciascuna fra 0 e $B - 1$, e il suo valore è

$$N = a_k B^k + a_{k-1} B^{k-1} + \dots + a_1 B + a_0.$$

In base 10, $134 = 1 \cdot 10^2 + 3 \cdot 10 + 4$. In base 2 le cifre sono bit: $01010_2 = 1 \cdot 2^3 + 1 \cdot 2^1 = 10$. Con $n$ bit si rappresentano i naturali da $0$ a $2^n - 1$; con 4 bit da $0000 = 0$ a $1111 = 15$. Il bit di peso massimo si chiama MSB (*most significant bit*), quello di peso minimo LSB.

**Da binario a decimale** si sommano le potenze di 2 dei bit a 1: $1001_2 = 2^3 + 2^0 = 9$ e $10100110010_2 = 1024 + 256 + 32 + 16 + 2 = 1330$. **Da decimale a binario** si divide ripetutamente per 2: i resti, dal primo all'ultimo, sono i bit dall'LSB all'MSB. Per $38$: $38 = 2 \cdot 19 + 0$, $19 = 2 \cdot 9 + 1$, $9 = 2 \cdot 4 + 1$, $4 = 2 \cdot 2 + 0$, $2 = 2 \cdot 1 + 0$, $1 = 2 \cdot 0 + 1$, quindi $38 = 100110_2$.

Le basi 8 (**ottale**) e 16 (**esadecimale**) sono comode perché una cifra corrisponde a un gruppo fisso di bit, 3 per l'ottale e 4 per l'esadecimale, e si convertono a gruppi partendo da destra. In esadecimale le cifre da 10 a 15 si scrivono A, …, F.

- $33_8 = 3 \cdot 8 + 3 = 27$, e in binario $011\,011_2$; viceversa $001\,010_2 = 12_8 = 10$.
- $0101\,1110_2 = 5E_{16} = 5 \cdot 16 + 14 = 94$; per divisioni successive per 16, $94 = 16 \cdot 5 + 14$ dà di nuovo $5E$.

Il **BCD** (*binary coded decimal*, codice 8421) scrive ogni cifra decimale con i suoi 4 bit: $1013 \to 0001\;0000\;0001\;0011$. È comodo per i visualizzatori, ma spreca 6 delle 16 combinazioni di 4 bit (da 1010 a 1111).

Il **codice Gray** ordina le combinazioni di $n$ bit in modo che due consecutive differiscano per un solo bit. Si costruisce per riflessione: si scrive la sequenza a $n - 1$ bit, poi la stessa al contrario, e si aggiunge davanti 0 alla prima metà e 1 alla seconda. Da $0, 1$ si ottiene $00, 01, 11, 10$, e da questa $000, 001, 011, 010, 110, 111, 101, 100$. È l'ordine delle righe e delle colonne delle mappe di Karnaugh.

Un **bit di parità** aggiunto a un dato permette di accorgersi di un errore di trasmissione su un bit. Con la parità pari il bit vale lo XOR di tutti i bit del dato, così il numero totale di 1 è pari: per il dato $0111010$, che ha quattro 1, il bit di parità è 0. Chi riceve rifà lo XOR di tutto: se viene 1, almeno un bit è cambiato. Due errori si compensano e non si vedono; per controlli più robusti si aggiunge in coda ai dati una somma di controllo (*checksum*).

## 2.5 Somma binaria

La somma si fa in colonna come in base 10, con il riporto: in base 10 $39 + 12 = 51$ perché $9 + 2 = 11$ dà 1 con riporto 1. In base 2, $1 + 1 = 10$: cifra 0 e riporto 1. Per esempio

$$1001010_2 + 110110_2 = 10000000_2,$$

cioè $74 + 54 = 128$: i riporti si propagano fino all'ultima colonna e il risultato ha un bit in più degli addendi.

Il **semisommatore** (*half adder*) somma due bit e dà la somma $S$ e il riporto $C$:

| $A$ | $B$ | $S$ | $C$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

quindi $S = A \oplus B$ e $C = AB$. Il **sommatore completo** (*full adder*) somma due bit e il riporto in ingresso $C_{in}$: la somma è lo XOR a tre ingressi $S = A \oplus B \oplus C_{in}$, e il riporto vale 1 quando almeno due dei tre ingressi valgono 1, $C_{out} = AB + AC_{in} + BC_{in}$ (la sintesi della mappa ha tre coppie). La figura 2.6 mostra i due circuiti.

![Figura 2.6](../figure/2-6.svg)

Il **sommatore a cascata** (*ripple carry adder*) a $n$ bit mette in fila $n$ full adder: il riporto in uscita di ogni bit è il riporto in ingresso del successivo, e il riporto in ingresso del bit 0 vale 0 (figura 2.7). Il blocco ADD4 ha ingressi $A_3 \dots A_0$, $B_3 \dots B_0$ e $C_{in}$, uscite $S_3 \dots S_0$ e il riporto finale; due ADD4 in cascata fanno un ADD8. Il difetto è la velocità: nel caso peggiore il riporto deve attraversare tutti gli $n$ stadi, e il ritardo cresce con $n$. Per i numeri naturali, un riporto finale a 1 vuol dire che il risultato non sta in $n$ bit: è un **overflow**.

![Figura 2.7](../figure/2-7.svg)

## 2.6 Sottrazione e numeri negativi

La sottrazione in colonna usa il **prestito**: $0 - 1$ non si può fare, quindi si prende 1 dalla colonna a sinistra, e la colonna vale $10_2 - 1 = 1$. Per esempio $1010010_2 - 111111_2 = 0010011_2$, cioè $82 - 63 = 19$.

Per i numeri negativi l'idea più immediata è usare il primo bit come segno e gli altri come modulo (**modulo e segno**). Ha due difetti: lo zero ha due rappresentazioni ($0000$ e $1000$), e il sommatore del paragrafo 2.5 non funziona più. Per esempio $7 + (-2)$ con 4 bit diventa $0111 + 1010 = 10001$, che non è 5.

> [!definizione] Complemento a 2
> Con $n$ bit, nella rappresentazione in **complemento a 2** il bit più significativo ha peso $-2^{n-1}$ invece di $+2^{n-1}$:
> $$N = -a_{n-1}\, 2^{n-1} + a_{n-2}\, 2^{n-2} + \dots + a_1 \cdot 2 + a_0.$$
> I numeri rappresentabili vanno da $-2^{n-1}$ a $2^{n-1} - 1$; quelli con il primo bit a 1 sono i negativi. Per cambiare segno a un numero si **negano tutti i bit e si somma 1**.

Con 3 bit:

| bit | valore | | bit | valore |
|---|---|---|---|---|
| 000 | 0 | | 100 | −4 |
| 001 | 1 | | 101 | −3 |
| 010 | 2 | | 110 | −2 |
| 011 | 3 | | 111 | −1 |

Si controlla la regola: $-3$ si ottiene da $011$ negando ($100$) e sommando 1 ($101$); $-0$ dà $111 + 1 = 1000$, cioè $000$ sui 3 bit, e lo zero è unico. Con 4 bit i valori vanno da $1000 = -8$ a $0111 = 7$, e $1111 = -1$. Il numero di bit va sempre specificato: $1111$ vale $-1$ su 4 bit e $15$ se è un naturale, e $-11$ su 8 bit si ottiene da $00001011$ negando ($11110100$) e sommando 1: $11110101$.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-03)
> **Estensione del segno.** Per scrivere un numero in complemento a 2 su più bit si ripete il bit di segno a sinistra: $-3 = 101$ su 3 bit è $11111101$ su 8 bit, e $3 = 011$ è $00000011$.

Il vantaggio del complemento a 2 è che la somma si fa con lo stesso sommatore dei naturali, ignorando il riporto finale:

- $3 + 4$: $0011 + 0100 = 0111 = 7$;
- $-7 + 3$: $1001 + 0011 = 1100 = -4$;
- $-8 + 6$: $1000 + 0110 = 1110 = -2$;
- $7 + (-2)$: $0111 + 1110 = 1\,0101$, e scartando il riporto $0101 = 5$.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-03)
> **Overflow in complemento a 2.** Il risultato è sbagliato quando non sta nell'intervallo $[-2^{n-1}, 2^{n-1} - 1]$, e questo può succedere solo sommando due numeri dello stesso segno. Si riconosce perché il risultato ha il segno opposto: con 4 bit $5 + 4$ dà $0101 + 0100 = 1001$, che vale $-7$. Il riporto finale qui non serve: l'overflow c'è quando il riporto che entra nel bit di segno è diverso da quello che ne esce, $V = c_n \oplus c_{n-1}$.
>
> **Sottrattore.** Poiché $A - B = A + (-B) = A + \bar{B} + 1$, un sommatore diventa un sottrattore negando $B$ e mettendo $C_{in} = 1$. Con una XOR davanti a ogni bit di $B$, comandata da un segnale $SUB$ che va anche su $C_{in}$, la stessa rete somma ($SUB = 0$) o sottrae ($SUB = 1$).

## 2.7 Prodotto, confronto e unità aritmetico-logica

Il prodotto binario si fa come in base 10, ma i prodotti parziali sono solo copie del moltiplicando, spostate, o zeri: per ogni bit a 1 del moltiplicatore si somma il moltiplicando spostato della sua posizione. Per esempio $10110 \times 111 = 10110 + 101100 + 1011000 = 10011010$, cioè $22 \cdot 7 = 154$. Il prodotto di due numeri di $n$ bit ha fino a $2n$ bit. Una rete moltiplicatrice combinatoria fa i prodotti parziali con porte AND (il prodotto di due bit è il loro AND) e li somma con una schiera di sommatori.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-03)
> **Comparatore.** Il comparatore di due bit ha tre uscite: $A > B$ vale $A\bar{B}$, $A = B$ vale $\overline{A \oplus B}$, $A < B$ vale $\bar{A}B$. Per due numeri di $n$ bit, l'uguaglianza è l'AND delle XNOR bit a bit; per il confronto di grandezza fra naturali si calcola $A - B$ con il sottrattore: c'è un prestito finale (il riporto finale del sommatore vale 0) se e solo se $A < B$.

L'**unità aritmetico-logica** (ALU, *arithmetic logic unit*) mette insieme più reti che lavorano in parallelo sugli stessi operandi $A$ e $B$, per esempio un sommatore, un moltiplicatore e un comparatore, e un MUX che sceglie quale risultato mandare in uscita secondo un codice di operazione $S_1 S_0$: $00$ somma, $01$ prodotto, $10$ confronto (figura 2.8).

![Figura 2.8](../figure/2-8.svg)

> [!nota] Virgola fissa e virgola mobile
> I numeri non interi si rappresentano in **virgola fissa** decidendo quanti bit stanno dopo la virgola: con tre bit frazionari $0{,}375 = 0{,}011_2$, perché $0{,}375 = 2^{-2} + 2^{-3}$. La precisione assoluta è la stessa per tutti i numeri. In **virgola mobile** il numero si scrive come in notazione scientifica, $7{,}3 \cdot 10^2$, con un bit di segno, un esponente e una mantissa: la precisione relativa è la stessa per numeri grandi e piccoli, mentre quella assoluta cambia con l'esponente. I formati standard non fanno parte di questo corso.

## Esempi ed esercizi svolti

**Esercizio 1.** Una rete con un MUX 4→1, una OR, una XNOR e una AND ha la tabella di verità che vale 1 solo per $ABC = 100$ e $111$. Trovare le sintesi minime.

Con righe $A$ e colonne $BC$, la riga $A = 0$ è tutta a 0, la riga $A = 1$ vale $1, 0, 1, 0$. Gli 1 sono isolati: $U = A\bar{B}\bar{C} + ABC$. Raggruppando gli 0, la riga $A = 0$ dà il fattore $A$, e i due 0 della riga $A = 1$ in $101$ e $110$ danno $(B + \bar{C})$ e $(\bar{B} + C)$: $U = A(B + \bar{C})(\bar{B} + C)$. Le due sintesi dicono la stessa cosa: $U = A \cdot \overline{B \oplus C}$, che è proprio la AND fra $A$ e una XNOR.

**Esercizio 2.** Conversioni. $11 = 1011_2$ (resti $1, 1, 0, 1$); $10 = 12_8$ (resti $2, 1$); $30 = 1E_{16}$ (resti $14, 1$); $-11$ in complemento a 2 su 8 bit è $11110101$.

**Esercizio 3.** Operazioni. $1010010 + 110010 = 10000100$ ($82 + 50 = 132$). $1010100 - 110001 = 0100011$ ($84 - 49 = 35$) e $1010100 - 111111 = 0010101$ ($84 - 63 = 21$). $1010 \times 110 = 10100 + 101000 = 111100$ ($10 \cdot 6 = 60$) e $1010 \times 10110 = 10100 + 101000 + 10100000 = 11011100$ ($10 \cdot 22 = 220$).

**Esercizio 4.** Generatore di parità per 4 bit $B_3 B_2 B_1 B_0$. Il bit di parità pari è $P = B_3 \oplus B_2 \oplus B_1 \oplus B_0$, che si realizza con tre porte XOR a due ingressi, in fila oppure ad albero ($(B_3 \oplus B_2) \oplus (B_1 \oplus B_0)$, più veloce perché i livelli sono due invece di tre). Con la mappa sarebbe una scacchiera, senza nessun raggruppamento possibile.

## Riepilogo

I blocchi standard delle reti combinatorie sono il multiplexer, che sceglie un ingresso dati secondo la selezione, il demultiplexer, che porta un ingresso su un'uscita scelta, il decoder, che accende una sola uscita per ogni combinazione e quindi produce tutti i mintermini, e l'encoder, che fa l'inverso. Il MUX è universale: con le variabili sulle selezioni e la tabella di verità sugli ingressi dati realizza qualsiasi funzione. Nel circuito reale ogni porta ha un ritardo di propagazione, e percorsi di lunghezza diversa producono alee: un'alea statica si vede sulla mappa come una transizione fra celle a 1 coperte da gruppi diversi, e si elimina con il termine di consenso. I numeri si scrivono in notazione posizionale; ottale ed esadecimale raggruppano i bit a 3 e a 4, il BCD codifica le cifre decimali e il codice Gray cambia un bit alla volta. La somma si fa con half e full adder in cascata; i numeri negativi si rappresentano in complemento a 2, che si ottiene negando i bit e sommando 1, e con cui la somma si fa con lo stesso sommatore. L'overflow in complemento a 2 si riconosce dal segno del risultato. Sottrattore, comparatore e moltiplicatore si costruiscono con il sommatore, e l'ALU li riunisce con un MUX che sceglie l'operazione.
