---
corso: Fisica 2
lezione: 11
data: 2026-10-27
argomenti: [condensatori in serie, partitore capacitivo, reti di condensatori con interruttori, conservazione della carica, diodo, elementi non lineari, forza elettromotrice, pila di Volta, legge delle maglie, leggi di Kirchhoff, regole dei segni, batteria reale, resistenza interna]
bibliography: fisica2.bib
tags: [fisica2]
---

# Lezione 11 — Forza elettromotrice e legge delle maglie

La lezione comincia con tre esercizi sui condensatori. Il primo ricava una formula utile da ricordare: come si divide una tensione tra due condensatori in serie. Il secondo la applica a una rete di quattro condensatori con due interruttori. Il terzo è un excursus su un elemento che nel corso non verrà più trattato, il **diodo**. Poi si passa alla teoria dei circuiti. Si introduce la **forza elettromotrice**, la grandezza che descrive ciò che fa una batteria, e la si collega alla corrente in due modi: con un argomento energetico e con la **legge delle maglie** di Kirchhoff. Dalla legge delle maglie escono le regole dei segni per percorrere un circuito e la descrizione di una **batteria reale**, con la sua resistenza interna.

> [!warning] Fonti di questa lezione
> Per questa lezione c'è **solo la trascrizione** (Parte 1), senza appunti a mano. La data non compare in nessuna fonte. La trascrizione riporta come data di registrazione il 28/10, che nelle lezioni precedenti era la data del caricamento. Ho indicato martedì **27 ottobre 2026**, coerente con il calendario del corso (martedì e venerdì), ma è una deduzione. Gli schemi dei circuiti li ho ricostruiti dalla descrizione a voce, perché la lavagna non è nella trascrizione: lo segnalo esercizio per esercizio.

## Due condensatori in serie: come si divide la tensione

> [!example] Testo
> Due condensatori $C_1$ e $C_2$ sono in serie, e ai capi della serie c'è una differenza di potenziale $V$. Quali sono le tensioni $V_1$ e $V_2$ ai capi di ciascun condensatore?

Il docente lo chiama un "esercizietto", ma lo propone perché il risultato è uno schema da ricordare: quando un sistema è più complicato, si può ricondurre a questo caso e scrivere subito le tensioni senza rifare tutti i conti.

![[F2-L11-partitore-capacitivo.svg]]

Due osservazioni bastano. La prima: i condensatori sono **in serie**, quindi hanno la **stessa carica**, $q_1 = q_2$. La seconda: le tensioni in serie si **sommano**, $V_1 + V_2 = V$. Il resto è applicare la definizione di capacità. Da $q_1 = C_1V_1$ e $q_2 = C_2V_2$, con cariche uguali:

$$
C_1V_1 = C_2V_2 .
$$

Si usa la seconda osservazione per eliminare $V_2 = V - V_1$:

$$
C_1V_1 = C_2(V - V_1) = C_2V - C_2V_1
\quad\Longrightarrow\quad
(C_1 + C_2)\,V_1 = C_2V .
$$

Il problema è simmetrico: per $V_2$ basta scambiare gli indici.

> [!important] Partitore capacitivo
> Due condensatori in serie, e soli, con una tensione $V$ ai loro capi:
> $$
> V_1 = \frac{C_2}{C_1 + C_2}\,V, \qquad V_2 = \frac{C_1}{C_1 + C_2}\,V .
> $$
> Al numeratore compare la capacità **dell'altro** condensatore.

Il risultato dice come la tensione totale "si scarica" sui due condensatori, per usare l'espressione del docente. Il condensatore più piccolo prende la tensione più grande, perché a parità di carica $V = q/C$. È lo stesso risultato visto nell'esercizio 1 della [[Fisica 2 - Lezione 09 - Energia dei condensatori e dielettrici|lezione 9]], dove $C_{12}$ e $C_3$ erano in serie. Il docente insiste su una condizione: la formula vale quando i condensatori sono **in serie** e sono **soltanto due**.

## Esercizio — Quattro condensatori e due interruttori

