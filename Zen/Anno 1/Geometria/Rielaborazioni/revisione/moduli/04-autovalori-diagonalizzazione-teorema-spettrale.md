---
corso: Geometria
modulo: 4
titolo: Autovalori, diagonalizzazione e teorema spettrale
programma: [GEO-05, GEO-06, GEO-07]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 4 · Autovalori, diagonalizzazione e teorema spettrale

**In questo modulo.** Servono le applicazioni lineari, le matrici associate e le matrici simili del modulo 3, il determinante del modulo 2 e i numeri complessi e le radici dei polinomi del modulo 1. Si cerca una base in cui un endomorfismo abbia matrice diagonale: si definiscono autovalori, autovettori e autospazi, il polinomio caratteristico, le molteplicità algebrica e geometrica, e si dimostra il criterio di diagonalizzabilità. Poi si generalizza il prodotto scalare di $\mathbb{R}^3$: prodotti scalari e hermitiani, basi ortonormali, matrici ortogonali, il procedimento di Gram-Schmidt e il complemento ortogonale. Il modulo si chiude con il teorema spettrale, per cui ogni matrice simmetrica reale si diagonalizza con una matrice ortogonale, e con gli autovalori complessi delle matrici reali. Alla fine si sa stabilire se una matrice è diagonalizzabile, trovare una base di autovettori, ortonormalizzare una base e diagonalizzare ortogonalmente una matrice simmetrica.

## 4.1 Autovalori e autovettori

> [!definizione] Autovalore, autovettore, autospazio
> Sia $f \in \mathrm{End}(V)$. Uno scalare $\lambda \in \mathbb{K}$ è un **autovalore** di $f$ se esiste un vettore $v \neq 0$ con $f(v) = \lambda v$; un tale $v$ è un **autovettore** relativo a $\lambda$. L'**autospazio** di $\lambda$ è $V_\lambda = \{v \in V \mid f(v) = \lambda v\} = \ker(f - \lambda\,\mathrm{id})$, e l'insieme degli autovalori si chiama **spettro**, $\mathrm{Sp}(f)$.

Un autovettore è una direzione che $f$ non cambia: la allunga, accorcia o rovescia del fattore $\lambda$. L'autospazio è un sottospazio (un nucleo), e contiene gli autovettori più il vettore nullo. Per una matrice $A \in \mathrm{Mat}_n(\mathbb{K})$ si parla di autovalori e autovettori di $f_A$.

Se $V$ ha una base $\mathcal{B} = (v_1, \dots, v_n)$ fatta di autovettori, con $f(v_i) = \lambda_i v_i$, la matrice di $f$ in quella base è diagonale, con $\lambda_1, \dots, \lambda_n$ sulla diagonale. È questo il motivo per cui si cercano.

> [!definizione] Endomorfismo diagonalizzabile
> $f$ è **diagonalizzabile** se esiste una base di $V$ formata da autovettori di $f$. Una matrice $A$ è diagonalizzabile se è simile a una matrice diagonale: $P^{-1}AP = D$ con $P$ invertibile, e allora le colonne di $P$ sono una base di autovettori e $D$ ha sulla diagonale i relativi autovalori.

## 4.2 Polinomio caratteristico

$\lambda$ è un autovalore di $A$ se e solo se il sistema omogeneo $(A - \lambda I_n)X = 0$ ha soluzioni non nulle, cioè se e solo se $\det(A - \lambda I_n) = 0$.

> [!definizione] Polinomio caratteristico
> Il **polinomio caratteristico** di $A \in \mathrm{Mat}_n(\mathbb{K})$ è $p_A(t) = \det(A - t I_n)$, un polinomio di grado $n$ in $t$. Gli autovalori di $A$ sono le sue radici in $\mathbb{K}$.

Matrici simili hanno lo stesso polinomio caratteristico, per Binet: $\det(P^{-1}AP - tI) = \det\big(P^{-1}(A - tI)P\big) = \det(A - tI)$. Quindi il polinomio caratteristico di un endomorfismo non dipende dalla base in cui lo si scrive. Per una matrice triangolare gli autovalori sono gli elementi della diagonale, perché $A - tI$ è ancora triangolare.

