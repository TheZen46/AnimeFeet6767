# Teorema (Fourier) — Definizioni e risultati utilizzati

## Osservazione (notazione e definizioni)

### Funzione periodica
Una funzione $f:\R\to\R$ è $2\pi$-periodica se
$\displaystyle f(x+2\pi)=f(x)\quad\forall x\in\R.$

Se $g$ è integrabile e $2\pi$-periodica, l'integrale su un intervallo di lunghezza $2\pi$ non dipende dall'estremo iniziale:
$\displaystyle\int_a^{a+2\pi}g(t)dt=\int_{-\pi}^{\pi}g(t)dt.$
È questa proprietà che giustifica la traslazione dell'intervallo nella dimostrazione.

### Limiti laterali
$\displaystyle f(x_-)=\lim_{h\to0^-}f(x+h),\qquad f(x_+)=\lim_{h\to0^+}f(x+h).$

$f(x_-)$ è il limite da sinistra, mentre $f(x_+)$ è il limite da destra. Non è necessario che coincidano con il valore $f(x)$.

- Se $f(x_-)=f(x_+)=f(x)$, $f$ è continua in $x$.
- Se $f(x_-)\ne f(x_+)$, $f$ presenta una discontinuità di salto in $x$.
- Il valore della serie di Fourier nel punto di salto è la media dei due limiti laterali.

### Funzione $C^1$ a tratti
Una funzione è $C^1$ a tratti se, in ogni periodo, si può suddividere l'intervallo in un numero finito di sottointervalli nei quali la funzione è derivabile con derivata continua. Ai punti di raccordo si considerano i limiti laterali, quando esistono.

La notazione $f'(x_+)$ indica il limite destro della derivata:
$\displaystyle f'(x_+)=\lim_{z\to x^+}f'(z).$
Non indica il valore della funzione $f$ a destra di $x$.

## Identità (trigonometriche)

### Formula di addizione del coseno
$\displaystyle \cos(A-B)=\cos(A)\cos(B)+\sin(A)\sin(B).$

Ponendo $A=kt$ e $B=kx$:
$\displaystyle\cos(kt)\cos(kx)+\sin(kt)\sin(kx)=\cos(k(t-x)).$

### Formula di Eulero
$\displaystyle e^{i\theta}=\cos(\theta)+i\sin(\theta).$

Da questa identità e da quella ottenuta sostituendo $\theta$ con $-\theta$:
$\displaystyle\cos(\theta)=\frac{e^{i\theta}+e^{-i\theta}}2,\qquad\sin(\theta)=\frac{e^{i\theta}-e^{-i\theta}}{2i}$

## Identità (nucleo di Dirichlet)

Definiamo il nucleo di Dirichlet:
$\displaystyle D_n(y)=\frac12+\suml_{k=1}^{n}\cos(ky).$

La sua forma chiusa è
$\displaystyle D_n(y)=\frac{\sin((n+\frac12)y)}{2\sin(\frac12y)}.$

Questa identità si ricava sommando la progressione geometrica
$\displaystyle\suml_{k=-n}^{n}e^{iky}$
e applicando le formule di Eulero.

Il quoziente è da intendersi per continuità nei punti in cui il denominatore si annulla. In particolare, $D_n(0)=n+\frac12$.

### Proprietà del nucleo di Dirichlet
- $D_n$ è pari, perché il coseno è pari.
- $D_n$ è $2\pi$-periodico.
- $\displaystyle\int_0^\pi D_n(y)dy=\frac\pi2$.
- Per parità, $\displaystyle\int_{-\pi}^0D_n(y)dy=\frac\pi2$.

Infatti:
$\displaystyle\int_0^\pi D_n(y)dy=\int_0^\pi\left(\frac12+\suml_{k=1}^{n}\cos(ky)\right)dy=\left[\frac y2+\suml_{k=1}^{n}\frac{\sin(ky)}k\right]_0^\pi=\frac\pi2$

## Teorema (Lagrange)

