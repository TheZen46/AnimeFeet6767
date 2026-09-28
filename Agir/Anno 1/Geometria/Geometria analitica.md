## Prodotto scalare
$\mathbb{R}^2+\mathbb{R}^2=\mathbb{R}$
$\mathbb{R}^3+\mathbb{R}^3=\mathbb{R}$

$(x_1,y_1)\cdot(x_2,y_2)=x_1x_2+y_1y_2\in\mathbb{R}$ = $\begin{pmatrix}x_1 & y_1 \end{pmatrix}\begin{pmatrix}x_2 \\ y_2\end{pmatrix}$ = $(\vec{v}, \vec{w})$ =

$(x_1,y_1,z_1)\cdot(x_2,y_2,z_2)=x_1x_2+y_1y_2+z_1z_2$

### Proprietà
$\forall v,w_1,w_2\in\mathbb{R}^2,\mathbb{R}^3$
$\forall\lambda,\mu\in\mathbb{R}$
$v\cdot(\lambda w_1+\mu w_2)=\lambda(v\cdot w_1)+\mu(v\cdot w_2)$

$\forall v,w\in\mathbb{R}^2,\mathbb{R}^3$
$v\cdot w=w\cdot v$
$v\perp w$ ($v$ e $w$ sono perpendicolari) $v\cdot w=0$

$v=(x_1,y_1,z_1)$
$w=(x_2,y_2,z_2)$
$v\times w$ oppure $v\wedge w$ $\in\mathbb{R}^3$
$(y_1z_2-y_2z_1,-(x_1z_2-x_2z_1), y_1z_2-y_2z_1)$ (determinant-ish)

$\begin{pmatrix}x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2\end{pmatrix}$

$v\wedge w\perp v$
	$\perp w$
$(v\wedge w)\cdot v=\begin{pmatrix}x_1&y_1&z_1\\x_1&y_1&z_1\\x_2&y_2&z_2\end{pmatrix}=0$

