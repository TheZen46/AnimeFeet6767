---
corso: Analisi Matematica 1B
modulo: 4
titolo: Equazioni differenziali ordinarie e sistemi
programma: [AM1B-08, AM1B-09, AM1B-10, AM1B-11, AM1B-12]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 4 · Equazioni differenziali ordinarie e sistemi

**In questo modulo.** Si usano le primitive del modulo 1 (*Calcolo integrale*), le derivate parziali del modulo 3 (*Funzioni di più variabili*) e, per i sistemi lineari, autovalori e autovettori dal corso di Geometria. Si parte da tre modelli (un corpo che cade nell'aria, una massa attaccata a una molla, una popolazione) che portano in modo naturale a equazioni differenziali. Poi si danno le definizioni generali e si risolvono le equazioni a variabili separabili, le lineari del primo ordine e le lineari del secondo ordine a coefficienti costanti, anche non omogenee con il metodo di somiglianza. L'ultima parte riguarda i sistemi: esistenza e unicità per il problema di Cauchy, struttura delle soluzioni dei sistemi lineari, calcolo dell'integrale generale con autovalori e autovettori, stabilità dell'equilibrio. Alla fine del modulo si sanno riconoscere e risolvere i tipi di equazione del programma, impostare un problema di Cauchy e valutare se la soluzione trovata è plausibile.

## 4.1 Tre modelli

**Caduta con attrito.** Un corpo di massa $m$ cade soggetto al peso $-mg$ e a un attrito viscoso $-kv$, con $k > 0$, proporzionale alla velocità e opposto al moto. Se $y(t)$ è la quota, la velocità è $y'$ e l'accelerazione $y''$, e la legge di Newton $F = ma$ diventa
$$m y'' = -mg - k y'.$$
È un'equazione del secondo ordine. Se il corpo parte da fermo dalla quota $h_0$, servono anche le condizioni $y(0) = h_0$, $y'(0) = 0$. La velocità tende alla **velocità limite** $v_{lim} = -\frac{mg}{k}$, per cui peso e attrito si bilanciano, e la soluzione è
$$y(t) = h_0 - \frac{mg}{k}\,t + \frac{m^2 g}{k^2}\left(1 - e^{-\frac{k}{m}t}\right).$$

**Massa e molla.** Una massa $m$ su un piano senza attrito è attaccata a una molla di costante $k$; lo spostamento $x(t)$ dall'equilibrio subisce la forza di richiamo $-kx$ (legge di Hooke). Da $m x'' = -kx$, posto $\omega^2 = \frac{k}{m}$:
$$x'' + \omega^2 x = 0,$$
l'equazione del **moto armonico**, con soluzioni $x(t) = c_1\cos(\omega t) + c_2\sin(\omega t)$; le costanti si fissano con la posizione e la velocità iniziali.

**Popolazioni.** Se $y(t)$ è il numero di individui, il modello di Malthus suppone la crescita proporzionale alla popolazione, $y' = \varepsilon y$. Il modello **logistico** (di Verhulst) tiene conto delle risorse limitate con una **capacità portante** $K$:
$$y' = \varepsilon y\left(1 - \frac{y}{K}\right).$$
Le funzioni costanti $y \equiv 0$ e $y \equiv K$ sono soluzioni (di **equilibrio**). Con $y(0) = P_0 \in (0, K)$ la popolazione cresce e si avvicina a $K$; la soluzione è $y(t) = \frac{K P_0 e^{\varepsilon t}}{K - P_0 + P_0 e^{\varepsilon t}}$.

## 4.2 Definizioni

> [!definizione] Equazione differenziale ordinaria
> Un'**equazione differenziale ordinaria** (EDO) di ordine $n$ è un'equazione $F\big(t, y(t), y'(t), \dots, y^{(n)}(t)\big) = 0$, dove $F$ è una funzione assegnata di $n + 2$ variabili e l'incognita è una funzione $y : I \to \mathbb{R}$, derivabile $n$ volte su un intervallo $I$, che la soddisfa per ogni $t \in I$. L'**ordine** è quello della derivata più alta. L'insieme di tutte le soluzioni è l'**integrale generale**.

> [!definizione] Problema di Cauchy
> Il **problema di Cauchy** associa all'equazione di ordine $n$ le $n$ **condizioni iniziali** $y(t_0) = y_0$, $y'(t_0) = y_1$, …, $y^{(n-1)}(t_0) = y_{n-1}$ in un punto $t_0$. Una soluzione è una funzione $y \in C^n(I)$, su un intervallo aperto $I \ni t_0$, che soddisfa l'equazione e tutte le condizioni.

Un'equazione è **autonoma** se $F$ non dipende esplicitamente da $t$ ($y'' + y = 0$ lo è, $y'' + ty = t$ no); è in **forma normale** se si può scrivere $y^{(n)} = f(t, y, \dots, y^{(n-1)})$; è **lineare** se ha la forma
$$a_n(t)\, y^{(n)} + \dots + a_1(t)\, y' + a_0(t)\, y = b(t),$$
**omogenea** se $b = 0$, **a coefficienti costanti** se le $a_i$ sono costanti.

> [!teorema] Struttura delle soluzioni di un'equazione lineare
> Se $y_p$ è una soluzione dell'equazione lineare completa, tutte le soluzioni sono $y = y_o + y_p$, con $y_o$ che varia fra le soluzioni dell'omogenea associata. Inoltre, se il termine noto è $b = b_1 + b_2$ e $y_1$, $y_2$ risolvono le equazioni con termini noti $b_1$ e $b_2$, allora $y_1 + y_2$ risolve quella con termine noto $b$ (**principio di sovrapposizione**).

Entrambe le affermazioni vengono dalla linearità: la differenza di due soluzioni della completa risolve l'omogenea.

## 4.3 Equazioni a variabili separabili

> [!definizione] Equazione a variabili separabili
> È un'equazione del primo ordine della forma $y' = g(t)\, h(y)$, con $g : I \to \mathbb{R}$ e $h : J \to \mathbb{R}$ continue su intervalli aperti.

**Metodo.** (1) Si cercano le soluzioni costanti: se $h(y_0) = 0$, la funzione $y \equiv y_0$ è una soluzione. (2) Dove $h(y) \neq 0$ si divide: $\frac{y'(t)}{h(y(t))} = g(t)$. Se $H$ è una primitiva di $\frac{1}{h}$ e $G$ una di $g$, il primo membro è la derivata di $H(y(t))$, quindi
$$H(y(t)) = G(t) + C,$$
e, se $H$ è invertibile, $y(t) = H^{-1}(G(t) + C)$. (3) L'integrale generale è l'unione di queste soluzioni e di quelle costanti. Il procedimento si ricorda separando formalmente i differenziali: $\int \frac{dy}{h(y)} = \int g(t)\, dt$.

> [!teorema] Problema di Cauchy per le equazioni separabili
> Siano $g$ continua su $I$, $h$ continua su $J$, $t_0 \in I$, $y_0 \in J$. Il problema $y' = g(t)h(y)$, $y(t_0) = y_0$ ha almeno una soluzione definita in un intervallo contenente $t_0$. La soluzione è unica (vicino a $t_0$) se $h$ è di classe $C^1$, o più in generale localmente lipschitziana, su $J$; è unica anche se $h(y_0) \neq 0$.

> [!esempio] Crescita esponenziale
> $y' = ky$: $h(y) = y$ si annulla in 0, quindi $y \equiv 0$ è soluzione. Per $y \neq 0$: $\int\frac{dy}{y} = \int k\, dt$, $\ln\lvert y\rvert = kt + C$, $y = \pm e^C e^{kt}$. Includendo la soluzione nulla, l'integrale generale è $y(t) = \alpha e^{kt}$ con $\alpha \in \mathbb{R}$. Con $y(0) = 1$ e $k = 1$ si ottiene $y(t) = e^t$.

> [!esempio] Equazione logistica
> $y' = 2y(1 - y)$ ha le soluzioni costanti $y = 0$ e $y = 1$. Per $y \neq 0, 1$, con i fratti semplici $\frac{1}{y(1 - y)} = \frac{1}{y} + \frac{1}{1 - y}$:
> $$\ln\lvert y\rvert - \ln\lvert 1 - y\rvert = 2t + C, \qquad \frac{y}{1 - y} = \alpha e^{2t}, \qquad y(t) = \frac{\alpha e^{2t}}{1 + \alpha e^{2t}}, \quad \alpha \neq 0.$$
> Con $y(0) = 2$: $\frac{\alpha}{1 + \alpha} = 2$, cioè $\alpha = -2$, e $y(t) = \frac{2e^{2t}}{2e^{2t} - 1}$, definita per $t > -\frac{\ln 2}{2}$ (dove il denominatore è positivo), decrescente e con limite 1.

> [!esempio] Pennello di Peano: manca l'unicità
> $y' = \sqrt[3]{y}$, $y(0) = 0$. La funzione $y \equiv 0$ è una soluzione. Ma $h(y) = y^{1/3}$ non è lipschitziana vicino a 0, e il teorema non garantisce l'unicità. Separando per $y > 0$: $\frac{3}{2}y^{2/3} = t + C$; con $C = 0$ si trova $y(t) = \left(\frac{2t}{3}\right)^{3/2}$ per $t \ge 0$. La funzione che vale 0 per $t < 0$ e $\left(\frac{2t}{3}\right)^{3/2}$ per $t \ge 0$ è di classe $C^1$, risolve l'equazione e soddisfa $y(0) = 0$. Spostando il punto di raccordo, cioè usando $\left(\frac{2(t - \tau)}{3}\right)^{3/2}$ per $t \ge \tau$ con $\tau \ge 0$, si ottengono infinite soluzioni dello stesso problema.

## 4.4 Equazioni lineari del primo ordine

L'equazione è $y' = a(t)\, y + b(t)$, con $a$, $b$ continue su $I$. Sia $A$ una primitiva di $a$.

- **Omogenea**, $y' = a(t)y$: è separabile, e come nell'esempio precedente l'integrale generale è $y(t) = C e^{A(t)}$, $C \in \mathbb{R}$.
- **Completa**: l'integrale generale è
$$y(t) = e^{A(t)}\left(\int b(t)\, e^{-A(t)}\, dt\right) = e^{A(t)}\big(K(t) + \alpha\big), \quad \alpha \in \mathbb{R},$$
dove $K$ è una primitiva di $b\, e^{-A}$.

La formula si verifica derivando: $\big(e^{A}(K + \alpha)\big)' = a\, e^{A}(K + \alpha) + e^{A} b\, e^{-A} = a\,y + b$. Si ottiene con il metodo della **variazione delle costanti** (si cerca una soluzione $C(t)\, e^{A(t)}$) o moltiplicando l'equazione per il **fattore integrante** $e^{-A(t)}$.

> [!esempio] Un problema di Cauchy
> $y' = -\sin t\; y + \sin t$, $y(0) = 3$. Qui $a(t) = -\sin t$, $A(t) = \cos t$, e $K(t) = \int \sin t\; e^{-\cos t}\, dt = e^{-\cos t}$. Quindi $y(t) = e^{\cos t}\left(e^{-\cos t} + \alpha\right) = 1 + \alpha e^{\cos t}$. Da $y(0) = 1 + \alpha e = 3$ si ha $\alpha = \frac{2}{e}$ e $y(t) = 1 + 2e^{\cos t - 1}$.

## 4.5 Equazioni lineari del secondo ordine a coefficienti costanti

L'equazione è $y'' + a y' + b y = f(t)$ con $a, b \in \mathbb{R}$.

**Omogenea.** Si cercano soluzioni della forma $e^{\lambda t}$: sostituendo si ottiene $e^{\lambda t}(\lambda^2 + a\lambda + b) = 0$, quindi $\lambda$ deve essere radice del **polinomio caratteristico** $P(\lambda) = \lambda^2 + a\lambda + b$. Secondo il discriminante $\Delta = a^2 - 4b$:

| Caso | Radici | Integrale generale dell'omogenea |
|---|---|---|
| $\Delta > 0$ | $\lambda_1 \neq \lambda_2$ reali | $c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$ |
| $\Delta = 0$ | $\lambda = -\frac{a}{2}$ doppia | $e^{\lambda t}(c_1 + c_2 t)$ |
| $\Delta < 0$ | $\alpha \pm i\beta$, con $\alpha = -\frac{a}{2}$, $\beta = \frac{\sqrt{-\Delta}}{2}$ | $e^{\alpha t}\big(c_1\cos(\beta t) + c_2\sin(\beta t)\big)$ |

Nel caso $\Delta < 0$ le funzioni $e^{(\alpha \pm i\beta)t}$ sono soluzioni complesse, e con la formula di Eulero se ne prendono parte reale e immaginaria, $e^{\alpha t}\cos(\beta t)$ ed $e^{\alpha t}\sin(\beta t)$. Nel caso $\Delta = 0$ la seconda soluzione $t e^{\lambda t}$ si verifica sostituendo: si ottiene $(2\lambda + a)e^{\lambda t} + P(\lambda)\, t e^{\lambda t}$, e entrambi i termini sono nulli perché $\lambda = -\frac{a}{2}$ è radice.

**Completa: metodo di somiglianza.** Per certi termini noti si conosce la forma di una soluzione particolare $y_p$, con coefficienti da determinare sostituendo nell'equazione.

- Se $f(t) = P_n(t)\, e^{\alpha t}$, con $P_n$ polinomio di grado $n$: $y_p = t^\mu Q_n(t)\, e^{\alpha t}$, con $Q_n$ polinomio di grado $n$ da determinare e $\mu$ la molteplicità di $\alpha$ come radice di $P$ ($\mu = 0$ se non è radice).
- Se $f(t) = P_n(t)\, e^{\alpha t}\cos(\beta t)$ (o con il seno): $y_p = t^\mu e^{\alpha t}\big(R_n(t)\cos(\beta t) + S_n(t)\sin(\beta t)\big)$, con $\mu$ la molteplicità di $\alpha + i\beta$.
- Se $f$ è una somma di termini di questo tipo, si sommano le soluzioni particolari (sovrapposizione).

> [!esempio] Due soluzioni particolari
>
> - $y'' + y = t^2$. $P(\lambda) = \lambda^2 + 1$ ha radici $\pm i$; $\alpha = 0$ non è radice, quindi $y_p = At^2 + Bt + C$. Sostituendo, $2A + At^2 + Bt + C = t^2$: $A = 1$, $B = 0$, $C = -2$. L'integrale generale è $y = c_1\cos t + c_2\sin t + t^2 - 2$.
> - $y'' + y = t^2\cos t$. Qui $\alpha + i\beta = i$ è radice semplice, quindi $\mu = 1$ e $y_p = t\big((At^2 + Bt + C)\cos t + (Dt^2 + Et + F)\sin t\big)$, con sei coefficienti da trovare sostituendo.

## 4.6 Sistemi: esistenza e unicità

Un **sistema del primo ordine** in forma normale è $y' = f(t, y)$, con $y(t) \in \mathbb{R}^n$ e $f : I \times D \to \mathbb{R}^n$, $I$ intervallo aperto e $D \subseteq \mathbb{R}^n$ aperto. Il problema di Cauchy aggiunge $y(t_0) = y_0$.

> [!teorema] Esistenza e unicità locale
> Se $f$ è continua su $I \times D$, per ogni $t_0 \in I$ e $y_0 \in D$ il problema di Cauchy ha una soluzione su un intervallo $J \ni t_0$. Se inoltre le derivate parziali $\frac{\partial f_i}{\partial y_j}$ sono continue (o, più in generale, $f$ è localmente lipschitziana in $y$), la soluzione è unica.

> [!teorema] Esistenza globale
> Se, oltre alle ipotesi di unicità, $f$ è **sublineare** in $y$, cioè $\lVert f(t, y)\rVert \le \alpha(t) + \beta(t)\lVert y\rVert$ con $\alpha$, $\beta$ continue e non negative (e $D = \mathbb{R}^n$), la soluzione è definita su tutto $I$.

> [!esempio] Globale e non globale
>
> - $y' = t^2\sin y + e^t y$: $f$ è di classe $C^1$ e $\lvert f\rvert \le t^2 + e^t\lvert y\rvert$. Ogni problema di Cauchy ha un'unica soluzione definita su tutto $\mathbb{R}$.
> - $y' = y^2$, $y(0) = 1$: $f$ è $C^1$, quindi la soluzione è unica, ma $y^2$ cresce più che linearmente. Separando si trova $y(t) = \frac{1}{1 - t}$, che "esplode" per $t \to 1^-$: la soluzione è definita solo su $(-\infty, 1)$.

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 2* (AM1B-09)
> **Un'equazione di ordine $n$ è un sistema.** Ponendo $y_1 = y$, $y_2 = y'$, …, $y_n = y^{(n-1)}$, l'equazione $y^{(n)} = f(t, y, \dots, y^{(n-1)})$ diventa il sistema del primo ordine $y_1' = y_2$, …, $y_{n-1}' = y_n$, $y_n' = f(t, y_1, \dots, y_n)$. Per questo i teoremi sui sistemi valgono anche per le equazioni di ordine $n$, e il problema di Cauchy richiede $n$ condizioni iniziali.

## 4.7 Sistemi lineari

Un **sistema lineare** è $y' = A(t)\, y + b(t)$, con $A(t)$ matrice $n \times n$ e $b(t) \in \mathbb{R}^n$ continue su $I$. Poiché $\lVert A(t)y\rVert \le \lVert A(t)\rVert\, \lVert y\rVert$, la condizione di sublinearità vale sempre.

> [!teorema] Sistemi lineari
>
> 1. Ogni problema di Cauchy per un sistema lineare ha un'unica soluzione, definita su tutto $I$.
> 2. Le soluzioni dell'omogeneo $y' = A(t)y$ formano uno spazio vettoriale di dimensione $n$.
> 3. Le soluzioni del sistema completo sono $y = y_o + y_p$, con $y_p$ una soluzione particolare e $y_o$ le soluzioni dell'omogeneo.

Se $\varphi_1, \dots, \varphi_n$ sono soluzioni linearmente indipendenti dell'omogeneo, la matrice che le ha come colonne, $W(t) = \big(\varphi_1(t) \mid \dots \mid \varphi_n(t)\big)$, si chiama **matrice fondamentale**, e ogni soluzione è $y(t) = W(t)\, c$ con $c \in \mathbb{R}^n$. La soluzione con $y(t_0) = y_0$ si ottiene da $W(t_0)c = y_0$:
$$y(t) = W(t)\, W(t_0)^{-1}\, y_0.$$
Per il sistema completo si cerca una soluzione $y_p = W(t)\, k(t)$ (**variazione delle costanti**).

## 4.8 Sistemi lineari a coefficienti costanti

Se $A$ è costante si cercano soluzioni $y(t) = v\, e^{\lambda t}$ con $v \neq 0$. Sostituendo: $\lambda v e^{\lambda t} = A v e^{\lambda t}$, cioè $Av = \lambda v$. Quindi $\lambda$ deve essere un **autovalore** di $A$, radice di $P(\lambda) = \det(A - \lambda I)$, e $v$ un **autovettore**.

Per ogni autovalore la **molteplicità algebrica** $m_a$ è la molteplicità come radice di $P$, la **molteplicità geometrica** $m_g$ la dimensione dell'autospazio $\ker(A - \lambda I)$; sempre $1 \le m_g \le m_a$, e l'autovalore è **regolare** se $m_g = m_a$. Se tutti gli autovalori sono regolari, $A$ è diagonalizzabile, ci sono $n$ autovettori indipendenti $v_i$ e l'integrale generale è $y(t) = \sum c_i\, v_i\, e^{\lambda_i t}$.

> [!esempio] Un sistema $2 \times 2$
> $y_1' = 2y_1 + 3y_2$, $y_2' = 2y_1 + y_2$. Con $A = \begin{pmatrix} 2 & 3 \\ 2 & 1 \end{pmatrix}$: $P(\lambda) = (2 - \lambda)(1 - \lambda) - 6 = \lambda^2 - 3\lambda - 4 = (\lambda - 4)(\lambda + 1)$. Per $\lambda = 4$: $2v_1 + 3v_2 = 4v_1$, cioè $2v_1 = 3v_2$, $v = (3, 2)$. Per $\lambda = -1$: $3v_1 = -3v_2$, $v = (1, -1)$. Quindi
> $$y(t) = c_1 e^{4t}\begin{pmatrix} 3 \\ 2 \end{pmatrix} + c_2 e^{-t}\begin{pmatrix} 1 \\ -1 \end{pmatrix}.$$

> [!esempio] Un sistema $3 \times 3$
> $A = \begin{pmatrix} 0 & 1 & -1 \\ 2 & 1 & 6 \\ 0 & 1 & -1 \end{pmatrix}$ ha $P(\lambda) = -\lambda(\lambda - 3)(\lambda + 3)$. Gli autovettori sono $(7, -2, -2)$ per $\lambda = 0$, $(1, 4, 1)$ per $\lambda = 3$ e $(1, -2, 1)$ per $\lambda = -3$, e
> $$y(t) = c_1\begin{pmatrix} 7 \\ -2 \\ -2 \end{pmatrix} + c_2 e^{3t}\begin{pmatrix} 1 \\ 4 \\ 1 \end{pmatrix} + c_3 e^{-3t}\begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}.$$

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 2* (AM1B-11)
> **Autovalori complessi.** Se $A$ è reale e ha l'autovalore $\lambda = \alpha + i\beta$, $\beta \neq 0$, con autovettore $v = u + iw$, la soluzione complessa $v\, e^{\lambda t}$ dà due soluzioni reali indipendenti, la sua parte reale e la sua parte immaginaria:
> $$e^{\alpha t}\big(u\cos(\beta t) - w\sin(\beta t)\big), \qquad e^{\alpha t}\big(u\sin(\beta t) + w\cos(\beta t)\big).$$
> Per esempio $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ ha autovalori $\pm i$, con autovettore $(1, i)$ per $i$: le soluzioni reali sono $(\cos t, -\sin t)$ e $(\sin t, \cos t)$.

**Autovalori non regolari.** Se $m_g < m_a$ mancano autovettori, e si usano gli **autovettori generalizzati**: partendo da un autovettore $v^{(0)}$ si risolvono a catena $(A - \lambda I)v^{(1)} = v^{(0)}$, $(A - \lambda I)v^{(2)} = v^{(1)}$, …, e alla catena corrispondono le soluzioni
$$v^{(0)} e^{\lambda t}, \qquad \big(v^{(1)} + t\, v^{(0)}\big) e^{\lambda t}, \qquad \left(v^{(2)} + t\, v^{(1)} + \frac{t^2}{2} v^{(0)}\right) e^{\lambda t}, \quad \dots$$
che completano la base.

> [!esempio] Un autovalore doppio con un solo autovettore
> $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & -4 & 4 \end{pmatrix}$ ha $P(\lambda) = -\lambda^3 + 4\lambda^2 - 4\lambda = -\lambda(\lambda - 2)^2$. Per $\lambda = 0$ l'autovettore è $(1, 0, 0)$. Per $\lambda = 2$, $(A - 2I)v = 0$ dà $-2v_1 + v_2 = 0$ e $-2v_2 + v_3 = 0$: un solo autovettore, $v^{(0)} = (1, 2, 4)$, quindi $m_g = 1 < m_a = 2$. L'autovettore generalizzato risolve $(A - 2I)v^{(1)} = v^{(0)}$: $-2a + b = 1$, $-2b + c = 2$, e si può scegliere $v^{(1)} = (0, 1, 4)$. L'integrale generale è
> $$y(t) = c_1\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + c_2 e^{2t}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix} + c_3 e^{2t}\begin{pmatrix} t \\ 1 + 2t \\ 4 + 4t \end{pmatrix}.$$

## 4.9 Stabilità dell'equilibrio

> [!definizione] Stabilità
> Sia $\tilde{y}$ un punto di equilibrio del sistema $y' = f(t, y)$, cioè $f(t, \tilde{y}) = 0$ per ogni $t$, così che $y \equiv \tilde{y}$ è una soluzione. $\tilde{y}$ è **stabile** (secondo Ljapunov) se per ogni $\varepsilon > 0$ esiste $\delta > 0$ tale che ogni soluzione con $\lVert y(t_0) - \tilde{y}\rVert < \delta$ soddisfa $\lVert y(t) - \tilde{y}\rVert < \varepsilon$ per ogni $t \ge t_0$. È **asintoticamente stabile** se è stabile e inoltre $y(t) \to \tilde{y}$ per $t \to +\infty$.

> [!teorema] Stabilità dei sistemi lineari a coefficienti costanti
> Per $y' = Ay$ l'origine è un equilibrio, e:
>
> 1. è asintoticamente stabile se e solo se ogni autovalore ha parte reale negativa;
> 2. è stabile se ogni autovalore ha parte reale $\le 0$ e quelli con parte reale nulla sono regolari;
> 3. è instabile negli altri casi: c'è un autovalore con parte reale positiva, oppure uno con parte reale nulla e non regolare.

Il motivo sta nella forma delle soluzioni: per un autovalore $\alpha + i\beta$ compaiono termini $t^k e^{\alpha t}\cos(\beta t)$ e $t^k e^{\alpha t}\sin(\beta t)$, con potenze $t^k$ solo se l'autovalore non è regolare. Se $\alpha < 0$ l'esponenziale porta tutto a zero anche in presenza delle potenze; se $\alpha = 0$ i termini restano limitati solo se non ci sono potenze; se $\alpha > 0$ crescono.

> [!esempio] Oscillatore smorzato
> $y'' + k y' + y = 0$, con $k \in \mathbb{R}$. Con $y_1 = y$, $y_2 = y'$ diventa il sistema con matrice $\begin{pmatrix} 0 & 1 \\ -1 & -k \end{pmatrix}$, il cui polinomio caratteristico è $\lambda^2 + k\lambda + 1$, con radici $\frac{-k \pm \sqrt{k^2 - 4}}{2}$.
>
> - $k > 0$ (attrito): per $k \ge 2$ radici reali negative, per $0 < k < 2$ complesse con parte reale $-\frac{k}{2} < 0$. In entrambi i casi l'origine è asintoticamente stabile: le oscillazioni si smorzano.
> - $k = 0$: radici $\pm i$, semplici. L'origine è stabile ma non asintoticamente: le traiettorie nel piano $(y, y')$ sono circonferenze, il moto armonico non si smorza.
> - $k < 0$: almeno una radice ha parte reale positiva e l'origine è instabile: il sistema riceve energia.

