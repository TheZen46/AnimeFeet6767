---
corso: Teoria dei Sistemi
lezione: 10
data: 2026-10-31
argomenti: [variabili di stato, vasche in cascata, equazioni di stato lineari, dimensioni delle matrici A B C D, ordine del sistema, esponenziale di matrice, soluzione nel tempo, soluzione con Laplace, poli del sistema e autovalori, risposte libere e forzate, matrice di trasferimento, inversa con la matrice aggiunta, causalità e gradino]
fonti: [trascrizione parte 1, dispensa del docente (inglese)]
tags: [teoria-dei-sistemi, lezione]
---

# Lezione 10 — Equazioni di stato

Questa nota ricostruisce la decima lezione. Le fonti sono:

- la trascrizione della registrazione (parte 1);
- la dispensa in inglese del docente (cap. 4, *Linear Systems Described by State Equations*, §4.1, pp. 45–48).

Per questa lezione non sono stati forniti appunti personali.

La lezione introduce la rappresentazione più generale di un sistema dinamico, quella con le **variabili di stato**, che verrà usata praticamente per tutto il resto del corso. Ricava la soluzione delle equazioni di stato nel tempo e con la trasformata di Laplace, definisce i **poli del sistema** e la **matrice di trasferimento**, e chiude con un esercizio che mette in luce una differenza importante: l'ordine del sistema e l'ordine dell'equazione differenziale tra ingresso e uscita non coincidono necessariamente.

## 1. Perché le variabili di stato

### 1.1 Un esempio: vasche in cascata

Il docente parte da un esempio idraulico: una serie di vasche, ciascuna delle quali scarica nella successiva. Un rubinetto versa nella prima con portata $u$; ogni vasca perde liquido attraverso un foro sul fondo, con una portata proporzionale al livello del liquido nella vasca stessa.

Se si volesse descrivere il sistema con un'unica equazione differenziale che leghi, ad esempio, il livello dell'ultima vasca alla portata $u$, bisognerebbe esprimere ciascuna vasca in funzione della precedente e sostituire a cascata. Ne verrebbe un'equazione con derivate di ordine elevato, tanto più lunga quante più sono le vasche.

Se invece si descrive **ogni vasca singolarmente**, le cose sono semplici. Si indica con $x_i$ il livello della vasca $i$-esima (per convenzione queste variabili si chiamano $x$). Ciascuna equazione è un bilancio: la variazione del livello è ciò che entra meno ciò che esce.

$$\begin{aligned}
\dot x_1 &= u - k_1 x_1 \\
\dot x_2 &= k_1 x_1 - k_2 x_2 \\
\dot x_3 &= k_2 x_2 - k_3 x_3 \\
&\ \ \vdots
\end{aligned}$$

Qui $k_1x_1$ è la portata che esce dalla prima vasca ed entra nella seconda, e così via: un coefficiente $k_i$ grande corrisponde a un foro grande. Nelle sezioni delle vasche, supposte unitarie, livello e volume coincidono, come nel recipiente della [[Lezione 01 - Sistemi dinamici e funzioni generalizzate|lezione 1]].

```mermaid
flowchart LR
    U["u (rubinetto)"] --> V1["Vasca 1<br/>x₁"]
    V1 -- "k₁ x₁" --> V2["Vasca 2<br/>x₂"]
    V2 -- "k₂ x₂" --> V3["Vasca 3<br/>x₃"]
    V3 -- "k₃ x₃" --> O["scarico"]
```

Nelle equazioni **ogni variabile compare derivata una volta sola**. Non c'è un'unica variabile derivata tante volte, come nelle equazioni differenziali di ordine $n$: ci sono tante variabili, ciascuna derivata una volta. Con $50$ vasche ci sarebbero $50$ equazioni di questo tipo, invece di un'equazione con una derivata di ordine $50$. L'esempio fa almeno capire che non sempre conviene rappresentare un sistema con un'unica equazione differenziale ingresso-uscita, soprattutto quando è fatto di parti interconnesse.