$\forall v,w_1,w_2\in\mathbb{R}^3$     $\forall\lambda,\mu\in\mathbb{R}$
$v\wedge(\lambda w_1+\mu w_2)=\lambda(v\wedge w_1)+\mu(v\wedge w_2$
$\forall v,w\in\mathbb{R}^3$    $v\wedge w=-w\vee v$

$|v\wedge w| = |v|\ |w|\ sin(\theta)$

### Identità di Lagrange
$|v\wedge w|^2=|v|^2\cdot|w|^2-(v\cdot w)^2$

$v\wedge w = 0 \iff v\parallel w$

### Triangolo

$S=\frac{1}{2}|(B-A)\wedge(C-A)|$

"prodotto misto" di $v_1,v_2,v_3$
$v_1\cdot(v_2\wedge v_3)$

$\begin{pmatrix}x_1&y_1&z_1\\x_2&y_2&z_2\\x_3&y_3&z_3\end{pmatrix}$ è 0 se e solo se i 3 vettori sono complanari

 $v=(1,1,1)$ e $w=(2,1,1)$
Trovare un vettore perpendicolare a $v$ e $w$ e di modulo 2
$v^1=v\wedge w$
$|v^1| = \pm\frac{2}{v\wedge w}(v\wedge w)$

$v\wedge w=\begin{pmatrix}1&1&1\\2&1&1\end{pmatrix} \rightarrow (0, -(1-2), 1-2) = (0,1,-1)$
$|v^1|=\pm\frac{2}{\sqrt2}(0,1,-1)=\pm(0,\frac{2}{\sqrt2},\frac{-2}{\sqrt2})$

Calcolare l'angolo tra $v=(2,-2,1)$ e $v^1=(0,1,-1)$
$v\cdot v^1=2\cdot0+(-2)\cdot1+1(-1)=-2-1=-3=|v||v^1|cos\theta$
$|v|=\sqrt{4+4+1}=3$
$|v^1|=\sqrt{0+1+1}=\sqrt{2}$
$\cos\theta=\frac{v\cdot v^1}{|v||v^1}=\frac{-3}{3\sqrt2}=\frac{-1}{\sqrt2}$
$\theta=\arccos\frac{-1}{sqrt2}$

$v=(1,2,1)$
$v^1=(2,0,-1)$
Calcoliamo un vettore non complementare con $v$ e $v^1$
$v\wedge v^1=(-2,3,4)$


Dati $A=(1,0,2)$ e $B=(3,1,0)$, trovare un punto sull'asse Z tale che il triangolo ABC abbia area 10

$10=\frac{1}{2}|(C-A)\wedge(B-A)|$

$C=(0,0,2)$
$C-A=(-1,0,Z-2)$
$B-A=(2,1,-2)$
$(C-A)\wedge(B-A)=(2-Z,-(2,2(Z-2),-1)=(2-Z,2Z-6,-1)$
$|(C-A)\wedge(B-A)|^2=(2-Z)^2+(2Z-6)^2+1$
Cerchiamo Z tale che $(2-Z)^2+(2Z-6)^2+1=400$
$4-4Z+Z^2+4Z^2-24Z+36+1=400 \rightarrow 5Z^2-28Z-359=0$
$Z=\frac{28\pm\sqrt{28^2+4\cdot5\cdot359}}{10}$

$A=(1,0,0)$,  $B=(2,1,1)$,  $C=(1,-1,0)$,  $D=(0,1,0)$
Quanti punti sono complementari?

$B-A=(1,1,1)$
$C-A=(0,-1,0)$
$D-A=(-1,1,0)$

$\left|\begin{array}\\1&1&1\\0&-1&0\\-1&1&0\end{array}\right|=\left|\begin{array}\\0&-1\\-1&1\end{array}\right|=-1\ne0$



$A, B, P \in \mathbb{R}^3$
$A, B, P$ sono allineati $\iff (P-A)\wedge(P-B)=0$
$\exists\ t\in\mathbb{R}\ \ \ \ P-A=t(P-B)$

$A=(-1,2,0)$
$B=(1,1,1)$
$P=(x,y,z)\in$ retta per $A$ e $B \iff (x+1,y-2,z)\wedge(x-1,y-1,z-1)=0 \rightarrow ((y-2)(z-1)-z(y-1), -(x+1)(z-1)-z(x-1)),(x+1)(y-1)-(y-z)(x-1)$

$\begin{cases}-y-2z+2+z=0\\x-z+1-z=0\\-x+y-1+2x+y-2=0\end{cases}$

$\begin{cases}y+z=2\\x-2z=-1\\x+2y=3\end{cases}$

$R_3=R_2+2R_1$

$P-A=t(P-B)$
$P=t(P-B)+A$
La retta è $\{t(P-B)+A|t\in\mathbb{R}\}$
$$
\left(
\begin{array}\
x\\y\\z
\end{array}
\right)
=
t
\left(
\begin{array}\
2\\-1\\1
\end{array}
\right)
+
\left(
\begin{array}\
-1\\2\\0
\end{array}
\right)
\ \ \ \
t\in\mathbb{R}
$$

$\begin{cases}x=2t-1\\y=1+1t\\z=2-1t\end{cases}\ \ \ \ t\in\mathbb{R}\leftrightarrow\begin{cases}x-2y=-1\\y+z=3\end{cases}$

$t=y-1$
$x=2(y-1)+1$
$z=2-(y-1)$


$$
\left(
\begin{array}{ccc|c}\
0 & 1 & 1 & 2\\
1 & 0 & -2 & -1\\
1 & 2 & 0 & 3
\end{array}
\right)
\rightarrow
\left(
\begin{array}{ccc|c}\
0 & 1 & 1 & 2\\
1 & 0 & -2 & -1\\
0 & 0 & 0 & 0
\end{array}
\right)
$$


Cerchiamo il piano $\pi$ passante per:
$A=(-1,1,1)$
$B=(1,1,2)$
$C=(2,0,1)$

$\left|\begin{array}\x-1 & y-1 & z-1\\0 & 0 & 1\\1 & -1 & 0\end{array}\right|=0$

$-(x-1)-(y-1)=0$
$x+y=2$
$v_\pi=(1,1,0)$

$x=2-s$
$y=s$
$z=t$
$s,t\in\mathbb{R}$

Un vettore direzionale é $(B-A)\wedge(C-A) = (1,1,0)$
$x+y=d$
$2=x+y=d$

$\begin{cases}x=0s+1t+1\\y=0s+(-1)t+1\\z=1s+0t+1\end{cases}$

$ax+by+cz=d$
$a'x+b'y+c'z=d'$

Due rette che non si intersecano sono:
- Parallele se esiste un piano che le contiene
- Sghembe se non esiste un piano che le contiene

$r_1\begin{cases}-\\-\end{cases}$

$r_2\begin{cases}-\\-\end{cases}$

$\left(\begin{array}\ -\\-\\-\\-\end{array}\right)\rightarrow\begin{array}\ -\\▭\\-\\▭\end{array}$

Parallele
- $\text{rk}A=2$
- $\text{rk}AB=3$

Sghembe
- $\text{rk}A=3$
- $\text{rk}AB=4$

Se $r_1,r_2$ sono sghembe, esistono due piani $\pi_1,\pi_2$ paralleli tale che $r_1\subseteq\pi_1$; $r_2\subseteq\pi_2$

$r_1\begin{cases}2x-z+1=0\\x-2y+3z=0\end{cases}$

$r_2\begin{cases}x-y=0\\x+y+z=0\end{cases}$

$$
\left(
\begin{array}\
2 & 0 & -1 & -1 \\
1 & -2 & 3 & 0 \\
1 & -1 & 0 & 0 \\
1 & 1 & 1 & 0
\end{array}
\right)
\rightarrow
\left(
\begin{array}\
2 & 0 & -1 & -1 \\
0 & -2 & \frac{7}{2} & \frac{1}{2} \\
0 & -1 & \frac{1}{2} & \frac{1}{2} \\
0 & 1 & \frac{3}{2} & \frac{1}{2}
\end{array}
\right)
\rightarrow
\left(
\begin{array}\
2 & 0 & -1 & -1 \\
0 & -2 & \frac{7}{2} & \frac{1}{2} \\
0 & 0 & -\frac{5}{4} & \frac{1}{4} \\
0 & 0 & \frac{13}{4} & \frac{3}{4}
\end{array}
\right)
$$
$\text{rk}=4$, quindi sghembe

$P(1,2,0)$

$r\begin{cases}x+2y-z=0\\x+y=1\end{cases}$

$r'\begin{cases}x=t+1\\y=2t+2\\z=-t\end{cases}\ \ \ \ t\in\mathbb{R}$


# Distanza punto-piano
Punto $P=(x_p,y_p,z_p)$
Piano $\pi$
$x\cdot v_\pi=d$
$x=(x,y,z)$
$v_\pi=(a,b,c)$
$ax+by+cz=d$

Retta per $p$ e $\perp$ a $\pi$
$x=tv_\pi+P\ \ \ \ t\in\mathbb{R}$

$\begin{cases}x=ta+x_p\\y=tb+y_p\\z=tc+z_p\end{cases}\ \ \ \ t\in\mathbb{R}$

$(tv+P)\cdot v_\pi=d\longrightarrow t||v_\pi||^2+P\cdot v_\pi=d\longrightarrow t=\frac{d-P\cdot v_\pi}{||v_\pi||^2}\longrightarrow P'=\frac{d-P\cdot v_\pi}{||v_\pi||^2}+P$
$d(p,p')^2=||P'-P||^2=(P'-P)\cdot(P'-P)=||\frac{d-p\cdot v_\pi}{||v_\pi||^2\cdot v_\pi}||^2=\frac{(d-p\cdot v_\pi)^2}{||v_\pi||^4}||v_\pi||^2=\frac{(d-p\cdot v_\pi)^2}{||v_\pi||^2}$


$P=(2,1,2)$
$\pi=x-y+2z=2$
$d(P,\pi)=\frac{|2-1+4-2|}{\sqrt{1+1+4}}=\frac3{\sqrt6}$

## Sfera
$C=(x_0,y_0,z_0)$
$d(P,C)^2=(x-x_0)^2+(y-y_0)^2+(z-z_0)^2=R^2$

$x^2+y^2+z^2-2x+4y+2=0$
###### Centro e raggio della sfera
$(x-1)^2+(y+2)^2+z^2=3$
$C=(1,-2,0)$
$R=\sqrt3$

$d(C,\pi)>R$ esterno
$d(C,\pi)=R$ tangente
$d(C,\pi)<R$ secante

###### Posizione rispetto al piano
$x^2+y^2+z^2-2x+4y+2=0$
$x+y+z=0$

Sostituisci C nel piano
$\frac{|1-2+0|}{\sqrt{1+1+1}}=\frac{1}{\sqrt3} < 3$ secante

###### Centro e raggio di $\gamma$
C'è la proiezione di C su $\pi$

$r\begin{cases}x=t+1\\y=t-2\\z=t\end{cases}\ \ \ \ t\in\mathbb{R}$

$C'=(\frac43,\frac{-5}3,\frac13)$

$r=\sqrt{R^2-d(c,c')^2}=\sqrt{3-\frac13}=\frac83$

# Spazi vettoriali
(Su un campo $\mathbb{K}$)

V con due operazioni

$+_v:V\times V\rightarrow V$
- Associativa
- Commutativa
- Esiste 0
	- Ogni vettore ha un opposto
Moltiplicazione per scalare
$\cdot_v:\mathbb{K}\times V\rightarrow V$
- Associatività $\forall\lambda,\mu\in\mathbb{K}\ \ \forall v\in V$ $(\lambda\cdot_k\mu)\cdot_v v=\lambda\cdot_v(\mu\cdot t)$
- Distributiva $\forall\lambda,\mu\in\mathbb{K}\ \ \forall v\in V$ $\lambda\cdot_v(v+_v w)=\lambda\cdot_v v+_v \lambda\cdot_v w$
- $\forall\lambda,\mu\in\mathbb{K}\ \ \forall v\in V$ $(\lambda+_k\mu)\cdot_v v=\lambda\cdot_v v+_v \mu\cdot_v v$
- $\begin{array}{c}0\cdot_v v=0\\1\cdot_v v=v\end{array}$

$\begin{array}{c}\mathbb{R}^n\\\mathbb{C}^n\end{array}$

$\begin{array}{c}\mathbb{R}[X] \\ \mathbb{C}[X]\end{array}$

$\begin{array}{c}\text{Mat}_{m\times n}(\mathbb{R})\\\text{Mat}_{m\times n}(\mathbb{C})\end{array}$


$\begin{array}{c}V=\mathbb{R^4}\\(1,2,4,2)+_v3\cdot_v(1,1,1,1)=(4,5,7,5)\end{array}$

Una combinazione lineare di vettori $v_1,\ldots,v_n\in V$ con coefficienti $\lambda_1,\ldots,\lambda_n\in\mathbb{K}$ è in'espressione del tipo $\lambda_1 v_1+\ldots+\lambda_n v_n\in V$

## Linearmente indipendenti
Def.
$v_1,\ldots,v_n\in V$ si dicono **linearmente indipendenti** se l'unica combinazione lineare $= 0$ è quella con $\lambda_1=\ldots=\lambda_n=0$ $\forall\lambda_1,\ldots,lambda_n\in\mathbb{K}\ \ \lambda_1 v_1+\ldots+\lambda_n v_n=0\Rightarrow\lambda_1=\ldots=\lambda_n=0$

$\begin{array}{c}V=\mathbb{R^3}\\\left(\begin{array}{c}1\\1\\2\end{array}\right)\cdot\left(\begin{array}{c}1\\0\\1\end{array}\right)\end{array}$

$\lambda_1\left(\begin{array}{c}1\\1\\2\end{array}\right)\cdot\lambda_2\left(\begin{array}{c}1\\0\\1\end{array}\right)=0$

$\begin{cases}\lambda_1+\lambda_2=0\\\lambda_1+0\lambda_2=0\\2\lambda_1+\lambda_2=0\end{cases}$

Rouché-Capelli: rango 2 $\rightarrow$ unica soluzione $\lambda_1=\lambda_2=0$

$\left(\begin{array}{c}1\\2\\1\end{array}\right)\cdot\left(\begin{array}{c}0\\1\\2\end{array}\right)\cdot\left(\begin{array}{c}1\\3\\3\end{array}\right)$

$\lambda_1\left(\begin{array}{c}1\\2\\1\end{array}\right)\cdot\lambda_2\left(\begin{array}{c}0\\1\\2\end{array}\right)\cdot\lambda_3\left(\begin{array}{c}1\\3\\3\end{array}\right)=0$

$\left(\begin{array}{c}1&0&1\\2&1&3\\1&2&3\end{array}\right)$

$\text{det}=(3-6)+(6-3)=0$
Infinite soluzioni, non sono indipendenti

V spazio vettoriale
$W\subseteq V$    W è un **sottospazio (vettoriale)** di V se $\forall v,w\in W \text{ e } \forall\lambda,\mu\in\mathbb{K}\ \ \ \ \lambda v+\mu w\in W \text{ e } W\ne0$

$V=\mathbb{R}[X]$
$W=\{p\in\mathbb{R}[X]|p(1)=0]\}$
$0\in W$
$\forall\lambda,\mu\in\mathbb{R}\ \ \forall\ p,q\in W$
$(\lambda p+\mu q)(1)=\lambda p(1)+\mu q(1)=\lambda\cdot0+\mu\cdot0=0$

$\mathbb{R}^3$
$\pi\ \ 2x+2y-z=0$
$r\begin{cases}x=2t+1\\y=t-1\\z=t\end{cases}\ \ \ \ t\in\mathbb{R}$

Verifichiamo se soddisfa la condizione
- Non è vuoto
- Siano $A,B\in\pi$ e $\lambda,\mu\in\mathbb{R}$
	$\lambda A+\mu B=\lambda(x_a,y_a,z_a)+\mu(x_b,y_b,z_b)=\lambda x_a+\mu x_b,\lambda y_a+\mu y_b,\lambda z_a+\mu z_b$
	$2(\lambda x_a+\mu x_b)+2(\lambda y_a+\mu y_b)-(\lambda z_a+\mu z_b)\stackrel{?}{=}0 \longrightarrow \lambda(2x_a+2y_a-z_a)+\mu(2x_b+2y_b-z_b)\stackrel{?}{=}0 \longrightarrow \lambda0+\mu0\stackrel{?}{=}0\longrightarrow 0=0\checkmark$

$A,B\in r$    $\lambda,\mu\in\mathbb{R}$

$\left(\begin{array}{c}2t+1\\t-1\\t\end{array}\right)\cdot\left(\begin{array}{c}2\mu+1\\u-1\\u\end{array}\right)$    $\left(\begin{array}{c}\lambda(2t+1)+\mu(2u+1)\\\lambda(t-1)+\mu(u-1)\\\lambda t+\mu u\end{array}\right)$

$0\notin r$    $r$ non è un sottospazio vettoriale
L'origine appartiene ad ogni sottospazio vettoriale

$\begin{array}{c}A\in\text{Mat}_{m\times n}(\mathbb{K})\\AX=0\end{array}$   Sistema lineare omogeneo

$S=\{v\in\mathbb{K}^n|Av=0\}$   L'insieme delle soluzioni
S è un sottospazio vettoriale di $\mathbb{K}^n$

Siano $\pi,v\in S$    $\lambda,\mu\in\mathbb{K}$
$\lambda v+\mu w\stackrel{?}{=}\in S$
$A(\lambda v+\mu w)\stackrel{?}{=}\in 0$
$\lambda Av(=0)+\mu Aw(=0)$

$AX=B$    $\begin{array}{c}A\in\text{Mat}_{m\times n}\\B\in\mathbb{K}^m\end{array}$
$S=\{v\in\mathbb{K}^n|Av=B\}$    Insieme delle soluzioni
$S_0=\{v\in\mathbb{K}^n|Av=0\}$    Soluzione del sistema omogeneo

Sia $w\in S$
Allora $S=\{v+w\in\mathbb{K}^n|v\in S_0\}$


$A\in\text{Mat}_{m\times n}$
$AX=B$    $B\in\mathbb{R}^n$
$X=(x_1,\ldots,x_m)\in\mathbb{R}^n$

$S=\{v\in\mathbb{R}^n|Av=B\}\subseteq\mathbb{R}^n$   insieme delle soluzioni
$S_0=\{v\in\mathbb{R}^n|Av=o\}\subseteq\mathbb{R}^n$
- $\forall v\in S\ \ \forall w\in S_0\ \ v+w\in S$
- $\forall v,w\in S\ \ v-w\in S_0$
$A(v+w)=Av+Aw=B+0=B$
$A(v-w)=Av-Aw=B-B=0$



$V$ spazio vettoriale
$v_1,\ldots,v_k\in V$
Il sottospazio vettoriale generato da $v_1,\ldots,v_k$ è l'insieme delle combinazioni lineari di $v_1,\ldots,v_k$
Equivalentemente, è il più piccolo sottospazio vettoriale di $V$ che contiene $v_1,\ldots,v_k$
Lo indichiamo:
	$<v_1,\ldots,v_k>$
	$\text{Span}(v_1,\ldots,v_k)$
	$\text{L}(v_1,\ldots,v_k)$
$\left(\begin{array}{c}1\\0\end{array}\right), \left(\begin{array}{c}0\\1\end{array}\right)\in\mathbb{R}$
$<\left(\begin{array}{c}1\\0\end{array}\right),\left(\begin{array}{c}0\\1\end{array}\right)>=\mathbb{R}^2$
$\left(\begin{array}{c}a\\b\end{array}\right)=a\left(\begin{array}{c}1\\0\end{array}\right)+b\left(\begin{array}{c}0\\1\end{array}\right)$
$<\left(\begin{array}{c}1\\2\end{array}\right),\left(\begin{array}{c}2\\3\end{array}\right)>=\mathbb{R}^2$
$\left(\begin{array}{c}a\\b\end{array}\right)=\lambda_1\left(\begin{array}{c}1\\2\end{array}\right)+\lambda_2\left(\begin{array}{c}2\\3\end{array}\right)$

$\begin{cases}\lambda_1+2\lambda_2=a\\2\lambda_1+3\lambda_3\end{cases}$

$\left|\begin{array}{c}1&2\\2&3\end{array}\right|=3-4\ne0$



$<\left(\begin{array}{c}1\\2\end{array}\right),\left(\begin{array}{c}2\\3\end{array}\right),\left(\begin{array}{c}5\\6\end{array}\right)>=\mathbb{R}^2$
$<\left(\begin{array}{c}1\\2\end{array}\right)>\ne\mathbb{R}^2$
$\left(\begin{array}{c}1\\0\end{array}\right)\ne<\left(\begin{array}{c}1\\2\end{array}\right)>$



Sia $W$ un sottospazio vettoriale di $V$
Un insieme di generatore per $W$ è un insieme di vettori $v_1,\ldots,v_k\in W$ tale che $W=<v_1,\ldots,v_k>$

### Osservazione

$v_1,\ldots,v_k\in V$ sono linearmente indipendenti $\iff$ almeno uno di essi è combinazione lineare degli altri
$v_k=\lambda_1 v_1+\ldots+\lambda_{k-1} v_{k-1}$
$\lambda_1 v_1+\ldots+\lambda_{k-1} v_{k-1}-v_k=0$

Esistono coefficienti non tutti $=0$ tale che $\lambda_1 v_1+\ldots+\lambda_{k-1} v_{k-1}=0$
Se $\lambda_i=0$    $v_1=-\frac{\lambda_1}{\lambda_i}v_1-\frac{\lambda_2}{\lambda_i}v_2\ldots-\frac{\lambda_K}{\lambda_i}v_K \leftarrow \text{escluso termine i}$

$v_1,\ldots,v_k\in\mathbb{R}$ sono linearmente indipendenti $\iff$ $\text{rk}\left(\begin{array}{c}|&&|\\v_1&\ldots&v_k\\|&&|\end{array}\right)=K$
### Definizione
Una **base** di uno spazio vettoriale è un insieme di generatori linearmente indipendenti
$v_1=\left(\begin{array}{c}1\\1\\1\end{array}\right)\ \ \ \ v_2=\left(\begin{array}{c}1\\0\\1\end{array}\right)$
$\text{rk}\left(\begin{array}{c}1&&1\\1&&0\\1&&1\end{array}\right)=2$    sono linearmente indipendenti

$\left(\begin{array}{cc|c}1&1&a\\1&0&b\\1&1&c\end{array}\right)$

$v_1,v_2,\left(\begin{array}{c}1\\0\\0\end{array}\right)$ è una base di $\mathbb{R}^3$
$\left(\begin{array}{c}1\\2\\1\end{array}\right)\left(\begin{array}{c}1\\1\\0\end{array}\right)\left(\begin{array}{c}-1\\0\\1\end{array}\right)\left(\begin{array}{c}2\\0\\2\end{array}\right)\left(\begin{array}{c}-1\\-1\\0\end{array}\right)$    sono un insieme di generatori?

$\left(\begin{array}{c}1&1&-1&2&-1\\2&1&0&0&-1\\1&0&1&2&0\end{array}\right)$ ha rango 3

Dato V spazio vettoriale
- Esiste sempre una base di V
- Due basi di V hanno sempre lo stesso numero di elementi, chiamiamo questo numero la **dimensione** di V $\rightarrow \dim V,\ \ \dim_K V$

Se $v_1,\ldots,v_k$ sono linearmente indipendenti e $v_{k+1}\notin<v1,\ldots,v_k>$ allora $v_1,\ldots,v_{k+1}$ sono linearmente indipendenti
Se non lo fossero, esisterebbero dei coefficienti $\lambda_1,\ldots,\lambda_{k+1}$ non tutti $=0$ tale che $\lambda_1 v_1+\ldots+\lambda_{k+1} v_{k+1}=0$



Sia $V$ uno spazio vettoriale e sia $v_1,\ldots, v_n$ una base di $V$
Ogni vettore di $V$ si scrive in modo unico come combinazione lineare di $v_1,\ldots,v_n$
$\exists!\lambda_1,\ldots,\lambda_n\in\mathbb{K}$ tale che $v=\lambda_1 v_+\ldots+\lambda_n v_n$

Verifichiamo l'unicità $\lambda_1,\ldots,\lambda_n, \mu_1,\ldots,\mu_n\in\mathbb{K}$
$\lambda_1 v_+\ldots+\lambda_n v_n=\mu_1 v_+\ldots+\mu v_n \longrightarrow (\lambda_1-\mu_1)v_1+\ldots+(\lambda_n-\mu-n)v_n=0$
Quindi $\lambda_1-\mu_1=\ldots=\lambda_n-\mu_n=0$ perché $v_1,\ldots,v_n$, i coefficienti $\lambda_1,\ldots,\lambda_n$ tale che $v=\sum\limits_{i=1}^{n}\lambda_1\cdot\mu_1$ sono le **coordinate** di $v$ rispetto a $v_1,\ldots,v_n$



Sia $V$ uno spazio vettoriale, $v_1,\ldots,v_n$ una base e $w_1,\ldots,w_n$ un insieme di vettori lineari indipendenti
Allora $r\le n$
$\lambda_1 v_+\ldots+\lambda_n v_n=0$
$W_i=\sum\limits_{J=1}^{n}a_{iJ}\cdot v_J$    $a_{ij}$ le coordinate di $W_i$ rispetto alla base $v_1,\ldots,v_n$
$\sum\limits_{i=1}^{r}\lambda_i\sum\limits_{J=1}^{n}a_{iJ}\cdot v_J=0  \longrightarrow  \sum\limits_{J=1}^{n}(\sum\limits_{i=1}^{r}\lambda_i a_{iJ})v_J=0$
Quindi $\forall J=1, n$    $\sum\limits_{i=1}^{r}\lambda_i\cdot a_{iJ}=0$ perché i $v_j$ sono linearmente indipendenti
$A=(a_{iJ})_{\begin{array}{c}i=1,\ r\\J=1,\ n\end{array}}$
$A\left(\begin{array}{c}\lambda_1\\\ldots\\\lambda_r\end{array}\right)=0$

Ma allora il numero di righe della matrice deve essere $\ge$ del numero di colonne, altrimenti per Rouché-Capelli il sistema avrebbe $\infty$ soluzioni, contro l'indipendenza dei $W_1$



$V=\mathbb{R}[x]_{\le1}=\{p(x)\in\mathbb{R}[x]\text{ di grado }\le1\}$
$p_1=2+x\ \  p_2=3+2x$
Sono una base?
$\lambda_1 p_1+\lambda_2 p_2=0$
$v_1,\ldots,v_n\in V$ sono linearmente indipendenti se $\forall\lambda_1,\ldots,\lambda_n\ \ \ \ \lambda_1 v_1+\ldots+\lambda_n v_n=0\Rightarrow\lambda_1=\ldots=\lambda_n=0$
$\lambda_1(2+x)+\lambda_2(3+2x)=0$
$(\lambda_1+2\lambda_2)X+(2\lambda_1+3\lambda_2)=0$
$\begin{cases}\lambda_1+2\lambda_2=0\\2\lambda_1+3\lambda_2=0\end{cases}$    $\left(\begin{array}{c}1&2\\2&3\end{array}\right)$

Prendo $q(x)$ qualunque in $V$
$\lambda_1 p_1+\lambda_2 p_2=q$
$\lambda_1(2+x)+\lambda_2(3+2x)=ax+b$
$(\lambda_1+2\lambda_2)X+(2\lambda_1+3\lambda_2)=ax+b$
$\begin{cases}\lambda_1+2\lambda_2=a\\2\lambda_1+3\lambda_2=b\end{cases}$    $\left(\begin{array}{cc|c}1&2&a\\2&3&b\end{array}\right)$



$W_1=x+1$
$W_2=-3$

$W_1=a_{11}p_1+a_{12}p_2 \Longrightarrow x+1=a_{11}(2+x)+a_{12}(3+2x) \longrightarrow x+1=(a_{11}+2a_{12})x+(2a_{11}+3a_{12})$
$\left(\begin{array}{cc|c}1&2&1\\2&3&1\end{array}\right)$
$\left(\begin{array}{c}1&2\\2&3\end{array}\right)^{-1}=\left(\begin{array}{c}-3&2\\2&1\end{array}\right)$
$\left(\begin{array}{c}a_{11}\\a_{12}\end{array}\right)=\left(\begin{array}{c}-3&2\\2&1\end{array}\right)\left(\begin{array}{c}1\\1\end{array}\right)=\left(\begin{array}{c}-1\\1\end{array}\right)$

$W_2=-3=(2+x)+a_{12}(3+2x) \longrightarrow x+1=(a_{11}+2a_{12})x+(2a_{11}+3a_{12})$



Sia $V$ uno spazio vettoriale
Sia $v_1,\ldots, v_n$ una base
Siano $W_1,\ldots,W_r$ dei generatori di $V$
Allora $r\ge n$
$\forall u\in V\ \ \exists\lambda_1,\ldots,\lambda_r\in\mathbb{K}$ tale che $\sum\limits_{i=1}^{r}\lambda_i W_i=u$    $u=\sum\limits_{J=1}^{n}b_J v_J$
$\sum\limits_{i=1}^{r}\lambda_1\sum\limits_{J=1}^{n}a_{iJ}v_J=\sum\limits_{J=1}^{n}b_J v_J$
$\sum\limits_{J=1}^{n}(\sum\limits_{i=1}^{r}\lambda_1 a_{iJ})v_J=\sum\limits_{J=1}^{n}b_J v_J$--
$\forall J=1,\ n\ \ \sum\limits_{i=1}^{r}\lambda_i a_{iJ}=b_J$  $(A|B)$

Due basi di uno spazio vettoriale hanno lo stesso numero di elementi
$v_1,\ldots,v_n$    $w_1,\ldots,w_r$    $\begin{array}{c}r\ge n\\n\ge r\end{array}\Rightarrow r=n$
$\mathbb{R}^n\ \ e_i\ \ \left(\begin{array}{c}0\\\vdots\\1\\0\\\vdots\end{array}\right)\leftarrow i$    $e_1, \ldots, e_v$ formano una base detta la **base canonica** di $\mathbb{R}^n$
Verifichiamo che l'insieme delle soluzioni del sistema lineare omogeneo $AX=0$ $a\in\text{Mat}_{m\times x}$ è uno spazio vettoriale di dimensione $n-\text{rk}A$



# Sottospazi vettoriali
## Intersezione
$V$ spazio vettoriale
$W_1,W_2\in V$ sottospazi
Allora $W_1\cap W_2$ è un sottospazio

$\mathbb{R}^4$
$W_1=<\begin{array}{c}v_1\\\left(\begin{array}{c}1\\1\\0\\1\end{array}\right)\end{array}, \begin{array}{c}v_2\\\left(\begin{array}{c}1\\0\\1\\0\end{array}\right)\end{array}, \begin{array}{c}v_3\\\left(\begin{array}{c}2\\1\\0\\-1\end{array}\right)\end{array}>$

$W_2=<\begin{array}{c}\left(\begin{array}{c}1\\2\\3\\4\end{array}\right)\\v_4\end{array}, \begin{array}{c}\left(\begin{array}{c}1\\2\\1\\2\end{array}\right)\\v_5\end{array}>$

$W_1\cap W_2=$

$a_1 v_1+a_2 v_2+a_3 v_3+a_4 v_4+a_5 v_5=0$
$a_1 v_1+a_2 v_2+a_3 v_3=-a_4 v_4-a_5 v_5$

$av_1+bv_2+cv_3=dv_4+ev_5$
$\left(\begin{array}{c}1&1&2&-1&-1\\1&0&1&-2&-2\\0&1&0&-3&-1\\1&0&-1&-4&-2\end{array}\right)$

$$
\left(\begin{array}{c}
1&1&2&-1&-1\\
1&0&1&-2&-2\\
0&1&0&-3&-1\\
1&0&-1&-4&-2
\end{array}\right)
\overset{\begin{array}{c}R_2\Rightarrow R_2-R_1\\R_4\Rightarrow R_4-R_1\end{array}}\longrightarrow
\left(\begin{array}{c}
1&1&2&-1&-1\\
0&-1&-1&-1&-1\\
0&1&0&-3&-1\\
0&-1&-3&-3&-1
\end{array}\right)
\overset{\begin{array}{c}R_3\Rightarrow R_3+R_2\\R_4\Rightarrow R_4-R_2\end{array}}\longrightarrow
\left(\begin{array}{c}
1&1&2&-1&-1\\
0&-1&-1&-1&-1\\
0&0&-1&-4&-2\\
0&0&-2&-2&0
\end{array}\right)
\overset{R_4\Rightarrow R_4-2R_2}\longrightarrow
\left(\begin{array}{c}
1&1&2&-1&-1\\
0&-1&-1&-1&-1\\
0&0&-1&-4&-2\\
0&0&0&6&4
\end{array}\right)
\overset{R_4\Rightarrow \frac12R_4}\longrightarrow
\left(\begin{array}{c}
1&1&2&-1&-1\\
0&-1&-1&-1&-1\\
0&0&-1&-4&-2\\
0&0&0&3&2
\end{array}\right)
$$

$W_1\cap W_2=\{(-\frac23e)v_4+ev_5|e\in\mathbb{R}\}$

$<-\frac23v_4+v_5>=<\left(\begin{array}{c}1-\frac23\\2-(\frac23)2\\1-(\frac23)3\\2-(\frac23)4\end{array}\right)>=<\left(\begin{array}{c}\frac13\\\frac23\\-1\\-\frac23\end{array}\right)>=<\left(\begin{array}{c}1\\2\\-3\\-2\end{array}\right)>$



## Unione
$W_1\cup W_2$
L'unione di due spazi vettoriale non è in generale un sottospazio vettoriale

$\mathbb{R}^2$
$V=<\left(\begin{array}{c}1\\2\end{array}\right)>$
$W=<\left(\begin{array}{c}1\\0\end{array}\right)>$



$W_1+W_2$ si dice **somma** di $W_1$ e $W_2$
Il più piccolo (rispetto a $\subseteq$) sottospazio di $V$ che contiene $W_1\cup W_2$
$W_1+W_2=\{v_1+v_2\ |\ v_1\in W_1,v_2\in W_2\}$

$W_1=<v_1,\ldots,v_r>$
$W_2=<w_1,\ldots,w_j>$
$W_1+W_2=<v_1,\ldots,v_r,w_1,\ldots,w_j>$



## Somma diretta
$W_1\oplus W_2$
$W_1+W_2=V$ e $W_1\cap W_2=\{0\}  \longrightarrow  \forall\ v\in V\ \exists!\ w_1\in W_1\ \exists!\ w_2\in W_2$
$v=w_1+w_2$

## Formula di Grassmann
$V$ spazio vettoriale
$W_1,W_2\subseteq V$ sottospazi

$\text{dim}(W_1+W_2)=\overbrace{\text{dim}W_1}^{r+s}+\overbrace{\text{dim}W_2}^{r+t}-\overbrace{\text{dim}(W_1\cap W_2)}^{r}$    $r+s+r+t-r=r+s+t$
$\text{dim}(W_1+W_2)<\text{dim}V$

Dimostrazione
Sia $v_1,\ldots,v_r$ una base di $W_1\cap W_2$
- Completare ad una base di $W_1$ $v_1,\ldots,v_r,w_1,\ldots,w_j$
- // $W_2$ $v_1,\ldots,v_r,\mu_1,\ldots,\mu_t$

$<v_1,\ldots,v_r,w_1,\ldots,w_j>=W_1+W_2$
$r+s+t\ge\text{dim}(W_1+W_2)$

Siano $a_1,\ldots,a_s,b_1,\ldots,b_s,c_1,\ldots,c_t\in\mathbb{R}$ tale che $\sum\limits_{i=1}^{r}a_i v_i+\sum\limits_{i=1}^{s}b_i w_i+\sum\limits_{i=1}^{t}c_i \mu_i$
$W_1\cap W_2\ni\overbrace{\sum{a_i v_i}+\sum{b_i w_i}}^{W_1}=\overbrace{-\sum{c_i \mu_i}}^{W_2}$

$\exists\ d_1,\ldots,d_r$ univocamente determinante

$\sum\limits_{i=1}^{r}a_i v_i+\sum\limits_{i=1}^{s}w_i v_i=0\longrightarrow d_1=\ldots=d_r=c_1=\ldots=c_t=0$ perché $v_1,\ldots,v_r,w_1,\ldots,w_j$ sono linearmente indipendenti

$\sum\limits_{i=1}^{r}d_i v_i+\sum\limits_{i=1}^{t}c_i \mu_i=0\longrightarrow d_1=\ldots=d_r=c_1=\ldots=c_t=0$ perché $v_1,\ldots,v_r,\mu_1,\ldots,\mu_t$ "

# Applicazioni lineari
$V\overset{f}{\longrightarrow}W$
$V, W$ spazi vettoriali su $\mathbb{K}$
$f\cdot V\rightarrow W$ si dice **lineare** se $\forall\ \lambda,\mu\in\mathbb{K}\ \ \forall\ v_1,v_2\in V$
$f(\lambda_1\cdot v_1\underset{v}{+}\lambda_2\cdot v_2)=\lambda_1\underset{w}{\cdot} f(v+1)\underset{w}{+}\lambda_2\underset{w}{\cdot}f(v_2)$

Oss
$f$ lineare $\Rightarrow\ f(O_v)=O_w$

$f\cdot\mathbb{R}^2\rightarrow\mathbb{R}^2$
$f(x,y)=(x+y,x-y)$

$\forall\ \lambda_1,\lambda_2,x_1,x_2,y_1,y_2$

$\begin{array}{c}f(\lambda_1(x_1,y_1)+\lambda_2(x_2,y_2))\\=\\f(\lambda_1x_1+\lambda_1y_1,\lambda_2x_2+\lambda_2y_2)\end{array}\overset{?}{=}\begin{array}{c}\lambda_1 f(x_1,y_2)\lambda_2 f(x_2, y_2)\\=\\\lambda_1(x_1+y_1,x_1-y_1)+\lambda_2(x_2+y_2,x_2-y_2)\end{array}$


$\lambda_1x_1+\lambda_2x_2+\lambda_1y_1+\lambda_2y_2,\lambda_1x_1+\lambda_2x_2-\lambda_1y_1-\lambda_2y_2\ =\ \lambda_1x_1-\lambda_2x_2+\lambda_1y_1-\lambda_2y_2$


$\mathbb{R}^2\rightarrow\mathbb{R}^2$
$f(x,y)=(x+y,x-y)$
$f(x,y)=\left(\begin{array}{c}1&1\\1&-1\end{array}\right)\left(\begin{array}{c}x\\y\end{array}\right)$

$f(\lambda_1v_1+\lambda_2v_2)=\lambda_1f(v_1)+\lambda_2f(v_2)$
$\left(\begin{array}{c}1&1\\1&-1\end{array}\right)(\lambda_1v_1+\lambda_2v_2)=\lambda_1\left(\begin{array}{c}1&1\\1&-1\end{array}\right)v_1+\lambda_2\left(\begin{array}{c}1&1\\1&-1\end{array}\right)v_2$





$\mathbb{R}^n\rightarrow\mathbb{R}^m\ \ \ \ A\in\text{Mat}_{m\times n}(\mathbb{K})$
$f_A\ \ \ \ f_A(\underline{x})=A\underline{x}$

$A\left(\begin{array}{c}x_1\\\ldots\\x_n\end{array}\right)=\left(\begin{array}{c}y_1\\\ldots\\y_m\end{array}\right)$
$f_A$ è lineare
$\forall\ \lambda_1,\lambda_2\in\mathbb{K}\ \ \forall\ v_1,v_2\in\mathbb{K}^n\ \ \ \ f_A(\lambda_1v_1+\lambda_2v_2)\overset?=\lambda_1 f_a(v_1)+\lambda_2 f_A(v_2)$
$A(\lambda_1v_1+\lambda_2v_2)=\lambda_1Av_1+\lambda_2Av_2$

Ogni applicazione lineare tra $\mathbb{K}^n$ e $\mathbb{K}^m$ è di questa forma

$f:\mathbb{R}^n\rightarrow\mathbb{R}^m$ lineare
$A=\left(\begin{array}{c}|&&|\\f(e_1)&\ldots&f(e_n)\\|&&|\end{array}\right)\in\text{Mat}_{m\times n}$
$e_i=\left(\begin{array}{c}0\\\ldots\\1\\\ldots\\0\end{array}\right)\leftarrow i\in\mathbb{R}^n$


Verifichiamo che $f=f_A$
Sia $v\in\mathbb{K}^n\ \ \ \ v=\left(\begin{array}{c}c_1\\\ldots\\c_n\end{array}\right)=c_1\left(\begin{array}{c}1\\0\ldots\\0\end{array}\right)+\left(\begin{array}{c}0\\1\\0\ldots\\0\end{array}\right)+\ldots+\left(\begin{array}{c}0\ldots\\0\\1\end{array}\right)=\sum\limits_{i=1}^n c_i e_i$
$f(v)=f(\sum\limits_{i=1}^n c_i e_i)=\sum\limits_{i=1}^n c_i f(e_i)$
$f_A(v)=A(\sum\limits_{i=1}^n c_i e_i)=\sum\limits_{i=1}^n c_i \underbrace{Ae_i}_{f(e_i)}=\sum\limits_{i=1}^n c_i f(e_i)\ \ \ \ a=\left(\begin{array}{c}|&&|\\f(e_i)&\ldots&f(e_n)\\|&&|\end{array}\right)$

Un'applicazione lineare é univocamente determinata dal valore che assume su una base
$V, W$ spazi vettoriali
$v_1,\ldots,v_n$ basi di $V$
$w_1,\ldots,w_n \in W$
$\exists! f:V\rightarrow W$ lineare e tale che $\forall\ i=1,\ldots,n\ \ \ \ f(v_i)=w_i$

$V\overset f \rightarrow W$
$\ker f=\{v\in V|f(v)=0\}\subseteq V$ **"nucleo"** $f^{-1}=0$
$\text{Im} f=\{w\in W|\ \exists\  v\in V\ \ f(v)=w\}\subseteq W$

$ker f$ è un sottospazio vettoriale di V
$\text{Im} f$ è un sottospazio vettoriale di W
$f_A:\mathbb{K}^N\rightarrow\mathbb{K}^m\ \ \ \ \ker f_A\ \ \ \ \underbrace{f_A(v)}_{A_v}=0$

$0\in\ker f$
Siano $v_1, v_2\in\ker f,\ \lambda_1,\lambda_2\in\mathbb{K}$
$f(\lambda_1 v_1+\lambda_2 v_2)=\lambda_1 f(v_1)+\lambda_2 f(v_2)=\lambda_1 0+\lambda_2 0=0$
$f(0)=0\Rightarrow\in\text{Im} f$  Siano $\lambda_1,\lambda_2\in\mathbb{K},\ w_1, w_2\in\text{Im} f$
$\exists\ v_1,v_2\in v$ tale che $f(v_1)=w_1\ \ f(v_2)=w_2$
$\lambda_1 w_1+\lambda_2 w_2=\lambda_1 f(v_1)+\lambda_2 f(v_2)=f(\lambda_1 v_1+\lambda_2 v_2)\Rightarrow \lambda_1 w_1+\lambda_2 w_2\in\text{Im} f$

$\mathbb{R}^2\rightarrow\mathbb{R}^3$
$A=\left(\begin{array}{c}1&-2\\2&-4\\0&1\end{array}\right)$
$f_A\left(\begin{array}{c}x\\y\end{array}\right)=A\left(\begin{array}{c}x\\y\end{array}\right)=\left(\begin{array}{c}x-2y\\2x-4y\\y\end{array}\right)$

$\ker f_a=\bigg\{\left(\begin{array}{c}x\\y\end{array}\right)\in\mathbb{R}^2|A\left(\begin{array}{c}x\\y\end{array}\right)=0\bigg\}$
$\text{im}f_a=\bigg\{A\left(\begin{array}{c}x\\y\end{array}\right)|\left(\begin{array}{c}x\\y\end{array}\right)\in\mathbb{R}^2\bigg\}=\bigg\{\left(\begin{array}{c}1x-2y\\2x-4y\\y\end{array}\right)|x,y]in\mathbb{R}\bigg\}=\bigg\{x\left(\begin{array}{c}1\\2\\0\end{array}\right)+y\left(\begin{array}{c}-2\\-4\\1\end{array}\right)|x,y\in\mathbb{R}\bigg\}=<\left(\begin{array}{c}1\\2\\0\end{array}\right),\left(\begin{array}{c}-2\\-4\\1\end{array}\right)>$
$\dim\ker f_A=0\ \ \ \ \ker f_A=\{0\}$
$\dim\text{im} f_A=2$
$\dim\text{im}f_A+\dim\ker f_A=2$

$f:V\rightarrow W$ applicazione lineare
$\underbrace{\dim V}_{n+r}=\underbrace{\dim\ker f}_{n}+\dim\text{im} f$

Sia $v_1,\ldots, v_n$ una base di $\ker f$
Completiamo $v_1,\ldots, v_n$ ad una base $v_1,\ldots, v_n, w_1,\ldots, w_r$ di $V$

Osservazione
$V\overset f \rightarrow W$  Se $<v_1,\ldots, v_n>=V$ allora $<f(v_1),\ldots,f(v_n)>=\text{im} f$
$\underbrace{f(v_1)}_{=0},\ldots,\underbrace{f(v_n)}_{=0},\underbrace{f(w_1)}_{=0},\ldots,\underbrace{f(w_r)}_{=0}$ è un insieme di generatori di $\text{im}f$
$<f(w_1),\ldots,f(w_r)>=\text{im}f$

Verifichiamo che $f(w_1),\ldots,f(w_r)$ sono linearmente indipendenti
Siano $\lambda_1,\ldots,\lambda_r\in\mathbb{K}$ tali che $\lambda_1f(w_1)+\ldots+\lambda_rf(w_r)=f(\lambda_1w_1+\ldots+\lambda_rw_r)=0$ quindi $\lambda_1w_1+\ldots+\lambda_rw_r\in\ker f$

Quindi esistono $\mu_1,\ldots,\mu_n\in\mathbb{K}$ $\lambda_1w_1+\ldots+\lambda_rw_r=\mu_1v_1+\ldots+\mu_nv_n$
$\mu_1v_1+\ldots+\mu_nv_n-\lambda_1w_1-\ldots-\lambda_rw_r=0$ quindi $\mu_1=\ldots=\mu_n=\lambda_1=\ldots=\lambda_r=0$

$f:V\rightarrow W$
$\text{im}f=W\iff f$ è suriettiva
$\ker f=\{0\}\iff f$ è iniettiva

Mostriamo che $\ker f=\{0\}\Rightarrow f$ è iniettiva

Siano $v_1, v_2\in V$ tali che $f(v_1)=f(v_2)$
$f(v_1)-f(v_2)=0$    $f(v_1-v_2)=0$    $v_1-v_2\in\ker f=\{0\}$
$v_1-v_2=0$    $v_1=v_2$

$V\overset f \rightarrow W$



$V$
$v_1,\ldots,v_n\mathcal\ {B}$ base di $V$
$v\in V$  $v=\sum\limits_{i=1}^n c_i v_i$  $\exists\ ! c_i\in\mathbb{K}$  $C_\mathcal{B}(v)=\left(\begin{array}{c}c_1\\\ldots\\c_n\end{array}\right)$

$C_\mathcal{B}:V\rightarrow\mathbb{K}^n$ è una funzione biunivoca
$C_\mathcal{B}$ è un'applicazione lineare

$h_1,\ldots,h_n\ \mathcal{B}$ di $V$
$v_1=\sum\limits_{i=1}^{n} a_i h_i$  $C_\mathcal{B}(v_1)=\left(\begin{array}{c}a_1\\\ldots\\a_n\end{array}\right)$
$v_2=\sum\limits_{i=1}^{n} b_i h_i$  $C_\mathcal{B}(v_2)=\left(\begin{array}{c}b_1\\\ldots\\b_n\end{array}\right)$

$\lambda_1C_\mathcal{B}(v_1)+\lambda_2C_\mathcal{B}(v_2)\overset?=C_\mathcal{B}(\lambda_1v_1+\lambda_2v_2)$

$\lambda_1\left(\begin{array}{c}a_1\\\ldots\\a_n\end{array}\right)+\lambda_2\left(\begin{array}{c}b_1\\\ldots\\b_n\end{array}\right)=\left(\begin{array}{c}\lambda_1a_1+\lambda_2b_1\\\ldots\\\lambda_1a_n+\lambda_2b_n\end{array}\right)$

$\underbrace{\lambda_1v_1+\lambda_2v_2}_{=\lambda_1\sum a_ih_i+\lambda_1\sum b_ih_i}\overset?=\sum\limits_{i=1}^n(\lambda_1a_i+\lambda_2b_i)h_i$

$\begin{array}{c}_{\mathcal{B}_1}V&\overset f\longrightarrow &W_{\mathcal{B}_2}\\C_{\mathcal{B}_1} \downarrow&&\downarrow C_{\mathcal{B}_2}\\\mathbb{K}^n&\longrightarrow&\mathbb{K}^m\end{array}$

Osservazione
La composizione di applicazioni lineare è un'applicazione lineare

$V\overset f\rightarrow W\overset g\rightarrow U\ \ \ \ V\overset {g\ \circ f}\rightarrow U$
$f,g$ lineare, mostriamo che $g\ \circ f$ è lineare
Siano $v_1, v_2\in V,\ \lambda_1,\lambda_2\in\mathbb{K}$
$g(f(\lambda_1v_1+\lambda_2v_2))=g(\lambda_1f(v_1)+\lambda_2f(v_2))=\lambda_1g(f(v_1))+\lambda_2g(f(v_2))$

Osservazione
L'inverso di un'applicazione lineare biunivoca è lineare

$V\overset f {\underset \sim \rightarrow}W\ \ f$ lineare e biunivoca
Siano $w_1, w_2\in W\ \ \lambda_1,\lambda_2\in\mathbb{K}$
$f^{-1}(\lambda_1w_1+\lambda_2w_2)\overset?=\lambda_1f^{-1}(w_1)+\lambda_2f^{-1}(w_2)$

$C_{\mathcal{B}_2}\circ f\circ C_{\mathcal{B}_1}:\mathbb{K}^n\rightarrow\mathbb{K}^m$ è lineare, quindi $C_{\mathcal{B}_2}\circ f\circ C_{\mathcal{B}_1}$ è rappresentata da una matrice $\in\text{mat}_{m\times n}(\mathbb{K})\ \ \ M_{\mathcal{B}_1\mathcal{B}_2}(f)\in\text{Mat}_{m\times n}(\mathbb{K})$
$\forall\ v\in V$
$C_{\mathcal{B}_2}(f(v))=M_{\mathcal{B}_1\mathcal{B}_2}(f)\cdot C_{\mathcal{B}_1}(v)$



$\mathbb{R}[X]_{\le2}\overset D\rightarrow\mathbb{R}[X]_{\le1}$
$p(x)\mapsto p'(x)$

Es:
1) Mostrare che D è lineare
2) Mostrare che $\mathcal{B}_1=1,x,x^2$ è una base di $\mathbb{R}[X]_{\le2}$
3) Mostrare che $\mathcal{B}_2=1+x,1-x$ è una base di $\mathbb{R}[X]_{\le1}$
4) Scrivere $M_{\mathcal{B}_1\mathcal{B}_2}(D)$

