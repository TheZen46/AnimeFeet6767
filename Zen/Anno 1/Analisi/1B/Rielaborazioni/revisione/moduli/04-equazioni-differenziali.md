---
corso: Analisi Matematica 1B
modulo: 4
titolo: Equazioni differenziali ordinarie e sistemi
programma: [AM1B-08, AM1B-09, AM1B-10, AM1B-11, AM1B-12]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-04
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
> - $y'' + y = t^2$. $P(\lambda) = \lambda^2 + 1$ ha radici $\pm i$; $\alpha = 0$ non è radice, quindi $y_p = At^2 + Bt + C$. Sostituendo, $2A + At^2 + Bt + C = t^2$: $A = 1$, $B = 0$, $C = -2$. L'integrale generale è $y = c_1\cos t + c_2\sin t + t^2 - 2$.
> - $y'' + y = t^2\cos t$. Qui $\alpha + i\beta = i$ è radice semplice, quindi $\mu = 1$ e $y_p = t\big((At^2 + Bt + C)\cos t + (Dt^2 + Et + F)\sin t\big)$, con sei coefficienti da trovare sostituendo.

## 4.6 Sistemi: esistenza e unicità

Un **sistema del primo ordine** in forma normale è $y' = f(t, y)$, con $y(t) \in \mathbb{R}^n$ e $f : I \times D \to \mathbb{R}^n$, $I$ intervallo aperto e $D \subseteq \mathbb{R}^n$ aperto. Il problema di Cauchy aggiunge $y(t_0) = y_0$.

> [!teorema] Esistenza e unicità locale
> Se $f$ è continua su $I \times D$, per ogni $t_0 \in I$ e $y_0 \in D$ il problema di Cauchy ha una soluzione su un intervallo $J \ni t_0$. Se inoltre le derivate parziali $\frac{\partial f_i}{\partial y_j}$ sono continue (o, più in generale, $f$ è localmente lipschitziana in $y$), la soluzione è unica.

> [!teorema] Esistenza globale
> Se, oltre alle ipotesi di unicità, $f$ è **sublineare** in $y$, cioè $\lVert f(t, y)\rVert \le \alpha(t) + \beta(t)\lVert y\rVert$ con $\alpha$, $\beta$ continue e non negative (e $D = \mathbb{R}^n$), la soluzione è definita su tutto $I$.

> [!esempio] Globale e non globale
> - $y' = t^2\sin y + e^t y$: $f$ è di classe $C^1$ e $\lvert f\rvert \le t^2 + e^t\lvert y\rvert$. Ogni problema di Cauchy ha un'unica soluzione definita su tutto $\mathbb{R}$.
> - $y' = y^2$, $y(0) = 1$: $f$ è $C^1$, quindi la soluzione è unica, ma $y^2$ cresce più che linearmente. Separando si trova $y(t) = \frac{1}{1 - t}$, che "esplode" per $t \to 1^-$: la soluzione è definita solo su $(-\infty, 1)$.

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 2* (AM1B-09)
> **Un'equazione di ordine $n$ è un sistema.** Ponendo $y_1 = y$, $y_2 = y'$, …, $y_n = y^{(n-1)}$, l'equazione $y^{(n)} = f(t, y, \dots, y^{(n-1)})$ diventa il sistema del primo ordine $y_1' = y_2$, …, $y_{n-1}' = y_n$, $y_n' = f(t, y_1, \dots, y_n)$. Per questo i teoremi sui sistemi valgono anche per le equazioni di ordine $n$, e il problema di Cauchy richiede $n$ condizioni iniziali.

## 4.7 Sistemi lineari

Un **sistema lineare** è $y' = A(t)\, y + b(t)$, con $A(t)$ matrice $n \times n$ e $b(t) \in \mathbb{R}^n$ continue su $I$. Poiché $\lVert A(t)y\rVert \le \lVert A(t)\rVert\, \lVert y\rVert$, la condizione di sublinearità vale sempre.

> [!teorema] Sistemi lineari
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
> 1. è asintoticamente stabile se e solo se ogni autovalore ha parte reale negativa;
> 2. è stabile se ogni autovalore ha parte reale $\le 0$ e quelli con parte reale nulla sono regolari;
> 3. è instabile negli altri casi: c'è un autovalore con parte reale positiva, oppure uno con parte reale nulla e non regolare.

