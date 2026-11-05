---
corso: Fondamenti di Informatica
modulo: 1
titolo: Insiemi, relazioni e funzioni
programma: [FI-01, FI-02]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 1 · Insiemi, relazioni e funzioni

**In questo modulo.** Non servono prerequisiti oltre all'aritmetica delle superiori. È la prima parte di matematica discreta del corso: il linguaggio degli insiemi, che poi torna nella programmazione (un tipo di dato è un insieme di valori, una funzione C++ realizza una funzione matematica, una relazione d'ordine è quella che usa un algoritmo di ordinamento). Si vedono gli insiemi e le loro operazioni, il prodotto cartesiano, le relazioni con le loro proprietà, le relazioni di equivalenza con le classi e le partizioni, le relazioni d'ordine con massimi, minimi, maggioranti ed estremi, e le funzioni con immagine, controimmagine, iniettività e suriettività. Alla fine del modulo si sanno risolvere gli esercizi "sì o no" della prova di teoria su un insieme, un ordine o una funzione dati, e contare relazioni e funzioni fra insiemi finiti.

Gli esercizi seguono il modello delle prove d'esame 2016-2020.

## 1.1 Insiemi e sottoinsiemi

Un **insieme** è una collezione di oggetti, i suoi **elementi**. Si descrive per elencazione, $S = \{g, 1, +\}$, oppure con una proprietà caratteristica, $T = \{x : x \text{ è una vocale}\}$. L'ordine in cui si elencano gli elementi non conta, e un elemento ripetuto conta una volta sola: $\{1, 2\} = \{2, 1\} = \{1, 1, 2\}$. Si scrive $x \in A$ se $x$ appartiene ad $A$, $x \notin A$ altrimenti. L'**insieme vuoto** $\emptyset$ non ha elementi; un insieme con un solo elemento, come $\{m\}$, si dice **singoletto**.

Gli insiemi numerici del corso: $\mathbb N_0 = \{0, 1, 2, \dots\}$ i naturali con lo zero, $\mathbb N = \{1, 2, 3, \dots\}$ i naturali senza lo zero, $\mathbb Z$ gli interi, $\mathbb Q$ i razionali, $\mathbb R$ i reali, $\mathbb C$ i complessi. Attenzione: in altri corsi $\mathbb N$ comprende lo zero; qui no.

La **cardinalità** (o ordine) $|A|$ è il numero degli elementi di $A$: $|\{g, 1, +\}| = 3$, $|\emptyset| = 0$. Un insieme è finito se la sua cardinalità è un numero naturale, altrimenti è infinito.

$A$ è **contenuto** in $B$ (è un **sottoinsieme** di $B$), $A \subseteq B$, se ogni elemento di $A$ è elemento di $B$:
$$A \subseteq B \iff (\forall x)(x \in A \Rightarrow x \in B).$$
$A$ è contenuto **strettamente** in $B$, $A \subset B$, se $A \subseteq B$ e $A \ne B$, cioè se in più c'è almeno un elemento di $B$ che non sta in $A$. Per ogni insieme $A$ valgono $\emptyset \subseteq A$ e $A \subseteq A$, e l'inclusione è transitiva: se $A \subseteq B$ e $B \subseteq C$ allora $A \subseteq C$. Due insiemi sono **uguali** se hanno gli stessi elementi, cioè se $A \subseteq B$ e $B \subseteq A$: è il metodo della **doppia inclusione**, che si usa per dimostrare le uguaglianze fra insiemi.

