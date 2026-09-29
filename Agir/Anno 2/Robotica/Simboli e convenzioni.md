| Simbolo                       | Significato                         | Unità   |
| ----------------------------- | ----------------------------------- | ------- |
| $x, y$                        | Coordinate del punto di riferimento | $m$     |
| $\theta$                      | Orientamento del robot              | $rad$   |
| $r_L,r_R$                     | Raggi efficaci delle ruote motrici  | $m$     |
| $b$                           | Distanza efficace fra le ruote      | $m$     |
| $\varphi_L,\varphi_R$         | Angoli di rotazione delle ruote     | $rad$   |
| $\dot\varphi_L,\dot\varphi_R$ | Velocità angolare delle ruote       | $rad/s$ |
| $v$                           | Velocità longitudinale              | $m/s$   |
| $\omega=\dot\theta$           | Velocità angolare dl corpo          | $rad/s$ |
| $\delta t$                    | Periodo di campionamento            | $s$     |

Corpo rigido: 3 gradi di libertà ($x,y,\theta$)
$Q=\left[x\ \ y\ \ \theta\right]^T\mskip{18mu}^B\xi=\left[v\ \ 0\ \ \omega\right]^T$
$\dot x=v\cos\theta\mskip{18mu}\dot y=v\sin\theta\mskip{18mu}\dot\theta=\omega$
$\dot q=G(q)u,\mskip{12mu} u=\left[ v\ \ \omega\right]^T$


In caso ideale, le ruote non hanno velocità laterale
Velocità lungo asse laterale: $v_{Y\mskip{-3mu}B}=-\dot x\sin\theta+\dot y\cos\theta$
# Cinematica diretta
Permette di calcolare, in base alla velocità ai giunti, l'evoluzione nel piano cartesiano
$v_L=r_L\dot\varphi_L\mskip{18mu}v_R=r_R\dot\varphi_R$
$v=\frac{v_R+v_L}{2}=\frac{r_R\dot\varphi_R+r_L\dot\varphi_L}{2}$
$\omega=\frac{v_R-v_L}{b}=\frac{r_R\dot\varphi_R-r_L\dot\varphi_L}{b}$

${v\\\omega}0=$
