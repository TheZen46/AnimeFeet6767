---
corso: Fisica Generale 1
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# Fisica Generale 1

**Appunti del corso · a.a. 2026/27 · Mobius**

Appunti personali e non ufficiali, rivisti e confrontati con il programma ufficiale del corso. Non sostituiscono le lezioni né i testi consigliati.

## Indice

1. Strumenti matematici e cinematica del punto
2. Dinamica del punto materiale
3. Lavoro, energia, quantità di moto e sistemi
4. Corpo rigido e momento angolare

## 1 · Strumenti matematici e cinematica del punto

**In questo modulo.** Servono le derivate e gli integrali di Analisi 1A e i vettori del piano e dello spazio (somma, prodotto per uno scalare, componenti). Si richiamano gli strumenti matematici usati in tutto il corso: grandezze scalari e vettoriali, derivata come velocità di variazione, integrale come somma, e le equazioni differenziali più semplici. Poi si descrive il moto di un punto materiale senza chiedersi che cosa lo causi: traiettoria e legge oraria, spostamento e distanza percorsa, velocità e accelerazione medie e istantanee, i moti rettilinei uniforme e uniformemente accelerato, il moto del proiettile, il moto circolare uniforme e la composizione delle velocità fra due sistemi di riferimento. Alla fine si sa scrivere e usare la legge oraria di un moto e ricavarne velocità e accelerazione.

### 1.1 Grandezze fisiche e strumenti matematici

La **meccanica** studia il moto dei corpi. Si divide in **cinematica**, che descrive come un corpo si muove (traiettorie, leggi orarie) senza occuparsi delle cause, e **dinamica**, che studia le forze che producono il moto. Il modello più semplice di corpo è il **punto materiale**: un oggetto di cui si trascurano le dimensioni, descritto da una sola posizione e da una massa.

Le grandezze fisiche si esprimono con un numero e un'unità di misura; nel Sistema Internazionale le unità di base della meccanica sono il metro (m), il kilogrammo (kg) e il secondo (s). Una grandezza è **scalare** se basta un numero (massa, tempo, energia), **vettoriale** se servono anche una direzione e un verso (spostamento, velocità, forza). In un sistema di assi cartesiani un vettore si scrive con le sue componenti, $v = (v_x, v_y, v_z) = v_x\hat\imath + v_y\hat\jmath + v_z\hat k$, dove $\hat\imath, \hat\jmath, \hat k$ sono i **versori** degli assi (vettori di lunghezza 1).

Tre strumenti di Analisi si usano continuamente:

- la **derivata** $\frac{df}{dt}$ misura quanto rapidamente varia $f$ nel tempo; per un vettore si deriva componente per componente;
- l'**integrale** $\int_{t_0}^{t_1} f(t)\, dt$ somma contributi infinitesimi, e permette di risalire a una grandezza conoscendone la velocità di variazione: se $\frac{dF}{dt} = f$, allora $F(t_1) - F(t_0) = \int_{t_0}^{t_1} f(t)\, dt$;
- le **equazioni differenziali**, in cui l'incognita è una funzione del tempo e compaiono le sue derivate. Le leggi del moto sono equazioni di questo tipo.

> [!esempio] Tre equazioni differenziali del corso
>
> - $\frac{dx}{dt} = v_0$ costante ha soluzioni $x(t) = v_0 t + x_0$: una retta, con la costante $x_0$ fissata dal valore iniziale.
> - $\frac{d^2x}{dt^2} = a_0$ costante si integra due volte: $x(t) = \frac12 a_0 t^2 + v_0 t + x_0$, con due costanti, la posizione e la velocità iniziali.
> - $\frac{d^2x}{dt^2} = -\omega^2 x$ (l'equazione dell'**oscillatore armonico**) ha soluzioni $x(t) = A\cos(\omega t + \phi)$: derivando due volte si ottiene $-A\omega^2\cos(\omega t + \phi) = -\omega^2 x$. Anche qui due costanti, l'ampiezza $A$ e la fase $\phi$, fissate dalle condizioni iniziali.

Un'equazione differenziale del secondo ordine ha in generale una famiglia di soluzioni con due costanti: per individuare il moto servono la posizione e la velocità iniziali.

### 1.2 Traiettoria, legge oraria, spostamento

Per descrivere il moto si fissa un **sistema di riferimento**: un'origine, tre assi e un orologio. La posizione del punto all'istante $t$ è il vettore $r(t) = (x(t), y(t), z(t))$.

> [!definizione] Traiettoria e legge oraria
> La **traiettoria** è la curva $\gamma$ formata dalle posizioni occupate dal punto durante il moto. La **legge oraria** è la funzione $t \mapsto r(t)$, cioè le tre funzioni $x(t)$, $y(t)$, $z(t)$, che dicono dove si trova il punto in ogni istante.

La traiettoria dice per dove passa il punto, la legge oraria anche quando. Fra due istanti $t_0$ e $t_1$ si distinguono:

- la **distanza percorsa**, uno scalare: la lunghezza dell'arco di traiettoria percorso;
- lo **spostamento**, un vettore: $\Delta r = r(t_1) - r(t_0) = (x_1 - x_0,\ y_1 - y_0,\ z_1 - z_0)$, che dipende solo dalle posizioni iniziale e finale.