> [!example] Testo
> Quattro condensatori, $C_1 = 1\ \mu\mathrm F$, $C_2 = 2\ \mu\mathrm F$, $C_3 = 3\ \mu\mathrm F$ e $C_4 = 4\ \mu\mathrm F$, sono collegati a una batteria come in figura, con due interruttori $S_1$ e $S_2$. (1) Si chiude $S_1$, con $S_2$ aperto: quali sono le cariche sui quattro condensatori? (2) Poi si chiude anche $S_2$: quali sono ora le cariche?

![[F2-L11-quattro-condensatori.svg]]

> [!warning] Schema e tensione della batteria
> Lo schema è ricostruito dalla descrizione a voce: due rami in parallelo ai capi della batteria, $C_1$–$C_3$ sopra e $C_2$–$C_4$ sotto, e l'interruttore $S_2$ che collega i punti intermedi dei due rami. È l'unica disposizione compatibile con quello che il docente dice e con i risultati. Il valore della tensione si perde nella trascrizione ("4 microfarad e..."). Dai risultati che il docente legge si ricava $V = 12\ \mathrm V$: ad esempio $q_1 = C_{13}V = 9\ \mu\mathrm C$ con $C_{13} = 0{,}75\ \mu\mathrm F$. Tutti e sei i valori numerici tornano con $V = 12\ \mathrm V$.

### Prima domanda: $S_2$ aperto

Con $S_1$ chiuso e $S_2$ aperto, il ramo di $S_2$ è come se non ci fosse. Restano due rami, ciascuno con due condensatori uno dopo l'altro. $C_1$ e $C_3$ sono **in serie**, e così $C_2$ e $C_4$:

$$
C_{13} = \frac{C_1C_3}{C_1 + C_3} = \frac{1\cdot3}{4}\ \mu\mathrm F = 0{,}75\ \mu\mathrm F,
\qquad
C_{24} = \frac{C_2C_4}{C_2 + C_4} = \frac{2\cdot4}{6}\ \mu\mathrm F = 1{,}33\ \mu\mathrm F .
$$

I due rami sono attaccati entrambi, da una parte, al polo positivo della batteria e, dall'altra, al polo negativo: hanno la stessa differenza di potenziale $V$, quindi sono **in parallelo**, con $C_{\text{eq}} = C_{13} + C_{24}$.

Per le cariche il docente guarda un ramo alla volta. $C_1$ e $C_3$ sono in serie, quindi hanno la stessa carica, ed è anche la carica del loro condensatore equivalente $C_{13}$: $q_1 = q_3 = q_{13}$. Il condensatore equivalente $C_{13}$ sente da una parte un polo della batteria e dall'altra l'altro polo, quindi ha ai capi l'intera tensione $V$:

$$
q_1 = q_3 = C_{13}V = \frac{C_1C_3}{C_1 + C_3}\,V = (0{,}75\ \mu\mathrm F)(12\ \mathrm V) = 9\ \mu\mathrm C .
$$

Lo stesso discorso vale per il ramo inferiore:

$$
q_2 = q_4 = C_{24}V = \frac{C_2C_4}{C_2 + C_4}\,V = (1{,}33\ \mu\mathrm F)(12\ \mathrm V) = 16\ \mu\mathrm C .
$$

Il metodo è sempre lo stesso, riassume il docente: capacità equivalenti, e poi ricordarsi che **in serie la carica è la stessa** e **in parallelo la tensione è la stessa**.

### Seconda domanda: $S_2$ chiuso

Chiudendo $S_2$ cambia la struttura del circuito. Il docente colora i conduttori: un colore per il filo collegato al polo positivo, uno per il filo intermedio (che ora, attraverso $S_2$, unisce i punti di mezzo dei due rami), uno per il filo collegato al polo negativo. I fili conduttori sono equipotenziali. Si vede allora che $C_1$ e $C_2$ hanno entrambi un'armatura sul primo filo e l'altra sul filo intermedio: hanno la stessa tensione e sono **in parallelo**. Lo stesso vale per $C_3$ e $C_4$, tra il filo intermedio e il terzo:

$$
C_{12} = C_1 + C_2 = 3\ \mu\mathrm F, \qquad C_{34} = C_3 + C_4 = 7\ \mu\mathrm F .
$$

I due blocchi sono in serie tra i poli della batteria, con $C_{\text{eq}} = C_{12}C_{34}/(C_{12} + C_{34}) = 2{,}1\ \mu\mathrm F$. Per le cariche però servono le tensioni, ed è qui che torna utile lo schema dell'esercizio precedente. $C_{12}$ e $C_{34}$ sono due condensatori in serie, e soli, con la tensione $V$ ai capi: è il partitore capacitivo, con $C_{12}$ al posto di $C_1$ e $C_{34}$ al posto di $C_2$.

