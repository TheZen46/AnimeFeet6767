
```
---
lezione: 1
data: 2026-09-21
argomenti: [introduzione, funzioni a più variabili, spazio Rn, norma, prodotto scalare, topologia, limiti, continuità]
---
```

# Introduzione al Corso

Il corso di Metodi Matematici per l'Ingegneria è strutturato per approfondire strumenti matematici avanzati, fondamentali per l'analisi dei segnali e per la fisica matematica. Il programma si articola in quattro aree tematiche principali:

  

1. **Calcolo differenziale per funzioni di più variabili**: estensione dei concetti di derivata per funzioni definite su domini multidimensionali.
    
      
    
2. **Integrazione di funzioni di più variabili**: calcolo di aree, volumi, lunghezze di curve e flussi attraverso superfici nello spazio, con l'introduzione dei teoremi della divergenza e del rotore (fondamentali per le equazioni di Maxwell).
    
      
    
3. **Serie di Fourier**: studio della convergenza delle serie e della loro applicazione nell'approssimazione e ricostruzione dei segnali.
    
      
    
4. **Funzioni di variabile complessa**: tecniche di integrazione nel piano complesso, utili per risolvere integrali reali altrimenti non calcolabili con le tecniche dell'Analisi 1 (ad esempio la trasformata della _sinc function_).
    
      
    

L'esame consiste nella risoluzione di un esercizio alla lavagna, seguita dalla discussione teorica dello stesso e da domande di teoria, per una durata complessiva di circa 40-45 minuti per candidato.

  

# Funzioni di Più Variabili Reali

L'oggetto di studio principale di questa prima parte del corso sono le funzioni che operano su insiemi a più dimensioni. Formalmente, studiamo applicazioni del tipo:

  

$$f: D \subseteq \mathbb{R}^n \to \mathbb{R}^m$$

dove $D$ rappresenta il dominio della funzione, ovvero l'insieme dei punti in cui la funzione è definita. A ogni elemento $\vec{x} \in D$, la funzione assegna uno e un solo elemento $\vec{y} \in \mathbb{R}^m$.

  

L'immagine della funzione, indicata con $f(D)$, è l'insieme di tutti i punti $\vec{y} \in \mathbb{R}^m$ che sono "raggiunti" dalla funzione a partire da un punto del dominio. Quando l'insieme di arrivo ha dimensione $m > 1$, la funzione a valori vettoriali può essere vista come una collezione di $m$ funzioni a valori reali, dette **componenti** della funzione. Possiamo quindi scrivere:

  

$$f(\vec{x}) = \Big( f_1(\vec{x}), f_2(\vec{x}), \dots, f_m(\vec{x}) \Big)$$

dove ogni $f_i : D \subseteq \mathbb{R}^n \to \mathbb{R}$. Questa scomposizione è estremamente utile, poiché studiare una funzione a valori vettoriali si riduce spesso allo studio delle singole funzioni scalari che la compongono.

  

Applicazioni fisiche tipiche includono la temperatura in una stanza (funzione scalare da $\mathbb{R}^3 \to \mathbb{R}$), il campo di velocità dell'aria o i campi elettromagnetici (funzioni vettoriali da $\mathbb{R}^3 \to \mathbb{R}^3$).

  

## Lo Spazio Vettoriale $\mathbb{R}^n$

Per poter manipolare queste funzioni, è essenziale definire la struttura dello spazio in cui operano. L'insieme $\mathbb{R}^n$ è lo spazio formato da tutte le $n$-uple ordinate di numeri reali. Un elemento generico $\vec{x} \in \mathbb{R}^n$ è descritto dalle sue componenti:

  

$$\vec{x} = (x_1, x_2, \dots, x_n)$$

con $x_i \in \mathbb{R}$ per ogni $i$.

  

> [!tip] Notazione Durante il corso, un vettore di $\mathbb{R}^n$ potrà essere indicato con diverse notazioni equivalenti: $\vec{x}$, $\underline{x}$, oppure in grassetto $\mathbf{x}$. Le componenti possono essere scritte in riga o in colonna tramite la notazione matriciale.
> 
>   

