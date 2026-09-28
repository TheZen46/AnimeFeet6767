$f\quad\text{Dom}(f)\subseteq \mathbb R^2\to\mathbb R$
Se $\exists\ g:(0,r)\to\mathbb R$ con $r>0$ tale che $
- ${\big|}f(\rho\cos{\small(\theta)},\rho\sin{\small(\theta)})-L{\big|}\le{\big|}g(\rho){\big|}\Leftarrow(\text{non dipende da }\theta)\quad\forall\rho\in(0,r),\ \ \forall\theta\in(0,2\pi)$ tale che $\rho\cos{\small(\theta)},\rho\sin{\small(\theta)}\in\text{Dom}(f)$
- $\lim\limits_{\rho\to0^+}g(\rho)=0$
Allora $\lim\limits_{(x,y)\to(0,0)}f(x,y)=L$

## Nota
$\rho\cos{\small(\theta)}'+\rho\sin{\small(\theta)}'=\rho^2(\cos^2\theta+\sin^2\theta)=\rho^2$

# Esempi
- $\displaystyle f(x,y)=\frac{x^3}{x^2+y^2}$
$f(\rho\cos{\small(\theta)},\rho\sin{\small(\theta)})=\frac{(\rho\cos{\small(\theta)})^3}{(\rho\cos{\small(\theta)})^2+(\rho\sin{\small(\theta)})^2}=\frac{\rho^3}{\rho^2}\cos^3\theta=\rho\cos^3\theta$
Questo tende a $0$ per $\rho\to0^+$, quindi proviamo a usare il criterio con $L=0$
${\big|}f(\rho\cos{\small(\theta)},\rho\sin{\small(\theta)})-0{\big|}={\big|}\rho\cos^3\theta{\big|}\le\rho=|g(\rho)|$
Dato che $g(\rho):=\rho$ (che non dipende da $0$), tende a $0$ per $\rho\to0^+$
Allora per il criterio $\lim\limits_{(x,y)\to(0,0)}=0$
- $f(x,y)=\frac{x^2y}{x^4+y^2}$
$\displaystyle f(\rho\cos{\small(\theta)},\rho\sin{\small(\theta)})=\frac{\rho^2\cos^2\theta\cdot\rho\sin\theta}{\rho^4\cos^4\theta+\rho^2\sin^2\theta}=\frac{\rho^{\cancel 3}}{\cancel{\rho^2}}\frac{\cos^2\theta\sin^2}{\rho^2\cos^4\theta+\rho^2\sin^2\theta}$ che tende a $0$ per $\rho\to0^+$, quindi se esiste si deve avere $L=0$.
$\displaystyle f(\rho\cos{\small(\theta)},\rho\sin{\small(\theta)})=\frac{\rho^2\cos^2\theta\cdot\rho\sin\theta}{\rho^4\cos^4\theta+\rho^2\sin^2\theta}=\frac{\rho^{\cancel 3}}{\cancel{\rho^2}}\frac{\cos^2\theta\sin^2}{\rho^2\cos^4\theta+\rho^2\sin^2\theta}$
${\big|}f(\rho\cos{\small(\theta)},\rho\sin{\small(\theta)})-0{\big|}=\rho\frac{|\cos^2\theta\sin\theta|}{|\rho^2\cos^4\theta+\sin^2\theta|}$
Il lato di destra tende a $0$ (ovvio se $\sin0\ne0$, ed è identicamente nullo se $\sin0\ne0$) però dipende da $0$
Si potrebbe maggiorare con $\rho\cdot\frac1{|\rho^2\cos^4\theta+\sin^2\theta|}$ ma questo continua a dipendere da $0$, e non è chiaro come rimuovere la dipendenza.
	Ciò in effetti non si può fare perché abbiamo già visto che questo limite non esiste.