1)
$\forall\ \lambda_1,\lambda_2\in\mathbb R\ \ \ \ \forall\ p_1,p_2\in\mathbb R[x]_{\le2}$
$(\lambda_1p_1+\lambda_2p_2)'\overset?=\lambda_1p_1'+\lambda_2p_2'$

2)
$a(1+x)+b(1-x)$





$\begin{array}{c}_{\mathcal{B}}V&\overset f\longrightarrow &W_{\mathcal F}\\C_{\mathcal{B}} \downarrow&&\downarrow C_{\mathcal F}\\\mathbb{K}^n&\underset{M_{\mathcal{B}\mathcal F}(f)}\longrightarrow&\mathbb{K}^m\end{array}\ \ \ \ \forall\ v\in V\ \ M_{\mathcal B \mathcal F}(f)C_\mathcal B(v)=C_\mathcal F(f(v))$
## Osservazione
Fissate le basi $\mathcal B, \mathcal F$, la corrispondenza $f\leftrightarrow M_{\mathcal B\mathcal F}(f)$ è una corrispondenza biunivoca
$\underbrace{\text{Hom}(v,w)}_{f:v\rightarrow w|f \text{ lineare}}\leftrightarrow\text{Mat}_{m\times n}(\mathbb R)$

$1\ \ \ \ \leftarrow(1\cdot1+0\cdot x+0\cdot x^2)$
$C_\mathcal B(1)=\left(\begin{array}{c}1\\0\\0\end{array}\right)$
$D(1)=0$
$C_\mathcal F(0)=\left(\begin{array}{c}0\\0\end{array}\right)$


