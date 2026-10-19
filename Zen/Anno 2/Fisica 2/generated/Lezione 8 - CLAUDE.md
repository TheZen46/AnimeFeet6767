---
corso: Fisica 2
lezione: 8
data: 2026-10-16
argomenti: [potenziale di un disco carico, campo dal gradiente del potenziale, differenza di potenziale in campo uniforme, capacità, farad, carica di un condensatore, condensatore a facce piane parallele, condensatore sferico, condensatori in parallelo, condensatori in serie, capacità equivalente]
bibliography: fisica2.bib
tags: [fisica2]
---

# Lezione 8 — Potenziale del disco, capacità e condensatori

La lezione chiude il discorso sul potenziale con due esempi: il potenziale di un disco carico, da cui si ritrova il campo della [[Fisica 2 - Lezione 03 - Distribuzioni continue di carica|lezione 3]] con il gradiente, e un calcolo di differenza di potenziale in un campo uniforme che mette in luce il carattere conservativo del campo. Poi si passa a un nuovo argomento: la **capacità** e i **condensatori** (o capacitori). Si calcola la capacità dei condensatori piano e sferico e si ricavano le regole per combinare condensatori in parallelo e in serie.

## Riepilogo

Il potenziale elettrostatico ha due facce, ricorda il docente. È legato all'energia: è il lavoro per spostare una carica lungo una traiettoria, diviso per la carica. Ed è legato al campo elettrico: $\Delta V = -\int\vec E\cdot d\vec s$ e, nel verso opposto, $\vec E = -\nabla V$. I fenomeni elettrostatici si possono descrivere con l'una o con l'altra grandezza, e conviene scegliere caso per caso.

## Potenziale di un disco carico sul suo asse

> [!example] Testo
> Un disco di raggio $R$ è carico uniformemente con densità superficiale $\sigma = Q/A$. Calcolare il potenziale nel punto $P$ sull'asse del disco, a distanza $z$ dal centro.

Come per il campo, conviene pensare il disco come un insieme di **anelli** concentrici. La carica di un anello di raggio $r$ e spessore $dr$ è $dq = \sigma\,dA = \sigma\,2\pi r\,dr$: la circonferenza per lo spessore, oppure il differenziale dell'area del cerchio. Tutti i punti dell'anello hanno la stessa distanza da $P$, $d = \sqrt{r^2 + z^2}$, quindi il potenziale dell'anello è quello di una carica puntiforme $dq$ a distanza $d$:

$$
dV = k\,\frac{dq}{d} = k\,\frac{\sigma\,2\pi r\,dr}{\sqrt{r^2 + z^2}} .
$$

Si integra in $r$ da $0$ a $R$. Al numeratore compare $r\,dr$, e la primitiva di $r/\sqrt{r^2+z^2}$ è $\sqrt{r^2+z^2}$:

$$
V = 2\pi k\sigma\int_0^R \frac{r\,dr}{\sqrt{r^2+z^2}} = 2\pi k\sigma\left[\sqrt{r^2+z^2}\right]_0^R = 2\pi k\sigma\left(\sqrt{R^2+z^2} - z\right).
$$

In $r = 0$ resta $\sqrt{z^2} = z$, perché $z$ è positivo. Durante il calcolo uno studente ha fatto notare al docente che sotto radice doveva comparire $z^2$ e non $d^2$, e il docente ha corretto.

> [!important] Potenziale di un disco carico uniformemente, sull'asse
> $$
> V(z) = 2\pi k\sigma\left(\sqrt{R^2+z^2} - z\right) = \frac{\sigma}{2\varepsilon_0}\left(\sqrt{R^2+z^2} - z\right)
> $$

![[F2-L08-potenziale-disco.svg]]

### Verifica: dal potenziale al campo

