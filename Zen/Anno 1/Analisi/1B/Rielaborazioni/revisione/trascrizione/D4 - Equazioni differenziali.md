# D4 - Equazioni differenziali

Testo estratto da `Rielaborazioni/ANALISI_eqDiff_260613_002153.pdf` (dispensa battuta, 2026) con `pdftotext -layout`. Le formule sono rese in modo approssimato dall'estrazione: per la lettura esatta fa fede il PDF. Tolti 133 rimandi `[cite: …]` e due numeri di matricola. Nessun'altra modifica.

```text
   Appunti di Equazioni Differenziali
                           Teoria, Modelli ed Esercizi

                     Trascrizione ed Espansione Accademica


Indice
1 Introduzione e Modelli Fisici                                                           2
  1.1 Caduta libera con attrito . . . . . . . . . . . . . . . . . . . . . . . . . . . .   2
  1.2 Sistema massa-molla . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     2
  1.3 Dinamica delle popolazioni . . . . . . . . . . . . . . . . . . . . . . . . . . .    3

2 Teoria Generale delle Equazioni Differenziali                                           3
  2.1 Definizioni Fondamentali . . . . . . . . . . . . . . . . . . . . . . . . . . . .    3
  2.2 Classificazione delle Equazioni Differenziali . . . . . . . . . . . . . . . . . .   4

3 Equazioni Differenziali a Variabili Separabili                                          5
  3.1 Metodo di Risoluzione . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     5
  3.2 Esempi Notabili . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   6

4 Equazioni Differenziali Lineari                                                    7
  4.1 Equazioni del Primo Ordine (n = 1) . . . . . . . . . . . . . . . . . . . . . . 7
      4.1.1 Caso Omogeneo (b(t) = 0) . . . . . . . . . . . . . . . . . . . . . . . 7
      4.1.2 Caso Non Omogeneo (b(t) ̸= 0) . . . . . . . . . . . . . . . . . . . . 8
  4.2 Equazioni del Secondo Ordine (n = 2) . . . . . . . . . . . . . . . . . . . . 8
      4.2.1 Caso Omogeneo a Coefficienti Costanti (f (t) = 0) . . . . . . . . . . 9
      4.2.2 Caso Non Omogeneo: Metodo di Somiglianza . . . . . . . . . . . . 10

5 Sistemi di Equazioni Differenziali del Primo Ordine                                     10
  5.1 Sistemi Lineari . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   11
  5.2 Sistemi Lineari Omogenei a Coefficienti Costanti . . . . . . . . . . . . . . .      12
       5.2.1 Autovalori con Molteplicità Carente (Non Regolari) . . . . . . . . .        12
       5.2.2 Esempi Pratici sui Sistemi . . . . . . . . . . . . . . . . . . . . . . .     13

6 Stabilità dei Punti di Equilibrio                                                      14




                                             1


<!-- nuova pagina -->

1     Introduzione e Modelli Fisici
Lo studio delle equazioni differenziali nasce dall’esigenza di modellizzare fenomeni naturali
in cui le grandezze fisiche variano nel tempo e nello spazio. Un’equazione differenziale
esprime una relazione tra una funzione incognita e le sue derivate. Di seguito si presentano
alcuni dei modelli fisici e biologici classici che portano alla formulazione di equazioni
differenziali.

1.1    Caduta libera con attrito
Consideriamo un corpo di massa m in caduta libera, soggetto alla forza di gravità e
alla resistenza dell’aria (attrito viscoso). Secondo il secondo principio della dinamica di
Newton:
                                          F =m·a                                        (1)
Sia y(t) la posizione dell’oggetto al tempo t. Sappiamo che la velocità v e l’accelerazione
a sono definite come le derivate della posizione:

                                       v(t) = y ′ (t)                                         (2)
                                       a(t) = v ′ (t) = y ′′ (t)                              (3)

Le forze in gioco sono la forza peso (Fp = −mg) e la forza di attrito viscoso, che si oppone
al moto ed è proporzionale alla velocità (Fa = −kv, con k > 0 costante di attrito).
Sostituendo nell’equazione di Newton otteniamo:

                          ma = −mg − kv =⇒ my ′′ = −mg − ky ′                                 (4)

Questa è un’equazione differenziale del secondo ordine. Se supponiamo che l’oggetto cada
da fermo da un’altezza h0 , per determinare la traiettoria dell’oggetto dobbiamo trovare
la funzione y(t) che soddisfa l’equazione differenziale e le condizioni iniziali y(0) = h0 e
y ′ (0) = 0. Questo costituisce un Problema di Cauchy.
      Risolvendo l’equazione per la velocità v(t), si ottiene la cosiddetta velocità limite
vlim = − mg k
              , raggiunta asintoticamente quando la forza peso è perfettamente bilanciata
dall’attrito. Integrando ulteriormente, la legge oraria assume la forma:

                                      m2         k
                                                 −m t
                                                       mg
                             y(t) =      g 1 − e       −   t + h0                             (5)
                                      k2                 k

1.2    Sistema massa-molla
Si consideri una massa m collegata ad una molla ideale su un piano orizzontale privo di
attrito.
    La forza di richiamo elastico è descritta dalla legge di Hooke:

                                             F = −kx                                          (6)

dove k è la costante elastica della molla e x(t) è lo spostamento dalla posizione di equilibrio.
Applicando nuovamente il principio di Newton]:

                                 −kx = ma =⇒ −kx = mx′′                                       (7)


                                                  2


<!-- nuova pagina -->

Figura 1: Disegno degli appunti: Sistema massa-molla. Il disegno rappresenta schemati-
camente una massa vincolata ad una parete tramite una molla deformabile.

                                  k
Dividendo per m e definendo ω 2 = m , l’equazione diventa:

                                        x′′ + ω 2 x = 0                                    (8)

Questa equazione differenziale descrive un moto armonico semplice. L’integrale generale,
ovvero l’insieme di tutte le soluzioni possibili, è una combinazione lineare di seni e coseni:
                                         r !                 r !
                                             k                  k
                          x(t) = c1 cos        t + c2 sin         t                         (9)
                                            m                  m

Le costanti di integrazione c1 e c2 dipendono unicamente dalle condizioni iniziali del
sistema (ad esempio, la posizione iniziale x(0) e la velocità iniziale x′ (0)).

1.3    Dinamica delle popolazioni
Le equazioni differenziali sono fondamentali anche in biologia per studiare la variazione di
una popolazione nel tempo. Sia y(t) il numero di individui di una popolazione al tempo
t].
    Un modello base è il modello malthusiano, che assume una crescita proporzionale alla
popolazione presente: y ′ = ϵy, dove ϵ rappresenta il tasso di crescita netto (nati meno
morti). Tuttavia, le risorse sono limitate. Si introduce quindi la capacità portante K,
limite dato dalle condizioni ambientali. Il modello logistico (o di Verhulst) è governato
dall’equazione:                                    y
                                       y ′ = ϵy 1 −                                     (10)
                                                    K
Ponendo la condizione iniziale y(0) = P0 , si osserva che se P0 = 0 oppure P0 = K,
la derivata y ′ si annulla per ogni t. Tali soluzioni, y(t) ≡ 0 e y(t) ≡ K, sono dette
soluzioni costanti o di equilibrio. Se 0 < P0 < K, la popolazione cresce fino ad avvicinarsi
asintoticamente al valore K. La soluzione analitica esplicita è data da:

                                               KP0 eϵt
                                   y(t) =                                                 (11)
                                            K − P0 + P0 eϵt

2     Teoria Generale delle Equazioni Differenziali
2.1    Definizioni Fondamentali
Definizione 2.1. Un’equazione differenziale ordinaria (EDO) di ordine n è un’equazione
del tipo:
                      F t, y(t), y ′ (t), . . . , y (n−1) (t), y (n) (t) = 0
                                                                        
                                                                                   (12)

                                               3 con F : dom(F ) ⊆ Rn+2 → R funzione assegnata. L’incognita da
determinare è una funzione scalare y : I ⊆ R → R derivabile n-volte, definita su un
intervallo I, che soddisfa l’equazione sopra citata. L’ordine dell’equazione è
dato dalla derivata di ordine massimo presente.
    L’insieme di tutte le funzioni che soddisfano l’equazione è detto integrale generale
dell’equazione differenziale.
Definizione 2.2. Il Problema di Cauchy è un sistema che associa all’equazione differen-
ziale un insieme di condizioni (dette condizioni iniziali) valutate in un punto specifico
t0. Ha la forma:
                                
                                
                                 F (t, y, y ′ , . . . , y (n) ) = 0
                                
                                y(t0 ) = y0
                                
                                
                                
                                  y ′ (t0 ) = y1                                    (13)
                                
                                  ...
                                
                                
                                
                                
                                
                                y (n−1) (t ) = y
                                             0          n−1 Una soluzione del Problema di Cauchy su un qualche intervallo I (aperto)
è una funzione y ∈ C n (I) con t0 ∈ I che soddisfa contemporaneamente l’equazione e tutte
le condizioni del sistema.
    Sotto opportune condizioni di regolarità della funzione F , si può dimostrare che la
soluzione del Problema di Cauchy esiste ed è unica in un intorno di t0.

2.2    Classificazione delle Equazioni Differenziali
   • Equazione Autonoma: Un’equazione differenziale si dice autonoma se la funzione
     F non dipende esplicitamente dalla variabile temporale t, ossia è del tipo
     F (y, y ′ , . . . , y (n) ) = 0.
      Esempio 2.1. y ′′ +y = 0 è un’equazione autonoma. Al contrario, y ′′ +ty =
      t non è autonoma.

   • Forma Normale: Un’equazione si dice in forma normale se la derivata di ordine
     maggiore può essere isolata algebricamente:

                                  y (n) = f t, y, y ′ , . . . , y (n−1)
                                                                        
                                                                              (14)
      Esempio 2.2. y ′′ = y 2 t cos(y) è in forma normale.

   • Equazione Lineare: Un’equazione differenziale si dice lineare se si presenta nella
     forma:
                an (t)y (n) + an−1 (t)y (n−1) + · · · + a1 (t)y ′ + a0 (t)y = b(t) (15) Si dice omogenea se il termine noto è nullo, ovvero b(t) = 0.

   • Coefficienti Costanti: Un’equazione differenziale lineare si dice a coefficienti co-
     stanti se le funzioni ai (t) sono costanti reali, ovvero ai (t) ≡ ai ∈ R.
     Esempio: 2y ′′ + 3y ′ + 4y = t2.

                                              4


<!-- nuova pagina -->

Osservazione 2.1 (Principio di Sovrapposizione per le EDO Lineari). Se il termine noto
è una somma di funzioni, b(t) = b1 (t)+b2 (t), allora le soluzioni y(t) di questa equazione si
possono scrivere come y(t) = y1 (t) + y2 (t), dove y1 è soluzione del problema
con termine noto b1 (t), e y2 è soluzione del problema con termine noto b2 (t). In particolare, se yo è una soluzione dell’omogenea associata e yp è una soluzione
particolare della completa, allora yo + yp è l’integrale generale della completa.


3     Equazioni Differenziali a Variabili Separabili
Le equazioni a variabili separabili costituiscono una classe fondamentale delle equazioni
differenziali del primo ordine.
Definizione 3.1. Sono equazioni differenziali della forma:
                                         y ′ = g(t)h(y)                                     (16) con g : I → R e h : J → R funzioni continue su intervalli aperti I e J.

3.1    Metodo di Risoluzione
Innanzitutto, verifichiamo l’esistenza di soluzioni costanti. Se y0 ∈ R è uno zero di h(y)
(ossia h(y0 ) = 0), allora la funzione costante y(t) = y0 per ogni t risolve l’equazione
differenziale, in quanto y ′ (t) = 0 = g(t) · 0.
    Dato un intervallo dove h(y) ̸= 0, possiamo dividere ambo i membri per h(y):
                                         y ′ (t)
                                                 = g(t)                                     (17)
                                        h(y(t))
                                              1
Se denotiamo con H(y) una primitiva di h(y)     , dal teorema di derivazione delle funzioni
composte abbiamo che dt [H(y(t))] = H ′ (y(t))y ′ (t) = h(y(t))
                          d                                1
                                                                y ′ (t). Uguagliando le
funzioni, otteniamo dtd [H(y(t))] = g(t). Integrando ambo i membri rispetto a t:
                                     H(y(t)) = G(t) + C                                     (18) dove G(t) è una primitiva di g(t) e C ∈ R è una costante arbitraria. Se la funzione
H è invertibile, si ottiene la soluzione in forma esplicita: y(t) = H −1 (G(t) + C).
    Informalmente, questa procedura viene ricordata separando formalmente i differenziali
dy e dt:                                                    Z             Z
              dy                      1                          1
                  = g(t)h(y) =⇒          dy = g(t)dt =⇒              dy = g(t)dt            (19)
               dt                   h(y)                        h(y) L’integrale generale dell’equazione differenziale è dato dall’unione delle soluzioni
cosı̀ trovate e delle eventuali soluzioni costanti analizzate precedentemente.
Teorema 3.1 (Problema di Cauchy per Equazioni a Variabili Separabili). Siano h : I →
R e g : J → R continue con I, J intervalli aperti. Siano t0 ∈ I e y0 ∈ J.
Allora il problema di Cauchy:    (
                                   y ′ = g(t)h(y)
                                                                                   (20)
                                   y(t0 ) = y0 ammette una soluzione definita su un sottointervallo I ′ ⊆ I con t0 ∈ I ′. Inoltre, se h ∈ C 1 (J) (oppure h è localmente lipschitziana) e se h(y0 ) ̸= 0,
allora tale soluzione è unica.

                                               5


<!-- nuova pagina -->

3.2     Esempi Notabili
Esempio 3.1 (Equazione banale). y ′ = g(t) (ossia h(y) = 1). La soluzione per
integrazione diretta è y(t) = G(t) + C, dove G è una primitiva di g.

Esempio 3.2 (Decadimento Radioattivo). y ′ = ky, con k costante di decadimento (se
k < 0) o di crescita (se k > 0). Qui g(t) = k e h(y) = y. Poiché h(0) = 0, y = 0
è una soluzione costante. Assumendo y ̸= 0:
          Z        Z
             dy
                = k dt =⇒ ln |y| = kt + C =⇒ |y| = eC ekt =⇒ y = ±eC ekt               (21)
              y Ponendo α = ±eC (che, includendo la soluzione costante y = 0, può assumere
qualsiasi valore in R), si ottiene la soluzione generale y(t) = αekt. Dato il pro-
blema di Cauchy con condizione y(0) = 1 e parametro k = 1 (dinamica delle popolazioni
con P0 = 1):

                         1 = y(0) = αe1·0 =⇒ α = 1 =⇒ y(t) = et                             (22)

Esempio 3.3 (Equazione Logistica). y ′ = 2y(1 − y). Qui g(t) = 2 e h(y) =
y(1 − y). Le radici di h(y) = 0 forniscono le soluzioni costanti y = 0 e y = 1. Assumiamo y ̸= 0 e y ̸= 1:
                                   Z                Z
                                          1
                                               dy = 2 dt                                 (23)
                                      y(1 − y)
                                                              1 Utilizzando la scomposizione in fratti semplici y(1−y) = y1 + 1−y
                                                                          1
                                                                             :
 Z              
       1   1                                                                y
         +           dy = 2t+C =⇒ ln |y|−ln |1−y| = 2t+C =⇒ ln                 = 2t+C (24)
       y 1−y                                                               1−y
                       y               y
                          = eC e2t =⇒     = αe2t con α ∈ R \ {0}                            (25)
                      1−y             1−y Risolvendo per y:

                                                                           αe2t
               y = (1 − y)αe2t =⇒ y + yαe2t = αe2t =⇒ y(t) =                                (26)
                                                                         1 + αe2t Risolviamo ora il problema di Cauchy con condizione y(0) = 2:
                                   α
                     2 = y(0) =         =⇒ 2 + 2α = α =⇒ α = −2                     (27)
                                1+α
                                                      −2e  2t   2e  2t Quindi la soluzione particolare è y(t) = 1−2e2t = 2e2t −1.


Esempio 3.4 (Equazione di Peano (Mancanza di Unicità)). Consideriamo il problema di
Cauchy:                           (     √
                                   y′ = 3 y
                                                                                (28)
                                   y(0) = 0

                                                6


<!-- nuova pagina -->

                                       √ Qui g(t) = 1 e h(y) = 3 y. Evidentemente y ≡ 0 è una soluzione
costante che soddisfa anche la condizione iniziale y(0) = 0. Tuttavia, la funzione
h(y) = y 1/3 non è derivabile (né lipschitziana) nel punto y = 0, quindi il Teorema 3.1 non
può garantire l’unicità della soluzione. Separando le variabili per y ̸= 0:
               Z              Z
                    −1/3                    3            3                2
                  y      dy = 1 dt =⇒ y 2/3 = t + C =⇒ y 2/3 = t + C                      (29)
                                            2            2                3
                                                                 q 
                                                                     2 3 Se poniamo C = 0, per t ≥ 0 otteniamo y(t) =             3
                                                                       t. Notiamo
che in t = 0, y(0) = 0 e la sua derivata destra in zero vale 0. Possiamo costruire
infinite soluzioni ”raccordando” la soluzione nulla con queste curve, formando il cosiddetto
”pennello di Peano”. Ad esempio:
                                           (
                                             0        se t < 0
                                   y(t) =      2 3/2
                                                                                         (30)
                                               3
                                                 t    se t ≥ 0 Questa funzione è derivabile con continuità su tutto R, soddisfa
l’equazione differenziale ovunque e rispetta la condizione iniziale y(0) = 0.
Spostando il punto di raccordo (e quindi ponendo C ̸= 0), si possono definire innumerevoli
altre soluzioni valide.


4       Equazioni Differenziali Lineari
L’espressione generale di un’equazione lineare di ordine n in forma normale è:

                    y (n) = an−1 (t)y (n−1) + · · · + a1 (t)y ′ + a0 (t)y + b(t)         (31)

4.1     Equazioni del Primo Ordine (n = 1)
L’equazione lineare del primo ordine ha la forma generale y ′ = a(t)y + b(t).

4.1.1    Caso Omogeneo (b(t) = 0)
L’equazione y ′ = a(t)y è a variabili separabili. Ha ovviamente la soluzione
costante y = 0. Per y ̸= 0:

          y′
             = a(t) =⇒ ln |y| = A(t) + C =⇒ |y| = eA(t)+C =⇒ y(t) = αeA(t)               (32)
          y con A(t) primitiva di a(t). L’integrale generale, includendo la
soluzione banale, è dunque:
                               y(t) = C · eA(t) , C ∈ R                           (33)




                                                 7


<!-- nuova pagina -->

4.1.2    Caso Non Omogeneo (b(t) ̸= 0)
Per risolvere y ′ = a(t)y + b(t) si utilizza il metodo del fattore integrante o della variazione
delle costanti. L’integrale generale è:
                                   Z                    
                              A(t)           −A(t)
                     y(t) = e          b(t)e       dt + α = eA(t) (K(t) + α)                (34) dove A(t) è una primitiva di a(t), α ∈ R, e K(t) è una primitiva di b(t)e−A(t). Possiamo verificarlo calcolando la derivata:

                                d  A(t)
                       y ′ (t) =
                                                    
                                    e (K(t) + α)
                               dt
                             = A′ (t)eA(t) (K(t) + α) + eA(t) K ′ (t)
                             = a(t) eA(t) (K(t) + α) + eA(t) b(t)e−A(t)
                                                                      

                             = a(t)y(t) + b(t)

Esempio 4.1. Risolviamo il problema di Cauchy:
                             (
                               y ′ = (− sin t)y + sin t
                                                                                              (35)
                               y(0) = 3 Identifichiamo a(t) = − sin t e b(t) = sin t. Una primitiva di a(t) è
A(t) = cos t. Calcoliamo l’integrale per trovare K(t):
                             Z                Z
                                   −A(t)
                     K(t) = b(t)e        dt = (sin t)e− cos t dt = e− cos t            (36) Sostituendo nella formula risolutiva:

                              y(t) = ecos t e− cos t + α = 1 + αecos t
                                                        
                                                                                              (37) Imponiamo la condizione iniziale y(0) = 3:

                    3 = 1 + αecos 0 = 1 + αe =⇒ αe = 2 =⇒ α = 2e−1                            (38) La soluzione finale è y(t) = 1 + 2e−1 ecos t = 1 + 2ecos t−1.

4.2     Equazioni del Secondo Ordine (n = 2)
La forma generale è y ′′ +a(t)y ′ +b(t)y = f (t). Noi studieremo approfonditamente
il caso in cui i coefficienti sono costanti:

                                   y ′′ + ay ′ + by = f (t),   a, b ∈ R                       (39)




                                                     8


<!-- nuova pagina -->

Figura 2: Illustrazione a margine della dispensa: Ritratto stilizzato di un personaggio,
somigliante ai disegni dei fumetti supereroistici.

4.2.1     Caso Omogeneo a Coefficienti Costanti (f (t) = 0)
Cerchiamo soluzioni della forma y(t) = eλt . Calcolando le derivate y ′ = λeλt e y ′′ = λ2 eλt e sostituendole nell’equazione omogenea y ′′ + ay ′ + by = 0, otteniamo:
                                      eλt (λ2 + aλ + b) = 0                                    (40) Poiché eλt ̸= 0 per ogni t, dobbiamo risolvere l’equazione caratteristica (o
polinomio caratteristico):
                                 P (λ) = λ2 + aλ + b = 0                             (41) Se λ è soluzione (radice) di P (λ) = 0, allora eλt è soluzione dell’equazione
differenziale. Le soluzioni differiscono in base al segno del discriminante
∆ = a2 − 4b:
                                                                             √
  1. ∆ > 0: Il polinomio ha due radici reali e distinte λ± = −a±2 ∆. Le due
     soluzioni fondamentali sono eλ+ t e eλ− t . L’integrale generale è combinazione lineare
     di esse:
                                   y(t) = c1 eλ+ t + c2 eλ− t                            (42)
  2. ∆ < 0: √Il polinomio ha due radici complesse coniugate λ± = α ± iβ, con α = −a/2
     e β = −∆ 2
                  ∈ R. Matematicamente e(α+iβ)t è soluzione, ma si
     preferisce un set di soluzioni fondamentali reali, usando le formule di Eulero:
                                    Re e(α+iβ)t = eαt cos(βt)
                                                
                                                                                     (43)
                                        (α+iβ)t     αt
                                    Im e           = e sin(βt)                       (44) L’integrale generale diviene:
                                  y(t) = eαt (c1 cos(βt) + c2 sin(βt))                         (45)
  3. ∆ = 0: C’è una sola radice reale doppia λ = −a/2. Abbiamo trovato
     una sola soluzione y1 (t) = eλt. Per trovarne una seconda linearmente
     indipendente, sapendo che per la radice doppia si ha P ′ (λ) = 0, si può verificare
     direttamente che y2 (t) = teλt è soluzione. Deriviamo: y2′ = eλt +λteλt , y2′′ =
     2λeλt + λ2 teλt . Sostituendo in y ′′ + ay ′ + by = 0 risulta (2λ + a)eλt + (λ2 + aλ + b)teλt .
     Essendo λ radice e −a/2, i termini si annullano. L’integrale generale è quindi:
                                 y(t) = c1 eλt + c2 teλt = eλt (c1 + c2 t)                     (46)

                                                 9


<!-- nuova pagina -->

4.2.2     Caso Non Omogeneo: Metodo di Somiglianza
Per l’equazione non omogenea y ′′ +ay ′ +by = f (t), le soluzioni sono della forma
y(t) = yom (t) + yp (t), dove yom (t) è l’integrale generale dell’omogenea
associata e yp (t) è una soluzione particolare qualsiasi della non omogenea.
    Se il termine noto f (t) ha forme specifiche, si può cercare yp (t) tramite il metodo di
somiglianza o dei coefficienti indeterminati:
    • Se f (t) = Pn (t)eαt (con Pn polinomio di grado n), la soluzione si cerca nella forma:

                                            yp (t) = tµ Qn (t)eαt                            (47) dove Qn è un polinomio generico dello stesso grado n, e µ è la molteplicità
        di α come radice del polinomio caratteristico P (λ) dell’omogenea (quindi µ = 0 se
        α non è radice, µ = 1 se è radice semplice, µ = 2 se è doppia).
    • Se f (t) = Pn (t)eαt cos(βt) (o analogo con seno), yp si cerca nella forma:

                              yp (t) = tµ eαt [Rn (t) cos(βt) + Sn (t) sin(βt)]              (48) dove Rn e Sn sono polinomi completi di grado n, e µ è la molteplicità del
        numero complesso α + iβ come radice del polinomio caratteristico.
Se f è la somma di funzioni di questo tipo, yp si ottiene sommando le corrispondenti
soluzioni particolari (Principio di Sovrapposizione).
Esempio 4.2. Impostiamo il calcolo per risolvere:

                                          y ′′ + y = t2 cos t                                (49) L’omogenea associata y ′′ + y = 0 ha polinomio caratteristico P (λ) = λ2 + 1 =
(λ − i)(λ + i) = 0. Le radici sono λ = ±i. L’integrale generale
dell’omogenea è:
                                yom (t) = c1 cos t + c2 sin t                         (50) Il termine noto f (t) = t2 cos t è del tipo associato al numero complesso α+iβ =
0 + 1i = i. Siccome i è radice del polinomio caratteristico con molteplicità µ = 1, la
soluzione particolare dovrà essere cercata nella forma:

                   yp (t) = t1 (At2 + Bt + C) cos t + (Dt2 + Et + F ) sin t
                                                                             
                                                                                          (51)

Derivando due volte ed uguagliando i termini, si calcoleranno le costanti.
    Nel testo si fa un altro esempio in cui f (t) = t2 per risolverlo a passi.
Se il termine noto fosse solo t2 , allora α = 0, che non è radice di λ2 + 1 = 0 (µ = 0). Dunque per y ′′ + y = t2 si cercherebbe yp (t) = At2 + Bt + C.


5       Sistemi di Equazioni Differenziali del Primo Ordine
Un sistema differenziale del primo ordine in forma normale si scrive in notazione vettoriale
come:
                                        y′ = f (y, t)                                  (52) dove y ∈ Rn , e f : D × I → Rn con D ⊆ Rn aperto e I ⊆ R intervallo.

                                                  10


<!-- nuova pagina -->

Teorema 5.1 (Esistenza e Unicità Locale e Globale). Sia I intervallo aperto, D ⊆ Rn
aperto e f ∈ C 0 (D × I). Allora ∀t0 ∈ I, ∀y0 ∈ D, esiste un intervallo J ⊆ I
contenente t0 in cui è definita una soluzione del Problema di Cauchy:
                                      (
                                        y′ = f (y, t)
                                                                                     (53)
                                        y(t0 ) = y0
                                                     ∂fi Se inoltre le derivate parziali ∂y    j
                                                         sono continue (condizione che implica
la locale lipschitzianità), la soluzione è unica.
    Esistono condizioni per garantire la soluzione globale, ovvero che J = I. Questo
avviene ad esempio se valgono condizioni di sublinearità rispetto a y:
                         ∥f (y, t)∥ ≤ α(t) + β(t)∥y∥     ∀y ∈ D, ∀t ∈ I                       (54) con α, β funzioni continue e non negative.
                    (
                      y ′ = t2 sin y + et y
Esempio 5.1. 1). La funzione f (y, t) = t2 sin y +et y
                      y(t0 ) = y0
è di classe C. Inoltre |f (y, t)| ≤ t2 + et |y|, rispettando la sublinearità. Il
               1

problema
       ( ammette soluzione unica globale definita su tutto R.
         y′ = y2
    2). Qui f (y, t) = y 2 ∈ C 1 , quindi la soluzione locale esiste ed
         y(0) = 1
è unica. Tuttavia, y 2 cresce più che linearmente (non vale la sublinearità). La soluzione y(t) = 1−t     ”esplode” a t = 1, perciò non è globale su R.

5.1     Sistemi Lineari
Un sistema lineare si presenta nella forma:
                                       y′ = A(t)y + b(t)                                      (55) dove A(t) ∈ Mn×n e b(t) ∈ Rn con componenti continue sull’intervallo I. Per i sistemi lineari, la condizione di sublinearità è implicitamente
soddisfatta (poiché ∥A(t)y∥ ≤ ∥A(t)∥∥y∥).
Corollario 5.1. Il problema di Cauchy associato ad un sistema lineare ammette un’unica
soluzione globale definita su tutto l’intervallo I in cui sono definite e continue A(t) e b(t).
    Si applica il Principio di Sovrapposizione. Lo spazio delle soluzioni dell’omogenea
associata y′ = A(t)y è uno spazio vettoriale di dimensione n. Siano φ1 (t), . . . , φn (t)
soluzioni linearmente indipendenti, esse formano una base. Ogni soluzione dell’omogenea
si scrive come:
                              y(t) = c1 φ1 (t) + · · · + cn φn (t)                    (56)
Si definisce Matrice Fondamentale per il sistema, W (t), la matrice n × n le cui colonne
sono i vettori base:                                     
                           W (t) = φ1 (t) | . . . | φn (t)                           (57)
In forma matriciale, la soluzione generica dell’omogenea è y(t) = W (t)c con c ∈ Rn . Per
il Problema di Cauchy y(t0 ) = y0 , imponendo W (t0 )c = y0 , si ricava il vettore delle
costanti c = W −1 (t0 )y0 . La soluzione al problema è dunque:
                                    y(t) = W (t)W (t0 )−1 y0                                  (58)

                                                11


<!-- nuova pagina -->

Per la non omogenea (b(t) ̸= 0), nota la matrice W (t), si sfrutta il metodo di Variazione
delle Costanti, cercando una soluzione del tipo yp (t) = W (t)k(t).

5.2     Sistemi Lineari Omogenei a Coefficienti Costanti
Se la matrice è costante (y′ = Ay con A ∈ Mn×n matrice di scalari), cerchiamo soluzioni
esponenziali del tipo:
                                       y(t) = veλt                                  (59)
Derivando, y′ = λveλt . Sostituendo nell’equazione:
                              λveλt = A(veλt ) =⇒ Av = λv                                (60)
Questa fondamentale relazione indica che λ deve essere un autovalore di A e v il cor-
rispondente autovettore. Gli autovalori si trovano calcolando le radici del polinomio
caratteristico:
                               P (λ) = det(A − λI) = 0                            (61)
   Ad ogni radice λ si associano:
   • ma (λ): molteplicità algebrica, ovvero quante volte la radice compare nella fattoriz-
     zazione di P (λ).
   • mg (λ): molteplicità geometrica, la dimensione dell’autospazio associato (dim(ker(A−
     λI))).
Risulta sempre 1 ≤ mg ≤ ma . Un autovalore si dice regolare se mg = ma . Se tutti gli
autovalori sono regolari, la matrice è diagonalizzabile , ed esiste una base di n autovettori
linearmente indipendenti, fornendo subito le n soluzioni necessarie φi (t) = vi eλi t .

5.2.1   Autovalori con Molteplicità Carente (Non Regolari)
Se un autovalore λ non è regolare (mg < ma ), mancano autovettori per completare la
base. In questo caso si ricercano gli autovettori generalizzati risolvendo successivi sistemi
lineari: Posto v(0) = v1 (l’autovettore canonico per cui (A − λI)v(0) = 0), si risolvono ”a
catena”:
                                    (A − λI)v(1) = v(0)                                  (62)
                                                 (2)         (1)
                                    (A − λI)v          =v                                (63)
                                                       ...
                                    (A − λI)v(j) = v(j−1)                                (64)
Le soluzioni associate a queste ”catene” contengono termini polinomiali in t:
                           w(0) (t) = v(0) eλt
                           w(1) (t) = v(1) + tv(0) eλt
                                                      
                                                                                         (65)
                                                          t2 (0) λt
                                                               
                            (2)          (2)        (1)
                           w (t) = v + tv + v                     e                      (66)
                                                          2
                                ...
                                         j
                                                        !
                                               l
                                        X    t
                           w(j) (t) =            v(j−l) eλt                              (67)
                                        l=0
                                             l!


                                                 12


<!-- nuova pagina -->

Queste funzioni sono linearmente indipendenti e completano la base della matrice fonda-
mentale.

5.2.2   Esempi Pratici sui Sistemi
Esempio 5.2 (Sistema 3 × 3 diagonalizzabile). Consideriamo il sistema:
             
                  ′
             y1 = y2 − y3
                                                          
                                                 0 1 −1
                y2′ = 2y1 + y2 + 6y3  =⇒ y′ = 2 1 6  y = Ay                            (68)
                                                  0 1 −1
             
              ′
                y = y2 − y3
                    3

Calcoliamo il polinomio caratteristico:
                                                
                               −λ       1   −1
          det(A − λI) = det  2 1 − λ        6 
                                0       1 −1 − λ
                                                                    
                       = −λ (1 − λ)(−1 − λ) − 6 − 2 1(−1 − λ) − (−1)(1)
                       = −λ(λ2 − 1 − 6) − 2(−λ − 1 + 1)
                       = −λ3 + 7λ + 2λ = −λ3 + 9λ
                       = −λ(λ − 3)(λ + 3)

Gli autovalori sono 0, 3, −3, tutti reali e distinti (quindi regolari, ma = mg = 1). Troviamo
i relativi autovettori:
    Per λ = 0: risolviamo Av1 = 0. Dalla prima e terza riga: x2 − x3 = 0 =⇒ x2 = x3 .
Dalla seconda: 2x1 + x2 + 6x3 = 0 =⇒         2x1 + 7x3 = 0. Scelto x3 = −2, otteniamo
                                           7
x1 = 7, x2 = −2. Autovettore v1 = −2.
                                          −2                                     
                                                         1                           1
    Con analoghi calcoli , si determinano v2 = 4 (per λ = 3) e v3 = −2 (per
                                                                                
                                                         1                           1
λ = −3).
    L’integrale generale è:
                                                           
                                     7            1              1
                        y(t) = c1 −2 + c2 4 e + c3 −2 e−3t
                                                   3t                                (69)
                                    −2            1              1
                                                                                           
                                                                                  1 1 0
Esempio 5.3 (Sistema con Autovalore Carente). Sia y′ = Ay con A =  0 0 1 
                                                                                 −1 3 −1
[Nota: l’elemento (3,3) in base al calcolo successivo del determinante deve essere −1 -
VERIFICARE] Il polinomio caratteristico è:

                          P (λ) = −λ3 + 4λ2 − 4λ = −λ(λ − 2)2                            (70)

Gli autovalori sono λ1 = 0 (ma = 1) e λ2 = 2 (ma = 2). Per λ2 = 2,       l’equazione
                                                                         1
(A − 2I)v = 0 porta ad un unico autovettore (a meno di multipli) v(0) = 1. Essendo
                                                                         2

                                             13


<!-- nuova pagina -->

la dimensione dell’autospazio 1 (mg = 1 < ma = 2), calcoliamo l’autovettore generalizzato
v(1) risolvendo (A − 2I)v(1) = v(0) :
                                                 
                               −1 1         0     x1        1
                              0 −2 1  x2  = 1                                    (71)
                               −1 3 −3            x3        2
                                                    
                                                     0
                                              (1)
Da cui x3 = 3, x2 = 1, x1 = 0, quindi v = 1. La terza soluzione fondamentale
                                                   
                                                     3
si costruisce come φ3 (t) = (v(1) + tv(0) )e2t . L’integrale generale, inclusa la soluzione
dell’autovalore λ = 0, è:
                                                               
                                               1              t
                      y(t) = c1 φ1 (t) + c2 1 e2t + c3  1 + t  e2t                 (72)
                                               2           3 + 2t

6      Stabilità dei Punti di Equilibrio
Studiare la stabilità di un sistema significa capire come si comportano le soluzioni qualora
vengano perturbate lievemente dallo stato di equilibrio (soluzione stazionaria/costante).

Definizione 6.1 (Stabilità di Ljapunov e Stabilità Asintotica). Dato un sistema y′ =
f (y, t) con soluzione costante ỹ0 (ovvero f (ỹ0 , t) = 0), il punto di equilibrio ỹ0 è detto:

    • Stabile (secondo Ljapunov): se per ogni ε > 0, esiste un δ > 0 tale che per ogni
      condizione iniziale y0 con ∥y0 − ỹ0 ∥ < δ, la soluzione del problema di Cauchy y(t)
      soddisfa ∥y(t) − ỹ0 ∥ < ε per ogni t ≥ t0 .

    • Asintoticamente Stabile: se è stabile e inoltre le soluzioni tendono asintotica-
      mente al punto di equilibrio:
                                     lim y(t) = ỹ0                               (73)
                                            t→∞

Teorema 6.1 (Stabilità per Sistemi Lineari a Coefficienti Costanti). Sia y′ = Ay con
A matrice costante. L’origine y = 0 è un punto di equilibrio. La sua stabilità dipende
esclusivamente dal segno della parte reale degli autovalori λ della matrice A:

    1. L’origine è Asintoticamente Stabile se e solo se per ogni autovalore λ si ha
       Re(λ) < 0.

    2. L’origine è Stabile se per ogni autovalore Re(λ) ≤ 0 e, per gli eventuali autovalori
       che risiedono esattamente sull’asse immaginario (Re(λ) = 0), la loro molteplicità
       algebrica coincide con la molteplicità geometrica (sono regolari).

    3. L’origine è Instabile in tutti gli altri casi (esiste un autovalore con Re(λ) > 0,
       oppure esiste un autovalore immaginario puro con molteplicità carente).

Dimostrazione. La dimostrazione discende direttamente dalla forma delle soluzioni del
sistema lineare. Sappiamo che la generica soluzione associata ad un autovalore λ = α + iβ
è una combinazione lineare di termini del tipo tk eαt cos(βt) e tk eαt sin(βt). Se α = Re(λ) <
0, l’esponenziale decrescente e−|α|t ”domina” qualsiasi potenza tk , spingendo il termine a

                                               14


<!-- nuova pagina -->

zero per t → ∞ e garantendo la limitatezza globale, da cui l’asintotica stabilità. Se α = 0,
il termine esponenziale degenera in una costante (oscillazione pura dettata dalle funzioni
goniometriche). In tal caso, il termine rimane limitato solo se non sono presenti potenze
tk derivanti da blocchi carenti di Jordan. Questo richiede che l’autovalore sia regolare
(ma = mg , nessuna catena di autovettori generalizzati), da cui la semplice stabilità.

Esempio 6.1 (Oscillatore Armonico Smorzato). Consideriamo l’equazione y ′′ + ky ′ +
y = 0 dipendente dal parametro reale k. Per analizzarlo, convertiamolo nel sistema di
prim’ordine standard impostando y1 = y e y2 = y ′ :
                  (
                   y1′ = y2
                                           ′              
                                            y1       0    1    y1
                                     =⇒      ′     =                             (74)
                     ′
                   y2 = −y1 − ky2           y2       −1 −k     y2
                                                       
                                            −λ      1
Il polinomio caratteristico è P (λ) = det                = λ2 + kλ + 1 = 0. Le radici
                                             −1 −k − λ
(autovalori) sono:                             √
                                           −k ± k 2 − 4
                                    λ1,2 =                                        (75)
                                                2
Esaminiamo la stabilità al variare di k:

   • Se k > 0, l’attrito disperde energia. Se k ≥ 2, le radici sono reali e negative. Se
     0 < k < 2, le radici sono complesse coniugate con parte reale −k/2 < 0. In entrambi
     i casi Re(λ) < 0, l’origine è Asintoticamente Stabile.

   • Se k = 0, l’equazione è y ′′ + y = 0 (moto puramente armonico). Gli autovalori sono
     λ = ±i, con Re(λ) = 0. Essendo semplici e distinti (quindi regolari), il sistema è
     semplicemente Stabile. Le traiettorie nello spazio delle fasi (y1 , y2 ) sono ellissi chiuse
     (orbite periodiche).

   • Se k < 0, la parte reale è positiva per almeno una radice. L’origine è un nodo o
     fuoco Instabile (il sistema immette energia divergendo progressivamente).




                                              15


<!-- nuova pagina -->
```
