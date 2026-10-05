

```
---
lezione: 2
data: 2026-09-25
argomenti: [campo elettrico, linee di campo, dipolo elettrico, principio di sovrapposizione, esercizi elettrostatica]
---
```

# Il Campo Elettrico

Sebbene l'elettrostatica possa essere interamente descritta quantitativamente tramite la legge di Coulomb, calcolando le interazioni a distanza tra cariche puntiformi, questa descrizione basata sulle forze dirette risulta spesso complessa e inefficace per sistemi articolati. Un approccio fisicamente più potente consiste nell'introdurre il concetto di campo.

  

Invece di considerare l'interazione diretta tra due cariche specifiche e note (es. $q_1$ e $q_2$), si ipotizza che una distribuzione di cariche modifichi lo spazio circostante generando un "campo elettrico". Per esplorare le proprietà di questo campo, si utilizza una carica fittizia molto piccola, detta "carica di prova" ($q_0$). Posizionando $q_0$ in un punto dello spazio, si osserva la forza ad essa applicata.

  

> [!important] Definizione di Campo Elettrico
> 
> Il campo elettrico $\vec{E}$ in un punto dello spazio è definito come il rapporto tra la forza elettrostatica $\vec{F}$ misurata in quel punto e la carica di prova $q_0$ che la subisce:
> 
>   
> 
> $$\vec{E} = \frac{\vec{F}}{q_0}$$
> 
>   

Dalla definizione, si evince che la forza subita da una carica immersa in un campo elettrico è esprimibile come $\vec{F} = q_0 \vec{E}$.

  

Nel caso in cui il campo sia generato da una singola carica puntiforme $q$, sfruttando la legge di Coulomb per la forza $\vec{F} = K \frac{q q_0}{r^2} \hat{r}$, l'espressione per il campo elettrico a distanza $r$ diventa:

  

$$\vec{E} = K \frac{q}{r^2} \hat{r}$$

  

Questa formula mostra che il campo elettrico vettoriale generato da una carica puntiforme dipende unicamente dal valore della carica sorgente $q$, scala con l'inverso del quadrato della distanza ($1/r^2$) e possiede una simmetria radiale.

  

## Rappresentazione tramite Linee di Campo

Per visualizzare il campo elettrico in modo intuitivo e qualitativo, si ricorre alle "linee di campo" (o linee di forza), una convenzione introdotta originariamente da Faraday.

  

- Le linee di campo escono dalle cariche positive.
    
      
    
- Le linee di campo entrano nelle cariche negative.
    
      
    
- La densità delle linee in una determinata regione dello spazio è proporzionale all'intensità del campo elettrico in quel punto: dove le linee sono più fitte (es. in prossimità della carica sorgente), il campo è più intenso.
    
      
    

> [!tip] Rappresentazione Grafica (Excalidraw)
> 
> Si consiglia di utilizzare uno schema disegnato a mano o in Excalidraw per visualizzare le linee di campo di configurazioni complesse (es. il campo in prossimità di due cariche dello stesso segno o di segno opposto), evidenziando la curvatura delle linee nella regione di interferenza.
> 
>   

Mentre il campo generato da cariche puntiformi è radiale e decresce quadraticamente con la distanza, esistono configurazioni continue che generano campi differenti. Un esempio fondamentale è il piano infinito uniformemente carico: per questioni di simmetria, il campo elettrico prodotto risulta ovunque ortogonale alla superficie del piano e la sua intensità è costante nello spazio, non dipendendo dalla distanza dal piano stesso.

  

## Principio di Sovrapposizione per il Campo Elettrico

Come la forza di Coulomb, anche il campo elettrico obbedisce al principio di sovrapposizione. Se lo spazio è perturbato da $n$ cariche distinte, il campo elettrico totale in un punto è pari alla somma vettoriale dei campi elettrici generati singolarmente da ciascuna delle cariche:

  

$$\vec{E}_{\text{tot}} = \sum_{i=1}^n \vec{E}_i$$

  

# Il Dipolo Elettrico

Un sistema elettrostatico di particolare rilevanza, detto "dipolo elettrico", è costituito da due cariche di eguale modulo ma segno opposto ($+q$ e $-q$) separate da una distanza fissa $d$. L'obiettivo è calcolare il campo elettrico risultante in un punto $P$ posto lungo l'asse del dipolo (la retta che congiunge le due cariche), a una distanza $z$ dal centro geometrico del sistema.

  

