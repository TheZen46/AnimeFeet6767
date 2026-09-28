# Media (empirica)
$x_1,\ldots,x_n\in\mathbb R$

| $v_i$    | $n_i$    | $f_i$    |
| -------- | -------- | -------- |
| $v_1$    | $n_1$    | $f_1$    |
| $v_2$    | $n_2$    | $f_2$    |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $v_m$    | $n_m$    | $f_m$    |

$\overline x=\frac{x_1+x_2+\ldots+x_n}n=\frac{n_1v_1+n_2v_2+\ldots+n_mv_m}n=f_1v_1+f_2v_2+\ldots+f_mv_m$

| Cognome | Voti |
| ------- | ---- |
| A       | 30   |
| B       | 24   |
| C       | 30   |
| D       | 24   |
| E       | 26   |
| F       | 18   |
$\overline x=\frac{30+24+30+24+26+18}6=\frac{76}3\approx 25.3$

Tabella a una via

| $v_i$ | $n_i$ | $f_i$  |
| ----- | ----- | ------ |
| 18    | $1$   | $17\%$ |
| 24    | $2$   | $33\%$ |
| 26    | $1$   | $17\%$ |
| 30    | $2$   | $33\%$ |
$\overline x=\frac{1\cdot 18+2\cdot24+1\cdot 26+2\cdot 30}6=\frac16\cdot 18+\frac13\cdot 24+\frac16\cdot 26+\frac13\cdot 30=\frac{76}3$

## Proprietà
$x_1,\ldots,x_n\in\mathbb R$
$v_1<v_2<\ldots<v_m$

- $v_1\le\overline x\le v_m\ \ \ \ \begin{array}{l}v_1=\text{valore minimo}\\v_m=\text{valore massimo}\end{array}$
- $y_l=a\cdot x_l+b\ \ \ \ a,b\in\mathbb R\ \ \ \ a\ne0$
	$\overline y=a\overline x+b$
### Centratura
$x_1,\ldots,x_n\in\mathbb R\ \ \ \ \overline x=\frac{x_1+\ldots+x_n}n$
$y_1=x_1-\overline x,\ y_2=x_2-\overline x,\ldots,y_n=x_n-\overline x$
$\overline y=\overline{(x-\overline x)}=\overline{ax+b}=a\overline x+b=\overline x-\overline x=0\ \ \ \text{(usando )}a=1,\ b=-\overline x$

#### Osservazione
- $x_l\rightarrow x_l-\overline x=y_l\ \ \ \ \text{centratura}$
- $\text{Se la media }\overline x=0\text{ i dati si dicono a media nulla o }\underline{\text{centrati}}$

# Quartile e mediana
$\begin{array}{l}\text{Peso}&\text{Primo quartile}&25\%\text{ percentile}\\\text{Altezza}&\text{Terzo quartile}&75\%\text{ percentile}\end{array}$

$x_1,x_2,\ldots,x_n$
$\underset{\min}{v_1}<v_2<\ldots<\underset\max{v_m}$

| $v_i$    | $n_i$    | $f_i$    |
| -------- | -------- | -------- |
| $v_1$    | $n_1$    | $f_1$    |
| $v_2$    | $n_2$    | $f_2$    |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $v_m$    | $n_m$    | $f_m$    |

## Definizione di quartile
$Q0=v_1=\min$
$Q1=v_i\ \ \ \ \begin{array}{l}f_1+f_2+\ldots+f_{i-1}&<\frac14\\f_1+f_2+\ldots+f_{i-1}+f_i&\ge\frac14\end{array}$

$Q2=v_i\ \ \ \ \begin{array}{l}f_1+f_2+\ldots+f_{i-1}&<\frac12\\f_1+f_2+\ldots+f_{i-1}+f_i&\ge\frac12\end{array}$
$Q3=v_i\ \ \ \ \begin{array}{l}f_1+f_2+\ldots+f_{i-1}&<\frac34\\f_1+f_2+\ldots+f_{i-1}+f_i&\ge\frac34\end{array}$

$Q0=\text{valore minimo}$
$Q1=\text{primo quartile}$
$Q2=\text{secondo quartile}=\text{mediana}=m$
$Q3=\text{terzo quartile}$
$Q4=\text{valore massimo}$

## Esercizio
$n=12$

| $v_i$ | $n_i$ | $f_1$        | $\approx$ |
| ----- | ----- | ------------ | --------- |
| 1     | 2     | $\frac2{12}$ | $17\%$    |
| 4     | 2     | $\frac2{12}$ | $33\%$    |
| 5     | 1     | $\frac1{12}$ | $42\%$    |
| 8     | 2     | $\frac2{12}$ | $58\%$    |
| 9     | 1     | $\frac1{12}$ | $67\%$    |
| 10    | 2     | $\frac2{12}$ | $83\%$    |
| 12    | 1     | $\frac1{12}$ | $92\%$    |
| 13    | 1     | $\frac1{12}$ | $100\%$   |
|       |       |              |           |
|       | 12    | $100\%$      |           |