> [!tip] Esercizio collegato
> La raccolta di esercizi svolti di D. Giglio (`esercizi.pdf`) contiene un sistema di tre vasche comunicanti (Esercizio 2.7), utile per ritrovare questa struttura in un caso completo.

### 1.2 La forma generale

La forma più generale delle **equazioni di stato** è

$$\dot x = f(x, u), \qquad y = g(x, u),$$

con $x$ **vettore di stato**, $u$ vettore degli **ingressi** (o controlli) e $y$ vettore delle **uscite**. Se $f$ non ha qualche proprietà di regolarità (continuità, derivabilità) non se ne può dire molto. Per il $90\%$ del corso, però, si studieranno sistemi **lineari, stazionari** (tempo-invarianti) **e a tempo continuo**, per i quali la forma è molto più semplice.

## 2. Le equazioni di stato lineari

### 2.1 L'equazione di stato

Se $x(t)\in\mathbb{R}^n$, anche $\dot x(t)$ è un vettore di $\mathbb{R}^n$: è il vettore delle derivate dei singoli elementi. Il secondo membro deve essere un vettore di $\mathbb{R}^n$, e nel caso lineare è la somma di due vettori di $\mathbb{R}^n$, uno che dipende dallo stato e uno dall'ingresso:

$$\dot x(t) = A\,x(t) + B\,u(t) .$$

Le dimensioni delle matrici si ricavano dalla regola del prodotto: il prodotto di due matrici esiste se il numero di colonne della prima è uguale al numero di righe della seconda, e ha tante righe quante la prima e tante colonne quante la seconda.

- $A\,x$ deve essere un vettore di $n$ righe, quindi $A$ ha $n$ righe. Per poterla moltiplicare per $x$, che ha $n$ righe, deve avere $n$ colonne. Quindi $A$ è **quadrata**, $n\times n$.
- Se $u(t)\in\mathbb{R}^m$, $B\,u$ deve avere $n$ righe e $B$ deve avere $m$ colonne. Quindi $B$ è $n\times m$.

Il caso scalare, $\dot x = a\,x + b\,u$ con $a$ e $b$ numeri, si recupera con $n = m = 1$.

### 2.2 L'equazione di uscita

Spesso non si possono misurare tutte le variabili di stato. Nelle $50$ vasche si sa che esistono $50$ livelli, ma magari il «metro» lo si può calare soltanto nell'ultima, perché si è lì. Le grandezze misurate, che possono essere anche combinazioni delle variabili di stato o dipendere direttamente dall'ingresso, si raccolgono nel vettore delle uscite $y(t)\in\mathbb{R}^q$:

$$y(t) = C\,x(t) + D\,u(t) .$$

> [!important] Equazioni di stato di un sistema lineare stazionario a tempo continuo
> $$\begin{cases}\dot x(t) = A\,x(t) + B\,u(t) \\[2pt] y(t) = C\,x(t) + D\,u(t)\end{cases}
> \qquad x\in\mathbb{R}^n,\ \ u\in\mathbb{R}^m,\ \ y\in\mathbb{R}^q$$
> $$A\in\mathbb{R}^{n\times n}, \qquad B\in\mathbb{R}^{n\times m}, \qquad C\in\mathbb{R}^{q\times n}, \qquad D\in\mathbb{R}^{q\times m} .$$
> La dimensione $n$ del vettore di stato si chiama **ordine del sistema**: un sistema con $50$ variabili di stato è un sistema di ordine $50$.

> [!warning] Notazione e un refuso nella registrazione
> - La dispensa in inglese indica con $p$ la dimensione dell'ingresso, $u\in\mathbb{R}^p$, e quindi scrive $B\in\mathbb{R}^{n\times p}$ e $D\in\mathbb{R}^{q\times p}$. Qui si segue la lezione, con $m$. Attenzione a non confondere questo $m$ con il grado del numeratore delle equazioni ingresso-uscita.
> - Nella trascrizione la matrice $D$ risulta «$q\times n$». Deve essere $q\times m$: moltiplica l'ingresso, che ha $m$ componenti.

## 3. La soluzione nel dominio del tempo

### 3.1 La formula