Il campo dello stesso disco è stato calcolato nella lezione 3. Con $\vec E = -\nabla V$ si può verificare che i due risultati sono collegati. Bisogna però tenere presente una cautela, che il docente non esplicita. La funzione trovata dà $V$ solo sull'asse, quindi le derivate rispetto a $x$ e $y$ non si possono ricavare da essa in senso stretto. Il ragionamento va letto così: sull'asse, per simmetria, $V$ non varia spostandosi di poco lateralmente nelle direzioni $x$ e $y$. Ne segue $E_x = E_y = 0$, lo stesso risultato ottenuto nella lezione 3 con elementi simmetrici le cui componenti trasversali si cancellano. La componente lungo $z$ è

$$
E_z = -\frac{\partial V}{\partial z} = -\frac{\sigma}{2\varepsilon_0}\left(\frac{2z}{2\sqrt{R^2+z^2}} - 1\right) = \frac{\sigma}{2\varepsilon_0}\left(1 - \frac{z}{\sqrt{R^2+z^2}}\right),
$$

esattamente il campo calcolato dai principi primi, con elementi, vettori e integrali. La parte difficile è arrivare al potenziale; una volta noto, il campo si ottiene con due derivate.

> [!warning] Refusi negli appunti
> Negli appunti si legge $(E_x, E_y, E_z) = \left(\frac{\partial V}{\partial x}, \frac{\partial V}{\partial y}, \frac{\partial V}{\partial z}\right)$, senza il segno meno: è $\vec E = -\nabla V$, come scritto subito prima. Nella derivata di $E_z$ compare "$-L$" dove va letto "$-1$", cioè la derivata di $z$.

> [!tip] Approfondimento — Due controlli sui limiti #approfondimento
> - **Lontano dal disco ($z \gg R$).** Con $\sqrt{R^2+z^2} \simeq z + \frac{R^2}{2z}$ si ottiene $V \simeq \frac{\sigma}{2\varepsilon_0}\frac{R^2}{2z} = \frac{k\,(\sigma\pi R^2)}{z} = \frac{kQ}{z}$: il potenziale di una carica puntiforme, come per il campo.
> - **Nel centro ($z = 0$).** $V(0) = \sigma R/(2\varepsilon_0)$ è finito. Il campo, invece, vale lì $\sigma/(2\varepsilon_0)$, come quello del piano infinito.

## Esercizio: differenza di potenziale in un campo uniforme

> [!example] Testo
> In un campo elettrico uniforme $\vec E$, diretto verso il basso, una carica si sposta da $A$ a $B$ in orizzontale, perpendicolarmente al campo, e poi da $B$ a $C$ lungo un tratto inclinato di $\theta = 45^\circ$. $A$ e $C$ stanno sulla stessa verticale, a distanza $d$. Calcolare la differenza di potenziale lungo il percorso $ABC$.

L'integrale è lineare, quindi lo si spezza nei due tratti:

$$
\Delta V_{ABC} = -\int_A^B \vec E\cdot d\vec s - \int_B^C \vec E\cdot d\vec s .
$$

- **Tratto $AB$.** Lo spostamento è orizzontale e il campo verticale: $\vec E\cdot d\vec s = 0$ in ogni punto, quindi $\Delta V_{AB} = 0$. $A$ e $B$ stanno sulla stessa equipotenziale.
- **Tratto $BC$.** Lo spostamento forma con il campo un angolo di $45^\circ$. In generale andrebbero distinti $\theta$ e $90^\circ - \theta$, ma qui valgono entrambi $45^\circ$. Quindi $\vec E\cdot d\vec s = E\,ds\cos45^\circ = E\,ds/\sqrt2$. L'inclinazione relativa non cambia lungo il tratto, perché sia il campo sia la direzione di moto sono fissi. Allora
  $$
  \Delta V_{BC} = -\frac{E}{\sqrt2}\int_B^C ds = -\frac{E}{\sqrt2}\,s .
  $$
  La lunghezza del tratto si ricava dal triangolo rettangolo: $d = s\sin45^\circ$, quindi $s = \sqrt2\,d$. Sostituendo, $\Delta V_{BC} = -Ed$.

In totale $\Delta V_{ABC} = -Ed$.

