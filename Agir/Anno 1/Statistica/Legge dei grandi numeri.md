$\begin{array}{l}x_1,x_2,\ldots,x_n,\ldots&\text{indipendenti e identicamente distribuite}\\\mu=\text{media}&\sigma^2=\text{varianza}\end{array}$

LGN
$\displaystyle\frac{x_1+\ldots+x_n}{\underbrace{n}_{\text{frequenza relativa}}}\underset{n\to+\infty}\longrightarrow n=\text{media}=\mathbb P[\text{successo}]$

## Disuguaglianza di Chebyshev
$y=\frac{x_1+\ldots+x_n}n$
$\mathbb P[|\frac{x_1+\ldots+x_n}n-\mu|>\varepsilon]\le\frac{\sigma^2}{n\varepsilon^2}$
$\mathbb E[y]=\mu$
$\operatorname{Var}[Y]=\frac{\sigma^2}n$

$\alpha=\text{Probabilità di essere lontani da }\mu$
$\alpha=\frac{\sigma^2}{n\sigma^2}$
$\varepsilon=\frac{\sigma}{\sqrt\alpha\sqrt n}$
$\underbrace{\mu-\frac{1}{\sqrt\alpha}\cdot\overbrace{\frac{\sigma}{\sqrt n}}^{\overset {n\to+\infty}0}\le\overbrace{\frac{x_1+\ldots+x_n}n}^{\overset{\overset{n\to+\infty}{n}}{\text{frequenza relativa teste}}}\le\overbrace{{\overset{\mathbb P[T]}{\mu}+\frac{1\sigma}{\sqrt\alpha\sqrt n}}}^{\text{dipendenza probabilistica}}}_{\text{regione vicino a }\mu}$ con probabilità $1-\alpha$

# Teorema limite centrale (TLC)
$\displaystyle\lim\limits_{n\to+\infty}\mathbb P\left[\frac{\overbrace{\frac{x_1+\ldots+x_n}{n}-\mu}^{\overset{n\to+\infty}0}}{\underbrace{\sqrt{\frac{\sigma^2}{n}}}_{\underset{\text{velocità di convergenza}}{\text{va a 0 come }\frac{1}{\sqrt n}}}}\right]=\mathbb P[Z\le z]\qquad Z\sim N(0,1)$
$\displaystyle\mathbb P\left[\left|\frac{\frac{x_1+\ldots+x_n}{n}-\mu}{\sqrt{\frac{\sigma^2}n}}\right|le\varepsilon\right]=\underbrace{\mathbb P\left[\frac{\frac{x_1+\ldots+x_n}n-\mu}{\sqrt{\frac{\sigma^2}n}}\le-\varepsilon\right]}_{\underset{n>>1}{\simeq}\mathbb P[Z\le-\varepsilon]+1-\mathbb P[Z\le\varepsilon]}+\mathbb P\left[\frac{\frac{x_1+\ldots+x_n}n-\mu}{\sqrt{\frac{\sigma^2}n}}\ge\varepsilon\right]$

$\underset{n>>1}{\simeq}2\mathbb P[Z\ge\varepsilon]=\alpha$
$\mathbb P[Z>\varepsilon]=\frac\alpha2$
$\displaystyle-Z_\frac{\alpha}{2}\ge\frac{\frac{x_1+\ldots+x_n}{n}-\mu}{\sqrt{\frac{\sigma^2}n}}\ge Z_\frac{\alpha}2$
$\mu=Z_\frac{\alpha}2\frac{\sigma}{\sqrt n}\le\frac{x_1\ldots+x_n}{n}\le\mu+Z_\frac{\alpha}{2}\frac{\sigma}{\sqrt n}\qquad\text{con probabilità }(1-\alpha)(\text{TLC})$
$\mu-\frac{1}{\sqrt\alpha}\frac{\sigma}{\sqrt n}\le\frac{x_1+\ldots+x_n}{n}\le\mu+\frac{1}{\sqrt\alpha}\frac{\sigma}{\sqrt n}$