Bisogna distinguere appartenenza e inclusione. Se $x \in A$ allora $\{x\} \subseteq A$, ma non $\{x\} \in A$ (a meno che l'insieme $\{x\}$ sia proprio uno degli elementi di $A$). E $\emptyset \ne \{\emptyset\}$: il primo non ha elementi, il secondo ne ha uno, l'insieme vuoto.

L'**insieme delle parti** (o insieme potenza) di $A$ è l'insieme di tutti i sottoinsiemi di $A$:
$$\mathcal P(A) = \{X : X \subseteq A\}.$$
Per $H = \{3, 5, 8\}$: $\mathcal P(H) = \{\emptyset, \{3\}, \{5\}, \{8\}, \{3, 5\}, \{3, 8\}, \{5, 8\}, H\}$. Contiene sempre $\emptyset$ e $A$, quindi non è mai vuoto.

> [!teorema] Cardinalità dell'insieme delle parti
> Se $|A| = n$, allora $|\mathcal P(A)| = 2^n$.

Per costruire un sottoinsieme si decide, per ciascuno degli $n$ elementi, se metterlo dentro o no: sono $n$ scelte indipendenti fra due possibilità, quindi $2 \cdot 2 \cdots 2 = 2^n$ sottoinsiemi (è il principio del prodotto del modulo 2).

## 1.2 Operazioni fra insiemi

Dati due insiemi $A$ e $B$:

- **unione** $A \cup B = \{x : x \in A \vee x \in B\}$;
- **intersezione** $A \cap B = \{x : x \in A \wedge x \in B\}$; se è vuota, $A$ e $B$ sono **disgiunti**;
- **differenza** $A \setminus B = \{x : x \in A \wedge x \notin B\}$;
- **complemento** di $A$ rispetto a un insieme universo $U$ che lo contiene: $\overline A = U \setminus A$;
- **differenza simmetrica** $A \,\Delta\, B = (A \setminus B) \cup (B \setminus A)$, gli elementi che stanno in uno solo dei due.

Le operazioni si visualizzano con i **diagrammi di Venn**. Valgono le proprietà commutativa e associativa di unione e intersezione, le distributive
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C), \qquad A \cup (B \cap C) = (A \cup B) \cap (A \cup C),$$
e le **leggi di De Morgan**
$$\overline{A \cup B} = \overline A \cap \overline B, \qquad \overline{A \cap B} = \overline A \cup \overline B.$$

Sono le stesse leggi della logica (unione come "o", intersezione come "e", complemento come "non"), e torneranno nelle condizioni dei programmi: `!(a || b)` equivale a `!a && !b`.

Per contare gli elementi di un'unione di insiemi finiti si usa il **principio di inclusione-esclusione**:
$$|A \cup B| = |A| + |B| - |A \cap B|, \qquad |A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|.$$
Sommando $|A|$ e $|B|$ gli elementi comuni si contano due volte, e vanno tolti una volta.

**Prodotto cartesiano.** Una **coppia ordinata** $(a, b)$ è diversa da $(b, a)$ se $a \ne b$: conta l'ordine, a differenza dell'insieme $\{a, b\}$. Il prodotto cartesiano di $A$ e $B$ è l'insieme delle coppie con il primo elemento in $A$ e il secondo in $B$:
$$A \times B = \{(a, b) : a \in A, b \in B\}, \qquad |A \times B| = |A| \cdot |B|.$$
In generale $A \times B \ne B \times A$. Il prodotto $A \times A$ si scrive anche $A^2$, e allo stesso modo si definiscono le terne, le $n$-uple e $A^n$.

**Partizioni.** Una **partizione** di $A$ è una famiglia di sottoinsiemi di $A$ non vuoti, disgiunti a due a due, la cui unione è $A$. Per esempio $\{\{1, 4\}, \{2\}, \{3, 5\}\}$ è una partizione di $\{1, 2, 3, 4, 5\}$; $\{\{1, 4\}, \{2, 4\}, \{3, 5\}\}$ no, perché il 4 sta in due blocchi.

## 1.3 Relazioni

Una **relazione** fra $A$ e $B$ è un sottoinsieme $R \subseteq A \times B$; si scrive $a \,R\, b$ per $(a, b) \in R$. Se $A = B$ si parla di relazione su $A$. Poiché le relazioni sono i sottoinsiemi di $A \times B$, il loro numero è
$$|\mathcal P(A \times B)| = 2^{|A| \cdot |B|}.$$
La relazione **inversa** è $R^{-1} = \{(b, a) : (a, b) \in R\}$.

Una relazione su un insieme finito si può rappresentare con l'elenco delle coppie, con una **matrice booleana** (riga $a$, colonna $b$, 1 se $a \,R\, b$) o con un **grafo orientato** (una freccia da $a$ a $b$ se $a \,R\, b$, un cappio se $a \,R\, a$).

