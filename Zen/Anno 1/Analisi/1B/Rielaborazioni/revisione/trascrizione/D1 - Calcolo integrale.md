# D1 - Calcolo integrale

Testo estratto da `Rielaborazioni/ANALISI_CalcoloIntegrale_260612_235414.pdf` (dispensa battuta, 2026) con `pdftotext -layout`. Le formule sono rese in modo approssimato dall'estrazione: per la lettura esatta fa fede il PDF. Tolti 178 rimandi `[cite: …]` e due numeri di matricola. Nessun'altra modifica.

```text
          Dispensa di Analisi Matematica
             Calcolo Integrale: Teoria, Metodi e Applicazioni

                  Materiale Didattico Rielaborato da [matricola tolta] e [matricola tolta]

                                          12 giugno 2026


Indice
1 Primitive e Integrali Indefiniti                                                                   2
  1.1 Definizione di Primitiva . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       2
  1.2 L’Integrale Indefinito . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     2
  1.3 Tabella delle Primitive Fondamentali . . . . . . . . . . . . . . . . . . . . . . . . .         3

2 Proprietà e Metodi di Integrazione                                                                 3
  2.1 Proprietà di Linearità . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       4
      2.1.1 Primitive di funzioni definite a tratti . . . . . . . . . . . . . . . . . . . . .        4
  2.2 Integrazione per Parti . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       5
  2.3 Integrazione per Sostituzione . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        5
  2.4 Integrazione di Funzioni Razionali . . . . . . . . . . . . . . . . . . . . . . . . . .         6

3 Integrali Definiti secondo Riemann                                                                 7
  3.1 Partizioni e Somme di Riemann . . . . . . . . . . . . . . . . . . . . . . . . . . . .          7
  3.2 Definizione di Integrabilità . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     8
  3.3 Proprietà dell’Integrale Definito . . . . . . . . . . . . . . . . . . . . . . . . . . . .      9
  3.4 Teorema della Media Integrale . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        9

4 Teorema Fondamentale del Calcolo Integrale                                                        10
  4.1 Funzione Integrale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      10
  4.2 Il Teorema Fondamentale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         10
  4.3 Teoremi di integrazione definita . . . . . . . . . . . . . . . . . . . . . . . . . . . .      12

5 Integrali Impropri (o Generalizzati)                                                              12
  5.1 A. Integrali su intervalli illimitati . . . . . . . . . . . . . . . . . . . . . . . . . . .   12
       5.1.1 Esempi Notabili su Intervalli Illimitati . . . . . . . . . . . . . . . . . . . .       13
  5.2 Criteri di Convergenza . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      14
  5.3 B. Integrali Impropri per Funzioni Illimitate . . . . . . . . . . . . . . . . . . . . .       15
       5.3.1 Criteri di Convergenza per Funzioni Illimitate . . . . . . . . . . . . . . . .         15




                                                  1


<!-- nuova pagina -->

1     Primitive e Integrali Indefiniti
Il calcolo integrale rappresenta, insieme al calcolo differenziale, uno dei due pilastri fondamentali
dell’Analisi Matematica. In questa prima sezione, affronteremo il problema inverso della
derivazione: data una funzione, vogliamo determinare una nuova funzione la cui derivata coincida
con la funzione di partenza. Questo processo è noto come ricerca della primitiva.

1.1    Definizione di Primitiva
Definizione 1.1 (Primitiva di una funzione). Sia I ⊆ R un intervallo e sia f : I → R una
funzione. Diciamo che una funzione F è una primitiva di f sull’intervallo I se F è
derivabile su I e risulta:
                                   F ′ (x) = f (x) ∀x ∈ I
                                                                                                   2
Esempio 1.1. Consideriamo la funzione f (x) = x definita su tutto R. La funzione F (x) = x2
è una primitiva di x su R. Infatti, applicando le regole di derivazione, si ottiene:
                                         2
                                    d    x     2x
                                             =    = x ∀x ∈ R
                                   dx     2     2
                                                            2 Tuttavia, si noti che anche la funzione F1 (x) = x2 + 1 è una primitiva di f (x), poiché la
derivata di una costante è nulla.

Esempio 1.2. Sia f (x) = sin x. La funzione F (x) = − cos x è una primitiva di sin x su R. Infatti, dx
               d
                 (− cos x) = sin x.

Osservazione 1.1 (Insieme delle primitive). Come intravisto nell’esempio precedente, se F è
una primitiva di f in un intervallo I, allora anche la funzione F (x) + c (con c ∈ R costante
arbitraria) lo è. Questo deriva dalla linearità della derivata e dal fatto che la derivata
di una costante è zero.
    Viceversa, se F e G sono due primitive della stessa funzione f sull’intervallo I, allora esse
differiscono necessariamente per una costante. Ovvero, esiste c ∈ R tale che F (x) −
G(x) = c per ogni x ∈ I.

Dimostrazione. Poniamo H(x) = G(x) − F (x). Poiché sia F che G sono primitive di f ,
derivando H otteniamo:

                       H ′ (x) = G′ (x) − F ′ (x) = f (x) − f (x) = 0 ∀x ∈ I Essendo la derivata identicamente nulla su un intervallo connesso I, segue dal Teorema
di Lagrange che H(x) è una funzione costante, ossia H(x) = c. Pertanto, G(x) =
F (x) + c.

1.2    L’Integrale Indefinito
Definizione 1.2 (Integrale Indefinito). L’insieme di tutte le primitive di una funzione f su un
intervallo I prende il nome di integrale indefinito di f. Esso si indica con la
notazione:                                Z
                                             f (x) dx


                                                 2 Se F è una primitiva particolare di f , scriveremo:
                                 Z
                                   f (x) dx = F (x) + c (x ∈ I)

Osservazione 1.2. È importante sottolineare che non tutte le funzioni ammettono una pri-
mitiva. Come vedremo in seguito, la continuità è una condizione sufficiente (ma non
necessaria) per l’esistenza della primitiva.

1.3    Tabella delle Primitive Fondamentali
Di seguito elenchiamo le primitive delle funzioni elementari più comuni. Tali formule derivano
direttamente dall’inversione delle regole di derivazione.

    • Potenze:
                                          xα+1
                            Z
                                xα dx =        + c (α ̸= −1, x ∈ dom(xα ))
                                          α+1

    • Funzione reciproca (α = −1):         Z
                                               1
                                                 dx = ln |x| + c
                                               x

    • Funzioni trigonometriche:
                           Z
                              sin x dx = − cos x + c (I = R)
                           Z
                              cos x dx = sin x + c (I = R)
                         Z
                                1
                                    dx = tan x + c
                             cos2 x

    • Funzione esponenziale:          Z
                                          ex dx = ex + c (I = R)

    • Funzioni iperboliche e inverse trigonometriche:
                        Z
                              1
                                   dx = arctan x + c
                           1 + x2
                      Z
                             1
                         √         dx = arcsin x + c (I =] − 1; 1[)
                           1 − x2

2     Proprietà e Metodi di Integrazione
Calcolare un integrale indefinito richiede non solo la conoscenza delle primitive fondamentali,
ma anche l’applicazione di specifiche proprietà algebriche e teoremi che consentono di ricondurre
funzioni complesse a casi elementari.

                                                  3


<!-- nuova pagina -->

2.1     Proprietà di Linearità
Teorema 2.1 (Linearità dell’integrale). Se f e g ammettono primitive su un intervallo I e
α, β ∈ R sono costanti arbitrarie, allora la combinazione lineare αf + βg ammette
primitiva su I. Inoltre vale la relazione:
                       Z                            Z             Z
                          (αf (x) + βg(x)) dx = α f (x) dx + β g(x) dx

Dimostrazione. Siano F e G le primitive di f e g rispettivamente. Vogliamo mostrare che αF +βG
è una primitiva per αf + βg. Derivando otteniamo:

                     d
                       [αF (x) + βG(x)] = αF ′ (x) + βG′ (x) = αf (x) + βg(x)
                    dx Questo dimostra l’asserto.

Esempio 2.1. Calcoliamo il seguente integrale utilizzando la linearità:
                                      Z
                                        (5x2 + ex ) dx Per la proprietà appena dimostrata:
                                 Z          Z
                                                 5
                              = 5 x2 dx + ex dx = x3 + ex + c
                                                 3

2.1.1    Primitive di funzioni definite a tratti
La ricerca di primitive per funzioni definite a tratti richiede particolare attenzione alla condizione
di continuità e derivabilità della primitiva nell’intervallo globale.

Esempio 2.2. Consideriamo la funzione f (x) = sin |x| definita su R. Essa si esplicita
come:                                  (
                                         sin x    se x > 0
                               f (x) =
                                         − sin x se x < 0 Se esiste una primitiva F , essa deve valere:
                                           (
                                            − cos x + c1    se x > 0
                                 F (x) =
                                            cos x + c2      se x < 0 Affinché F sia una primitiva su tutto R, deve essere derivabile, e quindi necessaria-
mente continua in x = 0. Imponiamo la continuità in zero:

                                  F (0) = lim F (x) = lim F (x)
                                          x→0+             x→0− Calcolando i limiti: limx→0+ (− cos x+c1 ) = −1+c1 limx→0− (cos x+c2 ) =
1 + c2 Uguagliando si ottiene −1 + c1 = 1 + c2 , da cui c1 = 2 + c2.
Scegliendo ad esempio c2 = c, avremo c1 = c + 2.

                                                  4


<!-- nuova pagina -->

                         (
                          0 se x < 0
Esempio 2.3. Sia f (x) = La primitiva generale assumerebbe la
                          x se x ≥ 0
forma:                              (
                                      c1        se x < 0
                            F (x) = x2
                                       2 + c2 se x ≥ 0 Imponendo la continuità in x = 0, otteniamo c1 = c2 = c, restituendo così una
primitiva globalmente derivabile su R.

2.2    Integrazione per Parti
Teorema 2.2 (Integrazione per parti). Siano f, g due funzioni derivabili su un intervallo I. Supponiamo che il prodotto f ′ g ammetta una primitiva su I. Allora anche la funzione f g ′
ammette una primitiva in I e vale la formula:
                        Z                             Z
                           f (x)g (x) dx = f (x)g(x) − f ′ (x)g(x) dx
                                 ′

Dimostrazione. Sia H una primitiva di f ′ g. Sappiamo per la regola di derivazione del prodotto
che:
                              d
                                [f (x)g(x)] = f ′ (x)g(x) + f (x)g ′ (x)
                             dx Integrando ambo i membri rispetto a x, si ricava la tesi isolando f g ′ dx.
                                                                            R


Esempio 2.4. Calcoliamo ln x dx sull’intervallo ]0, +∞[. Consideriamo ln x = 1 · ln x,
                             R

scegliendo f (x) = ln x e g ′ (x) = 1. Di conseguenza, f ′ (x) = x1 e g(x) = x. Applicando la
formula:      Z                         Z                    Z
                                          1
                 1 · ln x dx = x ln x −     · x dx = x ln x − 1 dx = x ln x − x + c
                                          x

2.3    Integrazione per Sostituzione
Teorema 2.3 (Integrazione per sostituzione). Sia f integrabile in un intervallo J con primitiva
F. Sia φ una funzione derivabile su un intervallo I a valori in J. Allora la funzione
composta (f ◦ φ) · φ′ ha primitiva su I e vale:
                                Z
                                  f (φ(x))φ′ (x) dx = F (φ(x)) + c Equivalentemente, ponendo y = φ(x), si ha dy = φ′ (x) dx, e l’integrale diventa
  f (y) dy.

Dimostrazione. Per la regola di derivazione della funzione composta (chain rule):

                        d
                          [F (φ(x))] = F ′ (φ(x)) · φ′ (x) = f (φ(x)) · φ′ (x)
                       dx

                                                 5


<!-- nuova pagina -->

                                 2
Esempio 2.5. 1. Calcoliamo xex dx. Si nota che la derivata dell’esponente x2 è 2x.
                             R

Moltiplicando e dividendo per 2:
                                   Z
                                 1       2     1 2
                                     2xex dx = ex + c
                                 2             2
    2. Calcoliamo x+1 dx. Ponendo φ(x) = x + 1, da cui φ′ (x) = 1:
                 R 1

                               Z
                                   1
                                     dy       = ln |x + 1| + c
                                   y    y=x+1
    3. Calcoliamo tan x dx. Essendo tan x = cos  x , poniamo φ(x) = cos x =⇒ φ (x) =
                                                       sin x                            ′
                   R

− sin x.
                                           − sin x
                       Z                Z
                          sin x
                                dx = −             dx = − ln | cos x| + c
                          cos x             cos x       R ex
    4. Calcoliamo 1+e2x dx. Sia y = e , allora dy = e dx. L’integrale
                                                 x                 x

diventa:              Z
                            1
                                 dy = arctan y + c = arctan(ex ) + c
                         1 + y2

2.4    Integrazione di Funzioni Razionali
                                                      R P (x)
Ci proponiamo di calcolare gli integrali della forma Q(x)     dx, dove P e Q sono polinomi con
deg(P ) < deg(Q). Analizziamo il caso in cui il denominatore è di grado 1 o 2.
   Caso 1: Denominatore di primo grado
                                         Z
                                            Ax + B
                                                     dx
                                            Cx + D Si può procedere per manipolazione algebrica dividendo i polinomi o per sostituzione,
riconducendosi a funzioni lineari o logaritmiche.
    Caso 2: Denominatore di secondo grado Consideriamo l’integrale ax2 +bx+c      1
                                                                                      dx con a ̸=
                                                                            R

0. Lo studio si ramifica in base al discriminante ∆ = b − 4ac del denominatore.

   • Se ∆ > 0: Il polinomio ammette due radici reali distinte x1 , x2 . Si fattorizza ax2 +bx+c =
     a(x − x1 )(x − x2 ). Tramite la decomposizione in fratti semplici:
                                         1              α      β
                                                    =       +
                                 (x − x1 )(x − x2 )   x − x1 x − x2 Si ricavano α, β e si integra termine a termine ottenendo una
      combinazione di logaritmi:

                                    α ln |x − x1 | + β ln |x − x2 | + c

   • Se ∆ = 0: Il denominatore è un quadrato perfetto: (x − x0 )2. L’integrale assume
     la forma di una potenza con esponente −2.

                                                 6


<!-- nuova pagina -->

    • Se ∆ < 0: Il polinomio non ha radici reali. Si procede "completando il quadrato" al
      denominatore per ricondursi alla forma di un’arcotangente:
                                Z
                                          1
                                                2 dx =⇒ arctan(...)
                                    1 + x+...
                                            ...


3     Integrali Definiti secondo Riemann
L’integrale definito permette di formalizzare matematicamente il concetto intuitivo di "area
sottesa" dal grafico di una funzione in un intervallo chiuso.

3.1   Partizioni e Somme di Riemann
Definizione 3.1 (Partizione). Sia f : [a, b] → R una funzione limitata. Una parti-
zione P dell’intervallo [a, b] è un insieme finito di punti {x0 , x1 , . . . , xk } tali che:

                                       a = x0 < x1 < x2 < · · · < xk = b Questo insieme divide [a, b] in k sotto-intervalli
Ii = [xi−1 , xi ] di ampiezza li = xi − xi−1.




Figura 1: Rappresentazione grafica delle somme inferiori e superiori. Sull’asse delle ascisse è rappresentata una partizione a = x0 < x1 < x2 < x3 < x4 = b.
Sono tracciati due sistemi di rettangoli: uno interno alla curva della funzione (somme inferiori)
e uno esterno ad essa (somme superiori).


    Data una partizione P , definiamo le somme inferiori s− (f, P ) e le somme superiori
S + (f, P ) di f relative a P come:

                                 k 
                                 X                                    k 
                                                                       X              
                    −
                   s (f, P ) =          inf f (x) li   e S (f, P ) =
                                                           +
                                                                             sup f (x) li
                                        x∈Ii                                 x∈Ii
                                 i=1                                   i=1 Ovviamente, si ha sempre s− (f, P ) ≤ S + (f, P ).

                                                       7


<!-- nuova pagina -->

Osservazione 3.1 (Raffinamento di una partizione). Raffinando una partizione (ovvero aggiun-
gendo nuovi punti di suddivisione), le somme inferiori crescono (o restano invariate), mentre le
somme superiori decrescono. Se P ∗ è un raffinamento di P , si ha:
                                s− (P ) ≤ s− (P ∗ ) ≤ S + (P ∗ ) ≤ S + (P ) Date due partizioni qualsiasi P1 e P2 , considerando il loro raffinamento comune P1 ∪P2 ,
vale sempre la relazione:
                                       s− (f, P1 ) ≤ S + (f, P2 ) Questo implica che l’estremo superiore di tutte le somme inferiori è minore o
uguale all’estremo inferiore di tutte le somme superiori.

3.2    Definizione di Integrabilità
Definizione 3.2 (Integrabilità secondo Riemann). Sia f : [a, b] → R limitata. Diciamo
che f è integrabile secondo Riemann se il sup delle somme inferiori coincide con l’inf delle
somme superiori, calcolati al variare di tutte le possibili partizioni P di [a, b].
In tal caso, questo valore comune è indicato con il simbolo:
                                            Z b
                                                 f (x) dx
                                                  a
Esempio 3.1 (Funzione Costante). Sia f (x) = k (costante). Per ogni partizione
P = {x0 , . . . , xk }, su ogni Ii si ha inf f = sup f = k. Le somme inferiori saranno:
                                       k
                                       X                k
                                                        X
                          −
                         s (f, P ) =         k · li = k   (xi − xi−1 ) = k(b − a)
                                       i=1            i=1 Le somme superiori saranno anch’esse uguali a k(b − a). Pertanto, f è
             Rb
integrabile e a k dx = k(b − a).




Figura 2: Area del rettangolo descritto dalla funzione costante f (x) = k nell’intervallo [a, b].
L’integrale è esattamente l’area del rettangolo, base per altezza: k(b − a).


                                                         (
                                                          1 se x ∈ Q
Esempio 3.2 (Funzione di Dirichlet). Sia f (x) =                       in [a, b]. Per la
                                                          0 se x ∈/Q
densità di Q e R \ Q in R, in ogni sotto-intervallo Ii avremo sup f = 1 e inf f = 0.
Pertanto le somme superiori misurano sempre 1 · (b − a) e le somme inferiori 0. I due
estremi non coincidono, quindi la funzione di Dirichlet non è integrabile secondo Riemann.

                                                      8


<!-- nuova pagina -->

3.3   Proprietà dell’Integrale Definito
Se f e g sono funzioni integrabili su [a, b], l’operatore integrale gode delle seguenti proprietà:

   1. Additività rispetto all’intervallo: Per ogni [c, d] ⊆ [a, b], f è integrabile su [c, d]. Inoltre, per ogni punto intermedio, l’integrale totale è la somma degli integrali sui
      sotto-intervalli.
                   Rb              Rb      Rb
   2. Linearità: a (αf + βg) = α a f + β a g per ogni α, β ∈ R.

   3. Valore Assoluto: Anche |f | risulta integrabile su [a, b], e vale la disuguaglianza triango-
                                                                              Rb
      lare continua. In particolare, geometricamente, l’integrale a |f | rappresenta la
      somma delle aree assolute A+ + A− , dove A+ è l’area tra asse x e il grafico dove f ≥ 0, e
      A− dove f < 0.

   4. Modifica su insiemi finiti: Se g è integrabile su [a, b] e f (x) = g(x) eccetto in un numero
      finito di punti in [a, b], allora f è integrabile e i loro integrali coincidono.

    Le classi di funzioni garantite essere integrabili secondo Riemann in un intervallo chiuso e
limitato [a, b] sono:
   • Le funzioni continue (anche a tratti).

   • Le funzioni monotone (crescenti o decrescenti) e limitate.

3.4   Teorema della Media Integrale
Definizione 3.3 (Media integrale). Se f è integrabile su [a, b], definiamo la sua media integrale
su tale intervallo come:                    Z b
                                        1
                                                f (x) dx
                                      b−a a
Teorema 3.1 (Della media integrale). Sia f : [a, b] → R una funzione continua.
Allora esiste almeno un punto c ∈ [a, b] tale che il valore della funzione nel punto coincida con
la media integrale:
                                                  Z b
                                              1
                                   f (c) =            f (x) dx
                                            b−a a
Dimostrazione. Essendo f continua nel compatto [a, b], per il Teorema di Weierstrass essa am-
mette un minimo globale m e un massimo globale M. Si ha dunque m ≤ f (x) ≤ M per
ogni x ∈ [a, b]. Integrando tali disuguaglianze sull’intervallo [a, b], per le proprietà di monotonia
dell’integrale e trattandosi di funzioni costanti, si ottiene:
                                             Z b
                                 m(b − a) ≤      f (x) dx ≤ M (b − a)
                                             a Dividendo per la lunghezza dell’intervallo (b − a) > 0, la media integrale
         Rb
          a f risulta compresa tra il minimo e il massimo di f : m ≤ µ ≤ M. Essendo f
       1
µ = b−a
continua, per il Teorema dei valori intermedi essa assume tutti i valori compresi tra il suo minimo
e il suo massimo. Ne consegue che esiste un punto c ∈ [a, b] tale che f (c) = µ.


                                                 9


<!-- nuova pagina -->

Figura 3: Significato geometrico del Teorema della Media Integrale: esiste un punto x = c
nell’intervallo tale che il rettangolo di base [a, b] e altezza f (c) abbia la stessa area della regione
posta sotto la curva f (x).



4     Teorema Fondamentale del Calcolo Integrale
Questo è senza dubbio il risultato centrale della teoria dell’integrazione, poiché unisce indissolubil-
mente il concetto geometrico di area (integrale definito) con l’operazione analitica di derivazione
(primitiva).

4.1    Funzione Integrale
Definizione 4.1 (Funzione integrale). Sia I un intervallo (anche illimitato) e sia f integrabile
su ogni sotto-intervallo chiuso e limitato contenuto in I. Fissato un punto base x0 ∈ I,
definiamo la funzione integrale di f centrata in x0 come:
                                            Z x
                                  Fx0 (x) =     f (y) dy per x ∈ I
                                              x0

4.2    Il Teorema Fondamentale
Teorema 4.1 (Teorema Fondamentale del Calcolo Integrale). Sia f continua su un intervallo
I e sia x0 ∈ I. Allora la funzione integrale Fx0 (x) è derivabile su I, ed è una
primitiva di f su tale intervallo. In formule:

                                       Fx′ 0 (x) = f (x)   ∀x ∈ I

Dimostrazione. Vogliamo calcolare la derivata di Fx0 (x) tramite la definizione di rapporto incre-
mentale. Fissato un x ∈ I e un incremento h ̸= 0 sufficientemente piccolo, valutiamo:
                                                   Z x+h                Z x              
                     Fx0 (x + h) − Fx0 (x)   1
                                           =                f (y) dy −         f (y) dy
                               h             h       x0                   x0 Per la proprietà di additività dell’integrale, l’espressione in parentesi corrisponde
all’integrale tra x e x + h:
                                            1 x+h
                                              Z
                                         =            f (y) dy
                                            h x

                                                    10 Notiamo che questa è esattamente la media integrale di f sull’intervallo [x, x +
h] (supponendo h > 0). Applicando il Teorema della Media Integrale (essendo f
continua), esisterà un punto ch ∈ [x, x + h] tale che:
                                           Z x+h
                                       1
                                                   f (y) dy = f (ch )
                                       h    x Per h → 0, l’intervallo [x, x + h] si restringe sul punto x. Di conseguenza, per il
teorema del confronto, il punto ch → x. Sfruttando la continuità della funzione f , si
conclude che:
                               Fx (x + h) − Fx0 (x)
                          lim 0                        = lim f (ch ) = f (x)
                          h→0             h              h→0 Il limite del rapporto incrementale esiste ed è proprio f (x), dimostrando
che Fx0 è una primitiva.




Figura 4: Costruzione grafica della funzione integrale. L’area sottesa alla curva dal punto fisso
x0 fino ad un estremo variabile x definisce il valore della funzione Fx0 (x).



Corollario 4.1 (Formula fondamentale del calcolo integrale / Torricelli-Barrow). Sia f continua
su [a, b] e sia F una qualunque sua primitiva su [a, b]. Allora l’integrale definito di f
tra a e b si calcola semplicemente come variazione della primitiva agli estremi:
                              Z b                             h     ib
                                    f (x) dx = F (b) − F (a) = F (x)
                                a                                         a

Dimostrazione. Sia Fx0 la funzione integrale di f (che sappiamo essere una primitiva per il
Teorema Fondamentale). Se F è un’altra qualunque primitiva, esse differiscono per una costante:
F (x) = Fx0 (x) + c. Calcoliamo la differenza agli estremi:

                  F (b) − F (a) = (Fx0 (b) + c) − (Fx0 (a) + c) = Fx0 (b) − Fx0 (a)

Riscrivendo Fx0 secondo la sua definizione integrale:
                                        Z b          Z a        Z b
                                                f−         f=         f
                                           x0         x0         a Il teorema è così dimostrato.

                                                      11


<!-- nuova pagina -->

4.3    Teoremi di integrazione definita
I metodi di calcolo dell’integrale indefinito si trasferiscono naturalmente all’integrale definito
modificando in modo coerente gli estremi di integrazione.

Teorema 4.2 (Integrazione definita per parti). Siano f, g derivabili su [a, b] con derivata conti-
nua. Allora:
                        Z b                  h         ib Z b
                                      ′
                              f (x)g (x) dx = f (x)g(x) −     f ′ (x)g(x) dx
                         a                                          a      a

Teorema 4.3 (Integrazione definita per sostituzione). Sia f continua su [a, b] e sia φ : [c, d] →
[a, b] una funzione derivabile in modo continuo, e possibilmente invertibile. Allora
il cambiamento di variabile comporta anche l’aggiornamento degli estremi:
                                Z b                    Z φ−1 (b)
                                          f (x) dx =               f (φ(t))φ′ (t) dt
                                  a                     φ−1 (a)


5     Integrali Impropri (o Generalizzati)
La teoria dell’integrale di Riemann (integrale definito) poggia su due ipotesi restrittive fonda-
mentali: 1. L’intervallo di integrazione [a, b] deve essere limitato e chiuso. 2. La
funzione f deve essere limitata in tale intervallo.
   Se cade anche solo una di queste ipotesi, si deve operare una generalizzazione del concetto
mediante un passaggio al limite, introducendo i cosiddetti integrali impropri.
Distinguiamo due casi principali: intervalli illimitati e funzioni illimitate.

5.1    A. Integrali su intervalli illimitati
Definizione 5.1 (Integrale improprio a +∞). Data f : [a, +∞[→ R integrabile in senso definito
(secondo Riemann) su ogni intervallo compatto [a, b] per ogni b > a, si definisce
l’integrale improprio di f tra a e +∞ come il limite:
                                  Z +∞                               Z b
                                              f (x) dx = lim               f (x) dx
                                      a                    b→+∞ a
    Studiare il comportamento di questo limite permette di classificare l’integrale improprio:

    • Convergente: se il limite esiste ed è un numero reale finito.

    • Divergente: se il limite è +∞ o −∞.

    • Oscillante: se il limite non esiste.

Osservazione 5.1. Se f (x) ≥ 0 in un intorno dell’infinito (cioè per x ≥ x0 ), la funzione integrale
                  Rb
associata F (b) = x0 f risulta essere una funzione monotona crescente. Pertanto, il limite per
b → +∞ può solo esistere finito o essere +∞; l’integrale di una funzione a segno costante non
può mai oscillare.

                                                          12


<!-- nuova pagina -->

   Simmetricamente, se il dominio di integrazione è esteso a −∞, per una funzione f :]−∞, b] →
R si pone:
                              Z b                    Z b
                                   f (x) dx = lim        f (x) dx
                                    −∞              a→−∞ a Mentre per un integrale su tutta la retta reale (f : R → R), l’integrale si spezza
in due limiti indipendenti:
                          Z +∞             Z 0             Z +∞
                                f (x) dx =      f (x) dx +       f (x) dx
                             −∞                −∞               0 L’integrale complessivo converge se e solo se convergono entrambi i sotto-
integrali.

5.1.1   Esempi Notabili su Intervalli Illimitati
Esempio 5.1. Studiamo la convergenza della funzione f (x) = 1+x
                                                              1
                                                                2 su [0, +∞[.
Applicando la definizione:
                           Z +∞                 Z b
                                 1                    1
                                    2
                                      dx =  lim           dx
                            0   1+x        b→+∞ 0 1 + x2 La primitiva è l’arcotangente:
                          h         ib                       π      π
                 = lim arctan x = lim (arctan b − arctan 0) = − 0 =
                   b→+∞              0   b→+∞                2      2 Poiché il limite è finito, l’integrale su questo intervallo illimitato è convergente.
                                                                             R +∞ 1
Esempio 5.2. Comportamento dell’integrale improprio per potenze: 1                 xα dx.
Valutiamo per α ̸= 1:
                         Z b                    1−α b             1−α             
                              −α                  x                   b          1
                   lim       x dx = lim                   = lim              −
                 b→+∞ 1                  b→+∞ 1 − α 1       b→+∞ 1 − α         1−α
   • Se α > 1, l’esponente (1 − α) è negativo, perciò b1−α = bα−1
                                                               1
                                                                  → 0. L’integrale converge al
     valore α−1.
             1


   • Se α < 1, l’esponente è positivo, quindi b1−α → +∞. L’integrale diverge a +∞.
Valutiamo infine per il caso α = 1:
                           Z b
                                1              h      ib
                     lim          dx = lim ln |x| = lim (ln b − ln 1) = +∞
                    b→+∞ 1 x            b→+∞           1    b→+∞
                                                             R +∞ 1 L’integrale di x1 diverge. In sintesi, 1    xα è integrabile (in senso improprio)
se e solo se α > 1.
                                                                             R +∞ 1
Esempio 5.3. Consideriamo le funzioni logaritmiche generalizzate: e                x(ln x)α dx.
Tramite sostituzione, ponendo y = ln x, la derivata dy = x dx ci permette di ricondurci
                                                                          1

all’integrale notevole precedente:
                                     Z b                        Z ln b
                                             1                          1
                                lim              α
                                                   dx = lim               dy
                               b→+∞ e x(ln x)            b→+∞ 1        yα Sostituendo il limite all’estremo superiore, osserviamo lo stesso comportamento di
convergenza di y1α all’infinito: converge se e solo se α > 1, diverge altrimenti.

                                                    13


<!-- nuova pagina -->

5.2   Criteri di Convergenza
Non sempre è possibile trovare una primitiva in termini di funzioni elementari. Pertanto, ci
affidiamo a criteri qualitativi che garantiscono la convergenza o divergenza dell’integrale tramite
confronti asintotici e disuguaglianze.

Teorema 5.1 (Criterio del Confronto). Siano f, g : [a, +∞[→ R due funzioni limitate e inte-
grabili su ogni intervallo limitato [a, b]. Supponiamo che siano a segno non negativo,
e che esista una dominanza 0 ≤ f (x) ≤ g(x) per ogni x maggiore di un certo valore.
Allora:
                                             R +∞
   1. Se l’integrale della "maggiorante" a g converge, allora converge anche l’integrale della
                     R +∞
       "minorante" a f.
                                        R +∞                                           R +∞
   2. Se l’integrale della "minorante" a f diverge a +∞, allora diverge a +∞ anche a g.




Figura 5: Visualizzazione grafica del criterio del confronto. Siano due curve
poste nel semipiano y ≥ 0, con la curva rossa g(x) costantemente superiore alla curva blu f (x).
Se l’area totale sotto la curva rossa è finita, lo è a maggior ragione quella sotto la curva blu
contenuta all’interno.



Teorema 5.2 (Criterio del Confronto Asintotico). Sia f : [a, +∞[→ R localmente integrabile, e
tale che f (x) ≥ 0 definitivamente. Supponiamo che per x → +∞, la funzione f (x) sia
un infinitesimo di ordine α rispetto alla funzione campione g(x) = x1α. Ovvero:

                                              f (x)
                                       lim            = L ∈]0, +∞[
                                      x→+∞ 1/xα

                                                    R +∞
In virtù di questa equazione asintotica, l’integrale a f (x) dx ha lo stesso carattere della fun-
zione campione: converge se α > 1, diverge se α ≤ 1.

Teorema 5.3 (Criterio di Convergenza Assoluta). Sia f : [a, +∞[→ R integrabile su ogni limi-
tato [a, b]. Se la funzione in modulo |f | è integrabile in senso improprio su [a, +∞[
(ovvero converge), allora anche la funzione originale f ha integrale convergente.
In questo caso, diciamo che la funzione è assolutamente convergente. Vale inoltre la seguente
disuguaglianza:                   Z   +∞           Z           +∞
                                           f (x) dx ≤               |f (x)| dx
                                  a                        a

                                                      14


<!-- nuova pagina -->

                                           R +∞ cos x
Esempio 5.4. Analizziamo l’integrale        1     x2
                                                     dx. Trattandosi di una
                                                                              R +∞ | cos x|
funzione a segno variabile, studiamo l’integrale del suo valore assoluto: 1           x2
                                                                                            dx. Poiché
la funzione coseno è limitata, abbiamo che | cos x| ≤ 1 per ogni x reale. Possiamo costruire la
disuguaglianza:
                                          | cos x|   1
                                     0≤        2
                                                   ≤ 2 ∀x ≥ 1
                                             x      x
                                                                          R +∞ 1 Sappiamo dall’esempio notevole che l’integrale maggiorante 1         x2
                                                                                    dx converge, trat-
tandosi della potenza con α = 2 > 1. Per il teorema del confronto, anche l’inte-
                         R +∞ | cos x|
grale del valore assoluto 1      x2
                                       dx converge. Infine, per il criterio di convergenza
assoluta, possiamo concludere che l’integrale originario converge.

5.3     B. Integrali Impropri per Funzioni Illimitate
L’altro scenario si presenta quando l’intervallo di integrazione [a, b] è finito, ma la funzione non
è limitata all’interno di esso, tipicamente per la presenza di un asintoto verticale in uno degli
estremi o al suo interno.

Definizione 5.2 (Integrale improprio su intervalli limitati). Sia f : [a, b[→ R una funzione
integrabile in senso definito in ogni sotto-intervallo chiuso di forma [a, c] con a < c < b.
Supponiamo che la funzione diverga (sia illimitata) per x → b− . L’integrale improprio di f su
[a, b[ è definito come:
                                   Z b                  Z c
                                       f (x) dx = lim       f (x) dx
                                    a             c→b−   a Anche qui, l’integrale può dirsi convergente, divergente (se il limite fa ±∞) o oscillante
a seconda dell’esistenza e finitezza di tale limite.

Osservazione 5.2. È rilevante notare che se la funzione in esame risulta essere regolarmente
limitata e già integrabile secondo Riemann (in senso definito) sull’intero intervallo chiuso [a, b],
la definizione mediante limite (integrale in senso improprio) restituisce esattamente il medesimo
valore calcolato col metodo canonico.

5.3.1    Criteri di Convergenza per Funzioni Illimitate
Tutti i teoremi strutturali validi per gli integrali impropri all’infinito (Criterio del Confronto e
Criterio di Convergenza Assoluta) mantengono intatta la loro validità logica in questo contesto
analogo, applicando i dovuti adattamenti nel calcolo del limite (ad esempio esaminando intorni
del punto in cui la funzione va ad asintoto).
    Relativamente al Criterio del Confronto Asintotico, il termine di paragone per eccellenza
diviene la funzione (b − x)−α valutata in prossimità del limite critico b. Pertanto, si
definisce l’ordine di infinito α calcolando il limite per x → b− . In questo scenario (duale rispetto
a quello per x → +∞), l’integrale risulta convergente se e solo se l’ordine di asintoto α è
strettamente minore di 1 (α < 1).




                                                  15


<!-- nuova pagina -->
```
