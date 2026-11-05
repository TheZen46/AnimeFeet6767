---
corso: Fondamenti di Informatica
modulo: 2
titolo: Strutture algebriche e calcolo combinatorio
programma: [FI-03, FI-04]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 2 · Strutture algebriche e calcolo combinatorio

**In questo modulo.** Si usano gli insiemi, il prodotto cartesiano e le funzioni del modulo 1. La prima parte studia le operazioni su un insieme e le strutture che ne nascono: semigruppi, monoidi, gruppi, anelli, corpi e campi. Sono le "regole del gioco" dei tipi di dato: gli interi del C++ con la somma, le stringhe con la concatenazione, i resti modulo $n$ dell'aritmetica dei calcolatori. La seconda parte è il calcolo combinatorio, cioè l'arte di contare senza elencare: principi della somma e del prodotto, disposizioni, permutazioni e combinazioni, semplici e con ripetizione, coefficienti binomiali. Alla fine del modulo si sa riconoscere la struttura di un insieme con le sue operazioni e scegliere la formula giusta per un problema di conteggio, come nell'esercizio di combinatoria delle prove scritte.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (1.3 Introduzione alle strutture algebriche, 1.4 Elementi di calcolo combinatorio), foglio `esercizi_matematica`; C. Delizia e altri, *Matematica discreta*, McGraw-Hill (FI-03, FI-04)
> Il modulo è scritto in revisione dal materiale del corso; gli esercizi sono nuovi, sul modello delle prove 2016-2020, e controllati con `strumenti/verifica.py`.

## 2.1 Operazioni

Un'**operazione (binaria) interna** su un insieme $A$ è una funzione $\ast : A \times A \to A$: a ogni coppia di elementi di $A$ associa un elemento di $A$, che si scrive $a \ast b$. "Interna" vuol dire che il risultato resta in $A$: la sottrazione è un'operazione interna su $\mathbb Z$ ma non su $\mathbb N_0$, perché $2 - 5 \notin \mathbb N_0$. Un'operazione **esterna** combina elementi di un altro insieme con quelli di $A$, $K \times A \to A$: il prodotto di un numero reale per un vettore è l'esempio tipico. Su un insieme finito un'operazione si descrive con la sua **tabella** (di Cayley): riga $a$, colonna $b$, nella casella $a \ast b$.

Le proprietà che contano:

| Proprietà | Definizione |
|---|---|
| associativa | $(a \ast b) \ast c = a \ast (b \ast c)$ per ogni $a, b, c$ |
| commutativa | $a \ast b = b \ast a$ per ogni $a, b$ |
| elemento neutro | esiste $e \in A$ con $a \ast e = e \ast a = a$ per ogni $a$ |
| elemento simmetrico di $a$ | $a' \in A$ con $a \ast a' = a' \ast a = e$ |

L'elemento neutro, se c'è, è unico: se $e$ ed $e'$ sono neutri, $e = e \ast e' = e'$. Se l'operazione è associativa anche il simmetrico di un elemento è unico. Il simmetrico si chiama **opposto** con la notazione additiva ($-a$, neutro 0) e **inverso** con quella moltiplicativa ($a^{-1}$, neutro 1). Nella tabella: l'operazione è commutativa se la tabella è simmetrica rispetto alla diagonale; $e$ è neutro se la sua riga e la sua colonna ripetono l'intestazione; $a$ ha un simmetrico se nella sua riga compare $e$.

## 2.2 Semigruppi, monoidi e gruppi

Un insieme con una o più operazioni è una **struttura algebrica**. Con una sola operazione interna $(A, \ast)$:

| Struttura | Richiede |
|---|---|
| semigruppo | $\ast$ associativa |
| monoide | semigruppo con elemento neutro |
| gruppo | monoide in cui ogni elemento ha il simmetrico |
| gruppo abeliano | gruppo con $\ast$ commutativa |

