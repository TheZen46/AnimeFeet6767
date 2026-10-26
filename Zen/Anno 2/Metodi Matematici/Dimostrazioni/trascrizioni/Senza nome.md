## Rettificabilità e lunghezza di una curva

Data una curva $\gamma$ parametrizzata da $\varphi : [a,b] \to \mathbb{R}^n$

$$L(\gamma) = \sup_{P} L(P) \qquad \text{con } P \text{ la poligonale su } [a,b]$$

Se $L(\gamma)$ esiste finita $\Rightarrow$ $\gamma$ è **rettificabile**.

Se $\gamma$ è rettificabile $\Rightarrow$

$$L(\gamma) = \int_a^b |\varphi'(t)|,dt$$

> [!warning] Ipotesi  
> La formula integrale richiede $\varphi \in C^1([a,b])$. L'enunciato corretto è: se $\varphi \in C^1$, allora $\gamma$ è rettificabile e $L(\gamma) = \int_a^b |\varphi'(t)|,dt$. La sola rettificabilità non basta: la dimostrazione usa infatti la continuità di $\varphi'$.

### Dimostrazione

Considero $\pi = {t_i}$, $i \in {0,\dots,N}$, una partizione di $[a,b]$.

$$L(P) = \sum_{i=1}^{N} |\varphi(t_i) - \varphi(t_{i-1})| = \sum \left| \int_{t_{i-1}}^{t_i} \varphi'(t),dt \right| \le \sum \int_{t_{i-1}}^{t_i} |\varphi'(t)|,dt = \int_a^b |\varphi'(t)|,dt$$

$$L(P) \le \int_a^b |\varphi'(t)|,dt \qquad \text{stima dall'alto di } L(\gamma)$$

Sia $\varphi'(t)$ continua su $[a,b]$ $\Rightarrow$ $\varphi'(t)$ è **uniformemente continua** per Heine-Cantor:

$$\forall \varepsilon > 0 ;; \exists \delta > 0 ;; \forall s,t \in [a,b] \quad |s-t| < \delta_\varepsilon \Rightarrow |\varphi'(s) - \varphi'(t)| < \varepsilon$$

Fisso un $\varepsilon > 0$ a cui è associato un $\delta_\varepsilon$. Sia $\pi = {t_i} \to a = t_0, t_1, \dots, t_N = b$.

Per avere $[t_i - t_{i-1}] < \delta_\varepsilon ;; \forall i \in {1,\dots,N}$, con $s \in [t_{i-1}, t_i]$ scrivo:

$$\varphi(t_i) - \varphi(t_{i-1}) = \int_{t_{i-1}}^{t_i} \varphi'(t),dt = \int_{t_{i-1}}^{t_i} \varphi'(t) - \varphi'(s) + \varphi'(s),dt$$

$$\varphi(t_i) - \varphi(t_{i-1}) = \int_{t_{i-1}}^{t_i} \varphi'(t) - \varphi'(s),dt + \underline{\varphi'(s)\cdot(t_i - t_{i-1})} \qquad \text{sposto il focus qui}$$

$$\varphi'(s)\cdot(t_i - t_{i-1}) = \varphi(t_i) - \varphi(t_{i-1}) - \int_{t_{i-1}}^{t_i} \varphi'(t) - \varphi'(s),dt$$

$$|\varphi'(s)\cdot(t_i - t_{i-1})| \le |\varphi(t_i) - \varphi(t_{i-1})| + \int_{t_{i-1}}^{t_i} |\varphi'(t) - \varphi'(s)|,dt \qquad |\varphi'(t) - \varphi'(s)| < \varepsilon$$

$$|\varphi'(s)| \le \frac{|\varphi(t_i) - \varphi(t_{i-1})|}{t_i - t_{i-1}} + \frac{1}{t_i - t_{i-1}}\cdot \varepsilon \cdot \underbrace{\int_{t_{i-1}}^{t_i} 1,dt}_{=, t_i - t_{i-1}}$$

$$|\varphi'(s)| \le \frac{|\varphi(t_i) - \varphi(t_{i-1})|}{t_i - t_{i-1}} + \varepsilon$$

$$\int_{t_{i-1}}^{t_i} |\varphi'(s)|,ds \le |\varphi(t_i) - \varphi(t_{i-1})| + \varepsilon\cdot(t_i - t_{i-1})$$

$$\int_a^b |\varphi'(s)|,ds \le L(P) + \varepsilon\cdot(b-a) \le \sup_P L(P) + \varepsilon(b-a) \le L(\gamma) \qquad \text{stima dal basso}$$

> [!warning] Ultimo passaggio  
> $\sup_P L(P) + \varepsilon(b-a) = L(\gamma) + \varepsilon(b-a)$, non $\le L(\gamma)$. Si ottiene $\int_a^b |\varphi'| \le L(\gamma) + \varepsilon(b-a)$ e, per l'arbitrarietà di $\varepsilon$, $\int_a^b |\varphi'| \le L(\gamma)$.

Unisco le due stime:

$$\int_a^b |\varphi'(s)|,ds \le L(\gamma) \le \int_a^b |\varphi'(s)|,ds \quad \text{da cui segue} \quad L(\gamma) = \int_a^b |\varphi'(s)|,ds \qquad \square$$

---

## Condizioni di integrabilità

Siano $f : Q \subset \mathbb{R}^2 \to \mathbb{R}$ e $Q = [a,b]\times[c,d]$ un compatto.

Allora se $f$ è continua è anche integrabile.

### Dimostrazione

$f$ continua su $Q$ compatto $\Rightarrow$ $f$ è uniformemente continua:

$$\forall \varepsilon > 0 ;; \exists \delta_\varepsilon > 0 ;; \text{t.c.} ;; |x - y| < \delta_\varepsilon \Rightarrow |f(x) - f(y)| < \varepsilon$$

Cerco una partizione di $Q$ adattata a $\delta_\varepsilon$:

$$a = x_0 < x_1 < \dots < x_r = b \qquad x_j - x_{j-1} = \Delta x_j < \frac{\delta_\varepsilon}{2} \quad \forall j \in {1,\dots,r}$$

$$c = y_0 < y_1 < \dots < y_s = d \qquad y_k - y_{k-1} = \Delta y_k < \frac{\delta_\varepsilon}{2} \quad \forall k \in {1,\dots,s}$$

Allora $Q_{jk} = [x_{j-1}, x_j]\times[y_{k-1}, y_k]$

e $z_1, z_2 \in Q_{jk}$ t.c. $|z_1 - z_2| < \left(\frac{\delta_\varepsilon}{2}\right)^2 + \left(\frac{\delta_\varepsilon}{2}\right)^2$

Stimo $|z_1 - z_2| < 2\cdot\frac{1}{4}\cdot\delta_\varepsilon^2 < \delta_\varepsilon^2$


> [!warning] Stima della distanza  
> La disuguaglianza riguarda il quadrato della distanza: $|z_1 - z_2|^2 < \left(\frac{\delta_\varepsilon}{2}\right)^2 + \left(\frac{\delta_\varepsilon}{2}\right)^2 = \frac{\delta_\varepsilon^2}{2}$, quindi $|z_1 - z_2| < \frac{\delta_\varepsilon}{\sqrt 2} < \delta_\varepsilon$, che è ciò che serve per applicare l'uniforme continuità.

Uso uniforme continuità $\Rightarrow |f(z_1) - f(z_2)| < \varepsilon$ cioè $M_{jk} - m_{jk} < \varepsilon$

$$M_{jk} = \sup f(z_1), \qquad m_{jk} = \inf f(z_2)$$

$$S_{sup}(D,f) - S_{inf}(D,f) = \sum_{j=1}^{r}\sum_{k=1}^{s} M_{jk},\Delta x_j,\Delta y_k - m_{jk},\Delta x_j,\Delta y_k =$$

$$= \sum_{jk} (M_{jk} - m_{jk})\cdot A(Q_{jk}) <$$

$$< \sum_{jk} \varepsilon\cdot A(Q_{jk}) = \varepsilon\cdot\sum_{jk} A(Q_{jk}) = \varepsilon\cdot A(Q)$$

Il risultato vale $\forall \varepsilon$ $\Rightarrow$ $f$ è integrabile su $Q$ $\square$

Ho dimostrato che: per $\varepsilon > 0 ;; \exists D \in \mathcal{P}$ t.c. $S_{sup}(D,f) - S_{inf}(D,f) < \varepsilon\cdot\text{costante}$

> [!note] Criterio di integrabilità  
> $D$ indica una partizione di $Q$ e $\mathcal{P}$ l'insieme delle partizioni. Una funzione limitata è integrabile secondo Riemann se e solo se, per ogni $\varepsilon > 0$, esiste una partizione per cui somma superiore e somma inferiore differiscono meno di $\varepsilon$. La costante $A(Q)$ non altera il criterio, perché basta scegliere $\varepsilon / A(Q)$ al posto di $\varepsilon$.

---

## Formula di Gauss-Green

Per $D \subset \mathbb{R}^2$ con $\partial D$ regolare a tratti e $\bar D = D \cup \partial D$ limitato.

Considero $F : \bar D \subset \mathbb{R}^2 \to \mathbb{R}^2$ un campo vettoriale $F = (F_1, F_2)$.

Per $F \in C^1_{(\bar D)}$ a tratti:

$$\int_{\partial D} F,dP = \iint_D \partial_x F_2 - \partial_y F_1,dx,dy$$

> [!note] Notazione  
> $\int_{\partial D} F,dP$ indica l'integrale di linea (lavoro) del campo lungo il bordo percorso in verso antiorario, cioè $\int_{\partial D} F_1,dx + F_2,dy$.

### Dimostrazione

Sia $D$ un dominio normale rispetto alle $x$:

$$D = {(x,y) \in \mathbb{R}^2 \mid x \in [a,b],; \alpha(x) \le y \le \beta(x)}$$

con $\alpha, \beta : [a,b] \to \mathbb{R}$, $\alpha, \beta \in C^1([a,b])$.

> [!info] Figura  
> Dominio normale rispetto all'asse $x$: compreso tra $x = a$ e $x = b$, delimitato in basso dal grafico di $\alpha(x)$ e in alto da quello di $\beta(x)$. Il bordo è diviso in quattro tratti percorsi in verso antiorario: $\gamma_1$ (grafico di $\alpha$, verso destra), $\gamma_2$ (segmento verticale in $x = b$, verso l'alto), $\gamma_3$ (grafico di $\beta$, verso sinistra), $\gamma_4$ (segmento verticale in $x = a$, verso il basso).
> 
> ```tikz
> \begin{document}  
> \begin{tikzpicture}[scale=1.3]  
> \draw[->] (-0.3,0) -- (4,0) node[right] {$x$};  
> \draw[->] (0,-0.3) -- (0,3.6) node[above] {$y$};  
> \draw[dashed] (1,0) -- (1,1.2);  
> \draw[dashed] (3,0) -- (3,0.8);  
> \draw (1,0.06) -- (1,-0.06) node[below] {$a$};  
> \draw (3,0.06) -- (3,-0.06) node[below] {$b$};  
> \draw[thick,blue] (1,1.2) .. controls (1.8,0.4) and (2.4,1.4) .. (3,0.8);  
> \draw[thick,blue] (1,2.2) .. controls (1.8,2.4) and (2.4,3.4) .. (3,2.8);  
> \draw[thick,blue] (1,1.2) -- (1,2.2);  
> \draw[thick,blue] (3,0.8) -- (3,2.8);  
> \node[blue] at (1.6,0.55) {$\alpha(x)$};  
> \node[blue] at (1.6,2.75) {$\beta(x)$};  
> \draw[->,green!50!black] (1.9,0.6) -- (2.3,0.75);  
> \node[green!50!black] at (2.4,1.25) {$\gamma_1$};  
> \draw[->,green!50!black] (3.2,1.5) -- (3.2,2.1);  
> \node[green!50!black] at (3.45,1.8) {$\gamma_2$};  
> \draw[->,green!50!black] (2.3,3.15) -- (1.9,2.75);  
> \node[green!50!black] at (2.6,3.35) {$\gamma_3$};  
> \draw[->,green!50!black] (0.8,2.0) -- (0.8,1.4);  
> \node[green!50!black] at (0.5,1.7) {$\gamma_4$};  
> \end{tikzpicture}  
> \end{document}  
> ```

