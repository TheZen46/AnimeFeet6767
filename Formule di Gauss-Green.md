$D\subset\R^2$
Se $D=\bigl\{(x,y)\ |\ x\in[a,b],\ \alpha(x)\le y\le \beta(x)\bigr\}\qquad \alpha,\beta\in C^1\bigl([a,b]\bigr)$

$\partial D=\gamma_1\cup\gamma_2\cup\gamma_3\cup\gamma_4\text{ regolare a tratti}$
($\gamma$ è il contorno del poligono, $\vec t$ è il vettore della curva in un certo punto, $\vec n$ il versore ($\perp\vec t$))

# Teorema di Green
$F:A\subset\R^2\to\R^2$
$F\in C^1(A)$
$D$ regolare
$\overline D\subset A$

$\array{D\ \text{aperto}\\\overline D\ \text{limitato}\\\overline D\subset A\\\partial D\text{ è regolare a tratti}}$

$F=(f_1,f_2)$
$f_1\in C^1(A)$
$f_2\in C^1(A)$
$dP=(dx,dy)$
$\displaystyle \iint_D\bigl(\frac{\partial f_2}{\partial x}-\frac{\partial f_1}{\partial y}\bigr)dxdy=\oint_{\partial D^+}F\cdot\ dP$
(l'integrale di un area è uguale all'integrale di linea)


## Dimostrazione
$D$ dominio normale rispetto a $x$