Ogni riga della tabella aggiunge una richiesta alla precedente. Gli esempi da sapere:

- $(\mathbb N, +)$ è un semigruppo ma non un monoide: lo 0 non c'è.
- $(\mathbb N_0, +)$ è un monoide ma non un gruppo: nessun numero positivo ha l'opposto in $\mathbb N_0$.
- $(\mathbb Z, +)$, $(\mathbb Q, +)$, $(\mathbb R, +)$ sono gruppi abeliani; $(\mathbb Q \setminus \{0\}, \cdot)$ anche.
- $(\mathbb Z, \cdot)$ è un monoide commutativo (neutro 1), non un gruppo: 2 non ha inverso intero.
- $(\mathbb Z, -)$ non è neppure un semigruppo: $(5 - 3) - 1 \ne 5 - (3 - 1)$.
- Le **stringhe** su un alfabeto con la **concatenazione** formano un monoide non commutativo: il neutro è la stringa vuota, e `"ab" + "c"` $\ne$ `"c" + "ab"`.
- $(\mathcal P(S), \cup)$ è un monoide commutativo con neutro $\emptyset$; $(\mathcal P(S), \cap)$ con neutro $S$; $(\mathcal P(S), \Delta)$ è un gruppo abeliano: neutro $\emptyset$, e ogni $X$ è il simmetrico di sé stesso, perché $X \,\Delta\, X = \emptyset$.
- Le biiezioni di un insieme in sé con la composizione formano un gruppo, non abeliano se l'insieme ha almeno tre elementi.

**I resti modulo $n$.** $\mathbb Z_n = \{0, 1, \dots, n - 1\}$, con la somma e il prodotto "modulo $n$": si fa l'operazione e si prende il resto della divisione per $n$ (sono le classi della congruenza del modulo 1). $(\mathbb Z_n, +_n)$ è un gruppo abeliano: l'opposto di $a \ne 0$ è $n - a$. È l'aritmetica degli interi senza segno di un calcolatore a $k$ bit, che lavora modulo $2^k$: `255 + 1` in un byte dà 0.

## 2.3 Anelli, corpi e campi

Con due operazioni $(A, \oplus, \otimes)$ si ha un **anello** se $(A, \oplus)$ è un gruppo abeliano e $\otimes$ è associativa e distributiva rispetto a $\oplus$:
$$a \otimes (b \oplus c) = (a \otimes b) \oplus (a \otimes c), \qquad (b \oplus c) \otimes a = (b \otimes a) \oplus (c \otimes a).$$
L'anello è **unitario** se $\otimes$ ha l'elemento neutro, **commutativo** se $\otimes$ è commutativa. $(\mathbb Z, +, \cdot)$ è un anello commutativo unitario, e così $(\mathcal P(S), \Delta, \cap)$, con l'unità $S$.

Un anello unitario con più di un elemento in cui ogni elemento diverso dal neutro di $\oplus$ ha l'inverso rispetto a $\otimes$ è un **corpo**; un corpo commutativo è un **campo**. $(\mathbb Q, +, \cdot)$, $(\mathbb R, +, \cdot)$ e $(\mathbb C, +, \cdot)$ sono campi; $(\mathbb Z, +, \cdot)$ no.

$(\mathbb Z_n, +_n, \cdot_n)$ è sempre un anello commutativo unitario, ed è un campo **se e solo se $n$ è primo**. Se $n$ non è primo, $n = a \cdot b$ con $1 < a, b < n$ e $a \cdot_n b = 0$: due elementi non nulli hanno prodotto nullo (**divisori dello zero**), e $a$ non può avere inverso. In $\mathbb Z_6$, $2 \cdot 3 = 0$; in $\mathbb Z_7$ invece ogni elemento non nullo è invertibile: $1 \cdot 1 = 2 \cdot 4 = 3 \cdot 5 = 6 \cdot 6 = 1$.

## 2.4 Contare: i due principi

