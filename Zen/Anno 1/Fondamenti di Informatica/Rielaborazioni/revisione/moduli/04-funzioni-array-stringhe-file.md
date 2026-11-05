---
corso: Fondamenti di Informatica
modulo: 4
titolo: Funzioni, array, stringhe, file e strutture
programma: [FI-06, FI-07]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 4 · Funzioni, array, stringhe, file e strutture

**In questo modulo.** Si usano i tipi, le espressioni e i cicli del modulo 3. Si impara a dividere un programma in **funzioni**, con il passaggio dei parametri per valore e per riferimento, e a gestire collezioni di dati: gli **array** a una e due dimensioni, con gli algoritmi di base (somma, massimo, ricerca, ordinamento), le **stringhe** come array di caratteri, i **file** di testo in lettura e in scrittura e le **strutture**, che raggruppano dati di tipo diverso. È il materiale della prova pratica del primo semestre. Alla fine del modulo si sa scrivere il prototipo di una funzione da una descrizione a parole, come nella prova di teoria, e un programma che legge dati da un file, li mette in array di strutture e li elabora con funzioni.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (programmazione in C++, primo semestre), esercitazioni E04-E07; H.M. Deitel e P.J. Deitel, *C++. Fondamenti di programmazione*, Apogeo (FI-06, FI-07)
> Il modulo è scritto in revisione dal materiale del corso. I programmi sono compilati con `g++ -std=c++17 -Wall -Wextra` ed eseguiti da `strumenti/verifica.py`. Come nel corso si usano gli array e le stringhe "alla C" (`char[]` e `<cstring>`), non `vector` e `string` della libreria standard.

## 4.1 Le funzioni

Una **funzione** è un sottoprogramma con un nome, dei **parametri** e un **valore di ritorno**. Serve a non ripetere codice, a dividere un problema in parti più semplici e a dare un nome a un'operazione. Si scrive il **prototipo** (la dichiarazione: tipo di ritorno, nome, tipi dei parametri, con il `;`) prima di `main`, e la **definizione** (con il corpo) dove si vuole:

```cpp
// file: potenza.cpp
#include <iostream>
using namespace std;

double potenza(double base, int esp);      // prototipo

int main() {
    cout << potenza(2, 10) << " " << potenza(0.5, 3) << endl;
    return 0;
}

double potenza(double base, int esp) {     // definizione
    double r = 1;
    for (int i = 0; i < esp; i++)
        r *= base;
    return r;                              // termina e restituisce r
}
```

Nella chiamata `potenza(2, 10)` i **parametri attuali** 2 e 10 vengono copiati nei **parametri formali** `base` ed `esp`. `return` termina la funzione e restituisce il valore; una funzione che non restituisce nulla ha tipo `void` e può usare `return;` senza valore.

**Passaggio per valore e per riferimento.** Normalmente i parametri sono passati **per valore**: la funzione lavora su una copia, e modificarla non cambia la variabile del chiamante. Con il **riferimento** `&` il parametro formale è un altro nome della variabile del chiamante, e le modifiche si vedono fuori. Serve quando una funzione deve "restituire" più valori (**parametri di uscita**) o modificare i suoi argomenti:

```cpp
// file: riferimenti.cpp
#include <iostream>
using namespace std;

void scambia(int& a, int& b) {
    int t = a;
    a = b;
    b = t;
}

void dividi(int n, int d, int& q, int& r) {   // q e r sono di uscita
    q = n / d;
    r = n % d;
}

void raddoppia(int x) { x *= 2; }             // per valore: inutile

int main() {
    int x = 3, y = 8, q, r;
    scambia(x, y);
    dividi(17, 5, q, r);
    raddoppia(x);
    cout << x << " " << y << " " << q << " " << r << endl;   // 8 3 3 2
    return 0;
}
```

Al parametro per riferimento si deve passare una variabile, non un'espressione: `scambia(x, 5)` non si compila. Per gli oggetti grandi, che non si vogliono copiare ma neanche modificare, si usa il riferimento costante `const T&`.