Se $g:[a,b]\to\R$ è continua su $[a,b]$ e derivabile su $(a,b)$, allora esiste $c\in(a,b)$ tale che
$\displaystyle g(b)-g(a)=g'(c)(b-a).$

Nella dimostrazione di Fourier si applica a $g(u)=f(x+u)$. Per $y>0$ sufficientemente piccolo, esiste $\eta_y\in(0,y)$ tale che
$\displaystyle f(x+y)-f(x_+)=f'(x+\eta_y)y.$

Poiché $0<\eta_y<y$, quando $y\to0^+$ anche $\eta_y\to0^+$. Si può quindi usare il limite destro di $f'$.

## Identità (limite fondamentale)

$\displaystyle\lim_{u\to0}\frac{\sin u}{u}=1.$

Di conseguenza:
$\displaystyle\lim_{y\to0}\frac{y/2}{\sin(y/2)}=1.$

È il limite usato per verificare che $\Phi_+(y)$ abbia limite finito per $y\to0^+$.

## Lemma (Riemann-Lebesgue)

Se $g$ è integrabile su un intervallo finito $[a,b]$, allora
$\displaystyle\lim_{\lambda\to+\infty}\int_a^b g(y)\sin(\lambda y)dy=0$

e analogamente

$\displaystyle\lim_{\lambda\to+\infty}\int_a^b g(y)\cos(\lambda y)dy=0$

### Applicazione nella dimostrazioni
Nella dimostrazione si ottengono gli integrali
$\displaystyle\int_{-\pi}^0\Phi_-(y)\sin((n+\frac12)y)dy,\qquad\int_0^\pi\Phi_+(y)\sin((n+\frac12)y)dy$

Le funzioni $\Phi_-$ e $\Phi_+$ non dipendono da $n$. Se sono integrabili, il lemma si applica perché
$\displaystyle\lambda_n=n+\frac12\longrightarrow+\infty.$

La continuità a tratti su un intervallo finito è una condizione sufficiente per l'integrabilità. Il lemma di Riemann-Lebesgue richiede in realtà soltanto l'integrabilità.

## Osservazione (parità)

Una funzione $g$ è pari se $g(-x)=g(x)$, ed è dispari se $g(-x)=-g(x)$.

Per una funzione pari:
$\displaystyle\int_{-a}^{a}g(t)dt=2\int_0^a g(t)dt.$

Per una funzione dispari:
$\displaystyle\int_{-a}^{a}g(t)dt=0.$

Poiché $\sin(kt)$ è dispari e $\cos(kt)$ è pari:
- Se $f$ è pari, $f(t)\sin(kt)$ è dispari e quindi $b_k=0$.
- Se $f$ è dispari, $f(t)\cos(kt)$ è dispari e quindi $a_k=0$. Inoltre $a_0=0$.

## Osservazione (notazione esponenziale)

I coefficienti complessi sono definiti da
$\displaystyle\alpha_k=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)e^{-ikt}dt,\quad k\in\mathcal Z.$

Per $k=0$:
$\displaystyle\alpha_0=\frac{a_0}{2}.$

Per $k>0$:
$\displaystyle\alpha_k=\frac12(a_k-i b_k),\qquad
\alpha_{-k}=\frac12(a_k+i b_k).$

Se $f$ è reale:
$\displaystyle\alpha_{-k}=\overline{\alpha_k}.$

La somma parziale complessa è
$\displaystyle s_n(x)=\suml_{k=-n}^{n}\alpha_ke^{ikx}.$

Si parla di somme parziali **simmetriche** perché gli indici sono compresi tra $-n$ e $n$.

## Osservazione (onda quadra)

Se un'onda quadra assume i valori $0$ e $1$, in un punto di salto la serie converge a
$\displaystyle\frac{0+1}{2}=\frac12.$

Il valore assegnato alla funzione esattamente nel punto di salto non modifica i coefficienti di Fourier, perché cambiare una funzione in un numero finito di punti non cambia i suoi integrali.
