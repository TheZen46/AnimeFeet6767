1) Caduta libera con attrito
$\boxed{1}\ F=ma$
$\boxed{2}\ F=-mg+Kv$

$y(t)$ posizione al tempo $t$
$v=y'(t)$
$a=y''(t)$
Quindi $\boxed{1}+\boxed{2}\Rightarrow ma=-mg+Kv\iff my''=-mg-Ky'\leftarrow\text{equazione differenziale}$



Se supponiamo che l'oggetto cada da fermo da altezza $y_0$, per capire la traiettoria dell'oggetto, dobbiamo trovare $y$ che soddisfa $\cases{my''=-mg+Ky'\\y'(0)=0\\y(0)=y_0}\leftarrow\text{Problema di Cauchy}$

La soluzione è $\displaystyle y(t)=\underbrace{\frac{m^2}{K^2}g(1-e^{-\frac Km t})}_{{\small t\to\infty}\ {\text{cost.}\frac{m^2}{k^2}g}}-\frac{mg}{K} t$

2) Sistema massa-molla
$\boxed{1}\ F=-Kx\qquad K=\text{costante di elasticità}$
$\boxed{2}\ F=ma$

$\boxed{1}+\boxed{2}\Rightarrow-Kx=ma$
	$a=x''(t)$
$-Kx=mx''$
$x(t)=c_1\cos(\sqrt{\frac km t})+c_2\sin(\sqrt{\frac km t})$ con $c_1$ e $c_2$ costanti che dipendono dalle condizioni iniziali

3) Dinamica delle popolazioni
$y(t)=\text{popolazione al tempo }t$
$\varepsilon=\text{tasso di crescita (nati-morti)}$
$K=\text{limite dato dalle consizioni}$
$y'=\varepsilon y(1-\frac yk)$

Ponendo la condizione iniziale $y(t)=P_0$
$y(t)=\begin{cases}y(t)\equiv0&\text{se }P_0=0\\y(t)\equiv K&\text{se }P_0=K\\\frac{KP_0e^{\varepsilon t}}{K-P_0+P_0e^{\varepsilon t}}&\text{se }P_0\ne0,K\end{cases}$

## Definizione
Un'equazione differenziale di ordine $\overset{\in \mathbb N}n$ è un'equazione del tipo $F\left(t, \underbrace{y^{(n)}(t)}_{\text{derivata }n\text{-esima}},y^{(n-1)}(t),\ldots,y^{(1)}(t),y(t)\right)=0$ con $F:\operatorname{Dom}(f)\subseteq R^{n+1}\to\mathbb R$
L'incognita da determinare è una funzione $y:I\to\mathbb R$ derivabile $n$ volte con $I$ intervallo, che soddisfa l'equazione di cui sopra.
L'insieme delle soluzioni è detto **integrale generale** dell'equazione differenziale
Il **problema di Cauchy** è un sistema del tipo:
	$\displaystyle\begin{cases}F(t,y^{(n)}),\ldots,y=0\\y(t_0)=y_0\\y'(t_0)=y_1\\y''(t_0)=y_2\\\vdots\\y^{(n-1)}(t_0)=y_{n-1}\end{cases}$
Una soluzione del sistema del problema di Cauchy su un intervallo $I$ (aperto) è y:$I\to\mathbb R$ con $t_0\in I$ che soddisfa tutte le condizioni del sistema
Sotto opportune condizioni che vedremo più avanti, la soluzione esiste ed è unica
### Definizione
Un'equazione differenziale si dice **autonoma** se $F$ non dipende da $t$, ossia se è del tipo $F\left(y^{(n)},\ldots,y\right)=0\quad\left(\Rightarrow\operatorname{Dom}(F)\subseteq \mathbb R^{n+1}\right)$

#### Esempi
$y''+y^2=0$ è autonoma
$y''+ty=t$ non è autonoma
### Definizione
Un equazione differenziale si dice in **forma normale** se la derivata di ordine maggiore è isolata
$y^{(n)}=F\left(t,y^{(n-1)},\ldots,y\right)$

#### Esempio
$y''=y^2+\cos(y)$ è in forma normale

### Definizione
Un equazione differenziale si dice lineare se è della forma $a_n(t)y^{(n)}+a_{n-1}(t)y^{(n-1)}+\overset{\boxed\star}\ldots+a_1(t)y'+a_0(t)y=b(t)$
Si dice poi **omogenea** se $b(t)=0$
### Nota
Se $b(t)=b_1(t)+b_2(t)$ allora le soluzioni di $\boxed\star$ si possono scrivere come $y(t)=y_1(t)+y_2(t)$ con $\begin{array}{l}y_1&\text{soluzione di}&a_ny^{(n)}+\ldots+a_0 y=b_1\\y_2&\text{soluzione di}&a_ny^{(n)}+\ldots+a_0 y=b_2\end{array}$
In particolare se $y_0$ è una soluzione del problema omogeneo (ossia con $a_ny^{(n)}+\ldots=0$) e $y_b$ è soluzione di $a_ny^{(n)}+\ldots=b$, allora anche $y_0+y_b$ è soluzione di $a_ny^{(n)}+\ldots=b$