$x\ \ \ \ \leftarrow(0\cdot1+1\cdot x+0\cdot x^2)$
$C_\mathcal B(x)=\left(\begin{array}{c}0\\1\\0\end{array}\right)$
$D(x)=1$
$C_\mathcal F(1)=\left(\begin{array}{c}\frac12\\\frac12\end{array}\right)\ \ \ \ \longleftarrow a(1+x)+b(1-x)=1\ \ \begin{cases}a+b=1\\a-b=0\end{cases}$


$x^2\ \ \ \ \leftarrow(0\cdot1+0\cdot x+1\cdot x^2)$
$C_\mathcal B(x^2)=\left(\begin{array}{c}0\\0\\1\end{array}\right)$
$D(x^2)=2x$
$C_\mathcal F(2x)=\left(\begin{array}{c}1\\-1\end{array}\right)\ \ \ \ \longleftarrow a(1+x)+b(1-x)=2x\ \ \begin{cases}a+b=0\\a-b=2\end{cases}\ \ \ \ \left(\begin{array}{c}a\\b\end{array}\right)=\frac12\left(\begin{array}{c}1&1\\1&-1\end{array}\right)$

$M_{\mathcal B\mathcal F}(D)=\left(\begin{array}{c}0&\frac12&1\\0&\frac12&-1\end{array}\right)$