**Principio della somma.** Se una scelta si fa *o* in un insieme di $m$ modi *o* in un altro, disgiunto, di $n$ modi, i modi sono $m + n$. È $|A \cup B| = |A| + |B|$ per insiemi disgiunti.

**Principio del prodotto.** Se una scelta si fa in due fasi, la prima in $m$ modi e la seconda in $n$ modi qualunque sia stata la prima, i modi sono $m \cdot n$. È $|A \times B| = |A| \cdot |B|$, e si estende a $k$ fasi.

Quasi tutto il calcolo combinatorio viene da questi due principi. Per scegliere la formula bastano due domande sul problema: **conta l'ordine?** (una sequenza o un insieme?) e **sono ammesse le ripetizioni?** (lo stesso oggetto può essere scelto più volte?).

## 2.5 Disposizioni, permutazioni, combinazioni

Si scelgono $k$ oggetti da un insieme di $n$. Il **fattoriale** è $n! = n (n - 1) \cdots 2 \cdot 1$, con $0! = 1$.

**Disposizioni semplici** (conta l'ordine, niente ripetizioni): sequenze di $k$ oggetti distinti. Il primo si sceglie in $n$ modi, il secondo in $n - 1$, …, il $k$-esimo in $n - k + 1$:
$$D_{n,k} = n (n - 1) \cdots (n - k + 1) = \frac{n!}{(n - k)!}.$$

**Disposizioni con ripetizione** (conta l'ordine, ripetizioni ammesse): ogni posizione si sceglie in $n$ modi, $D'_{n,k} = n^k$. Sono le stringhe di lunghezza $k$ su un alfabeto di $n$ simboli: $2^8 = 256$ byte diversi.

**Permutazioni**: le disposizioni semplici di tutti gli $n$ oggetti, cioè i modi di metterli in fila, $P_n = n!$. Se fra gli $n$ oggetti ce ne sono $k_1$ uguali fra loro, $k_2$ uguali fra loro, e così via, scambiare oggetti uguali non dà una fila nuova: le **permutazioni con ripetizione** sono
$$P_n^{(k_1, k_2, \dots)} = \frac{n!}{k_1!\, k_2! \cdots}.$$

**Combinazioni semplici** (l'ordine non conta, niente ripetizioni): sottoinsiemi di $k$ elementi. Ogni sottoinsieme corrisponde a $k!$ disposizioni (i suoi ordinamenti), quindi
$$C_{n,k} = \frac{D_{n,k}}{k!} = \frac{n!}{k!\,(n - k)!} = \binom{n}{k}.$$

**Combinazioni con ripetizione** (l'ordine non conta, ripetizioni ammesse): gruppi di $k$ oggetti in cui lo stesso può comparire più volte, come scegliere $k$ palline da $n$ colori. Sono
$$C'_{n,k} = \binom{n + k - 1}{k}.$$
Il motivo: un gruppo si descrive con $k$ "stelle" (gli oggetti) e $n - 1$ "sbarre" (i separatori fra un tipo e l'altro), e basta scegliere quali delle $n + k - 1$ posizioni sono stelle.

| | Niente ripetizioni | Con ripetizioni |
|---|---|---|
| **conta l'ordine** | $D_{n,k} = \dfrac{n!}{(n-k)!}$ | $n^k$ |
| **non conta l'ordine** | $\dbinom{n}{k}$ | $\dbinom{n+k-1}{k}$ |

## 2.6 I coefficienti binomiali

I numeri $\binom{n}{k}$ hanno proprietà che semplificano i conti:
$$\binom{n}{k} = \binom{n}{n - k}, \qquad \binom{n}{0} = \binom{n}{n} = 1, \qquad \binom{n}{k} = \binom{n - 1}{k - 1} + \binom{n - 1}{k}.$$
La prima dice che scegliere i $k$ elementi da prendere equivale a scegliere gli $n - k$ da lasciare. L'ultima (formula di Stifel) si legge così: fissato un elemento, i sottoinsiemi di $k$ elementi o lo contengono (e si scelgono gli altri $k - 1$ fra $n - 1$) o non lo contengono (e si scelgono tutti fra $n - 1$). È la regola del **triangolo di Tartaglia**, in cui ogni numero è la somma dei due sopra.

> [!teorema] Binomio di Newton
> $$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}.$$

Sviluppando il prodotto di $n$ fattori $(a + b)$, il termine $a^k b^{n-k}$ compare tante volte quanti sono i modi di scegliere da quali $k$ fattori prendere $a$. Con $a = b = 1$ si ottiene $\sum_k \binom{n}{k} = 2^n$: i sottoinsiemi di un insieme di $n$ elementi, contati per numero di elementi, sono $2^n$, come nel modulo 1.

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove 2016-2020 e del foglio `esercizi_matematica`; risultati controllati con `strumenti/verifica.py` (FI-03, FI-04)

**Esercizio 1. Che struttura è?**

| Struttura | Risposta | Perché |
|---|---|---|
| $(\mathbb N_0, \max)$ | monoide commutativo | $\max$ è associativa e commutativa, neutro 0; $\max(3, x) = 0$ non ha soluzione |
| $(\mathbb Z, \ast)$ con $a \ast b = a + b + 1$ | gruppo abeliano | associativa; neutro $-1$ ($a + (-1) + 1 = a$); simmetrico di $a$ è $-a - 2$ |
| $(\mathbb Z_6, \cdot_6)$ | monoide commutativo, non gruppo | neutro 1; 0, 2, 3, 4 non hanno inverso |
| $(\mathbb Z_5 \setminus \{0\}, \cdot_5)$ | gruppo abeliano | 5 è primo: $1 \cdot 1 = 2 \cdot 3 = 4 \cdot 4 = 1$ |
| $(\mathbb R, \ast)$ con $a \ast b = (a + b)/2$ | nessuna delle quattro | commutativa ma non associativa: $(0 \ast 0) \ast 4 = 2$, $0 \ast (0 \ast 4) = 1$ |

**Esercizio 2. Una tabella.** Su $A = \{e, a, b\}$:

| $\ast$ | $e$ | $a$ | $b$ |
|---|---|---|---|
| $e$ | $e$ | $a$ | $b$ |
| $a$ | $a$ | $b$ | $e$ |
| $b$ | $b$ | $e$ | $a$ |

La tabella è simmetrica (commutativa), $e$ è neutro, e $e$ compare in ogni riga: $a$ e $b$ sono l'uno il simmetrico dell'altro. L'associatività si controlla sui casi (sono 27, ma con il neutro bastano quelli con $a$ e $b$): per esempio $(a \ast a) \ast b = b \ast b = a$ e $a \ast (a \ast b) = a \ast e = a$. È un gruppo abeliano: è $\mathbb Z_3$ con $e = 0$, $a = 1$, $b = 2$.

**Esercizio 3. Inversi modulo $n$.** Trovare gli inversi in $\mathbb Z_7$ e dire perché $\mathbb Z_8$ non è un campo.

In $\mathbb Z_7$: $1^{-1} = 1$, $2^{-1} = 4$, $3^{-1} = 5$, $4^{-1} = 2$, $5^{-1} = 3$, $6^{-1} = 6$. In $\mathbb Z_8$: $2 \cdot 4 = 8 \equiv 0$, quindi 2 è un divisore dello zero; se avesse un inverso $x$, da $2 \cdot 4 = 0$ si avrebbe $4 = x \cdot 2 \cdot 4 = 0$, assurdo.

**Esercizio 4. La gelateria** (sul modello dell'esercizio delle crociere). Ci sono 12 gusti.

1. Coppette con 3 gusti diversi, l'ordine non conta: $\binom{12}{3} = 220$.
2. Coni a 3 strati di gusti diversi, conta l'ordine dal basso: $D_{12,3} = 12 \cdot 11 \cdot 10 = 1320$.
3. Coppette con 3 palline, anche dello stesso gusto: $\binom{14}{3} = 364$.
4. Coni a 3 strati con gusti anche ripetuti: $12^3 = 1728$.
5. Coppette da 2 gusti diversi oppure coni da 2 strati di gusti diversi: $\binom{12}{2} + D_{12,2} = 66 + 132 = 198$ (principio della somma).

**Esercizio 5. Password.** Password di 8 caratteri fra 26 lettere minuscole e 10 cifre. Quante sono? Quante contengono almeno una cifra?

Con ripetizione e conta l'ordine: $36^8 = 2\,821\,109\,907\,456$. Quelle senza cifre sono $26^8 = 208\,827\,064\,576$; quelle con almeno una cifra sono la differenza, $2\,612\,282\,842\,880$. Contare "almeno uno" passando al complementare evita di dividere in casi.

**Esercizio 6. Anagrammi.** Quanti anagrammi (anche senza senso) ha INFORMATICA?

11 lettere, con I e A due volte ciascuna: $\dfrac{11!}{2!\,2!} = \dfrac{39\,916\,800}{4} = 9\,979\,200$.

**Esercizio 7. Commissioni.** Fra 8 uomini e 6 donne si sceglie una commissione di 5 persone.

Con esattamente 2 donne: $\binom{6}{2}\binom{8}{3} = 15 \cdot 56 = 840$. Con almeno una donna: tutte meno quelle di soli uomini, $\binom{14}{5} - \binom{8}{5} = 2002 - 56 = 1946$.

**Esercizio 8. Byte e binomio.** Quanti byte hanno esattamente tre bit a 1? Qual è il coefficiente di $x^3$ in $(x + 2)^5$?

Si scelgono le 3 posizioni dei bit a 1 fra 8: $\binom{8}{3} = 56$. Nel binomio, il termine con $x^3$ è $\binom{5}{3} x^3 2^2 = 40 x^3$.

**Esercizio 9. Inclusione-esclusione.** Quanti numeri da 1 a 100 sono divisibili per 2, 3 o 5?

Divisibili per 2: 50; per 3: 33; per 5: 20; per 6: 16; per 10: 10; per 15: 6; per 30: 3. Totale $50 + 33 + 20 - 16 - 10 - 6 + 3 = 74$.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; risultati controllati con `strumenti/verifica.py` (FI-03, FI-04)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Scegliere la formula.** Una squadra di calcetto: fra 9 giocatori se ne scelgono 5.

*Passo 1: i 5 titolari, senza ruoli.* L'ordine non conta, niente ripetizioni: $\binom{9}{5} = 126$.

*Passo 2: con 5 ruoli diversi* (portiere, due difensori distinti, due attaccanti distinti). Ora conta a chi va quale ruolo: $D_{9,5} = 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 = 15\,120$.

*Passo 3: un portiere e 4 giocatori di movimento senza ruoli.* Due fasi: il portiere fra 9, poi 4 fra gli 8 rimasti, $9 \cdot \binom{8}{4} = 9 \cdot 70 = 630$.

*Passo 4: il controllo.* $630 = 5 \cdot 126$: ogni gruppo di 5 titolari dà 5 squadre diverse a seconda di chi va in porta.

**Guidato 2. La tabella di $\mathbb Z_6$ per il prodotto.**

*Passo 1: la tabella delle righe utili.* Riga del 2: $0, 2, 4, 0, 2, 4$. Riga del 3: $0, 3, 0, 3, 0, 3$. Riga del 5: $0, 5, 4, 3, 2, 1$.

*Passo 2: gli inversi.* Un elemento è invertibile se nella sua riga compare 1: solo 1 e 5 ($5 \cdot 5 = 25 \equiv 1$).

*Passo 3: i divisori dello zero.* Nelle righe di 2, 3 e 4 compare 0 fuori dalla colonna dello 0: $2 \cdot 3 = 3 \cdot 4 = 0$.

*Passo 4: la conclusione.* $\mathbb Z_6$ è un anello commutativo unitario ma non un campo. Gli elementi invertibili sono quelli primi con 6.

**Guidato 3. Mani di carte.** Da un mazzo di 40 carte (4 semi da 10) si pescano 4 carte.

*Passo 1: le mani possibili.* $\binom{40}{4} = 91\,390$.

*Passo 2: mani con 4 carte dello stesso seme.* Si sceglie il seme (4 modi), poi 4 carte su 10: $4 \cdot \binom{10}{4} = 4 \cdot 210 = 840$.

*Passo 3: mani con un seme per carta.* Una carta per seme: $10^4 = 10\,000$.

*Passo 4: la probabilità*, se servisse: casi favorevoli su casi possibili, $840 / 91\,390 \approx 0{,}9\%$.

## Riepilogo

Un'operazione interna associa a due elementi di un insieme un elemento dello stesso insieme; le proprietà associativa, commutativa, l'esistenza del neutro e dei simmetrici definiscono semigruppi, monoidi, gruppi e gruppi abeliani. Con due operazioni si hanno anelli (gruppo abeliano più un'operazione associativa e distributiva), corpi e campi; $\mathbb Z_n$ è un campo solo per $n$ primo, altrimenti ha divisori dello zero. Per contare si usano i principi della somma e del prodotto; la formula si sceglie chiedendosi se conta l'ordine e se sono ammesse ripetizioni: disposizioni semplici e con ripetizione, permutazioni (anche con oggetti ripetuti), combinazioni semplici e con ripetizione. I coefficienti binomiali sono simmetrici, seguono il triangolo di Tartaglia e danno lo sviluppo del binomio di Newton.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FI-03, FI-04)

### Strutture

| Struttura | Associativa | Neutro | Simmetrici | Commutativa |
|---|---|---|---|---|
| semigruppo | sì | | | |
| monoide | sì | sì | | |
| gruppo | sì | sì | sì | |
| gruppo abeliano | sì | sì | sì | sì |

Anello: $(A, \oplus)$ gruppo abeliano, $\otimes$ associativa e distributiva. Corpo: anello unitario, inversi per tutti tranne lo zero. Campo: corpo commutativo. $\mathbb Z_n$ campo $\iff n$ primo.

### Combinatoria

$$D_{n,k} = \frac{n!}{(n-k)!}, \quad D'_{n,k} = n^k, \quad P_n = n!, \quad \frac{n!}{k_1! k_2! \cdots}, \quad \binom{n}{k} = \frac{n!}{k!(n-k)!}, \quad C'_{n,k} = \binom{n+k-1}{k}.$$

$$\binom{n}{k} = \binom{n}{n-k}, \qquad \binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}, \qquad (a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}, \qquad \sum_{k=0}^n \binom{n}{k} = 2^n.$$

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Operazione interna | $A \times A \to A$, il risultato resta in $A$ |
| Elemento neutro, simmetrico | non cambia gli altri; riporta al neutro |
| Divisore dello zero | $a, b \ne 0$ con $a b = 0$ |
| Principio del prodotto | scelte in fasi: si moltiplicano i modi |
| Disposizione | sequenza ordinata di $k$ oggetti |
| Combinazione | sottoinsieme di $k$ oggetti |
| Permutazione con ripetizione | ordinamenti di oggetti non tutti distinti |

### Domande che tornano spesso

- Definire semigruppo, monoide, gruppo, anello, campo, con esempi e controesempi.
- Perché $(\mathbb N_0, +)$ non è un gruppo? Perché $\mathbb Z_6$ non è un campo?
- Come si sceglie fra disposizioni, permutazioni e combinazioni? Ricavare $\binom{n}{k}$ dalle disposizioni.
- Enunciare il binomio di Newton e la formula di Stifel.