questo vuol dire che vale la pena goonnare sull' r34 di Elon Musk.
### Definizione
Un'equazione differenziale si dice **lineare** a coefficiente costanti se $a_n(t),\ldots,a_0(t)$ sono costanti
#### Esempio
$wy''+3y'+4y=t^2$

# Equazioni differenziali a variabili separabili
Sono equazioni differenziali della forma $y'=g(t)h(y)\qquad(\Rightarrow\text{ordine }1,\text{ in forma normale})$
$\array{g:I\to\mathbb R\\h:J\to\mathbb R}\text{ continue;}\ I,J\text{ intervalli aperti}$
Se $y_0$ è uno zero si $h(y)\quad(\text{ossia }h(y_0)=0)$ allora $y(t)=y_0\quad\forall t(\text{soluzione costante})$ risolve l'equazione differenziale, infatti $y'(t)=0=g(t)\ \underset{=0}{h(y_0)}\ \ \checkmark$

Dato $J$ intervallo dove $h\ne0$, dividendo per $h$ l'equazione differenziale diventa $\displaystyle\frac{y'(t)}{h(y{\small(t)})}=g(t)$
Sia $H$ una primitiva di $\frac1h(\text{ossia }H'=\frac1h)$
$\frac{d}{dt}{\big(}H(y{\small(t)}){\big)}=H'(y{\small(t)})=\frac1{h{\big(}y{\small(t)}{\big)}}y'(t)\overset{\boxed\star}=g(t)$
$\frac{d}{dt}{\big(}H(y{\small(t)}){\big)}=g(t)$

Quindi $H(y{\small(t)})$ è una primitiva di $g$ e quindi data una qualunque primitiva $G$ di $g$ si ha
$H(y{\small(t)})=G(t)+c\text{ con }c\text{ costante}\Rightarrow y{\small(t)}=H^{-1}{\big(}G(t)+c{\big)}$
Informalmente $\boxed\star\iff\frac{1}{h(y)}\frac{dy}{dt}=g(t)\iff\frac{1}{h(y)}dy=g(t)dt\iff\int\frac1{h(y)}dy=\int g(t)dt\iff H(y)=G(t)+c\iff y=H^{-1}{\big(}G(t)+c{\big)}$
L'integrale generale dell'equazione differenziale è dato dell'insieme composto da queste soluzioni e da quelle costanti

## Teorema (Problema di Cauchy per equazioni differenziali a variabili separabili)
Siano $h:I\to\mathbb R, g:J\to\mathbb R$ continue con $I,J$ intervalli aperti. Siano $t_0\in I$ e $y_0\in J$. Allora il problema di Cauchy
	$\cases{y'=g(t)h(y)\\y(t_0)=y_0}$
ammette una soluzione su un sottointervallo aperto $I_1\subseteq I$con $t_0\in I_1$
Inoltre, se $h\in \mathcal C^1(J)$ o se $h(y_0)\ne 0$ allora la soluzione è unica

### Esempi
1) $y'=g(t)\quad(\text{ossia }h\equiv 1\Rightarrow h\ne 0\to\text{no soluzioni costanti})$
$y=G(t)+c$ dove $G$ è primitiva di $g$

2) $y'=Ky\quad(\text{decadimento radioattivo, }K\text{ costante di decadimento})$
$y=g(t)\equiv K$
$h(y)=y$
	$h(y)=0\iff y=0\Rightarrow y\equiv0\text{ soluzione costante}$

