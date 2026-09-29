
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
    
      
    

> [!important] Ruote Sterzanti (Ackermann vs Differential) 
> Per eliminare lo strisciamento laterale ("scrub") inevitabilmente indotto dalle ruote caster puramente passive durante le inversioni, alcuni robot adottano una ruota anteriore comandata con un proprio angolo di sterzo $\delta$. La geometria muta radicalmente passando al **Modello Car-Like** (bicicletta equivalente). La cinematica viene ora regolata dal passo $L$ (distanza asse posteriore-anteriore). Il veicolo perde la capacità di compiere pivot sul posto: il limite meccanico allo sterzo massimo $\delta_{max}$ impone l'esistenza di un raggio di curvatura minimo invalicabile $R_{min} = L / \tan(\delta_{max})$.
> 
>   

