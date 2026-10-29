$\dot x=f(x,u)\qquad x\in\R^n\quad u\in\R^m$

$\dot x=Ax+Bu\ \ \boxed\star$
$A\in\R^{n\times n}$
$B\in\R^{n\times m}$

$y=Cx+Du$
$A\in\R^{q\times n}$
$B\in\R^{q\times m}$

$\displaystyle x(t)=e^{At}x(0^-)+\int_{0^-}^t e^{A(t-\tau)}Bu(\tau)d\tau$
$\displaystyle y(t)=ce^{At}x(0^-)+c\int_{0^-}^t e^{A(t-\tau)}Bu(\tau)d\tau+Du(t)$

$\displaystyle e^{At}=\suml_{k=0}^\infty \frac{A^kt^k}{k!}$


$\boxed\star\ \ sX(s)-x(0^-)=AX(s)+BU(s)$
$sIX(s)-AX(s)=x(0^-)+BU(s)$
$\bigl(sI-A\bigr)X(s)=x(0^-)+BU(s)$
$X(s)=\bigl(sI-A\bigr)^{-1}x(0^-)+\bigl(sI-A\bigr)^{-1}BU(s)$

$\bigl(sI-A\bigr)^{-1}=\lt{e^{At}}$

$Y(s)=c\bigl(sI-A\bigr)^{-1}x(0^-)+\underbrace{\Bigl[C\bigl(sI-A\bigr)^{-1}B+D\Bigr]}_{M(s)}U(s)$
$\sqmatrix{Y_1(s)\\Y_2(s)\\\vdots\\Y_q(s)}=\sqmatrix{&\boxed{1,2}&\\\\\\\\}\sqmatrix{U_1(s)\\U_2(s)\\\vdots\\U_m(s)}$
$Y_q(S)=\ldots+\boxed{1,2}U_2(S)+\ldots$


# Esempio
$A=\sqmatrix{0&1\\-1&0}$
$sI-A=\sqmatrix{s&-1\\1&s}$

$\displaystyle M^{-1}=\frac{\operatorname{adj}(M)}{\det(M)}$

$\operatorname{c.alg}(sI-A)=\sqmatrix{s&-1\\1&s}\rightarrow\operatorname{adj}=\sqmatrix{s&1\\-1&s}$
$\displaystyle \sqmatrix{s&1\\-1&s}\frac{1}{s^2+1}$
$\displaystyle \bigl(sI-A\bigr)^{-1}=\sqmatrix{\Large\frac{s}{s^2+1}&\Large\frac{1}{s^2+1}\\\Large\frac{-1}{s^2+1}&\Large\frac{s}{s^2+1}}$

$e^{At}=\sqmatrix{\cos(t)&\sin(t)\\\sin(t)&\cos(t)}$