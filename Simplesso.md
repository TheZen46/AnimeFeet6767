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
