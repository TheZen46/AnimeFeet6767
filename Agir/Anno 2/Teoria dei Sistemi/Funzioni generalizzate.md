Anche note come **distribuzioni**

$\begin{array}{l}\delta(t)\mskip{8mu}&\text{delta Dirac (impulso ordine 0)}\\\dot\delta(t)=\frac{d}{dt}\delta(t)&\text{impulso ordine 1}\\\ddot\delta(t)=\frac{d}{dt}\dot\delta(t)&\text{impulso ordine 2}\\\int_{-\infty}^t\delta(t)dt=1(t)&\text{gradino unitario (impulso ordine -1)}\\\int_{-\infty}^t1(t)dt=t1(t)&\text{rampa unitaria (impulso ordine -2)}\end{array}$
$\displaystyle\int_{-\infty}^{t}\delta(\tau)d\tau=0\mskip{8mu}\forall t<0$
$\displaystyle\int_{0^-}^{0^+}\delta(\tau)d\tau=1$
$\displaystyle\int_{t}^{+\infty}\delta(\tau)d\tau=0\mskip{8mu}\forall t>0$

$\begin{cases}0&(-\infty, -T)\cup(T,+\infty)\\\frac1{2T}&(-T,T)\end{cases}$

$\lim\limits_{T\to0}\rightarrow\begin{cases}0&t\ne0\\\infty &t=0\end{cases}\leftarrow\text{non applica}$


$\delta(t-T)$
$\begin{cases}0&t\ne T\\\infty &t=T\end{cases}$

$\delta(t) \quad \text{delta di Dirac} \\[6pt]$
$\begin{align*}&\int_{-\infty}^{t} \delta(\tau)\,d\tau = 0 \quad \forall t < 0 \\&\int_{0^-}^{0^+} \delta(\tau)\,d\tau = 1\\&\int_{t}^{+\infty} \delta(\tau)\,d\tau = 0 \quad \forall t > 0 \\[6pt]\end{align*}$
&\text{Approssimazione rettangolare (area unitaria):} \\
&p_T(t) = \begin{cases} 
\dfrac{1}{2T} & t \in (-T, T) \\[4pt]
0 & t \in (-\infty, -T) \cup (T, +\infty) 
\end{cases} \\[6pt]
&\lim_{T \to 0} p_T(t) = \delta(t) \quad \text{(nel senso delle distribuzioni)} \\[6pt]
&\delta(t - T) \implies \text{impulso centrato in } t = T

$

$f(t)\in C^{\infty}$
$\text{Proprietà di campionamento (sifting):}$
$\int_{-\infty}^{+\infty} f(\tau)\delta(\tau - t)d\tau = f(t)$
$f(t)\delta(t-T)=\begin{cases}f(T)\delta(t-T)&f(T)\ne0\\0&f(T)=0\end{cases}\mskip{12mu}\leftarrow\text{valido solo per }\delta_0$

(permette di prelevare solo in $T$, quindi ottieni $f(T)$)

$\displaystyle\int_{-\infty}^t\delta(\tau)d\tau=\begin{cases}0&t<0\\1&t\ge0\end{cases}=1(t)$
Gradino unitario

$\displaystyle\int_{-\infty}^t 1(\tau)d\tau=\begin{cases}0&t<0\\t&t\ge0\end{cases}=t1(t)$
Rampa unitaria


$\displaystyle\frac{d}{dt}(fg)=\dot f g+f\dot g\leftarrow\text{anche se }g\text{ non derivabile}$
$\displaystyle\frac{d}{dt}\underbrace{f(t)\delta(t)}_{f(0)\delta(t)}=\dot f(t)\delta(t)+f(t)\dot\delta(t)=f(0)\delta(t)$


$1(t-T_1)-1(t-T_2)=\begin{cases}0&(-\infty,T_1)\cup(T_2,+\infty)\\1&(T_1,T_2)\end{cases}\leftarrow\text{gate pulse}\mskip{60mu}f(t)\big(1(t-T_1)-1(t-T_2)\big)=\begin{cases}0&(-\infty,T_1)\cup(T_2,+\infty)\\f(t)&(T_1,T_2)\end{cases}$


Funzione con $cos(x)$ da $0$ a $\frac\pi 2$, e una retta con coefficiente $\frac{1}{4-\pi}$ da $\pi$ a $4$
$\displaystyle f(t)=cos(t)\left[1(t)-1(t-\frac\pi2)\right]+\frac{1}{4-\pi}\left[1(t-\pi)-1(t-4)\right]$

$\displaystyle\dot f(t)=-\sin(t)\left[1(t)-1(t-\frac\pi2)\right]+\cos(t)\left[\delta(t)-\delta(t-\frac\pi2)\right]+\frac{1}{4-\pi}\left[1(t)-1(t-\frac\pi2)\right]+\frac{1}{4-\pi}(t-\pi)\left[\delta(t)-\delta(t-\frac\pi2)\right]=-\sin(t)\left[1(t)-1(t-\frac\pi2)\right]+\delta(t)+\frac{1}{4-\pi}\left[1(t)-1(t-\frac\pi2)\right]-\frac{1}{\cancel{4-\pi}}\cancel{4-\pi}\delta(t-4)$