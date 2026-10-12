YAML

```
---
lezione: "1-2"
data: 2026-09-22
argomenti: [sistemi, funzioni generalizzate, delta di dirac, trasformata di laplace, antitrasformazione, equazioni differenziali]
---
```

# Teoria dei Sistemi: Introduzione e Fondamenti Matematici

## 1. Introduzione e Classificazione dei Sistemi

Un sistema può essere modellato come un ente o un operatore matematico all'interno del quale è possibile isolare e identificare una precisa relazione tra una o più cause in ingresso e i corrispondenti effetti in uscita.

  


```
graph LR
    A[Cause Esterne <br/> $c_e(t)$] --> C[SISTEMA]
    B[Cause Interne <br/> $c_i(t_0)$] --> C
    C --> D[Effetto <br/> $e(t)$]
```

La distinzione fondamentale per l'analisi sistemistica divide i modelli in due grandi categorie:

  

- **Sistemi Algebrici**: L'effetto misurato in un determinato istante di tempo dipende unicamente dalla causa applicata in quello stesso identico istante. Un esempio emblematico è una semplice calcolatrice: il risultato fornito (effetto) deriva istantaneamente dagli operandi immessi (causa), a prescindere dalle operazioni eseguite in passato. Questa assenza di "memoria" rende tali sistemi di scarso interesse per la modellistica avanzata.
    
      
    
- **Sistemi Dinamici**: L'effetto in un determinato istante dipende sia dalle cause esterne $c_e(\tau)$ che hanno agito nell'intervallo di tempo precedente all'osservazione, sia dalle cause interne $c_i(t_0)$, che descrivono lo stato del sistema all'istante iniziale.
    
      
    

> [!example] Il Serbatoio (Sistema Dinamico) Immaginando un contenitore d'acqua in cui il livello totale è l'effetto misurabile $h(t)$ e la portata in ingresso tramite un rubinetto è la causa esterna $u(t)$, si evince che il livello finale di acqua non dipende solo da quanto rubinetto si è aperto. Risulta essenziale conoscere il livello di partenza $h(0)$ (la causa interna). L'equazione differenziale risolta che regola questo sistema è data da $h(t) = h(0) + \int_{0}^{t} u(\tau) d\tau$, in cui le due cause, interna ed esterna, si sommano algebricamente per generare l'effetto.
> 
>   

Il corso si concentra precipuamente sullo studio di sistemi che rispondono a tre specifiche caratteristiche matematiche:

  

1. **Linearità**: Vale in modo stretto il principio di sovrapposizione degli effetti. Se sono presenti molteplici cause, l'effetto totale del sistema è calcolabile come la pura somma algebrica degli effetti che si otterrebbero isolando ciascuna singola causa.
    
      
    
2. **Tempo-invarianza (Stazionarietà)**: Il comportamento del sistema è insensibile rispetto al posizionamento temporale assoluto dell'esperimento. Spostare le condizioni di ingresso avanti o indietro nell'asse dei tempi genera una risposta ritardata o anticipata della stessa identica entità, senza mutarne la forma.
    
      
    
3. **Tempo Continuo**: L'evoluzione del sistema può essere descritta tramite l'utilizzo di equazioni differenziali in cui la variabile temporale scorre come un continuum fluido, in opposizione ai sistemi che evolvono per variazioni a stati logici discreti.
    
      
    

## 2. Le Funzioni Generalizzate (Distribuzioni)

Per analizzare agevolmente segnali complessi e discontinuità nel tempo continuo, si introduce il concetto di funzioni generalizzate (o distribuzioni). La capostipite di tali funzioni è l'impulso di ordine 0, ossia la **Delta di Dirac** $\delta(t)$.

  

### 2.1 La Delta di Dirac $\delta(t)$ e le sue proprietà

La funzione $\delta(t)$ è definita unicamente attraverso il suo comportamento integrale. Essa è rigorosamente nulla per ogni $t \neq 0$, mentre nell'intorno dell'origine assume un valore tale che il suo integrale definito valga esattamente $1$:

  

$$\int_{-\infty}^{t} \delta(\tau) d\tau = 0 \quad \forall t < 0$$

$$\int_{0^-}^{0^+} \delta(\tau) d\tau = 1$$

