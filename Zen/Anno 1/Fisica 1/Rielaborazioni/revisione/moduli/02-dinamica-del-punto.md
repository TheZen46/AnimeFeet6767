---
corso: Fisica Generale 1
modulo: 2
titolo: Dinamica del punto materiale
programma: [FG1-01, FG1-05]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-04
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

## Riepilogo

I principi di Newton dicono che senza forza risultante un corpo mantiene il suo stato di moto, che la forza risultante produce un'accelerazione $a = F/m$, e che le forze fra due corpi sono uguali e opposte. La massa misura l'inerzia, la forza si misura in newton e si definisce con il dinamometro. Vicino alla Terra il peso è $mg$; i vincoli esercitano reazioni normali e, se ruvidi, attriti: dinamico, $\mu_d N$ opposto al moto, e statico, fino a $\mu_s N$, che si adatta per impedire lo scivolamento (un corpo su un piano inclinato resta fermo se $\tan\theta \le \mu_s$). Le funi ideali trasmettono la stessa tensione e impongono la stessa accelerazione ai corpi collegati. Ogni problema si imposta con il diagramma di corpo libero e $F = ma$ in componenti. Un moto circolare richiede una forza centripeta $mv^2/R$ fornita dalle forze presenti. La forza elastica $-kx$ produce oscillazioni armoniche con periodo $2\pi\sqrt{m/k}$, e il pendolo semplice, per piccole oscillazioni, oscilla con periodo $2\pi\sqrt{L/g}$.