$$
V_{12} = \frac{C_{34}}{C_{12} + C_{34}}\,V = \frac{7}{10}\,(12\ \mathrm V) = 8{,}4\ \mathrm V,
\qquad
V_{34} = \frac{C_{12}}{C_{12} + C_{34}}\,V = 3{,}6\ \mathrm V .
$$

$V_{12}$ è la differenza di potenziale tra il primo filo e quello intermedio, quindi è la tensione ai capi sia di $C_1$ sia di $C_2$. Allo stesso modo $V_{34}$ è la tensione ai capi di $C_3$ e di $C_4$. Le cariche sono allora:

$$
q_1 = C_1V_{12} = 8{,}4\ \mu\mathrm C, \quad
q_2 = C_2V_{12} = 16{,}8\ \mu\mathrm C, \quad
q_3 = C_3V_{34} = 10{,}8\ \mu\mathrm C, \quad
q_4 = C_4V_{34} = 14{,}4\ \mu\mathrm C .
$$

Le formule esplicite si possono scrivere, ma diventano complicate; con i numeri il calcolo è immediato.

Il docente ripete poi il ragionamento del partitore per chi l'aveva perso: con il partitore si evita di passare ogni volta per cariche, capacità equivalenti e inversioni. Una volta ricordata la regola, basta applicarla.

> [!tip] Controllo con la conservazione della carica #approfondimento
> Il filo intermedio, con le armature che vi sono collegate, è un conduttore isolato: la batteria non lo tocca. Prima della chiusura di $S_2$ i due pezzi di cui è fatto erano neutri, perché ciascuno portava $-q_1 + q_3 = 0$ e $-q_2 + q_4 = 0$. Dopo la chiusura la sua carica deve restare nulla, ed è così: $-q_1 - q_2 + q_3 + q_4 = -8{,}4 - 16{,}8 + 10{,}8 + 14{,}4 = 0$. Un controllo che non richiede di ricordare nessuna formula.

## Un excursus: il diodo

Gli esercizi sui condensatori, ammette il docente, possono diventare noiosi: in fondo sono sempre un rimescolamento di cariche. Ne mostra allora uno diverso, che fa lui alla lavagna e che "non vedremo più", perché contiene **diodi**, elementi non lineari che nel corso non verranno trattati. Serve a ragionare su come si muovono le cariche, su che cosa si carica e che cosa no.

### Che cos'è un diodo

Per l'esercizio basta una definizione operativa: il **diodo** è un elemento circuitale che lascia passare le cariche positive **solo nel verso della freccia** del suo simbolo. Nel verso opposto le blocca.

![[F2-L11-diodo.svg]]

È un elemento **non lineare**. Nella legge di Ohm la relazione tra tensione applicata e corrente è lineare, con pendenza fissata dalla resistenza ([[Fisica 2 - Lezione 10 - Corrente elettrica, resistenza e legge di Ohm|lezione 10]]). In un diodo reale invece, se si applica una tensione nel verso giusto, sotto una certa **tensione di soglia** non passa praticamente nulla; superata la soglia, la corrente cresce rapidamente. Se si inverte la polarità, la corrente è piccolissima, in pratica zero: si dice che il diodo è **polarizzato inversamente**. Nell'esercizio si assume il diodo ideale: corrente nulla nel verso vietato, nessun ostacolo nel verso permesso.

I diodi sono fondamentali in elettronica. Senza elementi come diodi e transistor, osserva il docente, ci sarebbe solo elettronica passiva. Nel corso però si studieranno solo elementi lineari.

> [!warning] Nome della tensione di soglia
> A lezione la tensione di soglia viene indicata con $V_T$ e chiamata "potenziale termico". Nella letteratura sui semiconduttori $V_T$ indica di solito la **tensione termica** $k_BT/e$, che a temperatura ambiente vale circa $26\ \mathrm{mV}$ ed è un'altra grandezza. La soglia di conduzione di un diodo al silicio è molto più alta, dell'ordine di qualche decimo di volt. Qui l'ho indicata con $V_s$ per evitare confusione.

