# Definizione
Data una successione $\{a_n\}_n$ di numeri reali, consideriamo $\sum\limits_{n=n_0}^\infty a_n=\sum\limits_{n\ge n_0}a_n=a_{n_0}+a_{n_0+1}+a_{n_0+2}+\ldots$
È fondamentalmente definita come $\sum\limits_{n=n0}^\infty a_n=\lim_{N\to\infty} S_N$, dove $S_N:=\sum\limits_{n=n_0}^N=a_{n_0}+a_{n_0+1}+\ldots+a_N$ (analogo a integrale improprio)

Abbiamo 3 possibilità:
- il limite esiste finito
In tal caso tale limite è detto il "valore della serie" e diciamo che la serie è convergente
- il limite è $+\infty$ o $-\infty$
In tal caso che la serie è divergente a $+\infty$ o $-\infty$ e scriviamo $\sum_{n\ge n_0}a_n=\pm\infty$
- il limite non esiste
In tal caso diciamo che la sere è indeterminata

## Esempi
1) $a_n=1\ \ \forall\ n\ge 1\Rightarrow S_N=\sum\limits_{n=1}^N1=\overbrace{1+\dots+1}^{N\text{ volte}}=N\Rightarrow\sum\limits_{n=1}^\infty 1=\lim\limits_{N\to\infty} S_N=\lim\limits_{N\to\infty}N=+\infty$
Quindi la serie diverge a $+\infty$

2) $a_n=(-1)^n,\ \ n\ge0\Rightarrow S_N=\sum\limits_{n=0}^n(-1)^n=\overbrace{1-1+1-1+\dots\pm1}^{N+1\text{ addendi}}=\cases{1\text{ se }N\text{ pari}\\0\text{ se }N\text{ dispari}}$
Quindi $\lim_{N\to\infty}S_N$ non esiste e quindi $\sum\limits_{n=0}^\infty(-1)^n$ è indeterminata

3) $1+\frac12+\frac14+\frac18+\dots$
Aggiungendo tutte le potenze di $\le0$ di $2$, andiamo a riempire l'intervallo $[0,2]$ e quindi $\sum\limits_{n=0}^\infty\frac1{2^n}=1+\frac12+\frac14+\frac18+\dots=2$
In generale possiamo considerare $\sum\limits_{n=0}^\infty q^n$ per $q\in\mathbb R$, detta **seria geometrica**

$S_N=\sum\limits_{n=0}^N q^n=1+q+q^2+\dots+q^N=(1+q+q^2+\dots+q^N)\frac{(1-q)}{(1-q)}=\frac{(1+\cancel q+\cancel{q^2}+\dots+\cancel{q^N})-(\cancel q+\cancel{q^2}+\dots+\cancel{q^n})}{1-q}=\frac{1-q^{N+1}}{1+q}$
Quindi $\sum\limits_{n=0}^\infty q^N=\lim\limits_{N\to\infty}S_N=\lim\limits_{N\to\infty}\frac{1-q^{N+1}}{1-q}=\begin{cases}\frac1{1-q}&\text{se }|q|<1\\+\infty&\text{se }q\ge1\\\text{non esiste}&\text{se }q\le-1\end{cases}$
Quindi, riassumendo, $\sum_{n=0}^\infty q^n$ converge se e solo se $|q|<1$ e in tal caso $\sum\limits_{n=0}^\infty q^n=\frac1{1-q}$

4) $\sum\limits_{n=1}^\infty\frac1{n(n+1)},\ \ \frac1{n(n+1)}$
È una serie del tipo telescopico ossia con $a_n$ che si può scrivere come $a_n=b_n-b_{n-1}$ per qualche $b_n$
$\frac1{n(n+1)}=\overbrace{\frac1n}^{b_n}-\overbrace{\frac1{n+1}}^{b_{n+1}}$
$S_N=\sum\limits_{n=1}^Na_n=a_1+\dots+a_N=\underbrace{(b_1-\cancel{b_2})}_{=a_1}+\underbrace{(\cancel{b_2}-\cancel{b_3})}_{=a_2}+\underbrace{(\cancel{b_3}-\cancel{b_4})}_{=a_3}+\dots+\underbrace{(\cancel{b_N}-b_{N+1})}_{=a_N}$
Quindi se $b\to0$ per $n\to\infty$, allora $\sum\limits_{n=1}^\infty a_n$ converge e vale $\sum\limits_{n=1}^\infty a_n=\lim\limits_{n\to\infty}S_N=\lim\limits_{n\to\infty}(b_1-b_ {N+1})=b_1$
Nel caso $a_n=\frac1{n(n+1)}$ in cui abbiamo $b_n=\frac1n$, si ha $\sum\limits_{n=1}^\infty\frac1{n(n+1)}=b_1=1$
$\left[(1-\cancel{\frac12})+(\cancel{\frac12}-\cancel{\frac13})+(\cancel{\frac13}-\cancel{\frac14})+\dots=1\right]$