Considero il verso **anti-orario**.

Bordo di $D = \partial D = \gamma_1 \cup \gamma_2 \cup \gamma_3 \cup \gamma_4$

$$\begin{aligned}  
\gamma_1(x) &= (x, \alpha(x)) & x &\in [a,b] & &\to & \gamma_1'(x) &= (1, \alpha'(x)) \  
\gamma_2(x) &= (b, y) & y &\in [\alpha(b), \beta(b)] & &\to & \gamma_2'(x) &= (0, 1) \  
\gamma_3^-(x) &= (x, \beta(x)) & x &\in [a,b] & &\to & {\gamma_3^-}'(x) &= (1, \beta'(x)) \  
\gamma_4^-(x) &= (a, y) & y &\in [\alpha(a), \beta(a)] & &\to & {\gamma_4^-}'(x) &= (0, 1)  
\end{aligned}$$

> [!note] Curve opposte  
> $\gamma_3^-$ e $\gamma_4^-$ sono le parametrizzazioni "naturali" (con $x$ e $y$ crescenti) di $\gamma_3$ e $\gamma_4$, che percorrono questi tratti nel verso opposto a quello antiorario. Per questo i rispettivi integrali vanno presi con segno meno.

$$\begin{aligned}  
\int_{\partial D} F,dP = &\int_a^b [F_1(x,\alpha(x)),, F_2(x,\alpha(x))]\cdot[1, \alpha'(x)],dx ;+ && \gamma_1 \

- &\int_{\alpha(b)}^{\beta(b)} [F_1(b,y),, F_2(b,y)]\cdot[0,1],dy ;+ && \gamma_2 \
- &\int_a^b [F_1(x,\beta(x)),, F_2(x,\beta(x))]\cdot[1, \beta'(x)],dx ;+ && \gamma_3^- \
- &\int_{\alpha(a)}^{\beta(a)} [F_1(a,y),, F_2(a,y)]\cdot[0,1],dy && \gamma_4^-  
    \end{aligned}$$

> [!warning] Segni  
> I termini relativi a $\gamma_3^-$ e $\gamma_4^-$ devono comparire con il segno meno. Nella riga successiva i segni sono già corretti.

$$\int_{\partial D} F,dP = \underbrace{\int_a^b F_1(x,\alpha(x)) - F_1(x,\beta(x)),dx}_{A} ;+$$

$$+ \underbrace{\underbrace{\int_a^b F_2(x,\alpha(x)),\alpha'(x),dx}_{1} + \underbrace{\int_{\alpha(b)}^{\beta(b)} F_2(b,y),dy}_{2} - \underbrace{\int_a^b F_2(x,\beta(x)),\beta'(x),dx}_{3} - \underbrace{\int_{\alpha(a)}^{\beta(a)} F_2(a,y),dy}_{4}}_{B}$$

Mi chiedo se $\displaystyle\int_{\partial D} F,dP = A + B$ ?

$$F_1(x,\alpha(x)) - F_1(x,\beta(x)) = -\int_{\alpha(x)}^{\beta(x)} \partial_y F_1(x,y),dy$$

$$A = \int_a^b \int_{\alpha(x)}^{\beta(x)} -\partial_y F(x,y),dy,dx = \iint_D -\partial_y F_1(x,y),dx,dy$$

Introduco

$$\mathcal{E}(x) = \int_{\alpha(x)}^{\beta(x)} F_2(x,y),dy$$

$$2 = \mathcal{E}(b) \qquad 4 = -\mathcal{E}(a) \qquad 2 + 4 = \mathcal{E}(b) - \mathcal{E}(a) = \int_a^b \partial_x \mathcal{E}(x),dx$$

$$\partial_x \mathcal{E}(x) = \int_{\alpha(x)}^{\beta(x)} \partial_x F_2(x,y),dy + F_2(x,\beta(x)),\beta'(x) - F_2(x,\alpha(x)),\alpha'(x)$$

> [!note] Derivazione sotto il segno di integrale  
> È la regola di Leibniz per un integrale con estremi variabili: si deriva l'integrando e si aggiungono i contributi degli estremi, $F_2$ valutata nell'estremo moltiplicata per la derivata dell'estremo stesso.

$$\Rightarrow \int_a^b \partial_x \mathcal{E}(x),dx = \int_a^b\int_{\alpha(x)}^{\beta(x)} \partial_x F_2(x,y),dx,dy + \underbrace{\int_a^b F_2(x,\beta(x)),\beta'(x),dx}_{-3} - \underbrace{\int_a^b F_2(x,\alpha(x)),\alpha'(x),dx}_{-1}$$

$$1 + 2 + 3 + 4 = \iint_D \partial_x F_2(x,y),dx,dy = B$$

$$\int_{\partial D} F,dP = \iint_D \partial_x F_2 - \partial_y F_1,dx,dy = A + B \qquad \square$$

---

## Divergenza in 2D

Sia $D$ un dominio regolare e $\partial D$ una curva regolare a tratti con $\bar D = D \cup \partial D$.

Sia $F : \bar D \subset \mathbb{R}^2 \to \mathbb{R}^2$ di classe $C^1_{(\bar D)}$ un campo vettoriale.

Allora

$$\iint_{\bar D} \nabla F,dx,dy = \int_{\partial D} F\cdot\underline{n},ds \qquad \underline{n} \text{ il vettore normale al bordo}$$

> [!note] Notazione  
> $\nabla F$ indica la **divergenza** $\nabla\cdot F = \partial_x F_1 + \partial_y F_2$. Il teorema afferma che l'integrale della divergenza sul dominio è uguale al flusso uscente del campo attraverso il bordo; $\underline n$ è la normale uscente unitaria.

### Dimostrazione

$$\iint_{\bar D} \nabla F,dx,dy = \iint_{\bar D} \partial_x F_1 + \partial_y F_2,dx,dy$$

Introduco $G : \bar D \subset \mathbb{R}^2 \to \mathbb{R}^2$ con $G = (G_1, G_2) = (-F_2, F_1)$

$$\iint_{\bar D} \partial_x F_1 + \partial_y F_2,dx,dy = \iint_{\bar D} \partial_x G_2 - \partial_y G_1,dx,dy = \int_{\partial D} G,dP \qquad \text{Gauss-Green}$$

$$s : [a,b] \to \partial D \qquad \varphi : s \to (x(s), y(s))$$

$\varphi'(s) = (x'(s), y'(s)) = \hat t$ il versore tangente al bordo

$\underline n = R_0^{\pi/2}(\hat t)$ lo stesso vettore ma ruotato, $\underline n = (y'(s), -x'(s))$

> [!warning] Verso della rotazione  
> $(y', -x')$ si ottiene ruotando $\hat t$ di $\pi/2$ in senso **orario** (cioè di $-\pi/2$). Con il bordo percorso in verso antiorario è questa la normale uscente. Inoltre, perché $\hat t$ sia un versore, $s$ deve essere l'ascissa curvilinea ($|\varphi'(s)| = 1$).

> [!info] Figura  
> Tratto del bordo $\partial D$ con, in un punto, il versore tangente $\hat t$ e il versore normale $\underline n$, ortogonale a $\hat t$ e rivolto verso l'esterno.
> 
> ```tikz
> \begin{document}  
> \begin{tikzpicture}[scale=1.4]  
> \draw[thick] (0,0.3) .. controls (1.2,0.4) and (1.8,0.7) .. (2.2,2);  
> \draw[->,thick] (1.9,1.0) -- (2.3,2.0) node[above] {$\hat t$};  
> \draw[->,thick] (1.9,1.0) -- (2.9,0.6) node[right] {$\underline{n}$};  
> \end{tikzpicture}  
> \end{document}  
> ```

$$\iint_{\bar D} \nabla F,dx,dy = \int_{\partial D} G,dP = \int_a^b G(\varphi(s))\cdot\varphi'(s),ds =$$

$$= \int_a^b G_1\cdot\frac{dx}{ds} + G_2\cdot\frac{dy}{ds},ds =$$

$$= \int_a^b -F_2\cdot x'(s) + F_1\cdot y'(s),ds =$$

$$= \int_a^b (F_1, F_2)\cdot(y'(s), -x'(s)),ds = \int_{\partial D} F\cdot\underline n,ds \qquad \square$$

---

## Teorema di Stokes in 2D

Sia $D \subset \mathbb{R}^2$.

Considero $f : D\times[-\varepsilon, \varepsilon] \subset \mathbb{R}^3 \to \mathbb{R}^3$ di classe $C^1$, $\quad \tilde D = D\times{0}$

Allora

$$\iint_D (\nabla\wedge f)\cdot e_3,dx,dy = \int_{\partial D} f(\cdot, 0),dP$$

> [!note] Significato  
> $D$ viene immerso nel piano $z = 0$ di $\mathbb{R}^3$. Il flusso del rotore di $f$ attraverso $\tilde D$ (con normale $e_3$) è uguale alla circuitazione di $f$ lungo il bordo. È la versione piana del teorema di Stokes e coincide con Gauss-Green.

### Dimostrazione

Espando il rotore

$$\nabla\wedge f = (\partial_2 f_3 - \partial_3 f_2,;; \partial_3 f_1 - \partial_1 f_3,;; \partial_1 f_2 - \partial_2 f_1)$$

$$(\nabla\wedge f)\cdot e_3 = \partial_1 f_2 - \partial_2 f_1$$

Impongo una restrizione $z = 0$:

$$\iint_D \partial_1 f_2(x,y,0) - \partial_2 f_1(x,y,0),dx,dy$$

Applico G.G.

$$\iint_D \partial_1 f_2 - \partial_2 f_1,dx,dy = \int_{\partial D} f_1,dx + f_2,dy$$

Per definizione

$$\int_{\partial D} f_1,dx + f_2,dy = \int_{\partial D} f(\cdot, 0),dP \qquad \square$$

> [!note] Terza componente  
> Lungo $\partial D$, che giace nel piano $z = 0$, si ha $dz = 0$: la componente $f_3$ non contribuisce all'integrale di linea.

---

## Teorema della funzione implicita

Sia $f : A \subset \mathbb{R}^2 \to \mathbb{R}$ con $f \in C^2_{(A)}$ a tratti e $\nabla f(x_0, y_0) \neq 0$

con $(x_0, y_0) \in A$ t.c. $f(x_0, y_0) = a$

Allora $\exists B$, un intorno di $(x_0, y_0)$ t.c. ${(x,y) \in B \mid f(x,y) = a}$ che coincide con $f(x)$ o con $\tilde g(y)$.

> [!warning] Notazione  
> Si intende che l'insieme di livello coincide, in $B$, con il **grafico** di $g(x)$ oppure con quello di $\tilde g(y)$, come precisato subito dopo.

Più precisamente se $\partial_y f(x_0, y_0) \neq 0 \Rightarrow \exists g : I \subset \mathbb{R} \to \mathbb{R}$ t.c.

$${(x,y) \in B \mid f(x,y) = a} = {(x, g(x)) \mid x \in I}$$

e se $\partial_x f(x_0, y_0) \neq 0 \Rightarrow \exists \tilde g : \tilde I \subset \mathbb{R} \to \mathbb{R}$ t.c.

$${(x,y) \in B \mid f(x,y) = a} = {(\tilde g(y), y) \mid y \in \tilde I}$$

con $\tilde g \in C^2_{(\tilde I)}$ a tratti.

### Dimostrazione per $\partial_y f(x_0, y_0) \neq 0$

Per il teorema di permanenza del segno: $\exists r > 0$ t.c. $B((x_0, y_0), r) \in D$ e la $\partial_y f \neq 0$ su $B$.

Cerco $g : I \subset \mathbb{R} \to \mathbb{R}$ con $I$ un intorno aperto di $\mathbb{R}$ che contiene $x_0$ t.c. $f(x, g(x)) = a$

$$\forall x \in I \quad \text{vale} \quad \partial_x f(x, g(x)) + \partial_y f(x, g(x))\cdot g'(x) = 0$$

So che dentro $B$ $\partial_y f \neq 0$, quindi scrivo la relazione con il vincolo:

$$\begin{cases} g'(x) = -\dfrac{\partial_x f(x, g(x))}{\partial_y f(x, g(x))} \[2mm] g(x_0) = y_0 \end{cases} \qquad \text{un problema di Cauchy}$$

$g'(x) \in C^1_{(B)}$: il problema ammette una sola soluzione definita su $I = (x_0 - \delta, x_0 + \delta)$, $\delta > 0$.

La soluzione è di classe $C^2$.

> [!note] Struttura dell'argomento  
> La relazione $\partial_x f + \partial_y f\cdot g' = 0$ si ottiene derivando $f(x, g(x)) = a$ con la regola della catena. Il secondo membro dell'equazione differenziale è $C^1$, quindi localmente lipschitziano: il teorema di Cauchy-Lipschitz (esistenza e unicità locale) fornisce $g$. Poiché $g'$ è composizione di funzioni $C^1$, $g$ risulta di classe $C^2$.

---

## Teorema della funzione inversa

$f : D \subset \mathbb{R}^n \to \mathbb{R}^n$, $f \in C^1_{(D)}$ e per $\hat x \in D$, $\det|J_{\hat x}| \neq 0$

Allora $\exists N$ un intorno di $\hat x$ t.c. $f : N \to f(N)$ è invertibile.

> [!note] Notazione  
> $J_{\hat x}$ è la matrice jacobiana di $f$ in $\hat x$. La condizione $\det J_{\hat x} \neq 0$ significa che il differenziale di $f$ in $\hat x$ è una mappa lineare invertibile.

### Dimostrazione

Provo che $\exists B(\hat x, \delta)$ con $\delta > 0$ t.c. $f$ è iniettiva su $B(\hat x, \delta) = N$

cioè $\forall x,y \in B(\hat x, \delta)$ per $x \neq y \Rightarrow f(x) - f(y) \neq 0 \quad \leftarrow f$ iniettiva

da $f(x) - f(y) \neq 0 \Rightarrow |f(x) - f(y)| > 0$

con $\tau > 0$ [?]

$$|J_{\hat x}^{-1}| = \frac{1}{\tau} \qquad \tau = \frac{1}{|J_{\hat x}^{-1}|}$$

Scrivo $g(x) = f(x) - J_{\hat x}\cdot x ;\to; f(x) = g(x) + J_{\hat x}\cdot x$

$$|f(x) - f(y)| \ge |\underbrace{J_{\hat x}\cdot(x-y)}_{\text{lineare}} + \underbrace{(g(x) - g(y))}_{\text{non lineare}}|$$

> [!warning] Passaggio  
> In questo punto vale l'uguaglianza: $|f(x) - f(y)| = |J_{\hat x}(x-y) + (g(x) - g(y))|$. La disuguaglianza utile, usata nella conclusione, è la triangolare inversa: $|f(x) - f(y)| \ge |J_{\hat x}(x-y)| - |g(x) - g(y)|$.

So che

$$|x - y| = |J_{\hat x}^{-1}\cdot J_{\hat x}\cdot(x-y)| \le |J_{\hat x}^{-1}|\cdot|J_{\hat x}\cdot(x-y)|$$

quindi: $|x - y|\cdot\tau \le |J_{\hat x}\cdot(x-y)|$

Calcolo $J_g(x) = J_f(x) - J_{\hat x}$

in $\hat x$: $J_g(\hat x) = J_{\hat x} - J_{\hat x} = 0$. Continuità: per $\varepsilon > 0 ;\exists; |J_g(x)| < \varepsilon$

Per il teorema della stima $|g(x) - g(y)| \le \varepsilon\cdot|x - y|$

> [!note] Continuità e teorema della stima  
> Poiché $J_g$ è continua e vale $0$ in $\hat x$, per ogni $\varepsilon > 0$ esiste $\delta > 0$ tale che $|J_g(x)| < \varepsilon$ per $x \in B(\hat x, \delta)$. Il "teorema della stima" è la disuguaglianza del valor medio su un convesso: $|g(x) - g(y)| \le \sup_B |J_g|\cdot|x - y|$.

Quindi

$$|f(x) - f(y)| \ge \tau\cdot|x-y| - \varepsilon\cdot|x-y| \ge (\tau - \varepsilon)\cdot|x-y| > 0 \qquad \tau > \varepsilon$$

$$|f(x) - f(y)| > 0$$

$f$ è iniettiva quindi invertibile $\square$

> [!note] Portata della dimostrazione  
> L'argomento prova l'iniettività locale, quindi l'invertibilità di $f : N \to f(N)$. L'enunciato completo del teorema aggiunge che $f(N)$ è aperto e che l'inversa è di classe $C^1$, con $J_{f^{-1}}(f(x)) = J_f(x)^{-1}$.

---

## Numeri complessi

$x^2 + 1 = 0 \qquad \nexists$ soluzioni in $\mathbb{R}$

Si introduce $i$, l'**unità immaginaria**, un numero t.c. $i^2 = -1$

$$\mathbb{C} := {a + ib ;\text{ t.c. }; a, b \in \mathbb{R}}$$

- $a$ = parte reale $= \operatorname{Re}(z)$
- $b$ = parte immaginaria $= \operatorname{Im}(z)$

$\mathbb{R}$ è un campo ordinato: dati due qualunque numeri riesco a stabilire il maggiore.  
$\mathbb{C}$ non è un campo ordinato.

### Operazioni tra numeri complessi

dati: $z_1 = a + ib$, $z_2 = c + id$ con $a,b,c,d \in \mathbb{R}$

#### Somma

$$z_1 + z_2 = a + c + i(b + d) = \operatorname{Re}(z_1 + z_2) + i\operatorname{Im}(z_1 + z_2)$$

es. $(1 + i) + (-2 + 3i) = -1 + 4i$

#### Prodotto

$$z_1\cdot z_2 = (a + ib)(c + id) = ac - bd + i(bc + ad)$$

### Complesso coniugato $\bar z$ (def.)

dato $z \in \mathbb{C}$, $\bar z = a - ib$ (con $z = a + ib$)

osservazione:

$$z = \bar z \iff z \in \mathbb{R}$$

$$z + \bar z = 2\operatorname{Re}(z)$$

$$z\cdot\bar z = (a + ib)(a - ib) = a^2 - i^2 b^2 = a^2 + b^2$$

### Norma di un numero complesso $N(z)$

$$N(z) = a^2 + b^2 \in \mathbb{R}$$

$$N(z) = 0 \iff z = 0 \qquad (a = b = 0)$$

### Inverso di un numero complesso

se $z \neq 0 \Rightarrow N(z) \neq 0$: l'inverso di $z$ sarà questo numero $\dfrac{1}{a^2 + b^2},\bar z \in \mathbb{C}$

per definizione di inverso: $z\cdot\dfrac{1}{a^2 + b^2},\bar z = 1$

$$\frac{1}{a^2 + b^2}\cdot\bar z \Rightarrow \left(\frac{a}{a^2 + b^2} - i,\frac{b}{a^2 + b^2}\right)\bar z = z^{-1}$$

> [!warning] Fattore in eccesso  
> Il $\bar z$ finale è di troppo: $z^{-1} = \dfrac{\bar z}{a^2 + b^2} = \dfrac{a}{a^2 + b^2} - i,\dfrac{b}{a^2 + b^2}$.

$$\forall z \in \mathbb{C}^* ;; \exists!, z^{-1}$$

> [!note] Notazione  
> $\mathbb{C}^* = \mathbb{C}\setminus{0}$.

### Forma algebrica

$a + ib$ con $a, b \in \mathbb{R}$

osservazioni:

$$a + ib = c + id \iff a = c,; b = d$$

$z = a + ib$, l'opposto $-z = -a - ib = -a + i(-b)$

$$z + (-z) = 0$$

$\forall z \in \mathbb{C}^*$, $z$ è invertibile rispetto al prodotto, cioè $\exists z^{-1} \in \mathbb{C}$ t.c. $z^{-1}\cdot z = 1$

$$z^{-1} = \frac{\bar z}{N(z)} = \frac{\bar z}{a^2 + b^2} = \frac{a}{N(z)} + i,\frac{b}{N(z)}$$

> [!warning] Segno  
> Il segno della parte immaginaria è sbagliato: $z^{-1} = \dfrac{a}{N(z)} - i,\dfrac{b}{N(z)}$. La verifica successiva usa correttamente $-\dfrac{b}{N(z)}$.

verifica:

$$z\cdot z^{-1} = 1 \Rightarrow (a + ib)\left(\frac{a}{N(z)} + i\cdot\left(-\frac{b}{N(z)}\right)\right) = 1$$

$$\frac{a^2}{N(z)} + \frac{b^2}{N(z)} + i\left(\frac{ab}{N(z)} - \frac{ab}{N(z)}\right) = \frac{a^2 + b^2}{N(z)} = \frac{N(z)}{N(z)} = 1$$

verifica: $z\cdot\bar z = N(z)$, $z = -3 + 2i$, $\dfrac{1}{z} = \dfrac{1}{-3 + 2i}$

$$\frac{1}{-3 + 2i}\cdot\frac{-3 - 2i}{-3 - 2i} = \frac{-3 - 2i}{13} = -\frac{3}{13} - \frac{2}{13},i$$

---

## Modulo di un numero complesso $|z|$

$z = \sqrt{a + ib}$ [?] $\qquad z \in \mathbb{R} \Rightarrow |z| = |a|$

> [!warning] Prima riga  
> Si intende $z = a + ib$. Il modulo è definito dalla riga successiva.

$$|z| = \sqrt{a^2 + b^2} = \sqrt{N(z)}$$

### Proprietà $|z|$

$$|z_1\cdot z_2| = |z_1|\cdot|z_2|$$

$$|z_1 + z_2| \neq |z_1| + |z_2| \qquad \neq \text{ in generale}$$

$$|z_1 + z_2| \le |z_1| + |z_2| \qquad \text{disuguaglianza triangolare}$$

### Forma geometrica

$$a + ib \leftrightarrow (a, b)$$

Legenda dei colori nel disegno: verde $\theta$, rosso $|z|$, viola $b$, blu $a$.

> [!info] Figura  
> Piano di Gauss con assi $\operatorname{Re}(z)$ e $\operatorname{Im}(z)$. Il punto $z = (a,b)$ è collegato all'origine da un segmento di lunghezza $|z|$ (rosso); le proiezioni tratteggiate sugli assi individuano $a$ (blu) e $b$ (viola); l'angolo tra l'asse reale e il segmento è $\theta$ (verde).
> 
> ```tikz
> \begin{document}  
> \begin{tikzpicture}[scale=1.3]  
> \draw[->] (-1,0) -- (3,0) node[right] {$\mathrm{Re}(z)$};  
> \draw[->] (0,-1) -- (0,2.3) node[above] {$\mathrm{Im}(z)$};  
> \draw[thick,red] (0,0) -- (2,1.5);  
> \draw[dashed,blue] (2,1.5) -- (2,0);  
> \draw[dashed,violet] (2,1.5) -- (0,1.5);  
> \fill (2,1.5) circle (1.5pt) node[above right] {$z$};  
> \draw[green!50!black] (0.5,0) arc (0:36.87:0.5);  
> \node[green!50!black] at (0.75,0.2) {$\theta$};  
> \node[red] at (0.9,0.95) {$|z|$};  
> \node[blue] at (1,-0.25) {$a$};  
> \node[violet] at (-0.25,0.75) {$b$};  
> \end{tikzpicture}  
> \end{document}  
> ```

$$|z| = \sqrt{a^2 + b^2} = \rho$$

$$a = \rho\cos\theta \qquad b = \rho\sin\theta$$

$$\theta = \operatorname{Arg}(z) \qquad 0 \le \theta < 2\pi \qquad \theta \bmod (2\pi)$$

### Forma trigonometrica

$$z = \rho(\cos\theta + i\sin\theta)$$

$z = 1 + i$, $\quad a = 1,; b = 1,; \rho = \sqrt 2$

$$\cos\theta = \frac{a}{\rho} = \frac{1}{\sqrt 2} \qquad \sin\theta = \frac{b}{\rho} = \frac{\sqrt 2}{2} \qquad \theta = \frac{\pi}{4}$$

osservazione:

$$\bar z = \rho\big(\cos(-\theta) + i\sin(-\theta)\big) = \rho\big(\cos(2\pi - \theta) + i\sin(2\pi - \theta)\big)$$

$$N(z) = \rho^2 \qquad z^{-1} = \frac{\bar z}{N(z)} = \frac{1}{\rho}\big(\cos(-\theta) + i\sin(-\theta)\big) \qquad z \neq 0$$

proprietà:

$$z_1 = \rho_1(\cos\theta_1 + i\sin\theta_1) \qquad z_2 = \rho_2(\cos\theta_2 + i\sin\theta_2)$$

$$z_1 z_2 = \rho_1\rho_2\big(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\big)$$

$$= \rho_1\rho_2\big[(\cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2) + i(\cos\theta_1\sin\theta_2 + \sin\theta_1\cos\theta_2)\big]$$

> [!note] Interpretazione  
> Nel prodotto i moduli si moltiplicano e gli argomenti si sommano. L'ultima riga è lo sviluppo diretto del prodotto, ricondotto alla prima tramite le formule di addizione di seno e coseno.

### Potenza

$$z = \rho(\cos\theta + i\sin\theta)$$

$$z^2 = \rho^2(\cos 2\theta + i\sin 2\theta)$$

$$z^n = \rho^n(\cos n\theta + i\sin n\theta) \qquad \cancel{n \ge 1};; \forall n \in \mathbb{Z}$$

> [!note] Formula di De Moivre  
> È la formula di De Moivre: discende dal prodotto applicato $n$ volte. Vale anche per $n$ negativo, usando l'espressione di $z^{-1}$ data sopra.

### Divisione

$$\frac{z_1}{z_2} = z_1\cdot\frac{1}{z_2} = \frac{\rho_1}{\rho_2}\big(\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)\big) \qquad z_2 \neq 0$$

