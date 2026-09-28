# Asintoti
## Definizione
Siano $f,g$ due funzioni definite in un intorno di $\pm\infty$
Si dice che $f$ è **asintotica** a g (a $\pm\infty$) se $\lim\limits_{x\rightarrow+\infty}(f(x)-g(x))=0$
In particolare, se $g(x)=mx+q$, si dice che la retta $g$ è **asintoto** (a $\pm\infty$) di $f$
- orizzontale se $m=0$
- obliquo se $m\ne0$

## Osservazione
Dire che $g(x)=mx+q$ è asintoto di $f$ equivale a $\lim\limits_{x\rightarrow+\infty}\frac{f(x)}{x}=m$, $\lim\limits_{x\rightarrow+\infty}(f(x)-mx)=q$
## Esempio
$\frac{x^2+x^\frac{1}{2}+sin(x)+2x}{x}$
Verifichiamo che $x+2$ è asintoto a $+\infty$
$\frac{x^2+x^\frac{1}{2}+sin(x)+2x}{x}-(x+2)$
$\frac{x^2+x^\frac{1}{2}+sin(x)+2x-x^2-2x}{x}$
$x^{-\frac{1}{2}}+\frac{sin(x)}{x}\overset{x\rightarrow+\infty}{\longrightarrow}0$
$x+2$ è asintoto a $+\infty$ $\checkmark$

Si dice che la retta di equazione $x=x_0$ è **asintoto verticale** di $f$ se $\lim\limits_{x\rightarrow x_0^\pm}f(x)=\pm\infty$