$Q0=1$
$Q4=13$

$Q1=4\leftarrow\frac4{12}=33\%\ge25\%$
$Q2=8\leftarrow\frac7{12}\approx58\%\ge50\%$
$Q3=10\leftarrow\frac10{12}\approx83\%\ge75\%$

# Box-Plot
$IRQ=Q3-Q1\ \ \ \ \text{range interquartile}$
$a=Q1-\frac32IRQ$
$b=Q3+\frac32IRQ$

$\text{Baffo sinistro}=\text{valore più piccolo}\ge a$
$\text{Baffo destro}=\text{valore più grande}\le a$
$\text{Outlier sinistri}=\text{valori più piccoli di }a$
$\text{Outlier destri}=\text{valori più grandi di }b$


## Esempio
$\text{Tempo di reazione }(ms)$

| $v_i$ | $f_i$  | $F_i=F(v_i)$ |
| ----- | ------ | ------------ |
| $10$  | $10\%$ | $10\%$       |
| $25$  | $10\%$ | $20\%$       |
| $35$  | $15\%$ | $35\%$       |
| $40$  | $20\%$ | $55\%$       |
| $45$  | $30\%$ | $85\%$       |
| $50$  | $5\%$  | $90\%$       |
| $60$  | $5\%$  | $95\%$       |
| $70$  | $5\%$  | $100\%$      |

$Q0=10$
$Q4=70$
$Q1=35$
$Q2=40$
$Q3=45$



$x_1=1,\ x_2=2,\ldots,\ x_{10}=10$
$\overline x=\frac{1+2+\ldots+10}{10}=\frac{\frac{\cancel{10}\cdot11}2}{\cancel{10}}=\frac{11}2=5.5$
$1+2+\ldots+n=\frac{n(n+1)}2$


$x_1=1,\ x_2=2,\ldots,\ x_9=9,\ x_{10}=100$
$\overline x=\frac{1+2+\ldots+9+100}{10}=14.5$

$Q2=5$

Mediana più "stabile"


# Percentili
$K\text{ percentile}\ \ \ \ \begin{array}{l}K=0,\ldots,100&q=\frac K{100}\in[0,1]\\x_1=v_i&f_1+\ldots+f_{i-1}<q&f_1+\ldots+f_{i-1}+f_i\ge q\end{array}$

| $v_i$ | $f_i$        | $F_i=F(v_i)$ |
| ----- | ------------ | ------------ |
| 1     | $\frac2{12}$ | $17\%$       |
| 4     | $\frac2{12}$ | $33\%$       |
| 5     | $\frac1{12}$ | $42\%$       |
| 8     | $\frac2{12}$ | $58\%$       |
| 9     | $\frac1{12}$ | $67\%$       |
| 10    | $\frac2{12}$ | $83\%$       |
| 12    | $\frac1{12}$ | $92\%$       |
| 13    | $\frac1{12}$ | $100\%$      |

$10^o\text{ percentile}=10\%$
$x_{0.01}=1$

$30^o\text{ percentile}=30\%$
$x_{0.02}=4$

$90^o\text{ percentile}=90\%$
$x_{0.90}=12$

$Q1=25^o\text{ percentile}=25\%$
$Q1=4$

$Q2=50^o\text{ percentile}=50\%$
$Q2=8$

$Q3=75^o\text{ percentile}=75\%$
$Q3=10$

# Indice di dispersione - Varianza
$x_1,x_2,\ldots,x_n\in\mathbb R$

| $v_i$    | $n_i$    | $f_i$    |
| -------- | -------- | -------- |
| $v_1$    | $n_1$    | $f_1$    |
| $v_2$    | $n_2$    | $f_2$    |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $v_m$    | $n_m$    | $f_m$    |

$\overline x=\frac{x_1+x_2+\ldots+x_n}n=\frac{n_1v_1+n_2v_2+\ldots+n_mv_m}n=f_1v_1+f_2v_2+\ldots+f_mv_m$

$I\text{ studente}$
$x_1=24,x_2=24,\ldots,x_{10}=24$
$\overline x=24$
$v_1=24$
$f_1=1$

$II\text{ studente}$
$x_1=18,x_2=18,\ldots,x_5=18,x_6=30,\ldots,x_{10}=30$

$\begin{array}{l}v_1=18&f_1=\frac5{10}=\frac12\\v_2=30&f_2=\frac5{10}=\frac12\end{array}$

