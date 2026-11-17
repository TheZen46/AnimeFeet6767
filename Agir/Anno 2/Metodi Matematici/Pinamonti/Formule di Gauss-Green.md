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
$\displaystyle \iint_D\bigl(\frac{\partial f_2}{\partial x}-\frac{\partial f_1}{\partial y}\bigr)dxdy=\int_{\partial D}F\cdot\ dP\text{ antiorario}$
(l'integrale di un area è uguale all'integrale di linea)


## Dimostrazione
$D$ dominio normale rispetto a $x$
$D=\bigl\{(x,y)\ |\ x\in[a,b],\ \alpha(x)\le y\le \beta(x)\bigr\}\qquad \alpha,\beta\in C^1\bigl([a,b]\bigr)$

$\ds\int_{\partial D}F\cdot\ dP=\int_{\gamma_1}F\cdot\ dP+\int_{\gamma_2}F\cdot\ dP+\int_{\gamma_3\cup\gamma_4}F\cdot\ dP$

$\array{\Large\gamma_1\normalsize(x)=\bigl(x,\alpha(x)\bigr)&x\in[a,b]\\\Large\gamma_2\normalsize(x)=(b,y)&x\in\bigl[\alpha(b),\beta(b)\bigr]\\\Large\gamma_3\normalsize(x)=\bigl(x,\beta(x)\bigr)&x\in[a,b]\\\Large\gamma_4\normalsize(y)=(a,y)&y\in\bigl[\alpha(a),\beta(a)\bigr]}$
$\displaystyle \int_{\gamma_1}F\cdot\ dP=\int_a^b\Bigl(f_1\bigl(x,\alpha(x)\bigr),f_2\bigl(x,\alpha(x)\bigr)\Bigr)\cdot\gamma_1'(x)dx$

$\array{\Large\gamma_1\normalsize'(x)=\bigl(1,\alpha'(x)\bigr)\\\Large\gamma_2\normalsize'(x)=\bigl(0,1\bigr)\\\Large\gamma_3\normalsize'(x)=\bigl(1,\beta'(x)\bigr)\\\Large\gamma_4\normalsize'(x)=\bigl(0,1\bigr)}$

$\bigl(f_1,f_2\bigr)\cdot\bigl(v_1,v_2\bigr)=f_1v_1+f_2v_2$

$\displaystyle \int_{\partial D}F\cdot dP=\underbrace{\int_a^b f_1\bigl(x,\alpha(x)\bigr)dx+\int_a^b f_2\bigl(x,\alpha(x)\bigr)\alpha'(x)dx}_{\Large{\gamma_1}}+\underbrace{\int_{\alpha(x)}^{\beta(x)} f_2\bigl(b,y\bigr)dy}_{\Large{\gamma_2}}-\underbrace{\int_a^b f_1\bigl(x,\beta(x)\bigr)dx-\int_a^b f_2\bigl(x,\beta(x)\bigr)\beta'(x)dx}_{\Large{\gamma_3}}-\underbrace{\int_{\alpha(x)}^{\beta(x)} f_2\bigl(a,y\bigr)dy}_{\Large{\gamma_4}}$