> [!definizione] Molteplicità
> Sia $\lambda$ un autovalore. La **molteplicità algebrica** $m_a(\lambda)$ è la sua molteplicità come radice di $p_A$ (l'esponente di $(t - \lambda)$ nella fattorizzazione). La **molteplicità geometrica** $m_g(\lambda) = \dim V_\lambda = n - \mathrm{rk}(A - \lambda I)$ è la dimensione dell'autospazio.

> [!teorema] Proprietà di autovettori e molteplicità
>
> 1. Autovettori relativi ad autovalori distinti sono linearmente indipendenti; quindi la somma degli autospazi è diretta.
> 2. Per ogni autovalore $1 \le m_g(\lambda) \le m_a(\lambda)$.

*Dimostrazione della 2.* Sia $k = m_g(\lambda)$ e $v_1, \dots, v_k$ una base di $V_\lambda$, completata a una base $\mathcal{B}$ di $V$. Nella base $\mathcal{B}$ la matrice di $f$ ha le prime $k$ colonne uguali a $\lambda e_1, \dots, \lambda e_k$, cioè è a blocchi $\begin{pmatrix} \lambda I_k & * \\ 0 & B \end{pmatrix}$. Il suo polinomio caratteristico è $(\lambda - t)^k \det(B - tI)$, quindi $(t - \lambda)^k$ divide $p_f$ e $m_a(\lambda) \ge k$. $\square$

## 4.3 Criterio di diagonalizzabilità

> [!teorema] Criterio di diagonalizzabilità
> $f \in \mathrm{End}(V)$, con $\dim V = n$, è diagonalizzabile se e solo se
>
> 1. $p_f$ ha tutte le radici in $\mathbb{K}$, cioè $\sum_{\lambda \in \mathrm{Sp}(f)} m_a(\lambda) = n$, e
> 2. per ogni autovalore $m_g(\lambda) = m_a(\lambda)$.
>
> In tal caso $V = V_{\lambda_1} \oplus \dots \oplus V_{\lambda_k}$, e unendo basi degli autospazi si ottiene una base di autovettori.

Infatti la somma degli autospazi è diretta e ha dimensione $\sum m_g(\lambda) \le \sum m_a(\lambda) \le n$: c'è una base di autovettori esattamente quando tutte le disuguaglianze sono uguaglianze. Un caso particolare frequente: se $A$ ha $n$ autovalori **distinti** in $\mathbb{K}$, è diagonalizzabile (ogni molteplicità algebrica è 1, e $1 \le m_g \le m_a$ forza $m_g = 1$). Basta quindi controllare la condizione 2 solo per gli autovalori con $m_a \ge 2$.

> [!esempio] Una matrice non diagonalizzabile
> $A = \begin{pmatrix} 2 & 1 & -1 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ è triangolare: $p_A(t) = (2 - t)^2(1 - t)$, con $m_a(2) = 2$ e $m_a(1) = 1$. Per $\lambda = 2$:
> $$A - 2I = \begin{pmatrix} 0 & 1 & -1 \\ 0 & 0 & 1 \\ 0 & 0 & -1 \end{pmatrix}$$
> ha rango 2, quindi $m_g(2) = 3 - 2 = 1 < 2$. La matrice non è diagonalizzabile: non c'è una base di autovettori.

> [!esempio] Una matrice diagonalizzabile
> $A = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$ è triangolare inferiore, con $p_A(t) = (2 - t)(1 - t)^2$. Per $\lambda = 1$, $A - I = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$ ha rango 1, quindi $m_g(1) = 2 = m_a(1)$ e $V_1 = \langle (0, 1, 0), (0, 0, 1)\rangle$. Per $\lambda = 2$, il nucleo di $A - 2I$ è $V_2 = \langle (1, 1, 1)\rangle$. Con $P$ che ha per colonne $(0, 1, 0)$, $(0, 0, 1)$, $(1, 1, 1)$:
> $$P^{-1}AP = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$$

Il criterio dipende dal campo: una matrice reale può non essere diagonalizzabile su $\mathbb{R}$ perché il polinomio caratteristico ha radici non reali, ed esserlo su $\mathbb{C}$ (paragrafo 4.7).

## 4.4 Prodotti scalari e hermitiani

> [!definizione] Prodotto scalare
> Un **prodotto scalare** su uno spazio reale $V$ è una funzione $\langle \cdot, \cdot\rangle : V \times V \to \mathbb{R}$ bilineare (lineare in ciascun argomento) e simmetrica, $\langle v, w\rangle = \langle w, v\rangle$. È **definito positivo** se $\langle v, v\rangle > 0$ per ogni $v \neq 0$.

Su $\mathbb{R}^n$ il **prodotto scalare standard** è $\langle X, Y\rangle = X^T Y = x_1 y_1 + \dots + x_n y_n$, definito positivo, che per $n = 3$ è quello del modulo 1. Più in generale, ogni matrice simmetrica $M$ dà il prodotto scalare $\langle X, Y\rangle_M = X^T M Y$ (simmetrico perché $(X^TMY)^T = Y^T M^T X = Y^T M X$), e ogni prodotto scalare su $\mathbb{R}^n$ è di questa forma. Per esempio $M = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ dà $\langle X, X\rangle_M = 2x_1^2 + 2x_1 x_2 + 2x_2^2 = x_1^2 + x_2^2 + (x_1 + x_2)^2$, definito positivo.

Su uno spazio complesso la simmetria non basta (con la bilinearità si avrebbe $\langle iv, iv\rangle = -\langle v, v\rangle$, e non si potrebbe avere positività). Un **prodotto hermitiano** è lineare nel secondo argomento, **antilineare** nel primo ($\langle \lambda v, w\rangle = \bar\lambda \langle v, w\rangle$) e verifica $\langle w, v\rangle = \overline{\langle v, w\rangle}$; quello standard su $\mathbb{C}^n$ è $\langle X, Y\rangle = \bar X^T Y = \sum \bar x_i y_i$, e $\langle X, X\rangle = \sum \lvert x_i\rvert^2 > 0$ per $X \neq 0$.

Con un prodotto definito positivo si definiscono la **norma** $\lVert v\rVert = \sqrt{\langle v, v\rangle}$, l'ortogonalità ($\langle v, w\rangle = 0$) e, nel caso reale, l'angolo. Vale la disuguaglianza di Cauchy-Schwarz $\lvert\langle v, w\rangle\rvert \le \lVert v\rVert\,\lVert w\rVert$.

## 4.5 Basi ortonormali, matrici ortogonali, Gram-Schmidt

Una base $(u_1, \dots, u_n)$ è **ortonormale** se $\langle u_i, u_j\rangle = 0$ per $i \neq j$ e $\lVert u_i\rVert = 1$. In una base ortonormale le coordinate si calcolano con i prodotti scalari, senza risolvere sistemi:
$$v = \langle u_1, v\rangle u_1 + \dots + \langle u_n, v\rangle u_n.$$
Infatti, se $v = \sum x_j u_j$, il prodotto con $u_i$ dà $\langle u_i, v\rangle = \sum x_j \langle u_i, u_j\rangle = x_i$. Vettori non nulli a due a due ortogonali sono sempre indipendenti, per lo stesso conto.

> [!definizione] Matrice ortogonale
> $Q \in \mathrm{Mat}_n(\mathbb{R})$ è **ortogonale** se $Q^T Q = I_n$, cioè $Q^{-1} = Q^T$. L'insieme delle matrici ortogonali si indica con $\mathrm{O}(n)$.

$Q$ è ortogonale se e solo se le sue colonne sono una base ortonormale di $\mathbb{R}^n$ (il coefficiente $(i, j)$ di $Q^TQ$ è il prodotto scalare delle colonne $i$ e $j$), e se e solo se conserva il prodotto scalare: $\langle QX, QY\rangle = X^TQ^TQY = \langle X, Y\rangle$. Per Binet $\det Q = \pm 1$; le ortogonali con determinante 1 sono le rotazioni, e formano $\mathrm{SO}(n)$. Il corrispondente complesso sono le matrici **unitarie**, con $\bar U^T U = I$, che formano $\mathrm{U}(n)$.

> [!teorema] Procedimento di Gram-Schmidt
> Se $v_1, \dots, v_n$ è una base di $V$ con un prodotto definito positivo, i vettori
> $$u_1 = \frac{v_1}{\lVert v_1\rVert}, \qquad u_k = \frac{w_k}{\lVert w_k\rVert}, \quad w_k = v_k - \sum_{i=1}^{k-1}\langle u_i, v_k\rangle\, u_i \quad (k = 2, \dots, n),$$
> formano una base ortonormale di $V$, e $\langle u_1, \dots, u_k\rangle = \langle v_1, \dots, v_k\rangle$ per ogni $k$.

A ogni passo si toglie a $v_k$ la sua proiezione sullo spazio generato dai vettori già costruiti, e si normalizza ciò che resta, che è ortogonale a tutti i precedenti. In particolare ogni spazio di dimensione finita con un prodotto definito positivo ha una base ortonormale.

> [!definizione] Complemento ortogonale
> Se $W \subseteq V$ è un sottospazio, il suo **complemento ortogonale** è $W^\perp = \{v \in V \mid \langle w, v\rangle = 0 \ \text{per ogni} \ w \in W\}$.

$W^\perp$ è un sottospazio e, per un prodotto definito positivo in dimensione finita, $V = W \oplus W^\perp$ e $\dim W^\perp = \dim V - \dim W$: completando con Gram-Schmidt una base ortonormale di $W$ a una di $V$, i vettori aggiunti sono una base di $W^\perp$. Per esempio, in $\mathbb{R}^3$ il complemento ortogonale di un piano per l'origine è la retta della sua normale.

## 4.6 Teorema spettrale

> [!definizione] Operatore autoaggiunto
> Un endomorfismo $f$ di uno spazio con prodotto scalare (o hermitiano) è **autoaggiunto** se $\langle f(v), w\rangle = \langle v, f(w)\rangle$ per ogni $v, w$.

In $\mathbb{R}^n$ con il prodotto standard, $f_A$ è autoaggiunto se e solo se $A$ è **simmetrica**: $\langle AX, Y\rangle = X^TA^TY$ e $\langle X, AY\rangle = X^TAY$. Nel caso complesso, se e solo se $A$ è **hermitiana**, $\bar A^T = A$. Più in generale, $f$ è autoaggiunto se e solo se la sua matrice in una base ortonormale è simmetrica (o hermitiana).

> [!teorema] Autovalori delle matrici simmetriche
> Gli autovalori di una matrice simmetrica reale (o hermitiana) sono tutti reali, e autovettori relativi ad autovalori distinti sono ortogonali.

*Dimostrazione.* Sia $AX = \lambda X$ con $X \in \mathbb{C}^n$ non nullo. Con il prodotto hermitiano, $\langle X, AX\rangle = \lambda\lVert X\rVert^2$ e, poiché $A$ è hermitiana, anche $\langle X, AX\rangle = \langle AX, X\rangle = \bar\lambda\lVert X\rVert^2$. Quindi $\lambda = \bar\lambda$ è reale. Se poi $AX = \lambda X$ e $AY = \mu Y$ con $\lambda \neq \mu$ reali, $\lambda\langle X, Y\rangle = \langle AX, Y\rangle = \langle X, AY\rangle = \mu\langle X, Y\rangle$, quindi $\langle X, Y\rangle = 0$. $\square$

> [!teorema] Teorema spettrale
> Sia $f$ un endomorfismo autoaggiunto di uno spazio reale con prodotto scalare definito positivo (o complesso con prodotto hermitiano definito positivo), di dimensione finita. Allora esiste una base ortonormale di $V$ formata da autovettori di $f$, e tutti gli autovalori sono reali.
>
> In forma matriciale: per ogni $A \in \mathrm{Mat}_n(\mathbb{R})$ simmetrica esistono $Q \in \mathrm{O}(n)$ e $D$ diagonale reale con $A = QDQ^T$ (cioè $Q^TAQ = D$); per ogni $A \in \mathrm{Mat}_n(\mathbb{C})$ hermitiana esistono $U \in \mathrm{U}(n)$ e $D$ diagonale reale con $A = UD\bar U^T$.

In pratica: si trovano gli autovalori, si prende una base di ciascun autospazio e la si ortonormalizza con Gram-Schmidt (autospazi diversi sono già ortogonali fra loro), e si mettono i vettori ottenuti nelle colonne di $Q$. Cambiando il segno di una colonna si può sempre avere $\det Q = 1$, cioè $Q \in \mathrm{SO}(n)$.

> [!esempio] Diagonalizzazione ortogonale
> $A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$ è simmetrica. Il polinomio caratteristico è $-t^3 + 3t + 2 = -(t - 2)(t + 1)^2$: autovalori $2$ (semplice) e $-1$ (doppio). L'autospazio $V_2$ è generato da $(1, 1, 1)$; l'autospazio $V_{-1}$ è il nucleo di $A + I$, che ha tutte le righe $(1, 1, 1)$: è il piano $x + y + z = 0$, ortogonale a $V_2$ come previsto. Una base ortonormale di $V_{-1}$ si ottiene da $(1, -1, 0)$ e dalla sua ortogonale nel piano, $(1, 1, -2)$. Quindi
> $$Q = \begin{pmatrix} \frac{1}{\sqrt3} & \frac{1}{\sqrt2} & \frac{1}{\sqrt6} \\ \frac{1}{\sqrt3} & -\frac{1}{\sqrt2} & \frac{1}{\sqrt6} \\ \frac{1}{\sqrt3} & 0 & -\frac{2}{\sqrt6} \end{pmatrix}, \qquad Q^TAQ = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix},$$
> con $\det Q = 1$.

