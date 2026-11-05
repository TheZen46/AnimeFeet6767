---
corso: Fondamenti di Informatica
modulo: 3
titolo: Calcolatori, algoritmi e primi programmi in C++
programma: [FI-05, FI-06]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 3 · Calcolatori, algoritmi e primi programmi in C++

**In questo modulo.** Si usano le funzioni e la logica del modulo 1. Si parte da com'è fatto un calcolatore e da come rappresenta numeri e caratteri con i bit. Poi si vede che cos'è un algoritmo e come un programma scritto in un linguaggio ad alto livello diventa un eseguibile. Il resto del modulo è il primo pezzo di C++: struttura di un programma, ingresso e uscita, variabili e tipi, operatori ed espressioni, istruzioni condizionali e iterative. Chiude il modulo una sezione pratica su come compilare ed eseguire da terminale Linux, come si fa all'esame. Alla fine del modulo si sa scrivere, compilare e provare un programma con letture da tastiera, condizioni e cicli, valutare a mano un'espressione C++ e scrivere la condizione che corrisponde a un intervallo, come negli esercizi della prova di teoria.

Tutti i programmi sono stati compilati con `g++ -std=c++17 -Wall -Wextra` ed eseguiti con gli ingressi indicati; la prima riga di ogni programma (`// file: …`) è il nome del file.

## 3.1 Il calcolatore

Un calcolatore esegue istruzioni su dati, entrambi conservati in memoria. Il modello è quello di **von Neumann**: una **CPU** (unità centrale di elaborazione) con l'**unità di controllo**, che legge le istruzioni dalla memoria e le fa eseguire una alla volta, e l'**ALU** (unità aritmetico-logica), che fa i calcoli e i confronti; una **memoria centrale** (la RAM, veloce, volatile) che contiene programmi e dati in uso; le **memorie di massa** (dischi, SSD) che conservano i dati in modo permanente; le **periferiche** di ingresso e uscita (tastiera, schermo, rete); i **bus**, i collegamenti fra le parti. Dentro la CPU ci sono i **registri**, poche celle velocissime. Il ciclo della CPU è sempre lo stesso: preleva l'istruzione, la decodifica, la esegue, passa alla successiva.

L'**hardware** è la parte fisica, il **software** l'insieme dei programmi: il **sistema operativo** gestisce le risorse (processore, memoria, file, periferiche) e offre servizi ai programmi applicativi.

## 3.2 Rappresentare l'informazione

Tutto in un calcolatore è fatto di **bit** (*binary digit*), che valgono 0 o 1. Il raggruppamento più noto è il **byte**, 8 bit; poi kilobyte, megabyte, gigabyte. Con $n$ bit si rappresentano $2^n$ valori diversi (modulo 2): un byte ha 256 valori.

**Numeri naturali in base 2.** Come in base 10 ogni cifra vale una potenza di 10, in base 2 ogni bit vale una potenza di 2: $1011_2 = 1 \cdot 8 + 0 \cdot 4 + 1 \cdot 2 + 1 \cdot 1 = 11$. Per passare da decimale a binario si divide ripetutamente per 2 e si leggono i resti dall'ultimo al primo: $11 \to$ resti $1, 1, 0, 1 \to 1011$. La base 16 (**esadecimale**, cifre 0-9 e A-F) è un modo compatto di scrivere il binario: ogni cifra esadecimale corrisponde a 4 bit, $1011\,0110_2 = \texttt{B6}_{16} = 182$.

**Interi con segno.** Si usa il **complemento a 2**: con $n$ bit si rappresentano i numeri da $-2^{n-1}$ a $2^{n-1} - 1$, il bit più significativo indica il segno, e per cambiare segno si invertono tutti i bit e si aggiunge 1. Così la somma si fa con lo stesso circuito per positivi e negativi. Un `int` di 32 bit va da $-2\,147\,483\,648$ a $2\,147\,483\,647$: oltre si ha **overflow**, e il risultato "gira".

**Numeri reali.** Si usa la **virgola mobile**: segno, mantissa ed esponente, come nella notazione scientifica. I reali rappresentabili sono un numero finito, quindi quasi sempre i calcoli sono approssimati: `0.1 + 0.2` non è esattamente `0.3`.

**Caratteri.** A ogni carattere corrisponde un numero, secondo il codice **ASCII** (7 bit, 128 caratteri; le estensioni come Unicode ne hanno molti di più). Da ricordare: `'0'` = 48, `'A'` = 65, `'a'` = 97, e le cifre, le maiuscole e le minuscole sono consecutive. Per questo `c - '0'` dà il valore della cifra `c`, e `c - 'a' + 'A'` la maiuscola di una minuscola.

