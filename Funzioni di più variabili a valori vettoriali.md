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