## 4.10 Il piano delle fasi dei sistemi lineari $2 \times 2$

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 2*; dispense del corso, § stabilità; ricostruzione della lezione 22 (19/05/2026), di cui mancano gli appunti, fra la lezione 21 sui sistemi lineari e la 23 (AM1B-09, AM1B-11)
> Per un sistema $y' = Ay$ con $A$ matrice reale $2 \times 2$ e $\det A \ne 0$, l'unico equilibrio è l'origine. Disegnando nel piano $(y_1, y_2)$ le traiettorie, cioè le curve $t \mapsto (y_1(t), y_2(t))$, si ottiene il **ritratto di fase**, che ha poche forme possibili decise dagli autovalori $\lambda_1, \lambda_2$.
>
> | Autovalori | Nome | Stabilità dell'origine |
> |---|---|---|
> | reali, entrambi negativi | nodo stabile: le traiettorie entrano nell'origine | asintoticamente stabile |
> | reali, entrambi positivi | nodo instabile: le traiettorie escono | instabile |
> | reali, di segno opposto | sella: si entra lungo un autovettore e si esce lungo l'altro | instabile |
> | $\alpha \pm i\beta$ con $\alpha < 0$ | fuoco stabile: spirali verso l'origine | asintoticamente stabile |
> | $\alpha \pm i\beta$ con $\alpha > 0$ | fuoco instabile: spirali verso l'esterno | instabile |
> | $\pm i\beta$ | centro: curve chiuse (ellissi) intorno all'origine | stabile, non asintoticamente |
>
> Gli autovalori sono le radici di $\lambda^2 - (\operatorname{tr} A)\,\lambda + \det A = 0$, quindi la classificazione si legge anche da **traccia** e **determinante**: se $\det A < 0$ è una sella; se $\det A > 0$ e $\operatorname{tr} A < 0$ l'origine è asintoticamente stabile (nodo se $(\operatorname{tr} A)^2 \ge 4\det A$, fuoco altrimenti); se $\det A > 0$ e $\operatorname{tr} A > 0$ è instabile; se $\det A > 0$ e $\operatorname{tr} A = 0$ è un centro.
>
> **Esempi.** $A = \begin{pmatrix} -2 & 1 \\ 0 & -3 \end{pmatrix}$: autovalori $-2$, $-3$, nodo stabile. $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$: sella, con soluzioni $y_1 = c_1 e^t$, $y_2 = c_2 e^{-t}$, e traiettorie sulle iperboli $y_1 y_2 = c_1 c_2$. $A = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}$: $\operatorname{tr} A = 2$, $\det A = 5$, autovalori $1 \pm 2i$, fuoco instabile. $A = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}$, cioè $y'' + 4y = 0$ scritto come sistema: autovalori $\pm 2i$, centro; le traiettorie sono le ellissi $4y_1^2 + y_2^2 = \text{cost}$, che sono la conservazione dell'energia dell'oscillatore armonico.
>
> **Linearizzazione.** Per un sistema non lineare autonomo $y' = F(y)$ con $F$ di classe $C^1$ e un equilibrio $\tilde{y}$ ($F(\tilde{y}) = 0$), vicino a $\tilde{y}$ il sistema si comporta come quello lineare con la matrice jacobiana $J = DF(\tilde{y})$. Vale il **teorema di linearizzazione**: se tutti gli autovalori di $J$ hanno parte reale negativa, $\tilde{y}$ è asintoticamente stabile; se almeno uno ha parte reale positiva, è instabile. Se ci sono autovalori con parte reale nulla (centri, per esempio) il teorema non conclude.
>
> Per una sola equazione autonoma $y' = f(y)$ il criterio diventa: un equilibrio $\tilde{y}$ è asintoticamente stabile se $f'(\tilde{y}) < 0$ e instabile se $f'(\tilde{y}) > 0$. Per l'equazione logistica $y' = y(1 - y)$, con $f'(y) = 1 - 2y$: $f'(0) = 1 > 0$, l'equilibrio 0 è instabile; $f'(1) = -1 < 0$, l'equilibrio 1 è asintoticamente stabile. Lo si vede anche dal segno di $f$: fra 0 e 1 le soluzioni crescono verso 1, sopra 1 decrescono verso 1.