**Lo stesso risultato per la via diretta.** Lungo il segmento $AC$, verticale, il campo è parallelo allo spostamento:

$$
\Delta V_{AC} = -\int_A^C E\,ds = -E\int_A^C ds = -Ed .
$$

Il risultato è lo stesso perché il campo elettrostatico è conservativo: la differenza di potenziale dipende solo dai punti iniziale e finale. Si sarebbe potuto rispondere subito: si parte da $A$, si arriva in $C$, e se si passi o no per $B$ non conta. Avendo la libertà di scegliere il percorso, conviene scegliere il più semplice. Il segno meno indica che, muovendosi nel verso del campo, il potenziale diminuisce.

![[F2-L08-percorso-ABC.svg]]

> [!warning] Una svista alla lavagna
> Nella trascrizione si sente "$d$ è uguale a $s$ per il seno di $45^\circ$, e quindi $d$ è uguale a $s$". La relazione corretta, riportata anche negli appunti, è $s = \sqrt2\,d$.

## Capacità e condensatori

### Definizione

Si considerano due corpi conduttori di forma qualsiasi, uno con carica $+q$ e l'altro con carica uguale e opposta $-q$. Il docente evita la parola "piatti", in inglese *plates*, perché in italiano suggerisce corpi piani, mentre possono avere qualsiasi forma. I due corpi generano un campo elettrico, che esce da quello positivo ed entra in quello negativo, e tra i due c'è una differenza di potenziale $V$. Un sistema di questo tipo si chiama **condensatore**, o capacitore.

> [!important] Capacità
> $$
> C = \frac{q}{V} \qquad\Longleftrightarrow\qquad q = CV
> $$
> La capacità è il rapporto tra la carica sui due conduttori e la differenza di potenziale che si stabilisce tra di essi. Si misura in **farad**: $1\ \mathrm F = 1\ \mathrm C/\mathrm V$.

La proprietà interessante della capacità è che **dipende solo dalla geometria**: dalla forma, dalle dimensioni e dalla disposizione dei conduttori, non dalla carica o da altri dettagli. I casi tipici sono due piani paralleli affacciati, due sfere concentriche e due cilindri coassiali. Una volta costruito un condensatore, la sua capacità è fissata; caricandolo con una carica $q$ si ottiene la differenza di potenziale $V = q/C$.

![[F2-L08-condensatore.svg]]

Un farad è una capacità enorme, che nei corpi macroscopici non si vede mai. I condensatori usati in pratica vanno dal **picofarad**, $1\ \mathrm{pF} = 10^{-12}\ \mathrm F$, al **microfarad**, $1\ \mu\mathrm F = 10^{-6}\ \mathrm F$. Negli esercizi, che sono idealizzati, possono comparire valori anche molto più grandi.

> [!tip] Approfondimento — Quanto è grande un farad #approfondimento
> Una sfera conduttrice isolata di raggio $R$ ha capacità $C = 4\pi\varepsilon_0R$, che si ottiene dal condensatore sferico, ricavato più avanti, facendo tendere all'infinito il raggio esterno. Anche una sfera grande come la Terra, $R \simeq 6{,}4\cdot10^6\ \mathrm m$, ha una capacità di appena $7\cdot10^{-4}\ \mathrm F$, meno di un millifarad. I condensatori da molti farad, detti supercondensatori, esistono, ma sfruttano strutture microscopiche con superfici enormi e distanze minuscole tra le cariche.

### Il simbolo e la carica di un condensatore

Nei circuiti il condensatore si indica con due sbarrette parallele, che ricordano il condensatore piano, qualunque sia la sua geometria reale. Per caricarlo lo si inserisce in un circuito con una **batteria** e un **interruttore**. Per ora basta sapere che la batteria ha un polo positivo e uno negativo; il suo funzionamento si vedrà più avanti. Il simbolo della batteria è una sbarretta lunga, il polo positivo, affiancata a una corta e spessa, il polo negativo.

