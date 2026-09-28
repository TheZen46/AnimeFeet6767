$y=f(x)$
$x, y \in \{0, 1\}$
$x \in \mathbb{B}^m=\{0,1\}^m$
$y \in \mathbb{B}^n=\{0,1\}^n$
	Variabili booleane

Funzioni possibili
	y = 0, ⏚
	y = 1
	y = x \[buffer gate]
	y = !x \[not gate]

$\underrightarrow{y} = \underrightarrow{f}(\underrightarrow{x})$
$x \in \mathbb{B}^d$
$y \in \mathbb{B}^p$

Per studiare la funzione iniziale si studiano i casi

$y = \underrightarrow{f}(\underrightarrow{x})$
$x \in \mathbb{B}^d$
$d = 2$
$y = \underrightarrow{f}(x_1, x_2)$


$y = \underrightarrow{f}(\underrightarrow{x})$
$\underrightarrow{f} \rightarrow 2^{2^n}$
$\underrightarrow{x} \rightarrow 2^n$

Tabella di verità
$y = f(x_1, x_2)$

| $x_1$ | $x_1$ | $y = f(x_1, x_2)$ |        Out         |
| :---: | :---: | :---------------: | :------------------: |
|   0   |   0   |     $f(0,0)$      | `0101010101010101` |
|   0   |   1   |     $f(0,1)$      | `0011001100110011` |
|   1   |   0   |     $f(1,0)$      | `0000111100001111` |
|   1   |   1   |     $f(1,1)$      | `0000000011111111` |

### Teoremi

$x + 1 = 1\  /\  x \cdot 0 = 0$

$x + 0 = x\  /\  x \cdot 1 = x$

$x + x = x\  /\  x \cdot x = x$

$x + y = y = x\  /\  x \cdot y = y \cdot x$

(x + y) + z = x + (y + z) = x + y + z  |  (x * y) * z = x * (y * z) = x * y * z

(x * y) + (x * z) = x * (y + z)  |  (x + y) * (x + z) = x + (y * z)

(x + y) * (x + z) = xx + xz + yx + yz = x + xz + yx + yz = x(1 + z) + yx + yz = x + yx + yz = x + y(1 + y) + yz = x + yz 

$x + \overline{x} = 1\  /\  x\cdot \overline{x} = 0$

$x + xy = x \cdot 1 + xy = x(1 + y) = x\  /\  x(x + y) = x$
$x + \overline{(xy)} = x + y\  /\  x\overline{(x + y)} = xy$

### De Morgan

$xy = \overline{(\overline{x}+\overline{y})} \rightarrow \overline{xy} = \overline{x}+\overline{y}$

$x+y = \overline{(\overline{x}\ *\ \overline{y})} \rightarrow \overline{x+y} = \overline{x}\ *\ \overline{y}$

$x_1*x_2*x_3*...*x_n = \overline{\overline{x_1}+\overline{x_2}}+\overline{x_3}+...+\overline{x_n}$
$\downarrow$
$x_1*a = \overline{\overline{x_1}+\overline{a}} = \overline{\overline{x_1}+\overline{x_2*B}}=\overline{x_1}+\overline{\overline{x_2}+\overline{B}} = \overline{\overline{x_1}+\overline{x_2}+\overline{B}}$
$a = x_2*x_3*...*x_n = x_2*B$

### Shannon (prima forma)
Somma di prodotto
$y = f(x_1,x_2) = \overline{x_1} f(0,x_2) + x_1 f(1,x_2) = \overline{x_1} (\overline{x_2} f(0,0) + x_2 f(0,1)) + x_1 (\overline{x_2} f(1,0) + x_2 f(1,1))$

$x_1 = 0 \rightarrow 1*f(0,x_2,x_3,...,x_n) + 0 * [...] = f(0,x_2,x_3,...,x_n)$
$x_1 = 1 \rightarrow 1*f(1,x_2,x_3,...,x_n) + 0 * [...] = f(1,x_2,x_3,...,x_n)$

$y=f(x_1,x_2,x_3)$
tabella di verità da 8 righe ($2^n$ possibilità)
$2^8$ funzioni ($2^{2^n}$ funzioni)


### Shannon (2)
Prodotto di somma
$y=f(x_1,x_2)=$



![[!(A)B+ACD.png]]
$y=\overline{A}B+ACD$

