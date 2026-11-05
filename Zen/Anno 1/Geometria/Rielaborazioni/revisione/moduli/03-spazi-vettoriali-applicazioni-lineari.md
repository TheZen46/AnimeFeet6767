---
corso: Geometria
modulo: 3
titolo: Spazi vettoriali e applicazioni lineari
programma: [GEO-05]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 3 · Spazi vettoriali e applicazioni lineari

**In questo modulo.** Servono le matrici, la riduzione di Gauss, il determinante e il rango del modulo 2. Si astraggono le proprietà della somma di vettori e del prodotto per uno scalare nella nozione di spazio vettoriale, che comprende $\mathbb{R}^n$, i polinomi, le matrici, le soluzioni di un sistema omogeneo. Si studiano i sottospazi, le combinazioni lineari, l'indipendenza lineare, le basi e la dimensione, le coordinate, l'intersezione e la somma di sottospazi con la formula di Grassmann. Poi si passa alle applicazioni lineari: matrice associata, nucleo e immagine, teorema della dimensione, isomorfismi, cambiamenti di base e matrici simili. Alla fine si sa verificare se un insieme è un sottospazio, trovarne una base e la dimensione, e studiare un'applicazione lineare con la sua matrice.

## 3.1 Spazi vettoriali

> [!definizione] Spazio vettoriale
> Uno **spazio vettoriale** sul campo $\mathbb{K}$ è un insieme $V$ con una somma $V \times V \to V$ e un prodotto per scalari $\mathbb{K} \times V \to V$ tali che, per ogni $u, v, w \in V$ e $\lambda, \mu \in \mathbb{K}$:
>
> 1. la somma è associativa e commutativa, ha un elemento neutro $0_V$ e ogni $v$ ha un opposto $-v$;
> 2. $\lambda(\mu v) = (\lambda\mu)v$ e $1 \cdot v = v$;
> 3. $(\lambda + \mu)v = \lambda v + \mu v$ e $\lambda(v + w) = \lambda v + \lambda w$.
>
> Gli elementi di $V$ si chiamano **vettori**, quelli di $\mathbb{K}$ **scalari**.

Dagli assiomi seguono le regole di calcolo attese: $0 \cdot v = 0_V$, $\lambda \cdot 0_V = 0_V$, $(-1)v = -v$, e $\lambda v = 0_V$ solo se $\lambda = 0$ o $v = 0_V$.

Esempi fondamentali:

- $\mathbb{K}^n$, le $n$-uple di scalari, con le operazioni componente per componente; per esempio in $\mathbb{R}^4$, con $v = (1, 2, 4, 2)$ e $w = (1, 1, 1, 1)$, $v + 3w = (4, 5, 7, 5)$;
- $\mathrm{Mat}_{m \times n}(\mathbb{K})$ con la somma di matrici e il prodotto per scalari;
- $\mathbb{K}[x]$, i polinomi, con la somma di polinomi e il prodotto per costanti; e $\mathbb{K}_n[x]$, i polinomi di grado al più $n$;
- le funzioni da un insieme a $\mathbb{R}$, con le operazioni punto per punto.

## 3.2 Sottospazi

> [!definizione] Sottospazio vettoriale
> Un sottoinsieme $W \subseteq V$ è un **sottospazio** se, con le operazioni di $V$, è a sua volta uno spazio vettoriale. Basta verificare che $0_V \in W$ e che $W$ sia **chiuso** rispetto alle operazioni: $v, w \in W \Rightarrow v + w \in W$ e $\lambda \in \mathbb{K}, v \in W \Rightarrow \lambda v \in W$ (o, in una sola condizione, $\lambda v + \mu w \in W$).

> [!esempio] Sottospazi e non sottospazi
>
> - $V = \{(x, y) \in \mathbb{R}^2 \mid xy = 0\}$, l'unione dei due assi, non è un sottospazio: $(1, 0)$ e $(0, 1)$ ci stanno, ma la loro somma $(1, 1)$ no.
> - $\{(x, y, z) \mid x + 2y + z = 1\}$ non è un sottospazio, perché non contiene $(0, 0, 0)$: è un piano che non passa per l'origine.
> - $W = \{p \in \mathbb{R}[x] \mid p(1) = 0\}$ è un sottospazio: contiene il polinomio nullo e, se $p(1) = q(1) = 0$, allora $(\lambda p + \mu q)(1) = \lambda p(1) + \mu q(1) = 0$.
> - L'insieme $S = \{X \in \mathbb{K}^n \mid AX = 0\}$ delle soluzioni di un sistema **omogeneo** è un sottospazio, perché $A(\lambda X + \mu Y) = \lambda AX + \mu AY = 0$. Le soluzioni di un sistema non omogeneo $AX = B$, se esistono, sono invece della forma $X_0 + S$, con $X_0$ una soluzione particolare: un sottospazio traslato, cioè uno **spazio affine**.