Dal punto di vista geometrico e per approssimazione, si può immaginare un impulso rettangolare $p_T(t)$ centrato nell'origine, avente base pari a $2T$ e altezza $1/(2T)$ (in modo da mantenere l'area costante e pari all'unità). Facendo tendere la base a $0$ ($T \to 0$), l'altezza del rettangolo diverge all'infinito e la funzione si restringe fino a collassare in un'unica freccia applicata in $t=0$, identificando così la delta di Dirac. Se l'impulso presenta un coefficiente moltiplicativo $A$, l'integrale a cavallo dell'impulso sarà pari esattamente all'area $A$.

  

> [!important] Proprietà di Campionamento (Sifting Property) Moltiplicando una funzione continua $f(t)$ per un impulso $\delta(t-T)$ traslato al tempo $T$, si annulla tutta la funzione eccezion fatta per il punto in cui cade l'impulso. Integrando tale espressione su tutto l'asse reale si ottiene esattamente il valore campionato di $f$ in $T$:
> 
>   
> 
> $$\int_{-\infty}^{+\infty} f(\tau)\delta(\tau-t) d\tau = f(t)$$
> 
> Allo stesso modo, il semplice prodotto per l'impulso restituisce l'impulso stesso ridimensionato: $f(t)\delta(t-T) = f(T)\delta(t-T)$ (che è vero a patto che $f(T) \neq 0$).
> 
>   

> [!tip] Approfondimento #approfondimento
> 
> La nozione di Delta di Dirac introdotta ingegneristicamente non è una funzione in senso stretto (non avendo valori ben determinabili sul codominio in $t=0$), ma appartiene allo spazio delle distribuzioni elaborato dalla _Teoria delle distribuzioni di Schwartz_. Si giustifica unicamente quando appare all'interno del segno di integrale ("sotto forma di operatore funzionale") applicata ad una funzione di test infinitamente derivabile a supporto compatto.
> 
>   

### 2.2 Gerarchia degli Impulsi per Integrazione e Derivazione

È possibile definire un'intera scala di ordini impulsivi attraverso le canoniche operazioni di calcolo infinitesimale. Partendo dalla $\delta(t)$ (ordine $0$), si ottengono impulsi di ordine superiore tramite derivazione e impulsi di ordine inferiore (negativo) tramite integrazione.

  

- **Derivata della Delta (Doppietto, ordine $1$)**: La funzione $\dot{\delta}(t) = \frac{d}{dt}\delta(t)$ rappresenta un impulso di ordine $1$. Essa graficamente viene rappresentata come un impulso positivo e uno negativo infinitamente vicini.
    
      
    
- **Gradino Unitario $1(t)$ (ordine $-1$)**: Integrando una volta la $\delta(t)$ si ottiene il gradino unitario, una funzione nulla per $t<0$ e pari a $1$ per $t>0$.
    
      
    
    $$\int_{-\infty}^{t} \delta(\tau) d\tau = 1(t)$$
    
- **Rampa Unitaria $t \cdot 1(t)$ (ordine $-2$)**: Iterando l'integrazione sul gradino si genera una rampa unitaria.
    
      
    
    $$\int_{-\infty}^{t} 1(\tau) d\tau = t \cdot 1(t)$$
    

### 2.3 Derivazione di Funzioni Discontinue e Gate Pulses

Le funzioni generalizzate sono ampiamente utilizzate per derivare funzioni discontinue. Qualsiasi "salto" a gradino in una funzione (discontinuità di prima specie) porta allo sviluppo matematico di un impulso di Dirac nella sua funzione derivata, di area esattamente pari all'ampiezza del salto. Si può formalizzare l'applicazione delle consuete regole di derivazione persino ai prodotti fra funzioni regolari e distribuzioni. Per il prodotto di una generica $f(t)$ continua per la delta, risulta:

  

$$\frac{d}{dt}[f(t)\delta(t)] = \dot{f}(t)\delta(t) + f(t)\dot{\delta}(t)$$

Isolando l'ultimo termine si ricava una relazione notevole per il campionamento di derivate:

  

$$f(t)\dot{\delta}(t) = f(0)\dot{\delta}(t) - \dot{f}(0)\delta(t)$$

Per estrarre o "fotografare" singoli spezzoni di una funzione, si fa abitualmente uso del "Gate pulse", costruito sottraendo due gradini traslati: $1(t-T_1) - 1(t-T_2)$. Questo costrutto algebrico produce una "finestra" (o boxcar) di valore $1$ esclusivamente nell'intervallo compreso tra i tempi $(T_1, T_2)$.

  

## 3. La Trasformata di Laplace

La trasformata di Laplace costituisce lo strumento cardine per ridurre equazioni differenziali complesse a molto più banali equazioni algebriche su variabili di campo complesso. L'operazione matematica di base converte una funzione del tempo $f(t)$ in una funzione complessa $F(s)$, dove la variabile complessa è espressa come $s = \sigma + j\omega$:

  