# Derivate parziali
## Definizione
Sia $f:\text{Dom}f\subseteq\mathbb R^n\to\mathbb R$, sia $x_0\in\text{Dom}f$ (ossia all'interno di $\text{Dom}f$)
Diciamo che $f$ ammette derivata parziale rispetto a $x_i$ in $\vec{x_0}$ se esiste finito il limite $\displaystyle\lim\limits_{h\to0}\frac{f(\vec{x_0}+h\overbrace{\vec{e_i}}^\text{canonica})-f(\vec{x_0})}h$ dove $\vec{e_i}=\underset{\text{i-esima componente}}{(0,0,\ldots,0,1,0,\ldots,0)}$
Quando esiste tale limite è detto la derivata parziale di $f$ in $x_0$ rispetto a $x_i$ e si indica con $\frac{\partial f}{\partial x_i}(\vec{x_0})$
Coincide con la solita derivata in $1$ variabile rispetto a $x_i$, trattando tutte le altre variabili come costanti
Nel caso $n=2$:
$\frac{\partial f}{\partial x}(x_0,y_0)=\lim\limits_{x\to x_0}\frac{f(x,y_0)-f(x_0,y_0)}{x-x_0}=\left[\lim\limits_{h\to0}\frac{f(x_0+h,y_0)-f(x_0,y_0)}{h}\right]$
$\frac{\partial f}{\partial y}(x_0,y_0)=\lim\limits_{y\to y_0}\frac{f(x_0,y)-f(x_0,y_0)}{y-y_0}$
Se questi limiti esistono

Une funzione $f$ che ammette derivate parziali in $x_0$ rispetto a tutte le variabili si dice **derivabile** in $\vec{x_0}$. In tal caso si definisce il **gradiente** di $f$ in $\vec{x_o}$ come $\nabla f(\vec{x_0})=\left(\frac{\partial f}{\partial x_1}(x_0),\ldots,\frac{\partial f}{\partial x_n}(x_0)(\right)$
$n-2:\ \nabla f(x_0,y_0)=\left(\frac{\partial f}{\partial x}(x_0, y_o),\frac{\partial f}{\partial y}(x_0, y_o)\right)$

## Esempi
- $f(x,y)=x$
$\frac{\partial f}{\partial x}(x, y)=1$
$\frac{\partial f}{\partial y}(x, y)=0$

$x$ è da considerare come costante quando calcoliamo $\frac{\partial}{\partial y}$, quindi ha derivata nulla

- $f(x,y,z)=x\ln(x+y-z)$
$\text{Dom}(f)=\{(x,y,z)\in\mathbb R^3|x+y-z>0\}$
$\displaystyle\frac{\partial f}{\partial x}(x,y,z)=1\cdot\ln(x+y-z)+x\cdot\frac{1}{x+y-z}$
$\displaystyle\frac{\partial f}{\partial y}(x,y,z)=x\frac{\partial f}{\partial y}\ln(x+y-z)=\frac{x}{x+y-z}$
$\displaystyle\frac{\partial f}{\partial z}(x,y,z)=\frac{-x}{x+y-z}$

$\displaystyle\nabla f(x,y,z)=\left(\ln(x+y-z)+\frac{x}{x+y-z},\frac{x}{x+y-z},\frac{-x}{x+y-z}\right)$


$\frac{\partial f}{\partial x}(x_0)$ è il coefficiente angolare della retta tangente al grafico rispetto al piano $x=x_0$

L'analogo in un direzione generica $\vec v\in\mathbb R^n$ è dato dalla derivata direzionale rispetto a $\vec v$ è $\displaystyle\frac{\partial f}{\partial \vec v}(\vec {x_0})=\lim\limits_{h\to 0}\frac{f(x_0+h\vec v)-f(\vec{x_0})}{h}$
Quando il limite esiste finito chiaramente $\frac{\partial f}{\partial x_i}=\frac{\partial f}{\partial e_i}$

## Esempi
- $f(x,y)=x^2+y^3,\quad(x_0,y_0)=(0,1)\quad\vec v=(1,1)$
$\displaystyle\lim\limits_{h\to0}\frac{f(0,1)+h(1,1)-f(0,1)}h=\lim\limits_{h\to0}\frac{f(h,1+h)-1}h=\lim\limits_{h\to0}\frac{h^2+(1+h)^2-1}h=\lim\limits_{h\to0}\frac{(1+h^3)-1}h=3$

- $f(x,y)=\begin{cases}\frac{x^2y}{x^4+y^2}&\text{se }(x,y)\ne(0,0)\\0&\text{se }(x,y)=(0,0)\end{cases}$
Calcoliamo la derivata direzionale rispetto a un generico vettore $\vec v=(v_1,v_2)\ne(0,0)$

$\displaystyle\frac{\partial f(0,0)}{\partial\vec v}=\lim\limits_{h\to0}\frac{f\left((0,0)+h(\vec v)-f(0,0)\right)}h=\lim\limits_{h\to0}\frac{f(hv_1,hv_2)}h=\lim\limits_{h\to0}\frac{\frac{h^2{v_1}^2\cdot hv_2}{h^4{v_1}^4+h^2{v_1}^2}}h=\lim\limits_{h\to0}\frac{h^3{v_1}^2v_2}{h^5{v_1}^4+h^3{v_2}^2}=\lim\limits_{h\to0}\frac{{v_1}^2v_2}{h^2{v_1}^4+{v_2}^2}=\begin{array}{l}\nearrow&\!\!\!\frac{{v_1}^2v_2}{{v_2}^2}=\frac{{v_1}^2}{v_2}&\text{se }v_2\ne0\\\searrow&\!\!\!0&\text{se }v_2=0\end{array}$

Quindi $f$ ammette derivate direzionali in $(0,0)$ lungo qualunque direzione (e in particolare è derivabile), pure non essendo continua in $(0,0)$
Quindi per $n\ge2$, la derivabilità non implica la continuità

# Differenziabilità
Sia $f:\text{Dom}f\subseteq\mathbb R^n\to\mathbb R$ derivabile in $\vec {x_0}\in\text{Dom} f$.
Diciamo che $f$ è **differenziabile** in $\vec{x_0}$ se $f(\vec x)=f(\vec {x_0})+\nabla f(x_0)\ \bullet\ (\vec {x}-x_0)+\theta(\Vert x-x_0\Vert)$ per $\vec x\to\vec{x_0}$
Equivalentemente se $\displaystyle\lim\limits_{(x,y)\to(x_0,y_0)}\frac{f(x,y)-f(x_0y_0)-\nabla f(\vec{x_0})\ \bullet\ (\vec x-\vec {x_0}))}{\Vert x-x_0\Vert}=\overset{\boxed\star}0$

## Nota
- $g:\mathbb R\to\mathbb R$ è derivabile in $\displaystyle x_0\iff\exists\ u\ \lim\limits_{x\to x_0}\frac{f(x)-f(x_0)-u(x-x_0)}{\vert x-x_0\vert}=0$
- $f$ differenziabile in $x_0\Rightarrow f$ continua in $x_0$
	Infatti $\boxed\star\Rightarrow\lim\limits_{x\to x_0}\left(f(\vec x)-f(\vec{x_0})-\nabla f(\overbrace{\vec x-\vec{x_0}}^0)\right)=0\Rightarrow\lim\limits_{\vec x\to \vec{x_0}}f(\vec x)=f(\vec {x_0})$
- Dalla definizione differenziabilità $\Rightarrow$ derivabilità
	In generale $f$ differenziabile $\Rightarrow f$ ha derivate direzionali in tutte le direzioni e si ha $\frac{\partial f}{\partial \vec v}(\vec{x_0})=\nabla f(\vec{x_0})\ \bullet\ \vec v\qquad\forall\ \vec v\in\mathbb R^n\setminus\{\vec 0\}$
- Posto $\vec w=(\vec x-\vec {x_0})$ (incremento) il differenziale di $f$ in $\vec x_0$ è l'applicazione lineare $df_{\vec x_0}:\begin{array}{l}\mathbb R^n&\longrightarrow&\mathbb R\\\vec w&\longmapsto& df_{\vec x_0}(\vec w)=\nabla f(\vec x_0)\ \bullet\ \vec w\end{array}$
- L'espressione $f(\vec x)=f(\vec x_0)+\nabla f(\vec x_0)\ \bullet\ (\vec x-\vec x_0)+0(\Vert x-x_0\Vert)$ è lo sviluppo di Taylor di ordine $1$ di $f$ centrato in $\vec x_0$
	L'iperpiano tangente al grafico di $f$ in $(\vec x_0,f(\vec x_0))\quad x_{n+1}=f(\vec x_0)+\nabla f(\vec x_0)\ \bullet\ (\vec x-\vec x_0)$
	Se $n=2$, il piano tangente al grafico di $f$ in $(x_0,y_0,f(x_0,y_0))$ è: $Z=f(x_0,y_0)+\nabla f(x_0,y_0)\ \bullet\ (x-x_0,y-y_0)$

## Esempio
- $f(x,y)=x^2+y^2\qquad\text{Dom}f=\mathbb R^2$
	Calcolare l'equazione del piano tangente al grafico di $f$ in $(1,3,f(1,3))=(1,3,10)$
Da teoremi visti più avanti abbiamo che $f$ è differenziabile in $\mathbb R^2$
$\frac{\partial f}{\partial x}(x,y)=2x,\ \frac{\partial f}{\partial y}(x,y)=2y$
$\nabla f(x,y)=(2x,2y),\ \nabla f(1,3)=(2,6)$
$Z=\overset{f(1,3)}{10}+(2,6)\ \bullet\ (x-1, y-3)=10+2(x-1)+6(y-3)=10+2x-2+6y-18=2x+6y-10$
$(Z=2x+6y-10)$

# Teorema del differenziale totale
Se $f$ è derivabile in $A\subseteq\text{Dom}f$ aperto con derivate parziali continue in $A$, allora $f$ è differenziabile in $A$
## Esempio
$f(x,y)=x^2+y^2,\quad\nabla f(x,y)=(2x,2y)$ che è continua in $\mathbb R^2$.
	Quindi $f$ è differenziabile in $\mathbb R^2$
# Derivate del secondo ordine
Sia $f$ derivabile in $\vec x_0\in\text{Dom}f$
Se $\frac{\partial f}{\partial x_i}(\vec x_0)$ ammette derivata parziale rispetto a $x_j$ in $x_0$, allora diciamo che $f$ ammette derivata parziale seconda rispetto a $x_i$ e $x_j$ in $x_0$.
Si denota come $\displaystyle\frac{\partial^2}{\partial{x_j}\partial{x_i}}f(\vec x_0)\ \left(\text{oppure }D_{X_i,\ X_j}f(\vec x_0)\right)$
Se $j\ne i$, si dice derivata **mista**
Se $j=i$, si dice derivata **pura** (e in tal caso scriviamo $\frac{\partial^2}{\partial x^2}f(\vec x_0)$)

Se $f$ ammette tutte le derivate parziali seconde definiamo la matrice **Hessiana** di $f$ in $\vec x_0$ come $\displaystyle Hf(\vec x_0)=\begin{pmatrix}\frac{\partial^2}{\partial {x_1}^2}f(\vec x_0)&\dots&\frac{\partial^2}{\partial x_1\partial x_n}f(\vec x_0)\\\vdots&&\vdots\\\frac{\partial^2}{\partial x_n\partial x_1}f(\vec x_0)&\dots&\frac{\partial^2}{\partial {x_n}^2}f(\vec x_0)\end{pmatrix}$
## Esempio
- $f(x,y)=\sin(xy^2)$
	$\frac{\partial f}{\partial x}(x,y)=y^2\cos(xy^2)$
	$\frac{\partial^2 f}{\partial x^2}(x,y)=-y^4\sin(xy^2)$
	$\frac{\partial f}{\partial y}=2yx\cos(xy^2)$
	$\frac{\partial^2 f}{\partial y^2}=2x\cos(xy^2)-4x^2y^2\sin(xy^2)$
	$\frac{\partial^2 f}{\partial y\partial x}(x,y)=2\cos(xy^2)-2xy^3\sin(xy^2)$
	$\frac{\partial^2 f}{\partial x\partial y}(x,y)=2\cos(xy^2)-2xy^3\sin(xy^2)$

## Definizione
Se le derivate seconde esistono e sono sono continue diciamo che $f$ è di classe 

## Teorema di Schwarz
Sia $F$ di classe $C^2$ in $x_0\in\operatorname{Dom}(f)$, allora $\frac{\partial^2}{\partial x_i\partial x_j}f(\vec x_0)=\frac{\partial^2}{\partial x_j\partial x_i}f(\vec x_0)$
In particolare, $Hf(\vec x)$ è una matrice simmetrica

Se $f$ è di classe $C^2$ in $\vec x_0$, allora vale la formula di Taylor di ordine $2$ centrata in $\vec x_0$:
$f(\vec x)=f(\vec x_0)+\nabla f(\vec x_0)\cdot(\vec x-x_0)+\frac 12(\vec x-\vec x_0)\ \bullet\ Hf(\vec x_0)\cdot(\vec x-\vec x_0)+o(\Vert x-x_0\Vert^2)$ per $\vec x\to\vec x_0$

## Differenziale di ordine 2
$d^2 f_{x_0}\quad\begin{array}{l}\mathbb R^2\times\mathbb R^2&\to&\mathbb R\\(\vec v,\vec w)&\mapsto& V\ \bullet\ Hf(\vec x_0)\cdot W\end{array}$

# Estremi di funzioni in più variabili
## Definizione
Sia $f:\operatorname{Dom}(f)\subseteq\mathbb R^n\to\mathbb R,\ \vec x_0\in\operatorname{Dom}f$
1) $\vec x_0$ si dice punto di minimo locale se esiste $\varepsilonlon>0$ tale che $f(\vec x)\ge f(\vec x_0)\quad\forall\ x\in B_\varepsilon(\vec x_0)\cap\operatorname{Dom}(f)$
	In tal caso $f(\vec x_0)$ si dice minimo locale
