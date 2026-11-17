$A\text{ aperto di }\mathbb R^n$
$f:A\subset\mathbb R^n\to\mathbb R$
$f\in C^2(A)$

(Ammette tutte le derivate parziali fino ad ordine 2 e sono continue)

# Teorema
Se le funzioni sono di classe $\displaystyle C^2\Rightarrow\frac{\partial^2f(x)}{\partial x_i\partial x_j}=\frac{\partial^2f(x)}{\partial x_j\partial x_i}$

## Dimostrazione
### Caso bidimensionale
$f(x,y)$
$(\hat x,\hat y)\text{ ed }(x,y)$
$\begin{cases}x=\hat x+h\\y=\hat y+k\end{cases}$

$\Delta(h,k)=f(\hat x+h,\hat y+k)-f(\hat h,\hat y)-f(\hat x,\hat y+k)+f(\hat x,\hat y)$
$\displaystyle \lim\limits_{\underset{h,k\ne0}{(h,k)\to(0,0)}}\frac{\Delta(h,k)}{hk}\overset?=$

$\varphi(x)=f(\hat x,\hat y+k)-f(x,\hat y)\mskip{36mu}\varphi:I_x\to\mathbb R$

$\varphi(\hat x+h)-\phi(\hat x)=\Delta(h,k)$
$\displaystyle \varphi\text{ è continua e derivabile in }I\Rightarrow\text{Teorema di Lagrange }(\exists\ a\in(\hat x,\hat x+k))\text{ dove }\varphi(\hat x+h)-\phi(\hat x)=\varphi'(a)\frac{\partial f}{\partial x}(a,\hat y+k)-\frac{\partial f}{\partial x}(a,\hat y)$
$\displaystyle \Delta(h,k)=\frac{\partial f}{\partial x}(a,\hat y+k)-\frac{\partial f}{\partial x}(a,\hat y)\mskip{60mu}y\mapsto\frac{\partial f}{\partial x}(a,y)\Leftarrow\text{soddisfa le ipotesi del teorema di Lagrange sull'intervallo }[\hat y,\hat y+k]\Rightarrow\exists b\in(\hat y,\hat y+k)\mskip{24mu}\Delta(h,k)=\frac{\partial}{\partial y}\frac{\partial}{\partial x}f(a,b)hk$
$\displaystyle \lim\limits_{(h,k)\to(0,0)}(a,b)=(\hat x,\hat y)$
Continuità di $\displaystyle \frac{\partial^2f}{\partial y\partial x}$
$\displaystyle \lim\limits_{\underset{h,k\ne0}{(h,k)\to(0,0)}}\frac{\Delta(h,k)}{hk}=\lim\limits_{\underset{h,k\ne0}{(h,k)\to(0,0)}}\frac{\frac{\partial}{\partial y}\frac{\partial}{\partial x}f(a,b)\cancel{hk}}{\cancel{hk}}=\frac{\partial^2}{\partial y\partial x}f(\hat x,\hat y)$


$\psi(x)=f(\hat x+h,\hat y)-f(\hat x,y)\mskip{36mu}\varphi:I_x\to\mathbb R$

$\varphi(\hat x+h)-\phi(\hat x)=\Delta(h,k)$
$\Delta(h,k)=\psi(\hat y+k)-\psi(\hat y)$
Ripetendo l'analisi precedentemente discussa $\displaystyle \lim\limits_{(h,k)\to(0,0)}(a,b)=\frac{\Delta(h,k)}{hk}=\frac{\partial^2}{\partial x\partial y}f(\hat x,\hat y)$
Per l' unicità del limite le derivate possono essere scambiate le derivate


## Esercizi
1) $\displaystyle f(x,y)=x^2e^{x-y}\sin(y^{-1})\mskip{30mu}D=\Bigl\{(x,y)\in\mathbb R^2,\ y\ne0\Bigr\}$
$\displaystyle \frac{\partial f}{\partial x}=2xe^{x-y}\sin(y^{-1})+x^2e^{x-y}\sin(y^{-1})$
$\displaystyle \frac{\partial f}{\partial y}=x^2e^{x-y}\bigl(-\sin(y^{-1})\cos(y^{-1})y^{-2}\bigr)$

$\displaystyle \frac{\partial^2 f}{\partial x\partial y}=\frac{\partial }{\partial y}(2x+x^2)e^{x-y}\sin(y^{-1})=(2x+x^2)(e^{x-y})\bigl(-\sin(y^{-1})\cos(y^{-1})y^{-2}\bigr)$

2) Derivazione di funzioni composte
$\begin{array}{l}f:\mathbb R^2\to\mathbb R&g:D\to\mathbb R^2\\&D=\Bigl\{(r,\theta)\in\mathbb R^2,r>0\\\displaystyle f(x,y)=e^{x^2+y^2}\ x&g(r,\theta)=\bigl(r\cos\theta,r\sin\theta\bigr)\end{array}$

$f\circ g:D\to\mathbb R$
$\displaystyle f\circ g(r,\theta)=f\bigl(g(r,\theta)\bigr)=e^{e^2}\ r\cos\theta$

$\displaystyle \frac{\partial f\circ g}{\partial r}=\frac{\partial f}{\partial x}\frac{\partial g_1}{\partial r}+\frac{\partial f}{\partial y}\frac{\partial g_1}{\partial r}=e^{x^2+y^2}(2x\ x+1)\cos\theta+e^{x^2+y^2}(2y x)\sin\theta$
$\displaystyle \frac{\partial f\circ g}{\partial r}=e^{r^2}\ (2r^2\cos^2\theta+1)\cos\theta+e^{r^2}\ (2r^2\sin^2\theta)\sin\theta=e^{r^2}\ (2r^2+1)\cos\theta$

Altro modo
$\displaystyle \frac{\partial f\circ g}{\partial r}=\frac{\partial}{\partial r}=\Bigr(e^{e^2}\ r\cos\theta\Bigl)=e^{r^2}\ (2r^2+1)\cos\theta$