### Radici

cerco i numeri complessi $x = c(\cos\varphi + i\sin\varphi)$ che verificano $x^n = z$

quindi

$$x^n = c^n(\cos n\varphi + i\sin n\varphi) = \rho(\cos\theta + i\sin\theta)$$

$$\Rightarrow \begin{cases} c^n = \rho & (c, \rho \in \mathbb{R}_{>0}) \ n\varphi \equiv \theta & \bmod (2\pi) \end{cases} = \begin{cases} c = \sqrt[n]{\rho} \ n\varphi = \theta + 2k\pi & k \in \mathbb{Z} \end{cases}$$

$$\begin{cases} c = \sqrt[n]{\rho} \[1mm] \varphi = \dfrac{\theta + 2k\pi}{n} & k \in \mathbb{Z} \end{cases} \qquad \begin{aligned} k = 0 &\quad \varphi = \theta/n \ k = 1 &\quad \varphi = \theta/n + 2\pi/n \ &;;\vdots \end{aligned}$$

le soluzioni

$$x_k = \sqrt[n]{\rho}\left(\cos\frac{\theta + 2k\pi}{n} + i\sin\frac{\theta + 2k\pi}{n}\right) \qquad k \in \mathbb{Z}$$

si trovano per i $k$ fino a $n - 1$ (poi si ripetono): $k = nq + r$, $0 \le r \le n - 1$, $\varphi = \theta/n + 2\pi r/n$ [?] [illeggibile]

