---
corso: Reti Logiche
modulo: 1
titolo: Algebra booleana e sintesi delle reti combinatorie
programma: [RL-01, RL-02]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 1 · Algebra booleana e sintesi delle reti combinatorie

**In questo modulo.** Non servono prerequisiti oltre all'algebra delle superiori. Si introducono le variabili e le funzioni booleane, le porte logiche che le realizzano e l'algebra che permette di trasformare un'espressione in un'altra equivalente. Poi si passa al problema centrale delle reti combinatorie: data una specifica, scritta come tabella di verità, trovare un circuito che la realizzi con il minor numero di porte. Gli strumenti sono le forme canoniche del teorema di Shannon e le mappe di Karnaugh, con le indifferenze e le variabili riportate. Alla fine del modulo si sa passare da una specifica a una sintesi minima a due livelli, nelle due forme AND-OR e OR-AND, e realizzarla anche con sole porte NAND o NOR.

## 1.1 Variabili e funzioni booleane

Nella matematica classica una funzione $y = f(x)$ associa a un numero reale $x$ un numero reale $y$. Nelle reti logiche le variabili possono assumere solo due valori, 0 e 1, che si leggono anche come *falso* e *vero*. Due valori sono la quantità minima per portare un'informazione: una variabile di questo tipo si chiama **variabile booleana**, e il suo valore è un **bit**.

> [!definizione] Funzione booleana
> Sia $\mathbb{B} = \{0, 1\}$. Una **funzione booleana** di $n$ variabili è una funzione $f : \mathbb{B}^n \to \mathbb{B}$, che associa a ogni $n$-upla $(x_1, \dots, x_n)$ di bit un bit $y = f(x_1, \dots, x_n)$. Una funzione con $p$ uscite, $f : \mathbb{B}^n \to \mathbb{B}^p$, è un vettore di $p$ funzioni booleane $y_k = f_k(x_1, \dots, x_n)$, che si studiano una alla volta.

Poiché ogni variabile ha due valori, le combinazioni degli ingressi sono $2^n$ (**principio di enumerazione**): una funzione si descrive completamente elencando il valore di uscita per ciascuna di esse, cioè con la sua **tabella di verità**, che ha $2^n$ righe. Ogni riga può contenere 0 o 1 indipendentemente dalle altre, quindi le funzioni distinte di $n$ variabili sono $2^{2^n}$: 4 per $n = 1$, 16 per $n = 2$, 256 per $n = 3$. Sono in numero finito, e per $n$ piccolo anche pochissime.

Una **rete combinatoria** è un circuito digitale le cui uscite, in ogni istante, dipendono solo dai valori degli ingressi in quello stesso istante (a meno dei ritardi, che si vedono nel modulo 2). Una rete combinatoria realizza quindi una funzione booleana, e la si può descrivere in quattro modi equivalenti: con la **tabella di verità** (la specifica), con un'**espressione** booleana (la rappresentazione matematica), con lo **schema** delle porte (la rappresentazione circuitale) e con il **diagramma temporale**, che mostra l'andamento nel tempo degli ingressi e delle uscite.

## 1.2 Le porte logiche

Le funzioni di una variabile sono quattro: le costanti $y = 0$ e $y = 1$, l'**identità** $y = x$, che nel circuito è un filo o un *buffer*, e la **negazione** $y = \bar{x}$ (NOT), che nei simboli si indica con un pallino.

Le funzioni di due variabili sono sedici. La tabella le elenca tutte, con i valori $f(0,0)$, $f(0,1)$, $f(1,0)$, $f(1,1)$ nella prima colonna.

| $f(00)\,f(01)\,f(10)\,f(11)$ | Espressione | Nome |
|---|---|---|
| 0 0 0 0 | $0$ | costante 0 |
| 0 0 0 1 | $x_1 x_2$ | AND |
| 0 0 1 0 | $x_1 \bar{x}_2$ | – |
| 0 0 1 1 | $x_1$ | identità di $x_1$ |
| 0 1 0 0 | $\bar{x}_1 x_2$ | – |
| 0 1 0 1 | $x_2$ | identità di $x_2$ |
| 0 1 1 0 | $x_1 \oplus x_2$ | XOR |
| 0 1 1 1 | $x_1 + x_2$ | OR |
| 1 0 0 0 | $\overline{x_1 + x_2}$ | NOR |
| 1 0 0 1 | $\overline{x_1 \oplus x_2}$ | XNOR |
| 1 0 1 0 | $\bar{x}_2$ | NOT $x_2$ |
| 1 0 1 1 | $x_1 + \bar{x}_2$ | – |
| 1 1 0 0 | $\bar{x}_1$ | NOT $x_1$ |
| 1 1 0 1 | $\bar{x}_1 + x_2$ | – |
| 1 1 1 0 | $\overline{x_1 x_2}$ | NAND |
| 1 1 1 1 | $1$ | costante 1 |

Le funzioni con un nome sono quelle che si realizzano con una sola porta (figura 1.1). L'**AND** vale 1 solo se entrambi gli ingressi valgono 1; l'**OR** vale 1 se almeno uno vale 1; lo **XOR** (*or esclusivo*) vale 1 se gli ingressi sono diversi, cioè se esattamente uno dei due vale 1. NAND, NOR e XNOR sono le loro negazioni. Le porte AND, OR, XOR e le loro negate si estendono a più ingressi: l'AND a $n$ ingressi vale 1 se tutti valgono 1, l'OR se almeno uno vale 1, lo XOR se il numero di ingressi a 1 è dispari.

![Figura 1.1](../figure/1-1.svg)

Lo XOR risolve subito la specifica "$w$ vale 1 se uno solo dei due ingressi vale 1": la tabella è proprio quella di $w = x \oplus y$. Con tre ingressi la stessa specifica ("$w$ vale 1 se uno solo fra $x$, $y$, $t$ vale 1") non è più uno XOR, perché lo XOR a tre ingressi vale 1 anche quando tutti e tre sono a 1. Per scrivere un'espressione a partire da una tabella qualsiasi servono le forme canoniche del paragrafo 1.4.

## 1.3 Algebra di Boole

Le espressioni booleane si manipolano con regole simili a quelle dell'algebra dei numeri, ma non identiche. Ogni identità si dimostra per **induzione perfetta**: si controlla sulla tabella di verità che i due membri valgano lo stesso per tutte le combinazioni delle variabili, che sono in numero finito.

**Proprietà dell'algebra di Boole.** Ogni riga è scritta nella forma per l'OR e nella forma duale per l'AND.

