---
corso: Fisica Generale 1
modulo: 4
titolo: Corpo rigido e momento angolare
programma: [FG1-03, FG1-07, FG1-02]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-04
---

# 4 · Corpo rigido e momento angolare

**In questo modulo.** Servono il moto circolare del modulo 1, la dinamica del modulo 2, l'energia e i sistemi di punti del modulo 3, il prodotto vettoriale e gli integrali multipli. Si studia il corpo rigido: gradi di libertà, cinematica delle rotazioni attorno a un asse fisso, energia cinetica di rotazione e momento d'inerzia, con il teorema di Huygens-Steiner e il calcolo dei momenti d'inerzia di asta, anello, disco e sfera. Poi la dinamica: momento di una forza, seconda equazione cardinale, puro rotolamento, macchina di Atwood con carrucola massiva. Infine il momento angolare rispetto a un polo e la sua conservazione, le forze centrali con la legge delle aree, e le condizioni di equilibrio di un corpo rigido. Alla fine si sanno risolvere problemi di rotazione e rotolamento, con le equazioni cardinali e con l'energia.

## 4.1 Corpo rigido e rotazioni

> [!definizione] Corpo rigido
> Un **corpo rigido** è un sistema di punti materiali in cui le distanze fra due punti qualsiasi restano costanti nel tempo.

Un punto materiale libero ha 3 **gradi di libertà** (le tre coordinate). Un corpo rigido ne ha 6: la sua posizione è fissata da tre punti non allineati (9 coordinate) legati da 3 vincoli sulle distanze reciproche, $9 - 3 = 6$; si possono pensare come 3 coordinate del centro di massa e 3 angoli di orientamento.

Nella **rotazione attorno a un asse fisso** ogni punto del corpo descrive una circonferenza con centro sull'asse. Il moto è descritto da un solo angolo $\theta(t)$, con **velocità angolare** $\omega = \frac{d\theta}{dt}$ e **accelerazione angolare** $\alpha = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$, uguali per tutti i punti. Un punto a distanza $R$ dall'asse percorre l'arco $l = R\theta$ e ha velocità e accelerazione tangenziali
$$v = R\omega, \qquad a_t = R\alpha,$$
più l'accelerazione centripeta $\omega^2 R$. Come vettore, $\omega$ è diretto lungo l'asse, con verso dato dalla regola della mano destra (la rotazione appare antioraria guardando dalla punta del vettore).

## 4.2 Momento d'inerzia

Sommando l'energia cinetica dei punti di un corpo che ruota attorno a un asse fisso, con $v_i = R_i\omega$:
$$T = \sum_i \tfrac12 m_i v_i^2 = \tfrac12\Big(\sum_i m_i R_i^2\Big)\omega^2 = \tfrac12 I\omega^2.$$

> [!definizione] Momento d'inerzia
> Il **momento d'inerzia** rispetto a un asse è
> $$I = \sum_i m_i R_i^2 \qquad \text{oppure} \qquad I = \int R^2\, dm = \int \rho\, R^2\, dV,$$
> dove $R_i$ (o $R$) è la distanza dall'asse. Si misura in kg·m².

Il momento d'inerzia è per le rotazioni ciò che la massa è per le traslazioni, ma dipende dall'asse: la massa lontana dall'asse conta di più.

> [!teorema] Teorema di Huygens-Steiner (assi paralleli)
> Se $I_{CM}$ è il momento d'inerzia rispetto a un asse per il centro di massa, rispetto a un asse parallelo a distanza $d$ il momento d'inerzia è
> $$I = I_{CM} + Md^2.$$

> [!esempio] Momenti d'inerzia notevoli
>
> - **Due masse $m$ agli estremi di un'asta leggera** di lunghezza $l$, asse per il centro: $I_{CM} = 2m\left(\frac l2\right)^2 = \frac12 ml^2$. Rispetto a un estremo, per Steiner $\frac12 ml^2 + 2m\left(\frac l2\right)^2 = ml^2$, come dal calcolo diretto $m \cdot 0 + m l^2$.
> - **Asta omogenea** di massa $M$ e lunghezza $l$, con $dm = \frac Ml dx$: rispetto al centro $I_{CM} = \int_{-l/2}^{l/2}\frac Ml x^2\, dx = \frac{1}{12}Ml^2$; rispetto a un estremo $\frac13 Ml^2$.
> - **Anello sottile** di raggio $R$, asse centrale: tutta la massa è a distanza $R$, quindi $I = MR^2$.
> - **Disco omogeneo** di raggio $R$: si somma su anelli di raggio $r$ e massa $dm = \frac{M}{\pi R^2}2\pi r\, dr$, e $I = \int_0^R r^2\, dm = \frac{2M}{R^2}\cdot\frac{R^4}{4} = \frac12 MR^2$.
> - **Sfera omogenea** di raggio $R$: in coordinate sferiche la distanza dall'asse $z$ è $r\sin\theta$ e $dV = r^2\sin\theta\, dr\, d\theta\, d\varphi$; integrando con $\rho = \frac{M}{\frac43\pi R^3}$ si trova $I = \frac25 MR^2$.

