# Definizione
$f,g$ funzioni definite in un intorno di $c$, eventualmente $c$ escluso, con $g(x)\ne0$ in tale intorno, $c$ escluso.
Si supponga che esista $l=\lim\limits_{x\rightarrow c}\frac{f(x)}{g(x)}$ (finito, $\pm\infty$)
Se $l\in\mathbb{R}$ è finito, diremo che $f$ è **controllata** da $g$ per $x\rightarrow c$, e scriveremo $f=O(g), x\rightarrow c$  "O grande"
In particolare, se $l=1$, diremo che $f$ è equivalente a $g$ per $x\rightarrow c$, e scriveremo $f \sim c, x\rightarrow c$
Inoltre, se $l=0$, diremo che $f$ è **trascurabile** rispetto a $g$ per $x\rightarrow c$, e scriveremo $f=o(g)$  "o piccolo"

# Esempi
- $sin(x)\sim x,\rightarrow 0$
- $1-cos(x)\sim\frac{1}{2}x^2,x\rightarrow 0$
- $\ln(1+x)\sim x, x\rightarrow 0$
- $e^n-1\sim x,x\rightarrow 0$
- $(1+x)^\alpha -1\sim \alpha x,x\rightarrow 0$
- $x^n=o(x^m),x\rightarrow 0\ \ \ \ n,m\in\mathbb{Z}, n>m$
- $x^m=o(x^n),x\rightarrow \pm\infty\ \ \ \ n,m\in\mathbb{Z}, n>m$

# Definizione
$f$ funzione definita in intorno di $c$, eventualmente $c$ escluso.
Diremo che $f$ è
- infinitesima in $c$ se $\lim\limits_{x\rightarrow c} f(x)=0$
- infinita in $c$ se $\lim\limits_{x\rightarrow c} f(x)=\pm\infty$

Se $f,g$ sono infinitesime in $c$, si dice che
- $f$ e $g$ sono **infinitesimi dello stesso ordine** se $\lim\limits_{x\rightarrow c} \frac{f(x)}{g(x)}\in\mathbb{R}\backslash\{0\}$ finito e non nullo
- $f$ è **infinitesimo di ordine superiore** rispetto a $g$ se $f=o(g)$
- $f$ è **infinitesimo di ordine inferiore** rispetto a $g$ se $g=o(f)$

Se $f,g$ sono infinite in $c$, si dice che
- $f$ e $g$ sono **infiniti dello stesso ordine** se $\lim\limits_{x\rightarrow c} \frac{f(x)}{g(x)}\in\mathbb{R}\backslash\{0\}$ finito e non nullo
- $f$ **è infinito di ordine superiore** rispetto a $g$ se $g=o(f)$
- $f$ **è infinito di ordine inferiore** rispetto a $g$ se $f=o(g)$

Se nessuno dei casi precedenti è verificato, si dice che $f$ e $g$ sono infinitesimi/infinito **non confrontabili**
## Esempio
$f(x)=x\sin(\frac{1}{x}), g(x)-x$
$\frac{g(x)}{f(x)}-\frac{1}{\sin(\frac{1}{x})}$  $\frac{f(x)}{g(x)}=\sin(\frac{1}{x})$  $\lim\limits_{x\rightarrow0}\nexists$

Talvolta è utile considerare infinitesimi/infiniti campione $\varphi$
$(c=x_0\in\mathbb{R})$
$\varphi(x)=x-x_0,\varphi(x)=|x-x_0|$ (infinitesimi)
$\varphi(x)=\frac{1}{|x-x_0|}$ (infiniti)

$(c=\pm\infty)$
$\varphi(x)=\frac{1}{x},\varphi(x)=\frac{1}{|x|}$ (infinitesimi)
$\varphi(x)=x, \varphi(x)=|x|$ (infiniti)

$(c=x_0^{\pm})$
$\varphi(x)=x-x_0,\varphi(x)=x_0-x$ (infinitesimi)
$\varphi(x)=\frac{1}{x-x_0}, \varphi(x)=\frac{1}{x_0-x}$ (infiniti)

# Definizione
Sia $f$ un infinitesimo/infinito in $c$
Se esiste $\alpha>0$ tale che $f$ è dello stesso ordine di $\varphi^\alpha$, si dice che $\alpha$ è l'ordine di $ f$ rispetto a $\varphi$ per $x\rightarrow c$, dove $\varphi$ è infinitesimo/infinito campione per $x\rightarrow c$

Se tale $\alpha$ esiste, posto $l=\lim\limits_{x\rightarrow c}\frac{f(x)}{\varphi(x)^{\alpha}}\in\mathbb{R}\backslash\{0\}$, diremo che $p(x)=l\varphi(x)^{\alpha}$ è la parte principale di $f$ rispetto a $\varphi$

## Esempio
Parte principale di $f(x)=x+x(5x-\sqrt{x}+\ln(x))^\frac{1}{2}$
per $x\rightarrow\infty$ rispetto all'infinito campione $\varphi(x)=x$ (maggiore di $\sqrt x$ e $\ln(x)$, si sceglie $x$)
$f(x)=x+x(5x-\sqrt{x}+\ln(x))^\frac{1}{2}=x+x^\frac{3}{2}(5-x^5\underbrace{\frac{1}{2}}_{o(1)}+\underbrace{\frac{\ln(x)}{x})}_{o(1)}=x^\frac{3}{2}(\underbrace{x^{-\frac{1}{2}}}_{o(1)}+\underbrace{(5-x^{-\frac{1}{2}}+\frac{\ln(x)}{x})^\frac{1}{2}}_{\sqrt{5}+o(1)})=x^\frac{3}{2}(\sqrt{5}+o(1)=\sqrt{5}^\frac{3}{2}+o(x^\frac{3}{2})$