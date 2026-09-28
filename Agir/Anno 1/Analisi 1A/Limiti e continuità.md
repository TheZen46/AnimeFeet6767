# Intorno
#### Definizione
$x_0,a,b,r$
- Intorno di $x_0$ di raggio $r$
	$I_r(x_0):=(x_0-r, x_0+r)=\{x\in\mathbb{R}:|x-x_0|<r\}$
- Intorno di $+\infty$ di estremo inferiore $a$
	$I_a(+\infty):=(a,+\infty)=\{x\in\mathbb{R}:x>a\}$
- Intorno di $-\infty$ di estremo superiore b
	$I_b(-\infty):=(-\infty,b)=\{x\in\mathbb{R}:x<b\}$

# Limiti di successioni
Una **successione** è una funzione definita in $\mathbb{N}$ a valori in $\mathbb{R}$
$a:\text{dom}(a)\subseteq\mathbb{N}\rightarrow\mathbb{R}$
$(a_n)_{n\ge n_0}\ \ \ \ n\mapsto a(n)=a_n$
$(\frac{1}{n})_{n\ge1}$ "converge" a 0
#### Definizione
Si dice che la successione $(a_n)$ **tende** (oppure **converge**) a $l\in\mathbb{R}, \lim_{n\to+\infty}a_n=l$, se, $\forall\varepsilon>0\exists n_\varepsilon\in\mathbb{N}:\forall n\ge n_\varepsilon \{|a_n-l|<\varepsilon\} \iff \{a_n\in I_\varepsilon(l)\}$

Inoltre si dice che $(a_n) **tende** (oppure **diverge**) a $+\infty$, $\lim_{n\rightarrow+\infty}a_n=+\infty$, se $\forall k>0\exists n_k\in\mathbb{N}:\forall n\ge n_k\ \ \{a_n>k\} \iff \{a_n\in I_k(+\infty)\}$
Analogamente, si dice che (a_n) **tende** (oppure **diverge**) a $-\infty, \lim_{n\rightarrow+\infty}a_n=-\infty$, se $\forall k>0\exists n_k\in\mathbb{N}:\forall n\ge n_k\ \ \ \ a_n<-k$, ovvero $a_n\in I_{-k}(-\infty)$

Le successioni che non sono convergenti o divergenti sono **indeterminate**

### Esempi
- $(\frac{1}{n})_{n\ge1}$ tende a 0
	Fisso $\varepsilon>0$ arbitrario
	Cerco $n_\varepsilon\in\mathbb{N}$ t.c. se $n\ge n_\varepsilon$ allora $|\frac{1}{n}-0|<\varepsilon \rightarrow \frac{1}{n}<\varepsilon \iff \frac{1}{\varepsilon}<n$
	Scelgo $n_\varepsilon\in\mathbb{N}$ t.c. $n_\varepsilon>\frac{1}{\varepsilon}$. Allora se $n\ge n_\varepsilon$ ne segue da $n\ge n_\varepsilon>\frac{1}{\varepsilon}$

- $(n^2)_{n\ge1}$ diverge a  $+\infty$
	Fisso $A>0$
	Cerco $n_A\in\mathbb{N}$ t.c. se $n\ge n_A$ allora $n^2>A$
	Scelgo $n_A\in\mathbb{N}$ t.c. $n_A>\sqrt{A}\ \ \ \ n\ge n_A>\sqrt{A}$

### Osservazione
Più avanti vedremo che, se esista, il limite è **unico**

### Definizione
La successione $(a_n)$ è detta:
- **monotona crescente** se $a_n\le a_{n+1}$
- **monotona decrescente** se $a_n\ge a_{n+1}$

### Teorema
Le successioni monotone convergono o divergono
Se $(a_n)$ è crescente allora
- **converge** se è limitato superiormente e $\lim_{n\rightarrow+\infty}a_n=\text{sup}\{a_n\}$
- **diverge** a $+\infty$ altrimenti

Se $(a_n)$ è decrescente allora
- **converge** se è limitato inferiormente e $\lim_{n\rightarrow+\infty}a_n=\text{inf}\{a_n\}$
- **diverge** a $-\infty$ altrimenti

