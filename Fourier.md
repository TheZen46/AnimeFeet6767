# Teorema (Fourier)
$\text{Sia }f:\R\to\R\ 2\pi\text{-periodica e di classe }C^1\text{ a tratti su tutti i periodi.}$
$\displaystyle\text{Allora la serie di Fourier }\frac12 a_0+\suml_{k=1}^{+\infty}\bigl(a_k\cos(kx)+b_k\sin(kx\bigr)\text{ dove }\array{a_k=\frac1\pi\int_{-\pi}^\pi f(t)\cos(kt)dt&a_0=\frac1\pi\int_{-\pi}^\pi f(t)dt\\b_k=\frac1\pi\int_{-\pi}^\pi f(t)\sin(kt)dt&\bigl(k\in\mathcal{Z}_{>0}\bigr)}\text{,converge per ogni }x\in\R\text{ a }\frac12\bigl(f(x_+)+f(x_-)\bigr)\text{, ovvero alle medie tra i limiti monotoni }f(x_\pm)\coloneqq\lim\limits_{y\to x^\pm}f(y)\text{ in }x\text.$
## Osservazione
$\text{Se }f\text{ è continua in }x\text{, allora la serie di Fourier converge proprio a }f(x)\text.\\\text{Se invece }f\text{ ha un salto in }x\text{, la serie converge al punto medio del salto.}$

(Un onda quadra ha valore $0.5$ nel cambio di polarità, altrimenti $0/1$)

## Dimostrazione
Obiettivo: Mostrare che la successione delle somme parziali $\displaystyle s_n(x)=\frac12a_0+\suml_{k=1}^{a_k}\bigl(\cos(kx)+b_k\sin(kx)\bigr)$ converge a $\displaystyle \frac12\bigl(f(x_+)+f(x_-)\bigr)$ per $n\to+\infty$
In realtà, verificheremo che $\lim\limits_{n\to+\infty}\biggl(s_n(x)-\frac12\bigl(f(x_+)+f(x_-)\bigr)\biggr)=0$

Sostituendo i coefficienti di Fourier, ottengo: $\downarrow\star:\int\text{ non dipende da punto centrale}$
$\displaystyle s_n(x)=\frac1\pi\int_{-\pi}^{\pi}f(t)\biggl(\frac12+\suml_{k=1}^n\bigl(\cos(kt)\cos(kx)+\sin(kt)\sin(kx)\bigr)\biggr)dt=\frac1\pi\int_{-\pi}^{\pi}f(t)\biggl(\frac12+\suml_{k=1}^n\cos\bigl(k(t-x)\bigr)\biggr)\overset{(y\m2=\m2 t-x)}{\Large=}\frac1\pi\int_{-\pi}^{\pi}f(x+y)\biggl(\frac12+\suml_{k=1}^n\cos(ky)\biggr)dy\overset{\large\star}=\frac1\pi\int_{-\pi}^\pi f(x+y)\biggl(\frac12+\suml_{k=1}^n\cos(ky)\biggr)dy=\frac1\pi\int_{-\pi}^\pi f(x+y)\overbrace{\m8\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}\m8}^{\text{ID Trig Lagrange}}dy=\\\displaystyle =\frac1\pi\int_{-\pi}^0f(x+y)\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy+\frac1\pi\int_0^\pi f(x+y)\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy$
		$\displaystyle \frac1\pi\int_0^\pi\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy=\frac1\pi\int_0^\pi\biggl(\frac12+\suml_{k=1}^n\cos(ky)\biggr)dy=\frac1\pi\biggl[\frac12y+\suml_{k=1}^n\frac1k\sin(ky)\biggr]_0^\pi=\color\yellow\frac12$
		$\displaystyle \frac1\pi\int_{-\pi}^0\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy=\color\lightblue\frac12$