L'equazione di uscita non pone difficoltà: una volta noto $x(t)$, $y(t)$ si calcola direttamente. L'unica difficoltà è l'equazione di stato, che è differenziale. Con l'istante iniziale in $0$, la sua soluzione (detta formula di Lagrange) è

$$x(t) = e^{At}\,x(0^-) + \int_{0^-}^{t} e^{A(t-\tau)}\,B\,u(\tau)\,d\tau ,$$

e quindi

$$y(t) = C\,e^{At}\,x(0^-) + C\int_{0^-}^{t} e^{A(t-\tau)}\,B\,u(\tau)\,d\tau + D\,u(t) .$$

Il caso scalare è familiare: per $\dot x = a\,x + b\,u$ si ritrova la soluzione dell'equazione lineare del primo ordine vista in analisi, con $e^{at}$ al posto di $e^{At}$.

### 3.2 Che cos'è $e^{At}$

> [!important] Esponenziale di matrice
> $e^{At}$ **non** è la matrice degli esponenziali degli elementi di $At$. Si definisce con la stessa serie dell'esponenziale scalare:
> $$e^{At} = \sum_{k=0}^{\infty}\frac{(At)^k}{k!} = I + At + \frac{A^2t^2}{2!} + \frac{A^3t^3}{3!} + \dots$$
> È una matrice $n\times n$.

La serie non è uno strumento pratico per calcolarla. Esistono metodi basati sulla diagonalizzazione: se $A$ è diagonalizzabile, la si diagonalizza, si calcola l'esponenziale della matrice diagonale (che, solo in quel caso, è la matrice degli esponenziali degli elementi della diagonale) e si torna indietro. Quando $A$ non è diagonalizzabile serve la forma di Jordan. Il docente non presenta questi metodi: con la trasformata di Laplace «sarà tutto molto più facile».

## 4. La soluzione con la trasformata di Laplace

### 4.1 Trasformare un'equazione vettoriale

La trasformata di un vettore (o di una matrice) di funzioni è il vettore (o la matrice) delle trasformate degli elementi ([[Lezione 03 - Trasformate notevoli, poli e andamento nel tempo|lezione 3]]): l'integrale si applica elemento per elemento. La proprietà della derivata vale quindi componente per componente:

$$\mathcal{L}\{\dot x\} = s\,X(s) - x(0^-) .$$

Le matrici costanti $A$ e $B$ si comportano, per la linearità, come coefficienti moltiplicativi. Trasformando l'equazione di stato:

$$s\,X(s) - x(0^-) = A\,X(s) + B\,U(s) .$$

### 4.2 Attenzione all'ordine dei prodotti

Per ricavare $X(s)$ bisogna raccogliere $X(s)$. Con matrici e vettori le cose non si possono spostare a piacere, perché **il prodotto tra matrici in generale non è commutativo**. In $A\,X(s)$, il vettore $X(s)$ deve restare a destra di $A$: non può «miracolosamente» finire a sinistra. Per raccoglierlo a destra bisogna scrivere $s\,X(s)$ come $s\,I\,X(s)$, con $I$ la matrice identità $n\times n$:

$$\big(sI - A\big)\,X(s) = x(0^-) + B\,U(s) \qquad\Longrightarrow\qquad X(s) = (sI-A)^{-1}x(0^-) + (sI-A)^{-1}B\,U(s) .$$

### 4.3 Quando $sI - A$ è invertibile: i poli del sistema

Chi garantisce che $sI-A$ sia invertibile? $s$ è una variabile, che può assumere tutti i valori del campo complesso. $sI - A$ non è invertibile esattamente quando $\det(sI-A) = 0$, cioè, per definizione, quando $s$ è un **autovalore** di $A$. Per tutti gli altri valori di $s$ è invertibile. Come per le trasformate di Laplace con un denominatore, si scrive la formula sapendo che negli autovalori di $A$ qualcosa «va all'infinito».

> [!important] Poli del sistema
> Gli **autovalori della matrice $A$** si chiamano **poli del sistema**. Il nome estende il concetto di polo di una singola trasformata di Laplace.

### 4.4 L'uscita e i quattro pezzi della soluzione

