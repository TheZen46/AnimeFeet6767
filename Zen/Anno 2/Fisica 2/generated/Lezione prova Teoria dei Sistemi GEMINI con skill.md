
# Introduzione ai Sistemi e Funzioni Generalizzate

## Concetti Introduttivi sui Sistemi

In ingegneria e nella teoria dei sistemi, un sistema è concettualmente descrivibile come una "scatola" logica che pone in relazione delle cause (o ingressi) con degli effetti (o uscite). 

```mermaid
graph LR
    C[Cause esterne c_e] --> S[SISTEMA]
    CI[Cause interne c_i] --> S
    S --> E[Effetto e]
````

I sistemi si suddividono principalmente in due grandi macro-categorie:

  

- **Sistemi Algebrici:** L'effetto valutato in un determinato istante di tempo dipende unicamente dalla causa applicata in quello stesso identico istante. Un esempio classico è la calcolatrice: l'operazione matematica restituisce un risultato in base ai tasti premuti in quel momento, senza conservare memoria delle operazioni passate (salvo memorie esplicite). Hanno un interesse teorico nullo ai fini di questo corso.
    
      
    
- **Sistemi Dinamici:** L'effetto misurato al tempo $t$ dipende non solo dalle cause esterne (gli ingressi) applicate nell'istante di osservazione, ma anche dalla storia passata del sistema. Questa "storia passata" viene riassunta in quelle che si definiscono _cause interne_ o _condizioni iniziali_ del sistema, valutate in un istante iniziale $t_0$.
    
      
    

> [!example] Il Sistema Dinamico "Lavandino" Per visualizzare il concetto di causa interna ed esterna, si consideri una vasca (o lavandino) di sezione unitaria in cui viene immessa dell'acqua tramite un rubinetto.
> 
>   
> 
> - L'altezza dell'acqua $h(t)$ (o volume) rappresenta l'effetto del sistema.
>     
>       
>     
> - La portata del rubinetto $u(t)$ rappresenta la causa esterna.
>     
>       
>     
> - L'altezza iniziale dell'acqua al tempo zero $h(0)$ rappresenta la causa interna.
>     
>       
>     
> 
> La dinamica è descritta dall'equazione differenziale $\dot{h}(\tau) = u(\tau)$. Integrando ambo i membri, si ottiene:
> 
>   
> 
> $$h(t) = h(0) + \int_{0}^{t} u(\tau) d\tau$$
> 
>   
> 
> L'effetto totale $h(t)$ è dato dalla somma della condizione iniziale $h(0)$ e dell'integrale della causa esterna $u(\tau)$ nell'intervallo di osservazione.
> 
>   

### Proprietà Fondamentali dei Sistemi Trattati

Il corso si concentra sullo studio di una classe ristretta ma fondamentale di sistemi, caratterizzati da tre proprietà matematiche:

  

- **Linearità:** Un sistema è lineare se vale il principio di sovrapposizione degli effetti. L'effetto complessivo dovuto all'azione simultanea di cause interne ed esterne (anche molteplici) equivale alla somma algebrica degli effetti calcolati considerando ogni causa agente singolarmente, ponendo le altre pari a zero.
    
      
    
- **Tempo-invarianza (Stazionarità):** Un sistema è stazionario se l'effetto prodotto da un esperimento non dipende dalla sua collocazione temporale sull'asse assoluto dei tempi. A parità di cause, un esperimento condotto oggi o domani produrrà l'identico andamento in uscita, semplicemente traslato nel tempo.
    
      
    
- **Tempo Continuo:** Le relazioni tra causa ed effetto sono modellate in un dominio temporale continuo tramite l'utilizzo di equazioni differenziali (a differenza dei sistemi a tempo discreto che impiegano equazioni alle differenze).
    
      
    

> [!tip] Approfondimento: Linearizzazione e il Pendolo Inverso #approfondimento Sebbene la realtà fisica sia dominata da fenomeni non lineari (presenza di attriti, saturazioni, funzioni trigonometriche come il seno nell'equazione del pendolo), la Teoria dei Sistemi Lineari è lo strumento cardine dell'ingegneria dei controlli. Molti sistemi non lineari complessi, se perturbati solo lievemente rispetto a un punto di equilibrio, si comportano localmente in modo lineare. Un esempio lampante discusso a lezione è il "Segway": esso è concettualmente assimilabile a un pendolo inverso (massa instabile incernierata in basso) che, se lasciato a sé, cadrebbe inevitabilmente. Tuttavia, retroazionando opportunamente il sistema per compensare i piccoli scostamenti (come fa intuitivamente una persona bilanciando un ombrello sul palmo della mano), è possibile stabilizzare la dinamica usando algoritmi sintetizzati unicamente sulle basi della teoria lineare[cite: 9].
> 
>   

## Funzioni Generalizzate (Distribuzioni)

Per trattare fenomeni impulsivi, discontinuità e variazioni repentine, il calcolo infinitesimale classico viene esteso introducendo le funzioni generalizzate (o distribuzioni).

  

### Il Gradino Unitario e la Rampa Unitaria

Il gradino unitario $1(t)$ (impulso di ordine $-1$) è una funzione che descrive un'attivazione improvvisa:

  

$$1(t) = \int_{-\infty}^{t} \delta(\tau) d\tau = \begin{cases} 0 & t < 0 \\ 1 & t \ge 0 \end{cases}$$

  

Una qualunque funzione $f(t)$ moltiplicata per il gradino $1(t)$ "esiste" solo per tempi positivi, annullandosi per $t < 0$.

  

L'integrale del gradino unitario origina la **rampa unitaria** (impulso di ordine $-2$):

  

$$\int_{-\infty}^{t} 1(\tau) d\tau = t \cdot 1(t) = \begin{cases} 0 & t < 0 \\ t & t \ge 0 \end{cases}$$

  

### L'Impulso di Dirac (Delta di Dirac)

L'impulso di ordine $0$, comunemente noto come Delta di Dirac $\delta(t)$, non è una funzione in senso classico, ma è definito matematicamente attraverso il suo integrale:

  

$$\int_{-\infty}^{t} \delta(\tau) d\tau = 0 \quad \forall t < 0$$

  

$$\int_{0^{-}}^{0^{+}} \delta(\tau) d\tau = 1$$

  

Graficamente, $\delta(t)$ può essere interpretato come il limite di un rettangolo centrato nell'origine, di base $2T$ e altezza $\frac{1}{2T}$, per $T \to 0$. Mentre la base si restringe a zero, l'altezza tende all'infinito, mantenendo rigorosamente l'area sottesa unitaria. L'equazione di traslazione $\delta(t-T)$ definisce un impulso che "esiste" ed è concentrato interamente all'istante di tempo $t = T$.

  

> [!important] Proprietà di Campionamento (Sifting Property)
> 
> Moltiplicando una funzione continua $f(t) \in C^{\infty}$ per una delta di Dirac traslata, la delta "campiona" o preleva il valore della funzione unicamente nell'istante di traslazione $T$:
> 
>   
> 
> $$f(t)\delta(t-T) = \begin{cases} f(T)\delta(t-T) & f(T) \ne 0 \\ 0 & f(T) = 0 \end{cases}$$
> 
>   
> 
> Integrando questo prodotto su tutto l'asse reale, l'impulso isola il valore esatto della funzione:
> 
>   
> 
> $$\int_{-\infty}^{+\infty} f(\tau)\delta(\tau-t) d\tau = f(t)$$
> 
>   

### Derivate delle Funzioni Generalizzate

Le funzioni con discontinuità generano impulsi quando vengono derivate. Un salto (discontinuità di prima specie) in una funzione produce, nella sua derivata, un impulso di Dirac la cui area, indicata dal coefficiente moltiplicativo, equivale all'ampiezza algebrica del salto stesso.

  

Applicando la regola di derivazione del prodotto, estesa anche al caso in cui una delle funzioni non sia derivabile in senso classico, si ottiene:

  

$$\frac{d}{dt}[f(t)g(t)] = \dot{f}(t)g(t) + f(t)\dot{g}(t)$$

  

Per una generica funzione $f(t)$ moltiplicata per un gradino unitario, si ha:

  

$$\frac{d}{dt}[f(t)1(t)] = \dot{f}(t)1(t) + f(t)\delta(t) = \dot{f}(t)1(t) + f(0)\delta(t)$$

  

Derivare l'impulso di Dirac $\delta(t)$ restituisce l'impulso di ordine $1$ o _doppietto_ $\dot{\delta}(t)$. L'operazione di derivazione incrementa di $1$ l'ordine dell'impulso, mentre l'operazione di integrazione riduce di $1$ l'ordine dell'impulso. Pertanto, la derivata di un doppietto origina un impulso di ordine $2$, $\ddot{\delta}(t)$.

  

> [!warning] Sezione ricostruita — inizio Nelle lezioni trasmesse emerge l'uso della funzione "Gate pulse" (o impulso rettangolare). Il docente lo costruisce definendo un intervallo $(T_1, T_2)$ tramite la sottrazione di due gradini unitari.
> 
>   
> 
> $$Puls(t) = 1(t-T_1) - 1(t-T_2) = \begin{cases} 0 & (-\infty, T_1) \cup (T_2, +\infty) \\ 1 & (T_1, T_2) \end{cases}$$
> 
>   
> 
> Moltiplicare una funzione $f(t)$ per tale costrutto significa estrarre, isolare o "fotografare" una specifica porzione temporale del segnale, annullando rigorosamente tutto il resto. Questa tecnica risulterà fondamentale quando bisognerà calcolare le trasformate di profili di ingresso compositi. Sezione ricostruita — fine
> 
>   

## La Trasformata di Laplace

Per convertire il difficile compito di risolvere equazioni differenziali in un problema più gestibile di algebra polinomiale, si introduce l'operatore Trasformata di Laplace. Data una funzione nel dominio del tempo $f(t)$, la sua trasformata $F(s)$ (con $s \in \mathbb{C}, s = \sigma + j\omega$) è definita come:

  

$$F(s) = \mathcal{L}\{f(t)\} = \int_{0^{-}}^{+\infty} f(t) e^{-st} dt$$

  

L'integrale viene valutato a partire da $0^-$ in modo da intercettare e inglobare correttamente le eventuali condizioni impulsive concentrate esattamente nell'origine. Questo integrale improprio converge solo per valori di $s$ in cui la parte reale $\sigma$ è sufficientemente elevata da garantire che il termine esponenziale decadente smorzi un'eventuale divergenza all'infinito di $f(t)$ (tale limite è detto _ascissa di convergenza_).

  

### Proprietà Fondamentali

La trasformata gode di notevoli proprietà matematiche che evitano il calcolo sistematico dell'integrale:

  

- **Linearità:** $\mathcal{L}\{\alpha f_1(t) + \beta f_2(t)\} = \alpha F_1(s) + \beta F_2(s)$
    
      
    
      
    
- **Derivazione Reale:** $\mathcal{L}\{\dot{f}(t)\} = sF(s) - f(0^-)$
    
      
    
      
    
- **Integrazione Reale:** $\mathcal{L}\{\int_{0}^{t} f(\tau) d\tau\} = \frac{1}{s}F(s)$
    
      
    
      
    
- **Traslazione nel Tempo:** $\mathcal{L}\{f(t-T)1(t-T)\} = e^{-sT}F(s)$
    
      
    
      
    
- **Traslazione in Frequenza:** $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$
    
      
    
      
    
- **Moltiplicazione per Potenze del Tempo:** $\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n}{ds^n}F(s)$
    
      
    
      
    

### Tabella delle Trasformate Notevoli

Utilizzando le proprietà descritte, si derivano direttamente dal calcolo della $\mathcal{L}\{\delta(t)\}$ le seguenti forme standard:

  

|**f(t)**|**F(s)**|**Note**|
|---|---|---|
|$\delta(t)$|$1$|Impulso di Dirac|
|$1(t)$|$\frac{1}{s}$|Gradino unitario|
|$t \cdot 1(t)$|$\frac{1}{s^2}$|Rampa unitaria|
|$\frac{t^n}{n!}1(t)$|$\frac{1}{s^{n+1}}$|Potenza scalata|
|$e^{at}1(t)$|$\frac{1}{s-a}$|Esponenziale|
|$\sin(\omega t)1(t)$|$\frac{\omega}{s^2+\omega^2}$|Sinusoide, ottenuta via formula di Eulero|
|$\cos(\omega t)1(t)$|$\frac{s}{s^2+\omega^2}$|Cosinusoide, ottenuta per derivazione del seno|

## Antitrasformazione e Metodo dell'Espansione in Fratti Semplici

L'operazione inversa, ovvero ricavare l'evoluzione temporale reale $f(t)$ a partire dalla $F(s)$, si effettua scomponendo i complessi rapporti polinomiali generati nei sistemi in somme di frazioni base di cui è nota l'antitrasformata (i cosiddetti fratti semplici). Sia data $F(s) = \frac{n(s)}{d(s)}$:

  

### Caso 1: Grado(Num) < Grado(Den)

Il denominatore $d(s)$ viene fattorizzato nelle sue radici (i _poli_ del sistema). Per poli reali e distinti $p_i$, con molteplicità $\mu_i$, l'espansione assume la forma:

  

$$F(s) = \sum_{i=1}^{N_d} \sum_{k=1}^{\mu_i} \frac{A_{ik}}{(s-p_i)^k}$$

  

Sapendo che $\mathcal{L}\{\frac{1}{n!}t^n e^{at} 1(t)\} = \frac{1}{(s-a)^{n+1}}$, la generica antitrasformata restituirà somme di andamenti esponenziali, modulati o meno dal tempo a seconda della molteplicità del polo. Nel caso di radici del denominatore a valori complessi coniugati $p_{1,2} = -\sigma \pm j\omega$, i fratti andranno ricondotti a polinomi di secondo grado a numeratore generico che daranno origine in campo temporale a funzioni di tipo sinusoidale smorzate come $e^{-\sigma t}\sin(\omega t)$ ed $e^{-\sigma t}\cos(\omega t)$.

  

> [!important] Calcolo dei Residui (Metodo Generale) Per calcolare formalmente un coefficiente (residuo) incognito $A_{ik}$ associato al polo $p_i$ di ordine $\mu_i$, si utilizza la formula dei limiti:
> 
>   
> 
> $$A_{ik} = \lim_{s \to p_i} \frac{1}{(\mu_i - k)!} \frac{d^{(\mu_i-k)}}{ds^{(\mu_i-k)}} \left[ (s-p_i)^{\mu_i} F(s) \right]$$
> 
>   

### Caso 2: Grado(Num) $\ge$ Grado(Den)

Non è possibile effettuare l'espansione in fratti semplici direttamente. Bisogna prima applicare la divisione lunga tra polinomi in modo da scorporare un quoziente intero (che genererà impulsi e derivate dell'impulso di ordine crescente nell'antitrasformata) ed un termine resto fratto analizzabile secondo il "Caso 1".

  

## Teoremi del Valore Iniziale e Finale

Questi teoremi consentono di indagare asintoticamente il comportamento nel tempo di una funzione studiando esclusivamente i limiti della sua trasformata, senza dover applicare l'antitrasformazione.

  

- **Teorema del Valore Iniziale:** $\lim_{t \to 0^+} f(t) = \lim_{s \to \infty} sF(s)$. Se il grado del numeratore pareggia o supera quello del denominatore, l'antitrasformata presenterà comportamenti impulsivi, per cui il limite di $sF(s)$ produrrà un esito divergente. Il teorema deve quindi essere applicato solo alla parte propria della funzione ottenuta dopo scomposizione polinomale.
    
      
    
- **Teorema del Valore Finale:** $\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$. Per applicare lecitamente questo calcolo asintotico, vi è una rigida precondizione: **il limite per $t \to \infty$ deve esistere a priori nel dominio del tempo**. La sua applicabilità è dettata esclusivamente dalla natura delle radici del denominatore $d(s)$:
    
      
    1. Tutte le radici (poli) devono avere parte reale strettamente negativa ($\sigma < 0$) affinché i modi propri decadano esponenzialmente a zero.
        
          
        
    2. Sono consentite radici nell'origine ($s=0$) a patto che presentino molteplicità strettamente unitaria.
        
          
        
    3. La presenza di poli complessi puramente immaginari annulla la fattibilità del teorema a causa delle oscillazioni perenni generate (es. seno o coseno che a infinito non ammettono limite definito).
        
          
        

## Stabilità dei Polinomi e Criterio di Routh-Hurwitz

Poiché per applicare il Teorema del Valore Finale (e per analizzare la stabilità asintotica dei sistemi) è necessario sincerarsi che le radici del polinomio a denominatore abbiano unicamente parti reali strettamente negative, è essenziale poter dedurre questa informazione a priori, senza calcolare manualmente le soluzioni algebriche del polinomio (che per gradi $>3$ risultano proibitive).

  

**1. Regola dei Segni di Cartesio** Costituisce una condizione _necessaria, ma non sufficiente_ per radici stabili. Si enuncia semplicemente verificando se il polinomio $s^n + a_{n-1}s^{n-1} + ... + a_0$ presenta dei coefficienti nulli o variazioni di segno. Se esistono variazioni di segno tra i coefficienti, o se manca uno dei monomi, di sicuro il polinomio possiederà almeno una radice a parte reale non negativa, rendendo di fatto inutile la compilazione della successiva e più complessa Tabella di Routh.

  

**2. Tabella di Routh-Hurwitz**

Se le condizioni necessarie di Cartesio sono rispettate, si procede inquadrando i coefficienti e calcolando determinanti per righe incrociate (simile all'algoritmo di Gauss).

  

$$T(i,j) = -\frac{\det\begin{pmatrix} T(i-2, 1) & T(i-2, j+1) \\ T(i-1, 1) & T(i-1, j+1) \end{pmatrix}}{T(i-1, 1)}$$

  

Una volta completata la tabella discesa fino al monomio di grado $0$ ($s^0$), la validazione del test è immediata: se e solo se **tutti gli elementi disposti nella prima colonna della tabella presentano segno positivo**, l'intero pacchetto di radici del polinomio possiederà garanzia di parte reale negativa (quindi stabilità del limite per tempi infiniti). Se compare uno zero, lo si sostituisce analiticamente con una variabile test $\epsilon \to 0^+$ per procedere coi calcoli asintotici e valutare i segni.

  

## Risoluzione di Equazioni Differenziali

La principale utilità della Trasformata di Laplace risiede nella metodica semplificata per la soluzione delle equazioni differenziali ordinarie a coefficienti costanti in forma ingresso/uscita:

  

$$y^{(n)} + a_{n-1}y^{(n-1)} + ... + a_0 y = b_m u^{(m)} + ... + b_0 u$$

  

Applicando a cascata l'operatore di Laplace e sfruttando la proprietà della derivata, le grandezze integrali originali e differenziali passano dalla dipendenza da $t$ a polinomi nella variabile complessa $s$ contenenti le condizioni iniziali necessarie del sistema al tempo zero:

  

$$L\{\dot{y}(t)\} = sY(s) - y(0^-)$$

  

$$L\{\ddot{y}(t)\} = s^2 Y(s) - sy(0^-) - \dot{y}(0^-)$$

  

Raggruppando matematicamente $Y(s)$, la soluzione generica esplicita i due contributi disgiunti del sistema:

  

$$Y(s) = \underbrace{\frac{b_m s^m + ... + b_0}{s^n + a_{n-1}s^{n-1} + ... + a_0} U(s)}_{Risposta\_a\_stato\_zero} + \underbrace{\frac{I^y(s, \text{condizioni\_iniziali}) - I^u(s, \text{derivate\_ingresso})}{s^n + a_{n-1}s^{n-1} + ... + a_0}}_{Risposta\_a\_ingresso\_nullo}$$

  

- La **Risposta a Ingresso Nullo (omogenea associata)** dipende esclusivamente dalle condizioni dello stato del sistema immagazzinate in $t=0^-$ ed evolve dinamicamente priva dell'influenza dell'ingresso esterno $u(t)$.
    
      
    
- La **Risposta a Stato Zero** analizza la pura dinamica del sistema sotto eccitazione dell'ingresso supponendo scarichi gli accumuli pregressi (tutte le condizioni iniziali e derivate a zero).
    
      
    

> [!important] La Funzione di Trasferimento $T(s)$ Isolando dalla precedente soluzione il rapporto puro tra le dinamiche di eccitazione (ingresso) e gli effetti (uscita) — annullando formalmente le condizioni di partenza — si giunge a delineare la "Funzione di Trasferimento" del sistema.
> 
>   
> 
> $$T(s) = \frac{Y(s)}{U(s)} = \frac{b_m s^m + ... + b_0}{s^n + a_{n-1}s^{n-1} + ... + a_0}$$
> 
>   
> 
> Questo rapporto polinomiale ingloba integralmente la struttura fisica, modale ed intrinseca del sistema dinamico modellato e costituisce la chiave di volta di tutta la Teoria dei Controlli.