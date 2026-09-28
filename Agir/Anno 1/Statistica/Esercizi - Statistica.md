1)
Una ditta produce tondali di ferro con lunghezza nominale $1.72m$.
Viene scelto un campione di $8$ tondini e si misura le rispettive lunghezze $x_1,\ldots,x_8$
- media empirica $\overline x=172.25cm$
- deviazione standard campionaria $S=7.924cm$
Supponendo che la lunghezza dei tondini sia descritta da una legge normale verificare l'ipotesi che
- media $\mu$ su $172cm$
- livello di significatività $20\%,\ 10\%$ e $2\%$
$X=\text{lunghezza tondino}\sim N(\mu,\sigma^2)\quad\begin{array}{l}\mu=\text{media}=\mathbb E[x]\\\sigma^2=\text{varianza}=\operatorname{var}[x]\end{array}$

$X_1,\ldots,X_n\sim X\sim N(\mu,\sigma^2)$
$\begin{array}{l}H_0&\mu=\mu_0&\mu_0&172\\H_1&\mu\neq\mu_0\end{array}$

\[Bell curve with $\mu-\sigma\to\mu+\sigma$, area $68\%$]

$\begin{array}{l}x_1=\\\vdots\\x_8=\end{array}\qquad\overline x-\frac{x_1+\ldots+x_n}n=177.25cm\qquad s^2=\frac{(x_1-\overline x)^2+\ldots+(x_n+\overline x)^2}{n-1}=(7.924)^2 cm^2$

Varianza ignota t-student

$\displaystyle\hat t=\frac{\overline x-\mu_0}{\sqrt\frac{s^2}{n}}$

Accettiamo $H_0$
$\left\vert\hat t\right\vert\le t_{n-1,\frac\alpha2}$

$\displaystyle\frac{\overline x-\mu_0}{\frac{s}{\sqrt n}}\Rightarrow\frac{177.25-172}{\frac{7.924}{\sqrt8}}\simeq1.874\Longrightarrow \left\vert\hat t\right\vert=1.874$

| $\alpha$ | $\frac\alpha2$ | $t_{7,\frac\alpha2}$ |         |
| -------- | -------------- | -------------------- | ------- |
| $20\%$   | $0.10$         | $1.415$              | Rifiuto |
| $10\%$   | $0.05$         | $1.895$              | Accetto |
| $2\%$    | $0.01$         | $2.998$              | Accetto |
Accetto $H_0\quad\mu=172$ a livello di significatività del $10\%$ e del $2\%$
Rifiuto $H_0$ cioè accetto $\mu\ne172$ a livello di significatività del $20\%$



$X_1,\ldots,X_n\sim N(\mu,\sigma^2)\qquad \sigma_0=7cm$
$\displaystyle\hat Z=\frac{\overline x-\mu_0}{\frac{\sigma_0}{\sqrt n}}\simeq2.12$
| $\alpha$ | $\frac\alpha2$ | $t_{7,\frac\alpha2}$ |         |
| -------- | -------------- | -------------------- | ------- |
| $20\%$   | $0.10$         | $1.282$              | Rifiuto |
| $10\%$   | $0.05$         | $1.645$              | Rifiuto |
| $2\%$    | $0.01$         | $2.326$              | Accetto |



$\displaystyle\left\vert\frac{\frac{x_1+\ldots+x_n}n -\mu_0}{\sqrt{\frac{\sigma_0^2}n}}\right\vert\le Z_\frac\alpha2\qquad H_0\text{ sia vera}$
$\displaystyle\underbrace{\mu_0-Z_\frac\alpha2\frac{\sigma_0}{\sqrt n}}_{166cm}\le\underbrace{\frac{x_1+\ldots+x_n}{n}}_{\overline x=172}\le\underbrace{\mu_0+Z_\frac\alpha2\frac{\sigma_0}{\sqrt n}}_{178cm}$
$\alpha=2\%\qquad Z_\frac\alpha2=Z_{0.01}\simeq 2.326$



Se $H_0$ è falsa
$X_1,\ldots,X_n\sim N(\mu,\sigma_0^2)\qquad\mu\neq\mu_0$

