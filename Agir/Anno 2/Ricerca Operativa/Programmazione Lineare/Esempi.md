## Industria chimica
Problema di allocazione ottima di risorse scarse
Un'industria chimica produce $4$ tipi di fertilizzanti prodotti in $2$ reparti. Tempi in ore:

|                   | $T_1$ | $T_2$  | $T_3$  | $T_4$ |
| ----------------- | ----- | ------ | ------ | ----- |
| $R_1$             | $2$   | $1.5$  | $0.5$  | $2.5$ |
| $R_2$             | $0.5$ | $0.25$ | $0.25$ | $1$   |
|                   |       |        |        |       |
| $\text{Profitto}$ | $250$ | $230$  | $110$  | $350$ |
Massimo utilizzo settimanale:
- $R_1\leftarrow100\text{ ore}$
- $R_1\leftarrow50\text{ ore}$

Obiettivo: Determinare produzione settimanale per massimizzare profitto
$\max\limits_{x\in S}f(x)$

### Variabili:
$x_i\leftarrow\text{tonnellate di fertilizzante di tipo di prodotto}$
$S\subseteq\{(x_1,x_2,x_3,x_4)\in\mathbb R^4\}$

### Funzione obiettivo
$250\cdot x_1+230\cdot x_2+110\cdot x_3+350\cdot x_4=(x_1,x_2,x_3,x_4)\leftarrow\text{da massimizzare}$

### Vincoli
$2x_1+1.5x_2+0.5x_3+2.5x_4\le 100$
$0.5x_1+0.25x_2+0.25x_3+1x_4\le 50$

$x_1\ge 0,x_2\ge 0,x_3\ge 0,x_4\ge 0$

$\max 250x_1+230x_2+110x_3+350x_4$
$(x_1,x_2,x_3,x_4)\in S$ con $S=\{(x_1,x_2,x_3,x_4)\in\mathbb R^4\text{ che soddisfano }\star\}$
($S\leftarrow\text{insieme ammissibile}$)

# Esempio Non-lineare
## Agenzia Pubblicitaria
Costo al minuto per annuncio radio: $\text{€}100-\text{€}2 \text{ per durata annuncio}\mskip{24mu}\text{Durata massima: }30\text{ minuti}$
Costo giornale: $\text{€}200\text{ per pagina (frazionabili)}$
Almeno $\frac13$ spesa da utilizzare per giornali
$1\text{ minuto annuncio radio: }100\ 000\text{ persone}$
$1\text{ pagina giornale: }15\ 000\text{ persone}$

Raggiungere $3\ 000\ 000$ persone minimizzando i costi

### Variabili
$x_1\text{: minuti radio}\mskip{24mu}x_2\text{: pagine giornale}\mskip{24mu}S\subseteq\mathbb R^2$

### Funzione obiettivo
$\min\limits_{x\in S}f(x)$
$x_1(100-2x_1)+200x_2$

### Vincoli
$200\cdot x_2\ge\frac13\big(x_1(100-2x_1)+200x_2\big)$
$x_1\cdot 100\ 000+x_2\cdot 15\ 000\ge3\ 000\ 000$
$x_1\ge0,x_2\ge0$