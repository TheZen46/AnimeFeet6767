---
corso: Fondamenti di Informatica
modulo: 5
titolo: Puntatori, memoria dinamica, ricorsione e template
programma: [FI-08]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 5 · Puntatori, memoria dinamica, ricorsione e template

**In questo modulo.** Si usano le funzioni, gli array e le strutture del modulo 4. È la parte di "C++ avanzato" con cui comincia il secondo semestre. Si vede che cos'è un indirizzo di memoria e come lo si manipola con i **puntatori**, il legame fra puntatori e array, l'aritmetica dei puntatori, e la differenza fra puntatori e riferimenti. Poi l'**allocazione dinamica**: creare variabili, array e matrici di dimensione decisa durante l'esecuzione, e liberarli. Poi la **ricorsione**, cioè le funzioni che chiamano sé stesse, e infine i **template di funzione**, che scrivono una funzione una volta sola per tutti i tipi. Alla fine del modulo si sa seguire a mano un programma con puntatori, gestire array dinamici senza perdite di memoria, scrivere e tracciare funzioni ricorsive e scrivere template di funzione.

I programmi sono stati compilati con `g++ -std=c++17 -Wall -Wextra` ed eseguiti. Gli indirizzi stampati da un programma cambiano da un'esecuzione all'altra: negli esempi si stampano solo valori.

## 5.1 Indirizzi e puntatori

Ogni variabile occupa una zona di memoria, che ha un **indirizzo**. L'operatore `&` applicato a una variabile ne dà l'indirizzo. Un **puntatore** è una variabile che contiene un indirizzo; il suo tipo dice a che tipo di dato punta: `int* p;` è un puntatore a `int`. L'operatore `*` (**dereferenziazione**) applicato a un puntatore dà la variabile puntata.

```cpp
// file: puntatori.cpp
#include <iostream>
using namespace std;

int main() {
    int x = 5, y = 9;
    int* p = &x;            // p punta a x
    *p = 7;                 // modifica x attraverso p
    p = &y;                 // ora p punta a y
    *p += *p;               // y = y + y
    int* q = p;             // q e p puntano alla stessa variabile
    *q = *q - 1;
    cout << x << " " << y << " " << (p == q) << endl;   // 7 17 1
    int* r = nullptr;       // puntatore che non punta a nulla
    if (r == nullptr) cout << "r e' nullo" << endl;
    return 0;
}
```

Il simbolo `*` ha due significati: nella dichiarazione (`int* p`) dice che `p` è un puntatore, in un'espressione (`*p`) dereferenzia. Attenzione: `int* a, b;` dichiara un puntatore `a` e un intero `b`. Un puntatore non inizializzato contiene un indirizzo a caso, e dereferenziarlo è un errore di esecuzione; per indicare "nessun oggetto" si usa il puntatore nullo, `nullptr` (o `NULL`, o 0 nel codice più vecchio). Dereferenziare un puntatore nullo fa terminare il programma.

**Puntatori come parametri.** Passare a una funzione l'indirizzo di una variabile le permette di modificarla, come il riferimento del modulo 4 ma in modo esplicito:

```text
void scambia(int* a, int* b) { int t = *a; *a = *b; *b = t; }
scambia(&x, &y);                  // si passano gli indirizzi
```

**Puntatori e riferimenti.** Un riferimento è un altro nome di una variabile: va inizializzato quando si dichiara, non si può "spostare" su un'altra variabile e non può essere nullo; si usa senza `*`. Un puntatore è una variabile a sé, può cambiare oggetto, può essere nullo, e va dereferenziato. Per i parametri di uscita si preferisce il riferimento; i puntatori servono per la memoria dinamica e le strutture collegate.

**Puntatori e `const`.** `const int* p` è un puntatore a un intero costante: non si può modificare `*p`, ma `p` può puntare altrove. `int* const p` è un puntatore costante: punta sempre alla stessa variabile, che però si può modificare. Si legge da destra a sinistra.

## 5.2 Puntatori e array

Il nome di un array, in quasi tutte le espressioni, vale l'indirizzo del suo primo elemento: `a` equivale a `&a[0]`. Per questo un array passato a una funzione non viene copiato: si passa questo indirizzo, e il parametro `int a[]` è in realtà un `int* a`.