Probabilità errore tipo $\displaystyle II=\mathbb P\left[\left\vert\frac{\frac{x_1+\ldots+x_n}n -\mu_0}{\sqrt{\frac{\sigma_0^2}n}}\right\vert\le Z_\frac\alpha2\right]=\mathbb P\left[\mu_0-Z_\frac\alpha2\frac{\sigma_0}{\sqrt n}\le\frac{x_1+\ldots+x_n}{n}\le\mu_0+Z_\frac\alpha2\frac{\sigma_0}{\sqrt n}\right]=\boxed\star$
$\begin{array}{l}\downarrow\\&\rightarrow H_0\text{ è falso}\quad\mu\ne\mu_0\rightarrow\text{accetto }H_0\end{array}$

$\displaystyle\boxed\star=\mathbb P\left[\frac{\mu_0-\mu-Z_\frac\alpha2 \frac{\sigma_0}{\sqrt n}}{\sqrt{\frac{\sigma_0^2}{n}}}\le\underbrace{\frac{\frac{x_1+\ldots+x_n}{n}-\mu}{\sqrt{\frac{\sigma_0^2}{n}}}}_{Z\sim N(0,1)}\le\frac{\mu_0-\mu+Z_\frac\alpha2 \frac{\sigma_0}{\sqrt n}}{\sqrt{\frac{\sigma_0^2}{n}}}\right]=\mathbb P\left[\underset{Z_1}{\frac{\mu_0-\mu}{\frac{\sigma_0}{\sqrt n}}-Z_\frac\alpha2}\le Z\le \underset{Z_2}{\frac{\mu_0-\mu}{\frac{\sigma_0}{\sqrt n}}-Z_\alpha}\right]$

Probabilità errore tipo $\displaystyle II=\varphi\left(\frac{\mu_0-\mu}{\frac{\sigma_0}{\sqrt n}}+Z_\frac\alpha2\right)-\varphi\left(\frac{\mu_0-\mu}{\frac{\sigma_0}{\sqrt n}}-Z_\frac\alpha2\right)=\begin{cases}86.7&\mu=175&\mu_0=177&\sigma_0=7&\alpha=2\%\\\varphi(-\infty)-\varphi(\infty)=0&\mu\to+\infty\\\varphi(\infty)-\varphi(-\infty)=0&\mu\to-\infty\\\varphi(Z_\frac\alpha2)-\varphi(-Z_\frac\alpha2)=1-\alpha&\mu\to\mu_0\\\varphi(\infty)-\varphi(-\infty)=1-0=100\%\end{cases}$
$\displaystyle\varphi(\frac{\mu_0-\mu}{\frac{\sigma_0}{\sqrt n}})-\varphi(\frac{\mu_0-\mu}{\frac{\sigma_0}{\sqrt n}})$


2) 
Una ditta produce mozzarelle con peso nominale di $250g$
Realizzare un test per verificare l'ipotesi $H_0\qquad\mu\le\mu_0$
- livello di significatività del $10\%, 5\%$ e $1\%$
- per un campione di $49$ mozzarelle la media empirica $\overline x=255g$, deviazione standard campionaria $s=21 g$
$H_0=\mu\le\mu_0$
$H_1=\mu\ge\mu_0$

t-student $\to\text{varianza ignota}$
$\hat t=\displaystyle\frac{\overline x-\mu_0}{\frac{s}{\sqrt n}}=1.67$
Accetto $H_0\quad \hat t<t_{n-1,\alpha}$
(perché qui solo $\alpha$ e non $\frac\alpha2$? Ci interessa solo il lato superiore, non inferiore)

| $\alpha$ | $t_{48,\alpha}$ |               | $Z_\alpha$ |
| -------- | --------------- | ------------- | ---------- |
| $0.10$   | $1.299$         | Rifiuto $H_0$ | $1.28$     |
| $0.05$   | $1.677$         | Accetto $H_0$ | $1.65$     |
| $0.01$   | $2.407$         | Accetto $H_0$ | $2.3$      |

Quanto deve essere grande il campione per rifiutare $H_0$ al $1\%$ di significatività?

$\displaystyle\frac{\hat t-\mu_0}{\frac{s}{\sqrt m}}>t_{n-1,\alpha}\sim Z_\alpha\qquad (\overline x=s\text{ non cambiano})$
$\displaystyle\sqrt m>\frac{Z_\alpha s}{\hat t-\mu_0}\qquad m>(\frac{Z_\alpha s}{\hat t-\mu_0})^2\simeq 93.3$

$m=100$
$\frac{\overline x-\mu_0}{\frac{s}{\sqrt m}}\simeq 2.381\overset?>\underbrace{t_{99,0.01}}_{t_{n-1,\alpha}}\simeq 2.365\quad H_0\text{ vera}\rightarrow$ Rifiutiamo $H_0$ al $1\%$ di significatività