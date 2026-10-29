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

$Y(s)=c\bigl(sI-A\bigr)^{-1}x(0^-)+\Bigl[C\bigl(sI-A\bigr)\Bigr]$