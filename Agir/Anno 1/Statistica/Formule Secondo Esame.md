# Esercizio 1
a/b)
$\displaystyle\mathbb P[S_n\ge a]=\sum\limits_{i=a}^{n}{n\choose i}(\mathbb P[E])^{i}(1-\mathbb P[E])^{n-i}$

c)
$E[S_n]=np$
$\operatorname{Var}[S_n]=np(1-p)$

## Teorema del limite centrale
d)
$\displaystyle\mathbb P[S_n\le a]=\mathbb P\left[Z\le\frac{a-E[S_n]}{\operatorname{Var}[S_n]}\right]$
Se non specificato, $Z\sim N(0,1)$

# Esercizio 2
$X\in\{a,b\}\qquad W=\operatorname{Bern}(p)\qquad Y=kh(X)$
a) 
 $f(x)=\begin{cases}\frac{1}{b-a}&a\le x\le b\\0&\text{altrove}\end{cases}$
 $\mathbb E[X]=\frac{a+b}{2}$
 $\operatorname{Var}[X]=\frac{(b-a)^2}{12}$
 
b)
$\mathbb P[c\le X\le d]=\frac{1}{b-a}\max(0,\min(b,d)-\max(a,c))$
$\mathbb P[X=n]=0\quad\text{poiché variabile con densità}$

c)
$\displaystyle\mathbb E[e^{XW}]=\mathbb P\left[{e^{XW}}\vert W=0\right]\cdot\mathbb P\left[W=0\right]+\mathbb P\left[e^{XW}\vert W=1\right]\cdot\mathbb P\left[W=1\right]=1(1-p)+p\int_a^b e^x f(x)dx=\{1-p\}+\left.e^x\right\vert_a^b\frac{p}{b-a}=\{1-p\}+\frac{p(e^b-e^a)}{b-a}$

d)
$\mathbb E[Y]=\mathbb E[kh(X)]=k\cdot f(x)\cdot\int_a^b h(X)dx=kf(x)\ H(X)\left.\right\vert_a^b$

e)
$a\le X\le b\Rightarrow h(a)\le Y\le h(b)\qquad g(y)=\begin{cases}0&y\le h(a)\\0&y\ge h(b)\end{cases}$
$G(y)=P[Y\le y]=\mathbb P[kh(x)\le y]=\mathbb P[X\le h^{-1}\frac yk]=\overbrace{f(x)\cdot h^{-1}\frac yk}^{✘\text{ ma funziona}}$
$g(y)=G'(y)=(h^{-1}\frac yk)=\boxed\star$
$g(y)=\begin{cases}0&y\le h(a)\\\boxed\star&h(a)<y<h(b)\\0&y\ge h(b)\end{cases}$
# Esercizio 
## Media con confidenza
b)
$\text{Confidenza}=\alpha$
$J=[\overline x-S,\ \overline x+S]$
$S=Z_{\frac\alpha2}\frac{\sqrt{p(1-p)}}{\sqrt n}$ oppure $S=t_{n-1,\frac\alpha2}\frac{\sqrt {s^2}}{\sqrt n}$

## Varianza con confidenza
c)
$\text{Confidenza}=\alpha$
$a=\chi^2_{\frac\alpha2,n-1}$
$b=\chi^2_{(1-\frac\alpha2),n-1}$
$\displaystyle J=\left[\frac{s^2}{\frac{a}{n-1}},\ \frac{s^2}{\frac{b}{n-1}}\right]$

d)
$\begin{array}{l}H_0:\ \mu=\mu_0& \mu_0=150g\\H_1:\ mu\ne\mu_0\end{array}$
$\hat t=\frac{|\overline x-\mu_0|}{\frac{s}{\sqrt n}}$

| $\alpha$ | $t_{\alpha,n-1}$ |
| -------- | ---------------- |
| $a\%$    | $b$              |

Accetto $H_0$ se $b>\hat t$
# Ulteriori

## Poisson
$N\sim\operatorname{Poisson}(\lambda)\qquad\mathbb E[N]=\lambda$
$\sigma=\sqrt\lambda$
$z=\frac{k-\lambda}{\sigma}$
$\mathbb P[N\le k]\approx\varphi(z)$