**Aritmetica dei puntatori.** Se `p` punta a un elemento di un array, `p + i` punta all'elemento $i$ posizioni dopo: il compilatore moltiplica $i$ per la dimensione del tipo. Quindi
$$\texttt{a[i]} \equiv \texttt{*(a + i)}, \qquad \texttt{\&a[i]} \equiv \texttt{a + i}.$$
Si possono incrementare i puntatori (`p++` passa all'elemento successivo), confrontarli e sottrarli: se `p` e `q` puntano allo stesso array, `q - p` è il numero di elementi fra loro. Non ha senso sommare due puntatori.

```cpp
// file: aritmetica.cpp
#include <iostream>
using namespace std;

int lunghezza(const char* s) {        // come strlen
    const char* p = s;
    while (*p != '\0') p++;
    return p - s;                     // differenza di puntatori
}

int somma(const int* inizio, const int* fine) {   // [inizio, fine)
    int s = 0;
    for (const int* p = inizio; p != fine; p++) s += *p;
    return s;
}

int main() {
    int a[6] = {4, 8, 15, 16, 23, 42};
    int* p = a + 2;                   // punta a a[2]
    cout << *p << " " << *(p + 1) << " " << p[2] << " " << *a + 1 << endl;
    cout << somma(a, a + 6) << " " << somma(a + 1, a + 3) << endl;
    cout << lunghezza("puntatore") << endl;
    return 0;
}
```

Stampa `15 16 23 5` (attenzione a `*a + 1`, che è `a[0] + 1`, non `a[1]`), poi `108 23` e `9`. Anche `p[2]` è lecito: l'indicizzazione funziona su qualunque puntatore.

## 5.3 La memoria dinamica

Le variabili locali stanno nello **stack** (la pila delle chiamate): vengono create all'ingresso nel blocco e distrutte all'uscita, e la loro dimensione deve essere nota quando si compila. Per creare oggetti la cui dimensione o durata si decide durante l'esecuzione si usa lo **heap** (la memoria libera), con l'operatore **`new`**, che alloca e restituisce l'indirizzo, e **`delete`**, che libera:

```text
int* p = new int(5);        // un intero, inizializzato a 5
delete p;                   // liberato
int* v = new int[n];        // array di n interi, n letto a run time
delete[] v;                 // per gli array: delete[]
```

Un oggetto allocato con `new` vive finché non viene liberato con `delete`, indipendentemente dalla funzione che l'ha creato: per questo una funzione può allocare un array e restituirne l'indirizzo. Gli errori da evitare:

- **perdita di memoria** (*memory leak*): perdere l'ultimo puntatore a un oggetto allocato senza liberarlo; la memoria resta occupata fino alla fine del programma;
- **puntatore pendente** (*dangling pointer*): usare un puntatore dopo il `delete`, o restituire l'indirizzo di una variabile locale, che non esiste più; conviene mettere il puntatore a `nullptr` dopo il `delete`;
- **doppio `delete`**, o `delete` di un indirizzo non ottenuto con `new`;
- usare `delete` per un array (serve `delete[]`).

```cpp
// file: dinamico.cpp
#include <iostream>
using namespace std;

int* crea(int n, int valore) {
    int* v = new int[n];
    for (int i = 0; i < n; i++) v[i] = valore + i;
    return v;                          // l'array sopravvive alla funzione
}

int* allunga(int* v, int n, int nuovo) {   // array di n + 1 elementi
    int* w = new int[n + 1];
    for (int i = 0; i < n; i++) w[i] = v[i];
    w[n] = nuovo;
    delete[] v;                        // il vecchio non serve piu'
    return w;
}

int main() {
    int n;
    cin >> n;
    int* v = crea(n, 10);
    v = allunga(v, n, 99);
    n++;
    for (int i = 0; i < n; i++) cout << v[i] << " ";
    cout << endl;
    delete[] v;
    v = nullptr;
    return 0;
}
```

**Matrici dinamiche.** Una matrice di $r$ righe e $c$ colonne decise a run time si costruisce come array di $r$ puntatori, ciascuno a un array di $c$ elementi; si libera in ordine inverso.

```cpp
// file: matrice_dinamica.cpp
#include <iostream>
using namespace std;

int** creaMatrice(int r, int c) {
    int** m = new int*[r];
    for (int i = 0; i < r; i++) m[i] = new int[c];
    return m;
}

void distruggi(int** m, int r) {
    for (int i = 0; i < r; i++) delete[] m[i];   // prima le righe
    delete[] m;                                  // poi l'array di puntatori
}

int main() {
    int r, c;
    cin >> r >> c;
    int** m = creaMatrice(r, c);
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) m[i][j] = i * c + j;
    cout << m[r - 1][c - 1] << " " << m[1][0] << endl;
    distruggi(m, r);
    return 0;
}
```

**Puntatori a strutture.** Se `p` punta a una struttura, si accede ai campi con `(*p).campo` o, più comodo, con **`p->campo`**. È l'operatore che si userà per gli oggetti allocati dinamicamente (modulo 6) e per i nodi delle liste (modulo 7).

## 5.4 La ricorsione

Una funzione è **ricorsiva** se chiama sé stessa. Funziona se ci sono un **caso base**, risolto direttamente, e un **passo ricorsivo** che riconduce il problema a uno più piccolo, avvicinandosi al caso base. Il modello è l'induzione del corso di Analisi: $n! = n \cdot (n - 1)!$ con $0! = 1$.

```cpp
// file: ricorsione.cpp
#include <iostream>
using namespace std;

long fattoriale(int n) {
    if (n == 0) return 1;                 // caso base
    return n * fattoriale(n - 1);         // passo ricorsivo
}

int mcd(int a, int b) { return b == 0 ? a : mcd(b, a % b); }

int sommaArray(const int a[], int n) {    // somma dei primi n
    if (n == 0) return 0;
    return sommaArray(a, n - 1) + a[n - 1];
}

bool palindroma(const char s[], int i, int j) {
    if (i >= j) return true;
    return s[i] == s[j] && palindroma(s, i + 1, j - 1);
}

void binario(int n) {                     // stampa i bit, dal piu' alto
    if (n >= 2) binario(n / 2);
    cout << n % 2;
}

int mosse = 0;
void hanoi(int n, char da, char a, char via) {
    if (n == 0) return;
    hanoi(n - 1, da, via, a);             // n-1 dischi sul piolo d'appoggio
    mosse++;                              // il disco grande va a destinazione
    hanoi(n - 1, via, a, da);             // gli n-1 sopra di lui
}

int main() {
    int v[] = {3, 1, 4, 1, 5};
    cout << fattoriale(10) << " " << mcd(84, 36) << " "
         << sommaArray(v, 5) << " " << palindroma("radar", 0, 4) << endl;
    binario(45);
    cout << endl;
    hanoi(5, 'A', 'C', 'B');
    cout << mosse << endl;
    return 0;
}
```

Stampa `3628800 12 14 1`, `101101` e 31. Ogni chiamata ha il suo **record di attivazione** sullo stack, con i parametri e le variabili locali: `fattoriale(3)` aspetta `fattoriale(2)`, che aspetta `fattoriale(1)`, fino a `fattoriale(0)` che restituisce 1; poi i risultati "risalgono" moltiplicandosi. Senza caso base (o se il passo non si avvicina al caso base) le chiamate non finiscono e lo stack si esaurisce (*stack overflow*).

Nella funzione `binario` la stampa viene **dopo** la chiamata ricorsiva: così i bit escono dal più significativo, al contrario dell'ordine in cui si calcolano. Le **torri di Hanoi** mostrano la forza della ricorsione: spostare $n$ dischi richiede di spostarne $n - 1$, il grande, e di nuovo $n - 1$, quindi $M(n) = 2M(n - 1) + 1$ con $M(0) = 0$, cioè $M(n) = 2^n - 1$.

**Ricorsione o iterazione?** Ogni funzione ricorsiva si può scrivere con un ciclo, e viceversa. La versione ricorsiva è spesso più chiara quando il problema ha una struttura ricorsiva (Hanoi, alberi, divide et impera), ma costa una chiamata per livello, e alcune ricorsioni ripetono molto lavoro: Fibonacci con $F(n) = F(n - 1) + F(n - 2)$ ricalcola gli stessi valori un numero esponenziale di volte, mentre un ciclo con due variabili impiega $n$ passi.

## 5.5 I template di funzione

Molte funzioni fanno la stessa cosa su tipi diversi: scambiare due valori, trovare il massimo di un array, ordinare. Invece di scrivere una versione per tipo (overloading), si scrive un **template**, con un parametro di tipo:

```cpp
// file: template.cpp
#include <iostream>
using namespace std;

template <typename T>
void scambia(T& a, T& b) {
    T t = a;
    a = b;
    b = t;
}

template <typename T>
T massimo(const T a[], int n) {
    T m = a[0];
    for (int i = 1; i < n; i++)
        if (m < a[i]) m = a[i];           // T deve avere l'operatore <
    return m;
}

template <typename T>
void ordina(T a[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j + 1] < a[j]) scambia(a[j], a[j + 1]);
}

int main() {
    int x = 1, y = 2;
    scambia(x, y);
    double d[] = {2.5, -1, 9.75, 3};
    char c[] = {'t', 'e', 'm', 'p'};
    ordina(c, 4);
    cout << x << y << " " << massimo(d, 4) << " " << massimo(c, 4) << " "
         << c[0] << c[1] << c[2] << c[3] << endl;
    return 0;
}
```

Il compilatore **istanzia** il template, cioè genera la funzione per il tipo usato, deducendolo dagli argomenti: `scambia(x, y)` crea `scambia<int>`. Il tipo si può anche indicare esplicitamente, `massimo<double>(d, 4)`. Il codice del template deve avere senso per ogni tipo con cui lo si usa: `massimo` richiede che `T` abbia l'operatore `<` (lo si definirà per le classi nel modulo 6). Si può scrivere `class` al posto di `typename`, con lo stesso significato.

## Esempi ed esercizi svolti

**Esercizio 1. Trovare e correggere gli errori** (sul modello della prova di teoria).

```text
1   int* crea(int n) {
2       int v[n];
3       for (int i = 0; i <= n; i++) v[i] = 0;
4       return v;
5   }
6   int main() {
7       int* p;
8       *p = 3;
9       int* a = crea(10);
10      delete a;
11  }
```

Riga 2: la dimensione di un array locale deve essere costante, e comunque un array locale sparisce all'uscita: serve `int* v = new int[n];`. Riga 3: l'ultimo indice valido è `n - 1`, la condizione è `i < n`. Riga 4: restituire l'indirizzo di una variabile locale crea un puntatore pendente (corretto dalla riga 2 con `new`). Riga 8: `p` non è inizializzato; serve per esempio `int x; int* p = &x;`. Riga 10: un array si libera con `delete[] a;`.

**Esercizio 2. Che cosa stampa?**

```cpp
// file: traccia_puntatori.cpp
#include <iostream>
using namespace std;

void f(int* p, int& r, int v) {
    *p += v;
    r = *p * 2;
    p = &v;          // cambia solo la copia locale del puntatore
    *p = 100;
}

int main() {
    int a[3] = {1, 2, 3};
    int* q = a;
    f(q + 1, a[0], 5);
    q += 2;
    *q = *(q - 1) + a[0];
    cout << a[0] << " " << a[1] << " " << a[2] << endl;
    return 0;
}
```

In `f`, `p` punta ad `a[1]`, che diventa $2 + 5 = 7$; `r` è `a[0]`, che diventa 14; poi `p` punta alla copia locale `v`, e `*p = 100` cambia solo quella. Nel `main`, `q` punta ad `a[2]`, che diventa $a[1] + a[0] = 7 + 14 = 21$. Stampa `14 7 21`.

**Esercizio 3. Array dinamico dei valori sopra soglia.** La funzione riceve un array, la sua dimensione e una soglia; restituisce un nuovo array, allocato dinamicamente, con i soli elementi maggiori della soglia, e la sua dimensione per riferimento.

```cpp
// file: filtra.cpp
#include <iostream>
using namespace std;

int* filtra(const int a[], int n, int soglia, int& m) {
    m = 0;
    for (int i = 0; i < n; i++)         // prima passata: quanti sono
        if (a[i] > soglia) m++;
    int* b = new int[m];
    int k = 0;
    for (int i = 0; i < n; i++)         // seconda passata: copia
        if (a[i] > soglia) b[k++] = a[i];
    return b;
}

int main() {
    int a[] = {12, 5, 30, 8, 19, 7, 25};
    int m;
    int* b = filtra(a, 7, 10, m);
    cout << m << ":";
    for (int i = 0; i < m; i++) cout << " " << b[i];
    cout << endl;
    delete[] b;
    return 0;
}
```

Stampa `4: 12 30 19 25`. Le due passate evitano di allocare "abbastanza" memoria a caso; chi chiama la funzione deve ricordarsi del `delete[]`.

**Esercizio 4. Ricorsione su un array: il massimo e la ricerca binaria.**

```cpp
// file: ricorsione_array.cpp
#include <iostream>
using namespace std;

int massimo(const int a[], int n) {            // n >= 1
    if (n == 1) return a[0];
    int m = massimo(a + 1, n - 1);             // massimo del resto
    return a[0] > m ? a[0] : m;
}

int cerca(const int a[], int sx, int dx, int x) {
    if (sx > dx) return -1;
    int c = (sx + dx) / 2;
    if (a[c] == x) return c;
    if (a[c] < x) return cerca(a, c + 1, dx, x);
    return cerca(a, sx, c - 1, x);
}

int main() {
    int a[] = {2, 3, 5, 7, 11, 13, 17, 19};
    cout << massimo(a, 8) << " " << cerca(a, 0, 7, 13) << " "
         << cerca(a, 0, 7, 4) << endl;
    return 0;
}
```

Stampa `19 5 -1`. In `massimo(a + 1, n - 1)` si passa il "resto" dell'array con l'aritmetica dei puntatori.

**Esercizio 5. Fibonacci: ricorsivo e iterativo.** Quante chiamate fa la versione ricorsiva per $F(20)$?

```cpp
// file: fibonacci.cpp
#include <iostream>
using namespace std;

long chiamate = 0;

long fibR(int n) {
    chiamate++;
    if (n < 2) return n;
    return fibR(n - 1) + fibR(n - 2);
}

long fibI(int n) {
    long a = 0, b = 1;                  // F(0), F(1)
    for (int i = 0; i < n; i++) {
        long t = a + b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    cout << fibR(20) << " " << fibI(20) << " " << chiamate << endl;
    return 0;
}
```

Stampa `6765 6765 21891`: quasi ventiduemila chiamate contro 20 giri di ciclo. Il numero di chiamate $C(n) = C(n - 1) + C(n - 2) + 1$ cresce come i numeri di Fibonacci stessi.

### Esercizi più impegnativi

**Esercizio 6. Merge sort.** Ordinare un array con l'algoritmo per fusione: si divide l'array a metà, si ordinano ricorsivamente le due metà, si fondono (guidato 2 del modulo 4). Il buffer per la fusione si alloca dinamicamente.

```cpp
// file: mergesort.cpp
#include <iostream>
using namespace std;

// fonde a[sx..c] e a[c+1..dx], gia' ordinati
void fondi(int a[], int sx, int c, int dx, int buf[]) {
    int i = sx, j = c + 1, k = 0;
    while (i <= c && j <= dx) buf[k++] = a[i] <= a[j] ? a[i++] : a[j++];
    while (i <= c) buf[k++] = a[i++];
    while (j <= dx) buf[k++] = a[j++];
    for (int t = 0; t < k; t++) a[sx + t] = buf[t];      // ricopia
}

void mergeSort(int a[], int sx, int dx, int buf[]) {
    if (sx >= dx) return;                 // 0 o 1 elementi: gia' ordinato
    int c = (sx + dx) / 2;
    mergeSort(a, sx, c, buf);
    mergeSort(a, c + 1, dx, buf);
    fondi(a, sx, c, dx, buf);
}

int main() {
    int n;
    cin >> n;
    int* a = new int[n];
    int* buf = new int[n];                // un solo buffer per tutte le fusioni
    for (int i = 0; i < n; i++) cin >> a[i];
    mergeSort(a, 0, n - 1, buf);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    delete[] a;
    delete[] buf;
    return 0;
}
```

Con `8  5 2 9 1 5 6 3 7` stampa `1 2 3 5 5 6 7 9`. Le chiamate formano un albero di profondità circa $\log_2 n$, e a ogni livello le fusioni toccano in tutto $n$ elementi: il merge sort fa circa $n \log_2 n$ confronti, contro gli $n^2/2$ dell'ordinamento per selezione (per $n = 1000$, circa 10 000 contro 500 000). È anche l'esempio di ricorsione più chiesto all'orale di Architettura, dove va tradotto in assembly.

**Esercizio 7. Tutte le permutazioni di una stringa.** Stampare le permutazioni dei caratteri di una stringa con una funzione ricorsiva: si fissa a turno ogni carattere in prima posizione e si permutano gli altri.

```cpp
// file: permutazioni.cpp
#include <iostream>
#include <cstring>
using namespace std;

int conta = 0;

void permuta(char s[], int k, int n) {    // permuta le posizioni k..n-1
    if (k == n - 1) {
        cout << s << " ";
        conta++;
        return;
    }
    for (int i = k; i < n; i++) {
        swap(s[k], s[i]);                 // s[i] in posizione k
        permuta(s, k + 1, n);
        swap(s[k], s[i]);                 // si rimette a posto
    }
}

int main() {
    char s[12];
    cin >> s;
    permuta(s, 0, strlen(s));
    cout << endl << conta << endl;
    return 0;
}
```

Con `abc` stampa `abc acb bac bca cba cab` e 6; con quattro lettere diverse 24 righe, cioè $4!$ come nel modulo 2. Il secondo `swap` è il passo indietro (*backtracking*): senza, la stringa resterebbe modificata e le permutazioni successive sarebbero sbagliate. `swap` è nella libreria standard (`<utility>`, incluso da `<iostream>`).

**Esercizio 8. Potenza veloce.** Calcolare $x^n$ con la ricorsione $x^n = (x^{n/2})^2$ se $n$ è pari e $x \cdot x^{n-1}$ se è dispari, contando le moltiplicazioni.

```cpp
// file: potenza_veloce.cpp
#include <iostream>
using namespace std;

int molt = 0;

long long potenza(long long x, int n) {
    if (n == 0) return 1;
    if (n % 2 == 0) {
        long long m = potenza(x, n / 2);     // una sola chiamata, non due
        molt++;
        return m * m;
    }
    molt++;
    return x * potenza(x, n - 1);
}

int main() {
    cout << potenza(3, 20) << " " << molt << endl;
    molt = 0;
    cout << potenza(2, 62) << " " << molt << endl;
    return 0;
}
```

Stampa `3486784401 6` e `4611686018427387904 10`: per $3^{20}$ servono 6 moltiplicazioni invece di 19, in generale circa $2 \log_2 n$. Il punto delicato è salvare $x^{n/2}$ in `m`: scrivendo `potenza(x, n / 2) * potenza(x, n / 2)` le chiamate raddoppierebbero a ogni livello e si tornerebbe a un costo proporzionale a $n$.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Tracciare una ricorsione.** Che cosa stampa `f(4)`?

```cpp
// file: traccia_ricorsione.cpp
#include <iostream>
using namespace std;

int f(int n) {
    if (n <= 1) return 1;
    int a = f(n - 1);
    int b = f(n - 2);
    int r = a + b;
    cout << n << ":" << r << " ";
    return r;
}

int main() {
    cout << endl << f(4) << endl;
    return 0;
}
```

*Passo 1: l'albero delle chiamate.* `f(4)` chiama prima `f(3)` e poi `f(2)` (le due chiamate sono in istruzioni separate apposta: in `f(n - 1) + f(n - 2)` l'ordine di valutazione dei due operandi non è stabilito dal linguaggio); `f(3)` chiama `f(2)` e `f(1)`; ogni `f(2)` chiama `f(1)` e `f(0)`.