## 4.7 Autovalori complessi delle matrici reali

Una matrice reale ha polinomio caratteristico reale, quindi le sue radici non reali vengono a coppie coniugate (modulo 1). Inoltre, se $AX = \lambda X$ con $X \in \mathbb{C}^n$, coniugando si ottiene $A\bar X = \bar\lambda\bar X$: gli autovettori di $\bar\lambda$ sono i coniugati di quelli di $\lambda$. Una matrice reale senza autovalori reali non è diagonalizzabile su $\mathbb{R}$, ma può esserlo su $\mathbb{C}$.

L'esempio tipico è la **rotazione** di un angolo $\theta$ nel piano,
$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad p(t) = t^2 - 2\cos\theta\, t + 1,$$
con radici $\cos\theta \pm i\sin\theta = e^{\pm i\theta}$. Per $\theta \neq 0, \pi$ non sono reali: nessuna direzione del piano resta fissa sotto una rotazione, come ci si aspetta. Su $\mathbb{C}$ invece gli autovalori sono distinti e $R_\theta$ è diagonalizzabile, con autovettori $(1, \mp i)$. È anche il motivo geometrico della moltiplicazione per $e^{i\theta}$ del modulo 1: in coordinate reali è proprio $R_\theta$.

## 4.8 Forme quadratiche e classificazione delle coniche

