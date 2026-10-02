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

$\Delta(h,k)=f(\hat x+h,\hat y+k)-f(\hat +h,\hat y)-f(\hat x,\hat y+k)+f(\hat x,\hat y)$
$\displaystyle \lim\limits_{\underset{h,k\ne0}{(h,k)\to(0,0)}}\frac{\Delta(h,k)}{hk}\overset?=$

$\varphi(x)=f(\hat x,\hat y+k)-f(\hat x,\hat y)\mskip{36mu}\varphi:I_x\to\mathbb R$

$\varphi(\hat x+h)-\phi(\hat x)=\Delta(h,k)$
$\displaystyle \varphi\text{ `e continua e derivabile in }I\Rightarrow\text{Teorema di Lagrange }(\exists\ a\in(\hat x,\hat x+k))\text{ dove }\varphi(\hat x+h)-\phi(\hat x)=\varphi'(a)\frac{\partial f}{\partial x}(a,\hat y+k)-\frac{\partial f}{\partial x}(a,\hat y)$
$\displaystyle \Delta(h,k)=\frac{\partial f}{\partial x}(a,\hat y+k)-\frac{\partial f}{\partial x}(a,\hat y)\mskip{60mu}y\mapsto\frac{\partial f}{\partial x}(a,y)$