| A   | B   | C   | D   | Y   |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |     |
| 0   | 0   | 0   | 1   |     |
| 0   | 0   | 1   | 0   |     |
| 0   | 0   | 1   | 1   |     |
| 0   | 1   | 0   | 0   | 1   |
| 0   | 1   | 0   | 1   | 1   |
| 0   | 1   | 1   | 0   | 1   |
| 0   | 1   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   |     |
| 1   | 0   | 0   | 1   |     |
| 1   | 0   | 1   | 0   |     |
| 1   | 0   | 1   | 1   | 1   |
| 1   | 1   | 0   | 0   |     |
| 1   | 1   | 0   | 1   |     |
| 1   | 1   | 1   | 0   |     |
| 1   | 1   | 1   | 1   | 1   |

$Y=ADC+\overline{C}\cdot (\overline{A}B+A\cdot (B+D))$   5 livelli
$=ADC+\overline{C}(B+(\overline{A}+A)+AD)$
$=ADC+\overline{C}(B+AD)$
$=ADC+\overline{C}B+\overline{C}AD$
$=AD(C+\overline{C})+B\overline{C}$
$=AD+B\cdot \overline{C}$   2 livelli

### Mappa di Karnaugh
Rappresentazione grafica della tabella di verità

Regola 1
Coprire tutti gli 1

Regola 2
Minimo numero di gruppi

Regole 3
Gruppi più grandi possibile (in potenze di 2)

| A   | B   | C   | Y   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 0   |
| 1   | 0   | 0   | 1   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |

| A/BC | 00  | 01  | 11  | 10  |
| ---- | --- | --- | --- | --- |
| 0    | 0   | 1   | 0   | 0   |
| 1    | 1   | 1   | 1   | 0   |

|     |     |     | B   | B   |
| --- | --- | --- | --- | --- |
|     | 0   | 1   | 0   | 0   |
| A   | 1   | 1   | 1   | 0   |
|     |     | C   | C   |     |

SH1
$Y=\overline{A}\,\overline{B}C+A\overline{B}\,\overline{C}+A\overline{B}C+ABC$
$=\overline{A}\,\overline{B}C+A\overline{B}\,\overline{C}+A\overline{B}C+A\overline{B}C+A\overline{B}C+ABC$
$=\overline{B}C+A\overline{B}+AC$


|     |     |     | B   | B   |
| --- | --- | --- | --- | --- |
|     | 0   | 1   | 1   | 0   |
| A   | 0   | 1   | 1   | 0   |
|     |     | C   | C   |     |
$Y=\overline{A}\,\overline{B}C+\overline{A}BC+A\overline{B}C+ABC$
$=C(\overline{A}\,\overline{B}+A\overline{B}+\overline{A}B+AB)$
$=C(B(A+\overline{A})+\overline{B}(A+\overline{A}))$
$=C(B+\overline{B})$
$=C$


|     |     |     | B   | B   |
| --- | --- | --- | --- | --- |
|     | 0   | 1   | 1   | 1   |
| A   | 0   | 1   | 1   | 1   |
|     |     | C   | C   |     |
$Y=\overline{A}\,\overline{B}C+\overline{A}BC+A\overline{B}C+ABC+\overline{A}B\overline{C}+AB\overline{C}$
$=B(\overline{A}\,\overline{C}+A\overline{C}+\overline{A}C+AC)+C(\overline{A}\,\overline{B}+A\overline{B}+\overline{A}B+AB)$
$=B(C(A+\overline{A})+\overline{C}(A+\overline{A}))+C(B(A+\overline{A})+\overline{B}(A+\overline{A}))$
$=B(C+\overline{C})+C(B+\overline{B})$
$=B+C$

|     |     |     | B   | B   |     |
| --- | --- | --- | --- | --- | --- |
|     | 1   | 0   | 0   | 1   |     |
|     | 0   | 1   | 1   | 1   | C   |
| A   | 0   | 0   | 0   | 0   | C   |
| A   | 1   | 0   | 0   | 1   |     |
|     |     | D   | D   |     |     |
$Y=+\overline{A}B\overline{D}+\overline{A}CD+\overline{C}\,\overline{D}$

$Y=A\oplus B+B\cdot C$
| A   | B   | C   | Y   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   |
| 0   | 1   | 0   | 1   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 1   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |

| A\BC | 00  | 01  | 11  | 10  |
| ---- | --- | --- | --- | --- |
| 0    | 0   | 0   | 1   | 1   |
| 1    | 1   | 1   | 1   | 0   |

$Y=A\overline{B}+BC+\overline{A}B$
![[A!B+BC+!(A)B.png]]

NAND
Not = $\overline{A\cdot A}$
And = $\overline{\overline{A\cdot B}}$
Or = $\overline{(\overline{A\cdot A}) (\overline{B\cdot B})}$