L'intersezione di due sottospazi è un sottospazio. L'unione invece in generale non lo è (lo mostra il primo esempio, unione di due rette): il sottospazio "più piccolo" che contiene entrambi è la somma, paragrafo 3.5.

## 3.3 Combinazioni lineari, generatori, indipendenza

Una **combinazione lineare** dei vettori $v_1, \dots, v_k \in V$ è un vettore $\lambda_1 v_1 + \dots + \lambda_k v_k$ con $\lambda_i \in \mathbb{K}$. L'insieme di tutte le combinazioni lineari,
$$\langle v_1, \dots, v_k \rangle = \{\lambda_1 v_1 + \dots + \lambda_k v_k \mid \lambda_i \in \mathbb{K}\},$$
è un sottospazio, il **sottospazio generato** (*span*), ed è il più piccolo che contiene i $v_i$. Se $\langle v_1, \dots, v_k\rangle = V$, i vettori sono un **sistema di generatori** di $V$. Per esempio $e_1 = (1, 0)$ ed $e_2 = (0, 1)$ generano $\mathbb{R}^2$, perché $(a, b) = a e_1 + b e_2$.

> [!definizione] Indipendenza lineare
> I vettori $v_1, \dots, v_k$ sono **linearmente indipendenti** se l'unica combinazione lineare nulla è quella con tutti i coefficienti nulli:
> $$\lambda_1 v_1 + \dots + \lambda_k v_k = 0 \implies \lambda_1 = \dots = \lambda_k = 0.$$
> Altrimenti sono **linearmente dipendenti**.

I vettori sono dipendenti se e solo se uno di essi è combinazione lineare degli altri: se $\lambda_1 v_1 + \dots + \lambda_k v_k = 0$ con $\lambda_1 \neq 0$, allora $v_1 = -\frac{1}{\lambda_1}(\lambda_2 v_2 + \dots + \lambda_k v_k)$. Un vettore da solo è indipendente se e solo se non è nullo; due vettori sono dipendenti se e solo se sono proporzionali.

In $\mathbb{K}^n$ la verifica si fa con le matrici: messi i vettori in colonna in una matrice $M$, sono indipendenti se e solo se il sistema omogeneo $M\lambda = 0$ ha solo la soluzione nulla, cioè se e solo se $\mathrm{rk}(M)$ è uguale al numero dei vettori. Se i vettori sono $n$, basta che $\det M \neq 0$.

> [!esempio] Tre vettori del piano
> $v_1 = (1, 1)$, $v_2 = (2, 1)$, $v_3 = (1, 2)$ in $\mathbb{R}^2$: tre vettori in uno spazio di dimensione 2 sono dipendenti (paragrafo 3.4). Le combinazioni nulle $av_1 + bv_2 + cv_3 = 0$ sono le soluzioni di $a + 2b + c = 0$, $a + b + 2c = 0$: sottraendo, $b = c$, e poi $a = -3c$. Sono le terne $(-3c, c, c)$ con $c \in \mathbb{R}$, per esempio $-3v_1 + v_2 + v_3 = 0$.

## 3.4 Basi, dimensione, coordinate

> [!definizione] Base
> Una **base** di $V$ è un sistema di generatori linearmente indipendente.

> [!teorema] Basi e dimensione
>
> 1. Se $v_1, \dots, v_k$ sono indipendenti e $v_{k+1} \notin \langle v_1, \dots, v_k\rangle$, allora $v_1, \dots, v_{k+1}$ sono indipendenti.
> 2. Da ogni sistema finito di generatori si può estrarre una base; ogni insieme indipendente si può completare a una base.
> 3. Tutte le basi di $V$ hanno lo stesso numero di elementi, la **dimensione** $\dim V$.
> 4. Se $\dim V = n$, $n$ vettori indipendenti sono una base, e $n$ generatori sono una base; più di $n$ vettori sono dipendenti.

La dimensione di $\mathbb{K}^n$ è $n$, con la **base canonica** $e_1, \dots, e_n$; quella di $\mathbb{K}_n[x]$ è $n + 1$, con base $1, x, \dots, x^n$; quella di $\mathrm{Mat}_{m \times n}$ è $mn$. $\mathbb{K}[x]$ non ha dimensione finita. Lo spazio delle soluzioni di un sistema omogeneo $AX = 0$ in $n$ incognite ha dimensione $n - \mathrm{rk}(A)$, il numero di parametri liberi. Un sottospazio $W \subseteq V$ ha $\dim W \le \dim V$, con l'uguaglianza solo se $W = V$.

Il rango di una matrice è la dimensione del sottospazio generato dalle sue righe, e anche di quello generato dalle colonne: le operazioni elementari non cambiano lo spazio delle righe, e in una forma a scala le righe non nulle sono indipendenti.

> [!teorema] Coordinate
> Se $\mathcal{B} = (v_1, \dots, v_n)$ è una base di $V$, ogni $v \in V$ si scrive in **un solo modo** come $v = x_1 v_1 + \dots + x_n v_n$. Gli scalari $(x_1, \dots, x_n)$ sono le **coordinate** di $v$ rispetto a $\mathcal{B}$.

