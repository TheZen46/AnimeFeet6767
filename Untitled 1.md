2 Miniere $M_1,M_2$
3 impianti di produzione $P_1,P_2,P_3$
Produzione miniere: $\array{M_1:&130\operatorname{ton}\\M_2:&200\operatorname{ton}}$
Richiesta impianti: $\array{P_1:&80\operatorname{ton}\\P_2:&100\operatorname{ton}\\P_3:&150\operatorname{ton}}$

| $\text €/\operatorname{ton}$ | $P_1$ | $P_2$ | $P_3$ |
| ---------------------------- | ----- | ----- | ----- |
| $M_1$                        | $10$  | $8$   | $21$  |
| $M_2$                        | $12$  | $20$  | $14$  |
# Variabili
$x_{mn}=\text{tonnellate inviate da miniera m ad impianto n}$

# Funzione obiettivo
$f(x_{11},\ldots,x_{23})=10x_{11}+\ldots+14x_{23}$

# Vincoli
$\begin{cases}x_{11}+x_{21}=80\\x_{12}+x_{22}=100\\x_{13}+x_{23}=150\\x_{11}+x_{12}+x_{13}=130\\x_{21}+x_{22}+x_{23}=200\end{cases}$



# Modello generale
1) Allocazione Risorse (altro esercizio)
$\max_{x_1,x_2}(7x_1+10x_2)$
$\begin{cases}x_1+x_2\le750\\x_1+2x_2\le1000\\x_2\le400\\x_1,x_2\ge0\end{cases}$

Tracciato grafico dell'insieme ammissibile