$$\mathcal{L}\{f(t)\} = F(s) = \int_{0^-}^{\infty} f(t)e^{-st} dt \quad \text{per } s \in \mathbb{C}$$

L'integrale sussiste fintanto che la convergenza è assicurata: la parte reale $\sigma$ dell'esponenziale funge da fattore di smorzamento, sopprimendo le divergenze della $f(t)$ originaria per tutti i valori posizionati a destra di una critica _ascissa di convergenza_ $\sigma^*$.

  

### 3.1 Proprietà Fondamentali

|**Proprietà**|**Dominio del Tempo f(t)**|**Dominio di Laplace F(s)**|
|---|---|---|
|**Linearità**|$\alpha f_1(t) + \beta f_2(t)$|$\alpha F_1(s) + \beta F_2(s)$|
|**Derivazione**|$\dot{f}(t)$|$s F(s) - f(0^-)$|
|**Integrazione**|$\int_{0}^{t} f(\tau)d\tau$|$\frac{1}{s}F(s)$|
|**Traslazione nel tempo**|$f(t-\tau)1(t-\tau)$|$e^{-s\tau} F(s)$|
|**Traslazione complessa**|$e^{at} f(t)$|$F(s-a)$|
|**Moltiplicazione per $t^n$**|$t^n f(t)$|$(-1)^n \frac{d^n}{ds^n}F(s)$|

### 3.2 Trasformate Notevoli

In virtù delle proprietà e ricorrendo alle forme cisoidali di Eulero per il seno e il coseno $\left( \sin(\omega t) = \frac{e^{j\omega t} - e^{-j\omega t}}{2j} \right)$, si può evitare il calcolo integrativo tabulando le principali funzioni:

  

- $\mathcal{L}\{\delta(t)\} = 1$
    
      
    
      
    
- $\mathcal{L}\{1(t)\} = \frac{1}{s}$
    
      
    
      
    
- $\mathcal{L}\{t \cdot 1(t)\} = \frac{1}{s^2}$
    
      
    
      
    
- $\mathcal{L}\left\{\frac{t^n}{n!}1(t)\right\} = \frac{1}{s^{n+1}}$
    
      
    
      
    
- $\mathcal{L}\{\sin(\omega t)\} = \frac{\omega}{s^2+\omega^2}$
    
      
    
      
    
- $\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2+\omega^2}$
    
      
    
      
    

## 4. Antitrasformazione e Metodo dei Fratti Semplici

Il cammino inverso, ovvero l'estrapolazione della $f(t)$ partendo da $F(s)$, seppur definito formalmente tramite integrali di contorno nel piano complesso, è operativamente affrontato riducendo le frazioni complesse a somme elementari. Supponendo di possedere una trasformata razionale $F(s) = \frac{n(s)}{d(s)}$, ci troviamo dinanzi a due diramazioni algoritmiche:

  

1. Se $deg(n(s)) \ge deg(d(s))$: È imperativo eseguire una divisione polinomiale preventiva, scorporando eventuali termini polinomiali secchi (es. costanti o s), i quali nel tempo andranno in antitrasformata impulsiva (delta e relative derivate).
    
      
    
2. Se $deg(n(s)) < deg(d(s))$: Ci si addentra nello **Sviluppo in Fratti Semplici**. Fattorizzando il polinomio a denominatore in radici, $F(s)$ è riscrivibile come somma:
    
      
    
    $$F(s) = \sum_{i=1}^{N_d} \sum_{k=1}^{\mu_i} \frac{A_{ik}}{(s-p_i)^k}$$
    
    dove $p_i$ rappresenta il singolo polo di molteplicità $\mu_i$. Ad ognuno di questi addendi corrisponderà un'antitrasformata immediata proporzionale a $t^{k-1} e^{p_i t}$. Nel caso di radici immaginarie o complesse (presenti in coppie coniugate), queste possono esser congiunte ricostituendo dei fratti con termini di secondo grado (es. $\frac{Cs+D}{(s+\sigma_j)^2+\omega_j^2}$), corrispondenti direttamente a seni o coseni smorzati esponenzialmente.
    
      
    

> [!important] Formula Generale del Calcolo dei Residui Il coefficiente incognito (residuo) $A_{ik}$ riferito ad una certa radice complessa può esser calcolato direttamente per limitazione:
> 
>   
> 
> $$A_{ik} = \lim_{s \to p_i} \frac{1}{(\mu_i-k)!} \frac{d^{\mu_i-k}}{ds^{\mu_i-k}} \left[ (s-p_i)^{\mu_i} F(s) \right]$$

