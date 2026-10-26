# Teorema di Stokes in 2D

Sia $D \subset \mathbb{R}^2$.

Considero $f : D\times[-\varepsilon, \varepsilon] \subset \mathbb{R}^3 \to \mathbb{R}^3$ di classe $C^1$, $\quad \tilde D = D\times\{0\}$

Allora

$$\iint_D (\nabla\wedge f)\cdot e_3\,dx\,dy = \int_{\partial D} f(\cdot, 0)\,dP$$

> [!note] Significato
> $D$ viene immerso nel piano $z = 0$ di $\mathbb{R}^3$. Il flusso del rotore di $f$ attraverso $\tilde D$ (con normale $e_3$) è uguale alla circuitazione di $f$ lungo il bordo. È la versione piana del teorema di Stokes e coincide con Gauss-Green.

### Dimostrazione

Espando il rotore

$$\nabla\wedge f = (\partial_2 f_3 - \partial_3 f_2,\;\; \partial_3 f_1 - \partial_1 f_3,\;\; \partial_1 f_2 - \partial_2 f_1)$$

$$(\nabla\wedge f)\cdot e_3 = \partial_1 f_2 - \partial_2 f_1$$

Impongo una restrizione $z = 0$:

$$\iint_D \partial_1 f_2(x,y,0) - \partial_2 f_1(x,y,0)\,dx\,dy$$

Applico G.G.

$$\iint_D \partial_1 f_2 - \partial_2 f_1\,dx\,dy = \int_{\partial D} f_1\,dx + f_2\,dy$$

Per definizione

$$\int_{\partial D} f_1\,dx + f_2\,dy = \int_{\partial D} f(\cdot, 0)\,dP \qquad \square$$

> [!note] Terza componente
> Lungo $\partial D$, che giace nel piano $z = 0$, si ha $dz = 0$: la componente $f_3$ non contribuisce all'integrale di linea.