> [!note] Perché $n$ radici  
> Scrivendo $k = nq + r$ si ha $\varphi = \frac{\theta}{n} + \frac{2\pi r}{n} + 2\pi q$: il termine $2\pi q$ non cambia il punto. Le radici distinte sono quindi esattamente $n$, per $k = 0, \dots, n-1$, e sono i vertici di un poligono regolare inscritto nella circonferenza di raggio $\sqrt[n]{\rho}$.

---

## Numeri complessi (2024)

prop. sia $z$ un numero t.c. $z \in \mathbb{C}$

|||
|---|---|
|$\overline{(\bar z)} = z$|$\overline{(z + w)} = \bar z + \bar w$|
|$\lvert\bar z\rvert = z$|$\overline{(z\cdot w)} = \bar z\cdot\bar w$|
|$\lvert z\rvert = 0 \iff z = 0$|$z\cdot\bar z = a^2 + b^2 = \lvert z\rvert^2$|
|$\forall z \neq 0 \quad \overline{z^{-1}} = (\bar z)^{-1}$|$z + \bar z = 2a$|

> [!warning] Modulo del coniugato  
> La proprietà corretta è $|\bar z| = |z|$.

**def.** Si definisce **argomento** di un numero complesso l'angolo che si forma tra l'asse reale e la semiretta che collega $z$ con l'origine.

$$\sin(\operatorname{Arg}(z)) = \frac{b}{|z|} \qquad b = |z|\cdot\sin(\operatorname{Arg}(z))$$

$$\cos(\operatorname{Arg}(z)) = \frac{a}{|z|} \qquad a = |z|\cdot\cos(\operatorname{Arg}(z))$$

$$z = a + ib = |z|\cdot\cos(\operatorname{Arg}(z)) + |z|,i\sin(\operatorname{Arg}(z)) =$$

$$= |z|\cdot\big(\cos(\arg(z)) + i\sin(\arg(z))\big)$$

$$\tan(\arg(z)) = \frac{\sin(\arg(z))}{\cos(\arg(z))} = \frac{b/|z|}{a/|z|} = \frac{b}{a} \qquad \text{con } a \neq 0$$

### Ricavare l'opposto

$z\cdot w$ t.c. $z\cdot w = 1$, $w = z^{-1}$

> [!warning] Terminologia  
> Si sta ricavando l'**inverso** (rispetto al prodotto), non l'opposto.

$$z^{-1} = \frac{\bar z}{|z|^2} \qquad \cos(-\alpha) = \cos\alpha, \quad \sin(-\alpha) = -\sin\alpha$$

$$z = |z|(\cos\alpha + i\sin\alpha), \qquad z^{-1} = \frac{1}{|z|}(\cos\beta + i\sin\beta)$$

$$\Rightarrow z\cdot z^{-1} = \frac{|z|}{|z|}\big(\cos\alpha\cos\beta + i\cos\alpha\sin\beta + i\sin\alpha\cos\beta + i^2\sin\alpha\sin\beta\big) = 1$$