*Passo 2: l'ordine delle stampe.* Si stampa dopo le due chiamate, quindi "dal basso": prima `f(2)` dentro `f(3)` (`2:2`), poi `f(3)` (`3:3`), poi il secondo `f(2)` (`2:2`), infine `f(4)` (`4:5`).

*Passo 3: l'uscita.* La riga vuota iniziale, poi `2:2 3:3 2:2 4:5 `, e dopo il valore restituito `5`. Attenzione: in C++17 l'operando di sinistra di `<<` si valuta prima di quello di destra, perciò `endl` è scritto prima della chiamata.

**Guidato 2. Template per contare.** Scrivere un template che conti quante volte un valore compare in un array, e provarlo su interi e caratteri.

*Passo 1: il prototipo.* `template <typename T> int conta(const T a[], int n, const T& x);`

*Passo 2: il corpo.* Un ciclo con `if (a[i] == x)`: il tipo deve avere `==`.

```cpp
// file: conta_template.cpp
#include <iostream>
using namespace std;

template <typename T>
int conta(const T a[], int n, const T& x) {
    int k = 0;
    for (int i = 0; i < n; i++)
        if (a[i] == x) k++;
    return k;
}

int main() {
    int v[] = {1, 3, 1, 1, 2};
    char s[] = "ricorsione";
    cout << conta(v, 5, 1) << " " << conta(s, 10, 'r') << endl;
    return 0;
}
```