Trasformando l'equazione di uscita, $Y(s) = C\,X(s) + D\,U(s)$, e sostituendo:

$$Y(s) = C\,(sI-A)^{-1}x(0^-) + \Big[\,C\,(sI-A)^{-1}B + D\,\Big]\,U(s) .$$

Confrontando con la soluzione nel tempo si riconoscono quattro termini (dispensa inglese, pp. 46–47).

| Nel tempo | Nel dominio di $s$ | Nome |
| :--- | :--- | :--- |
| $e^{At}x(0^-)$ | $(sI-A)^{-1}x(0^-)$ | risposta dello **stato** a ingresso nullo |
| $\int_{0^-}^t e^{A(t-\tau)}Bu(\tau)\,d\tau$ | $(sI-A)^{-1}B\,U(s)$ | risposta dello **stato** nello stato zero |
| $Ce^{At}x(0^-)$ | $C(sI-A)^{-1}x(0^-)$ | risposta dell'**uscita** a ingresso nullo |
| $C\int_{0^-}^t e^{A(t-\tau)}Bu(\tau)\,d\tau + Du(t)$ | $\big[C(sI-A)^{-1}B + D\big]U(s)$ | risposta dell'**uscita** nello stato zero |

Come osserva il docente, la questione dei nomi è «sintattica»: non c'è nulla di profondo. Se l'ingresso è nullo resta solo il pezzo con $x(0^-)$; se lo stato iniziale è nullo resta solo il pezzo con $U$. Per il principio di sovrapposizione, la risposta completa è la somma dei due.

### 4.5 $e^{At}$ con Laplace

Dal confronto tra le due soluzioni, poiché $x(0^-)$ può essere qualunque vettore, segue (dispensa inglese, formula 4.16):

> [!important] Esponenziale di matrice e trasformata di Laplace
> $$\mathcal{L}\{e^{At}\} = (sI - A)^{-1}, \qquad\qquad e^{At} = \mathcal{L}^{-1}\big\{(sI-A)^{-1}\big\} .$$
> Si calcola $(sI-A)^{-1}$, che è una matrice i cui elementi sono trasformate di Laplace. Si antitrasforma ciascun elemento e lo si rimette al suo posto: si ottiene $e^{At}$.

## 5. La matrice di trasferimento

> [!important] Matrice di trasferimento (dispensa inglese, formula 4.15)
> $$M(s) = C\,(sI-A)^{-1}B + D$$
> è la **matrice di trasferimento** del sistema: permette di calcolare la trasformata dell'uscita a partire da quella dell'ingresso, se lo stato iniziale è nullo, $Y(s) = M(s)\,U(s)$. È una matrice $q\times m$.

Fa «in grande» la stessa cosa della funzione di trasferimento della [[Lezione 08 - Equazioni differenziali, funzione di trasferimento e risposte|lezione 8]]: lì lo stato era contenuto nelle condizioni iniziali, e uscita e ingresso erano scalari; qui sono vettori.

Ogni elemento della matrice di trasferimento è, come interpretazione fisica, una **funzione di trasferimento**. Si scrive il prodotto riga per colonna:

$$\begin{bmatrix} Y_1(s)\\ \vdots\\ Y_q(s)\end{bmatrix} = \begin{bmatrix} M_{11}(s) & \cdots & M_{1m}(s)\\ \vdots & & \vdots\\ M_{q1}(s) & \cdots & M_{qm}(s)\end{bmatrix}\begin{bmatrix} U_1(s)\\ \vdots\\ U_m(s)\end{bmatrix}, \qquad Y_i(s) = \sum_{j=1}^m M_{ij}(s)\,U_j(s) .$$

Se tutti gli ingressi sono nulli tranne il $j$-esimo, $Y_i(s) = M_{ij}(s)\,U_j(s)$. L'elemento $M_{ij}(s)$ è dunque la **funzione di trasferimento tra l'ingresso $j$ e l'uscita $i$**. Ad esempio $M_{13}$ lega il terzo ingresso alla prima uscita. Quando ingresso e uscita sono scalari ($m = q = 1$), la matrice di trasferimento è una matrice $1\times1$, cioè la funzione di trasferimento.