*Dimostrazione.* L'esistenza viene dal fatto che i $v_i$ generano. Se $v = \sum x_i v_i = \sum y_i v_i$, allora $\sum (x_i - y_i)v_i = 0$ e, per l'indipendenza, $x_i = y_i$ per ogni $i$. $\square$

Le coordinate trasformano ogni spazio di dimensione $n$ in $\mathbb{K}^n$: si lavora sulle colonne delle coordinate con le matrici.

> [!esempio] Una base di $\mathbb{R}^3$ e le coordinate di un vettore
> $v_1 = (1, 0, 1)$, $v_2 = (-1, 1, 1)$, $v_3 = (0, 1, 1)$: la matrice con queste colonne ha determinante $\begin{vmatrix} 1 & -1 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{vmatrix} = -1 \neq 0$, quindi sono tre vettori indipendenti in $\mathbb{R}^3$, cioè una base. Le coordinate di $u = (1, 1, -1)$ si trovano risolvendo $x_1 v_1 + x_2 v_2 + x_3 v_3 = u$, che dà $(x_1, x_2, x_3) = (-2, -3, 4)$: infatti $-2(1, 0, 1) - 3(-1, 1, 1) + 4(0, 1, 1) = (1, 1, -1)$.

> [!esempio] Una base di polinomi
> In $\mathbb{R}_1[x] = \{a + bx\}$, i polinomi $p_1 = 2 + x$ e $p_2 = 3 + 2x$ hanno coordinate $(2, 1)$ e $(3, 2)$ rispetto alla base $1, x$, e $\begin{vmatrix} 2 & 3 \\ 1 & 2 \end{vmatrix} = 1 \neq 0$: sono una base. Il polinomio $1 + x$ ha coordinate $(-1, 1)$ rispetto a $p_1, p_2$, perché $-(2 + x) + (3 + 2x) = 1 + x$.

## 3.5 Intersezione, somma, formula di Grassmann

> [!definizione] Somma e somma diretta
> Se $W_1, W_2$ sono sottospazi di $V$, la loro **somma** è $W_1 + W_2 = \{w_1 + w_2 \mid w_1 \in W_1,\ w_2 \in W_2\}$, il più piccolo sottospazio che contiene entrambi. Se $W_1 = \langle u_1, \dots, u_k\rangle$ e $W_2 = \langle w_1, \dots, w_h\rangle$, allora $W_1 + W_2 = \langle u_1, \dots, u_k, w_1, \dots, w_h\rangle$. La somma è **diretta**, $W_1 \oplus W_2$, se $W_1 \cap W_2 = \{0\}$: allora ogni vettore della somma si scrive in un solo modo come $w_1 + w_2$.

> [!teorema] Formula di Grassmann
> Se $V$ ha dimensione finita, $\dim(W_1 + W_2) = \dim W_1 + \dim W_2 - \dim(W_1 \cap W_2)$.

*Idea della dimostrazione.* Si prende una base $u_1, \dots, u_r$ di $W_1 \cap W_2$ e la si completa a una base di $W_1$ con $v_1, \dots, v_s$ e a una base di $W_2$ con $w_1, \dots, w_t$. Si verifica che $u_1, \dots, u_r, v_1, \dots, v_s, w_1, \dots, w_t$ è una base di $W_1 + W_2$: genera per costruzione, ed è indipendente perché una combinazione nulla porterebbe un vettore di $W_2$ a stare anche in $W_1$, quindi nell'intersezione. Contando, $r + s + t = (r + s) + (r + t) - r$. $\square$

Per calcolare l'intersezione di due sottospazi dati con dei generatori si cercano i vettori che si scrivono in entrambi i modi; se sono dati con equazioni cartesiane, basta mettere insieme le equazioni.