## 3.3 Algoritmi, programmi, linguaggi

Un **algoritmo** è una sequenza finita di passi non ambigui ed eseguibili che risolve un problema: deve terminare, ogni passo deve essere chiaro, e deve funzionare per tutti i dati previsti. Un **programma** è un algoritmo scritto in un **linguaggio di programmazione**. Il processore capisce solo il **linguaggio macchina** (istruzioni codificate in binario); l'**assembly** ne è la versione simbolica; i **linguaggi ad alto livello** come il C++ sono vicini al modo di ragionare del programmatore e indipendenti dalla macchina.

Il passaggio da sorgente a eseguibile: il **preprocessore** tratta le direttive `#include` (inserisce i file di intestazione); il **compilatore** traduce il sorgente in codice oggetto e segnala gli errori di sintassi; il **linker** collega il codice oggetto con le librerie e produce l'eseguibile. Gli errori sono di tre tipi: **di compilazione** (sintassi, tipi: il programma non parte), **di esecuzione** (divisione per zero, accesso fuori da un array: il programma si interrompe o si comporta in modo imprevedibile), **logici** (il programma gira ma dà risultati sbagliati: si trovano solo provandolo).

La **programmazione strutturata** costruisce ogni algoritmo con tre schemi: **sequenza** (un'istruzione dopo l'altra), **selezione** (scegliere fra alternative con una condizione), **iterazione** (ripetere finché vale una condizione). Il teorema di Böhm e Jacopini dice che bastano questi tre per scrivere qualunque algoritmo, senza salti arbitrari.

## 3.4 Il primo programma: variabili e tipi

```cpp
// file: somma.cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;                       // due variabili intere
    cout << "Inserisci due interi: ";
    cin >> a >> b;                  // lettura da tastiera
    int s = a + b;                  // dichiarazione con inizializzazione
    cout << "La somma e' " << s << endl;
    return 0;                       // 0 = terminazione regolare
}
```

`#include <iostream>` rende disponibili `cin` (il flusso d'ingresso, la tastiera) e `cout` (il flusso d'uscita, lo schermo); `using namespace std;` evita di scrivere `std::cout`. L'esecuzione comincia da `main`, che restituisce un intero al sistema operativo. Ogni istruzione finisce con `;`, i blocchi stanno fra graffe, `//` apre un commento fino alla fine della riga. `<<` "manda" valori a `cout`, `>>` "estrae" valori da `cin` saltando gli spazi; `endl` va a capo.

Una **variabile** è una zona di memoria con un **nome**, un **tipo** e un **valore**. Il tipo dice quanta memoria serve, quali valori sono ammessi e quali operazioni si possono fare. I tipi fondamentali:

| Tipo | Valori | Esempio |
|---|---|---|
| `int` | interi (di solito 32 bit) | `int n = -7;` |
| `double`, `float` | reali in virgola mobile (doppia, singola precisione) | `double x = 3.14;` |
| `char` | un carattere (un byte, il suo codice) | `char c = 'A';` |
| `bool` | `true` o `false` | `bool trovato = false;` |

Il nome (identificatore) è fatto di lettere, cifre e `_`, non comincia con una cifra e non è una parola riservata; maiuscole e minuscole sono diverse. Una variabile va **dichiarata** prima dell'uso; se non viene inizializzata il suo valore è indefinito (quello che c'era in memoria). Una **costante** si dichiara con `const` e non può cambiare: `const double PI = 3.14159;`.

## 3.5 Operatori ed espressioni

**Aritmetici**: `+`, `-`, `*`, `/`, `%`. Fra due interi `/` è la **divisione intera** (troncata verso lo zero) e `%` il resto: `7 / 2` vale 3, `7 % 2` vale 1, `-7 / 2` vale $-3$. Se almeno un operando è reale la divisione è reale: `7 / 2.0` vale 3.5. Attenzione a `double m = (a + b) / 2;` con `a` e `b` interi: la divisione è intera e solo dopo il risultato diventa `double`. Si corregge con una **conversione esplicita**, `static_cast<double>(a + b) / 2`, o scrivendo `2.0`.

