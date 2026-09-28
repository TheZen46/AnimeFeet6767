1) 
Luca lancia una moneta $100$ volte ottenendo $60$ teste.
Determinare un intervallo di confidenza per la probabilità di ottenere testa a livello di confidenza del $90\%$ e del $99\%$

$\mathbb P[T]=p\in[0,1]\qquad p\text{ ignota}$
$x_1,\ldots,x_n\quad n=100$
$(\underset{\tiny T}1,\underset{\tiny C}0,0,\ldots,1)$

Modello statistico $X_1,\ldots,X_n\sim B(p)\text{ indipendenti}$
$p=\mathbb P[T]=\mathbb E[X_i]$
Stimatore non distorto (corretto)
$\displaystyle\hat p=\underbrace{\frac{x_1+\ldots+x_n}{n}}_{\tiny\array{\text{media empirica = }\\\text{frequenza relativa empirica}}}=\frac{\text{numero di teste}}{\text{numero di lanci}}=\frac mn=\frac{60}{100}=0.60$
$\begin{array}{l}I_1=[\hat p-S_1, \hat p+S_1]&S_1=Z_{\frac\alpha2}\frac{\sigma_0}{\sqrt n}&\sigma_0=\frac12&\mskip{12mu}Z_{\frac\alpha2}=\text{valore critico distribuzione normale}\\I_2=[\hat p-S_2, \hat p+S_2]&S_1=Z_{\frac\alpha2}\frac{\sqrt{\hat p(1-p)}}{\sqrt n}&\sigma^2=p(1-p)&\mskip{12mu}1-\alpha=\text{livello di confidenza}\end{array}$

$\text{Livello di confidenza: }90\%$
$1-\alpha=90\%\Rightarrow\alpha=10\%\Rightarrow\alpha=0.10\Rightarrow\frac\alpha2=0.05$
$Z_{\frac\alpha2}=Z_{0.05}=1.6449$
$n=100\qquad\hat p=0.6$
$S_1=0.082\qquad S_2=0.081$
$I_1=[0.518,0.682]$
$I_2=[0.519,0.681]$
$0.52\le p\le0.68$

$\text{Livello di confidenza: }99\%$
$1-\alpha=99\%\Rightarrow\alpha=1\%\Rightarrow\alpha=0.01\Rightarrow\frac\alpha2=0.005$
$Z_{\frac\alpha2}=Z_{0.005}\simeq 2.5758$
$n=100\qquad\hat p=0.6$
$S_1=0.129\qquad S_2=0.126$
$I_1=[0.471,0.729]$
$I_2=[0.474,0.726]$
$0.47\le p\le0.72$

Come cambia l'intervallo di confidenza a livello di confidenza del $99\%$ se il numero di teste è $90$?
$1-\alpha=99\%\Rightarrow\alpha=1\%\Rightarrow\alpha=0.01\Rightarrow\frac\alpha2=0.005$
$Z_{\frac\alpha2}=Z_{0.005}\simeq 2.5758$
$S_1=0.129\qquad S_2=0.077$
$n=100\qquad\hat p=0.9$
$I_1=[0.771, 1.029]$
$I_2=[0.823,0.977]$



Intervallo di confidenza per la media di un campione normale con media e varianza ignote
Modello statistico $X_1,\ldots,X_n\sim N(\mu,\sigma^2)\text{ indipendenti}$
$\mu=\mathbb E[X_i]\qquad\sigma^2=\operatorname{Var}[X_i]$

Legge $\underbrace{\text{chi quadro}}_{\chi^2}$ con $n$ gradi di libertà

$W_n\sim{\chi_n}^2$
Se $W_n=\underbrace{{Z_1}^2+\ldots+{Z_n}^2}_{n\text{ addendi}}$
$Z_1,\ldots,Z_n\sim N(0,1)\text{ indipendenti}$
$W_n$ ha densità $f_n(w)=\text{formula complicata}$