### Esempi
- $(\frac{1}{n})$
- $(n^2)$
- $(\frac{n-1}{n})$
- $((1+\frac{1}{n})^n)_{n\ge1}$
	è crescente e limitato superiormente (da $\varepsilon$)
	Allora $((1+\frac{1}{n})^n)_{n\ge1}$ converge $\lim_{n\rightarrow+\infty}(1+\frac{1}{n})^n=\text{sup}(1+\frac{1}{n})^n=:l$    NUMERO DI NEPERO

### Dimostrazione
Suppongo $(a_n)$ crescente e limitato superiormente. Dimostro che $(a_n)$ converge al sup $\{a_n\}$
Limitato superiormente: $\exists M>0$ t.c. $\forall n\ \ \ \ a_n<M$ crescente: $a_n\le a_{n+1}$
Vogliamo verificare che, posto $l=\text{sup}\{a_n\}\in\mathbb{R},\ \forall \varepsilon>0\exists n_\varepsilon\in\mathbb{N}:\forall n\ge n_\varepsilon\ \ \ \ |a_n-l|<\varepsilon$
Fisso $\varepsilon>0$ e cerco $n_\varepsilon$    $|a_n-l|<\varepsilon\iff l-\varepsilon<a_n<l+\varepsilon$
Per definizione di estremo superiore:
	1) $a_n\le\text{sup}\{a_n\}=l<l+\varepsilon$
	2) Esiste sempre $n_\varepsilon$ t.c. $l-\varepsilon=\sup\{a_n\}-\varepsilon\le a_{n_\varepsilon}\le\text{sup}\{a_n\}=l$
Sia $n\ge n_\varepsilon$    $l-\varepsilon<a_{n_\varepsilon}\le a_n \le \text{sup}\{a_n\}=l<l+\varepsilon$

 # Limiti di funzioni di continuità
#### Definizione (limite di funzione all'infinito)
Sia $f:\text{dom}(f)\subseteq\mathbb{R}\rightarrow\mathbb{R}$
Una funzione definita in un intorno di $+\infty$
Diremo che, per x tendente a $+\infty$
$f$ **tende** a 
- limite finito $l\in\mathbb{R}; \lim_{x\rightarrow+\infty}f(x)=l$, se $\forall\varepsilon>0\ \ \exists\  B>0; \forall x\in\text{dom}(f)$ vale $x>B\Rightarrow|f(x)-l|<\varepsilon$
- $+\infty\ \ \lim_{x\rightarrow+\infty}f(x)=+\infty$, se $\forall\ M>0\ \ \exists\ B>0;\forall x\in\text{dom}(f), x>B\Rightarrow f(x)>M$

### Esempio
Verifico che $f(x)=\frac{x^2+3x+2}{3x^2+1}$ tende a $\frac{1}{3}$ per x tendente a $+\infty$