Applicando il principio di sovrapposizione, il campo elettrico totale è la somma algebrica dei campi generati dalle singole cariche (i vettori giacciono sulla medesima retta, dunque il problema è trattabile proiettandoli sull'asse unidimensionale). Il campo generato dalla carica positiva (che dista $z - \frac{d}{2}$ dal punto) e quello generato dalla carica negativa (che dista $z + \frac{d}{2}$) hanno versi opposti. L'intensità del campo totale $E$ è:

  

$$E = E_+ - E_- = K \frac{q}{\left(z - \frac{d}{2}\right)^2} - K \frac{q}{\left(z + \frac{d}{2}\right)^2}$$

  

Raccogliendo $Kq$ e svolgendo il denominatore comune, si ottiene:

  

$$E = Kq \frac{\left(z + \frac{d}{2}\right)^2 - \left(z - \frac{d}{2}\right)^2}{\left(z - \frac{d}{2}\right)^2 \left(z + \frac{d}{2}\right)^2}$$

  

Sviluppando i quadrati al numeratore ($z^2 + \frac{d^2}{4} + dz - z^2 - \frac{d^2}{4} + dz$) ed espandendo il denominatore notevole, si ha:

  

$$E = \frac{2Kqdz}{\left(z^2 - \frac{d^2}{4}\right)^2} = \frac{2Kqdz}{z^4 \left(1 - \frac{d^2}{4z^2}\right)^2}$$

  

Semplificando la $z$ al numeratore, la formula esatta per l'asse del dipolo risulta:

  

$$E = \frac{2Kqd}{z^3 \left(1 - \frac{d^2}{4z^2}\right)^2}$$

  

**Approssimazione per grandi distanze ($z \gg d$)** Quando la distanza $z$ a cui si valuta il campo è molto maggiore della distanza interna $d$ tra le cariche, il termine $\frac{d^2}{4z^2}$ diventa trascurabile rispetto a $1$ ($\frac{d^2}{4z^2} \ll 1$). L'espressione si semplifica in modo significativo:

  

$$E \approx \frac{2Kqd}{z^3}$$

  

Per descrivere in modo compatto il sistema a grandi distanze, si definisce il **momento di dipolo elettrico** (indicato con $p$), definito come il prodotto tra la carica e la distanza:

  

$$p = qd$$

  

Di conseguenza, il modulo del campo elettrico approssimato per il dipolo può essere scritto in funzione del momento di dipolo:

  

$$E \approx \frac{2Kp}{z^3}$$

  

Tale andamento dimostra che il campo di un dipolo decade più rapidamente ($1/z^3$) rispetto a quello di una carica puntiforme singola ($1/z^2$).

  

# Esercizi Svolti e Metodologia Vettoriale

> [!example] Esercizio 1: Sovrapposizione di Forze 1D e 2D **Dati iniziali:** Due cariche positive si trovano a distanza $r = 0.2 \, \text{m}$.
> 
>   
> 
> - $q_1 = 1.6 \cdot 10^{-19} \, \text{C}$ (posizionata nell'origine).
>     
>       
>     
> - $q_2 = 3.2 \cdot 10^{-19} \, \text{C}$.
>     
>       
>     
> 
> **Parte A: Calcolo della forza tra $q_1$ e $q_2$** La forza che $q_2$ esercita su $q_1$ è repulsiva (dunque diretta verso il semiasse negativo delle $x$). Fissato il sistema di riferimento sull'asse $x$, il vettore forza è:
> 
>   
> 
> $$\vec{F}_{1,2} = - K \frac{q_1 q_2}{r^2} \hat{i}$$
> 
>   
> 
> Sostituendo i valori numerici, controllando analiticamente che l'unità di misura diventi Newton ($\text{N}$):
> 
>   
> 
> $$F_{1,2} = - 8.99 \cdot 10^9 \, \frac{\text{Nm}^2}{\text{C}^2} \frac{(1.6 \cdot 10^{-19} \, \text{C})(3.2 \cdot 10^{-19} \, \text{C})}{(0.2 \, \text{m})^2} = - 1.15 \cdot 10^{-24} \, \text{N}$$
> 
>   
> 
> **Parte B: Inserimento di una terza carica (1D)** Si inserisce una terza carica $q_3 = -q_2$ a una distanza $\frac{3}{4} r$ da $q_1$. La forza totale netta su $q_1$ è la somma vettoriale della repulsione di $q_2$ e dell'attrazione di $q_3$. Proiettando sull'asse $x$:
> 
>   
> 
> $$F_{1,\text{netta}} = F_{1,3} - F_{1,2} = \frac{K q_1 \vert{}q_3\vert{}}{\left(\frac{3}{4}r\right)^2} - \frac{K q_1 q_2}{r^2}$$
> 
>   
> 
> Ricordando che $\vert{}q_3\vert{} = q_2$, si raccoglie a fattor comune:
> 
>   
> 
> $$F_{1,\text{netta}} = \left( \frac{16}{9} - 1 \right) \frac{K q_1 q_2}{r^2} = \frac{7}{9} \frac{K q_1 q_2}{r^2} = 9 \cdot 10^{-25} \, \text{N}$$
> 
>   
> 
> **Parte C: Spostamento angolare (2D)** La carica $q_3$ viene ora posizionata ruotandola di un angolo $\theta = 60^\circ$ attorno a $q_1$, mantenendo invariata la sua distanza $\frac{3}{4} r$. Il modulo di $\vec{F}_{1,3}$ resta:
> 
>   
> 
> $$\vert{}F_{1,3}\vert{} = \frac{16}{9} \frac{K q_1 q_2}{r^2} = \frac{16}{9} \vert{}F_{1,2}\vert{}$$
> 
>   
> 
> La forza deve ora essere scomposta nelle componenti lungo $x$ e $y$:
> 
>   
> 
> - $F_{1,3}^x = F_{1,3} \cos(60^\circ)$
>     
>       
>     
>       
>     
> - $F_{1,3}^y = F_{1,3} \sin(60^\circ)$
>     
>       
>     
>       
>     
> 
> La forza totale vettoriale su $q_1$ si ricava per sovrapposizione sulle singole componenti:
> 
>   
> 
> $$\vec{F}_{1,\text{netta}} = \vec{F}_{1,2} + \vec{F}_{1,3} = (F_{1,3} \cos\theta - \vert{}F_{1,2}\vert{})\hat{i} + (F_{1,3} \sin\theta)\hat{j}$$
> 
>   
> 
> $$\vec{F}_{1,\text{netta}} = \left(\frac{16}{9} \cos(60^\circ) - 1\right) \vert{}F_{1,2}\vert{} \hat{i} + \vert{}F_{1,2}\vert{} \sin(60^\circ) \hat{j}$$
> 
>   
> 
> Che risulta numericamente in $1.25 \cdot 10^{-25} \, \text{N} \, \hat{i} + 1.78 \cdot 10^{-24} \, \text{N} \, \hat{j}$.
> 
>   

> [!example] Esercizio 2: Ricerca del punto di equilibrio **Dati iniziali:** Due cariche poste a distanza fissa $L$ su un asse.
> 
>   
> 
> - $q_1 = 8q$ (positiva)
>     
>       
>     
> - $q_2 = -2q$ (negativa)
>     
>       
>     
> 
> Si cerca la posizione $x$ lungo l'asse congiungente in cui una carica di prova $Q > 0$ si trovi in equilibrio perfetto (forza netta nulla).
> 
>   
> 
> **Analisi dei casi:**
> 
>   
> 
> 1. **Tra le due cariche:** Entrambe le forze indurrebbero uno spostamento verso $q_2$ (repulsione da $q_1$ e attrazione da $q_2$). La somma dei vettori non può mai essere nulla.
>     
>       
>     
> 2. **Esterno, lato $q_1$:** Le forze hanno verso opposto. Supponendo $Q$ a distanza $x$ da $q_1$ e $(x+L)$ da $q_2$, l'equilibrio impone:
>     
>       
>     
>     $$K \frac{8q Q}{x^2} = K \frac{2q Q}{(x+L)^2}$$
>     
>       
>     
>     Semplificando si arriva a $\frac{4}{x^2} = \frac{1}{(x+L)^2}$, da cui $2(x+L) = x \Rightarrow x = -2L$. Ottenere una coordinata spaziale negativa contrasta matematicamente con la definizione preliminare di $x$ intesa come distanza posizionale positiva da $q_1$ verso l'esterno; pertanto non vi è soluzione fisica in questa regione.
>     
>       
>     
> 3. **Esterno, lato $q_2$:** Le forze hanno verso opposto. Posizionando $Q$ a distanza $x$ da $q_2$ e $(x+L)$ da $q_1$:
>     
>       
>     
>     $$K \frac{8q Q}{(x+L)^2} = K \frac{2q Q}{x^2}$$
>     
>       
>     
>     Si semplificano $K$, $q$ e $Q$, arrivando all'equazione ridotta:
>     
>       
>     
>     $$\frac{4}{(x+L)^2} = \frac{1}{x^2}$$
>     
>       
>     
>     Estraendo la radice quadrata su entrambi i membri:
>     
>       
>     
>     $$\frac{2}{x+L} = \frac{1}{x} \implies 2x = x + L \implies x = L$$
>     
>       
>     
>     La posizione di equilibrio si trova esternamente al segmento, dal lato della carica più debole $q_2$, a una distanza esatta $L$ da essa.
>