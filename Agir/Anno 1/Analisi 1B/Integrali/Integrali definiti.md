zSia $f:[a,b]\rightarrow\mathbb R\text{ limitata } (\text{ossia }\exists\ \text{ tale che }|f(x)\le c\ \ \forall\ x\in[a,b]|)$

Una partizione $\mathcal P$ di $[a,b]$ è un insieme finito $x_0,\ldots,x_k\in[a,b]$ tale che $a=x_0\le x_1\le\ldots\le x_k=b$


$I_i=[x_{i-1},x_i],\ l_i=x_i-x_{i-1}=\overset\ell{\text{lung}}([x_{i-1},x_i])$

Definiamo le somme inferiori $S^-$ e superiori $S^+$ di $f$ relativi a $\mathcal P$ come
$S^-(f,\mathcal P):=\sum\limits_{i=1}^k\left(\underset{x\in I_i}{\inf}(f(x)\right)l_i$
$S^-(f,\mathcal P):=\sum\limits_{i=1}^k\left(\underset{x\in I_i}{\sup}(f(x)\right)l_i$

Chiaramente $S^-(f,\mathcal P)\le S^+(f,\mathcal P)$

($S^-$ prende il valore minimo in $[x_{i-1},x_i]$, mentre $S^+$ il massimo)

Raffinando una partizione (ossia aggiungere punti) si ha che $S^-$ cresce e $S^+$ decresce
Se $\mathcal P^*$ si ottiene aggiungendo punti a $\mathcal P$ si ha $S^-(\mathcal P)\le S^-(P^*), S^+(\mathcal P)\ge S^+(P^*)$

Date due qualunque partizioni $\mathcal P_1$ e $\mathcal P_2$, $S^-(f,\mathcal P_1)\overset\star\le S^+(f,\mathcal P_2)$

$\mathcal P_1 \cup \mathcal P_2$ è raffinamento sia di $\mathcal P_1$ che di $\mathcal P_2\Rightarrow S^-(f,\mathcal P_1)\le S^-(f,\mathcal P_1\cup \mathcal P_2)\le S^+(f, \mathcal P_1\cup\mathcal P_2)\le S^+(f, \mathcal P_2)$

$\star\text{ implica che }\overbrace{\underset{\mathcal P}\sup(S^-(f,\mathcal P))}^{S^-(f)}\le\overbrace{\underset{\mathcal P}\inf(S^+(f,\mathcal P))}^{S^+(f)}$ dove $\underset{\mathcal P}\sup\text{ e }\underset{\mathcal P}\inf$ sono calcolati al variare di tutte le partizioni $\mathcal P$ di $[a,b]$

# Definizione
Sia $F:[a,b]\rightarrow \mathbb R$ limitata
Diciamo che $f$ è integrabile $(\text{secondo Riemann})$ se $S^-(f)=S^+(f)$
In tal caso questo valore $S^+(f)=S^-(f)$ è indicato con $\int_a^bf(x)dx$ o $\int_a^bf$

## Esempi
1) $f(x)=K\text{ costante }\ \ (K\in\mathbb R)$
$\forall\ \mathcal P=\{x_0,\ldots,x_m\}\ \ S^-(f,\mathcal P)=\sum\limits_{i=1}^m\left(\underset{x\in I_i}\inf f(x)\right)l_i=\sum\limits_{i=1}^m K\cdot l_i=K\sum\limits_{i=1}^ml_i=K(l_1+\ldots+l_m=K\left((x_1-x_0)+(x_2-x_1)+\ldots+(x_m-x_{m-1})\right))=K(x_m-x_0)=K(b-a)$
Allo stesso modo $S^+(f,\mathcal P)=K(b-a)\Rightarrow S^-(f)=S_+(f)=K(b-a)\Rightarrow\int_a^bKdx=K(b-a)$

2) $f(x)=\begin{cases}0&\text{se }x\in \mathbb Q\\1&\text{se }x\notin \mathbb Q\end{cases}$
$\forall\ I_i$, abbiamo $\underset{x\in I_i}\sup\left(f(x)\right)=1\text{ e }\underset{x\in I_i}\inf\left(f(x)\right)=0$
Quindi lo stesso calcolo di 1), da $S^+(f)=1\cdot(b-a)\text{ e }S^-(f)=0$
Quindi $(\text{per }a\ne b)$ abbiamo $S^-(f)\ne S^+(f)$ quindi $f$ non è integrabile $(\text{secondo Riemann})$

# Proprietà
Sia $f:[a,b]\to\mathbb R$ integrabile su $[a,b]$
1) $\forall\text{ intervallo} [c,d]\subseteq[a,b]$, allora $f$ è integrabile su $[c,d]$
2) Poniamo $\int_b^af=-\int_a^bf\text{ e }\int_a^a=0$
	Abbiamo poi $\forall\ c\in[a,b]\ \ \int_a^bf=\int_a^cf+\int_c^bf$
