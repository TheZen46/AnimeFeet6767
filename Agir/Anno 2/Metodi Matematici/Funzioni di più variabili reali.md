$f:D\subset\mathbb R^n\to\mathbb R^m$

$\forall x\in D\mskip{18mu}\exists!\ y\in\mathbb R^m$
$f(x)=y$

$R^n$ indica l'insieme delle $n$-uple di numeri reali
$\vec x\in\mathbb R^n\mskip{24mu}\vec x=(x_1,x_2,\ldots,x_n)\mskip{24mu}x_n\in R\ \ \forall i$

$\mathbb R^n$ è uno spazio vettoriale
$\vec x=(x_1,\ldots,x_n)\mskip{24mu}\lambda_1,\lambda_2\in\mathbb R$
$\vec y=(y_1,\ldots,y_n)$
$\lambda_1\ \vec x+\lambda_2\ \vec y\in\mathbb R^n=(\lambda_1x_1+\lambda_2y_1,\ldots,\lambda_1x_n+\lambda_2y_n)$
Proprietà e operazioni di $\mathbb R^n$
È uno spazio vettoriale di dimensione n

$e_1=\pmatrix{1\\0\\0\\\vdots\\0}\mskip{24mu}e_2=\pmatrix{0\\1\\0\\\vdots\\0}\mskip{12mu}\dots\mskip{12mu}e_n=\pmatrix{0\\0\\0\\\vdots\\1}$

$\{\vec e_i\}_{x\in\{1n\ldots,n\}}$ è una base di $\mathbb R^n$
$\vec x=(x_1,\ldots,x_n)$
$\displaystyle\vec x=(x_1e_1,\ldots,x_ne_n)=\sum\limits_{i=1}^n x_i e_i$
$\vec x\in\mathbb R$
$\Vert\vec x\Vert=\sqrt{{x_1}^2+\ldots+{x_n}^2}=\sqrt{\sum\limits_{i=1}^n {x_i}^2}$   è detta **modulo** e **norma** di $\vec x\mskip{24mu}\Vert\vec x\Vert=|\vec x|$

###### Notazioni equivalenti
$\underline x=\vec x= X\mskip{36mu}(x_1,x_2,\ldots,x_n)=\pmatrix{x_1\\x_2\\\vdots\\x_n}\mskip{36mu}\hat x=x_0$

Proprietà
$\begin{cases}\Vert\vec x\Vert\ge0\\\Vert\vec x\Vert=0\Rightarrow \vec x=0\end{cases}$   Positività

$\Vert\lambda\vec x\Vert=|\lambda|\Vert\vec x\Vert$   Omogeneità

$\Vert\vec x+\vec y\Vert\le\Vert\vec x\Vert + \Vert\vec y\Vert$   Distanza traingolare

## Distanza
$\vec x, \vec y\in\mathbb R^n$
Proprietà
- È positiva
	$d(\vec x,\vec y)\ge0$
	$d(\vec x,\vec y)=0\Rightarrow \vec x=\vec y$
- È simmetrica
	$d(\vec x,\vec y)=d(\vec y,\vec x)$
$d(\vec x,\vec y)\le d(\vec x,\vec z) + d(\vec z,\vec y)$

## Prodotto scalare
$\mathbb R^n\cdot \mathbb R^n\to\mathbb R$
$\vec x=(x_1,\ldots,x_n)\mskip{24mu}\vec y=(y_1,\ldots,y_n)$
$\vec x\cdot \vec y=x_1y_1+\ldots+x_ny_n=\sum\limits_{i=1}^n x_iy_i$
Proprietà
$(\alpha_1\vec x_1+\alpha_2\vec x_2)\cdot \vec y=\alpha_1\vec x_1\cdot \vec y+\alpha_2\vec x_2\cdot \vec y$   Bilineare
$\vec x\cdot \vec y = \vec y\cdot \vec x$   Simmetrica
$\vec x\cdot \vec x\ge 0$ Definita positiva

Vale la diseguaglianza di Cauchy-Schwarz
$\vec x,\vec y\in\mathbb R^n$
$|\vec x\cdot \vec y|\le\Vert\vec x\Vert\ \Vert\vec y\Vert$
Caso $\vec x=0$ o $\vec y=0$ è ovvio

Positività
$(\vec x+\lambda\vec y)\cdot (\vec x+\lambda\vec y)\ge0$
$(\vec x+\lambda\vec y)\cdot (\vec x+\lambda\vec y) = \vec x\cdot\vec x+2\lambda(\vec x\cdot\vec y) + \lambda^2\vec y\cdot \vec y=\Vert\vec x\Vert ^2+2\lambda(\vec x\cdot\vec y)+\lambda\Vert\vec y\Vert ^2\ge 0$