> [!esempio] Intersezione in $\mathbb{R}^4$
> $W_1 = \langle (1, 1, 0, 1), (1, 0, 0, 0), (2, 1, 0, -1)\rangle$ e $W_2 = \langle (1, 1, 1, 4), (1, 2, 1, 2)\rangle$. I generatori di $W_1$ sono indipendenti (rango 3), quelli di $W_2$ anche (rango 2), e i cinque vettori insieme hanno rango 4: $W_1 + W_2 = \mathbb{R}^4$. Per Grassmann $\dim(W_1 \cap W_2) = 3 + 2 - 4 = 1$. Si osserva che i vettori di $W_1$ hanno tutti terza coordinata nulla (e $W_1$ è proprio l'iperpiano $z = 0$, perché ha dimensione 3); un vettore $d(1, 1, 1, 4) + e(1, 2, 1, 2)$ di $W_2$ sta in $W_1$ se $d + e = 0$, cioè per $d = -1$, $e = 1$: $W_1 \cap W_2 = \langle (0, 1, 0, -2)\rangle$.

## 3.6 Applicazioni lineari

> [!definizione] Applicazione lineare
> Siano $V, W$ spazi vettoriali su $\mathbb{K}$. Una funzione $f : V \to W$ è **lineare** se $f(\lambda v + \mu w) = \lambda f(v) + \mu f(w)$ per ogni $v, w \in V$ e $\lambda, \mu \in \mathbb{K}$. Se $V = W$ si chiama **endomorfismo**; l'insieme degli endomorfismi si indica con $\mathrm{End}(V)$.

Una applicazione lineare manda lo zero nello zero, $f(0_V) = 0_W$: una traslazione $v \mapsto v + v_0$ con $v_0 \neq 0$ non è lineare. Esempi: $f(x, y) = (2x + y, -y)$ su $\mathbb{R}^2$; la derivata $D : \mathbb{R}_n[x] \to \mathbb{R}_{n-1}[x]$; la moltiplicazione per una matrice.

> [!teorema] Applicazioni lineari e matrici
>
> 1. Per ogni $A \in \mathrm{Mat}_{m \times n}(\mathbb{K})$, $f_A(X) = AX$ è lineare da $\mathbb{K}^n$ a $\mathbb{K}^m$.
> 2. Ogni applicazione lineare $f : \mathbb{K}^n \to \mathbb{K}^m$ è di questa forma, con $A$ la matrice che ha per colonne $f(e_1), \dots, f(e_n)$.
> 3. Più in generale un'applicazione lineare è determinata dai valori su una base, e questi si possono scegliere ad arbitrio.

La 2 viene dalla linearità: $f(x_1 e_1 + \dots + x_n e_n) = x_1 f(e_1) + \dots + x_n f(e_n) = AX$. Per esempio $f(x, y) = (2x + y, -y)$ ha matrice $\begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix}$. La composizione di applicazioni lineari corrisponde al prodotto delle matrici: $f_A \circ f_B = f_{AB}$, e questo è il motivo della definizione del prodotto righe per colonne.

## 3.7 Nucleo, immagine, teorema della dimensione

> [!definizione] Nucleo e immagine
> Il **nucleo** di $f : V \to W$ è $\ker f = \{v \in V \mid f(v) = 0_W\}$, l'**immagine** è $\mathrm{Im} f = \{f(v) \mid v \in V\}$. Sono sottospazi di $V$ e di $W$.

Per $f_A$ il nucleo è lo spazio delle soluzioni del sistema omogeneo $AX = 0$, e l'immagine è lo spazio generato dalle colonne di $A$, quindi $\dim \mathrm{Im} f_A = \mathrm{rk}(A)$. In generale, se $v_1, \dots, v_n$ generano $V$, allora $f(v_1), \dots, f(v_n)$ generano $\mathrm{Im} f$.

> [!teorema] Iniettività e nucleo
> $f$ è iniettiva se e solo se $\ker f = \{0\}$.

*Dimostrazione.* Se $f$ è iniettiva e $f(v) = 0 = f(0)$, allora $v = 0$. Viceversa, se $\ker f = \{0\}$ e $f(v) = f(w)$, allora $f(v - w) = 0$, quindi $v - w = 0$. $\square$

> [!teorema] Teorema della dimensione (rango-nullità)
> Se $V$ ha dimensione finita e $f : V \to W$ è lineare, $\dim V = \dim \ker f + \dim \mathrm{Im} f$.

*Dimostrazione.* Sia $u_1, \dots, u_k$ una base di $\ker f$, completata a una base $u_1, \dots, u_k, w_1, \dots, w_r$ di $V$. Le immagini $f(w_1), \dots, f(w_r)$ generano $\mathrm{Im} f$ (le $f(u_i)$ sono nulle) e sono indipendenti: se $\sum \lambda_j f(w_j) = 0$, allora $\sum \lambda_j w_j \in \ker f$, quindi è combinazione delle $u_i$, e per l'indipendenza della base di $V$ tutti i coefficienti sono nulli. Quindi $\dim \mathrm{Im} f = r = \dim V - k$. $\square$

Conseguenze: un'applicazione lineare fra spazi della **stessa dimensione** è iniettiva se e solo se è suriettiva, e se e solo se la sua matrice ha determinante non nullo. In questo caso è un **isomorfismo**, cioè ha un'inversa lineare. Due spazi di dimensione finita sono isomorfi se e solo se hanno la stessa dimensione: le coordinate rispetto a una base sono un isomorfismo $V \to \mathbb{K}^n$.

> [!esempio] Nucleo e immagine
> $f : \mathbb{R}^2 \to \mathbb{R}^3$, $f(x, y) = (x - 2y,\ 2x - 4y,\ y)$, ha matrice $\begin{pmatrix} 1 & -2 \\ 2 & -4 \\ 0 & 1 \end{pmatrix}$ di rango 2. Quindi $\dim \mathrm{Im} f = 2$ e $\dim \ker f = 2 - 2 = 0$: $f$ è iniettiva (lo si vede anche direttamente: $y = 0$ e $x - 2y = 0$ danno $x = y = 0$), ma non suriettiva, perché l'immagine è un piano di $\mathbb{R}^3$.
>
> La derivata $D : \mathbb{R}_2[x] \to \mathbb{R}_2[x]$ ha nucleo le costanti (dimensione 1) e immagine $\mathbb{R}_1[x]$ (dimensione 2): $1 + 2 = 3 = \dim \mathbb{R}_2[x]$. Nella base $1, x, x^2$ ha matrice $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$, perché $D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$.