Una relazione $R$ su $A$ è:

| Proprietà | Definizione | Nella matrice o nel grafo |
|---|---|---|
| riflessiva | $a \,R\, a$ per ogni $a \in A$ | diagonale tutta a 1; un cappio su ogni nodo |
| simmetrica | $a \,R\, b \Rightarrow b \,R\, a$ | matrice simmetrica; frecce sempre in coppia |
| antisimmetrica | $a \,R\, b \wedge b \,R\, a \Rightarrow a = b$ | mai due frecce opposte fra nodi diversi |
| transitiva | $a \,R\, b \wedge b \,R\, c \Rightarrow a \,R\, c$ | ogni percorso di due frecce ha la "scorciatoia" |

Simmetrica e antisimmetrica non sono l'una il contrario dell'altra: la relazione di uguaglianza è entrambe le cose, e una relazione può non essere né l'una né l'altra.

**Relazioni di equivalenza.** Una relazione riflessiva, simmetrica e transitiva si dice **di equivalenza** (si scrive spesso $a \sim b$). La **classe di equivalenza** di $a$ è l'insieme degli elementi equivalenti ad $a$, $[a] = \{x \in A : x \sim a\}$; l'insieme delle classi è l'**insieme quoziente** $A/\!\sim$.

> [!teorema] Equivalenze e partizioni
> Le classi di una relazione di equivalenza su $A$ formano una partizione di $A$. Viceversa, ogni partizione di $A$ definisce un'equivalenza: due elementi sono equivalenti se stanno nello stesso blocco.

Le classi non sono vuote ($a \in [a]$ per la riflessività), coprono $A$, e due classi sono disgiunte o coincidono: se $c \in [a] \cap [b]$, per simmetria e transitività ogni elemento equivalente ad $a$ lo è anche a $b$, quindi $[a] = [b]$.

Esempio importante: su $\mathbb Z$, $a \equiv b \pmod n$ se $n$ divide $a - b$ (**congruenza modulo $n$**). È un'equivalenza, le classi sono $n$, una per ogni resto della divisione per $n$: $[0], [1], \dots, [n - 1]$. Per $n = 2$ le classi sono i pari e i dispari.

## 1.4 Relazioni d'ordine

Una relazione riflessiva, **antisimmetrica** e transitiva è una **relazione d'ordine** (si scrive spesso $\le$), e $(A, \le)$ è un **insieme ordinato**. Due elementi sono **confrontabili** se $a \le b$ oppure $b \le a$. L'ordine è **totale** se tutte le coppie sono confrontabili, **parziale** altrimenti.

Esempi: $(\mathbb N, \le)$ con l'ordine usuale è totale. $(\mathbb N, \mid)$ con la divisibilità ($a \mid b$ se $a$ divide $b$) è parziale: 2 e 3 non sono confrontabili. $(\mathcal P(A), \subseteq)$ è parziale se $|A| \ge 2$: $\{1\}$ e $\{2\}$ non sono confrontabili.

Un ordine su un insieme finito si disegna con il **diagramma di Hasse**: un punto per elemento, $b$ più in alto di $a$ se $a < b$, e un segmento solo fra $a$ e $b$ quando $b$ "copre" $a$, cioè $a < b$ senza elementi in mezzo. Riflessività e transitività restano sottintese. Per i divisori di 12 con la divisibilità, $\{1, 2, 3, 4, 6, 12\}$: 1 in basso, sopra 2 e 3, sopra il 2 il 4 e il 6 (il 6 anche sopra il 3), in cima 12, collegato a 4 e 6.

**Elementi particolari.** Sia $(A, \le)$ ordinato e $X \subseteq A$ non vuoto.

