# Rettificabilità e lunghezza di una curva

Data una curva $\gamma$ parametrizzata da $\varphi : [a,b] \to \mathbb{R}^n$

$$L(\gamma) = \sup_{P} L(P) \qquad \text{con } P \text{ la poligonale su } [a,b]$$

Se $L(\gamma)$ esiste finita $\Rightarrow$ $\gamma$ è **rettificabile**.

Se $\gamma$ è rettificabile $\Rightarrow$

$$L(\gamma) = \int_a^b |\varphi'(t)|\,dt$$

> [!warning] Ipotesi
> La formula integrale richiede $\varphi \in C^1([a,b])$. L'enunciato corretto è: se $\varphi \in C^1$, allora $\gamma$ è rettificabile e $L(\gamma) = \int_a^b |\varphi'(t)|\,dt$. La sola rettificabilità non basta: la dimostrazione usa infatti la continuità di $\varphi'$.

### Dimostrazione

Considero $\pi = \{t_i\}$, $i \in \{0,\dots,N\}$, una partizione di $[a,b]$.

$$L(P) = \sum_{i=1}^{N} |\varphi(t_i) - \varphi(t_{i-1})| = \sum \left| \int_{t_{i-1}}^{t_i} \varphi'(t)\,dt \right| \le \sum \int_{t_{i-1}}^{t_i} |\varphi'(t)|\,dt = \int_a^b |\varphi'(t)|\,dt$$

$$L(P) \le \int_a^b |\varphi'(t)|\,dt \qquad \text{stima dall'alto di } L(\gamma)$$

Sia $\varphi'(t)$ continua su $[a,b]$ $\Rightarrow$ $\varphi'(t)$ è **uniformemente continua** per Heine-Cantor:

$$\forall \varepsilon > 0 \;\; \exists \delta > 0 \;\; \forall s,t \in [a,b] \quad |s-t| < \delta_\varepsilon \Rightarrow |\varphi'(s) - \varphi'(t)| < \varepsilon$$

Fisso un $\varepsilon > 0$ a cui è associato un $\delta_\varepsilon$. Sia $\pi = \{t_i\} \to a = t_0, t_1, \dots, t_N = b$.

Per avere $[t_i - t_{i-1}] < \delta_\varepsilon \;\; \forall i \in \{1,\dots,N\}$, con $s \in [t_{i-1}, t_i]$ scrivo:

$$\varphi(t_i) - \varphi(t_{i-1}) = \int_{t_{i-1}}^{t_i} \varphi'(t)\,dt = \int_{t_{i-1}}^{t_i} \varphi'(t) - \varphi'(s) + \varphi'(s)\,dt$$

$$\varphi(t_i) - \varphi(t_{i-1}) = \int_{t_{i-1}}^{t_i} \varphi'(t) - \varphi'(s)\,dt + \underline{\varphi'(s)\cdot(t_i - t_{i-1})} \qquad \text{sposto il focus qui}$$

$$\varphi'(s)\cdot(t_i - t_{i-1}) = \varphi(t_i) - \varphi(t_{i-1}) - \int_{t_{i-1}}^{t_i} \varphi'(t) - \varphi'(s)\,dt$$

$$|\varphi'(s)\cdot(t_i - t_{i-1})| \le |\varphi(t_i) - \varphi(t_{i-1})| + \int_{t_{i-1}}^{t_i} |\varphi'(t) - \varphi'(s)|\,dt \qquad |\varphi'(t) - \varphi'(s)| < \varepsilon$$

$$|\varphi'(s)| \le \frac{|\varphi(t_i) - \varphi(t_{i-1})|}{t_i - t_{i-1}} + \frac{1}{t_i - t_{i-1}}\cdot \varepsilon \cdot \underbrace{\int_{t_{i-1}}^{t_i} 1\,dt}_{=\, t_i - t_{i-1}}$$

$$|\varphi'(s)| \le \frac{|\varphi(t_i) - \varphi(t_{i-1})|}{t_i - t_{i-1}} + \varepsilon$$

$$\int_{t_{i-1}}^{t_i} |\varphi'(s)|\,ds \le |\varphi(t_i) - \varphi(t_{i-1})| + \varepsilon\cdot(t_i - t_{i-1})$$

$$\int_a^b |\varphi'(s)|\,ds \le L(P) + \varepsilon\cdot(b-a) \le \sup_P L(P) + \varepsilon(b-a) \le L(\gamma) \qquad \text{stima dal basso}$$

> [!warning] Ultimo passaggio
> $\sup_P L(P) + \varepsilon(b-a) = L(\gamma) + \varepsilon(b-a)$, non $\le L(\gamma)$. Si ottiene $\int_a^b |\varphi'| \le L(\gamma) + \varepsilon(b-a)$ e, per l'arbitrarietà di $\varepsilon$, $\int_a^b |\varphi'| \le L(\gamma)$.

Unisco le due stime:

$$\int_a^b |\varphi'(s)|\,ds \le L(\gamma) \le \int_a^b |\varphi'(s)|\,ds \quad \text{da cui segue} \quad L(\gamma) = \int_a^b |\varphi'(s)|\,ds \qquad \square$$