Meno usata ma con lo stesso significato è $(sI-A)^{-1}B$, la **matrice di trasferimento ingresso-stato**.

## 6. Calcolare $(sI-A)^{-1}$

### 6.1 L'inversa con la matrice aggiunta

Il docente chiede come si calcola l'inversa di una matrice, ad esempio $50\times50$, «non con i trucchi ma con la formula generale». Uno studente propone il metodo di Gauss-Jordan: affiancare l'identità e ridurre la matrice di sinistra fino a farla diventare l'identità. È corretto, ma per i conti a mano richiede molto lavoro. Il docente preferisce la formula con la **matrice aggiunta**: non fa risparmiare conti, che vanno fatti comunque, ma mette in evidenza delle cose che altrimenti non si vedono.

> [!important] Inversa con la matrice aggiunta
> $$M^{-1} = \frac{\operatorname{adj}(M)}{\det M}$$
> - l'**aggiunta** $\operatorname{adj}(M)$ è la **trasposta** della matrice dei complementi algebrici;
> - il **complemento algebrico** dell'elemento $(i,j)$ è $(-1)^{i+j}$ per il determinante della matrice che si ottiene cancellando la riga $i$ e la colonna $j$.

### 6.2 Che cosa mette in evidenza

Si applichi la formula a $sI - A$. Gli elementi di $A$ sono numeri e $s$ compare solo sulla diagonale. I determinanti delle sottomatrici $(n-1)\times(n-1)$ sono quindi **polinomi** in $s$, di grado al più $n-1$. Il determinante di $sI-A$ è il **polinomio caratteristico** di $A$, di grado esattamente $n$: le sue $n$ radici sono gli autovalori.

$$(sI - A)^{-1} = \frac{\operatorname{adj}(sI-A)}{\det(sI-A)} \qquad\Longrightarrow\qquad \text{ogni elemento è un rapporto di polinomi strettamente proprio.}$$

Con una matrice $30\times30$, ad esempio, ogni complemento algebrico è al più un polinomio di grado $29$, e il denominatore comune è di grado $30$. I rapporti di polinomi sono proprio gli oggetti che si sanno antitrasformare. Quindi l'antitrasformata di $(sI-A)^{-1}$, cioè $e^{At}$, non presenta difficoltà concettuali, solo conti. Inoltre i denominatori sono tutti divisori del polinomio caratteristico, quindi le funzioni che compaiono in $e^{At}$ sono legate agli **autovalori di $A$**. È il motivo per cui questi si chiamano poli del sistema.

### 6.3 Esempio svolto a lezione

> [!example] $A = \begin{bmatrix} 0 & 1\\ -1 & 0\end{bmatrix}$
> $$sI - A = \begin{bmatrix} s & -1\\ 1 & s\end{bmatrix}, \qquad \det(sI-A) = s^2 + 1 .$$
> **Complementi algebrici.** Per una $2\times2$ non ci sono determinanti da calcolare: il complemento di ciascun elemento è l'elemento «opposto», con il segno cambiato se $i+j$ è dispari.
> - $(1,1)$, pari: l'elemento $(2,2)$, cioè $s$;
> - $(1,2)$, dispari: l'elemento $(2,1)$ cambiato di segno, cioè $-1$;
> - $(2,1)$, dispari: l'elemento $(1,2)$ cambiato di segno, cioè $1$;
> - $(2,2)$, pari: l'elemento $(1,1)$, cioè $s$.
>
> Trasponendo e dividendo per il determinante:
> $$(sI-A)^{-1} = \frac{1}{s^2+1}\begin{bmatrix} s & 1\\ -1 & s\end{bmatrix} = \begin{bmatrix} \dfrac{s}{s^2+1} & \dfrac{1}{s^2+1}\\[8pt] -\dfrac{1}{s^2+1} & \dfrac{s}{s^2+1}\end{bmatrix}.$$
> **Verifica.** Il docente raccomanda di controllare sempre l'inversa moltiplicandola per la matrice di partenza. Ad esempio, l'elemento $(1,1)$ del prodotto $(sI-A)^{-1}(sI-A)$ è $\frac{s\cdot s + 1\cdot1}{s^2+1} = 1$, l'elemento $(1,2)$ è $\frac{s\cdot(-1) + 1\cdot s}{s^2+1} = 0$, e così via.
>
> **Antitrasformata.** Sono tutti fratti semplici della tabella:
> $$e^{At} = \begin{bmatrix} \cos t & \sin t\\ -\sin t & \cos t\end{bmatrix}.$$
> Come si vede, non è affatto la matrice degli esponenziali degli elementi di $At$, che darebbe $\begin{bmatrix} 1 & e^{t}\\ e^{-t} & 1\end{bmatrix}$.

