
```
---
lezione: 2
data: 2026-09-25
argomenti: [Funzioni a valori vettoriali, Grafico e Immagine, Derivate parziali, Derivate direzionali, Differenziabilità, Gradiente]
---
```


# Metodi Matematici per l'Ingegneria: Lezione 2

## 1. Funzioni di Più Variabili: Dominio e Immagine

L'estensione dei concetti dell'analisi matematica a spazi multidimensionali richiede di studiare funzioni che operano su vettori e restituiscono vettori. Formalmente, si definisce una funzione a valori vettoriali di più variabili reali come un'applicazione:

  

$$f: D \subseteq \mathbb{R}^n \to \mathbb{R}^m$$

  

dove $D$ rappresenta il dominio della funzione, ovvero un sottoinsieme dello spazio $\mathbb{R}^n$ su cui la funzione è ben definita. Tale funzione associa ad ogni elemento $\mathbf{x} = (x_1, \dots, x_n) \in D$ un unico elemento $\mathbf{y} \in \mathbb{R}^m$.

  

L'**immagine** della funzione, indicata con $f(D)$, è il sottoinsieme del codominio $\mathbb{R}^m$ costituito da tutti e soli i vettori che sono "raggiunti" dalla funzione, ossia:

  

$$f(D) = \{ \mathbf{y} \in \mathbb{R}^m \mid \exists \mathbf{x} \in D : f(\mathbf{x}) = \mathbf{y} \}$$

.

  

Poiché il risultato dell'applicazione $f(\mathbf{x})$ è un vettore in $\mathbb{R}^m$, la funzione vettoriale $f$ può essere disaccoppiata e interpretata come una collezione di $m$ funzioni a valori scalari:

  

$$f(\mathbf{x}) = \big( f_1(\mathbf{x}), f_2(\mathbf{x}), \dots, f_m(\mathbf{x}) \big)$$

. In questa scrittura, ogni componente $f_i$ è una funzione scalare $f_i: D \subseteq \mathbb{R}^n \to \mathbb{R}$. L'analisi delle proprietà globali del campo vettoriale $f$ si riconduce molto spesso allo studio delle proprietà delle sue singole componenti scalari $f_i$.

  

## 2. Rappresentazione Grafica e Campi Vettoriali

Il **grafico** di una funzione $f$ contiene informazioni combinate sia del dominio che dell'immagine. Matematicamente, è definito come un sottoinsieme dello spazio prodotto $\mathbb{R}^{n+m}$:

  

$$\mathcal{G} = \{ (\mathbf{x}, f(\mathbf{x})) \in \mathbb{R}^{n+m} \mid \mathbf{x} \in D \}$$

.

  

La rappresentazione visiva diretta di tale grafico è fisicamente possibile solo se la dimensione totale dello spazio, $n+m$, è minore o uguale a 3. Esistono diverse casistiche fondamentali:

  

- **$n=1, m=1$:** È il caso classico dell'Analisi 1, in cui si studiano funzioni $f(x)$ rappresentabili nel piano cartesiano $\mathbb{R}^2$.
    
      
    
- **$n=2, m=1$:** Si tratta di funzioni a valori scalari $f(x_1, x_2)$ (es. distribuzioni di temperatura su una piastra). Il grafico è una superficie (un "lenzuolo") che vive nello spazio tridimensionale $\mathbb{R}^3$.
    
      
    
- **$n=1, m=2$:** Rappresenta curve parametriche nel piano. Ad esempio, la funzione $f(t) = (t^2, \sin(t))$ associa a un parametro reale (il "tempo" $t$) un punto nel piano. In questo scenario, invece di tracciare il grafico tridimensionale astratto, è consuetudine visualizzare unicamente l'immagine $f(D)$ in $\mathbb{R}^2$, perdendo l'esplicita dipendenza temporale ma evidenziando la traiettoria percorsa.
    
      
    
- **$n=2, m=2$ (Campi Vettoriali):** Impossibili da rappresentare come grafico (richiederebbero 4 dimensioni). Si utilizza quindi una rappresentazione che enfatizza il dominio: per ogni punto $\mathbf{x} \in D \subset \mathbb{R}^2$, si disegna una freccia che rappresenta in modulo, direzione e verso il vettore restituito dalla funzione.
    
      
    