L'insieme $\mathbb{R}^n$ è uno spazio vettoriale di dimensione $n$. Dati due vettori $\vec{x}, \vec{y} \in \mathbb{R}^n$ e due scalari $\lambda_1, \lambda_2 \in \mathbb{R}$, è possibile definire la combinazione lineare, che restituisce a sua volta un elemento di $\mathbb{R}^n$:

  

$$\lambda_1 \vec{x} + \lambda_2 \vec{y} = (\lambda_1 x_1 + \lambda_2 y_1, \dots, \lambda_1 x_n + \lambda_2 y_n)$$

.

  

Una base naturale (o canonica) per questo spazio è l'insieme di vettori $\{\vec{e}_i\}_{i=1,\dots,n}$, dove il vettore $\vec{e}_i$ ha la componente $i$-esima pari a $1$ e tutte le altre nulle. Sfruttando questa base, ogni vettore $\vec{x}$ può essere scritto in modo compatto come:

  

$$\vec{x} = \sum_{i=1}^n x_i \vec{e}_i$$

.

  

### Norma e Distanza

Per quantificare la "lunghezza" di un vettore in $\mathbb{R}^n$, si introduce il concetto di **norma** (o modulo), che generalizza il teorema di Pitagora a $n$ dimensioni.

  

> [!important] Definizione di Norma
> 
> La norma di un vettore $\vec{x} \in \mathbb{R}^n$ è definita come:
> 
>   
> 
> $$\vert{}\vert{}\vec{x}\vert{}\vert{} := \sqrt{x_1^2 + x_2^2 + \dots + x_n^2} = \sqrt{\sum_{i=1}^n x_i^2}$$
> 
> .
> 
>   

La norma gode di tre proprietà fondamentali:

  

1. **Positività**: $\vert{}\vert{}\vec{x}\vert{}\vert{} \ge 0$ e $\vert{}\vert{}\vec{x}\vert{}\vert{} = 0$ se e solo se $\vec{x} = \vec{0}$.
    
      
    
2. **Omogeneità**: $\vert{}\vert{}\lambda \vec{x}\vert{}\vert{} = \vert{}\lambda\vert{} \vert{}\vert{}\vec{x}\vert{}\vert{}$ per ogni $\lambda \in \mathbb{R}$.
    
      
    
3. **Disuguaglianza triangolare**: $\vert{}\vert{}\vec{x} + \vec{y}\vert{}\vert{} \le \vert{}\vert{}\vec{x}\vert{}\vert{} + \vert{}\vert{}\vec{y}\vert{}\vert{}$.
    
      
    

Dalla norma deriva naturalmente il concetto di **distanza** tra due punti $\vec{x}$ e $\vec{y}$ nello spazio $\mathbb{R}^n$, definita come la norma del vettore differenza:

  

$$d(\vec{x}, \vec{y}) = \vert{}\vert{}\vec{x} - \vec{y}\vert{}\vert{}$$

. La distanza eredita le proprietà della norma, risultando positiva, simmetrica ($d(\vec{x}, \vec{y}) = d(\vec{y}, \vec{x})$) e soddisfacendo anch'essa la disuguaglianza triangolare: $d(\vec{x}, \vec{y}) \le d(\vec{x}, \vec{z}) + d(\vec{z}, \vec{y})$.

  

### Prodotto Scalare e Disuguaglianza di Cauchy-Schwarz

Il **prodotto scalare** è un'operazione che prende in input due vettori e restituisce un numero reale. In $\mathbb{R}^n$, il prodotto scalare standard tra $\vec{x}$ e $\vec{y}$ è definito come la somma dei prodotti componente per componente:

  

$$\vec{x} \cdot \vec{y} = \sum_{i=1}^n x_i y_i$$

.

  

Le proprietà principali del prodotto scalare sono:

  

- **Bilinearità**: è lineare rispetto a entrambe le entrate (es. $(\alpha_1 \vec{x}_1 + \alpha_2 \vec{x}_2) \cdot \vec{y} = \alpha_1 (\vec{x}_1 \cdot \vec{y}) + \alpha_2 (\vec{x}_2 \cdot \vec{y})$).
    
      
    
- **Simmetria**: $\vec{x} \cdot \vec{y} = \vec{y} \cdot \vec{x}$.
    
      
    
