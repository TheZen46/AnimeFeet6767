

```
---
lezione: 1
data: 2026-09-24
argomenti: [Storia della robotica, Livelli di autonomia, Architetture di controllo, Cinematica, Guida differenziale, Odometria]
---
```

# Introduzione alla Robotica e Autonomia

Il corso di Robotica 2 si articola su due filoni complementari, gestiti da due docenti con formazioni differenti. Da un lato, l'ambito legato alla teoria dei controlli, che si occupa della realizzazione precisa del movimento e della stima dello stato, gestito dal professor Wanderlingh. Dall'altro, l'ambito informatico e algoritmico, incentrato sul comportamento autonomo, la percezione e la presa di decisioni, trattato in questa sezione.

  

L'obiettivo fondamentale della robotica mobile moderna è il raggiungimento dell'**autonomia**. Un robot si definisce autonomo nella misura in cui è capace di decidere da solo quali azioni intraprendere per raggiungere un obiettivo assegnato, muovendosi all'interno di un ambiente che non conosce completamente a priori. A differenza della robotica industriale classica, non vi è una traiettoria prefissata da un operatore: è il robot stesso a dover calcolare il "come" muoversi, affrontando l'incertezza del mondo reale e adattando i propri piani dinamicamente (ad esempio, aggirando una porta trovata improvvisamente chiusa).

  

Per modellare e comprendere questa autonomia, la storia della robotica può essere letta attraverso l'evoluzione del ciclo fondamentale che ogni automa deve compiere: il ciclo di **Percezione, Stima dello Stato, Decisione e Controllo**.

  

- **Percezione (Sense):** L'acquisizione di informazioni sull'ambiente tramite i sensori (es. telecamere, lidar, sonar) per capire "cosa c'è e dove".
    
      
    
- **Stima dello Stato (Model/Stima):** La capacità di rispondere alle domande "dove sono io?" (autolocalizzazione) e "com'è fatto il mondo?" (mappatura).
    
      
    
- **Decisione (Plan):** Il processo logico che, noto l'obiettivo e lo stato, determina quale sequenza di azioni conviene eseguire (pianificazione).
    
      
    
- **Controllo (Act):** La traduzione della decisione in segnali fisici da inviare agli attuatori (es. motori delle ruote) per realizzare materialmente il movimento.
    
      
    

## La scala dell'autonomia (Da L0 a L5)

La complessità delle macchine può essere classificata in livelli di autonomia crescenti. Questa suddivisione storica e funzionale aiuta a inquadrare i colli di bottiglia tecnologici affrontati nei decenni:

  

- **Livello L0 (Teleoperazione):** L'anello di controllo è chiuso interamente dall'essere umano. Un esempio classico sono i bracci manipolatori teleoperati degli anni '50, dove il robot si limita a eseguire ciecamente i comandi manuali.
    
      
    
- **Livello L1 (Automazione senza percezione):** Il robot ripete in modo estremamente preciso una sequenza fissa memorizzata. È il caso di _Unimate_ (1961), utilizzato nell'industria automobilistica, che operava senza alcun sensore ambientale, pretendendo che il mondo fosse strutturato perfettamente su di esso.
    
      
    