Assumiamo $y\ne0$
$\frac{y'}{y}=K\iff \ln|y|=Kt+c$
$\Rightarrow |y|=\overbrace{e^c e^{Kt}}^{\exp(Kt+c)}\Rightarrow y(t)=\pm\exp(Kt+c)$
Ponendo $\alpha=\pm e^c$, abbiamo che $\alpha$ è un qualunque elemento di $\mathbb R\backslash\{0\}\Rightarrow y(t)=\alpha e^{Kt}\qquad\alpha\in\mathbb R$ dove ammettendo anche $\alpha=0$ abbiamo ammesso anche la soluzione costante $y\equiv 0$

Se abbiamo il problema di Cauchy
	$\cases{y'=Ky\\y(0)=1}$
dobbiamo risolvere $1=y(0)=\alpha e^{K0}\Rightarrow \alpha=1\Rightarrow y(t)=e^{Kt}$ è soluzione del problema di Cauchy su $\mathbb R$. Per il THM è unica $\left(h\in \mathcal C^1(\mathbb R)\right)$

3) $y'=2(1-y)y$ dinamica popolazione $P_0=2, K=1$

$g(t)=2$
$h(y)=(1-y)y$
$h(y)=0\iff y=0\text{ o }y=1$
$y\equiv0,\ y\equiv1\text{ soluzioni costanti}$
Supponiamo $y\ne0,1$

$\frac{1}{y(1-y)}y'=2\iff \ln|y|-\ln|1-y|=2t+c\iff\ln(\left|\frac{y}{1-y}\right|)=2t+c\iff\left|\frac{y}{1-y}\right|=e^ce^{2t}\iff\frac{y}{1-y}=\pm e^ce^{2t}\iff\frac{y}{1-y}=\alpha e^{2t}\qquad\alpha\in\mathbb R_{\ne0}$
$\iff y=\alpha e^{2t}(1-y)\qquad(y\ne1)$
$\iff(1+\alpha e^{2t})y=\alpha e^{2t}\iff y=\frac{\alpha e^{2t}}{1+\alpha e^{2t}}$

Ammettiamo $\alpha=0$ così includiamo la soluzione costante $y\equiv0$ (ma non $y\equiv1$)
Quindi l'integrale generale è $\{y\equiv 1\}\cup\{y=\frac{\alpha e^{2t}}{1+\alpha e^{2t}}|\alpha\in\mathbb R\}$

Problema di Cauchy
$\cases{y'=2y(1-y)\\y(0)=2}$

$2=y(0)=\frac{\alpha e^{2\cdot0}}{1+\alpha e{^2\cdot 0}}\Rightarrow 2=\frac{\alpha}{1+\alpha}\Rightarrow 2+2\alpha=\alpha\Rightarrow \alpha=-2\Rightarrow\text{ La soluzione è }y(t)=\frac{-2e^{2t}}{1-2e^{2t}}$
Questa funzione è definita per $1-2e^{2t}\ne0\iff2e^{2t}\ne1\iff e^{2t}\ne\frac12\iff 2t\ne-\ln(2)\iff t\ne-\frac12\ln 2$
Dato che $0>-\frac12\ln2$, la soluzione del problema di Cauchy è definita su $(-\frac12\ln2,\infty)$

Altro Problema di Cauchy
$\cases{y'=2y(1-y)\\y(0)=1}$
$\Rightarrow$ La soluzione è la soluzione costante $y\equiv 1$
In entrambi i case la soluzione è unica poiché $h\in\mathcal C^1(\mathbb R)$

4) $y'=2te^y$
$g(t)=2t,\quad h(y)=e^y$
$h\ne0\Rightarrow$ no soluzioni costanti
$\frac{y'}{e^y}=2t\iff e^{-y}y'=2t$
$-e^{-y}=t^2-c\iff e^{-y}=c-t^2$

$-y=\ln(c-t^2)\iff y=-\ln(c-t^2)$
Il dominio é non vuoto $\iff c>0$ (In tal caso il dominio è $-\sqrt c,\sqrt c$)
Integrale generale è $-\ln(\underset{c>0}{c-t^2})$

Problema di Cauchy
$\cases{y'=2te^y\\y(0)=0}$
Risolvere e dire se la soluzione è unica

5) $\cases{y'=\sqrt[3]{y}\\y(0)=0}$
$\left(\array{g(t)=1\\h(y)=\sqrt[3]y}\text{ entrambe }\mathcal C\in\mathbb R\right)$
$h(y)=0\iff\sqrt[3]{y}=0\iff y=0$
Quindi $y\equiv0$ è soluzione costante che risolve anche la condizione iniziale $y(0)=0$
Abbiamo che $y_0=0$ e $h$ non è di classe $\mathcal C^1\leftarrow\text{derivabile con derivata continua}$
$(\sqrt[3]{y}\text{ non è derivabile in }0)$, quindi il teorema non ci garantisce l'unicità della soluzione
Proviamo a trovarne altre

Se $y\ne0$ abbiamo $\frac{y'}{\sqrt y}=1\iff\frac{y'}{y^{\frac13}}=1\iff\int\frac{1}{y^{\frac13}}dy=\int1dt\iff \frac32y^{\frac23}=t+c\iff y^{\frac23}y+c\iff y^2=\left(\frac23t+c\right)^3\iff y=\sqrt{(\frac23t+c)}\text{ per }t>\frac32$
Notiamo che, prendendo $c=0,\ y(t)=\sqrt{t^3}$ è derivabile da destra in $t=0$, con derivata 0
Quindi definendo $\overset \sim y(t)=\begin{cases}0&t\le0\\\sqrt{t^3}&t\ge0\end{cases}$
Abbiamo che $\overset\sim y$ è derivabile in $0$ (e su $\mathbb R$) e soddisfa l'equazione differenziale e anche la condizione iniziale
$\overset{\sim}{y}(0)=0$
Si possono definire anche altre soluzioni ponendo $y_0(t)=\begin{cases}0&t\le-\frac32c\\\sqrt{(\frac23t+c)^3}&t\ge-\frac32c\end{cases}$ che soddisfa la condizione iniziale se
In ogni intorno di $0$ possiamo definire $\infty$ soluzioni diverse

# Equazioni differenziali lineari
$y^{(n)}=a_{n-1}(t)y^{(n-1)}+\ldots+a_1(t)y'+a_0(t)y+b(t)$ (in forma parziale di ordine $n$) (è omogeneo se $b\equiv 0$) ($a,b$ continue)
## Ordine $n=1$
A) Omogenea
	$y'=a(t)y$
	È a variabili separabili $\left(g(t)=a(t),h(y)=y\right)$
	Quindi ha la soluzione costante $y\equiv0\quad(\iff h(y)=0)$
	per $y\ne0\quad\frac{y'}{y}=a(t)\iff\ln|y|=A(t)+c\ (\text{con }A\text{ primitiva di }a)\iff|y|=e^{A(t)+c}\iff y=\pm e^ce^{A(t)}\iff y=\alpha e^{A(t)},\alpha\ne0$
	Quindi, includendo anche la soluzione costante, abbiamo che l'integrale generale di $y'=a(t)y$ è $y=\alpha e^{A(t)},\ \alpha\in\mathbb R$ con $A$ è primitiva di $a$
B) Non omogenea $y'=a(t)y+b(t)$
	L'integrale generale è $y(t)=e^{A(t)}(K(t)+\alpha),^{(\alpha\in\mathbb R)}$ dove $\begin{array}{l}A&\text{è primitiva di}&a\\K&\text{è primitiva di}&e^{-A}b\end{array}$
	Verifichiamolo: $y'=\frac d{dt}(e^{A(t)})(K(t)+\alpha)+e^{A(t)}K'(t)=A'(t)e^{A(t)}(K(t)+\alpha)+\cancel{e^{A(t)}}\cancel{e^{-A(t)}}b(t)=ae^{A(t)}(K(t)+\alpha)+b(t)=a(t)y+b(t),\text{ come volevasi}$
$y'=a(t)y+b(t)$

### Esempio
$\left.\cases{y'=-\sin(t)y+\sin(t)\\y(0)=3}\right|\ \begin{array}{l}a(t)=-\sin(t)\\b(t)=\sin(t)\end{array}$
$A(t)=\cos(t)$
$K(t)$ è primitiva di $e^{-A}b=e^{-cos(t)}sin(t)$
Quindi $K(t)=e^{-cos(t)}\Rightarrow y(t)=e^{\cos(t)}\left(e^{-\cos(t)}+\alpha\right)=1+\alpha e^{\cos(t)},\ \alpha\in\mathbb R$
Ponendo $y(0)=3$ otteniamo $1+\alpha e^{\cos 0}=3\iff 1+\alpha e^1=3\iff \alpha=\frac2 e$
Quindi la soluzione del problema di Cauchy è $y=1+2e^{cos(t)}e^{-1}=1+2e^{cos(t)-1}$

## Ordine $n=2$

C'è un errore da qualche parte, la formula sarebbe $y_P=t^\mu(R_n e^{\alpha t}\cos(\beta t)+S_M e^{\alpha t}\sin(\beta t))\Rightarrow y_P=t^\mu e^{\alpha t} (R_n\cos(\beta t)+S_M \sin(\beta t))$

$y''+a(t)y'+b(t)y=f(t)$
Considereremo il caso $a$ a coefficienti costanti ossia $y''+ay'+by=f(t),\ a,b\in\mathbb R$
A) Omogenea
	$y''+ay'+by=0$
Abbiamo $3$ casi a seconda del segno
$\Delta=a^4-4b$ che è il discriminante di $\mathcal P(\lambda)=\lambda^2+a\lambda+b$
Infatti, se $\overset\sim\lambda$ è soluzione di $\mathcal P(\lambda)=0$, allora $e^{\overset\sim\lambda t}$ è soluzione dell'equazione differenziale
Infatti $y'=\overset\sim\lambda e^{\overset\sim\lambda t},\ y''=(\overset\sim\lambda)^2e^{\overset\sim\lambda t}\Rightarrow y''+ay'+by=(\overset\sim\lambda)^2e^{\overset\sim\lambda t}+a\overset\sim\lambda e^{\overset\sim\lambda t}+b e{\overset\sim\lambda t}=\mathcal P(\overset\sim\lambda)e^{\overset\sim\lambda t}=0$ perché $\lambda$ è radice di $\mathcal P$
$\Delta>0$
	$\mathcal P(\lambda)$ ha due radici reali $\lambda_\pm=\frac{-a\pm\sqrt\delta}2$
L'integrale generale è $y=c_1 e^{\lambda_1 t}+c_2 e^{\lambda_2 t}\quad c_1,\ c_2\in\mathbb R$
$\Delta<0$
	$\mathcal P(\lambda)$ ha due soluzioni complesse coniugate $\lambda_\pm=\alpha\pm i\beta\quad\alpha,\beta\in\mathbb R$
	Come prima $e^{\lambda_\pm t}$ è soluzione dell'equazione differenziale, ma è più comodo usare come "soluzione fondamentali" $\begin{array}{l}\Re\left(e^{\lambda_\pm t}\right)&\mskip{-15mu}=&\mskip{-15mu}e^{\alpha t}\cos(\beta t)\\\Im\left(e^{\lambda_\pm t}\right)&\mskip{-15mu}=&\mskip{-15mu}e^{\alpha t}\sin(\beta t)\end{array}$
L'integrale generale è quindi $y(t)=c_1 e^{\alpha t}\cos(\beta t)c_2 e^{\alpha t}\sin(\beta t)$
$\Delta = 0$
	Abbiamo un'unica soluzione (doppia) $\overset\sim\lambda$ di $\mathcal P(\lambda)=0$
	Quindi sicuramente $y=e^{\overset\sim\lambda t}$ è soluzione
	Dobbiamo trovarne un'altra (indipendente)
	Dato che $\mathcal P'(\overset\sim\lambda)=0$ (poiché $\overset\sim\lambda$ è soluzione doppia)
	Si verifica come prima che anche $y=t e^{\overset\sim\lambda t}$ è soluzione dell'equazione differenziale
Quindi l'integrale generale è $y=c_1 e^{\overset\sim\lambda t} + c_2 t\ e^{\overset\sim\lambda t}\quad c_1,\ c_2\in\mathbb R$

B) Non omogenea
	$y''+ay'+by=f(t)$
	Le soluzioni sono della forma $y=y_{\text{OM}}+y_P$ dove $y_{\text{OM}}$ è l'integrale generale dell'omogenea associata (ossia $y''+ay'+by=0$) e $y_P$ è una soluzione qualsiasi ('' particolare) di $y''+ay'+by=f(t)$
	Per trovare $y_P$ si può usare il metodo di somiglianza
		- Se $f(t)=Q_n(t) e^{\alpha t}$ con $Q_n$ polinomio di grado $\alpha$
			La soluzione $y_P$ si cerca tra le funzioni del tipo $y_P(t)=t^\mu\cdot R_n(t) e^{\alpha t}$ con $R_n$ polinomio generico di grado $n$ e $\mu$ è l'ordine di $\alpha$ come soluzione di $\mathcal P(\lambda)=\lambda^2+a\lambda+b$
				Ossia $\mu=0$ se $\alpha$ non è soluzione di $\mathcal P(\lambda)$, $\mu=1$ se $\alpha$ è soluzione semplice, $\mu=2$ se $\alpha$ è soluzione doppia
		- Se $f(t)=Q_n e^{\alpha t}\cos(\beta t)$
			($Q_n$ come sopra), allora $y_P$ va cercata del tipo $y_P=t^\mu R_n(t) e^{\alpha t}\cos(\beta t)$ con $R_n$ come sopra e $\mu=0$ se$\alpha+i\beta$ non è soluzione di $\mathcal (\lambda)$ e $\mu=1$ se lo è ($a,b\ \Re$)
		- Se $f$ è somma di funzioni di questi tipi $y_P$ si ottiene sommando le corrispondenti soluzioni particolari

### Esempio
$\cases{y''+y=t^2+\cos t\\y(0)=0\\y'(0)=0}\leftarrow(2\text{ condizioni iniziali perché di secondo ordine})$
Omogenea associata $y''+y=0\Rightarrow \mathcal P(\lambda)=\lambda^2+1=(\lambda+i)(\lambda-i)\Rightarrow$ Le radici di $\mathcal P(\lambda)$ sono $0\pm i\cdot 1\quad(\Delta=-4<0)$
$y_\text{OM}(t)=c_1 e^{0t}\cos(1\cdot t)+c_2 e^{0t}\sin(1\cdot t)=c_1\cos(t)+c_s\sin(t)$
Risolviamo $\array{1)&y''+y=t^2\\2)&y''+y=\cos(t)}$
1) $t^2$ è della forma $Q_2 e^{\alpha t}$ con $Q_2=t^2,\ \alpha=0$
	$\alpha=0$ non risolve $P(\lambda)=0\quad(P(0)=1\ne0)\Rightarrow\mu=0$
	Quindi cerco la soluzione $y_1$ della forma $y(t)=\cancel{t^\mu} R_1(t) \cancel{e^{\alpha t}}=(At^2+Bt+B)$ con $A,B,C\in\mathbb R$
	La inserisco in $y''+y=t^2$ e vedo quando la soddisfa
		$y'=2At+b,\ y''=2A$
		1) $\iff 2A+At^2+Bt+c=t^2\iff At^2+Bt+(2A+c)=1t^2+0t+0\iff\cases{a=1\\b=0\\2A+C=0}\Rightarrow\cases{A=1\\B=0\\C=-2}\Rightarrow y_1(t)=t^2-2$