| Proprietà | Forma OR | Forma AND |
|---|---|---|
| Elemento neutro | $A + 0 = A$ | $A \cdot 1 = A$ |
| Elemento nullo | $A + 1 = 1$ | $A \cdot 0 = 0$ |
| Idempotenza | $A + A = A$ | $A \cdot A = A$ |
| Complemento | $A + \bar{A} = 1$ | $A \cdot \bar{A} = 0$ |
| Involuzione | $\bar{\bar{A}} = A$ | $\bar{\bar{A}} = A$ |
| Commutativa | $A + B = B + A$ | $AB = BA$ |
| Associativa | $(A + B) + C = A + (B + C)$ | $(AB)C = A(BC)$ |
| Distributiva | $A + BC = (A + B)(A + C)$ | $A(B + C) = AB + AC$ |
| Assorbimento | $A + AB = A$ | $A(A + B) = A$ |
| Assorbimento del complemento | $A + \bar{A}B = A + B$ | $A(\bar{A} + B) = AB$ |
| De Morgan | $\overline{A + B} = \bar{A}\,\bar{B}$ | $\overline{AB} = \bar{A} + \bar{B}$ |
| Consenso | $AB + \bar{A}C + BC = AB + \bar{A}C$ | $(A + B)(\bar{A} + C)(B + C) = (A + B)(\bar{A} + C)$ |

Due proprietà non hanno corrispondente nell'algebra dei numeri: l'idempotenza e la distributiva della somma rispetto al prodotto, $A + BC = (A + B)(A + C)$.

**Principio di dualità.** Se un'identità è vera, resta vera scambiando ovunque $+$ con $\cdot$ e 0 con 1 (le variabili e le negazioni restano). Per questo ogni proprietà della tabella compare in coppia, e i teoremi di questo modulo hanno sempre una versione AND-OR e una OR-AND.

Le leggi di **De Morgan** valgono con un numero qualsiasi di variabili: la negazione di una somma è il prodotto delle negazioni, e la negazione di un prodotto è la somma delle negazioni. Sono lo strumento per portare le negazioni dentro le parentesi e, nel paragrafo 1.7, per passare da porte AND e OR a sole NAND o NOR.

Il **termine di consenso** $BC$ della proprietà omonima si ottiene dai due termini $AB$ e $\bar{A}C$ che contengono una variabile in forma diretta e negata, togliendola: è ridondante, perché quando vale 1 vale 1 anche uno degli altri due. Nel modulo 2 si vedrà che, nel circuito reale, proprio questo termine ridondante può servire.

> [!esempio] Due semplificazioni
> Sia $Y = \bar{A}\bar{B}\bar{C} + \bar{A}B\bar{C} + AB\bar{C}$. Per l'idempotenza si può duplicare il termine centrale, poi si raccoglie:
> $$Y = \bar{A}\bar{B}\bar{C} + \bar{A}B\bar{C} + \bar{A}B\bar{C} + AB\bar{C} = \bar{A}\bar{C}(\bar{B} + B) + B\bar{C}(\bar{A} + A) = \bar{A}\bar{C} + B\bar{C} = \bar{C}(\bar{A} + B).$$
> Sia ora $Y = \bar{A}\bar{B}\bar{C} + \bar{A}B\bar{C} + \overline{AB\bar{C}}$. Con De Morgan l'ultimo termine diventa $\bar{A} + \bar{B} + C$; i primi due si raccolgono in $\bar{A}\bar{C}$, che è assorbito da $\bar{A}$:
> $$Y = \bar{A}\bar{C} + \bar{A} + \bar{B} + C = \bar{A}(\bar{C} + 1) + \bar{B} + C = \bar{A} + \bar{B} + C.$$
> La funzione vale 0 solo per $ABC = 110$, come si vede dalla tabella.

## 1.4 Forme canoniche e teorema di Shannon

Il teorema di Shannon dice come scrivere un'espressione per una funzione qualsiasi a partire dalla sua tabella.

**Mintermini e maxtermini.** Un **mintermine** di $n$ variabili è un prodotto in cui compaiono tutte le variabili, ciascuna in forma diretta o negata: vale 1 per una sola combinazione degli ingressi. Per $ABC = 101$ il mintermine è $A\bar{B}C$ (la variabile è negata dove vale 0). Un **maxtermine** è una somma in cui compaiono tutte le variabili: vale 0 per una sola combinazione. Per $ABC = 101$ il maxtermine è $\bar{A} + B + \bar{C}$ (la variabile è negata dove vale 1).

> [!teorema] Teorema di espansione di Shannon
> Per ogni funzione booleana $f$ e ogni sua variabile $x_1$:
> $$f(x_1, x_2, \dots, x_n) = \bar{x}_1 \cdot f(0, x_2, \dots, x_n) + x_1 \cdot f(1, x_2, \dots, x_n)$$
> e, nella forma duale,
> $$f(x_1, x_2, \dots, x_n) = \big(x_1 + f(0, x_2, \dots, x_n)\big) \cdot \big(\bar{x}_1 + f(1, x_2, \dots, x_n)\big).$$
> Applicando il teorema a tutte le variabili si ottengono le due **forme canoniche**: $f$ è la somma dei mintermini delle combinazioni in cui vale 1 (**prima forma**, somma di prodotti, SOP) e il prodotto dei maxtermini delle combinazioni in cui vale 0 (**seconda forma**, prodotto di somme, POS).

La dimostrazione è immediata: per $x_1 = 0$ il membro destro della prima forma vale $f(0, x_2, \dots)$, per $x_1 = 1$ vale $f(1, x_2, \dots)$. Per due variabili le due forme sono

$$f(x_1, x_2) = \bar{x}_1\bar{x}_2\, f(0,0) + \bar{x}_1 x_2\, f(0,1) + x_1\bar{x}_2\, f(1,0) + x_1 x_2\, f(1,1)$$

$$f(x_1, x_2) = \big(x_1 + x_2 + f(0,0)\big)\big(x_1 + \bar{x}_2 + f(0,1)\big)\big(\bar{x}_1 + x_2 + f(1,0)\big)\big(\bar{x}_1 + \bar{x}_2 + f(1,1)\big).$$

Nella prima i termini con $f = 0$ spariscono, e restano i mintermini degli 1; nella seconda spariscono i fattori con $f = 1$, e restano i maxtermini degli 0.