### Esercizio — Due condensatori e due diodi

> [!example] Testo
> Un circuito ha due morsetti d'ingresso $A$ e $B$ e due morsetti d'uscita $C$ e $D$. Contiene due condensatori uguali di capacità $C$ e due diodi. (1) Ai capi $AB$ si applica una batteria con $V = 100\ \mathrm V$, positiva in $A$: quale tensione $V_{\text{out}}$ misura un voltmetro ai capi $CD$? (2) Con i condensatori carichi, si inverte la polarità della batteria: quanto vale ora $V_{\text{out}}$?

![[F2-L11-circuito-diodi.svg]]

> [!warning] Schema ricostruito
> Il disegno della lavagna non è disponibile. Dalla descrizione del docente lo schema è questo: il primo condensatore sta sul tratto orizzontale in alto, subito dopo $A$; segue un diodo $D_1$ che lascia passare le cariche positive verso l'uscita; il secondo condensatore è ai capi dell'uscita, tra $C$ e $D$; un secondo diodo $D_2$ collega il punto tra il primo condensatore e $D_1$ al filo in basso, orientato in modo da far passare le cariche positive solo dal basso verso l'alto. Tutto quello che il docente dice nei due punti è coerente con questa disposizione. Attenzione al doppio uso della lettera: $C$ è sia la capacità sia il nome di un morsetto d'uscita.

**(1) $A$ positivo.** Il docente segue le cariche positive. Dal polo positivo arrivano sull'armatura sinistra del primo condensatore e la caricano. Le cariche positive dell'armatura destra vengono respinte e si spostano verso destra. Incontrano $D_1$, che le lascia passare, e caricano positivamente l'armatura superiore del condensatore d'uscita. Le cariche respinte dall'armatura inferiore di questo tornano, lungo il filo in basso, verso il polo negativo: il circuito è chiuso, e i due condensatori si caricano. Nel ramo di $D_2$ invece le cariche positive dovrebbero scendere, e il diodo lo vieta: quel ramo è come se non ci fosse.

Il circuito equivalente è allora una batteria con **due condensatori uguali in serie**:

$$
C_{\text{eq}} = \frac{C\cdot C}{C + C} = \frac{C}{2}, \qquad
q = C_{\text{eq}}V = \frac{C}{2}\,V .
$$

In serie ogni condensatore porta la carica totale $q$, quindi la tensione ai capi del condensatore d'uscita è

$$
V_{\text{out}} = \frac{q}{C} = \frac{V}{2} = 50\ \mathrm V .
$$

È anche il partitore capacitivo con due capacità uguali: la tensione si divide a metà.

**(2) Polarità invertita.** Ora $A$ è negativo e $B$ positivo. Le cariche positive dell'armatura sinistra del primo condensatore sono attratte dal polo negativo, e il condensatore si scarica. Questa volta $D_2$ lascia passare le cariche positive dal filo in basso verso l'alto: arrivano sull'armatura destra del primo condensatore, che era negativa, e ne neutralizzano la carica.

Il condensatore d'uscita invece non può scaricarsi. Per farlo, le cariche positive della sua armatura superiore dovrebbero tornare indietro attraverso $D_1$, l'unico filo collegato a quell'armatura, e il diodo lo vieta. Le cariche restano dove sono, trattengono le cariche negative sull'altra armatura, e il condensatore resta carico come prima. Di fatto non è più collegato alla batteria. Quindi

$$
V_{\text{out}} = 50\ \mathrm V
$$

anche dopo l'inversione. Il diodo funziona come una valvola che "intrappola" la carica.

> [!warning] Il primo condensatore non resta scarico
> Il docente dice che il primo condensatore "si scarica e non è più carico". Con una batteria ideale e diodi ideali, dopo l'inversione il primo condensatore si trova direttamente ai capi della batteria, attraverso $D_2$ che conduce. Quindi non si ferma a carica zero: si scarica e poi si ricarica con la polarità opposta, fino ad avere ai capi l'intera tensione $V = 100\ \mathrm V$. La conclusione sull'uscita non cambia. Il punto tra il primo condensatore e $D_1$ è collegato al morsetto $B$, mentre l'armatura superiore del condensatore d'uscita resta a $50\ \mathrm V$ sopra $B$. $D_1$ è quindi polarizzato inversamente, non conduce, e $V_{\text{out}}$ resta $50\ \mathrm V$.

