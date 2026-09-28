-- $\mathbb{N}_0=\{0,1,2,3,...\}$
$\mathbb{N}=\{1,2,3,...\}$
$\mathbb{N}_p/2\mathbb{N}_0=\{2,4,6,...\}$
$\mathbb{N}_d=\{1,3,5,...\}$
$\mathbb{Z}=\{0,1,-1,2,-2,...\}$
$\mathbb{Q}$: razionali
$\mathbb{R}$: reali
$\mathbb{C}$: complessi

Ordine/Cardinalità di un insieme: numero di elementi dell'insieme

Sottoinsieme: ogni elemento dell'insieme A è elemento di B
$A\subseteq{B}$ / $B\supseteq{A}$
$A\subseteq{B}:= \forall\ x \in A, x \in B$

Qualunque sia l'insieme A:
$\varnothing\subseteq{A}$
$A\subseteq{A}$
$\{x\}\subseteq{A}$

Se $A\subseteq{B}$ e $B\subseteq{C}$, allora $A\subseteq{C}$
	Proprietà transitiva dell'inclusione

Insieme A contenuto strettamente se contenuto in B ma distinto (B contiene tutti gli elementi di A + un elemento non contenuto in A)
$H\subset K$

Insieme delle parti / Insieme potenza
Insieme di tutti i sottoinsiemi di A
$\mathcal{P}(A):=\{X:X\subseteq{A})$
$H=\{3,5,8\}$
$\mathcal{P}(H)=\{\varnothing,\{3\},\{5\},\{8\},\{3,5\},\{3,8\},\{5,8\},\{3,5,8\}\}$
$|\mathcal{P}(A)|=2^{|A|}$

Uguaglianza tra insiemi
	$A=B x\in{A} \iff x\in{B}$

Unione
$A\cup{B}$

Intersezione
$A\cap{B}$

Dati A,B,C,D:
$A\subseteq{A} \cup B$ e $B\subseteq{A}\cup B$
$A\cup{B} = B\cup{A}$ / $A\cap{B}=B\cap{A}$
	Proprietà commutativa
$(A\cup{B})\cup{C} = A\cup{(B\cup{C})}$
	Proprietà associativa
$A\cup{\varnothing}=\varnothing\cup{A}$
	Elemento neutro per l'unione
$A\cup{A}=A$
	Proprietà iterativa
$A\cap{B}\subseteq{A}$ e $A\cap{B}\subseteq{B}$

$A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ / $(A\cap B)\cup C=(A\cup C)\cap(B\cup C)$
	Proprietà distributiva dell'unione rispetto all'intersezione
$A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$

Partizione di un insieme
$F\subseteq\mathcal{P}(A)$
F partizione di A $:=${
$X\neq\varnothing, \forall X\in F$
$X,Y\in F, X\neq Y \rightarrow X\cup Y = \varnothing$
Altro
}

Copmlemento di insiemi
A e B insiemi
Complemento di B rispetto ad A (o differenza tra A e B) insieme costituito da tutti e soli gli elementi di A che non appartengono a B
$A \setminus B$
$S=\{g, 1, +\},\ W=\{+, 5, m, 1, k\}$
$S\setminus W={G},\ W\setminus S={5,m,k}$
Dati gli insiemi A e B
**Non** vale la proprietà commutativa
**Non** vale la proprietà associativa
$A\setminus B \subseteq A$
$A \setminus \varnothing = A$
$\varnothing \setminus A=\varnothing$
$A \setminus A = \varnothing$
$A\cap(B\setminus A)=\varnothing$

Dati gli insiemi A, B e C:
$(A\cup B)\setminus C = (A\setminus C)\cup(B\setminus C)$
	Proprietà distributiva a destra del complemento rispetto all'unione
$A\setminus(B\cup C) = (A\setminus B)\cap(A\setminus C) / A\setminus(B\cap C) = (A\setminus B)\cup(A\setminus C)$
	De Morgan

Unione disgiunta (xor)
A e B insiemi
$S=\{g,1,+\}, W=\{+,5,m,1,k\}$
$S\Delta W= {g,5,m,k}$
$A\Delta B := (A\cup B)\setminus(A\cap B)$

Dati gli insiemi A, B e C:
$A\Delta B = B\Delta A$
	Proprietà commutativa