$_\mathcal B V\overset f\rightarrow \overset{^\mathcal F}W\overset g\rightarrow U_\mathcal E\ \ \ \ V\overset {g\ \circ f}\rightarrow U$
$$\left(\begin{array}{c}
_\mathcal{B}V & \overset f\rightarrow & \overset{^\mathcal F}W & \overset g\rightarrow & U_\mathcal E\\
\small{C_\mathcal B}\downarrow&&\small{C_\mathcal F}\downarrow&&\downarrow\small{C_\mathcal E}\\
\mathbb K^n&\rightarrow&\mathbb K^m&\rightarrow&\mathbb K^r
\end{array}\right)$$

$M_{\mathcal{BE}}(g\circ f)C_\mathcal B(v)=C_\mathcal E(g(f(v)) )=M_\mathcal{FE}(g)C_\mathcal F(f(v))=M_\mathcal{FE}(g)M_\mathcal{BE}(f)C_\mathcal B(v)$

$M_\mathcal{BE}(g\circ f)=M_\mathcal{FE}(g)M_\mathcal{BF}(f)$


$$\left(\begin{array}{c}
_\mathcal{B}V & \overset f\rightarrow & \overset{^\mathcal F}W & \overset g\rightarrow & U_\mathcal E & \overset h \rightarrow & L_\mathcal D\\
\small{C_\mathcal B}\downarrow&&\small{C_\mathcal F}\downarrow&&\downarrow\small{C_\mathcal E}&&\downarrow\small{C_\mathcal D}\\
\mathbb K^n & \rightarrow & \mathbb K^m & \rightarrow & \mathbb K^r & \rightarrow & \mathbb K^s
\end{array}\right)$$