Finché l'interruttore è aperto non passa corrente e il condensatore è scarico. Quando lo si chiude, le cariche nei fili possono muoversi. Nei fili si muovono gli **elettroni**, che sono negativi. Vengono attratti dal polo positivo della batteria, quindi l'armatura collegata a quel polo perde elettroni e si carica positivamente. Dal polo negativo, invece, gli elettroni vengono spinti verso l'altra armatura, che si carica negativamente. L'equilibrio si raggiunge quando le due armature hanno cariche uguali e opposte, $+q$ e $-q$. A quel punto tra le armature c'è la differenza di potenziale $V$ legata a $q$ dalla capacità.

![[F2-L08-carica-condensatore.svg]]

> [!important] I fili all'equilibrio sono equipotenziali
> All'equilibrio ogni filo conduttore è tutto allo stesso potenziale. Se due punti dello stesso conduttore avessero potenziali diversi, ci sarebbe un campo elettrico, e quindi cariche in movimento e dissipazione. Il periodo in cui le cariche scorrono, subito dopo la chiusura dell'interruttore, si chiama **transitorio**. La capacità descrive il sistema **all'equilibrio**, dopo il transitorio. Ne segue che la differenza di potenziale tra due punti qualsiasi dei due fili, uno collegato al polo positivo e l'altro al negativo, è la stessa $V$ che c'è tra le armature e tra i poli della batteria.

> [!tip] Corrente convenzionale ed elettroni
> Quando si iniziò a studiare la corrente si sapeva già che esistono due tipi di carica, ma non quale si muovesse nei fili. Si suppose che fossero le cariche positive; più tardi si scoprì che le cariche mobili sono gli elettroni. Per questo nei circuiti si ragiona di solito come se si muovessero cariche positive, cioè con la corrente convenzionale, anche se a muoversi sono gli elettroni in verso opposto. È la conseguenza della convenzione sui segni vista nella [[Fisica 2 - Lezione 01 - Carica elettrica e legge di Coulomb|lezione 1]].

## Condensatore a facce piane parallele

Due armature piane conduttrici di area $A$, affacciate a distanza $d$, portano cariche $+q$ e $-q$. Il metodo, che vale per ogni geometria, è in quattro passi: si calcola il campo con il teorema di Gauss, si calcola la differenza di potenziale con l'integrale del campo, si lega $V$ a $q$ e si fa il rapporto.

**Campo.** Le armature sono conduttori, quindi le cariche stanno sulle superfici, e quelle affacciate si attraggono. Se le armature sono abbastanza grandi da poterle considerare infinite, il campo tra di esse è perpendicolare alle armature e uniforme, come visto nella [[Zen/Anno 2/Fisica 2/generated/Lezione 6 - CLAUDE|lezione 6]]. Si prende una superficie gaussiana a forma di scatola che racchiude la faccia carica dell'armatura positiva.

- **Facce laterali (1 e 2).** Il campo è parallelo a esse, quindi perpendicolare alla loro normale: $\Phi_1 = \Phi_2 = 0$.
- **Faccia 3.** Si trova dentro il conduttore, dove il campo è nullo: $\Phi_3 = 0$.
- **Faccia 4.** Si trova tra le armature, dove il campo è parallelo alla normale e uniforme: $\Phi_4 = EA$.

Il teorema di Gauss dà quindi

$$
\varepsilon_0 EA = q \quad\Longrightarrow\quad E = \frac{q}{\varepsilon_0 A},
$$

che è il campo $\sigma/\varepsilon_0$ del piano conduttore, con $\sigma = q/A$.

**Potenziale.** Il campo è conservativo, quindi si sceglie il percorso più comodo: un segmento perpendicolare alle armature, dall'armatura negativa a quella positiva. Lungo questo percorso il campo e lo spostamento sono antiparalleli, $\vec E\cdot d\vec s = -E\,ds$, e il segno meno si cancella con quello della definizione. Il campo è costante, quindi esce dall'integrale, e resta la lunghezza del percorso, cioè la distanza $d$ tra le armature:

$$
V = -\int_i^f \vec E\cdot d\vec s = \int_i^f E\,ds = E\,d = \frac{q\,d}{\varepsilon_0 A}.
$$

**Capacità.** Facendo il rapporto:

> [!important] Capacità del condensatore piano
> $$
> C = \frac{q}{V} = \frac{\varepsilon_0 A}{d}
> $$

![[F2-L08-condensatore-piano.svg]]

La capacità dipende solo dalla geometria, cioè dall'area delle armature e dalla loro distanza. Per aumentarla si aumenta l'area oppure si avvicinano le armature: più sono grandi e vicine, maggiore è la capacità. Una volta costruito il condensatore, la capacità è bloccata. Si sa allora che, caricandolo con $q$, si ottiene la differenza di potenziale $V = q/C$.

## Condensatore sferico

Una sfera conduttrice di raggio $a$ con carica $+q$ è circondata da un guscio sferico concentrico di raggio $b > a$ con carica $-q$. Il procedimento è lo stesso.

**Campo.** Si prende una superficie gaussiana sferica di raggio $r$, con $a < r < b$. Il campo è radiale, parallelo al vettore area, e per simmetria costante sulla sfera. La carica racchiusa è solo quella della sfera interna, $+q$:

$$
\varepsilon_0\,E\,4\pi r^2 = q \quad\Longrightarrow\quad E = \frac{q}{4\pi\varepsilon_0 r^2}.
$$

**Potenziale.** Il percorso più comodo è radiale, perché i prodotti scalari si ottengono "gratis". La differenza rispetto al caso piano è che ora il campo dipende dalla distanza, quindi l'integrale va fatto davvero. La differenza di potenziale tra l'armatura interna, positiva, e quella esterna, negativa, è

$$
V = V_a - V_b = -\int_b^a E\,dr = \int_a^b \frac{q}{4\pi\varepsilon_0}\frac{dr}{r^2} = \frac{q}{4\pi\varepsilon_0}\left[-\frac1r\right]_a^b = \frac{q}{4\pi\varepsilon_0}\left(\frac1a - \frac1b\right) = \frac{q\,(b-a)}{4\pi\varepsilon_0\,ab}.
$$

L'armatura positiva è, come deve essere, a potenziale più alto.

> [!important] Capacità del condensatore sferico
> $$
> C = \frac{q}{V} = 4\pi\varepsilon_0\,\frac{ab}{b-a}
> $$

![[F2-L08-condensatore-sferico.svg]]

Anche qui la capacità dipende solo dalla geometria, cioè dai due raggi. Una volta scelti, la capacità è determinata in modo univoco.

> [!warning] I segni nel calcolo alla lavagna
> Alla lavagna il docente sceglie un percorso dall'armatura esterna a quella interna. Scrive $\vec E\cdot d\vec s = -E\,ds$ e poi integra in $dr$ da $b$ ad $a$, contando così due volte il cambio di verso. Uno studente fa notare che la primitiva di $1/r^2$ è $-1/r$, e il risultato esce con un segno sbagliato. Negli appunti la capacità è scritta $4\pi\varepsilon_0\,ab/(a-b)$, che è negativa per $a < b$. Come dice il docente, la capacità è per definizione **positiva**: si prendono i valori assoluti, $C = |q/V| = 4\pi\varepsilon_0\,ab/(b-a)$. Il calcolo pulito è quello riportato sopra. Negli appunti, inoltre, la sezione del condensatore sferico è intitolata per errore "Capacitore piani paralleli".

> [!tip] Approfondimento — Limiti e condensatore cilindrico #approfondimento
> - **Raggio esterno all'infinito ($b \to \infty$).** $C \to 4\pi\varepsilon_0 a$, la capacità di una sfera isolata.
> - **Armature molto vicine ($b - a = d \ll a$).** $C \simeq 4\pi\varepsilon_0 a^2/d = \varepsilon_0 A/d$, con $A = 4\pi a^2$: da vicino le sfere sembrano piani, e si ritrova il condensatore piano.
> - **Condensatore cilindrico.** Il docente lo nomina senza svolgerlo. Con due cilindri coassiali di raggi $a < b$ e lunghezza $L$, lo stesso procedimento, con il campo del filo $\lambda/(2\pi\varepsilon_0 r)$, dà $C = 2\pi\varepsilon_0 L/\ln(b/a)$.

