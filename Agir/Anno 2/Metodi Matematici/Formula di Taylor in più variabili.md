$f:D\subset\mathbb R^n\to\mathbb R$
$f(x)=f(\hat x)+d_{\hat x}f(x-\hat x)+o\bigl(|x-\hat x\bigr)$
Cerchiamo polinomio di ordine $K$ che approssimi $f(x)$ per $x$ vicino a $\hat x$

# Teorema
$f:D\subset\mathbb R^n\to\mathbb R$
Punti $x,\ \hat x$ e consideriamo $S(\hat x,x)$
$\exists\ U\text{ aperto}\mskip{12mu}U\subset D\mskip{12mu} S(\hat x,x)\subset U$
$f\in C^K(U)$
$f(x)=f(\hat x)+P_K(\hat x,x)+R$
	$\displaystyle P_K(\hat x)=\sum\limits_{p_0}^K\sum\limits_{\mathcal I}\frac{1}{i_1!\ldots i_n!}{\partial_1}^{i_1}f(\hat x)$
		$\mathcal I=\bigl\{i_1,\ldots,i_n\bigr\}$
Ho smesso di scrivere perché la notazione era incomprensibile

## Esempio
$f:\mathbb R^2\to\mathbb R$
$f(x,y)=e^{x-y}(\sin x+1)$
Maclaurin di ordine $2$
$f(0,0)=1$
$\displaystyle \frac{\partial f}{\partial x}(x,y)=e^{x-y}(\sin x+1+\cos x)\mskip{36mu}\frac{\partial f}{\partial x}(0,0)=2$
$\displaystyle \frac{\partial f}{\partial y}(x,y)=-e^{x-y}(\sin x+1\cos x)\mskip{36mu}\frac{\partial f}{\partial y}(0,0)=2$

$\displaystyle \frac{\partial^2 f}{\partial x^2}=e^{x-y}(\cos x+\cancel{\sin x} +1-\cancel{\sin x}+\cos x)\mskip{36mu}\frac{\partial f^2}{\partial x^2}(0,0)=3$
$\displaystyle \frac{\partial^2 f}{\partial y^2}=e^{x-y}(\sin x+1)\mskip{36mu}\frac{\partial f^2}{\partial y^2}(0,0)=1$
$\displaystyle \frac{\partial^2 f}{\partial x\partial y}=-e^{x-y}(\sin x+1)\mskip{36mu}\frac{\partial f^2}{\partial x\partial y}(0,0)=-1$

$P_2(x,y)=f(0,0)+\frac{\partial f}{\partial x}(0,0)$