> [!tip] Un circuito che si usa davvero #approfondimento
> La combinazione di un condensatore in serie con un diodo verso massa, seguita da un diodo e da un condensatore d'uscita, è la struttura di un **duplicatore di tensione**. Se all'ingresso si applica una tensione che si inverte periodicamente, il primo condensatore si carica attraverso $D_2$ in una semionda, e nella semionda successiva la sua tensione si somma a quella del generatore. Ciclo dopo ciclo il condensatore d'uscita si carica sempre di più, fino a tendere al **doppio** dell'ampiezza della tensione d'ingresso.

## La forza elettromotrice

### Che cosa fa una batteria

Il docente introduce il concetto con una domanda. Si collega un dispositivo a una batteria (un cellulare, un tablet, un computer) e la corrente continua a scorrere. Com'è possibile? Se nel circuito non ci fosse nient'altro, le cariche positive uscite da un polo arriverebbero all'altro, le cariche si bilancerebbero e tutto si fermerebbe, come quando un condensatore carico si scarica attraverso un filo.

Il trucco è che nella batteria c'è qualcosa che **fa lavoro**. Quando le cariche positive arrivano al polo negativo, vengono riportate al polo positivo, "in salita", contro il campo elettrico. Così la differenza di potenziale si ricrea continuamente e la corrente continua a scorrere. Questa capacità di spostare cariche contro il potenziale si chiama **forza elettromotrice** (abbreviata f.e.m.) e si indica con $\varepsilon$ (o anche $\mathcal E$).

Il primo esempio è la **pila di Volta**. Alessandro Volta, che lavorava a Pavia, la costruì impilando elementi chimici, da cui il nome "pila". In una pila è la **chimica** a spostare le cariche dal polo negativo al positivo e a mantenere costante la differenza di potenziale. Per questo le pile si scaricano: quando le reazioni chimiche hanno esaurito il loro "potenziale chimico", in senso lato, non riescono più a spostare cariche. Ma ci sono altri modi di produrre una forza elettromotrice: i **generatori elettrici**, ad esempio quelli azionati da un motore diesel o a benzina, oppure le **termopile**, che trasformano una differenza di temperatura in forza elettromotrice. La forza elettromotrice è quindi la generalizzazione della batteria: qualunque dispositivo che fa lavoro per spostare cariche elettriche contro il potenziale.

> [!tip] La pila di Volta #approfondimento
> Volta annunciò la sua pila nel 1800, in una lettera a Sir Joseph Banks, presidente della Royal Society, pubblicata nelle *Philosophical Transactions* [@volta1800]. Era una colonna di dischi di due metalli diversi, alternati con dischi di cartone o panno imbevuti di acqua salata. Fu la prima sorgente di corrente continua, e rese possibili gli esperimenti sulla corrente elettrica del primo Ottocento, compresi quelli di Ohm ([[Fisica 2 - Lezione 10 - Corrente elettrica, resistenza e legge di Ohm|lezione 10]]).

### Definizione

In termini matematici, la forza elettromotrice è il lavoro fatto per unità di carica spostata:

> [!important] Forza elettromotrice
> $$
> \varepsilon = \frac{dL}{dq} .
> $$
> È il lavoro $dL$ che il generatore compie per spostare una carica $dq$ dal polo negativo al polo positivo, diviso per la carica. Si misura in volt, come una differenza di potenziale: $1\ \mathrm V = 1\ \mathrm J/\mathrm C$.

### La f.e.m. e la corrente: l'argomento energetico

Si consideri un circuito con una forza elettromotrice $\varepsilon$ e una resistenza $R$, percorso da una corrente $i$. Dalla definizione, il lavoro fatto dal generatore per spostare la carica $dq$ è $dL = \varepsilon\,dq$. Poiché $i = dq/dt$, la carica che passa in un tempo $dt$ è $dq = i\,dt$, e quindi

$$
dL = \varepsilon\,i\,dt .
$$

D'altra parte la potenza è il lavoro per unità di tempo, $P = dL/dt$, e nella lezione 10 abbiamo visto che in una resistenza $P = i^2R$. Il lavoro infinitesimo si può allora scrivere anche

$$
dL = P\,dt = i^2R\,dt .
$$

