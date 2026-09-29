$\text{polpa}+\text{dolcificante}$
$\text{Vincoli sulle quantità di vitamina C, sali minerali, zucchero}$

|                   | $\text{polpa}$ | $\text{dolcificante}$ |
| ----------------- | -------------- | --------------------- |
| $\text{vit C}$    | $140\text{mg}$ | $0$                   |
| $\text{sali}$     | $20\text{mg}$  | $10\text{mg}$         |
| $\text{zuccheri}$ | $25\text{g}$   | $50\text{g}$          |
|                   |                |                       |
| $\text{Costo}$    | $\text{€}4$    | $\text{€}6$           |
### Vincoli
Succo contiene:
	$\ge70mg\text{ vitamina C}$
	$\ge30\text{mg sali minerali}$
	$\ge75\text{g zucchero}$
$\min\text{ costo}$?

### Funzione obiettivo
$f(x,y)=4x_1+6x_2$

### Variabili
$x_1=\text{quantità di polpa }(x_1\cdot 100\text{g})$
$x_2=\text{quantità di dolcificante }(x_2\cdot 100\text{g})$

### Vincoli
$\displaystyle \begin{array}{l}\frac{140x_1}{x_1+x_2}\ge 70\rightarrow\frac{x_1}{x_1+x_2}\ge\frac12\rightarrow1+\frac{x_2}{x_1}\le2\rightarrow x_2\le x_1\\\frac{20x_1+10x_2}{x_1+x_2}\ge 30\\\frac{25x_1+50x_2}{x_1+x_2}\ge 75\\x_1\ge0\\x_2\ge0\end{array}$`


$\min(x_1,x_2)=Ax\ge b$
$x=\pmatrix{x_1\\x_2}$
$A=\pmatrix{140&0\\20&10\\25&50\\1&0\\0&1}$
$b=\pmatrix{70\\30\\75\\0\\0}$

Il vincolo $x_1\ge0$ è ridondante perché da $140x_1\ge70$ abbiamo già $x_1\ge\frac12$

$A=\pmatrix{140&0\\20&10\\25&50\\0&1}$
$b=\pmatrix{70\\30\\75\\0}$

Retta: $a_1x_1+a_2x_2=b$
Semipiani (chiusi): $\array{a_1x_1+a_2x_2\ge b\Leftarrow \underline b\\a_1x_1+a_2x_2\le b\Leftarrow \overline b}$
$\underline b<b<\overline b$

Se consideriamo la funzione $g(x_1,x_2)=a_1x_1+a_2x_2$
Il vettore $a=\pmatrix{a_1\\a_2}$ ci indica la direzione (e gli insiemi di livello di $g$ sono rette parallele alla forma $a_1x_1+a_2x_2=b$)