Il motivo sta nella forma delle soluzioni: per un autovalore $\alpha + i\beta$ compaiono termini $t^k e^{\alpha t}\cos(\beta t)$ e $t^k e^{\alpha t}\sin(\beta t)$, con potenze $t^k$ solo se l'autovalore non è regolare. Se $\alpha < 0$ l'esponenziale porta tutto a zero anche in presenza delle potenze; se $\alpha = 0$ i termini restano limitati solo se non ci sono potenze; se $\alpha > 0$ crescono.

> [!esempio] Oscillatore smorzato
> $y'' + k y' + y = 0$, con $k \in \mathbb{R}$. Con $y_1 = y$, $y_2 = y'$ diventa il sistema con matrice $\begin{pmatrix} 0 & 1 \\ -1 & -k \end{pmatrix}$, il cui polinomio caratteristico è $\lambda^2 + k\lambda + 1$, con radici $\frac{-k \pm \sqrt{k^2 - 4}}{2}$.
> - $k > 0$ (attrito): per $k \ge 2$ radici reali negative, per $0 < k < 2$ complesse con parte reale $-\frac{k}{2} < 0$. In entrambi i casi l'origine è asintoticamente stabile: le oscillazioni si smorzano.
> - $k = 0$: radici $\pm i$, semplici. L'origine è stabile ma non asintoticamente: le traiettorie nel piano $(y, y')$ sono circonferenze, il moto armonico non si smorza.
> - $k < 0$: almeno una radice ha parte reale positiva e l'origine è instabile: il sistema riceve energia.

## Esempi ed esercizi svolti

**Esercizio 1.** $y'' - 3y' + 2y = e^t$. $P(\lambda) = \lambda^2 - 3\lambda + 2 = (\lambda - 1)(\lambda - 2)$, quindi $y_o = c_1 e^t + c_2 e^{2t}$. Il termine noto ha $\alpha = 1$, radice semplice: $y_p = A t e^t$. Con $y_p' = A(1 + t)e^t$ e $y_p'' = A(2 + t)e^t$, sostituendo si ottiene $A\big((2 + t) - 3(1 + t) + 2t\big)e^t = -A e^t = e^t$, quindi $A = -1$ e $y = c_1 e^t + c_2 e^{2t} - t e^t$.

**Esercizio 2.** $y' = \frac{t}{y}$, $y(0) = 2$. Separando: $y\, dy = t\, dt$, $\frac{y^2}{2} = \frac{t^2}{2} + C$; con la condizione iniziale $C = 2$, quindi $y^2 = t^2 + 4$ e, poiché $y(0) > 0$, $y(t) = \sqrt{t^2 + 4}$ per ogni $t \in \mathbb{R}$.

**Esercizio 3.** $y' = \frac{2}{t}\,y + t^3$ su $(0, +\infty)$. $A(t) = 2\ln t$, $e^{A} = t^2$, $K(t) = \int t^3 \cdot t^{-2}\, dt = \frac{t^2}{2}$. Quindi $y(t) = t^2\left(\frac{t^2}{2} + \alpha\right) = \frac{t^4}{2} + \alpha t^2$.

**Esercizio 4.** Stabilità dell'origine per $y' = \begin{pmatrix} -1 & 2 \\ 0 & -3 \end{pmatrix} y$. La matrice è triangolare, con autovalori $-1$ e $-3$, entrambi negativi: l'origine è asintoticamente stabile.

## Riepilogo

Le equazioni differenziali nascono dalla modellizzazione: la legge di Newton per la caduta con attrito e per la molla, la crescita esponenziale e logistica per le popolazioni. Un'equazione di ordine $n$ ha come soluzioni funzioni derivabili $n$ volte su un intervallo; il problema di Cauchy aggiunge $n$ condizioni iniziali. Le equazioni separabili si risolvono separando le variabili, dopo aver trovato le soluzioni costanti; l'unicità può mancare quando $h$ non è lipschitziana, come nel pennello di Peano. Le lineari del primo ordine hanno la formula $y = e^{A}(\int b\, e^{-A} + \alpha)$. Le lineari del secondo ordine a coefficienti costanti si risolvono con il polinomio caratteristico, nei tre casi del discriminante, e il metodo di somiglianza dà una soluzione particolare per termini noti polinomiali, esponenziali e trigonometrici, tenendo conto della molteplicità della radice. Per i sistemi la continuità di $f$ dà l'esistenza, la continuità delle derivate in $y$ l'unicità, la sublinearità l'esistenza globale. I sistemi lineari hanno soluzioni globali che formano uno spazio di dimensione $n$, descritte da una matrice fondamentale; a coefficienti costanti si costruiscono con autovalori e autovettori, generalizzati quando un autovalore non è regolare. Il segno della parte reale degli autovalori decide la stabilità dell'origine.
