Vettori
Somma
	$(a+ib) + (c+id) = (a+c)+i(b+d)$
$Z_1\cdot Z_2 = (a+ib)(c+id) = (ac-bd)+i(ad+bc)$
$i^2=-1$

Un insieme K, con due operazioni + e $\cdot$, si dice un **CAMPO** se:
	+ é assiocativa $\forall a,b,c: (a+b)+c = a+(b+c)$
	+ é commutativa $\forall a,b: a+b = b+a$
	esiste lo 0 $\forall a: a + 0 = 0 + a = a$
	esiste l'opposto $\forall a: a+(-a) = 0$
	$\cdot$ é associativo e commutativo
	esiste l'1 $\forall a: 1\cdot a = a\cdot 1 = a$
	esiste l'inverso $\forall a \ne 0: a\cdot (a^-1) = (a^-1)\cdot a = 1$
	+ e $\cdot$  $\forall a,b,c: a(b+c) = ab+ac$
		$(a+b)c = ac+bc$
	$(a+ib)+(c+id)+(e+if)$
		$(a+c+i(b+d))+(e+if) = (a+ib)+(c+e+i(d+f))$

$(0+i0)+(a+ib)=(0+a)+i(0+b)=a+ib$
$(a+ib)+((-a)+i(-b))=(a-a)+i(b-b)=0+i0$
Se $Z = a+ib$
	$Re(Z)=a$ PARTE REALE
	$Im(Z)=b$ PARTE IMMAGINARIA
	$|Z|=\sqrt{a^2+b^2}$ "MODULO"

Associatività del prodotto
$((a+ib)\cdot (c+id))\cdot (e+if)$
$(ac-bd)+i(ad+bc)\cdot (e+if)$ \[$i^2=-1, i^2bd=-bd$]
$((ac-bd)e-(ad+bc)f)+i((ac-bd)f+(ad+bc)e)$
	$ace-bde-adf-bcf+i(acf-bdf+ade+bce)$

 $(a+ib)\cdot ((c+id)\cdot (e+if))$
 $(a+ib)\cdot (ce-df)+i(cf+de)$
 
$(1+i0)(a+ib) = (1\cdot a)-(0\cdot b)+i(1\cdot b+0\cdot a) = a+ib$
$(a+ib)((c+id)+(e+if)) = (a+ib)(c+id)+(a+ib)(e+if)$

$\frac{1}{a+ib} = \frac{1}{a+ib} \cdot \frac{a-ib}{a-ib} = \frac{a-ib}{a^2+b^2} = \frac{a}{a^2+b^2} + i(\frac{b}{a^2+b^2})$

$Z = a+ib$
$\overline{Z} = a-ib$ "CONIUGATO" di $Z$

coniugato del coniugato -> numero di partenza

$\overline{Z_1+Z_2} = \overline{Z_1}+\overline{Z_2}$

$\overline{Z_1\cdot Z_2} = \overline{Z_1}\cdot \overline{Z_2}$

$\overline{|Z|} = |Z|$

$Z\cdot \overline{Z} = |Z|^2$

$Z \in \mathbb{R} \iff Z = \overline{Z}$

$|Z| = 0 <=> Z = 0$

$Z\cdot \overline{Z}$ e $Z+\overline{Z} \in \mathbb{R}$

$(2+3i)(5-3i) = 10-6i+15i-9i^2 = 19+9i$
$\frac{2+i}{3-i} \cdot  \frac{3+i}{3+i} = \frac{6+2i+3i-1}{9+1} = \frac{5+5i}{10} = \frac{1+i}{2}$

FORMA ALGEBRICA o CARTESIANA (a,b)

FORMA TRIGONOMETRICA ($r,\theta$) ($r$ distanza da origine (reale positivo), $\theta$ angolo antiorario da asse "x")

$a=r\cos{\theta}$
$b=r\sin{\theta}$

$a+ib = r(\cos(\theta)+i\sin(\theta))$
$r=|Z|$
$Arg(Z) = \theta(Z)$

$Z_1=r_1(\cos{\theta_1}+i\sin{\theta_1}) = r_1\cdot \cos{\theta_1} + i\cdot r\sin{\theta_1}$
$Z_2=r_2(\cos{\theta_2}+i\sin{\theta_2}) = r2\cdot \cos{\theta_2} + i\cdot r\cdot \cos{\theta_2}$

