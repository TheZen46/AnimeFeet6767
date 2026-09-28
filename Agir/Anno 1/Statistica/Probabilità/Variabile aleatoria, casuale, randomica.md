Funzione

Lancio una moneta 3 volte
$\Omega={\text{digramma ad albero}}$
$\omega=TCT,\ CCT...$
$\omega=\text{risultato}\quad\in\Omega$
$x=\text{numero di teste}\quad\in\mathbb R$

$\begin{array}{l}TCT\quad x=2\\CCT\quad x=1\end{array}$

$\underset{\text{spazio campionario}}{\Omega}\ni\underset{\begin{gather}\text{possibile risultato}\\\text{esperimentato}\end{gather}}{\omega}\longrightarrow \underset{\text{risposta}}{x}\in\mathbb R$

$X:\omega\to\mathbb R$
$x=X(\omega)$

Dato uno spazio campionario $\Omega$ (esperimento aleatorio) una variabile aleatoria (casuale, randomica) è una funzione $X:\omega\to\mathbb R\quad x=X(\omega)$ che associa ad ogni possibile risultato $\omega\in\Omega$ dell'esperimento aleatorio la risposta $x=X(\omega)\in\mathbb R$
$X$ è una "domanda" sull'esperimento aleatorio

# Notazione
$X:\Omega\to\mathbb R$ variabile aleatoria
- $x\in\mathbb R\quad\text{definiamo gli eventi}\quad E\subseteq\Omega$
	$\{X=x\}=\{\omega\in\Omega|X(w)=x\}$
	$\{X>x\}=\{\omega\in\Omega|X(w)>x\}$
	$\{X<x\}=\{\omega\in\Omega|X(w)<x\}$
	$\{X\ge x\}=\{\omega\in\Omega|X(w)\ge x\}$
	$\{X\le x\}=\{\omega\in\Omega|X(w)\le x\}$

## Esempio
Lancio $3$ volte una moneta
$X=\text{numero di teste}$
$\{X=1\}=\{\text{è uscita }1\ T\text{ e }2\ C\}=\{TCC,\ CTC, CCT\}$
$\{X\le1\}=\{CCC,\ TCC,\ CTC, CCT\}$
$\{X>7\}=\varnothing$

$X:\omega\to\mathbb R\text{ variabile aleatoria}$
- Se $I\subseteq R$
	$\{X\in I\}=\{\omega\in\Omega|X(\omega)=x\in I\}=X^{-1}(I)$
- Scriviamo $X\in I\quad I\subseteq \mathbb R\text{ se }\{X\in I\}=\omega$

### Esempio
$X=\text{numero di teste in tre lanci}$
$X\in\{0,1,2,3\}$



- $X$ è retta variabile aleatoria **finita** se $X\in\{x_1,x_2,\ldots,x_n\}=I\quad \# I\text{ finita}$
- $X$ è retta variabile **discreta** se $X\in\{x_1,x_2,\ldots,x_n,\ldots\}=I\quad \# I\text{ numerabile}$

## Esempio
1) 
$X=\text{numero di teste in tre lanci}$
$X\in\{0,1,2,3\}\quad \#I=4\quad x\text{ variabile finita}$

2) Lancio una moneta finché non esce testa
$X=\text{numero di lanci}$
$X\in\{1,2,3,\ldots,n,\ldots\}=\mathbb N\setminus\{0\}\quad \#I=\quad x\text{ variabile discreta}$

3) 
$X=\text{tempo di attesa}\in[0,+\infty)\quad\array{X\text{ non è finita}\\X\text{ non è discreta}}$

4) 
Dato un evento $E$

$E=\text{"successo"}$
$\overline E=\text{"insuccesso"}$

$X(\omega)\in\begin{cases}1&\text{se }\omega\in E\\0&\text{se }\omega\in \overline E\end{cases}$
$X=\text{numero successi in una prova}\in\{0,1\}$

# La legge di una variabile aleatoria
$(\Omega, \mathbb P)\text{ spazio di probabilità}$

Evento $E\subseteq\Omega\qquad\mathbb P[E]=\text{probabilità che l'evento }E\text{ accada}$
$X:\omega\to\mathbb R\text{ variabile aleatoria}$
$x=X(\omega)\quad x=\text{risposta se il risultato è}\omega\in\Omega$

$\mathbb P[E]$
$\mu(I)=\mathbb P[X\in I]=\mathbb P[\{\omega\in\Omega|x(\omega)\subseteq I\}]$
Legge della variabile aleatoria: lunghezza dell'insieme $I$

Dato un insieme $I\subseteq \mathbb R$
La legge $\mu(I)$ è la probabilità che la variabile aleatoria $X$ ($=$ domanda sull'esperimento aleatorio) prenda valori (risposte) nell'insieme $I$ e valgono le seguenti proprietà:
- $\mu(\mathbb R)=1$
- $\mu(I\cup J)=\mu(I)+\mu(J)\text{ se }I\cap J=\varnothing$



# Esempio
Lancio una moneta truccata $\mathbb P[T]=\frac13$
$X=\text{numero di teste}$
$X\in\{0,1\}$
$\{X=1\}=\{T\}$
$\{X=0\}=\{C\}$

$\mu(I)=\begin{cases}0&\longrightarrow&0,1\notin I\\\frac23&\longrightarrow&0\in I&1\notin I\\\frac13&\longrightarrow&0\notin I&1\in I\\1&\longrightarrow&0,1\in I\end{cases}$

Per una variabile aleatoria finita
$X\in\{x_1,x_2,\ldots,x_n\}\quad x_i\ne x_j\ \ i-ne j$
La legge di $X$ è determinata da

| $x$      | $\mathbb P[X=x]$               |
| -------- | ------------------------------ |
| $x_1$    | $\mathbb P_1=\mathbb P[X=x_1]$ |
| $x_2$    | $\mathbb P_2=\mathbb P[X=x_2]$ |
| $\vdots$ |                                |
| $x_n$    | $\mathbb P_n=\mathbb P[X=x_n]$ |
$\mathbb P_1,\ldots,\mathbb P_n\in[0,1]$
$\mathbb P_1+\ldots+\mathbb P_n=1$

Stesse probabilità viste in statistica descrittiva per le tabelle a una via delle frequenze relative