Fisso $\varepsilon>0$ e cerco $B>0$ t.c. $x>B\Rightarrow|f(x)-\frac{1}{3}|<\varepsilon$
$|f(x)-\frac{1}{3}| = |\frac{x^2+3x+2-x^2-\frac{1}{3}}{3x^2+1}|=|\frac{3x+\frac{5}{3}}{3x^2+1}|=\frac{|3x+\frac{5}{3}|}{3x^2+1}<\frac{|3x+\frac{5}{3}|}{3x^2}$ (supponendo $x>0$) $=\frac{3x+\frac{5}{3}}{3x^2+1}=\frac{1}{x}+\frac{5}{9x^2}$
Ora cerco $B>0$ in modo che se $x>B$, allora $\frac{1}{x}<]\frac{\varepsilon}{2}$ e $\frac{5}{9x^2}<\frac{\varepsilon}{2}$
$B\le\frac{2}{\varepsilon}, \sqrt\frac{10}{9\varepsilon}$
Ad esempio $B=\text{max}\{\frac{2}{\varepsilon},\sqrt\frac{10}{9\varepsilon} < \frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon$

### Definizione (limite di funzione al finito)
Sia$x_o\in\mathbb{R}$ e sia $f\ \ \text{dom}(f)\subseteq\mathbb{R}\rightarrow\mathbb{R}$ definita in un intorno di $x_0$, eventualmente $x_0$ escluso, si dice che, per x tendente a $x_0$, $f$ tende a
- **limite finito** $l\in\mathbb{R}$, $\lim_{x\rightarrow x_0}f(x)=l$, se $\forall\varepsilon>0\ \exists\delta>0:\forall x\in\text{dom}(f),\ 0<|x-x_0|<\delta\Rightarrow|f(x)-l|<\varepsilon$
- **$+\infty$**, $\lim_{x\rightarrow x_0}f(x)=+\infty$, se $\forall B>0\ \exists\delta>0:\forall x\in\text{dom}(f),\ 0<|x-x_0|<\delta\Rightarrow f(x)>B$
- **$-\infty$**, $\lim_{x\rightarrow x_0}f(x)=-\infty$, se $\forall B>0\ \exists\delta>0:\forall x\in\text{dom}(f),\ 0<|x-x_0|<\delta\Rightarrow f(x)<-B$

### Definizione (funzione continua)
Sia $f:\text{dom}(f)\subseteq\mathbb{R}\rightarrow\mathbb{R}$ una funzione e sia $x_0\in\text{dom}(d), si dice che $f$ è continua in $x_0$ se, $\forall\varepsilon>0\exists\delta>0:\forall x\in\text{dom}(f)$ vale $|x-x_0|<\delta\Rightarrow|f(x)-f(x_0)|<\varepsilon$
Sia $I\subseteq\text{dom}(f)$, si dice che $f$ è continua su $I$ se $l$ è $\forall x_0\in I$

### Osservazione
Per una funzione $f$ definita su un intorno di $x_0\in\text{dom}(f)$ sono equivalenti le condizioni:
- $f$ è continua in $y_0$
- $\lim_{x\rightarrow x_0}f(x)=f(x_0)$

### Proposizione
Le funzioni elementari (elevamento a potenza, polinomi, funzioni razionali, esponenziali, , logaritmi, cos, sin, tan, cot, arcsin, arccos, arctan, arccot) sono continue

### Esempio
La funzione modulo è continua
$||x|-|x_0||\le|x-y_0|$

# Limiti monolateri
### Definizione (intorni monolateri)
$x_0\in\mathbb{R}, r>0$
$I_r^+(x_0):=[x_0,x_0+r)$
$I_r^-(x_0):=(x_0-r,x_0]$

### Definizione (limite monolatero)
$f:\text{dom}\subseteq\mathbb{R}\rightarrow\mathbb{R}$ definita su un interno destro di $x_0$, eventualmente $x_0$ escluso
Diremo che, per $x$ tendente a $x_0$ da destra
$f$ tende a
- limite finito $l\in\mathbb{R}$ se $\lim_{x\rightarrow {x_0}^+}f(x)=l\ \ \ \ \forall\ \varepsilon>0\ \ \exists\ \delta>0:\begin{array}\ x\in\text{dom}(f) \\ 0<x-x_0<\delta\end{array}\Rightarrow|f(x)-l|<\varepsilon$$
- $+\infty$
- $-\infty$

$f:\text{dom}\subseteq\mathbb{R}\rightarrow\mathbb{R}$ definita su un interno sinistro di $x_0$, eventualmente $x_0$ escluso
Diremo che, per $x$ tendente a $x_0$ da sinistra
$f$ tende a
- limite finito $l\in\mathbb{R}$ se $\lim_{x\rightarrow {x_0}^-}f(x)=l\ \ \ \ \forall\ \varepsilon>0\ \ \exists\ \delta>0:\begin{array}\ x\in\text{dom}(f) \\ -\delta<x-x_0<0\end{array}\Rightarrow|f(x)-l|<\varepsilon$
- $+\infty$
- $-\infty$

### Osservazione
Se i limiti monolateri esistono e coincidono, allora esiste il limite e vale $\lim_{x\rightarrow x_0}f(x)=\lim_{x\rightarrow {x_0}^+}f(x)=\lim_{x\rightarrow {x_0}^-}f(x)$

### Esempio
$\lim_{x\rightarrow {x_0}^\pm}\frac{1}{x}=\pm\infty$

```functionplot
---
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=1/x
b(x)=2
```
Fisso $B>0$ e cerco $\delta>0+c$
$0<x<\delta\Rightarrow\frac{1}{x}>B \Rightarrow x<\frac{1}{B}$
Scelgo $\delta=\frac{1}{B}>0$
Ne segue che, se $0<x<\delta$ allora $\frac{1}{x}>\frac{1}{\delta}=B:\checkmark$

### Definizione (continuità monolatera)
$f:\text{dom}\subseteq\mathbb{R}\rightarrow\mathbb{R}, x_0\in\text{dom}(f)$
Diremo che $f$ è continua in $x_0$ da destra se $\forall\ \varepsilon>0\ \ \exists\ \delta>0:\begin{array}\ x\in\text{dom}(f) \\ 0<x-x_0<\delta\end{array}\Rightarrow|f(x)-f(x_0)|<\varepsilon$

### Esempio
$f:\mathbb{R}\rightarrow\mathbb{R}, x\mapsto\begin{cases}1\text{ se } x\ge1\\0\text{ se } -1<x<1\\-1\text{ se } x\le-1\end{cases}$

# Classificazioni di discontinuità
### Discontinuità
$f:\text{dom}\subseteq\mathbb{R}\rightarrow\mathbb{R}$ definita in un interno di $x_0\in\text{dom}(f)$, eventualmente $x_0$ escluso
$x_0$ è punto di discontinuità eliminabile se
- esiste finito $\lim_{x\rightarrow x_0}f(x)$ e
- **(a)** $x_0\notin\text{dom}(f)$ oppure **(b)** $f(x_0)\ne\lim_{x\rightarrow x_0}f(x)$

### Discontinuità di salto (prima specie)
Se esistono finiti *i* limiti monolateri, ma non coincidono
$\lim_{x\rightarrow {x_0}^+}f(x)\ne\lim_{x\rightarrow {x_0}^-}f(x)$

# Limiti e continuità (II parte)
Unicità del limite, permanenza del segno, confronto

## Teorema (unicità del limite)
Se $f$ ammette limite (finito oppure $\pm\infty$) per $x$ tendente a $c\ (c=x_0\in\mathbb{R}, \pm\infty, {x_0}^\pm)$
allora tale limite è unico

### Dimostrazione
Caso di limite finito $l\in\mathbb{R}$ per $x\rightarrow x_0\in\mathbb{R}$
Supponiamo che sia $l\in\mathbb{R}$ che $l'\in\mathbb{R}$ verifichino la condizione di limite per $f$ al tendere di $x$ a $x_0$
(1): $\forall\ \varepsilon>0\ \ \exists\ \delta>0:\begin{array}\ x\in\text{dom}(f) \\ 0<x-x_0<\delta\end{array}\Rightarrow|f(x)-l|<\varepsilon$

(2): $\forall\ \varepsilon>0\ \ \exists\ \delta'>0:\begin{array}\ x\in\text{dom}(f) \\ 0<x-x_0<\delta'\end{array}\Rightarrow|f(x)-l'|<\varepsilon$
Fisso $\varepsilon>0$. Trovo $\delta>0,\delta'>0$ tali per cui valgono le implicazioni (1) e (2)

$|l-l'|=f(x)-l'-(f(x)-l)\le|f(x)-l'|+|f(x)-l|$        $|a+b|\le|a|+|b|$
Prendo $x\in\text{dom}(f)$ tale che $0<|x-x_0|<\text{min}\{\delta,\delta'\}$
Sono verificate ipotesi delle implicazioni (1) e (2)
Verificato che; $\forall\varepsilon>0,|l-l'|<2\varepsilon$ cioè $|l-l'|\le\text{inf}\{2\varepsilon:\varepsilon>0\}=0\Rightarrow|l-l'|=0$, cioè $l=l'\checkmark$

## Teorema (permanenza del segno)
Supponendo che $f$ ammette limite in $x_0\in\mathbb{R}$
(a) Se esiste $\delta>0$ tale che $\begin{array}\ x\in\text{dom}(f) \\ 0<|x-x_0|<\delta\end{array}\Rightarrow f(x)\ge 0$ allora $\lim_{x\rightarrow x_0}f(x)\ge 0$ (eventualmente $+\infty$)
(b) Se $\lim_{x\rightarrow x_0}f(x)>0$ oppure $+\infty$, allora esiste $\delta>0$ tale che $\begin{array}\ x\in\text{dom}(f) \\ 0<|x-x_0|<\delta\end{array}\Rightarrow f(x)>0$

### Dimostrazione
(a) $|f(x)-l|<\varepsilon\Rightarrow f(x)<l+\varepsilon \leftrightarrow f(x)\ge 0$
$\Rightarrow l+\varepsilon>f(x)\ge 0\rightarrow l+e\ge0$
$\Rightarrow\forall\varepsilon>0$
$l=\text{inf}\{l+\varepsilon:\varepsilon>0\}\ge0$

(b) $\forall\varepsilon>0\ \ \exists\delta>0\begin{array}\ x\in\text{dom}(f) \\ 0<|x-x_0|<\delta\end{array}\Rightarrow |f(x)-l|<\varepsilon$
$l=lim_{x\rightarrow x_0}f(x)>0$
Prendo $\varepsilon=\frac{l}{2}>0$. Ottengo dalla definizione di limite $\delta>0$ tale che $\begin{array}\ x\in\text{dom}(f) \\ 0<|x-x_0|<\delta\end{array}\Rightarrow |f(x)-l|<\varepsilon=\frac{l}{2}$
$-\frac{l}{2}<f(x)-l<\frac{l}{2}$

### Osservazione
(a): se anche $f(x)>0$ in un intorno di $x_0$, **non** si può concludere (in generale) che $\lim_{x\rightarrow x_0}f(x)>0$. Ad esempio $\lim_{x\rightarrow x_0}x^2=0$

## Teorema (algebra dei limiti)
Siano $f,g$ funzioni che ammettono limiti $l, m$ per $x$ tendente a $c$
Allora vale
	1- $\lim_{n\rightarrow c}(f(x)+g(x))=l+m$
	2- $\lim_{n\rightarrow c}(f(x)\cdot g(x))=lm$
	3- $\lim_{n\rightarrow c}(f(x)/g(x))=\frac{l}{m}$
ogni volta che $l,m$ sono entrambi finiti, oppure è verificata una delle seguenti situazioni
	1- $a+\infty=+\infty$,  $a-\infty=-\infty$,  $\pm\infty+\pm\infty=\pm\infty$
	2- $\pm\infty\cdot\pm\infty=\pm\infty$,  $\pm\infty\cdot\mp\infty=-\infty$,  $a(\pm\infty)=\begin{cases}\pm\infty,\text{ se }a>0\\\mp\infty,\text{ se }a<0\end{cases}$
	3- $\frac{a}{\pm\infty}=0$,  $\frac{a}{0^\pm}=\begin{cases}\pm\infty,\text{ se }a>0\\\mp\infty,\text{ se }a<0\end{cases}$,  
$0^\pm$ significa che $lim_{x\rightarrow x_0}g(x)=0$ e inoltre esiste intorno di $c$ in cui $g(x)>0\ \ (p(x)<0)$

# Limiti notevoli

$\lim_{x\rightarrow{0}}\frac{\sin(x)}{x}=1$

$\lim_{x\rightarrow{1}}\frac{\sin(x-1)}{x-1}=1$

$\lim_{x\rightarrow{0}}\frac{\sin^2(x)}{x}=\lim_{x\rightarrow{0}}\frac{\sin(x)\cdot \sin(x)}{x}=0$

$\lim_{x\rightarrow{0}}\frac{\sin(x)}{x^2}=\lim_{x\rightarrow{0}}\frac{\sin^(x)}{x}\frac{1}{x}=+\infty$

$\lim_{x\rightarrow{0}}\frac{3x+5\sin(x)}{4x+7\sin(X)}=\lim_{x\rightarrow{0}}\frac{\frac{3x}{x}+\frac{5\sin(x)}{x}}{\frac{4x}{x}+\frac{7\sin(x)}{x}}=\frac{3+5}{4+7}=\frac{8}{11}$
$\lim_{x\rightarrow{\frac{\pi}{2}}}\frac{\sin(x-\frac{\pi}{2})}{x-\frac{\pi}{2}}$  $x-\frac{\pi}{2}=x$  $\lim_{t\rightarrow{0}}\frac{\sin(t)}{t}=1$



$\lim_{x\rightarrow{1}}(1+\frac{1}{x})^2=e$

$\lim_{x\rightarrow+\infty}(\frac{x+5}{x})^x=\lim_{x\rightarrow+\infty}(1+\frac{5}{x})^x=\lim_{x\rightarrow+\infty}(1+\frac{1}{t})^5t=\lim_{x\rightarrow+\infty}((1+\frac{1}{t})^t)^5=e^5$

$\lim_{x\rightarrow+\infty}(\frac{x-1}{x+3})^{x+2}$
$1+\alpha(x)=\frac{x-1}{x+3}$  $\alpha(x)=\frac{x-1}{x+3}-1=\frac{x-1-x-3}{x+3}=\frac{-4}{x+3}$  $\frac1t=\frac{-4}{x+3}$  $-t=\frac{x+3}{4}$  $-4t=x+3$  $4t=-x-3$  $x=-4t-3$
Provi a portare a $(1+\frac1x)^2$
$\lim_{x\rightarrow+\infty}(1-\frac{4}{x+3})^{x+2}=\lim_{t\rightarrow-\infty}(1+\frac1t)^{-3-4t+2}=\lim_{t\rightarrow-\infty}(1+\frac1t)^{-4t}\cdot(1+\frac1t)^{-1}=e^{-4}$



$f(x)^{g(x)}=e^{g(x)\ln{f(x)}}$

$\lim_{x\rightarrow+\infty}(\frac{1+x^2}{4x^2+3})^{x^2+1}=\lim_{x\rightarrow+\infty}e^{x^{2+1}\ln(\frac{1+x^2}{4x^3+3})}=\lim_{x\rightarrow+\infty}e^{x^{2+1}\ln(\frac{1}{4})}=\lim_{x\rightarrow+\infty}e^{+\infty\ln(\frac{1}{4})}=e^{-\infty}=0$

# Continuità

$f(x)=\begin{cases} ln(x-2)\ \ \ \ x>3\\ x^2+x-3\ \ \ \ x\le3\end{cases}$

$\lim\limits_{x\rightarrow x_0^-}f(x)=\lim\limits_{x\rightarrow x_0^+}f(x)=f(x_0)$

$\lim\limits_{x\rightarrow 3^-}x^2+x-3\overset?=\lim\limits_{x\rightarrow 3^+}\ln(x-2)\overset?=(3)^2+3-3$
$9+3-3=\ln(3-2)=9+3-3$
$9\ne0\ne9$
Non è continua



$f(x)=\begin{cases} -x^2+2\ \ \ \ x\ge1 \\ \arcsin(x^2-1)\ \ \ \ -1<x<1 \\ x^3+1\ \ \ \ x<-1\end{cases}$

$-1\le x^2-1\le 1$
$0\le x^2\le 2$
$x^2\le2$
$-\sqrt2\le x\le\sqrt2$

$\nexists f(-1)$

$\lim\limits_{x\rightarrow 1^-}\arcsin(x^2-1)\overset?=\lim\limits_{x\rightarrow 1^+}-x^2+2\overset?=-x^2+2$
$0=-1+2=-1+2$
$0\ne1=1$
Non è continua

$f(x)=\begin{cases}a\sin(x)+2b\cos(x)+1\ \ \ \ x\le0 \\ 5\sin(x)-2a\cos^2(x)+4b \ \ \ \ 0<x<\pi \\ -a\sin(\frac{x}{2})+2b\sin(x)\ \ \ \ x\ge\pi\end{cases}$

$\lim\limits_{x\rightarrow 0^-}a\sin(x)+2b\cos(x)+1=2b+1$
$\lim\limits_{x\rightarrow 0^+}5\sin(x)-2a\cos^2(x)+4b=-2a+4b$
$2b+1=-2a+4b$

$\lim\limits_{x\rightarrow \pi^-}5\sin(x)-2a\cos^2(x)+4b=-2a+4b$
$\lim\limits_{x\rightarrow \pi^+}-a\sin(\frac{x}{2})+2b\sin(x)=-a$
$-2a+4b=-a$



## Retta bucata
$y=\frac{x^2-1}{x+1}=\frac{(x-1)(x+1)}{x+1}\ \ \ \ D:x\ne-1$