Prodotto cartesiano di insiemi
$A\times B:={(x,y):x\in A, y\in B}$
$S=\{g,1\}, W=\{5,m,1\}$
$S\times W=\{(g,5),(g,m),(g,1),(1,5),(1,m),(1,1)\}$

Dati gli insiemi A, B e C:
$(A\cup B)\times C = (A\times C)\cup(B\times C)$
	Proprietà distributiva a destra
$A\times(B\cup C)=(A\times B)\cup(A\times C)$
	Proprietà distributiva a sinistra
$\varnothing\times A=A\times\varnothing=\varnothing$
$|A\times B|=|A|\cdot|B|=|B\times A|$

$A_1,A_2,...,A_n (n\ge2)$ allora $(x_1,x_2,...,n_x)$ con $n_1\in A_1, x_2\in A_1,...,x_n\in A_n$ si dice n-upla
Prodotto cartesiano di $A_1\times A_2\times...\times A_n$ si definisce come l'insieme di tutte e sole le n-uple $(x_1,x_2,...,x_n)$ con $n_1\in A_1, x_2\in A_1,...,x_n\in A_n$
Se $A_1=A_2=...=A_n=A$ il prodotto cartesiano di $A_1=A_2=...=A_n=A\times...\times A$ ($n$ volte) viene detto prodotto cartesiano di $n$ coppie di $A$ e denotato con $A^n$

Siano A e B insiemi
Un sottoinsieme $\mathcal{R}$ di $A\times B$ è detto relazione o corrispondenza tra A e B
Se $x\in A$ e $y\in B$ sono tali che $(x,y)\in\mathcal{R}$ si scrive $x\mathcal{R}y$ e si dice che $x$ è nella relazione di $\mathcal{R}$ con $y$ o che $y$ è corrispondente in $\mathcal{R}$ di $x$.
$S=\{g,1,+\}, W=\{+,5,m,1,k\}$
Esempi di relazione
$\mathcal{R}_1=\{(g,5),(g,1)\}$

Spesso per assegnare una relazione si precisa una proprietà che individua un sottoinsieme di $A\times B$
Sono relazioni in $N_0\times Z$:
$x\mathcal{R}_4 y\iff x=y$
$x\mathcal{R}_5 y\iff x=y^2$
$x\mathcal{R}_6 y\iff y^3=x$

Se A e B sono insiemi finiti non vuoti, esiste un numero finito di relazioni tra A e B e tale numero è $|\mathcal{P}(A\times B)|=2^{|A\times B|}=2^{|A|\cdot|B|}$
Esempio: Il numero di relazioni in $S\times W$ è $2^{3\cdot 5}=2^{15}=32768$

$\mathcal{R}^{op}={(y,x):x,y}\in\mathbb{R}$
$S=\{g,1,+\}, W=\{+,5,m,1,k\}$
Esempi di relazione
$\mathcal{R}_1=\{(g,+),(g,5),(g,m)\}$
$\mathcal{R}_2=\{(+,g),(5,g),(m,g)\}$

Relazione binaria
$x(id_A)y\iff x=y$
$S=\{g,1,+\}$
$\Delta_S={(g,g),(1,1),(+,+)}$

Riflessiva
	Tutte le coppie ${(g,g),(1,1),(+,+)}$
Simmetrica
	${(g,1),(+,+),(g,+),(1,g),(+,g)}$
Assimmetrica
	Non simmetrica
Transitiva
	${(g,1),(1,1),(g,g)}$

Relazione di equivalenza: riflessiva, simmetrica, transitiva

Insieme quoziente
$A\setminus\mathcal{R}:=\{[X]_\mathcal{R}:x\in A\}$
Sia A un insieme non vuoto. Allora:
	Se $\mathcal{R}$ è una relazione di equivalenza in A, l'insieme quoziente $A / \mathcal{R}$ è una partizione di A
	Se F è una partizione di A, esiste una 

Relazione d'ordine
	Una relazione binaria $\mathcal{R}$ in un insieme A è detta relazione d'ordine se è
		- Riflessiva
		- Asimmetrica
		- Transitiva
	Spesso si denota una r d'ordine con $\le$ ($x\le Y:= x\ \mathcal{R}\ y$), si dice x minore o uguale di y
	$y\ge x$ si dice y maggiore o uguale di x

$S=\{g,1,+\}, \mathcal{R}=\{(g,g),(1,1),(+,+),(g,1)\}$ è una relazione d'ordine
Ordini usuali in $\mathbb{N}_0$ e $\mathbb{Z}$ sono relazioni d'ordine

