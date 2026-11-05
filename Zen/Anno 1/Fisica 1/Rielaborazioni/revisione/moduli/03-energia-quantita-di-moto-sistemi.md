---
corso: Fisica Generale 1
modulo: 3
titolo: Lavoro, energia, quantità di moto e sistemi
programma: [FG1-04, FG1-06, FG1-02]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 3 · Lavoro, energia, quantità di moto e sistemi

**In questo modulo.** Servono la dinamica del modulo 2, il prodotto scalare fra vettori e gli integrali; per le forze conservative anche il gradiente (Analisi 1B). Si introducono due modi di risolvere i problemi di dinamica senza integrare le equazioni del moto. Il primo è l'energia: lavoro di una forza, energia cinetica e teorema dell'energia cinetica, forze conservative ed energia potenziale, conservazione dell'energia meccanica, punti di equilibrio, forze dissipative e potenza. Il secondo è la quantità di moto: impulso, conservazione nei sistemi isolati, urti. Infine si passa dal punto ai sistemi di punti: forze interne ed esterne, prima equazione cardinale, centro di massa e teorema di König. Alla fine si sanno usare i teoremi di conservazione per risolvere problemi di cadute, molle, urti e sistemi.

## 3.1 Lavoro ed energia cinetica

> [!definizione] Lavoro
> Il **lavoro** di una forza $F$ su un punto che si sposta lungo una curva $\gamma$ è l'integrale di linea
> $$L_\gamma(F) = \int_\gamma F \cdot dl,$$
> dove $dl$ è lo spostamento infinitesimo. Per una forza costante e uno spostamento rettilineo $\Delta r$, $L = F \cdot \Delta r = F\,\lvert\Delta r\rvert\cos\theta$.

Il lavoro si misura in **joule**, $1\ \mathrm{J} = 1\ \mathrm{N \cdot m}$. Conta solo la componente della forza lungo lo spostamento: una forza perpendicolare al moto (la reazione normale di un piano, la forza centripeta) non compie lavoro.

> [!teorema] Teorema dell'energia cinetica
> Il lavoro della risultante delle forze che agiscono su un punto materiale è uguale alla variazione della sua **energia cinetica** $T = \frac12 mv^2$:
> $$L_\gamma(F) = T_f - T_i.$$

*Dimostrazione.* Con $F = m\frac{dv}{dt}$ e $dl = v\, dt$:
$$L = \int m\frac{dv}{dt} \cdot v\, dt = m\int_{v_i}^{v_f} v \cdot dv = m\int \tfrac12 d(v^2) = \tfrac12 mv_f^2 - \tfrac12 mv_i^2. \ \square$$

**Lavoro della forza peso.** Per $F = -mg\hat k$ e uno spostamento da quota $z_i$ a quota $z_f$, $F \cdot dl = -mg\, dz$, quindi $L = -mg(z_f - z_i)$: dipende solo dal dislivello, non dal percorso.

**Lavoro della forza elastica.** Per una molla di lunghezza a riposo $l_0$, $F = -k(x - l_0)$; da $x = l_0$ a $x = x_1$:
$$L_{el} = \int_{l_0}^{x_1} -k(x - l_0)\, dx = -\tfrac12 k(x_1 - l_0)^2.$$
Comprimere o allungare una molla di 10 cm con $k = 200$ N/m richiede un lavoro esterno di $\frac12 \cdot 200 \cdot 0{,}01 = 1$ J.

## 3.2 Forze conservative ed energia potenziale

> [!definizione] Forza conservativa
> Una forza (posizionale) è **conservativa** se il lavoro per andare da $A$ a $B$ non dipende dal percorso ma solo da $A$ e $B$. Equivalentemente, il lavoro lungo ogni percorso chiuso è nullo: $\oint F \cdot dl = 0$.

Le due definizioni sono equivalenti: un cammino chiuso si spezza in un ramo $\gamma_1$ da $A$ a $B$ e un ramo $\gamma_2$ da $B$ ad $A$, e il lavoro totale è nullo se e solo se $L_{\gamma_1} = -L_{\gamma_2} = L_{-\gamma_2}$, cioè se due percorsi qualsiasi da $A$ a $B$ danno lo stesso lavoro. Il peso e la forza elastica sono conservative; l'attrito no, perché lavora sempre contro il moto.

> [!definizione] Energia potenziale
> Per una forza conservativa, fissato un punto di riferimento $A$, l'**energia potenziale** in $B$ è l'opposto del lavoro della forza da $A$ a $B$:
> $$U(B) - U(A) = -L_{A \to B} = -\int_A^B F \cdot dl.$$

Hanno significato solo le differenze di energia potenziale; la scelta del riferimento aggiunge una costante. Per il peso $U = mgz$, per la molla $U = \frac12 k\,\Delta x^2$.