$\overline x=\frac1218+\frac1230=\frac{48}2=24$


$\sigma^2=\frac{(x_1-\overline x)^2+(x_2-\overline x)^2+\ldots+(x_n-\overline x)^2}n\ \ \ \ \text{varianza (della popolazione)}$
$s^2=\frac{(x_1-\overline x)^2+(x_2-\overline x)^2+\ldots+(x_n-\overline x)^2}{n-1}\ \ \ \ \text{varianza (del campione)}$

$\sigma^2=\overline{(x-\overline x)^2}$
$s^2=\frac n{n-1}\sigma^2=\frac{n-1+1}{n-1}\sigma^2=(1+\frac1{n-1})\sigma^2$

$n>1\ \ s^2\simeq\sigma^2$

$s^2\ge0$
$\sigma^2\ge0$

$\sigma=\text{deviazione standard popolazione}$
$s=\text{deviazione standard campione}$



$x_1,\ldots,x_n$ hanno la stessa unità di misura (e.g. $\begin{array}{l}\text{altezza}&x_l=m\\\text{peso}&x_l=kg\end{array}$)

$\sigma^2,s^2\ \ \ \ \text{hanno (unità di misura)}^2\qquad\text{e.g. }\begin{array}{l}m^2\\{kg}^2\end{array}$
$\overline x=\frac{x_1+\ldots+x_n}n\ \ \ \ \text{stessa unità di misura di }x_l$

$\sigma\text{ e }s\text{ hanno la stessa unità di misura di }x_1,\ldots,x_n$


$I\text{ studente}$
$x_1=24,x_2=24,\ldots,x_{10}=24$
$\overline x=24$
$\sigma^2=\frac{(x_1-\overline x)^2+(x_2-\overline x)^2+\ldots+(x_n-\overline x)^2}n=\frac{(\cancel{24}-\cancel{24})^2}{10}=0$

$II\text{ studente}$
$x_1=18,x_2=18,\ldots,x_5=18,x_6=30,\ldots,x_{10}=30$
$\overline x=24$
$\sigma^2=\frac{\overbrace{(18-24)^2+\ldots+(18-24)^2}^5+\overbrace{(30-24)^2+\ldots+(30-24)^2}^5}{10}=\frac5{10}\overbrace{36}^{6^2}+\frac5{10}36=36$
$\sigma=6$

## Proprietà
1) $s^2=\frac n{n-1}\sigma^2\ \ \ \ \sigma^2=\frac{n-1}ns^2$
2) ${\sigma^2}=\overline{(x^2)}-(\overline x)^2$
	$\overline{x^2}=\frac{{x_1}^2+{x_2}^2+\ldots+{x_n}^2}n=f_1{v_1}^2+\ldots+f_m{v_m}^2$
3) $\begin{array}{l}y_1=ax_1+b\\\vdots\\y_n=ax_n+b\end{array}\ \ \begin{array}{c}a,b\in\mathbb R\\a\ne0\end{array}\ \ \ \ {\sigma_y}^2=a^2{\sigma_x}^2\ \ \ \ \overline y=a\overline x+b$

# Coefficiente di correlazione
$\begin{array}{l}x_1,x_2,\ldots,x_n\in\mathbb R&&\overline x=\text{media}&\overline y=\text{media}\\y_1,y_2,\ldots,y_n\in\mathbb R&&{\sigma_x}^2=\text{varianza}&{\sigma_y}^2=\text{varianza}\end{array}\{\sigma_x>0\}\{\sigma_y>0\}$

$\displaystyle\underbrace{\rho_{x,y}}_{\text{coefficiente di correlazione}}=\frac{\overline{(xy)}-(\overline x)(\overline y)}{\sigma_x\sigma_y}$
$\overline{xy}=\frac{x_1y_1+\ldots+x_ny_n}n$

## Osservazione
1)
$\sigma_x=0$
${\sigma_x}^2=0\Rightarrow x_1,\ldots,x_n\text{ costante}$
$\frac{(x_1-\overline x)^2+\ldots+(x_n-\overline x)^2}n=0\iff\begin{array}{l}(x_1-\overline x)\\\vdots\\(x_n-\overline x)^2=0\end{array}\iff\begin{array}{l}x_1=\overline x\\\vdots\\x_n=\overline x\end{array}\ \ \ \ x_1=\ldots=x_n=v_1=\overline x$