## 4.11 Studio qualitativo senza risolvere

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 2*; prove scritte 2025-2026 (AM1B-08, AM1B-10)
> Molte domande d'esame chiedono informazioni sulla soluzione di un problema di Cauchy $y' = f(t, y)$, $y(t_0) = y_0$, *senza risolverlo*. Gli strumenti sono quattro.
>
> **1. Esistenza e unicità locale.** Se $f$ e $\frac{\partial f}{\partial y}$ sono continue in un intorno di $(t_0, y_0)$, il teorema di Cauchy garantisce una e una sola soluzione in un intorno di $t_0$. Basta controllare queste due continuità nel punto: per $y' = t e^{-y}$, $f$ e $f_y = -t e^{-y}$ sono continue ovunque, e il problema ha soluzione unica per ogni dato iniziale. Per $y' = \sqrt{|y|}$ con $y(0) = 0$, invece, $f_y$ non esiste in $y = 0$, e infatti le soluzioni sono infinite ($y \equiv 0$ e $y = \frac{t^2}{4}$ per $t \ge 0$, per esempio).
>
> **2. Derivate nel punto iniziale.** L'equazione dà subito $y'(t_0) = f(t_0, y_0)$. Derivando l'equazione rispetto a $t$, con la regola della catena ($y$ è funzione di $t$), si ottiene $y''(t) = f_t(t, y) + f_y(t, y)\,y'(t)$, e quindi $y''(t_0)$. Così si scrive il **polinomio di Taylor** della soluzione,
> $$y(t) = y_0 + y'(t_0)(t - t_0) + \frac{y''(t_0)}{2}(t - t_0)^2 + o\big((t - t_0)^2\big),$$
> e si calcolano limiti come $\lim_{t \to t_0} \frac{y(t) - y_0}{t - t_0} = y'(t_0)$.
>
> **3. Grafico locale.** Il segno di $y'(t_0)$ dice se la soluzione cresce o decresce vicino a $t_0$, quello di $y''(t_0)$ se è convessa o concava; insieme danno il disegno della soluzione vicino al punto iniziale, con la tangente $y = y_0 + y'(t_0)(t - t_0)$.
>
> **4. Soluzioni costanti.** Se $f(t, \tilde{y}) = 0$ per ogni $t$, la costante $y \equiv \tilde{y}$ è una soluzione (un equilibrio). Per l'unicità, nessun'altra soluzione può attraversarla: per $y' = (y - 1)t$ la retta $y = 1$ separa le soluzioni che restano sopra da quelle che restano sotto, e con $y(0) = 1$ la soluzione è proprio $y \equiv 1$.

