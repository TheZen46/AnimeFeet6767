

```
---
lezione: 1 e 2
data: 2026-09-24
argomenti: [Sistemi, Sistemi Dinamici, Funzioni Generalizzate, Delta di Dirac, Trasformata di Laplace]
---
```

# Introduzione alla Teoria dei Sistemi e Modelli Matematici

Lo studio della teoria dei sistemi si fonda sull'analisi rigorosa delle relazioni che intercorrono tra le sollecitazioni applicate a un'entità fisica o astratta e le reazioni che tale entità produce. Un sistema può essere concettualizzato, da un punto di vista formale e grafico, come una "scatola nera" (o "scatoletta") all'interno della quale risiede una logica operativa, caratterizzata da variabili in ingresso, definite come cause, e variabili in uscita, definite come effetti.

  

L'obiettivo fondamentale dell'ingegneria dei sistemi e del controllo è determinare l'operatore matematico $\mathcal{O}$ che lega la causa $c(t)$ all'effetto $e(t)$.

  


``` mermaid
graph LR
    C[Causa c_e] -->|Input| S[SISTEMA - Operatore O]
    S -->|Output| E[Effetto e]
    CI[Causa interna c_i] -.->|Stato Iniziale| S
```

## Classificazione Fondamentale dei Sistemi

La natura dell'operatore $\mathcal{O}$ definisce la tipologia del sistema in esame. La distinzione primaria riguarda la dipendenza dell'effetto dalla storia passata delle sollecitazioni applicate.

  

### Sistemi Algebrici

Un sistema viene definito algebrico quando l'effetto misurato in un determinato istante di tempo $t$ dipende in modo esclusivo e diretto dalla causa applicata nel medesimo e identico istante $t$. Questi sistemi sono privi di memoria, non possiedono una "storia passata" che influenzi l'uscita attuale. Un esempio emblematico citato in letteratura è la calcolatrice: digitando un'operazione come "3 + 5" e premendo il tasto uguale, il risultato "8" dipende unicamente dai numeri appena immessi, indipendentemente dai miliardi di calcoli che il processore potrebbe aver eseguito negli anni precedenti. A causa di questa risposta istantanea e della mancanza di dinamica temporale, i sistemi algebrici presentano un interesse teorico quasi nullo nell'ambito del controllo.

  

### Sistemi Dinamici

I sistemi di interesse ingegneristico sono i sistemi dinamici, nei quali l'effetto a un dato istante $t$ non è funzione della sola causa applicata in $t$, ma dipende dall'intera evoluzione temporale del sistema, ovvero dalla sua storia passata. Nei sistemi dinamici, le cause si diramano in due categorie distinte:

  

1. **Cause esterne $c_e(\tau)$:** Le sollecitazioni forzanti applicate al sistema dall'ambiente circostante nell'intervallo di osservazione $t_0 \le \tau \le t$.
    
      
    
2. **Cause interne $c_i(t_0)$:** Il riassunto di tutta la storia passata del sistema da $t = -\infty$ fino all'istante iniziale di osservazione $t_0$. Matematicamente, queste si traducono nelle "condizioni iniziali" del sistema.
    
      
    

L'effetto finale è dunque descrivibile dalla relazione formale $e(t) = \mathcal{O}(c_i(t_0), c_e(\tau))$.

  

