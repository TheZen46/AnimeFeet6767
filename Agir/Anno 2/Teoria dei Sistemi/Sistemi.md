$\underset{c(t)}{\overset{\text{Causa}}\longrightarrow}\fbox{Sistema}\underset{e(t)}{\overset{\text{Effetto}}\longrightarrow}$
$e(t)=O\big(c(t)\big)$

Sistemi algebrici: l'effetto ha dipendenza algebrica dalla casua, non dinamico
Sistemi dinamici:
$\displaystyle\begin{array}{r}\underset{c_e(t)}{\overset{\overset{\text{Cause}}{\text{esterne}}\\}\longrightarrow}\\\underset{c_i(t)}{\overset{\overset{\text{Cause}}{\text{interne}}\\}\longrightarrow}\end{array}\boxed{\begin{array}{c}\\\text{Sistema}\\\mskip{1mu}\end{array}}\underset{e(t)}{\overset{\text{Effetto}}\longrightarrow}$

Esempio: lavandino
$h(t)=\text{livello dell'acqua (causa interna)}$
$u(t)=\text{velocità di alzamento del livello (rubinetto, causa esterna)}$

$\dot h(\tau)=u(\tau)$

$\displaystyle\int_0^t \dot h(\tau)d\tau=h(t)-h(0)=\int_0^t u(\tau)d\tau$
$h(t)=h(0)+\int_0^tu(\tau)d\tau$
$e(t)=O\big(c_i(t_0),c_e(\tau)\big)\mskip{18mu}t_0\le\tau<t$

$5l\to 5cm=h(0)$
$\begin{array}{c}2l/sec\\5sec\end{array}\mskip{6mu}=h(5sec)=15cm=15l$

Sistema tempo-invariante/stazionario: il risultato non dipende dall'asse assoluto del tempo

La quasi totalità dei sistemi possono essere studiati localmente con i sistemi lineari