# Lemma di Riemann

Se $g : [a,b] \to \mathbb{R}$ di classe $C^0$ a tratti

allora

$$\lim_{\lambda\to+\infty}\int_a^b g(x)\cdot\sin(\lambda x)\,dx = \lim_{\lambda\to+\infty}\int_a^b g(x)\cdot\cos(\lambda x)\,dx = 0$$

> [!note] Significato
> Per $\lambda$ grande la funzione oscilla così rapidamente che, su ogni piccolo intervallo dove $g$ è quasi costante, i contributi positivi e negativi si compensano.

### Dimostrazione

Considero un intervallo $[\tilde a, \tilde b]$ su cui $g$ è continua.

Lo suddivido in $n$ parti di pari ampiezza: $\tilde a = a_0, a_1, \dots, a_n = \tilde b$, $\forall i = 0, 1, \dots, n-1$

$$\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x)\,dx = \sum_{i=0}^{n-1}\int_{a_i}^{a_{i+1}} g(x)\cdot\sin(\lambda x)\,dx = \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i) + g(x_i)]\cdot\sin(\lambda x)\,dx =$$

$$= \sum\int_{a_i}^{a_{i+1}} g(x_i)\cdot\sin(\lambda x)\,dx + \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i)]\cdot\sin(\lambda x)\,dx =$$

$$= \sum g(x_i)\cdot\left[-\frac{\cos(\lambda x)}{\lambda}\right]_{a_i}^{a_{i+1}} + \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i)]\cdot\sin(\lambda x)\,dx =$$

$$= \sum g(x_i)\cdot\frac{1}{\lambda}\cdot[\cos(\lambda a_i) - \cos(\lambda a_{i+1})] + \sum\int_{a_i}^{a_{i+1}}[g(x) - g(x_i)]\cdot\sin(\lambda x)\,dx =$$

> [!note] Notazione
> $x_i$ è un punto fissato di $[a_i, a_{i+1}]$ (ad esempio $x_i = a_i$).

Ora si confrontano i moduli:

$$\left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x)\,dx\right| \le$$

$$\le \sum|g(x_i)|\cdot\frac{1}{\lambda}\cdot\underbrace{|\cos(\lambda a_i) - \cos(\lambda a_{i+1})|}_{0\,\le\,\cdot\,\le\,2} + \sum\int_{a_i}^{a_{i+1}}|g(x) - g(x_i)|\cdot\underbrace{|\sin(\lambda x)|}_{0\,\le\,\cdot\,\le\,1}\,dx \le$$

$$\le \sum|g(x_i)|\cdot\frac{2}{\lambda} + \sum\int_{a_i}^{a_{i+1}}|g(x) - g(x_i)|\cdot 1 \qquad \text{si stima} \quad \int_{a_i}^{a_{i+1}}|g(x) - g(x_i)| < \varepsilon\cdot(a_{i+1} - a_i)$$

$g$ è continua su $[\tilde a, \tilde b] \Rightarrow g$ è limitata e uniformemente continua:

$$\forall \varepsilon > 0 \;\; \exists \delta > 0 \;\; \text{t.c. se } x_1, x_2 \in [\tilde a, \tilde b] \text{ si ha } |x_2 - x_1| < \delta \Rightarrow |g(x_2) - g(x_1)| < \varepsilon$$

$$\frac{\tilde b - \tilde a}{n} < \delta \;\to\; n > \frac{\tilde b - \tilde a}{\delta}$$

quindi se $x, x' \in [a_i, a_{i+1}]$ si ha $|x' - x| < \delta \Rightarrow |g(x') - g(x)| < \varepsilon$

$$\le \sum|g(x_i)|\cdot\frac{2}{\lambda} + \sum\int_{a_i}^{a_{i+1}}\varepsilon\,dx \le$$

$$\le \sum M\cdot\frac{2}{\lambda} + \sum\varepsilon\cdot[a_{i+1} - a_i] \le M\cdot\frac{2}{\lambda}\sum 1 + \varepsilon\cdot\frac{\tilde b - \tilde a}{n}\sum 1 \le$$

$$\le M\cdot\frac{2}{\lambda}\cdot n + \varepsilon\cdot\frac{\tilde b - \tilde a}{n}\cdot n \le \frac{2nM}{\lambda} + \varepsilon\cdot(\tilde b - \tilde a)$$

> [!note] Costante $M$
> $M = \sup_{[\tilde a, \tilde b]}|g|$, finito perché $g$ è continua su un compatto.

Ora mostro

$$\lim_{\lambda\to+\infty}\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x)\,dx = 0$$

$$\forall \tilde\varepsilon > 0 \;\; \exists \Lambda > 0 \;\; \text{t.c.} \;\; \forall \lambda > \Lambda \Rightarrow \left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x)\,dx\right| \le \tilde\varepsilon$$

Definito $\varepsilon \in \left(0, \dfrac{\tilde\varepsilon}{2(\tilde b - \tilde a)}\right)$ e $\tilde\Lambda > \dfrac{4nM}{\tilde\varepsilon}$

$$\left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x)\,dx\right| \le \frac{2nM}{\lambda} + \varepsilon(\tilde b - \tilde a) \le$$

$$\le 2nM\cdot\frac{\tilde\varepsilon}{4nM} + \frac{\tilde\varepsilon}{2(\tilde b - \tilde a)}\cdot(\tilde b - \tilde a) \le$$

$$\le \frac{\tilde\varepsilon}{2} + \frac{\tilde\varepsilon}{2} = \tilde\varepsilon = 0$$

$$\left|\int_{\tilde a}^{\tilde b} g(x)\cdot\sin(\lambda x)\,dx\right| \le \tilde\varepsilon = 0 \qquad \square$$

> [!warning] Conclusione
> La scrittura "$\tilde\varepsilon = 0$" è impropria. La conclusione corretta è: poiché la stima $\le \tilde\varepsilon$ vale per ogni $\tilde\varepsilon > 0$ e ogni $\lambda > \tilde\Lambda$, il limite è $0$. Si noti che $n$ dipende da $\varepsilon$ tramite $\delta$: va fissato prima di scegliere $\tilde\Lambda$.

> [!note] Estensione al caso a tratti e al coseno
> Per $g$ continua a tratti si applica il risultato a ciascuno dei finiti intervalli di continuità e si sommano i contributi. Per il coseno l'argomento è identico, con $\left[\frac{\sin(\lambda x)}{\lambda}\right]$ come primitiva.
