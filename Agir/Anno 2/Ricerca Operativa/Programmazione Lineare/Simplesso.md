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