> [!teorema] Conservazione dell'energia meccanica
> Se su un punto agiscono solo forze conservative, l'**energia meccanica** $E = T + U$ si conserva.

*Dimostrazione.* Per il teorema dell'energia cinetica $L_{A \to B} = T_B - T_A$, e per la definizione di $U$ $L_{A \to B} = U_A - U_B$. Uguagliando, $T_A + U_A = T_B + U_B$. $\square$

Per esempio un corpo che cade da fermo da un'altezza $h = 5$ m arriva a terra con $\frac12 mv^2 = mgh$, cioè $v = \sqrt{2gh} \approx 9{,}9$ m/s, qualunque sia la forma del percorso se non c'è attrito.

**Forza ed energia potenziale.** In una dimensione $F = -\frac{dU}{dx}$; in tre dimensioni la forza è il gradiente cambiato di segno:
$$F = -\nabla U = -\left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right).$$
Nei punti in cui $\frac{dU}{dx} = 0$ la forza è nulla: sono le **posizioni di equilibrio**. Sviluppando con Taylor attorno a un equilibrio $x_0$,
$$U(x) \approx U(x_0) + \tfrac12 k(x - x_0)^2, \qquad k = U''(x_0):$$
se $k > 0$ (minimo di $U$) l'equilibrio è **stabile**, perché un piccolo spostamento produce una forza $-k(x - x_0)$ che riporta verso $x_0$, e il corpo oscilla come un oscillatore armonico; se $k < 0$ (massimo) è **instabile**. Per $U(x) = x^3 - 3x$ gli equilibri sono $x = \pm 1$; $U''(x) = 6x$, quindi $x = 1$ è stabile e $x = -1$ instabile.

## 3.3 Forze non conservative e potenza

In presenza di attriti o resistenze l'energia meccanica non si conserva: la sua variazione è il lavoro delle forze non conservative,
$$\Delta E = (T_f + U_f) - (T_i + U_i) = L_{nc},$$
che per l'attrito è negativo (l'energia si trasforma in calore).

> [!definizione] Potenza
> La **potenza** è il lavoro fatto nell'unità di tempo. Quella media è $\bar P = \frac{L}{\Delta t}$, quella istantanea
> $$P = \frac{dL}{dt} = F \cdot v.$$
> Si misura in **watt**, $1\ \mathrm{W} = 1\ \mathrm{J/s}$.

Un'auto che va a velocità costante di 20 m/s contro una resistenza totale di 500 N deve sviluppare $P = 500 \cdot 20 = 10$ kW.

## 3.4 Quantità di moto e urti

> [!definizione] Quantità di moto e impulso
> La **quantità di moto** di un punto è $p = mv$. Il secondo principio si scrive $F = \frac{dp}{dt}$, e integrando nel tempo si ottiene il **teorema dell'impulso**:
> $$I = \int_{t_1}^{t_2} F\, dt = p(t_2) - p(t_1).$$

La forma $F = \frac{dp}{dt}$ è la più generale del secondo principio. In un urto agiscono per tempi brevissimi forze molto intense, di cui interessa solo l'effetto complessivo, l'impulso.

> [!teorema] Conservazione della quantità di moto
> In un sistema **isolato** (la risultante delle forze esterne è nulla) la quantità di moto totale $P = \sum p_i$ si conserva.

È una conseguenza del terzo principio (paragrafo 3.5). Per esempio, un fucile di massa $M = 4$ kg, inizialmente fermo, spara un proiettile di 10 g a 400 m/s: $0 = mv_p + Mv_R$, quindi rincula con $v_R = -\frac{m}{M}v_p = -1$ m/s.

Durante un **urto** le forze interne sono così intense che le forze esterne sono trascurabili: la quantità di moto totale si conserva. Gli urti si classificano in base all'energia cinetica:

- **completamente anelastico**: i corpi restano attaccati e proseguono con la stessa velocità $v_f = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$; l'energia cinetica persa è la massima compatibile con la conservazione della quantità di moto;
- **elastico**: si conserva anche l'energia cinetica totale;
- **anelastico**: si conserva la quantità di moto, e si perde una parte dell'energia cinetica.

> [!esempio] Due urti in una dimensione
> Un carrello di 2 kg a 3 m/s urta un carrello di 1 kg fermo. Se restano agganciati, $v_f = \frac{2 \cdot 3}{3} = 2$ m/s, e l'energia cinetica passa da 9 J a $\frac12 \cdot 3 \cdot 4 = 6$ J: si perdono 3 J. Se l'urto è elastico, risolvendo le due conservazioni si ottiene
> $$v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1 = 1\ \mathrm{m/s}, \qquad v_2' = \frac{2m_1}{m_1 + m_2}v_1 = 4\ \mathrm{m/s},$$
> e si controlla che $\frac12 \cdot 2 \cdot 1 + \frac12 \cdot 1 \cdot 16 = 9$ J.

## 3.5 Sistemi di punti e centro di massa