$f\circ(g\circ h)=(f\circ g)\circ h \iff M_\mathcal{BF}(f)(\small M_\mathcal{FE}(g)M_\mathcal{ED}(h)\normalsize)=(\small M_\mathcal{BF}(f)M_\mathcal{FE}(g)\normalsize)M_\mathcal{ED}(h))$



$_\mathcal B V\overset f \rightarrow V_\mathcal B$   "endomorfismo"
$M_\mathcal B(f)$

$f$ è un endomorfismo $\iff\ M_\mathcal B(f)$ è invertibile
In questo caso $M_\mathcal B(f^{-1})=(M_\mathcal B(f))^{-1}$

$M_\mathcal B(\text{id})=\text{Id}_n$
$\small\forall\ v\in V$
$M_\mathcal B(\text{id})C_\mathcal B(v)=C_\mathcal B(\text{id}(v))$

$$
\begin{array}{c}
\mathbb K^n & \underset{\small M_{\mathcal B_1 \mathcal F_1}(f)\normalsize}\longrightarrow & \mathbb K^n\\
\small _{\mathcal B_1}\normalsize\uparrow \small C_{\mathcal B_1} & & \small C_{\mathcal F_1}\normalsize \uparrow \small_{\mathcal F_1}\normalsize\\
V & \overset f \longrightarrow & W\\
\small ^{\mathcal B_2}\normalsize\downarrow \small C_{\mathcal B_2} & & \small C_{\mathcal F_2}\normalsize \downarrow \small_{\mathcal F_2}\normalsize\\
\mathbb K^m & \overset{M_{\small \mathcal B_2\mathcal F_2\normalsize}(f)}\longrightarrow & \mathbb K^m
\end{array}
$$


