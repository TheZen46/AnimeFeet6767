# Teorema di Fourier

Se $f : \mathbb{R} \to \mathbb{R}$ è una funzione $2\pi$ periodica di classe $C^1$ a tratti

allora

$$a_0\cdot\frac{1}{2} + \sum_{k=1}^{\infty} a_k\cdot\cos(kx) + b_k\cdot\sin(kx) \quad \text{converge a} \quad \frac{f(x^+) + f(x^-)}{2}$$

> [!note] Coefficienti e notazione
> $a_k = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cos(kt)\,dt$ e $b_k = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\sin(kt)\,dt$. $f(x^\pm)$ sono i limiti destro e sinistro di $f$ in $x$: nei punti di continuità la serie converge a $f(x)$, nei salti al valor medio. $S_n$ indica la somma parziale fino a $k = n$.

### Dimostrazione

$$\lim_{n\to+\infty}\left[S_n - \frac{f(x^+) + f(x^-)}{2}\right] = 0$$

$$S_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cdot\left[\frac{1}{2} + \sum\cos(kt)\cdot\cos(kx) + \sin(kt)\cdot\sin(kx)\right]dt =$$

$$= \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cdot\left[\frac{1}{2} + \sum\cos(k(t - x))\right]dt = \qquad \text{sostituzione } t - x = y$$

$$= \frac{1}{\pi}\int_{-\pi}^{\pi} f(x + y)\cdot\left[\frac{1}{2} + \sum\cos(ky)\right]dy =$$

$$= \frac{1}{\pi}\int_{-\pi}^{0} f(x + y)\cdot\frac{\sin\left(y + (n + \frac{1}{2})\right)}{2\cdot\sin(y/2)}\,dy + \frac{1}{\pi}\int_{0}^{\pi} f(x + y)\cdot\frac{\sin\left(y + (n + \frac{1}{2})\right)}{2\cdot\sin(y/2)}\,dy =$$

> [!warning] Nucleo di Dirichlet
> L'argomento del seno è $y\left(n + \frac{1}{2}\right)$, come nelle righe successive. Vale l'identità $\frac{1}{2} + \sum_{k=1}^{n}\cos(ky) = \frac{\sin\left((n + \frac{1}{2})y\right)}{2\sin(y/2)}$ (nucleo di Dirichlet). Dopo la sostituzione gli estremi restano $-\pi, \pi$ grazie alla $2\pi$-periodicità dell'integrando.

$$\Rightarrow \frac{1}{\pi}\int_{-\pi}^{0} f(x^-)\cdot\left[\frac{1}{2} + \sum\cos(ky)\right]dy = f(x^-)\cdot\frac{1}{\pi}\cdot\left[\int_{-\pi}^{0}\frac{1}{2}\,dy + \cancel{\int_{-\pi}^{0}\sum\cos(ky)\,dy}\right] = f(x^-)\cdot\frac{1}{2}$$

Vale lo stesso per $f(x^+)$.

> [!note] Passaggio successivo
> Grazie a questo calcolo si possono scrivere $\frac{f(x^-)}{2}$ e $\frac{f(x^+)}{2}$ come integrali del nucleo su $[-\pi, 0]$ e $[0, \pi]$. Sottraendoli da $S_n$, la riga seguente rappresenta $S_n - \frac{f(x^+) + f(x^-)}{2}$.

$$= \frac{1}{\pi}\int_{-\pi}^{0}[f(x + y) - f(x^-)]\cdot\frac{\sin\left(y(n + \frac{1}{2})\right)}{2\cdot\sin(y/2)}\,dy + \frac{1}{\pi}\int_{0}^{\pi}[f(x + y) - f(x^+)]\cdot\frac{\sin\left(y(n + \frac{1}{2})\right)}{2\cdot\sin(y/2)}\,dy =$$

$$= \frac{1}{\pi}\int_{-\pi}^{0}\underbrace{\frac{f(x + y) - f(x^-)}{2\cdot\sin(y/2)}}_{\Phi^-(x)}\cdot\sin\left(y(n + \tfrac{1}{2})\right)dy + \frac{1}{\pi}\int_{0}^{\pi}\underbrace{\frac{f(x + y) - f(x^+)}{2\cdot\sin(y/2)}}_{\Phi^+(x)}\cdot\sin\left(y(n + \tfrac{1}{2})\right)dy$$

$$\lim_{n\to+\infty}\frac{1}{\pi}\int_{-\pi}^{0}[f(x + y) - f(x^-)]\cdot\frac{\sin\left(y(n + \frac{1}{2})\right)}{2\cdot\sin(y/2)}\,dy = 0 \qquad \text{questo è vero se vale:}$$

$$\Phi^- : [-\pi, 0] \to \mathbb{R} \qquad y \to \begin{cases}\dfrac{f(x + y) - f(x^-)}{2\cdot\sin(y/2)} & \text{su } y \in [-\pi, 0) \\[2mm] f'(x^-) & \text{su } y = 0\end{cases}$$

$\Phi^-$ è continua a tratti su $[-\pi, 0)$: devo provare che $\displaystyle\lim_{y\to 0^-}$ $\exists$ finito.

> [!note] Ruolo del lemma di Riemann
> Se $\Phi^-$ è continua a tratti su tutto $[-\pi, 0]$, il lemma di Riemann con $\lambda = n + \frac{1}{2}$ garantisce che l'integrale tende a $0$. L'unico punto critico è $y = 0$, dove il denominatore si annulla: serve che il limite di $\Phi^-$ per $y \to 0^-$ sia finito.

Esiste un intorno finito sinistro $(x - \delta, x)$ con $\delta > 0$ in cui $f \in C^1$.

In particolare:

$\forall y \in (-\delta, 0)$ il Th. Lagrange garantisce che $\exists \eta \in (y, 0)$ t.c.

$$f(x + y) - f(x^-) = f'(x + \eta)\,y$$

Da cui:

$$\lim_{y\to 0^-}\Phi^-(y) = \lim_{y\to 0^-} f'(x + \eta)\,y\cdot\frac{1}{2\cdot\sin(y/2)} = f'(x^-)$$

> [!note] Limite
> Si usa $\frac{y}{2\sin(y/2)} \to 1$ per $y \to 0$, e $f'(x + \eta) \to f'(x^-)$ perché $\eta \to 0^-$.

Questo ci dice che $\displaystyle\lim_{n\to+\infty} S_n - \frac{f(x^-)}{2} = 0$

Allo stesso modo si prova $\displaystyle\lim_{n\to+\infty} S_n - \frac{f(x^+)}{2} = 0$

Da cui ovviamente risulta

$$\lim_{n\to+\infty} S_n - \frac{f(x^+) + f(x^-)}{2} = 0 \qquad \square$$

> [!warning] Formulazione delle due metà
> Le due affermazioni intermedie vanno lette sulle metà dell'integrale: la parte di $S_n$ su $[-\pi, 0]$ tende a $\frac{f(x^-)}{2}$ e quella su $[0, \pi]$ tende a $\frac{f(x^+)}{2}$. Riferite all'intera $S_n$ sarebbero incompatibili tra loro; sommandole si ottiene la tesi.