## 3.8 Matrice associata e cambiamenti di base

Siano $\mathcal{B} = (v_1, \dots, v_n)$ una base di $V$ e $\mathcal{C} = (w_1, \dots, w_m)$ una base di $W$. La **matrice associata** a $f : V \to W$ rispetto a $\mathcal{B}$ e $\mathcal{C}$ è la matrice $M^{\mathcal{B}}_{\mathcal{C}}(f) \in \mathrm{Mat}_{m \times n}$ che ha nella colonna $j$ le coordinate di $f(v_j)$ rispetto a $\mathcal{C}$. Con questa matrice, se $X$ sono le coordinate di $v$, le coordinate di $f(v)$ sono $M^{\mathcal{B}}_{\mathcal{C}}(f)\, X$: l'applicazione diventa una moltiplicazione per matrice, e nucleo e immagine si calcolano come nel caso di $\mathbb{K}^n$.

La **matrice di cambiamento di base** da $\mathcal{B}'$ a $\mathcal{B}$ è la matrice $P$ che ha nelle colonne le coordinate dei vettori di $\mathcal{B}'$ rispetto a $\mathcal{B}$: è la matrice associata all'identità $V \to V$ con base $\mathcal{B}'$ in partenza e $\mathcal{B}$ in arrivo. È invertibile, e se $X'$ sono le coordinate di un vettore rispetto a $\mathcal{B}'$, quelle rispetto a $\mathcal{B}$ sono $X = PX'$.

> [!teorema] Cambiamento di base per un endomorfismo
> Se $f \in \mathrm{End}(V)$ ha matrice $A$ rispetto a $\mathcal{B}$ e $P$ è la matrice di cambiamento di base da $\mathcal{B}'$ a $\mathcal{B}$, la matrice di $f$ rispetto a $\mathcal{B}'$ è $A' = P^{-1}AP$.

Si legge da destra: $P$ porta le coordinate rispetto a $\mathcal{B}'$ in quelle rispetto a $\mathcal{B}$, $A$ applica $f$, $P^{-1}$ riporta in $\mathcal{B}'$.

> [!definizione] Matrici simili
> $A, B \in \mathrm{Mat}_n(\mathbb{K})$ sono **simili** se esiste $P \in \mathrm{GL}_n(\mathbb{K})$ con $B = P^{-1}AP$.

Matrici simili rappresentano lo stesso endomorfismo in basi diverse, e quindi hanno le stesse proprietà che non dipendono dalla base: stesso rango, stesso determinante ($\det(P^{-1}AP) = \det P^{-1}\det A\det P = \det A$ per Binet) e, come si vedrà, stesso polinomio caratteristico. Il problema del modulo 4 è trovare una base in cui la matrice sia la più semplice possibile, cioè diagonale.

## Esempi ed esercizi svolti

**Esercizio 1 (un'applicazione con un parametro).** Sia $\varphi_\lambda : \mathbb{R}^3 \to \mathbb{R}^3$, $\varphi_\lambda(x, y, z) = (x + \lambda y,\ y + \lambda z,\ z + \lambda x)$. a) Per quali $\lambda$ è suriettiva? La matrice nella base canonica è
$$A_\lambda = \begin{pmatrix} 1 & \lambda & 0 \\ 0 & 1 & \lambda \\ \lambda & 0 & 1 \end{pmatrix}, \qquad \det A_\lambda = 1 + \lambda^3.$$
Fra spazi della stessa dimensione, suriettiva vuol dire invertibile, cioè $\det A_\lambda \neq 0$: $\varphi_\lambda$ è suriettiva per ogni $\lambda \neq -1$. Per $\lambda = -1$ ha rango 2 e nucleo $\langle (1, 1, 1)\rangle$. b) La controimmagine $\varphi_2^{-1}(1, 1, 1)$ è la soluzione di $x + 2y = 1$, $y + 2z = 1$, $z + 2x = 1$: per simmetria si prova $x = y = z$, che dà $3x = 1$; poiché $\det A_2 = 9 \neq 0$ la soluzione è unica, $\left(\frac13, \frac13, \frac13\right)$.

**Esercizio 2 (verificare un sottospazio di matrici).** Le matrici simmetriche $2 \times 2$ formano un sottospazio di $\mathrm{Mat}_2(\mathbb{R})$: la somma di simmetriche e un multiplo di una simmetrica sono simmetriche, e la matrice nulla lo è. Una simmetrica si scrive $\begin{pmatrix} a & b \\ b & c \end{pmatrix} = a\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, e le tre matrici sono indipendenti: il sottospazio ha dimensione 3.