> [!example] Il Modello Idraulico del Serbatoio (Sistema Dinamico) Per visualizzare concretamente un sistema dinamico, si analizzi un serbatoio cilindrico (una vasca o una pentola) a tenuta stagna e con sezione costante unitaria.
> 
>   
> 
> - L'**effetto** in uscita dal sistema è l'altezza del livello dell'acqua all'istante $t$, indicata come $h(t)$. Data la sezione unitaria, l'altezza corrisponde numericamente al volume in litri.
>     
>       
>     
> - La **causa esterna** in ingresso è la portata dell'acqua versata da un rubinetto, ovvero la velocità di innalzamento del livello, indicata con $u(t)$.
>     
>       
>     
> 
> La variazione istantanea del volume d'acqua, cioè la derivata temporale $\dot{h}(t)$, è direttamente pari alla portata in ingresso: $\dot{h}(\tau) = u(\tau)$. Per conoscere il livello dell'acqua a un istante $t$ successivo all'istante iniziale $0$, è necessario integrare l'equazione differenziale:
> 
>   
> 
> $$\int_{0}^{t} \dot{h}(\tau) d\tau = \int_{0}^{t} u(\tau) d\tau$$
> 
>   
> 
> Dal teorema fondamentale del calcolo integrale si ricava:
> 
>   
> 
> $$h(t) - h(0) = \int_{0}^{t} u(\tau) d\tau \implies h(t) = h(0) + \int_{0}^{t} u(\tau) d\tau$$
> 
>   
> 
> Questa equazione esprime perfettamente la natura del sistema dinamico: il volume d'acqua $h(t)$ è la somma esatta della **causa interna** $h(0)$ (l'acqua già presente nel serbatoio all'inizio dell'osservazione, determinata da eventi precedenti non modellati) e del contributo delle **cause esterne** (l'integrale della portata versata durante l'intervallo di osservazione). Se il serbatoio contenesse già 5 litri iniziali e il rubinetto versasse 2 litri al secondo per 5 secondi, il volume finale sarebbe di 15 litri.
> 
>   

## Proprietà Strutturali dei Sistemi

La trattazione formale della teoria dei sistemi si concentra su modelli che rispettano tre proprietà restrittive ma fondamentali, necessarie per garantire la trattabilità matematica attraverso le trasformate integrali.

  

### 1. Linearità

Un sistema è definito lineare se e solo se per esso vale rigorosamente il Principio di Sovrapposizione degli Effetti. Se un sistema è soggetto a una pluralità di cause (siano esse plurime cause interne o plurime cause esterne), l'effetto complessivo totale è calcolabile come la somma algebrica dei singoli effetti che ciascuna causa produrrebbe qualora agisse da sola sul sistema. Riprendendo il modello del serbatoio, la scomposizione $h(t) = h(0) + \int u(\tau) d\tau$ dimostra la linearità: l'effetto dovuto alla condizione iniziale $h(0)$ si somma algebricamente all'effetto dovuto all'ingresso $\int u(\tau) d\tau$. Se vi fossero molteplici rubinetti (es. 122 cause esterne), la linearità dell'operatore di integrazione garantisce che l'integrale della somma delle portate equivale alla somma degli integrali delle singole portate.

  

### 2. Tempo-Invarianza (o Stazionarietà)

Un sistema è tempo-invariante se l'effetto finale prodotto non dipende dalla collocazione assoluta dell'esperimento sull'asse del tempo. Se un esperimento condotto oggi, con specifiche condizioni iniziali e un preciso andamento dell'ingresso, produce un certo effetto, lo stesso identico esperimento replicato in un futuro arbitrario produrrà lo stesso identico effetto, puramente traslato in avanti della medesima quantità di tempo.

  

### 3. Tempo Continuo

I sistemi a tempo continuo sono quelli le cui relazioni causa-effetto sono modellate e descrivibili da equazioni differenziali. Il tempo fluisce in modo continuo, in netto contrasto con i sistemi a tempo discreto (come i moderni elaboratori digitali o automi a stati finiti), le cui transizioni di stato avvengono istantaneamente in corrispondenza di precisi colpi di clock o eventi sincroni.

  

