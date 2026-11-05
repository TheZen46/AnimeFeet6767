# D3 - Spazi euclidei e piu variabili

Testo estratto da `Rielaborazioni/ANALISI_SpaziEuclidi_260613_000837.pdf` (dispensa battuta, 2026) con `pdftotext -layout`. Le formule sono rese in modo approssimato dall'estrazione: per la lettura esatta fa fede il PDF. Tolti 0 rimandi `[cite: …]` e due numeri di matricola. Nessun'altra modifica.

```text
         Spazi Euclidei e Funzioni in Più
                    Variabili
                         Appunti Rielaborati ed Estesi

                           A cura di [matricola tolta] e [matricola tolta]

                              Anno Accademico in Corso



Indice

1 Spazi Euclidei e Struttura Algebrica                                                       3
  1.1 Definizione di Rn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      3
  1.2 Operazioni nello Spazio Vettoriale . . . . . . . . . . . . . . . . . . . . . . .       3
  1.3 Norma Euclidea e Distanza . . . . . . . . . . . . . . . . . . . . . . . . . .          4
  1.4 Prodotto Scalare e Angoli . . . . . . . . . . . . . . . . . . . . . . . . . . .        4

2 Nozioni Topologiche in Rn                                                                 5
  2.1 Intorni e Punti di un Insieme . . . . . . . . . . . . . . . . . . . . . . . . .       5
  2.2 Insiemi Aperti, Chiusi e Connessi . . . . . . . . . . . . . . . . . . . . . . .       6
  2.3 Punti di Accumulazione e Proprietà Globali . . . . . . . . . . . . . . . . .          6

3 Funzioni in Più Variabili Reali                                                           7
  3.1 Dominio, Immagine e Grafico . . . . . . . . . . . . . . . . . . . . . . . . .         7
  3.2 Curve e Insiemi di Livello . . . . . . . . . . . . . . . . . . . . . . . . . . .      7

4 Limiti e Continuità                                                                    8
  4.1 Definizione di Limite e Continuità . . . . . . . . . . . . . . . . . . . . . . . 8
  4.2 Esempi ed Esistenza del Limite . . . . . . . . . . . . . . . . . . . . . . . . 8
  4.3 Criterio in Coordinate Polari . . . . . . . . . . . . . . . . . . . . . . . . . . 10

5 Calcolo Differenziale in Rn                                                               10
  5.1 Derivate Parziali e Gradiente . . . . . . . . . . . . . . . . . . . . . . . . . .     10
  5.2 Derivate Direzionali . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    11
  5.3 Differenziabilità . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   11

6 Derivate del Secondo Ordine e Matrice Hessiana                                    12
  6.1 Matrice Hessiana e Teorema di Schwarz . . . . . . . . . . . . . . . . . . . . 13

                                              1


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                       Dispense Accademiche


7 Estremi di Funzioni in Più Variabili                                                  13
  7.1 Massimi e Minimi Locali/Globali . . . . . . . . . . . . . . . . . . . . . . .     13
  7.2 Punti Critici e Teorema di Fermat . . . . . . . . . . . . . . . . . . . . . . .   14
  7.3 Criterio della Matrice Hessiana . . . . . . . . . . . . . . . . . . . . . . . .   15
      7.3.1 Formula Pratica per Funzioni in 2 Variabili (n = 2) . . . . . . . . .       15
  7.4 Esempi Dettagliati di Classificazione Punti Critici . . . . . . . . . . . . . .   15




                                            2


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                                  Dispense Accademiche


1     Spazi Euclidei e Struttura Algebrica
L’analisi matematica a più variabili fonda le sue basi sullo studio dello spazio euclideo
n-dimensionale, denotato con Rn . Questo spazio generalizza i concetti di retta reale (R),
piano cartesiano (R2 ) e spazio tridimensionale (R3 ) ad una dimensione arbitraria n ∈ N.

1.1     Definizione di Rn
Definiamo formalmente lo spazio Rn come l’insieme di tutte le n-uple ordinate di numeri
reali:
                     Rn = {(x1 , x2 , . . . , xn ) | x1 , x2 , . . . , xn ∈ R}      (1)
Casi particolari notevoli sono:
    • R2 = {(x, y) | x, y ∈ R}, il piano cartesiano.
    • R3 = {(x, y, z) | x, y, z ∈ R}, lo spazio tridimensionale classico.
    Lo spazio Rn possiede una duplice natura geometrica e algebrica, e può essere identi-
ficato in due modi fondamentali:
    1. Come Spazio Affine: Un insieme di punti le cui coordinate indicano una posizione
       specifica. Ad esempio, il punto P = (x0 , y0 , z0 ) in R3 .
    2. Come Spazio Vettoriale: Un insieme di vettori applicati nell’origine, che indicano
       spostamenti, direzioni o grandezze fisiche (come velocità o forza). Un vettore è
       indicato in queste dispense con il grassetto v (negli appunti manoscritti viene spesso
       indicata la notazione con il tratto inferiore v).




Figura 1: Spazio per Diagramma 1: Rappresentazione grafica degli assi cartesiani x, y, z in
R3 . Viene mostrato un punto (x0 , y0 , z0 ) e il vettore corrispondente che parte dall’origine
e punta verso le coordinate indicate, evidenziando la duplice natura di spazio affine e
vettoriale.


1.2     Operazioni nello Spazio Vettoriale
Pensando a Rn come spazio vettoriale, possiamo definire formalmente le operazioni alge-
briche che lo caratterizzano:
Definizione 1.1 (Somma tra vettori). Dati due vettori x = (x1 , . . . , xn ) e y = (y1 , . . . , yn )
in Rn , si definisce la somma componente per componente:
                            x + y = (x1 + y1 , x2 + y2 , . . . , xn + yn )                       (2)

                                                  3


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                                Dispense Accademiche


Definizione 1.2 (Prodotto per uno scalare). Dato un vettore x = (x1 , . . . , xn ) ∈ Rn e
uno scalare reale α ∈ R, si definisce il prodotto per uno scalare come:

                                      αx = (αx1 , . . . , αxn )                                  (3)

    In virtù di queste due operazioni, Rn acquisisce la struttura algebrica di spazio vetto-
riale. È possibile esprimere qualsiasi vettore x = (x1 , . . . , xn ) tramite una combinazione
lineare dei vettori della base canonica:

                                 x = x1 e1 + x2 e2 + · · · + xn en                               (4)

dove i vettori base sono definiti come e1 = (1, 0, . . . , 0), e2 = (0, 1, 0, . . . , 0), e en =
(0, . . . , 0, 1).

1.3     Norma Euclidea e Distanza
Per dotare lo spazio vettoriale di una metrica geometrica (lunghezze e distanze), introdu-
ciamo il concetto di norma euclidea.
Definizione 1.3 (Norma euclidea). Dato un vettore x = (x1 , . . . , xn ) ∈ Rn , si definisce
norma (o modulo) del vettore la quantità non negativa:
                                    q
                             ∥x∥ = x21 + x22 + · · · + x2n                               (5)

     Geometricamente, la norma ∥x∥ rappresenta la distanza del punto x dall’origine
(0, . . . , 0). Da questo concetto deriva immediatamente la definizione di distanza tra due
punti qualsiasi nello spazio euclideo: se x, y ∈ Rn , la distanza tra essi è data dalla norma
della loro differenza:

                                                                                           (6)
                                           p
                      d(x, y) = ∥x − y∥ = (x1 − y1 )2 + · · · + (xn − yn )2

Proposizione 1.1 (Proprietà della Norma). Per ogni x, y ∈ Rn e per ogni scalare α ∈ R,
valgono le seguenti proprietà:
   1. ∥x∥ ≥ 0 e in particolare ∥x∥ = 0 ⇐⇒ x = 0 (Annullamento).

   2. ∥αx∥ = |α| · ∥x∥ (Omogeneità assoluta).

   3. ∥x + y∥ ≤ ∥x∥ + ∥y∥ (Disuguaglianza triangolare).

1.4     Prodotto Scalare e Angoli
Il prodotto scalare standard permette di introdurre nozioni di ortogonalità e di misurare
angoli nello spazio ad n dimensioni.
Definizione 1.4 (Prodotto Scalare). Dati due vettori x = (x1 , . . . , xn ) e y = (y1 , . . . , yn ),
il prodotto scalare euclideo è definito come:

                                x · y = x1 y1 + x2 y2 + · · · + xn yn                            (7)

   È immediato notare la stretta relazione tra il prodotto scalare e la norma:
                                √
                        ∥x∥ = x · x       =⇒       ∥x∥2 = x · x                                  (8)

                                                 4


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                              Dispense Accademiche


Teorema 1.1 (Disuguaglianza di Cauchy-Schwarz). Per ogni coppia di vettori x, y ∈ Rn
risulta:
                                |x · y| ≤ ∥x∥ ∥y∥                                 (9)

   Questa disuguaglianza fondamentale garantisce che il rapporto ∥x∥∥y∥
                                                                   x·y
                                                                        sia sempre com-
preso tra −1 e 1, permettendo così di definire univocamente l’angolo θ ∈ [0, π] tra i due
vettori x e y:                                       
                                               x·y
                               θ = arccos                                            (10)
                                              ∥x∥ ∥y∥
Ne consegue l’utile formula: x · y = ∥x∥ ∥y∥ cos θ.


2     Nozioni Topologiche in Rn
Per definire rigorosamente i concetti di limite e derivata in più variabili, dobbiamo prima
stabilire l’impalcatura topologica di Rn , ovvero la struttura che definisce la "vicinanza"
tra i punti.

2.1    Intorni e Punti di un Insieme
Definizione 2.1 (Intorno Sferico). Dato un punto x0 ∈ Rn e un raggio r > 0, definiamo
l’intorno sferico (o palla aperta) centrato in x0 di raggio r l’insieme:

                              Br (x0 ) = {x ∈ Rn | ∥x − x0 ∥ < r}                            (11)




Figura 2: Spazio per Diagramma 2: Un cerchio rosso rappresentante un intorno aperto
Br (x0 ) in R2 . Si noti il centro del cerchio, il raggio r, e la linea tratteggiata della circon-
ferenza per indicare che il bordo non è incluso nell’insieme.

   Sia ora Ω ⊆ Rn un sottoinsieme arbitrario e x ∈ Rn un punto dello spazio. Diciamo
che x è:

    • Interno a Ω: Se esiste un raggio r > 0 tale che l’intero intorno Br (x) è completa-
      mente contenuto in Ω (Br (x) ⊆ Ω).

    • Esterno a Ω: Se esiste un raggio r > 0 tale che l’intorno non interseca Ω, ovvero
      è contenuto nel complementare (Br (x) ⊆ Ωc ).

    • Di Frontiera per Ω: Se non è né interno né esterno. Equivalentemente, per ogni
      r > 0, l’intorno Br (x) contiene sia punti appartenenti ad Ω sia punti appartenenti
      al complementare Ωc .

                                                5


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                         Dispense Accademiche


   A partire da queste definizioni puntuali, definiamo i tre insiemi caratteristici generati
da Ω:

  1. L’interno di Ω (denotato con Ω◦ o Ω̊): l’insieme di tutti i punti interni di Ω.

  2. La frontiera di Ω (denotata con ∂Ω): l’insieme di tutti i punti di frontiera.

  3. La chiusura di Ω (denotata con Ω): è l’unione di Ω con la sua frontiera, ovvero
     Ω = Ω ∪ ∂Ω.

Vale sempre la relazione di inclusione: Ω◦ ⊆ Ω ⊆ Ω.

2.2    Insiemi Aperti, Chiusi e Connessi
Definizione 2.2 (Insiemi Aperti e Chiusi). Un insieme Ω ⊆ Rn si dice Aperto se coincide
con il proprio interno (Ω = Ω◦ ), ossia se ogni suo punto è interno. Un insieme Ω si dice
Chiuso se contiene la sua frontiera (∂Ω ⊆ Ω), o equivalentemente se coincide con la sua
chiusura (Ω = Ω).

Osservazione 2.1 (Proprietà degli aperti e chiusi).     • L’intero spazio Rn e l’insieme
    vuoto ∅ sono gli unici sottoinsiemi che sono sia aperti che chiusi (insiemi "clopen").

   • L’intorno Br (x0 ) è sempre un insieme aperto per ogni r > 0.

   • L’insieme palla chiusa Br (x0 ) = {x ∈ Rn | ∥x − x0 ∥ ≤ r} è un insieme chiuso.

   • L’unione (anche infinita) di aperti è aperta. L’intersezione (anche infinita) di chiusi
     è chiusa.

Esempio 2.1. L’insieme anulare A = {x ∈ Rn | 2 < ∥x∥ ≤ 3} non è né aperto né
chiuso. Non è aperto perché i punti con norma 3 appartengono ad A ma nessun loro
intorno è interamente contenuto in A. Non è chiuso perché i punti di norma 2 sono di
frontiera per A ma non appartengono ad A.

2.3    Punti di Accumulazione e Proprietà Globali
Definizione 2.3 (Punto di accumulazione e isolato). Un punto x0 ∈ Rn si dice di
accumulazione per Ω se ogni suo intorno, privato al più del punto stesso, interseca
Ω:
                       ∀r > 0, [Br (x0 ) \ {x0 }] ∩ Ω ̸= ∅                     (12)
Se un punto x0 ∈ Ω non è di accumulazione, viene detto punto isolato di Ω.

   Infine, per lo studio dell’ottimizzazione, introduciamo due concetti globali:

   • Un insieme Ω si dice Limitato se è possibile contenerlo interamente all’interno di
     un intorno sferico di raggio finito R: ∃R > 0 : Ω ⊆ BR (0).

   • Un insieme Ω si dice Connesso se non è l’unione di due insiemi aperti, non vuoti
     e disgiunti. Intuitivamente, un insieme connesso è formato da un "unico pezzo".
     Rigorosamente, Ω è connesso se, per ogni scomposizione Ω = A ∪ B con A, B ̸= ∅,
     si ha A ∩ B ̸= ∅ o A ∩ B ̸= ∅.

                                             6


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                            Dispense Accademiche


3     Funzioni in Più Variabili Reali
Una funzione in più variabili è una legge che ad ogni vettore di un dominio assegna un
unico numero scalare reale.
                                 f : dom(f ) ⊆ Rn → R                             (13)

3.1     Dominio, Immagine e Grafico
    • L’Immagine della funzione è il sottoinsieme dei reali coperto dai valori della fun-
      zione: Im(f ) = {f (x) | x ∈ dom(f )} ⊆ R.
    • Il Grafico della funzione è un sottoinsieme di Rn+1 definito da:
                              G(f ) = {(x, xn+1 ) ∈ Rn+1 | xn+1 = f (x)}                   (14)
Esempio 3.1 (Studio del Dominio). Vediamo alcuni casi di determinazione del dominio:
                   2   2
    1. f (x, y) = xx2 −y
                      +y
                         2 . Il denominatore deve essere non nullo: x − y
                                                                     2    2
                                                                            ̸= 0 =⇒ x2 ̸=
       y 2 =⇒ x ̸= ±y. Il dominio è R2 escluse le due bisettrici principali.
    2. f (x, y, z) = ln(1 − x2 − y 2 − z 2 ). L’argomento del logaritmo deve essere strettamente
       positivo: 1 − x2 − y 2 − z 2 > 0 =⇒ x2 + y 2 + z 2 < 1. Il dominio è l’intorno sferico
       aperto centrato nell’origine di raggio 1: B1 (0) in R3 .
    3. f (x, y) = ln(xy − x2 ). Bisogna imporre xy − x2 > 0 =⇒ x(y − x) > 0. Risolvendo
       la disequazione, abbiamo due casi:
          • Caso 1: x > 0 e y − x > 0 =⇒ x > 0, y > x.
          • Caso 2: x < 0 e y − x < 0 =⇒ x < 0, y < x.
       Il dominio è costituito da due angoli infiniti aperti del piano cartesiano.

3.2     Curve e Insiemi di Livello
Nel caso n = 2, il grafico della funzione "vive" in R3 e genera una superficie tridimensio-
nale. Essendo a volte difficile la visualizzazione 3D, si introduce lo strumento delle curve
di livello.
Definizione 3.1 (Insieme di livello). Dato k ∈ R, l’insieme di livello k della funzione f
è il sottoinsieme del dominio in cui la funzione assume esattamente il valore k:
                              L(f, k) = {x ∈ dom(f ) | f (x) = k}                          (15)
Esempio 3.2. Sia f (x, y) = x + y . L’immagine è [0, +∞).
                                 2    2

    • Fissando k > 0, l’equazione
                            √     x2 + y 2 = k descrive una circonferenza centrata
      nell’origine di raggio k.
    • Per k = 0, l’insieme L(f, 0) si riduce al solo punto origine: {(0, 0)}.
    • Per k < 0 (es. k = −1), l’insieme è vuoto: L(f, −1) = ∅.
Il grafico G(f ) è un paraboloide. Le sue "sezioni" ad altezza k costante (proiettate sul
piano xy) sono esattamente circonferenze  concentriche.
    Altro esempio: f (x, y) = x + y . Il grafico in R3 corrisponde all’equazione z 2 =
                              p
                                  2   2

x + y 2 (con z ≥ 0), che rappresenta un cono con vertice nell’origine.
  2




                                               7


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                            Dispense Accademiche




Figura 3: Spazio per Diagramma 3: Rappresentazione topografica di curve di livello per
un paraboloide (cerchi concentrici che si infittiscono radialmente) ed un cono (cerchi con-
centrici equispaziati).


4     Limiti e Continuità
L’estensione del concetto di limite a spazi multi-dimensionali presenta ostacoli concettuali:
in R, ci si può avvicinare a x0 solo da due direzioni (destra e sinistra). In Rn , si può
tendere a x0 da infinite direzioni (rette, parabole, spirali, ecc.). Affinché il limite esista,
deve essere indipendente dal percorso scelto.

4.1     Definizione di Limite e Continuità
Definizione 4.1 (Limite). Sia f : Ω ⊆ Rn → R e sia x0 un punto di accumulazione per
Ω. Diciamo che il limite di f per x tendente a x0 è il numero L ∈ R se:

                ∀ε > 0, ∃δ > 0 : ∀x ∈ Ω ∩ Bδ (x0 ) \ {x0 } =⇒ |f (x) − L| < ε              (16)

In simboli scriviamo: limx→x0 f (x) = L.

    Nota: valgono le usuali proprietà dei limiti per somma, prodotto, quoziente, unicità e
teoremi del confronto.

Definizione 4.2 (Continuità). Una funzione f si dice continua in x0 ∈ Ω se:

    1. Se x0 è un punto isolato di Ω, la funzione è banalmente continua.

    2. Se x0 è un punto di accumulazione, il limite esiste e coincide col valore della funzione:

                                          lim f (x) = f (x0 )                              (17)
                                         x→x0


   Come in Analisi 1, composizioni, somme e quozienti di funzioni elementari (polinomi,
espoenziali, logaritmi, radici, funzioni trigonometriche) generano funzioni che sono sempre
continue nel proprio dominio di esistenza.

4.2     Esempi ed Esistenza del Limite
Esempio 1: Calcolo tramite maggiorazioni Calcoliamo il limite:

                                                      x3
                                          lim
                                       (x,y)→(0,0) x2 + y 2


                                                8


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                          Dispense Accademiche


Il dominio è R2 \ {(0, 0)}. Valutiamo il modulo della funzione cercando maggiorazioni
opportune:
                                           x3        |x|3
                            |f (x, y)| = 2      = 2
                                         x + y2   x + y2
Poiché sappiamo che x2 + y 2 ≥ x2 , deduciamo che x2 +y
                                                     1
                                                        2 ≤ x2 . Moltiplicando per |x| :
                                                            1                         3



                                                    |x|3
                                    |f (x, y)| ≤         = |x|
                                                     x2
Dato che per (x, y) → (0, 0) si ha che |x| → 0, per il teorema del confronto anche
|f (x, y)| → 0. Pertanto il limite esiste e fa zero.

   Esempio 2: Non esistenza del limite Studiamo il limite:
                                                   x+y
                                          lim
                                       (x,y)→(0,0) x − y


Il dominio esclude la retta y = x. Per esistere, il limite deve essere univoco indipendente-
mente dalla traiettoria scelta per avvicinarsi all’origine. Proviamo a restringerci all’asse
y (curva x = 0):
                                            0+y
                         lim f (0, y) = lim        = lim (−1) = −1
                         y→0            y→0 0 − y     y→0

Ora proviamo a restringerci all’asse x (curva y = 0):

                                                    x+0
                                lim f (x, 0) = lim        =1
                                x→0             x→0 x − 0


I due limiti lungo curve diverse forniscono risultati differenti (1 ̸= −1). Pertanto, si
deduce che il limite globale non esiste.

   Esempio 3: L’inganno delle rette Studiamo:

                                                    x2 y
                                         lim
                                      (x,y)→(0,0) x4 + y 2


Se ci restringiamo ad una qualsiasi retta passante per l’origine, parametrizzata come
y = mx:

                               x2 (mx)             x3 m           xm
          lim f (x, mx) = lim  4    2  2
                                         = lim  2  2    2
                                                          = lim 2      =0
          x→0             x→0 x + m x      x→0 x (x + m )   x→0 x + m2


Si potrebbe esser tentati di concludere che il limite faccia zero. Tuttavia, se cambiamo
curva d’approccio e scegliamo la parabola y = x2 :

                                             x2 (x2 )          x4    1
                       lim f (x, x2 ) = lim 4       2 2
                                                        = lim    4
                                                                   =
                       x→0             x→0 x + (x )       x→0 2x     2

Ancora una volta, troviamo un percorso per il quale il limite vale 21 ̸= 0. Dunque, il
limite non esiste.

                                                9


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                             Dispense Accademiche


4.3     Criterio in Coordinate Polari
In R2 , lo studio del limite per (x, y) → (0, 0) diventa spesso più immediato adottando una
trasformazione in coordinate polari:
                                         (
                                          x = ρ cos θ
                                          y = ρ sin θ

La condizione di limite originaria (x, y) → (0, 0) diventa ρ → 0+ , indipendentemente
dall’angolo θ.
Teorema 4.1 (Criterio in Coordinate Polari). Sia f : R2 → R. Se esiste una funzione
g(ρ) e una costante L tale che:
    1. |f (ρ cos θ, ρ sin θ) − L| ≤ g(ρ) per ogni ρ in un intorno dello zero e per ogni θ ∈
       [0, 2π).
    2. g(ρ) dipende solo da ρ (la variabile θ deve essere maggiorata ed eliminata dalla
       formula).
    3. limρ→0+ g(ρ) = 0.
Allora, si ha che:
                                         lim        f (x, y) = L
                                      (x,y)→(0,0)

                                                                                     3
  Ripresa dell’Esempio 1 in polari: Vogliamo dimostrare che lim(x,y)→(0,0) x2x+y2 = 0.
Applicando la trasformazione:
                                            ρ3 cos3 θ      ρ3 cos3 θ
          |f (ρ cos θ, ρ sin θ) − 0| = 2    2       2 2  =      2
                                                                     = ρ cos3 θ
                                       ρ cos θ + ρ sin θ      ρ
Sappiamo che la funzione coseno è superiormente limitata: |cos θ| ≤ 1 =⇒ |cos3 θ| ≤ 1.
Pertanto possiamo maggiorare:

                                      ρ cos3 θ ≤ ρ = g(ρ)

Poiché g(ρ) = ρ tende a 0 per ρ → 0+ , il limite di partenza esiste e fa rigorosamente 0.


5     Calcolo Differenziale in Rn
5.1     Derivate Parziali e Gradiente
Il concetto di derivata in più variabili si scompone considerando l’incremento lungo cia-
scuna direzione degli assi cartesiani, mantenendo costanti le restanti variabili.
Definizione 5.1 (Derivata Parziale). Sia f : dom(f ) ⊆ Rn → R e sia x0 un punto interno
al dominio. Diciamo che f ammette derivata parziale rispetto alla componente i-esima in
x0 se esiste finito il seguente limite:
                              ∂f              f (x0 + hei ) − f (x0 )
                                  (x0 ) = lim                                            (18)
                              ∂xi         h→0          h
dove ei è l’i-esimo vettore della base canonica.

                                                    10


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                            Dispense Accademiche


    In R2 , la derivata rispetto ad x si calcola derivando la funzione secondo le regole usuali
rispetto a x, e trattando la variabile y come fosse una costante numerica. Il discorso
analogo vale per la derivazione rispetto a y.
Definizione 5.2 (Gradiente). Se una funzione ammette tutte le n derivate parziali nel
punto x0 , essa si dice derivabile in quel punto. Possiamo raggruppare tutte le derivate
parziali costruendo un vettore detto Gradiente, denotato con l’operatore nabla ∇:
                                                                           
                                     ∂f        ∂f                 ∂f
                       ∇f (x0 ) =       (x0 ),     (x0 ), . . . ,     (x0 )         (19)
                                    ∂x1        ∂x2                ∂xn
   Esempio di Calcolo: Sia f (x, y, z) = x ln(x + y − z). Il dominio impone l’argomento
x + y − z > 0. Calcoliamo le tre derivate parziali e generiamo il gradiente, applicando la
regola del prodotto per derivare lungo x:
          ∂f                               1                           x
             = 1 · ln(x + y − z) + x ·         · 1 = ln(x + y − z) +
          ∂x                           x+y−z                         x+y−z
          ∂f            1               x
             =x·             ·1=
          ∂y        x+y−z          x+y−z
          ∂f            1                    x
             =x·             · (−1) = −
          ∂z        x+y−z                 x+y−z
Da cui si costruisce il vettore ∇f (x, y, z) affiancando le espressioni trovate.

5.2    Derivate Direzionali
Possiamo estendere la nozione lungo direzioni arbitrarie. Se v ∈ Rn è un vettore non
nullo (tipicamente un versore con norma unitaria), definiamo la derivata direzionale
rispetto alla direzione v come:
                                     ∂f             f (x0 + hv) − f (x0 )
                      Dv f (x0 ) =      (x0 ) = lim                                       (20)
                                     ∂v         h→0          h
    Per calcolarla, applichiamo la definizione pratica. Sia f (x, y) = x2 + y 3 , x0 = (0, 1),
direzione v = (1, 1).
                                    f ((0, 1) + h(1, 1)) − f (0, 1)
                 Dv f (0, 1) = lim
                                h→0               h
                                    f (h, 1 + h) − f (0, 1)
                              = lim
                                h→0             h
                                    h2 + (1 + h)3 − 1
                              = lim
                                h→0           h
                                    h + 1 + 3h + 3h2 + h3 − 1
                                      2
                              = lim
                                h→0               h
                                    h(3 + 4h + h2 )
                              = lim                   = lim (3 + 4h + h2 ) = 3
                                h→0         h            h→0


5.3    Differenziabilità
In più variabili, la derivabilità non implica la continuità. Questo perché le derivate parziali
verificano l’esistenza del limite esclusivamente lungo l’asse x e l’asse y. Serve una condi-
zione più forte che imbrigli tutte le direzioni d’avvicinamento al punto simultaneamente:
la differenziabilità.

                                               11


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                                      Dispense Accademiche


Definizione 5.3 (Differenziabilità). Sia f : Ω ⊆ Rn → R derivabile in x0 ∈ Ω◦ . La fun-
zione si dice Differenziabile in x0 se vale il seguente sviluppo asintotico locale (formula
di Taylor al primo ordine):

               f (x) = f (x0 ) + ∇f (x0 ) · (x − x0 ) + o(∥x − x0 ∥) per x → x0                  (21)

Equivalentemente, portando i termini algebrici a primo membro, questo sviluppo si può
riformulare con il seguente limite che deve esistere e valere zero:
                               f (x) − f (x0 ) − ∇f (x0 ) · (x − x0 )
                          lim                                         =0                         (22)
                          x→x0               ∥x − x0 ∥

Teorema 5.1 (Implicazioni della Differenziabilità). Se una funzione è differenziabile in
x0 , allora gode di formidabili regolarità:
    1. f è continua in x0 .

    2. f possiede derivate direzionali lungo ogni direzione v ∈ Rn \ {0}.

    3. Vale la formula del gradiente per il calcolo rapido delle derivate direzionali:

                                            Dv f (x0 ) = ∇f (x0 ) · v                            (23)

    Geometricamente, la differenziabilità garantisce l’esistenza del piano tangente (o
dell’iperpiano in dimensione superiore) al grafico della funzione nel punto (x0 , f (x0 )).
L’equazione di tale piano per n = 2 è data esattamente dalla porzione lineare dello
sviluppo differenziale:
                                      ∂f                          ∂f
                 z = f (x0 , y0 ) +      (x0 , y0 ) · (x − x0 ) +    (x0 , y0 ) · (y − y0 )      (24)
                                      ∂x                          ∂y
   Per determinare in maniera semplice se una funzione è differenziabile, si adopera questo
potente strumento teorico:
Teorema 5.2 (Teorema del Differenziale Totale). Se una funzione f possiede derivate
parziali in un intorno di x0 e queste funzioni derivate parziali sono continue nel punto
x0 , allora la funzione originaria f è differenziabile in x0 .


6     Derivate del Secondo Ordine e Matrice Hessiana
Se la funzione f ammette derivate parziali ∂x ∂f
                                                i
                                                  , queste costituiscono a loro volta funzioni
dipendenti dallo spazio. A questo punto possiamo derivare ulteriormente tali funzioni
rispetto ad una variabile xj , ottenendo le derivate seconde.
    Se deriviamo per due volte rispetto alla medesima variabile (i = j) si parla di derivata
pura:
                                        ∂ 2f
                                             = fxi xi                                     (25)
                                        ∂x2i
Se deriviamo per variabili differenti (i ̸= j) si parla di derivata mista:

                                              ∂ 2f
                                                     = fxi xj                                    (26)
                                             ∂xi ∂xj

                                                     12


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                              Dispense Accademiche


6.1     Matrice Hessiana e Teorema di Schwarz
Definizione 6.1 (Matrice Hessiana). Se f ammette in x0 tutte le n2 derivate parziali
seconde possibili, queste vengono organizzate in una struttura tabellare chiamata Matrice
Hessiana, denotata con Hf (x0 ):
                                         2                      
                                           ∂ f            ∂2f
                                               2  .  . . ∂x1 ∂xn
                                         ∂x. 1    .        .. 
                                         ..
                             Hf (x0 ) =             ..      .                     (27)
                                             2
                                           ∂ f              2
                                                          ∂ f
                                          ∂xn ∂x1
                                                  ...     ∂x2  n


    Una funzione si definisce di Classe C 2 su un aperto Ω se tutte le sue derivate seconde
esistono e sono simultaneamente funzioni continue su tale insieme. In tal caso subentra
un importante risultato di simmetria.
Teorema 6.1 (Teorema di Schwarz). Sia f di classe C 2 nel dominio Ω. Allora l’ordine
di derivazione per le derivate miste è ininfluente, ovvero:

                                ∂ 2f            ∂ 2f
                                       (x0 ) =         (x0 )   ∀i, j                         (28)
                               ∂xi ∂xj         ∂xj ∂xi

Di conseguenza, la matrice Hessiana Hf (x0 ) è una matrice simmetrica.
   L’Hessiana riveste il ruolo geometrico della "concavità" (paragonabile alla derivata
seconda in Analisi 1). Per funzioni di classe C 2 , il polinomio di Taylor troncato al secondo
ordine acquisisce la seguente forma quadratica:
                                            1
    f (x) = f (x0 ) + ∇f (x0 ) · (x − x0 ) + (x − x0 )T Hf (x0 )(x − x0 ) + o(∥x − x0 ∥2 )   (29)
                                            2

7     Estremi di Funzioni in Più Variabili
Studieremo infine i meccanismi algoritmici per l’ottimizzazione in più dimensioni, con lo
scopo di trovare i picchi massimi e minimi per una determinata funzione topografica.

7.1     Massimi e Minimi Locali/Globali
Definizione 7.1 (Estremi). Sia f : dom(f ) → R e sia x0 ∈ dom(f ).
    • x0 è un punto di minimo locale per f se esiste un ϵ > 0 tale che:

                               f (x) ≥ f (x0 ) ∀x ∈ Bϵ (x0 ) ∩ dom(f )

    • x0 è un punto di minimo globale sull’insieme A ⊆ dom(f ) se vale f (x) ≥ f (x0 )
      per ogni singolo punto appartenente all’insieme A.
Analoga definizione invertendo le disuguaglianze vale per i massimi locali e globali. I
massimi e i minimi presi nel loro complesso vengono chiamati estremi.
   In base a specifici set d’ingresso, non è detto che tali estremi si palesino, specialmente
su domini aperti o illimitati. L’ancora di salvezza per garantire a priori la loro sussistenza
proviene dalla topologia.

                                               13


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                         Dispense Accademiche


Teorema 7.1 (Teorema di Weierstrass). Sia f una funzione continua definita in un
dominio Ω ⊆ Rn . Se prendiamo un insieme K ⊆ Ω tale che K sia un insieme simulta-
neamente Chiuso e Limitato (insieme geometricamente Compatto), allora la funzione
f ammette tassativamente almeno un punto di massimo globale e almeno un punto di
minimo globale all’interno di K.


7.2    Punti Critici e Teorema di Fermat
La ricerca pratica degli estremi interni al dominio inizia dallo studio dell’annullamento
della "pendenza".

Definizione 7.2 (Punto Critico o Stazionario). Sia f derivabile in x0 . Il punto si dice
critico se il gradiente della funzione si annulla:
                                                                     
                                                ∂f              ∂f
                     ∇f (x0 ) = 0    =⇒            = 0, . . . ,     =0              (30)
                                               ∂x1              ∂xn

Teorema 7.2 (Teorema di Fermat in Rn ). Se f è differenziabile in un punto interno x0
al dominio, e se questo punto è un estremo (massimo o minimo) locale per f , allora x0 è
obbligatoriamente un punto critico (cioè ∇f (x0 ) = 0).

Dimostrazione. Se x0 è un estremo locale per f , allora lo deve essere anche valutando
la funzione ristretta su ogni singola retta che transita per quel punto. Consideriamo la
restrizione parametrizzata γ(t) = x0 + tv, dove t ∈ R e v è una generica direzione.
La funzione scalare composta g(t) = f (x0 + tv) possiede un estremo locale in t = 0.
Applicando il Teorema di Fermat classico per le funzioni ad 1 variabile, la derivata in
t = 0 deve far zero: g ′ (0) = 0. Ma tramite la regola della catena derivando nel punto
t = 0:
                                 d
                        g ′ (0) = f (x0 + tv)     = ∇f (x0 ) · v = 0
                                 dt           t=0

Prendendo come direzioni v i vari assi canonici ei , concludiamo che ∂x
                                                                     ∂f
                                                                       i
                                                                         (x0 ) = 0 per tutti
gli assi i = 1, . . . , n, da cui l’asserto ∇f (x0 ) = 0.

    Attenzione: Il teorema di Fermat non assicura che un punto critico sia sempre un
estremo, esattamente come in una dimensione. Esistono infatti punti critici in cui il
gradiente è nullo, ma che rappresentano i cosiddetti Punti di Sella (es: f (x, y) = xy,
con critico in (0, 0)).
    Pertanto, gli estremi locali e globali dovranno essere setacciati in tre zone specifiche
di controllo:

  1. Punti critici (dove ∇f = 0).

  2. Punti di singolarità, in cui la funzione non è differenziabile o non ammette il calcolo
     derivativo (es. cuspidi 3D come in f (x, y) = x + y dove nel vertice l’origine non
                                                    p
                                                        2    2

     è derivabile).

  3. Punti situati sulla frontiera dell’insieme considerato (non studiabili col gradiente
     perché non si dispone di un intorno aperto circostante in cui sondare liberamente le
     pendenze radiali).

                                            14


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                            Dispense Accademiche


7.3      Criterio della Matrice Hessiana
Per classificare analiticamente i punti critici interni, valutiamo il segno della parabola
locale creata dalla struttura Hessiana.

Teorema 7.3 (Test dell’Hessiana). Sia x0 un punto critico per f (∇f (x0 ) = 0) e sup-
poniamo che f sia di classe C 2 in un suo intorno. Studiamo le proprietà algebriche
(autovalori) della matrice Hf (x0 ):

  1. Se l’Hessiana è Definita Positiva (tutti gli autovalori λ > 0): x0 è un punto di
     minimo locale.

  2. Se l’Hessiana è Definita Negativa (tutti gli autovalori λ < 0): x0 è un punto di
     massimo locale.

  3. Se l’Hessiana è Indefinita (esistono contemporaneamente autovalori positivi e au-
     tovalori negativi): x0 è un punto di sella. Non è né massimo né minimo.

  4. Se l’Hessiana è Semidefinita (positiva o negativa, possiede almeno un autovalore
     pari a zero e gli altri hanno concordanza di segno, o sono tutti zeri): la matrice non
     offre informazioni definitive. Il criterio è inconcludente (occorre indagare con
     studio di limitazione e metodi topologici sul segno diretto di f (x, y) − f (x0 , y0 )).

7.3.1     Formula Pratica per Funzioni in 2 Variabili (n = 2)
In R2 , la matrice è formata da 2×2 celle. L’analisi degli autovalori per il criterio precedente
viene surrogato ed inglobato dal rapido studio del suo Determinante (det(H)).

  Calcoliamo ∆ = det(Hf (x0 , y0 )) = fxx · fyy − (fxy )2 .

        • Se ∆ > 0 e fxx > 0 =⇒ Punto di Minimo locale.

        • Se ∆ > 0 e fxx < 0 =⇒ Punto di Massimo locale.

        • Se ∆ < 0 =⇒ Punto di Sella.

        • Se ∆ = 0 =⇒ Caso dubbio / inconcludente (ulteriori test necessari).


7.4      Esempi Dettagliati di Classificazione Punti Critici
Analizziamo ora compiutamente cinque casistiche emblematiche per padroneggiare la
tecnica computazionale in R2 .
   Esempio 1: f (x, y) = x2 + y 2 . Calcoliamo il gradiente: ∇f (x, y) = (2x, 2y). Im-
ponendo ∇f = 0, otteniamo l’unico punto critico nell’origine: P (0, 0). Calcoliamo le
derivate seconde: fxx = 2, fyy = 2, fxy = fyx = 0. L’Hessiana in (0, 0) è:
                                                 
                                             2 0
                                  H(0, 0) =
                                             0 2

Valutiamo: det(H) = 4 > 0. Osserviamo che fxx = 2 > 0. Essendo la concavità verso
l’alto lungo gli assi, concludiamo che (0, 0) è un punto di minimo locale (che si rivela
poi essere globale).

                                               15


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                             Dispense Accademiche


    Esempio 2: f (x, y) = −x2 − y 2 . Gradiente: ∇f (x, y) = (−2x, −2y). Punto critico in
P (0, 0). L’Hessiana:                                
                                              −2 0
                                H(0, 0) =
                                               0 −2
Il determinante vale det(H) = 4 > 0. Osserviamo fxx = −2 < 0. Concludiamo che
l’origine è un punto di massimo locale.

    Esempio 3: f (x, y) = x2 − y 2 . Gradiente: ∇f (x, y) = (2x, −2y). Punto critico:
(0, 0). L’Hessiana:                             
                                            2 0
                                H(0, 0) =
                                            0 −2
Il determinante restituisce det(H) = −4 < 0. A fronte di un determinante negativo, si
decreta univocamente la presenza di un punto di sella. Il paraboloide assume forma di
sella di cavallo, salendo lungo l’asse x e affondando lungo l’asse y.

    Esempio 4: f (x, y) = x2 + y 4 . Gradiente: ∇f (x, y) = (2x, 4y 3 ). Uguagliando a
zero ambo le componenti, l’unico punto critico è (0, 0). Calcoliamo le derivate seconde:
fxx = 2, fyy = 12y 2 , fxy = 0. L’Hessiana generica e nel punto (0, 0):
                                                                          
                                    2  0                               2 0
                    H(x, y) =                     =⇒   H(0, 0) =
                                    0 12y 2                            0 0

Il calcolo del determinante in (0, 0) fornisce det(H) = 0. Il criterio di classificazione
con la matrice Hessiana fallisce (caso dubbio). Tuttavia, agendo con l’intuito
matematico e testando il segno diretto della funzione: dato che le potenze sono pari,
x2 + y 4 ≥ 0 in tutto R2 . Essendo f (0, 0) = 0, capiamo analiticamente senza necessitare
di derivate superiori che il punto (0, 0) è un punto di minimo globale assoluto.

    Esempio 5: Caso di Sella Degenerata (Superficie di Peano) Consideriamo
f (x, y) = (y − x2 )(y − 2x2 ). Svolgiamo il prodotto intermedio per semplificare le derivate:
f (x, y) = y 2 − 2yx2 − yx2 + 2x4 = y 2 − 3x2 y + 2x4 . Deriviamo per estrarre il gradiente:

                                     ∂f
                                        (x, y) = −6xy + 8x3
                                     ∂x
                                     ∂f
                                        (x, y) = 2y − 3x2
                                     ∂y

Se analizziamo il punto origine (0, 0), notiamo che ∇f (0, 0) = (0, 0). L’origine è effetti-
vamente un punto critico. Calcoliamo le derivate seconde per strutturare l’Hessiana:

                                       fxx = −6y + 24x2
                                       fyy = 2
                                       fxy = −6x

Valutata nel punto (0, 0), la matrice si rivela:
                                                     
                                                  0 0
                                       H(0, 0) =
                                                  0 2

                                                  16


<!-- nuova pagina -->

Calcolo Differenziale in Rn                                           Dispense Accademiche


Nuovamente det(H) = 0. Il criterio classico dell’Hessiana non fornisce alcun verdetto
decisivo. Come risolviamo l’arcano?
   Andando ad indagare la limitazione di segno di (y − x2 )(y − 2x2 ), osserviamo che
questo prodotto di due parentesi si annulla sulle parabole gemelle y = x2 e y = 2x2 .

   • Se ci posizioniamo nella "valle" interna contenuta tra l’abbraccio delle due parabole,
     ovvero per i punti in cui si realizza x2 < y < 2x2 , il primo fattore diviene positivo e
     il secondo fattore diviene negativo. Conseguentemente, per tali punti interni all’area
     la funzione assume segno negativo (f (x, y) < 0).

   • Viceversa, per i punti localizzati "all’esterno" della valle (ossia per y > 2x2 o per
     y < x2 ), entrambi i fattori assumono lo stesso segno matematico (entrambi positivi o
     entrambi negativi), restituendo una valutazione finale di funzione con segno positivo
     (f (x, y) > 0).

Appurando quindi come la funzione, misurata in un intorno minuscolo a piacimento con-
vergente all’origine, sia costellata simultaneamente di zone a risultato positivo interspazia-
te a falci a risultato negativo, sanciamo con inequivocabile certezza che il punto esplorato
non possa essere né un minimo né un massimo. L’origine per la superficie di Peano è un
atipico punto di sella.




                                             17


<!-- nuova pagina -->
```