| Nome | Definizione |
|---|---|
| massimo di $X$ | $M \in X$ e $x \le M$ per ogni $x \in X$ |
| minimo di $X$ | $m \in X$ e $m \le x$ per ogni $x \in X$ |
| massimale di $X$ | elemento di $X$ senza elementi di $X$ strettamente maggiori |
| minimale di $X$ | elemento di $X$ senza elementi di $X$ strettamente minori |
| maggiorante di $X$ in $A$ | $u \in A$ confrontabile con ogni $x \in X$ e $x \le u$ per ogni $x$ |
| minorante di $X$ in $A$ | $v \in A$ confrontabile con ogni $x \in X$ e $v \le x$ per ogni $x$ |
| estremo superiore | minimo dei maggioranti (se esiste) |
| estremo inferiore | massimo dei minoranti (se esiste) |

Massimo e minimo, se esistono, sono unici e appartengono a $X$; i massimali e i minimali possono essere più di uno. Maggioranti e minoranti stanno in $A$, non necessariamente in $X$. Se il massimo esiste è anche l'unico massimale e l'estremo superiore; in un ordine totale massimale e massimo coincidono.

Nei divisori di 12, per $X = \{4, 6\}$: non c'è massimo (4 e 6 non sono confrontabili), entrambi sono massimali; i maggioranti sono i multipli comuni in $A$, cioè solo 12, che è l'estremo superiore; i minoranti sono 1 e 2, e l'estremo inferiore è 2. Con la divisibilità, estremo superiore ed estremo inferiore sono il minimo comune multiplo e il massimo comune divisore.

## 1.5 Funzioni

Una **funzione** (o applicazione) $f : A \to B$ è una relazione fra $A$ e $B$ in cui ogni elemento di $A$ è in relazione con **uno e un solo** elemento di $B$, la sua **immagine** $f(a)$. $A$ è il **dominio**, $B$ il **codominio**. Non tutte le relazioni sono funzioni: in una funzione da ogni elemento del dominio parte esattamente una freccia.

L'**immagine** di un sottoinsieme $X \subseteq A$ è $f(X) = \{f(x) : x \in X\}$, e $f(A)$ si chiama immagine di $f$. La **controimmagine** di $Y \subseteq B$ è $f^{-1}(Y) = \{a \in A : f(a) \in Y\}$: è sempre definita, anche quando la funzione non è invertibile, e può essere vuota.

| Proprietà | Definizione | Significato |
|---|---|---|
| iniettiva | $a_1 \ne a_2 \Rightarrow f(a_1) \ne f(a_2)$ | elementi diversi hanno immagini diverse |
| suriettiva | $f(A) = B$ | ogni elemento del codominio è immagine di qualcuno |
| biiettiva | iniettiva e suriettiva | corrispondenza uno a uno |

Per dimostrare l'iniettività conviene la forma equivalente $f(a_1) = f(a_2) \Rightarrow a_1 = a_2$; per smentirla basta trovare due elementi diversi con la stessa immagine. Per esempio $f : \mathbb Z \to \mathbb Z$, $f(x) = 2x + 1$ è iniettiva ($2a_1 + 1 = 2a_2 + 1 \Rightarrow a_1 = a_2$) ma non suriettiva (i pari non sono immagini); $g : \mathbb Z \to \mathbb N_0$, $g(x) = |x|$ è suriettiva ma non iniettiva ($g(-1) = g(1)$).

La **composizione** di $f : A \to B$ e $g : B \to C$ è $g \circ f : A \to C$, $(g \circ f)(a) = g(f(a))$; non è commutativa. Una funzione biiettiva ha la **funzione inversa** $f^{-1} : B \to A$, con $f^{-1}(f(a)) = a$; solo le biiezioni sono invertibili.

**Contare le funzioni.** Se $|A| = k$ e $|B| = n$:

- le funzioni $A \to B$ sono $n^k$ (ogni elemento di $A$ sceglie la sua immagine fra $n$);
- quelle iniettive sono $n (n - 1) \cdots (n - k + 1)$ se $k \le n$, e nessuna se $k > n$;
- se $k = n$ le biiezioni sono $n!$.

Il caso $k > n$ è il **principio dei cassetti**: se si mettono $k$ oggetti in $n < k$ cassetti, almeno un cassetto ne contiene due.

Fra insiemi infiniti si confrontano le cardinalità con le biiezioni: due insiemi sono **equipotenti** se esiste una biiezione fra loro. $\mathbb N$, $\mathbb Z$ e $\mathbb Q$ sono equipotenti (insiemi **numerabili**), $\mathbb R$ no: è "più grande".