**Esercizio 3 (equazioni di uno span).** Trovare un'equazione cartesiana di $W = \langle (1, 0, 1), (0, 1, 1)\rangle \subseteq \mathbb{R}^3$. Un vettore $(x, y, z)$ sta in $W$ se la matrice con colonne $(1, 0, 1)$, $(0, 1, 1)$, $(x, y, z)$ ha rango 2, cioè determinante nullo: $\begin{vmatrix} 1 & 0 & x \\ 0 & 1 & y \\ 1 & 1 & z \end{vmatrix} = z - x - y = 0$. Quindi $W$ è il piano $x + y - z = 0$.

### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove scritte 2024-2026 e dei fogli "Spazi vettoriali", "Applicazioni lineari", "Matrici associate"; soluzioni verificate con `strumenti/verifica_ampliamento.py` (GEO-05)
> Due esercizi su cinque, in ogni prova, sono di questo modulo: sottospazi di $\mathbb{R}^4$ (basi, intersezione, somma, equazioni) e un'applicazione lineare (matrice associata, nucleo, immagine, spesso con un parametro).

**Esercizio 4. Intersezione e somma in $\mathbb{R}^4$.** $V = \{(x, y, z, t) : x + y - z = 0,\ y + t = 0\}$ e $W = \langle (1, 0, 1, 0), (1, 1, 0, 0) \rangle$. (a) Basi e dimensioni di $V$ e $W$. (b) $V \cap W$ e $V + W$, con un'equazione cartesiana di $V + W$. (c) $(1, 0, 1, 3) \in V + W$?

(a) $V$ è dato da due equazioni indipendenti in 4 incognite: $\dim V = 2$. Con $y = s$ e $x = u$ liberi, $t = -s$ e $z = u + s$: $V = \langle (1, 0, 1, 0), (0, 1, 1, -1) \rangle$. I due generatori di $W$ non sono proporzionali: $\dim W = 2$.

(b) Un vettore di $W$ è $a(1, 0, 1, 0) + b(1, 1, 0, 0) = (a + b, b, a, 0)$; sta in $V$ se $(a + b) + b - a = 2b = 0$ e $b + 0 = 0$: quindi $b = 0$, e $V \cap W = \langle (1, 0, 1, 0) \rangle$, di dimensione 1. Per Grassmann $\dim(V + W) = 2 + 2 - 1 = 3$, con base $(1, 0, 1, 0)$, $(0, 1, 1, -1)$, $(1, 1, 0, 0)$. Un iperpiano di $\mathbb{R}^4$ ha una sola equazione $ax + by + cz + dt = 0$; imponendo il passaggio per i tre vettori: $a + c = 0$, $b + c - d = 0$, $a + b = 0$. Con $b = 1$: $a = -1$, $c = 1$, $d = 2$, e
$$V + W:\ -x + y + z + 2t = 0.$$
(c) $-1 + 0 + 1 + 6 = 6 \ne 0$: no.

**Esercizio 5. Matrice associata in due basi.** Sia $f(x, y, z) = (x + y,\ y - z,\ x + z)$ e $\mathcal{F} = ((1, 1, 0), (1, 0, 1), (0, 1, 1))$. (a) $M^{\mathcal{E}}_{\mathcal{F}}(f)$, con $\mathcal{E}$ base canonica in partenza. (b) Nucleo e immagine.

(a) Nella colonna $j$ vanno le coordinate di $f(e_j)$ rispetto a $\mathcal{F}$. $f(e_1) = (1, 0, 1) = f_2$: coordinate $(0, 1, 0)$. $f(e_2) = (1, 1, 0) = f_1$: $(1, 0, 0)$. $f(e_3) = (0, -1, 1)$: si risolve $af_1 + bf_2 + cf_3 = (0, -1, 1)$, cioè $a + b = 0$, $a + c = -1$, $b + c = 1$, con soluzione $a = -1$, $b = 1$, $c = 0$. Quindi
$$M^{\mathcal{E}}_{\mathcal{F}}(f) = \begin{pmatrix} 0 & 1 & -1 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$
In alternativa, con $P$ la matrice che ha per colonne i vettori di $\mathcal{F}$, si calcola $P^{-1}A$, dove $A$ è la matrice di $f$ nella base canonica.

(b) La matrice ha rango 2, quindi $\dim\operatorname{Im} f = 2$ e, per il teorema della dimensione, $\dim\ker f = 1$. Il nucleo: $x + y = 0$, $y - z = 0$, $x + z = 0$ danno $\ker f = \langle (-1, 1, 1) \rangle$. L'immagine è generata da $f_1$ e $f_2$, cioè $\operatorname{Im} f = \langle (1, 1, 0), (1, 0, 1) \rangle$, il piano $x - y - z = 0$.