## 4.3 Momento di una forza e seconda equazione cardinale

L'effetto di rotazione di una forza dipende da dove è applicata. Il **momento** (momento torcente) di una forza $F$ applicata a distanza $R$ dall'asse ha modulo
$$\tau = RF\sin\varphi,$$
dove $\varphi$ è l'angolo fra il raggio e la forza: conta solo la componente perpendicolare al raggio, e $R\sin\varphi$ si chiama **braccio**. Le forze che passano per l'asse hanno momento nullo.

> [!teorema] Seconda equazione cardinale per un asse fisso
> Per un corpo rigido che ruota attorno a un asse fisso, il momento risultante delle forze esterne rispetto all'asse è
> $$\tau = I\alpha = I\frac{d^2\theta}{dt^2}.$$

È l'analogo di $F = ma$: il momento al posto della forza, il momento d'inerzia al posto della massa, l'accelerazione angolare al posto di quella lineare.

> [!esempio] Carrucola con attrito al perno
> Una forza costante $F = 15$ N è applicata tangenzialmente al bordo di una carrucola di raggio $R_0 = 33$ cm, che parte da ferma e raggiunge $\omega = 30$ rad/s in 3 s; il perno esercita un momento d'attrito costante $\tau_A = 1{,}1$ N·m. L'accelerazione angolare è $\alpha = 10$ rad/s², e
> $$R_0 F - \tau_A = I\alpha \quad \Longrightarrow \quad I = \frac{0{,}33 \cdot 15 - 1{,}1}{10} = 0{,}385\ \mathrm{kg\,m^2}.$$

## 4.4 Energia nelle rotazioni e puro rotolamento

Anche per le rotazioni vale la conservazione dell'energia, con l'energia cinetica $\frac12 I\omega^2$ e, per il peso, l'energia potenziale $Mgz_{CM}$ calcolata nel centro di massa.

> [!esempio] Un palo che cade
> Un palo omogeneo di massa $M$ e lunghezza $l = 2{,}3$ m, incernierato alla base, cade dalla posizione verticale. All'inizio $E = Mg\frac l2$; quando tocca terra $E = \frac12 I_A\omega^2$ con $I_A = \frac13 Ml^2$. Uguagliando, $\omega = \sqrt{\frac{3g}{l}}$, e l'estremo libero arriva a $v = l\omega = \sqrt{3gl} \approx 8{,}2$ m/s, più di quanto avrebbe un sasso lasciato cadere dalla stessa altezza ($\sqrt{2gl} \approx 6{,}7$ m/s).

Un corpo a simmetria circolare (cilindro, sfera, anello) di raggio $R$ **rotola senza strisciare** se il punto di contatto ha velocità nulla. La condizione di puro rotolamento è
$$v_{CM} = \omega R, \qquad a_{CM} = \alpha R,$$
e per il teorema di König l'energia cinetica è $T = \frac12 Mv_{CM}^2 + \frac12 I_{CM}\omega^2 = \frac12\left(M + \frac{I_{CM}}{R^2}\right)v_{CM}^2$.