> [!tip] Il trucco per le matrici $2\times2$
> Per una $2\times2$ l'inversa si ottiene scambiando i due elementi della diagonale principale, cambiando di segno quelli dell'altra diagonale e dividendo per il determinante:
> $$\begin{bmatrix} a & b\\ c & d\end{bmatrix}^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b\\ -c & a\end{bmatrix}.$$
> È la formula dell'aggiunta scritta per esteso.

> [!tip] Matrici triangolari
> Se $A$ è triangolare, anche $sI - A$ lo è. Il determinante di una matrice triangolare è il **prodotto degli elementi sulla diagonale**, e gli autovalori di $A$ sono proprio i suoi elementi diagonali.

## 7. Esercizio: un sistema di ordine 2 con un'equazione ingresso-uscita del primo ordine

### 7.1 Il testo

Il docente propone un esercizio da fare in aula, «non manco parecchio un esercizio d'esame». Se all'esame chiedesse una cosa del genere, si starebbe decidendo se dare il $18$ oppure no.

> [!example] Testo
> $$\dot x = \begin{bmatrix} -1 & 0\\ 1 & -2\end{bmatrix}x + \begin{bmatrix} 1\\ 1\end{bmatrix}u, \qquad y = \begin{bmatrix} 1 & 0\end{bmatrix}x, \qquad x(0^-) = \begin{bmatrix} 1\\ 0\end{bmatrix}, \qquad u(t) = \delta(t) .$$
> Calcolare $x(t)$ e $y(t)$, e individuare l'equazione differenziale che lega $y$ a $u$, con le sue condizioni iniziali.
>
> Le matrici sono state ricostruite dai passaggi udibili della registrazione: $sI - A$ dettata alla lavagna, la combinazione delle colonne per $x(0^-)$ e per $B$, la scelta della prima riga per $C$. Sono coerenti con tutti i risultati intermedi riportati dal docente.

### 7.2 Svolgimento

**L'inversa.**

$$sI - A = \begin{bmatrix} s+1 & 0\\ -1 & s+2\end{bmatrix}, \qquad \det(sI-A) = (s+1)(s+2),$$

perché la matrice è triangolare. Con i complementi algebrici, o con il trucco per le $2\times2$:

$$(sI-A)^{-1} = \frac{1}{(s+1)(s+2)}\begin{bmatrix} s+2 & 0\\ 1 & s+1\end{bmatrix} = \begin{bmatrix} \dfrac{1}{s+1} & 0\\[8pt] \dfrac{1}{(s+1)(s+2)} & \dfrac{1}{s+2}\end{bmatrix}.$$

I poli del sistema sono gli autovalori di $A$, cioè $-1$ e $-2$, gli elementi diagonali di una matrice triangolare.

**Un'osservazione sui prodotti.** Il docente sottolinea un fatto che ripeterà molte volte.

> [!important] Prodotti per vettori e combinazioni lineari
> - **Post-moltiplicare** una matrice per un vettore colonna significa fare una **combinazione lineare delle colonne** della matrice, con i coefficienti dati dagli elementi del vettore.
> - **Pre-moltiplicare** una matrice per un vettore riga significa fare una **combinazione lineare delle righe**.

Quindi:

- $(sI-A)^{-1}x(0^-)$ con $x(0^-) = [1\ \ 0]^\top$ è $1$ volta la prima colonna più $0$ volte la seconda: si «pesca» la **prima colonna**;
- $(sI-A)^{-1}B$ con $B = [1\ \ 1]^\top$ è la **somma delle due colonne**;
- $C(sI-A)^{-1}$ con $C = [1\ \ 0]$ è la **prima riga**.