Si consideri un sistema di $N$ punti materiali. Sul punto $i$ agiscono **forze interne**, esercitate dagli altri punti del sistema, e **forze esterne**. Scrivendo $\frac{dp_i}{dt} = F_i^{(int)} + F_i^{(est)}$ e sommando su tutti i punti, le forze interne si annullano a coppie per il terzo principio.

> [!teorema] Prima equazione cardinale
> La quantità di moto totale $P = \sum_i m_i v_i$ di un sistema varia solo per effetto delle forze esterne:
> $$\frac{dP}{dt} = F^{(est)}.$$

> [!definizione] Centro di massa
> Il **centro di massa** di un sistema di punti è il punto di posizione
> $$r_{CM} = \frac{1}{M}\sum_i m_i r_i, \qquad M = \sum_i m_i.$$
> Per un corpo continuo la somma diventa un integrale: $r_{CM} = \frac{1}{M}\int r\, dm$.

Derivando, $P = Mv_{CM}$, e la prima equazione cardinale diventa
$$Ma_{CM} = F^{(est)}:$$
il centro di massa si muove come un punto materiale con tutta la massa del sistema, soggetto alla risultante delle forze esterne. Se il sistema è isolato, il centro di massa si muove di moto rettilineo uniforme.

> [!esempio] Centro di massa di un'asta non omogenea
> Un'asta sottile fra $x = 0$ e $x = l$ ha densità lineare $\lambda(x) = \lambda_0(1 + \alpha x)$, con $[\lambda_0] = \mathrm{kg/m}$ e $[\alpha] = \mathrm{m^{-1}}$. Con $dm = \lambda(x)\, dx$:
> $$M = \int_0^l \lambda_0(1 + \alpha x)\, dx = \lambda_0\left(l + \frac{\alpha l^2}{2}\right), \qquad \int_0^l x\, dm = \lambda_0\left(\frac{l^2}{2} + \frac{\alpha l^3}{3}\right),$$
> $$x_{CM} = \frac{l}{2}\cdot\frac{1 + \frac23\alpha l}{1 + \frac12\alpha l}.$$
> Per $\alpha = 0$ (asta omogenea) è il punto medio $\frac l2$; per $\alpha > 0$ la massa è spostata verso $x = l$ e il centro di massa anche.

> [!teorema] Teorema di König
> L'energia cinetica di un sistema è la somma dell'energia cinetica del centro di massa, con tutta la massa, e dell'energia cinetica dei moti relativi al centro di massa:
> $$T = \tfrac12 Mv_{CM}^2 + \sum_i \tfrac12 m_i \lvert v_i^{rel}\rvert^2, \qquad v_i^{rel} = v_i - v_{CM}.$$

*Dimostrazione.* Con $v_i = v_{CM} + v_i^{rel}$,
$$T = \sum_i \tfrac12 m_i (v_{CM} + v_i^{rel}) \cdot (v_{CM} + v_i^{rel}) = \tfrac12 Mv_{CM}^2 + v_{CM} \cdot \sum_i m_i v_i^{rel} + \sum_i \tfrac12 m_i\lvert v_i^{rel}\rvert^2,$$
e il termine misto è nullo perché $\sum_i m_i v_i^{rel} = \sum_i m_i v_i - Mv_{CM} = 0$: nel sistema del centro di massa la quantità di moto totale è nulla. $\square$

## Esempi ed esercizi svolti

**Esercizio 1 (una molla che lancia un blocco).** Una molla con $k = 200$ N/m, compressa di 10 cm, lancia un blocco di $0{,}5$ kg su un piano liscio. L'energia elastica $\frac12 k\Delta x^2 = 1$ J diventa tutta cinetica: $\frac12 \cdot 0{,}5 \cdot v^2 = 1$, quindi $v = 2$ m/s. Se dopo la molla c'è un tratto con attrito $\mu_d = 0{,}2$, il blocco si ferma quando il lavoro dell'attrito $\mu_d mg\,d$ ha consumato quel joule: $d = \frac{1}{0{,}2 \cdot 0{,}5 \cdot 9{,}8} \approx 1{,}02$ m.

**Esercizio 2 (pendolo balistico).** Un proiettile di 10 g a 300 m/s si conficca in un blocco di 2 kg appeso a un filo. Nell'urto, completamente anelastico, si conserva la quantità di moto: $V = \frac{0{,}01 \cdot 300}{2{,}01} \approx 1{,}49$ m/s. Dopo l'urto si conserva l'energia meccanica, e il blocco sale fino a $h = \frac{V^2}{2g} \approx 11{,}4$ cm. Misurando $h$ si risale alla velocità del proiettile; non si può usare l'energia nell'urto, dove quasi tutta l'energia cinetica del proiettile si dissipa.

