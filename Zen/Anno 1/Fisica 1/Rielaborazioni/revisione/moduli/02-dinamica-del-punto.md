---
corso: Fisica Generale 1
modulo: 2
titolo: Dinamica del punto materiale
programma: [FG1-01, FG1-05]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 2 · Dinamica del punto materiale

**In questo modulo.** Si usano la cinematica del modulo 1 (velocità, accelerazione, moto circolare) e le equazioni differenziali più semplici. Si passa dalla descrizione del moto alle sue cause: i tre principi di Newton, la definizione operativa di forza e di massa, la forza peso e la gravitazione, le reazioni vincolari, le tensioni delle funi e le forze di attrito statico e dinamico. Si impara il metodo del diagramma di corpo libero e lo si applica al piano inclinato, ai corpi collegati da funi e carrucole, al moto circolare (forza centripeta, giro della morte) e alle oscillazioni della molla e del pendolo. Alla fine si sa impostare e risolvere le equazioni del moto di uno o più corpi collegati.

## 2.1 I principi della dinamica

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

## 2.2 Forza peso e reazioni vincolari

Due masse puntiformi $m_1$ e $m_2$ a distanza $r$ si attraggono con la forza di **gravitazione universale**
$$F = G\frac{m_1 m_2}{r^2}, \qquad G \approx 6{,}67 \cdot 10^{-11}\ \mathrm{N\,m^2/kg^2},$$
diretta lungo la congiungente. Vicino alla superficie terrestre l'attrazione della Terra su un corpo di massa $m$ è la **forza peso** $F_p = mg$, verticale verso il basso, con $g \approx 9{,}8$ m/s².

Quando un corpo è appoggiato a una superficie o vincolato in altro modo, il vincolo esercita una **reazione vincolare** che impedisce al corpo di attraversarlo. Se il contatto è liscio (senza attrito), la reazione è perpendicolare alla superficie e si chiama **reazione normale** $N$; il suo valore non è dato a priori, ma è quello che serve per rispettare il vincolo.

**Metodo del diagramma di corpo libero.** Per ogni problema di dinamica:

1. si individuano i corpi di cui studiare il moto;
2. per ciascuno si disegnano tutte le forze che agiscono su di esso (peso, reazioni, tensioni, attriti, forze applicate);
3. si scelgono assi comodi (per esempio uno parallelo al moto);
4. si scrive $F = ma$ in componenti, aggiungendo le relazioni imposte dai vincoli (accelerazioni nulle in una direzione, accelerazioni uguali per corpi legati da una fune).

## 2.3 Piano inclinato e tensioni

> [!esempio] Piano inclinato liscio
> Un blocco di massa $m$ è su un piano inclinato liscio di angolo $\theta$. Con l'asse $x$ lungo il piano (verso il basso) e $y$ perpendicolare, il peso ha componenti $mg\sin\theta$ e $-mg\cos\theta$. Il blocco non si stacca dal piano, quindi $a_y = 0$:
> $$ma_x = mg\sin\theta, \qquad N - mg\cos\theta = 0 \quad \Longrightarrow \quad a_x = g\sin\theta, \quad N = mg\cos\theta.$$
> Con $\theta = 30°$, $a = 4{,}9$ m/s². La reazione normale è minore del peso.

Una **fune ideale** è inestensibile e di massa trascurabile: trasmette una forza di trazione diretta lungo la fune, la **tensione** $T$, che ha lo stesso valore in ogni punto. Due corpi collegati da una fune tesa hanno accelerazioni di uguale modulo. Una **carrucola ideale** (senza massa e senza attrito) cambia la direzione della fune senza cambiare la tensione.

> [!esempio] Due scatole trascinate
> Due scatole A e B di masse $m_A$ e $m_B$, su un tavolo liscio, sono collegate da una fune; ad A si applica una forza orizzontale $F$. In verticale le normali bilanciano i pesi; in orizzontale le due scatole hanno la stessa accelerazione $a$:
> $$m_A a = F - T, \qquad m_B a = T.$$
> Sommando si elimina la tensione: $a = \frac{F}{m_A + m_B}$, e poi $T = \frac{m_B F}{m_A + m_B}$. Con $m_A = 2$ kg, $m_B = 3$ kg e $F = 10$ N: $a = 2$ m/s² e $T = 6$ N. La fune tira B con una forza minore di $F$, perché $F$ deve accelerare anche A.

## 2.4 Forze di attrito

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

## 2.5 Dinamica del moto circolare