5) $a_n=\ln(1+\frac1n)\ \ n\ge1$
$\ln(1+\frac1n)=\ln(\frac{n+1}n)=\ln(n+1)-\ln(n)=b_n-b_{n+1}$ con $b_n=-\ln(n)$
Quindi $S_N=b_1-b_{N+1}=\cancel{-ln1}+\ln(N+1)$
Quindi $S_N\to\infty$ per $N\to\infty\Rightarrow\sum\limits_{n=1}^\infty\ln(1+\frac1n)=\infty$

# Proprietà
1) Il comportamento (ossia la convergenza/divergenza/indeterminatezza) di una serie non cambia se aggiungiamo o rimuoviamo un numero finito di termini (non cambia il valore della serie, se convergente)
2) Se $\sum\limits_{n=n_0}^\infty a_n$ è convergente, allora $\lim\limits_{n\to\infty}a_n=0$  \[è una condizione necessaria ma non sufficiente per la convergenza di $\sum_{n=n_0}a_n$\]
Infatti $\lim\limits_{n\to\infty}a_n=\lim\limits_{N\to\infty}(S_N-S_{N-1})$
La serie è convergente per ipotesi $=\sum\limits_{n=n_0}^\infty a_n-\sum_{n=n_0}^\infty a_n=0$
3) Se $\sum\limits_{n=n_0}^\infty a_n$ è convergente, allora $R_N=\sum\limits_{n\ge N+1}a_n\to0$ per $N\to\infty$
Infatti $R_N=\sum\limits_{n=n_0}^\infty a_n-S_N\to\sum\limits_{n=n_0}^\infty a_n-\sum\limits_{n=n_0}^\infty a_n=0$
4) Se $a_n\ge 0$ per $n\ge\overline n$ per un qualche $\overline n$, allora $\sum\limits_{n=n_0}^\infty a_n$ o converge o diverge a $+\infty$
Infatti $S_N$ è crescente per $N\ge \overline n$ e quindi $S_N$ ha limite finito o $+\infty$

# Criteri di convergenza per serie a termini positivi
## Criterio del confronto
Si supponga che $\exists\ \overline n$ tale che $0\le a_n\le b_n$ per $n\ge\overline n$
Allora
- $\sum\limits_{n=n_0}^\infty a_n=\underset{\small\text{diverge}}\infty\Rightarrow\sum\limits_{n=n_0}^\infty b_n$
- $\sum\limits_{n=n_0}^\infty b_n$ converge $\Rightarrow\sum\limits_{n=n_0}^\infty a_n$ converge \[Segue dai teoremi di confronto dei limiti applicati a $S_N$\]

### Esempi
1) $\frac1n\le\ln(1+\frac1n)\ \ \forall\ n\ge1$ e abbiamo visto $\sum\limits_{n=1}^\infty\ln(1+\frac1n)=\infty\Rightarrow\sum\limits_{n=1}^\infty\frac1n=\infty\ \  [\leftarrow\text{serie armonica}]$
2) $\frac1{n^2}\le\frac2{n(n+1)}\ \ \forall\ n\ge1$ e $\sum\limits_{n=1}^\infty\frac2{n(n+1)}=2\sum\limits_{n=1}^\infty\frac1{n(n+1)}=2\cdot 2=4$ converge, quindi anche $\sum\limits_{n=1}^\infty\frac1{n^2}$ converge

## Criterio del confronto asintotico
Si supponga che esista $\overline n$ tale che $a_n,b_n\ge0$ per $n\ge\overline n$ e che $\lim\limits_{n\to\infty}\frac{a_n}{b_n}$ esiste finito e sia $\ne0$
Allora $\sum\limits_{n=n_0}^\infty a_n$ $\array{\text{converge}\\\text{diverge}}$ $\iff\sum\limits_{n=n_0}^\infty b_n$ $\array{\text{converge}\\\text{diverge}}$

### Esempi
1) $a_n=\frac{n+3}{2n^2+5}\ge0\quad\forall\ n\ge0$
Confrontiamo con $b_n=\frac1n(\ge0\quad n\ge1)$
$\lim\limits_{n\to\infty}\frac{a_n}{b_n}=\lim\limits_{n\to\infty}n\cdot\frac{n+3}{2n^2+5}=\frac12\in\mathbb R_{\ne0}$
Dato che $\sum\limits_{n\ge1}\frac1n$ diverge, allora per confronto asintotico anche $\sum\limits_{n\ge0}\frac{n+3}{2n^2+5}$ diverge (potrebbe essere sbagliata)