- **Definito positivo**: $\vec{x} \cdot \vec{x} = \vert{}\vert{}\vec{x}\vert{}\vert{}^2 \ge 0$, e l'uguaglianza a zero vale solo se $\vec{x} = \vec{0}$.
    
      
    

Dal prodotto scalare e dalla norma discende una delle disuguaglianze più importanti dell'analisi: la disuguaglianza di Cauchy-Schwarz.

  

> [!important] Disuguaglianza di Cauchy-Schwarz
> 
> Per ogni coppia di vettori $\vec{x}, \vec{y} \in \mathbb{R}^n$, il modulo del loro prodotto scalare è sempre minore o uguale al prodotto delle loro norme:
> 
>   
> 
> $$\vert{}\vec{x} \cdot \vec{y}\vert{} \le \vert{}\vert{}\vec{x}\vert{}\vert{} \vert{}\vert{}\vec{y}\vert{}\vert{}$$
> 
> .
> 
>   

**Dimostrazione:** Se $\vec{x} = \vec{0}$ oppure $\vec{y} = \vec{0}$, la disuguaglianza è banalmente verificata come $0 \le 0$. Supponiamo quindi che i vettori siano non nulli. Sfruttando la proprietà di positività della norma, costruiamo una forma quadratica basata su un parametro reale $\lambda$:

  

$$\vert{}\vert{}\vec{x} + \lambda \vec{y}\vert{}\vert{}^2 \ge 0 \quad \forall \lambda \in \mathbb{R}$$

Espandendo il quadrato del binomio vettoriale tramite il prodotto scalare e la sua bilinearità, otteniamo:

  

$$(\vec{x} + \lambda \vec{y}) \cdot (\vec{x} + \lambda \vec{y}) = \vec{x} \cdot \vec{x} + 2\lambda (\vec{x} \cdot \vec{y}) + \lambda^2 (\vec{y} \cdot \vec{y}) \ge 0$$

$$\vert{}\vert{}\vec{x}\vert{}\vert{}^2 + 2\lambda (\vec{x} \cdot \vec{y}) + \lambda^2 \vert{}\vert{}\vec{y}\vert{}\vert{}^2 \ge 0$$

. Abbiamo ottenuto un polinomio di secondo grado nella variabile $\lambda$ che, rappresentando una parabola rivolta verso l'alto (poiché $\vert{}\vert{}\vec{y}\vert{}\vert{}^2 > 0$), deve essere sempre maggiore o uguale a zero. Affinché un polinomio di secondo grado non assuma mai valori negativi, il suo discriminante $\Delta$ (o $\Delta/4$) deve essere minore o uguale a zero. Calcolando il discriminante ridotto $\frac{\Delta}{4}$ rispetto al parametro $\lambda$:

  

$$\frac{\Delta}{4} = (\vec{x} \cdot \vec{y})^2 - \vert{}\vert{}\vec{x}\vert{}\vert{}^2 \vert{}\vert{}\vec{y}\vert{}\vert{}^2 \le 0$$

Da cui si ricava immediatamente:

  

$$(\vec{x} \cdot \vec{y})^2 \le \vert{}\vert{}\vec{x}\vert{}\vert{}^2 \vert{}\vert{}\vec{y}\vert{}\vert{}^2$$

Estraendo la radice quadrata si ottiene l'asserto finale: $\vert{}\vec{x} \cdot \vec{y}\vert{} \le \vert{}\vert{}\vec{x}\vert{}\vert{} \vert{}\vert{}\vec{y}\vert{}\vert{}$.

  

# Elementi di Topologia in $\mathbb{R}^n$

Per poter parlare di limiti e continuità in più dimensioni, è necessario definire la struttura topologica dello spazio, ovvero come misuriamo la "vicinanza" tra i punti e come classifichiamo i sottoinsiemi di $\mathbb{R}^n$.

  

Il concetto fondamentale per definire la vicinanza è l'**intorno sferico** (o palla aperta).

  

> [!important] Intorno Sferico
> 
> Un intorno sferico di centro $\vec{x} \in \mathbb{R}^n$ e raggio $r > 0$ è l'insieme di tutti i punti $\vec{y}$ la cui distanza da $\vec{x}$ è strettamente minore di $r$:
> 
>   
> 
> $$B(\vec{x}, r) = \{ \vec{y} \in \mathbb{R}^n \mid \vert{}\vert{}\vec{x} - \vec{y}\vert{}\vert{} < r \}$$
> 
> .
> 
>   