2) $\cos(t)$ è della forma $Q_0e^{\alpha t}$ con $Q_0=1,\ \array{\alpha=0\\\beta=1}$
	$\alpha+i\beta=i$ è soluzione di $\mathcal P(\lambda)=0\ (\Rightarrow\mu=1)$
	Quindi $y_2$ va cercato della forma $y_2=t^\mu \cancel{e^{\alpha t}} (R_0\cos(\beta t)+S_0 \sin(\beta t))=t(A\cos(t)+B\sin(t))\quad A,B\in\mathbb R$
	Inseriamo in $y''+y=\cos(t)$
	$y'=A\cos (t)+B\sin(t)+t(-A\sin (t)+B\cos(t))=(A+tB)\cos(t)+(B-tA)\sin(t)$
	$y''=B\cos(t)-(A+tB)\sin(t)-A\sin(t)+(B-tA)\cos(t)=(2B-tA)\cos(t)-(2A+tb)\sin(t)$
	$\boxed{2}\iff(2B-\cancel{tA})\cos(t)-(2A+\cancel{tB})\sin(t)+t(\cancel{A\cos(t)}+\cancel{B\sin(t)})=\cos(t)\iff 2B\cos(t)-2A\sin(t)=1\cos(t)+0\sin(t)$
	$\cases{2B=1\\-2A=0}\iff\cases{B=\frac12\\A=0}$
	$\Rightarrow y_2=\frac t2\sin(t)$
	Quindi $y_P=y_1+y_2=t^2-2+\frac t2\sin(t)\Rightarrow$ L'integrale generale di $y''+y=t^2+\cos(t)$ è $t^2-2+\frac t2\sin(t)+\overbrace{c_1\cos(t)+c_2\sin(t)}^{y_\text{OM}}$
	$y'=2t+\frac12\sin t+\frac t2\cos t-c_2\sin t+c_2\cos t\Rightarrow y'(0)=c_2$ e $y(0)=-2+c_2$
	Quindi per trovare la soluzione del problema di Cauchy pongo $y(0)=0, y'(0)=0\iff\cases{-2+c_1=0\\c_2=0}\iff\cases{c_1=2\\c_2=0}$