> [!aggiunta] Aggiunta in revisione · fonte: programma del corso 2025/26 ("Forme quadratiche. Applicazione alla classificazione affine delle coniche"); foglio "Matrici simmetriche e coniche" (GEO-05, GEO-06)
> **Forme quadratiche.** Una **forma quadratica** su $\mathbb{R}^n$ è un polinomio omogeneo di secondo grado, $q(x) = x^T A x$ con $A$ simmetrica: per esempio $q(x, y) = 5x^2 + 4xy + 2y^2$ ha $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ (il coefficiente del termine misto si divide a metà fra i due posti fuori diagonale). Per il teorema spettrale esiste una matrice ortogonale $P$ con $P^T A P = D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$; con il cambio di coordinate $x = PX$, che è una rotazione (eventualmente con una simmetria), la forma diventa
> $$q = \lambda_1 X_1^2 + \dots + \lambda_n X_n^2,$$
> senza termini misti. La forma è **definita positiva** se tutti gli autovalori sono positivi ($q > 0$ per $x \ne 0$), **definita negativa** se sono tutti negativi, **indefinita** se ce ne sono di segni opposti, **semidefinita** se qualcuno è nullo e gli altri hanno lo stesso segno. In due variabili basta il determinante: $\det A > 0$ dice che gli autovalori hanno lo stesso segno (quello di $a_{11}$), $\det A < 0$ che hanno segni opposti. È lo stesso criterio dell'Hessiana per i massimi e i minimi in Analisi 1B.
>
> **Coniche.** Una **conica** è il luogo dei punti del piano che soddisfano un'equazione di secondo grado
> $$a_{11}x^2 + 2a_{12}xy + a_{22}y^2 + 2a_{13}x + 2a_{23}y + a_{33} = 0,$$
> che si scrive con la matrice simmetrica $3 \times 3$
> $$\bar A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{12} & a_{22} & a_{23} \\ a_{13} & a_{23} & a_{33} \end{pmatrix}$$
> e con il suo blocco $2 \times 2$ in alto a sinistra $A$, la matrice della parte quadratica. Il tipo della conica non cambia con le rotazioni e le traslazioni, e si legge da $\det\bar A$ e da $\det A$:
>
> | $\det\bar A$ | $\det A$ | Conica |
> |---|---|---|
> | $\ne 0$ | $> 0$ | ellisse (reale se $(a_{11} + a_{22})\det\bar A < 0$, altrimenti senza punti reali) |
> | $\ne 0$ | $< 0$ | iperbole |
> | $\ne 0$ | $= 0$ | parabola |
> | $= 0$ | $> 0$ | un solo punto (due rette complesse coniugate) |
> | $= 0$ | $< 0$ | due rette incidenti |
> | $= 0$ | $= 0$ | due rette parallele o coincidenti (o nessun punto reale) |
>
> Se $\det\bar A \ne 0$ la conica è **non degenere**; se $\det\bar A = 0$ è **degenere**, e si spezza in rette. Gli autovalori di $A$ danno anche le direzioni degli assi (gli autovettori) e, per le coniche a centro, le lunghezze dei semiassi.
>
> **Esempio: riduzione a forma canonica.** $5x^2 + 4xy + 2y^2 = 6$. La parte quadratica ha autovalori 1 e 6, con autovettori $(-1, 2)$ e $(2, 1)$, ortogonali. Nelle coordinate $X, Y$ lungo questi due assi (normalizzati, $P = \frac{1}{\sqrt5}\begin{pmatrix} -1 & 2 \\ 2 & 1 \end{pmatrix}$) l'equazione diventa $X^2 + 6Y^2 = 6$, cioè
> $$\frac{X^2}{6} + Y^2 = 1:$$
> un'ellisse di semiassi $\sqrt6$ e 1, con l'asse maggiore lungo $(-1, 2)$. Con la tabella: $\det A = 6 > 0$, $\det\bar A = -36 \ne 0$ e $(5 + 2)(-36) < 0$, ellisse reale.

