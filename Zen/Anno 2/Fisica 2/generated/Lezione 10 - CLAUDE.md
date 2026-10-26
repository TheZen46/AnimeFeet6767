---
corso: Fisica 2
lezione: 10
data: 2026-10-23
argomenti: [condensatore con lastra dielettrica, corrente elettrica, verso convenzionale della corrente, ampere, conduttori e isolanti, elettroni di conduzione, velocità di deriva, tempo di scattering, densità di corrente, corrente come flusso, resistenza, legge di Ohm, conduttori ohmici e non ohmici, resistività, potenza elettrica, conservazione della corrente nei nodi, reti di condensatori, conservazione della carica, condensatori con più dielettrici]
bibliography: fisica2.bib
tags: [fisica2]
---

# Lezione 10 — Corrente elettrica, resistenza e legge di Ohm

La lezione comincia chiudendo l'esercizio sul condensatore con la lastra dielettrica della [[Fisica 2 - Lezione 09 - Energia dei condensatori e dielettrici|lezione 9]]. Poi il docente cambia argomento e passa alla **corrente elettrica**, l'ingrediente che manca per studiare i circuiti. Dopo la definizione macroscopica si costruisce un modello microscopico della conduzione nei metalli, da cui escono la **velocità di deriva** degli elettroni e la **densità di corrente**. Seguono la **resistenza**, la **legge di Ohm**, la **resistività** e la **potenza elettrica**. Un esercizio sulla conservazione della corrente nei nodi e quattro esercizi sui condensatori chiudono la lezione.

> [!warning] Numerazione e fonti
> Il file della trascrizione si chiama "Lezione 10", mentre l'intestazione interna dice "Lezione: 9" e riporta come data quella del caricamento (25/10). La data della lezione, 23 ottobre 2026, viene dagli appunti. La numerazione 10 è coerente con la sequenza: la lezione online del 20/10 è la [[Fisica 2 - Lezione 09 - Energia dei condensatori e dielettrici|lezione 9]]. Le fonti sono la trascrizione (Parte 1, che copre quasi tutta la lezione) e i tuoi appunti a mano (quattro pagine).

## Ripresa: la tensione ai capi del condensatore con la lastra dielettrica