$\cases{y''+y'=-g\\y(0)=y'(0)=0}\quad(\text{caduta libera con attrito }m=1,K=1)$
Ordine $n\ge2$
Ci si riconduce a sistemi di equazioni differenziali
$y^{(n)}+a_{n-1}y^{(n-1)}+\ldots+a_0y\overset{\boxed\star}{=}f(t)$
Poniamo $y_1=y,\ y_2=y'\ (\Rightarrow y_2={y_1}'),\ y_3=y''\ (\Rightarrow y_3={y_2}'),\ldots$
$y_n=y^{(n-1)}\ (\Rightarrow y_n={y_{n-1}}')$
$\boxed\star$ si può riscrivere con il sistema
$\left.\cases{{y_1}'=y_2\\{y_2}'=y_3\\\vdots\\{y_{n-1}}'=y_n\\y_n'+a_{n-1}y_{n-1}+\ldots+y_1=f(t)}\ \right|\ \begin{array}{l}\text{Sistema di }n\\\text{equazioni differenziali}\\\text{in }n\text{ funzioni}\\\text{incognite}\end{array}$
In modo più compatto si scrive come $\underline{y}'=\underline f(t,\underline y)$ dove $\array{\underline y:\mathbb R\to\mathbb R\\\underline y={\small{\pmatrix{y_1\\\vdots\\y_n}}}}$
$\underline f(t,\underline y)=\pmatrix{f_1(t,y)\\\vdots\\f_n(t,y)}=\pmatrix{y_1\\\vdots\\v_n\\-a_{n-1}y_{n-1}-\ldots-a_1y_1+f(t)}$
$\underline f:\underbrace{I}_{\operatorname{Dom}(f{\small{(t)}})}\times\mathbb R^n\to\mathbb R^n$

## Sistemi di equazione differenziale del primo ordine e in forma normale
$\cases{y_1'=f_1(y_1,\ldots,y_{n_1}t)\\\vdots\\y_n'=f_n(y_1,\ldots,y_{n_1}t)}\iff\array{\underline y'=\underline f(\underline y,t)\\\underline y=\pmatrix{y_1\\\vdots\\y_n}, \underline f=\pmatrix{y_1\\\vdots\\y_n}}$
$\underline f:D\times I\to\mathbb R^n\qquad D\subseteq\mathbb R^n$

### Teorema (Problema di Cauchy per sistemi)
Sia $I$ intervallo aperto, $D\subseteq \mathbb R^n$ aperto e sia $\underline f\in\mathcal C(D\times I)$
Allora $\forall\  t_0\in I,\ \forall\ \underline{y_0}\in D$ esiste $J\subseteq I$ aperto con $t_0\in J$, tale che il problema di Cauchy $\cases{\underline y'=\underline f(\underline y,t)\\\underline y(t)=\underline{y_0}}$ ammetta una soluzione $\underline y:J\to\mathbb R^n$
Inoltre, se $\underline f\in\mathcal C'(D\times I)$ allora la soluzione è unica
Inoltre, se vale una tra le seguenti condizioni:
1) $D=\mathbb R^n,\ \underset{\array{t\in I\\\underline y\in D}}\sup\left|\frac{\partial f_i}{\partial y_j}(\underline y,t)\right|<\infty\ \forall\ i,\forall\ j\in\{1,\ldots,n\}$
2) $F=\mathbb R^n$ e
	i) $\frac{\partial f_i}{\partial y_j}\in\mathcal(I\times\mathbb R^n)$
	ii) $\text{esistono }\alpha,\beta\in\mathcal C(I)\text{ non negative, tali che }\Vert f(\underline y,t)\Vert<\alpha(t)\Vert\underline y\Vert+\beta(t)\ \ \array{\forall\ y\in D\\\forall\ t\in I}$