$M_{\mathcal B_2\mathcal F_2}(f)=M_{\mathcal B_2\mathcal F_2}(\text{id }w\circ f\circ \text{id }v)=M_{\mathcal F_1\mathcal F_2}(\text{id w})M_{\mathcal B_1\mathcal F_1}(f)M_{\mathcal B_2\mathcal B_1}(\text{id }v)$

$M_{\mathcal B_2\mathcal B_1}(\text{id }v) = M_{\mathcal B_1\mathcal B_2}(\text{id }v)^{-1}$



$\mathbb R^4$
$\mathcal{F\left(\begin{array}{c}1\\1\\0\\0\end{array}\right)},\left(\begin{array}{c}1\\1\\1\\1\end{array}\right),\left(\begin{array}{c}0\\0\\2\\0\end{array}\right),\left(\begin{array}{c}0\\0\\0\\1\end{array}\right)$
$\mathcal K\left(\begin{array}{c}1\\0\\0\\0\end{array}\right),\left(\begin{array}{c}0\\1\\0\\0\end{array}\right),\left(\begin{array}{c}0\\0\\1\\0\end{array}\right),\left(\begin{array}{c}0\\0\\0\\1\end{array}\right)$

$M_\mathcal{FK}(\text{id}_{\mathbb R^4})C_\mathcal F(v)=C_\mathcal K(v)=v$
$C_\mathcal F\left(\begin{array}{c}1\\1\\0\\0\end{array}\right)=\left(\begin{array}{c}1\\0\\0\\0\end{array}\right)$





