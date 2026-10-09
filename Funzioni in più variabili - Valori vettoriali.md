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