2) Se $\vec x_0$ si dice punto di minimo globale se $f(\vec x)\ge f(\vec x_0)\quad\forall\ x\in\operatorname{Dom}(f)$
	In tal caso $f(\vec x_0)$ si dice minimo globale e si scrive $f(\vec x_0)=\min\limits_{\vec x\in A}f(\vec x)$
3) Punti di massimo locale e globale (e i corrispettivi massimi) sono definiti nello stesso modo ma con $\ge$ invece che $\le$
4) Un punto di $\max$ o $\min$ (locale o globale) si dice **estremo** (locale o globale) per $f$

# Teorema di Weierstrass
Sia $f:\operatorname{Dom}(f)\subseteq\mathbb R^n\to\mathbb R$
Sia $K\subseteq\operatorname{Dom}(f)$ chiuso e limitato
Allora $f$ ammette massimo e minimo (globale) su $K$ (ossia esistono almeno un punto $\min$ e uno $\max$ globale su $K$)

## Esempi
1) $f(x,y)=x^2+y^2$
$\operatorname{Dom}(f)=\mathbb R^2$
$K=\{(x,y)\in\mathbb R^2|x^2+y^2\le 1\}$

$f(0,0)=0$
$f(x,y)\ge0\quad\forall\ x,y$
Quindi $(0,0)$ è punto $\min$ locale e globale per $f\ {\big(}\Rightarrow\min\limits_{(x,y)\in K}f(x,y)=0{\big)}$
$f$ non ha punti $\max$ locali o globali su $\operatorname{Dom}(f)$, ma dal teorema sappiamo che ha massimo su $K$
Osserviamo che $f(x,y)=1\quad\forall\ (x,y)\in\partial K$ e $f(x,y)\le 1)\quad\forall(x,y)\in K$
Quindi tutti i punti di $\partial K$ sono punti $\max$ su $K$ e $\max\limits_{(x,y)\in K}f(x,y)=1$
Dato che $\min\limits_{(x,y)\in K}f(x,y)=0,\ \ \max\limits_{(x,y)\in K}f(x,y)=1\Rightarrow f(K)=[0,1]$