> [!example] Campo Vettoriale 
> Si consideri la funzione $f(x_1, x_2) = (-x_2, x_1)$. Questa mappa prende un punto nel piano e gli associa un vettore ruotato di 90 gradi rispetto al vettore posizione originale. Disegnando questo campo, si ottiene un pattern di frecce circolari attorno all'origine, tipico della rappresentazione di moti di fluidi o atmosfere.
> 
>   

## 3. Calcolo Differenziale: Derivate Parziali e Direzionali

Per superare i limiti della visualizzazione globale di funzioni complesse, si studia il loro comportamento locale linearizzandole. Fissiamo l'attenzione su funzioni a valori scalari $f: D \subset \mathbb{R}^n \to \mathbb{R}$ e consideriamo un punto $\hat{\mathbf{x}}$ strettamente **interno** al dominio $D$, così da garantire l'esistenza di un intorno sferico completamente contenuto in $D$.

  

### 3.1 Derivate Parziali

La derivata parziale valuta il tasso di variazione della funzione quando ci si muove parallelamente a uno degli assi coordinati, mantenendo costanti tutte le altre variabili. La derivata parziale rispetto alla $k$-esima variabile nel punto $\hat{\mathbf{x}}$ è definita tramite il limite del rapporto incrementale:

  

$$\frac{\partial f}{\partial x_k}(\hat{\mathbf{x}}) = \lim_{h \to 0} \frac{f(\hat{x}_1, \dots, \hat{x}_k + h, \dots, \hat{x}_n) - f(\hat{\mathbf{x}})}{h}$$

. Esistono diverse notazioni equivalenti per indicare lo stesso operatore: $\frac{\partial f}{\partial x_k}(\hat{\mathbf{x}})$, $\partial_k f(\hat{\mathbf{x}})$, oppure $D_{x_k}f(\hat{\mathbf{x}})$.

  

Geometricamente (nel caso $n=2$), calcolare la derivata parziale significa intersecare il grafico della superficie con un piano parallelo all'asse di interesse e valutare la pendenza della retta tangente alla curva risultante nell'intersezione.

  

> [!example] Calcolo di derivate parziali Sia $f: \mathbb{R}^2 \to \mathbb{R}$ definita come $f(x,y) = y e^{xy}$. Derivando rispetto a $x$ (trattando $y$ come costante):
> 
>   
> 
> $$\frac{\partial f}{\partial x} = y \cdot (y e^{xy}) = y^2 e^{xy}$$
> 
> . Derivando rispetto a $y$ (trattando $x$ come costante e applicando la regola del prodotto):
> 
>   
> 
> $$\frac{\partial f}{\partial y} = 1 \cdot e^{xy} + y \cdot (x e^{xy}) = e^{xy}(1 + xy)$$
> 
> .
> 
>   

### 3.2 Derivate Direzionali

Limitarsi alle sole direzioni degli assi coordinati è restrittivo. È possibile calcolare il tasso di variazione di $f$ lungo una qualsiasi direzione individuata da un vettore $\mathbf{v} \neq \mathbf{0}$. Si costruisce una retta passante per $\hat{\mathbf{x}}$ parametrizzata come $\mathbf{x}(t) = \hat{\mathbf{x}} + t\mathbf{v}$ e si valuta la funzione lungo questa restrizione. La **derivata direzionale** di $f$ nella direzione $\mathbf{v}$ si definisce come:

  

$$\frac{\partial f}{\partial \mathbf{v}}(\hat{\mathbf{x}}) = \lim_{t \to 0} \frac{f(\hat{\mathbf{x}} + t\mathbf{v}) - f(\hat{\mathbf{x}})}{t}$$

.

  

È immediato notare che le derivate parziali non sono altro che casi particolari di derivate direzionali in cui il vettore direzione coincide con i versori della base canonica $\mathbf{e}_k$.

  

Una proprietà fondamentale delle derivate direzionali è la loro omogeneità rispetto al vettore direzione. Se si modula (allunga o accorcia) il vettore $\mathbf{v}$ di un fattore $\lambda \neq 0$, ponendo $\mathbf{u} = \lambda \mathbf{v}$, la derivata direzionale scala proporzionalmente:

  

$$\frac{\partial f}{\partial \mathbf{u}}(\hat{\mathbf{x}}) = \lim_{t \to 0} \frac{f(\hat{\mathbf{x}} + t\lambda\mathbf{v}) - f(\hat{\mathbf{x}})}{t}$$