*Passo 3: il controllo.* Stampa `3 2`. Con `conta(v, 5, 1.0)` il compilatore non saprebbe se `T` è `int` o `double` e darebbe errore: si risolve con `conta<int>(v, 5, 1)`.

**Guidato 3. Una matrice triangolare dinamica.** Allocare il triangolo di Tartaglia con $n$ righe, dove la riga $i$ ha $i + 1$ elementi.

*Passo 1: la struttura.* Un array di $n$ puntatori; la riga $i$ è un array di $i + 1$ interi: righe di lunghezza diversa, impossibile con una matrice statica.

*Passo 2: i valori.* Gli estremi valgono 1, gli altri sono la somma dei due sopra.

```cpp
// file: tartaglia.cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int** t = new int*[n];
    for (int i = 0; i < n; i++) {
        t[i] = new int[i + 1];
        t[i][0] = t[i][i] = 1;
        for (int j = 1; j < i; j++) t[i][j] = t[i - 1][j - 1] + t[i - 1][j];
    }
    for (int j = 0; j < n; j++) cout << t[n - 1][j] << " ";
    cout << endl;
    for (int i = 0; i < n; i++) delete[] t[i];
    delete[] t;
    return 0;
}
```

*Passo 3: la prova.* Con $n = 7$ l'ultima riga è `1 6 15 20 15 6 1`, i coefficienti $\binom{6}{k}$ del modulo 2. Si liberano prima le righe, poi l'array dei puntatori.