## 4.12 Equazioni di Bernoulli

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 2*; prova scritta del 17/06/2025 (AM1B-08)
> Un'equazione della forma
> $$y' = a(t)\,y + b(t)\,y^\alpha, \qquad \alpha \ne 0, 1,$$
> si chiama **di Bernoulli**. Non è lineare per il termine $y^\alpha$, ma lo diventa con il cambio di variabile $z = y^{1 - \alpha}$. Infatti, dove $y \ne 0$, $z' = (1 - \alpha)y^{-\alpha}y'$, e moltiplicando l'equazione per $(1 - \alpha)y^{-\alpha}$:
> $$z' = (1 - \alpha)a(t)\,z + (1 - \alpha)b(t),$$
> che è lineare del primo ordine e si risolve con la formula del paragrafo 4.4. Se $\alpha > 0$ anche $y \equiv 0$ è una soluzione, che il cambio di variabile perde e va aggiunta a parte. Il caso più frequente è $\alpha = 2$, con $z = \frac{1}{y}$.

## Esempi ed esercizi svolti

**Esercizio 1.** $y'' - 3y' + 2y = e^t$. $P(\lambda) = \lambda^2 - 3\lambda + 2 = (\lambda - 1)(\lambda - 2)$, quindi $y_o = c_1 e^t + c_2 e^{2t}$. Il termine noto ha $\alpha = 1$, radice semplice: $y_p = A t e^t$. Con $y_p' = A(1 + t)e^t$ e $y_p'' = A(2 + t)e^t$, sostituendo si ottiene $A\big((2 + t) - 3(1 + t) + 2t\big)e^t = -A e^t = e^t$, quindi $A = -1$ e $y = c_1 e^t + c_2 e^{2t} - t e^t$.