## Proprietà
1) $\displaystyle\rho_{x,y}=\frac{\overbrace{\frac1n\left[(x_1-\overline x)(y_1-\overline y)+\ldots+(x_n-\overline x)(y_n-\overline y)\right]}^{\text{covarianza tra }x\text{ e }y}}{\sigma_x\sigma_y}$
2) $\rho_{x,y}=\rho_{y,x}$
3) $-1\le\rho_{x_y}\le1$
4) $\rho_{x,x}=1$
5) $\displaystyle\text{se }\begin{array}{l}z_1=ax_1+b\\\vdots\\z_n=ax_n+b\end{array}\ \ \ \ \{a,b\in\mathbb R\}\{a\ne0\}\rightarrow\begin{array}{l}\rho_{x,y}=\rho_{z,y}\\{\sigma_z}^2=a^2{\sigma_x}^2\\\overline z=a\overline z+b\end{array}$

$\rho_{x,y}\text{ è un numero puro}\rightarrow\text{non ha unità di misura}$
	$\color{#2d7}x=m\text{ metri}$
	$\color{#49d}y=kg$
	$\overline x,\sigma_x\text{ metri}$
	$\overline y,\sigma_y\ kg$
	$\displaystyle\rho_{x,y}=\frac{\overline {{\color{#2d7}x}{\color{#49d}y}}-\overline {\color{#2d7}x}\ \overline {\color{#49d}y}}{{\color{#2d7}\sigma_x}{\color{#49d}\sigma_y}}=\frac{\cancel m\cdot \cancel{kg}}{\cancel m\cdot \cancel{kg}}$

## Esempio
$x,y$ variabili con tabella a due vie

| $\begin{array}{c}&y\\x\end{array}$ | $-1$ | $0$ | $1$ |     | $n_{i:}$ |
| ---------------------------------- | ---- | --- | --- | --- | -------- |
| $1$                                | $1$  | $2$ | $3$ |     | $6$      |
| $2$                                | $3$  | $1$ | $0$ |     | $4$      |
|                                    |      |     |     |     |          |
| $n_{:j}$                           | $4$  | $3$ | $3$ |     | $10$     |
$i=1,2\ \ \ \ \ \ \ \ v_1=1,\ v_2=2$
$j=1,2,3\ \ \ \ \ \ \ \ w_1=-1,\ w_2=0,\ w_3=1$

| $\begin{array}{c}&y\\x\end{array}$ | $-1$                            | $0$                            | $1$                            |     | $f_{i:}$     |
| ---------------------------------- | ------------------------------- | ------------------------------ | ------------------------------ | --- | ------------ |
| $1$                                | $\frac1{10}\ ^{\color{#FF0}-1}$ | $\frac2{10}\ ^{\color{#FF0}0}$ | $\frac3{10}\ ^{\color{#FF0}1}$ |     | $\frac6{10}$ |
| $2$                                | $\frac3{10}\ ^{\color{#FF0}-2}$ | $\frac1{10}\ ^{\color{#FF0}0}$ | $0\ ^{\color{#FF0}2}$          |     | $\frac4{10}$ |
|                                    |                                 |                                |                                |     |              |
| $f_{:j}$                           | $\frac4{10}$                    | $\frac3{10}$                   | $\frac3{10}$                   |     | $1$          |
$\overline x=\frac6{10}1+2\frac4{10}=\frac{14}{10}=1.4$
$\overline y=\frac4{10}(-1)+\cancel{\frac{3}{10}0}+\frac{3}{10}1=-\frac1{10}=-0.1$


${\sigma_x}^2=\overline{x^2}-(\overline x)^2=\frac{22}{10}-(\frac{14}{10})^2=\frac6{25}\ \ \ \ \ \ \ \ \sigma_x=\frac{\sqrt6}5\approx0.49$
$\overline {x^2}=\frac6{10}1^2+\frac4{10}2^2=\frac{22}{10}$

${\sigma_y}^2=\overline{y^2}-(\overline y)^2=\frac7{10}-(-\frac1{10})^2=\frac7{10}-\frac1{100}=\frac{69}{100}\ \ \ \ \ \ \ \ \sigma_y=\frac{\sqrt{69}}10\approx0.83$
$\overline{y^2}=\frac4{10}(-1)^2+\frac3{10}1^2=\frac7{10}$


$\displaystyle\rho_{xy}=\frac{\overline{xy}-\overline x\ \overline y}{\sigma_x\sigma_y}$
$\overline{xy}=\frac1{10}({\color{yellow}{-1}})+\frac3{10}({\color{yellow}{-2}})+\frac3{10}({\color{yellow}1})=-\frac45$
$\displaystyle\rho_{xy}=\frac{-\frac45-\frac{14}{10}\left(-\frac1{10}\right)}{\frac{\sqrt6}5\frac{\sqrt{69}}{10}}=-\frac{13}{3\sqrt{46}}\approx-0.6389$