**Assegnamento**: `x = espr` calcola l'espressione e la mette in `x`; è anch'esso un'espressione, che vale il valore assegnato. Forme composte: `x += 3` equivale a `x = x + 3`, e così `-=`, `*=`, `/=`, `%=`. **Incremento e decremento**: `++x` incrementa e poi vale il nuovo valore (prefisso), `x++` vale il vecchio valore e poi incrementa (postfisso).

**Relazionali**: `==`, `!=`, `<`, `<=`, `>`, `>=`; **logici**: `&&` (e), `||` (o), `!` (non). Il risultato è un `bool`; in C++ ogni valore numerico diverso da 0 conta come vero e 0 come falso. Gli operatori logici sono valutati in **cortocircuito**: in `a && b`, se `a` è falso `b` non viene valutato; in `a || b`, se `a` è vero neanche. Si sfrutta per scrivere `(d != 0) && (n / d > 2)` senza rischiare la divisione per zero.

Un errore classico è scrivere `if (x = 5)` invece di `if (x == 5)`: è un assegnamento, vale 5, cioè sempre vero. E una condizione come $0 < x < 10$ va scritta `(x > 0) && (x < 10)`: `0 < x < 10` si compila ma confronta con 10 il risultato (0 o 1) di `0 < x`.

**Precedenza** (dalla più alta): `!`, `++`, `--` unari; `*`, `/`, `%`; `+`, `-`; `<`, `<=`, `>`, `>=`; `==`, `!=`; `&&`; `||`; assegnamenti. Nel dubbio, parentesi.

## 3.6 Le istruzioni condizionali

```cpp
// file: giudizio.cpp
#include <iostream>
using namespace std;

int main() {
    int voto;
    cin >> voto;
    if (voto < 0 || voto > 30)
        cout << "voto non valido" << endl;
    else if (voto < 18)
        cout << "insufficiente" << endl;
    else if (voto < 24)
        cout << "sufficiente" << endl;
    else if (voto < 28)
        cout << "buono" << endl;
    else
        cout << "ottimo" << endl;
    return 0;
}
```

`if (condizione) istruzione1 else istruzione2` esegue la prima se la condizione è vera, la seconda altrimenti; il ramo `else` è facoltativo, e se un ramo ha più istruzioni le si chiude in un blocco `{ }`. Nella catena `else if` le condizioni si controllano in ordine e si esegue solo il primo ramo vero: per questo il secondo test può limitarsi a `voto < 24`, sapendo già che `voto >= 18`. Un `else` si lega sempre all'`if` più vicino senza `else`: con gli `if` annidati conviene usare le graffe.

L'istruzione **`switch`** sceglie in base al valore di un'espressione intera o carattere:

```cpp
// file: calcolatrice.cpp
#include <iostream>
using namespace std;

int main() {
    double x, y;
    char op;
    cin >> x >> op >> y;
    switch (op) {
        case '+': cout << x + y << endl; break;
        case '-': cout << x - y << endl; break;
        case '*':
        case 'x': cout << x * y << endl; break;    // due etichette
        case '/':
            if (y != 0) cout << x / y << endl;
            else cout << "divisione per zero" << endl;
            break;
        default: cout << "operatore sconosciuto" << endl;
    }
    return 0;
}
```

L'esecuzione salta all'etichetta `case` uguale al valore e prosegue **fino al `break`**: senza `break` si "cade" nei casi successivi, cosa che si sfrutta per dare più etichette allo stesso codice. `default` raccoglie i valori non previsti.

## 3.7 Le istruzioni iterative

C++ ha tre cicli. **`while (condizione) corpo`**: controlla la condizione prima di ogni ripetizione, quindi il corpo può non essere mai eseguito. **`do corpo while (condizione);`**: controlla dopo, quindi il corpo si esegue almeno una volta; è il ciclo giusto per **validare** un dato letto, che va chiesto di nuovo finché non è valido. **`for (inizializzazione; condizione; aggiornamento) corpo`**: equivale a un `while` con le tre parti raccolte in testa, ed è il ciclo naturale quando il numero di ripetizioni è controllato da un **contatore** (cicli *definiti*). Quando invece si ripete finché succede qualcosa (un valore **sentinella**, un dato non valido) il ciclo è *indefinito*.

`break` esce subito dal ciclo più interno; `continue` salta il resto del corpo e passa alla ripetizione successiva.

```cpp
// file: media.cpp
#include <iostream>
using namespace std;

int main() {
    int x, n = 0, somma = 0;
    cin >> x;
    while (x != -1) {               // -1 e' la sentinella
        if (x < 0) {                // altri negativi: scartati
            cin >> x;
            continue;
        }
        somma += x;
        n++;
        cin >> x;
    }
    if (n > 0)
        cout << "media " << static_cast<double>(somma) / n << endl;
    else
        cout << "nessun valore" << endl;
    return 0;
}
```