Per il modulo 1, un corpo in moto circolare uniforme ha accelerazione centripeta $\frac{v^2}{R}$. Per il secondo principio deve quindi agire una forza risultante diretta verso il centro, la **forza centripeta**:
$$F_c = m\frac{v^2}{R} = m\omega^2 R.$$
Non è un nuovo tipo di forza: è la componente radiale della risultante delle forze presenti (una tensione, il peso, una reazione, l'attrito delle gomme in curva).

> [!esempio] Giro della morte con una fune
> Un corpo di massa $m$ ruota su una circonferenza verticale di raggio $R$ legato a una fune. Nel punto più alto sia il peso sia la tensione puntano verso il centro (in basso):
> $$m\frac{v^2}{R} = mg + T \quad \Longrightarrow \quad T = m\frac{v^2}{R} - mg.$$
> La fune resta tesa se $T \ge 0$, cioè se $v \ge \sqrt{gR}$. Con $R = 1$ m la velocità minima in cima è $\sqrt{9{,}8} \approx 3{,}13$ m/s; con $m = 0{,}5$ kg e $v = 4$ m/s la tensione è $0{,}5 \cdot 16 - 0{,}5 \cdot 9{,}8 = 3{,}1$ N.

## 2.6 Oscillazioni: molla e pendolo

Una molla di costante elastica $k$ (in N/m) esercita sul corpo attaccato all'estremo una forza di richiamo proporzionale all'allungamento rispetto alla lunghezza a riposo (**legge di Hooke**): $F = -kx$, con $x$ la deformazione.

> [!teorema] Oscillatore armonico
> Una massa $m$ attaccata a una molla, su un piano orizzontale liscio, ha equazione del moto $m\ddot x = -kx$, cioè $\ddot x = -\omega^2 x$ con $\omega = \sqrt{\frac{k}{m}}$. Le soluzioni sono
> $$x(t) = A\cos(\omega t + \phi), \qquad T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}.$$

L'ampiezza $A$ e la fase $\phi$ dipendono dalle condizioni iniziali, la **pulsazione** $\omega$ e il periodo no. Con $k = 200$ N/m e $m = 0{,}5$ kg si ha $\omega = 20$ rad/s e $T \approx 0{,}314$ s.

> [!teorema] Pendolo semplice
> Una massa $m$ appesa a un filo ideale di lunghezza $L$, spostata di un angolo $\theta$ dalla verticale, ha accelerazione tangenziale $L\ddot\theta = -g\sin\theta$. Per **piccole oscillazioni** ($\sin\theta \approx \theta$) l'equazione diventa quella dell'oscillatore armonico, $\ddot\theta = -\frac{g}{L}\theta$, e
> $$\theta(t) = \theta_0\cos\left(\sqrt{\tfrac{g}{L}}\, t + \phi\right), \qquad T = 2\pi\sqrt{\frac{L}{g}}.$$

Il periodo non dipende né dalla massa né, per piccole oscillazioni, dall'ampiezza (isocronismo): un pendolo lungo 1 m ha periodo di circa 2 s. Lungo il filo, la tensione bilancia la componente radiale del peso e fornisce la forza centripeta.

## Esempi ed esercizi svolti

**Esercizio 1 (piano inclinato e massa appesa).** Un blocco $m_1 = 4$ kg su un piano inclinato di $30°$ con $\mu_d = 0{,}2$ è collegato con una fune, attraverso una carrucola in cima al piano, a una massa $m_2 = 3$ kg che pende in verticale. Se $m_2$ scende, il blocco sale lungo il piano e l'attrito è rivolto verso il basso. Le equazioni, con l'accelerazione comune $a$ positiva nel verso del moto, sono
$$m_2 a = m_2 g - T, \qquad m_1 a = T - m_1 g\sin\theta - \mu_d m_1 g\cos\theta.$$
Sommando: $a = \frac{m_2 g - m_1 g\sin\theta - \mu_d m_1 g\cos\theta}{m_1 + m_2} = \frac{29{,}4 - 19{,}6 - 6{,}79}{7} \approx 0{,}43$ m/s², positiva, quindi il moto avviene davvero nel verso supposto. La tensione è $T = m_2(g - a) \approx 28{,}1$ N.

**Esercizio 2 (peso apparente in ascensore).** Una persona di 70 kg è su una bilancia in un ascensore che accelera verso l'alto con $a = 2$ m/s². Sulla persona agiscono il peso e la reazione $N$ della bilancia: $N - mg = ma$, quindi $N = m(g + a) = 70 \cdot 11{,}8 = 826$ N. La bilancia, che misura $N$, segna circa 84 kg. In discesa accelerata segnerebbe meno, e in caduta libera zero.