**Esercizio 3 (esplosione).** Un oggetto fermo esplode in due frammenti di masse $m$ e $2m$. La quantità di moto totale resta nulla, quindi i frammenti partono in versi opposti e il più leggero ha velocità doppia. Il centro di massa resta fermo (o, se l'oggetto era in volo, prosegue sulla sua parabola).

### Esercizi dalle esercitazioni

Prima di scrivere equazioni conviene chiedersi che cosa si conserva: l'energia meccanica se lavorano solo forze conservative, la quantità di moto se la risultante delle forze esterne è nulla (in un urto, per la sua breve durata, quasi sempre), nessuna delle due se ci sono attriti e forze esterne.

**Esercizio 4. Il lavoro dipende dal percorso?** Sulla particella agisce $\vec F = (axy,\ -ax^2)$ con $a = 60$ N/m². Calcolare il lavoro dall'origine a $P = (l, l)$, $l = 0{,}1$ m, lungo il percorso che passa per $A = (l, 0)$ e lungo quello che passa per $B = (0, l)$.

Su $OA$ è $y = 0$ e $dy = 0$: $\vec F \cdot d\vec r = axy\,dx = 0$. Su $AP$ è $x = l$ e $dx = 0$: $\int_0^l (-al^2)\,dy = -al^3 = -0{,}06$ J. Su $OB$ è $x = 0$: lavoro nullo. Su $BP$ è $y = l$: $\int_0^l alx\,dx = \frac{al^3}{2} = 0{,}03$ J. I due lavori sono diversi: la forza **non è conservativa**, e non ha un'energia potenziale.

**Esercizio 5. Quando una forza lineare è conservativa?** $\vec F = (\alpha x + \beta y,\ \gamma x + \delta y)$. Condizione ed energia potenziale.

Una forza nel piano, definita su tutto $\mathbb{R}^2$, è conservativa se e solo se $\frac{\partial F_x}{\partial y} = \frac{\partial F_y}{\partial x}$, cioè $\beta = \gamma$. Allora $U$ si trova da $F_x = -\frac{\partial U}{\partial x}$ e $F_y = -\frac{\partial U}{\partial y}$: integrando la prima in $x$, $U = -\frac{\alpha x^2}{2} - \beta xy + g(y)$; derivando in $y$ e confrontando con la seconda, $g'(y) = -\delta y$. Quindi
$$U(x, y) = -\frac{\alpha}{2}x^2 - \beta xy - \frac{\delta}{2}y^2 + C.$$
Nell'esercizio 4 la forza non è di questo tipo, e infatti $\partial_y(axy) = ax \ne \partial_x(-ax^2) = -2ax$.

**Esercizio 6. La catena che scivola dal tavolo.** Una catena di 3 m, di peso lineare 18 N/m, ha 2 m su un piano orizzontale liscio e 1 m che pende. Quanto lavoro fa la forza peso mentre la catena scivola tutta giù?

Il lavoro del peso è $-\Delta U$, e $U$ dipende solo dalla quota del centro di massa di ogni tratto. All'inizio il tratto che pende ha peso 18 N e baricentro 0,5 m sotto il bordo: $U_i = -9$ J (il tratto sul piano ha $U = 0$). Alla fine la catena intera, di peso 54 N, ha il baricentro 1,5 m sotto il bordo: $U_f = -81$ J. Il lavoro è $W = U_i - U_f = 72$ J. Integrare la forza, che cresce con la parte che pende, darebbe lo stesso risultato con più fatica.

**Esercizio 7. Lancio su un piano scabro.** Un corpo è lanciato in salita con velocità $v_0$ su un piano inclinato di $\theta$ con attrito $\mu_d$. Altezza massima e lavoro dell'attrito.

Lungo il piano, fino a fermarsi dopo un tratto $d$: $-\frac12 mv_0^2 = -mgd\sin\theta - \mu_d mgd\cos\theta$ (teorema dell'energia cinetica). Quindi $d = \frac{v_0^2}{2g(\sin\theta + \mu_d\cos\theta)}$, l'altezza è $h = d\sin\theta$ e il lavoro dell'attrito è $W_a = -\mu_d mgd\cos\theta$. Senza attrito si ritrova $h = \frac{v_0^2}{2g}$, indipendente dall'inclinazione.

**Esercizio 8. Due pendoli che si urtano elasticamente.** Un pendolo di massa 2 kg e lunghezza 50 cm, lasciato da 30°, urta nel punto più basso una massa di 1 kg appesa a un filo di 20 cm. L'urto è elastico. Angolo massimo del secondo pendolo?

*Prima dell'urto*: $v_1 = \sqrt{2gL(1 - \cos 30°)} = 1{,}15$ m/s. *Urto elastico*, con il secondo corpo fermo: $v_2' = \frac{2M}{M + m}v_1 = \frac43 \cdot 1{,}15 = 1{,}53$ m/s. *Dopo*: il secondo pendolo sale di $h = \frac{v_2'^2}{2g} = 0{,}119$ m, e $\cos\theta = 1 - \frac{h}{l} = 0{,}405$: $\theta = 66°$. Sono tre fasi, e in ognuna si conserva una cosa diversa: energia, poi quantità di moto ed energia, poi energia.

**Esercizio 9. Un urto in due dimensioni.** Un corpo di 10 g a velocità $v_0$ urta un corpo identico fermo. Dopo l'urto si muovono a 3 m/s e 5 m/s lungo direzioni che formano 60°. Trovare $v_0$ e l'energia dissipata.

La quantità di moto si conserva come vettore: $m\vec v_0 = m\vec v_A + m\vec v_B$. Con il teorema del coseno sul triangolo dei vettori, $v_0^2 = v_A^2 + v_B^2 + 2v_A v_B\cos 60° = 9 + 25 + 15 = 49$, $v_0 = 7$ m/s. L'energia cinetica passa da $\frac12 m \cdot 49$ a $\frac12 m \cdot 34$: si perdono $\frac12 \cdot 0{,}01 \cdot 15 = 0{,}075$ J. Se l'urto fosse elastico fra masse uguali, le velocità finali sarebbero perpendicolari.

**Esercizio 10. Urto anelastico e molla.** Un corpo di 1 kg urta su un piano liscio un corpo fermo di 2 kg e resta attaccato; i due comprimono una molla ($k = 100$ N/m) di 5,8 cm. Velocità dopo l'urto e prima dell'urto.

*Dopo l'urto* si conserva l'energia: $\frac12(m_1 + m_2)V^2 = \frac12 k\Delta l^2$, quindi $V = \Delta l\sqrt{\frac{k}{m_1 + m_2}} = 0{,}335$ m/s. *Nell'urto* si conserva la quantità di moto: $m_1 v_1 = (m_1 + m_2)V$, quindi $v_1 = 3V = 1{,}00$ m/s. L'ordine è il contrario di quello in cui avvengono le cose: si risale dall'effetto alla causa.

### Esercizi sul modello delle prove d'esame

**Esercizio 11. Molla, piano inclinato e attrito.** Un corpo di 0,4 kg è appoggiato alla base di un piano inclinato di 30° contro una molla ($k = 100$ N/m) compressa di 20 cm. Lasciato libero, risale con $\mu_d = 0{,}15$. (a) Velocità quando la molla torna a riposo. (b) Distanza totale percorsa in salita.

(a) Nei primi 20 cm la molla cede $\frac12 kx^2 = 2$ J; il peso assorbe $mg\sin 30° \cdot 0{,}2 = 0{,}392$ J e l'attrito dissipa $\mu_d mg\cos 30° \cdot 0{,}2 = 0{,}102$ J. Restano $1{,}506$ J di energia cinetica: $v = \sqrt{\frac{2 \cdot 1{,}506}{0{,}4}} = 2{,}74$ m/s.

(b) Su tutta la salita, lunga $s$: $2 = (mg\sin 30° + \mu_d mg\cos 30°)\,s = 2{,}47\,s$, quindi $s = 0{,}81$ m dal punto di partenza. Se $\tan 30° = 0{,}577 > \mu_s$ il corpo poi ridiscende: va controllato con l'attrito statico, che il testo dovrebbe dare.

### Altri esercizi delle esercitazioni, con le soluzioni degli appunti a mano

**Esercizio 12. Un attrito che cambia lungo il piano.** Su un piano inclinato con $\tan\alpha = \frac34$ il coefficiente d'attrito vale $\frac12$ in cima ($s = 0$) e diminuisce come $\mu(s) = \mu_0 - ks^2$ fino a 0 in fondo ($s = L$). Velocità in fondo partendo da fermo.

Dalle condizioni agli estremi $\mu_0 = \frac12$ e $k = \frac{1}{2L^2}$. Lungo il piano $a(s) = g\sin\alpha - \mu(s)g\cos\alpha$. Poiché l'accelerazione dipende dalla posizione si usa $a = \frac{dv}{dt} = \frac{dv}{ds}\frac{ds}{dt} = v\frac{dv}{ds}$ e si separano le variabili: $\int_0^{v}v\,dv = \int_0^L(g\sin\alpha - \mu(s)g\cos\alpha)\,ds$, cioè $\frac{v^2}{2} = gL\sin\alpha - g\cos\alpha\left(\frac L2 - \frac L6\right) = gL\left(\sin\alpha - \frac13\cos\alpha\right)$. Con $\sin\alpha = \frac35$ e $\cos\alpha = \frac45$: $v = \sqrt{\frac23gL}$. Lo stesso risultato si ha dal teorema dell'energia cinetica, con il lavoro dell'attrito $-mg\cos\alpha\int_0^L\mu(s)\,ds$.

**Esercizio 13. Un corpo su un piano inclinato attaccato a una molla.** $m = 5$ kg, $k = 98$ N/m, $\mu_s = 0{,}4$, $\mu_d = 0{,}1$, $\theta = 22°$. Il corpo parte da fermo con la molla a riposo. Di quanto scende? Resta fermo laggiù? Legge oraria.

Un oscillatore si ferma prima di tornare indietro, quindi fra la partenza e il punto più basso $K_i = K_f = 0$ e il teorema lavoro-energia dà $mgd\sin\theta - \frac12kd^2 - \mu_dmgd\cos\theta = 0$: oltre a $d = 0$, $d = \frac{2mg(\sin\theta - \mu_d\cos\theta)}{k} = 0{,}28$ m. Laggiù l'attrito necessario per l'equilibrio è $F = kd - mg\sin\theta = 9{,}3$ N (9,06 N nei risultati, che usano $d$ arrotondato), minore di $\mu_sN = 18{,}2$ N: l'attrito statico basta e il corpo resta fermo. Durante la discesa $m\ddot x = mg\sin\theta - kx - \mu_dmg\cos\theta$, cioè $\ddot x + \omega^2x = A$ con $\omega^2 = \frac km$ e $A = g(\sin\theta - \mu_d\cos\theta)$: la soluzione è la somma di quella dell'omogenea e di quella particolare costante $\frac{A}{\omega^2}$, e con $x(0) = 0$, $\dot x(0) = 0$ si ottiene $x(t) = \frac{A}{\omega^2}(1 - \cos\omega t)$. L'attrito dinamico, finché ha verso costante, sposta soltanto il centro dell'oscillazione.

**Esercizio 14. Blocco, molla, fune e carrucola.** Il blocco $m_A = 1$ kg su un piano liscio è attaccato a una molla ($k = 20$ N/m) e, con una fune su una carrucola ideale, a $m_B = 0{,}5$ kg appeso; si parte da fermi con la molla a riposo. Allungamento massimo, tensione in quel momento, periodo.

All'allungamento massimo tutto è fermo, e l'energia si conserva: $0 = \frac12kx^2 - m_Bgx$, quindi $x = \frac{2m_Bg}{k} = 0{,}49$ m. Per la tensione: $T - kx = m_Aa$ per A e $m_Bg - T = m_Ba$ per B, da cui $a = \frac{m_Bg - kx}{m_A + m_B}$ e $T = m_B(g - a) = m_Bg\frac{m_A + 2m_B}{m_A + m_B} = 6{,}5$ N. Per il periodo si scrive l'accelerazione come $a = -\frac{k}{m_A + m_B}(x - x_0)$, con $x_0 = \frac{m_Bg}{k}$ posizione d'equilibrio: è un moto armonico attorno a $x_0$, con $T = 2\pi\sqrt{\frac{m_A + m_B}{k}} = 1{,}72$ s. Il peso di B sposta il centro dell'oscillazione, non il periodo.

**Esercizio 15. Quando si allenta il filo del pendolo?** Un pendolo di lunghezza $L$ passa per la verticale con $v_0 = \sqrt{3gL}$. Tensione in funzione dell'angolo; il filo resta teso?

Radialmente $T - mg\cos\theta = m\frac{v^2}{L}$, e per l'energia $v^2 = v_0^2 - 2gL(1 - \cos\theta)$: quindi $T = mg(1 + 3\cos\theta)$. Se il filo restasse teso il pendolo si fermerebbe dove $v = 0$, cioè $1 + 2\cos\theta = 0$, $\theta = 120°$; ma la tensione si annulla prima, a $\cos\theta = -\frac13$, $\theta \approx 109{,}5°$. Il filo **non** resta teso: oltre quell'angolo il corpo si stacca e prosegue in moto parabolico.

**Esercizio 16. Il distacco da una cupola.** Un corpo parte da fermo dalla cima di un cilindro liscio di raggio $R$. A che angolo dalla verticale si stacca?

Radialmente $mg\cos\alpha - N = m\frac{v^2}{R}$, e il distacco è a $N = 0$. Dall'energia, con lo zero alla base, $2mgR = \frac12mv^2 + mgR(1 + \cos\alpha)$, cioè $v^2 = 2gR(1 - \cos\alpha)$. Allora $mg\cos\alpha = 2mg(1 - \cos\alpha)$, $\cos\alpha = \frac23$, $\alpha = 48°$, indipendente da massa e raggio.

**Esercizio 17. Quattro molle a croce.** Quattro molle uguali ($k = 50$ N/m, lunghezza a riposo trascurabile) sono fissate in $(\pm L, 0, 0)$ e $(0, \pm L, 0)$, $L = 20$ cm, e legate a un corpo di 50 g lasciato da fermo in $(0, 0, L)$. Velocità nell'origine, periodo, energia potenziale nel piano orizzontale.

Ogni molla è lunga $\sqrt{z^2 + L^2}$, quindi l'energia potenziale totale è $U = 2k(z^2 + L^2)$: da $4kL^2 = 2kL^2 + \frac12mv^2$ si ha $v = \sqrt{\frac{4kL^2}{m}} = 12{,}65$ m/s. La componente $z$ di ogni forza è $-k\sqrt{z^2 + L^2}\frac{z}{\sqrt{z^2 + L^2}} = -kz$: le quattro insieme danno $-4kz$, un moto armonico con $\omega = 2\sqrt{k/m}$ e $T = \pi\sqrt{m/k} = 0{,}1$ s. Nel piano $z = 0$, sommando i quadrati delle quattro lunghezze, $U = 2k(r^2 + L^2)$, che a $r = 2L$ vale $10kL^2 = 20$ J.

**Esercizio 18. Un corpo su una guida libera di muoversi.** Una guida di massa $M = 0{,}8$ kg, libera su un piano liscio, è fatta da due quarti di circonferenza ($R = 20$ cm) uniti da un tratto piano scabro ($\mu = 0{,}2$, $d = 50$ cm). Un corpo di $0{,}2$ kg parte da fermo dal bordo. A che quota risale dall'altra parte, e di quanto si è spostata la guida?

Sul sistema non agiscono forze esterne orizzontali e all'inizio tutto è fermo: la quantità di moto orizzontale resta nulla, quindi $X_{CM}$ non cambia, e quando il corpo si ferma si ferma anche la guida. Il teorema lavoro-energia sul sistema dà $mg(R - h) - \mu mgd = 0$ (il lavoro totale dell'attrito dipende dallo scorrimento relativo, che è $d$), quindi $h = R - \mu d = 10$ cm. Per lo spostamento $s$ della guida: imponendo che $X_{CM}$ sia lo stesso all'inizio e alla fine, $s = \frac{m}{m + M}[d + R(1 + \sin\theta)]$ con $\cos\theta = \frac{R - h}{R} = \frac12$, cioè $s = 17{,}5$ cm.

**Esercizio 19. Su per un cuneo che scivola.** Un corpo di 10 g con $v_0 = 2$ m/s sale su un cuneo liscio di 1 kg, alto 30 cm, libero su un piano liscio. Fin dove sale? Con che velocità minima supererebbe il cuneo?

In orizzontale si conserva la quantità di moto, e alla quota massima corpo e cuneo hanno la stessa velocità: $mv_0 = (m + M)V$. Si conserva anche l'energia: $\frac12mv_0^2 = \frac12(m + M)V^2 + mgy$. Eliminando $V$: $y = \frac{M}{M + m}\frac{v_0^2}{2g} = 20$ cm, poco meno dei $\frac{v_0^2}{2g}$ che si avrebbero con il cuneo fermo, perché una parte dell'energia resta come moto del cuneo. Imponendo $y = h$: $v_0 = \sqrt{2gh\frac{M + m}{M}} = 2{,}4$ m/s.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Da che altezza per fare il giro della morte?** Una pallina scivola senza attrito su una guida che finisce in un anello verticale di raggio $R$. Altezza minima di partenza.

*Passo 1: la condizione nel punto più alto.* Per restare sulla guida serve $N \ge 0$; con $N + mg = m\frac{v^2}{R}$, la velocità minima è $v^2 = gR$.

*Passo 2: l'energia.* Partendo da ferma da $h$: $mgh = mg \cdot 2R + \frac12 mv^2$.

*Passo 3: mettere insieme.* $h = 2R + \frac{R}{2} = \frac{5}{2}R$.

*Passo 4: il controllo.* Partendo da $2R$, l'altezza dell'anello, non basta: arrivata in cima la pallina avrebbe velocità nulla, mentre ne serve una.

**Guidato 2. La massima compressione in un urto con molla.** Un carrello di 2 kg a 3 m/s raggiunge un carrello fermo di 1 kg che porta una molla ($k = 600$ N/m) sul davanti. Massima compressione?

*Passo 1: che cosa succede alla compressione massima.* I due carrelli hanno la stessa velocità: un istante prima si avvicinano, un istante dopo si allontanano.

*Passo 2: quantità di moto.* $2 \cdot 3 = 3V$, $V = 2$ m/s.

*Passo 3: energia.* Senza attriti si conserva l'energia meccanica, molla compresa: $\frac12 \cdot 2 \cdot 9 = \frac12 \cdot 3 \cdot 4 + \frac12 k x^2$, cioè $9 = 6 + 300x^2$.

*Passo 4: risultato.* $x = 0{,}1$ m. Nel riferimento del centro di massa, che si muove a 2 m/s, l'energia cinetica iniziale è proprio i 3 J che finiscono nella molla.

**Guidato 3. Centro di massa di tre punti.** Masse 1, 2, 3 kg in $(0, 0)$, $(2, 0)$, $(0, 3)$ m, con velocità $(1, 0)$, $(0, 1)$, $(0, 0)$ m/s.

*Passo 1: posizione.* $\vec r_{CM} = \frac{1 \cdot (0, 0) + 2 \cdot (2, 0) + 3 \cdot (0, 3)}{6} = \left(\frac23, \frac32\right)$ m.

*Passo 2: velocità.* $\vec v_{CM} = \frac{1 \cdot (1, 0) + 2 \cdot (0, 1)}{6} = \left(\frac16, \frac13\right)$ m/s.

*Passo 3: quantità di moto totale.* $\vec P = M\vec v_{CM} = (1, 2)$ kg·m/s, la somma delle tre quantità di moto. Se non agiscono forze esterne, il centro di massa continua a muoversi di moto rettilineo uniforme qualunque cosa facciano i punti fra loro.

## Riepilogo

Il lavoro di una forza è l'integrale $\int F \cdot dl$, e il lavoro della risultante è uguale alla variazione dell'energia cinetica $\frac12 mv^2$. Una forza è conservativa se il suo lavoro dipende solo dagli estremi; allora si definisce un'energia potenziale ($mgz$ per il peso, $\frac12 k\Delta x^2$ per la molla) con $F = -\nabla U$, e l'energia meccanica $T + U$ si conserva. Gli equilibri sono i punti stazionari di $U$, stabili nei minimi. Le forze non conservative cambiano l'energia meccanica del loro lavoro; la potenza è $F \cdot v$. La quantità di moto $mv$ varia dell'impulso delle forze e si conserva nei sistemi isolati; negli urti si conserva sempre, mentre l'energia cinetica si conserva solo negli urti elastici e si perde al massimo in quelli completamente anelastici. Per un sistema di punti le forze interne si annullano: la quantità di moto totale varia per le sole forze esterne e il centro di massa si muove come un punto con tutta la massa. Per il teorema di König l'energia cinetica è quella del centro di massa più quella del moto relativo.

## Formulario

Lavoro, energia, quantità di moto, urti e sistemi, con i termini per l'orale.

### Lavoro ed energia

$$W = \int_A^B \vec F \cdot d\vec r, \qquad K = \frac12 mv^2, \qquad W_{tot} = \Delta K, \qquad W_{cons} = -\Delta U, \qquad \Delta(K + U) = W_{nc}, \qquad P = \frac{dW}{dt} = \vec F \cdot \vec v.$$

| Forza | Energia potenziale |
|---|---|
| Peso | $U = mgh$ |
| Elastica | $U = \frac12 k x^2$ |
| Gravitazionale | $U = -\frac{GMm}{r}$ |
| Nel piano, conservativa | $\vec F = -\nabla U$, con $\partial_y F_x = \partial_x F_y$ |

### Quantità di moto e urti

$$\vec p = m\vec v, \qquad \vec J = \int \vec F\,dt = \Delta\vec p, \qquad \vec F_{ext} = \frac{d\vec P}{dt} = M\vec a_{CM}.$$

| Urto (1D, $m_2$ fermo) | Risultato |
|---|---|
| Completamente anelastico | $V = \frac{m_1 v_1}{m_1 + m_2}$, energia persa $\frac{m_2}{m_1 + m_2}K_1$ |
| Elastico | $v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1$, $v_2' = \frac{2m_1}{m_1 + m_2}v_1$ |
| Elastico, masse uguali | si scambiano le velocità |

### Sistemi di punti

$$\vec r_{CM} = \frac{\sum m_i\vec r_i}{M}, \qquad \vec v_{CM} = \frac{\vec P}{M}, \qquad K = \frac12 Mv_{CM}^2 + K' \ \text{(König)}.$$

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Lavoro | prodotto scalare della forza per lo spostamento, sommato lungo il percorso |
| Teorema dell'energia cinetica | il lavoro totale è la variazione di energia cinetica |
| Forza conservativa | il lavoro dipende solo dagli estremi; ha un'energia potenziale |
| Energia meccanica | $K + U$; si conserva se lavorano solo forze conservative |
| Potenza | lavoro per unità di tempo |
| Impulso | integrale della forza nel tempo, uguale alla variazione di quantità di moto |
| Urto elastico, anelastico | si conserva o no l'energia cinetica (la quantità di moto sempre) |
| Centro di massa | punto che si muove come se tutta la massa e tutte le forze esterne fossero lì |
| Forze interne | si annullano a coppie e non cambiano $\vec P$ |

### Domande che tornano spesso

- Dimostrare il teorema dell'energia cinetica.
- Definire una forza conservativa; perché l'attrito non lo è?
- Conservazione dell'energia meccanica e sua estensione con le forze non conservative.
- Teorema dell'impulso e conservazione della quantità di moto per un sistema isolato.
- Urti elastici e anelastici in una dimensione: ricavare le velocità finali.
- Moto del centro di massa e teorema di König.
