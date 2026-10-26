# Divergenza in 2D

Sia $D$ un dominio regolare e $\partial D$ una curva regolare a tratti con $\bar D = D \cup \partial D$.

Sia $F : \bar D \subset \mathbb{R}^2 \to \mathbb{R}^2$ di classe $C^1_{(\bar D)}$ un campo vettoriale.

Allora

$$\iint_{\bar D} \nabla F\,dx\,dy = \int_{\partial D} F\cdot\underline{n}\,ds \qquad \underline{n} \text{ il vettore normale al bordo}$$

> [!note] Notazione
> $\nabla F$ indica la **divergenza** $\nabla\cdot F = \partial_x F_1 + \partial_y F_2$. Il teorema afferma che l'integrale della divergenza sul dominio è uguale al flusso uscente del campo attraverso il bordo; $\underline n$ è la normale uscente unitaria.

### Dimostrazione

$$\iint_{\bar D} \nabla F\,dx\,dy = \iint_{\bar D} \partial_x F_1 + \partial_y F_2\,dx\,dy$$

Introduco $G : \bar D \subset \mathbb{R}^2 \to \mathbb{R}^2$ con $G = (G_1, G_2) = (-F_2, F_1)$

$$\iint_{\bar D} \partial_x F_1 + \partial_y F_2\,dx\,dy = \iint_{\bar D} \partial_x G_2 - \partial_y G_1\,dx\,dy = \int_{\partial D} G\,dP \qquad \text{Gauss-Green}$$

$$s : [a,b] \to \partial D \qquad \varphi : s \to (x(s), y(s))$$

$\varphi'(s) = (x'(s), y'(s)) = \hat t$ il versore tangente al bordo

$\underline n = R_0^{\pi/2}(\hat t)$ lo stesso vettore ma ruotato, $\underline n = (y'(s), -x'(s))$

> [!warning] Verso della rotazione
> $(y', -x')$ si ottiene ruotando $\hat t$ di $\pi/2$ in senso **orario** (cioè di $-\pi/2$). Con il bordo percorso in verso antiorario è questa la normale uscente. Inoltre, perché $\hat t$ sia un versore, $s$ deve essere l'ascissa curvilinea ($|\varphi'(s)| = 1$).

> [!info] Figura
> Tratto del bordo $\partial D$ con, in un punto, il versore tangente $\hat t$ e il versore normale $\underline n$, ortogonale a $\hat t$ e rivolto verso l'esterno.
> ```tikz
> \begin{document}
> \begin{tikzpicture}[scale=1.4]
> \draw[thick] (0,0.3) .. controls (1.2,0.4) and (1.8,0.7) .. (2.2,2);
> \draw[->,thick] (1.9,1.0) -- (2.3,2.0) node[above] {$\hat t$};
> \draw[->,thick] (1.9,1.0) -- (2.9,0.6) node[right] {$\underline{n}$};
> \end{tikzpicture}
> \end{document}
> ```

$$\iint_{\bar D} \nabla F\,dx\,dy = \int_{\partial D} G\,dP = \int_a^b G(\varphi(s))\cdot\varphi'(s)\,ds =$$

$$= \int_a^b G_1\cdot\frac{dx}{ds} + G_2\cdot\frac{dy}{ds}\,ds =$$

$$= \int_a^b -F_2\cdot x'(s) + F_1\cdot y'(s)\,ds =$$

$$= \int_a^b (F_1, F_2)\cdot(y'(s), -x'(s))\,ds = \int_{\partial D} F\cdot\underline n\,ds \qquad \square$$