![Figura 4.1 · Forze su un corpo che rotola giù per un piano inclinato: solo l'attrito statico ha momento rispetto al centro.](../figure/4-1.svg)

> [!esempio] Rotolamento lungo un piano inclinato
> Un corpo di massa $M$, raggio $R$ e momento d'inerzia $I_{CM}$ scende rotolando su un piano inclinato di angolo $\theta$. Peso e normale passano per il centro di massa e non danno momento: a far ruotare il corpo è l'attrito statico $F_A$, rivolto verso l'alto lungo il piano, nel punto di contatto. Le equazioni cardinali, con il vincolo $a_{CM} = \alpha R$, sono
> $$Mg\sin\theta - F_A = Ma_{CM}, \qquad F_A R = I_{CM}\alpha.$$
> Risolvendo,
> $$a_{CM} = \frac{g\sin\theta}{1 + \frac{I_{CM}}{MR^2}}, \qquad F_A = \frac{I_{CM}}{MR^2 + I_{CM}}Mg\sin\theta.$$
> Il corpo scende tanto più lentamente quanto più massa ha lontano dal centro: $a_{CM}$ vale $\frac12 g\sin\theta$ per un anello, $\frac23 g\sin\theta$ per un disco, $\frac57 g\sin\theta$ per una sfera. Perché non strisci deve essere $F_A \le \mu_s Mg\cos\theta$, cioè $\mu_s \ge \frac{I_{CM}}{MR^2 + I_{CM}}\tan\theta$: per un disco su un piano di $30°$, $\mu_s \ge \frac13\tan 30° \approx 0{,}19$.

## 4.5 Macchina di Atwood con carrucola massiva

Due masse $m_1 > m_2$ sono appese ai capi di una fune che passa senza strisciare su una carrucola di raggio $R$ e momento d'inerzia $I$. Se la carrucola ha massa, le tensioni nei due rami sono diverse: la loro differenza dà il momento che la fa ruotare. Con $a$ l'accelerazione ($m_1$ scende) e $\alpha = \frac aR$:
$$m_1 g - T_1 = m_1 a, \qquad T_2 - m_2 g = m_2 a, \qquad (T_1 - T_2)R = I\frac aR.$$
Sommando tutto si eliminano le tensioni:
$$a = \frac{(m_1 - m_2)g}{m_1 + m_2 + \frac{I}{R^2}}.$$
La carrucola si comporta come una massa aggiuntiva $\frac{I}{R^2}$. Con $m_1 = 3$ kg, $m_2 = 2$ kg e una carrucola a disco di 2 kg ($\frac{I}{R^2} = 1$ kg): $a = \frac{9{,}8}{6} \approx 1{,}63$ m/s².

## 4.6 Momento angolare

> [!definizione] Momento della forza e momento angolare rispetto a un polo
> Per un punto materiale in posizione $r$, con quantità di moto $p = mv$ e soggetto alla forza $F$, e un punto $\Omega$ (il **polo**) di posizione $r_\Omega$:
> $$\tau_\Omega = (r - r_\Omega) \times F, \qquad L_\Omega = (r - r_\Omega) \times p.$$
> Per un sistema si sommano i contributi dei singoli punti.

> [!teorema] Teorema del momento angolare
> $$\frac{dL_\Omega}{dt} = \tau_\Omega - v_\Omega \times p.$$
> Se il polo è fisso ($v_\Omega = 0$) o coincide con il centro di massa, il termine correttivo è nullo e $\frac{dL}{dt} = \tau$ (**seconda equazione cardinale**). Per un sistema conta solo il momento delle forze esterne.

*Dimostrazione.* Con la regola di derivazione del prodotto vettoriale,
$$\frac{dL_\Omega}{dt} = \left(\frac{dr}{dt} - \frac{dr_\Omega}{dt}\right) \times p + (r - r_\Omega) \times \frac{dp}{dt} = (v - v_\Omega) \times mv + (r - r_\Omega) \times F.$$
Poiché $v \times v = 0$, resta $-v_\Omega \times p + \tau_\Omega$. Se $\Omega$ è il centro di massa di un sistema, $v_\Omega = v_{CM}$ è parallela a $P = Mv_{CM}$ e il prodotto vettoriale è ancora nullo. $\square$

Per un corpo rigido che ruota attorno a un asse fisso di simmetria, $L = I\omega$, e la seconda equazione cardinale diventa $\frac{d}{dt}(I\omega) = \tau$, cioè $I\alpha = \tau$ se $I$ è costante.

> [!teorema] Conservazione del momento angolare
> Se il momento risultante delle forze esterne rispetto a un polo fisso (o al centro di massa) è nullo, il momento angolare rispetto a quel polo si conserva.

Una pattinatrice che ruota con le braccia aperte ($I_1 = 4$ kg·m², $\omega_1 = 2$ rad/s) e le chiude ($I_2 = 1{,}6$ kg·m²) passa a $\omega_2 = \frac{I_1\omega_1}{I_2} = 5$ rad/s. L'energia cinetica di rotazione $\frac12 I\omega^2$ invece aumenta, da 8 J a 20 J: la differenza è il lavoro dei muscoli che tirano le braccia verso l'asse.

## 4.7 Forze centrali

Un campo di forze è **centrale** se la forza è sempre diretta lungo la retta che congiunge il punto con un centro fisso $O$, con un'intensità che dipende solo dalla distanza: $F(r) = F(r)\,\hat u_r$, $r = \lvert r\rvert$. Esempi sono la gravitazione e la forza elettrostatica.

- **Sono conservative**: in coordinate polari $dl = dr\,\hat u_r + r\,d\theta\,\hat u_\theta$, quindi $F \cdot dl = F(r)\, dr$ e il lavoro $\int_{r_i}^{r_f}F(r)\, dr$ dipende solo dalle distanze iniziale e finale.
- **Conservano il momento angolare** rispetto a $O$: $\tau = r \times F(r)\hat u_r = 0$, perché i due vettori sono paralleli.

Dalla conservazione di $L = r \times mv$ seguono due fatti. Il moto è **piano**: $r$ e $v$ restano perpendicolari al vettore costante $L$. E, scrivendo $v = \dot r\,\hat u_r + r\dot\theta\,\hat u_\theta$, si ha $L = mr^2\dot\theta$, quindi
$$r^2\frac{d\theta}{dt} = \text{costante}.$$
La quantità $\frac12 r^2\dot\theta$ è la **velocità areolare**, l'area spazzata dal raggio vettore nell'unità di tempo: è costante per ogni forza centrale. Per la gravitazione è la seconda legge di Keplero (il raggio vettore di un pianeta spazza aree uguali in tempi uguali).

## 4.8 Equilibrio del corpo rigido

Un corpo rigido è in equilibrio (fermo) se sono nulle la risultante delle forze esterne e il loro momento risultante rispetto a un polo qualsiasi:
$$\sum F^{(est)} = 0, \qquad \sum \tau^{(est)} = 0.$$
Sono le due equazioni cardinali con le derivate nulle. Se la risultante è nulla, il momento risultante non dipende dal polo, e conviene scegliere il polo dove agiscono forze incognite, per eliminarle dall'equazione dei momenti.

> [!esempio] Trave appoggiata con un carico
> Una trave omogenea di 4 m e 20 kg è appoggiata ai due estremi; un carico di 30 kg è a 1 m dall'estremo sinistro. Con i momenti rispetto all'appoggio sinistro, la reazione destra $R_2$ deve bilanciare il peso della trave (applicato a 2 m) e il carico: $4R_2 = 20g \cdot 2 + 30g \cdot 1$, da cui $R_2 = 17{,}5g \approx 171{,}5$ N. La risultante nulla dà $R_1 = 50g - R_2 = 32{,}5g \approx 318{,}5$ N: l'appoggio più vicino al carico sostiene di più.

## Esempi ed esercizi svolti

**Esercizio 1 (un disco che parte da fermo).** Un disco di massa 2 kg e raggio 10 cm, libero di ruotare attorno al suo asse, è messo in rotazione da una fune avvolta sul bordo, tirata con forza costante di 4 N. Con $I = \frac12 MR^2 = 0{,}01$ kg·m², $\alpha = \frac{FR}{I} = \frac{0{,}4}{0{,}01} = 40$ rad/s². Dopo 2 s, $\omega = 80$ rad/s; l'energia cinetica $\frac12 I\omega^2 = 32$ J è uguale al lavoro della forza, $F$ per la fune svolta: $4 \cdot R\theta = 4 \cdot 0{,}1 \cdot \frac12 \cdot 40 \cdot 4 = 32$ J.

**Esercizio 2 (sfera e cilindro in gara).** Una sfera e un cilindro pieno, con qualsiasi massa e raggio, partono da fermi dalla stessa altezza $h$ su un piano inclinato, rotolando senza strisciare. Per la conservazione dell'energia $Mgh = \frac12\left(M + \frac{I}{R^2}\right)v^2$, quindi $v = \sqrt{\frac{2gh}{1 + I/(MR^2)}}$: $\sqrt{\frac{10}{7}gh}$ per la sfera, $\sqrt{\frac43 gh}$ per il cilindro. Arriva prima la sfera, e il risultato non dipende né dalla massa né dal raggio.

**Esercizio 3 (momento angolare di un punto in moto rettilineo).** Un punto che si muove di moto rettilineo uniforme ha, rispetto a un polo $O$ fuori dalla retta, momento angolare $L = mvd$, dove $d$ è la distanza di $O$ dalla retta: è costante, come deve essere perché la forza è nulla. È anche un caso (banale) della legge delle aree: il raggio vettore spazza triangoli di uguale area in tempi uguali.

## Riepilogo

Un corpo rigido ha 6 gradi di libertà; nella rotazione attorno a un asse fisso tutti i punti hanno la stessa $\omega$ e $\alpha$, con $v = R\omega$ e $a_t = R\alpha$. L'energia cinetica di rotazione è $\frac12 I\omega^2$, con il momento d'inerzia $I = \int R^2\, dm$ che dipende dall'asse e si trasporta con Huygens-Steiner ($I = I_{CM} + Md^2$): $\frac{1}{12}Ml^2$ per l'asta al centro, $MR^2$ per l'anello, $\frac12 MR^2$ per il disco, $\frac25 MR^2$ per la sfera. Il momento di una forza è $RF\sin\varphi$ e, per un asse fisso, $\tau = I\alpha$. Nel puro rotolamento $v_{CM} = \omega R$, l'attrito statico fornisce il momento e non compie lavoro, e i corpi con più massa lontana dall'asse accelerano meno. Una carrucola con massa equivale a una massa aggiuntiva $I/R^2$. Il momento angolare rispetto a un polo fisso o al centro di massa varia del momento delle forze esterne e si conserva se questo è nullo. Le forze centrali sono conservative e conservano il momento angolare: il moto è piano e la velocità areolare è costante. Un corpo rigido è in equilibrio se risultante e momento risultante delle forze esterne sono nulli.