## Riepilogo

Un puntatore contiene un indirizzo: `&` dà l'indirizzo di una variabile, `*` la variabile puntata, `nullptr` indica nessun oggetto. Il nome di un array è l'indirizzo del primo elemento e `a[i]` equivale a `*(a + i)`; l'aritmetica dei puntatori conta in elementi. Un riferimento è un alias fisso; un puntatore è una variabile che può cambiare oggetto ed essere nullo. Con `new` e `delete` (o `new[]` e `delete[]`) si gestiscono oggetti nello heap, che vivono finché non vengono liberati: bisogna evitare perdite di memoria, puntatori pendenti e doppi `delete`; le matrici dinamiche sono array di puntatori a righe. Una funzione ricorsiva ha un caso base e un passo che riduce il problema; ogni chiamata ha il suo record sullo stack. I template di funzione scrivono una funzione per tutti i tipi che offrono le operazioni usate, e il compilatore li istanzia per i tipi effettivi.

## Formulario

### Schemi

```text
int* p = &x;   *p = 3;   p = nullptr;          // puntatore
a[i] == *(a + i)    &a[i] == a + i    q - p    // aritmetica
T* p = new T;  delete p;   T* v = new T[n];  delete[] v;
T** m = new T*[r];  m[i] = new T[c];  ... delete[] m[i]; delete[] m;
p->campo  ==  (*p).campo
template <typename T> T f(const T a[], int n);
```

