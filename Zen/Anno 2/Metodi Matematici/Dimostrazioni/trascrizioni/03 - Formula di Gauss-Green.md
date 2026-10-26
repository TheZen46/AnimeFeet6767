# Formula di Gauss-Green

Per $D \subset \mathbb{R}^2$ con $\partial D$ regolare a tratti e $\bar D = D \cup \partial D$ limitato.

Considero $F : \bar D \subset \mathbb{R}^2 \to \mathbb{R}^2$ un campo vettoriale $F = (F_1, F_2)$.

Per $F \in C^1_{(\bar D)}$ a tratti:

$$\int_{\partial D} F\,dP = \iint_D \partial_x F_2 - \partial_y F_1\,dx\,dy$$

> [!note] Notazione
> $\int_{\partial D} F\,dP$ indica l'integrale di linea (lavoro) del campo lungo il bordo percorso in verso antiorario, cioè $\int_{\partial D} F_1\,dx + F_2\,dy$.

### Dimostrazione

Sia $D$ un dominio normale rispetto alle $x$:

$$D = \{(x,y) \in \mathbb{R}^2 \mid x \in [a,b],\; \alpha(x) \le y \le \beta(x)\}$$

con $\alpha, \beta : [a,b] \to \mathbb{R}$, $\alpha, \beta \in C^1([a,b])$.