allora esiste una **soluzione globale** al problema di Cauchy, ossia la soluzione è unica
#### Esempi
1) $\begin{cases}y'=t^2\sin(y)+e^t y\\y(t_0)=y_0\end{cases}\qquad\small\pmatrix{D=\mathbb R\\I=\mathbb R}$
$f(y,t)=t^2\sin(y)+e^t y$
È di classe $\mathcal C'$ \[quindi vale $2)\ i)$] e si ha $\left|f(y,t)\right|\le|t^2||\sin y|+|e^t||y|\le|t^2|+e^t|y|=\alpha(t)|y|+\beta(t)\quad\text{con }\alpha(t)=e^t,\ \beta(t)=t^2$
Quindi vale anche $2)\ ii)$
Quindi il problema di Cauchy ammette una soluzione globale $y:\mathbb R\to\mathbb R$

2) $\cases{y'=y^2\\y(0)=1}$
$f(y,t)=y^2$
È di classe $\mathcal C'$ \[quindi vale $2)\ i)$] mentre $2)\ ii)$ non vale ($y$ ha grado $2$)
Quindi il Teorema non ci da l'esistenza di una soluzione globale $y:\mathbb R\to\mathbb R$ (ma ci dà come al solito l'esistenza e l'unicità di una soluzione locale)
Risolvendo l'equazione (è a variabili separabili) otteniamo la soluzione $y(t)=\frac1{1-t}$ con dominio $(-\infty, 1)$, quindi la soluzione non è definita globalmente (ossia su $I$)

# Sistemi lineari
$\underline y'=A(t)\underline y\qquad\text{con }A(t)\in M_{n\times n}$
$\text{con }A(t)=\left(a_{i,j}(t)\right)_{i,j}\qquad\text{con }a_{i, j}\in\mathcal(I)$
$I$ intervallo aperto, $\underline b:I\to\mathbb R^n$ continua 

#### Corollario
Siano $A,\underline b$ come sopra
Sia $t_0]in I,\ y_0\in\mathbb R^n$
Allora il problema di Cauchy $\cases{\underline y'=A(t)\underline y+b(t)\\\underline y(t_0)=y_0}$ ammette un'unica soluzione globale su $I$
##### Dimostrazione
Posto $f(\underline y,t)=A(t)\underline y+b(t)$ abbiamo $\frac{\partial f_i}{\partial y_j}(y,t)=a_{i,j}(t)\in\mathcal C(I)$
Quindi $2)\ i)$ è verificata