> [!tip] Approfondimento: Linearizzazione di Sistemi Non Lineari #approfondimento Sebbene l'intero impianto teorico del corso si basi sull'assunto di linearità, la quasi totalità dei sistemi fisici reali è intrinsecamente non lineare. La presenza di attriti, saturazioni, o relazioni trigonometriche (es. funzioni seno o coseno nelle equazioni differenziali del moto) infrange il principio di sovrapposizione. Tuttavia, i sistemi fisici possono essere studiati localmente mediante approssimazioni lineari attorno a specifici punti di equilibrio. Un esempio classico è il pendolo semplice: per piccole oscillazioni attorno alla posizione di riposo (testa in giù), la funzione $\sin(\theta)$ è approssimabile con l'angolo $\theta$ stesso, rendendo l'equazione differenziale temporaneamente lineare. Un esempio applicativo avanzato di questo concetto è il _Segway_. Esso è assimilabile a un pendolo inverso (testa in su), un sistema non lineare e intrinsecamente instabile (un minimo disturbo lo farebbe cadere). Il sistema di controllo elettronico a bordo retroaziona la posizione della base spostandola in avanti o all'indietro per controbilanciare la caduta del guidatore. Pur essendo una dinamica complessa e non lineare, la progettazione delle leggi di controllo si basa primariamente su astrazioni e tecniche riciclate dalla teoria dei sistemi lineari.
> 
>   

# Funzioni Generalizzate (Distribuzioni)

Per poter descrivere fenomeni fisici ideali (come sollecitazioni impulsive di durata nulla ma energia finita) e per manipolare derivate di segnali discontinui, la trattazione matematica standard basata su funzioni analitiche di classe $C^\infty$ risulta insufficiente. Si introducono perciò le Funzioni Generalizzate, o Distribuzioni.

  

## L'Impulso di Dirac (Ordine 0)

La funzione capostipite di questa famiglia è l'Impulso di Dirac, indicato con $\delta(t)$, detto anche impulso di ordine 0. A rigore matematico non è una funzione puntuale, ma un funzionale definito dalle sue proprietà integrali.

  

L'origine concettuale della $\delta(t)$ deriva da un processo di passaggio al limite. Si definisca un impulso rettangolare $p_T(t)$, centrato nell'origine, di base temporale $2T$ e altezza $\frac{1}{2T}$.

  

$$p_T(t) = \begin{cases} \frac{1}{2T} & t \in (-T, T) \\ 0 & t \in (-\infty, -T] \cup [T, +\infty) \end{cases}$$

  

