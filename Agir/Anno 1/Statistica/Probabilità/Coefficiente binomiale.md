# Proprietà
- ${n\choose {n}}={n\choose{0}}=1$
- ${n\choose k}={n\choose n-k}$
- ${n\choose k}={n-1\choose k-1}+{n-1\choose k}$
- $(a+b)^n=\sum\limits_{k=0}^{n}{n\choose k}a^kb^{n-k}$

# Esercizi
## 1
Mazzo da 52 carte

{fill}

$\mathbb P[\text{full}]$
$\displaystyle\frac{\overbrace{13}^{\text{tris}}\overbrace{12}^{\text{coppia}}{4\choose3}{4\choose2}}{{52\choose 5}}=\frac{13\cdot12\cdot{\color{#F44}4}\cdot{\color{#74F}6}}{{52\choose 5}}\approx0.14\%$
${13\choose2}=\frac{13\cdot12}2$
${4\choose3}=\frac{4\cdot3\cdot2}{3\cdot2\cdot1}={4\choose1}={\color{#F44}4}$


## 2
Scegliendo a caso un monomio di grado $6$ in tre incognite, qual'è la probabilità che compaiano tutte e tre le incognite $x,y,z$?

e.g. $\overset{\color{#4C4}\checkmark}{x^3y^2z},\ {\color{#F44}x^6},\ {\color{#F44}y^3z^3}$

$n=3\text{ oggetti distinti}\quad x,y,z$
$k=6\text{ lunghezza (\# di estrazioni)}$
$\begin{array}{l}\text{Ripetizione:}&\text{Sì}\\\text{Ordine:}&\text{No}\rightarrow\text{Combinazioni}\end{array}$

$\mathbb P[E]=\frac{\text{\# casi favorevoli}}{\text{\# casi possibili}}=\frac{3+3-1\choose 3}{3+6-1\choose 6}=\frac{5\choose 3}{8\choose 6}=\frac{5\choose 2}{8\choose 2}=\frac{\frac{5\cdot 4}{\cancel2}}{\frac{8\cdot 7}{\cancel2}}=\frac{\ 5\cdot\cancel4}{\underset2{\cancel8}\cdot 7\ }=\frac5{14}\approx36\%<\frac12$

### Formula
Combinazioni di lunghezza $k$ con ripetizioni
$\text{\# modi}={n+k-1\choose k}$


$x^3y^2z=xyz(x^2y)$
$\text{casi favorevoli:}\quad \begin{array}{l}n=3&x\ y\ z\\k=\text{grado}&3=6-3\end{array}$

# Probabilità condizionata
Estraggo da un mazzo di $52$ carte ($4$ semi)
Qual'è la probabilità di estrarre $2\ \clubsuit$?

$\mathbb P[2 \ \clubsuit]=\frac{13\choose 2}{52\choose 2}=\frac{\frac{13\cdot 12}{\cancel2}}{\frac{52\cdot51}{\cancel 2}}=\frac{13\cdot12}{52\cdot51}={\color{#F94}\frac{13}{52}}\overbrace{{\frac{12}{51}}}^{\mathbb P[F|E]}$
$\mathbb P[2\ \clubsuit]=(\underbrace{1^o\ \clubsuit}_E)\cap(\underbrace{2^o\ \clubsuit}_F)$
${\color{#F94}\mathbb P[E]}=\frac{13}{52}=\frac14$
${\color{#C7F}\mathbb P[F]}=\frac{\cancel{51}\cdot 13}{52\cdot \cancel{51}}=\frac14$

$\mathbb P[F|E]=\text{probabilità di }F\text{ sapendo che }E\text{ è accaduto }\leftarrow\text{probabilità condizionata}$
$\mathbb P[E\cap F]=\mathbb P[E]\cdot \mathbb P[F|E]$

$\mathbb P[2\ \clubsuit]={\color{#F94}\frac{13}{52}}\cdot\frac{13-1}{52-1}={\color{#F94}\frac{13}{52}}\cdot\frac{12}{51}$

# Probabilità condizionata
## Definizione
**Probabilità condizionata di $F$ dato $E$**
Dati due eventi $E,\ F$
$\mathbb P[F|E]=\frac{\mathbb P[E\cap F]}{\mathbb P[E]}$

## Osservazione
Se $\mathbb P[E]=0\rightarrow E\cap F\subseteq E\Rightarrow\mathbb P[E\cap F]=0$

$\mathbb P[F|E]=\frac{\mathbb P[E\cap F]}{\mathbb P[E]}=\frac00=0$

## Proprietà
- Dati due eventi $E,\ F$
$\mathbb P[E\cap F]=\mathbb P[E]\cdot \mathbb P[F|E]$

- Data una famiglia di eventi $E_1,\ E_2,\ \ldots,\ E_n$
$\mathbb P[E_1\cap E_2\cap\ldots\cap E_n]=\mathbb P[E_1]\cdot \mathbb P[E_2|E_1]\cdot \mathbb P[E_3|E_1\cap E_2]\cdot\ldots\cdot \mathbb P[E_n|E_1\cap E_2\cap\ldots\cap E_{n-1}]$

## Esercizio
$10$ coppie vanno in crociera prenotando una camera con letto matrimoniale che vengono sistemate a caso nelle $10$ cabine
Qual'è la probabilità che ogni coppia abbia condiviso la stessa stanza?

$\mathbb P[\text{successo}]=\frac{\text{\# casi favorevoli}}{\text{\# casi possibili}}=\frac{(\overbrace{10\cdot9\cdot\ldots\cdot2\cdot1}^\text{stanze})\overbrace{(2\cdot2\cdot\ldots\cdot2)}^{10\text{ stanze}}}{\underbrace{20\cdot19\cdot18\cdot\ldots\cdot2\cdot1}_{\text{letti}}}=\frac{10!2^{10}}{20!}=\frac{\cancel{20}\cdot\cancel{18}\cdot\ldots\cdot\cancel4\cdot\cancel2}{\cancel{20}\cdot19\cdot\cancel{18}\cdot17\cdot\ldots\cdot3\cdot\cancel2\cdot1}=\frac1{19\cdot17\cdot15\cdot\ldots\cdot3\cdot1}$

$\begin{array}{l}E_1&=&1^a\text{ coppia nella stessa stanza}\\E_2&=&2^a\text{ coppia nella stessa stanza}\\&\ \vdots\\E_{10}&=&{10}^a\text{ coppia nella stessa stanza}\end{array}$

$\mathbb P[E_1\cap \ldots\cap E_{10}]=\mathbb P[E_1]\cdot\mathbb P[E_2|E_1]\cdot\mathbb P[E_3|E_1\cap E_2]\cdot\ldots\cdot\mathbb P[E|10|E_1\cap\ldots\cap E_{10}]=\frac{10}{\frac{20\cdot19}2}\frac{9}{\frac{18\cdot17}2}\dots\frac{1}{\frac22}=\frac{\cancel{20}}{\cancel{20}19}\frac{\cancel{18}}{\cancel{18}17}\dots\frac{\cancel{2}}{\cancel{2}}=\frac1{19}\frac1{17}\cdot\ldots\cdot\frac13\cdot\frac11$

In un'urna ci sono $10$ palline numerate da $1$ a $10$
Le estraggo consecutivamente senza rimetterle nell'urna

Qual'è la probabilità che alla terza estrazione esca la pallina numero $3$?

$\mathbb P[\text{Pallina numero }3\text{ alla terza estrazione}]=\frac{\#\text{ casi favorevoli}}{\#\text{ casi possibili}}$

$\frac{\cancel{9}\cdot\cancel{8}\cdot\ldots\cdot\cancel{2}\cdot\cancel{1}}{10\cdot\cancel{9}\cdot\cancel{8}\cdot\ldots\cdot\cancel{2}\cdot\cancel{1}}=\frac{\cancel{9!}}{10\cdot\cancel{9!}}=\frac1{10}=10\%$

# Formula della probabilità totale
1) Dati due eventi $E$ e $F$
$\mathbb P[F]=\mathbb P[E]\cdot \mathbb P[F|E]+\mathbb P[\overline E]\cdot\mathbb P[F|\overline E]$

## Esempio 1
Estraggo $2$ carte consecutivamente da un mazzo di $52$ carte con $4$ semi senza rimettere le carte estratte nel mazzo.
Qual'è la probabilità che la seconda carta sia $\clubsuit$?

$\mathbb P[\underbrace{2^a\ \clubsuit}_F]=\mathbb P[\underbrace{1^a\ \clubsuit}_E]\cdot \mathbb P[\underbrace{2^a\ \clubsuit\ |\ 1^a\ \clubsuit}_{F|E}]+\mathbb P[\underbrace{1^a\ \cancel\clubsuit}_{\overline E}]\cdot \mathbb P[\underbrace{2^a\ \clubsuit\ |\ 1^a\ \cancel\clubsuit}_{F|\overline E}]=\frac{13}{52}\frac{12}{51}+\frac{39}{52}\frac{13}{51}=\frac{13}{52}\frac{12}{51}+\frac{13}{52}\frac{39}{51}=\frac{13}{52}\frac{12+39}{51}=\frac{13}{52}\frac{\cancel{51}}{\cancel{51}}=\frac{13}{52}=\frac14=\mathbb P[1^a\ \clubsuit]$

2) Una famiglia $E_1,\ldots,E_n$ di eventi a due a due disgiunti $E_i\cap E_j=\emptyset\ \ i\ne j$ e $\Omega=E_1\cup E_2\cup\ldots\cup E_n$ e un evento $F$
$\mathbb P[F]=\mathbb P[E_1]\cdot \mathbb P[F|E_1]+\mathbb P[E_2]\cdot \mathbb P[F|E_2]+\ldots+\mathbb P[E_n]\cdot \mathbb P[F|E_n]$

## Esempio 2
Lancio un dado equilibrato con le facce numerate da $1$ a $6$. In bae al risultato ottenuto lancio una moneta equilibrata tante volte quanto è il risultato del dado. Qual'è la probabilità di ottenere, esattamente, $4$ teste?

$\mathbb P[^"1^"]=\ldots=\mathbb P[^"6^"]=\frac16$
$\mathbb P[4\ T|^"1^"]=\mathbb P[4\ T|^"2^"]=\mathbb P[4\ T|^"3^"]=0$

$\displaystyle\mathbb P[4\ T|^"4^"]=\frac{4\choose 0}{2^4}=\frac1{16}$

$\displaystyle\mathbb P[4\ T|^"5^"]=\frac{5\choose 1}{2^5}=\frac5{32}$

$\displaystyle\mathbb P[4\ T|^"6^"]=\frac{6\choose 2}{2^6}=\frac{15}{64}$



$\mathbb P[4\ T]=\mathbb P[^"1^"]\cdot\mathbb P[4\ T|^"1^"]+\ldots+\mathbb P[^"6^"]\cdot\mathbb P[4\ T|^"6^"]=\frac16\cdot0+\frac16\cdot0+\frac16\cdot0+\frac16\frac1{16}+\frac16\frac5{32}+\frac16+\frac{15}{64}$


# Formula di Bayes
$\mathbb P[{\color{#C7F}E}\cap {\color{#4C4}F}]=\mathbb P[{\color{#C7F}E}]\cdot \mathbb P[{\color{#4C4}F}|{\color{#C7F}E}]=\mathbb P[{\color{#4C4}F}]\cdot\mathbb P[{\color{#C7F}E}|{\color{#4C4}F}]$

## Esempio
Estraggo $2$ carte senza rimpiazzo da un mazzo di $52$ carte con $4$ semi.
Qual'è la probabilità che la prima esca di fiori, sapendo che la seconda è di fiori?

$\displaystyle\mathbb P[1^a\ \clubsuit\ |\ 2^a\ \clubsuit]=\frac{\overbrace{\frac{13}{52}}^{1^a\ \clubsuit}\cdot\overbrace{\frac{12}{51}}^{2^a\ \clubsuit\ |\ 1^a\ \clubsuit}}{\underbrace{\frac{13}{52}\cdot\frac{12}{51}+\frac{39}{52}\cdot\frac{13}{51}}_{2^a\ \clubsuit}}=\frac{\cancel{\frac14}\frac{12}{51}}{\cancel{\frac14}}=\frac{12}{51}$

# Formula di Bayes (caso generale)
Data una famiglia $E_1,\ldots,E_n$ di eventi tale che:
- $E_i\cap E_j=\emptyset\ \ i\ne j$
- $\Omega=E_1\cup E_2\cup\ldots\cup E_n$
e un evento $F$
$\mathbb P[E_i|F]=\frac{\mathbb P[E_i]\cdot\mathbb P[F|E_i]}{\mathbb P[F]}\quad\small i=1,\ldots,n$

## Esempio
Lancio un dado equilibrato con le facce numerate da $1$ a $6$. In bae al risultato ottenuto lancio una moneta equilibrata tante volte quanto è il risultato del dado. Qual'è la probabilità di ottenere $^"5^"$ sapendo che sono uscite $4$ teste?

$\mathbb P[^"5^"|4\ T]=\frac{\frac16\cdot\frac5{36}}{\frac16\frac1{16}\cdot\frac16\frac5{36}\cdot\frac16\frac{15}{64}}=\frac{10}{29}\approx34\%$

# Indipendenza
1) Dati due eventi $E$ e $F$ si dicono indipendenti se
- $\mathbb P[E\cap F]=\mathbb P[E]\cdot \mathbb P[F]$ e si scrive $E\perp\!\!\!\perp F$ ($E$ e $F$ indipendenti)
- $\mathbb P[E\cup F]=\mathbb P[E]+ \mathbb P[F]$ se $E$ e $F$ sono disguinti

## Osservazione
Se $E$ e $F$ sono disgiunti $E\cap F=\emptyset\Rightarrow\mathbb P[E\cap F]=0$
Se $E$ e $F$ sono **anche** indipendenti $0=\mathbb P[E\cap F]=\mathbb P[E]\cdot\mathbb P[F]\ \ \begin{array}c\nearrow&\!\!\!\mathbb P[E]=0\\\searrow&\!\!\!\mathbb P[F]=0\end{array}$

2) Tre eventi $E_1, E_2$ e $E_3$ sono indipendenti se
- $\mathbb P[E_1\cap E_2\cap E_3]=\mathbb P[E_1]\cdot\mathbb P[E_2]\cdot\mathbb P[E_3]$
	- $\mathbb P[E_1\cap E_2]=\mathbb P[E_1]\cdot \mathbb P[E_2]$
	- $\mathbb P[E_1\cap E_3]=\mathbb P[E_1]\cdot \mathbb P[E_3]$
	- $\mathbb P[E_2\cap E_3]=\mathbb P[E_2]\cdot \mathbb P[E_3]$
# Regola del prodotto (per eventi indipendenti)

$\mathbb P[E\cap F]=\mathbb P[E]\cdot\mathbb P[F]$ se $E$ e $F$ sono indipendenti
$\mathbb P[E_1\cap\ldots\cap E_n]=\mathbb P[E_1]\cdot\ldots\cdot\mathbb P[E_n]$ se $E_1,\ldots,E_n$ indipendenti

Se non sono indipendenti
$\mathbb P[E\cap F]=\mathbb P[E]\cdot\mathbb P[F|E]$