3) Se anche $g$ è integrabile su $[a,b]$ e $\alpha, \beta\in\mathbb R$, allora $\alpha f+\beta g$ è integrabile su $[a,b]$ e vale $\int_a^b(\alpha f+\beta g)=\alpha\int_a^bf+\beta\int_a^bg$
4) Anche $|f|$ è integrabile su $[a,b]$ e vale $|f|\le\int_a^b|f|$
	Più precisamente, se $A^+$ è l'area tra l'asse delle $x$ e il grafico di $f$ dove $f\ge0$ (per $x\in[a,b]$) e $A^-$ è l'area tra il grafico di $f$ dove $f<0$ e l'asse delle $x$ (con $x\in[a,b]$) allora $\int_a^bf=A^+-A^-,\ \int_a^b|f|=A^++A^-$
5) Se $g$ è integrabile su $[a,b]$ e $f(x)\le g(x)\ \ \forall\ x\in[a,b]\ \ \ \ \int_a^bf\le\int_a^bg$

# Teorema
Sono integrabili su $[a,b]$
1) Le funzioni continue su $[a,b]$ (anche a tratti)
2) Le funzioni continue su $(a,b)$ e limitate su $[a,b]$
3) Le funzioni monotone su $[a,b]$ e limitate su $[a,b]$

# Definizione
Sia $f$ integrabile su $[a,b]$
La media integrale di $f$ su $[a,b]$ è $\frac1{b-a}\int_a^bf$

## Teorema della media integrale
Sia $f:[a,b]\to\mathbb R$ continua
Allora $\exists\  c\in[a,b]\text{ tale che }\frac1{b-a}\int_a^bf=f(c)$

### Dimostrazione
$\underset{x\in[a,b}\min\left(f(x)\right)\le f(x)\underset{x\in[a,b}\max f(x)\Rightarrow\text{ Per Proprietà 5}\ \ \ \ \underbrace{\int_a^b\min f}_{(\min f)(b-a)}\le\int_a^b f\le\underbrace{\int_a^b\max f}_{(\max f)(b-a)}\Rightarrow\frac1{b-a}\int_a^b f\in[\min(f),\max(f)]$

Per il teorema del valore intermedio $\exists\ c\in[a,b]\text{ tale che }f(c)=\frac1{b-a}\int_a^bf$

# Definizione
Sia $I$ intervallo $I$ (anche infinito) e sia $f$ integrabile su ogni $[a.b]\subseteq I$
Dato $x_0\in I$ definiamo la funzione integrale come $F_{x_0}(x):=\int_{x_0}^xf(z)dz$

# Teorema fondamentale del calcolo integrale
Sia $f$ continua su un intervallo $I$
Sia $x_0\in I$
Allora $F_{x_0}(x)$ è una primitiva di $f$ su $I$, ossia ${F_{x_0}}'(x)=f(x)\ \ \ \ \forall\ x\in I$

## Dimostrazione
Sia $h>0$
Si ha $\frac{F_{x_0}(x+h)-F_{x_0}(x)}h=\frac1h\left(\int_{x_0}^{x+h}f-\int_{x_0}^xf\right)=\frac1h\left(\cancel{\int_{x_0}^{x}f}+\int_{x}^{x+h}-\cancel{\int_{x_0}^xf}\right)$ ossia la media integrale di $f$ su $[x, x+h]$

$\exists\ c\in[x,x+h]\text{ tale che }\frac1h\int_x^{x+h}f=f(c)$
Se $h\to0^+$, allora $c\to x$ e quindi, dato che $f$ è continua, $\lim\limits_{h\to0^+}f(c)=f(x)$

Riassumendo $\lim\limits_{h\to0^+}\frac{F_{x_0}(x+h)-F_{x_0}(x)}g=\lim\limits_{h\to0^+}\frac1h\int_x^{x+h}f=\lim\limits_{x\to0^+}f(c)=f(x)$
Analogamente si calcola il limite per $h\to 0\Rightarrow\lim\limits_{h\to0}\frac{F_{x_0}(x+h)-F_{x_0}(x)}g=f(x)$ ossia, per definizione di derivata ${F_{x_0}}'(x)=f(x)$

# Corollario
Sia $f$ come sopra e sia $F$ una qualunque primitiva di $f$
Allora $\int_a^bf=F(b)-F(a)=\left[F(x)\right]_{x=a}^{x=b}$

## Dimostrazione
$F_x(x)$ è un'altra primitiva $\left(x_0\in[a,b]\right)\Rightarrow F_{x_0}(x)=F(x)+c \text{ per un qualche }c\Rightarrow F(b)-F(a)=F_{x_0}(b)-F_{x_0}(a)=\int_{x_0}^bf-\int_{x_0}âf\underset{\text{prop 2}}=\int_a^b{f}$

# Teorema (integrazione (definita) per parti)
Siano $f,g$ derivabili su $[a,b]$ con derivata continua.
Allora $\int_a^bfg'=fg-\int_a^bf'g=\left[fg\right]_a^b-\int_a^bf'g$

# Teorema (integrazione (definita) per sostituzione)
Sia $f$ continua su $[a,b],\ \varphi:[\alpha,\beta]\to[a,b]$ derivabile con derivata continua e invertibile.
Allora $\displaystyle\int_a^bf(x)dx=\int_{\underbrace{phi^{-1}(a)}_\alpha}^{\overbrace{phi^{-1}(b)}^\beta}f\left(\varphi\left(y\right)\right)\varphi'\left(y\right)dy$

## Dimostrazione
Segue dal TFCI + analoghi teoremi per integrali indefiniti