$\Delta=4(\vec x\cdot\vec y)^2-4\Vert\vec x\Vert ^2\Vert\vec y\Vert ^2\le0\Rightarrow (\vec x\cdot\vec y)^2\le\Vert\vec x\Vert ^2\Vert\vec y\Vert ^2\Rightarrow(\vec x\cdot\vec y)\le\Vert\vec x\Vert\Vert\vec y\Vert$


# Funzioni da $\mathbb R^n$ in $\mathbb R^m$
$f:D\subset\mathbb R^n\to\mathbb R^m$
$D$   dominio di $f$
$f(D)=\{\vec y\in\mathbb R^n\ \ t.c. \exists \vec x\in D\}$   immagine di $f$      $f(\vec x)=\vec y$
$f(\vec x)\in\mathbb R^n$
$\vec x\in D\subset\mathbb R^n$
$f(\vec x)=\Big(f_1(\vec x),f_2(\vec x),\ldots,f_m(\vec x) \Big)$
$f_i:D\subset\mathbb R^n\to\mathbb R\mskip{12mu}i\in\{1,\ldots,m\}$

Intorno sferico di $\vec x\in\mathbb R^n$
$B(\vec x, r)=\{\vec y\in\mathbb R^n|\Vert\vec x-\vec y\Vert<r\}$

Definizione
$A\subset \mathbb R^n$
$\vec x\in\mathbb R^n$ è punto di accumulazione
Per A   se $\forall\ r>0$
$B(\vec x,r)\setminus\{\vec x\}\cap A\ne\varnothing$

$A\subset \mathbb R^n$ è detto **limitato** se $\exists M>0$

$A\subset \mathbb R^n$ è detto **chiuso** se $A^C=\mathbb R^n\setminus A$ è aperto

$A\subset \mathbb R^n\qquad A$ è chiuso e limitato $\Rightarrow$ A  è compatto

Es
$\mathbb R\ge(a,b)$ è aperto

$\mathbb R>[a,b]$ è chiuso e limitato $\Rightarrow$ è compatto

$[a,b)\subset\mathbb R^n$ non è chiuso, né aperto e limitato

$B(\vec x,r)\subset\mathbb R^n$ è aperta

$\overline{B(\vec x, r)}=\left\{\vec y\in\mathbb R^n | \Vert\vec x-\vec y\Vert\le r\right\}$ è chiuso

$F:A\subset\mathbb R^n\to\mathbb R^m$
Sia $\underbrace{\hat x}_{\mathbb R^n}$ punto di accumulazione
Si dice $\vec l\in\mathbb R^n$ limite di $\vec F$ per $\vec x$ che tende a $\hat x$ se si scrive $\lim\limits_{x\to\hat x}F(\vec x)=\vec l$ se $\forall \varepsilon>0\quad\exists\delta_\varepsilon$ t.c. $\forall\vec x 0<\Vert \vec x-\underline{\hat x}\Vert<\delta_\varepsilon\Rightarrow\Vert F(\vec x)=\vec l\Vert<\varepsilon$
Definizione
$F:D\subset \mathbb R^Nn\to\mathbb R^n$
$\hat x\in D$ di accumulazione
A funzione F è continua in $\hat x$ se $\lim\limits_{x\to\hat x}F(\vec x)=F(\hat x)$   se $\forall \vec x\in A$ la funzione è continua    $\vec F$ è continua in $A$

Esempio
$\tilde f:R^3\setminus\{0\}\to \mathbb R$
$\displaystyle\tilde f(x,y,z)=\frac{xyz^3}{x^4+y^4+z^4}$

$\lim\limits_{\vec x=(x,y,z)\to 0}F(\vec x)=0$

Scelgo $\vec x=t\vec v\qquad \vec x\in\mathbb R^3\setminus\{0\}$
$\vec v=\frac{\vec x}{\Vert\vec x\Vert}\qquad t=\Vert\vec x\Vert$

$\vec v=(a,b,c)$
$\displaystyle\tilde f(\vec x)=\frac{(ta)(tb)(tc)^3}{(ta)^4+(tb)^4+(tc)^4}=\frac{t^5}{t^4}\frac{abc^3}{a^4+b^4+c^4}$
$\displaystyle\exists c\ge\frac{abc^3}{a^4+b^4+c^4}$
$Lc$
$\Vert\tilde f\Vert<ct$
$\Vert\tilde f\Vert<c\Vert\vec x\Vert$

Dato $\varepsilon$
$\delta_\varepsilon=\frac{\varepsilon}{c}$
$0<\Vert\vec x-0\Vert<\delta_\varepsilon\Rightarrow\Vert\tilde f(\vec x)-0\Vert<\cancel c\frac{\varepsilon}{\cancel c}=\varepsilon$

Grafico di $f$
$\left\{x,f(x)\in\mathbb R^{n+m}\vert x\in D\right\}\subset \mathbb R^n\times\mathbb R^m$
Se $n+m\le 3$ possiamo rappresentare $G$