```cpp
// file: validazione.cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    do {
        cout << "Numero fra 1 e 10: ";
        cin >> n;
    } while (n < 1 || n > 10);
    for (int i = 1; i <= 10; i++)
        cout << n << " x " << i << " = " << n * i << endl;
    return 0;
}
```

Una variabile dichiarata nell'intestazione del `for`, come `i`, esiste solo dentro il ciclo. Per scrivere un ciclo corretto conviene chiedersi tre cose: da dove parte (inizializzazione), quando si ferma (condizione, che prima o poi deve diventare falsa, altrimenti il ciclo è **infinito**), che cosa cambia a ogni giro.

## 3.8 Compilare ed eseguire da terminale, come all'esame

La prova pratica si svolge su macchine Linux. C'è Visual Studio Code, ma la compilazione automatica è disattivata e non si può attivare: il programma va compilato **a mano**, scrivendo ogni volta il comando nel terminale. Si può anche consegnare senza aver mai compilato, ma un programma che non compila vale poco: conviene arrivare all'esame sapendo fare questi passi senza pensarci.

**Il terminale in cinque comandi.** Si apre il terminale (in VS Code dal menu *Terminal › New Terminal*; la scorciatoia da tastiera cambia con la tastiera italiana o inglese) e si lavora sempre in una cartella nota.

| Comando | Che cosa fa |
|---|---|
| `pwd` | mostra la cartella in cui si è |
| `ls` | elenca i file della cartella (`ls -l` con i dettagli) |
| `mkdir esame` | crea la cartella `esame` |
| `cd esame`, `cd ..`, `cd ~` | entra nella cartella, risale di un livello, torna alla cartella personale |
| `code .` | apre in VS Code la cartella corrente |

Due tasti fanno risparmiare tempo: <kbd>Tab</kbd> completa i nomi di file e cartelle (scrivere `cd es` e premere <kbd>Tab</kbd>), la **freccia su** richiama i comandi già dati, così il comando di compilazione si scrive una volta sola. <kbd>Ctrl</kbd>+<kbd>C</kbd> interrompe un programma bloccato (per esempio in un ciclo infinito).

**Una cartella per la prova.** All'inizio si crea una cartella facile da raggiungere e ci si mette dentro:

```bash
cd ~
mkdir esame
cd esame
code .
```

Tutti i file (sorgenti e file di dati del testo) vanno lì. Un programma che apre `dati.txt` lo cerca **nella cartella da cui viene eseguito**, non in quella del sorgente: se il file "non si trova", il primo controllo è `ls` nel terminale.

**Compilare ed eseguire.**

```bash
g++ -std=c++17 -Wall -Wextra -o es5 es5.cpp     # compila es5.cpp in es5
./es5                                           # esegue
./es5 < ingresso.txt                            # legge da file invece che da tastiera
g++ -std=c++17 -Wall -Wextra -o es5 es5.cpp && ./es5   # esegue solo se compila
g++ -std=c++17 -Wall -o prog main.cpp Classe.cpp       # programma su piu' file
```

`-o es5` dà il nome all'eseguibile (senza, si chiama `a.out`); `./` vuol dire "nella cartella corrente". I file `.h` non si mettono nel comando: li include il preprocessore. Prima di compilare si **salva** (<kbd>Ctrl</kbd>+<kbd>S</kbd>): il compilatore legge il file su disco, non quello aperto nell'editor, e un errore "già corretto" che non sparisce di solito è una modifica non salvata.

**Leggere gli errori.** Un messaggio ha la forma `es5.cpp:12:9: error: …`: file, riga, colonna, descrizione. Si corregge **il primo** errore e si ricompila, perché spesso gli altri sono conseguenze del primo (un `;` mancante ne genera decine). Gli avvisi (`warning`) con `-Wall -Wextra` vanno letti: segnalano `=` al posto di `==` in un `if`, variabili usate senza valore, confronti fra interi con e senza segno.