## Esempi ed esercizi svolti

**Esercizio 1 (Gram-Schmidt).** Ortonormalizzare $v_1 = (1, 1, 0)$, $v_2 = (1, 0, 1)$, $v_3 = (0, 1, 1)$ in $\mathbb{R}^3$. Si ha $u_1 = \frac{1}{\sqrt2}(1, 1, 0)$. Poi $\langle u_1, v_2\rangle = \frac{1}{\sqrt2}$, $w_2 = v_2 - \frac12(1, 1, 0) = \left(\frac12, -\frac12, 1\right)$, di norma $\sqrt{\frac32}$, quindi $u_2 = \frac{1}{\sqrt6}(1, -1, 2)$. Infine $\langle u_1, v_3\rangle = \frac{1}{\sqrt2}$, $\langle u_2, v_3\rangle = \frac{1}{\sqrt6}$, e
$$w_3 = (0, 1, 1) - \tfrac12(1, 1, 0) - \tfrac16(1, -1, 2) = \left(-\tfrac23, \tfrac23, \tfrac23\right), \qquad u_3 = \tfrac{1}{\sqrt3}(-1, 1, 1).$$
Si controlla che i tre vettori hanno norma 1 e prodotti scalari nulli.

**Esercizio 2 (i numeri di Fibonacci).** La successione $F_0 = 0$, $F_1 = 1$, $F_{n+1} = F_n + F_{n-1}$ si scrive in forma matriciale:
$$\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = A\begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix}, \qquad A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \text{quindi} \quad \begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = A^n\begin{pmatrix} 1 \\ 0 \end{pmatrix}.$$
Il polinomio caratteristico è $t^2 - t - 1$, con radici distinte $\varphi_\pm = \frac{1 \pm \sqrt5}{2}$: $A$ è diagonalizzabile (è anche simmetrica), $A = PDP^{-1}$, e $A^n = PD^nP^{-1}$ si calcola elevando alla $n$ i due autovalori. Si ottiene la formula di Binet
$$F_n = \frac{\varphi_+^n - \varphi_-^n}{\sqrt5},$$
che per $n = 10$ dà $F_{10} = 55$. La diagonalizzazione serve proprio a calcolare le potenze di una matrice.