$n=1,m=1$
$f(x)\in\mathbb R\ \forall x\in D\subset\mathbb R$
$\big(x,f(x)\big)\leftarrow y=f(x)$

$n=2,m=1$
$f(x):D\subset\mathbb R^2\to\mathbb R$
$(x_1,x_2)=\underline x\in D$
$f(x_1,x_2)\in\mathbb R$
$\big(x_1,x_2,f(x_1,x_2)\big)\in\mathbb R^3\ \forall (x_1,x_2)\in D$


$f:D\subset\mathbb R\to\mathbb R^2$
$f(t)=\big(t^2,\sin(t)\big)$
$G=\Big\{\big(x,f_1(x),f_2(x)\big)\Big\vert x\in D\Big\}$
$f(D)\leftarrow\text{Immagine}$
$x=f_1(t),\ y=f_2(t)$
$t\in D\mskip{12mu}\big(f_1(t),f_2(t)\big)$

## Campo vettoriale
$f:D\subset\mathbb R^2\to\mathbb R^2$
$f(x_1,x_2)=(-x_1,x_2)$
	$f_1(x_1,x_2)=-x_2$
	$f_2(x_1,x_2)=x_1$

# Calcolo differenziale
Caso $f:D\subset\mathbb R^n\to\mathbb R$

#### Definizione
Derivata parziale di $f$ nel punto $\hat x\in D\mskip{18mu}\hat x\text{ interno a }D\ \ \big(\exists r\big\vert B(\hat x,r)\subset D\big)$
$\displaystyle\frac{\partial f}{\partial x_k}(\hat x)=\lim\limits_{h\to 0}\frac{f\big(\hat x_1,\ldots,\hat x_{k-1},\hat x_k+h, \hat x_{k+1},\ldots,\hat x_n\big)-f(\hat x)}{h}$
$\displaystyle\varphi(y)=f\big(\hat x_1,\hat x_2,\ldots,y,\ldots,\hat x_n\big)\leftarrow\text{tutte trattate come costanti eccetto }y$

Notazione equivalente
$\frac{\partial f}{\partial x_k}(\hat x),\ \partial_k f(\hat x),\ D_{x_n} f$

$\varphi:I\subset\mathbb R\to\mathbb R$