| Messaggio | Causa tipica |
|---|---|
| `'cout' was not declared in this scope` | manca `#include <iostream>` o `using namespace std;` |
| `expected ';' before …` | manca il `;` alla riga **precedente** |
| `undefined reference to 'f(int)'` | la funzione è dichiarata ma non definita, o il suo `.cpp` non è nel comando |
| `no matching function for call to …` | tipi o numero dei parametri sbagliati |
| `Segmentation fault` (in esecuzione) | indice fuori dall'array, puntatore nullo o non inizializzato |
| il programma "non fa nulla" | sta aspettando un dato da tastiera |
| `No such file or directory` su `./es5` | il programma non è stato compilato, o si è in un'altra cartella |

**Il metodo.** Si compila spesso, dopo ogni funzione, non alla fine: un errore trovato subito si corregge in un minuto, venti errori insieme no. Si prova ogni funzione con un `main` minimo e valori di cui si conosce il risultato, poi si costruisce il programma richiesto. Per capire dove sbaglia un programma si stampano i valori intermedi con `cerr << "i = " << i << endl;`, da togliere prima di consegnare. Se il testo chiede di consegnare uno `.zip` con i sorgenti, si può fare dal file manager oppure con `zip consegna.zip *.cpp *.h`. Gli ultimi cinque minuti servono a ricompilare tutto da capo e a rileggere il testo: nomi delle funzioni e dei parametri devono essere quelli richiesti.

## Esempi ed esercizi svolti

**Esercizio 1. Conversioni.** Scrivere 45 in binario e in esadecimale; scrivere $-45$ in complemento a 2 su 8 bit; che carattere ha codice 100?

$45 = 32 + 8 + 4 + 1 = 0010\,1101_2 = \texttt{2D}_{16}$. Per $-45$: si invertono i bit, $1101\,0010$, e si aggiunge 1: $1101\,0011$. Controllo: $-128 + 64 + 16 + 2 + 1 = -45$. Il codice 100 è `'a' + 3`, cioè `'d'`.

**Esercizio 2. Valutare espressioni.** Con `int a = 7, b = 2;` e `double c;`, che valore hanno, nell'ordine, queste espressioni (ognuna parte dai valori lasciati dalla precedente)?

```cpp
// file: espressioni.cpp
#include <iostream>
using namespace std;

int main() {
    int a = 7, b = 2, zero = 0;
    double c;
    cout << a / b << " " << a % b << endl;       // 3 1
    c = a / b;
    cout << c << " " << a / (double)b << endl;   // 3 3.5
    int d = a++ + ++b;                           // 7 + 3
    cout << d << " " << a << " " << b << endl;   // 10 8 3
    cout << (a > b && b == 3) << " " << !(a % 2) << endl;   // 1 1
    a -= b * 2;                                  // 8 - 6
    cout << a << " " << (a == 2 || 1 / zero > 0) << endl;
    return 0;
}
```

`c = a / b` vale 3 perché la divisione è fra interi; `a / (double)b` è 3.5. In `a++ + ++b` si usa il vecchio `a` (7) e il nuovo `b` (3). `!(a % 2)` è vero perché `a` vale 8. Nell'ultima riga `a` vale 2, `a == 2` è vero e il cortocircuito evita di valutare `1 / zero`, che farebbe fermare il programma: stampa `2 1`.

**Esercizio 3. Intervalli** (sul modello della prova intermedia). Completare le espressioni in modo che `y` sia vero se e solo se l'intero `x` appartiene all'insieme.

| Insieme | Espressione |
|---|---|
| $[-5, 5]$ | `y = (x >= -5) && (x <= 5);` |
| $(-\infty, 0) \cup (10, 20]$ | `y = (x < 0) \|\| ((x > 10) && (x <= 20));` |
| $[0, 100]$, $x \ne 50$, $x$ pari | `y = (x >= 0) && (x <= 100) && (x != 50) && (x % 2 == 0);` |
| $\mathbb Z \setminus [3, 7]$ | `y = (x < 3) \|\| (x > 7);` oppure `y = !((x >= 3) && (x <= 7));` |

L'ultima riga mostra De Morgan: il complementare di un intervallo è un "o" di due condizioni.

```cpp
// file: intervalli.cpp
#include <iostream>
using namespace std;

int main() {      // conta gli interi di [-30, 120] in ciascun insieme
    int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
    for (int x = -30; x <= 120; x++) {
        if ((x >= -5) && (x <= 5)) c1++;
        if ((x < 0) || ((x > 10) && (x <= 20))) c2++;
        if ((x >= 0) && (x <= 100) && (x != 50) && (x % 2 == 0)) c3++;
        if (!((x >= 3) && (x <= 7))) c4++;
    }
    cout << c1 << " " << c2 << " " << c3 << " " << c4 << endl;
    return 0;
}
```