. Effettuando la sostituzione $h = t\lambda$ (e moltiplicando/dividendo per $\lambda$), si ottiene:

  

$$\lim_{h \to 0} \left( \frac{f(\hat{\mathbf{x}} + h\mathbf{v}) - f(\hat{\mathbf{x}})}{h / \lambda} \right) = \lambda \lim_{h \to 0} \frac{f(\hat{\mathbf{x}} + h\mathbf{v}) - f(\hat{\mathbf{x}})}{h} = \lambda \frac{\partial f}{\partial \mathbf{v}}(\hat{\mathbf{x}})$$

.

  

## 4. Differenziabilità

In una dimensione, l'esistenza della derivata garantisce la continuità della funzione e l'esistenza di una retta tangente ben definita. In più variabili, il semplice possesso di tutte le derivate parziali (e persino direzionali) in un punto non è sufficiente per garantire che la funzione sia ben approssimabile da un iperpiano tangente, né tantomeno ne assicura la continuità.

  

> [!tip] #approfondimento Relazione tra derivabilità e continuità 
> A differenza di quanto avviene in $\mathbb{R}$, in $\mathbb{R}^n$ l'esistenza delle derivate parziali in un punto non implica la continuità della funzione in quel punto. Ad esempio, la funzione $f(x,y) = \frac{xy}{x^2+y^2}$ per $(x,y) \neq (0,0)$ e $f(0,0)=0$, ha derivate parziali nulle nell'origine, ma non è continua, poiché avvicinandosi all'origine lungo la bisettrice $y=x$ il limite vale $1/2 \neq 0$. Serve un concetto di regolarità più "forte".
> 
>   

Il concetto corretto che generalizza l'approssimazione lineare è la **differenziabilità**. Ricordando che in Analisi 1 l'espansione di Taylor al primo ordine è $g(x+h) - g(x) = g'(x)h + o(\vert{}h\vert{})$, cerchiamo un'espansione analoga per $\mathbb{R}^n$.

  

**Definizione:** Una funzione $f: D \subset \mathbb{R}^n \to \mathbb{R}$ si dice differenziabile in un punto interno $\hat{\mathbf{x}}$ se esiste un'applicazione lineare $\phi: \mathbb{R}^n \to \mathbb{R}$ tale per cui, per un incremento $\mathbf{h}$ sufficientemente piccolo, valga:

  

$$f(\hat{\mathbf{x}} + \mathbf{h}) - f(\hat{\mathbf{x}}) = \phi(\mathbf{h}) + o(\Vert{}\mathbf{h}\Vert{})$$

. Il termine "o piccolo" di $\Vert{}\mathbf{h}\Vert{}$ indica una quantità che tende a zero più velocemente dell'incremento stesso, ovvero:

  

$$\lim_{\mathbf{h} \to \mathbf{0}} \frac{o(\Vert{}\mathbf{h}\Vert{})}{\Vert{}\mathbf{h}\Vert{}} = 0$$

.

  

L'applicazione lineare $\phi(\mathbf{h})$ viene chiamata **differenziale** di $f$ in $\hat{\mathbf{x}}$ ed è abitualmente indicata con la notazione $d_{\hat{\mathbf{x}}}f(\mathbf{h})$. Essendo un'applicazione lineare da $\mathbb{R}^n$ a $\mathbb{R}$, può essere sempre rappresentata vettorialmente tramite un prodotto riga per colonna, ossia una combinazione lineare delle componenti dell'incremento $\mathbf{h}$:

  

$$d_{\hat{\mathbf{x}}}f(\mathbf{h}) = \sum_{i=1}^n \alpha_i h_i$$

. L'esistenza del differenziale equivale geometricamente all'esistenza di un (iper)piano tangente al grafico di $f$ nel punto $\hat{\mathbf{x}}$.

  

### 4.1 Teoremi Fondamentali sulla Differenziabilità

L'assunzione di differenziabilità è estremamente potente e ripristina la gerarchia di regolarità attesa:

  

**Teorema 1 (Continuità):** Se $f$ è differenziabile in $\hat{\mathbf{x}}$, allora $f$ è continua in $\hat{\mathbf{x}}$. _Dimostrazione:_ Dalla definizione di differenziabilità, valutando il limite per $\mathbf{h} \to \mathbf{0}$ dell'incremento della funzione si ha:

  