> [!esempio] Le due forme di una funzione di tre variabili
> Sia $y$ la funzione che vale 1 per $ABC = 000, 001, 100, 110$ e 0 altrove. La prima forma prende gli 1:
> $$y = \bar{A}\bar{B}\bar{C} + \bar{A}\bar{B}C + A\bar{B}\bar{C} + AB\bar{C} = \bar{A}\bar{B}(\bar{C} + C) + A\bar{C}(\bar{B} + B) = \bar{A}\bar{B} + A\bar{C}.$$
> La seconda prende gli 0, cioè $010, 011, 101, 111$:
> $$y = (A + \bar{B} + C)(A + \bar{B} + \bar{C})(\bar{A} + B + \bar{C})(\bar{A} + \bar{B} + \bar{C}).$$
> Posto $P = A + \bar{B}$, i primi due fattori danno $(P + C)(P + \bar{C}) = P + C\bar{C} = P$ per la distributiva; allo stesso modo gli ultimi due danno $\bar{A} + \bar{C}$. Quindi $y = (A + \bar{B})(\bar{A} + \bar{C})$.

La forma SOP si realizza con una **rete a due livelli** AND-OR: un livello di porte AND, una per ogni prodotto, e una porta OR che li somma. La forma POS dà la rete OR-AND. Nel contare i livelli non si contano i NOT sugli ingressi, perché si suppone di avere ogni variabile disponibile sia diretta sia negata. Una rete a due livelli è la più veloce possibile, perché ogni segnale attraversa al più due porte; le forme canoniche però hanno in genere molti termini, e il problema della **sintesi** è trovare un'espressione equivalente con meno porte e meno ingressi. Non sempre esiste una sola sintesi minima: possono essercene diverse con lo stesso costo.

## 1.5 Mappe di Karnaugh

La semplificazione algebrica si basa sempre sullo stesso passo, $XA + X\bar{A} = X$: due prodotti che differiscono per una sola variabile si fondono in uno. La **mappa di Karnaugh** è una tabella di verità disposta in modo che questi prodotti si vedano a colpo d'occhio.

> [!definizione] Mappa di Karnaugh
> La mappa di una funzione di $n$ variabili ha $2^n$ celle, una per combinazione degli ingressi. Righe e colonne sono ordinate secondo il **codice Gray** (00, 01, 11, 10), in cui due valori consecutivi differiscono per un solo bit. Due celle sono **adiacenti** quando differiscono per una sola variabile: sono adiacenti le celle vicine, e anche le celle ai bordi opposti della stessa riga o colonna, perché la mappa si richiude su se stessa.

Le combinazioni di due variabili sono i quattro vertici di un quadrato, quelle di tre gli otto vertici di un cubo, quelle di quattro i vertici di un ipercubo: due vertici sono collegati da uno spigolo se differiscono per una variabile. La mappa è il modo di disegnare questi oggetti su un foglio senza perdere le adiacenze. Oltre le quattro variabili le adiacenze non si vedono più bene, e si usano metodi tabellari o programmi.

Un **gruppo** di $2^k$ celle adiacenti a forma di rettangolo (anche spezzato dai bordi) che contengono tutte 1 corrisponde a un prodotto con $n - k$ variabili: restano solo quelle che hanno lo stesso valore in tutte le celle del gruppo. Una cella isolata è un mintermine, una coppia toglie una variabile, una quaterna due, e così via.

> [!definizione] Regole di raggruppamento (sintesi SOP)
>
> 1. Coprire tutti gli 1 della mappa.
> 2. Usare gruppi più grandi possibile, di $2^k$ celle.
> 3. Usare il minimo numero di gruppi.
>
> I gruppi possono sovrapporsi. Per la sintesi POS si raggruppano gli 0: ogni gruppo dà una somma in cui una variabile compare negata se nel gruppo vale 1, diretta se vale 0.

**Implicanti primi ed essenziali.** Un gruppo di 1 è un **implicante** della funzione: quando il suo prodotto vale 1, vale 1 anche la funzione. Un implicante è **primo** se non è contenuto in un gruppo più grande; è **essenziale** se copre almeno un 1 che nessun altro implicante primo copre. Una sintesi minima usa solo implicanti primi e contiene sempre tutti quelli essenziali. Il procedimento è quindi: individuare gli implicanti primi, prendere gli essenziali, e coprire gli 1 rimasti con il minor numero di implicanti primi. Quando nell'ultimo passo ci sono più scelte equivalenti, ci sono più sintesi minime.

Nelle mappe di questo modulo le righe e le colonne portano in testa le variabili, nell'ordine di Gray. Negli esempi seguenti, con tre variabili, le righe sono $A$ e le colonne $BC$.

> [!esempio] Una mappa a tre variabili, con un errore da evitare
> La funzione vale 1 per $ABC = 000, 001, 010, 100, 101$.
>
> | $A \backslash BC$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | 0 | 1 | 1 | 0 | 1 |
> | 1 | 1 | 1 | 0 | 0 |
>
> Le prime due colonne formano una quaterna, in cui solo $B$ resta costante a 0: il prodotto è $\bar{B}$. Resta l'1 in $010$, che si raggruppa con la cella $000$, adiacente perché la riga si richiude: il gruppo è $\bar{A}\bar{C}$. Quindi $U = \bar{B} + \bar{A}\bar{C}$.
>
> Sarebbe sbagliato prendere tutta la riga $A = 0$ come gruppo $\bar{A}$: la cella $011$ vale 0.

> [!esempio] Una sintesi senza quaterne
> La funzione vale 1 per $ABC = 001, 010, 100, 110$.
>
> | $A \backslash BC$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | 0 | 0 | 1 | 0 | 1 |
> | 1 | 1 | 0 | 0 | 1 |
>
> L'1 in $001$ non ha vicini a 1: resta il mintermine $\bar{A}\bar{B}C$. Le celle $100$ e $110$ sono adiacenti (ai due bordi della riga) e danno $A\bar{C}$; le celle $010$ e $110$ sono nella stessa colonna e danno $B\bar{C}$. La sintesi minima è $U = \bar{A}\bar{B}C + A\bar{C} + B\bar{C}$, con tre implicanti tutti essenziali.

> [!esempio] Sintesi AND-OR e OR-AND della stessa funzione
> Sia $U = A \oplus B + BC$. Gli 1 sono in $010, 011, 100, 101, 111$.
>
> | $A \backslash BC$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | 0 | 0 | 0 | 1 | 1 |
> | 1 | 1 | 1 | 1 | 0 |
>
> Raggruppando gli 1 si trovano $\bar{A}B$ (le ultime due celle della prima riga), $A\bar{B}$ (le prime due della seconda) e, per l'1 in $111$, a scelta $BC$ oppure $AC$: due sintesi minime, $U = A\bar{B} + \bar{A}B + BC$ e $U = A\bar{B} + \bar{A}B + AC$. Raggruppando gli 0 ($000$, $001$, $110$) si trovano $\bar{A}\bar{B}$, cioè il fattore $(A + B)$, e la cella $110$, cioè $(\bar{A} + \bar{B} + C)$: $U = (A + B)(\bar{A} + \bar{B} + C)$.