## 5. Teoremi dei Limiti e Stabilità all'Infinito

La preveggenza sui limiti temporali, scavalcando del tutto il gravoso compito di antitrasformare, risiede in due potentissimi teoremi limitistici, a patto di rispettare strettissime condizioni di validità.

  

- **Teorema del Valore Iniziale**: $\lim_{t \to 0^+} f(t) = \lim_{s \to \infty} sF(s)$. Restituisce unicamente il valore assunto dal segnale immediatamente dopo l'istante zero (escludendo logicamente eventuali impulsi). Se i gradi dei polinomi generano impulsi all'infinito, il limite sul residuo dell'antitrasformata non divergente è comunque calcolabile dopo opportuna divisione per scissione dei gradi superiori.
    
      
    
- **Teorema del Valore Finale**: $\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$. Questo calcolo esige a priori l'assicurazione che $\lim_{t \to \infty} f(t)$ fisicamente esista e non oscilli e non diverga verso infinito.
    
      
    

Per assicurare l'usabilità del Valore Finale, si ispeziona analiticamente la struttura radicale di $d(s)$:

  

1. Tutte le radici possiedono parte reale **strettamente negativa** $\rightarrow$ la risposta tenderà a zero nel tempo (Condizione Perfetta per il teorema).
    
      
    
2. Esiste almeno un polo **immaginario puro** (eccetto radici nulle multiple) $\rightarrow$ il sistema genererà risposte sinusoidali oscillanti, per cui il limite di tempo all'infinito per definizione non si stabilizzerà su un valore unico (Teorema non applicabile).
    
      
    
3. Esiste un qualsiasi polo con parte reale **positiva** o radici a parte reale nulla aventi **moltiplicità > 1** $\rightarrow$ la risposta divergerà in ampiezza esponenzialmente o per rampizzazione e il teorema fallirà.
    
      
    

### 5.1 Calcolo dei segni tramite Criteri Algebrici

Senza sviscerare le radici con formule ad alto rango non computabili a mano, si attesta la negatività delle parti reali (e con essa la stabilità di $F(s)$):

  

- **Regola di Cartesio**: per sistemi di ordine basso (grado 2), il numero di radici a parte reale positiva eguaglia le variazioni di segno nei coefficienti del polinomio. A patto ovviamente che non vi siano nullità.
    
      
    
- **Metodo di Routh-Hurwitz**: Impiantando una matrice in cui righe successive vengono formate con somme e sottrazioni normalizzate dei termini, $T(i,j) = -\det \begin{pmatrix} T(i-2, 1) & T(i-2, j+1) \\ T(i-1, 1) & T(i-1, j+1) \end{pmatrix} / T(i-1, 1)$, è possibile decretare l'infalibilità o meno dei segni. Un polinomio possiede tutte radici strettamente a parte reale minore di zero se, e solo se, l'intera prima colonna della tabella costruita reca esiti rigorosamente positivi.
    
      
    

## 6. Risoluzione di Equazioni Differenziali

Una generica equazione differenziale governante un sistema $y^{(n)} + \dots + a_0 y = b_m u^{(m)} + \dots + b_0 u$ è prontamente trasportabile nel dominio di Laplace sfruttando la regola di derivazione (in cui entra in gioco la memoria $f(0^-)$). L'equazione algebrica prodotta viene quindi scomposta come:

  

$$Y(s) = \frac{b_m s^m + \dots + b_0}{s^n + a_{n-1} s^{n-1} + \dots + a_0}U(s) + \frac{I^y(\dots) - I^u(\dots)}{s^n + \dots + a_0}$$

Tale approccio separa magnificamente due macro-contributi della teoria sistemistica:

  

1. **Risposta a Ingresso Nullo $y_{oa}$**: È il segmento dell'antitrasformata derivato unicamente dalla perturbazione delle condizioni iniziali del sistema ($I^y, I^u$). Identifica sostanzialmente l'evoluzione autogena che il sistema (omogenea associata) produrrebbe senza spinte esogene.
    
      
    
2. **Risposta a Stato Zero $y_{sz}$**: È il risultato esclusivo del controllo immesso con i componenti forzanti esterni, assumendo partenze dallo stato inerziale zero. La porzione a moltiplicare il segnale d'ingresso viene riconosciuta universalmente come la **Funzione di Trasferimento** $T(s)$ del sistema studiato.