Le due espressioni descrivono lo stesso lavoro: quello che il generatore fornisce è quello che la resistenza dissipa. Uguagliandole, $\varepsilon\,i\,dt = i^2R\,dt$, e semplificando $i\,dt$:

$$
\varepsilon = iR .
$$

Il risultato conferma che la forza elettromotrice ha le dimensioni di una tensione. La fenomenologia può essere qualsiasi (chimica, meccanica, termica), ma in un circuito la f.e.m. si comporta come una differenza di potenziale, legata alla resistenza e alla corrente dalla stessa relazione della legge di Ohm.

Nei circuiti la forza elettromotrice si rappresenta con lo stesso simbolo della batteria, due tratti paralleli: quello lungo e sottile è il polo positivo, quello corto e spesso il negativo.

> [!tip] Forza elettromotrice e differenza di potenziale #approfondimento
> Nonostante il nome, la forza elettromotrice non è una forza ma un lavoro per unità di carica. E non è nemmeno la stessa cosa della differenza di potenziale. La f.e.m. misura il lavoro delle forze **non elettrostatiche** (chimiche, meccaniche) che spingono le cariche dentro il generatore. La differenza di potenziale misura il lavoro del campo elettrostatico. Le due coincidono ai capi di una batteria ideale; in una batteria reale, come si vedrà tra poco, la tensione ai morsetti è minore della f.e.m. quando circola corrente.

## La legge delle maglie

### L'enunciato

Alla relazione $\varepsilon = iR$ si arriva anche per un'altra strada, che ha il vantaggio di introdurre una delle due **leggi di Kirchhoff**, gli strumenti fondamentali per studiare i circuiti. Una **maglia** è un percorso chiuso in un circuito.

> [!important] Legge delle maglie
> Partendo da un punto di un circuito e percorrendo una maglia completa fino a tornare al punto di partenza, la **somma algebrica** delle differenze di potenziale incontrate attraverso tutti gli elementi del circuito è **zero**.

"Somma algebrica" significa che ogni differenza di potenziale va presa con il suo segno: a volte positivo, a volte negativo.

> [!tip] Perché la legge vale #approfondimento
> La legge delle maglie è la conservazione dell'energia per una carica che percorre un circuito chiuso. Nella [[Fisica 2 - Lezione 07 - Potenziale elettrico|lezione 7]] abbiamo visto che il campo elettrostatico è conservativo e che il potenziale è una funzione del punto: tornando al punto di partenza si ritrova lo stesso potenziale, qualunque sia il percorso. Le variazioni lungo il giro devono quindi compensarsi esattamente. Le due leggi dei circuiti, nodi e maglie, prendono il nome da Gustav Kirchhoff, che le formulò nel 1845 da studente, in un lavoro sul passaggio della corrente in una lastra conduttrice [@kirchhoff1845].

### Un esempio: ancora $\varepsilon = iR$

Il docente applica la legge al circuito più semplice: una batteria ideale e una resistenza.

![[F2-L11-maglia-potenziale.svg]]

Il punto di partenza è arbitrario, perché si percorre un giro chiuso. Il docente parte dal punto $a$, collegato al polo negativo della batteria, e gli associa un potenziale $V_a$ non noto. Anche il verso di percorrenza è arbitrario; sceglie quello orario. A ogni elemento del circuito che si incontra bisogna chiedersi se si sta andando verso un potenziale più alto o più basso.

Il primo elemento è la batteria, che si attraversa dal polo negativo al polo positivo. Il punto $b$, collegato al polo positivo, ha un potenziale maggiore di $a$, e la differenza è proprio la forza elettromotrice:

$$
V_b = V_a + \varepsilon .
$$

Poi si percorre il filo fino alla resistenza. Un filo ideale è equipotenziale, quindi il capo superiore della resistenza è a potenziale $V_b$. L'altro capo, il punto $c$, è sullo stesso filo di $a$ e quindi $V_c = V_a$. La corrente nel circuito esterno scorre dal polo positivo verso il negativo, cioè da $b$ verso $c$ attraverso la resistenza. Attraversando la resistenza da $b$ a $c$ si va da un potenziale più alto a uno più basso, e la caduta di potenziale ai capi di una resistenza è $iR$ ([[Fisica 2 - Lezione 10 - Corrente elettrica, resistenza e legge di Ohm|lezione 10]]):