| $SEL\backslash S_0\ S_1$ | 00  | 01  | 11  | 10  |
| ------------------------ | --- | --- | --- | --- |
| 0                        | 0   | 0   | 1   | 1   |
| 1                        | 0   | 1   | 1   | 0   |
Shannon (2)
$Y=(SEL+S_0)\cdot(\overline{SEL}+S_1)$

| $A\ B\backslash C\ D$ | 00  | 01  | 11  | 10  |
| --------------------- | --- | --- | --- | --- |
| 00                    | 0   | 0   | 0   | 0   |
| 01                    | 1   | 0   | 1   | 1   |
| 11                    | 1   | 0   | 1   | 0   |
| 10                    | 0   | 0   | 0   | 0   |
Shannon (1)
$Y=B\overline{C}\,\overline{D}+BCD+\overline{A}BC$

Shannon (2)
$Y=(B)\cdot(C+\overline{D})\cdot(\overline{A}+\overline{C}+D)$

### Porta logica programmabile
Voglio un sistema con:
	4 ingressi $[A,B,S_0,S_1]$
	IF $S_0=0, S_1=0 \rightarrow Y=AB$
	IF $S_0=0, S_1=1 \rightarrow Y=A+B$
	IF $S_0=1, S_1=0 \rightarrow Y=\overline{A}$
	IF $S_0=1, S_1=1 \rightarrow -$

| $S_0$ | $S_1$ | A   | B   | Y   |
| ----- | ----- | --- | --- | --- |
| 0     | 0     | 0   | 0   | 0   |
| 0     | 0     | 0   | 1   | 0   |
| 0     | 0     | 1   | 0   | 0   |
| 0     | 0     | 1   | 1   | 1   |
|       |       |     |     |     |
| 0     | 1     | 0   | 0   | 0   |
| 0     | 1     | 0   | 1   | 1   |
| 0     | 1     | 1   | 0   | 1   |
| 0     | 1     | 1   | 1   | 1   |
|       |       |     |     |     |
| 1     | 0     | 0   | 0   | 1   |
| 1     | 0     | 0   | 1   | 1   |
| 1     | 0     | 1   | 0   | 0   |
| 1     | 0     | 1   | 1   | 0   |
|       |       |     |     |     |
| 1     | 1     | 0   | 0   | -   |
| 1     | 1     | 0   | 1   | -   |
| 1     | 1     | 1   | 0   | -   |
| 1     | 1     | 1   | 1   | -   |
$- \rightarrow$ Indifferenza sulla uscita (1 o 0 in base a quale viene meglio)
| $S_0$ | $S_1$ | A   | B   | Y   |
| ----- | ----- | --- | --- | --- |
| 0     | 0     | 0   | 0   | 0   |
| 0     | 0     | 0   | 1   | 0   |
| 0     | 0     | 1   | 0   | 0   |
| 0     | 0     | 1   | 1   | 1   |
|       |       |     |     |     |
| 0     | 1     | 0   | 0   | 0   |
| 0     | 1     | 0   | 1   | 1   |
| 0     | 1     | 1   | 0   | 1   |
| 0     | 1     | 1   | 1   | 1   |
|       |       |     |     |     |
| 1     | 0     | 0   | -   | 1   |
| 1     | 0     | 1   | -   | 0   |
|       |       |     |     |     |
| 1     | 1     | -   | -   | -   |

| $S_0\ S_1\backslash A\ B$ | 00  | 01  | 11  | 10  |
| ------------------------- | --- | --- | --- | --- |
| 00                        | 0   | 0   | 1   | 0   |
| 01                        | 0   | 1   | 1   | 1   |
| 11                        | -   | -   | -   | -   |
| 10                        | 1   | 1   | 0   | 0   |
Shannon (1)
$Y=S_0\ \overline{A}+S_1\ A+S1\ B+\overline{S_0}\ A\ B$

Shannon (2)
$Y=(S_0+S_1+A)(\overline{S_1}+A+B)(S_0+S_1+B)(\overline{S_0}+\overline{A})$

### MUX, DEMUX e DEC
###### Multiplexer

| $SEL_1$ | $SEL_0$ | Y     |
| ------- | ------- | ----- |
| 0       | 0       | $S_0$ |
| 0       | 1       | $S_1$ |
| 1       | 0       | $S_2$ |
| 1       | 1       | $S_3$ |
MUX $2^n\rightarrow 1$
$n$: numero selettori

Utilizzato a cascata con multiplexer $2\rightarrow 1$

Può fare da selettore

