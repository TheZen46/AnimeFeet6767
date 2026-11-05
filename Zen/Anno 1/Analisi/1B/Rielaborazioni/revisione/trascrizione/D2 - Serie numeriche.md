# D2 - Serie numeriche

Testo estratto da `Rielaborazioni/ANALISI_SerieNumeriche_260613_000338.pdf` (dispensa battuta, 2026) con `pdftotext -layout`. Le formule sono rese in modo approssimato dall'estrazione: per la lettura esatta fa fede il PDF. Tolti 79 rimandi `[cite: …]` e due numeri di matricola. Nessun'altra modifica.

```text
Teoria delle Serie Numeriche
         Parte I & II


      Appunti Universitari Rielaborati
             [matricola tolta] [matricola tolta]


<!-- nuova pagina -->

Indice

1 Introduzione alle Serie Numeriche                                                                3
  1.1 Definizioni Fondamentali . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     3
  1.2 Comportamento di una Serie . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         3
       1.2.1 Esempi Introduttivi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       4

2 Serie Notevoli ed Esempi Fondamentali                                                           6
  2.1 La Serie Geometrica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     6
  2.2 Le Serie Telescopiche e di Mengoli . . . . . . . . . . . . . . . . . . . . . . . . . .      7

3 Proprietà Fondamentali delle Serie                                                               9
  3.1 Invarianza Asintotica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    9
  3.2 Condizione Necessaria per la Convergenza . . . . . . . . . . . . . . . . . . . . . .         9
  3.3 Il Resto N -esimo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   10

4 Serie a Termini Positivi e Relativi Criteri                                                     11
  4.1 Criterio del Confronto Diretto . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    11
  4.2 Criterio del Confronto Asintotico . . . . . . . . . . . . . . . . . . . . . . . . . . .     12
  4.3 Criterio Integrale (di Maclaurin-Cauchy) . . . . . . . . . . . . . . . . . . . . . . .      13
  4.4 Criterio del Rapporto e della Radice . . . . . . . . . . . . . . . . . . . . . . . . .      15

5 Serie a Termini di Segno Variabile                                                              16
  5.1 Convergenza Assoluta e Semplice . . . . . . . . . . . . . . . . . . . . . . . . . . .       16
  5.2 Serie a Segno Alterno: Criterio di Leibniz . . . . . . . . . . . . . . . . . . . . . .      17




                                                 2


<!-- nuova pagina -->

Capitolo 1

Introduzione alle Serie Numeriche

1.1     Definizioni Fondamentali
Lo studio delle serie numeriche rappresenta uno dei pilastri dell’Analisi Matematica, fornendo
gli strumenti necessari per dare un senso all’operazione di somma applicata a un numero infinito
di addendi.
     Data una successione
                                              {an }n∈N
di numeri reali, vogliamo definire rigorosamente il concetto di somma infinita dei suoi
termini. Consideriamo l’espressione formale:
                               ∞
                               X
                                      an = an0 + an0 +1 + an0 +2 + . . .
                               n=n0

dove n0 ∈ N indica l’indice di partenza (tipicamente 0 o 1).
    Poiché non è possibile sommare materialmente infiniti termini, si ricorre al concetto di limite.
È fondamentale, a tal proposito, notare l’analogia formale e concettuale che intercorre tra le serie
numeriche e gli integrali impropri.

Definizione 1.1 (Somma Parziale e Serie). Si definisce successione delle somme parziali (o
ridotte) la successione
                                        {SN }
così costruita:
                                      N
                                      X
                             SN :=           an = an0 + an0 +1 + · · · + aN
                                      n=n0

La serie numerica è fondamentalmente definita come il limite per N → ∞ di tale successione:
                                     X∞
                                          an = lim SN
                                                         N →∞
                                          n=n0


1.2     Comportamento di una Serie
Il carattere di una serie numerica è determinato esclusivamente dal comportamento del limite del-
le sue somme parziali. A priori, essendo un limite, si presentano esattamente tre possibilità:

                                                     3


<!-- nuova pagina -->

  1. Serie Convergente: Il limite delle somme parziali esiste ed è un numero finito.
     In tal caso, diciamo che la serie è convergente e tale limite è detto il "valore della
     serie".

  2. Serie Divergente: Il limite delle somme parziali esiste ma vale

                                                           +∞

      o
                                                           −∞. In tal caso, diciamo che la serie è divergente e scriveremo
                                                   ∞
                                                   X
                                                          an = ±∞
                                                   n=n0.

  3. Serie Indeterminata (o Irregolare): Il limite per N → ∞ della successione SN non
     esiste. In tal caso, diciamo che la serie è indeterminata.

1.2.1      Esempi Introduttivi
Analizziamo alcuni casi elementari per applicare direttamente la definizione appena introdotta.

Esempio 1.1 (Serie Divergente a +∞). Sia data la successione costantemente uguale a 1, ovvero

                                                    an = 1

per ogni
                                                    n≥1
. Calcoliamo le ridotte:
                                          N
                                          X
                                  SN =                     {z· · · + 1} = N
                                                1 = 1| + 1 +
                                          n=1              N volte

Passando al limite si ottiene:
                                  ∞
                                  X
                                        1 = lim SN = lim N = +∞
                                            N →∞            N →∞
                                  n=1

Pertanto, questa serie diverge positivamente.

Esempio 1.2 (Serie di Grandi - Indeterminata). Consideriamo la successione a segni alterni

                                                 an = (−1)n

per
                                                    n≥0
. Calcoliamo le somme parziali:
                                  N
                                  X
                           SN =         (−1)n = 1 − 1 + 1 − 1 + · · · + (−1)N
                                  n=0


                                                       4


<!-- nuova pagina -->

Raggruppando i termini, notiamo che:
                                         (
                                          1 se N è pari
                                    SN =
                                          0 se N è dispari

Poiché la successione assume indefinitamente i valori 0 e 1, il limite

                                              lim SN
                                             N →∞

non esiste e, di conseguenza, la serie
                                            ∞
                                            X
                                                (−1)n
                                            n=0

è indeterminata.




                                                  5


<!-- nuova pagina -->

Capitolo 2

Serie Notevoli ed Esempi Fondamentali

2.1    La Serie Geometrica
In generale, possiamo considerare la serie di termine generale
                                                 an = q n
per
                                                  q∈R
, detta serie geometrica di ragione q. Questa è una delle pochissime serie di cui è
possibile calcolare esplicitamente la somma in forma chiusa.
    Calcoliamo la somma parziale N -esima:
                                       N
                                       X
                                SN =         qn = 1 + q + q2 + · · · + qN
                                       n=0

Per calcolare questo polinomio, moltiplichiamo e dividiamo l’espressione per 1 − q (assumendo
temporaneamente q ̸= 1):
                                                                      1−q
                                SN = (1 + q + q 2 + · · · + q N ) ·
                                                                      1−q
Svolgendo il prodotto al numeratore si osserva una massiccia cancellazione dei termini (proprietà
telescopica intrinseca del prodotto):
                   (1 + q + q 2 + · · · + q N ) − (q + q 2 + q 3 + · · · + q N +1 )   1 − q N +1
            SN =                                                                    =
                                                1−q                                     1−q
    Adesso siamo in grado di analizzare il comportamento della serie geometrica studiando il
limite di SN , che dipende dal valore della base q:

                                                                 se |q| < 1
                                                    1
                        ∞                   N +1    1−q
                                                   
                       X
                            n         1−q
                           q = lim               = +∞            se q > 1
                                N →∞    1−q
                                                      non esiste se q ≤ −1
                                                   
                       n=0                         

Nel caso in cui q = 1, la formula trovata perde significato (forma 00 ). Tuttavia, per q = 1, la
serie si riduce a                       X        X
                                           1n =      1
che, come abbiamo già dimostrato, diverge a +∞.

                                                     6


<!-- nuova pagina -->

Esempio 2.1 (Il paradosso di Zenone e la convergenza). Aggiungendo tutte le potenze di 12 , si
va a riempire l’intervallo (0, 2]. Esaminando la serie per q = 12 :

                                               1 1 1
                                        1+      + + + ...
                                               2 4 8 Essendo   1
                     2   < 1, applichiamo la formula risolutiva:
                                         ∞
                                         X 1               1
                                                     =          =2
                                         n=0
                                               2n        1 − 12

La serie converge a 2.




   [Spazio riservato a uno schema: Grafico della somma delle aree dei quadrati di lato √12n ,
         che illustra geometricamente come l’area totale converga al valore limite di 2,
                      corrispondente alla scomposizione di un rettangolo.]




           Figura 2.1: Rappresentazione geometrica della serie convergente          1/2n .
                                                                                P




2.2     Le Serie Telescopiche e di Mengoli
Un’altra famiglia di serie in cui è possibile calcolare il limite in modo analitico è quella delle
serie telescopiche. Si tratta di serie del tipo telescopico, ossia con termine generale an che si può
esprimere come una differenza della forma bn − bn+1 per qualche successione ausiliaria bn.
     Il prototipo di questa famiglia è la Serie di Mengoli :
                                               ∞
                                               X        1
                                                     n(n + 1)
                                               n=1 Possiamo scomporre il termine generale in fratti semplici:

                                              1      1  1
                                    an =            = −
                                           n(n + 1)  n n+1 Impostiamo il calcolo della successione delle somme parziali SN :
                                               N                    
                                               X   1        1
                                       SN =               −
                                                         n n+1
                                               n=1


                                                         7


<!-- nuova pagina -->

Scriviamo per esteso i primi termini per evidenziare la cancellazione:
                                                                       
                            1       1 1         1 1                 1      1
               SN = 1 −         +     −     +     −      + ··· +       −
                            2       2 3         3 4                N     N +1 Tutti i termini intermedi si elidono a vicenda (fenomeno telescopico), lasciando solo il
primo termine e l’ultimo:
                                                       1
                                          SN = 1 −
                                                     N +1
Passando al limite per la valutazione globale della serie, si ha:
                       ∞                                    
                       X        1                         1
                                     = lim SN = lim 1 −        =1
                             n(n + 1) N →∞     N →∞     N +1
                       n=1
    In generale, per qualunque serie in cui

                                           an = bn − bn+1

, risulta che
                                          SN = b1 − bN +1
. Ne consegue che se
                                              lim bn = L
                                              n→∞

(con L finito), allora la serie converge e vale

                                                  b1 − L. Se considerassimo un caso in cui, ad esempio,

                                            bn = − ln(n)

, le somme parziali diventerebbero

                       SN = b1 − bN +1 = − ln(1) + ln(N + 1) = ln(N + 1)

. Tale successione diverge a +∞ per N → ∞.




                                                    8


<!-- nuova pagina -->

Capitolo 3

Proprietà Fondamentali delle Serie

3.1    Invarianza Asintotica
Lo studio della convergenza è un’indagine sul comportamento "all’infinito". Ne discende una
proprietà cruciale: il comportamento (ossia la convergenza, la divergenza o l’indeterminazione)
non cambia se si aggiunge, si rimuove o si modifica un numero finito di termini.
Ovviamente, se la serie era inizialmente convergente, una perturbazione su un numero finito di
termini andrà a cambiare il valore numerico della somma, ma non altererà il fatto che essa risulti
convergente.


3.2    Condizione Necessaria per la Convergenza
Il seguente teorema rappresenta lo strumento più rapido e immediato per escludere a priori la
convergenza di innumerevoli serie.
Teorema 3.1 (Condizione Necessaria di Cauchy). Se una serie
                                              ∞
                                              X
                                                     an
                                              n=n0

è convergente, allora il suo termine generale è infinitesimo. In formule:

                                           lim an = 0
                                           n→∞ Tale condizione è necessaria ma non sufficiente ad assicurare la convergenza.
Dimostrazione. Supponiamo per ipotesi che la serie converga. Ciò equivale ad affermare che la
successione delle somme parziali SN converge a un limite reale e finito L:

                                        lim SN = L ∈ R
                                       N →∞

Osserviamo ora il termine generale aN . Per definizione di somma parziale, esso può essere
espresso come la differenza fra l’N-esima somma e la somma precedente:

                                        aN = SN − SN −1

Sfruttando l’algebra dei limiti, calcoliamo il limite per N → ∞:

              lim aN = lim (SN − SN −1 ) = lim SN − lim SN −1 = L − L = 0
             N →∞        N →∞                   N →∞       N →∞


                                                 9 Quindi, la serie converge implica

                                               an → 0

.

    Si rimarca come tale condizione non garantisca la convergenza. Un controesempio classico è
la serie armonica                            X1
                                                 n
, la quale possiede il termine generale tendente a zero (1/n → 0), ma come dimostreremo nel
capitolo successivo, la serie diverge a +∞.


3.3     Il Resto N -esimo
Se una serie
                                               ∞
                                               X
                                                       an
                                               n=n0

è convergente, possiamo definire la porzione "rimanente" della serie dal termine N -esimo in poi,
chiamata Resto. Definiamo il resto di ordine N come:
                                                   ∞
                                                   X
                                         RN =               an
                                                  n=N +1 Una diretta conseguenza della definizione di convergenza è che l’errore commesso
nell’approssimare la serie totale con una somma parziale tende a svanire all’aumentare dei termini;
pertanto:
                                            lim RN = 0
                                           N →∞




                                                  10


<!-- nuova pagina -->

Capitolo 4

Serie a Termini Positivi e Relativi
Criteri

Si definisce "serie a termini positivi" una serie
                                               X
                                                    an

tale per cui il termine generale an risulti maggiore o uguale a zero definitivamente. Formalmente:
se
                                               an ≥ 0
per un qualche n ≥ n, allora la serie:
                                                ∞
                                                X
                                                        an
                                                n=n0

converge oppure diverge a +∞.
    Il motivo di questo comportamento risiede nella monotonia: le somme parziali SN sono
crescenti per N ≥ n (poiché stiamo aggiungendo quantità non negative) e quindi, per il teorema
sulle successioni monotone, SN ammette necessariamente un limite, che sarà finito o +∞. Non esistono serie a termini positivi indeterminate.


4.1    Criterio del Confronto Diretto
Il principio su cui si basa questo criterio è l’idea che se una serie "piccola" diverge a infinito,
a maggior ragione lo farà una serie più "grande". E viceversa, se una "grande" ha una somma
finita, quella più "piccola" non potrà divergere.

Teorema 4.1 (Criterio del Confronto). Siano

                                                   an

e
                                                   bn
due successioni tali che esista un n per cui:

                                       0 ≤ an ≤ bn           ∀n ≥ n Allora valgono le seguenti implicazioni:

                                                   11


<!-- nuova pagina -->

   • Se la serie minorante diverge:
                                     ∞
                                     X                           ∞
                                                                 X
                                            an = +∞ =⇒                  bn = +∞
                                     n=n0                        n=n0
   • Se la serie maggiorante converge:
                                    ∞
                                    X                            ∞
                                                                 X
                                          bn converge =⇒                an converge
                                  n=n0                           n=n0
Esempio 4.1. Dimostriamo per confronto una notevole disuguaglianza basata sulla serie di
Mengoli appena vista. Sappiamo che la serie
                                       X    1
                                                    n(n + 1)
converge. Osserviamo la successione
                                                     1
                                                     n2
. Si verifica analiticamente che:
                                          1       2
                                             ≤                  ∀n ≥ 1
                                          n2   n(n + 1) Poiché la serie maggiorante è proporzionale alla serie di Mengoli:
                            ∞                       ∞
                            X        2        X    1
                                           =2            =2·1=2
                                  n(n + 1)      n(n + 1)
                            n=1                     n=1

(che converge). Ne deduciamo, per il Criterio del Confronto, che anche
                                                    ∞
                                                    X 1
                                                          n2
                                                    n=1
                                               2
converge (è noto che il valore esatto è π6 , ma non occorre calcolarlo col criterio).


4.2     Criterio del Confronto Asintotico
Nella pratica, il confronto diretto risulta spesso impervio a causa delle difficoltà algebriche nel
risolvere la disequazione an ≤ bn . Si preferisce ricorrere ai limiti.
Teorema 4.2 (Criterio del Confronto Asintotico). Si supponga che an ≥ 0 e bn > 0 per n ≥
n. Se il limite del rapporto esiste finito e strettamente positivo:
                                          an
                                    lim        =L    con 0 < L < +∞
                                    n→∞ bn

Allora le due serie condividono lo stesso carattere (se una converge, l’altra converge; se una
diverge, l’altra diverge):
                              ∞
                              X                                ∞
                                                               X
                                    an converge ⇐⇒                    bn converge
                             n=n0                              n=n0


                                                     12


<!-- nuova pagina -->

Esempio 4.2 (Funzioni razionali). Si studi il comportamento della serie con termine generale
                                                     n+3
                                             an =
                                                    2n2 + 5
per n ≥ 0. Evidentemente an ≥ 0 per ogni n ≥ 0. All’infinito, il numeratore
si comporta come n e il denominatore come n2 . Ciò suggerisce che an abbia lo stesso ordine di
grandezza di 1/n. Scegliamo quindi la successione di confronto
                                                         1
                                                 bn =
                                                         n
(la quale genera la ben nota Serie Armonica, divergente a +∞). Eseguiamo il limite
del rapporto:
                                     an            n+3        1
                                lim     = lim n · 2         =
                               n→∞ bn    n→∞      2n + 5      2 Poiché L = 1/2 ̸= 0 ed è finito, le serie condividono il carattere. Dal
momento che                                 X
                                               bn
diverge, per il criterio asintotico anche           X
                                                        an
diverge a +∞.
Esempio 4.3 (Sviluppi di Taylor e limiti notevoli). Consideriamo la serie
                                         ∞      
                                       X          1
                                           sin
                                                 n2
                                              n=1. Per n ≥ 1, l’argomento del seno è nell’intervallo (0, 1], dove la funzione seno è
strettamente positiva. Quindi an ≥ 0. Confrontiamo con bn = n12 avvalendoci del limite notevole
limx→0 sinx x = 1:
                                         sin(1/n2 )
                                     lim            = 1 ̸= 0
                                    n→∞     1/n2 Poiché la serie 1/n2 converge (come visto in precedenza), la serie originaria converge
                           P
anch’essa.


4.3     Criterio Integrale (di Maclaurin-Cauchy)
Questo ponte teorico tra la matematica del discreto e del continuo risulta estremamente efficace
quando la successione originaria può essere facilmente considerata come il campionamento di una
funzione di cui si sappia agevolmente calcolare l’integrale.
Teorema 4.3 (Criterio Integrale). Sia
                                            f : [n0 , +∞) → R
una
P funzione positiva e debolmenteR    decrescente per x ≥ n0. Allora la serie numerica
  f (n) e l’integrale improprio f (x)dx posseggono lo stesso carattere:
                          X∞                       Z ∞
                              f (n) converge ⇐⇒        f (x)dx converge
                          n=n0                               n0

                                                    13


<!-- nuova pagina -->

Dimostrazione. L’idea geometrica è chiara se sovrapponiamo al grafico decrescente di f (x) i
rettangoli
R∞         di base 1 e altezza f (n). L’area esatta sottesa dalla funzione è data dall’integrale
 n0 f (x)dx. Possiamo costruire dei rettangoli che sovrastimano l’area della funzione,
spostandoci "a sinistra", o dei rettangoli che la sottostimano,   spostandoci
                                                                        P∞ "a destra".          L’area
totale dei rettangoli inscritti è data dalla somma ∞
                                                    P                                
                                                      n=n0 +1 f (n) =      n=n0 f (n)   − f (n 0 ). Per costruzione geometrica, questa area risulta inferiore all’integrale definito:

                                        ∞
                                        X                 Z ∞
                                                f (n) ≤          f (x)dx
                                      n=n0 +1               n0 Dall’altro lato, considerando i rettangoli circoscritti, si può dedurre la disuguaglianza
globale:
                              Z ∞               ∞
                                                X            Z ∞
                                   f (x)dx ≤        f (n) ≤        f (x)dx
                              n0 +1              n=n0 +1             n0

Questa catena dimostra formalmente che le due entità covariano, garantendo l’equivalenza di
comportamento.




     [Spazio riservato a uno schema: Rappresentazione grafica del Criterio Integrale. Sarà
    disegnata la curva decrescente y = f (x) con in evidenza i rettangoli superiori e inferiori
         di larghezza unitaria. L’area totale dei rettangoli rappresenterà visivamente la
      sommatoria della serie da confrontare con l’integrale improprio limitato dalla curva
                                             stessa.]




 Figura 4.1: L’area sottesa al grafico della funzione approssimata dalla somma dei rettangoli.

   Un’applicazione inestimabile del Criterio Integrale riguarda lo studio della convergenza della
Serie Armonica Generalizzata:
                                      ∞
                                      X         1
                                                           con α, β ∈ R
                                            nα (ln n)β
                                      n=2 Utilizzando la teoria degli integrali impropri, si dimostra che la serie converge se e
solo se:

   • α > 1 (indipendentemente da β);

   • α = 1 e contestualmente β > 1.

                                                     14


<!-- nuova pagina -->

4.4    Criterio del Rapporto e della Radice
Concludiamo la panoramica delle serie a termini positivi con due criteri classici.

Teorema 4.4 (Criterio del Rapporto e Criterio della Radice). Sia data una serie
                                                                                         P
                                                                                             an con
an > 0. Definiamo il limite L ∈ R ∪ {+∞} come:
                            an+1
                    L = lim       (Criterio del Rapporto o di D’Alembert)
                       n→∞ an
                            √
                    L = lim n an (Criterio della Radice o di Cauchy)
                        n→∞

Sulla base del valore di L, si deduce che:

   • Se L < 1, la serie
                         P
                            an converge.

   • Se L > 1 (o L = +∞), la serie
                                       P
                                           an non converge (diverge a +∞).

   Sulla base del valore di L, si deduce che:

   • Se L < 1, la serie    an converge.
                        P

   • Se L > 1 (o L = +∞), la serie      an non converge (diverge a +∞).
                                      P

Osservazione 4.1. Se risulta L = 1, il criterio non conclude (caso dubbio). In tal
frangente, per serie complesse che includono fattoriali, può essere utile avvalersi della formula di
approssimazione di Stirling
                                            √        n n
                                        n! ∼ 2πn ·
                                                      e
per proseguire lo studio congiuntamente al criterio del confronto asintotico.




                                                15


<!-- nuova pagina -->

Capitolo 5

Serie a Termini di Segno Variabile

Rimuovendo l’ipotesi della positività, le serie possono contenere un’alternanza irregolare o strut-
turata di segni algebrici. In questo contesto, non potendosi appoggiare ai lemmi sulle successioni
crescenti, la teoria si ramifica.


5.1    Convergenza Assoluta e Semplice
Definizione 5.1 (Convergenza Assoluta). Si supponga che la serie dei moduli
                                             ∞
                                             X
                                                    |an |
                                             n=n0

converga. Allora necessariamente converge anche la serie originaria senza modulo
                                              ∞
                                              X
                                                       an
                                             n=n0

. In tal caso diciamo che la serie converge Assolutamente.

Osservazione 5.1. Per distinguere il tipo di convergenza ottenuto, qualora una serie non converga
assolutamente ma risulti comunque convergente in virtù di cancellazioni strutturate, si dirà che
tale serie converge semplicemente.

Esempio 5.1. Studiare il comportamento della serie trigonometrica:
                                            ∞
                                            X cos(n)
                                                    n2
                                            n=1 Il numeratore cos(n) assume valori sia positivi che negativi con andamento irregolare,
rendendo la serie non a termini positivi. Passiamo perciò allo studio della convergenza assoluta,
aggiungendo il valore assoluto. Maggioriamo il termine generale sapendo che la funzione coseno
è limitata:
                                     cos(n)     |cos(n)|     1
                                         2
                                             =       2
                                                         ≤ 2
                                       n           n         n Poiché la serie maggiorante
                                              ∞
                                              X 1
                                                    n2
                                              n=1


                                                  16


<!-- nuova pagina -->

converge, dal criterio del confronto diretto la serie dei moduli converge. Di conseguenza,
la serie originale
                                               ∞
                                              X    cos(n)
                                                     n2
                                            n=1

converge assolutamente (e quindi converge).


5.2     Serie a Segno Alterno: Criterio di Leibniz
Un sottoinsieme molto speciale delle serie a segno variabile è costituito dalle serie in cui il segno
oscilla regolarmente da positivo a negativo a ogni iterazione:
                                            ∞
                                            X
                                                  (−1)n bn
                                           n=n0

con la parte in modulo bn ≥ 0.

Teorema 5.1 (Criterio di Leibniz per serie a segno alterno). Data la serie
                                            ∞
                                            X
                                                  (−1)n bn
                                           n=n0. Se sono simultaneamente rispettate le seguenti tre condizioni:

  1. bn ≥ 0    ∀n (i termini senza segno sono non negativi)

  2. La successione bn è monotona decrescente, ossia bn+1 ≤ bn per ogni n (o definitivamente)

  3. Il limite della successione all’infinito è zero: limn→∞ bn = 0

Allora la serie converge (almeno semplicemente).

    Inoltre, questo teorema (che omettiamo di dimostrare per brevità formale, pur essendo radi-
cato nella teoria della convergenza degli intervalli annidati) garantisce una stima eccezionale del
resto: il modulo del resto troncato al termine N -esimo non supera mai, in grandezza, il modu-
lo del primissimo termine trascurato, ovverosia bN +1 . Questo rende le serie verificanti Leibniz
preziosissime dal punto di vista dell’analisi numerica.




                                                  17


<!-- nuova pagina -->
```