Da notare che la frontiera della sfera (la "buccia") non è inclusa nell'intorno aperto. Se includessimo la disuguaglianza $\le$, otterremmo un intorno sferico chiuso, indicato solitamente con $\overline{B(\vec{x}, r)}$.

  

Un punto cruciale per la definizione formale di limite è la nozione di accumulazione, che indica se un punto è "circondato" da elementi di un certo insieme.

  

> [!important] Punto di Accumulazione Sia $A \subset \mathbb{R}^n$. Un punto $\vec{x} \in \mathbb{R}^n$ è detto punto di accumulazione per $A$ se ogni intorno sferico di $\vec{x}$, indipendentemente da quanto sia piccolo il raggio $r > 0$, contiene almeno un punto di $A$ diverso da $\vec{x}$ stesso. Formalmente, per ogni $r > 0$:
> 
>   
> 
> $$\Big( B(\vec{x}, r) \setminus \{\vec{x}\} \Big) \cap A \neq \emptyset$$
> 
> . Non è necessario che il punto di accumulazione appartenga all'insieme $A$: ad esempio, i punti sul bordo di un dominio aperto non vi appartengono, ma sono punti di accumulazione per esso.
> 
>   

Attraverso gli intorni sferici possiamo definire le principali caratteristiche topologiche di un insieme $A \subset \mathbb{R}^n$:

  

- **Insieme Limitato**: $A$ è limitato se esiste un raggio sufficientemente grande $M > 0$ tale che l'insieme possa essere interamente contenuto all'interno di un intorno sferico centrato nell'origine, ovvero $A \subset B(\vec{0}, M)$.
    
      
    
- **Insieme Aperto**: $A$ è aperto se, per ogni suo punto $\vec{x} \in A$, è possibile trovare un intorno sferico centrato in $\vec{x}$ (con $r>0$) che sia interamente contenuto in $A$. In pratica, non comprende il proprio bordo.
    
      
    
- **Insieme Chiuso**: $A$ è chiuso se il suo complementare, $\mathbb{R}^n \setminus A$, è un insieme aperto. In pratica, un insieme chiuso contiene sempre tutto il suo bordo.
    
      
    
- **Insieme Compatto**: $A$ è detto compatto se è simultaneamente **chiuso** e **limitato**. Gli insiemi compatti hanno proprietà molto forti in analisi, come garantire l'esistenza di massimi e minimi per le funzioni continue (Teorema di Weierstrass).
    
      
    

# Limiti e Continuità in Più Variabili

Avendo stabilito cos'è un punto di accumulazione e come calcolare le distanze, è possibile formalizzare il concetto di limite. Quando valutiamo un limite in più variabili per $\vec{x} \to \hat{x}$, ci stiamo domandando se la funzione $F(\vec{x})$ si avvicina stabilmente a un certo valore $\vec{l}$ mano a mano che $\vec{x}$ si stringe in un intorno sferico del punto di accumulazione $\hat{x}$, indipendentemente dalla direzione o dalla traiettoria di avvicinamento.

  

> [!important] Definizione di Limite
> 
> Sia $F: A \subset \mathbb{R}^n \to \mathbb{R}^m$ e sia $\hat{x}$ un punto di accumulazione per $A$. Si dice che $\vec{l}$ è il limite di $F$ per $\vec{x}$ che tende a $\hat{x}$:
> 
>   
> 
> $$\lim_{\vec{x} \to \hat{x}} F(\vec{x}) = \vec{l}$$
> 
> se, per ogni $\epsilon > 0$, esiste un $\delta_\epsilon > 0$ tale che, per ogni $\vec{x} \in A$ con $0 < \vert{}\vert{}\vec{x} - \hat{x}\vert{}\vert{} < \delta_\epsilon$, risulta:
> 
>   
> 
> $$\vert{}\vert{}F(\vec{x}) - \vec{l}\vert{}\vert{} < \epsilon$$
> 
> .
> 
>   

Se $\hat{x}$ è un punto non solo di accumulazione ma che appartiene al dominio della funzione, possiamo valutare la continuità della funzione in quel punto.

  

