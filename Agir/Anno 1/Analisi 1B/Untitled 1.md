 ****$\displaystyle\sum\limits_{n=1}^\infty\frac{\cos(n^4)}{n^2+1}$
$|\frac{\cos(n^4)}{n^2+1}|\le\frac{1}{n^2+1}\le\frac1{n^2}\overset{n\to\infty}\longrightarrow\ 0\text{ di ordine }2\rightarrow\text{converge}$



$\displaystyle\sum\limits_{n=1}^\infty2^n\sin(\frac1{3^n})$
$2^n\sin(\frac1{3^n})\overset{n\to\infty}\sim2^n\frac{1}{3^n}=(\frac23)^n=(\frac32)^{-n}\longrightarrow0\text{ esponenzialmente}$
$(\sin x\sim x\ \ x\to 0)$
$\sum\limits_{n=1}^\infty(\frac23)^n\quad a_n=(\frac23)^n\quad\sqrt[n]{a_n}=\sqrt[n]{(\frac23)^n}=(\frac23)^{n\cdot\frac1n}=\frac23<1$



$\displaystyle\sum\limits_{n=1}^\infty\frac{(2n)!}{n^{2n}}$
$n!\sim\sqrt{2\pi n}(\frac ne)^n\quad n!=n(n-1)!$

$\frac{a_{n+1}}{a_n}=\frac{[2(n+1)]!}{n+1^{2(n+1)}}\cdot\frac{n^{2n}}{(2n!)}=\frac{(2n+2)(2n+1)\cancel{(2n)!}}{(n+1)^{2n}(n+1)^2}\frac{n^{2n}}{\cancel{(2n)!}}=\underbrace{\frac{2(n+1)(2n+1)}{(n+1)^2}}_{4}(\frac{n}{n+1})^{2n}\longrightarrow 4e^{-2}$



$\displaystyle\sum\limits_{n=1}^\infty(1-\frac1{n^2})^{n^2}$
$a_n=\exp(n^2\cdot\ln(1-\frac1{n^2}))=$
$\small\ln(1+x)=x+o(x^2)$
$=\exp\left(n^2\cdot\left(-1\frac{x^2}+o(\frac1{n^4})\right)\right)=\exp\left(-1+o(\frac1{n^2}\right)=e^{-1+o(\frac1{n^2})}\rightarrow e^{-1}=\frac1e\ngtr0$



$\displaystyle\sum\limits_{n=1}^\infty(-1)^n\frac{2^n+n}{3^n+n^2}$

$|a_n|=\frac{2^n+n}{3^n+n^2}\sim\frac{2^n}{3^n}=(\frac23)^n\to0\text{esponenzialmente}$



$\displaystyle\sum\limits_{n=1}^\infty(-1)^n\frac{2+n}{1+n+n^2}$

$|a_n|=\frac{n+2}{n^2+n+1}\sim\frac1n\to0\text{ di ordine }1$

$\frac{2+n}{n^2+n+1}\sim\frac n{n^2}=\frac1n\searrow\text{ Leibniz}$

Non converge assolutamente ma converge semplicemente



$\displaystyle\sum\limits_{n=1}^\infty\left(\frac{\ln(n)}n\right)^2$
$\frac{(\ln n)^2}{n^2}\to 0\text{ di ordine}>2-\varepsilon\ \ \forall\ \varepsilon$
$\frac{(\ln n)^2}{n^2}\le7\frac{\sqrt n}{n^2}=\frac1{n^{\frac32}}\to0\text{ di ordine }\frac32$



$\displaystyle\sum\limits_{n=1}^\infty\frac{\ln(n!)}{n^3}$
$\frac{\ln(n!)}{n^3}\le\frac{\ln(n^n)}{n^3}=\frac{n\ln n}{n^3}=\frac{ln n}{n^2}\to 0\text{ di ordine }>\frac32>2-\varepsilon$



$\displaystyle\sum\limits_{n=1}^\infty\frac{1}{n\sqrt[n]{n!}}\overset{\text{conv}}=?$

$n!=n\cdot(n-1)\cdot(n-2)\cdot\ldots\cdot3\cdot2\cdot1=n\cdot(2(n-1))\cdot(3(n-2))\cdot\ldots\ge\overset{{\frac n2\text{ termini}}}{n\cdot n\cdot n\cdot\ldots}=n^{\frac n2}$

$\sqrt[n]{n!}\ge\sqrt[n]{n^\frac n2}=n^\frac12$

$\frac1{n\sqrt[n]{n!}}\le\frac1{n\cdot n^12}\to0\text{ di ordine }\frac32$



$\displaystyle\sum\limits_{n=1}^\infty\frac{x^n}{n\cdot 2^n}\quad\text{Studiare il carattere della serie al variare di }x\in\mathbb R$

$\frac{x^n}{n\cdot2^n}=\frac1n(\frac x2)^n$



$\displaystyle\sum\limits_{n=1}^\infty(-1)^{n+1}\frac{(\ln 10)^n}{n!}$

$\left|(-1)^{n+1}\frac{(\ln 10)^n}{n!}\right|\ge\frac{(\ln 10)^n}{n^{n/2}}\text{ converge}$
$\sum\limits_{n=1}^\infty{x^n}{n!}=e^x\quad |x|<1$



$\displaystyle\sum\limits_{n=1}^\infty\frac{\sin(n^3)-n^\frac35}{n^\frac14\ln(n^n+n!)}$




Sia $\displaystyle F=\left\{d\in\mathbb R_+:\sum\limits_{n=1}^\infty\sqrt{\frac{n^2+\ln n}{n^\alpha\ln(n+1)}}\text{ diverge}\right\}$
Trova $\sup E$

$a_n=\sqrt{\frac{n^2+\ln n}{n^\alpha\ln(n+1)}}\sim\sqrt{\frac{n^2}{n^\alpha\ln(n+1)}}=\frac1{n^\frac{a-2}2+\sqrt{\ln n}}=\frac{1}{n^\frac\alpha2+\sqrt{\ln n}}$
