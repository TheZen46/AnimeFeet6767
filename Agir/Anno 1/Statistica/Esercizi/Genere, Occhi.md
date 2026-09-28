A un gruppo di $50$ persone viene chiesto il genere $(\text{femmina, maschio})$ e il colore degli occhi $(\text{azzurro, verde, castano})$
Le risposte sono sintetizzate nella tabella a due vie delle frequenze assolute

|     | $A$ | $V$ | $C$ |
| --- | --- | --- | --- |
| $F$ | 5   | 8   | 7   |
| $M$ | 4   | 6   | 20  |


- Costruire la tabella a due vie delle frequenze relative, marginale riga e marginale colonna
$l=1,\ldots,50$
$l=\text{persona intervistata}$

$x_l=\text{genere}$
$v_1=\text{femmina}=F$
$v_2=\text{maschio}=M$
$v_i\ \ \ \ i=1,2\ \ (2\text{ righe})$

$y_l=\text{genere}$
$w_1=\text{azzurro}=A$
$w_2=\text{verde}=V$
$w_3=\text{castano}=C$
$w_j\ \ \ \ j=1,2,3\ \ (3\text{ colonne})$

| $\begin{array}{c}&y_l\\x_l&\end{array}$ | $A$    | $V$    | $C$    |     | $y_l$   |
| --------------------------------------- | ------ | ------ | ------ | --- | ------- |
| $F$                                     | $10\%$ | $16\%$ | $14\%$ |     | $40\%$  |
| $M$                                     | $8\%$  | $12\%$ | $40\%$ |     | $60\%$  |
|                                         |        |        |        |     |         |
| $x_l$                                   | $18\%$ | $28\%$ | $54\%$ |     | $100\%$ |
$f_{i,j}=\frac{n_{i,j}}n$
$f_{1,1}=\frac5{50}=0.1=10\%$


Marginale riga

| $w_j$    | $A$    | $V$    | $C$    |
| -------- | ------ | ------ | ------ |
| $n_{:j}$ | $9$    | $14$   | $27$   |
| $f_{:j}$ | $18\%$ | $28\%$ | $54\%$ |

Marginale colonna

| $v_{i}$ | $n_{i:}$ | $f_{i:}$ |
| ------- | -------- | -------- |
| $F$     | $20$     | $40\%$   |
| $M$     | $30$     | $60\%$   |


- Calcolare il profilo riga
Sottocampione femmine

$f_{j\mid i=1}\ \ \ \ \text{frequena relativa del colore dato genere=}F$
$f_{j\mid i=2}\ \ \ \ \text{frequena relativa del colore dato genere=}M$

$f_{\underset j{1}\mid\underset i {1}}=\frac{n_{1,1}}{n_{1j}}=\frac5{20}$
$f_{\underset j{1}\mid\underset i {2}}=\frac{n_{2,1}}{n_{2}}=\frac4{20}$

|     | $A$    | $V$    | $C$    |     |         |
| --- | ------ | ------ | ------ | --- | ------- |
| $F$ | $25\%$ | $40\%$ | $35\%$ |     | $100\%$ |
|     |        |        |        |     |         |
| $M$ | $13\%$ | $20\%$ | $67\%$ |     | $100\%$ |


- Calcolare il profilo colonna
$f_{i\mid j}=\frac{n_{ij}}{n_{:j}}$    $j=1,2,3$    $i=1,2$

|     | $A$     |     | $V$     |     | $C$     |
| --- | ------- | --- | ------- | --- | ------- |
| $F$ | $56\%$  |     | $57\%$  |     | $26\%$  |
| $M$ | $44\%$  |     | $43\%$  |     | $74\%$  |
|     |         |     |         |     |         |
|     | $100\%$ |     | $100\%$ |     | $100\%$ |

