# Derivate e regole di derivazione
## Definizione (rapporto incrementale, derivata)
Sia $f:\text{dom}(f)\subseteq\mathbb{R}\rightarrow\mathbb{R}$ e e $x_0\in\text{dom}(f)$
Supponiamo che $f$ sia definita in un intorno $I_\gamma(x_0), \gamma>0$ di $x_0$

Si dice **rapporto incrementale** di $f$ in $x_0$ la funzione $R_{f,x_0}:\text{dom}(f)\backslash\{x_0\}\subseteq\mathbb{R}\Rightarrow\mathbb{R},x\mapsto\frac{f(x)-f(x_0)}{x-x_0}$
Si dice che $f$ è **derivabile** in $x_0$ se esiste finito $l$ limite per $x\rightarrow x_0$ di $R_{f,x_0}$

In tal caso si dice che $\frac{df}{dx}(x_0)=f'(x_0):=\lim\limits_{x\rightarrow x_0}\frac{f(x)-f(x_0)}{x-x_0}\in\mathbb{R}$ è la **derivata** (prima) di $f$ in $x_0$
## Esempio
Retta secante per $(x_0, f(x_0)),(x_1,f(x_1))$
$y=\underbrace{\frac{f(x_1)-f(x_0)}{x_1-x_0}}_{=R{f,x_0}(x_1)}(x-x_0)+f(x_0)$
Interpreto il rapporto incrementale
$R_{f,x_0}(x_1)$ come coefficiente angolare della retta secante

Nel limite $x_0\rightarrow x_1$, la retta secante tende alla retta tangente al grafico nel punto $x_0,f(x_0)$ mentre $R_{f,x_0}(x_1)$ tende alla derivata $f'(x_0)$

# Proposizione (derivabile -> continua)
Sia $f$ derivabile in $x_0\in\text{dom}(f)$
Allora $f$ è continua in $x_0$