Se il punto va e torna, lo spostamento può essere nullo mentre la distanza percorsa no. Nel moto unidimensionale (lungo l'asse $x$) la legge oraria si rappresenta con un grafico spazio-tempo $x(t)$.

### 1.3 Velocità e accelerazione

> [!definizione] Velocità media e istantanea
> La **velocità scalare media** è la distanza percorsa divisa per il tempo impiegato; la **velocità vettoriale media** è $\langle v\rangle = \frac{\Delta r}{\Delta t}$. La **velocità istantanea** è il limite per $\Delta t \to 0$:
> $$v(t) = \lim_{\Delta t \to 0} \frac{r(t + \Delta t) - r(t)}{\Delta t} = \frac{dr}{dt} = \left(\frac{dx}{dt}, \frac{dy}{dt}, \frac{dz}{dt}\right).$$

La velocità istantanea è tangente alla traiettoria e il suo modulo, la **celerità**, è la velocità con cui si percorre la traiettoria. Nel grafico $x(t)$ è la pendenza della tangente.

> [!definizione] Accelerazione
> L'**accelerazione media** è $\frac{\Delta v}{\Delta t}$, quella **istantanea** è
> $$a(t) = \frac{dv}{dt} = \frac{d^2 r}{dt^2}.$$

Le unità sono m/s per la velocità e m/s² per l'accelerazione. Viceversa, conoscendo l'accelerazione si risale alla velocità e alla posizione integrando: $v(t) = v(t_0) + \int_{t_0}^{t} a(s)\, ds$ e $r(t) = r(t_0) + \int_{t_0}^{t} v(s)\, ds$.

### 1.4 Moti rettilinei notevoli

> [!definizione] Moto rettilineo uniforme
> Il moto avviene lungo una retta con velocità costante $v_0$. Integrando $\frac{dx}{dt} = v_0$:
> $$x(t) = x_0 + v_0 t, \qquad x_0 = x(0).$$

Il grafico spazio-tempo è una retta di pendenza $v_0$, e il tempo per percorrere una distanza $d$ è $\frac{d}{v_0}$.

> [!definizione] Moto rettilineo uniformemente accelerato
> Il moto avviene lungo una retta con accelerazione costante $a_0$. Integrando due volte:
> $$v(t) = v_0 + a_0 t, \qquad x(t) = x_0 + v_0 t + \tfrac12 a_0 t^2.$$

Eliminando il tempo fra le due equazioni si ottiene una relazione utile quando il tempo non interessa:
$$v^2 = v_0^2 + 2a_0(x - x_0).$$
Per esempio, un'auto che viaggia a 30 m/s (108 km/h) e frena con decelerazione costante di 5 m/s² si ferma in $t = \frac{30}{5} = 6$ s, percorrendo $30 \cdot 6 - \frac12 \cdot 5 \cdot 36 = 90$ m; lo stesso risultato viene da $0 = 30^2 - 2 \cdot 5 \cdot d$. Un corpo in **caduta libera** vicino alla superficie terrestre ha accelerazione costante $g \approx 9{,}8$ m/s² verso il basso.

### 1.5 Moto in più dimensioni e moto del proiettile

Nel piano (o nello spazio) posizione, velocità e accelerazione sono vettori, e le loro componenti si trattano separatamente: $v = (v_x, v_y) = \left(\frac{dx}{dt}, \frac{dy}{dt}\right)$ e $a = \left(\frac{dv_x}{dt}, \frac{dv_y}{dt}\right)$. Se l'accelerazione è costante, ogni componente segue un moto rettilineo uniformemente accelerato.

> [!esempio] Moto del proiettile
> Un corpo lanciato vicino al suolo, trascurando l'aria, ha accelerazione $(0, -g)$, con l'asse $y$ verticale verso l'alto. Le leggi orarie sono disaccoppiate:
> $$x(t) = x_0 + v_{0x} t, \qquad y(t) = y_0 + v_{0y} t - \tfrac12 g t^2:$$
> moto uniforme in orizzontale, uniformemente accelerato in verticale. Ricavando $t = \frac{x - x_0}{v_{0x}}$ dalla prima e sostituendo nella seconda si trova la traiettoria
> $$y = y_0 + \frac{v_{0y}}{v_{0x}}(x - x_0) - \frac{g}{2v_{0x}^2}(x - x_0)^2,$$
> una parabola.

Per un lancio dal suolo con velocità $v_0$ e angolo $\theta$ sull'orizzontale ($v_{0x} = v_0\cos\theta$, $v_{0y} = v_0\sin\theta$), il corpo torna a terra quando $y = 0$, cioè dopo il **tempo di volo** $t_v = \frac{2v_0\sin\theta}{g}$; la **gittata** è $x(t_v) = \frac{v_0^2\sin 2\theta}{g}$, massima per $\theta = 45°$, e l'**altezza massima**, dove $v_y = 0$, è $\frac{v_0^2\sin^2\theta}{2g}$. Con $v_0 = 20$ m/s e $\theta = 30°$: tempo di volo $2{,}04$ s, gittata $35{,}3$ m, altezza massima $5{,}10$ m.

![Figura 1.1 · Traiettorie di un proiettile lanciato a 20 m/s con angoli diversi: la gittata è massima a 45° e uguale per angoli complementari.](figure/1-1.svg)

### 1.6 Moto circolare uniforme

Un punto percorre una circonferenza di raggio $R$ con celerità costante. Con l'origine nel centro e $\theta(t) = \omega t$, dove $\omega$ è la **velocità angolare** (in rad/s):
$$x(t) = R\cos(\omega t), \qquad y(t) = R\sin(\omega t).$$
Si verifica che $x^2 + y^2 = R^2$. Derivando:
$$v_x = -R\omega\sin(\omega t) = -\omega y, \qquad v_y = R\omega\cos(\omega t) = \omega x,$$
quindi la velocità è perpendicolare al raggio (tangente alla circonferenza) e ha modulo costante $v = \omega R$. Derivando ancora:
$$a_x = -\omega^2 x, \quad a_y = -\omega^2 y, \qquad \text{cioè} \quad a = -\omega^2 r.$$

> [!teorema] Accelerazione centripeta
> Nel moto circolare uniforme l'accelerazione è diretta verso il centro e ha modulo
> $$a_c = \omega^2 R = \frac{v^2}{R}.$$

Anche se la celerità è costante, la velocità cambia direzione, e quindi c'è accelerazione. Il **periodo**, il tempo di un giro, è $T = \frac{2\pi}{\omega}$, e la **frequenza** è $f = \frac1T$. Per esempio un punto a $0{,}5$ m dal centro di un disco che fa 2 giri al secondo ha $\omega = 4\pi \approx 12{,}6$ rad/s, $v = 2\pi \approx 6{,}28$ m/s e $a_c = \omega^2 R \approx 79$ m/s², circa $8g$.

### 1.7 Moti relativi

Lo stesso moto descritto da due osservatori diversi ha leggi orarie diverse. Siano $(O, x, y)$ un sistema considerato fisso e $(O', x', y')$ un sistema che trasla con velocità costante $v_0$ rispetto al primo, con gli assi paralleli e $O' = O$ all'istante 0. Le coordinate di un punto $P$ sono legate dalle **trasformazioni di Galileo**:
$$x_P = x'_P + v_{0x}t, \qquad y_P = y'_P + v_{0y}t.$$
Derivando si ottiene la **composizione delle velocità**
$$v_P = v'_P + v_0:$$
la velocità rispetto al sistema fisso è quella relativa più la velocità di trascinamento.

> [!teorema] Invarianza dell'accelerazione
> Se $v_0$ è costante, derivando $v_P = v'_P + v_0$ si trova $a_P = a'_P$: l'accelerazione è la stessa in due sistemi di riferimento che si muovono di moto rettilineo uniforme l'uno rispetto all'altro.

È il fatto che renderà le leggi della dinamica valide allo stesso modo in tutti i **sistemi inerziali** (modulo 2).

### Esempi ed esercizi svolti

**Esercizio 1 (attraversare un fiume).** Una barca attraversa un fiume largo 60 m puntando perpendicolarmente alla riva con velocità 3 m/s rispetto all'acqua; la corrente scorre a 4 m/s. Rispetto alla riva la velocità è la somma vettoriale $(4, 3)$ m/s, di modulo $\sqrt{16 + 9} = 5$ m/s. Il tempo di attraversamento dipende solo dalla componente perpendicolare alla riva: $\frac{60}{3} = 20$ s. In questo tempo la corrente trascina la barca di $4 \cdot 20 = 80$ m a valle.

**Esercizio 2 (dall'accelerazione alla legge oraria).** Un punto parte da fermo dall'origine con accelerazione $a(t) = 6t$ (in m/s², con $t$ in secondi). Integrando: $v(t) = \int_0^t 6s\, ds = 3t^2$ e $x(t) = \int_0^t 3s^2\, ds = t^3$. Dopo 2 s il punto è a 8 m con velocità 12 m/s. L'accelerazione non è costante, quindi le formule del moto uniformemente accelerato non valgono: si integra.

**Esercizio 3 (velocità e accelerazione nel moto circolare).** Nel moto circolare uniforme $r \cdot v = x v_x + y v_y = -\omega xy + \omega xy = 0$: la velocità è sempre perpendicolare al raggio. Allo stesso modo $v \cdot a = 0$: l'accelerazione è perpendicolare alla velocità, e infatti non cambia il modulo della velocità ma solo la direzione.

#### Esercizi dalle esercitazioni

> [!aggiunta] Aggiunta in revisione · fonte: esercitazioni 1 (24/02/2025) e 5 (20/03/2025) del corso, testi riformulati, con i risultati confrontati con quelli delle esercitazioni e con gli appunti a mano delle esercitazioni; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-01)
> Il metodo è sempre lo stesso: si fissa un sistema di riferimento con l'origine e il verso positivo, si scrive la legge oraria di ogni corpo, e si traduce la domanda in un'equazione ("si incontrano" vuol dire stessa posizione nello stesso istante).

**Esercizio 4. Prendere al volo un corpo che cade.** Un corpo B viene lasciato cadere da fermo da 120 m; nello stesso istante un corpo A, a 7 m dalla verticale di B, parte in moto rettilineo uniforme sul piano orizzontale. Con che velocità deve muoversi A per trovarsi sotto B quando B tocca terra?

B arriva a terra dopo $t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{240}{9{,}81}} = 4{,}95$ s. In questo tempo A deve percorrere 7 m: $v = \frac{7}{4{,}95} = 1{,}4$ m/s. I due moti sono indipendenti: li lega solo il tempo.

**Esercizio 5. Quanto è profondo il pozzo?** Si lascia cadere un sasso in un pozzo e si sente il tonfo dopo $T = 4{,}8$ s. La velocità del suono è 340 m/s.

Il tempo totale è la caduta più il ritorno del suono: $T = \sqrt{\frac{2h}{g}} + \frac{h}{v_s}$. Con $u = \sqrt{h}$ diventa un'equazione di secondo grado, $\frac{u^2}{v_s} + \sqrt{\frac{2}{g}}\,u - T = 0$, con la soluzione positiva $u = 9{,}98$, cioè $h = 99{,}6$ m. Trascurando il tempo del suono si troverebbe $h = \frac12 g T^2 = 113$ m, un errore del 13%.

**Esercizio 6. Il tempo minimo su un rettilineo.** Un'auto deve percorrere 2 km partendo e arrivando ferma, accelerando con $a_1 = 2$ m/s² e poi frenando con $|a_2| = 3$ m/s², senza tratti a velocità costante. Quale frazione del percorso fa accelerando, e in quanto tempo arriva?

La velocità massima $v$ si raggiunge al cambio. Accelerando si percorre $x_1 = \frac{v^2}{2a_1}$, frenando $x_2 = \frac{v^2}{2|a_2|}$: il rapporto è $\frac{x_1}{x_2} = \frac{|a_2|}{a_1} = \frac32$, quindi $x_1 = \frac35 L = 1200$ m, il 60%. Poi $v = \sqrt{2a_1 x_1} = 69{,}3$ m/s e il tempo è $\frac{v}{a_1} + \frac{v}{|a_2|} = 34{,}6 + 23{,}1 = 57{,}7$ s.

**Esercizio 7. La distanza minima per non tamponare.** L'auto A a 130 km/h è a distanza $d$ dietro l'auto B a 70 km/h, e frena con $|a| = 4$ m/s². Quanto deve valere almeno $d$?

Conviene mettersi nel riferimento di B, che si muove di moto uniforme ed è quindi inerziale rispetto alla strada: lì A ha velocità iniziale $\Delta v = 60$ km/h $= 16{,}7$ m/s e decelera con 4 m/s². Si ferma rispetto a B dopo $\frac{\Delta v^2}{2|a|} = 34{,}7$ m: è la distanza minima. Nel riferimento della strada si arriva allo stesso risultato imponendo che le posizioni coincidano quando le velocità diventano uguali, ma con più conti.

**Esercizio 8. Una legge oraria complicata.** Una particella si muove su una retta con $x(t) = ut(1 - 2\sin\omega t)$, $u = 3$ m/s, $\omega = 4$ s⁻¹. (a) Quando passa per l'origine? (b) Velocità media fra 0,5 s e 1 s e velocità istantanea nel punto medio. (c) Accelerazione al primo ritorno nell'origine.

(a) $x = 0$ per $t = 0$ oppure $\sin\omega t = \frac12$, cioè $\omega t = \frac{\pi}{6} + 2k\pi$ o $\frac{5\pi}{6} + 2k\pi$. Il primo ritorno è $t_1 = \frac{\pi}{24} = 0{,}131$ s.

(b) $x(1) = 3(1 - 2\sin 4) = 7{,}54$ m e $x(0{,}5) = 1{,}5(1 - 2\sin 2) = -1{,}23$ m (gli angoli in radianti), quindi $v_m = \frac{7{,}54 + 1{,}23}{0{,}5} = 17{,}5$ m/s. La velocità istantanea è $v(t) = u(1 - 2\sin\omega t) - 2u\omega t\cos\omega t$, e $v(0{,}75) = 20{,}0$ m/s: vicina ma diversa, perché il moto non è uniformemente accelerato.

(c) Derivando ancora, $a(t) = -4u\omega\cos\omega t + 2u\omega^2 t\sin\omega t$. In $t_1$, con $\cos\omega t_1 = \frac{\sqrt3}{2}$ e $\sin\omega t_1 = \frac12$: $a = -24\sqrt3 + 2\pi = -35{,}3$ m/s².

#### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove del 03/09/2025 e del 05/02/2026; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-01)

**Esercizio 9. Due leggi orarie.** Due punti su una retta hanno $x_1 = 3t$ e $x_2 = t^2 + 2$ (unità SI, $t \ge 0$). Quando sono nello stesso punto? Quando hanno la stessa velocità? E la stessa accelerazione?

Stesso punto: $t^2 - 3t + 2 = 0$, cioè $t = 1$ s e $t = 2$ s (il secondo punto supera il primo e poi viene superato). Stessa velocità: $3 = 2t$, $t = 1{,}5$ s, proprio a metà fra i due incontri, quando la distanza fra i due è massima. Stessa accelerazione: mai, perché $a_1 = 0$ e $a_2 = 2$ m/s².

**Esercizio 10. Due oscillatori che si scontrano.** Due punti si muovono su una retta con $x_1 = A\sin\omega t$ e $x_2 = A\cos\omega t$, $A = 1$ m, $\omega = 1$ s⁻¹. Descrivere i moti e trovare il primo istante $t > 0$ in cui si scontrano.

Sono due moti armonici con la stessa ampiezza e la stessa pulsazione, sfasati di un quarto di periodo: il primo parte dal centro, il secondo da un estremo. Si incontrano quando $\sin\omega t = \cos\omega t$, cioè $\tan\omega t = 1$: la prima volta per $\omega t = \frac{\pi}{4}$, $t = 0{,}785$ s, nel punto $x = \frac{\sqrt2}{2}$ m.

### Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-01)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Un proiettile lanciato da una terrazza.** Una palla è lanciata da 20 m di altezza con velocità 15 m/s a 30° sopra l'orizzontale. Dove cade e con che velocità?

*Passo 1: il riferimento.* Origine a terra sotto il punto di lancio, $x$ orizzontale, $y$ verso l'alto. Componenti iniziali: $v_{0x} = 15\cos 30° = 13{,}0$ m/s, $v_{0y} = 15\sin 30° = 7{,}5$ m/s.

*Passo 2: le leggi orarie.* $x = 13{,}0\,t$, $y = 20 + 7{,}5\,t - 4{,}905\,t^2$.

*Passo 3: il tempo di volo.* $y = 0$: $4{,}905t^2 - 7{,}5t - 20 = 0$, soluzione positiva $t = 2{,}92$ s.

*Passo 4: dove cade.* $x = 13{,}0 \cdot 2{,}92 = 38{,}0$ m.

*Passo 5: la velocità d'impatto.* $v_x = 13{,}0$ m/s, $v_y = 7{,}5 - 9{,}81 \cdot 2{,}92 = -21{,}1$ m/s, modulo 24,8 m/s. Con l'energia (modulo 3) si fa prima: $v = \sqrt{v_0^2 + 2gh} = \sqrt{225 + 392} = 24{,}8$ m/s.

**Guidato 2. Il moto circolare non uniforme.** Un punto parte da fermo su una circonferenza di raggio 2 m con accelerazione tangenziale costante $1$ m/s². Dopo quanto tempo l'accelerazione forma 45° con la velocità?

*Passo 1: le due componenti.* $a_t = 1$ m/s² costante; $a_n = \frac{v^2}{R}$ con $v = a_t t$.

*Passo 2: la condizione.* L'angolo con la velocità è 45° quando $a_n = a_t$: $\frac{t^2}{2} = 1$.

*Passo 3: risultato.* $t = \sqrt2 = 1{,}41$ s, con $v = 1{,}41$ m/s e $|a| = \sqrt2$ m/s².

**Guidato 3. Pioggia vista dal treno.** La pioggia cade verticale a 8 m/s. Un treno viaggia a 72 km/h. Che angolo fanno le gocce con la verticale, viste dal finestrino?

*Passo 1.* $v_{goccia,suolo} = (0, -8)$ m/s; $v_{treno} = (20, 0)$ m/s.

*Passo 2: la composizione.* $v_{goccia,treno} = v_{goccia,suolo} - v_{treno} = (-20, -8)$ m/s.

*Passo 3: l'angolo.* $\tan\varphi = \frac{20}{8}$, $\varphi = 68°$ dalla verticale, inclinate all'indietro.

### Riepilogo

La cinematica descrive il moto con la legge oraria $r(t)$ in un sistema di riferimento; la traiettoria è la curva percorsa, lo spostamento è la differenza fra le posizioni finale e iniziale, diverso in generale dalla distanza percorsa. Velocità e accelerazione istantanee sono le derivate prima e seconda della posizione, e si risale da esse alla posizione integrando. Nel moto rettilineo uniforme $x = x_0 + v_0 t$; in quello uniformemente accelerato $x = x_0 + v_0 t + \frac12 a_0 t^2$ e $v^2 = v_0^2 + 2a_0\Delta x$. Il moto del proiettile è la composizione di un moto uniforme orizzontale e di uno uniformemente accelerato verticale, con traiettoria parabolica, gittata $\frac{v_0^2\sin 2\theta}{g}$ e altezza massima $\frac{v_0^2\sin^2\theta}{2g}$. Nel moto circolare uniforme la velocità è tangente con modulo $\omega R$ e l'accelerazione è centripeta con modulo $\omega^2 R = \frac{v^2}{R}$. Passando a un sistema che trasla con velocità costante, le velocità si compongono per somma e l'accelerazione non cambia.

### Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FG1-01)
> Le formule della cinematica, con i termini per l'orale.

#### Definizioni

$$\vec v = \frac{d\vec r}{dt}, \qquad \vec a = \frac{d\vec v}{dt}, \qquad v_m = \frac{\Delta x}{\Delta t}, \qquad x(t) = x_0 + \int_0^t v\,dt', \qquad v\,dv = a\,dx.$$

#### Moti notevoli

| Moto | Leggi |
|---|---|
| Rettilineo uniforme | $x = x_0 + vt$ |
| Uniformemente accelerato | $x = x_0 + v_0 t + \frac12 at^2$, $v = v_0 + at$, $v^2 = v_0^2 + 2a(x - x_0)$ |
| Caduta libera da fermo | $t = \sqrt{2h/g}$, $v = \sqrt{2gh}$ |
| Proiettile | $x = v_0\cos\theta\,t$, $y = v_0\sin\theta\,t - \frac12 gt^2$; gittata $\frac{v_0^2\sin 2\theta}{g}$, altezza massima $\frac{v_0^2\sin^2\theta}{2g}$ |
| Circolare uniforme | $v = \omega R$, $a_c = \frac{v^2}{R} = \omega^2 R$, $T = \frac{2\pi}{\omega}$ |
| Circolare vario | $a_t = \frac{dv}{dt} = \alpha R$, $a_n = \frac{v^2}{R}$ |
| Armonico | $x = A\cos(\omega t + \varphi)$, $a = -\omega^2 x$ |
| Moti relativi | $\vec v = \vec v' + \vec v_O$ (traslazione), $\vec a = \vec a' + \vec a_O$ |

#### Termini per l'orale

| Termine | In una riga |
|---|---|
| Punto materiale | corpo di cui si trascurano le dimensioni |
| Sistema di riferimento | origine, assi e orologio rispetto a cui si descrive il moto |
| Traiettoria, legge oraria | curva percorsa; posizione in funzione del tempo |
| Spostamento | differenza fra posizione finale e iniziale, vettore |
| Velocità media, istantanea | rapporto incrementale; derivata della posizione |
| Accelerazione tangenziale, centripeta | cambia il modulo della velocità; cambia la direzione |
| Moto armonico | moto con $a = -\omega^2 x$, proiezione di un moto circolare uniforme |
| Composizione delle velocità | velocità assoluta = relativa + di trascinamento |

#### Domande che tornano spesso

- Definire velocità e accelerazione; come si passa dalla legge oraria all'accelerazione e viceversa?
- Ricavare le leggi del moto uniformemente accelerato e la relazione $v^2 = v_0^2 + 2a\Delta x$.
- Moto del proiettile: traiettoria parabolica, gittata, angolo di gittata massima.
- Accelerazione nel moto circolare: componenti tangenziale e normale.
- Moti relativi: composizione delle velocità per un riferimento in traslazione.

## 2 · Dinamica del punto materiale

**In questo modulo.** Si usano la cinematica del modulo 1 (velocità, accelerazione, moto circolare) e le equazioni differenziali più semplici. Si passa dalla descrizione del moto alle sue cause: i tre principi di Newton, la definizione operativa di forza e di massa, la forza peso e la gravitazione, le reazioni vincolari, le tensioni delle funi e le forze di attrito statico e dinamico. Si impara il metodo del diagramma di corpo libero e lo si applica al piano inclinato, ai corpi collegati da funi e carrucole, al moto circolare (forza centripeta, giro della morte) e alle oscillazioni della molla e del pendolo. Alla fine si sa impostare e risolvere le equazioni del moto di uno o più corpi collegati.

### 2.1 I principi della dinamica

La **forza** si definisce operativamente con un **dinamometro**: una molla tarata, il cui allungamento è proporzionale alla forza applicata. La forza è un vettore; più forze applicate allo stesso punto si sommano come vettori, e la loro somma è la **risultante** $F$.

> [!definizione] Primo principio (principio d'inerzia)
> Un corpo su cui non agisce alcuna forza risultante resta in quiete o si muove di moto rettilineo uniforme.

I sistemi di riferimento in cui vale il primo principio si dicono **inerziali**; per il modulo 1 ogni sistema che trasla con velocità costante rispetto a un sistema inerziale è ancora inerziale, perché le accelerazioni sono le stesse.

> [!definizione] Secondo principio
> In un sistema inerziale l'accelerazione di un corpo è proporzionale alla forza risultante che agisce su di esso e inversamente proporzionale alla sua massa:
> $$F = m a.$$

La forza si misura in **newton**, $1\ \mathrm{N} = 1\ \mathrm{kg \cdot m/s^2}$. La **massa** (inerziale) misura la resistenza del corpo a cambiare il suo stato di moto: sottoponendo due corpi alla stessa forza si misurano accelerazioni $a_1 = \frac{F}{m_1}$ e $a_2 = \frac{F}{m_2}$, da cui $m_2 = m_1\frac{a_1}{a_2}$; scelto un campione di 1 kg, si può così misurare qualsiasi massa. Proiettando sugli assi, il secondo principio diventa un sistema di equazioni differenziali:
$$m\frac{d^2x}{dt^2} = F_x, \qquad m\frac{d^2y}{dt^2} = F_y, \qquad m\frac{d^2z}{dt^2} = F_z,$$
che, con la posizione e la velocità iniziali, determinano il moto.

> [!esempio] Accelerare un'automobile
> Per portare un'auto di 1500 kg da ferma a 100 km/h in 20 s con forza costante: $v = \frac{100}{3{,}6} \approx 27{,}8$ m/s, $a = \frac{27{,}8}{20} \approx 1{,}39$ m/s², quindi $F = ma \approx 2{,}08 \cdot 10^3$ N.

> [!definizione] Terzo principio (azione e reazione)
> Se un corpo 1 esercita una forza $F_{1 \to 2}$ su un corpo 2, il corpo 2 esercita sul corpo 1 una forza uguale e opposta: $F_{2 \to 1} = -F_{1 \to 2}$.

Le due forze agiscono su corpi diversi, quindi non si annullano a vicenda: si annullano solo quando si sommano le forze su un sistema che contiene entrambi i corpi (modulo 3).

### 2.2 Forza peso e reazioni vincolari

Due masse puntiformi $m_1$ e $m_2$ a distanza $r$ si attraggono con la forza di **gravitazione universale**
$$F = G\frac{m_1 m_2}{r^2}, \qquad G \approx 6{,}67 \cdot 10^{-11}\ \mathrm{N\,m^2/kg^2},$$
diretta lungo la congiungente. Vicino alla superficie terrestre l'attrazione della Terra su un corpo di massa $m$ è la **forza peso** $F_p = mg$, verticale verso il basso, con $g \approx 9{,}8$ m/s².

Quando un corpo è appoggiato a una superficie o vincolato in altro modo, il vincolo esercita una **reazione vincolare** che impedisce al corpo di attraversarlo. Se il contatto è liscio (senza attrito), la reazione è perpendicolare alla superficie e si chiama **reazione normale** $N$; il suo valore non è dato a priori, ma è quello che serve per rispettare il vincolo.

**Metodo del diagramma di corpo libero.** Per ogni problema di dinamica:

1. si individuano i corpi di cui studiare il moto;
2. per ciascuno si disegnano tutte le forze che agiscono su di esso (peso, reazioni, tensioni, attriti, forze applicate);
3. si scelgono assi comodi (per esempio uno parallelo al moto);
4. si scrive $F = ma$ in componenti, aggiungendo le relazioni imposte dai vincoli (accelerazioni nulle in una direzione, accelerazioni uguali per corpi legati da una fune).

### 2.3 Piano inclinato e tensioni

> [!esempio] Piano inclinato liscio
> Un blocco di massa $m$ è su un piano inclinato liscio di angolo $\theta$. Con l'asse $x$ lungo il piano (verso il basso) e $y$ perpendicolare, il peso ha componenti $mg\sin\theta$ e $-mg\cos\theta$. Il blocco non si stacca dal piano, quindi $a_y = 0$:
> $$ma_x = mg\sin\theta, \qquad N - mg\cos\theta = 0 \quad \Longrightarrow \quad a_x = g\sin\theta, \quad N = mg\cos\theta.$$
> Con $\theta = 30°$, $a = 4{,}9$ m/s². La reazione normale è minore del peso.

Una **fune ideale** è inestensibile e di massa trascurabile: trasmette una forza di trazione diretta lungo la fune, la **tensione** $T$, che ha lo stesso valore in ogni punto. Due corpi collegati da una fune tesa hanno accelerazioni di uguale modulo. Una **carrucola ideale** (senza massa e senza attrito) cambia la direzione della fune senza cambiare la tensione.

> [!esempio] Due scatole trascinate
> Due scatole A e B di masse $m_A$ e $m_B$, su un tavolo liscio, sono collegate da una fune; ad A si applica una forza orizzontale $F$. In verticale le normali bilanciano i pesi; in orizzontale le due scatole hanno la stessa accelerazione $a$:
> $$m_A a = F - T, \qquad m_B a = T.$$
> Sommando si elimina la tensione: $a = \frac{F}{m_A + m_B}$, e poi $T = \frac{m_B F}{m_A + m_B}$. Con $m_A = 2$ kg, $m_B = 3$ kg e $F = 10$ N: $a = 2$ m/s² e $T = 6$ N. La fune tira B con una forza minore di $F$, perché $F$ deve accelerare anche A.

### 2.4 Forze di attrito

Fra superfici ruvide la reazione del vincolo ha anche una componente parallela alla superficie, l'**attrito**.

> [!definizione] Attrito dinamico e statico
>
> - **Attrito dinamico**: se le superfici strisciano l'una sull'altra, la forza di attrito ha verso opposto alla velocità relativa e modulo $F_A = \mu_d N$, dove $\mu_d$ è il **coefficiente di attrito dinamico**.
> - **Attrito statico**: se le superfici sono in quiete relativa, l'attrito è la forza, parallela alla superficie, che serve a mantenerle ferme, fino a un valore massimo: $F_s \le \mu_s N$, con $\mu_s$ **coefficiente di attrito statico**.
>
> In generale $\mu_s > \mu_d$: è più faticoso mettere in moto un corpo che mantenerlo in moto.

La relazione $F_A = \mu_d N$ vale fra i moduli: i due vettori sono perpendicolari. L'attrito statico, come la reazione normale, si adatta alle altre forze; la disuguaglianza dice solo fino a dove può arrivare.

> [!esempio] Piano inclinato scabro
> Un blocco fermo su un piano inclinato di angolo $\theta$ resta fermo finché la componente del peso lungo il piano non supera l'attrito statico massimo:
> $$mg\sin\theta \le \mu_s mg\cos\theta \quad \Longleftrightarrow \quad \tan\theta \le \mu_s.$$
> L'**angolo di attrito** $\arctan\mu_s$ non dipende dalla massa: con $\mu_s = 0{,}5$ è circa $26{,}6°$. Quando il blocco scivola, lungo il piano agiscono $mg\sin\theta$ verso il basso e $\mu_d mg\cos\theta$ verso l'alto, quindi $a = g(\sin\theta - \mu_d\cos\theta)$: con $\theta = 30°$ e $\mu_d = 0{,}2$, $a \approx 3{,}20$ m/s².

### 2.5 Dinamica del moto circolare

Per il modulo 1, un corpo in moto circolare uniforme ha accelerazione centripeta $\frac{v^2}{R}$. Per il secondo principio deve quindi agire una forza risultante diretta verso il centro, la **forza centripeta**:
$$F_c = m\frac{v^2}{R} = m\omega^2 R.$$
Non è un nuovo tipo di forza: è la componente radiale della risultante delle forze presenti (una tensione, il peso, una reazione, l'attrito delle gomme in curva).

> [!esempio] Giro della morte con una fune
> Un corpo di massa $m$ ruota su una circonferenza verticale di raggio $R$ legato a una fune. Nel punto più alto sia il peso sia la tensione puntano verso il centro (in basso):
> $$m\frac{v^2}{R} = mg + T \quad \Longrightarrow \quad T = m\frac{v^2}{R} - mg.$$
> La fune resta tesa se $T \ge 0$, cioè se $v \ge \sqrt{gR}$. Con $R = 1$ m la velocità minima in cima è $\sqrt{9{,}8} \approx 3{,}13$ m/s; con $m = 0{,}5$ kg e $v = 4$ m/s la tensione è $0{,}5 \cdot 16 - 0{,}5 \cdot 9{,}8 = 3{,}1$ N.

### 2.6 Oscillazioni: molla e pendolo

Una molla di costante elastica $k$ (in N/m) esercita sul corpo attaccato all'estremo una forza di richiamo proporzionale all'allungamento rispetto alla lunghezza a riposo (**legge di Hooke**): $F = -kx$, con $x$ la deformazione.

> [!teorema] Oscillatore armonico
> Una massa $m$ attaccata a una molla, su un piano orizzontale liscio, ha equazione del moto $m\ddot x = -kx$, cioè $\ddot x = -\omega^2 x$ con $\omega = \sqrt{\frac{k}{m}}$. Le soluzioni sono
> $$x(t) = A\cos(\omega t + \phi), \qquad T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}.$$

L'ampiezza $A$ e la fase $\phi$ dipendono dalle condizioni iniziali, la **pulsazione** $\omega$ e il periodo no. Con $k = 200$ N/m e $m = 0{,}5$ kg si ha $\omega = 20$ rad/s e $T \approx 0{,}314$ s.

> [!teorema] Pendolo semplice
> Una massa $m$ appesa a un filo ideale di lunghezza $L$, spostata di un angolo $\theta$ dalla verticale, ha accelerazione tangenziale $L\ddot\theta = -g\sin\theta$. Per **piccole oscillazioni** ($\sin\theta \approx \theta$) l'equazione diventa quella dell'oscillatore armonico, $\ddot\theta = -\frac{g}{L}\theta$, e
> $$\theta(t) = \theta_0\cos\left(\sqrt{\tfrac{g}{L}}\, t + \phi\right), \qquad T = 2\pi\sqrt{\frac{L}{g}}.$$

Il periodo non dipende né dalla massa né, per piccole oscillazioni, dall'ampiezza (isocronismo): un pendolo lungo 1 m ha periodo di circa 2 s. Lungo il filo, la tensione bilancia la componente radiale del peso e fornisce la forza centripeta.

### Esempi ed esercizi svolti

**Esercizio 1 (piano inclinato e massa appesa).** Un blocco $m_1 = 4$ kg su un piano inclinato di $30°$ con $\mu_d = 0{,}2$ è collegato con una fune, attraverso una carrucola in cima al piano, a una massa $m_2 = 3$ kg che pende in verticale. Se $m_2$ scende, il blocco sale lungo il piano e l'attrito è rivolto verso il basso. Le equazioni, con l'accelerazione comune $a$ positiva nel verso del moto, sono
$$m_2 a = m_2 g - T, \qquad m_1 a = T - m_1 g\sin\theta - \mu_d m_1 g\cos\theta.$$
Sommando: $a = \frac{m_2 g - m_1 g\sin\theta - \mu_d m_1 g\cos\theta}{m_1 + m_2} = \frac{29{,}4 - 19{,}6 - 6{,}79}{7} \approx 0{,}43$ m/s², positiva, quindi il moto avviene davvero nel verso supposto. La tensione è $T = m_2(g - a) \approx 28{,}1$ N.

**Esercizio 2 (peso apparente in ascensore).** Una persona di 70 kg è su una bilancia in un ascensore che accelera verso l'alto con $a = 2$ m/s². Sulla persona agiscono il peso e la reazione $N$ della bilancia: $N - mg = ma$, quindi $N = m(g + a) = 70 \cdot 11{,}8 = 826$ N. La bilancia, che misura $N$, segna circa 84 kg. In discesa accelerata segnerebbe meno, e in caduta libera zero.

**Esercizio 3 (curva piana).** Un'auto percorre una curva piana di raggio 50 m. La forza centripeta è l'attrito statico fra gomme e asfalto, al più $\mu_s mg$. Deve essere $m\frac{v^2}{R} \le \mu_s mg$, cioè $v \le \sqrt{\mu_s g R}$: con $\mu_s = 0{,}8$, $v \le \sqrt{0{,}8 \cdot 9{,}8 \cdot 50} \approx 19{,}8$ m/s (circa 71 km/h), indipendentemente dalla massa.

#### Esercizi dalle esercitazioni

> [!aggiunta] Aggiunta in revisione · fonte: esercitazioni 3 (13/03/2025) e 6 (03/04/2025) del corso, testi riformulati, con i risultati confrontati con quelli delle esercitazioni; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-01, FG1-05)
> Per ogni corpo si disegna il diagramma delle forze, si scelgono gli assi (lungo il piano e perpendicolare, se c'è un piano inclinato) e si scrive $\vec F = m\vec a$ componente per componente. Le reazioni vincolari e le tensioni sono incognite come le accelerazioni.

**Esercizio 4. Fin dove si può inclinare il piano?** Un corpo sta su un piano inclinato scabro con $\mu_s = 0{,}3$ e $\mu_d = 0{,}2$, all'altezza $h = 2$ m. (a) Angolo massimo $\alpha_0$ di equilibrio. (b) Accelerazione e tempo di discesa se il piano è inclinato di $2\alpha_0$.

(a) In equilibrio, lungo il piano $mg\sin\alpha = f_s$ e perpendicolarmente $N = mg\cos\alpha$. Con $f_s \le \mu_s N$ si ottiene $\tan\alpha \le \mu_s$: $\alpha_0 = \arctan 0{,}3 = 16{,}7°$. Non dipende dalla massa.

(b) Con $\alpha = 33{,}4°$ il corpo scivola e l'attrito è dinamico: $a = g(\sin\alpha - \mu_d\cos\alpha) = 9{,}81(0{,}551 - 0{,}2 \cdot 0{,}835) = 3{,}76$ m/s². Il tratto è $\frac{h}{\sin\alpha} = 3{,}63$ m, percorso partendo da fermo in $t = \sqrt{\frac{2 \cdot 3{,}63}{3{,}76}} = 1{,}39$ s.

**Esercizio 5. Due masse legate che scivolano.** Due corpi uguali di massa $m$, legati da una fune, scivolano su un piano inclinato di $\alpha$; solo il corpo 1 ha attrito ($\mu_d$), il corpo 2 no, e sta più in basso (così la fune resta tesa). Trovare la tensione e l'angolo per cui scendono a velocità costante.

Con la stessa accelerazione $a$ lungo il piano, verso il basso: corpo 1, $ma = mg\sin\alpha - \mu_d mg\cos\alpha + T$; corpo 2, $ma = mg\sin\alpha - T$ (la fune frena il corpo senza attrito e tira quello con attrito). Sottraendo, $0 = -\mu_d mg\cos\alpha + 2T$:
$$T = \frac12\mu_d mg\cos\alpha.$$
Sommando, $2ma = 2mg\sin\alpha - \mu_d mg\cos\alpha$, e $a = 0$ per $\tan\alpha = \frac{\mu_d}{2}$. Il sistema si comporta come un unico corpo con coefficiente d'attrito dimezzato.

**Esercizio 6. Il seggiolino della giostra.** Un seggiolino di 5 kg è appeso a una fune di 5 m attaccata alla cima di un palo che ruota con $\omega = 1{,}5$ rad/s; l'angolo fra fune e palo è costante. Distanza dal palo e tensione.

Il seggiolino fa un moto circolare uniforme di raggio $r = L\sin\theta$. In verticale $T\cos\theta = mg$; in orizzontale la componente della tensione verso il palo è la forza centripeta, $T\sin\theta = m\omega^2 L\sin\theta$. Dalla seconda $T = m\omega^2 L = 56{,}3$ N, e dalla prima $\cos\theta = \frac{g}{\omega^2 L} = 0{,}872$, $\theta = 29{,}3°$, $r = 5\sin\theta = 2{,}45$ m. È il **pendolo conico**: c'è una soluzione con $\theta \ne 0$ solo se $\omega^2 > \frac{g}{L}$.

**Esercizio 7. Molle in serie e in parallelo, e la pistola giocattolo.** (a) Costante equivalente di due molle $k_1$, $k_2$ in serie e in parallelo e periodo di una massa $m$ attaccata. (b) Una pistola a molla si carica con una forza massima di 10 N; si aggiunge una seconda molla uguale alla prima ($k = 200$ N/m). Conviene metterla in serie o in parallelo per sparare più veloce un proiettile di 50 g?

(a) In **parallelo** le molle si allungano dello stesso tratto e le forze si sommano: $k_p = k_1 + k_2$. In **serie** trasmettono la stessa forza e gli allungamenti si sommano: $\frac{1}{k_s} = \frac{1}{k_1} + \frac{1}{k_2}$. Il periodo è $T = 2\pi\sqrt{m/k_{eq}}$.

(b) A forza massima fissata $F$, la molla equivalente si comprime di $\frac{F}{k_{eq}}$ e immagazzina $E = \frac{F^2}{2k_{eq}}$: conviene la costante più piccola. In serie $k_s = 100$ N/m ed $E = 0{,}5$ J, quindi $v = \sqrt{2E/m} = 4{,}47$ m/s; in parallelo $k_p = 400$ N/m, $E = 0{,}125$ J, $v = 2{,}24$ m/s; con una molla sola $v = 3{,}16$ m/s. In serie: la molla più "morbida" a parità di forza si carica di più.

#### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizio nuovo sul modello della prova del 05/02/2026, con dati diversi; soluzione verificata con `strumenti/verifica_ampliamento.py` (FG1-01, FG1-05, FG1-07)

**Esercizio 8. Una massa che gira attaccata a una molla.** Su un piano orizzontale liscio un punto di 200 g, attaccato a una molla di lunghezza a riposo 10 cm e $k = 50$ N/m fissata al centro, fa un moto circolare uniforme con periodo 0,5 s. (a) Allungamento della molla. (b) Energia meccanica. (c) Momento angolare rispetto al centro.

(a) La forza elastica è la forza centripeta: $k(l - l_0) = m\omega^2 l$, con $\omega = \frac{2\pi}{T} = 12{,}57$ rad/s e $m\omega^2 = 31{,}6$ N/m. Quindi $l = \frac{kl_0}{k - m\omega^2} = \frac{5}{18{,}4} = 0{,}271$ m, allungamento $0{,}171$ m. Se fosse $m\omega^2 \ge k$ non ci sarebbe soluzione: la molla non riuscirebbe a trattenere il punto.

(b) $E = \frac12 m(\omega l)^2 + \frac12 k(l - l_0)^2 = 1{,}16 + 0{,}74 = 1{,}90$ J.

(c) $L = m l^2\omega = 0{,}185$ kg·m²/s, perpendicolare al piano; per un moto in senso orario visto dall'alto, per la regola della mano destra, è diretto verso il basso.

### Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: il guidato 1 è l'esercizio 3 dell'esercitazione 3 (13/03/2025), testo riformulato; gli altri sono nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-01, FG1-05)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Si muove o no?** Una massa $m_1 = 5$ kg su un piano inclinato di 30° ($\mu_s = 0{,}5$, $\mu_d = 0{,}3$) è legata, con una fune che passa su una carrucola ideale in cima al piano, a una massa $m_2 = 10$ kg appesa. Le masse partono ferme: si muovono? Con che accelerazione?

*Passo 1: chi vince senza attrito.* Il peso di $m_2$ tira con $m_2 g = 98{,}1$ N; la componente del peso di $m_1$ lungo il piano tira dall'altra parte con $m_1 g\sin 30° = 24{,}5$ N. Se si muovono, $m_2$ scende.

*Passo 2: il test dell'attrito statico.* L'attrito si oppone al moto incipiente, quindi verso il basso del piano, al più $\mu_s m_1 g\cos 30° = 21{,}2$ N. Le forze che trattengono valgono al più $24{,}5 + 21{,}2 = 45{,}8$ N $< 98{,}1$ N: si muovono.

*Passo 3: le equazioni con l'attrito dinamico.* $m_2 a = m_2 g - T$; $m_1 a = T - m_1 g\sin 30° - \mu_d m_1 g\cos 30°$.

*Passo 4: sommare.* $a = \frac{98{,}1 - 24{,}5 - 12{,}7}{15} = 4{,}06$ m/s², e $T = m_2(g - a) = 57{,}5$ N.

**Guidato 2. La curva sopraelevata.** Con che inclinazione va costruita una curva di raggio 100 m perché un'auto a 72 km/h la percorra senza bisogno di attrito?

*Passo 1: le forze.* Peso e reazione normale, perpendicolare alla strada inclinata di $\theta$.

*Passo 2: le equazioni.* In verticale $N\cos\theta = mg$; in orizzontale $N\sin\theta = m\frac{v^2}{R}$.

*Passo 3: dividere.* $\tan\theta = \frac{v^2}{gR} = \frac{400}{981}$, $\theta = 22{,}2°$. Non dipende dalla massa: va bene per tutte le auto alla stessa velocità.

**Guidato 3. Il pendolo: periodo e tensione.** Un pendolo di 0,8 m e massa $m$ è lasciato da fermo a 60° dalla verticale. Periodo delle piccole oscillazioni e tensione nel punto più basso.

*Passo 1: il periodo.* Per piccole oscillazioni $T = 2\pi\sqrt{L/g} = 1{,}79$ s. A 60° le oscillazioni non sono piccole e il periodo vero è un po' più lungo.

*Passo 2: la velocità in basso.* Con l'energia: $v^2 = 2gL(1 - \cos 60°) = gL$.

*Passo 3: la tensione.* In basso $T - mg = m\frac{v^2}{L} = mg$, quindi $T = 2mg$: il filo deve reggere il doppio del peso.

### Riepilogo

I principi di Newton dicono che senza forza risultante un corpo mantiene il suo stato di moto, che la forza risultante produce un'accelerazione $a = F/m$, e che le forze fra due corpi sono uguali e opposte. La massa misura l'inerzia, la forza si misura in newton e si definisce con il dinamometro. Vicino alla Terra il peso è $mg$; i vincoli esercitano reazioni normali e, se ruvidi, attriti: dinamico, $\mu_d N$ opposto al moto, e statico, fino a $\mu_s N$, che si adatta per impedire lo scivolamento (un corpo su un piano inclinato resta fermo se $\tan\theta \le \mu_s$). Le funi ideali trasmettono la stessa tensione e impongono la stessa accelerazione ai corpi collegati. Ogni problema si imposta con il diagramma di corpo libero e $F = ma$ in componenti. Un moto circolare richiede una forza centripeta $mv^2/R$ fornita dalle forze presenti. La forza elastica $-kx$ produce oscillazioni armoniche con periodo $2\pi\sqrt{m/k}$, e il pendolo semplice, per piccole oscillazioni, oscilla con periodo $2\pi\sqrt{L/g}$.

### Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FG1-01, FG1-05)
> Principi, forze e oscillazioni, con i termini per l'orale.

#### Principi e forze

$$\vec F = m\vec a, \qquad \vec F_{12} = -\vec F_{21}, \qquad P = mg, \qquad f_s \le \mu_s N, \qquad f_d = \mu_d N, \qquad F_{el} = -k\,\Delta x, \qquad F_c = m\frac{v^2}{R}.$$

| Situazione | Risultato |
|---|---|
| Piano inclinato liscio | $a = g\sin\alpha$ |
| Piano inclinato scabro, discesa | $a = g(\sin\alpha - \mu_d\cos\alpha)$ |
| Equilibrio limite sul piano | $\tan\alpha_0 = \mu_s$ |
| Curva piana | $v_{max} = \sqrt{\mu_s g R}$ |
| Curva sopraelevata senza attrito | $\tan\theta = \frac{v^2}{gR}$ |
| Pendolo conico | $T = m\omega^2 L$, $\cos\theta = \frac{g}{\omega^2 L}$ |
| Giro della morte, punto più alto | $v_{min} = \sqrt{gR}$ |

#### Oscillazioni

$$m\ddot x = -kx \Rightarrow x = A\cos(\omega t + \varphi),\ \omega = \sqrt{\frac{k}{m}}, \qquad \text{pendolo: } \omega = \sqrt{\frac{g}{L}} \text{ per piccole oscillazioni},$$

$$k_{parallelo} = k_1 + k_2, \qquad \frac{1}{k_{serie}} = \frac{1}{k_1} + \frac{1}{k_2}.$$

#### Termini per l'orale

| Termine | In una riga |
|---|---|
| Sistema inerziale | riferimento in cui vale il primo principio |
| Massa inerziale | resistenza di un corpo a cambiare velocità |
| Reazione vincolare | forza che il vincolo esercita per impedire certi moti |
| Attrito statico, dinamico | si oppone al moto incipiente / al moto relativo |
| Forza centripeta | risultante delle forze diretta verso il centro nel moto circolare |
| Forza apparente | termine $-m\vec a_O$ che compare in un riferimento accelerato |
| Moto armonico | soluzione di $\ddot x = -\omega^2 x$ |
| Isocronismo | il periodo delle piccole oscillazioni non dipende dall'ampiezza |

#### Domande che tornano spesso

- Enunciare i tre principi della dinamica; che cos'è un sistema inerziale?
- Differenza fra attrito statico e dinamico; perché $f_s$ è una disuguaglianza?
- Ricavare il moto armonico della molla e il periodo del pendolo per piccole oscillazioni.
- Che cosa fornisce la forza centripeta in una curva, in un pendolo conico, in un satellite?
- Peso apparente in un ascensore accelerato.

## 3 · Lavoro, energia, quantità di moto e sistemi

**In questo modulo.** Servono la dinamica del modulo 2, il prodotto scalare fra vettori e gli integrali; per le forze conservative anche il gradiente (Analisi 1B). Si introducono due modi di risolvere i problemi di dinamica senza integrare le equazioni del moto. Il primo è l'energia: lavoro di una forza, energia cinetica e teorema dell'energia cinetica, forze conservative ed energia potenziale, conservazione dell'energia meccanica, punti di equilibrio, forze dissipative e potenza. Il secondo è la quantità di moto: impulso, conservazione nei sistemi isolati, urti. Infine si passa dal punto ai sistemi di punti: forze interne ed esterne, prima equazione cardinale, centro di massa e teorema di König. Alla fine si sanno usare i teoremi di conservazione per risolvere problemi di cadute, molle, urti e sistemi.

### 3.1 Lavoro ed energia cinetica

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

### 3.2 Forze conservative ed energia potenziale

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

### 3.3 Forze non conservative e potenza

In presenza di attriti o resistenze l'energia meccanica non si conserva: la sua variazione è il lavoro delle forze non conservative,
$$\Delta E = (T_f + U_f) - (T_i + U_i) = L_{nc},$$
che per l'attrito è negativo (l'energia si trasforma in calore).

> [!definizione] Potenza
> La **potenza** è il lavoro fatto nell'unità di tempo. Quella media è $\bar P = \frac{L}{\Delta t}$, quella istantanea
> $$P = \frac{dL}{dt} = F \cdot v.$$
> Si misura in **watt**, $1\ \mathrm{W} = 1\ \mathrm{J/s}$.

Un'auto che va a velocità costante di 20 m/s contro una resistenza totale di 500 N deve sviluppare $P = 500 \cdot 20 = 10$ kW.

### 3.4 Quantità di moto e urti

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

### 3.5 Sistemi di punti e centro di massa

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

### Esempi ed esercizi svolti

**Esercizio 1 (una molla che lancia un blocco).** Una molla con $k = 200$ N/m, compressa di 10 cm, lancia un blocco di $0{,}5$ kg su un piano liscio. L'energia elastica $\frac12 k\Delta x^2 = 1$ J diventa tutta cinetica: $\frac12 \cdot 0{,}5 \cdot v^2 = 1$, quindi $v = 2$ m/s. Se dopo la molla c'è un tratto con attrito $\mu_d = 0{,}2$, il blocco si ferma quando il lavoro dell'attrito $\mu_d mg\,d$ ha consumato quel joule: $d = \frac{1}{0{,}2 \cdot 0{,}5 \cdot 9{,}8} \approx 1{,}02$ m.

**Esercizio 2 (pendolo balistico).** Un proiettile di 10 g a 300 m/s si conficca in un blocco di 2 kg appeso a un filo. Nell'urto, completamente anelastico, si conserva la quantità di moto: $V = \frac{0{,}01 \cdot 300}{2{,}01} \approx 1{,}49$ m/s. Dopo l'urto si conserva l'energia meccanica, e il blocco sale fino a $h = \frac{V^2}{2g} \approx 11{,}4$ cm. Misurando $h$ si risale alla velocità del proiettile; non si può usare l'energia nell'urto, dove quasi tutta l'energia cinetica del proiettile si dissipa.

**Esercizio 3 (esplosione).** Un oggetto fermo esplode in due frammenti di masse $m$ e $2m$. La quantità di moto totale resta nulla, quindi i frammenti partono in versi opposti e il più leggero ha velocità doppia. Il centro di massa resta fermo (o, se l'oggetto era in volo, prosegue sulla sua parabola).

#### Esercizi dalle esercitazioni

> [!aggiunta] Aggiunta in revisione · fonte: esercitazioni 4 (19/03/2025), 6 (03/04/2025) e 8 (14/04/2025) del corso, testi riformulati; l'esercizio 10 è il problema M1 della prova di luglio 2016 svolto in esercitazione; risultati confrontati con quelli delle esercitazioni e verificati con `strumenti/verifica_ampliamento.py` (FG1-02, FG1-04, FG1-06)
> Prima di scrivere equazioni conviene chiedersi che cosa si conserva: l'energia meccanica se lavorano solo forze conservative, la quantità di moto se la risultante delle forze esterne è nulla (in un urto, per la sua breve durata, quasi sempre), nessuna delle due se ci sono attriti e forze esterne.

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

#### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizio nuovo sul modello del problema M1 della prova di febbraio 2025 svolto in esercitazione, con dati diversi; soluzione verificata con `strumenti/verifica_ampliamento.py` (FG1-04, FG1-05)

**Esercizio 11. Molla, piano inclinato e attrito.** Un corpo di 0,4 kg è appoggiato alla base di un piano inclinato di 30° contro una molla ($k = 100$ N/m) compressa di 20 cm. Lasciato libero, risale con $\mu_d = 0{,}15$. (a) Velocità quando la molla torna a riposo. (b) Distanza totale percorsa in salita.

(a) Nei primi 20 cm la molla cede $\frac12 kx^2 = 2$ J; il peso assorbe $mg\sin 30° \cdot 0{,}2 = 0{,}392$ J e l'attrito dissipa $\mu_d mg\cos 30° \cdot 0{,}2 = 0{,}102$ J. Restano $1{,}506$ J di energia cinetica: $v = \sqrt{\frac{2 \cdot 1{,}506}{0{,}4}} = 2{,}74$ m/s.

(b) Su tutta la salita, lunga $s$: $2 = (mg\sin 30° + \mu_d mg\cos 30°)\,s = 2{,}47\,s$, quindi $s = 0{,}81$ m dal punto di partenza. Se $\tan 30° = 0{,}577 > \mu_s$ il corpo poi ridiscende: va controllato con l'attrito statico, che il testo dovrebbe dare.

### Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-02, FG1-04, FG1-06)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

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

### Riepilogo

Il lavoro di una forza è l'integrale $\int F \cdot dl$, e il lavoro della risultante è uguale alla variazione dell'energia cinetica $\frac12 mv^2$. Una forza è conservativa se il suo lavoro dipende solo dagli estremi; allora si definisce un'energia potenziale ($mgz$ per il peso, $\frac12 k\Delta x^2$ per la molla) con $F = -\nabla U$, e l'energia meccanica $T + U$ si conserva. Gli equilibri sono i punti stazionari di $U$, stabili nei minimi. Le forze non conservative cambiano l'energia meccanica del loro lavoro; la potenza è $F \cdot v$. La quantità di moto $mv$ varia dell'impulso delle forze e si conserva nei sistemi isolati; negli urti si conserva sempre, mentre l'energia cinetica si conserva solo negli urti elastici e si perde al massimo in quelli completamente anelastici. Per un sistema di punti le forze interne si annullano: la quantità di moto totale varia per le sole forze esterne e il centro di massa si muove come un punto con tutta la massa. Per il teorema di König l'energia cinetica è quella del centro di massa più quella del moto relativo.

### Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FG1-02, FG1-04, FG1-06)
> Lavoro, energia, quantità di moto, urti e sistemi, con i termini per l'orale.

#### Lavoro ed energia

$$W = \int_A^B \vec F \cdot d\vec r, \qquad K = \frac12 mv^2, \qquad W_{tot} = \Delta K, \qquad W_{cons} = -\Delta U, \qquad \Delta(K + U) = W_{nc}, \qquad P = \frac{dW}{dt} = \vec F \cdot \vec v.$$

| Forza | Energia potenziale |
|---|---|
| Peso | $U = mgh$ |
| Elastica | $U = \frac12 k x^2$ |
| Gravitazionale | $U = -\frac{GMm}{r}$ |
| Nel piano, conservativa | $\vec F = -\nabla U$, con $\partial_y F_x = \partial_x F_y$ |

#### Quantità di moto e urti

$$\vec p = m\vec v, \qquad \vec J = \int \vec F\,dt = \Delta\vec p, \qquad \vec F_{ext} = \frac{d\vec P}{dt} = M\vec a_{CM}.$$

| Urto (1D, $m_2$ fermo) | Risultato |
|---|---|
| Completamente anelastico | $V = \frac{m_1 v_1}{m_1 + m_2}$, energia persa $\frac{m_2}{m_1 + m_2}K_1$ |
| Elastico | $v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1$, $v_2' = \frac{2m_1}{m_1 + m_2}v_1$ |
| Elastico, masse uguali | si scambiano le velocità |

#### Sistemi di punti

$$\vec r_{CM} = \frac{\sum m_i\vec r_i}{M}, \qquad \vec v_{CM} = \frac{\vec P}{M}, \qquad K = \frac12 Mv_{CM}^2 + K' \ \text{(König)}.$$

#### Termini per l'orale

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

#### Domande che tornano spesso

- Dimostrare il teorema dell'energia cinetica.
- Definire una forza conservativa; perché l'attrito non lo è?
- Conservazione dell'energia meccanica e sua estensione con le forze non conservative.
- Teorema dell'impulso e conservazione della quantità di moto per un sistema isolato.
- Urti elastici e anelastici in una dimensione: ricavare le velocità finali.
- Moto del centro di massa e teorema di König.

## 4 · Corpo rigido e momento angolare

**In questo modulo.** Servono il moto circolare del modulo 1, la dinamica del modulo 2, l'energia e i sistemi di punti del modulo 3, il prodotto vettoriale e gli integrali multipli. Si studia il corpo rigido: gradi di libertà, cinematica delle rotazioni attorno a un asse fisso, energia cinetica di rotazione e momento d'inerzia, con il teorema di Huygens-Steiner e il calcolo dei momenti d'inerzia di asta, anello, disco e sfera. Poi la dinamica: momento di una forza, seconda equazione cardinale, puro rotolamento, macchina di Atwood con carrucola massiva. Infine il momento angolare rispetto a un polo e la sua conservazione, le forze centrali con la legge delle aree, e le condizioni di equilibrio di un corpo rigido. Alla fine si sanno risolvere problemi di rotazione e rotolamento, con le equazioni cardinali e con l'energia.

### 4.1 Corpo rigido e rotazioni

> [!definizione] Corpo rigido
> Un **corpo rigido** è un sistema di punti materiali in cui le distanze fra due punti qualsiasi restano costanti nel tempo.

Un punto materiale libero ha 3 **gradi di libertà** (le tre coordinate). Un corpo rigido ne ha 6: la sua posizione è fissata da tre punti non allineati (9 coordinate) legati da 3 vincoli sulle distanze reciproche, $9 - 3 = 6$; si possono pensare come 3 coordinate del centro di massa e 3 angoli di orientamento.

Nella **rotazione attorno a un asse fisso** ogni punto del corpo descrive una circonferenza con centro sull'asse. Il moto è descritto da un solo angolo $\theta(t)$, con **velocità angolare** $\omega = \frac{d\theta}{dt}$ e **accelerazione angolare** $\alpha = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$, uguali per tutti i punti. Un punto a distanza $R$ dall'asse percorre l'arco $l = R\theta$ e ha velocità e accelerazione tangenziali
$$v = R\omega, \qquad a_t = R\alpha,$$
più l'accelerazione centripeta $\omega^2 R$. Come vettore, $\omega$ è diretto lungo l'asse, con verso dato dalla regola della mano destra (la rotazione appare antioraria guardando dalla punta del vettore).

### 4.2 Momento d'inerzia

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

### 4.3 Momento di una forza e seconda equazione cardinale

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

### 4.4 Energia nelle rotazioni e puro rotolamento

Anche per le rotazioni vale la conservazione dell'energia, con l'energia cinetica $\frac12 I\omega^2$ e, per il peso, l'energia potenziale $Mgz_{CM}$ calcolata nel centro di massa.

> [!esempio] Un palo che cade
> Un palo omogeneo di massa $M$ e lunghezza $l = 2{,}3$ m, incernierato alla base, cade dalla posizione verticale. All'inizio $E = Mg\frac l2$; quando tocca terra $E = \frac12 I_A\omega^2$ con $I_A = \frac13 Ml^2$. Uguagliando, $\omega = \sqrt{\frac{3g}{l}}$, e l'estremo libero arriva a $v = l\omega = \sqrt{3gl} \approx 8{,}2$ m/s, più di quanto avrebbe un sasso lasciato cadere dalla stessa altezza ($\sqrt{2gl} \approx 6{,}7$ m/s).

Un corpo a simmetria circolare (cilindro, sfera, anello) di raggio $R$ **rotola senza strisciare** se il punto di contatto ha velocità nulla. La condizione di puro rotolamento è
$$v_{CM} = \omega R, \qquad a_{CM} = \alpha R,$$
e per il teorema di König l'energia cinetica è $T = \frac12 Mv_{CM}^2 + \frac12 I_{CM}\omega^2 = \frac12\left(M + \frac{I_{CM}}{R^2}\right)v_{CM}^2$.

![Figura 4.1 · Forze su un corpo che rotola giù per un piano inclinato: solo l'attrito statico ha momento rispetto al centro.](figure/4-1.svg)

> [!esempio] Rotolamento lungo un piano inclinato
> Un corpo di massa $M$, raggio $R$ e momento d'inerzia $I_{CM}$ scende rotolando su un piano inclinato di angolo $\theta$. Peso e normale passano per il centro di massa e non danno momento: a far ruotare il corpo è l'attrito statico $F_A$, rivolto verso l'alto lungo il piano, nel punto di contatto. Le equazioni cardinali, con il vincolo $a_{CM} = \alpha R$, sono
> $$Mg\sin\theta - F_A = Ma_{CM}, \qquad F_A R = I_{CM}\alpha.$$
> Risolvendo,
> $$a_{CM} = \frac{g\sin\theta}{1 + \frac{I_{CM}}{MR^2}}, \qquad F_A = \frac{I_{CM}}{MR^2 + I_{CM}}Mg\sin\theta.$$
> Il corpo scende tanto più lentamente quanto più massa ha lontano dal centro: $a_{CM}$ vale $\frac12 g\sin\theta$ per un anello, $\frac23 g\sin\theta$ per un disco, $\frac57 g\sin\theta$ per una sfera. Perché non strisci deve essere $F_A \le \mu_s Mg\cos\theta$, cioè $\mu_s \ge \frac{I_{CM}}{MR^2 + I_{CM}}\tan\theta$: per un disco su un piano di $30°$, $\mu_s \ge \frac13\tan 30° \approx 0{,}19$.

### 4.5 Macchina di Atwood con carrucola massiva

Due masse $m_1 > m_2$ sono appese ai capi di una fune che passa senza strisciare su una carrucola di raggio $R$ e momento d'inerzia $I$. Se la carrucola ha massa, le tensioni nei due rami sono diverse: la loro differenza dà il momento che la fa ruotare. Con $a$ l'accelerazione ($m_1$ scende) e $\alpha = \frac aR$:
$$m_1 g - T_1 = m_1 a, \qquad T_2 - m_2 g = m_2 a, \qquad (T_1 - T_2)R = I\frac aR.$$
Sommando tutto si eliminano le tensioni:
$$a = \frac{(m_1 - m_2)g}{m_1 + m_2 + \frac{I}{R^2}}.$$
La carrucola si comporta come una massa aggiuntiva $\frac{I}{R^2}$. Con $m_1 = 3$ kg, $m_2 = 2$ kg e una carrucola a disco di 2 kg ($\frac{I}{R^2} = 1$ kg): $a = \frac{9{,}8}{6} \approx 1{,}63$ m/s².

### 4.6 Momento angolare

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

### 4.7 Forze centrali

Un campo di forze è **centrale** se la forza è sempre diretta lungo la retta che congiunge il punto con un centro fisso $O$, con un'intensità che dipende solo dalla distanza: $F(r) = F(r)\,\hat u_r$, $r = \lvert r\rvert$. Esempi sono la gravitazione e la forza elettrostatica.

- **Sono conservative**: in coordinate polari $dl = dr\,\hat u_r + r\,d\theta\,\hat u_\theta$, quindi $F \cdot dl = F(r)\, dr$ e il lavoro $\int_{r_i}^{r_f}F(r)\, dr$ dipende solo dalle distanze iniziale e finale.
- **Conservano il momento angolare** rispetto a $O$: $\tau = r \times F(r)\hat u_r = 0$, perché i due vettori sono paralleli.

Dalla conservazione di $L = r \times mv$ seguono due fatti. Il moto è **piano**: $r$ e $v$ restano perpendicolari al vettore costante $L$. E, scrivendo $v = \dot r\,\hat u_r + r\dot\theta\,\hat u_\theta$, si ha $L = mr^2\dot\theta$, quindi
$$r^2\frac{d\theta}{dt} = \text{costante}.$$
La quantità $\frac12 r^2\dot\theta$ è la **velocità areolare**, l'area spazzata dal raggio vettore nell'unità di tempo: è costante per ogni forza centrale. Per la gravitazione è la seconda legge di Keplero (il raggio vettore di un pianeta spazza aree uguali in tempi uguali).

### 4.8 Equilibrio del corpo rigido

Un corpo rigido è in equilibrio (fermo) se sono nulle la risultante delle forze esterne e il loro momento risultante rispetto a un polo qualsiasi:
$$\sum F^{(est)} = 0, \qquad \sum \tau^{(est)} = 0.$$
Sono le due equazioni cardinali con le derivate nulle. Se la risultante è nulla, il momento risultante non dipende dal polo, e conviene scegliere il polo dove agiscono forze incognite, per eliminarle dall'equazione dei momenti.

> [!esempio] Trave appoggiata con un carico
> Una trave omogenea di 4 m e 20 kg è appoggiata ai due estremi; un carico di 30 kg è a 1 m dall'estremo sinistro. Con i momenti rispetto all'appoggio sinistro, la reazione destra $R_2$ deve bilanciare il peso della trave (applicato a 2 m) e il carico: $4R_2 = 20g \cdot 2 + 30g \cdot 1$, da cui $R_2 = 17{,}5g \approx 171{,}5$ N. La risultante nulla dà $R_1 = 50g - R_2 = 32{,}5g \approx 318{,}5$ N: l'appoggio più vicino al carico sostiene di più.

### Esempi ed esercizi svolti

**Esercizio 1 (un disco che parte da fermo).** Un disco di massa 2 kg e raggio 10 cm, libero di ruotare attorno al suo asse, è messo in rotazione da una fune avvolta sul bordo, tirata con forza costante di 4 N. Con $I = \frac12 MR^2 = 0{,}01$ kg·m², $\alpha = \frac{FR}{I} = \frac{0{,}4}{0{,}01} = 40$ rad/s². Dopo 2 s, $\omega = 80$ rad/s; l'energia cinetica $\frac12 I\omega^2 = 32$ J è uguale al lavoro della forza, $F$ per la fune svolta: $4 \cdot R\theta = 4 \cdot 0{,}1 \cdot \frac12 \cdot 40 \cdot 4 = 32$ J.

**Esercizio 2 (sfera e cilindro in gara).** Una sfera e un cilindro pieno, con qualsiasi massa e raggio, partono da fermi dalla stessa altezza $h$ su un piano inclinato, rotolando senza strisciare. Per la conservazione dell'energia $Mgh = \frac12\left(M + \frac{I}{R^2}\right)v^2$, quindi $v = \sqrt{\frac{2gh}{1 + I/(MR^2)}}$: $\sqrt{\frac{10}{7}gh}$ per la sfera, $\sqrt{\frac43 gh}$ per il cilindro. Arriva prima la sfera, e il risultato non dipende né dalla massa né dal raggio.

**Esercizio 3 (momento angolare di un punto in moto rettilineo).** Un punto che si muove di moto rettilineo uniforme ha, rispetto a un polo $O$ fuori dalla retta, momento angolare $L = mvd$, dove $d$ è la distanza di $O$ dalla retta: è costante, come deve essere perché la forza è nulla. È anche un caso (banale) della legge delle aree: il raggio vettore spazza triangoli di uguale area in tempi uguali.

#### Esercizi dalle esercitazioni

> [!aggiunta] Aggiunta in revisione · fonte: esercitazioni 10 (08/05/2025) e 11 (15/05/2025) del corso, testi riformulati, con i risultati confrontati con quelli delle esercitazioni; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-03, FG1-07)
> Per il corpo rigido le equazioni sono due: $\vec F_{ext} = M\vec a_{CM}$ e $\vec\tau_{ext} = I\vec\alpha$ (rispetto a un asse fisso o al centro di massa). In statica si annullano entrambe, e conviene calcolare i momenti rispetto al punto in cui agiscono più forze incognite: i loro momenti sono nulli.

**Esercizio 4. Una trave su due appoggi.** Una trave omogenea di 1 m e 2 kg poggia orizzontale su due appoggi agli estremi $A$ e $B$; una massa di 0,5 kg è appoggiata a $\frac{L}{3}$ da $A$. Reazioni degli appoggi.

Equilibrio delle forze: $R_A + R_B = (M + m)g = 24{,}5$ N. Momenti rispetto ad $A$: $R_B L = Mg\frac{L}{2} + mg\frac{L}{3}$, quindi $R_B = 9{,}81 + 1{,}64 = 11{,}45$ N e $R_A = 13{,}08$ N. L'appoggio più vicino alla massa regge di più, come ci si aspetta.

**Esercizio 5. La scala appoggiata al muro.** Una scala omogenea poggia su un muro verticale liscio e su un pavimento con $\mu_s = 0{,}1$. Angolo massimo con il muro?

Forze: peso $Mg$ nel centro, reazione del muro $N_m$ orizzontale (muro liscio), reazione del pavimento $N_p$ verticale e attrito $f$ orizzontale. Traslazione: $N_p = Mg$, $f = N_m$. Momenti rispetto al piede della scala, con $\theta$ l'angolo con il muro: $N_m L\cos\theta = Mg\frac{L}{2}\sin\theta$, quindi $f = \frac{Mg}{2}\tan\theta$. La condizione $f \le \mu_s N_p$ dà $\tan\theta \le 2\mu_s = 0{,}2$: $\theta_{max} = 11{,}3°$. Con un pavimento così scivoloso la scala deve stare quasi verticale.

**Esercizio 6. Momenti d'inerzia di corpi pieni.** (a) Parallelepipedo omogeneo di lati $a$, $b$, $c$ e massa $M$, rispetto all'asse per il centro parallelo a $c$. (b) Asta di lunghezza $L$ rispetto a un estremo.

(a) Il corpo si divide in sottili lastre perpendicolari all'asse, ognuna con il momento di una lastra rettangolare, e il risultato non dipende da $c$: $I = \frac{M}{12}(a^2 + b^2)$. (b) Per un'asta rispetto al centro $I_{CM} = \frac{ML^2}{12}$; per il teorema di Steiner, rispetto all'estremo, a distanza $\frac{L}{2}$, $I = \frac{ML^2}{12} + M\frac{L^2}{4} = \frac{ML^2}{3}$.

**Esercizio 7. La puleggia che continua a girare.** Una massa di 2 kg appesa a una fune avvolta su una puleggia (disco) di 10 kg e raggio 0,5 m scende da ferma e si sgancia dopo 2 m. Velocità angolare della puleggia dopo lo sgancio.

Finché la fune è tesa: $ma = mg - T$ e $TR = I\alpha = \frac12 MR^2\frac{a}{R}$, cioè $T = \frac12 Ma$. Quindi $a = \frac{mg}{m + M/2} = 2{,}80$ m/s². Dopo 2 m, $v = \sqrt{2ah} = 3{,}35$ m/s e $\omega = \frac{v}{R} = 6{,}70$ rad/s. Dopo lo sgancio nessuna forza fa momento sulla puleggia (l'asse è senza attrito) e $\omega$ resta 6,70 rad/s.

**Esercizio 8. L'asta incernierata che cade.** Un'asta omogenea di lunghezza $L$, incernierata a un estremo, parte da ferma dalla posizione verticale in alto. Velocità angolare quando passa per la verticale in basso.

Il centro scende di $L$ (da $\frac{L}{2}$ sopra la cerniera a $\frac{L}{2}$ sotto). Conservazione dell'energia con $I = \frac{ML^2}{3}$: $MgL = \frac12 \cdot \frac{ML^2}{3}\omega^2$, quindi $\omega = \sqrt{\frac{6g}{L}}$. La reazione della cerniera non fa lavoro perché il suo punto di applicazione è fermo.

**Esercizio 9. Un disco che rotola su un piano a 45°.** Disco pieno di 2 kg e raggio 0,5 m, $\mu_s = 0{,}5$. (a) Accelerazione angolare. (b) Attrito. (c) Angolo oltre il quale striscia.

Puro rotolamento: $a = \alpha R$. Traslazione: $Ma = Mg\sin\theta - f$; rotazione attorno al centro: $fR = \frac12 MR^2\alpha$, cioè $f = \frac12 Ma$. Quindi $a = \frac23 g\sin\theta = 4{,}62$ m/s², $\alpha = \frac{a}{R} = 9{,}25$ rad/s², $f = \frac13 Mg\sin\theta = 4{,}62$ N. Il rotolamento regge finché $f \le \mu_s Mg\cos\theta$, cioè $\tan\theta \le 3\mu_s = 1{,}5$: $\theta_{max} = 56{,}3°$. L'attrito statico nel rotolamento non dissipa energia, perché il punto di contatto è fermo.

**Esercizio 10. Molla, fune e carrucola: il periodo.** Una massa di 1 kg è appesa a una fune che passa su una carrucola (disco di 10 kg, raggio 0,5 m) ed è legata dall'altra parte a una molla ($k = 30$ N/m). (a) Allungamento all'equilibrio. (b) Periodo delle piccole oscillazioni.

(a) All'equilibrio la tensione è la stessa da entrambe le parti (la carrucola non accelera): $k\Delta l = mg$, $\Delta l = 0{,}327$ m. (b) Spostando la massa di $x$, le equazioni danno $\left(m + \frac{M}{2}\right)\ddot x = -kx$: la carrucola si comporta come una massa aggiunta $\frac{I}{R^2} = \frac{M}{2}$. Il periodo è $2\pi\sqrt{\frac{m + M/2}{k}} = 2\pi\sqrt{\frac{6}{30}} = 2{,}81$ s.

#### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove del 03/09/2025 e del 05/02/2026, con dati e geometrie diversi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-03, FG1-06, FG1-07)

**Esercizio 11. La biglia colpita dalla stecca.** Una biglia di 170 g e raggio 2,85 cm, ferma, riceve un colpo centrale con impulso $J = 1{,}5$ N·s. (a) Velocità iniziale. (b) Velocità angolare quando smette di strisciare. (c) Lavoro dell'attrito fino a quel momento.

(a) $v_0 = \frac{J}{m} = 8{,}82$ m/s; il colpo è centrale e non dà rotazione: $\omega_0 = 0$.

(b) All'inizio la biglia striscia: l'attrito dinamico la frena e le dà un momento che la fa girare, finché $v = \omega R$. Il momento angolare rispetto al punto di contatto con il piano si conserva (l'attrito passa per quel punto, peso e normale sono allineati): $mv_0 R = mvR + \frac25 mR^2\omega = \frac75 mvR$. Quindi $v = \frac57 v_0 = 6{,}30$ m/s e $\omega = \frac{v}{R} = 221$ rad/s.

(c) $W_a = \Delta K = \frac12 mv^2 + \frac12 \cdot \frac25 mR^2\omega^2 - \frac12 mv_0^2 = \frac{7}{10}mv^2 - \frac12 mv_0^2 = -1{,}89$ J: due settimi dell'energia iniziale. Non serve conoscere il coefficiente d'attrito: decide solo quanto dura lo strisciamento.

**Esercizio 12. L'asta che cade e urta una massa.** Un'asta di 1 kg e 1 m, incernierata in un estremo $O$, è lasciata da ferma in orizzontale. Quando passa per la verticale urta una massa puntiforme di 0,5 kg appesa a un filo lungo 1 m fissato in $O$, che resta attaccata alla punta dell'asta. (a) $\omega$ prima dell'urto. (b) $\omega$ subito dopo. (c) Angolo massimo raggiunto dopo l'urto.

(a) Energia: $Mg\frac{L}{2} = \frac12 \cdot \frac{ML^2}{3}\omega^2$, $\omega = \sqrt{\frac{3g}{L}} = 5{,}42$ rad/s.

(b) Nell'urto la cerniera esercita forze impulsive, quindi la quantità di moto non si conserva; si conserva però il momento angolare rispetto a $O$, perché quelle forze passano per $O$. $\frac{ML^2}{3}\omega = \left(\frac{ML^2}{3} + mL^2\right)\omega'$, quindi $\omega' = \frac{1/3}{1/3 + 1/2}\omega = 0{,}4\,\omega = 2{,}17$ rad/s.

(c) Dopo l'urto si conserva l'energia: $\frac12\left(\frac13 + \frac12\right)\omega'^2 = 1{,}96$ J deve diventare l'energia potenziale del centro dell'asta (che sale di $\frac{L}{2}(1 - \cos\theta)$) e della massa (che sale di $L(1 - \cos\theta)$): $\left(Mg\frac{L}{2} + mgL\right)(1 - \cos\theta) = 9{,}81(1 - \cos\theta)$. Quindi $\cos\theta = 0{,}8$, $\theta = 36{,}9°$.

### Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (FG1-03, FG1-07)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. La sfera che rotola giù.** Una sfera piena parte da ferma e rotola senza strisciare giù da un'altezza di 1 m. Velocità in fondo.

*Passo 1: l'energia cinetica di un corpo che rotola.* $K = \frac12 Mv^2 + \frac12 I\omega^2$ con $\omega = \frac{v}{R}$ e $I = \frac25 MR^2$: $K = \frac{7}{10}Mv^2$.

*Passo 2: la conservazione.* L'attrito statico non lavora: $Mgh = \frac{7}{10}Mv^2$.

*Passo 3: risultato.* $v = \sqrt{\frac{10}{7}gh} = 3{,}74$ m/s, contro i 4,43 m/s di un corpo che scivola senza attrito: una parte dell'energia va nella rotazione.

**Guidato 2. L'asta tenuta da una fune orizzontale.** Un'asta di 2 kg, incernierata in basso in $O$, forma 40° con la verticale ed è tenuta da una fune orizzontale attaccata all'altro estremo. Tensione della fune.

*Passo 1: dove calcolare i momenti.* Rispetto a $O$, così la reazione della cerniera (incognita) non compare.

*Passo 2: i bracci.* Il peso, applicato al centro, ha braccio $\frac{L}{2}\sin 40°$; la tensione, orizzontale, applicata all'estremo, ha braccio $L\cos 40°$.

*Passo 3: l'equilibrio dei momenti.* $TL\cos 40° = Mg\frac{L}{2}\sin 40°$, quindi $T = \frac{Mg}{2}\tan 40° = 8{,}23$ N.

*Passo 4: la cerniera.* Dall'equilibrio delle forze, la cerniera dà una componente orizzontale uguale e opposta a $T$ e una verticale uguale a $Mg$.

**Guidato 3. Steiner per un disco forato.** Un disco omogeneo di raggio $R$ e massa (prima del foro) $M$ ha un foro circolare di raggio $\frac{R}{2}$ con il centro a $\frac{R}{2}$ dal centro del disco. Momento d'inerzia rispetto all'asse per il centro del disco.

*Passo 1: la massa del foro.* L'area del foro è un quarto di quella del disco: $m_f = \frac{M}{4}$.

*Passo 2: il momento del disco pieno.* $\frac12 MR^2$.

*Passo 3: il momento del foro con Steiner.* Rispetto al proprio centro $\frac12 m_f\left(\frac{R}{2}\right)^2 = \frac{MR^2}{32}$; spostato a distanza $\frac{R}{2}$: $\frac{MR^2}{32} + \frac{M}{4}\cdot\frac{R^2}{4} = \frac{3MR^2}{32}$.

*Passo 4: sottrarre.* $I = \frac12 MR^2 - \frac{3}{32}MR^2 = \frac{13}{32}MR^2$. I momenti d'inerzia rispetto allo stesso asse si sommano e si sottraggono come le masse.

### Riepilogo

Un corpo rigido ha 6 gradi di libertà; nella rotazione attorno a un asse fisso tutti i punti hanno la stessa $\omega$ e $\alpha$, con $v = R\omega$ e $a_t = R\alpha$. L'energia cinetica di rotazione è $\frac12 I\omega^2$, con il momento d'inerzia $I = \int R^2\, dm$ che dipende dall'asse e si trasporta con Huygens-Steiner ($I = I_{CM} + Md^2$): $\frac{1}{12}Ml^2$ per l'asta al centro, $MR^2$ per l'anello, $\frac12 MR^2$ per il disco, $\frac25 MR^2$ per la sfera. Il momento di una forza è $RF\sin\varphi$ e, per un asse fisso, $\tau = I\alpha$. Nel puro rotolamento $v_{CM} = \omega R$, l'attrito statico fornisce il momento e non compie lavoro, e i corpi con più massa lontana dall'asse accelerano meno. Una carrucola con massa equivale a una massa aggiuntiva $I/R^2$. Il momento angolare rispetto a un polo fisso o al centro di massa varia del momento delle forze esterne e si conserva se questo è nullo. Le forze centrali sono conservative e conservano il momento angolare: il moto è piano e la velocità areolare è costante. Un corpo rigido è in equilibrio se risultante e momento risultante delle forze esterne sono nulli.

### Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FG1-03, FG1-07)
> Rotazioni, momenti d'inerzia, equazioni cardinali e momento angolare, con i termini per l'orale.

#### Rotazioni

$$v = \omega r, \quad a_t = \alpha r, \quad K_{rot} = \frac12 I\omega^2, \quad \vec\tau = \vec r \times \vec F, \quad \tau = I\alpha, \quad \vec L = I\vec\omega, \quad \vec\tau_{ext} = \frac{d\vec L}{dt}.$$

#### Momenti d'inerzia ($I_{CM}$)

| Corpo | Asse | $I$ |
|---|---|---|
| Anello, guscio cilindrico | asse di simmetria | $MR^2$ |
| Disco, cilindro pieno | asse di simmetria | $\frac12 MR^2$ |
| Sfera piena | diametro | $\frac25 MR^2$ |
| Guscio sferico | diametro | $\frac23 MR^2$ |
| Asta | perpendicolare per il centro | $\frac{1}{12}ML^2$ |
| Asta | perpendicolare per un estremo | $\frac13 ML^2$ |
| Lastra rettangolare $a \times b$ | perpendicolare per il centro | $\frac{1}{12}M(a^2 + b^2)$ |

Steiner: $I = I_{CM} + Md^2$.

#### Equazioni cardinali e rotolamento

$\vec F_{ext} = M\vec a_{CM}$, $\vec\tau_{ext} = \frac{d\vec L}{dt}$. Equilibrio: entrambe nulle. Puro rotolamento: $v_{CM} = \omega R$; $K = \frac12 Mv^2\left(1 + \frac{I}{MR^2}\right)$; su un piano inclinato $a = \frac{g\sin\theta}{1 + I/(MR^2)}$, limite $\tan\theta \le \mu_s\left(1 + \frac{MR^2}{I}\right)$.

#### Momento angolare

Si conserva rispetto a un polo se il momento delle forze esterne rispetto a quel polo è nullo: in un urto con una cerniera, rispetto alla cerniera. Forze centrali: $\vec L$ costante, moto piano, velocità areolare costante.

#### Termini per l'orale

| Termine | In una riga |
|---|---|
| Corpo rigido | sistema in cui le distanze fra i punti non cambiano |
| Momento d'inerzia | $\sum m_i r_i^2$: resistenza a cambiare velocità angolare |
| Momento di una forza | $\vec r \times \vec F$, capacità di far ruotare |
| Coppia | due forze opposte non allineate: risultante nulla, momento non nullo |
| Puro rotolamento | il punto di contatto ha velocità nulla |
| Momento angolare | $\vec r \times \vec p$; per un corpo rigido attorno a un asse fisso, $I\omega$ |
| Forza centrale | diretta sempre verso un punto fisso, con modulo che dipende dalla distanza |

#### Domande che tornano spesso

- Definire il momento d'inerzia e ricavarlo per l'asta e per il disco; dimostrare Steiner.
- Seconda equazione cardinale e sua forma per un asse fisso.
- Energia cinetica di un corpo che rotola; perché l'attrito statico non lavora?
- Condizioni di equilibrio di un corpo rigido, con un esempio (scala, trave).
- Conservazione del momento angolare: quando vale? Esempi (pattinatore, urto con cerniera).
- Forze centrali e seconda legge di Keplero.