2) Stesso di 1) ma su $A=\overset\circ K=\{(x,y)|x^2+y^2<1\}$
$0$ è $\min$ su $A$
$A$ non è chiuso, quindi non è detto che $f$ abbia $\max/\min$ su $A$

In effetti in questo caso $f$ non ha $\max$ su $A$ perché è chiaro che $\sup\limits_{(x,y)\in A}f(x,y)=1$, ma il valore $1$ non è mai raggiunto
$f(A)=[0,1)$


3) $f(x,y)=\frac1{xy}\quad\operatorname{Dom}f=\left\{(x,y)\in\mathbb R^2|\array{x\ne0\\y\ne0}\right\}$
$\operatorname{Dom}(f)$ non è né chiuso né limitato, quindi non è detto che $f$ abbia $\max$ e $\min$ su $\operatorname{Dom}(f)$
In effetti, $\underbrace{f\left(\operatorname{Dom}(f)\right)}_{\operatorname{Im}(f)}=(-\infty,0)\cup 0,\infty)$
Quindi $f$ non ha n'$\min$ né $\max$ su $\operatorname{Dom}(f)$
In ogni caso, però, se $K\in\operatorname{Dom}(f)$ è chiuso e limitato, allora $f$ ha $\max$ e $\min$ su $K$