> [!info] Figura
> Dominio normale rispetto all'asse $x$: compreso tra $x = a$ e $x = b$, delimitato in basso dal grafico di $\alpha(x)$ e in alto da quello di $\beta(x)$. Il bordo è diviso in quattro tratti percorsi in verso antiorario: $\gamma_1$ (grafico di $\alpha$, verso destra), $\gamma_2$ (segmento verticale in $x = b$, verso l'alto), $\gamma_3$ (grafico di $\beta$, verso sinistra), $\gamma_4$ (segmento verticale in $x = a$, verso il basso).
> ```tikz
> \begin{document}
> \begin{tikzpicture}[scale=1.3]
> \draw[->] (-0.3,0) -- (4,0) node[right] {$x$};
> \draw[->] (0,-0.3) -- (0,3.6) node[above] {$y$};
> \draw[dashed] (1,0) -- (1,1.2);
> \draw[dashed] (3,0) -- (3,0.8);
> \draw (1,0.06) -- (1,-0.06) node[below] {$a$};
> \draw (3,0.06) -- (3,-0.06) node[below] {$b$};
> \draw[thick,yellow] (1,1.2) .. controls (1.8,0.4) and (2.4,1.4) .. (3,0.8);
> \draw[thick,yellow] (1,2.2) .. controls (1.8,2.4) and (2.4,3.4) .. (3,2.8);
> \draw[thick,yellow] (1,1.2) -- (1,2.2);
> \draw[thick,yellow] (3,0.8) -- (3,2.8);
> \node[yellow] at (1.6,0.55) {$\alpha(x)$};
> \node[yellow] at (1.6,2.75) {$\beta(x)$};
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
\gamma_1(x) &= (x, \alpha(x)) & x &\in [a,b] & &\to & \gamma_1'(x) &= (1, \alpha'(x)) \\
\gamma_2(x) &= (b, y) & y &\in [\alpha(b), \beta(b)] & &\to & \gamma_2'(x) &= (0, 1) \\
\gamma_3^-(x) &= (x, \beta(x)) & x &\in [a,b] & &\to & {\gamma_3^-}'(x) &= (1, \beta'(x)) \\
\gamma_4^-(x) &= (a, y) & y &\in [\alpha(a), \beta(a)] & &\to & {\gamma_4^-}'(x) &= (0, 1)
\end{aligned}$$

> [!note] Curve opposte
> $\gamma_3^-$ e $\gamma_4^-$ sono le parametrizzazioni "naturali" (con $x$ e $y$ crescenti) di $\gamma_3$ e $\gamma_4$, che percorrono questi tratti nel verso opposto a quello antiorario. Per questo i rispettivi integrali vanno presi con segno meno.

$$\begin{aligned}
\int_{\partial D} F\,dP = &\int_a^b [F_1(x,\alpha(x)),\, F_2(x,\alpha(x))]\cdot[1, \alpha'(x)]\,dx \;+ && \gamma_1 \\
+ &\int_{\alpha(b)}^{\beta(b)} [F_1(b,y),\, F_2(b,y)]\cdot[0,1]\,dy \;+ && \gamma_2 \\
+ &\int_a^b [F_1(x,\beta(x)),\, F_2(x,\beta(x))]\cdot[1, \beta'(x)]\,dx \;+ && \gamma_3^- \\
+ &\int_{\alpha(a)}^{\beta(a)} [F_1(a,y),\, F_2(a,y)]\cdot[0,1]\,dy && \gamma_4^-
\end{aligned}$$

> [!warning] Segni
> I termini relativi a $\gamma_3^-$ e $\gamma_4^-$ devono comparire con il segno meno. Nella riga successiva i segni sono già corretti.

$$\int_{\partial D} F\,dP = \underbrace{\int_a^b F_1(x,\alpha(x)) - F_1(x,\beta(x))\,dx}_{A} \;+$$

$$+ \underbrace{\underbrace{\int_a^b F_2(x,\alpha(x))\,\alpha'(x)\,dx}_{1} + \underbrace{\int_{\alpha(b)}^{\beta(b)} F_2(b,y)\,dy}_{2} - \underbrace{\int_a^b F_2(x,\beta(x))\,\beta'(x)\,dx}_{3} - \underbrace{\int_{\alpha(a)}^{\beta(a)} F_2(a,y)\,dy}_{4}}_{B}$$

Mi chiedo se $\displaystyle\int_{\partial D} F\,dP = A + B$ ?

$$F_1(x,\alpha(x)) - F_1(x,\beta(x)) = -\int_{\alpha(x)}^{\beta(x)} \partial_y F_1(x,y)\,dy$$

$$A = \int_a^b \int_{\alpha(x)}^{\beta(x)} -\partial_y F(x,y)\,dy\,dx = \iint_D -\partial_y F_1(x,y)\,dx\,dy$$

Introduco

$$\mathcal{E}(x) = \int_{\alpha(x)}^{\beta(x)} F_2(x,y)\,dy$$

$$2 = \mathcal{E}(b) \qquad 4 = -\mathcal{E}(a) \qquad 2 + 4 = \mathcal{E}(b) - \mathcal{E}(a) = \int_a^b \partial_x \mathcal{E}(x)\,dx$$

$$\partial_x \mathcal{E}(x) = \int_{\alpha(x)}^{\beta(x)} \partial_x F_2(x,y)\,dy + F_2(x,\beta(x))\,\beta'(x) - F_2(x,\alpha(x))\,\alpha'(x)$$

> [!note] Derivazione sotto il segno di integrale
> È la regola di Leibniz per un integrale con estremi variabili: si deriva l'integrando e si aggiungono i contributi degli estremi, $F_2$ valutata nell'estremo moltiplicata per la derivata dell'estremo stesso.

$$\Rightarrow \int_a^b \partial_x \mathcal{E}(x)\,dx = \int_a^b\int_{\alpha(x)}^{\beta(x)} \partial_x F_2(x,y)\,dx\,dy + \underbrace{\int_a^b F_2(x,\beta(x))\,\beta'(x)\,dx}_{-3} - \underbrace{\int_a^b F_2(x,\alpha(x))\,\alpha'(x)\,dx}_{-1}$$

$$1 + 2 + 3 + 4 = \iint_D \partial_x F_2(x,y)\,dx\,dy = B$$

$$\int_{\partial D} F\,dP = \iint_D \partial_x F_2 - \partial_y F_1\,dx\,dy = A + B \qquad$$