$$= \underbrace{\cos\alpha\cos\beta - \sin\alpha\sin\beta}_{=1} + \underbrace{i(\cos\alpha\sin\beta + \cos\beta\sin\alpha)}_{=0} = 1$$

$\beta = -\alpha ;\to$

$$= \cos\alpha\cdot\cos(-\alpha) - \sin\alpha\sin(-\alpha) + i\big(\cos(\alpha)\sin(-\alpha) + \cos(-\alpha)\sin\alpha\big) = 1$$

$\cos\alpha = \cos(-\alpha)$, $-\sin\alpha = \sin(-\alpha) ;\to$

$$= \cos\alpha\cos\alpha - \sin\alpha(-\sin\alpha) + i\big(\cos\alpha\cdot(-\sin\alpha) + \cos\alpha\sin\alpha\big) = 1$$

$\cos^2 x + \sin^2 x = 1 ;\to$

$$= \cos^2\alpha + \sin^2\alpha + i\cdot 0 = 1 \Rightarrow 1 = 1$$

> [!note] Conclusione  
> La scelta $\beta = -\alpha$ soddisfa le due condizioni (parte reale $= 1$, parte immaginaria $= 0$). Quindi l'inverso ha modulo $1/|z|$ e argomento $-\alpha$.

### Formula di Eulero

sia $z = \alpha + i\beta \in \mathbb{C}$

$$e^z = e^\alpha\underbrace{(\cos\beta + i\sin\beta)}_{e^{i\beta}} = e^a\cdot e^{ib} = e^{a + ib}$$

$$z = |z|(\cos\alpha + i\sin\alpha) = |z|,e^{i\alpha} \qquad \textit{forma esponenziale}$$

proprietà:

- $z\cdot w = |z|\cdot|w|\cdot e^{i(\arg(z) + \arg(w))}$
- $z^{-1} = \dfrac{1}{|z|}\cdot e^{-i\alpha}$

### Equazioni di forma $x^n = w$

con $w \in \mathbb{C}$, $\theta = \arg w$

$$w = |w|\cdot e^{i\theta}$$

$$x^n = |w|\cdot e^{i\theta}$$

$$x = \sqrt[n]{|w|}\cdot\left(e^{i\theta}\right)^{1/n} = \sqrt[n]{|w|}\cdot e^{i\theta/n}$$

$$n\cdot\arg(x) = \theta + 2k\pi \qquad k \in \mathbb{N},; 0 \le k \le n-1$$

esempio: $x^3 = 1 ;\to; |w| = 1$, $\theta = 0$

$$|x| = \sqrt[3]{1} = 1$$

$$3\arg(x) = \theta + 2k\pi \qquad k \in \mathbb{N},; 0 \le k \le 2$$

$$3\arg(x) = 2k\pi$$

$$\arg(x) = \frac{2\pi}{3}\cdot k$$

$$x_1 = 1\cdot e^{i0}, \qquad x_2 = 1\cdot e^{i\frac{2}{3}\pi}, \qquad x_3 = e^{i\frac{4}{3}\pi}$$

---

## Condizioni di Cauchy-Riemann

Sia $f = u + i\cdot v$ una funzione $f : D \subset \mathbb{C} \to \mathbb{C}$, $; z \mapsto f(z)$

$$x + iy \to u(x,y) + i\cdot v(x,y) \qquad z_0 = (x_0, y_0) \in D$$

**1]** Se $\exists f'(z_0)$ con $z_0 \in D \Rightarrow \exists$ le derivate parziali di $u, v$ in $z_0$

$$\begin{cases} u_x(x_0, y_0) = v_y(x_0, y_0) \ u_y(x_0, y_0) = -v_x(x_0, y_0) \end{cases} \qquad \text{valgono le condizioni di Cauchy-Riemann}$$

### Dimostrazione

Per ipotesi

$$\exists f'(z_0) = \lim_{z\to z_0}\frac{f(z) - f(z_0)}{z - z_0} \in \mathbb{C}$$

considero 2 restrizioni.

> [!note] Idea  
> Se il limite esiste in $\mathbb{C}$, deve valere lo stesso lungo qualunque direzione di avvicinamento. Confrontando la direzione reale ($h$) e quella immaginaria ($ih$) si ottengono le due condizioni.

**Restrizione 1:** $z = z_0 + h$, $h \in \mathbb{R}$, $h \to 0$

$$z_0 + h = \begin{cases} x = x_0 + h \ y = y_0 \end{cases}$$

$$\frac{f(z) - f(z_0)}{z - z_0} = \frac{[u(x,y) + i\cdot v(x,y)] - [u(x_0,y_0) + i,v(x_0,y_0)]}{h} =$$

$$= \frac{u(x,y) - u(x_0,y_0)}{h} + i,\frac{v(x,y) - v(x_0,y_0)}{h} =$$

$$= \frac{u(x_0 + h, y_0) - u(x_0,y_0)}{h} + i,\frac{v(x_0 + h, y_0) - v(x_0,y_0)}{h} =$$

$$\lim_{h\to 0}\frac{f(z) - f(z_0)}{h} = \lim_{h\to 0}\frac{u(x_0 + h, y_0) - u(x_0,y_0)}{h} + i,\frac{v(x_0 + h, y_0) - v(x_0,y_0)}{h} =$$

$$= u_x(x_0,y_0) + i,v_x(x_0,y_0) = f'(z_0)$$

**Restrizione 2:** $z = z_0 + ih$

$$z_0 + ih = \begin{cases} x = x_0 \ y = y_0 + h \end{cases}$$

$$\lim_{h\to 0}\frac{f(z) - f(z_0)}{ih} = \lim_{h\to 0}\frac{u(x,y) - u(x_0,y_0)}{ih} + \cancel{i},\frac{v(x,y) - v(x_0,y_0)}{\cancel{i}h} =$$

$$= \lim_{h\to 0} -i,\frac{u(x_0, y_0 + h) - u(x_0,y_0)}{h} + \frac{v(x_0, y_0 + h) - v(x_0,y_0)}{h} =$$

$$= v_y(x_0,y_0) - i,u_y(x_0,y_0) = f'(z_0)$$

> [!note] Passaggio  
> Si è usato $\frac{1}{i} = -i$.

Quindi $u_x(x_0,y_0) = v_y(x_0,y_0)$ e $v_x(x_0,y_0) = -u_y(x_0,y_0)$ $\square$

**2]** Se $u, v$ sono differenziabili in $(x_0, y_0)$ e valgono le C.R.

allora $\exists f'(z_0) = f'(x_0 + i,y_0)$, $\quad f'(z_0) = u_x(x_0,y_0) + i,v_x(x_0,y_0)$

### Dimostrazione

$$\text{differenziabili} \Rightarrow \begin{cases} u(x,y) = u(x_0,y_0) + u_x(x_0,y_0)\cdot(x - x_0) + u_y(x_0,y_0)\cdot(y - y_0) + o(|z - z_0|) \ v(x,y) = v(x_0,y_0) + \underbrace{v_x(x_0,y_0)}_{-u_y(x_0,y_0)}\cdot(x - x_0) + \underbrace{v_y(x_0,y_0)}_{u_x(x_0,y_0)}\cdot(y - y_0) + o(|z - z_0|) \end{cases} \leftarrow \text{C.R.}$$

$$f(z) - f(z_0) = u(x,y) + i,v(x,y) - u(x_0,y_0) - i,v(x_0,y_0) =$$

$$= u(x,y) - u(x_0,y_0) + i,[v(x,y) - v(x_0,y_0)] =$$

$$= u_x(x_0,y_0)(x - x_0) + u_y(x_0,y_0)(y - y_0) + o(|z - z_0|) + i,[v_x(x_0,y_0)(x - x_0) + v_y(x_0,y_0)(y - y_0) + o(|z - z_0|)] =$$

$$= u_x(x_0,y_0)(x - x_0) + u_y(x_0,y_0)(y - y_0) + o(|z - z_0|) + i,[-u_y(x_0,y_0)(x - x_0) + u_x(x_0,y_0)(y - y_0) + o(|z - z_0|)] =$$

$$= [u_x(x_0,y_0) - i,u_y(x_0,y_0)]\cdot(x - x_0) + [u_y(x_0,y_0) + i,u_x(x_0,y_0)]\cdot(y - y_0) + o(|z - z_0|) =$$

$$= [u_x(x_0,y_0) - i,u_y(x_0,y_0)]\cdot(x - x_0) + i,[u_x(x_0,y_0) - i,u_y(x_0,y_0)]\cdot(y - y_0) + o(|z - z_0|) =$$

$$= [u_x(x_0,y_0) - i,u_y(x_0,y_0)]\cdot[(x - x_0) + i(y - y_0)] + o(|z - z_0|) =$$

$$= [u_x(x_0,y_0) - i,u_y(x_0,y_0)]\cdot(z - z_0) + o(|z - z_0|)$$

$$\frac{f(z) - f(z_0)}{z - z_0} = [u_x(x_0,y_0) - i,u_y(x_0,y_0)]\cdot\frac{z - z_0}{z - z_0} + \frac{o(|z - z_0|)}{z - z_0} =$$

$$= [u_x(x_0,y_0) - i,u_y(x_0,y_0)]\cdot 1 + 0 =$$

$$= u_x(x_0,y_0) - i,u_y(x_0,y_0) = u_x(x_0,y_0) + i,v_x(x_0,y_0) = f'(z_0) \qquad \square$$

> [!note] Passaggio al limite  
> Le ultime due righe valgono nel limite $z \to z_0$: è il termine $\frac{o(|z - z_0|)}{z - z_0}$ a tendere a $0$.

---

## Teorema di Cauchy

Siano: $f : D \subset \mathbb{C} \to \mathbb{C}$ **olomorfa** e $C$ una curva chiusa.

Se il bordo di $C$ e $A_C$ la sua regione interna $A_C$ sono contenuti in $D$ $\Rightarrow$

$$\oint_C f(z),dz = 0$$

> [!note] Olomorfa  
> Una funzione è **olomorfa** su un aperto se è derivabile in senso complesso in ogni suo punto.

### Dimostrazione

Sia $\gamma : [a,b] \to D \subset \mathbb{C}$ una parametrizzazione di $C$, una curva chiusa.

$$\int_C f(z),dz = \int_a^b (f\circ\gamma)(\eta)\cdot\gamma'(\eta),d\eta \qquad f(z) = u(x,y) + i,v(x,y) \qquad \gamma(\eta) = x(\eta) + i\cdot y(\eta)$$

$$= \int_a^b [u(x(\eta), y(\eta)) + i\cdot v(x(\eta), y(\eta))]\cdot(x'(\eta) + i\cdot y'(\eta)),d\eta =$$