| Prob lontani | Prob vicini |                         | TLC                  |
| ------------ | ----------- | ----------------------- | -------------------- |
| $\alpha$     | $1-\alpha$  | $\frac{1}{\sqrt\alpha}$ | $Z_\frac{\alpha}{2}$ |
| $25\%$       | $75\%$      | $2$                     | $1.15$               |
| $10\%$       | $90\%$      | $3.2$                   | $1.64$               |
| $5\%$        | $95\%$      | $4.5$                   | $1.96$               |
| $1\%$        | $99\%$      | $10$                    | $2.56$               |
TLC (in breve)
$\displaystyle\mathbb P\left[\frac{\frac{x_1+\ldots+x_n}{x}-\mu}{\sqrt{\frac{\sigma^2}n}}\le z\right]_{\underset{x>>1}{\text{TLC}}}\simeq\underset{Z\simeq N(0,1)}{\mathbb P[Z\le z]}$

$\overline X=\frac{X_1+\ldots+X_n}n$
$\mathbb E[\overline X]=\mathbb E[\frac{X_1+\ldots+X_n}n]=\frac{\mathbb E[X_1]+\ldots+\mathbb E[X_n]}{n}\overbrace{=}^{\begin{array}{c}\text{indipendendemente distribuite}\\\text{con media }\mu\end{array}}\frac{\overbrace{n+\ldots+n}^{n\text{ addendi}}}{n}=\mu$

$\operatorname{Var}[\overline X]=\operatorname{Var}[\frac{x_1+\ldots+x_n}n]\overbrace{=}^{\text{indipendenti}}\frac{\operatorname{Var}[X_1]+\ldots+\operatorname{Var}[X_n]}{n^2}\overbrace{=}^{\begin{array}{c}\text{indipendendemente distribuite}\\\text{con varianza }\sigma^2\end{array}}\frac{\sigma^2+\ldots+\sigma^2}{n^2}=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}n$

$\mathbb P\left[\frac{(x_1+\ldots+x_n)-n\mu}{\sqrt{n\sigma^2}}\le z\right]\underset{\underset{n>>1}{\text{TLC}}}{\simeq}\underset{Z\sim N(0,1)}{\mathbb P[Z\le z]}$
$\mathbb E[S_n]=\mathbb E[\underbrace{x_1+\ldots+x_n}_{S_n}]=n\mu$
$\operatorname{Var}[S_n]=n\sigma^2$

Lancio una moneta equilibrata $100$ volte
$y=\text{Frequenza relativa del numero testa}$

a) Qual'è la probabilità che $y\in[0.4,0.6]$
$\begin{cases}1&\text{Testa primo lancio}\\0&\text{Croce primo lancio}\end{cases}\ldots\begin{cases}1&\text{Testa primo lancio}\\0&\text{Croce primo lancio}\end{cases}$
$y=\frac{x_1+\ldots+x_n}n=\frac{S_n}n\quad S_n=x_1+\ldots+x_n$

$\mathbb P[0.4<Y<0.6]$
$x_1,\ldots,x_n\sim B(p)\quad p=\frac12=\mathbb P[T]$
Metodo 1
	$S_n=x_1+\ldots+x_n\sim\operatorname{Bin}(n,p)\quad n=100$
	$\mathbb P[0.4<\frac{S_n}n<0.6]=\mathbb P[40<S_n<60]=\sum\limits_{n=41}^{59}\mathbb P[S_n=K]=\sum\limits_{n=41}^{59}{n\choose k}p^k(1-p)^{n-k}\simeq 94.3\%$
Metodo 2
	$\mathbb P\left[0.4<\frac{x_1+\ldots+x_n}n<0.6\right]=$
		$\mathbb E[x_i]=p=\frac12=\mu$
		$x_i\sim B(p)$
		$\operatorname{Var}[x_i]=p(1-p)=\frac14=\sigma^2$
	$\displaystyle=\mathbb P\left[\frac{0.4-0.5}{\underset{\sigma}{\frac12}\underset{\frac{1}{\sqrt n}}{\frac{1}{10}}}<\frac{\frac{x_1+\ldots+x_n}{n}-\mu}{\sqrt{\frac{\sigma^2}n}}\le\frac{0.6-0.5}{\frac12\frac1{10}}\right]\underset{\underset{\text{TLC}}{n>>1}}\simeq\mathbb P\left[-\frac{20}{10}<Z<\frac{20}{10}\right]\le\mathbb P[-2<Z<2]=1-2]\varphi(-2.00)=1-2(0.0228)\simeq95.5\%$

