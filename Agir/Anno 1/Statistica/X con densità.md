$f_X(x)=\cases{0&x<0\\2x&0<x<1\\0&x>1}$

$Y=-3X+1=\varphi(X)$
$y=\varphi(x)=-3x+1$

$0\le X\le 1\Rightarrow -2\le Y\le 1$

$f(x)=\cases{0&y<-2\\&-2<y<1\\0&y>1}$

$F_Y(y)=\mathbb P[Y\le y]$
$f_y(y)=F_Y'(y)$
$F_Y(y)=\mathbb P[-3X+1\le y]$

$\varphi(x)=-3X+1\le y$

$\cases{y=\varphi(x)\\\varphi(x)\le y}$

$\varphi(x)=y\iff -3x+1=y$
$1-y=3x\Rightarrow x=\frac{1-y}3$

$F_Y(y)=\mathbb P[x\ge\frac{1-y}3]=\mathbb P[-3x\le y-1]=\mathbb P[X\ge\frac{y-1}{-3}]=\mathbb P[x\ge\frac{1-y}3]=1-\frac12\underbrace{\left(\frac{1-y}3\right)}_{\text{base}}2\left(\frac{1-y}3\right)=1-\left(\frac{1-y}3\right)^2\quad=\quad1-\mathbb P[X<\frac{1-y}3]=1-\mathbb P 1-\mathbb P[x\le\frac{1-y}3]$
$-2\le y\le 1\qquad x=\frac{1-y}3\quad0\ge x\ge1$
$=\int_{\frac{1-y}3}^{+\infty}\underset X{f(x)}dx=$

$F_Y(y)=1-\left(\frac{1-y}3\right)^2=1-\frac{1-2y+y^2}9=\frac89+\frac29y-\frac19y^2$

$F_Y(2)=\frac89-\frac49-\frac49=0\checkmark$
$F_Y(1)=\frac89+\frac29-\frac29=\frac99=1\checkmark$

$f_Y(y)=F_Y'(y)=(\frac89+\frac29y+\frac19y^2)'=\frac29-\frac29y=\frac29(1-y)\quad -2<y<1$

$f_Y(y)=\cases{0&y<-2\\\frac29(1-y)&-2<y<1\\0&y>1}$
$F_Y(y)=\mathbb P[X\ge\frac{1-y}3]=1-\mathbb P[X\le\frac{1-y}]3=1-F_X(\frac{1-y}3)$
$f_Y(y)=\left[F_Y(y)\right]'=\left[1-F_X(\frac{1-y}3)\right]'=-\left[F_X(\frac{1-y}3)\right]'$

$\left[y(h(x))\right]$ Derivata di funzione composta $=g'(h(x))\cdot h'(x)$

$f_Y(y)=F-_X'\left(\frac{1-y}3\right)\qquad\left(\frac{1-y}3\right)=-f_X\left(\frac{1-y}3\right)\frac{0-1}3=\frac13$


## Esercizio
$X$ ha densità
$f_X(x)=\cases{0&x<0\\1&0<x<1\\0&x>1}$

$Y=(3x-1)^2$

$0\le X\le 1$

$\varphi(x)=(3x-1)^2$=y
$0\le X\le 1\Rightarrow0\le Y\le 4$

$f_Y(y)=\cases{0&y<0\\&0<y<4\\0&y>4}$
$F_Y(y)=\mathbb P[Y\le y]=\mathbb[(3X-1)^2\le y]$

$\varphi(x_1)=\varphi(x_2)=y$
$(3x-1)^2=y$

Caso $0<y<1$
$(3x-1)=\pm\sqrt y$
$x=\frac{1\pm\sqrt y}3\qquad\array{x_1=\frac{1-\sqrt y}3\\x_2=\frac{1+\sqrt y}3}$


## Esercizio
$X$ ha densità $f_X(x)=\cases{\frac12&0<x<2\\0&\text{altrimenti}}$

$Y=\begin{cases}0&x\le 1\\x-1&x>1\end{cases}$

$F_Y$ e $Y$ ammette densità

$y=\varphi(x)=\begin{cases}0&x\le 1\\x-1&x>1\end{cases}$