| $S_1$ | $S_0$ | Y                  |
| ----- | ----- | ------------------ |
| 0     | 0     | $I_0 = U(0,0)$     |
| 0     | 1     | $I_1 = U(0,1)$     |
| 1     | 0     | $I_2 = U(1,0)$<br> |
| 1     | 1     | $I_3 = U(1,1)$     |

| $A$ | $B$ | $A\oplus B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 1           |
| 1   | 0   | 1           |
| 1   | 1   | 0           |

Anche detto **porta logica universale**
###### Demultiplexer

| $S_1$ | $S_0$ | IN  |     | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
| ----- | ----- | --- | --- | ----- | ----- | ----- | ----- |
| 0     | 0     | 0   |     | 0     | 0     | 0     | 0     |
| 0     | 0     | 1   |     | 1     | 0     | 0     | 0     |
| 0     | 1     | 0   |     | 0     | 0     | 0     | 0     |
| 0     | 1     | 1   |     | 0     | 1     | 0     | 0     |
| 1     | 0     | 0   |     | 0     | 0     | 0     | 0     |
| 1     | 0     | 1   |     | 0     | 0     | 1     | 0     |
| 1     | 1     | 0   |     | 0     | 0     | 0     | 0     |
| 1     | 1     | 1   |     | 0     | 0     | 0     | 1     |

| $S_1$ | $S_0$ |     | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
| ----- | ----- | --- | ----- | ----- | ----- | ----- |
| 0     | 0     |     | IN    | 0     | 0     | 0     |
| 0     | 1     |     | 0     | IN    | 0     | 0     |
| 1     | 0     |     | 0     | 0     | IN    | 0     |
| 1     | 1     |     | 0     | 0     | 0     | IN    |

###### Decoder
$n$ input
$2^n$ output

| $I_2$ | $I_1$ | $I_0$ |     | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ | $Y_4$ | $Y_5$ | $Y_6$ | $Y_7$ |
| ----- | ----- | ----- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0     | 0     | 0     |     | 1     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| 0     | 0     | 1     |     | 0     | 1     | 0     | 0     | 0     | 0     | 0     | 0     |
| 0     | 1     | 0     |     | 0     | 0     | 1     | 0     | 0     | 0     | 0     | 0     |
| 0     | 1     | 1     |     | 0     | 0     | 0     | 1     | 0     | 0     | 0     | 0     |
| 1     | 0     | 0     |     | 0     | 0     | 0     | 0     | 1     | 0     | 0     | 0     |
| 1     | 0     | 1     |     | 0     | 0     | 0     | 0     | 0     | 1     | 0     | 0     |
| 1     | 1     | 0     |     | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 0     |
| 1     | 1     | 1     |     | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 1     |

### Tabelle di funzionamento

| $S_0\backslash S_1$ | 0     | 1     |
| ------------------- | ----- | ----- |
| 0                   | $S_0$ | $S_2$ |
| 1                   | $S_1$ | $S_3$ |
Mappe a variabili riportare
	Gli ingressi possono comparire all'interno dei quadrati della mappa di Karnaugh
	Sintesi quasi minima

| A\B | 0   | 1   |
| --- | --- | --- |
| 0   | 1   | I   |
| 1   | 1   | 0   |
Corrisponde a 2 mappe

I=0

| A\B | 0   | 1   |
| --- | --- | --- |
| 0   | 1   | 0   |
| 1   | 1   | 0   |

I=1

| A\B | 0   | 1   |
| --- | --- | --- |
| 0   | 1   | 1   |
| 1   | 1   | 0   |
$Y=\overline{I}(\text{Kmap})+I(\text{Kmap})=\overline{I}(\overline{B})+I(\overline{B}+\overline{A})$

$\overline{I}(\overline{B})+I(\overline{B}) = \overline{B}$
La mappa diventa quindi

| A\B | 0   | 1   |
| --- | --- | --- |
| 0   | -   | 1   |
| 1   | -   | 0   |
$Y=\overline{B}+I\overline{A}$


| $A\backslash B C$ | 00  | 01  | 11  | 10  |
| ----------------- | --- | --- | --- | --- |
| 0                 | 1   | 1   | Y   | Y   |
| 1                 | 1   | X   | 0   | 0   |
X=0, Y=0

| $A\backslash B C$ | 00  | 01  | 11  | 10  |
| ----------------- | --- | --- | --- | --- |
| 0                 | 1   | 1   | 0   | 0   |
| 1                 | 1   | 0   | 0   | 0   |
X=1

| $A\backslash B C$ | 00  | 01  | 11  | 10  |
| ----------------- | --- | --- | --- | --- |
| 0                 | -   | -   | 0   | 0   |
| 1                 | -   | 1   | 0   | 0   |
Y=1