## Condensatori in parallelo

> [!warning] Inizio della parte dopo la pausa
> La ripresa dopo la pausa è in parte coperta da conversazioni in aula. La trascrizione torna leggibile quando il docente sta già descrivendo il circuito in parallelo, con tre condensatori collegati agli stessi due fili. L'impostazione si ricava dal seguito e dagli appunti.

In un collegamento **in parallelo**, ogni condensatore ha un'armatura collegata al filo superiore e l'altra al filo inferiore. Il filo superiore è collegato al polo positivo della batteria e quello inferiore al polo negativo. I fili sono conduttori, quindi equipotenziali: tutte le armature superiori sono allo stesso potenziale, e così tutte quelle inferiori. Ne segue che **la differenza di potenziale è la stessa** su tutti i condensatori, ed è quella $V$ della batteria. È la quantità invariante del collegamento in parallelo. Le cariche, invece, dipendono dalle singole capacità:

$$
q_1 = C_1 V, \qquad q_2 = C_2 V, \qquad q_3 = C_3 V .
$$

La carica totale accumulata è la somma:

$$
q_{\text{tot}} = q_1 + q_2 + q_3 = \left(C_1 + C_2 + C_3\right)V .
$$

È una relazione tra la carica totale e il potenziale applicato, cioè la definizione di una nuova capacità, la **capacità equivalente**: $q_{\text{tot}} = C_{\text{eq}}V$. Il circuito con tre condensatori si comporta esattamente come un circuito con un solo condensatore di capacità $C_{\text{eq}}$.

> [!important] Condensatori in parallelo
> Stessa differenza di potenziale su tutti; le capacità si sommano:
> $$
> C_{\text{eq}} = \sum_{i=1}^{n} C_i
> $$

![[F2-L08-condensatori-parallelo.svg]]

Mettendo condensatori in parallelo si aumenta la capacità. Se servono mille volte la capacità di un condensatore, se ne mettono mille in parallelo, e il circuito si comporta esattamente allo stesso modo. Per studiare circuiti complessi, ad esempio la carica e la scarica dopo la chiusura di un interruttore, la strada è sempre calcolare la capacità equivalente e studiare il comportamento complessivo.

## Condensatori in serie

In un collegamento **in serie** i condensatori sono uno dopo l'altro sullo stesso ramo. Ora i tratti di filo tra un condensatore e l'altro non sono collegati alla batteria, quindi in generale non sono allo stesso potenziale delle armature estreme.

La quantità invariante qui è la **carica**. L'armatura superiore del primo condensatore è collegata al polo positivo e si carica con $+q$; quella inferiore dell'ultimo è collegata al polo negativo e si carica con $-q$. All'equilibrio le due armature di ogni condensatore hanno cariche uguali e opposte, quindi l'armatura inferiore del primo ha $-q$. Il tratto di filo tra il primo e il secondo condensatore, insieme alle armature che collega, è un conduttore isolato e **neutro**. Se su un'estremità si accumula $-q$, sull'altra deve comparire $+q$: sono solo gli elettroni del tratto di filo che si spostano, attratti dall'armatura positiva. Per questo effetto di **carica indotta**, tutti i condensatori in serie portano la stessa carica $q$, mentre le differenze di potenziale sono in generale diverse:

$$
V_1 = \frac{q}{C_1}, \qquad V_2 = \frac{q}{C_2}, \qquad V_3 = \frac{q}{C_3}.
$$

La differenza di potenziale totale è la somma:

$$
V = V_1 + V_2 + V_3 = q\left(\frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}\right).
$$

Per un circuito equivalente con un solo condensatore, $V = q/C_{\text{eq}}$. Uguagliando:

> [!important] Condensatori in serie
> Stessa carica su tutti; si sommano gli inversi delle capacità:
> $$
> \frac{1}{C_{\text{eq}}} = \sum_{i=1}^{n}\frac{1}{C_i}
> $$
> Per due condensatori, il caso più comune:
> $$
> C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2}.
> $$

![[F2-L08-condensatori-serie.svg]]

> [!warning] L'errore più frequente e come accorgersene
> Il docente avverte che la formula per due condensatori in serie viene spesso scritta capovolta, $(C_1 + C_2)/(C_1C_2)$, perché si dimentica di invertire alla fine. Il controllo dimensionale lo rivela subito. A sinistra c'è una capacità, in farad. Con la formula corretta, a destra c'è $\mathrm F^2/\mathrm F = \mathrm F$. Con quella sbagliata, $\mathrm F/\mathrm F^2 = 1/\mathrm F$, che è impossibile. È un controllo banale che salva da un errore grossolano.

Con queste due regole, cioè capacità che si sommano in parallelo e inversi che si sommano in serie, un circuito di condensatori complesso a piacere si può trasformare in uno equivalente più semplice. Secondo il docente è il principio su cui si regge tutta l'elettronica, che funziona in modo modulare (lo stesso vale per le resistenze). Senza questa possibilità, circuiti con miliardi di componenti sarebbero impossibili da capire e progettare.

## Esercizi

> [!warning] Sezione ricostruita — inizio
> La trascrizione (Parte 1) si interrompe proprio mentre il docente presenta il primo esercizio sulla capacità equivalente. Gli esercizi che seguono vengono dai tuoi **appunti a mano**, l'unica fonte disponibile per questa parte. Le spiegazioni sono mie e i calcoli li ho verificati.

### Esercizio 1 — Capacità equivalente di un circuito misto

> [!example] Testo (dagli appunti)
> Ai capi di una porzione di circuito c'è una differenza di potenziale $V$. Non interessa da dove provenga: potrebbe esserci una batteria o un altro pezzo di circuito. La porzione contiene due condensatori $C_1$ e $C_2$ in parallelo, a loro volta in serie con un condensatore $C_3$. Trovare la capacità equivalente.
>
> Si riduce il circuito un passo alla volta. $C_1$ e $C_2$ sono in parallelo, quindi equivalgono a $C_{12} = C_1 + C_2$. $C_{12}$ è poi in serie con $C_3$:
> $$
> \frac{1}{C_{\text{eq}}} = \frac{1}{C_{12}} + \frac{1}{C_3}
> \quad\Longrightarrow\quad
> C_{\text{eq}} = \frac{C_{12}C_3}{C_{12} + C_3} = \frac{(C_1 + C_2)\,C_3}{C_1 + C_2 + C_3}.
> $$

![[F2-L08-circuito-misto.svg]]

> [!warning] Dati mancanti
> Negli appunti il risultato numerico è $C_{\text{eq}} = 3{,}5\ \mu\mathrm F$, ma i valori di $C_1$, $C_2$ e $C_3$ non sono riportati, quindi non posso verificarlo. Il controllo dimensionale della formula è corretto: $\mathrm F\cdot\mathrm F/\mathrm F = \mathrm F$.

### Esercizio 2 — Potenziale di un quarto di disco