## Definizione
Dato $f:\operatorname{Dom}(f)\subseteq\mathbb R^n\to\mathbb R$, derivabile in $\vec x_0\in\operatorname{Dom}(f)$, diciamo che $\vec x_0$ è un punto critico per $f$ se $\nabla f(x_0)=\vec 0\leftarrow\text{sistema di }n\text{ equazioni in }n\text{ variabili}$

## Teorema di Fermat
Sia $f$ differenziabile in $\vec x_0\in\operatorname{Dom}(f)$
Se $x_0$ è estremo locale per $f$, allora $\vec x_0$ è punto critico

### Dimostrazione
Sia $\vec v\in\mathbb R^n\backslash\{\vec0\}$
Dato che $\vec x_0$ è estremo locale per $f$, allora lo è anche per $f$ rispetto alla retta $\{\vec x_0+t\vec v|t\in\mathbb R\}$, ossia $f(\vec x_0+t\vec v)$ ha un estremo locale in $t=0$
Per il teorema di Fermat in una variabile si ha $\frac d{dt}f(\vec x_0)+t\vec v|_{t=0}=0$, ma $\frac d{dt}f(\vec x_0)+t\vec v|_{t=0}=\frac{\partial f}{\partial \vec v}(\vec x_0)$
Prendendo $\vec v=\vec l_i$ abbiamo quindi $\frac{\partial f}{\partial \vec v}(\vec x_0)\quad\forall i=1,\ldots,n\iff\nabla f(\vec x_0)=\vec 0$