2) $\sum\limits_{n=1}^\infty \sin(\frac1{n^2})$
$a_n=\sin(\overset{\small \in[0,1]}{\frac1{n^2}})\ge0\quad\forall\ n\ge1$
Dato che $\sin x\sim x$ per $x\sim 0$ confrontiamo con $\frac1{n^2}=b_n\ge0\quad\forall\ n\ge1$
$\lim\limits_{n\to\infty}\frac{\sin(\frac1{n^2})}{\frac1{n^2}}=1\in\mathbb R_{\ne0}$
Quindi, dato che $\sum\limits_{n=1}^\infty\frac1{n^2}$ converge, allora anche $\sum\limits_{n=1}^\infty\sin(\frac1{n^2})$ converge

## Criterio integrale
Sia $f:[n_0,\infty)\to\mathbb R$ che sia $\ge0$ e decrescente per $x\ge n_0$
Allora $\sum\limits_{n=n_0}^\infty f(n)$ converge se e solo se $\int_{n_0}^\infty f(x)dx$ converge
In tal caso si ha $\int_{n_0}^\infty f(x)dx\le\sum\limits_{n=n_0}^\infty f(n)\le f(n_0)+\int_{n_0}^\infty f(x)dx$
L'area totale dei rettangoli è $\sum\limits_{n=n_0}^\infty f(n_0)$ e per costruzione è $\ge$ area sottesa del grafico di $f$, ossia $\int_{n_0}^\infty f(x)dx$

## Altri criteri
### Criterio di convergenza assoluta
Se $\sum\limits_{n=n_0}^\infty|a_n|$ converge, allora converge anche $\sum\limits_{n=n_0}^\infty a_n$
In tal caso diciamo che $\sum\limits_{n=n_0}^\infty a_n$ converge assolutamente

#### Nota
Per distinguere dalla convergenza assoluta, qualche volta diremo che una serie converge semplicemente se converge

#### Esempio
$\sum\limits_{n=1}^\infty\frac{\cos(n)}{n^2}$

Vediamo se $\sum\limits_{n=1}^\infty|\frac{\cos(n)}{n^2}|$ converge
$|\frac{\cos n}{n^2}|\le\frac1{n^2}$ e $\sum\limits_{n=1}^\infty\frac1{n^2}$ converge
Quindi per confronto anche $\sum\limits_{n=1}^\infty|\frac{\cos(n)}{n^2}|$ converge
Quindi $\sum\limits_{n=1}^\infty\frac{\cos(n)}{n^2}$ converge

### Criterio del **rapporto** e della **radice**
Se esiste $\displaystyle\lim\limits_{n\to\infty}|\frac{a_{n+1}}{\underbrace{a_n}_{(a_n\ne 0\quad\forall\ n\ge\overline n)}}|=L\quad\small\in\mathbb R\cup\{\infty\}$ o se esiste $\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L\quad\small\in\mathbb R\cup\{\infty\}$

Allora:
- Se $L>1,\ \sum\limits_{n=n_0}^\infty a_n$ non converge
- Se $L<1,\ \sum\limits_{n=n_0}^\infty a_n$ converge
- Se $L=1,$ il criterio non conclude

#### Nota
Se $L=1,$ allora può essere utile usare la formula di Stirling $n!\sim\sqrt{2\pi n}\cdot n^n\cdot e^{-n}$ con in criterio del confronto asintotico

### Criterio di **Leibniz** per serie a segno alterno
$\sum\limits_{n=n_0}^\infty\underbrace{(-1)^n b_n}_{a_n}$ 
Allora, se
- $b_n\ge 0\quad\forall n\ge \overline n$
- $b_n$ decrescente $\forall n\ge \overline n$
- $\lim\limits_{n\to\infty}b_n=0$
Allora la serie $\sum\limits_{n=n_0}^\infty(-1)^n$ converge
#### Esempio
1) $\sum\limits_{n=1}^\infty\frac{(-1)^n}n$ converge
Infatti $b=\frac1n$ soddisfa le condizioni di Leibniz

2) $\sum\limits_{n=0}^\infty\frac n{3^n}\quad a_n=\frac n{3^n}$
$\lim\limits_{n\to\infty}\frac{a_{n+1}}a=\frac{n+1}{3^{n+1}}\frac{3^n}n=\frac 13<1$
Quindi la serie converge per il criterio del rapporto

3) $\sum\limits_{n=1}^\infty\frac{n^n}{10^n}\quad a_n=\frac{n^n}{10^n}$
$\lim\limits_{x\to\infty}\sqrt[n]{|a_n|}=\lim\limits_{n\to\infty}\left(\frac{n^n}{10^n}\right)^\frac1n=\lim\limits_{n\to\infty}\frac{10}=\infty$
Quindi per il criterio della radice la serie diverge