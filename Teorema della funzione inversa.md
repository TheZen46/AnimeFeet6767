$f:D\subset\R^n\to\R^n$
- $\hx\text{ interno a }D$
- $f\in C^1(D)$
- $J_\hx^f=d_\hx f\m{30}\det J_\hx f\ne0$}
$\Rightarrow\ \exists\ N\text{ intorno di }\hx\text{ t.c. }f\text{ ristretta a }N\text{ è invertibile}\qquad N\subset D$

# Dimostrazione
$\det J_\hx^f\ne0\Rightarrow J_\hx^f\text{ è invertibile}$

$\text{Indichiamo con}({J_\hx^f})^{-1}\text{ la matrice inversa}$

$\displaystyle \Bigl\Vert ({J_\hx^f})^{-1}\Bigr\Vert=\sup\limits_{z\ne0}\left|\ ({J_\hx^f})^{-1}\frac{z}{|z|}\right|=\frac1r$
Funzione ausiliaria
$g(x)=f(x)-{J_\hx^f}(x)$
$g(x)-g(y)=f(x)-f(y)-{J_\hx^f}(x-y)$

Diseguaglianza triangolare
$\Bigl|\ f(x)-f(y)-\bigl(g(x)-g(y)\bigr)\Bigr|=\left|J_\hx^f(x-y)\right|$
$\Bigl|\ f(x)-f(y)\Bigr|+\Bigl|\bigl(g(x)-g(y)\bigr)\Bigr|\ge\left|J_\hx^f(x-y)\right|$
$\abs{({J_\hx^f})^{-1}\ J_\hx f(x-y)}=\abs{x-y}$
$\norm{(J_\hx f)^{-1}}\abs{J_\hx^f(x-y)}\ge\abs{x-y}$
$\displaystyle \abs{J_\hx f(x-y)}\ge\frac{1}{\norm{(J_\hx f)^{-1}}}\abs{x-y}\ge r\abs{x-y}$
$\abs{f(x)-f(y)}+\abs{g(x)-g(y)}\ge r\abs{x-y}$
$\abs{f(x)-f(y)}\ge r\abs{x-y}-\abs{g(x)-g(y)}$

Dal teorema della stima applicato a $g$
$\forall\epsilon\quad\exists\ \delta_\epsilon\text{ t.c. }N=B(\hx,\deleps)$
$\forall\ x,y\in N\m{30}\abs{g(x)-g(y)}<$