$$
\begin{array}{1}
Z_1\cdot Z_2=\\
=r_1\cdot r_2\cdot \cos\theta_1\cdot \cos\theta_2-r_1\cdot r_2\cdot \sin\theta_1\sin\theta_2+i(r_1\cdot r_2\cdot \cos\theta_1\cdot \sin\theta_2+r_1\cdot r_2\cdot \cos\theta_2\cdot \sin\theta_1) =\\
=r_1\cdot r_2((\cos\theta_1\cdot \cos\theta_2-\sin\theta_1\cdot \sin\theta_2)+i(\cos\theta_1\cdot \sin\theta_2+\cos\theta_2\cdot \sin\theta_1)) =\\
=r_1\cdot r_2 (\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2))
\end{array}
$$

$|Z_1\cdot Z_2| = |Z_1|\cdot |Z_2|$
$Arg(Z_1\cdot Z_2) = Arg(Z_1) + Arg(Z_2)$

Moltiplicare per Z corrisponde geometricamente a
	Una dilatazione di fattore $|Z|$
	seguita/preceduta da una
	Rotazione di angolo $Arg(Z)$
	centrate nell'origine

Teorema fondamentale dell'algebra
Ogni polinomio $p(x)\in \mathbb{C}[x]$ con grado $\ge1$ ammette una radice in $\mathbb{C}$ \[Radice: $p(x)=0$]

Corollario:
Sia $p(x)\in \mathbb{C}[X]$ di grado d$\ge 1$
Esistono $\alpha{_1}, \alpha{_2} \in \mathbb{C}$ e $c \in \mathbb{C}$ tale che $p(x)=c(x-\alpha{_1})(x-\alpha{_2})...(x-\alpha{_d})$
Fattorizzazione con Ruffini

Def. Se $\alpha$ è una radice di $p(x)$ la moltiplicità di $\alpha$ (come radice di $p$) è il massimo esponente m tale che $(x-\alpha)^m | p(x)$
*Quante volte viene ripetuto il fattore lineare*

Osservazione
Siano $p(x) \in \mathbb{R}[X]$ e $\alpha \in \mathbb{C}$ tali che $p(\alpha)=0$
Allora $p(\overline{\alpha})=0$
Dim $p(x)=\sum\limits_{J=0}^N{\alpha_J x^J}=(\alpha_0 x^0)+(\alpha_1 x^1)+...+(\alpha_J x^J)$

$p(\alpha)=0$
$p(x)=\sum\limits_{J=0}^N{\alpha_J x^J}$

$\overline{p(\alpha)}=\overline{0}$
$\overline{p(x)}=\overline{\sum\limits_{J=0}^N\alpha_J x^J}=\sum\limits_{J=0}^N \overline{\alpha{_J} x^J} = \sum\limits_{J=0}^N{\alpha_J \overline{x^J}}$

L'insieme delle soluzioni di un polinomio in $\mathbb{R}[X]$ è simmetrico rispetto all'asse reaDle
Le radici **non** reali di un polinomio in $\mathbb{R}[X]$ compaiono a coppie coniugate

### De Moivre
$n\in\mathbb{C}\ \ n\ge1$ intero ($\Re(n)\ge1$)
Cerchiamo le radici di $x^n-z$ in $\mathbb{C}$
$Z=r(\cos\theta+i\sin\theta)$
Sia $W$ una radice di $x^n-z$
$W=\rho(\cos\varphi+i\sin\varphi)$
$W^n=Z\rightarrow\rho^n=r$    $n\cdot\varphi=\theta (\mod 2\pi) \rightarrow \varphi=\frac{\theta}{n}(\mod \frac{2\pi}{n})$
$K\in\mathbb{Z}$
$n\cdot\varphi=\theta+2K\pi \rightarrow \varphi=\frac{\theta}{n}+\frac{2K\pi}{n}$
(basta considerare $K=0,1,2,...,n-1$)
$W_j=\sqrt[n]{r}(\cos(\frac{\theta}{n}+\frac{2J\pi}{n})+i\sin(\frac{\theta}{n}+\frac{2J\pi}{n}))$
I $W_J$ sono i vertici di un n-agono regolare con centro in O
$W^n=Z \rightarrow |W^n|=|W|^n=|Z| \rightarrow |W|=|Z|^{\frac{1}{n}}$

$X^6=-4i \rightarrow 4(\cos\frac{-\pi}{2}+i\sin\frac{-\pi}{2})$

Forma esponenziale
cos'è $e^Z$ con $Z\in\mathbb{C}$?
$e^{io}=\cos\theta+i\sin\theta\ \ \theta\in\mathbb{R}$