$\displaystyle\mathbb P\left[0.4<\frac{\overbrace{x_1+\ldots+x_n}^{S_n=\text{numero di teste}}}{\underbrace{n}_{\text{frequenza relativa}}}<0.6\right]\simeq 95\%$

b) Quante volte occorre lanciare una moneta equilibrata in modo tale che $\mathbb P\left[0.49<\frac{x_1+\ldots+x_n}{n}<0.51\right]\simeq 90\%$
$0.49=\mu-\delta$
$0.51=\mu+\delta$
$\mu=\mathbb P=0.5$
$s=\frac1{100}$
$\mathbb P\left[\mu-s<\frac{x_1+\ldots+x_n}{n}<\mu+s\right]=\mathbb P\left[-\frac{\sigma}{\sqrt{\frac{\sigma^2}{n}}}\le\frac{\frac{x_1+\ldots+x_n}{n}-\mu}{\sqrt{\frac{\sigma^2}{n}}}\le\frac{\sigma}{\sqrt{\frac{\sigma^2}{n}}}\right]\underset{\underset{\text{TLC}}{n>>1}}{\simeq}\mathbb P\left[-\frac{\sigma}{\sqrt{\frac{\sigma^2}{n}}}<Z<\frac{\sigma}{\sqrt{\frac{\sigma^2}{n}}}\right]$

$\frac{\delta}{\sqrt{\delta^2}{n}}\simeq Z_\alpha\qquad\alpha=5\%$
$\delta=Z_\alpha\quad\frac{\sigma}{\sqrt n}\quad\sqrt n=\frac{Z_\alpha \sigma}{\delta}\quad n=(\frac{Z_\alpha\sigma}\delta)^2=6804$
$\delta^2=\operatorname{Var}[B(p)]=p(1-p)=\frac14$
$p=\frac12$
$\sigma=\frac12$
$S=\frac1{100}$
$Z_{0.05}\simeq 1.6449\simeq 1.65$

Esercizio
Il numero di clienti in un ristorante è descritto da una poisson di parametro $\lambda$. In media al ristorante ci sono $225$ clienti
Stimate la probabilità di avere un numero di clienti $\le200$
$N=\text{numero clienti ristorante}$
$N\sim\operatorname{Poisson}(\lambda)\qquad\mathbb E[N]=225$
$\mathbb E[N]\operatorname{Var}[N]=\lambda$
$\mathbb P[N\le200]=\mathbb P[N=0]+\ldots+\mathbb P[N=200]=4.3\%$
$\mathbb P[N=K]=e^{-\lambda}\frac{\lambda^K}{K!}$
$\displaystyle\underbrace{N}_{\underset{\lambda=225}{\operatorname{Poisson}(\lambda)}}=N_1+\ldots+N_n$
$N_1,\ldots,N_n\text{ indipendenti, identicamente distribuite}$

$\begin{array}{l}X\sim\operatorname{Poisson}(n)\\Y\sim\operatorname{Poisson}\end{array}\quad x\perp\!\!\!\perp y\quad X+Y\sim\operatorname{Poisson}(\lambda+\mu)$

$N_1,\ldots,N_n\sim\operatorname{Poisson}(\mu)$
$\lambda=\mathbb E[N]=\mathbb E[N_1+\ldots+N_n]=n\mu$
$\mathbb P[n\le200]=\mathbb P[N_1+\ldots+N_n\le200]=\mathbb P[N_1+\ldots+N_n]=\mathbb P\left[\frac{(N_1+\ldots+N_n)-\lambda}{\sqrt{\lambda}}<\frac{200-225}{\sqrt{225}}\right]$
$\operatorname{Var}[N]=\operatorname{Var}[N_1+\ldots+N_n]$

$\varphi(-1.67)\simeq4.8\%$