Con quattro variabili le righe sono $AB$ e le colonne $CD$, entrambe in ordine di Gray, e si richiudono sia le righe sia le colonne: i quattro angoli sono adiacenti fra loro.

> [!esempio] Una mappa a quattro variabili
> La funzione vale 1 per i mintermini 0, 1, 2, 5, 8, 9, 10 (numerati in binario come $ABCD$).
>
> | $AB \backslash CD$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | 00 | 1 | 1 | 0 | 1 |
> | 01 | 0 | 1 | 0 | 0 |
> | 11 | 0 | 0 | 0 | 0 |
> | 10 | 1 | 1 | 0 | 1 |
>
> Le prime due colonne nelle righe $00$ e $10$ (adiacenti, perché le righe si richiudono) formano la quaterna $\bar{B}\bar{C}$. I quattro angoli formano la quaterna $\bar{B}\bar{D}$. Resta l'1 in $0101$, che si raggruppa con $0001$: $\bar{A}\bar{C}D$. Tutti e tre gli implicanti sono essenziali e $U = \bar{B}\bar{C} + \bar{B}\bar{D} + \bar{A}\bar{C}D$.

Ci sono funzioni che le mappe non semplificano affatto. La funzione di tre variabili che vale 1 quando il numero di ingressi a 1 è pari ha la mappa a scacchiera:

| $x \backslash yz$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |

Nessuna cella ha vicini con lo stesso valore, quindi sia la SOP sia la POS sono le forme canoniche, con quattro termini da tre variabili ciascuno. Raggruppando gli 0 si ottiene

$$U = (x + y + \bar{z})(x + \bar{y} + z)(\bar{x} + y + z)(\bar{x} + \bar{y} + \bar{z}).$$

È la funzione $U = \overline{x \oplus y \oplus z}$, che con le porte XOR richiede due sole porte. Le funzioni di parità sono il caso peggiore per le reti a due livelli e il caso migliore per le porte XOR.

## 1.6 Indifferenze e variabili riportate

Spesso alcune combinazioni degli ingressi non si presentano mai, oppure il valore dell'uscita in corrispondenza di esse non interessa. In quelle celle si scrive un trattino, che si chiama **indifferenza** (*don't care*): nella sintesi lo si considera 1 se aiuta a fare gruppi più grandi, 0 altrimenti. Un'indifferenza non va mai coperta per forza.

Il trattino si usa anche negli ingressi di una tabella: una riga come "$S_1 S_0 = 1\,1$, $A = -$" vuol dire che il valore di $A$ non conta, e la riga vale per entrambi i valori. Le due cose sono diverse: la prima è un'indifferenza sull'uscita, la seconda sugli ingressi.

> [!esempio] Sintesi SOP e POS con le indifferenze
> Righe $AC$, colonne $BD$ (stesso ordine di Gray):
>
> | $AC \backslash BD$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | 00 | 1 | 1 | 1 | 1 |
> | 01 | 0 | – | 0 | 0 |
> | 11 | 0 | 1 | 0 | 0 |
> | 10 | 1 | – | 0 | 0 |
>
> Per la SOP: la prima riga è il gruppo $\bar{A}\bar{C}$; la colonna $BD = 01$, con le due indifferenze, è il gruppo $\bar{B}D$; le righe $00$ e $10$ nelle colonne $00$ e $01$ danno $\bar{B}\bar{C}$. Quindi $U = \bar{A}\bar{C} + \bar{B}\bar{C} + \bar{B}D$.
>
> Per la POS si raggruppano gli 0: le colonne $11$ e $10$ nelle righe $11$ e $10$ ($A = 1$, $B = 1$) danno $(\bar{A} + \bar{B})$; le colonne $00$ e $10$ nelle righe $01$ e $11$ ($C = 1$, $D = 0$) danno $(\bar{C} + D)$; le colonne $11$ e $10$ nelle righe $01$ e $11$ ($B = 1$, $C = 1$) danno $(\bar{B} + \bar{C})$. Quindi $U = (\bar{A} + \bar{B})(\bar{C} + D)(\bar{B} + \bar{C})$.

> [!attenzione]
> Nella sintesi OR-AND è facile sbagliare la polarità: il fattore del gruppo con $B = 1$ e $C = 1$ è $(\bar{B} + \bar{C})$, non $(\bar{B} + C)$. Conviene sempre controllare la sintesi su una cella a 1: qui $\bar{A}B\bar{C}D$ deve dare 1, e con $(\bar{B} + C)$ darebbe 0.

Una mappa può contenere, oltre a 0, 1 e trattini, anche delle **variabili riportate** (*map-entered variables*): una cella che contiene $I$ vuol dire che in quella combinazione l'uscita vale $I$. Così una funzione di tre variabili si scrive su una mappa di due, e una di cinque o sei su una mappa di quattro. Le variabili riportate nascono in modo naturale con i multiplexer (modulo 2), dove ogni cella corrisponde a un ingresso dati.

> [!definizione] Sintesi con le variabili riportate
>
> 1. Si individuano le variabili riportate.
> 2. Si fa la mappa con tutte le variabili riportate poste a 0 e la si sintetizza.
> 3. Per ogni variabile riportata si fa una mappa in cui le celle con quella variabile valgono 1, le celle con 1 diventano indifferenze (sono già coperte dalla mappa del punto 2), le celle con 0 restano 0, e le celle con le altre variabili riportate valgono 0.
> 4. Si sommano le sintesi: quella del punto 2 e, per ogni variabile riportata, la sua sintesi moltiplicata (AND) per la variabile.

Il risultato è una sintesi **quasi minima**: è corretta, ma non è garantito che sia la più piccola possibile, perché le variabili riportate non si raggruppano con le adiacenze delle altre.

> [!esempio] Una variabile riportata
> Righe $A$, colonne $B$: $f(0,0) = 1$, $f(0,1) = I$, $f(1,0) = 1$, $f(1,1) = 0$.
>
> Con $I = 0$ la mappa ha gli 1 nella colonna $B = 0$: $\bar{B}$. Nella mappa di $I$ le due celle con 1 diventano indifferenze e la cella $\bar{A}B$ vale 1: con l'indifferenza in $\bar{A}\bar{B}$ si forma il gruppo $\bar{A}$. Quindi $U = \bar{B} + I\bar{A}$.
>
> Sarebbe inutile scrivere $\bar{I}(\dots) + I(\dots)$ con due mappe complete: le celle a 1 verrebbero coperte due volte. Le celle a 1 sono già nella mappa del punto 2, e la mappa di $I$ deve coprire solo le celle con $I$.