Il programma stampa `11 40 50 146`: 11 interi in $[-5, 5]$; 30 negativi più 10 in $(10, 20]$; i 51 pari da 0 a 100 meno il 50; tutti i 151 meno i 5 di $[3, 7]$.

**Esercizio 4. Somma delle cifre.** Leggere un intero positivo e stampare la somma delle sue cifre.

```cpp
// file: cifre.cpp
#include <iostream>
using namespace std;

int main() {
    int n, somma = 0;
    cin >> n;
    while (n > 0) {
        somma += n % 10;    // l'ultima cifra
        n /= 10;            // la si toglie
    }
    cout << somma << endl;
    return 0;
}
```

Con 4096 stampa 19. `n % 10` e `n / 10` sono i due attrezzi per lavorare sulle cifre di un intero.

**Esercizio 5. Massimo comun divisore** con l'algoritmo di Euclide: $\text{MCD}(a, b) = \text{MCD}(b, a \bmod b)$, e $\text{MCD}(a, 0) = a$.

```cpp
// file: mcd.cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    cout << a << endl;
    return 0;
}
```

Con 84 e 36: $(84, 36) \to (36, 12) \to (12, 0)$, stampa 12. Il ciclo termina perché il resto diminuisce strettamente a ogni passo.

**Esercizio 6. Numero primo.** Dire se un intero $n \ge 2$ è primo.

```cpp
// file: primo.cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    bool primo = (n >= 2);
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0) {
            primo = false;
            break;          // inutile continuare
        }
    cout << n << (primo ? " e' primo" : " non e' primo") << endl;
    return 0;
}
```

Basta provare i divisori fino a $\sqrt n$: se $n = d \cdot e$ con $d \le e$, allora $d \le \sqrt n$. L'operatore `c ? x : y` vale `x` se `c` è vero, `y` altrimenti.

**Esercizio 7. Da decimale a binario.** Stampare i bit di un intero fra 0 e 255, dal più significativo.

```cpp
// file: binario.cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int p = 128; p >= 1; p /= 2) {   // potenze di 2 decrescenti
        if (n >= p) {
            cout << 1;
            n -= p;
        } else
            cout << 0;
    }
    cout << endl;
    return 0;
}
```

Con 45 stampa `00101101`. Invece delle divisioni successive (che danno i bit dal meno significativo, quindi al contrario) si confronta il numero con le potenze di 2 dalla più grande.

**Esercizio 8. Cicli annidati.** Stampare un triangolo di asterischi alto $h$.

```cpp
// file: triangolo.cpp
#include <iostream>
using namespace std;

int main() {
    int h;
    cin >> h;
    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= h - i; j++) cout << ' ';
        for (int j = 1; j <= 2 * i - 1; j++) cout << '*';
        cout << endl;
    }
    return 0;
}
```

La riga $i$ ha $h - i$ spazi e $2i - 1$ asterischi: prima si scrive la formula di una riga, poi il ciclo esterno sulle righe.

### Esercizi più impegnativi

**Esercizio 9. Numeri perfetti.** Un numero è perfetto se è uguale alla somma dei suoi divisori propri ($6 = 1 + 2 + 3$). Stampare i numeri perfetti fino a $N$.

```cpp
// file: perfetti.cpp
#include <iostream>
using namespace std;

int sommaDivisori(int n) {          // divisori propri, a coppie fino a sqrt(n)
    if (n < 2) return 0;
    int s = 1;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0) {
            s += d;
            if (d != n / d) s += n / d;   // il "compagno" del divisore
        }
    return s;
}

int main() {
    int N;
    cin >> N;
    for (int n = 2; n <= N; n++)
        if (sommaDivisori(n) == n) cout << n << " ";
    cout << endl;
    return 0;
}
```

Con $N = 10\,000$ stampa `6 28 496 8128`. Cercare i divisori fino a $\sqrt n$ e aggiungere anche $n / d$ porta il costo da $n$ a $\sqrt n$ passi per numero; la condizione `d != n / d` evita di contare due volte la radice dei quadrati perfetti (per 16 il 4 va contato una volta sola).

**Esercizio 10. Il complemento a 2 su 8 bit.** Leggere un intero fra $-128$ e $127$ e stamparne la rappresentazione in complemento a 2 su 8 bit.

```cpp
// file: complemento.cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n < -128 || n > 127) {
        cout << "fuori dall'intervallo" << endl;
        return 0;
    }
    int u = (n + 256) % 256;      // i negativi diventano 256 + n
    for (int p = 128; p >= 1; p /= 2) {
        cout << (u >= p ? 1 : 0);
        if (u >= p) u -= p;
    }
    cout << endl;
    return 0;
}
```