**Esercizio 6. Un'applicazione definita su una base.** $f : \mathbb{R}^3 \to \mathbb{R}^3$ è lineare con $f(1, 1, 0) = (2, 1, 1)$, $f(1, 0, 1) = (1, 1, 0)$, $f(0, 0, 1) = (1, 0, 1)$. Trovare $f(x, y, z)$ e il nucleo.

Si scrivono i vettori della base canonica come combinazioni dei tre dati: $e_3 = (0, 0, 1)$, $e_1 = (1, 0, 1) - e_3$, $e_2 = (1, 1, 0) - e_1$. Per linearità $f(e_3) = (1, 0, 1)$, $f(e_1) = (1, 1, 0) - (1, 0, 1) = (0, 1, -1)$, $f(e_2) = (2, 1, 1) - (0, 1, -1) = (2, 0, 2)$. Quindi
$$f(x, y, z) = x(0, 1, -1) + y(2, 0, 2) + z(1, 0, 1) = (2y + z,\ x,\ -x + 2y + z).$$
La seconda e la terza colonna sono proporzionali: rango 2, $\ker f = \langle (0, 1, -2) \rangle$ (infatti $f(e_2) - 2f(e_3) = 0$).

**Esercizio 7. Nucleo con un parametro.** $f_a$ ha matrice $\begin{pmatrix} 1 & 2 & 1 \\ 0 & a & 1 \\ 1 & 2 & a \end{pmatrix}$ nella base canonica. Per quali $a$ è $\ker f_a \ne \{0\}$? Basi di nucleo e immagine per $a = 0$.

$\det = 1(a^2 - 2) - 2(0 - 1) + 1(0 - a) = a^2 - a = a(a - 1)$: il nucleo non è banale per $a = 0$ e $a = 1$. Per $a = 0$ il sistema $x + 2y + z = 0$, $z = 0$, $x + 2y = 0$ dà $\ker f_0 = \langle (-2, 1, 0) \rangle$. L'immagine ha dimensione $3 - 1 = 2$ ed è generata da due colonne indipendenti, per esempio la prima e la terza: $\operatorname{Im} f_0 = \langle (1, 0, 1), (1, 1, 0) \rangle$.

**Esercizio 8. Un complemento diretto.** Sia $W = \{x_4 = 0\} \subset \mathbb{R}^4$. Trovare $S$ con $S \oplus W = \mathbb{R}^4$. È unico?

$\dim W = 3$, quindi $S$ deve avere dimensione 1 e intersecare $W$ solo nello 0: basta un vettore fuori da $W$, per esempio $S = \langle e_4 \rangle$. Non è unico: va bene $\langle (1, 2, 3, 1) \rangle$, o qualsiasi vettore con $x_4 \ne 0$. Il complemento diretto di un sottospazio esiste sempre ma non è unico (lo è il complemento ortogonale, del modulo 4).

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (GEO-05)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Da un sottospazio generato alle equazioni cartesiane.** Trovare le equazioni di $U = \langle (1, 1, 0, 1), (0, 1, 1, 0) \rangle$ in $\mathbb{R}^4$.

*Passo 1: quante equazioni.* $\dim U = 2$ in $\mathbb{R}^4$: servono $4 - 2 = 2$ equazioni indipendenti.

*Passo 2: la condizione.* $(x, y, z, t) \in U$ se la matrice con righe i due generatori e il vettore ha rango 2.

*Passo 3: ridurre.* Un vettore di $U$ è $a(1, 1, 0, 1) + b(0, 1, 1, 0) = (a, a + b, b, a)$: quindi $x = a$, $z = b$, e le altre coordinate devono essere $y = x + z$ e $t = x$.

*Passo 4: le equazioni.* $U: x - y + z = 0,\ x - t = 0$. Controllo sui generatori: $(1, 1, 0, 1)$ dà $0$ e $0$; $(0, 1, 1, 0)$ dà $0$ e $0$.

**Guidato 2. Cambiamento di base per un endomorfismo.** $f$ ha matrice $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$ nella base canonica di $\mathbb{R}^2$. Trovare la matrice rispetto a $\mathcal{B}' = ((1, 0), (1, 1))$.

*Passo 1: la matrice di passaggio.* $P$ ha per colonne i vettori di $\mathcal{B}'$: $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.

*Passo 2: $AP$.* $\begin{pmatrix} 2 & 3 \\ 0 & 3 \end{pmatrix}$.

*Passo 3: $P^{-1}AP$.* $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$.

*Passo 4: la lettura.* Nella nuova base la matrice è diagonale: $(1, 0)$ e $(1, 1)$ sono autovettori di autovalori 2 e 3. È esattamente il problema del modulo 4.