$(x_k,\varphi(x_k)\Rightarrow (1,\varphi'(x_k))$

$v_k=\Big(\underbrace{0,\ldots,0}_{k-1},1,0,\ldots,0,\frac{\partial f}{\partial x_n}(\hat x)\Big)$

$\{v_k\}_{k\in\{1,\ldots,n\}}\text{ sono linearmente indipendenti}$
$\{v_k\}_{k\in\{1,\ldots,n\}}\text{ se la funzione è buona generano l'iperpiano tangente in }\big(\hat x,f(\hat x)\big)\text{ al grafico della funzione}$

Esempio
$f:\mathbb R^2\to\mathbb R$
$f(x,y)=y^{xy}y$
$\displaystyle\frac{\partial f}{\partial x}=y\ e^{xy}y$
$\displaystyle\frac{\partial f}{\partial y}=e^{xy}xy+e^{xy}$

Derivata direzionale

$f:D\subset\mathbb R^n\to\mathbb R$
$\hat x\in D\text{ interno}\mskip{24mu}\text{sia }\hat v]in\mathbb R\mskip{12mu}\hat v\ne 0$
$t\mapsto\hat x+t\hat v$
$\displaystyle\frac{\partial f}{\partial \hat v}(\hat x)=\lim\limits_{t\to 0}\frac{f(\hat x+t\hat v)-f(\hat x)}{t}$

$\displaystyle\frac{\partial f}{\partial x_k}(\hat x)=\frac{\partial f}{\partial \vec {e_k}}(\hat x)$

$\vec{e_k}=\Big(\underbrace{0,\ldots,0}_{k-1},1,\underbrace{0,\ldots,0}_{n-k}\Big)$

### Osservazione
$f:D\subset\mathbb R^n\to\mathbb R$
$\hat x\text{ punto interno a }D$
$\hat v\ne0\mskip{36mu}\hat u=\lambda\hat v\mskip{36mu}\underset{\mathbb R}\lambda\ne0$
$\displaystyle\lambda\frac{\partial f}{\partial \hat v}(\hat x)=\frac{\partial f}{\partial \hat u}(\hat x)$
$\displaystyle\frac{\partial f}{\partial \hat u}(\hat x)=\lim\limits_{t\to0}\frac{f(\hat x+t\hat u)-f(\hat x)}{t}=\lim\limits_{t\to0}\frac{f(\hat x+t\lambda\hat v)-f(\hat x)}{t\lambda}\lambda=\lim\limits_{v\to0}\left(\frac{f(\hat x+h\hat v)-f(\hat x)}{v}\right)=\lambda\frac{\partial f}{\partial \hat v}(\hat x)$


# Differenziale
$g:D\subset \mathbb R\to\mathbb R$
$x\in\mathring D$
$\mathring D\text{ è l'insieme dei punte interni a }D$
$g(x+h)-g(x)=g'(h)+r$
$\displaystyle r=o(h)\mskip{30mu}\lim\limits_{h\to0}\frac{0(h)}{|h|}=0$

$\tilde g(\tilde h)=g(x)+g'(x)(\tilde x-x)$

## Definizione
$f:D\subset\mathbb R^n\to\mathbb R$
$\hat x\in D\text{ punto interno}$
Si dice che $f$ è differenziabile in $\hat x$ se $\exists\ \varphi:\mathbb R^n\to\mathbb R$ (Funzione **lineare**) tale che $f\underbrace{(\hat x+h)}_{\hat x+h\in D}-f(\hat x)=\varphi(h)+0(|h|)\leftarrow\text{(è differenziabile se ammette un piano tangente)}$
$\varphi$ lineare
$\varphi:\mathbb R^n\to\mathbb R$
$a_1,a_2\in\mathbb R\mskip{30mu}h_1,h_2\in\mathbb R^n$
$\varphi(a_1h_1+a_2h_2)=a_1\varphi(h_1)+a_2\varphi(h_2)$

Siccome $\vec\in\mathbb R^n$
$\displaystyle\vec h=\sum\limits_{i=1}^b\beta_i\vec {e_i}$
$\displaystyle\varphi(\vec h)=\sum\limits_{i=1}^b\beta_i\underbrace{\varphi(\vec {e_i})}_{\alpha_i}=\sum\limits_{i=1}^b\beta_i\alpha_i$
$\varphi\leftrightarrow(\alpha_1,\alpha_2,\ldots,\alpha_n)$
$\varphi(h)=\pmatrix{&\alpha&}\pmatrix{\ \\h\\\ }$
$\varphi(h)=(d_{\hat x}f)h\mskip{40mu}d_{\hat x}f\text{ è in differenziale di }f\text{ in }\hat x\text{ ed è l'applicazione lineare }\varphi$

$f\text{ derivabile (ammette derivate parziali)}$
1) Teorema
		$f:D\subset\mathbb R^n\to\mathbb R$
		$\hat x\in \mathring D$
		$f$ differenziabile in $\hat x$
		Allora $f$ è continua in $\hat x$
	Dimostrazione
		$\displaystyle\lim\limits_{x\to\hat x}f(x)\overset?=f(\hat x)$
		$x=\hat x+h\mskip{30mu}x-\hat x=h$
		$\displaystyle\lim\limits_{x\to\hat x}f(\hat x+h)-f(\hat x)=\lim\limits_{x\to\hat x}\underbrace{(d_{\hat x}f)g}_{=0}-\frac{o(h)}{|h|}|h|=0$
2) Teorema
		$f:D\subset\mathbb R^n\to\mathbb R$
		$\hat x\in \mathring D$
		$f$ differenziabile in $\hat x\Rightarrow\ f\text{ ammette le derivate direzionali }\frac{\partial f}{\partial \vec v}(\hat x)\mskip{30mu}\forall\vec v\ne0$
	Inoltre
		$\displaystyle d_{\hat x}f(h)=\sum\limits_{i=1}^n\alpha_i h_i$
		$\vec v=(v_1,\ldots,v_n)$
		$\displaystyle\frac{\partial f}{\partial \vec v}(\hat x)=\sum\limits_{i=1}^n\alpha_iv_i\Rightarrow\frac{\partial f}{\partial x_k}(\hat x)=\frac{\partial f}{\partial \vec{e_k}}=d_k$
		$\displaystyle\frac{\partial f}{\partial \vec v}(\hat x)=\lim\limits{t\to0}\frac{f(\hat x+t\vec v)-f(\vec x)}{t}\overset{??}=$
			$f(\hat x+h)=f(\hat x)=d_{\hat x}f h+0(|h|)\mskip{36mu}h=t\vec v$
			$f(\hat x+t\vec v)-f|\hat x|=d_{\hat x}f(t\vec v)+o(|t\vec v|)=t(d_{\hat x}f)\vec v+o(t)$
		$\displaystyle\frac{f(\hat x+t\vec v)-f(\hat x)}{t}=d_{\hat x}f\vec v+\overset{=0}{\frac{o(t)}t}$
		$\displaystyle\lim\limits_{t\to0}\frac{f(\hat x+t\vec v)-f(\hat x)}t=d_{\hat x}f\vec v$
		Esiste il limite, è uguale a $d_{\hat x}f\vec v$
# Gradiente
$d_{\hat x}f \vec h=\nabla f(\hat x)\vec h$