#### Nota
Non tutti i punti critici sono estremi locali
Ad esempio $f(x,y)=x\cdot y$
$\nabla f(x,y)=(y,x)$
$\nabla f(x,y)=(0,0)\iff\cases{y=0\\x=0}\iff(x,y)=(0,0)$
$(0,0)$ è punto critico

$f(0,0)=0$
Per quanto vicino ci mettiamo a $(0,0)$ troviamo punti tali che $f(x,y)>0\ {\big()\iff f(x,y)>f(0,0)}{\big)}$ e punti tali che $f(x,y)<0{\big(}\iff f(x,y)<f(0,0){\big)}$
Quindi $(0,0$) non può essete né punto $\max$ né punto $\min$

Per il Teorema di Fermat, gli estremi locali (e globali se esistono) sono da cercare
- Punti critici di $f$
- Punti in cui $f$ non è differenziabile
- Punti del bordo del $\operatorname{Dom}(f)$ (o dell'insieme considerato)

### Esempio
$f(x,y)=\sqrt{x^2+y^2}\qquad \operatorname{Dom}(f)=\mathbb R^2$   cono circolare
$\nabla f(x,y)=\left(\frac x{\sqrt {x^2+y^2}},\frac y{\sqrt{x^2+y^2}}\right)\in\mathbb R^2\backslash\{0\}$
$f$ non è derivabile in $(0,0)$ e ha $\min$ locale e globale in $(0,0)$

# Teorema (criterio) dell'Hessiana
Sia $\vec x_0\in\operatorname{Dom}(f)$ un punto critico per $f$ e che $f$ sia di classe $C^2$ in $\vec x_0$
Allora:
1) Se $Hf(\vec x_0)$ è definita positiva (ossia ha tutti gli autovalori $>0$) allora $\vec x_0$ è punto di $\min$
2) Se $Hf(\vec x_0)$ è definita negativa (ossia ha tutti gli autovalori $<0$) allora $\vec x_0$ è punto $\max$
3) Se $Hf(\vec x_0)$ è indefinita (ossia si sono sia autovalori $>0$ che $<0$) allora $\vec x_0$ non è estremo locale e si dice punto di sella
4) Se $Hf(\vec x_0)$ è semidefinita positiva o negativa (ossia se c'è almeno un autovalore $=0$ e tutti gli altri sono tutti $\ge/\le$) allora il criterio non conclude
Nel caso $n=2$, il criterio diventa
- Se $\det\left(Hf(\vec x_0)\right)>0$
	$\frac{\partial^2}{\partial x^2}f(\vec x_0)>0\Rightarrow \vec x_0$ è punto $\min$ locale ($\vec x_0=\text{elemento di }H$)
	$\frac{\partial^2}{\partial x^2}f(\vec x_0)<0\Rightarrow \vec x_0$ è punto $\max$ locale
- Se $\det\left(Hf(\vec x_0)\right)<0\Rightarrow \vec x_0$ è punto di sella
- Se $\det\left(Hf(\vec x_0)\right)=0\Rightarrow$ il criterio non conclude

## Esempio
1) $f(x,y)=x^2+y^2$
$\nabla f(x,y)=(2x,2y)$
$\nabla f(x,y)=(0,0)\iff(x,y)=(0,0)\Rightarrow(0,0)$ è l'unico punto critico
$\array{\frac{\partial^2}{\partial x^2}f(x,y)=2\\\frac{\partial^2}{\partial y^2}f(x,y)=2}\qquad\frac{\partial^2}{\partial x\partial y}f(x,y)=0\qquad Hf(x,y)=\pmatrix{2&0\\0&2}\Rightarrow Hf(0,0)=\pmatrix{2&0\\0&2}$
Gli autovalori sono $2,2>0$ (nota: la matrice è diagonale) e quindi $(0,0)$ è $\min$ locale
	In alternativa potevamo osservare che $\det\left(Hf(0,0)\right)=4>0$ e $\frac{\partial^2}{\partial x^2}f(x,y)=2>0\Rightarrow\min$ locale

