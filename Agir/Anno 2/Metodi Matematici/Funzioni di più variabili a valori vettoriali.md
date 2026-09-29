$f:D\subset\mathbb R^n\to\mathbb R^m$
$\lim\limits_{x\to\hat x}f(x)=i\iff\lim\limits_{x\to\hat x}f_i(x)=l_i\ \ \forall\ i\in\{1,\ldots,n\}$

# Derivate direzionali
$\vec v\ne 0$
$\displaystyle \frac{\partial f}{\partial \vec v}(\hat x)=\lim\limits_{t\to0}\frac{f(\hat x+t\vec v)-f(\hat x)}{t}=\left(\frac{\partial f_1}{\partial \vec v}(\hat x),\ldots,\frac{\partial f_m} {\partial \vec v}(\hat x)\right)$

## Definizione
$f:D\subset\mathbb R^n\to\mathbb R^m$
$\hat x$ punto interno a $D$
Si dice che $f$ è differenziabile in $\hat x$ se $\exists\ \phi:\mathbb R^n\to\mathbb R^m$ lineare tale che $f(x)-f(\hat x)=\phi(x-\hat x)+o(\Vert\vec x-\hat{\vec x}\Vert)$
$\displaystyle \lim\limits_{x\to\hat x}\frac{o(\Vert\vec x-\hat{\vec x}\Vert)}{\Vert\vec x-\hat{\vec x}\Vert)}=0$

$\phi\vec h= d_{\hat x}f\vec h$
$\vec h\in\mathbb R^n$ lineare

$\left.\overbrace{\begin{pmatrix}&&&&\\&&&&\\&&&&\end{pmatrix}}^{n}\right\}m$

La matrice che descrive $d_{\hat x}f$ è detta Jacobiana
$\displaystyle J_{\hat x}f=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\frac{\partial f_1}{\partial x_2}&&\frac{\partial f_1}{\partial x_n}\\\frac{\partial f_2}{\partial x_1}&\frac{\partial f_2}{\partial x_2}&&\frac{\partial f_2}{\partial x_n}\\\\\frac{\partial f_m}{\partial x_1}&\frac{\partial f_m}{\partial x_2}&&\frac{\partial f_m}{\partial x_n}\end{pmatrix}$

$j-\text{esima riga di }J{\hat x}f\text{ è }\nabla_{\hat x}f_j$
$k-\text{esima riga di }J{\hat x}f\text{ è }\frac{\partial \vec f}{\partial x_k}$

Regola derivazione funzioni composte
$g: D \subset \mathbb R^n \to \mathbb R^m$
$f: D' \subset \mathbb R^m \to \mathbb R^k$
$D \subset \mathbb R^n \Rightarrow g(D) \subset D' \subset \mathbb R^m$
$D' \subset \mathbb R^m \overset{f}{\Longrightarrow} \mathbb R^k$

$g(D)\subset D'$

Ha senso calcolare $f(g(x))\ \ \forall x\in D$
$f\circ g$ composizione

Teorema (catena)
$g: D \subset \mathbb R^n \to \mathbb R^m$
$f: D' \subset \mathbb R^m \to \mathbb R^k$

Se $g$ è differenziabile in $\hat x$ ed $f$ differenziabile in $\hat y=g(\hat x)\Rightarrow f\circ g$ è differenziabile in $\hat x$
$d_{\hat x}(f\circ g)=d_{g(\hat x)}\circ d_{\hat x}g$
ovvero
$\displaystyle f\big(g(x)\big)-f\big(g(\hat x)\big)=\sum\limits_j \sum\limits_k\frac{\partial f_{\big(y(\hat x)\big)}}{\partial y_j}\frac{\partial g_{j(\hat x)}}{\partial x_k}-(x-\hat x)_k)+o(\Vert x-\hat x\Vert)$
