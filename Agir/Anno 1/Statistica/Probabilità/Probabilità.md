$T, T, C, C, T, T, T, \ldots$

Esperimento casuale, aleatorio, randomico
È una procedura tale che se ripetuta nelle stesse condizioni produce risultati diversi

$\Omega=\text{Spazio campionario: Insieme di tutti i possibili risultati}$

$\begin{array}{l}\text{Lancio di moneta}&\Omega=\{T,C\}\\\text{Lancio del dado}&\Omega=\{1,2,3,4,5,6\}\\\text{Voti statistica}&\Omega=\{18,19,\ldots,30,30\text{ e lode}\}\\\text{Altezza studenti}&\Omega=[0,+\infty)\end{array}$

# Evento
Un evento $E$ è un sottoinsieme di $\Omega$
$E\subseteq\Omega$
$E$ è una collezione di possibili risultati

$\text{Lancio del dado}\qquad E=\text{"Numero pari"}=\{2,4,6\}\qquad E=\text{"Numero primo"}=\{1,2,3,5\}$


Dato un evento $E\subseteq\Omega$, se esce il risultato $\omega\in\Omega$
- $\omega\in E\qquad E\text{ è accaduto}$
- $\omega\notin E\qquad E\text{ non è accaduto}$

Esce il quattro  $\omega=4$
- $4\in E\qquad E\text{ è accaduto = è uscito un numero pari}$
- $4\notin F\qquad F\text{ non è accaduto = non è uscito un numero pari}$


$\Omega=\text{Evento certo (tutti i possibili risultati)}$
$\varnothing=\text{Evento impossibile}$
$E\in\Omega\qquad \overline E=\{\omega\in\Omega|w\notin E\}=\text{Evento opposto}$

$\begin{array}{l}E=\text{Numeri pari}=\{2,4,6\}&\overline E=\{1,3,5\}=\text{Numeri dispari}\\F=\text{Numeri primi}=\{1,2,3,5\}&\overline F=\{4,6\}=\text{Numeri non primi}\end{array}$

$E$ ed $F$ due eventi
$E\cap F=\{\omega\in\Omega\ |\ \omega\in E\ \cap \ \omega\in F\}\quad\text{Evento congiunto}$
$E\cup F=\{\omega\in\Omega\ |\ \omega\in E\ \cup \ \omega\in F\}\quad\text{Evento unione}$

$E=\text{Numero pari}=\{2,4,6\}$
$F=\text{Numero primo}=\{1,2,3,5\}$

$E\cap F=\{2\}$
$E\cup F=\{1,2,3,4,5,6\}=\Omega$



