---
corso: Fisica Generale 1
modulo: 3
titolo: Lavoro, energia, quantità di moto e sistemi
programma: [FG1-04, FG1-06, FG1-02]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-04
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

## Riepilogo

Il lavoro di una forza è l'integrale $\int F \cdot dl$, e il lavoro della risultante è uguale alla variazione dell'energia cinetica $\frac12 mv^2$. Una forza è conservativa se il suo lavoro dipende solo dagli estremi; allora si definisce un'energia potenziale ($mgz$ per il peso, $\frac12 k\Delta x^2$ per la molla) con $F = -\nabla U$, e l'energia meccanica $T + U$ si conserva. Gli equilibri sono i punti stazionari di $U$, stabili nei minimi. Le forze non conservative cambiano l'energia meccanica del loro lavoro; la potenza è $F \cdot v$. La quantità di moto $mv$ varia dell'impulso delle forze e si conserva nei sistemi isolati; negli urti si conserva sempre, mentre l'energia cinetica si conserva solo negli urti elastici e si perde al massimo in quelli completamente anelastici. Per un sistema di punti le forze interne si annullano: la quantità di moto totale varia per le sole forze esterne e il centro di massa si muove come un punto con tutta la massa. Per il teorema di König l'energia cinetica è quella del centro di massa più quella del moto relativo.