Dato $K\in M_{n\times n}$ la sua norma è $\Vert K\Vert=\underset{\underline x\in\mathbb R^n}{\max}\frac{\Vert K\cdot\underline x\Vert}{\Vert\underline x\Vert}<\infty\leftarrow(\text{norma matriciale})$
Dalla definizione segue che $\Vert K\cdot\underline x\Vert\le\Vert K\Vert\ \Vert\underline x\Vert$

Quindi $\Vert f(\underline y,t)\Vert\le\Vert A(t)\underline y\Vert+\Vert\underline b(t)\Vert\le\Vert A(t)\Vert\Vert\underline y\Vert+\Vert \underline b(t)\Vert=\alpha(t)\Vert\underline y\Vert+\beta (t)$ con $\alpha(t)=\Vert A(t)\Vert,\ \beta(t)=\Vert\underline b(t)\Vert$
Quindi $2)\ ii)$ è verificato e possiamo concludere invocando il teorema

###### Nota
Se $\underline y_1$ risolve $\underline {y}'=A\underline y+b_1$ e $\underline y_2$ risolve $y''=A\underline y+b_2$, allora $y_1+y_2$ risolve $\underline y'=A \underline y+b_1+b_2$
In particolare lo spazio delle soluzioni di un sistema omogeneo (ossia $b\equiv 0$) è uno spazio vettoriale (mentre la soluzione di $y'=A\underline y+\underline b$ si scrivono come $y_{OM}+y_P$)
Si dimostra che tale spazio vettoriale ha dimensione $n\leftarrow\text{numero di equazioni}$
In altre parole esistono $n$ soluzioni linearmente indipendenti $\underline\varphi_1,\ldots,\underline\varphi_n$ che soddisfano l'equazione differenziale
$\underline\varphi_1,\ldots,\underline\varphi_n$ formano una base delle soluzioni, quindi tutte le soluzioni si possono scrivere come $y(t)=c_1\underline\varphi_1(t)+\ldots+c_n\underline\varphi_n(t)$ con $c_1,\ldots,c_n\in]mathbb R$
Più brevemente si scrivono come $y(t)=W(t)\underline c$ con $\underline c\in\mathbb R^n$ e $W(t)=\Big(\varphi_1,\ldots,\varphi_n\Big)\leftarrow(\text{matrice fondamentale per il sistema }\underline y'=A\underline y)$
Il problema di Cauchy $\cases{\underline y'=A\underline y\\\underline y(t_0)=\underline y_0}\begin{array}{l}\iff y=W\cdot\underline c\\&\end{array}$
deve avere soluzione $\underline y=W(t)\cdot\underline c$ per qualche $\underline c\in\mathbb R^n\Rightarrow \underline y(t_0)=y_0\Rightarrow W(t_0)\cdot\underline c=y_0\Rightarrow E(t)^{-1}\underline y_0$ ossia la soluzione del problema di Cauchy è $\underline y=W(t)W(t_0)^{-1}y_0$
###### Nota
$W(t)$ è sempre invertibile (equivalentemente $\operatorname{det}(W)\ne0$)

###### Nota
Una volta nota $W(t)$, la matrice fondamentale del sistema omogeneo, la soluzione particolare del sistema non omogeneo $\underline y'=A\underline y+\underline b$ si trova usando il metodo di variazioni delle costanti

## Sistemi lineari omogenei con matrice costante
$\underline y'=A\cdot\underline y$ con $A\in M_{n\times n}$ costante
Se $\underline v$ è autovettore di $A$ con autovalore $\lambda\in\mathbb C$ (ossia $A\underline v=\lambda\underline v$), allora $\underline y=\underline v e^{\lambda t}$ è soluzione dell'equazione differenziale
Infatti $\underline y'=\frac{d}{dt}\underline v e^{\lambda t}=\underbrace{\lambda \underline v}_{=A\underline v}e^{\lambda t}=A\underline v e^{\lambda t}=A\underline y$
###### Nota
Se $A$ è matrice reale e $\lambda$ è autovalore $\notin\mathbb R$ con autovettore $\underline v$, allora anche $\overline\lambda$ è autovalore con autovettore $\overline{\underline v}$
Le soluzioni $\underline v e^{\lambda t}$ e $\overline{\underline v}e^{\lambda t}$ si possono rimpiazzare le soluzioni reali $\Re(\underline v e^{\lambda t}),\ \Im(\underline v e^{\lambda t})$ (ossia se $\underline v=\underline u+i\underline w,\ \lambda=\alpha+i\beta$ si può usare $\underline u e^{\lambda t}\cos(\beta t)-\underline u e^{\lambda t}\sin (\beta t)$ e $\underline u e^{\alpha t}\sin(\beta t)+\underline w e^{\alpha t}\cos(\beta t)$)

###### Nota
Gli autovalori di $A$ si trovano risolvendo $P(\lambda)=\operatorname{det}(A-\lambda I)$

Le radici di $P(\lambda)$ sono gli autovalori e data una radice $\lambda$ si pone

$\begin{array}{l}m_\lambda=\text{molteplicità algebrica di }\lambda\text{ come radice di }P\\\mu_\lambda=\text{molteplicità geometrica di }\lambda\text{, ossia la dimensione dello spazio di autovettori con autovalore }\lambda\end{array}$

###### Nota
Se $m_\lambda=1$, l'autovalore è automaticamente regolare

Una matrice è diagonalizzabile se e solo se tutti gli autovalori sono regolari


# Soluzioni del sistema lineare associate all'autovalore λ
Ogni autovalore $\lambda$ produce $m_\lambda$ soluzioni linearmente indipendenti
Come visto, per ogni autovettore $\underline v$ associato a $\lambda,\ \underline v e^{\lambda t}$ è soluzione
Questo produce $\mu_\lambda$ soluzioni linearmente indipendenti
In particolare, se $\lambda$ è regolare ($\mu_\lambda=m_\lambda$) abbiamo trovato tutte le soluzioni cercate
Se $\lambda$ non è regolare abbiamo $\mu_\lambda$ soluzioni associate agli autovettori $v_1,\ldots,v_2$ linearmente indipendenti
Per trovare gli altri procediamo come segue:
- $\boxed\star$ Prendiamo l'autovettore $v_1$
	Pongo $\underline v^{(0)}=\underline v_1$
- Risolvo in sequenza i sistemi
	$\begin{array}{l}(A-\lambda I)\underline v^{(1)}=\underline v^{(0)}\\(A-\lambda I)\underline v^{(2)}=\underline v^{(1)}\\\vdots\\(A-\lambda I)\underline v^{(J)}=\underline v^{(J-1)}\end{array}$
	finché trovo soluzioni (questi vettori $\underline v^{(0)},\ldots,\underline v^{(J)}$ sono detti autovettori generalizzati)
- Le soluzioni al sistema associate agli autovettori generalizzati sono $\begin{array}{l}w^{(1)}=(\underline v^{(1)}+t\underline  v^{(0)})e^{\lambda t}\\w^{(2)}=(\underline v^{(2)}+t\underline  v^{(1)})+\frac{t^2}{2}\underline v^{(0)})e^{\lambda t}\\\vdots\\\underline w^{(J)}=(\underline v^{(J)})+\underline v^{(J-1)}+\frac{t^2}{2!}\underline v^{(n-2)}+\ldots+\frac{t^J}{J!}\underline v^{(0)})e^{\lambda t}&=&e^{\lambda t}\sum\limits_{l=0}^j\frac{t^l\underline v^{(J-l)}}{l!}\end{array}$
- Rifaccio lo stesso caso prendendo nel primo passo $\boxed\star\ \underline v^{(0)}=\underline v_2$, poi $\underline v^{(0)}=\underline v_3,\ldots$

## Esempio
$y'''+y'=0$
Riduciamola a un'equazione del primo ordine
Pongo $y_1=y,\ y_2=y'=y_1',y_3=y_2'=y''$
$y'''+y'=0\iff y_3'+y_1=0\iff y_3'=-y_1$
$\cases{y_1'=y_2\\y_2'=y_3\\y_3'=-y_2}\iff\underline y'=\pmatrix{0&1&0\\0&0&1\\0&-1&0}\underline y\qquad \underline y=\pmatrix{y_1\\y_2\\y_3}$