## Dimostrazione
$\lim\limits_{x\rightarrow x_0}f(x)=\lim\limits_{x\rightarrow x_0}(f(x)-f(x_0)-f'(x_0)(x-x_0))=\lim\limits_{x\rightarrow x_0}(f(x_0)+f'(x)(x-x_0))=\lim\limits_{x\rightarrow x_0}(\overset{=0}{(x-x_0)}\frac{f(x)-f(x_0)}{x-x_0}-f'(x_0))+f(x_0)=0+f'(x_0)=f'(x_0)\ \checkmark$

## Esempi
$f$ costante $\Rightarrow R_{f,x_0}(x)=\frac{f(x)-f(x_0)}{x-x_0}=0\Rightarrow f'=0$


$\sin'(x_0)=\cos(x_0)$
$\lim\limits_{x\rightarrow x_0}\frac{\sin(x)-\sin(x_0)}{x-x_0}=\lim\limits_{h\rightarrow 0}\frac{\sin(x_0+h)-\sin{x_0}}{h}=\lim\limits_{h\rightarrow 0}\frac{\sin(x_0)\cos(h)+\cos(x_0)\sin(h)-\sin(x_0)}{h}=\sin(x_0)\lim\limits_{h\rightarrow 0}\frac{\cos(h)-1}{h}+\cos(x_0)\lim\limits_{h\rightarrow 0}\frac{\sin{h}}{h}=-\sin(x_0)\lim\limits_{h\rightarrow 0}\frac{1-\cos(h)}{h^2}h+\cos(x_0)=\cos(x_0)$
$h=x-x_0\rightarrow 0$


$\cos'(x)=-\sin(x)$


Ci sono funzioni continue che non sono derivabili, ad esempio $f(x)=|x|$ **non** è derivabile in 0
$x\rightarrow 0, \frac{|x|-|0|}{x-0}=\frac{|x|}{x}=\begin{cases}+1, x>0\\-1,x<0\end{cases}$

$(x^\alpha)'=\alpha x^{\alpha-1}$  $\alpha\in\mathbb{R}, x>0$
$\lim\limits_{h\rightarrow 0}\frac{(x+h)^\alpha-x^\alpha}{h}=x^\alpha\lim\limits_{h\rightarrow 0}\frac{(1+\frac{h}{x})^\alpha-1}{h}=x^{\alpha-1}\underbrace{\lim\limits_{h\rightarrow 0}\frac{(1+\frac{h}{x})^\alpha-1}{\frac{h}{x}}}_{y=\frac{h}{x}\rightarrow 0}=x^{\alpha-1}\underbrace{\lim\limits_{y\rightarrow 0}\frac{(1+y)^\alpha-1}{y'}}_{\alpha}$
# Teorema (algebra delle derivate)
## Regole di Leibniz
$f,g$ derivabili in $x_0$
Allora sono derivabili in $x_0$ anche $f\pm g$ e $f\cdot g$ e valgono le seguenti uguaglianze:
$(f\pm g)'(x_0)=f'(x_0)\pm y'(x_0)$
$(f\cdot g', x_0)=f'(x_0)g(x_0)+f(x_0)g'(x_0)$

### Dimostrazione
Guardiamo regole di Leibniz

$\lim\limits_{h\rightarrow 0}\frac{(f\cdot g)(x_0+h)-(f\cdot g)(x_0)}{h}=\lim\limits_{h\rightarrow 0}\frac{f(x_0+h)g(x_0+h)-f(x_0)g(x_0)}{h}=\lim\limits_{h\rightarrow 0}\frac{f(x_0+h)g(x_0+h)-f(x)g(x_0+h)+f(x_0)g(x_0+g)-f(x_0)g(x_0)}{h}=\lim\limits_{h\rightarrow 0}\overbrace{\frac{f(x_0+h)-f(x_0)}{h}}^{f'(x_0)}\overbrace{g(x_0+h)}^{g(x_0)}+\lim\limits_{h\rightarrow 0}f(x_0)\overbrace{\frac{g(x_0+h)-g(x_0)}{h}}^{g'(x_0)}=f'(x_0)g(x_0)+f(x_0)g'(x_0)$

## Corollario (derivata è lineare)
$f,g$ derivabili in $x_0$, $\alpha,\beta\in\mathbb{R}$
$(\alpha f+\beta g)'(x_0)=\alpha f'(x_0)+\beta y'(x_0)$

### Dimostrazione
$(\alpha f+\beta g)'(x_0)=(\alpha f')(x_0)+(\beta y')(x_0)$
Leibniz $\alpha'(x_0)f(x_0)+\alpha(x_0)f(x_0)+\beta'(x_0)g(x_0)+\beta(x_0)g'(x_0)=\alpha f'(x_0)+\beta g'(x_0)$

## Teorema (regola delle catene)
$f$ derivabile in $x_0$, $g$ derivabile in $f(x_0)=y_0$
Allora la funzione composta $g\circ f$ è derivabile in $x_0$ e vale $(g\circ f)'(x_0)=g'(y_0)f'(x_0)=g'(f(x_0))f'(x_0)$

### Dimostrazione
$\lim\limits_{h\rightarrow 0}\frac{(g\circ f)(x_0+h)-(g\circ f)(x_0)}{h}=\lim\limits_{h\rightarrow 0}\frac{g(f(x_0+h))-g(f(x_0))}{h}=\lim\limits_{h\rightarrow 0}\frac{g(f(x_0+h))-g(f(x_0))}{f(x_0+h)-f(x_0)}\cdot \frac{f(x_0+h)-f(x_0)}{h}=\underbrace{\lim\limits_{h\rightarrow 0}\frac{g(f(x_0+h))-g(f(x_0))}{f(x_0+h)-f(x_0)}}_{}\cdot\lim\limits_{h\rightarrow 0}\frac{f(x_0+h)-f(x_0)}{h}=\lim\limits_{y\rightarrow y_0}\frac{g(y)-g(y_0)}{y-y_0}f'(x_0)=y'(y_0)f'(x_0)$

## Corollario (derivata del quoziente)
$f,g$ derivabile in $x_0$, $y(x_0)\ne0$
Allora $\frac f g$ è derivabile in $x_0$ e vale $(\frac{f}{g})'(x_0)=\frac{f(x_0)}{g(x_0)}-\frac{f(x_0)g'(x_0)}{(g(x_0))^2}$

### Dimostrazione
$\frac f g=f\cdot \frac 1 g\overset{\text{Leibniz}}{\Rightarrow}(\frac f g)'(x)_0=\underbrace{f'(x_0)\cdot(\frac 1 g)(x_0)}_{\frac 1 {y(x_0)}}+f(x_0)+(\frac 1 g)'(x_0)$
$\frac 1 g = r\circ g$ dove $r=\mathbb{R}\backslash\{0\}\rightarrow\mathbb{R}, y\mapsto\frac 1 y\overset{\text{catena}}{\Rightarrow}(\frac 1 g)'(x_0)=r'(g(x_0))\cdot g'(x_0)=-\frac{g(x_0)}{(g(x_0))^2}$

$r(y)=y^{-1}$
$r'(y)=-1\cdot y^{-1-1}=-y^{-2}=-r(y)^2$
$(\frac f g)'(x_0)=\frac{f'(x_0)}{g(x_0)}-\frac{f(x_0)g'(x_0)}{(g(x_0))^2}$

## Teorema (derivara della funzione inversa)
Sia $f$ continua e invertibile in un interno di $x_0$
Inoltra, sia $f$ derivabile in $x_0$ con $f'(x_0)\ne0$
Allora la funzione inversa $f^{-1}$ è derivabile in $y_0=f(x_0)$ e vale $(f^{-1})(y_0)=\frac 1 {f'(x_0)}$

### Dimostrazione
$f^{-1}$  è continua in un intorno di $x_0$ (segue le ipotesi inv + cont)
$\lim\limits_{y\rightarrow y_0}\frac{f^{-1}(y)-f^{-1}(y_0)}{y-y_0}=\lim\limits_{y\rightarrow y_0}$