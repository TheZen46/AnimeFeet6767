# Lemma (integrazione per parti generalizzata)
Siano $f,g:[a,b]\to\R$ continua e di classe $C^1$ a tratti. Allora $\displaystyle \int_a^b f'(x)\ g(x)dx=f(b)\ g(b)-f(a)\ g(a)-\int_a^bf(x)\ g'(x)dx$
## Dimostrazione
$\displaystyle \int_a^b\underbrace{\bigl(fg\bigr)'(x)}_{f'(x)g(x)+f(x)g'(x)}dx=\int_a^bf'(x)\ g(x)dx+\int_a^bf(x)\ g' (x)dx$

# Lemma (Riemann)
Sia $g:{a,b}\to\R$ continua a tratti. Allora $\displaystyle \lim\limits_{\lambda\to+\infty}\int_a^b g(x)\array{\sin(\lambda x)\\\cos(\lambda x)}=0$

## Dimostrazione
Considero solo il caso di $\sin$
Mi basta dimostrare la tesi per un intervallo $\bigl[\tilde a,\tilde b\bigr]\subseteq\bigl[a,b\bigr]$ in cui $f$ è continua
Divido $\bigl[\tilde a,\tilde b\bigr]$ in $\overset{\boxed\star}{n}$ intervalli della stessa lunghezza: ( $\boxed\star\ \text{da decidere nel seguito}$ )
$\tilde a=a_0,a_1,a_2,\ldots,a_n=\tilde b$
$\displaystyle \int_\tilde a^\tilde bg(x)\sin(\lambda x)dx=\su$