**Esercizio 3 (diagonalizzabilità con un parametro).** Per quali $k \in \mathbb{R}$ la matrice $A_k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ è diagonalizzabile? L'unico autovalore è 1, con $m_a(1) = 2$, e $A_k - I = \begin{pmatrix} 0 & k \\ 0 & 0 \end{pmatrix}$ ha rango 1 se $k \neq 0$: allora $m_g(1) = 1$ e $A_k$ non è diagonalizzabile. Per $k = 0$ è già l'identità.

### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove scritte 2024-2026 e dei fogli "Diagonalizzazione" e "Matrici simmetriche e coniche"; soluzioni verificate con `strumenti/verifica_ampliamento.py` (GEO-05 … GEO-07)
> L'ultimo esercizio di ogni prova è quasi sempre una diagonalizzazione: dire se una matrice è diagonalizzabile su $\mathbb{R}$ (e su $\mathbb{C}$) e trovare $D$ e $P$.

**Esercizio 4. Diagonalizzazione ortogonale di una matrice simmetrica $3 \times 3$.** $A = \begin{pmatrix} 3 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 3 \end{pmatrix}$.

$A = 2I + J$, con $J$ la matrice di tutti 1, che ha autovalori 3 (autovettore $(1, 1, 1)$) e 0 (doppio, sul piano $x + y + z = 0$). Quindi $A$ ha autovalori $5$ e $2$ (doppio). $V_5 = \langle (1, 1, 1) \rangle$; $V_2 = \{x + y + z = 0\} = \langle (-1, 1, 0), (-1, 0, 1) \rangle$, di dimensione 2 = molteplicità algebrica: $A$ è diagonalizzabile, come garantisce il teorema spettrale. Per avere $P$ ortogonale si ortonormalizza $V_2$ con Gram-Schmidt: $u_1 = \frac{1}{\sqrt2}(-1, 1, 0)$; $(-1, 0, 1) - \frac12(-1, 1, 0) = \left(-\frac12, -\frac12, 1\right)$, cioè $u_2 = \frac{1}{\sqrt6}(-1, -1, 2)$; infine $u_3 = \frac{1}{\sqrt3}(1, 1, 1)$, già ortogonale agli altri perché autospazi di autovalori diversi di una matrice simmetrica sono ortogonali. Con $P = (u_1 \mid u_2 \mid u_3)$, $P^T A P = \operatorname{diag}(2, 2, 5)$.