$\displaystyle \frac12\bigl(f(x_+)+f(x_-)\bigr)={\color\lightblue\frac12}f(x_-)+{\color\yellow\frac12}f(x_+)=\frac1\pi\int_{-\pi}^0f(x_-)\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy+\frac1\pi\int_0^\pi f(x_+)\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy$
$\displaystyle s_n(x)-\frac12\bigl(f(x_+)+f(x_-)\bigr)=\frac1\pi\int_{-\pi}^0\bigl(f(x+y)-f(x_-)\bigr)\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy+\frac1\pi\int_0^\pi\bigl(f(x+y)-f(x_+)\bigr)\frac{\sin\bigl((n+\frac12)y\bigr)}{2\sin(\frac12y)}dy=\frac1\pi\int_{-\pi}^0\underbrace{\frac{f(x+y)-f(x_-)}{2\sin(\frac12y)}}_{\Large\Phi_-(y)}\sin\bigl((n+\frac12)y\bigr)dy+\frac1\pi\int_0^{\pi}\underbrace{\frac{f(x+y)-f(x_+)}{2\sin(\frac12y)}}_{\Large\Phi_+(y)}\sin\bigl((n+\frac12)y\bigr)dy$
Verifichiamo che, per $n\to+\infty$, entrambi gli integrali convergano a zero per il lemma di Riemann
Per applicare Riemann devo verificare che $\Phi_+$ e $\Phi_-$ siano continui a tratti
$\Phi_+:\bigl[0,\pi\bigr]\to\R,\ y\mapsto\cases{\frac{f(x+y)-f(x_-)}{2\sin(\frac12y)}&y\ne0\\f'(x_+)&y=0}$
Siccome $f$ è per ipotesi continua a tratti, per confermare che $\Phi_+$ è continua a tratti basta verificare che esiste finito $\lim\limits_{y\to0^+}\Phi_+(y)$
Esamino $\Phi_+$ in $\bigl(0,\pi\bigr]$: $\displaystyle \Phi_+(y)=\frac{f(x+y)-f(x_+)}{2\sin(\frac12y)}$
Poiché $f$ è $C^1$ a tratti, esiste un intorno destro $\bigl(x,x+\delta\bigr)$ di $x$ in cui $f$ è $C^1$, $\delta>0$
Inoltre, $\bigl[x,x+\delta\bigr]\to\R,\ x+y\mapsto\cases{f(x+y)&y\ne0\\f(x_+)&y=0}$ è continua
Fisso $y\in\bigl(0,\delta\bigr]$ e applico il teorema di Lagrange:
	Trovo $\eta\in\bigl(0,y\bigr)$ tale che $\displaystyle f(x+y)-f(x_+)=f'(x+\eta)y\Rightarrow\Phi_+(y)=\frac{f'(x+\eta)y}{2\sin(\frac12y)}=f'(x+\eta)\cdot\frac{y/2}{\sin(y/2)}$
	$\displaystyle \lim\limits_{y\to0^+}\Phi_](y)=\biggl(\lim\limits_{y\to0^+}f'(x+y)\biggr)\cdot\underbrace{\biggl(\lim\limits_{y\to0^+}\frac{y/2}{\sin(y/2)}\biggr)}_{=1}$
		$\array{0&<&\eta&<&y\\&&\downarrow&\Leftarrow&\downarrow\\&&0^+&&0^+}$
	$=\lim\limits_{\large{z\to x^+}}f'(z)=f'(x_+)\ \ \exists$ finito perché $f$ è $C^1$ a tratti

## Osservazione
$f$ pari $\Rightarrow b_k=0$ / $f$ dispari $\Rightarrow a_k=0$

$f$ pari: $\displaystyle b_k=\frac1\pi\int_{-\pi}^\pi f(t)\sin(kt)dt\overset{(t'=-t)}=\frac1\pi\int_{-\pi}^\pi \underbrace{f(-t')}_{=f(t')}\underbrace{\sin(-kt')}_{=-\sin(kt')}dt'=-\frac1\pi\int_{-\pi}^\pi f(t')\sin(kt')dt'=-bk\Rightarrow 2b_k=0\Rightarrow b_k=0$

$f$ dispari: $\displaystyle a_k=\frac1\pi\int_{-\pi}^\pi f(t)\cos(kt)dt\overset{(t'=-t)}=\frac1\pi\int_{-\pi}^\pi \underbrace{f(-t')}_{=-f(t')}\underbrace{\cos(-kt')}_{=\cos(kt')}dt'=-\frac1\pi\int_{-\pi}^\pi f(t')\cos(kt')dt'=-a_k\Rightarrow 2a_k=0\Rightarrow a_k=0$

# Osservazione (notazione esponenziale)
$e^{ikx}=\cos(kx)+i\sin(kx)$
	$\displaystyle \cos(kx)=\frac{e^{ikx}+e^{-ikx}}2$
	$\displaystyle \sin(kx)=\frac{e^{ikx}-e^{-ikx}}{2i}$

$\displaystyle s_n(x)=\frac12a_0+\suml_{k=1}^n\Bigl(\frac{e^{ikx}+e^{-ikx}}2+b_k\frac{e^{ikx}-e^{-ikx}}{2i}\Bigr)=\suml_{k=1}^n e^{-ikx}\frac12\bigl(a_k+i\ b_k\bigr)+\frac12a_0\suml_{k=1}^n e^{ikx}\frac12\bigl(a_k-i\ b_k\bigr)$
Introduciamo 