**Lo stato.** Con $U(s) = \mathcal{L}\{\delta\} = 1$:

$$(sI-A)^{-1}B = \begin{bmatrix} \dfrac{1}{s+1}\\[8pt] \dfrac{1}{(s+1)(s+2)} + \dfrac{1}{s+2}\end{bmatrix} = \begin{bmatrix} \dfrac{1}{s+1}\\[8pt] \dfrac{1 + (s+1)}{(s+1)(s+2)}\end{bmatrix} = \begin{bmatrix} \dfrac{1}{s+1}\\[8pt] \dfrac{1}{s+1}\end{bmatrix},$$

perché al numeratore $s+2$ si semplifica con il denominatore. Quindi

$$X(s) = \underbrace{\begin{bmatrix} \dfrac{1}{s+1}\\[8pt] \dfrac{1}{(s+1)(s+2)}\end{bmatrix}}_{\text{ingresso nullo}} + \underbrace{\begin{bmatrix} \dfrac{1}{s+1}\\[8pt] \dfrac{1}{s+1}\end{bmatrix}}_{\text{stato zero}} .$$

Antitrasformando, con $\frac{1}{(s+1)(s+2)} = \frac{1}{s+1} - \frac{1}{s+2}$:

$$x(t) = \begin{bmatrix} e^{-t}\\ e^{-t} - e^{-2t}\end{bmatrix} + \begin{bmatrix} e^{-t}\\ e^{-t}\end{bmatrix}1(t) .$$

### 7.3 Chi si moltiplica per $1(t)$?

A questo punto il docente pone una domanda «a cui non risponde nessuno», e a cui da studente non rispondeva nemmeno lui: quali termini vanno moltiplicati per $1(t)$ e quali no? Di solito è indifferente, perché la trasformata non vede ciò che accade prima di zero. Ma se si vogliono fare le cose con precisione, la risposta è questa.

- La **risposta nello stato zero** va moltiplicata per $1(t)$, per il **principio di causalità**. L'effetto non può precedere la causa, e l'ingresso agisce da $0$ in avanti: in $0^-$ quel contributo non esisteva.
- La **risposta a ingresso nullo** **non** va moltiplicata per $1(t)$. Se lo si facesse, in $0^-$ varrebbe zero, e la soluzione non rispetterebbe più la condizione iniziale $x(0^-)$ assegnata.

Infatti, valutando il termine libero in $0^-$, si ritrova esattamente $x(0^-) = [1\ \ 0]^\top$: $e^{0} = 1$ ed $e^{0} - e^{0} = 0$. Lo stesso criterio è usato dalla dispensa in inglese nell'esempio E/3.0/1. Dopo questa precisazione, osserva il docente, si può «far finta di niente»: per sapere che cosa succede da zero in avanti si possono sommare i due contributi. Per $t > 0$:

$$x_1(t) = 2\,e^{-t}, \qquad x_2(t) = 2\,e^{-t} - e^{-2t} .$$

**L'uscita.** Con $C = [1\ \ 0]$ e $D = 0$:

$$Y(s) = \underbrace{C(sI-A)^{-1}x(0^-)}_{\frac{1}{s+1}} + \underbrace{C(sI-A)^{-1}B}_{M(s)\,=\,\frac{1}{s+1}}\cdot 1, \qquad y(t) = e^{-t} + e^{-t}\,1(t) \;=\; 2\,e^{-t}\ \ (t>0) .$$

Ingresso e uscita sono scalari ($m = q = 1$), quindi la matrice di trasferimento è la funzione di trasferimento $M(s) = \frac{1}{s+1}$.

### 7.4 Il punto dell'esercizio: ordine del sistema e ordine dell'equazione

Il sistema ha due variabili di stato: è di **ordine 2**. Ci si aspetterebbe che l'equazione differenziale che lega $y$ a $u$ sia anch'essa del secondo ordine. **Non è così.**