$\cases{\mathbb E[W_n]=n\\\operatorname{Var}[W_n]=2n\\W_n\ge0}$
$Z\sim N(0,1)$
$\mathbb P[-Z_\alpha\le Z\le Z_\alpha]=1-2\alpha$
$\mathbb P[-Z_\frac\alpha2\le Z\le Z_\frac\alpha2]=1-\alpha$
$\mathbb P[\chi_{n,1-\alpha}^2\le W_n\le\chi_{n,\alpha}^2]=1-2\alpha$
$\mathbb P[\chi_{n,1-\frac\alpha2}^2\le W_n\le\chi_{n,\frac\alpha2}^2]=1-\alpha$


Legge T-Student con $n$ gradi di libertà
$T_n\sim t_n$
Se $T_n=\frac{Z}{\sqrt{\frac{W_n}n}}$ dove $\array{Z\sim N(0,1)\\W_n\sim{\chi_n}^2\\Z\perp\!\!\!\perp W_n}$
$T_n$ ha densità $g_n(t)$

$t_n\quad t\text{ student}$
$Z\quad\text{normale}$
$t_m\quad t\text{ student}\quad m>n$

$\mathbb E[T_n]=0\quad n\ge2$
$\operatorname{Var}[T_n]=\frac{n}{n-2}\quad n\ge2$

$\mathbb P[t_{n,\frac\alpha2}\le T_n\le t_{n,\frac\alpha2}]=1-\alpha$

Teorema
$X_1,\ldots,X_n$ variabili aleatorie indipendenti e identicamente distribuite come $W(\mu,\sigma^2)$
$\overline x=\frac{x_1+\ldots+x_n}{n}$ media empirica stimatore di $\mu=\text{media}$
$S_2=\frac{(x_1-\overline x)^2+\ldots+(x_n-\overline x)^2}{n-1}$ varianza campionaria stimatore di $\sigma^2=\text{varianza}$

Allora
a) $\displaystyle\frac{\overline x-\mu}{\sqrt{\frac{S^2}n}}\sim t_{n-1}$    T-Student con $(n-1)$ gradi di libertà

b) $\displaystyle\frac{S^2}{\sqrt{\frac{\sigma^2}n}}\sim\chi_{n-1}^2$ chi quadro con $(n-1)$ gradi di libertà


Esercizio
Il numero di ore di straordinario svolte dai dipendenti di un'azienda è descritto da una legge normale.
Da un campione di $80$ dipendenti risulta che il numero medio di ore di straordinario $\overline X=24$ con una varianza campionaria di $s^2=36$
Determinare un intervallo di confidenza per la media e la varianza a livello di confidenza del $99\%$

Modello
$X_1,\ldots,X_n\sim N(\mu,\sigma^2)$
$n=80\quad x_1,\ldots,x_n\qquad \overline x=\frac{x_1+\ldots+x_n}{n}=24\qquad S^2=\frac{(x_1-\overline x)^2+\ldots+(x_n-\overline x)^2}{n-1}=36\qquad S=\sqrt{36}=6$
$\overline x=24$
$S=t_{n-1,\frac\alpha2}\frac{S}{\sqrt n}$
$1-\alpha=0.99\Rightarrow \frac\alpha2=0.005$
$t_{79,0.005}=2.639$
$22.24\le\mu\le25.76$

Varianza $\sigma^2$
$S^2=36$
$\chi^2_{n-1,1-\frac\alpha2}=\chi^2_{79,0.995}\simeq51.172$
$\chi^2_{n-1,\frac\alpha2}=\chi^2_{79,0.005}\simeq116.321$

$51<116\ \checkmark$
$\frac{36}{\frac{116}{79}}\le\sigma^2\le\frac{36}{\frac{51}{79}}\Rightarrow24.76\le\sigma^2\le56.28\Rightarrow4.96\le\sigma\le7.5$
