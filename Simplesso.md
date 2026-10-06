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
$\begin{array}{ll}\text{vincoli di }\le&\rightarrow a_1x_1+a_2x_2+\ldots+a_nx_n\
- vincoli di $\ge$
- variabili libere (non vincolate in segno)