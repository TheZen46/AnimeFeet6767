# Statistica · notazione comune

| Oggetto | Notazione nei moduli | Negli appunti |
|---|---|---|
| Dati di un campione | $x_1, \dots, x_n$, valori distinti $v_1 < \dots < v_m$ | $x_\ell$ con $\ell = 1, \dots, n$ |
| Frequenze assolute e relative | $n_i$, $f_i = n_i / n$ | uguale |
| Tabella a due vie | $n_{ij}$, $f_{ij}$, marginali $n_{i\cdot}$, $n_{\cdot j}$, profili $f_{j \mid i}$ | uguale |
| Media, varianza dei dati | $\bar x$, $\sigma_x^2$ (con $\frac1n$), $s_x^2$ (con $\frac{1}{n-1}$) | uguale |
| Probabilità | $P[E]$, $P[F \mid E]$ | $\mathbb{P}[E]$ |
| Evento opposto | $\bar E$ | uguale |
| Speranza, varianza, covarianza | $\mathbb{E}[X]$, $\mathrm{Var}[X]$, $\mathrm{Cov}[X, Y]$ | anche $\mathrm{VAR}$, $\mathrm{cov}$ |
| Coefficiente di correlazione | $\rho_{X,Y}$ | $\rho$, $\varsigma$ |
| Indipendenza | $X \perp Y$ | $X \perp\!\!\!\perp Y$ |
| Stessa legge | $X \sim Y$ | uguale |
| Leggi | $B(p)$, $\mathrm{Bin}(n, p)$, $\mathrm{Geo}(p)$, $\mathrm{Pascal}(k, p)$, $\mathrm{Poisson}(\lambda)$, $\mathrm{Hyper}(r, b, n)$, $U[a, b]$, $\mathcal{E}(\lambda)$, $N(\mu, \sigma^2)$ | $g(p)$ per la geometrica |
| Normale standard | $Z$, densità $\phi$, ripartizione $\Phi$ | solo $\Phi$ |
| Quantile e valore critico | $\varphi_p$ ($P[Z \le \varphi_p] = p$), $z_\alpha$ ($P[Z > z_\alpha] = \alpha$) | $\phi_p$ |
| Valori critici t e chi-quadro | $t_{\alpha, n}$, $\chi^2_{\alpha, n}$ (coda destra $\alpha$) | uguale |
| Stimatore e stima | $\hat\theta = T(X_1, \dots, X_n)$ e il suo valore sul campione osservato | $\Theta$ e $\hat\theta$ |
| Media e varianza campionaria | $\bar X$, $S^2$; sui dati $\bar x$, $s^2$ | uguale |

I numeri decimali si scrivono con la virgola ($0{,}05$). Le probabilità si danno come frazione quando il calcolo è esatto, altrimenti con tre cifre o in percentuale.

**Incoerenze trovate e uniformate.** Gli appunti usano sia $\mathbb{P}$ sia $\mathrm{P}$, sia $\Theta$ sia $\hat\theta$ per lo stimatore, e $\phi_p$ per il quantile (che si confonde con la densità): nei moduli si usa $P$, $\hat\theta$ per lo stimatore e $\varphi_p$ per il quantile. Nella statistica descrittiva la varianza "della popolazione" $\sigma^2$ ha $\frac1n$ e quella "del campione" $s^2$ ha $\frac{1}{n-1}$, come negli appunti.