**Guidato 3. Il teorema della dimensione come controllo.** $f : \mathbb{R}^4 \to \mathbb{R}^3$ ha matrice $\begin{pmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 1 & 1 & 2 & 3 \end{pmatrix}$. Dimensioni di nucleo e immagine; $f$ è suriettiva?

*Passo 1: il rango.* La terza riga è la somma delle prime due: rango 2.

*Passo 2: l'immagine.* $\dim\operatorname{Im} f = 2 < 3$: non è suriettiva.

*Passo 3: il nucleo.* $\dim\ker f = 4 - 2 = 2$. Dalle prime due righe: $x = -z - 2t$, $y = -z - t$, quindi $\ker f = \langle (-1, -1, 1, 0), (-2, -1, 0, 1) \rangle$.

*Passo 4: controllo.* $2 + 2 = 4$, la dimensione del dominio.

## Riepilogo

Uno spazio vettoriale è un insieme con somma e prodotto per scalari che verificano gli assiomi; esempi sono $\mathbb{K}^n$, le matrici, i polinomi. Un sottospazio contiene lo zero ed è chiuso per le operazioni; le soluzioni di un sistema omogeneo ne sono un esempio, quelle di un sistema non omogeneo un sottospazio traslato. Lo span di alcuni vettori è l'insieme delle loro combinazioni lineari; i vettori sono indipendenti se l'unica combinazione nulla è quella banale, cosa che in $\mathbb{K}^n$ si controlla con il rango o il determinante. Una base è un sistema di generatori indipendente, tutte le basi hanno lo stesso numero di elementi, la dimensione, e ogni vettore ha coordinate uniche rispetto a una base. Intersezione e somma di sottospazi sono sottospazi, legati dalla formula di Grassmann. Un'applicazione lineare è determinata dai valori su una base e corrisponde a una matrice (le cui colonne sono le immagini dei vettori della base); il nucleo è un sottospazio che decide l'iniettività, l'immagine ha dimensione uguale al rango, e $\dim V = \dim\ker f + \dim\mathrm{Im} f$. Cambiando base la matrice di un endomorfismo diventa $P^{-1}AP$: matrici simili hanno rango e determinante uguali.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (GEO-05)
> Definizioni, teoremi e procedure su spazi vettoriali e applicazioni lineari, con i termini per l'orale.

### Sottospazi

- $U \subseteq V$ è un sottospazio se contiene 0 ed è chiuso per somma e prodotto per scalari. Le soluzioni di un sistema omogeneo formano un sottospazio; quelle di un sistema non omogeneo no.
- In $\mathbb{R}^n$: $\dim U$ = numero di generatori indipendenti = $n$ − numero di equazioni cartesiane indipendenti.
- **Grassmann:** $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$. Somma diretta $U \oplus W$: $U \cap W = \{0\}$.
- Per $U \cap W$: si mettono a sistema le equazioni, o si impone a una combinazione dei generatori di uno di soddisfare le equazioni dell'altro. Per $U + W$: si uniscono i generatori e si tolgono quelli dipendenti.

### Applicazioni lineari

$$f(\lambda u + \mu v) = \lambda f(u) + \mu f(v), \qquad \dim V = \dim\ker f + \dim\operatorname{Im} f, \qquad \operatorname{Im} f = \langle f(v_1), \dots, f(v_n) \rangle.$$

$f$ è iniettiva $\iff \ker f = \{0\}$; suriettiva $\iff \operatorname{rk} = \dim W$; un endomorfismo è iniettivo se e solo se è suriettivo. Un'applicazione lineare è determinata dai valori su una base.

### Matrici associate

Colonna $j$ di $M^{\mathcal{B}}_{\mathcal{C}}(f)$ = coordinate di $f(v_j)$ rispetto a $\mathcal{C}$. $M^{\mathcal{B}}_{\mathcal{D}}(g \circ f) = M^{\mathcal{C}}_{\mathcal{D}}(g)\,M^{\mathcal{B}}_{\mathcal{C}}(f)$. Cambiamento di base: $A' = P^{-1}AP$, con $P$ che ha per colonne i vettori della nuova base scritti nella vecchia.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Spazio vettoriale | insieme con somma e prodotto per scalari che rispettano gli assiomi |
| Combinazione lineare, span | somma di multipli; insieme di tutte le combinazioni |
| Linearmente indipendenti | nessuno è combinazione degli altri; l'unica combinazione nulla è quella banale |
| Base, dimensione | generatori indipendenti; numero di vettori di una base (lo stesso per tutte) |
| Coordinate | coefficienti di un vettore rispetto a una base |
| Somma diretta | somma con intersezione nulla: ogni vettore si scrive in un solo modo |
| Nucleo, immagine | vettori mandati in 0; vettori raggiunti |
| Isomorfismo | applicazione lineare biiettiva |
| Matrici simili | $B = P^{-1}AP$: stesso endomorfismo in basi diverse |

### Domande che tornano spesso

- Definire base e dimensione; perché tutte le basi hanno lo stesso numero di vettori?
- Enunciare e dimostrare la formula di Grassmann.
- Nucleo e immagine sono sottospazi: dimostrarlo. Enunciare e dimostrare il teorema della dimensione.
- Come si costruisce la matrice associata, e come cambia cambiando base?
- Proprietà invarianti per similitudine.