L'area di questo rettangolo è strettamente unitaria per costruzione (base $\times$ altezza = $2T \cdot \frac{1}{2T} = 1$). Calcolando il limite per $T \to 0$, la base si restringe a un punto e l'altezza tende all'infinito, ma l'integrale complessivo (l'area) si conserva inalterato e pari a 1. Si definisce quindi:

  

$$\lim_{T \to 0} p_T(t) = \delta(t)$$

  

Le proprietà definitorie fondamentali della Delta di Dirac sono:

  

1. **Concentrazione Puntuale:** $\int_{-\infty}^{t} \delta(\tau) d\tau = 0 \quad \forall t < 0$ e $\int_{t}^{+\infty} \delta(\tau) d\tau = 0 \quad \forall t > 0$. La funzione è rigorosamente nulla in ogni punto dell'asse reale ad eccezione dell'origine. Essa esiste esclusivamente laddove il suo argomento è nullo.
    
      
    
2. **Area Unitaria:** $\int_{0^-}^{0^+} \delta(\tau) d\tau = 1$. L'intero "peso" della funzione è racchiuso nell'istante di discontinuità.
    
      
    
3. **Coefficiente di Area:** Un'espressione del tipo $A\delta(t)$ indica un impulso la cui area è pari ad $A$. Graficamente viene rappresentata come una freccia posizionata nell'origine con lunghezza proporzionale ad $A$; se $A$ è negativo, la freccia è orientata verso il basso (simulando il limite di un triangolo rovesciato).
    
      
    

### Proprietà di Campionamento (Sifting Property)

La peculiarità più rilevante dell'impulso di ordine 0 è la sua capacità di "campionare" il valore di altre funzioni. Data una funzione $f(t)$ continua all'infinito e una delta traslata in un istante $T$, il loro prodotto è non nullo solo in $t=T$. Pertanto:

  

$$f(t)\delta(t-T) = \begin{cases} f(T)\delta(t-T) & \text{se } f(T) \ne 0 \\ 0 & \text{se } f(T) = 0 \end{cases}$$

  

Integrando questo prodotto su tutto l'asse reale, la delta "estrae" e restituisce unicamente il valore numerico che la funzione assume nel punto $T$ in cui l'impulso è centrato:

  

$$\int_{-\infty}^{+\infty} f(\tau)\delta(\tau-T) d\tau = f(T)$$

  

## Derivate e Integrali delle Funzioni Generalizzate

L'insieme delle funzioni generalizzate è generato a partire dalla $\delta(t)$ attraverso iterazioni di calcolo differenziale o integrale. Per convenzione, derivare un impulso ne incrementa l'ordine di 1, mentre integrarlo ne decrementa l'ordine di 1.

  

### Impulsi di Ordine Positivo (Derivate)

Derivando l'impulso di ordine 0 si ottiene il **doppietto** (impulso di ordine 1), indicato come $\dot{\delta}(t)$. Graficamente, esso deriva dal limite della derivata di un impulso triangolare che si stringe: produce un picco positivo infinito seguito immediatamente da un picco negativo infinito. Iterando, $\ddot{\delta}(t)$ è l'impulso di ordine 2, e così via. Tutti gli impulsi di ordine $\ge 0$ sono graficamente indefiniti e si manifestano come singolarità concentrate nel punto in cui l'argomento si annulla.

  

### Impulsi di Ordine Negativo (Integrali)

L'integrazione, al contrario, trasforma singolarità impulsive in funzioni regolari e definite a tratti, annullandole per tempi precedenti l'attivazione.

  

1. **Gradino Unitario $1(t)$ (Impulso di ordine -1):** Rappresenta l'integrale della delta. Visto che la delta concentra area unitaria in $t=0$, il suo integrale da $-\infty$ a $t$ "accumula" questo valore 1 appena si attraversa l'origine.
    
      
    
    $$\int_{-\infty}^{t} \delta(\tau) d\tau = \begin{cases} 0 & t < 0 \\ 1 & t \ge 0 \end{cases} \equiv 1(t)$$
    
      
    
    Il gradino unitario, pur rappresentando un salto ideale non realizzabile fisicamente (senza pendenza infinita), è cruciale come elemento interruttore.
    
      
    
2. **Rampa Unitaria $t \cdot 1(t)$ (Impulso di ordine -2):** Si ottiene integrando il gradino unitario.
    
      
    
    $$\int_{-\infty}^{t} 1(\tau) d\tau = \begin{cases} 0 & t < 0 \\ t & t \ge 0 \end{cases} \equiv t \cdot 1(t)$$
    
      
    
    La rampa è una funzione continua (di classe $C^0$) ma non derivabile nell'origine, in quanto il suo coefficiente angolare varia istantaneamente da 0 a 1. Ulteriori integrazioni (impulsi di ordine -3, -4) generano potenze del tempo sempre più regolari (es. parabole $\frac{t^2}{2}1(t)$, cubiche, ecc.), incrementando la continuità delle derivate.
    
      
    


``` 
type: line
labels: [-1, 0, 1, 2, 3, 4]
series:
  - title: 1(t) Gradino
    data: [0, 0, 1, 1, 1, 1]
  - title: t*1(t) Rampa
    data: [0, 0, 1, 2, 3, 4]
```

## Calcolo Differenziale con Funzioni Discontinue

L'inclusione delle distribuzioni permette di estendere le regole del calcolo analitico a funzioni discontinue a salti, senza violare le regole classiche dell'analisi.

  

La regola di derivazione del prodotto continua a valere:

  

$$\frac{d}{dt}(fg) = \dot{f}g + f\dot{g}$$

  

Questa regola resta valida anche se $g$ non è analiticamente derivabile in senso classico (es. se è una distribuzione o un gradino).

  

> [!warning] Sezione ricostruita — inizio (Definizione analitica del salto e della sua derivata)
> 
> _La trascrizione allude all'interpretazione fisica del salto senza sviluppare la formula limite. Integrare il calcolo algebrico rafforza la comprensione formale._
> 
>   
> 
> Se una generica funzione presenta una discontinuità "a gradino" (salto) in un istante $t=T$, passando repentinamente da un valore $f(T^-)$ a un valore $f(T^+)$, la sua derivata generalizzata genera, in quel punto, un impulso di Dirac la cui area è quantificata dall'ampiezza del salto stesso.
> 
>   
> 
> $$\text{Ampiezza Salto} = f(T^+) - f(T^-)$$
> 
> In tal caso, la derivata conterrà il termine $[f(T^+) - f(T^-)]\delta(t-T)$. Similmente, un cambiamento brusco di pendenza (come nel vertice della rampa) genera un salto nella derivata prima, che si manifesta come una discontinuità a gradino. Sezione ricostruita — fine
> 
>   

> [!tip] Creazione di Finestre Temporali (Gate Pulse) tramite Excalidraw È fortemente consigliato creare uno schema a mano libera (tramite Excalidraw) per tracciare il grafico della funzione "Boxcar" o "Gate Pulse". Sottraendo un gradino ritardato da un gradino originario, si ottiene una "finestrella" logica:
> 
>   
> 
> $$1(t-T_1) - 1(t-T_2) = \begin{cases} 1 & T_1 < t < T_2 \\ 0 & \text{altrove} \end{cases}$$
> 
>   
> 
> Qualsiasi funzione $f(t)$ moltiplicata per tale gate pulse verrà isolata ("fotografata") esclusivamente nell'intervallo compreso tra $T_1$ e $T_2$, risultando azzerata prima e dopo. Questo strumento è essenziale per frammentare e ricomporre funzioni definite a tratti.
> 
>   

### Esempio Pratico: Derivazione di un Segnale Finestrato

Sia data una funzione composita formata da un tratto di coseno tra $0$ e $\pi/2$, nessuna emissione tra $\pi/2$ e $\pi$, e una rampa con pendenza che la porta da $0$ in $\pi$ a $1$ in $t=4$.

  

L'espressione matematica, generata sovrapponendo funzioni Boxcar, risulta:

  

$$f(t) = \cos(t)[1(t) - 1(t-\frac{\pi}{2})] + \frac{1}{4-\pi}(t-\pi)[1(t-\pi) - 1(t-4)]$$

  

Calcolandone la derivata generalizzata, applichiamo la regola del prodotto $\frac{d}{dt}(fg) = \dot{f}g + f\dot{g}$ ai vari termini. Ricordiamo che la derivata del gradino $1(t-T)$ è l'impulso $\delta(t-T)$.

  

**Primo pezzo (coseno):**

  

$$\frac{d}{dt} \left\{ \cos(t) [1(t) - 1(t-\frac{\pi}{2})] \right\} = -\sin(t)[1(t) - 1(t-\frac{\pi}{2})] + \cos(t)[\delta(t) - \delta(t-\frac{\pi}{2})]$$

  

Sfruttando la proprietà di campionamento $f(t)\delta(t-T) = f(T)\delta(t-T)$:

  

- $\cos(t)\delta(t) = \cos(0)\delta(t) = 1 \cdot \delta(t)$ (Impulso positivo in 0).
    
      
    
- $-\cos(t)\delta(t-\frac{\pi}{2}) = -\cos(\frac{\pi}{2})\delta(t-\frac{\pi}{2}) = 0 \cdot \delta(t-\frac{\pi}{2}) = 0$. In questo punto la funzione è già a zero, quindi non c'è discontinuità a salto da generare impulsi nella derivata.
    
      
    

**Secondo pezzo (rampa traslata):**

  

$$\frac{d}{dt} \left\{ \frac{1}{4-\pi}(t-\pi)[1(t-\pi) - 1(t-4)] \right\} = \frac{1}{4-\pi}[1(t-\pi) - 1(t-4)] + \frac{1}{4-\pi}(t-\pi)[\delta(t-\pi) - \delta(t-4)]$$

  

Applicando nuovamente il campionamento agli impulsi:

  

- In $t=\pi$, $\frac{1}{4-\pi}(\pi-\pi)\delta(t-\pi) = 0$. La rampa parte da zero, non c'è salto, la funzione è $C^0$.
    
      
    
- In $t=4$, $-\frac{1}{4-\pi}(4-\pi)\delta(t-4) = -1 \cdot \delta(t-4)$. Qui la funzione si interrompe bruscamente troncando il valore 1 a 0, il che corrisponde a una discontinuità a salto negativo generante un impulso rovesciato di area 1.
    
      
    

Ricomponendo il tutto, la derivata esatta risulta:

  

$$\dot{f}(t) = -\sin(t)[1(t) - 1(t-\frac{\pi}{2})] + \delta(t) + \frac{1}{4-\pi}[1(t-\pi) - 1(t-4)] - \delta(t-4)$$

  

Questa forma evidenzia chiaramente sia i contributi analitici (seno e retta costante) sia le discontinuità topologiche (impulsi nei salti verticali).

  

# Trasformata di Laplace

La Trasformata di Laplace è un operatore matematico lineare essenziale nell'ingegneria dei sistemi; il suo scopo primario è quello di mappare problemi definiti da equazioni differenziali nel dominio del tempo reale, trasformandoli in sistemi di equazioni puramente algebriche nel dominio complesso.

  

Si adotta la notazione convenzionale che prevede l'uso di lettere minuscole (es. $f(t)$) per identificare funzioni nel dominio del tempo, e delle corrispondenti lettere maiuscole (es. $F(s)$) per indicare le relative funzioni trasformate nel dominio di Laplace.

  

Data una funzione causale del tempo $f(t)$ (ovvero nulla per $t<0$), la sua Trasformata di Laplace $F(s) = \mathcal{L}\{f(t)\}$ è definita attraverso l'integrale improprio:

  

$$F(s) = \int_{0^-}^{+\infty} f(t) e^{-st} dt \quad \text{con } s \in \mathbb{C}$$

  

La variabile complessa $s$ è definita come $s = \sigma + j\omega$. Il nucleo dell'integrale $e^{-st}$ si espande dunque in $e^{-\sigma t} \cdot e^{-j\omega t}$. Mentre $e^{-j\omega t}$ è una componente puramente oscillatoria in base alla formula di Eulero, il termine reale $e^{-\sigma t}$ funge da fattore di smorzamento o attenuazione. Se la funzione originaria $f(t)$ tende a divergere all'infinito, l'integrale improprio non potrebbe convergere; tuttavia, imponendo che la parte reale $\sigma$ assuma valori sufficientemente grandi e positivi (superando un valore di soglia noto come _ascissa di convergenza_ $\sigma^*$), l'esponenziale decrescente annulla la divergenza della funzione garantendo l'esistenza finita dell'integrale.

  

## Proprietà e Teoremi della Trasformata

L'utilità suprema della trasformata di Laplace non risiede nel calcolo iterato e tedioso dell'integrale di definizione, bensì nella capacità di ricavare le trasformate di funzioni complesse operando per via puramente algebrica a partire da un insieme di proprietà e teoremi basilari.

  

### Linearità dell'Operatore

Data la linearità intrinseca dell'operazione integrale, la Trasformata di Laplace è un operatore lineare. Siano $\alpha, \beta$ due scalari reali, si ha:

  

$$\mathcal{L}\{\alpha f_1(t) + \beta f_2(t)\} = \alpha F_1(s) + \beta F_2(s)$$

  

### Derivazione nel Dominio del Tempo

Questo teorema è il perno della conversione da differenziale ad algebrico. La trasformata della derivata prima di una funzione $f(t)$ è pari a:

  

$$\mathcal{L}\{\dot{f}(t)\} = sF(s) - f(0^-)$$

  

> **Dimostrazione mediante Integrazione per Parti**
> 
>   
> 
>   
> 
> $$\mathcal{L}\{\dot{f}(t)\} = \int_{0^-}^{+\infty} \dot{f}(t)e^{-st} dt$$
> 
>   
> 
> Scegliendo $\dot{f}(t)$ come fattore da integrare e $e^{-st}$ da derivare, si ottiene:
> 
>   
> 
> $$\left[ f(t)e^{-st} \right]_{0^-}^{+\infty} - \int_{0^-}^{+\infty} f(t)(-s)e^{-st} dt$$
> 
>   
> 
> Valutando il termine racchiuso: per $t \to +\infty$, l'esponenziale convergente $e^{-st}$ costringe il termine a $0$. Per $t \to 0^-$, si ottiene $-f(0^-)$. Portando la costante $+s$ fuori dal secondo integrale, si palesa la definizione stessa della trasformata:
> 
>   
> 
> $$-f(0^-) + s \int_{0^-}^{+\infty} f(t)e^{-st} dt = sF(s) - f(0^-)$$
> 
>   

### Integrazione nel Dominio del Tempo

Complementarmente, l'integrazione di una funzione nel dominio del tempo equivale a una semplice divisione algebrica per la variabile complessa $s$ nel dominio di Laplace.

  

$$\mathcal{L}\left\{ \int_{0}^{t} f(\tau) d\tau \right\} = \frac{1}{s}F(s)$$

  

### Traslazione e Ritardo nel Tempo

Se un segnale viene ritardato rigorosamente nel tempo, ovvero traslato mantenendo la sua assenza per valori antecedenti (moltiplicandolo per il gradino ritardato), nel dominio di Laplace si riflette come una moltiplicazione per un esponenziale.

  

$$\mathcal{L}\{f(t-T)1(t-T)\} = e^{-sT}F(s)$$

  

È cruciale la presenza del termine $1(t-T)$ per escludere il dominio precedente alla traslazione, diversamente, l'integrale ingloberebbe parti di funzione "sconosciute" non incluse nella trasformata originaria $F(s)$.

  

### Traslazione nel Dominio Complesso S

Analogamente, moltiplicare una funzione del tempo per un esponenziale reale $e^{at}$ provoca una traslazione rigida della funzione trasformata all'interno del dominio complesso $s$.

  

$$\mathcal{L}\{e^{at}f(t)\} = F(s-a)$$

  

### Moltiplicazione per t

Moltiplicare un segnale temporale per la variabile tempo $t$ corrisponde, a meno del segno, alla derivazione rispetto alla variabile complessa $s$ della sua trasformata.

  

$$\mathcal{L}\{t f(t)\} = -\frac{d}{ds}F(s)$$

  

## Calcolo di Trasformate Notevoli dalle Proprietà

In virtù delle proprietà formali sin qui esposte, è possibile dedurre le Trasformate di Laplace delle funzioni canoniche più utilizzate senza dover calcolare alcun integrale improprio.

  

1. **Impulso di Dirac $\delta(t)$:**
    
    Applicando direttamente la proprietà di campionamento dell'integrale di definizione della trasformata:
    
      
    
    $$\mathcal{L}\{\delta(t)\} = \int_{0^-}^{+\infty} \delta(t) e^{-st} dt = e^{-s \cdot 0} = 1$$
    
      
    
    La trasformata della Delta è unificante e vale semplicemente 1.
    
      
    
2. **Gradino Unitario $1(t)$ e Costanti:** Riconoscendo che il gradino è per definizione l'integrale dell'impulso $\int \delta(\tau) d\tau$, si applica il teorema dell'integrazione reale sull'operatore di Laplace.
    
      
    
    $$\mathcal{L}\{1(t)\} = \frac{1}{s}\mathcal{L}\{\delta(t)\} = \frac{1}{s} \cdot 1 = \frac{1}{s}$$
    
      
    
    Qualsiasi costante $K$ integrata da 0 in avanti (assimilabile a $K \cdot 1(t)$) ha come trasformata $K/s$.
    
      
    
3. **Potenze del Tempo (Rampe, Parabole):** Iterando il ragionamento, la Rampa $t \cdot 1(t)$ è l'integrale del gradino.
    
      
    
    $$\mathcal{L}\{t \cdot 1(t)\} = \frac{1}{s} \mathcal{L}\{1(t)\} = \frac{1}{s} \cdot \frac{1}{s} = \frac{1}{s^2}$$
    
      
    
    Generalizzando per un impulso di ordine negativo arbitrario (integrali successivi), per la forma ridotta $t^k/k!$ si ottiene:
    
      
    
    $$\mathcal{L}\left\{ \frac{t^k}{k!} 1(t) \right\} = \frac{1}{s^{k+1}}$$
    
      
    
4. **Esponenziale $e^{at}$:** Si sfrutta la proprietà di traslazione nel dominio complesso, identificando l'esponenziale come la funzione gradino costantemente 1, pre-moltiplicata per $e^{at}$.
    
      
    
    $$\mathcal{L}\{e^{at} \cdot 1(t)\} = \left. \mathcal{L}\{1(t)\} \right\vert{}_{s \to s-a} = \frac{1}{s-a}$$
    
      
    
5. **Funzioni Armoniche: Seno $\sin(\omega t)$ e Coseno $\cos(\omega t)$:** La deduzione delle trasformate delle funzioni goniometriche si avvale della Formula di Eulero per transitare agilmente nel campo complesso. La funzione seno si espande in: $\sin(\omega t) = \frac{e^{j\omega t} - e^{-j\omega t}}{2j}$. Sfruttando la linearità dell'operatore di Laplace $\mathcal{L}$ e il risultato acquisito sull'esponenziale con esponente complesso immaginario:
    
      
    
    $$\mathcal{L}\{\sin(\omega t)\} = \frac{1}{2j} \left[ \mathcal{L}\{e^{j\omega t}\} - \mathcal{L}\{e^{-j\omega t}\} \right]$$
    
      
    
    Applicando le singole trasformate esponenziali si ottiene la differenza di frazioni:
    
      
    
    $$= \frac{1}{2j} \left( \frac{1}{s - j\omega} - \frac{1}{s + j\omega} \right)$$
    
      
    
    Trovando il minimo comune multiplo algebrico al denominatore (somma per differenza: $s^2 - (j\omega)^2 = s^2 + \omega^2$):
    
      
    
    $$= \frac{1}{2j} \left( \frac{s + j\omega - (s - j\omega)}{s^2 + \omega^2} \right) = \frac{1}{2j} \left( \frac{2j\omega}{s^2 + \omega^2} \right)$$
    
      
    
    L'espressione semplificata finale, depurata dai termini immaginari come atteso analiticamente (la trasformata di una funzione reale produce coefficienti complessi polinomiali unicamente a simmetria reale), è:
    
      
    
    $$\mathcal{L}\{\sin(\omega t)\} = \frac{\omega}{s^2 + \omega^2}$$
    
      
    
    Attraverso procedimenti speculari (od operando direttamente la derivazione temporale sul risultato del seno), si ricava in maniera compatta anche il corrispettivo per la funzione Coseno:
    
      
    
    $$\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2 + \omega^2}$$