**Esercizio 2.** $y' = \frac{t}{y}$, $y(0) = 2$. Separando: $y\, dy = t\, dt$, $\frac{y^2}{2} = \frac{t^2}{2} + C$; con la condizione iniziale $C = 2$, quindi $y^2 = t^2 + 4$ e, poiché $y(0) > 0$, $y(t) = \sqrt{t^2 + 4}$ per ogni $t \in \mathbb{R}$.

**Esercizio 3.** $y' = \frac{2}{t}\,y + t^3$ su $(0, +\infty)$. $A(t) = 2\ln t$, $e^{A} = t^2$, $K(t) = \int t^3 \cdot t^{-2}\, dt = \frac{t^2}{2}$. Quindi $y(t) = t^2\left(\frac{t^2}{2} + \alpha\right) = \frac{t^4}{2} + \alpha t^2$.

**Esercizio 4.** Stabilità dell'origine per $y' = \begin{pmatrix} -1 & 2 \\ 0 & -3 \end{pmatrix} y$. La matrice è triangolare, con autovalori $-1$ e $-3$, entrambi negativi: l'origine è asintoticamente stabile.

### Altri esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello dei fogli "Equazioni differenziali", "… lineari", "Sistemi …", "Esistenza e unicità" e delle prove scritte 2025-2026; soluzioni verificate con `strumenti/verifica_ampliamento.py` (AM1B-08 … AM1B-11)
> La seconda parte di ogni prova è un problema di Cauchy: esistenza e unicità, polinomio di Taylor o grafico locale senza risolvere, poi la soluzione esplicita con il suo intervallo di definizione.