Con $-45$ stampa `11010011`, con 127 `01111111`, con $-128$ `10000000`. Il trucco è che su $k$ bit il complemento a 2 di un negativo $n$ è il naturale $2^k + n$: qui $256 - 45 = 211$. Attenzione: in C++ `%` con un operando negativo dà un resto negativo (`-45 % 256` vale $-45$), per questo prima si somma 256.

**Esercizio 11. $e^x$ con la serie, fino alla precisione voluta.** Calcolare $e^x = \sum_k x^k / k!$ sommando termini finché il termine è minore di $10^{-12}$ in valore assoluto, e confrontare con `exp`.

```cpp
// file: esponenziale.cpp
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double x;
    cin >> x;
    double termine = 1, somma = 1;
    int k = 0;
    while (fabs(termine) >= 1e-12) {
        k++;
        termine *= x / k;           // x^k / k! dal termine precedente
        somma += termine;
    }
    cout << setprecision(12) << somma << " " << exp(x) << " " << k << endl;
    return 0;
}
```

Con $x = 1$ stampa `2.71828182846 2.71828182846 15`: bastano 15 termini. Ogni termine si ottiene dal precedente moltiplicando per $x / k$: calcolare a parte $x^k$ e $k!$ sarebbe più lento e farebbe traboccare il fattoriale (già $13!$ non sta in un `int`). Con $x = -20$ il ciclo termina ma il risultato è sbagliato (`6.14764462906e-09` contro `2.06115362244e-09`): i termini arrivano a $10^7$ con segni alterni e la cancellazione distrugge le cifre (modulo 3 di Architettura). Si rimedia calcolando $1 / e^{20}$.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Che cosa stampa?** Seguire a mano il programma con l'ingresso `5`.

```cpp
// file: traccia.cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int i = 0, s = 0;
    while (i < n) {
        i++;
        if (i % 2 == 0) continue;
        s += i * i;
        if (s > 20) break;
    }
    cout << i << " " << s << endl;
    cout << (s > 30 || n / (i - 5) > 0) << endl;
    return 0;
}
```

*Passo 1: la tabella dei valori.* Si scrive una riga per giro con `i` e `s` dopo il corpo: $i = 1$, $s = 1$; $i = 2$, pari, `continue`, $s = 1$; $i = 3$, $s = 10$; $i = 4$, `continue`; $i = 5$, $s = 35$, e $35 > 20$: `break`.

*Passo 2: la prima riga.* `5 35`.

*Passo 3: la seconda riga.* `s > 30` è vero: per il cortocircuito `n / (i - 5)`, che sarebbe una divisione per zero, non si valuta; stampa `1` (un `bool` vero si stampa come 1).

**Guidato 2. Validare e contare.** Leggere numeri fino a 0; contare quanti sono positivi, quanti negativi, e trovare il più grande.

*Passo 1: che ciclo?* Indefinito con sentinella: `while`, leggendo prima del ciclo e alla fine del corpo.

*Passo 2: il massimo.* Non lo si può inizializzare a 0 (se i numeri sono tutti negativi sarebbe sbagliato): si usa il primo valore letto.

```cpp
// file: conta.cpp
#include <iostream>
using namespace std;

int main() {
    int x, pos = 0, neg = 0, massimo = 0;
    bool primo = true;
    cin >> x;
    while (x != 0) {
        if (x > 0) pos++;
        else neg++;
        if (primo || x > massimo) {
            massimo = x;
            primo = false;
        }
        cin >> x;
    }
    cout << pos << " positivi, " << neg << " negativi" << endl;
    if (!primo) cout << "massimo " << massimo << endl;
    return 0;
}
```

*Passo 3: le prove.* Con `-4 -9 -2 0` stampa 0 positivi, 3 negativi, massimo $-2$; con `3 8 -1 8 0`, 3 positivi, 1 negativo, massimo 8; con `0` solo i conteggi a zero. Provare sempre i casi limite: nessun dato, tutti negativi, valori uguali.

**Guidato 3. La somma di una serie.** Calcolare $\sum_{k=1}^{n} \frac{1}{k^2}$ e confrontarla con $\pi^2/6$.

*Passo 1: il ciclo.* Definito, da 1 a $n$: `for`.