## Esempi ed esercizi svolti

**Esercizio 1. Sì o no sull'insieme delle parti.** $A = \{2, x, \#\}$, $\mathcal P(A)$ con $X \,R\, Y \iff X \subseteq Y$.

| Affermazione | Risposta | Perché |
|---|---|---|
| $(\mathcal P(A), R)$ è un insieme ordinato | sì | l'inclusione è riflessiva, antisimmetrica, transitiva |
| è totalmente ordinato | no | $\{2\}$ e $\{x\}$ non sono confrontabili |
| $A$ è il massimo | sì | ogni sottoinsieme è contenuto in $A$ |
| $\{2\}$ è l'unico minimale | no | l'unico minimale è $\emptyset$, che è anche il minimo |
| $(\{2, x\}, \{x, \#\}) \in R$ | no | $2 \notin \{x, \#\}$ |
| $\lvert \mathcal P(A)\rvert = 8$ | sì | $2^3$ |
| i maggioranti di $\{\{2\}, \{x\}\}$ sono $\{2, x\}$ e $A$ | sì | sono i sottoinsiemi che contengono 2 e $x$ |
| l'estremo superiore di $\{\{2\}, \{x\}\}$ è $\{2, x\}$ | sì | il minimo dei maggioranti; in generale è l'unione |

Con $f : \mathcal P(A) \to \mathbb N_0$, $f(X) = |X|$:

| Affermazione | Risposta | Perché |
|---|---|---|
| $f(\emptyset) = 1$ | no | $f(\emptyset) = 0$ |
| $f(\{\{x\}, \{2, \#\}\}) = \{1, 2\}$ | sì | le cardinalità dei due elementi |
| $f^{-1}(\{2\}) = \{\{2, x\}, \{2, \#\}, \{x, \#\}\}$ | sì | i sottoinsiemi con due elementi |
| $f^{-1}(\{5\}) = \emptyset$ | sì | nessun sottoinsieme ha 5 elementi |
| $f$ è iniettiva | no | $f(\{2\}) = f(\{x\}) = 1$ |
| $f$ è suriettiva | no | 4 non è immagine di nulla |

**Esercizio 2. Riconoscere un'equivalenza.** Su $A = \{1, 2, 3, 4\}$, $R = \{(1,1), (2,2), (3,3), (4,4), (1,2), (2,1), (3,4), (4,3)\}$.

Riflessiva: le quattro coppie $(a, a)$ ci sono. Simmetrica: $(1,2)$ e $(2,1)$, $(3,4)$ e $(4,3)$. Transitiva: le uniche catene sono del tipo $1 \,R\, 2 \,R\, 1$, che richiede $1 \,R\, 1$, presente, e così via. È un'equivalenza, con classi $[1] = \{1, 2\}$ e $[3] = \{3, 4\}$: l'insieme quoziente è $\{\{1, 2\}, \{3, 4\}\}$, una partizione di $A$. Non è antisimmetrica: $(1,2)$ e $(2,1)$ con $1 \ne 2$.

**Esercizio 3. Proprietà di tre relazioni su $\mathbb Z$.**

(a) $a \,R\, b \iff a - b$ è pari: riflessiva ($0$ è pari), simmetrica ($b - a = -(a - b)$), transitiva ($a - c = (a - b) + (b - c)$): equivalenza, con classi pari e dispari. È la congruenza modulo 2.

(b) $a \,S\, b \iff a < b$: non riflessiva, non simmetrica, antisimmetrica (la premessa $a < b \wedge b < a$ non è mai vera), transitiva. Non è un ordine perché non è riflessiva: è un ordine **stretto**.

(c) $a \,T\, b \iff |a - b| \le 1$: riflessiva e simmetrica, ma non transitiva: $0 \,T\, 1$ e $1 \,T\, 2$, ma non $0 \,T\, 2$.

**Esercizio 4. Divisori con la divisibilità.** In $D = \{1, 2, 3, 4, 6, 12\}$ ordinato da $\mid$, trovare massimo, minimo e, per $X = \{2, 3\}$ e $Y = \{2, 4\}$, maggioranti, minoranti ed estremi.

$D$ ha massimo 12 e minimo 1. $X = \{2, 3\}$: maggioranti 6 e 12, estremo superiore 6; minoranti solo 1, estremo inferiore 1; $X$ non ha massimo né minimo. $Y = \{2, 4\}$: $2 \mid 4$, quindi $Y$ ha minimo 2 e massimo 4; i maggioranti sono 4 e 12 (estremo superiore 4, che appartiene a $Y$), i minoranti 1 e 2 (estremo inferiore 2).

**Esercizio 5. Contare relazioni e funzioni.** $|A| = 3$, $|B| = 2$.

Relazioni fra $A$ e $B$: $2^{3 \cdot 2} = 64$. Funzioni $A \to B$: $2^3 = 8$; nessuna è iniettiva (principio dei cassetti); le suriettive sono le 8 meno le 2 costanti, cioè 6. Funzioni $B \to A$: $3^2 = 9$, di cui iniettive $3 \cdot 2 = 6$, e nessuna suriettiva.

**Esercizio 6. Inclusione-esclusione.** Su 40 studenti, 25 hanno usato il C++, 18 il Python e 10 entrambi. Quanti nessuno dei due?

$|C \cup P| = 25 + 18 - 10 = 33$, quindi $40 - 33 = 7$ studenti non hanno usato nessuno dei due. Solo il C++: $25 - 10 = 15$.

**Esercizio 7. Una dimostrazione per doppia inclusione.** Dimostrare che $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$.

($\subseteq$) Se $x \in A \setminus (B \cup C)$, allora $x \in A$ e $x \notin B \cup C$, cioè $x \notin B$ e $x \notin C$; quindi $x \in A \setminus B$ e $x \in A \setminus C$. ($\supseteq$) Se $x$ sta in entrambe le differenze, allora $x \in A$, $x \notin B$, $x \notin C$, quindi $x \notin B \cup C$ e $x \in A \setminus (B \cup C)$. È la legge di De Morgan dentro $A$.

**Esercizio 8. Composizione.** $f : \mathbb Z \to \mathbb Z$, $f(x) = 2x + 1$ e $g : \mathbb Z \to \mathbb N_0$, $g(x) = |x|$. Calcolare $g \circ f$ e dire se è iniettiva.

$(g \circ f)(x) = |2x + 1|$. Non è iniettiva: $(g \circ f)(0) = 1 = (g \circ f)(-1)$. La composizione di una funzione iniettiva con una non iniettiva può perdere l'iniettività; la composizione di due funzioni iniettive è sempre iniettiva.

### Esercizi più impegnativi

**Esercizio 9. Le frazioni come classi di equivalenza.** Su $\mathbb Z \times (\mathbb Z \setminus \{0\})$ si pone $(a, b) \sim (c, d) \iff ad = bc$. Dimostrare che è un'equivalenza e descrivere le classi.

Riflessiva: $ab = ba$. Simmetrica: da $ad = bc$ segue $cb = da$. Transitiva, la parte delicata: se $(a, b) \sim (c, d)$ e $(c, d) \sim (e, f)$, cioè $ad = bc$ e $cf = de$, moltiplicando la prima per $f$ e usando la seconda si ha $adf = bcf = bde$, quindi $d(af - be) = 0$; poiché $d \ne 0$ (è un secondo elemento), $af = be$, cioè $(a, b) \sim (e, f)$. Qui serve proprio che i secondi elementi non siano nulli: con $d = 0$ si avrebbe $(1, 1) \sim (0, 0) \sim (2, 1)$ senza che $(1, 1) \sim (2, 1)$. Le classi sono i numeri razionali: $[(1, 2)] = \{(1, 2), (2, 4), (-3, -6), \dots\}$ è $\frac12$. È il modo in cui la matematica costruisce $\mathbb Q$ a partire da $\mathbb Z$.

**Esercizio 10. Quante equivalenze su un insieme di quattro elementi?** Le equivalenze su $A$ sono tante quante le partizioni di $A$ (teorema di 1.3). Per $A = \{1, 2, 3, 4\}$ si contano le partizioni per forma dei blocchi:

| Blocchi | Esempio | Quante |
|---|---|---|
| un blocco di 4 | $\{1234\}$ | 1 |
| 3 + 1 | $\{123\}\{4\}$ | $\binom{4}{3} = 4$ |
| 2 + 2 | $\{12\}\{34\}$ | $\binom{4}{2} / 2 = 3$ |
| 2 + 1 + 1 | $\{12\}\{3\}\{4\}$ | $\binom{4}{2} = 6$ |
| 1 + 1 + 1 + 1 | $\{1\}\{2\}\{3\}\{4\}$ | 1 |

In tutto 15. Nella riga 2 + 2 si divide per 2 perché scegliere $\{12\}$ o $\{34\}$ come "primo" blocco dà la stessa partizione: è l'errore tipico di questo conteggio.

**Esercizio 11. Composizione e iniettività.** Dimostrare che se $f : A \to B$ e $g : B \to C$ sono iniettive allora $g \circ f$ è iniettiva, e che se $g \circ f$ è iniettiva allora $f$ lo è, mentre $g$ può non esserlo.

(1) Se $g(f(a_1)) = g(f(a_2))$, per l'iniettività di $g$ si ha $f(a_1) = f(a_2)$, e per quella di $f$, $a_1 = a_2$. (2) Se $f(a_1) = f(a_2)$, applicando $g$ si ha $(g \circ f)(a_1) = (g \circ f)(a_2)$, e quindi $a_1 = a_2$. (3) Controesempio per $g$: $A = \{1\}$, $B = \{1, 2\}$, $C = \{1\}$, $f(1) = 1$, $g$ costante. $g \circ f$ ha dominio con un solo elemento, quindi è iniettiva, ma $g(1) = g(2)$. Il controesempio più piccolo possibile è spesso il più convincente all'orale.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. È un ordine? Disegnare il diagramma.** Su $A = \{a, b, c, d\}$: $R = \{(a,a), (b,b), (c,c), (d,d), (a,b), (a,c), (a,d), (b,d), (c,d)\}$.

*Passo 1: riflessiva.* Ci sono tutte le coppie $(x, x)$: sì.

*Passo 2: antisimmetrica.* Fra elementi diversi c'è sempre al più una delle due coppie: sì.

*Passo 3: transitiva.* Le catene di due coppie con elementi diversi sono $a \,R\, b \,R\, d$ e $a \,R\, c \,R\, d$; entrambe richiedono $(a, d)$, che c'è: sì. È un ordine.

*Passo 4: Hasse.* $a$ in basso, sopra $b$ e $c$ (non confrontabili fra loro), in cima $d$. Il segmento $a$-$d$ non si disegna: si ottiene passando da $b$ o da $c$.

*Passo 5: elementi particolari.* Minimo $a$, massimo $d$. Per $X = \{b, c\}$: due massimali e due minimali ($b$ e $c$), estremo superiore $d$, estremo inferiore $a$. L'ordine non è totale.

**Guidato 2. Le classi della congruenza modulo 4.** Su $A = \{0, 1, \dots, 11\}$, $a \sim b$ se $4 \mid (a - b)$.

*Passo 1: è un'equivalenza.* È la congruenza modulo 4 ristretta ad $A$.

*Passo 2: le classi.* Si raggruppano gli elementi per resto: $[0] = \{0, 4, 8\}$, $[1] = \{1, 5, 9\}$, $[2] = \{2, 6, 10\}$, $[3] = \{3, 7, 11\}$.

*Passo 3: il controllo.* Sono 4 classi di 3 elementi, disgiunte, con unione $A$: $4 \times 3 = 12 = |A|$.

**Guidato 3. Immagine e controimmagine.** $f : \{1, 2, 3, 4, 5, 6\} \to \mathbb N_0$, $f(n) = n \bmod 3$.

*Passo 1: la tabella.* $f(1) = 1$, $f(2) = 2$, $f(3) = 0$, $f(4) = 1$, $f(5) = 2$, $f(6) = 0$.

*Passo 2: immagini.* $f(\{1, 4, 6\}) = \{0, 1\}$; l'immagine di $f$ è $\{0, 1, 2\}$.

*Passo 3: controimmagini.* $f^{-1}(\{0\}) = \{3, 6\}$; $f^{-1}(\{1, 2\}) = \{1, 2, 4, 5\}$; $f^{-1}(\{7\}) = \emptyset$.

*Passo 4: proprietà.* Non è iniettiva ($f(1) = f(4)$), non è suriettiva su $\mathbb N_0$. Le controimmagini dei singoli valori, $\{3, 6\}$, $\{1, 4\}$, $\{2, 5\}$, formano una partizione del dominio: è sempre così, e la relazione "hanno la stessa immagine" è un'equivalenza.

## Riepilogo

Un insieme è determinato dai suoi elementi; l'inclusione si controlla elemento per elemento e l'uguaglianza con la doppia inclusione; l'insieme delle parti di un insieme con $n$ elementi ne ha $2^n$. Unione, intersezione, differenza, complemento e differenza simmetrica seguono le leggi della logica, comprese le leggi di De Morgan; il principio di inclusione-esclusione conta gli elementi di un'unione. Il prodotto cartesiano è fatto di coppie ordinate e ha $|A| \cdot |B|$ elementi. Una relazione è un sottoinsieme del prodotto cartesiano: fra $A$ e $B$ ce ne sono $2^{|A||B|}$. Le relazioni riflessive, simmetriche e transitive sono equivalenze, e le loro classi formano una partizione; le riflessive, antisimmetriche e transitive sono ordini, totali o parziali, con massimi, minimi, massimali, minimali, maggioranti, minoranti ed estremi. Una funzione associa a ogni elemento del dominio una sola immagine; può essere iniettiva, suriettiva o biiettiva, e solo nell'ultimo caso è invertibile; fra insiemi finiti le funzioni sono $n^k$.

## Formulario

### Conteggi

$$|\mathcal P(A)| = 2^{|A|}, \qquad |A \times B| = |A||B|, \qquad \#\text{relazioni} = 2^{|A||B|}, \qquad \#\text{funzioni } A \to B = |B|^{|A|},$$
$$\#\text{iniettive} = \frac{n!}{(n - k)!} \ (k \le n), \qquad \#\text{biiezioni} = n!, \qquad |A \cup B| = |A| + |B| - |A \cap B|.$$

### Leggi

$$\overline{A \cup B} = \overline A \cap \overline B, \quad \overline{A \cap B} = \overline A \cup \overline B, \quad A \cap (B \cup C) = (A \cap B) \cup (A \cap C), \quad A \,\Delta\, B = (A \setminus B) \cup (B \setminus A).$$

### Proprietà delle relazioni

| Tipo | Riflessiva | Simmetrica | Antisimmetrica | Transitiva |
|---|---|---|---|---|
| equivalenza | sì | sì | – | sì |
| ordine | sì | – | sì | sì |
| ordine stretto | no | – | sì | sì |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Sottoinsieme proprio | contenuto e diverso |
| Partizione | blocchi non vuoti, disgiunti, che coprono l'insieme |
| Classe di equivalenza, insieme quoziente | elementi equivalenti a uno dato; insieme delle classi |
| Confrontabili | $a \le b$ oppure $b \le a$ |
| Massimale | nessuno strettamente più grande in $X$ |
| Maggiorante | in $A$, più grande o uguale di tutti gli elementi di $X$ |
| Estremo superiore | il più piccolo dei maggioranti |
| Controimmagine | elementi del dominio con immagine in $Y$ |
| Principio dei cassetti | $k > n$ oggetti in $n$ cassetti: un cassetto ne ha due |
| Numerabile | in biiezione con $\mathbb N$ |

### Domande che tornano spesso

- Differenza fra $\in$ e $\subseteq$; fra $\emptyset$ e $\{\emptyset\}$.
- Quanti sono i sottoinsiemi, le relazioni, le funzioni fra insiemi finiti?
- Definire equivalenza e ordine; legame fra equivalenze e partizioni.
- Massimo e massimale, maggiorante ed estremo superiore: differenze, con un esempio.
- Iniettiva, suriettiva, biiettiva; quando esiste l'inversa?