> [!esempio] Due variabili riportate
> Righe $A$, colonne $BC$:
>
> | $A \backslash BC$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | 0 | 1 | 1 | $y$ | $y$ |
> | 1 | 1 | $x$ | 0 | 0 |
>
> Con $x = y = 0$ si trovano $\bar{A}\bar{B}$ e $\bar{B}\bar{C}$. Nella mappa di $x$ la cella $101$ vale 1 e, con le indifferenze delle prime due colonne, forma la quaterna $\bar{B}$. Nella mappa di $y$ le celle $011$ e $010$ valgono 1 e, con le indifferenze, formano la riga $\bar{A}$. Quindi
> $$U = \bar{A}\bar{B} + \bar{B}\bar{C} + x\bar{B} + y\bar{A}.$$

## 1.7 Reti con sole porte NAND o NOR

Con le porte AND, OR e NOT si realizza qualsiasi funzione, perché esistono le forme canoniche. Lo stesso vale per la sola porta NAND, che quindi è **funzionalmente completa**: un NOT è una NAND con gli ingressi uniti ($\overline{A \cdot A} = \bar{A}$), un AND è una NAND seguita da un NOT, e un OR è una NAND con gli ingressi negati, perché per De Morgan $\overline{\bar{A}\,\bar{B}} = A + B$ (figura 1.2). Per dualità anche la sola porta NOR è completa.

![Figura 1.2](../figure/1-2.svg)

Una rete AND-OR si trasforma in una rete di sole NAND senza aggiungere livelli. Negando due volte la SOP e applicando De Morgan alla negazione esterna:

$$U = AB + CD = \overline{\overline{AB + CD}} = \overline{\overline{AB} \cdot \overline{CD}}.$$

Le porte AND del primo livello diventano NAND, e la OR del secondo livello diventa una NAND. Allo stesso modo una rete OR-AND diventa una rete di sole NOR. Le porte NAND e NOR sono le più semplici da costruire con i transistori, e questa trasformazione è quella che si usa in pratica.

**Da POS a sole NOR.** Per dualità, $U = (A + B)(C + D) = \overline{\overline{(A + B)(C + D)}} = \overline{\overline{A + B} + \overline{C + D}}$: le OR del primo livello diventano NOR e la AND del secondo livello diventa una NOR.

## Esempi ed esercizi svolti

**Esercizio 1.** Una rete realizza $F = ACD + \bar{C}\big(\bar{A}D + A(B + D)\big)$, con 5 livelli di porte. Trovare una rete equivalente a due livelli.

Si distribuisce $A$ e si raccoglie $D$ fra i termini con $\bar{A}D$ e $AD$:
$$\bar{A}D + AB + AD = D(\bar{A} + A) + AB = D + AB,$$
quindi
$$F = ACD + \bar{C}(D + AB) = ACD + \bar{C}D + AB\bar{C} = D(AC + \bar{C}) + AB\bar{C} = D(A + \bar{C}) + AB\bar{C},$$
dove nell'ultimo passaggio si è usato l'assorbimento del complemento, $\bar{C} + AC = \bar{C} + A$. Il risultato è
$$F = AD + \bar{C}D + AB\bar{C},$$
una rete AND-OR a due livelli con tre porte AND e una OR.

> [!attenzione]
> Il termine $AB\bar{C}$ non si può perdere per strada: per $ABCD = 1100$ la rete di partenza vale 1, mentre $AD + \bar{C}D$ vale 0.

**Esercizio 2.** Sintesi SOP e POS della funzione con la mappa (righe $X$, colonne $YZ$)

| $X \backslash YZ$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |

Per la SOP: la colonna $00$ dà $\bar{Y}\bar{Z}$; le celle $100$ e $110$ (adiacenti ai bordi) danno $X\bar{Z}$; l'1 in $011$ resta solo: $U = \bar{Y}\bar{Z} + X\bar{Z} + \bar{X}YZ$. Per la POS: la colonna $01$ dà $(Y + \bar{Z})$; le celle $101$ e $111$ danno $(\bar{X} + \bar{Z})$; lo 0 in $010$ resta solo e dà $(X + \bar{Y} + Z)$. Quindi $U = (Y + \bar{Z})(\bar{X} + \bar{Z})(X + \bar{Y} + Z)$.

**Esercizio 3.** Semplificare $x + xy + xyz + xyzw + xz + xw + xzw$.

Raccogliendo $x$: $x(1 + y + yz + yzw + z + w + zw) = x \cdot 1 = x$, perché una somma che contiene 1 vale 1. È l'assorbimento, $x + xP = x$, applicato a ogni termine.

### Esercizi del laboratorio con il simulatore