**Esercizio 5. Separabile, con l'intervallo massimale.** Risolvere $y' = x e^{y}$, $y(0) = 0$, e scrivere senza risolverla il polinomio di Taylor di grado 2 della soluzione.

*Senza risolvere.* $f = x e^y$ e $f_y = x e^y$ sono continue: soluzione unica. $y'(0) = 0 \cdot e^0 = 0$. Derivando, $y'' = e^y + x e^y y'$, quindi $y''(0) = 1$. Il polinomio è $P_2(x) = \frac{x^2}{2}$: la soluzione ha un minimo in 0.

*Risolvendo.* $e^{-y}\,dy = x\,dx$, quindi $-e^{-y} = \frac{x^2}{2} + C$ e, con $y(0) = 0$, $C = -1$: $e^{-y} = 1 - \frac{x^2}{2}$ e
$$y(x) = -\ln\left(1 - \frac{x^2}{2}\right), \qquad -\sqrt{2} < x < \sqrt{2}.$$
L'intervallo è quello che contiene 0 su cui l'argomento del logaritmo è positivo: agli estremi la soluzione va a $+\infty$ (esplode in tempo finito). Lo sviluppo $-\ln(1 - u) = u + o(u)$ con $u = \frac{x^2}{2}$ ritrova il polinomio di Taylor.

**Esercizio 6. Bernoulli.** Risolvere $y' = \frac{y}{t} + y^2$, $y(1) = 1$.

È di Bernoulli con $\alpha = 2$: si pone $z = \frac{1}{y}$, $z' = -\frac{y'}{y^2} = -\frac{1}{ty} - 1 = -\frac{z}{t} - 1$. L'equazione lineare $z' + \frac{z}{t} = -1$ si moltiplica per $t$: $(tz)' = -t$, quindi $tz = -\frac{t^2}{2} + C$. Con $z(1) = 1$: $C = \frac{3}{2}$, e
$$z = \frac{3 - t^2}{2t}, \qquad y(t) = \frac{2t}{3 - t^2}, \qquad 0 < t < \sqrt{3}.$$
L'intervallo contiene $t_0 = 1$ e si ferma in 0 (dove il coefficiente $\frac{1}{t}$ non è definito) e in $\sqrt{3}$ (dove la soluzione esplode).

**Esercizio 7. Un parametro in un'equazione del secondo ordine.** Per quale $k$ la funzione $e^{2x}\cos(3x)$ risolve $y'' - 4y' + ky = 0$? Per $k = -5$, quali soluzioni tendono a 0 per $x \to +\infty$?