- **Livello L2 (Sistemi reattivi):** Il robot reagisce agli stimoli sensoriali ma non costruisce alcuna mappa o rappresentazione interna del mondo. Esempi storici includono le tartarughe di Grey Walter (1948) o i veicoli teorizzati da Valentino Braitenberg, in cui un comportamento apparentemente "intelligente" (come l'inseguimento di una sorgente luminosa) emerge dal semplice cablaggio fisico tra sensori e attuatori, senza l'uso di calcolatori. Anche il primo aspirapolvere _Roomba_ (2002) operava a questo livello, coprendo lo spazio in modo puramente stocastico.
    
      
    
- **Livello L3 (Pianificazione in mondo noto):** Il robot possiede o costruisce un modello simbolico dell'ambiente (spesso un "mondo giocattolo" semplificato) e pianifica su di esso. Il capostipite è _Shakey_ (1969), il primo a integrare percezione, ragionamento e azione, per il quale furono inventati l'algoritmo di ricerca su grafi A* e il linguaggio STRIPS. Il limite era la lentezza: il mondo doveva restare statico per permettere al robot di "pensare".
    
      
    
- **Livello L4 (Esplorazione e incertezza):** Il robot costruisce la mappa in tempo reale e vi si localizza (problema SLAM) gestendo l'incertezza dei sensori. È l'epoca della robotica probabilistica, con esempi come le guide museali _RHINO_ e _MINERVA_ (1997-1998).
    
      
    
- **Livello L5 (Generalizzazione e modelli generativi):** È la frontiera odierna, in cui il robot riceve istruzioni in linguaggio naturale (es. "riordina la cucina") e utilizza Modelli Visione-Linguaggio-Azione (VLA) per interpretare la semantica della scena e generare autonomamente le leggi di controllo per corpi anche mai visti in fase di addestramento.
    
      
    

## Paradigmi e Architetture Software

Il problema di come far coesistere la necessità di reagire istantaneamente agli imprevisti con la capacità di pianificare a lungo termine ha portato allo sviluppo di diverse architetture software.

  

Inizialmente, il paradigma dominante era il **Sense-Plan-Act (Deliberativo)**, introdotto con Shakey. Questo approccio richiedeva che il robot completasse ciclicamente l'intero processo: acquisire dati, ricostruire la mappa, pianificare una rotta ed eseguire il movimento. Tuttavia, per via delle limitazioni computazionali, tale processo richiedeva tempi biblici (lo _Stanford Cart_ nel 1979 impiegava cinque ore per attraversare una stanza), rendendolo inadatto a mondi dinamici.

  

Come reazione a questa inefficienza, negli anni '80 nacque il paradigma **Reattivo (o Subsumption)**. Ricercatori come Rodney Brooks proposero di eliminare del tutto il modello centrale. L'architettura _Subsumption_ si basa su strati di comportamenti paralleli (es. "vaga", "evita ostacoli"), ciascuno dei quali collega direttamente i sensori ai motori. Se il robot incontra un ostacolo, il livello inferiore (reattivo) prende istantaneamente la precedenza (sopprime) sul livello superiore, garantendo tempi di reazione nell'ordine dei millisecondi. Parallelamente, Oussama Khatib introdusse i **Campi di Potenziale Artificiale**, in cui l'obiettivo agisce come una carica attrattiva e gli ostacoli (rilevati istantaneamente tramite sensori a ultrasuoni) come cariche repulsive. Il robot si muove semplicemente seguendo il vettore somma delle forze.

  

> [!important] Il fallimento dei modelli puri e la sintesi ibrida Sebbene velocissimo, un sistema puramente reattivo soffre di miopia: i campi di potenziale si incastrano nei minimi locali e l'architettura _Subsumption_ non permette di pianificare compiti complessi a lungo termine. La soluzione adottata universalmente oggi è l'**Architettura Ibrida a tre livelli**, che separa il problema su scale temporali differenti.
> 
>   



```
graph TD
    subgraph Architettura_Ibrida
        A[Livello Deliberativo: Pianificazione globale, Mappatura <br> Tempo: Secondi/Minuti]
        B[Livello Esecutivo: Sequenziazione e gestione eventi <br> Tempo: ~100 ms]
        C[Livello Reattivo: Controllo motori e anti-collisione istantanea <br> Tempo: Millisecondi]
    end
    
    Sensori --> C
    Sensori --> B
    Sensori --> A
    
    A -- Piani --> B
    B -- Comandi Locali --> C
    C -- Segnali --> Motori
    
    Motori --> Mondo
    Mondo --> Sensori
```

## La svolta probabilistica: SLAM e Monte Carlo

A cavallo tra gli anni '90 e 2000, ci si rese conto che i sensori a basso costo (come i sonar a ultrasuoni, capaci di restituire distanze ma soggetti a coni ampi di incertezza) necessitavano di una trattazione statistica.

  

Invece di chiedersi "c'è un ostacolo qui?", si iniziò a dividere lo spazio in griglie di occupazione, assegnando a ogni cella una probabilità di essere occupata, aggiornata ricorsivamente a ogni nuova lettura. Questa intuizione portò alla rivoluzione della **Localizzazione Monte Carlo (MCL)**: poiché l'odometria accumula errori, il robot non è mai certo della propria posa. L'algoritmo MCL rappresenta le possibili pose del robot come un insieme di particelle (campioni pesati) distribuite nello spazio. Mano a mano che il robot si muove e confronta le letture dei sensori (es. la distanza da un muro) con la mappa nota, la probabilità delle particelle incompatibili scende, facendole sparire, mentre le particelle compatibili si addensano attorno alla posizione reale.

  

Quando anche la mappa è ignota, il problema diventa **SLAM (Simultaneous Localization and Mapping)**: il robot deve stimare la propria posizione rispetto a una mappa che sta costruendo in quel preciso istante, un traguardo che ha finalmente abilitato l'autonomia in ambienti pubblici non modificati.

  

> [!tip] Approfondimento #approfondimento Lo sviluppo dello SLAM e del filtro a particelle ha sbloccato la robotica negli anni 2000, culminando poi nella necessità di standardizzare il software. Nel 2010 nasce **ROS (Robot Operating System)**, un framework basato su nodi (processi indipendenti) che comunicano tramite messaggi. Questo ecosistema open-source ha permesso ai ricercatori di smettere di "reinventare la ruota" (driver, matrici matematiche) per focalizzarsi sull'algoritmica avanzata, rendendo possibile l'integrazione di sensori ad alta densità come i LIDAR (sebbene accecati dai vetri) e l'evoluzione della percezione profonda (Deep Learning, es. algoritmo YOLO per il rilevamento real-time).
> 
>   

# Cinematica e Odometria della Guida Differenziale

Passando dalla teoria generale all'implementazione fisica, il primo passo è comprendere come si modella matematicamente il movimento di una piattaforma robotica. Il modello più comune e studiato, in quanto semplice ma emblematico del problema dell'autonomia, è il **robot a guida differenziale**.

  

## Geometria e Modello di Stato

Il veicolo è costituito da due ruote motrici indipendenti disposte sullo stesso asse trasversale e da una (o più) ruote folli (caster) che garantiscono stabilità meccanica (almeno tre punti d'appoggio per non cadere) senza vincolare la traiettoria, adattandosi passivamente al moto generato dalle ruote attive.

  

Fissiamo un sistema di riferimento globale (Mondo, $x_W, y_W$) e un sistema di riferimento solidale al robot (Corpo, $x_B, y_B$). Per comodità geometrica, l'origine del sistema Corpo (il punto $P$) si posiziona esattamente al centro dell'assale delle ruote motrici, con l'asse $x_B$ orientato in avanti (direzione longitudinale) e l'asse $y_B$ verso la ruota sinistra (direzione laterale).

  

La **posa** (stato) del robot nel piano si descrive con tre gradi di libertà, riuniti nel vettore configurazione $q$:

  

$$q = \begin{bmatrix} x \\ y \\ \theta \end{bmatrix}$$

Dove $x$ e $y$ sono le coordinate del punto $P$ nel riferimento Mondo, e $\theta$ è l'orientamento del robot (l'angolo tra $x_B$ e $x_W$).

  

I parametri costruttivi della macchina sono esclusivamente geometrici:

  

- $r_L, r_R$: raggi efficaci delle ruote sinistra e destra.
    
      
    
- $b$: interasse trasversale efficace (la distanza tra i punti di contatto delle due ruote col suolo).
    
      
    

> [!important] Il concetto di "Raggio Efficace" Nella pratica, non si usano quasi mai i raggi nominali da libretto di istruzioni. Le ruote reali possono essere leggermente sgonfie, usurate, o gravate dal carico in modo asimmetrico. Se $r_L \neq r_R$, imponendo ai motori la stessa velocità angolare, il robot non andrà dritto ma devierà costantemente (bias laterale). Usare i parametri "efficaci" (calibrati) è essenziale per limitare gli errori sistematici.
> 
>   

Le variabili di controllo (ingressi del sistema) sono le velocità angolari imposte ai motori: $\dot{\varphi}_L$ e $\dot{\varphi}_R$ (in rad/s).

  

## Il Vincolo Non Olonomo

Una ruota ideale sottoposta a puro rotolamento avanza lungo la sua direzione, ma non può assolutamente scivolare o traslare di lato (la componente di velocità lungo il mozzo è nulla). Di conseguenza, l'intero veicolo non può spostarsi lateralmente: il suo twist (vettore velocità) nel sistema Corpo è $\xi = \begin{bmatrix} v & 0 & \omega \end{bmatrix}^\top$, indicando che la velocità lungo l'asse laterale $y_B$ è strettamente uguale a zero.

  

Questo limite fisico prende il nome di **vincolo cinematico non olonomo**. In termini formali, proiettando la condizione $v_{y_B} = 0$ nel sistema di riferimento Mondo, si ottiene l'equazione del vincolo:

  

$$-\dot{x} \sin\theta + \dot{y} \cos\theta = 0$$

> [!example] Implicazione pratica del vincolo olonomo
> 
> Si supponga che il robot sia orientato a $\theta = 45^\circ$. In questo caso, $\sin(45^\circ) = \cos(45^\circ) = \frac{\sqrt{2}}{2}$. Sostituendo nell'equazione del vincolo:
> 
>   
> 
> $$-\dot{x} \left(\frac{\sqrt{2}}{2}\right) + \dot{y} \left(\frac{\sqrt{2}}{2}\right) = 0 \implies \dot{x} = \dot{y}$$
> 
> Questo significa che, affinché il vincolo sia rispettato, il robot _deve_ avere velocità uguali lungo gli assi globali X e Y. A differenza dei veicoli olonomi (es. droni in volo), il robot differenziale non può parcheggiare spostandosi istantaneamente di lato: qualsiasi posa è raggiungibile, ma richiede una composizione di traslazioni e rotazioni nel tempo.
> 
>   

## Cinematica Diretta e Modello di Stato

La **cinematica diretta** risponde alla domanda: "Date le velocità di rotazione dei motori, come si muove il centro del robot?". Le velocità lineari al suolo per ciascuna ruota sono:

  

$$v_L = r_L \dot{\varphi}_L \quad \text{e} \quad v_R = r_R \dot{\varphi}_R$$

Il centro dell'assale avanza con una velocità longitudinale $v$ pari alla media delle velocità delle ruote, mentre la velocità angolare $\omega$ (yaw rate) del corpo nasce dalla loro differenza, normalizzata sull'interasse $b$:

  

$$v = \frac{v_R + v_L}{2}$$

$$\omega = \frac{v_R - v_L}{b}$$

Ruotando questo vettore velocità dal sistema Corpo al sistema Mondo, si ottiene il modello di stato non lineare dell'evoluzione della posa:

  

$$\dot{q} = \begin{bmatrix} \dot{x} \\ \dot{y} \\ \dot{\theta} \end{bmatrix} = \begin{bmatrix} v \cos\theta \\ v \sin\theta \\ \omega \end{bmatrix}$$

Questa rappresentazione matematica evidenzia la difficoltà nell'integrazione: l'evoluzione di $x$ e $y$ dipende non linearmente da $\theta$ (tramite seno e coseno), e $\theta$ varia a sua volta nel tempo a causa di $\omega$.

  

> [!warning] Sezione Ricostruita — Inizio
> 
> (La porzione seguente ricostruisce integralmente la trattazione su cinematica inversa, odometria ed errori sistematici presente nelle slide ufficiali del corso, sopperendo alla chiusura anticipata della trascrizione dell'audio della lezione).
> 
>   

## Cinematica Inversa e Regimi di Moto

La **cinematica inversa** si occupa del problema complementare per il controllo: "Data la velocità lineare $v$ e angolare $\omega$ desiderate per il corpo, a quali velocità devo far ruotare i singoli motori?". Invertendo le equazioni dirette otteniamo:

  

$$\dot{\varphi}_L = \frac{v - \frac{b \omega}{2}}{r_L}$$

$$\dot{\varphi}_R = \frac{v + \frac{b \omega}{2}}{r_R}$$

Qualora i valori risultanti superino il limite fisico di saturazione dei motori ($\dot{\varphi}_{max}$), non è sufficiente "tagliare" il valore in eccesso. Bisogna calcolare un fattore di scala $k = \dot{\varphi}_{max} / \dot{\varphi}_{critica}$ e moltiplicare _entrambe_ le ruote per questo fattore: ciò rallenta il robot ma preserva la curvatura della traiettoria impostata, salvando l'ostacolo.

  

A velocità costanti, il robot si muove su un arco di circonferenza ruotando attorno a un unico **Centro Istantaneo di Curvatura (ICC)**. Il raggio $R$ di questo arco è dato dal rapporto tra velocità lineare e angolare (o tra arco percorso e angolo spazzato):

  

$$R = \frac{v}{\omega} = \frac{\Delta s}{\Delta\theta}$$

I principali regimi di moto sono determinati dalla differenza di velocità tra le ruote:

  

- Se $v_R = v_L$, il moto è rettilineo ($\omega = 0, R \to \infty$).
    
      
    
- Se $v_R = -v_L$, il robot ruota sul posto (pivot) senza avanzare ($v = 0, R = 0$).
    
      
    
- Se una ruota è ferma (es. $v_R = 0$), il robot pernotta attorno alla ruota ferma, e l'ICC coincide con essa ($R = b/2$).
    
      
    

## Integrazione Odometrica

L'**odometria** è un processo di inferenza basato su ipotesi (_dead reckoning_), in cui si stima la posa corrente integrando le misure dei conteggi provenienti dagli _encoder_ incrementali montati sulle ruote. La nuova posa dipende totalmente da quella precedente: ogni minimo errore si accumula inesorabilmente nel tempo senza possibilità di essere corretto autonomamente dal sistema.

  

L'acquisizione procede a passi discreti $k$ con frequenza di campionamento $\Delta t$. Per ciascuna ruota $i \in \{L, R\}$ con risoluzione $N$ (impulsi giro), data la lettura grezza del contatore $c_k$, si calcola l'incremento di conteggi $\Delta c = c_k - c_{k-1}$ compensando digitalmente i problemi di _wrap-around_ numerico (overflow del registro del contatore). L'arco al suolo vale:

  

$$\Delta s_i = \frac{2\pi \cdot r_i}{N} \Delta c_i$$

L'avanzamento $\Delta s$ e la variazione di orientamento $\Delta\theta$ del corpo nell'intervallo sono:

  

$$\Delta s = \frac{\Delta s_R + \Delta s_L}{2} \quad \text{e} \quad \Delta\theta = \frac{\Delta s_R - \Delta s_L}{b}$$

A questo punto si deve aggiornare il vettore posa $q$. Si presentano due opzioni numeriche standard, più una strategia geometricamente esatta.

  

### Approssimazioni di Eulero e Punto Medio

1. **Eulero Esplicito:** Assume che la direzione $\theta$ resti costante e pari a quella iniziale ($\theta_k$) per tutto il campionamento.
    
      
    
    $$x_{k+1} = x_k + \Delta s \cos\theta_k \quad;\quad y_{k+1} = y_k + \Delta s \sin\theta_k$$
    
2. **Metodo del Punto Medio (Runge-Kutta 2):** Usa la direzione media del passo, minimizzando grandemente l'errore a parità di sforzo computazionale.
    
      
    
    $$x_{k+1} = x_k + \Delta s \cos\left(\theta_k + \frac{\Delta\theta}{2}\right) \quad;\quad y_{k+1} = y_k + \Delta s \sin\left(\theta_k + \frac{\Delta\theta}{2}\right)$$
    
    In entrambi i casi, l'angolo si aggiorna in coda e va sempre normalizzato nel range $[-\pi, \pi]$ (o $[0, 2\pi)$): $\theta_{k+1} = \text{wrap}(\theta_k + \Delta\theta)$.
    
      
    

### L'Integrazione Esatta

Se si assume che nei millisecondi del campione le velocità $v$ e $\omega$ siano costanti, il robot si è mosso su un arco perfetto. Il sistema non può utilizzare indiscriminatamente la formula dell'arco (che richiede la divisione per $\Delta\theta$ per trovare $R$) perché esploderebbe a infinito sui tratti rettilinei ($\Delta\theta \to 0$). Di conseguenza, il codice software reale discrimina il caso in base a una soglia arbitraria $\epsilon$:

  

**CASO 1: Moto Rettilineo ($\vert{}\Delta\theta\vert{} < \epsilon$)** Si applica l'aggiornamento come in Eulero, procedendo dritti.

  

**CASO 2: Moto su Arco ($\vert{}\Delta\theta\vert{} \ge \epsilon$)** Si calcola il raggio $R = \Delta s / \Delta\theta$. Le coordinate si aggiornano derivando la posizione del Centro Istantaneo di Curvatura, che per ipotesi resta fisso durante il campione, elidendolo con semplici passaggi algebrici:

  

$$x_{k+1} = x_k + R [\sin(\theta_k + \Delta\theta) - \sin\theta_k]$$

$$y_{k+1} = y_k - R [\cos(\theta_k + \Delta\theta) - \cos\theta_k]$$

$$\theta_{k+1} = \text{wrap}(\theta_k + \Delta\theta)$$

## Errori Odometrici e Modelli Alternativi

La deriva dell'odometria è alimentata da due categorie di disturbi, le cui tracce (_firme_) si manifestano in modo peculiare nella geometria del percorso:

  

1. **Errori Sistematici:** Sono legati alla cinematica interna e costanti. I più incidenti sono l'asimmetria dei raggi ($r_L \neq r_R$, che introduce una curvatura spuria costante traducendosi in un drift laterale lineare con l'avanzamento) e l'incertezza sull'interasse $b$ (che causa una fatale sovra/sotto-stima dell'angolo durante ogni rotazione). Questi errori sono identificabili a posteriori e cancellabili tramite calibrazione software. La prova principe in robotica è la prova **UMBmark** (Borenstein e Feng): eseguendo ripetutamente quadrati in senso orario e antiorario e misurando l'errore di chiusura (il buco rispetto al ritorno al punto base) si riescono a isolare matematicamente l'influenza dei raggi da quella dell'interasse.
    
      
    
2. **Errori Non Sistematici:** Sono legati all'interazione terreno-ruota (es. urti, buche, tappeti, o il puro slittamento durante le svolte critiche sul posto, note come pivot). Questi generano variazioni non predicibili (dispersione probabilistica random-walk) che nessun setup cinematico può correggere da solo.
    
      
    

> [!important] Ruote Sterzanti (Ackermann vs Differential) Per eliminare lo strisciamento laterale ("scrub") inevitabilmente indotto dalle ruote caster puramente passive durante le inversioni, alcuni robot adottano una ruota anteriore comandata con un proprio angolo di sterzo $\delta$. La geometria muta radicalmente passando al **Modello Car-Like** (bicicletta equivalente). La cinematica viene ora regolata dal passo $L$ (distanza asse posteriore-anteriore). Il veicolo perde la capacità di compiere pivot sul posto: il limite meccanico allo sterzo massimo $\delta_{max}$ impone l'esistenza di un raggio di curvatura minimo invalicabile $R_{min} = L / \tan(\delta_{max})$.
> 
>   