$E$ evento  $E\subseteq\Omega$
$\mathbb P[E]=\mathbb P(E)=\text{Probabilità dell'evento }E\text{ tale che:}\quad\begin{array}{l}\mathbb P[\Omega]=1&100\%\\E\subseteq\Omega&0\le\mathbb P[E]\le 1\\\text{se }E\ \cap F=\varnothing&\mathbb P[E\ \cup F]=\mathbb P[E]+\mathbb P[F]\end{array}$

$\Omega$ ha area $1\times 1=1$
$\mathbb P[E]$ come "area"$\quad0\le\underbrace{\mathbb P[E]}_{\text{area}}\le 1$

$E\ \cap F=\varnothing\Rightarrow\mathbb P[E\ \cup F]=\mathbb P[E] + \mathbb P[F]$
$E\ \cap F\ne\varnothing\Rightarrow\mathbb P[E\ \cup F]\ne\mathbb P[E] + \mathbb P[F]$



# Lancio di un dado equilibrato
$\Omega=\{1,2,3,4,5,6\}$
$\mathbb P[E]=\frac{\# E}{\# \Omega}=\frac{\text{Casi favorevoli}}{\text{Casi possibili}}=\frac{\text{Numero elementi in E}}6$

Probabilità che esca $2$
$E=\{2\}$
$\mathbb P[E]=\frac16=0.1\overline6\approx0.17\approx17\%$

$\mathbb P[\{1\}]=\mathbb P[\{2\}]=\ldots=\mathbb P[\{6\}]\approx17\%$

$\mathbb P[\{\underbrace{\text{Numero pari}}_{E=\{2,4,6\}}\}]=\frac36=\frac12=50\%$
$\mathbb P[\{\underbrace{\text{Numero primo}}_{E=\{1,2,3,5\}}\}]=\frac46=\frac23\approx67\%$

$\mathbb P[E\cup F]=\mathbb P[\text{Numero pari o numero primo}]=\mathbb P[\Omega]=\frac66=1=100\%$



Lancio due dadi equilibrati
1) $\underbrace{\text{Probabilità somma }\color{#F44}{7}}_E$
2) $\underbrace{\text{Probabilità somma } \color{#47F}11}_F$

$\Omega=\{2,3,\ldots,12\}$

| $\array{&\mathrm{II}\\\mathrm{I}}$ | $1$             | $2$             | $3$             | $4$             | $5$              | $6$              |
| ---------------------------------- | --------------- | --------------- | --------------- | --------------- | ---------------- | ---------------- |
| $1$                                | $2$             | $3$             | $4$             | $5$             | $6$              | $\color{#F44}7$  |
| $2$                                | $3$             | $4$             | $5$             | $6$             | $\color{#F44}7$  | $8$              |
| $3$                                | $4$             | $5$             | $6$             | $\color{#F44}7$ | $8$              | $9$              |
| $4$                                | $5$             | $6$             | $\color{#F44}7$ | $8$             | $9$              | $10$             |
| $5$                                | $6$             | $\color{#F44}7$ | $8$             | $9$             | $10$             | $\color{#47F}11$ |
| $6$                                | $\color{#F44}7$ | $8$             | $9$             | $10$            | $\color{#47F}11$ | $12$             |

$\Omega=\{(i,j)|\array{i=1,\ldots,6\\j=1,\ldots,6}$

$\mathbb P[\text{Somma }7]=\mathbb P[E]=\frac{\color{#F44}{\#E}}{\#\Omega}=\frac{\color{#F44}{6}}{6\cdot 6}=\frac16\approx17\%$
$\mathbb P[\text{Somma }11]=\mathbb P[F]=\frac{\color{#47F}{\#E}}{\#\Omega}=\frac{\color{#47F}{2}}{6\cdot 6}=\frac1{18}=0.0\overline5\approx5.55\%$


Lancio tre dadi equilibrati
1) $\underbrace{\text{Probabilità somma }\color{#F44}{9}}_E$
2) $\underbrace{\text{Probabilità somma } \color{#47F}10}_F$

$\color{#F44}E$ somma $9$
$\underset{6=3!}{1+2+6},\ \underset{6}{1+3+5},\ \underset{3=2!}{1+4+4},\ \underset{3}{2+2+5},\ \underset{6}{2+3+4},\ \underset{1=1!}{3+3+3}$ 

$\color{#47F}F$ somma $10$
$\underset{6}{1+3+6},\ \underset{6}{1+4+5},\ \underset{3}{2+2+6},\ \underset{6}{2+3+5},\ \underset{3}{2+4+4},\ \underset{3}{3+3+4}$

$\mathbb P[{\color{#F44}\text{Somma }9}]=\frac{25}{6\cdot6\cdot6}=\frac{25}{216}\approx11.6\%$

# Proprietà

- $\mathbb P[\varnothing]=0$
- $E\subseteq F\quad\text{allora }\mathbb P[E]\le \mathbb P[F]$
- $E$ e $F$ due eventi    $\mathbb P[E\cup F]=\mathbb P[E]+\mathbb P[F]-\mathbb P[E\cap F]$
- $E_1,\ldots,E_n$ famiglia di insiemi a due a due disgiunti, cioè $E_i\cap E_j=\varnothing\quad i\neq j$ allora $\mathbb P[E_1\cup\ldots\cup E_n]=\mathbb P[E_1]+\ldots+\mathbb P[E_n]$
- $E_1, E_2, E_3$ eventi    $\mathbb P[E_1\cup E_2\cup E_3]=\mathbb P[E_1]+\mathbb P[E_2]+\mathbb P[E_3]-(\mathbb P[E_1\cap E_2]+\mathbb P[E_1\cap E_3]+\mathbb P[E_2\cap E_3])+\mathbb P[E_1\cap E_2\cap E_3]$
- $\mathbb P[\overline E]=1-\mathbb P[E]$

# Paradosso dei compleanni
In un gruppo di $n$ persone:
- Qual'è la probabilità che ci siano almeno $2$ persone nate lo stesso giorno?
- Qual'è la probabilità che ci sia ancora una persona nata il nostro stesso giorno?

$\omega=\{1,2,\ldots,365\}$

$n>365\quad\mathbb P_n=\mathbb P[\text{almeno due persone nate lo stesso giorno}]=1$
$n=2\quad\mathbb P_2=\frac{\cancel{365}\cdot 1}{365\cdot\cancel{365}}=\frac1{365}\approx 0.3\%$

$n=3\quad\mathbb P_n=\mathbb P[\text{almeno due persone nate lo stesso giorno}]=\mathbb P[E_{AB}\cup E_{AC}\cup E_{BC}]$
$\mathbb P[E_{AB}]+\mathbb P[E_{AC}]+\mathbb P[E_{BC}]-(\mathbb P[E_{AB}\cap E_{AC}]+\mathbb P[E_{AB}\cap E_{BC}]+\mathbb P[E_{Ac}\cap E_{BC}])+\mathbb P[E_{AB}\cap E_{AC}\cap E_{BC}]=3\mathbb P[E_AB]-3\mathbb P[\text{3 persone nate lo stesso giorno}]+\mathbb P[\text{3 persone nate lo stesso giorno}]$
$\displaystyle3\underbrace{\frac{\cancel{365}\cdot1\cdot\cancel{365}}{365\cdot\cancel{365}\cdot\cancel{365}}}_{\frac1{365}}-2\underbrace{\frac{\cancel{365}\cdot1\cdot1}{365\cdot365\cdot\cancel{365}}}_{\frac1{365^2}}$
$\mathbb P_3=\frac3{365}-2\frac1{365^2}\approx 0.8\%$


$E=\text{almeno due persone nate lo stesso giorno}$

$\overline E=n\text{ persone nate tutti in giorni diversi}$

$n>365\quad \overline E=\varnothing\quad\mathbb P[\varnothing]=1\quad\mathbb P[E]=1$

$2\le n\le365$
$\mathbb P_n=\mathbb P[\overline E]=\frac{\text{casi possibili}}{\text{casi favorevoli}}=\frac{365\cdot364\cdot\ldots\cdot(365-n+1}){{365}^n}=\frac{365}{365}+\frac{364}{365}+\ldots+\frac{365-n+1}{365}=\mathbb P_{n-1}\frac{365-n+1}{365}=1\frac{365-1}{365}\cdot\frac{365-(n-1)}{365}=1(1-\frac{1}{365})(1-\frac{n-1}{365})=\underbrace{1(1-\frac{1}{365})(1-\frac{(n-1)-1}{365})}_{\mathbb P_{n-1}}(1-\frac{n-1}{365})$

$1-x\approx e^{-x}$
$y=x+1$ simile a $e^x<<1$

$\approx 1e^{-\frac1{365}}e^{-\frac{n-1}{365}}=e^{-\frac1{365}-\dots-\frac{n-1}{365}}$

$\mathbb P[\overline E]\approx e^{-\frac{1+\ldots+(n-1)}{365}}=e^{-\frac1{365}\frac{(n-1)n}2}$

$\displaystyle\mathbb P[R]=1-\mathbb P[\overline E]\approx1- e^{-\frac{1+\ldots+(n-1)}{365}}=e^{-\frac1{365}\frac{(n-1)n}2}$

| $n$  | $\mathbb P[E]$ | $\approx$ |
| ---- | -------------- | --------- |
| $2$  | $0.3\%$        | $0.3\%$   |
| $3$  | $0.8\%$        | $0.8\%$   |
| $5$  | $2.7\%$        | $2.7\%$   |
| $10$ | $11.7\%$       | $11.6\%$  |
| $20$ | $41.1\%$       | $40.6\%$  |
| $23$ | $50.7\%$       | $50\%$    |
| $30$ | $70.6\%$       | $69.6\%$  |
| $50$ | $97\%$         | $96.5\%$  |


## Seconda richiesta
$F=\text{almeno una persona nata l'1/01}$
$\overline F=\text{nessuna persona nata l'1/01}$

$\mathbb P[F]=1-\mathbb P[\overline F]=1-\frac{364\cdot\ldots364}{365\cdot\ldots\cdot365}=1-(\frac{364}{365})^n=1-(\frac{365-1}{365})^n=1-(1-\frac{1}{365})^n\approx1-\left[e^{\frac1{365}}\right]^n=1-e^{-\frac n{365}}$

| $n$  | $\mathbb P[E]$ | $\approx$ | $\mathbb P[F]$ |
| ---- | -------------- | --------- | -------------- |
| $2$  | $0.3\%$        | $0.3\%$   | $0.5\%$        |
| $3$  | $0.8\%$        | $0.8\%$   | $0.8\%$        |
| $5$  | $2.7\%$        | $2.7\%$   | $1.4\%$        |
| $10$ | $11.7\%$       | $11.6\%$  | $2.7\%$        |
| $20$ | $41.1\%$       | $40.6\%$  | $5.3\%$        |
| $23$ | $50.7\%$       | $50\%$    | $6.1\%$        |
| $30$ | $70.6\%$       | $69.6\%$  | $7.9\%$        |
| $50$ | $97\%$         | $96.5\%$  | $12.8\%$       |

# Spazio di probabilità finito
Uno spazio di probabilità si dice **finito** se lo spazio campionario $\Omega$ ha un numero finito di elementi  $\Omega=\{\omega_1,\ldots,\omega_n\}\quad\omega_i\neq\omega_j\quad i\ne j\quad n\in\mathbb N$

La probabilità di un evento è nota conoscendo la probabilità dei possibili risultati

| $\omega$   | $\mathbb P[\{\omega\}]$ |
| ---------- | ----------------------- |
| $\omega_1$ | $\mathbb P_1$           |
| $\omega_2$ | $\mathbb P_2$           |
| $\vdots$   | $\vdots$                |
| $\omega_n$ | $\mathbb P_n$           |
(distribuzione di probabilità)


Per $\mathbb P_n\ge 0\quad\mathbb P_1+\mathbb P_2+\ldots+\mathbb P_n=1\Rightarrow \underset{i=1,\ldots,n}{0\le\mathbb P_i\le1}$
$M=\#E$
$\mathbb P[E]=\{\omega_{i_1},\ldots,\\omega_{i_M}\}=\mathbb P[\{\omega_{i_1}\}]+\ldots+\mathbb P[\{\omega_{i_M}\}]=p_{i_1}+\ldots+p_{i_M}$
$E=\{\omega_2,\omega_2\}\quad\mathbb P[E]=p_2+p_3$

## Lancio di una moneta
$\omega=\{T,C\}\quad n=2$

| $\omega$ | $\mathbb P[\{\omega\}]$ |
| -------- | ----------------------- |
| $T$      | $p$                     |
| $C$      | $q$                     |
$\begin{cases}p\ge 0&q\ge1\\p+q=1\end{cases}\quad\cases{q=1-p\\p\ge0\\p\le1}$

| $\omega$ | $\mathbb P[\{\omega\}]$ |
| -------- | ----------------------- |
| $T$      | $p$                     |
| $C$      | $1-p$                   |
$0\le p\le1$
$p=\mathbb P[T]$
$1-p=q=\mathbb P[C]$

### Moneta equilibrata

$\mathbb P[T]=\mathbb P[C]\iff p=1-p\iff p=\frac12$
| $\omega$ | $\mathbb P[\{\omega\}]$ |
| -------- | ----------------------- |
| $T$      | $\frac12$               |
| $C$      | $\frac12$               |

## Dado
Lancio un dado in cui la probabilità di "due" è doppia degli altri numeri.
Qual'è la probabilità che esca un numero pari?

| $\omega$ | $\mathbb P[\{\omega\}]$ | <         |
| -------- | ----------------------- | --------- |
| $1$      | $p$                     | $\frac17$ |
| $2$      | $2p$                    | $\frac27$ |
| $3$      | $p$                     | $\frac17$ |
| $4$      | $p$                     | $\frac17$ |
| $5$      | $p$                     | $\frac17$ |
| $6$      | $p$                     | $\frac17$ |

$\mathbb P[\underbrace{\text{"Numero pari"}}_E]=\underset{\array{\#E=3\\\#\omega=6}}{\mathbb P[\{{\color{#F44}2},{\color{#47F}4},{\color{#4C4}6}\}]}={\color{#F44}\frac27}+{\color{#47F}\frac17}+{\color{#4C4}\frac17}=\frac47\in[0,1]$
$\mathbb P[\text{"Numero dispari"}]=\mathbb P[\{1,3,5\}]=1-\frac47=\frac37$



$\Omega=\{\omega_1,\omega_2,\ldots,\omega_N\}$
$N=\#\Omega\quad\omega_i\ne\omega_j\quad =\ne j$

| $\omega$   | $\mathbb P[\{\omega\}]$ |
| ---------- | ----------------------- |
| $\omega_1$ | $p$                     |
| $\omega_2$ | $p$                     |
| $\vdots$   | $\vdots$                |
| $\omega_N$ | $p$                     |
$p\ge 0\quad \underbrace{p+\ldots+p}_{N\text{ addendi}}=1\qquad Np=1\quad p=\frac1N\in\mathbb N\iff\mathbb P[\{\omega_i\}]=\frac1N\ \ \small i=1,\ldots,N$

$\mathbb P[E]=\mathbb P[\{\omega_{i_1},\ldots,\omega_{i_M}\}]=p_{i_1}+\ldots+p_{i_M}=\frac MN=\frac{\#E}{\#\Omega}\quad\array{E\subseteq\Omega\\\#E=M}$

$\mathbb P[E]=\frac{\text{Casi favorevoli}}{\text{Casi possibili}}$   Solo per spazi equiparabile


# Fattoriale
$n\in \mathbb N$
$n!=n\cdot(n-1)\cdot\ldots\cdot2\cdot1$
$\color{orange}0!=1$

## Coefficiente binomiale
$n,k\in\mathbb N\quad 0\le k\le n$

$n\choose k=\frac{n!}{k!(n-k)!}$
$5\choose 3=\frac{5!}{3!(2)!}=\frac{120}{6\cdot 2}=10$

## Calcolo combinatorio
$n\text{ oggetti distinti}$
$k\text{ estrazioni}$

Modalità di estrazione
1) Estrazione senza ripetizioni
2) Estrazione con ripetizione

Modalità di memorizzazione del risultato
1) Si tiene conto dell'ordine (permutazioni)
2) Non si tiene conto dell'ordine (combinazioni)

Il calcolo combinatorio conta in quanti modi posso fare le estrazioni
$n=\text{numero oggetti}\quad k=\text{numero estrazioni (lunghezza)}$
 
1) Permutazioni (ordine si) senza ripetizioni (no permutazione)
$k\le n\qquad\text{numero modi}=n(n-1)\ldots(n-k+1)$
2) Permutazioni con ripetizioni
$\text{numero modi}=\underbrace{n\cdot\ldots\cdot n}_{k\text{ volte}}=n^k$

Se $k=n$ permutazioni a lunghezza $n=\text{permutazioni}$
$\#\text{nomi}=n(n-1)\ldots 1=n!$

# Lancio di moneta truccata
$\mathbb P[T]=\frac23$
Qual'è la probabilità di ottenere $2$ teste e $1$ croce con $3$ lanci?
$\mathbb P[2T\ 1C]=\mathbb P\underbrace{\left[\{TTC\}\cup\{TCT\}\cup\{CTT\}\right]}_{3={3\choose 2}={3\choose 1}=\text{\# casi favorevoli}}=3\mathbb P[TTC]=3\mathbb P[\{I^o=T\}\cup\{II^o=T\}\cup\{III^o=C\}]\underset{\perp\!\!\perp}{=}3\mathbb P[I^o=T]\mathbb P[II^o=T]\mathbb P[III^o=C]=3\mathbb P[T]\mathbb P[T]\mathbb P[C]=\cancel3\frac23\frac23\frac1{\cancel3}=\frac49$

# Urne
$\begin{array}{l}\text{Urna }A:&5{\color{#F44}\text{ palline}}&5{\color{#74F}\text{ palline}}\\\text{Urna }B:&4{\color{#F44}\text{ palline}}&6{\color{#74F}\text{ palline}}\end{array}$

Viene lanciata una moneta truccata $\mathbb P[T]=\frac34$
Se esce $T$ estraggo $2$ palline senza rimpiazzo da urna $A$
Se esce $C$ estraggo $2$ palline con rimpiazzo da urna $B$

1) Sapendo che è uscito $T$, qual'è la probabilità di estrarre $1{\color{#F44}\text{ rossa}}$ e $1{\color{#74F}\text{ blu}}$?
$E={\color{#F44}R}{\color{#74F}B}\quad(\text{non interessa ordine})$
$\displaystyle\mathbb P[E|T]=\mathbb P[{\color{#F44}R}{\color{#74F}B}|T]=\frac{{5\choose1}{5\choose1}}{10\choose2}=\frac{\cancel5\cdot 5}{\cancel{45}_9}=\frac59$
2) Sapendo che è uscito $C$, qual'è la probabilità di estrarre $1{\color{#F44}\text{ rossa}}$ e $1{\color{#74F}\text{ blu}}$?
$\displaystyle\mathbb P[E|C]=\mathbb P[{\color{#F44}R}{\color{#74F}B}|C]=\mathbb P[{\color{#F44}R}_1{\color{#74F}B}_2|C]+\mathbb P[{\color{#74F}B}_1{\color{#F44}R}_2|C]=\frac4{10}\frac6{10}+\frac6{10}\frac4{10}=\frac{4\cdot 6}{10\cdot 10}+\frac{6\cdot 4}{10\cdot 10}=\frac{12}{25}$
3) Qual é la probabilità di estrarre $1{\color{#F44}\text{ rossa}}$ e $1{\color{#74F}\text{ blu}}$?
$\mathbb P[{\color{#F44}R}{\color{#74F}B}]=\mathbb P[T]\cdot\mathbb P[{\color{#F44}R}{\color{#74F}B}|T]+\mathbb P[C]\cdot\mathbb P[{\color{#F44}R}{\color{#74F}B}|C]=\frac34\frac59+\frac14\frac{12}{25}=\frac{161}{300}\approx54\%$
4) Sapendo che é uscita $1{\color{#F44}\text{ rossa}}$ e $1{\color{#74F}\text{ blu}}$, qual'è la probabilità che si uscito $T$?
$\displaystyle\mathbb P[T|{\color{#F44}R}{\color{#74F}B}]=\frac{\mathbb P[T]\cdot\mathbb P[{\color{#F44}R}{\color{#74F}B}|T]}{\mathbb P[{\color{#F44}R}{\color{#74F}B}]}=\frac{\frac34\frac59}{\underbrace{\frac34\frac59+\frac14\frac{12}{25}}_{\text{\# casi possibili}}}=\frac{125}{161}\approx78\%$