Insiemi ordinati
	La coppia ($A, \le$) con A insieme e $\le$ relazione d'ordine in A è detta insieme ordinato o parzialmente ordinato
	Esempi: ($\mathbb{N}_0,$ usuale), ($\mathbb{Z}$, usuale), ($\mathcal{P}(T), \subseteq$) con T insieme arbitrario

Minimo
	Sia ($A, \le$) un insieme ordinato
	Un elemento $a \in A$ è detto minimo di A e si denota con min a, se è confrontabile con ogni elemento di A e risulta $a \le x \text{ per ogni } x \in A$
		$a = \text{min}\ A:=a\le x\ \forall\  x\in A$
		
Massimo
	Sia ($A, \le$) un insieme ordinato
	Un elemento $a \in A$ è detto massimo di A e si denota con max a, se è confrontabile con ogni elemento di A e risulta $a \ge x \text{ per ogni } x \in A$
		$a = \text{max}\ A:=a\ge x\ \forall\  x\in A$
		
$S=\{g,1,+\}, \mathcal{R}_1=\{(g,g),(1,1),(+,+),(g,1)\}$
Non esiste né massimo né minimo in ($S, \mathcal{R}_2$)

$S=\{g,1,+\}, \mathcal{R}_2=\{(g,g),(1,1),(+,+),(g,1), (1,+), (g,+)\}$
In ($S, \mathcal{R}_2$) g è minimo e + è massimo

Minimali/massimali
		Non esistono elementi strettamente minori/maggiori di c
		$A \text{ ben ordinato }:=\ \forall\ X\subseteq A, X\neq\varnothing, \exists \text{ min } X$
Insieme $C={2,3,4,5,6}$ e la relazione d'ordine $x\ \mathcal{R}_d\ y \iff x$ divide $y$
Applicando $\mathcal{R}_d$ si ha che $2\le4, 2\le6, 3\le6$
Dunque:
	- 2, 3, 5 sono minimali in ($C, \mathcal{R}_d$)
	- 4, 5, 6 sono massimali in ($C, \mathcal{R}_d$)
	- In ($C, \mathcal{R}_d$) non esiste minimo
	- In ($C, \mathcal{R}_d$) non esiste massimo

Minoranti e maggioranti
Tutti gli elementi di A minori/maggiori di X
Confronto con TUTTI gli elementi di X

Estremo inferiore di X
	Elemento che delimita il confine tra X e A (elemento più grande dei minoranti)

Estremo superiore di X
	Elemento che delimita il confine tra X e A (elemento più piccolo dei maggioranti)

Un sottoinsieme non vuoto di un insieme ordinato può non avere minoranti (maggioranti), averne uno solo, averne un numero finito o un nnumero infinito
Se il xottoinsieme $X\subseteq A$ ha minoranti, è non vuoto l'insieme $M

$T={a,b,c}$
$\mathcal{P}(C)=\{\varnothing,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\}\}$
$X=\{\{a\},\{b\}\}$
$\varnothing\subseteq\{a\}\ \checkmark$
$\varnothing\subseteq\{b\}\ \checkmark$
$\{c\}\subseteq\{a\}\ \times$
$\{c\}\subseteq\{b\}\ \times$

$\{a\}\subseteq\{a,b\}$
$\{b\}\subseteq\{a,b\}$

$\{a\}\subseteq\{a,b\}$
$\{b\}\subseteq\{a,b,c\}$
$\{a,b\}\subseteq\{a,b,c\}$

$\varnothing$ minorante
$\{a,b\}$ maggiorante

$K=\{3,6,12,18,36\}$
$x\ \mathcal{R}_d\ y \iff x \text{ divide } y$
$\mathcal{R}_d=\{(3,3),(6,6),(12,12),(18,18),(36,36),(3,6),(3,12),(3,18),(3,18),(6,12),(6,18),(6,36),(12,36),(18,36)\}$
$X=\{12,18\}
Minoranti di $X=\{3,6\}$
Maggioranti di $X=\{36\}$
Inf X=? (si controllano i minoranti)
	$3\le6?\ \checkmark$
inf $X=3$
sup $X=36$
min X
	$12\le18?\ \times \text{ con }\mathcal{R}_d$
		perché $(12,18)\notin\mathcal{R}_d$

$\nexists$ min in X
$\nexists$ max in X