> [!example] Testo (ultimo punto dell'esercizio della lezione 9)
> Un condensatore piano ($A = 115\ \mathrm{cm^2}$, $d = 1{,}24\ \mathrm{cm}$) è stato caricato a $V_0 = 85{,}5\ \mathrm V$, con carica $q_0 = 702\ \mathrm{pC}$, e poi isolato. Tra le armature c'è una lastra di spessore $b = 0{,}78\ \mathrm{cm}$ e costante dielettrica $\kappa = 2{,}61$. Il campo nel vuoto è $E_0 = 6{,}90\ \mathrm{kV/m}$, quello nel dielettrico è $E_1 = E_0/\kappa = 2{,}64\ \mathrm{kV/m}$. Qual è ora la differenza di potenziale $V$ tra le armature?

Il docente ricorda la definizione: la differenza di potenziale è l'integrale di linea del campo, $V = -\int\vec E\cdot d\vec s$, lungo una curva scelta da noi tra le due armature. Conviene la curva più semplice, un segmento perpendicolare alle armature che va da quella positiva a quella negativa, nello stesso verso del campo. Così $\vec E\cdot d\vec s = E\,ds$, e la tensione cercata (positiva) è $V = \int E\,ds$.

Prima un'osservazione sulle cariche, che il docente fa guardando il disegno. Le armature hanno le loro cariche $\pm q_0$; il dielettrico si polarizza e accumula carica negativa sulla faccia superiore, vicina all'armatura positiva, e positiva su quella inferiore. Lungo il segmento si attraversano quindi tre tratti, e in ciascuno il campo è **costante**:

![[F2-L09-lastra-dielettrica.svg]]

- **Primo tratto**, dall'armatura positiva alla lastra. Se la lastra è centrata, la distanza è la metà dello spazio vuoto: $\dfrac d2 - \dfrac b2 = \dfrac{d-b}{2}$. Il campo è $E_0$.
- **Secondo tratto**, dentro la lastra: lunghezza $b$, campo $E_1 = E_0/\kappa$.
- **Terzo tratto**, dalla lastra all'armatura negativa: di nuovo $\dfrac{d-b}{2}$ con campo $E_0$.

Quando il campo è costante esce dall'integrale, e l'integrale di $ds$ è la lunghezza del tratto. Ogni tratto contribuisce quindi con campo per lunghezza:

$$
V_0' = \frac{d-b}{2}\,E_0, \qquad V_1 = b\,E_1 = \frac{b\,E_0}{\kappa},
$$

(il docente chiama $V_0$ la tensione di un tratto vuoto; qui è $V_0'$, per non confonderla con la tensione iniziale $V_0 = 85{,}5\ \mathrm V$), e la tensione totale è la somma dei tre contributi:

$$
V = 2\,\frac{d-b}{2}\,E_0 + \frac{b}{\kappa}\,E_0 = \left(d - b + \frac{b}{\kappa}\right)E_0 .
$$

Con i numeri:

$$
V = \left(1{,}24 - 0{,}78 + \frac{0{,}78}{2{,}61}\right)\cdot10^{-2}\ \mathrm m\cdot\left(6{,}90\cdot10^{3}\ \mathrm{V/m}\right) = 52{,}3\ \mathrm V .
$$

La tensione è scesa da $85{,}5$ a $52{,}3\ \mathrm V$ perché nel tratto occupato dal dielettrico il campo è più debole. Il risultato non dipende dalla posizione della lastra: se non fosse centrata, i due tratti vuoti avrebbero lunghezze diverse, ma la loro somma resterebbe $d - b$.

Il docente lo legge anche in termini di condensatori. Ogni tratto si comporta come un condensatore a sé, con la sua tensione: i due tratti vuoti come condensatori nel vuoto, la lastra come un condensatore con dielettrico. I tre sono attraversati dalla stessa carica, quindi sono **in serie**, e le loro tensioni si sommano. È un metodo generale: un condensatore con dielettrici si spezza in tratti in cui il campo è costante, e il calcolo diventa immediato.

> [!tip] Completamento: la capacità con la lastra #approfondimento
> Il docente si ferma alla tensione, ma da qui la capacità è immediata:
> $$
> C = \frac{q_0}{V} = \frac{702\ \mathrm{pC}}{52{,}3\ \mathrm V} = 13{,}4\ \mathrm{pF},
> \qquad
> C = \frac{\varepsilon_0A}{d - b + b/\kappa}.
> $$
> È maggiore di $C_0 = 8{,}21\ \mathrm{pF}$, ma minore di $\kappa C_0 = 21{,}4\ \mathrm{pF}$, che si avrebbe con il dielettrico a riempire tutto lo spazio. La formula si ritrova anche con la serie: $1/C = (d-b)/(\varepsilon_0A) + b/(\kappa\varepsilon_0A)$. Per $b = 0$ dà $C_0$, per $b = d$ dà $\kappa C_0$. Anche l'energia cambia: a carica costante scende da $U_0 = q_0^2/(2C_0) = 30{,}0\ \mathrm{nJ}$ a $U = q_0^2/(2C) = 18{,}4\ \mathrm{nJ}$. La differenza è il lavoro fatto dal campo, che **attira** la lastra tra le armature: per tirarla fuori bisognerebbe fornire quei $11{,}6\ \mathrm{nJ}$.

## La corrente elettrica

### Definizione

La corrente era già comparsa parlando della carica dei condensatori, nella [[Fisica 2 - Lezione 08 - Potenziale del disco e condensatori|lezione 8]]. Ora la si definisce con precisione. Quando delle cariche si spostano, attraverso una sezione di un filo passa una certa carica in un certo tempo. La **corrente elettrica** è la carica che attraversa la sezione per unità di tempo:

> [!important] Corrente elettrica
> $$
> i = \frac{dq}{dt}.
> $$
> Se la corrente è **stazionaria**, cioè costante nel tempo, la derivata si può sostituire con il rapporto tra variazioni finite: si misura la carica passata in un intervallo $\Delta t$ e $i = \Delta q/\Delta t$.

La corrente è uno **scalare**, un numero e non un vettore, ma uno scalare un po' particolare, sottolinea il docente: bisogna sempre dire anche **in quale verso** scorre lungo il filo, da $A$ a $B$ o da $B$ ad $A$. Nei calcoli si sceglie un verso arbitrario e lo si indica con una freccia. Se alla fine la corrente risulta negativa, scorre nel verso opposto a quello scelto. Lo vedremo nell'esercizio sui nodi.

### Il verso convenzionale

L'idea di corrente è antica: c'era già prima del Settecento. Solo studiando la conduzione su scala microscopica si è capito che nei metalli la corrente è trasportata dagli **elettroni**, che sono negativi. Per tradizione, però, si continua a ragionare come se si muovessero cariche **positive**.

![[F2-L10-verso-corrente.svg]]

Dire che la corrente scorre da $A$ a $B$ significa quindi immaginare cariche positive che vanno da $A$ a $B$, cioè dal potenziale più alto a quello più basso. In un filo metallico avviene il contrario: gli elettroni si muovono da $B$ ad $A$. I due modi di vedere sono equivalenti. Cariche negative che vanno da $B$ ad $A$ trasportano carica nello stesso modo di cariche positive che vanno da $A$ a $B$: in entrambi i casi la carica di $A$ diminuisce e quella di $B$ aumenta.

### L'ampere

La corrente si misura in **ampere**, il cui simbolo è A:

$$
1\ \mathrm A = \frac{1\ \mathrm C}{1\ \mathrm s}.
$$

Un ampere corrisponde al passaggio di un coulomb al secondo attraverso la sezione del filo.

> [!tip] L'ampere nel Sistema Internazionale #approfondimento
> Dal 2019 l'ampere è definito fissando il valore esatto della carica elementare, $e = 1{,}602\,176\,634\cdot10^{-19}\ \mathrm C$ [@bipm2019]. Un ampere corrisponde quindi al passaggio di $1/e \simeq 6{,}24\cdot10^{18}$ cariche elementari al secondo. È la conferma, a livello di definizione delle unità, che la carica è quantizzata, come si è visto nella [[Fisica 2 - Lezione 01 - Carica elettrica e legge di Coulomb|lezione 1]].

### Isolanti, conduttori, superconduttori

I materiali si classificano in base a come rispondono a una differenza di potenziale, cioè a quanto bene trasportano corrente. Gli **isolanti** in pratica non la trasportano. I **conduttori** la trasportano bene. I **superconduttori** la trasportano ancora meglio, senza alcuna resistenza, ma sono casi particolari: solo alcuni materiali diventano superconduttori, e di solito a temperature molto basse.

> [!tip] La scoperta della superconduttività #approfondimento
> La superconduttività fu scoperta nel 1911 nel laboratorio di Heike Kamerlingh Onnes a Leida: raffreddato con elio liquido a poco più di $4\ \mathrm K$, il mercurio perdeva bruscamente ogni resistenza elettrica [@vanDelft2010].

## Il modello microscopico della conduzione nei metalli

Il docente vuole ora capire la corrente su scala microscopica, cioè come si ricava dal moto delle cariche nel materiale.

### Gli elettroni liberi

I buoni conduttori sono metalli come il **rame** (Cu), l'**argento** (Ag) e l'**oro** (Au), con numeri atomici $29$, $47$ e $79$. Il numero atomico conta i protoni del nucleo, e quindi gli elettroni dell'atomo neutro: il rame ha 29 protoni e 29 elettroni. Questi metalli hanno una caratteristica in comune: nel guscio elettronico più esterno c'è **un solo elettrone**. Nel rame, 28 elettroni stanno nei gusci interni, fortemente legati al nucleo, mentre il ventinovesimo, sul guscio esterno, ne sente molto meno l'attrazione ed è quasi libero.

Ne viene un'immagine semplice del metallo. I nuclei, con i loro elettroni interni, formano un **reticolo cristallino** di ioni positivi fissi. Gli elettroni esterni, uno per atomo, non appartengono più a un atomo particolare e si muovono quasi liberamente in tutto il reticolo: sono gli **elettroni di conduzione**. Appena si applica un campo elettrico, questi elettroni si spostano.

Gli elettroni di conduzione sono moltissimi. Nel rame la loro densità, cioè il numero per unità di volume, è

$$
n_{\text{Cu}} \simeq 8{,}5\cdot10^{28}\ \text{elettroni}/\mathrm m^3 ,
$$

ed è proprio questa enorme quantità di cariche mobili che rende il rame un buon conduttore.

> [!warning] Densità degli elettroni nel rame
> Nella trascrizione e negli appunti la densità è $8{,}5\cdot10^{25}\ \mathrm{m^{-3}}$: l'esponente è sbagliato di tre ordini di grandezza. Il valore si può ricavare con un conto semplice. Il rame ha densità $8{,}96\ \mathrm{g/cm^3}$ e massa molare $63{,}5\ \mathrm{g/mol}$, quindi in un metro cubo ci sono $8{,}96\cdot10^{6}/63{,}5 \simeq 1{,}41\cdot10^{5}$ moli, cioè $1{,}41\cdot10^{5}\cdot6{,}02\cdot10^{23} \simeq 8{,}5\cdot10^{28}$ atomi. Con un elettrone di conduzione per atomo, $n \simeq 8{,}5\cdot10^{28}\ \mathrm{m^{-3}}$, in accordo con il valore tabulato $8{,}47\cdot10^{28}\ \mathrm{m^{-3}}$ [@hyperphysicsFermi; @ashcroft1976].

### Velocità casuali: in media nessun moto

Gli elettroni di conduzione non stanno fermi: si muovono velocissimi, con velocità dell'ordine di $10^6\ \mathrm{m/s}$. Ma in assenza di campo ogni elettrone si muove in una direzione diversa, a caso. Per questo un filo di rame a cui non si applica una differenza di potenziale non è percorso da corrente: gli elettroni si muovono, ma non vanno da nessuna parte in particolare.

![[F2-L10-moto-elettroni.svg]]

In formule, il moto complessivo degli elettroni si descrive con la **velocità media** su tutti gli $N$ elettroni:

$$
\vec v_{\text{tot}} = \frac1N\sum_i \vec v_i = 0 .
$$

La somma di moltissimi vettori orientati a caso ha media nulla. Si può dimostrare matematicamente, dice il docente, ma qui basta l'intuizione (pannello a). Non c'è uno spostamento netto di elettroni e quindi non c'è corrente.

> [!tip] Velocità di Fermi, non velocità termica #approfondimento
> Si potrebbe pensare che questa sia l'agitazione termica, ma per un gas di particelle classiche alla temperatura ambiente si avrebbe $v \sim \sqrt{3k_BT/m_e} \simeq 1{,}2\cdot10^5\ \mathrm{m/s}$, dieci volte meno. La velocità degli elettroni di conduzione è dovuta a un effetto quantistico: per il principio di esclusione di Pauli gli elettroni non possono stare tutti nello stato di energia più bassa e occupano stati con energie e velocità via via maggiori, fino alla cosiddetta **velocità di Fermi**, che per il rame vale $1{,}57\cdot10^6\ \mathrm{m/s}$ [@hyperphysicsFermi; @ashcroft1976]. È per questo che resta grande anche a temperature molto basse.

### Che cosa cambia con un campo elettrico

La differenza compare quando si applica un campo elettrico. Il campo esercita una forza sugli elettroni, e la forza produce un'**accelerazione**:

$$
\vec F = -e\vec E = m\vec a \quad\Longrightarrow\quad \vec a = -\frac{e}{m}\,\vec E ,
$$

dove $e$ è la carica elementare e $m$ la massa dell'elettrone. Il segno meno dice che l'accelerazione è opposta al campo, perché l'elettrone è negativo. A differenza delle velocità casuali, l'accelerazione ha una **direzione privilegiata**: è la stessa per tutti gli elettroni.

Il docente assume che tra un urto e l'altro l'elettrone sia libero e senta solo il campo. Il suo moto è allora uniformemente accelerato, e se la velocità iniziale dell'elettrone $i$-esimo è $\vec v_{0i}$, dopo un tempo $\tau$ la velocità è

$$
\vec v_i = \vec v_{0i} + \vec a\,\tau .
$$

Si fa di nuovo la media su tutti gli elettroni. Le velocità iniziali sono casuali e si mediano a zero, come prima. Il termine $\vec a\tau$ è invece uguale per tutti: sommato $N$ volte e diviso per $N$, resta $\vec a\tau$:

$$
\vec v_{\text{tot}} = \frac1N\sum_i\vec v_{0i} + \frac1N\sum_i\vec a\,\tau = 0 + \vec a\,\tau = -\frac{e\tau}{m}\,\vec E .
$$

Ora la velocità media non è più nulla: gli elettroni, nel complesso, si spostano nel verso opposto al campo, e nel filo scorre una corrente. A livello microscopico, conclude il docente, la corrente è un effetto dell'accelerazione prodotta dal campo elettrico. In un circuito il campo è prodotto dalla differenza di potenziale: collegando un filo a una batteria si crea il campo, e gli elettroni cominciano a scorrere.

> [!warning] Segni negli appunti
> Negli appunti c'è $\vec v_i = \vec v_i^{\,0} - \vec a\tau$ insieme ad $\vec a = -\dfrac{e}{m}\vec E$. Così il segno meno compare due volte e la velocità media risulterebbe concorde con il campo, il che è sbagliato per un elettrone. La forma coerente è quella usata sopra: $\vec v_i = \vec v_{0i} + \vec a\tau$ con $\vec a = -e\vec E/m$. In alternativa si può scrivere $\vec v_i = \vec v_{0i} - (e\vec E/m)\tau$. Il docente stesso osserva che per gli elettroni "bisogna metterci il segno meno" e che lavorare con cariche positive cambia solo i versi.

### Il tempo di scattering

Che cos'è $\tau$? L'equazione $\vec v_i = \vec v_{0i} + \vec a\tau$ descrive il moto di un elettrone **tra due urti**. L'elettrone parte con una certa velocità e viene accelerato dal campo; poi urta uno ione del reticolo e viene deviato in un'altra direzione; di nuovo viene accelerato, urta, è deviato, e così via (pannello b della figura). Ne risulta una traiettoria a zig-zag. Tra un urto e l'altro i tratti sono archi di parabola, perché l'accelerazione è costante. Nel complesso la traiettoria deriva lentamente nel verso opposto al campo.

> [!important] Tempo di scattering
> $\tau$ è il **tempo di scattering** (o tempo di vita, o tempo libero medio) dell'elettrone: il **tempo medio** tra un urto e il successivo con il reticolo. È una grandezza statistica. Con $10^{28}$ elettroni per metro cubo non si può seguire il singolo elettrone, e se ne descrivono gli effetti medi: per questo si media sugli $N$ elettroni.

Il docente precisa che negli urti, in questo modello, si può considerare conservata anche l'energia, e che la relazione tra $\tau$ e le proprietà del materiale "si ricava, ma non ci interessa granché come".

### La velocità di deriva

> [!important] Velocità di deriva
> La velocità media degli elettroni in presenza di campo si chiama **velocità di deriva**:
> $$
> \vec v_d = \vec a\,\tau = -\frac{e\tau}{m}\,\vec E .
> $$
> È lo spostamento medio per unità di tempo nella direzione del campo, quello che si osserva macroscopicamente come corrente.

La velocità di deriva è piccolissima. Il valore riportato a lezione è $|\vec v_d| \simeq 5\cdot10^{-3}\ \mathrm{m/s}$, da confrontare con i $10^6\ \mathrm{m/s}$ del moto casuale: un fattore dell'ordine di $10^{-9}$. Il moto effettivo degli elettroni, quello che conta per la corrente, è lentissimo rispetto al loro moto disordinato.

> [!warning] La velocità di deriva non è una costante del materiale
> Il valore $5\cdot10^{-3}\ \mathrm{m/s}$ va preso come ordine di grandezza indicativo: $v_d$ dipende dalla corrente e dalla sezione del filo. Dalla relazione $i = n e v_d\Sigma$ ricavata più sotto, per un filo di rame da $1{,}5\ \mathrm{mm^2}$ percorso da $10\ \mathrm A$, una situazione domestica tipica, si ha
> $$
> v_d = \frac{i}{n e\Sigma} = \frac{10}{(8{,}5\cdot10^{28})(1{,}60\cdot10^{-19})(1{,}5\cdot10^{-6})}\ \mathrm{m/s} \simeq 5\cdot10^{-4}\ \mathrm{m/s},
> $$
> mezzo millimetro al secondo. Per avere $5\cdot10^{-3}\ \mathrm{m/s}$ servirebbe una densità di corrente dieci volte maggiore. In ogni caso la conclusione del docente resta valida: la deriva è miliardi di volte più lenta del moto casuale.

> [!tip] Perché la lampadina si accende subito? #approfondimento
> Se gli elettroni avanzano di mezzo millimetro al secondo, come mai la luce si accende appena si preme l'interruttore? Perché non serve che gli elettroni arrivino dall'interruttore alla lampadina: il filo è già pieno di elettroni di conduzione. Chiudendo il circuito si stabilisce il **campo elettrico** lungo il filo, e questo si propaga a una velocità paragonabile a quella della luce. Gli elettroni di tutto il filo cominciano a derivare quasi insieme, come l'acqua in un tubo già pieno che esce dal rubinetto appena lo si apre.

## Corrente e densità di corrente

### La corrente in un filo

Si può ora collegare la corrente, grandezza macroscopica, alla velocità di deriva, grandezza microscopica. Il docente considera un filo cilindrico di sezione $\Sigma$, con un campo elettrico lungo l'asse. Ragiona con cariche **positive**, secondo la convenzione tradizionale, che si muovono con velocità di deriva $v_d$ nel verso del campo. Con gli elettroni il discorso è identico, ma con tutti i versi invertiti.

![[F2-L10-filo-corrente.svg]]

Una carica che entra in un tratto di filo a un certo istante, procedendo con velocità $v_d$, in un tempo $\Delta t$ percorre la distanza $v_d\Delta t$. Ci si focalizza allora sul tratto di filo di lunghezza $v_d\Delta t$. Nel tempo $\Delta t$ tutte le cariche contenute in questo tratto ne attraversano la faccia di destra: quelle vicine alla faccia escono subito, quella più lontana arriva alla faccia proprio alla fine dell'intervallo. Il volume del tratto è

$$
\Sigma\,v_d\,\Delta t .
$$

Se $n$ è il numero di portatori di carica per unità di volume ed $e$ la carica di ciascuno, la carica che attraversa la sezione in $\Delta t$ è densità per carica per volume:

$$
\Delta q = n\,e\,\Sigma\,v_d\,\Delta t .
$$

Dividendo per $\Delta t$ si ottiene la corrente:

$$
i = \frac{\Delta q}{\Delta t} = n\,e\,v_d\,\Sigma .
$$

È la corrente scritta in termini microscopici. $e$ è la carica del portatore. $n$ è la densità di portatori, i circa $10^{28}$ elettroni per metro cubo del rame. $v_d$ è la velocità di deriva, che dipende dall'accelerazione e quindi dal campo. $\Sigma$ è la sezione del filo.

> [!warning] Notazione degli appunti
> Negli appunti il volume del tratto è indicato con $\Delta V$, lo stesso simbolo della differenza di potenziale. Qui l'ho scritto per esteso, $\Sigma v_d\Delta t$, per evitare confusione. Il pedice in $n_+$ degli appunti ricorda che si stanno considerando portatori positivi.

### La densità di corrente

La quantità che moltiplica la sezione ha un nome.

> [!important] Densità di corrente
> $$
> j = n\,e\,v_d, \qquad i = j\,\Sigma .
> $$
> La **densità di corrente** $j$ è la corrente per unità di sezione e si misura in $\mathrm{A/m^2}$. Dipende solo dal materiale ($n$, $e$) e dallo stato di moto dei portatori ($v_d$), non dalle dimensioni del filo.

La corrente invece dipende dalla sezione, ed è intuitivo, osserva il docente: un filo sottile trasporta meno corrente di un cavo grosso. A parità di materiale e di differenza di potenziale, la densità di corrente resta la stessa. Per trasportare più corrente serve allora un cavo di sezione maggiore, perché $j$ non cambia ma $\Sigma$ sì.

### La densità di corrente è un vettore

Il calcolo precedente presupponeva una corrente costante nel tempo e portatori che si muovono tutti nella stessa direzione, perpendicolare alla sezione. In generale la densità di corrente è un **vettore**,

$$
\vec j = n\,q\,\vec v_d ,
$$

con la direzione del moto dei portatori positivi. Per gli elettroni $q = -e$ e $\vec v_d$ è opposta al campo, quindi $\vec j = -ne\vec v_d$ è di nuovo **concorde con $\vec E$**. Comunque si scelgano i portatori, la densità di corrente punta nel verso convenzionale della corrente.

Come nella [[Fisica 2 - Lezione 04 - Dipolo in campo elettrico e flusso|lezione 4]] per il flusso del campo elettrico, a una superficie piana di area $\Sigma$ si associa il vettore $\vec\Sigma = \Sigma\,\hat n$, che ha per modulo l'area e per direzione la normale. La relazione $i = j\Sigma$ si generalizza allora in un prodotto scalare:

$$
i = \vec j\cdot\vec\Sigma .
$$

![[F2-L10-densita-corrente.svg]]

Se poi la corrente non è uniforme sulla superficie, o la superficie non è piana, si procede come per il flusso. Si divide la superficie in elementi $d\Sigma$ abbastanza piccoli da poterli considerare piani, a ciascuno si associa il vettore $d\vec\Sigma = \hat n\,d\Sigma$, si calcola $\vec j\cdot d\vec\Sigma$ e si sommano i contributi:

> [!important] La corrente come flusso della densità di corrente
> $$
> i = \int_\Sigma \vec j\cdot d\vec\Sigma .
> $$
> La corrente attraverso una superficie è il **flusso** del vettore $\vec j$ attraverso quella superficie. È uno scalare, anche se calcolato da un vettore.

Il docente non è sicuro che questa forma generale verrà usata nel corso, ma la scrive perché chiarisce che cosa sia davvero la corrente.

> [!warning] Freccia sulla corrente negli appunti
> Negli appunti la relazione è scritta $\vec i = \vec j\cdot\vec\Sigma$. Il prodotto scalare di due vettori è uno scalare, e la corrente è uno scalare: la freccia su $i$ va tolta.

## Resistenza e legge di Ohm

### La resistenza

Il modello degli elettroni liberi non dice tutto. Gli elettroni non sono davvero liberi e gli urti con il reticolo non sono del tutto elastici: per questo i metalli oppongono **resistenza** al passaggio della corrente.

Se si applica una differenza di potenziale $V$ ai capi di un filo, nel filo scorre una corrente $i$. Il rapporto tra le due si chiama resistenza.

> [!important] Resistenza
> $$
> R = \frac{V}{i}, \qquad V = i\,R .
> $$
> La resistenza si misura in **ohm**, simbolo $\Omega$: $1\ \Omega = 1\ \mathrm V/1\ \mathrm A$. Un filo ha la resistenza di un ohm se, applicando ai suoi capi una differenza di potenziale di un volt, vi scorre una corrente di un ampere.

### La legge di Ohm

Il docente insiste su una distinzione che spesso si confonde. La relazione $R = V/i$, e quindi $V = iR$, si può scrivere **sempre**: si applica una tensione, si misura la corrente, il rapporto è la resistenza. La **legge di Ohm** è un'altra cosa: è il caso particolare in cui $R$ è **costante**, cioè non dipende dalla tensione applicata né dalla corrente. In quel caso $V$ e $i$ sono proporzionali, con $R$ come costante di proporzionalità: raddoppiando la tensione raddoppia la corrente.

![[F2-L10-caratteristiche.svg]]

Nel grafico della tensione in funzione della corrente, un conduttore che segue la legge di Ohm dà una retta con pendenza costante, pari a $R$ (pannello a). Questi sono i **conduttori ohmici**. Ci sono però anche conduttori in cui la relazione non è lineare (pannello b): per generare una certa corrente serve una certa tensione, e per avere più corrente la tensione deve crescere in un modo che non è proporzionale. Sono i **conduttori non ohmici**.

La legge di Ohm è un caso particolare, ma è anche il più diffuso: i conduttori tradizionali come rame, oro e argento la rispettano. A volte conviene invece un comportamento non ohmico. Nei **diodi** e nei **transistor**, spiega il docente, si applica una tensione e non succede niente; superata una certa soglia, il dispositivo comincia a condurre (pannello c). Nel corso si studieranno quasi solo conduttori ohmici.

> [!warning] Il grafico (b) degli appunti
> Il secondo grafico degli appunti, con $V$ in funzione di $i$ e una curva che si impenna, rappresenta un generico conduttore non ohmico. Il comportamento a soglia dei diodi descritto a lezione si rappresenta di solito al contrario, con la corrente in funzione della tensione: la corrente resta quasi nulla finché la tensione non supera la soglia, poi cresce rapidamente. L'ho aggiunto come pannello (c).

> [!tip] Una legge sperimentale #approfondimento
> Georg Simon Ohm pubblicò la sua analisi dei circuiti nel 1827, nel libro *Die galvanische Kette, mathematisch bearbeitet* ("Il circuito galvanico trattato matematicamente") [@ohm1827]. Nonostante il nome, la "legge" di Ohm non è una legge fondamentale come il teorema di Gauss: è una proprietà, approssimata, di molti materiali in un ampio intervallo di condizioni.

### La resistività

La resistenza, come la corrente, non dipende solo dal materiale ma anche dalla **forma** del conduttore. Per un filo cilindrico di lunghezza $L$ e sezione di area $A$:

> [!important] Resistenza di un filo e resistività
> $$
> R = \rho\,\frac{L}{A}.
> $$
> $\rho$ è la **resistività** del materiale e si misura in $\Omega\cdot\mathrm m$. È un parametro del solo materiale, che può dipendere dalla temperatura di lavoro: il rame ha la sua resistività, l'oro la sua, l'argento la sua.

![[F2-L10-filo-resistenza.svg]]

La resistività caratterizza il materiale, la resistenza caratterizza il **singolo conduttore**: materiale e geometria insieme. A parità di materiale, un filo più lungo ha una resistenza maggiore, e vedremo che dissipa di più. Un filo di sezione maggiore ha una resistenza minore. Le due dipendenze si capiscono pensando al filo come a una serie di tratti in fila, le cui resistenze si sommano, oppure come a tanti fili sottili affiancati, che offrono alla corrente più strade in parallelo.

> [!example] Resistenza di un filo di rame
> Un filo di rame lungo $L = 10\ \mathrm m$ con diametro di $1\ \mathrm{mm}$ ha sezione $A = \pi(0{,}5\cdot10^{-3}\ \mathrm m)^2 = 7{,}85\cdot10^{-7}\ \mathrm{m^2}$. Con la resistività del rame a $20\ ^\circ\mathrm C$, $\rho \simeq 1{,}7\cdot10^{-8}\ \Omega\cdot\mathrm m$ [@hyperphysicsRes]:
> $$
> R = \rho\,\frac{L}{A} = (1{,}68\cdot10^{-8})\,\frac{10}{7{,}85\cdot10^{-7}}\ \Omega \simeq 0{,}21\ \Omega .
> $$
> Dieci metri di filo hanno una resistenza di appena due decimi di ohm. Per questo nei circuiti la resistenza dei fili di collegamento si trascura quasi sempre.

> [!tip] Dal modello microscopico alla legge di Ohm #approfondimento
> Il modello degli elettroni liberi spiega perché tanti materiali seguono la legge di Ohm. In un filo con campo uniforme, $V = EL$ e $i = jA$. Sostituendo in $V = iR = i\rho L/A$ si ottiene $EL = j\rho L$, cioè la legge di Ohm in **forma locale**:
> $$
> \vec j = \frac{\vec E}{\rho} = \sigma\vec E,
> $$
> dove $\sigma = 1/\rho$ è la **conducibilità**. D'altra parte, dal modello, $\vec j = -ne\vec v_d = \dfrac{ne^2\tau}{m}\vec E$. La densità di corrente è proporzionale al campo se il tempo di scattering $\tau$ non dipende dal campo, ed è il caso dei metalli, perché la deriva è una piccolissima correzione al moto casuale. Il confronto dà
> $$
> \rho = \frac{m}{ne^2\tau}.
> $$
> È il modello proposto da Paul Drude nel 1900 [@drude1900; @ashcroft1976]. Con i valori del rame ($n = 8{,}47\cdot10^{28}\ \mathrm{m^{-3}}$, $\rho = 1{,}68\cdot10^{-8}\ \Omega\cdot\mathrm m$) si ottiene $\tau = m/(ne^2\rho) \simeq 2{,}5\cdot10^{-14}\ \mathrm s$. Con la velocità di Fermi, tra un urto e l'altro un elettrone percorre in media $v_F\tau \simeq 40\ \mathrm{nm}$, più di cento distanze tra atomi vicini.

## La potenza elettrica

Insieme alla legge di Ohm, una delle relazioni che si useranno più spesso è quella della potenza elettrica. La **potenza** è sempre una variazione di energia nel tempo:

$$
P = \frac{dU}{dt},
$$

e si misura in **watt**, $1\ \mathrm W = 1\ \mathrm J/\mathrm s$. Qualunque sia il fenomeno, che si spostino cariche elettriche o altro, interessa sempre un'energia al secondo.

Nel caso elettrico l'energia è quella associata al potenziale: una carica $q$ che attraversa una differenza di potenziale $V$ scambia l'energia $U = qV$ ([[Fisica 2 - Lezione 07 - Potenziale elettrico|lezione 7]]). Se la tensione è costante, differenziando si ottiene $dU = V\,dq$: è l'energia necessaria per far attraversare a una carica infinitesima $dq$ la differenza di potenziale $V$. La potenza è allora

$$
P = \frac{dU}{dt} = V\,\frac{dq}{dt} = i\,V ,
$$

perché $dq/dt$ è la corrente. Per un conduttore che segue la legge di Ohm si può sostituire $V = iR$ oppure $i = V/R$:

> [!important] Potenza elettrica
> $$
> P = iV = i^2R = \frac{V^2}{R}.
> $$
> $P = iV$ vale per qualunque elemento di circuito; le altre due forme valgono per una resistenza. In una resistenza questa energia viene **dissipata**, cioè convertita in calore: è l'**effetto Joule**.

> [!example] Potenza dissipata in un filo
> Il filo di rame dell'esempio precedente ($R = 0{,}21\ \Omega$), percorso da una corrente di $10\ \mathrm A$, dissipa $P = i^2R = (10)^2(0{,}21)\ \mathrm W \simeq 21\ \mathrm W$. La dipendenza da $i^2$ spiega perché l'energia elettrica si trasporta ad alta tensione e bassa corrente: a parità di potenza trasmessa $iV$, le perdite nei cavi $i^2R$ si riducono con il quadrato della corrente.

## Conservazione della corrente nei nodi

Nei circuiti i fili si diramano. Un punto in cui si incontrano tre o più fili si chiama **nodo**. La carica non si crea e non si distrugge, e in regime stazionario non si accumula nel nodo: tutta la corrente che entra deve uscire.

![[F2-L10-nodo.svg]]

Per il nodo della figura, con $i_1$ entrante e $i_2$, $i_3$ uscenti:

$$
i_1 = i_2 + i_3 .
$$

> [!example] Esercizio — La corrente iniettata in un punto di una rete
> Una rete di fili ha vari nodi (i puntini dove i fili si separano o si uniscono). In alcuni tratti sono note le correnti, in ampere, con i loro versi: $2$, $4$, $3$, $2$, $2$ entranti e $1$ uscente, come in figura. Quanta corrente viene iniettata nel punto $A$?

![[F2-L10-rete-correnti.svg]]

Il metodo è conservare la corrente nodo per nodo. Si chiama $x$ la corrente incognita e le si dà un verso arbitrario: entrante in $A$. Poi si procede da un nodo all'altro.

- Nel primo nodo entrano $x$ (da $A$) e $2$ (dal tratto a destra): verso il nodo successivo scorre $x + 2$.
- Nel nodo seguente, sul filo verticale, entrano $x + 2$ e la corrente $4$ che sale dal basso: più su scorre $x + 6$.
- Nel nodo di sinistra entrano $2$ e $3$, quindi verso il filo verticale scorre $5$. Sul filo verticale, oltre questo nodo, scorre $x + 6 + 5 = x + 11$.
- Nel nodo successivo entra un'altra corrente $2$: più su scorre $x + 13$.
- Nell'ultimo nodo tutta questa corrente esce dall'unico filo rimasto, quello in alto a sinistra, dove scorre $1$.

Quindi

$$
x + 13 = 1 \quad\Longrightarrow\quad x = -12\ \mathrm A .
$$

Il valore assoluto è $12\ \mathrm A$, e il segno meno significa che la corrente scorre nel verso **opposto** a quello scelto: non viene iniettata in $A$, ma **esce** da $A$. La corrente è uno scalare, ma ha un verso, e il segno conta. Si può scegliere un verso qualsiasi all'inizio. Se alla fine si trova un segno meno, il verso giusto è l'altro. Con $x = -12$ le correnti nei tratti intermedi diventano $x + 2 = -10$, $x + 6 = -6$ e $x + 11 = -1$: anche queste scorrono al contrario rispetto alle frecce iniziali. Le correnti date restano invece quelle del testo. Il controllo globale torna: entrano $2 + 3 + 4 + 2 + 2 = 13\ \mathrm A$ ed escono $1 + 12 = 13\ \mathrm A$.

> [!tip] Un consiglio di metodo
> Qualcuno in aula chiede se le correnti $3$ e $2$ del nodo di sinistra non fossero inutili, visto che non dipendono da $x$. Il docente risponde di no: senza di esse non si saprebbe che nel tratto successivo scorre $5$, e la catena si interromperebbe. E coglie l'occasione per un consiglio generale: negli esercizi di fisica e di matematica, se non sono sbagliati e chi li propone "non è cattivo", ci sono esattamente i dati che servono. Se si arriva a una soluzione senza usare un dato, probabilmente la soluzione è sbagliata. Se invece sembra mancare un dato, bisogna cambiare ragionamento.

## Esercizi sui condensatori

Il docente dedica l'ultima parte della lezione agli esercizi sui condensatori. Ne mostra uno o due per tipo, perché, dice, una volta presa la mano si somigliano tutti.

### Esercizio 1 — Una rete di sei condensatori

> [!example] Testo
> Una batteria con $V = 20\ \mathrm V$ alimenta la rete di condensatori della figura, con $C_1 = C_6 = 3\ \mu\mathrm F$, $C_3 = C_5 = 4\ \mu\mathrm F$, $C_2 = C_4 = 2\ \mu\mathrm F$. Trovare la capacità equivalente e la carica totale immagazzinata.

![[F2-L10-sei-condensatori.svg]]

Come in tutti questi esercizi, bisogna riconoscere quali condensatori sono in serie e quali in parallelo, e semplificare un pezzo alla volta. Ci vuole un po' di occhio, ammette il docente.

$C_3$ e $C_5$ stanno sullo stesso ramo, uno dopo l'altro, senza diramazioni in mezzo: sono **in serie**.

$$
\frac{1}{C_{35}} = \frac{1}{C_3} + \frac{1}{C_5}
\quad\Longrightarrow\quad
C_{35} = \frac{C_3C_5}{C_3 + C_5} = \frac{4\cdot4}{8}\ \mu\mathrm F = 2\ \mu\mathrm F .
$$

Per il passo successivo il docente colora i fili: un colore per il filo in alto a sinistra, uno per il filo centrale con il tratto a destra. Tutto ciò che è collegato con un filo senza condensatori in mezzo è un unico conduttore, quindi allo stesso potenziale. Si vede allora che $C_4$, $C_{35}$ e $C_2$ hanno tutti un'armatura sul primo filo e l'altra sul secondo: hanno la stessa differenza di potenziale e sono **in parallelo**.

$$
C' = C_4 + C_2 + C_{35} = (2 + 2 + 2)\ \mu\mathrm F = 6\ \mu\mathrm F .
$$

Conviene sostituire subito i numeri, consiglia il docente, altrimenti l'algebra diventa troppo complicata. Rimangono $C_1$ e $C_6$: entrambi hanno un'armatura sul filo centrale e l'altra sul filo in basso, collegato al polo negativo della batteria. Anche loro sono in parallelo:

$$
C'' = C_1 + C_6 = (3 + 3)\ \mu\mathrm F = 6\ \mu\mathrm F .
$$

Infine $C'$ e $C''$ sono in serie tra i due poli della batteria:

$$
C_{\text{eq}} = \frac{C'C''}{C' + C''} = \frac{6\cdot6}{12}\ \mu\mathrm F = 3\ \mu\mathrm F .
$$

La carica totale immagazzinata è quella del condensatore equivalente:

$$
q = C_{\text{eq}}V = (3\cdot10^{-6})(20)\ \mathrm C = 6\cdot10^{-5}\ \mathrm C = 60\ \mu\mathrm C .
$$

Il trucco è sempre lo stesso, conclude il docente: i circuiti possono essere complicati e noiosi, ma basta trovare i pezzi in serie e in parallelo e semplificarli uno dopo l'altro.

> [!tip] Controllo: la tensione sui due blocchi #approfondimento
> $C'$ e $C''$ sono in serie, quindi hanno la stessa carica di $60\ \mu\mathrm C$. Le loro tensioni sono $V' = q/C' = 10\ \mathrm V$ e $V'' = q/C'' = 10\ \mathrm V$, e la somma ridà i $20\ \mathrm V$ della batteria. Da qui si risale ai singoli condensatori: ad esempio $C_4$ ha $10\ \mathrm V$ ai capi e porta $q_4 = 20\ \mu\mathrm C$, mentre $C_3$ e $C_5$ si dividono i $10\ \mathrm V$ del loro ramo, $5\ \mathrm V$ ciascuno.

### Esercizio 2 — Due condensatori carichi con polarità opposte

> [!example] Testo
> Due condensatori, $C_1 = 1\ \mu\mathrm F$ e $C_2 = 3\ \mu\mathrm F$, sono stati caricati separatamente alla stessa tensione $V = 100\ \mathrm V$ ma con polarità opposte: $C_1$ ha l'armatura superiore positiva, $C_2$ quella inferiore. Poi vengono collegati tra loro chiudendo contemporaneamente, all'istante $t = 0$, due interruttori. Quali sono le cariche finali $q_1$ e $q_2$?

![[F2-L10-polarita-opposte.svg]]

Il docente propone di pensare alla situazione iniziale come a due circuiti separati: ciascun condensatore è stato caricato da una batteria, ma la batteria di $C_2$ era montata al contrario. Le cariche iniziali si calcolano subito:

$$
q_1^0 = C_1V = 100\ \mu\mathrm C, \qquad q_2^0 = C_2V = 300\ \mu\mathrm C .
$$

Quando si chiudono gli interruttori, l'armatura positiva di ciascun condensatore viene collegata all'armatura negativa dell'altro. Le cariche si mescolano e in parte si neutralizzano. Il punto chiave, ancora una volta, è la **conservazione della carica**. Le due armature superiori formano ora un unico conduttore isolato, e la sua carica è quella che c'era prima: $+100\ \mu\mathrm C$ da $C_1$ e $-300\ \mu\mathrm C$ da $C_2$, in totale $-200\ \mu\mathrm C$. Allo stesso modo le armature inferiori portano in totale $+200\ \mu\mathrm C$. La carica netta che resta è dunque

$$
q_{\text{netta}} = q_2^0 - q_1^0 = (C_2 - C_1)\,V = 200\ \mu\mathrm C .
$$

Se le capacità fossero uguali, le cariche si neutralizzerebbero del tutto e i condensatori finirebbero scarichi. Qui $C_2$ ne aveva di più, e l'eccesso non può sparire: "quelle cariche ce le dobbiamo tenere", dice il docente. Domina $C_2$: alla fine le armature superiori sono entrambe negative e quelle inferiori positive, con la polarità iniziale di $C_2$.

Nella configurazione finale i due condensatori hanno le armature collegate a due a due, quindi sono **in parallelo**, con la stessa tensione $V'$ e capacità equivalente $C_{\text{eq}} = C_1 + C_2$:

$$
V' = \frac{q_{\text{netta}}}{C_{\text{eq}}} = \frac{(C_2 - C_1)\,V}{C_1 + C_2} = \frac{2\cdot100}{4}\ \mathrm V = 50\ \mathrm V,
$$

$$
q_1 = C_1V' = 50\ \mu\mathrm C, \qquad q_2 = C_2V' = 150\ \mu\mathrm C .
$$

Il controllo: $q_1 + q_2 = 200\ \mu\mathrm C = q_{\text{netta}}$.

> [!warning] Segno e un refuso
> Negli appunti c'è $q_{\text{netta}} = q_2^0 - q_1^0 = (C_1 - C_2)V$: l'ultimo passaggio ha i segni invertiti e darebbe $-200\ \mu\mathrm C$. La forma corretta è $(C_2 - C_1)V$, ed è quella usata subito dopo negli appunti stessi per calcolare $V' = 50\ \mathrm V$. Nella trascrizione il risultato finale compare come "105 micrometri", un errore di trascrizione per $q_2 = 150\ \mu\mathrm C$, il valore degli appunti.

L'idea si ritrova in tutti gli esercizi in cui dei condensatori carichi vengono collegati chiudendo un interruttore: le cariche si spostano, ma la carica totale di ogni conduttore isolato si conserva.

> [!tip] Anche qui l'energia diminuisce #approfondimento
> Prima della chiusura i due condensatori immagazzinano $\tfrac12(C_1 + C_2)V^2 = 20\ \mathrm{mJ}$; dopo, $\tfrac12(C_1 + C_2)V'^2 = 5\ \mathrm{mJ}$. Tre quarti dell'energia si dissipano nei fili durante la ridistribuzione, come nell'esercizio 2 della [[Fisica 2 - Lezione 09 - Energia dei condensatori e dielettrici|lezione 9]].

### Esercizio 3 — Un condensatore con tre dielettrici

> [!example] Testo
> Un condensatore piano ha armature di area $A = 10{,}5\ \mathrm{cm^2}$ a distanza $2d = 7{,}12\ \mathrm{mm}$. Lo spazio tra le armature è riempito da tre dielettrici: il primo, con $\kappa_1 = 21$, occupa metà dell'area per tutta l'altezza $2d$; nell'altra metà ci sono due strati sovrapposti, ciascuno di altezza $d$, con $\kappa_2 = 42$ e $\kappa_3 = 58$. Trovare la capacità equivalente.

![[F2-L10-tre-dielettrici.svg]]

In generale, dice il docente, questi esercizi si risolvono pensando la struttura come un insieme di condensatori in serie e in parallelo, uno per ogni dielettrico. Ogni pezzo è un condensatore piano con la sua area, la sua distanza tra le armature e il suo dielettrico.

- Il blocco $\kappa_1$ è un condensatore di area $A/2$ e distanza $2d$.
- Gli strati $\kappa_2$ e $\kappa_3$ sono due condensatori di area $A/2$ e distanza $d$, uno sopra l'altro: la carica li attraversa uno dopo l'altro, quindi sono **in serie**.
- Il blocco $\kappa_1$ e la pila $\kappa_2$–$\kappa_3$ sono affiancati tra le stesse armature, con la stessa tensione: sono **in parallelo**.

Il docente calcola prima le capacità **senza dielettrico**, che dipendono solo dalla geometria:

$$
C_1^0 = \varepsilon_0\,\frac{A/2}{2d} = \varepsilon_0\,\frac{A}{4d},
\qquad
C_2^0 = C_3^0 = \varepsilon_0\,\frac{A/2}{d} = \varepsilon_0\,\frac{A}{2d}.
$$

$C_2^0$ e $C_3^0$ sono uguali perché i due strati hanno la stessa geometria. Poi inserisce i dielettrici, che moltiplicano ciascuna capacità per il proprio $\kappa$ ([[Fisica 2 - Lezione 09 - Energia dei condensatori e dielettrici|lezione 9]]):

$$
C_1 = \kappa_1\varepsilon_0\,\frac{A}{4d}, \qquad
C_2 = \kappa_2\varepsilon_0\,\frac{A}{2d}, \qquad
C_3 = \kappa_3\varepsilon_0\,\frac{A}{2d}.
$$

Ora basta ridurre il circuito: $C_2$ e $C_3$ in serie danno $C_{23} = C_2C_3/(C_2 + C_3)$, e $C_{23}$ è in parallelo con $C_1$:

$$
C_{\text{eq}} = C_1 + C_{23} = C_1 + \frac{C_2C_3}{C_2 + C_3}.
$$

Con $d = 3{,}56\ \mathrm{mm}$ si ottiene $C_1 = 13{,}7\ \mathrm{pF}$, $C_2 = 54{,}8\ \mathrm{pF}$, $C_3 = 75{,}7\ \mathrm{pF}$, $C_{23} = 31{,}8\ \mathrm{pF}$, e infine

$$
C_{\text{eq}} = 4{,}55\cdot10^{-11}\ \mathrm F = 45{,}5\ \mathrm{pF}.
$$

Sono esercizi standard, conclude il docente: anche con configurazioni complicate, si tratta di riconoscere la geometria di ogni pezzo e poi inserire il fattore $\kappa$ del dielettrico.

> [!tip] Perché la scomposizione funziona #approfondimento
> La superficie di separazione tra $\kappa_2$ e $\kappa_3$ è parallela alle armature e, lontano dai bordi, è una superficie equipotenziale. Vi si può immaginare un sottilissimo foglio conduttore senza cambiare nulla: diventa l'armatura comune dei due condensatori in serie. La scomposizione trascura però ciò che accade lungo la superficie verticale tra il blocco $\kappa_1$ e la pila. A metà altezza il potenziale nella pila non coincide esattamente con quello nel blocco $\kappa_1$, e lì il campo si deforma un po'. È un effetto di bordo, che questi esercizi trascurano come si trascurano i bordi delle armature.

### Esercizio 4 — Un condensatore che si scarica su altri due

> [!example] Testo
> Una batteria con $V = 10\ \mathrm V$, tre condensatori $C_1 = 10\ \mu\mathrm F$ e $C_2 = C_3 = 20\ \mu\mathrm F$ e un commutatore $S$ formano il circuito della figura. Inizialmente $S$ è chiuso a sinistra; poi viene spostato a destra. Qual è la carica finale $q_1$ su $C_1$?

![[F2-L10-commutatore.svg]]

Il circuito ha due configurazioni. Con $S$ a sinistra, solo $C_1$ è collegato alla batteria e ne sente la tensione. $C_2$ e $C_3$ sono su un ramo aperto, quindi scarichi: è come se non ci fossero. Allora

$$
q_1^0 = C_1V = (10\cdot10^{-6})(10)\ \mathrm C = 100\ \mu\mathrm C .
$$

Con $S$ a destra la situazione si capovolge. Il ramo della batteria resta aperto, quindi la batteria è di fatto staccata dal circuito. Il circuito chiuso in cui le cariche si riassestano contiene $C_1$, $C_2$ e $C_3$, ma non la batteria. Le cariche che si ridistribuiscono possono venire solo da $C_1$. Come sempre in queste configurazioni, la carica si conserva:

$$
q_f = q_1 + q_2 + q_3 = q_1^0 .
$$

Nella configurazione finale le armature superiori dei tre condensatori sono collegate tra loro, e così quelle inferiori: tutti e tre hanno la stessa tensione e sono **in parallelo**, con

$$
C_{\text{eq}} = C_1 + C_2 + C_3 = 50\ \mu\mathrm F .
$$

> [!warning] Sezione ricostruita — inizio
> La trascrizione si interrompe proprio mentre il docente scrive la tensione finale. La conclusione viene dai tuoi appunti, dove il calcolo è completo.

La tensione finale è la carica totale divisa per la capacità equivalente:

$$
V_f = \frac{q_f}{C_{\text{eq}}} = \frac{q_1^0}{C_1 + C_2 + C_3} = \frac{C_1V}{C_1 + C_2 + C_3} = \frac{100\ \mu\mathrm C}{50\ \mu\mathrm F} = 2\ \mathrm V,
$$

e la carica finale su $C_1$ è

$$
q_1 = C_1V_f = (10\ \mu\mathrm F)(2\ \mathrm V) = 20\ \mu\mathrm C .
$$

Il controllo: $C_2$ e $C_3$ portano ciascuno $q_2 = q_3 = (20\ \mu\mathrm F)(2\ \mathrm V) = 40\ \mu\mathrm C$, e $20 + 40 + 40 = 100\ \mu\mathrm C = q_1^0$. $C_1$ ha ceduto l'80% della sua carica agli altri due condensatori, che insieme hanno una capacità quattro volte più grande.

> [!warning] Sezione ricostruita — fine