**Visibilità.** Una variabile dichiarata in un blocco (anche il corpo di una funzione) è **locale**: esiste solo lì, dal punto della dichiarazione alla graffa che chiude. Le variabili dichiarate fuori da tutte le funzioni sono **globali**, visibili ovunque: vanno evitate, perché rendono difficile capire chi modifica che cosa. Ogni chiamata ha le sue variabili locali, create all'ingresso e distrutte all'uscita.

**Sovraccarico (overloading).** Più funzioni possono avere lo stesso nome se differiscono per numero o tipo dei parametri: il compilatore sceglie in base agli argomenti. Non basta che differiscano per il tipo di ritorno.

```cpp
// file: overloading.cpp
#include <iostream>
using namespace std;

int massimo(int a, int b) { return a > b ? a : b; }
double massimo(double a, double b) { return a > b ? a : b; }
int massimo(int a, int b, int c) { return massimo(massimo(a, b), c); }

int main() {
    cout << massimo(3, 9) << " " << massimo(2.5, 1.5) << " "
         << massimo(4, 11, 7) << endl;          // 9 2.5 11
    return 0;
}
```

Fra le funzioni di libreria più usate: `<cmath>` (`sqrt`, `pow`, `fabs`, `sin`…) e `<cstdlib>` (`abs`, `rand`, `srand`). `rand()` dà un intero pseudocasuale fra 0 e `RAND_MAX`; `rand() % n` uno fra 0 e $n - 1$; `srand(seme)` sceglie il punto di partenza della sequenza.

## 4.2 Gli array

Un **array** è una sequenza di elementi dello stesso tipo, in posizioni consecutive di memoria, a cui si accede con un **indice** intero che va da 0 a $n - 1$:

```text
int v[5];                        // 5 interi, v[0] ... v[4], valori indefiniti
int w[5] = {3, 1, 4, 1, 5};      // inizializzati
double z[100] = {0};             // tutti a 0
const int N = 10;  int a[N];     // la dimensione deve essere una costante
```

La dimensione è fissata al momento della compilazione. Il C++ **non controlla** gli indici: `v[5]` o `v[-1]` sono errori di esecuzione che possono scrivere su altre variabili senza alcun messaggio. Un array non si può assegnare in blocco (`v = w` non si compila) né confrontare con `==`: si lavora elemento per elemento con un ciclo. Spesso si dichiara un array "abbastanza grande" e si tiene a parte il numero di elementi effettivamente usati.