| Dichiarazione | Si può cambiare `p`? | Si può cambiare `*p`? |
|---|---|---|
| `int* p` | sì | sì |
| `const int* p` | sì | no |
| `int* const p` | no | sì |
| `const int* const p` | no | no |

$$\text{Hanoi: } M(n) = 2M(n - 1) + 1 = 2^n - 1; \qquad \text{Fibonacci ricorsivo: } C(n) = C(n-1) + C(n-2) + 1.$$

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Dereferenziazione | accesso alla variabile puntata con `*` |
| Puntatore nullo | non punta a nessun oggetto |
| Stack, heap | memoria delle chiamate; memoria allocata con `new` |
| Memory leak | memoria allocata e non più raggiungibile |
| Dangling pointer | puntatore a memoria non più valida |
| Caso base, passo ricorsivo | soluzione diretta; riduzione a un problema più piccolo |
| Record di attivazione | parametri e variabili locali di una chiamata |
| Istanziazione | generazione della funzione dal template per un tipo |

### Domande che tornano spesso

- Che cosa sono `&` e `*`? Differenza fra puntatore e riferimento.
- Perché `a[i]` equivale a `*(a + i)`? Che cosa vale `q - p`?
- Come si alloca e libera un array dinamico e una matrice dinamica? Quali errori si fanno?
- Struttura di una funzione ricorsiva; che cosa succede sullo stack; ricorsione e iterazione.
- Che cos'è un template di funzione e quando il compilatore lo istanzia?