**Esercizio 3 (curva piana).** Un'auto percorre una curva piana di raggio 50 m. La forza centripeta è l'attrito statico fra gomme e asfalto, al più $\mu_s mg$. Deve essere $m\frac{v^2}{R} \le \mu_s mg$, cioè $v \le \sqrt{\mu_s g R}$: con $\mu_s = 0{,}8$, $v \le \sqrt{0{,}8 \cdot 9{,}8 \cdot 50} \approx 19{,}8$ m/s (circa 71 km/h), indipendentemente dalla massa.

### Esercizi dalle esercitazioni

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

### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizio nuovo sul modello della prova del 05/02/2026, con dati diversi; soluzione verificata con `strumenti/verifica_ampliamento.py` (FG1-01, FG1-05, FG1-07)

**Esercizio 8. Una massa che gira attaccata a una molla.** Su un piano orizzontale liscio un punto di 200 g, attaccato a una molla di lunghezza a riposo 10 cm e $k = 50$ N/m fissata al centro, fa un moto circolare uniforme con periodo 0,5 s. (a) Allungamento della molla. (b) Energia meccanica. (c) Momento angolare rispetto al centro.

(a) La forza elastica è la forza centripeta: $k(l - l_0) = m\omega^2 l$, con $\omega = \frac{2\pi}{T} = 12{,}57$ rad/s e $m\omega^2 = 31{,}6$ N/m. Quindi $l = \frac{kl_0}{k - m\omega^2} = \frac{5}{18{,}4} = 0{,}271$ m, allungamento $0{,}171$ m. Se fosse $m\omega^2 \ge k$ non ci sarebbe soluzione: la molla non riuscirebbe a trattenere il punto.

(b) $E = \frac12 m(\omega l)^2 + \frac12 k(l - l_0)^2 = 1{,}16 + 0{,}74 = 1{,}90$ J.

(c) $L = m l^2\omega = 0{,}185$ kg·m²/s, perpendicolare al piano; per un moto in senso orario visto dall'alto, per la regola della mano destra, è diretto verso il basso.

## Esercizi guidati

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

## Riepilogo

I principi di Newton dicono che senza forza risultante un corpo mantiene il suo stato di moto, che la forza risultante produce un'accelerazione $a = F/m$, e che le forze fra due corpi sono uguali e opposte. La massa misura l'inerzia, la forza si misura in newton e si definisce con il dinamometro. Vicino alla Terra il peso è $mg$; i vincoli esercitano reazioni normali e, se ruvidi, attriti: dinamico, $\mu_d N$ opposto al moto, e statico, fino a $\mu_s N$, che si adatta per impedire lo scivolamento (un corpo su un piano inclinato resta fermo se $\tan\theta \le \mu_s$). Le funi ideali trasmettono la stessa tensione e impongono la stessa accelerazione ai corpi collegati. Ogni problema si imposta con il diagramma di corpo libero e $F = ma$ in componenti. Un moto circolare richiede una forza centripeta $mv^2/R$ fornita dalle forze presenti. La forza elastica $-kx$ produce oscillazioni armoniche con periodo $2\pi\sqrt{m/k}$, e il pendolo semplice, per piccole oscillazioni, oscilla con periodo $2\pi\sqrt{L/g}$.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FG1-01, FG1-05)
> Principi, forze e oscillazioni, con i termini per l'orale.

### Principi e forze

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

### Oscillazioni

$$m\ddot x = -kx \Rightarrow x = A\cos(\omega t + \varphi),\ \omega = \sqrt{\frac{k}{m}}, \qquad \text{pendolo: } \omega = \sqrt{\frac{g}{L}} \text{ per piccole oscillazioni},$$

$$k_{parallelo} = k_1 + k_2, \qquad \frac{1}{k_{serie}} = \frac{1}{k_1} + \frac{1}{k_2}.$$

### Termini per l'orale

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

### Domande che tornano spesso

- Enunciare i tre principi della dinamica; che cos'è un sistema inerziale?
- Differenza fra attrito statico e dinamico; perché $f_s$ è una disuguaglianza?
- Ricavare il moto armonico della molla e il periodo del pendolo per piccole oscillazioni.
- Che cosa fornisce la forza centripeta in una curva, in un pendolo conico, in un satellite?
- Peso apparente in un ascensore accelerato.