*Passo 2: il tranello.* `1 / (k * k)` è una divisione intera, che vale 0 per $k \ge 2$: bisogna scrivere `1.0 / (k * k)`.

```cpp
// file: serie.cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    double s = 0;
    for (int k = 1; k <= n; k++)
        s += 1.0 / (k * k);
    double esatto = M_PI * M_PI / 6;
    cout << s << " " << esatto - s << endl;
    return 0;
}
```

*Passo 3: il risultato.* Con $n = 1000$ stampa `1.64393 0.0009995`: l'errore è circa $1/n$, la serie converge lentamente. `<cmath>` dà `sqrt`, `pow`, `fabs` e la costante `M_PI`.

## Riepilogo

Il calcolatore di von Neumann ha CPU (unità di controllo e ALU), memoria centrale, memorie di massa, periferiche e bus; tutto è rappresentato con bit: naturali in base 2 (e 16), interi in complemento a 2, reali in virgola mobile con approssimazioni, caratteri con il codice ASCII. Un algoritmo è una sequenza finita di passi non ambigui; il programma in C++ passa per preprocessore, compilatore e linker, e gli errori possono essere di compilazione, di esecuzione o logici. Un programma C++ comincia da `main`, legge con `cin` e scrive con `cout`; le variabili hanno nome, tipo e valore. La divisione fra interi è intera, gli operatori logici sono in cortocircuito, `=` assegna e `==` confronta. Le condizioni si scrivono con `if`-`else` e `switch` (con `break`), le ripetizioni con `while`, `do`-`while` (almeno una volta, per validare) e `for` (con contatore); `break` e `continue` modificano il flusso dei cicli. All'esame si compila da terminale con `g++ -std=c++17 -Wall -Wextra -o prog prog.cpp`, si esegue con `./prog` e si corregge sempre il primo errore.

## Formulario

### Rappresentazioni

$$\text{con } n \text{ bit: } 2^n \text{ valori}; \quad \text{complemento a 2: } [-2^{n-1}, 2^{n-1} - 1]; \quad -x = \bar x + 1; \quad 1 \text{ cifra esadecimale} = 4 \text{ bit}.$$

ASCII: `'0'` = 48, `'A'` = 65, `'a'` = 97; cifra `c - '0'`; maiuscola `c - 'a' + 'A'`.

### Schemi C++

```text
if (c) { ... } else if (c2) { ... } else { ... }
switch (v) { case k: ...; break; default: ...; }
while (c) { ... }               // 0 o piu' volte
do { ... } while (c);           // almeno una volta
for (int i = 0; i < n; i++) { ... }
```

| Attenzione | Giusto |
|---|---|
| `7 / 2` vale 3 | `7 / 2.0`, `static_cast<double>(a) / b` |
| `if (x = 5)` | `if (x == 5)` |
| `0 < x < 10` | `(x > 0) && (x < 10)` |
| `x++` e `++x` | vecchio valore e poi incremento; incremento e nuovo valore |
| `switch` senza `break` | ogni `case` finisce con `break` |

### Comandi per la prova al calcolatore

```text
cd ~ ; mkdir esame ; cd esame ; code .     cartella della prova
g++ -std=c++17 -Wall -Wextra -o es es.cpp  compila (prima salvare!)
./es    ./es < dati.txt                    esegue, con ingresso da file
g++ ... -o es es.cpp && ./es               esegue solo se compila
Tab completa, freccia su ripete, Ctrl+C interrompe, ls controlla i file
```

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Von Neumann | programma e dati nella stessa memoria, eseguiti dalla CPU |
| Bit, byte | cifra binaria; 8 bit |
| Complemento a 2 | rappresentazione degli interi con segno |
| Algoritmo | sequenza finita di passi non ambigui ed eseguibili |
| Compilatore, linker | traduce il sorgente; unisce codice oggetto e librerie |
| Programmazione strutturata | solo sequenza, selezione, iterazione |
| Cortocircuito | il secondo operando di `&&`, `\|\|` si valuta solo se serve |
| Ciclo definito, indefinito | con contatore; con condizione o sentinella |

### Domande che tornano spesso

- Componenti del calcolatore e ciclo della CPU.
- Convertire fra decimale, binario ed esadecimale; il complemento a 2.
- Fasi della compilazione e tipi di errore.
- Differenza fra `while`, `do`-`while` e `for`; a che cosa servono `break` e `continue`.
- Che cosa succede con la divisione fra interi; precedenza e cortocircuito.
- Come si compila un programma da terminale e come si legge un messaggio d'errore?