> [!important] Definizione di Continuità
> 
> Una funzione $F$ si dice continua nel punto $\hat{x} \in D$ se il limite della funzione per $\vec{x} \to \hat{x}$ esiste e coincide col valore che la funzione assume nel punto:
> 
>   
> 
> $$\lim_{\vec{x} \to \hat{x}} F(\vec{x}) = F(\hat{x})$$
> 
> . Se questa proprietà vale per tutti i punti del dominio, la funzione è detta continua nel dominio.
> 
>   

> [!example] Esercizio: Verifica di un limite in più variabili Calcolare e verificare formalmente, tramite le restrizioni o la definizione $\epsilon-\delta$, il seguente limite:
> 
>   
> 
> $$\lim_{(x,y,z) \to (0,0,0)} \frac{xyz^3}{x^4+y^4+z^4}$$
> 
> **Svolgimento:** Definiamo la funzione $\tilde{f}: \mathbb{R}^3 \setminus \{(0,0,0)\} \to \mathbb{R}$. Il valore del limite è $0$. Per dimostrarlo, passiamo a coordinate sferiche generalizzate, esprimendo il vettore generico $\vec{x} = (x,y,z)$ come un versore moltiplicato per il suo modulo. Poniamo $\vec{x} = t\vec{v}$, dove $\vec{v} = (a,b,c)$ è un vettore di modulo unitario (quindi $\vert{}\vert{}\vec{v}\vert{}\vert{}^2 = a^2+b^2+c^2 = 1$) e $t = \vert{}\vert{}\vec{x}\vert{}\vert{}$ è la distanza dall'origine (con $t > 0$). Sostituiamo le componenti $(ta, tb, tc)$ nella funzione:
> 
>   
> 
> $$\tilde{f}(t\vec{v}) = \frac{(ta)(tb)(tc)^3}{(ta)^4 + (tb)^4 + (tc)^4} = \frac{t^5 \cdot a b c^3}{t^4(a^4 + b^4 + c^4)} = t \frac{a b c^3}{a^4 + b^4 + c^4}$$
> 
> . Osserviamo il termine frazionario rimanente, dipendente solo dal versore $\vec{v}$. Poiché il versore $\vec{v}$ appartiene alla sfera unitaria (che è un insieme compatto, cioè chiuso e limitato), la funzione $g(a,b,c) = \frac{a b c^3}{a^4 + b^4 + c^4}$ ammette un massimo assoluto per il Teorema di Weierstrass. Esiste quindi una costante positiva $C$ tale che:
> 
>   
> 
> $$\left\vert{} \frac{a b c^3}{a^4 + b^4 + c^4} \right\vert{} \le C \quad \forall (a,b,c) \text{ con } \vert{}\vert{}(a,b,c)\vert{}\vert{}=1$$
> 
> . Un possibile candidato per questa costante, stimandolo grossolanamente, è ad esempio $C=5$. Di conseguenza, possiamo maggiorare il modulo della funzione:
> 
>   
> 
> $$\vert{}\vert{}\tilde{f}(\vec{x})\vert{}\vert{} = \left\vert{} t \frac{a b c^3}{a^4 + b^4 + c^4} \right\vert{} \le C \cdot t = C \vert{}\vert{}\vec{x}\vert{}\vert{}$$
> 
> . Ritorniamo ora alla definizione formale di limite: vogliamo che $\vert{}\vert{}\tilde{f}(\vec{x}) - 0\vert{}\vert{} < \epsilon$. Dalla disuguaglianza precedente, affinché ciò sia vero, basta imporre che $C \vert{}\vert{}\vec{x}\vert{}\vert{} < \epsilon$, ovvero $\vert{}\vert{}\vec{x}\vert{}\vert{} < \frac{\epsilon}{C}$. Fissato $\epsilon > 0$, è sufficiente scegliere $\delta_\epsilon = \frac{\epsilon}{C}$. In questo modo, per ogni $0 < \vert{}\vert{}\vec{x} - \vec{0}\vert{}\vert{} < \delta_\epsilon$, risulta verificato che $\vert{}\vert{}\tilde{f}(\vec{x})\vert{}\vert{} < \epsilon$, dimostrando rigorosamente che il limite è $0$.

