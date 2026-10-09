$f:D\subset\mathbb R^n\to\mathbb R^m$
$\hat x\in \dot D$
Se $f$ è differenziabile in $\hat x$
$J=d_{\hat x}f$
$J_{\hat x_{ij}}=\overbrace{\begin{pmatrix}&&&&\\&&&&\\&&&&\end{pmatrix}}^{m}\left.\array{\\\\\\}\right\}n$

$J_{\hat x}$ è una matrice $m\times n$
$J_\hat x:\mathbb R^n\to\mathbb R^m$
$v\in\mathbb R^n$
$J_{\hat x}v\in\mathbb R^m\quad\bigl(J_{\hat x}v\bigr)_i\in\mathbb R\quad i\in\{1,\ldots,m\}$
$f(x)-f(\hat x)=J_{\hat x}(x-\hat x)+o\bigl(|x-\hat x|\bigr)$
$\lim\limits_{x\to\hat x}\frac{o\bigl(|x-\hat x|\bigr)}{|x-\hat x|}=0$

# Teorema della stima
$f:D\subset\mathbb R^n\to\mathbb R^m$
Differenziabile con continuità in un intorno $B$ di $\hat x\in D$
$f\in C^1(B)$
$\Rightarrow\forall\epsilon>0 \exists\delta_\epsilon\text{ t.c. }\forall\ x,y\in B(x_0,\delta_\epsilon)\quad |f(x)-f(y)|<\bigl(\Vert J_{\hat x}\Vert+\epsilon\bigr)|x-y|$
$\displaystyle \Vert J_{\hat x}\Vert=\sup\limits_{\underset{z\ne0}{Z\in\mathbb R^n}}\frac{|J_{\hat x}Z|}{|Z|}$
$J_{\hat x}=d_{\hat x}f$

## Dimostrazione
Consideriamo $g(x)=f(x)-J_{\hat x}x$
$g:B\subset\mathbb R^n\to\mathbb R^m$

$f\text{ è }C^1(B)$
$J_{\hat x}x\text{ è }C^1(B)$
$g(x)\text{ è }C^1$
$\partial _{x_j}g\text{ sono continue}$

$\displaystyle \partial_x g(x)=\partial_{x_j}f(x)-\underbrace{J_{\hat x}e_j}_{\partial_{x_j}f(x)-\partial_{x_j}f(\hat x)}$
$\lim\limits_{x\to\hat x}\partial_x g(x)=0$

$\forall\epsilon\quad\exists\delta_\epsilon\text{ t.c. }x\in B(\hat x,\delta_\epsilon)$
$\displaystyle \bigl|\partial_{x_j}g_i(x)\bigr|<\frac{\epsilon}{\sqrt{mn}}$
$\displaystyle g_i(x)-g_i(y)=\sum\limits_j\partial_{x_j}g_i(\tilde x)(x-y)_j$
$\displaystyle \bigl|g_i(x)-g_i(y)\bigr|^2=\bigl|\sum\limits_{j=1}^n\partial_{x_j}g_i(\tilde x)(x-y)_j\bigr|^2=\bigl|\nabla_{\tilde x}g_i\ (x-y)\bigr|^2\quad \forall\ i\text{ per Cauchy-Schwarz }\le\bigl|\nabla_{\tilde x}g_i\bigr|^2|\bigl|x-y\bigr|^2$
$\displaystyle \bigl|\nabla_{\tilde x}g_i\bigr|^2=\sum\limits_j|\bigl|\partial_{x_j}g_i(\tilde x)\bigr|^2\le\sum\limits_{j=1}^n\frac{\epsilon^2}{mn}=\cancel n\frac{\epsilon^2}{m\cancel n}=\frac{\epsilon^2}{m}$
$\bigl|g_i(x)-g_i(y)\bigr|^2<\frac{\epsilon^2}{m}\bigl|x-y\bigr|$
$\forall\epsilon\ \ \exists\ \delta_\epsilon\text{ t.c. }x\in B(\hat x,\delta_\epsilon)$
	$\bigl|g(x)-g(y)\bigr|^2<\sum\limits_{i=1}^m\frac{\epsilon^2}m\bigl|x-y\bigr|^2$
	$\bigl|g(x)-g(y)\bigr|^2<\epsilon^2\bigl|x-y\bigr|^2$
	$\bigl|g(x)-g(y)\bigr|<\epsilon\bigl|x-y\bigr|$
$f(x)-f(y)=g(x)=J_{\hat x}-g(y)-J_{\hat x}y=$
	$g(x)=f(x)-J_{\hat x}(x)$
$=g(x)-g(y)+J_{\hat x}(x-y)$
$\bigl|f(x)-f(y)\bigr|\le\bigl|g(x)-g(y)\bigr|+\bigl|J_{\hat x}(x-y)\bigr|$

$\bigl|f(x)-f(y)\bigr|<\epsilon\bigl|x-y\bigr|+\bigl|J_{\hat x}(x-y)\bigr|$
$x-y=e|x-y|\qquad |e|=1$
$J_{\hat x}\ e\bigl|x-y\bigr|=\bigl|x-y\bigr|J_{\hat x}e$
$\bigl|J_{\hat x}(x-y)\bigr|=\bigl|x-y\bigr|\bigl|J_{\hat x}e\bigr|\le\bigl|x-y\bigr|\sup\limits_{\underset{z\ne0}{Z\in\mathbb R^n}}\left|\frac{|J_{\hat x}Z|}{|Z|}\right|=\bigl|x-y\bigr|\bigl\Vert J_{\hat x}\bigr\Vert$
$\forall x,y\in B(\hat x,\delta_\epsilon)$
$|f(x)-f(y)|<\bigl(\epsilon+\bigl\Vert J_{\hat x}\bigr\Vert\bigr)\bigl|x-y\bigr|$