$$= \int_a^b u(x(\eta),y(\eta))\cdot x'(\eta) - v(x(\eta),y(\eta))\cdot y'(\eta),d\eta + i\int_a^b u(x(\eta),y(\eta))\cdot y'(\eta) + v(x(\eta),y(\eta))\cdot x'(\eta),d\eta =$$

$$\int_a^b u(x(\eta),y(\eta))\cdot x'(\eta),d\eta = \int_C u(x,y),dx \qquad \int_a^b u(x(\eta),y(\eta))\cdot y'(\eta),d\eta = \int_C u(x,y),dy$$

$$= \int_C u(x,y),dx - \int_C v(x,y),dy + i\int_C u(x,y),dy + i\int_C v(x,y),dx = \qquad \text{ora Gauss-Green}$$

$$= -\iint_{A_C} u_y(x,y),dx,dy - \iint_{A_C} v_x(x,y),dx,dy + i\iint_{A_C} u_x(x,y),dx,dy - i\iint_{A_C} v_y(x,y),dx,dy =$$

$$= -\iint_{A_C} u_y(x,y) + v_x(x,y),dx,dy + i\iint_{A_C} u_x(x,y) - v_y(x,y),dx,dy = \qquad \text{applico le C.R.}$$

$$= -\iint_{A_C} u_y(x,y) - u_y(x,y),dx,dy + i\iint_{A_C} u_x(x,y) - u_x(x,y),dx,dy = 0$$

$$\oint_C f(z),dz = 0 \qquad \square$$

$f$ è olomorfa, $A_C \subset D \Rightarrow \forall z \in A_C$ valgono le condizioni di Cauchy-Riemann.

> [!note] Applicazione di Gauss-Green  
> Con $\int_C P,dx + Q,dy = \iint (Q_x - P_y)$: per la parte reale $P = u$, $Q = -v$; per la parte immaginaria $P = v$, $Q = u$. Questa dimostrazione richiede che $u, v$ siano di classe $C^1$, ipotesi necessaria per applicare Gauss-Green.

---

## Formula integrale di Cauchy

Sia $f : D \subset \mathbb{C} \to \mathbb{C}$

con $D$ un insieme semplicemente connesso e $C$ una curva chiusa semplice.

Sia $z_0$ un punto interno a $C$ $\Rightarrow$

$$f(z_0) = \frac{1}{2\pi i}\cdot\oint_C\frac{f(z)}{z - z_0},dz$$

> [!warning] Ipotesi  
> Manca l'ipotesi che $f$ sia **olomorfa** su $D$, usata nella dimostrazione.

> [!note] Semplicemente connesso  
> Un insieme connesso è **semplicemente connesso** se non ha "buchi": ogni curva chiusa in esso può essere deformata con continuità fino a un punto senza uscirne. Una curva **semplice** non ha autointersezioni.

### Dimostrazione

$z_0$ è interno a $C$ che è chiusa e supportata su $D$ semplicemente connesso $\Rightarrow z_0 \in D$

$$C_0 = \gamma_0 : [0, 2\pi] \to \mathbb{C}, \qquad \eta \to z_0 + \delta\cdot e^{i\eta}$$

Introduco $\tilde C = C * T * C_0^- * T^-$

La regione interna di $\tilde C$ è contenuta in $D$ ma non contiene $z_0$

$$D\setminus{z_0} \to \mathbb{C}, \qquad z \to \frac{f(z)}{z - z_0} \quad \text{è olomorfa su } D\setminus{z_0}$$

> [!info] Figura  
> Insieme $D$ (rettangolo) contenente la curva chiusa $C$ (rossa, verso antiorario). Al suo interno la circonferenza $C_0$ (verde) di centro $z_0$ e raggio $\delta$. Il segmento $T$ collega $C$ a $C_0$. La regione tratteggiata compresa tra $C$ e $C_0$ è la regione interna di $\tilde C$, che esclude $z_0$. $\delta$ = raggio di $C_0$.
> 
> ```tikz
> \begin{document}  
> \begin{tikzpicture}[scale=1.1]  
> \draw (0,0) rectangle (5,4);  
> \node at (4.75,3.75) {$D$};  
> \draw[thick,red] (2.5,2) ellipse (2 and 1.5);  
> \node[red] at (4.65,2.9) {$C$};  
> \draw[->,thick,red] (4.5,1.9) -- (4.5,2.1);  
> \draw[thick,green!50!black] (2.8,2.2) circle (0.6);  
> \node[green!50!black] at (3.6,2.75) {$C_0$};  
> \fill (2.8,2.2) circle (1.2pt) node[left] {$z_0$};  
> \draw (2.8,2.2) -- (3.4,2.2) node[midway,above] {$\delta$};  
> \draw[->,thick] (2.8,0.52) -- (2.8,1.6);  
> \node at (3.05,1.0) {$T$};  
> \end{tikzpicture}  
> \end{document}  
> ```

> [!note] Cammino $\tilde C$  
> $*$ indica la concatenazione di curve. Si percorre $C$, si entra lungo $T$, si percorre $C_0$ in verso opposto ($C_0^-$) e si torna indietro lungo $T$ ($T^-$). I due passaggi su $T$ si annullano, e $\tilde C$ racchiude una regione su cui $f(z)/(z - z_0)$ è olomorfa.

Uso il teorema di Cauchy:

$$\oint_{\tilde C}\frac{f(z)}{z - z_0},dz = 0$$

$$\int_C\frac{f(z)}{z - z_0},dz + \int_T\frac{f(z)}{z - z_0},dz - \int_{C_0}\frac{f(z)}{z - z_0},dz - \int_T\frac{f(z)}{z - z_0},dz = 0$$

Si vuole provare che

$$\int_C\frac{f(z)}{z - z_0},dz = \int_{C_0}\frac{f(z)}{z - z_0},dz$$

$$\int_C\frac{f(z)}{z - z_0},dz - 2\pi i\cdot f(z_0) = \int_{C_0}\frac{f(z)}{z - z_0},dz - 2\pi i\cdot f(z_0)$$

$$= \int_0^{2\pi}\frac{f(z_0 + \delta\cdot e^{i\eta})}{\delta\cdot e^{i\eta}}\cdot i,\delta e^{i\eta},d\eta - 2\pi i\cdot f(z_0) = i\int_0^{2\pi} f(z_0 + \delta\cdot e^{i\eta}) - f(z_0),d\eta$$

$f$ olomorfa $\Rightarrow f$ continua

Posso fissare $\varepsilon > 0$ e trovare $\delta > 0$ t.c. $|z - z_0| \le \delta \Rightarrow |f(z) - f(z_0)| \le \varepsilon$

$$\left|\int_C\frac{f(z)}{z - z_0},dz - 2\pi i\cdot f(z_0)\right| = \left|\int_0^{2\pi} f(z_0 + \delta\cdot e^{i\eta}) - f(z_0),d\eta\right| \le$$

$$\le \int_0^{2\pi}\left|f(z_0 + \delta\cdot e^{i\eta}) - f(z_0)\right|d\eta \le 2\pi\cdot\varepsilon$$

La disuguaglianza vale $\forall \varepsilon > 0$

Quindi

$$\int_C\frac{f(z)}{z - z_0},dz - 2\pi i\cdot f(z_0) = 0 \qquad \square$$

> [!note] Perché si può scegliere $\delta$  
> Il primo membro non dipende da $\delta$, grazie all'uguaglianza tra l'integrale su $C$ e quello su $C_0$. Si può quindi prendere il raggio $\delta$ piccolo quanto richiesto dalla continuità di $f$ in $z_0$.

---

## Teorema dei residui

Sia $D \subset \mathbb{C}$ un sottoinsieme semplicemente connesso.

Siano $z_1, \dots, z_n \in D$ i punti singolari isolati di $f(z)$ olomorfa, $f : D\setminus{z_1, \dots, z_n} \subset \mathbb{C} \to \mathbb{C}$.

Presa una curva chiusa semplice supportata in $D$ che contiene $z_1, \dots, z_n$

vale la formula

$$\oint_C f(z),dz = 2\pi i\cdot\sum_{k=1}^{n}\operatorname{Res}(f, z_k)$$

> [!note] Residuo  
> Il **residuo** di $f$ in una singolarità isolata $z_k$ è il coefficiente $c_{-1}$ dello sviluppo di Laurent di $f$ attorno a $z_k$. Equivalentemente, $\operatorname{Res}(f, z_k) = \frac{1}{2\pi i}\oint_{C_k} f(z),dz$, con $C_k$ una piccola circonferenza attorno a $z_k$ percorsa in verso antiorario. È questa identità a giustificare il penultimo passaggio della dimostrazione.

### Dimostrazione

