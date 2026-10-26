# Seno cardinale

$$\operatorname{sinc}(x) : \mathbb{R} \to \mathbb{R} \qquad f(x) = \begin{cases}\dfrac{\sin(x)}{x}, & x \neq 0 \\[2mm] 1, & x = 0\end{cases} \quad \Rightarrow \quad \int_{-\infty}^{+\infty}\operatorname{sinc}(x)\,dx = \pi$$

$$\int_{-\infty}^{+\infty}\operatorname{sinc}(x)\,dx = \lim_{\substack{R\to+\infty \\ \varepsilon\to 0^+}}\int_{[-R,R]\setminus[-\varepsilon,\varepsilon]}\frac{\sin(x)}{x}\,dx =$$

$$= \lim\int\frac{e^{ix} - e^{-ix}}{2ix}\,dx =$$

$$= \frac{1}{2i}\left(\lim\int e^{ix}\cdot\frac{1}{x}\,dx + \lim\int e^{-ix}\cdot\left(-\frac{1}{x}\right)dx\right)$$

$$y = -x \qquad dy = -dx$$

$$= \frac{1}{2i}\left(\lim\int e^{ix}\cdot\frac{1}{x}\,dx + \lim\int e^{-i(-y)}\cdot\left(-\frac{1}{-y}\right)\cdot(-1)\,dy\right)$$

$$= \frac{1}{i}\cdot\lim\int e^{ix}\cdot\frac{1}{x}\,dx$$

$$= \frac{1}{i}\cdot\pi i = \pi$$

> [!note] Passaggi chiave
> L'esclusione di $[-\varepsilon, \varepsilon]$ serve a separare $\sin x / x$ in due termini singolari in $0$. La sostituzione $y = -x$ lascia invariato il dominio simmetrico $[-R,R]\setminus[-\varepsilon,\varepsilon]$, quindi il secondo integrale coincide con il primo e si ottiene il fattore $2$. Il valore $\lim\int e^{ix}/x\,dx = i\pi$ (valore principale) si ricava con il teorema dei residui su un cammino formato dal segmento, da una semicirconferenza piccola attorno a $0$ (che contribuisce con $-i\pi\operatorname{Res}(e^{iz}/z, 0) = -i\pi$) e da una semicirconferenza grande, il cui contributo si annulla per il lemma di Jordan.
