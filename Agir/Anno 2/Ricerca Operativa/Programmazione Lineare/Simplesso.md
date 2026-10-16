1) Parto da $P$ che non contiene rette ed è $\ne\varnothing$
2) Devo aver verificato che il problema non sia illimitato inferiormente
3) Seleziono un vertice, verifico che non sia soluzione
	Se non lo è, mi muovo in un vertice con costo minore
# Esempio
$n=2$
Quadrato da $(0,0)$ a $(1,1)$
$2^2\text{ vertici}$


$n=3$
Cubo da $(0,0,0)$ a $(1,1,1)$
$2^3\text{ vertici}$

# Problema in forma standard
$\left[\begin{array}{l}\min\ c^Tx\\Ax=b\\x\ge0\end{array}\right.$

# Poliedro -> forma standard
Supponiamo di avere un poliedro descritto da
$\text{vincoli di }\le\mskip{14mu}\rightarrow a_1x_1+a_2x_2+\ldots+a_nx_n\le b\mskip{14mu}\rightarrow\text{aggiungo }s\text{ e scrivo }a_1x_1+\ldots+a_nx_n+s=b\text{ con }s\ge0$

$P=\bigl\{(x_1,\ldots,x_n)\ |\ a_1x_1+\ldots+a_nx_n\le b\bigr\}=\bigl\{(x_1,\ldots,x_n)\ |\ a_1x_1+\ldots+a_nx_n+s=b,\text{ per qualche }s\ge0\bigr\}$
Esempio
	$2x_1+x_2\le3\to(1,0)\text{ verifico la disuguaglianza}$
	$2\cdot1+1\cdot0+\underset{\small\array{\uparrow\\\!s}}1=3$

$\text{vincoli di }\ge\mskip{14mu}\rightarrow a_1x_1+a_2x_2+\ldots+a_nx_n\ge b\mskip{14mu}\rightarrow\text{aggiungo }u\text{ e scrivo }a_1x_1+\ldots+a_nx_n+-=b\text{ con }u\ge0$

$x\rightarrow x=x^+-x^-\mskip{36mu}x^+\ge0,\ x^-\ge0$


$\left[\begin{array}{l}\min\ 12x_1+x_2+5x_3\\x_2-2x_3\ge7\\2x_1x_3\le10\\3x_1-x_2-2x_3=3\\x_1\ge0,\ x_3\ge0\end{array}\right.\Rightarrow\left[\begin{array}{l}\min\ 12x_1+x_2+5x_3\\x_2-2x_3-u_1=7\\2x_1x_3+s_1=10\\3x_1-x_2-2x_3=3\\x_1\ge0,\ x_3\ge0,\ u_1\ge0,\ s_1\ge0\end{array}\right.$

$\operatorname{rank}x_2={x_2}^-{x_2}^-$

$\left[\begin{array}{l}\min\ 12x_1+x_2+5x_3\\{x_2}^+-{x_2}^--2x_3-u_1=7\\2x_1x_3+s_1=10\\3x_1-({x_2}^+-{x_2}^-)-2x_3=3\\x_1\ge0,\ {x_2}^+\ge0,\ {x_2}^-\ge0,\ x_3\ge0,\ u_1\ge0,\ s_1\ge0\end{array}\right.$

$A=\underset{{x_1\mskip{24mu}{x_2}^+\mskip{18mu}{x_2}^-\mskip{30mu}x_3\mskip{24mu}s_1\mskip{24mu}u_1}}{\left[\begin{array}{c}0&1&-1&-2&0&1\\2&0&0&1&1&0\\3&1&1&2&0&0\end{array}\right]}$
$A$ è $3\times 6$
$b=\left[\array{7\\10\\3}\right]$

# Caratterizazione di vertici in un poliedro in forma standard
$P=\{x\in\mathbb R^n|Ax=b,\ x\ge0\}$
$A:\ m\times n$
Supposiamo $P\ne\varnothing$ e $\operatorname{rank}(A)=m\ \ (\Rightarrow m\le n)$
## Teorema
Sia $\overline x\in P$
Allora $\overline x$ è un vertice di $P\iff$ le colonne corrispondenti alle entrate strettamente positive di $\overline x$ sono linearmente indipendenti

### Esempio
$m=2,\mskip{12mu}n=4\mskip{24mu}\overline x=(1,0,2,0)\in P$

$m=2,\mskip{12mu}n=4\mskip{24mu}\overline x=(1,1,2,0)\in P\text{    Non è un vertice}$
## Osservazione
Ogni vertice ha al più $m$ entrate non nulle

$\overline x=(1,0,0,0)$ è un vertice (se la corrispondente colonna è non nulla)

## Dimostrazione
Scrivo $P$ in forma generale
$Ax\ge b$
$-Ax\ge-b$
$x\ge0$

$\begin{array}{l}m\\m\\n\end{array}\left[\begin{array}{c}A\\-A\\I\end{array}\right]x\ge\left[\begin{array}{c}b\\-b\\0\end{array}\right]$

Supponiamo che le componenti nulle di $x$ siano le ultime $n-r\Rightarrow\text{Matrice vincoli arrivi}:\operatorname{rank}\left(\left[\begin{array}{c}A\\-A\\I_{n-r}\end{array}\right]\right)=n\iff\overline x\text{ è un vertice}$
$\operatorname{rank}\left(\left[\begin{array}{c}A\\-A\\I_{n-r}\end{array}\right]\right)=\operatorname{rank}\left(\left[\begin{array}{c}A\\I_{n-r}\end{array}\right]\right)\iff\operatorname{rank}\overset{\tilde A}{\left[{\begin{array}{l}a_1\\\vdots\\a_n\\0&\begin{array}{l}1&&0\\\\0&&1\end{array}\end{array}}\right]}\left[\begin{array}{c}x_1\\x_2\\\vdots\\\vdots\\\vdots\\x_n\end{array}\right]$

$\operatorname{rank}(\tilde A)=n\iff\tilde A\left[\begin{array}{l}x_1\\\vdots\\x_n\end{array}\right]=\left[\begin{array}{l}0\\vdots\\0\end{array}\right]\Rightarrow\left[\begin{array}{l}x_1\\\vdots\\x_n\end{array}\right]=\left[\begin{array}{l}0\\\vdots\\0\end{array}\right]$

$\displaystyle \operatorname{rank}\left[\begin{array}{l}x_1\\\vdots\\x_n\end{array}\right]=\left[\begin{array}{l}y\\z\end{array}\right],\text{ con }y=(y_1,\ldots,y_r),\ \ z=(z_1,\ldots,z_{n-r})$
$\tilde a\left[\begin{array}{l}y\\z\end{array}\right]=\left[\begin{array}{l}0\\\vdots\\0\end{array}\right]\iff\cases{{a_1}^T\pmatrix{y\\z}=0\\\vdots\\{a_m}^T\pmatrix{y\\z}=0\\z=0}\iff\cases{{a_1}^T[1,\ldots,r]=0\\\vdots\\{a_m}^T\pmatrix[1,\ldots,r]=0\\z=0}\Rightarrow\text{la matrice fatta dalle prime }r\text{ colonne di }A\text{ ha rango }r$
Ma poi sotto ho $I_{n-r}$ che ha $n-r$ colonne indipendenti $\Rightarrow$ ci sono $n$ colonne indipendenti





Supponiamo $\overline x=\Small\left[\array{1\\1\\0\\0}\right]$ sia una **SBA**; $I_b=\{1,2\}\m{20}\bigl(\overline x_B=\left[\array{1\\1}\right],\ \ \overline x_N=\left[\array{0\\0}\right]\bigr)$
Supponiamo $\gamma^T=\bigl[-1,0\bigr]$
Supponiamo che $f(\overline x)=12$
Quanto vale la funzione obiettivo in $\Small\left[\array{1\\1\\3\\0}\right]$?

Si ha: $f(x)={C_B}^T B^{-1}b+\gamma^T(3,0)$

Criterio ottimalità: $\gamma\ge0\Rightarrow\overline x$ è soluzione ottima
Osservazione: Se $\gamma>0\Rightarrow\overline x$ è l'unica soluzione ottima

Sia $x\ne\overline x,\ x\in\mc{P}$
$f(x)=C^Tx={C_B}^TB{^-1}b+\gamma^T x_N>{C_B}^T B^{-1}b=C^T\overline x=f(\overline x)$

Test di illimitatezza:
Supponiamo che $\exists\ h$ radice tale che $\gamma_h<0$
Se la colonna $h$-esima di $B^{-1}N$ ha tutte entrate negative (o nulle) allora il problema è illimitato


$\gamma=\bigl(\gamma_1,\ldots,\gamma_{n-m}\bigr)$ si ha $\gamma_h<0$
Considero $x_N=t e_h=\bigl[0,\ldots,1,0\ldots,0\bigr]^T\cdot t$
Se definisco $x_B=B^{-1}b-B^{-1}Nx_N$, il vettore $\left[\array{x_B\\x_N}\right]$ verifica $Ax=b$
Sia $\large t>0\Rightarrow x_N\ge0$ è $\large x_B=B^{-1}b-B^{-1}N\Small\left[\begin{array}{c}0\\\vdots\\t\\\vdots\\0\end{array}\right]\large=\underbrace{B^{-1}b}_{\ge0}-\underbrace{\bigl[B^{-1}N\bigr]_h}_{\text{colonna }\\h\text{-esima}}\cdot\ t\Rightarrow x_B\ge0$

$f(x)={C_B}^TB^{-1}b+\gamma^T\cdot\ te_h={C_B}^TB^{-1}b+t\gamma_h\underset{t\to+\infty}{\longrightarrow}-\infty$


# Esercizio
$\cases{\min -x_1-x_2\\x_1-x_2=x_3=1\\-x_1+x_2+x_4=1\\x_1\ge0,\ x_2\ge0,\ x_3\ge0,\ x_4\ge0}$

$A=\sqmatrix{1&-1&1&0\\-1&1&0&1}\m{30}b=\sqmatrix{1\\1}\m{30}B=\sqmatrix{1&0\\-1&1}\Leftarrow\text{è una matrice di base}$
$B^{-1}=\sqmatrix{1&0\\1&1}\Rightarrow B^{-1}b=\sqmatrix{1\\2}\Rightarrow\overline x=\sqmatrix{1\\0\\0\\2}\text{è SBA}$
$\overline x_B=\sqmatrix{1\\2},\quad \overline x_N=\sqmatrix{0\\0}$
${C_B}^T=\sqmatrix{-1,0}\quad {C_N}^T=\sqmatrix{-1,0}\qquad N=\sqmatrix{-1&1\\1&0}\qquad B^{-1}N=\sqmatrix{-1&1\\0&1}$
$\gamma^T=\sqmatrix{-1,0}-\sqmatrix{-1,0}\sqmatrix{-1&1\\0&1}=\sqmatrix{-1,0}-\sqmatrix{1,-1}=\sqmatrix{-2,1}\leftarrow\text{vettore costi ridotti}$
$\gamma_1=-2<0$
$\bigl[B^{-1}N\bigr]_1=\sqmatrix{-1\\0}\Rightarrow\text{il pb è illimitato}$

$\cases{\min\ -x_1-x_2\\x_1=1+x_2-x_3\\x_4=1+x_1-x_2=2-x_3\\x\ge0}\m{30}\cases{\min\ -1-2x_2+x_3\\x_1=1+x_2-x_3\\x_4=2-x_3\\x\ge0}$

$B^{-1}N=\sqmatrix{-1&1\\0&1}$

$\overline x_B=\sqmatrix{1\\2}\quad\overline x_N=\sqmatrix{0\\0}$

### Osservazione
Test ottimalità non superato $\Rightarrow\exists\ \gamma_h<0$
Test illimitatezza non superato $\Rightarrow$ in corrispondenza di tutte le entrate negative (streattamente) di $\gamma$ esiste un elemento strettamente positivo nella colonna corrispondente di $B^{-1}N$

Fisso $h$ indice tale che $\gamma_h<0$ e quindi esiste un elemento $B^{-1}N_{ih}>0$

Come si aggiorna le SBA??
$\array{\overline x_B=B^{-1}b\\\overline x_N=\tiny{\sqmatrix{0\\\vdots\\0}}}\longrightarrow \array{x_B=B^{-1}b-B^{-1}Nte_k\\\\x_N=te_k}$

Come scegliere $k$? Come scegliere $t$?
1) Scegliamo $k=h$, perche $\gamma_h<0$
$x_B=B^{-1}b-B^{-1}Nx_N=B^{-1}b-\bigl[B^{-1}N\bigr]_h\ t$
Affinché il vettore sia ammissibilie:
	$B^{-1}b_j-\bigl[B^{-1}N\bigr]_{jh}\ t\ge0\qquad\forall\ j$
Se $\bigl[B^{-1}N\bigr]_{jh}\le0\Rightarrow(x_B)_j\ge0\qquad\forall\ t\ge0$
Se $\displaystyle \bigl[B^{-1}N\bigr]_{jh}\qquad t\le\frac{\bigl(B^{-1}b\bigr)_j}{\bigl[B^{-1}N\bigr]_{jh}}$

Per garantire $\sqmatrix{x_B\\x_N}$ ammissibile devo scegliere: $\ds t\le\min\limits_{j:B^{-1}N_{jh}>0}\frac{B^{-1}b_j}{\bigl[B^{-1}N\bigr]_{jh}}$

Criterio del rapporto minimo: $\ds\large t\le\min\limits_{j:[B^{-1}N]_{jh}>0}\frac{B^{-1}b_j}{\bigl[B^{-1}N\bigr]_{jh}}$
Sia $k=$indice su cui si ottiene il minimo
Allora la nuova SBA si ottiene:
	$\to$ facendo entrare $(x_N)_h\qquad(\gamma_h<0)$
	$\to$ facendo uscire $(x_B)_h\qquad(\text{corrispondente al rapporto min})$