2) $f(x,y)=-x^2-y^2$
$\nabla f(x,y)=(-2x,-2y)$
$\nabla f(x,y)=(0,0)\iff(x,y)=(0,0)\Rightarrow(0,0)$ è l'unico punto critico
$\array{\frac{\partial^2}{\partial x^2}f(x,y)=-2\\\frac{\partial^2}{\partial y^2}f(x,y)=-2}\qquad\frac{\partial^2}{\partial x\partial y}f(x,y)=0\qquad Hf(x,y)=0\qquad Hf(x,y)\pmatrix{-2&0\\0&-2}\Rightarrow Hf(0,0)=\pmatrix{-2&0\\0&-2}$
Gli autovalori sono $-2,-2<0$ e quindi $(0,0)$ è $\max$ locale
	In alternativa potevamo osservare che $\det\left(Hf(0,0)\right)=-4<0$ e $\frac{\partial^2}{\partial x^2}f(x,y)=-<>0\Rightarrow\max$ locale

3) $f(x,y)=x^2-y^2$
$\nabla f(x,y)=(2x,-2y)$
$\nabla f(x,y)=(0,0)\iff(x,y)=(0,0)\Rightarrow(0,0)$ è l'unico punto critico
$Hf(x,y)=\pmatrix{2&0\\0&-2}\Rightarrow Hf(0,0)=\pmatrix{2&0\\0&-2}$
Gli autovalori sono $2>0,-2<0\Rightarrow(0,0)$ è punto di sella