$$
V_c = V_b - iR .
$$

Mettendo insieme, con $V_c = V_a$:

$$
V_a + \varepsilon - iR = V_a
\quad\Longrightarrow\quad
\varepsilon = iR .
$$

È la stessa relazione ottenuta con l'argomento energetico. Il grafico (b) della figura mostra l'idea: lungo la maglia il potenziale sale di $\varepsilon$ attraversando la batteria e scende di $iR$ attraversando la resistenza, e alla fine del giro torna al valore iniziale.

### Le regole dei segni

Dall'esempio si ricavano regole che, una volta capite, si applicano sempre in modo meccanico. Si fissa un verso di percorrenza della maglia, a piacere. Poi, a ogni elemento:

![[F2-L11-regole-segni.svg]]

> [!important] Regole dei segni
> - **Resistenza** percorsa da una corrente $i$: se la si attraversa **nello stesso verso della corrente** si va da un potenziale più alto a uno più basso, e la variazione è $\Delta V = -iR$. Se la si attraversa **in verso opposto** alla corrente, $\Delta V = +iR$.
> - **Forza elettromotrice**: se la si attraversa **dal polo negativo al polo positivo** il potenziale aumenta, $\Delta V = +\varepsilon$. Se la si attraversa dal positivo al negativo, $\Delta V = -\varepsilon$.

Il verso di percorrenza è arbitrario, ribadisce il docente. In un circuito con molte maglie si può scegliere una maglia qualsiasi e percorrerla in un verso qualsiasi. Una volta scelto il verso, però, le regole vanno applicate con coerenza.

> [!warning] "La corrente scorre sempre dal più al meno"
> A lezione si dice che la corrente scorre sempre dal polo positivo al polo negativo. Vale per il **circuito esterno** al generatore. **Dentro** il generatore la corrente va dal polo negativo al positivo: è proprio il lavoro della forza elettromotrice a spingerla "in salita". Inoltre in un circuito con più generatori il verso della corrente in un ramo non si conosce in anticipo. Si sceglie un verso arbitrario, e se alla fine la corrente risulta negativa scorre nel verso opposto, come per i nodi nella lezione 10.

### La batteria reale

Come ultimo esempio il docente tratta le **batterie non ideali**. Una batteria reale ha una **resistenza interna** $r$, dovuta alla sua costruzione, che non si può eliminare. Nei circuiti la si schematizza come una f.e.m. ideale in serie con una piccola resistenza $r$.

![[F2-L11-batteria-reale.svg]]

Si usa la legge delle maglie, partendo da un punto $a$ e percorrendo la maglia nel verso della corrente. Attraversando la f.e.m. dal polo negativo al positivo il potenziale sale di $\varepsilon$. Poi si incontra la resistenza interna. La corrente la attraversa nello stesso verso del percorso, quindi il potenziale scende di $ir$. Si percorre il filo fino alla resistenza esterna $R$, anch'essa attraversata nel verso della corrente: il potenziale scende di $iR$. Superata $R$ si torna su un filo al potenziale $V_a$:

$$
V_a + \varepsilon - ir - iR = V_a
\quad\Longrightarrow\quad
\varepsilon = i\,(r + R) .
$$

La forza elettromotrice di una batteria reale fa circolare la corrente attraverso la resistenza esterna e quella interna insieme. Il docente anticipa che questa è in realtà la regola delle **resistenze in serie**: $r$ e $R$ sono attraversate dalla stessa corrente e si sommano. Lo si vedrà meglio nella lezione successiva ([[Fisica 2 - Lezione 12 - Circuiti in corrente continua e circuiti RC|lezione 12]]).

> [!tip] La tensione ai morsetti #approfondimento
> La tensione che un voltmetro misura ai morsetti di una batteria reale è $V = \varepsilon - ir$, minore della f.e.m. quando circola corrente. Con il circuito aperto ($i = 0$) si misura proprio $\varepsilon$; più corrente si chiede, più la tensione ai morsetti scende. Se si cortocircuitano i morsetti ($R = 0$), la corrente è limitata solo dalla resistenza interna, $i = \varepsilon/r$: con $r$ piccola può essere molto intensa, ed è per questo che un cortocircuito scalda pericolosamente la batteria.