**Esercizio 5. Diagonalizzabile su $\mathbb{C}$ ma non su $\mathbb{R}$.** $B = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 2 \end{pmatrix}$.

Il polinomio caratteristico è $(\lambda^2 + 1)(2 - \lambda)$ a meno del segno: in $\mathbb{R}$ c'è solo la radice 2, e la somma delle molteplicità (1) è minore di 3, quindi $B$ non è diagonalizzabile su $\mathbb{R}$. In $\mathbb{C}$ le radici $i$, $-i$, $2$ sono distinte: diagonalizzabile. Un autovettore reale esiste: $(0, 0, 1)$, di autovalore 2. Il blocco in alto è la rotazione di $90°$ del piano $xy$, che non manda nessuna retta in sé.

**Esercizio 6. Un parametro che decide.** Per quali $k$ è diagonalizzabile $C_k = \begin{pmatrix} 1 & k & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$?

Triangolare: autovalori 1 (doppio) e 2. L'autovalore 2 è semplice e non dà problemi. Per 1: $C_k - I = \begin{pmatrix} 0 & k & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ ha rango 2 se $k \ne 0$ e rango 1 se $k = 0$. La molteplicità geometrica è $3 - \operatorname{rk}$: vale 2 = molteplicità algebrica solo per $k = 0$. $C_k$ è diagonalizzabile se e solo se $k = 0$.

**Esercizio 7. Classificare una conica.** Che conica è $x^2 - 4xy + y^2 + 2x + 2y = 0$?

$\bar A = \begin{pmatrix} 1 & -2 & 1 \\ -2 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}$ (i coefficienti dei termini $xy$, $x$, $y$ si dividono a metà). $\det A = 1 - 4 = -3 < 0$ e $\det\bar A = -6 \ne 0$: iperbole non degenere. Passa per l'origine, che soddisfa l'equazione.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (GEO-05 … GEO-07)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Diagonalizzare e controllare.** $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$.

*Passo 1: polinomio caratteristico.* $\det(A - \lambda I) = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda - 2)(\lambda - 5)$.

*Passo 2: autovettori.* Per 2: $(A - 2I)v = 0$ con $A - 2I = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}$, $v = (1, -2)$. Per 5: $A - 5I = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}$, $v = (1, 1)$.

*Passo 3: $P$ e $D$.* $P = \begin{pmatrix} 1 & 1 \\ -2 & 1 \end{pmatrix}$, $D = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$, nello stesso ordine.

*Passo 4: controllo senza invertire.* Basta verificare $AP = PD$: $AP = \begin{pmatrix} 2 & 5 \\ -4 & 5 \end{pmatrix}$ e $PD = \begin{pmatrix} 2 & 5 \\ -4 & 5 \end{pmatrix}$. La traccia ($7 = 2 + 5$) e il determinante ($10 = 2 \cdot 5$) tornano.

**Guidato 2. Una famiglia di coniche.** Classificare $x^2 + 2txy + y^2 = 1$ al variare di $t \in \mathbb{R}$.

*Passo 1: le matrici.* $A = \begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}$, $\bar A = \operatorname{diag}$ a blocchi con $A$ e $-1$: $\det\bar A = -\det A = -(1 - t^2)$.

*Passo 2: $|t| < 1$.* $\det A > 0$ e $\det\bar A \ne 0$; $(1 + 1)\det\bar A < 0$: ellisse reale (per $t = 0$ la circonferenza unitaria).

*Passo 3: $|t| > 1$.* $\det A < 0$: iperbole.

*Passo 4: $t = \pm 1$.* $\det\bar A = 0$ e $\det A = 0$: degenere. Infatti $x^2 \pm 2xy + y^2 = (x \pm y)^2 = 1$ dà le due rette parallele $x \pm y = 1$ e $x \pm y = -1$.

*Passo 5: gli assi.* Gli autovalori di $A$ sono $1 + t$ e $1 - t$, con autovettori $(1, 1)$ e $(1, -1)$ per ogni $t$: gli assi sono sempre le bisettrici, e la forma canonica è $(1 + t)X^2 + (1 - t)Y^2 = 1$.

## Riepilogo

