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
	$\le70mg\text{ vitamina C}$
	$\le30\text{mg sali minerali}$
	$\le75\text{g zucchero}$
$\min\text{ costo}$?

### Variabili
$x_1=\text{quantità di polpa }(x_1\cdot 100\text{g})$
$x_2=\text{quantità di dolcificante }(x_2\cdot 100\text{g})$

$\displaystyle \begin{array}{l}\frac{140x_1}{x_1+x_2}\le 70\rightarrow\frac{x_1}{x_1+x_2}\le\frac12\rightarrow1+\frac{x_2}{x_1}\ge2\rightarrow x_2\ge x_\\\frac{20x_1+10x_2}{x_1+x_2}\le 30\\\frac{25x_1+50x_2}{x_1+x_2}\le 75\end{array}$