> [!info] Figura  
> Curva chiusa $C$ (rossa, verso antiorario; nell'originale ha forma a "boomerang") che racchiude tre singolarità $z_1, z_2, z_3$. Attorno a ciascuna è tracciata una piccola circonferenza $C_k$ (verde). I segmenti $T_k$ collegano $C$ a ciascuna $C_k$.
> 
> ```tikz
> \begin{document}  
> \begin{tikzpicture}[scale=1.0]  
> \draw[thick,red] (3,1.5) ellipse (3 and 1.5);  
> \draw[->,thick,red] (6,1.4) -- (6,1.6);  
> \node[red] at (6.3,2.3) {$C$};  
> \draw[thick,green!50!black] (1.5,1.5) circle (0.35);  
> \draw[thick,green!50!black] (3,2.0) circle (0.35);  
> \draw[thick,green!50!black] (4.5,1.2) circle (0.35);  
> \fill (1.5,1.5) circle (1.2pt) node[right] {$z_1$};  
> \fill (3,2.0) circle (1.2pt) node[right] {$z_2$};  
> \fill (4.5,1.2) circle (1.2pt) node[right] {$z_3$};  
> \node[green!50!black] at (1.5,2.1) {$C_1$};  
> \node[green!50!black] at (3,2.6) {$C_2$};  
> \node[green!50!black] at (4.5,1.8) {$C_3$};  
> \draw[thick] (1.5,0.2) -- (1.5,1.15) node[midway,left] {$T_1$};  
> \draw[thick] (3,0) -- (3,1.65) node[midway,left] {$T_2$};  
> \draw[thick] (4.5,0.2) -- (4.5,0.85) node[midway,left] {$T_3$};  
> \end{tikzpicture}  
> \end{document}  
> ```

Dal cammino scelto sulla curva $C$ e sui segmenti $T$, escludo i punti interni di $C_1, C_2, C_3$.

Il cammino si chiama $\tilde C$.

Per il teorema di Cauchy $\displaystyle\oint_{\tilde C} f(z),dz = 0$

$$\int_C f(z),dz = \sum_{k=1}^{n}\int_{C_k} f(z),dz + \int_{T_k} f(z),dz - \int_{T_k} f(z),dz =$$

$$= \sum_{k=1}^{n}\int_{C_k} f(z),dz =$$

$$= \sum_{k=1}^{n} 2\pi i\cdot\operatorname{Res}(f, z_k) =$$

$$\oint_C f(z),dz = 2\pi i\cdot\sum_{k=1}^{n}\operatorname{Res}(f, z_k) \qquad \square$$

---

## Lemma di Jordan

Sia $g : \mathbb{C}\setminus{\text{un disco}} \to \mathbb{C}$ una funzione continua.

Suppongo esista $G$ che domina $g$, cioè $|g(z)| \le G(|z|)$ $\forall z \in \mathbb{C}$, $|z| > R$, ed è infinitesima all'infinito.

Allora:

$$\lim_{\rho\to+\infty}\int_{\Gamma_\rho} e^{iaz}\cdot g(z),dz = 0$$

$\Gamma_\rho$ è una semicirconferenza di raggio $= \rho > R$.

Per $a > 0$ si trova nel semipiano positivo, per $a < 0$ in quello negativo.

> [!note] Uso tipico  
> Il lemma serve a mostrare che, nel calcolo con i residui di integrali del tipo $\int_{-\infty}^{+\infty} e^{iax}g(x),dx$, il contributo della semicirconferenza grande si annulla. Il semipiano va scelto in modo che $|e^{iaz}| = e^{-a\operatorname{Im}(z)}$ decada.

### Dimostrazione

Parametrizzo $\Gamma_\rho$ con $\gamma : [0, \pi] \to \mathbb{C}$, $; \eta \to \rho\cdot e^{i\eta} = \rho\cdot\cos(\eta) + \rho\cdot i\cdot\sin(\eta)$

$$\int_{\Gamma_\rho} e^{iaz}\cdot g(z),dz = \int_0^\pi e^{ia\cos(\eta)}\cdot e^{-a\rho\sin(\eta)}\cdot g(\rho e^{i\eta})\cdot i\rho,e^{i\eta},d\eta \qquad \text{(1)}$$

> [!warning] Esponente  
> Il primo fattore è $e^{ia\rho\cos(\eta)}$ (manca $\rho$). Il passaggio successivo non cambia, perché il modulo di tale fattore è comunque $1$.

$$\left|\int_{\Gamma_\rho} e^{iaz}\cdot g(z),dz\right| \le \int_0^\pi\left|e^{ia\cos(\eta)}\right|\cdot\left|e^{-a\rho\sin(\eta)}\right|\cdot\underline{\left|g(\rho\cdot e^{i\eta})\right|}\cdot\left|i\rho,e^{i\eta}\right|d\eta \qquad \text{(2)}$$

$$\le \int_0^\pi 1\cdot e^{-a\rho\sin(\eta)}\cdot\underline{G(|\rho\cdot e^{i\eta}|)}\cdot\rho,d\eta \le G(\rho)\cdot\rho\cdot\int_0^\pi e^{-a\rho\sin(\eta)},d\eta$$

$$\int_0^\pi e^{-a\rho\sin(\eta)},d\eta = 2\int_0^{\pi/2} e^{-a\rho\sin(\eta)},d\eta \le 2\int_0^{\pi/2} e^{-a\rho\frac{2\eta}{\pi}},d\eta \qquad \text{(3)}$$

$$2\int_0^{\pi/2} e^{-a\rho\frac{2\eta}{\pi}},d\eta = 2\left[\frac{-\pi}{2a\rho}\cdot e^{-a\rho\frac{2\eta}{\pi}}\right]_0^{\pi/2} = -\frac{\pi}{a\rho}\left[e^{-a\rho} - 1\right] = \frac{\pi}{a\rho}\left(1 - e^{-a\rho}\right)$$

$$\left|\int_{\Gamma_\rho} e^{iaz}\cdot g(z),dz\right| \le G(\rho)\cdot\rho\cdot\int_0^\pi e^{-a\rho\sin(\eta)},d\eta = G(\rho)\cdot\cancel{\rho}\cdot\frac{\pi}{a\cancel{\rho}}\left(1 - e^{-a\rho}\right)$$

$$\lim_{\rho\to+\infty}\left|\int_{\Gamma_\rho} e^{iaz}\cdot g(z),dz\right| \le \lim_{\rho\to+\infty} G(\rho)\cdot\frac{\pi}{a}\left(1 - e^{-a\rho}\right) = 0 \qquad \text{(4)}$$

$$\lim_{\rho\to+\infty}\int_{\Gamma_\rho} e^{iaz}\cdot g(z),dz = 0 \qquad \square$$

**Note ai passaggi**

1. $z(\eta) = \rho\cdot e^{i\eta}$

$$\frac{dz}{d\eta} = \frac{d(\rho\cdot e^{i\eta})}{d\eta} \qquad dz = \rho\cdot\frac{d(e^{i\eta})}{d\eta}\cdot d\eta = \rho\cdot i\cdot e^{i\eta}\cdot d\eta$$

2. Qui si usa che $G$ domina $g$.
    
3. Tra $[0, \frac{\pi}{2}]$ si ha $\frac{2}{\pi}\eta \le \sin(\eta)$ $\forall \eta \in [0, \frac{\pi}{2}]$
    

$$\frac{2}{\pi}\eta \le \sin(\eta)$$

$$-a\rho\cdot\frac{2}{\pi}\eta \ge -a\rho\cdot\sin(\eta) ;\to; e^{-a\rho\cdot\frac{2}{\pi}\eta} \ge e^{-a\rho\cdot\sin(\eta)} \qquad \forall \eta \in [0, \tfrac{\pi}{2}]$$

4. $G(+\infty) = 0$, $G$ infinitesima all'infinito.

> [!note] Dettagli  
> Il primo passaggio della (3) usa la simmetria $\sin(\pi - \eta) = \sin\eta$. La disuguaglianza $\frac{2}{\pi}\eta \le \sin\eta$ (disuguaglianza di Jordan) discende dalla concavità del seno su $[0, \pi/2]$: la corda tra $(0,0)$ e $(\pi/2, 1)$ sta sotto il grafico. La dimostrazione è svolta per $a > 0$; il caso $a < 0$ è analogo sul semipiano inferiore.

---

## Seno cardinale

$$\operatorname{sinc}(x) : \mathbb{R} \to \mathbb{R} \qquad f(x) = \begin{cases}\dfrac{\sin(x)}{x}, & x \neq 0 \[2mm] 1, & x = 0\end{cases} \quad \Rightarrow \quad \int_{-\infty}^{+\infty}\operatorname{sinc}(x),dx = \pi$$

$$\int_{-\infty}^{+\infty}\operatorname{sinc}(x),dx = \lim_{\substack{R\to+\infty \ \varepsilon\to 0^+}}\int_{[-R,R]\setminus[-\varepsilon,\varepsilon]}\frac{\sin(x)}{x},dx =$$

$$= \lim\int\frac{e^{ix} - e^{-ix}}{2ix},dx =$$

$$= \frac{1}{2i}\left(\lim\int e^{ix}\cdot\frac{1}{x},dx + \lim\int e^{-ix}\cdot\left(-\frac{1}{x}\right)dx\right)$$

$$y = -x \qquad dy = -dx$$

$$= \frac{1}{2i}\left(\lim\int e^{ix}\cdot\frac{1}{x},dx + \lim\int e^{-i(-y)}\cdot\left(-\frac{1}{-y}\right)\cdot(-1),dy\right)$$

$$= \frac{1}{i}\cdot\lim\int e^{ix}\cdot\frac{1}{x},dx$$

$$= \frac{1}{i}\cdot\pi i = \pi$$

> [!note] Passaggi chiave  
> L'esclusione di $[-\varepsilon, \varepsilon]$ serve a separare $\sin x / x$ in due termini singolari in $0$. La sostituzione $y = -x$ lascia invariato il dominio simmetrico $[-R,R]\setminus[-\varepsilon,\varepsilon]$, quindi il secondo integrale coincide con il primo e si ottiene il fattore $2$. Il valore $\lim\int e^{ix}/x,dx = i\pi$ (valore principale) si ricava con il teorema dei residui su un cammino formato dal segmento, da una semicirconferenza piccola attorno a $0$ (che contribuisce con $-i\pi\operatorname{Res}(e^{iz}/z, 0) = -i\pi$) e da una semicirconferenza grande, il cui contributo si annulla per il lemma di Jordan.

---

## Lemma di Riemann

Se $g : [a,b] \to \mathbb{R}$ di classe $C^0$ a tratti

allora

$$\lim_{\lambda\to+\infty}\int_a^b g(x)\cdot\sin(\lambda x),dx = \lim_{\lambda\to+\infty}\int_a^b g(x)\cdot\cos(\lambda x),dx = 0$$

> [!note] Significato  
> Per $\lambda$ grande la funzione oscilla così rapidamente che, su ogni piccolo intervallo dove $g$ è quasi costante, i contributi positivi e negativi si compensano.

### Dimostrazione

Considero un intervallo $[\tilde a, \tilde b]$ su cui $g$ è continua.

Lo suddivido in $n$ parti di pari ampiezza: $\tilde a = a_0, a_1, \dots, a_n = \tilde b$, $\forall i = 0, 1, \dots, n-1$

$$\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x),dx = \sum_{i=0}^{n-1}\int_{a_i}^{a_{i+1}} g(x)\cdot\sin(\lambda x),dx = \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i) + g(x_i)]\cdot\sin(\lambda x),dx =$$

$$= \sum\int_{a_i}^{a_{i+1}} g(x_i)\cdot\sin(\lambda x),dx + \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i)]\cdot\sin(\lambda x),dx =$$

$$= \sum g(x_i)\cdot\left[-\frac{\cos(\lambda x)}{\lambda}\right]_{a_i}^{a_{i+1}} + \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i)]\cdot\sin(\lambda x),dx =$$

$$= \sum g(x_i)\cdot\frac{1}{\lambda}\cdot[\cos(\lambda a_i) - \cos(\lambda a_{i+1})] + \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i)]\cdot\sin(\lambda x),dx =$$

> [!note] Notazione  
> $x_i$ è un punto fissato di $[a_i, a_{i+1}]$ (ad esempio $x_i = a_i$).

Ora si confrontano i moduli:

$$\left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x),dx\right| \le$$

$$\le \sum|g(x_i)|\cdot\frac{1}{\lambda}\cdot\underbrace{|\cos(\lambda a_i) - \cos(\lambda a_{i+1})|}_{0,\le,\cdot,\le,2} + \sum\int_{a_i}^{a_{i+1}}|g(x) - g(x_i)|\cdot\underbrace{|\sin(\lambda x)|}_{0,\le,\cdot,\le,1},dx \le$$