4) $f(x,y)=x^2+y^4$
$\nabla f(x,y)=(2x,4y^3)$
$\nabla f(x,y)=(0,0)\iff(x,y)=(0,0)\Rightarrow(0,0)$ è l'unico punto critico
$\array{\frac{\partial^2}{\partial x^2}f(x,y)&\mskip{-12mu}=&\mskip{-12mu}2\\\frac{\partial^2}{\partial y^2}f(x,y)&\mskip{-12mu}=&\mskip{-12mu}12y^2}\qquad\frac{\partial^2}{\partial x\partial y}f(x,y)=0=\frac{\partial^2}{\partial y\partial x}\qquad Hf(x,y)=0\qquad Hf(x,y)\pmatrix{2&0\\0&12y^2}\Rightarrow Hf(0,0)=\pmatrix{-2&0\\0&0}$
$Hf(x,y)=\pmatrix{2&0\\0&12y^2}\Rightarrow Hf(0,0)=\pmatrix{2&0\\0&0}$
Gli autovalori sono $2>0$ e $0\Rightarrow Hf(0,0)$ è semidefinita positiva, il criterio non conclude
	Anche se il criterio non conclude, $f(x,y)\ge0=f(0,0)^{\forall\ (x,y)}\Rightarrow(0,0)$ è $\min$ locale e globale

5) $f(x,y)=(y-x^2)(y-2x^2)$
$\frac{\partial}{\partial x}f(x,y)=-2x(y-x^2)+(y-x^2)(-4x)=8x^3-6xy=2x(4x^2-3y)\qquad\frac{\partial}{\partial y}f(x,y)=y-2x^2+y-x^2=2y-3x^2$
$\nabla f(x,y)=\left(2x(4x^3-3y),2y-3x^2\right)$
$\nabla f(x,y)=(0,0)\iff\cases{2x(4x^2-3y)=0\ \  \boxed{1}\ \boxed{2}\\2y-3x^2=0}$
$\boxed{1}\ \cases{2x=0\\2y-3x^2=0}\Rightarrow(x,y)=(0,0)$
$\boxed{2}\ \cases{4x^2-3y=0\\2y-3x^2=0}\Rightarrow\cases{y=\frac43x^2\\2(\frac43x^2)-3x^2=0}\Rightarrow\cases{y=\frac43x^2\\-\frac13x^2=0}\Rightarrow(x,y)=(0,0)$
$(0,0)$ è l'unico punto critico
$\array{\frac{\partial^2}{\partial x^2}f(x,y)&\mskip{-12mu}=&\mskip{-12mu}24x^2-6y\\\frac{\partial^2}{\partial y^2}f(x,y)&\mskip{-12mu}=&\mskip{-12mu}2}\qquad\frac{\partial^2}{\partial x\partial y}f(x,y)=-6x\qquad Hf(x,y)\pmatrix{24x^2-6y&-6x\\-6x&2}\Rightarrow Hf(0,0)=\pmatrix{0&0\\0&2}$
Il criterio non conclude ($H$ è semidefinita positiva)
$f(0,0)=\vec 0$
$f(x,y)=\underbrace{(y-x^2)}_{y=x^2\iff0}\ \cdot\ \underbrace{(y-2x^2)}_{y=2x^2\iff0}$
Intorno a $(0,0)$ ci sono punti in cui $f$ e sia $>0$ che $<0$ quindi $(0,0)$ non è estremo locale
Però $f$ rispetto a qualunque retta per $(0,0)$ ha $\min$ locale in $(0,0)$

## Note
In generale se il criterio non conclude bisogna studiare il segno di $f(\vec x)-f(\vec x_0)$
Se è $\ge0$ in un intorno di $\vec x_0$ allora $x_0$ è $\min$ locale
Se è $\le0$ in un intorno di $\vec x_0$ allora $x_0$ è $\max$ locale