$\begin{array}{c}_\mathcal B V & \overset f \longrightarrow & V_\mathcal B\\\downarrow&&\downarrow\\\mathbb K^n & \underset A \longrightarrow & \mathbb K^n\end{array}$

$\mathcal F$ altra base di $V$

$P=M_\mathcal{FB}(\text{id})$
$M_\mathcal F (f)=M_\mathcal{BF}(\text{id})A\ \ M_\mathcal{FB}(\text{id})=P^{-1}AP\longleftarrow$ " matrice coniugata a $A$ rispetto $P$ "
$A$ e $P^{-1}AP$ si dicono **simili**

Definizione
$A,B\in\text{Mat}_n(\mathbb K)$
$A$ e $B$ sono simili (su $\mathbb K$) se $\exists] P\in GL_n(\mathbb K)$ tale che $A=P^{-1}BP$  $B=PAP^{-1}$

Se $A$ e $B$ sono **simili** $\text{det}A=\text{det}B$

$\text{det}A=\text{det}(P^{-1}BP)=\underbrace{(\text{det}P^-1)}_{(\text{det}P)^-1}\ (\text{det}B)\ (\text{det}P)$
$\text{rk}A=\text{rk}B$

$P^{-1}(M_1+M_2)P=P^{-1}M_1P_+P^{-1}M_2P$
$P^{-1}(M_1M_2)P=P^{-1}M_1P_\cdot P^{-1}M_2P$



$\left.\begin{array}{l}A\sim A&\text{(riflessiva)}\\A\sim B \Rightarrow B\sim A&\text{(simmetrica)}\\A\sim B \text{ e } B\sim C \Rightarrow A\sim B&\text{(transitiva)}\end{array}\right\}$


