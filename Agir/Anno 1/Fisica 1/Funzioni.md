```functionplot
---
title: y=c
xLabel: x
yLabel: y
bounds: [-5,5,-5,5]
disableZoom: false
grid: true
---
y=1
```


```functionplot
---
title: y=mx+q
xLabel: x
yLabel: y
bounds: [-5,5,-5,5]
disableZoom: false
grid: true
---
y=2x-1
```
```functionplot
---
title: y=ax^2+bx+c
xLabel: x
yLabel: y
bounds: [-5,5,-5,5]
disableZoom: false
grid: true
---
y=x^2-2x+1
```
```functionplot
---
title: y=sin(x)
xLabel: x
yLabel: y
bounds: [-5,5,-2,2]
disableZoom: false
grid: true
---
y=sin(x)
```
```functionplot
---
title: y=sin(x)
xLabel: x
yLabel: y
bounds: [-5,5,-2,2]
disableZoom: false
grid: true
---
y=cos(x)
```
```functionplot
---
title: y=e^x
xLabel: x
yLabel: y
bounds: [-5,5,-5,5]
disableZoom: false
grid: true
---
y=e^(x)
```
```functionplot
---
title: y=e^(-x)
xLabel: x
yLabel: y
bounds: [-5,5,-5,5]
disableZoom: false
grid: true
---
y=e^(-x)
```

Funzione pari: $f(x)=f(-x)$
Funzione dispari: $f(-x)=-f(x)$

# Derivate
$\frac{df}{dx}$
$f'(x)$
$\frac1{dx}(f)$

Se derivando su tempo: $\overset{\cdot}{f}(t)$

$\frac{df}{dx}=\lim\limits_{h\rightarrow0}\frac{f(x+h)-f(x)}h$

$\frac{d}{dx}(c)=0$
$\frac{d}{dx}(mx+q)=m$
$\frac{d}{dx}(ax^2+bx+c)=2ax+b$
$\frac{d}{dx}(\sin(\alpha x))=\alpha\cos (\alpha x)$
$\frac{d}{dx}(\cos(\alpha x))=-\alpha\sin (\alpha x)$
$\frac{d}{dx}(e^{\alpha x})=e^{\alpha x}$
$\frac{d}{dx}(\alpha f(x)+\beta g(x))=\alpha\frac{d}{dx}f(x)+\beta\frac{d}{dx}g(x)$

$v=\frac{\Delta s}{\Delta t}$
$\Delta s=v\cdot\Delta t$

# Integrale
$A(x_0,x_1)$ area sottesa dalla curva

$\frac{A(x_0,x_1+h)-A(x_0,x_1)}{h}=f(x_1)$

$A(x_0,x_1)=\int\limits_{x_0}^{x_1}f(x)dx$

$\frac{d}{dx_1}A(x_0,x_1)=f(x_1)$

$A(x_0,x_0)=0$

## Esempi

$\int\limits_0^1(3)dx$
$A(0,1)=3$
$\frac d{dx}A(x_1)=3$
$A(x_1)=3x_1+c$

$\int\limits_0^3(4x)dx$
$A(0,3)=\frac{12\cdot3}2=18$

$\frac{df}{dx}=4x$
$f=2x^2+c$


$\int\limits_{x_0}^{x_1}(\alpha f(x)+\beta g(x))=\alpha\int\limits_{x_0}^{x_1}(f(x))dx+\beta\int\limits_{x_0}^{x_1}(g(x))dx$


$\int\limits_{x_0}^{x_1}(c)dx=c(x_1-x_0)$



$\int\limits_{x_0}^{x_1}(mx+q)dx=\left[\frac{mx^2}2+qx\right]_{x_0}^{x_1}=\frac{mx_1^2}2+qx_1-(\frac{mx_0^2}2+qx_0)$

$\int\limits_{x_0}^{x_1}(x^\alpha)dx=\left[\frac1{\alpha+1}x^{\alpha+1}\right]_{x_0}^{x_1}$

$\int\limits_{x_0}^{x_1}(e^{\alpha x})dx=\left[\frac1\alpha e^{\alpha x}\right]_{x_0}^{x_1}$

$\int\limits_{x_0}^{x_1}(\sin(\alpha x))dx=\left[\frac{-\cos(\alpha x)}\alpha\right]_{x_0}^{x_1}$

$\int\limits_{x_0}^{x_1}(\cos(\alpha x))dx=\left[\frac{\sin(\alpha x)}\alpha\right]_{x_0}^{x_1}$


# Equazioni differenziali

$\frac{df(x)}{dx}=0$
$f(x)=c$

$\begin{cases}\frac{df(x)}{dx}=0\\f(0)=3\end{cases}\rightarrow f(x)=3$

$\begin{cases}\frac{df(x)}{dx}=c&\rightarrow&f(x)=cx+q\\f(x_0)=f_0\end{cases}$
$f(x_0)=cx_0+q=f_0$
$q=f_0-cx_0$
$f(x)=cx+f_0-cx_0=c(x-x_0)+f_0$

$\begin{cases}\frac{df}{dx}=\alpha f\\f(0)=1\end{cases}\rightarrow e^{\alpha x}$

$\begin{cases}\frac{d^2f}{dx^2}=0&\rightarrow&y=mx+q\\f(x_0)=x_0\\f'(x_0)=v_0\end{cases}$

$\begin{cases}\frac{d^2f}{dx^2}=c&\rightarrow&f(x)=\frac c2x^2+mx+q\\f(x_0)=f_0\\f'(x_0)=v_0\end{cases}$

$\begin{cases}\frac{d^2f}{dx^2}=-w^2f\\f(x)=c_1\sin(wx)+c_2\cos(wx)\end{cases}$