**Array e funzioni.** Un array si passa a una funzione scrivendo il parametro come `int a[]`, insieme alla sua dimensione, perché la funzione non ha modo di conoscerla. L'array **non viene copiato**: la funzione lavora sull'originale (si vedrà nel modulo 5 che viene passato l'indirizzo del primo elemento). Se la funzione non deve modificarlo, si scrive `const int a[]`.

```cpp
// file: array.cpp
#include <iostream>
using namespace std;

const int MAX = 100;

int leggi(int a[]) {                    // restituisce quanti ne ha letti
    int n;
    do cin >> n; while (n < 1 || n > MAX);
    for (int i = 0; i < n; i++) cin >> a[i];
    return n;
}

int posMassimo(const int a[], int n) {
    int p = 0;
    for (int i = 1; i < n; i++)
        if (a[i] > a[p]) p = i;
    return p;
}

int cerca(const int a[], int n, int x) {      // ricerca lineare
    for (int i = 0; i < n; i++)
        if (a[i] == x) return i;
    return -1;                                // non trovato
}

void ordina(int a[], int n) {                 // selection sort
    for (int i = 0; i < n - 1; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[m]) m = j;
        int t = a[i]; a[i] = a[m]; a[m] = t;
    }
}

int cercaBinaria(const int a[], int n, int x) {   // a ordinato
    int sx = 0, dx = n - 1;
    while (sx <= dx) {
        int c = (sx + dx) / 2;
        if (a[c] == x) return c;
        if (a[c] < x) sx = c + 1;
        else dx = c - 1;
    }
    return -1;
}

int main() {
    int a[MAX];
    int n = leggi(a);
    cout << "massimo in posizione " << posMassimo(a, n) << endl;
    cout << "il 7 e' in posizione " << cerca(a, n, 7) << endl;
    ordina(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl << "dopo l'ordinamento il 7 e' in posizione "
         << cercaBinaria(a, n, 7) << endl;
    return 0;
}
```

Gli algoritmi da sapere:

- **Massimo**: si parte dal primo elemento e lo si confronta con tutti gli altri ($n - 1$ confronti).
- **Ricerca lineare**: si scorre finché si trova l'elemento; nel caso peggiore $n$ confronti.
- **Ordinamento per selezione** (*selection sort*): al passo $i$ si cerca il minimo fra le posizioni $i, \dots, n - 1$ e lo si scambia con l'elemento in posizione $i$; dopo il passo $i$ i primi $i + 1$ elementi sono ordinati e definitivi. Circa $n^2/2$ confronti.
- **Ordinamento a bolle** (*bubble sort*): si confrontano le coppie adiacenti e si scambiano quelle in ordine sbagliato; dopo ogni passata il più grande "sale" in fondo. Se una passata non fa scambi, l'array è ordinato.
- **Ricerca binaria** (solo su array ordinati): si guarda l'elemento centrale e si dimezza la zona di ricerca; al massimo circa $\log_2 n$ confronti, 7 per 100 elementi.

## 4.3 Le matrici

Un array a due dimensioni è un array di righe: `int m[3][4];` ha 3 righe e 4 colonne, e `m[i][j]` è l'elemento di riga `i` e colonna `j`. In memoria le righe sono una dopo l'altra (memorizzazione per righe). Si scorrono con due cicli annidati. Passando una matrice a una funzione si deve indicare il **numero delle colonne**, perché il compilatore deve sapere quanto saltare per passare da una riga alla successiva: `void stampa(int m[][4], int righe)`.

```cpp
// file: matrici.cpp
#include <iostream>
using namespace std;

const int R = 3, C = 4;

void sommeRighe(const int m[][C], int s[]) {
    for (int i = 0; i < R; i++) {
        s[i] = 0;
        for (int j = 0; j < C; j++) s[i] += m[i][j];
    }
}

void trasposta(const int m[][C], int t[][R]) {
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) t[j][i] = m[i][j];
}

int main() {
    int m[R][C] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    int s[R], t[C][R];
    sommeRighe(m, s);
    trasposta(m, t);
    for (int i = 0; i < R; i++) cout << s[i] << " ";
    cout << endl;
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < R; j++) cout << t[i][j] << " ";
        cout << endl;
    }
    return 0;
}
```

## 4.4 Le stringhe

In C++ "alla C" una **stringa** è un array di `char` che termina con il carattere nullo `'\0'`: `char s[10] = "ciao";` occupa 5 caratteri (`c`, `i`, `a`, `o`, `\0`) e ne può contenere al massimo 9. Il terminatore è ciò che permette alle funzioni di sapere dove finisce la stringa. Per leggere:

- `cin >> s;` legge una parola (si ferma al primo spazio);
- `cin.getline(s, 10);` legge una riga intera, al massimo 9 caratteri più il terminatore.

Le funzioni di `<cstring>`:

| Funzione | Effetto |
|---|---|
| `strlen(s)` | lunghezza, senza il terminatore |
| `strcpy(d, s)` | copia `s` in `d` (`d` deve essere abbastanza grande) |
| `strcat(d, s)` | accoda `s` a `d` |
| `strcmp(a, b)` | 0 se uguali, negativo se `a` viene prima in ordine alfabetico, positivo se dopo |

Servono perché sulle stringhe C non funzionano `=` e `==`: `s1 == s2` confronta gli indirizzi, non il contenuto. Per elaborare una stringa carattere per carattere si scorre finché si incontra `'\0'`; `<cctype>` offre `isdigit`, `isalpha`, `toupper`, `tolower`.

```cpp
// file: stringhe.cpp
#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;

bool palindroma(const char s[]) {
    int i = 0, j = strlen(s) - 1;
    while (i < j) {
        if (tolower(s[i]) != tolower(s[j])) return false;
        i++; j--;
    }
    return true;
}

int contaVocali(const char s[]) {
    int n = 0;
    for (int i = 0; s[i] != '\0'; i++)
        if (strchr("aeiouAEIOU", s[i]) != nullptr) n++;
    return n;
}

int main() {
    char a[40], b[40], c[80];
    cin.getline(a, 40);
    cin >> b;
    cout << strlen(a) << " " << contaVocali(a) << " "
         << palindroma(b) << endl;
    strcpy(c, a);
    strcat(c, "-");
    strcat(c, b);
    cout << c << " " << (strcmp(a, b) < 0 ? "prima" : "dopo") << endl;
    return 0;
}
```

## 4.5 I file

I file di testo si usano come `cin` e `cout`, con i flussi di `<fstream>`: `ifstream` per leggere, `ofstream` per scrivere. Si apre il file, si controlla che l'apertura sia riuscita, si legge o si scrive con `>>`, `<<` e `getline`, si chiude.

```cpp
// file: voti.cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream in("voti.txt");
    if (!in) {                          // apertura fallita
        cout << "file non trovato" << endl;
        return 1;
    }
    char nome[30];
    int voto, n = 0, somma = 0;
    ofstream out("promossi.txt");
    while (in >> nome >> voto) {        // si ferma a fine file
        n++;
        somma += voto;
        if (voto >= 18) out << nome << endl;
    }
    in.close();
    out.close();
    if (n > 0) cout << n << " voti, media " << (double)somma / n << endl;
    ifstream ri("promossi.txt");        // rilettura del file scritto
    while (ri >> nome) cout << nome << " ";
    cout << endl;
    return 0;
}
```

`while (in >> nome >> voto)` è il modo sicuro di leggere "fino alla fine": l'espressione è falsa quando la lettura fallisce, perché il file è finito o il dato non è del tipo atteso. Il controllo con `in.eof()` *prima* di leggere è un errore frequente: `eof` diventa vero solo dopo un tentativo di lettura fallito, e così l'ultimo dato viene elaborato due volte. Per leggere righe intere si usa `in.getline(riga, MAX)`. Aprendo un `ofstream` il file viene creato, o svuotato se esiste; per aggiungere in fondo si apre con `ofstream out("f.txt", ios::app);`.

## 4.6 Le strutture

Una **struttura** raggruppa sotto un nome dati di tipo diverso, i suoi **campi**:

```cpp
// file: studenti.cpp
#include <iostream>
#include <cstring>
using namespace std;

struct Data { int g, m, a; };

struct Studente {
    char nome[30];
    Data nascita;              // struttura annidata
    double media;
};

void stampa(const Studente& s) {
    cout << s.nome << " (" << s.nascita.g << "/" << s.nascita.m << "/"
         << s.nascita.a << ") " << s.media << endl;
}

void ordinaPerMedia(Studente v[], int n) {      // bubble sort, decrescente
    bool scambi = true;
    for (int k = 0; k < n - 1 && scambi; k++) {
        scambi = false;
        for (int i = 0; i < n - 1 - k; i++)
            if (v[i].media < v[i + 1].media) {
                Studente t = v[i];             // le strutture si copiano
                v[i] = v[i + 1];
                v[i + 1] = t;
                scambi = true;
            }
    }
}

int main() {
    Studente v[3] = {{"Anna", {3, 5, 2006}, 26.5},
                     {"Bruno", {12, 1, 2007}, 28.0},
                     {"Carla", {30, 9, 2006}, 24.25}};
    ordinaPerMedia(v, 3);
    for (int i = 0; i < 3; i++) stampa(v[i]);
    strcpy(v[2].nome, "Carlotta");
    cout << v[2].nome << endl;
    return 0;
}
```

Si accede ai campi con il punto: `s.media`, `s.nascita.a`. A differenza degli array, le strutture **si possono assegnare** (`t = v[i]` copia tutti i campi, compresi gli array dentro) e passare per valore; per non copiarle inutilmente le si passa per riferimento, costante se non vanno modificate. Non si possono confrontare con `==`. Un **array di strutture** è il modo naturale di rappresentare una tabella: una struttura per riga, un campo per colonna.

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove 2016-2020 e delle esercitazioni E04-E07; programmi compilati ed eseguiti con `strumenti/verifica.py` (FI-06, FI-07)

**Esercizio 1. Prototipi** (sul modello della prova di teoria). Scrivere il prototipo di: (1) `f1`, che riceve per valore un carattere e due reali e restituisce un intero; (2) `f2`, che riceve una matrice di reali di 50 righe e 20 colonne, una stringa e, per riferimento, un reale, e non restituisce nulla; (3) `f3`, che riceve un array di strutture `Studente`, la sua dimensione e un intero per riferimento, e restituisce una struttura `Studente`; (4) `f4`, che riceve una stringa costante e restituisce un booleano.

```cpp
// file: prototipi.cpp
struct Studente { char nome[30]; double media; };

int f1(char c, double x, double y);
void f2(double m[][20], char s[], double& r);
Studente f3(Studente v[], int n, int& k);
bool f4(const char s[]);

int main() { return 0; }
```

Nella matrice il numero di righe si può omettere (o scrivere: `m[50][20]` è equivalente), quello delle colonne no. I nomi dei parametri sono facoltativi nel prototipo, ma aiutano a capire.

**Esercizio 2. Da esadecimale a decimale** (sul modello dell'esercizio "converti"). La funzione `valore` riceve una stringa di cifre esadecimali (0-9, A-F) e restituisce il numero; il programma rifiuta le stringhe con caratteri non validi e le richiede.

```cpp
// file: esadecimale.cpp
#include <iostream>
using namespace std;

int cifra(char c) {                 // -1 se non e' una cifra esadecimale
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return -1;
}

int valore(const char s[]) {
    int v = 0;
    for (int i = 0; s[i] != '\0'; i++)
        v = v * 16 + cifra(s[i]);   // schema di Horner
    return v;
}

bool valida(const char s[]) {
    if (s[0] == '\0') return false;
    for (int i = 0; s[i] != '\0'; i++)
        if (cifra(s[i]) < 0) return false;
    return true;
}

int main() {
    char s[9];
    cin >> s;
    while (!valida(s)) {
        cout << "stringa non valida, riprova" << endl;
        cin >> s;
    }
    cout << valore(s) << endl;
    return 0;
}
```

Con `B6` stampa 182; con `1G` chiede di nuovo. Lo schema di Horner evita le potenze: $\texttt{B6} = (0 \cdot 16 + 11) \cdot 16 + 6$.

**Esercizio 3. Un file di misure** (sul modello degli esercizi su file). Il file `misure.txt` contiene per ogni riga il nome di un sensore e tre misure intere. Scrivere un programma che, per ogni riga, stampi il nome e la media, e alla fine il sensore con la media più alta. Il numero di righe non è noto, ma è al più 50.

```cpp
// file: misure.cpp
#include <iostream>
#include <fstream>
using namespace std;

struct Sensore { char nome[20]; int m[3]; double media; };

int leggiFile(const char nomeFile[], Sensore v[], int max) {
    ifstream in(nomeFile);
    int n = 0;
    while (n < max && in >> v[n].nome >> v[n].m[0] >> v[n].m[1] >> v[n].m[2]) {
        v[n].media = (v[n].m[0] + v[n].m[1] + v[n].m[2]) / 3.0;
        n++;
    }
    return n;
}

int main() {
    Sensore v[50];
    int n = leggiFile("misure.txt", v, 50);
    int best = 0;
    for (int i = 0; i < n; i++) {
        cout << v[i].nome << " " << v[i].media << endl;
        if (v[i].media > v[best].media) best = i;
    }
    if (n > 0) cout << "migliore: " << v[best].nome << endl;
    return 0;
}
```

Il limite `n < max` impedisce di scrivere oltre la fine dell'array se il file avesse più righe del previsto; va messo **prima** della lettura nella condizione, così il cortocircuito evita di leggere una riga in più.

**Esercizio 4. Matrice e diagonali.** Data una matrice quadrata $5 \times 5$ di interi, scrivere una funzione che restituisca, per riferimento, la somma della diagonale principale e di quella secondaria, e una che dica se la matrice è simmetrica.

```cpp
// file: diagonali.cpp
#include <iostream>
using namespace std;

const int N = 5;

void diagonali(const int m[][N], int& princ, int& sec) {
    princ = sec = 0;
    for (int i = 0; i < N; i++) {
        princ += m[i][i];
        sec += m[i][N - 1 - i];
    }
}

bool simmetrica(const int m[][N]) {
    for (int i = 0; i < N; i++)
        for (int j = i + 1; j < N; j++)     // solo sopra la diagonale
            if (m[i][j] != m[j][i]) return false;
    return true;
}

int main() {
    int m[N][N];
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) m[i][j] = (i + 1) * (j + 1);
    int p, s;
    diagonali(m, p, s);
    cout << p << " " << s << " " << simmetrica(m) << endl;
    m[0][4] = 0;
    cout << simmetrica(m) << endl;
    return 0;
}
```

Con $m_{ij} = (i + 1)(j + 1)$ la diagonale principale somma $1 + 4 + 9 + 16 + 25 = 55$, la secondaria $5 + 8 + 9 + 8 + 5 = 35$, e la matrice è simmetrica: stampa `55 35 1`, poi `0`. Il secondo ciclo parte da `i + 1`: ogni coppia si controlla una volta sola.

**Esercizio 5. Parole in una frase.** Contare le parole di una riga (separate da uno o più spazi) e stampare la più lunga.

```cpp
// file: parole.cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char riga[200], lunga[200] = "";
    cin.getline(riga, 200);
    int parole = 0, i = 0;
    while (riga[i] != '\0') {
        while (riga[i] == ' ') i++;             // salta gli spazi
        if (riga[i] == '\0') break;
        char p[200];
        int k = 0;
        while (riga[i] != ' ' && riga[i] != '\0') p[k++] = riga[i++];
        p[k] = '\0';                             // chiude la parola
        parole++;
        if (strlen(p) > strlen(lunga)) strcpy(lunga, p);
    }
    cout << parole << " " << lunga << endl;
    return 0;
}
```

Con `  il compilatore   segnala un errore ` stampa `5 compilatore`. Dimenticare `p[k] = '\0'` è l'errore tipico: la parola continuerebbe con quello che c'è in memoria.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; programmi compilati ed eseguiti con `strumenti/verifica.py` (FI-06, FI-07)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Valore o riferimento?** Che cosa stampa il programma?

```cpp
// file: passaggi.cpp
#include <iostream>
using namespace std;

void f(int a, int& b, int c[]) {
    a++;
    b += a;
    c[0] = a + b;
}

int main() {
    int x = 1, y = 10, v[2] = {0, 0};
    f(x, y, v);
    f(y, x, v);
    cout << x << " " << y << " " << v[0] << endl;
    return 0;
}
```

*Passo 1: prima chiamata.* `a` è una copia di `x` (1) e diventa 2; `b` è `y`, che diventa 12; `v[0] = 2 + 12 = 14`. Dopo: `x = 1`, `y = 12`.

*Passo 2: seconda chiamata.* `a` è una copia di `y` (12) e diventa 13; `b` è `x`, che diventa $1 + 13 = 14$; `v[0] = 13 + 14 = 27`.

*Passo 3: la stampa.* `14 12 27`. L'array è modificato anche senza `&`, perché non viene mai copiato.

**Guidato 2. Ordinare e fondere.** Due array ordinati `a` ($n$ elementi) e `b` ($m$ elementi) vanno fusi in un terzo array ordinato.

*Passo 1: l'idea.* Due indici `i` e `j`; a ogni passo si copia in `c` il più piccolo fra `a[i]` e `b[j]` e si avanza quell'indice.

*Passo 2: la fine.* Quando uno dei due array finisce, si copia il resto dell'altro.

```cpp
// file: fusione.cpp
#include <iostream>
using namespace std;

int fondi(const int a[], int n, const int b[], int m, int c[]) {
    int i = 0, j = 0, k = 0;
    while (i < n && j < m)
        if (a[i] <= b[j]) c[k++] = a[i++];
        else c[k++] = b[j++];
    while (i < n) c[k++] = a[i++];
    while (j < m) c[k++] = b[j++];
    return k;
}

int main() {
    int a[] = {1, 4, 9, 12}, b[] = {2, 3, 10}, c[7];
    int k = fondi(a, 4, b, 3, c);
    for (int i = 0; i < k; i++) cout << c[i] << " ";
    cout << endl;
    return 0;
}
```

*Passo 3: il risultato.* `1 2 3 4 9 10 12`, con al più $n + m$ confronti: è il cuore dell'ordinamento *merge sort*.

**Guidato 3. Statistiche su un file di temperature.** Il file `temperature.txt` contiene una temperatura reale per riga; contare i giorni sopra la media.

*Passo 1: due passate.* La media si conosce solo alla fine: o si rilegge il file, o si mettono i valori in un array. Si sceglie l'array (al più 365 valori).

*Passo 2: il programma.*

```cpp
// file: temperature.cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream in("temperature.txt");
    double t[365], somma = 0;
    int n = 0;
    while (n < 365 && in >> t[n]) somma += t[n++];
    double media = somma / n;
    int sopra = 0;
    for (int i = 0; i < n; i++)
        if (t[i] > media) sopra++;
    cout << n << " " << media << " " << sopra << endl;
    return 0;
}
```

*Passo 3: la prova.* Con i valori 12.5, 14, 9.5, 16, 13 stampa `5 13 2`: media 13, sopra la media 14 e 16. Con un file vuoto `n` sarebbe 0 e la divisione darebbe un risultato non numerico: in un programma d'esame va controllato.

## Riepilogo

Una funzione ha prototipo e definizione; i parametri passano per valore (copia) o per riferimento (`&`, le modifiche si vedono fuori, per i parametri di uscita); le variabili locali vivono solo nel loro blocco; più funzioni possono avere lo stesso nome con parametri diversi. Gli array hanno dimensione costante, indici da 0 a $n - 1$ non controllati, non si assegnano né si confrontano in blocco e si passano alle funzioni senza copia, con la dimensione a parte; gli algoritmi base sono massimo, ricerca lineare e binaria, ordinamento per selezione e a bolle, fusione. Le matrici sono array di righe e nei parametri richiedono il numero di colonne. Le stringhe sono array di `char` terminati da `'\0'` e si gestiscono con `<cstring>`. I file di testo si leggono con `ifstream` controllando la lettura nella condizione del ciclo e si scrivono con `ofstream`. Le strutture raggruppano campi di tipi diversi, si assegnano e si passano come un tutto, e negli array rappresentano tabelle.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FI-06, FI-07)

### Schemi

```text
tipo nome(tipo p1, tipo& p2, const tipo a[], int n);   // prototipo
void f(int m[][COL], int righe);                       // matrice
char s[N];  cin.getline(s, N);  strlen strcpy strcat strcmp
ifstream in("f.txt");  if (!in) ...;  while (in >> x) ...;  in.close();
ofstream out("f.txt");  out << x << endl;  // ios::app per accodare
struct T { tipo campo; ... };  T v[N];  v[i].campo
```

| Algoritmo | Idea | Confronti |
|---|---|---|
| ricerca lineare | scorre tutto | fino a $n$ |
| ricerca binaria | dimezza (array ordinato) | circa $\log_2 n$ |
| selection sort | minimo del resto in posizione $i$ | circa $n^2/2$ |
| bubble sort | scambi fra adiacenti, il massimo sale | fino a circa $n^2/2$ |
| fusione | il più piccolo dei due in testa | fino a $n + m$ |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Prototipo | dichiarazione della funzione: tipo, nome, parametri |
| Parametro formale, attuale | quello della definizione; quello della chiamata |
| Per valore, per riferimento | copia; alias della variabile del chiamante |
| Visibilità (scope) | parte del programma in cui un nome esiste |
| Overloading | stesso nome, parametri diversi |
| Terminatore `'\0'` | segna la fine di una stringa C |
| Flusso (stream) | sequenza di caratteri da o verso tastiera, schermo, file |
| Struttura | tipo composto da campi di tipi diversi |

### Domande che tornano spesso

- Differenza fra passaggio per valore e per riferimento; perché un array si comporta come per riferimento?
- Perché nel parametro matrice serve il numero di colonne?
- Come si legge un file fino alla fine senza usare `eof()` prima della lettura?
- Che cosa succede con un indice fuori dall'array?
- Descrivere un algoritmo di ordinamento e la ricerca binaria.