Gli esercizi che seguono ricalcano quelli fatti in laboratorio con Deeds: si disegna lo schema, si ricava la tabella con la simulazione funzionale (l'animazione, in cui si cambiano gli interruttori e si guardano le uscite) e si controlla con la simulazione temporale. Qui il lavoro si fa a mano, come all'esame, e la simulazione serve da verifica.

**Esercizio 4. Analisi di una rete di porte semplici.** Gli ingressi $A$ e $B$ vanno a una NAND e a una OR; le due uscite entrano in una AND, che dà $U$. Ricavare la tabella di verità e dire che funzione è.

Si ragiona porta per porta, scrivendo una colonna per ogni uscita intermedia: $N = \overline{AB}$ e $O = A + B$.

| $A$ | $B$ | $N = \overline{AB}$ | $O = A + B$ | $U = N \cdot O$ |
|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 0 |

L'uscita vale 1 quando gli ingressi sono diversi: è lo XOR. Lo si vede anche con l'algebra, distribuendo: $\overline{AB}(A + B) = (\bar{A} + \bar{B})(A + B) = \bar{A}B + A\bar{B}$, perché $\bar{A}A$ e $\bar{B}B$ valgono 0. Per la simulazione temporale conviene far cambiare gli ingressi nell'ordine di Gray, $00, 01, 11, 10$: cambia un ingresso alla volta e ogni variazione dell'uscita si attribuisce subito a quell'ingresso.

**Esercizio 5. Controllo di parità a più livelli.** Un ricevitore riceve tre bit di dato $D_2 D_1 D_0$ e un bit di parità $RP$, calcolato dal trasmettitore con la **parità dispari**: il numero totale di 1 nei quattro bit deve essere dispari. La rete di controllo è costruita così: $C_1 = D_2\bar{D}_1 + \bar{D}_2 D_1$, $C_2 = D_0\overline{RP} + \bar{D}_0\,RP$, $ERR = C_1 C_2 + \bar{C}_1\bar{C}_2$. Che cosa fanno $C_1$, $C_2$ ed $ERR$? Si può fare la stessa rete con meno porte?

$C_1$ è la forma SOP di $D_2 \oplus D_1$ e $C_2$ quella di $D_0 \oplus RP$: ciascuna vale 1 se fra i suoi due bit c'è un solo 1. $ERR = C_1 C_2 + \bar{C}_1\bar{C}_2$ è lo XNOR di $C_1$ e $C_2$, quindi
$$ERR = \overline{C_1 \oplus C_2} = \overline{D_2 \oplus D_1 \oplus D_0 \oplus RP}.$$
Lo XOR dei quattro bit vale 1 quando il numero di 1 è dispari, cioè quando la trasmissione è corretta; $ERR$ ne è la negazione e vale 1 quando il numero di 1 è pari, cioè quando c'è un errore. La rete di partenza ha nove porte su quattro livelli (più i NOT); quella con le XOR ha due XOR e una XNOR, oppure tre XOR in cui l'ultima ha un ingresso negato.

Due prove. Il dato $101$ ha due 1, quindi il trasmettitore manda $RP = 1$: i quattro bit $1011$ hanno tre 1 e $ERR = 0$. Se durante la trasmissione $D_1$ si altera, il ricevitore vede $1111$, con quattro 1, ed $ERR = 1$. Se si alterano due bit, per esempio $D_1$ e $RP$, il ricevitore vede $1110$, con tre 1, ed $ERR = 0$: come detto nel modulo 2, un solo bit di parità non vede gli errori doppi.

**Esercizio 6. Sintesi AND-OR e OR-AND, e scelta della più economica.** La funzione $F(X, Y, Z)$ vale 1 per $XYZ = 001, 010, 111$ e 0 altrove. Trovare le due sintesi minime e dire quale costa meno.

| $X \backslash YZ$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |

*Gli 1.* Si controllano i vicini di ogni 1: la cella $001$ è adiacente a $000$, $011$ e $101$, tutte a 0; lo stesso succede per $010$ (vicini $000$, $011$, $110$) e per $111$ (vicini $110$, $101$, $011$). Nessun 1 si raggruppa, e la sintesi AND-OR è la forma canonica:
$$F = \bar{X}\bar{Y}Z + \bar{X}Y\bar{Z} + XYZ.$$

*Gli 0.* Gli zeri sono $000, 011, 100, 101, 110$. Lo 0 in $011$ ha tutti i vicini a 1 e resta solo: $(X + \bar{Y} + \bar{Z})$. Lo 0 in $000$ si può raggruppare solo con $100$ (gli altri vicini sono 1): gruppo con $Y = 0$, $Z = 0$, fattore $(Y + Z)$. Lo 0 in $101$ si raggruppa solo con $100$: $X = 1$, $Y = 0$, fattore $(\bar{X} + Y)$. Lo 0 in $110$ si raggruppa solo con $100$: $X = 1$, $Z = 0$, fattore $(\bar{X} + Z)$. Tutti e quattro i gruppi sono essenziali:
$$F = (Y + Z)(\bar{X} + Y)(\bar{X} + Z)(X + \bar{Y} + \bar{Z}).$$

*Costo.* Si contano le porte e gli ingressi delle porte, senza i NOT. La SOP ha tre AND a tre ingressi e una OR a tre ingressi: 4 porte e 12 ingressi. La POS ha tre OR a due ingressi, una OR a tre e una AND a quattro: 5 porte e 13 ingressi. Costa meno la SOP. Non c'è una regola generale: conviene raggruppare gli 1 quando sono pochi e gli 0 quando sono pochi gli 0, ma il conto va sempre fatto.

**Esercizio 7. Porta logica programmabile.** La rete ha due ingressi di controllo $F_1 F_0$ e due ingressi dati $A$, $B$. Con $F_1 F_0 = 00$ l'uscita è il NOR di $A$ e $B$, con $01$ lo XNOR, con $10$ la NAND; la combinazione $11$ non si presenta mai. Trovare la sintesi AND-OR minima.

Prima la tabella, riga per riga del controllo: NOR dà $1, 0, 0, 0$ per $AB = 00, 01, 10, 11$; XNOR dà $1, 0, 0, 1$; NAND dà $1, 1, 1, 0$. Poi la mappa, con righe $F_1 F_0$ e colonne $AB$ entrambe in ordine di Gray (attenzione: la riga $10$ è l'ultima, la $11$ la terza):

| $F_1 F_0 \backslash AB$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 1 | 0 | 0 | 0 |
| 01 | 1 | 0 | 1 | 0 |
| 11 | – | – | – | – |
| 10 | 1 | 1 | 0 | 1 |

I gruppi, usando le indifferenze della riga $11$: la colonna $AB = 00$ è tutta a 1 o indifferente, e dà $\bar{A}\bar{B}$; le celle $F_1 = 1$, $A = 0$ (righe 11 e 10, colonne 00 e 01) danno $F_1\bar{A}$; le celle $F_1 = 1$, $B = 0$ (righe 11 e 10, colonne 00 e 10) danno $F_1\bar{B}$; l'1 in $01\,11$ con l'indifferenza sotto di lui dà $F_0 AB$. Quindi
$$U = \bar{A}\bar{B} + F_1\bar{A} + F_1\bar{B} + F_0 AB.$$
Verifica sulle tre righe: con $F_1 F_0 = 00$ resta $\bar{A}\bar{B}$, il NOR; con $01$ resta $\bar{A}\bar{B} + AB$, lo XNOR; con $10$ resta $\bar{A}\bar{B} + \bar{A} + \bar{B} = \bar{A} + \bar{B}$, la NAND.

**Esercizio 8. Una funzione di quattro variabili con molte indifferenze.** La funzione $F(X, Y, Z, T)$ si comporta così: con $X = 0$ vale 1 per $YZT = 000, 010, 011, 111$ e 0 per le altre combinazioni; con $X = 1$ si presentano solo $YZT = 001$, in cui $F = 1$, e $YZT = 101$, in cui $F = 0$. Trovare la sintesi AND-OR minima.

Le combinazioni con $X = 1$ che non si presentano sono indifferenze. Mappa con righe $XY$ e colonne $ZT$:

| $XY \backslash ZT$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 1 | 0 | 1 | 1 |
| 01 | 0 | 0 | 1 | 0 |
| 11 | – | 0 | – | – |
| 10 | – | 1 | – | – |

Si parte dagli 1 che hanno meno possibilità. L'1 in $1001$ (riga 10, colonna 01) ha sopra lo 0 di $0001$ e sotto lo 0 di $1101$: si può allargare solo lungo la riga, che è tutta a 1 o indifferente, e il gruppo è $X\bar{Y}$. L'1 in $0111$ sta nella colonna $ZT = 11$, che non contiene 0: gruppo $ZT$, che copre anche $0011$. Restano $0000$ e $0010$: con le indifferenze della riga 10 formano la quaterna $\bar{Y}\bar{T}$ (righe 00 e 10, colonne 00 e 10). Quindi
$$F = ZT + X\bar{Y} + \bar{Y}\bar{T}.$$
Le indifferenze hanno permesso gruppi da quattro celle dove, senza, ci sarebbero state coppie o celle isolate.

**Esercizio 9. Analisi di un decoder con abilitazione.** Una rete a due livelli ha tre ingressi $EN$, $S_1$, $S_0$ e quattro uscite $U_0 = EN\,\bar{S}_1\bar{S}_0$, $U_1 = EN\,\bar{S}_1 S_0$, $U_2 = EN\,S_1\bar{S}_0$, $U_3 = EN\,S_1 S_0$. Che ruolo hanno gli ingressi?

Con $EN = 0$ tutte le uscite valgono 0, qualunque sia la selezione. Con $EN = 1$ si accende una sola uscita, quella il cui indice è il numero binario $S_1 S_0$: per $S_1 S_0 = 10$ vale 1 solo $U_2$. $S_1 S_0$ scelgono quindi *quale* uscita, ed $EN$ decide *se* accenderla. È il decoder 2→4 con abilitazione del modulo 2, cioè un DEMUX 1→4 in cui $EN$ fa da ingresso dati: con $n$ ingressi di selezione le uscite sono $2^n$. Con due di questi blocchi si fa un decoder 3→8: il bit più alto $S_2$ va sull'$EN$ del secondo blocco e, negato, sull'$EN$ del primo; gli altri due bit vanno su entrambi.

## Esercizi guidati

Ogni esercizio è diviso in passi. Conviene provare un passo alla volta, coprendo il resto, e confrontare solo dopo.

**Guidato 1. Una spia per i numeri primi.** Tre interruttori $A$, $B$, $C$ formano un numero binario $N = ABC$ ($A$ è il bit più significativo). La spia $U$ deve accendersi quando $N$ è un numero primo. Progettare la rete AND-OR e la rete OR-AND minime, e la versione a sole NAND.

*Passo 1: la specifica diventa una tabella.* $N$ va da 0 a 7; i primi sono 2, 3, 5, 7 (1 non è primo). Quindi $U = 1$ per $ABC = 010, 011, 101, 111$.

*Passo 2: la mappa.* Righe $A$, colonne $BC$:

| $A \backslash BC$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 |

*Passo 3: gli implicanti primi.* Sulla prima riga le celle $011$ e $010$ formano $\bar{A}B$. Sulla seconda riga $101$ e $111$ formano $AC$. C'è anche il gruppo verticale $BC$ (celle $011$ e $111$), che però copre solo 1 già coperti: è un implicante primo ma non essenziale. Gli essenziali sono $\bar{A}B$ (unico a coprire $010$) e $AC$ (unico a coprire $101$), e bastano:
$$U = \bar{A}B + AC.$$

*Passo 4: la sintesi OR-AND.* Gli 0 sono $000, 001, 100, 110$. La coppia $000$, $001$ ha $A = 0$, $B = 0$: fattore $(A + B)$. La coppia $100$, $110$ ha $A = 1$, $C = 0$: fattore $(\bar{A} + C)$. Quindi $U = (A + B)(\bar{A} + C)$.

*Passo 5: sole NAND.* Dalla SOP, negando due volte: $U = \overline{\overline{\bar{A}B} \cdot \overline{AC}}$. Servono una NAND per $\bar{A}B$, una per $AC$ e una finale, più il NOT di $A$ (una NAND con gli ingressi uniti).

*Passo 6: controllo.* Si prova una cella a 1 e una a 0 su tutte le forme. Per $N = 5$, $ABC = 101$: $\bar{A}B + AC = 0 + 1 = 1$ e $(A + B)(\bar{A} + C) = 1 \cdot 1 = 1$. Per $N = 6$, $ABC = 110$: $\bar{A}B + AC = 0 + 0 = 0$ e $(A + B)(\bar{A} + C) = 1 \cdot 0 = 0$.

**Guidato 2. Il segmento $a$ del visualizzatore a sette segmenti.** Un visualizzatore riceve una cifra decimale in BCD, $ABCD$ con $A$ più significativo, e accende il segmento $a$ (quello in alto) per le cifre 0, 2, 3, 5, 6, 7, 8, 9. Le combinazioni da 10 a 15 non arrivano mai. Trovare la sintesi AND-OR minima.

*Passo 1.* Gli 1 sono i mintermini 0, 2, 3, 5, 6, 7, 8, 9; gli 0 sono 1 e 4; le indifferenze sono da 10 a 15.

*Passo 2.* Mappa con righe $AB$ e colonne $CD$:

| $AB \backslash CD$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 1 | 0 | 1 | 1 |
| 01 | 0 | 1 | 1 | 1 |
| 11 | – | – | – | – |
| 10 | 1 | 1 | – | – |

*Passo 3: i gruppi più grandi.* Le righe $11$ e $10$ sono tutte a 1 o indifferenti: ottetto $A$. Le colonne $11$ e $10$ sono tutte a 1 o indifferenti: ottetto $C$. Restano $0101$ e $0000$. La cella $0101$ con $0111$, $1101$, $1111$ forma la quaterna $BD$. La cella $0000$ con $0010$, $1000$, $1010$ (i quattro angoli) forma la quaterna $\bar{B}\bar{D}$.

*Passo 4.*
$$a = A + C + BD + \bar{B}\bar{D} = A + C + \overline{B \oplus D}.$$
Senza le indifferenze, al posto di $A$ e di $C$ ci sarebbero gruppi più piccoli e più variabili per termine: è il caso tipico in cui le combinazioni impossibili fanno risparmiare molto.

*Passo 5: controllo sugli 0.* Per la cifra 1 ($0001$): $A = 0$, $C = 0$, $BD = 0$, $\bar{B}\bar{D} = 0$, e $a = 0$. Per la cifra 4 ($0100$): $BD = 0$ e $\bar{B}\bar{D} = 0$, quindi $a = 0$.

**Guidato 3. Semplificazione con l'algebra.** Semplificare $F = \overline{(\bar{A} + B)\,\bar{C}} + A\bar{B}C$.

*Passo 1: De Morgan sul prodotto negato.* $\overline{(\bar{A} + B)\,\bar{C}} = \overline{\bar{A} + B} + \bar{\bar{C}} = A\bar{B} + C$.

*Passo 2: assorbimento.* $F = A\bar{B} + C + A\bar{B}C$, e il termine $A\bar{B}C$ è assorbito da $A\bar{B}$ (anche da $C$): $F = A\bar{B} + C$.

*Passo 3: controllo con la tabella.* $F$ vale 0 solo quando $C = 0$ e $A\bar{B} = 0$, cioè per $ABC = 000, 010, 110$. Nella forma di partenza, per $ABC = 110$: $(\bar{A} + B)\bar{C} = 1$, il primo termine vale 0, il secondo pure, $F = 0$. Torna.

## Riepilogo

Una funzione booleana di $n$ variabili è descritta dalla sua tabella di verità, che ha $2^n$ righe; le funzioni possibili sono $2^{2^n}$. Le funzioni di una e due variabili sono realizzate dalle porte NOT, AND, OR, XOR e dalle loro negate. L'algebra di Boole permette di trasformare un'espressione in un'altra equivalente; le proprietà vengono a coppie per il principio di dualità, e le leggi di De Morgan scambiano somme e prodotti sotto negazione. Il teorema di Shannon dà le due forme canoniche: la somma dei mintermini degli 1 e il prodotto dei maxtermini degli 0, da cui le reti a due livelli AND-OR e OR-AND. Le mappe di Karnaugh rendono visibili le adiacenze: si coprono gli 1 (o gli 0) con il minimo numero di gruppi rettangolari di $2^k$ celle, i più grandi possibile, usando gli implicanti primi essenziali. Le indifferenze si usano solo se allargano i gruppi; le variabili riportate permettono di sintetizzare con mappe più piccole una funzione di più variabili, con un risultato quasi minimo. Le porte NAND e NOR sono complete da sole, e una rete AND-OR diventa una rete di sole NAND con la stessa struttura.

## Formulario

Il formulario raccoglie quello che serve avere sotto mano negli esercizi e all'orale. Non sostituisce le spiegazioni: ogni riga rimanda a un paragrafo del modulo.

### Conteggi e forme

| Che cosa | Formula o regola | Par. |
|---|---|---|
| Combinazioni di $n$ ingressi | $2^n$ righe della tabella | 1.1 |
| Funzioni distinte di $n$ variabili | $2^{2^n}$ (16 per $n = 2$) | 1.1 |
| Mintermine di una riga | prodotto di tutte le variabili, negata dove vale 0 | 1.4 |
| Maxtermine di una riga | somma di tutte le variabili, negata dove vale 1 | 1.4 |
| Prima forma canonica (SOP) | somma dei mintermini delle righe con $f = 1$ | 1.4 |
| Seconda forma canonica (POS) | prodotto dei maxtermini delle righe con $f = 0$ | 1.4 |
| Gruppo di $2^k$ celle su $n$ variabili | prodotto (o somma) di $n - k$ variabili | 1.5 |

### Identità che si usano di più

$$A + \bar{A}B = A + B \qquad A(\bar{A} + B) = AB \qquad A + AB = A \qquad A + BC = (A + B)(A + C)$$

$$\overline{A + B + C} = \bar{A}\,\bar{B}\,\bar{C} \qquad \overline{ABC} = \bar{A} + \bar{B} + \bar{C} \qquad AB + \bar{A}C + BC = AB + \bar{A}C$$

$$A \oplus B = A\bar{B} + \bar{A}B \qquad \overline{A \oplus B} = AB + \bar{A}\bar{B} \qquad A \oplus 1 = \bar{A} \qquad A \oplus A = 0$$

### Teoremi

- **Shannon:** $f = \bar{x}_1\, f(0, x_2, \dots) + x_1\, f(1, x_2, \dots)$ e, nella forma duale, $f = (x_1 + f(0, \dots))(\bar{x}_1 + f(1, \dots))$.
- **Dualità:** un'identità resta vera scambiando $+$ con $\cdot$ e 0 con 1.
- **Completezza:** {AND, OR, NOT}, {NAND} e {NOR} bastano a realizzare ogni funzione.
- **Da AND-OR a NAND:** $AB + CD = \overline{\overline{AB} \cdot \overline{CD}}$; **da OR-AND a NOR:** $(A + B)(C + D) = \overline{\overline{A + B} + \overline{C + D}}$.

### Mappe di Karnaugh: la procedura

1. Ordine di Gray su righe e colonne (00, 01, 11, 10); i bordi opposti sono adiacenti.
2. Si individuano gli implicanti primi, gruppi rettangolari di $2^k$ celle più grandi possibile.
3. Si prendono gli essenziali (coprono un 1 che nessun altro copre), poi si coprono gli 1 rimasti con il minimo numero di primi.
4. Indifferenze: si usano solo se allargano un gruppo, non vanno mai coperte per forza.
5. POS: si raggruppano gli 0; nel fattore la variabile è negata se nel gruppo vale 1.
6. Controllo finale su almeno una cella a 1 e una a 0.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Variabile booleana, bit | grandezza con due soli valori, 0 e 1 |
| Rete combinatoria | rete le cui uscite dipendono solo dagli ingressi presenti |
| Tabella di verità | elenco dell'uscita per tutte le $2^n$ combinazioni: è la specifica |
| Induzione perfetta | dimostrazione di un'identità controllando tutte le combinazioni |
| Rete a due livelli | AND-OR o OR-AND: ogni segnale attraversa al più due porte, è la più veloce |
| Implicante | prodotto che, quando vale 1, fa valere 1 la funzione |
| Implicante primo | implicante non contenuto in uno più grande |
| Implicante essenziale | implicante primo che copre un 1 coperto da nessun altro |
| Indifferenza (*don't care*) | combinazione che non si presenta o il cui valore non interessa |
| Variabile riportata | variabile scritta in una cella della mappa; dà una sintesi quasi minima |
| Termine di consenso | prodotto ridondante $BC$ ottenuto da $AB$ e $\bar{A}C$ |
| Funzione di parità | XOR di più variabili; mappa a scacchiera, nessun gruppo possibile |
| Costo di una rete | numero di porte e di ingressi delle porte (i NOT sugli ingressi non si contano) |
| Completezza funzionale | proprietà di un insieme di porte di realizzare ogni funzione |

### Domande che tornano spesso

- Perché le funzioni di $n$ variabili sono $2^{2^n}$?
- Enunciare e dimostrare il teorema di Shannon; come se ne ricavano le forme canoniche?
- Perché nella mappa si usa il codice Gray? Quando due celle sono adiacenti?
- Differenza fra implicante primo ed essenziale, con un esempio.
- Come si usano le indifferenze, e perché non si devono coprire per forza?
- Perché la NAND è funzionalmente completa? Come si passa da una rete AND-OR a una di sole NAND?
- Perché le funzioni di parità sono il caso peggiore per le reti a due livelli?