> [!example] Testo (dagli appunti)
> Un disco di raggio $R = 64\ \mathrm{cm}$ è carico uniformemente con densità $\sigma = 7{,}73\ \mathrm{fC/m^2}$, dove $1\ \mathrm{fC} = 10^{-15}\ \mathrm C$. Del disco resta un solo quadrante. Calcolare il potenziale nel punto $P$ sull'asse, a distanza $D = 25{,}9\ \mathrm{cm}$ dal centro.
>
> Il potenziale è uno scalare e gode della sovrapposizione: il disco intero equivale alla somma dei quattro quadranti, $V_{\text{disco}} = V_1 + V_2 + V_3 + V_4$. Visto da un punto dell'asse, ogni quadrante ha la stessa distribuzione di distanze da $P$, quindi i quattro contributi sono uguali: $V_{\text{disco}} = 4V_1$. Con il potenziale del disco ricavato sopra:
> $$
> V_1 = \frac{V_{\text{disco}}}{4} = \frac{\sigma}{8\varepsilon_0}\left(\sqrt{D^2 + R^2} - D\right)
> = \frac{7{,}73\cdot10^{-15}}{8\,(8{,}85\cdot10^{-12})}\left(0{,}690 - 0{,}259\right)\ \mathrm V \simeq 4{,}71\cdot10^{-5}\ \mathrm V .
> $$

![[F2-L08-quarto-disco.svg]]

Questo esercizio mostra il vantaggio del potenziale. Il **campo** di un quarto di disco non è un quarto del campo del disco intero. Con un quadrante solo, le componenti trasversali non si cancellano più, e il campo non è più diretto lungo l'asse. Il potenziale, essendo uno scalare, si divide semplicemente per quattro.

> [!warning] Unità negli appunti
> Negli appunti la distanza è scritta "$D = 25{,}9$" senza unità. Il risultato $4{,}71\cdot10^{-5}\ \mathrm V$ torna con $D = 25{,}9\ \mathrm{cm}$, come $R$.

### Esercizio 3 — Una particella tra due armature

> [!example] Testo (dagli appunti)
> Due armature parallele, a distanza $d = 2\ \mathrm{mm}$, si trovano ai potenziali $V_1 = -70\ \mathrm V$ e $V_2 = -50\ \mathrm V$. Una particella parte dall'armatura 1 verso l'armatura 2 con velocità $v_0 = 90\ \mathrm{km/s}$ e **rallenta**. (a) È un elettrone o un protone? (b) Con quale velocità arriva all'armatura 2?
>
> **(a)** Il potenziale cresce da 1 a 2: $\Delta V = V_2 - V_1 = +20\ \mathrm V > 0$. Da $\Delta V = -\int\vec E\cdot d\vec s > 0$ segue $\vec E\cdot d\vec s < 0$: il campo è opposto allo spostamento, cioè punta dall'armatura 2 verso l'armatura 1, dal potenziale più alto a quello più basso. Se la particella rallenta, la forza è opposta al moto, quindi concorde con il campo. Poiché $\vec F = q\vec E$, la carica è positiva: è un **protone**.
>
> **(b)** Il campo è conservativo, quindi si conserva l'energia meccanica, cinetica più potenziale, con $U = qV$:
> $$
> \tfrac12 m_p v_0^2 + qV_1 = \tfrac12 m_p v_f^2 + qV_2
> \quad\Longrightarrow\quad
> v_f = \sqrt{v_0^2 + \frac{2q}{m_p}\left(V_1 - V_2\right)} .
> $$
> Con $q = e = 1{,}60\cdot10^{-19}\ \mathrm C$, $m_p = 1{,}67\cdot10^{-27}\ \mathrm{kg}$ e $V_1 - V_2 = -20\ \mathrm V$:
> $$
> v_f = \sqrt{(9{,}0\cdot10^4)^2 - \frac{2\,(1{,}60\cdot10^{-19})(20)}{1{,}67\cdot10^{-27}}}\ \mathrm{m/s} \simeq 6{,}53\cdot10^{4}\ \mathrm{m/s}.
> $$
> La distanza $d$ non serve: conta solo la differenza di potenziale.

![[F2-L08-particella-armature.svg]]

> [!tip] Il controllo con l'elettrone #approfondimento
> Con un elettrone la forza sarebbe opposta al campo, quindi concorde con il moto, e la particella accelererebbe: $v_f = \sqrt{v_0^2 + 2e\cdot20/m_e} \simeq 2{,}65\cdot10^6\ \mathrm{m/s}$. È in contraddizione con il testo, e conferma che la particella è un protone.

> [!warning] Sezione ricostruita — fine