Nella [[Lezione 08 - Equazioni differenziali, funzione di trasferimento e risposte|lezione 8]] si era visto che la risposta libera dell'uscita ha la forma $\frac{Z(s)}{D_y(s)}$, con $D_y$ il polinomio caratteristico dell'equazione differenziale. Qui

$$C(sI-A)^{-1}x(0^-) = \begin{bmatrix} \dfrac{1}{s+1} & 0\end{bmatrix}\begin{bmatrix} x_1(0^-)\\ x_2(0^-)\end{bmatrix} = \frac{x_1(0^-)}{s+1}$$

per **qualunque** stato iniziale. Il polinomio caratteristico è $s+1$, di grado $1$, e la funzione di trasferimento è $\frac{1}{s+1}$. L'equazione differenziale tra ingresso e uscita è quindi

$$\dot y + y = u, \qquad y(0^-) = x_1(0^-),$$

del **primo** ordine. Si vede anche direttamente dalle equazioni: $y = x_1$ e $\dot x_1 = -x_1 + u$, quindi $\dot y = -y + u$. La seconda variabile di stato esiste ed evolve, con l'autovalore $-2$, ma non ha alcun effetto sull'uscita.

> [!important] Tre «ordini» da non confondere
> - L'**ordine del sistema** è la dimensione $n$ del vettore di stato.
> - L'**ordine dell'equazione differenziale** tra ingresso e uscita è il grado del suo polinomio caratteristico.
> - L'**ordine della funzione di trasferimento** è il grado del suo denominatore dopo le semplificazioni.
>
> In generale sono cose diverse. Quando coincidono dipende da proprietà strutturali che verranno studiate nel corso.

> [!tip] Collegamento con il seguito del corso
> Le proprietà strutturali a cui allude il docente sono, nella dispensa in inglese, la **raggiungibilità** e la **osservabilità** (§4.3–4.5). In questo esempio, ad esempio, la variabile $x_2$ non influenza l'uscita, e il polo $-2$ «sparisce» da tutto ciò che si vede dall'uscita. Anche la semplificazione di $s+2$ in $(sI-A)^{-1}B$ non è un caso. Il docente invita a seguire un filo logico, invece di andare a memoria: «dovete capire perché questo, perché questo, perché questo, allora è ovvio che è così».

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. *Perché la matrice $A$ è necessariamente quadrata?* $A\,x$ deve avere le stesse righe di $\dot x$, cioè $n$, e per moltiplicare $x$, che ha $n$ righe, $A$ deve avere $n$ colonne.
2. *Perché $e^{At}$ non è la matrice degli esponenziali degli elementi?* È definita dalla serie $\sum (At)^k/k!$, in cui compaiono le potenze della matrice, non degli elementi.
3. *Perché nel raccogliere $X(s)$ bisogna scrivere $sI - A$ e non $s - A$?* $s$ è uno scalare e $A$ una matrice: per sottrarli bisogna trasformare $s$ nella matrice $sI$. Inoltre $X(s)$ va raccolto a destra, perché il prodotto tra matrici non è commutativo.
4. *Perché gli autovalori di $A$ si chiamano poli del sistema?* $(sI-A)^{-1}$ ha come denominatore comune $\det(sI-A)$, le cui radici sono gli autovalori: sono i poli degli elementi di $(sI-A)^{-1}$ e quindi determinano le funzioni presenti in $e^{At}$.
5. *Che cosa rappresenta l'elemento $(i,j)$ della matrice di trasferimento?* La funzione di trasferimento tra il $j$-esimo ingresso e la $i$-esima uscita, con tutti gli altri ingressi nulli.
6. *Perché la risposta nello stato zero si moltiplica per $1(t)$ e quella a ingresso nullo no?* La prima, per causalità, non esiste prima dell'ingresso. La seconda deve valere $x(0^-)$ in $0^-$: moltiplicata per $1(t)$ varrebbe zero.
7. *Un sistema di ordine $2$ ha sempre un'equazione ingresso-uscita del secondo ordine?* No: nell'esempio del §7 l'equazione è $\dot y + y = u$, del primo ordine, perché la seconda variabile di stato non influenza l'uscita.