Un autovettore di $f$ è un vettore non nullo mandato in un suo multiplo $\lambda v$; gli autovalori sono le radici del polinomio caratteristico $\det(A - tI)$, che è lo stesso per matrici simili, e gli autospazi sono i nuclei di $A - \lambda I$. Autovettori di autovalori distinti sono indipendenti, e per ogni autovalore $1 \le m_g \le m_a$. Un endomorfismo è diagonalizzabile, cioè ha una base di autovettori in cui la matrice è diagonale ($P^{-1}AP = D$), se e solo se il polinomio caratteristico si spezza nel campo e ogni molteplicità geometrica è uguale a quella algebrica; $n$ autovalori distinti bastano. Un prodotto scalare (o hermitiano, nel caso complesso) definito positivo dà norme e ortogonalità; ogni spazio ha basi ortonormali, costruite con Gram-Schmidt, in cui le coordinate sono prodotti scalari, e le matrici di cambiamento di base fra basi ortonormali sono ortogonali (o unitarie). Ogni sottospazio ha un complemento ortogonale supplementare. Per il teorema spettrale un operatore autoaggiunto, cioè una matrice simmetrica reale o hermitiana, ha autovalori reali e una base ortonormale di autovettori: $Q^TAQ = D$ con $Q$ ortogonale. Una matrice reale può avere autovalori complessi coniugati, come le rotazioni, ed essere diagonalizzabile solo su $\mathbb{C}$.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (GEO-05 … GEO-07)
> Autovalori, diagonalizzazione, prodotti scalari, teorema spettrale e coniche, con i termini per l'orale.

### Autovalori e diagonalizzazione

$$Av = \lambda v,\ v \ne 0 \qquad p_A(\lambda) = \det(A - \lambda I), \qquad \operatorname{tr} A = \sum \lambda_i, \qquad \det A = \prod \lambda_i.$$

$1 \le m_g(\lambda) = n - \operatorname{rk}(A - \lambda I) \le m_a(\lambda)$. **Criterio:** $A$ è diagonalizzabile su $\mathbb{K}$ se e solo se $p_A$ ha tutte le radici in $\mathbb{K}$ e $m_g = m_a$ per ognuna. Autovalori distinti bastano. Se $P^{-1}AP = D$, le colonne di $P$ sono autovettori nello stesso ordine degli autovalori in $D$, e $A^n = PD^nP^{-1}$.

### Prodotti scalari e ortogonalità

$$\text{Gram-Schmidt: } w_k = v_k - \sum_{j < k} \langle v_k, u_j\rangle u_j, \quad u_k = \frac{w_k}{\|w_k\|}; \qquad P \text{ ortogonale} \iff P^T P = I \iff P^{-1} = P^T.$$

### Teorema spettrale

Una matrice reale simmetrica ha autovalori reali, autospazi ortogonali fra loro, ed è diagonalizzabile con una matrice ortogonale: $P^T A P = D$. (Per le hermitiane vale lo stesso con le unitarie.)

### Coniche e forme quadratiche

Forma $q = x^T A x$: definita positiva se tutti gli autovalori sono $> 0$; in due variabili, $\det A > 0$ e $a_{11} > 0$. Conica con matrice $\bar A$ e parte quadratica $A$: non degenere se $\det\bar A \ne 0$, e allora ellisse, iperbole o parabola secondo che $\det A$ sia positivo, negativo o nullo (tabella del paragrafo 4.8).

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Autovalore, autovettore, autospazio | $\lambda$ con $Av = \lambda v$ per qualche $v \ne 0$; il $v$; l'insieme dei $v$ con lo 0 |
| Molteplicità algebrica, geometrica | come radice di $p_A$; $\dim V_\lambda$ |
| Matrice diagonalizzabile | simile a una diagonale; esiste una base di autovettori |
| Prodotto scalare definito positivo | bilineare simmetrico con $\langle v, v\rangle > 0$ per $v \ne 0$ |
| Base ortonormale | vettori di norma 1 a due a due ortogonali |
| Matrice ortogonale | colonne ortonormali; rappresenta rotazioni e simmetrie |
| Forma quadratica | polinomio omogeneo di grado 2, $x^T A x$ |
| Conica degenere | si spezza in rette (o in un punto) |

### Domande che tornano spesso

- Autovettori di autovalori distinti sono indipendenti: dimostrarlo.
- Perché il polinomio caratteristico è invariante per similitudine?
- Enunciare il criterio di diagonalizzabilità; un esempio non diagonalizzabile ($\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$).
- Descrivere il procedimento di Gram-Schmidt.
- Enunciare il teorema spettrale; perché gli autovalori di una matrice simmetrica reale sono reali?
- Come si classifica una conica con gli invarianti, e come si trovano gli assi?