$$\le \sum|g(x_i)|\cdot\frac{2}{\lambda} + \sum\int_{a_i}^{a_{i+1}}|g(x) - g(x_i)|\cdot 1 \qquad \text{si stima} \quad \int_{a_i}^{a_{i+1}}|g(x) - g(x_i)| < \varepsilon\cdot(a_{i+1} - a_i)$$

$g$ è continua su $[\tilde a, \tilde b] \Rightarrow g$ è limitata e uniformemente continua:

$$\forall \varepsilon > 0 ;; \exists \delta > 0 ;; \text{t.c. se } x_1, x_2 \in [\tilde a, \tilde b] \text{ si ha } |x_2 - x_1| < \delta \Rightarrow |g(x_2) - g(x_1)| < \varepsilon$$

$$\frac{\tilde b - \tilde a}{n} < \delta ;\to; n > \frac{\tilde b - \tilde a}{\delta}$$

quindi se $x, x' \in [a_i, a_{i+1}]$ si ha $|x' - x| < \delta \Rightarrow |g(x') - g(x)| < \varepsilon$

$$\le \sum|g(x_i)|\cdot\frac{2}{\lambda} + \sum\int_{a_i}^{a_{i+1}}\varepsilon,dx \le$$

$$\le \sum M\cdot\frac{2}{\lambda} + \sum\varepsilon\cdot[a_{i+1} - a_i] \le M\cdot\frac{2}{\lambda}\sum 1 + \varepsilon\cdot\frac{\tilde b - \tilde a}{n}\sum 1 \le$$

$$\le M\cdot\frac{2}{\lambda}\cdot n + \varepsilon\cdot\frac{\tilde b - \tilde a}{n}\cdot n \le \frac{2nM}{\lambda} + \varepsilon\cdot(\tilde b - \tilde a)$$

> [!note] Costante $M$  
> $M = \sup_{[\tilde a, \tilde b]}|g|$, finito perché $g$ è continua su un compatto.

Ora mostro

$$\lim_{\lambda\to+\infty}\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x),dx = 0$$

$$\forall \tilde\varepsilon > 0 ;; \exists \Lambda > 0 ;; \text{t.c.} ;; \forall \lambda > \Lambda \Rightarrow \left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x),dx\right| \le \tilde\varepsilon$$

Definito $\varepsilon \in \left(0, \dfrac{\tilde\varepsilon}{2(\tilde b - \tilde a)}\right)$ e $\tilde\Lambda > \dfrac{4nM}{\tilde\varepsilon}$

$$\left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x),dx\right| \le \frac{2nM}{\lambda} + \varepsilon(\tilde b - \tilde a) \le$$

$$\le 2nM\cdot\frac{\tilde\varepsilon}{4nM} + \frac{\tilde\varepsilon}{2(\tilde b - \tilde a)}\cdot(\tilde b - \tilde a) \le$$

$$\le \frac{\tilde\varepsilon}{2} + \frac{\tilde\varepsilon}{2} = \tilde\varepsilon = 0$$

$$\left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x),dx\right| \le \tilde\varepsilon = 0 \qquad \square$$

> [!warning] Conclusione  
> La scrittura "$\tilde\varepsilon = 0$" è impropria. La conclusione corretta è: poiché la stima $\le \tilde\varepsilon$ vale per ogni $\tilde\varepsilon > 0$ e ogni $\lambda > \tilde\Lambda$, il limite è $0$. Si noti che $n$ dipende da $\varepsilon$ tramite $\delta$: va fissato prima di scegliere $\tilde\Lambda$.

> [!note] Estensione al caso a tratti e al coseno  
> Per $g$ continua a tratti si applica il risultato a ciascuno dei finiti intervalli di continuità e si sommano i contributi. Per il coseno l'argomento è identico, con $\left[\frac{\sin(\lambda x)}{\lambda}\right]$ come primitiva.

---

## Teorema di Fourier

Se $f : \mathbb{R} \to \mathbb{R}$ è una funzione $2\pi$ periodica di classe $C^1$ a tratti

allora

$$a_0\cdot\frac{1}{2} + \sum_{k=1}^{\infty} a_k\cdot\cos(kx) + b_k\cdot\sin(kx) \quad \text{converge a} \quad \frac{f(x^+) + f(x^-)}{2}$$

> [!note] Coefficienti e notazione  
> $a_k = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cos(kt),dt$ e $b_k = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\sin(kt),dt$. $f(x^\pm)$ sono i limiti destro e sinistro di $f$ in $x$: nei punti di continuità la serie converge a $f(x)$, nei salti al valor medio. $S_n$ indica la somma parziale fino a $k = n$.

### Dimostrazione

$$\lim_{n\to+\infty}\left[S_n - \frac{f(x^+) + f(x^-)}{2}\right] = 0$$

$$S_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cdot\left[\frac{1}{2} + \sum\cos(kt)\cdot\cos(kx) + \sin(kt)\cdot\sin(kx)\right]dt =$$

$$= \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cdot\left[\frac{1}{2} + \sum\cos(k(t - x))\right]dt = \qquad \text{sostituzione } t - x = y$$

$$= \frac{1}{\pi}\int_{-\pi}^{\pi} f(x + y)\cdot\left[\frac{1}{2} + \sum\cos(ky)\right]dy =$$

$$= \frac{1}{\pi}\int_{-\pi}^{0} f(x + y)\cdot\frac{\sin\left(y + (n + \frac{1}{2})\right)}{2\cdot\sin(y/2)},dy + \frac{1}{\pi}\int_{0}^{\pi} f(x + y)\cdot\frac{\sin\left(y + (n + \frac{1}{2})\right)}{2\cdot\sin(y/2)},dy =$$

> [!warning] Nucleo di Dirichlet  
> L'argomento del seno è $y\left(n + \frac{1}{2}\right)$, come nelle righe successive. Vale l'identità $\frac{1}{2} + \sum_{k=1}^{n}\cos(ky) = \frac{\sin\left((n + \frac{1}{2})y\right)}{2\sin(y/2)}$ (nucleo di Dirichlet). Dopo la sostituzione gli estremi restano $-\pi, \pi$ grazie alla $2\pi$-periodicità dell'integrando.

$$\Rightarrow \frac{1}{\pi}\int_{-\pi}^{0} f(x^-)\cdot\left[\frac{1}{2} + \sum\cos(ky)\right]dy = f(x^-)\cdot\frac{1}{\pi}\cdot\left[\int_{-\pi}^{0}\frac{1}{2},dy + \cancel{\int_{-\pi}^{0}\sum\cos(ky),dy}\right] = f(x^-)\cdot\frac{1}{2}$$

Vale lo stesso per $f(x^+)$.

> [!note] Passaggio successivo  
> Grazie a questo calcolo si possono scrivere $\frac{f(x^-)}{2}$ e $\frac{f(x^+)}{2}$ come integrali del nucleo su $[-\pi, 0]$ e $[0, \pi]$. Sottraendoli da $S_n$, la riga seguente rappresenta $S_n - \frac{f(x^+) + f(x^-)}{2}$.

$$= \frac{1}{\pi}\int_{-\pi}^{0}[f(x + y) - f(x^-)]\cdot\frac{\sin\left(y(n + \frac{1}{2})\right)}{2\cdot\sin(y/2)},dy + \frac{1}{\pi}\int_{0}^{\pi}[f(x + y) - f(x^+)]\cdot\frac{\sin\left(y(n + \frac{1}{2})\right)}{2\cdot\sin(y/2)},dy =$$

$$= \frac{1}{\pi}\int_{-\pi}^{0}\underbrace{\frac{f(x + y) - f(x^-)}{2\cdot\sin(y/2)}}_{\Phi^-(x)}\cdot\sin\left(y(n + \tfrac{1}{2})\right)dy + \frac{1}{\pi}\int_{0}^{\pi}\underbrace{\frac{f(x + y) - f(x^+)}{2\cdot\sin(y/2)}}_{\Phi^+(x)}\cdot\sin\left(y(n + \tfrac{1}{2})\right)dy$$

$$\lim_{n\to+\infty}\frac{1}{\pi}\int_{-\pi}^{0}[f(x + y) - f(x^-)]\cdot\frac{\sin\left(y(n + \frac{1}{2})\right)}{2\cdot\sin(y/2)},dy = 0 \qquad \text{questo è vero se vale:}$$

$$\Phi^- : [-\pi, 0] \to \mathbb{R} \qquad y \to \begin{cases}\dfrac{f(x + y) - f(x^-)}{2\cdot\sin(y/2)} & \text{su } y \in [-\pi, 0) \[2mm] f'(x^-) & \text{su } y = 0\end{cases}$$

$\Phi^-$ è continua a tratti su $[-\pi, 0)$: devo provare che $\displaystyle\lim_{y\to 0^-}$ $\exists$ finito.

> [!note] Ruolo del lemma di Riemann  
> Se $\Phi^-$ è continua a tratti su tutto $[-\pi, 0]$, il lemma di Riemann con $\lambda = n + \frac{1}{2}$ garantisce che l'integrale tende a $0$. L'unico punto critico è $y = 0$, dove il denominatore si annulla: serve che il limite di $\Phi^-$ per $y \to 0^-$ sia finito.

Esiste un intorno finito sinistro $(x - \delta, x)$ con $\delta > 0$ in cui $f \in C^1$.

In particolare:

$\forall y \in (-\delta, 0)$ il Th. Lagrange garantisce che $\exists \eta \in (y, 0)$ t.c.

$$f(x + y) - f(x^-) = f'(x + \eta),y$$

Da cui:

$$\lim_{y\to 0^-}\Phi^-(y) = \lim_{y\to 0^-} f'(x + \eta),y\cdot\frac{1}{2\cdot\sin(y/2)} = f'(x^-)$$

> [!note] Limite  
> Si usa $\frac{y}{2\sin(y/2)} \to 1$ per $y \to 0$, e $f'(x + \eta) \to f'(x^-)$ perché $\eta \to 0^-$.

Questo ci dice che $\displaystyle\lim_{n\to+\infty} S_n - \frac{f(x^-)}{2} = 0$

Allo stesso modo si prova $\displaystyle\lim_{n\to+\infty} S_n - \frac{f(x^+)}{2} = 0$

Da cui ovviamente risulta

$$\lim_{n\to+\infty} S_n - \frac{f(x^+) + f(x^-)}{2} = 0 \qquad \square$$

> [!warning] Formulazione delle due metà  
> Le due affermazioni intermedie vanno lette sulle metà dell'integrale: la parte di $S_n$ su $[-\pi, 0]$ tende a $\frac{f(x^-)}{2}$ e quella su $[0, \pi]$ tende a $\frac{f(x^+)}{2}$. Riferite all'intera $S_n$ sarebbero incompatibili tra loro; sommandole si ottiene la tesi.