$e^{2x}\cos(3x)$ è soluzione se $2 \pm 3i$ sono radici del polinomio caratteristico, cioè se $\lambda^2 - 4\lambda + k = (\lambda - 2)^2 + 9 = \lambda^2 - 4\lambda + 13$: $k = 13$. Per $k = -5$, $\lambda^2 - 4\lambda - 5 = (\lambda - 5)(\lambda + 1)$, e $y = c_1 e^{5x} + c_2 e^{-x}$. Tende a 0 per $x \to +\infty$ se e solo se $c_1 = 0$: le soluzioni cercate sono $y = c\,e^{-x}$.

**Esercizio 8. Risonanza nel metodo di somiglianza.** Risolvere $y'' - 5y' + 6y = 3e^{3x}$, $y(0) = 0$, $y'(0) = 0$.

$\lambda^2 - 5\lambda + 6 = (\lambda - 2)(\lambda - 3)$: $y_o = c_1 e^{2x} + c_2 e^{3x}$. Il termine noto ha $\alpha = 3$, radice semplice: si cerca $y_p = Ax e^{3x}$ (con $Ae^{3x}$ si otterrebbe 0, perché è già una soluzione dell'omogenea). Sostituendo, i termini con $x e^{3x}$ si cancellano e resta $A(2 \cdot 3 - 5)e^{3x} = 3e^{3x}$, quindi $A = 3$. Dalle condizioni iniziali, $c_1 + c_2 = 0$ e $2c_1 + 3c_2 + 3 = 0$: $c_1 = 3$, $c_2 = -3$.
$$y(x) = 3e^{2x} - 3e^{3x} + 3x e^{3x}.$$

**Esercizio 9. Il dato iniziale cambia tutto.** Sia $y' = (y + 1)t^2$, $y(0) = y_0$. Discutere esistenza e unicità e risolvere.

$f = (y + 1)t^2$ e $f_y = t^2$ sono continue ovunque: per ogni $y_0$ la soluzione esiste ed è unica. $y \equiv -1$ è una soluzione costante, quindi per $y_0 = -1$ la soluzione è quella. Per $y_0 \ne -1$ si separano le variabili: $\ln|y + 1| = \frac{t^3}{3} + C$, e
$$y(t) = -1 + (y_0 + 1)e^{t^3/3}, \qquad t \in \mathbb{R}.$$
La formula comprende anche il caso $y_0 = -1$. Le soluzioni non attraversano mai la retta $y = -1$, come previsto dall'unicità.

**Esercizio 10. Grafico locale senza risolvere.** Disegnare vicino a $x_0 = 1$ la soluzione di $y' = \frac{x^2 - y}{1 + y^2}$, $y(1) = 0$.

$f$ e $f_y$ sono continue ($1 + y^2 \ne 0$): soluzione unica. $y'(1) = \frac{1 - 0}{1} = 1 > 0$: crescente, con tangente $y = x - 1$. Derivando con la regola del quoziente,
$$y'' = \frac{(2x - y')(1 + y^2) - (x^2 - y)\,2yy'}{(1 + y^2)^2},$$
e in $x = 1$, con $y = 0$ e $y' = 1$: $y''(1) = 1 > 0$. Vicino a 1 la soluzione è crescente e convessa, sopra la tangente: $y(x) = (x - 1) + \frac{(x - 1)^2}{2} + o\big((x - 1)^2\big)$.

**Esercizio 11. Classificare l'equilibrio.** Classificare l'origine per $y' = Ay$ con $A = \begin{pmatrix} 1 & -5 \\ 1 & -3 \end{pmatrix}$.

$\operatorname{tr} A = -2$, $\det A = -3 + 5 = 2 > 0$: l'origine è asintoticamente stabile. $(\operatorname{tr} A)^2 = 4 < 8 = 4\det A$, quindi gli autovalori sono complessi, $-1 \pm i$: è un fuoco stabile, e le traiettorie spiraleggiano verso l'origine.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (AM1B-08 … AM1B-11)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Il polinomio di Taylor della soluzione.** Sia $y' = y^2 e^x$, $y(0) = 1$. Scrivere il polinomio di Taylor di ordine 2 della soluzione e poi risolvere.

*Passo 1: esistenza e unicità.* $f = y^2 e^x$ e $f_y = 2ye^x$ sono continue: soluzione unica vicino a 0.

*Passo 2: $y'(0)$.* Dall'equazione, $y'(0) = 1^2 \cdot e^0 = 1$.

*Passo 3: $y''(0)$.* Derivando $y' = y^2 e^x$: $y'' = 2yy'e^x + y^2 e^x$. In 0: $y''(0) = 2 \cdot 1 \cdot 1 + 1 = 3$.

*Passo 4: il polinomio.* $P_2(x) = 1 + x + \frac{3}{2}x^2$.

*Passo 5: la soluzione.* Separando, $\frac{dy}{y^2} = e^x\,dx$: $-\frac{1}{y} = e^x + C$, con $C = -2$. Quindi $y = \frac{1}{2 - e^x}$, definita per $x < \ln 2$ (l'intervallo che contiene 0). Controllo: $\frac{1}{2 - e^x} = \frac{1}{1 - x - \frac{x^2}{2} + o(x^2)} = 1 + x + \frac{x^2}{2} + x^2 + o(x^2) = 1 + x + \frac{3}{2}x^2 + o(x^2)$.

**Guidato 2. Un'equazione lineare del primo ordine con intervallo.** Risolvere $y' + \frac{2}{t}y = \frac{\cos t}{t^2}$, $y(\pi) = 0$.

*Passo 1: il coefficiente.* $\frac{2}{t}$ non è definito in 0, e $t_0 = \pi > 0$: si lavora su $(0, +\infty)$.

*Passo 2: il fattore integrante.* $e^{\int 2/t} = t^2$. Moltiplicando, $(t^2 y)' = \cos t$.

*Passo 3: integrare.* $t^2 y = \sin t + C$, e con $y(\pi) = 0$: $C = 0$.

*Passo 4: la soluzione.* $y(t) = \frac{\sin t}{t^2}$ su $(0, +\infty)$. Per $t \to 0^+$ la soluzione si comporta come $\frac{1}{t}$ ed esplode, coerentemente con il coefficiente singolare.

**Guidato 3. Un sistema non lineare linearizzato.** Trovare gli equilibri del sistema $x' = x - xy$, $y' = -y + xy$ e studiarne la stabilità con la linearizzazione.

*Passo 1: gli equilibri.* $x(1 - y) = 0$ e $y(x - 1) = 0$: $(0, 0)$ e $(1, 1)$.

*Passo 2: la jacobiana.* $J(x, y) = \begin{pmatrix} 1 - y & -x \\ y & x - 1 \end{pmatrix}$.

*Passo 3: nell'origine.* $J(0, 0) = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$: autovalori $\pm 1$, sella, equilibrio instabile.

*Passo 4: in $(1, 1)$.* $J(1, 1) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$: autovalori $\pm i$, parte reale nulla. Il teorema di linearizzazione non conclude. (Per questo sistema, il modello preda-predatore di Lotka-Volterra, si dimostra con una quantità conservata che le traiettorie intorno a $(1, 1)$ sono chiuse: l'equilibrio è stabile, non asintoticamente.)

## Riepilogo

Le equazioni differenziali nascono dalla modellizzazione: la legge di Newton per la caduta con attrito e per la molla, la crescita esponenziale e logistica per le popolazioni. Un'equazione di ordine $n$ ha come soluzioni funzioni derivabili $n$ volte su un intervallo; il problema di Cauchy aggiunge $n$ condizioni iniziali. Le equazioni separabili si risolvono separando le variabili, dopo aver trovato le soluzioni costanti; l'unicità può mancare quando $h$ non è lipschitziana, come nel pennello di Peano. Le lineari del primo ordine hanno la formula $y = e^{A}(\int b\, e^{-A} + \alpha)$. Le lineari del secondo ordine a coefficienti costanti si risolvono con il polinomio caratteristico, nei tre casi del discriminante, e il metodo di somiglianza dà una soluzione particolare per termini noti polinomiali, esponenziali e trigonometrici, tenendo conto della molteplicità della radice. Per i sistemi la continuità di $f$ dà l'esistenza, la continuità delle derivate in $y$ l'unicità, la sublinearità l'esistenza globale. I sistemi lineari hanno soluzioni globali che formano uno spazio di dimensione $n$, descritte da una matrice fondamentale; a coefficienti costanti si costruiscono con autovalori e autovettori, generalizzati quando un autovalore non è regolare. Il segno della parte reale degli autovalori decide la stabilità dell'origine.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (AM1B-08 … AM1B-12)
> Metodi risolutivi, teoremi e criteri di stabilità, con i termini per l'orale.

### Equazioni del primo ordine

| Tipo | Forma | Metodo |
|---|---|---|
| Separabile | $y' = a(t)\,b(y)$ | soluzioni costanti dove $b = 0$; poi $\int \frac{dy}{b(y)} = \int a(t)\,dt$ |
| Lineare | $y' = a(t)y + f(t)$ | $y = e^{A(t)}\left(\int f(t)e^{-A(t)}dt + C\right)$, $A' = a$ |
| Bernoulli | $y' = a(t)y + b(t)y^\alpha$ | $z = y^{1-\alpha}$ dà un'equazione lineare; $y \equiv 0$ a parte se $\alpha > 0$ |

### Secondo ordine a coefficienti costanti: $y'' + ay' + by = f(t)$

| Radici di $\lambda^2 + a\lambda + b$ | Integrale dell'omogenea |
|---|---|
| reali distinte $\lambda_1, \lambda_2$ | $c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$ |
| reale doppia $\lambda$ | $(c_1 + c_2 t)e^{\lambda t}$ |
| complesse $\alpha \pm i\beta$ | $e^{\alpha t}(c_1\cos\beta t + c_2\sin\beta t)$ |

Somiglianza: per $f = P_n(t)e^{\alpha t}$ si cerca $y_p = t^\mu Q_n(t)e^{\alpha t}$, con $\mu$ la molteplicità di $\alpha$ come radice (0 se non lo è); per $f = e^{\alpha t}(P\cos\beta t + Q\sin\beta t)$ si guarda $\alpha + i\beta$.

### Teoremi

- **Cauchy (esistenza e unicità locale):** $f$ e $f_y$ continue vicino a $(t_0, y_0)$ $\Rightarrow$ una e una sola soluzione in un intorno di $t_0$.
- **Esistenza globale (lineari):** coefficienti continui su un intervallo $I$ $\Rightarrow$ la soluzione esiste su tutto $I$.
- **Struttura:** l'integrale generale di un'equazione o di un sistema lineare è $y_o + y_p$; le soluzioni dell'omogenea di ordine $n$ formano uno spazio vettoriale di dimensione $n$.
- **Sistemi $y' = Ay$:** con autovettori $v_i$ di autovalori $\lambda_i$, $y = \sum c_i e^{\lambda_i t}v_i$ (se $A$ è diagonalizzabile); matrice fondamentale $\Phi(t)$ con $\Phi' = A\Phi$.

### Stabilità

| Caso | Criterio |
|---|---|
| $y' = Ay$ | asintoticamente stabile $\iff$ tutti gli autovalori con parte reale $< 0$ |
| $2 \times 2$ | $\det A < 0$ sella; $\det A > 0$: $\operatorname{tr} A < 0$ stabile, $> 0$ instabile, $= 0$ centro |
| $y' = F(y)$ non lineare | autovalori della jacobiana nell'equilibrio: tutti $\operatorname{Re} < 0$ stabile, uno $\operatorname{Re} > 0$ instabile |
| $y' = f(y)$ scalare | $f'(\tilde{y}) < 0$ stabile, $f'(\tilde{y}) > 0$ instabile |

### Senza risolvere

$$y'(t_0) = f(t_0, y_0), \qquad y''(t_0) = f_t(t_0, y_0) + f_y(t_0, y_0)\,f(t_0, y_0).$$

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Ordine di un'equazione | ordine massimo di derivata che compare |
| Problema di Cauchy | equazione più condizioni iniziali nel punto $t_0$ |
| Integrale generale | famiglia di tutte le soluzioni, con costanti arbitrarie |
| Soluzione massimale | soluzione definita sull'intervallo più grande possibile |
| Equazione autonoma | $f$ non dipende da $t$ |
| Equilibrio | soluzione costante, zero di $f$ |
| Stabile / asintoticamente stabile | le soluzioni vicine restano vicine / tendono all'equilibrio |
| Ritratto di fase | disegno delle traiettorie nel piano $(y_1, y_2)$ |
| Nodo, sella, fuoco, centro | le forme del ritratto di fase di un sistema lineare $2 \times 2$ |

### Domande che tornano spesso

- Enunciare il teorema di esistenza e unicità; un esempio in cui l'unicità manca ($y' = \sqrt{|y|}$).
- Ricavare la formula risolutiva delle equazioni lineari del primo ordine.
- Perché le soluzioni di un'equazione lineare omogenea di ordine $n$ formano uno spazio di dimensione $n$?
- Come si passa da un'equazione di ordine $n$ a un sistema del primo ordine?
- Spiegare il metodo di somiglianza e il caso di risonanza.
- Definire la stabilità e classificare gli equilibri dei sistemi lineari $2 \times 2$.