$$\lim_{\mathbf{h} \to \mathbf{0}} [f(\hat{\mathbf{x}} + \mathbf{h}) - f(\hat{\mathbf{x}})] = \lim_{\mathbf{h} \to \mathbf{0}} \Big( d_{\hat{\mathbf{x}}}f(\mathbf{h}) + o(\Vert{}\mathbf{h}\Vert{}) \Big)$$

. Essendo $d_{\hat{\mathbf{x}}}f$ un'applicazione lineare, $d_{\hat{\mathbf{x}}}f(\mathbf{0}) = 0$. Inoltre, il termine $o(\Vert{}\mathbf{h}\Vert{})$ tende a zero per costruzione. Pertanto il limite complessivo è zero, il che prova che $\lim_{\mathbf{x} \to \hat{\mathbf{x}}} f(\mathbf{x}) = f(\hat{\mathbf{x}})$, dimostrando la continuità.

  

**Teorema 2 (Esistenza delle Derivate e Gradiente):** Se $f$ è differenziabile in $\hat{\mathbf{x}}$, allora ammette derivata in ogni direzione $\mathbf{v} \neq \mathbf{0}$, e vale l'identità:

  

$$\frac{\partial f}{\partial \mathbf{v}}(\hat{\mathbf{x}}) = d_{\hat{\mathbf{x}}}f(\mathbf{v})$$

. _Dimostrazione:_ Riscriviamo la definizione di differenziabilità scegliendo come incremento $\mathbf{h} = t\mathbf{v}$:

  

$$f(\hat{\mathbf{x}} + t\mathbf{v}) - f(\hat{\mathbf{x}}) = d_{\hat{\mathbf{x}}}f(t\mathbf{v}) + o(\Vert{}t\mathbf{v}\Vert{})$$

. Per la linearità del differenziale, $d_{\hat{\mathbf{x}}}f(t\mathbf{v}) = t \, d_{\hat{\mathbf{x}}}f(\mathbf{v})$. Dividendo tutto per $t$ e calcolando il limite per $t \to 0$:

  

$$\lim_{t \to 0} \frac{f(\hat{\mathbf{x}} + t\mathbf{v}) - f(\hat{\mathbf{x}})}{t} = d_{\hat{\mathbf{x}}}f(\mathbf{v}) + \lim_{t \to 0} \frac{o(\vert{}t\vert{}\Vert{}\mathbf{v}\Vert{})}{t}$$

. Poiché il secondo addendo a destra si annulla, il limite esiste e coincide esattamente con il differenziale valutato nel vettore $\mathbf{v}$.

  

Snippet di codice

```
graph TD
    A[Differenziabilità] -->|Implica| B(Continuità)
    A -->|Implica| C(Esistenza derivate direzionali)
    C -->|Implica| D(Esistenza derivate parziali)
    D -.->|NON implica| B
    D -.->|NON implica| A
```

## 5. Il Gradiente

Dal Teorema 2 discende una conseguenza vitale. Se scegliamo come direzione i vettori della base canonica $\mathbf{e}_k$, scopriamo che l'azione del differenziale su $\mathbf{e}_k$ restituisce esattamente la derivata parziale rispetto a $x_k$:

  

$$d_{\hat{\mathbf{x}}}f(\mathbf{e}_k) = \frac{\partial f}{\partial x_k}(\hat{\mathbf{x}})$$

.

  

Viene così introdotto un nuovo operatore vettoriale, il **Gradiente**, denotato con $\nabla f(\hat{\mathbf{x}})$, definito come il vettore avente per componenti le derivate parziali di $f$ calcolate in $\hat{\mathbf{x}}$:

  

$$\nabla f(\hat{\mathbf{x}}) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right)$$

.

  

Grazie al gradiente, la forma astratta del differenziale $d_{\hat{\mathbf{x}}}f(\mathbf{h}) = \sum_{i=1}^n \alpha_i h_i$ assume una veste estremamente concreta. I coefficienti $\alpha_i$ sono proprio le derivate parziali, e il differenziale calcolato per un incremento $\mathbf{h}$ si riduce al prodotto scalare tra il gradiente della funzione e il vettore incremento:

  

$$d_{\hat{\mathbf{x}}}f(\mathbf{h}) = \nabla f(\hat{\mathbf{x}}) \cdot \mathbf{h}$$

.