| $A\backslash B C$ | 00  | 01  | 11  | 10  |
| ----------------- | --- | --- | --- | --- |
| 0                 | -   | -   | 1   | 1   |
| 1                 | -   | 0   | 0   | 0   |
$U=\overline{A}\cdot\overline{B}+\overline{B}\cdot\overline{C}+X(\overline{B})+Y(\overline{C})$

#### Passaggi
1- Si individuano le variabili riportate
	X, Y , XY
2- Mappa con tutte le variabili riportare = 0
	Mappa con una variabile riportata per volta = 1 (altre = 0)
3- Si sommano la mappa con tutte + la variabile riportata che moltiplica la sua mappa

| $A B\backslash C D$ | 00  | 01  | 11  | 10  |
| ------------------- | --- | --- | --- | --- |
| 00                  | 1   | 1   | XY  | Y   |
| 01                  | 1   | X   | 0   | 0   |
| 11                  | 0   | -   | -   | 0   |
| 10                  | 0   | X   | 0   | 0   |

$X=0, Y=0, XY=0$

| $A B\backslash C D$ | 00  | 01  | 11  | 10  |
| ------------------- | --- | --- | --- | --- |
| 00                  | 1   | 1   | 0   | 0   |
| 01                  | 1   | 0   | 0   | 0   |
| 11                  | 0   | -   | -   | 0   |
| 10                  | 0   | 0   | 0   | 0   |
$U=\overline{A}\cdot\overline{B}\cdot\overline{D}+\overline{A}\cdot\overline{C}\cdot\overline{D}$


$X=1$
| $A B\backslash C D$ | 00  | 01  | 11  | 10  |
| ------------------- | --- | --- | --- | --- |
| 00                  | -   | -   | 0   | 0   |
| 01                  | -   | 1   | 0   | 0   |
| 11                  | 0   | -   | -   | 0   |
| 10                  | 0   | 1   | 0   | 0   |
}$U=\overline{C}\cdot D$


$Y=1$
| $A B\backslash C D$ | 00  | 01  | 11  | 10  |
| ------------------- | --- | --- | --- | --- |
| 00                  | -   | -   | 0   | 1   |
| 01                  | -   | 0   | 0   | 0   |
| 11                  | 0   | -   | -   | 0   |
| 10                  | 0   | 0   | 0   | 0   |
$U=\overline{A}\cdot\overline{B}\cdot\overline{D}$


$XY=1$
| $A B\backslash C D$ | 00  | 01  | 11  | 10  |
| ------------------- | --- | --- | --- | --- |
| 00                  | -   | -   | 1   | 0   |
| 01                  | -   | 0   | 0   | 0   |
| 11                  | 0   | -   | -   | 0   |
| 10                  | 0   | 0   | 0   | 0   |
$U=\overline{A}\cdot\overline{B}\cdot D$


$U=\overline{A}\cdot\overline{B}\cdot\overline{D}+\overline{A}\cdot\overline{C}\cdot\overline{D}+X(\overline{C}\cdot D)+Y(\overline{A}\cdot\overline{B}\cdot\overline{D})+XY(\overline{A}\cdot\overline{B}\cdot D)$


| $A\backslash B C$ | 00  | 01             | 11  | 10  |
| ----------------- | --- | -------------- | --- | --- |
| 0                 | -   | -              | 1   | -   |
| 1                 | 1   | $\overline{X}$ | X   | 0   |
X=0, $\overline{X}$=0

| $A\backslash B C$ | 00  | 01  | 11  | 10  |
| ----------------- | --- | --- | --- | --- |
| 0                 | -   | -   | 1   | -   |
| 1                 | 1   | 0   | 0   | 0   |
$Y=\overline{A}+\overline{B}\cdot\overline{C}$


X=0

| $A\backslash B C$ | 00  | 01  | 11  | 10  |
| ----------------- | --- | --- | --- | --- |
| 0                 | -   | -   | -   | -   |
| 1                 | -   | 0   | 1   | 0   |
$Y=B\cdot C$


$\overline{X}$=0

| $A\backslash B C$ | 00  | 01  | 11  | 10  |
| ----------------- | --- | --- | --- | --- |
| 0                 | -   | -   | -   | -   |
| 1                 | -   | 1   | 0   | 0   |
$Y=\overline{C}$


$Y=\overline{A}+\overline{B}\cdot\overline{C}+X(B\cdot C)+\overline{X}(\overline{C})$


| $SEL_0\backslash SEL_1$ | 0     | 1     |
| ----------------------- | ----- | ----- |
| 0                       | $S_0$ | $S_2$ |
| 1                       | $S_1$ | $S_3$ |
