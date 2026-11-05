---
corso: Fondamenti di Informatica
modulo: 6
titolo: Classi e oggetti
programma: [FI-09]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 6 · Classi e oggetti

**In questo modulo.** Si usano le strutture e le funzioni del modulo 4 e i puntatori, la memoria dinamica e i template del modulo 5. Si passa dalla struttura, che raggruppa solo dati, alla **classe**, che mette insieme dati e operazioni e decide che cosa è visibile da fuori. Si vedono attributi e metodi, il controllo di accesso, i costruttori (di default, con parametri, di copia) e il distruttore, i selettori e i modificatori, i metodi costanti e il puntatore `this`, il sovraccarico degli operatori, le classi che gestiscono memoria dinamica con la "regola dei tre", e i template di classe. È la base della prova pratica del secondo semestre, che chiede sempre di scrivere una classe con costruttori, selettori, modificatori, operatore di assegnamento e alcuni metodi di calcolo. Alla fine del modulo si sa scrivere una classe completa da una specifica a parole e usarla in un programma con oggetti allocati dinamicamente.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (Fondamenti, secondo semestre: classi, template delle classi), esercitazioni del 18 e 25 marzo, del 1° aprile, `Esercitazioni_15_classi_allocazione_dinamica`; prove 2016-2020 (FI-09)
> Il modulo è scritto in revisione dal materiale del corso. Si seguono le convenzioni delle slide: attributi privati con il trattino basso (`_dim`), selettori `get…`, modificatori `set…`, operatore di assegnamento che restituisce un riferimento costante. I programmi sono compilati ed eseguiti da `strumenti/verifica.py`, con AddressSanitizer per le perdite di memoria.

## 6.1 Dalla struttura alla classe

Una struttura del modulo 4 è un contenitore di dati: chiunque può leggerne e modificarne i campi, anche mettendoci valori senza senso (una data con il mese 13, una frazione con denominatore 0). Nella **programmazione orientata agli oggetti** un **oggetto** ha uno **stato** (i suoi dati, gli **attributi**) e un **comportamento** (le operazioni che sa fare, i **metodi**), e una **classe** è il tipo degli oggetti, il loro "stampo".

Il **controllo di accesso** separa ciò che si usa da fuori da ciò che riguarda solo la classe. I membri **`private`** sono accessibili solo dai metodi della classe; quelli **`public`** da chiunque. Di regola gli attributi sono privati e si raggiungono solo attraverso i metodi pubblici: è l'**incapsulamento**, che permette alla classe di garantire che il suo stato sia sempre valido e di cambiare la rappresentazione interna senza toccare il codice che la usa (modulo 7). In una `class` i membri sono privati se non si dice altro, in una `struct` pubblici: è l'unica differenza.

```cpp
// file: data.cpp
#include <iostream>
using namespace std;

class Data {
    int _g, _m, _a;                        // privati
    static int giorni(int m, int a);       // metodo d'aiuto, privato
public:
    Data();                                // costruttore di default
    Data(int g, int m, int a);             // costruttore con parametri
    int getGiorno() const { return _g; }   // selettori
    int getMese() const { return _m; }
    int getAnno() const { return _a; }
    bool setData(int g, int m, int a);     // modificatore con controllo
    void avanza();                         // giorno successivo
    void stampa() const;
};

int Data::giorni(int m, int a) {
    if (m == 2) return (a % 4 == 0 && a % 100 != 0) || a % 400 == 0 ? 29 : 28;
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

Data::Data() : _g(1), _m(1), _a(2000) {}

Data::Data(int g, int m, int a) : _g(1), _m(1), _a(2000) {
    setData(g, m, a);                      // se non valida resta 1/1/2000
}

bool Data::setData(int g, int m, int a) {
    if (m < 1 || m > 12 || g < 1 || g > giorni(m, a)) return false;
    _g = g; _m = m; _a = a;
    return true;
}

void Data::avanza() {
    if (++_g > giorni(_m, _a)) {
        _g = 1;
        if (++_m > 12) { _m = 1; _a++; }
    }
}

void Data::stampa() const { cout << _g << "/" << _m << "/" << _a << endl; }

int main() {
    Data d(28, 2, 2028), e(31, 4, 2026);   // e non valida
    d.avanza();
    d.stampa();                            // 29/2/2028: bisestile
    d.avanza();
    d.stampa();
    e.stampa();
    cout << e.setData(31, 12, 2026) << " ";
    e.avanza();
    e.stampa();
    return 0;
}
```

La dichiarazione della classe è la sua **interfaccia**: dice che cosa si può fare con gli oggetti. Le definizioni dei metodi, fuori dalla classe, si scrivono con il nome della classe e l'operatore di **risoluzione di visibilità** `::` (`void Data::avanza()`); i metodi molto brevi si possono definire direttamente dentro la classe. Nei progetti veri l'interfaccia sta in un file di intestazione (`Data.h`) e l'implementazione in `Data.cpp`. Un metodo si chiama su un oggetto con il punto, `d.avanza()`, e lavora sugli attributi di quell'oggetto. Un metodo `static` appartiene alla classe e non a un oggetto: `giorni` non usa gli attributi.

## 6.2 Costruttori e distruttore

Un **costruttore** è un metodo con lo stesso nome della classe e senza tipo di ritorno, chiamato automaticamente quando un oggetto viene creato: serve a dare agli attributi valori iniziali validi. Ce ne possono essere più d'uno (overloading):

- il **costruttore di default**, senza parametri, usato in `Data d;` e quando si crea un array di oggetti; se una classe non dichiara nessun costruttore il compilatore ne genera uno che non inizializza gli attributi di tipo fondamentale;
- i **costruttori con parametri**, `Data e(31, 4, 2026);`;
- il **costruttore di copia**, `Data(const Data& d)`, usato quando si crea un oggetto come copia di un altro: `Data f(d);`, `Data f = d;`, e ogni volta che un oggetto si passa o si restituisce **per valore**. Il parametro deve essere un riferimento: se fosse per valore, per passarlo servirebbe già il costruttore di copia.

La **lista di inizializzazione** (`: _g(1), _m(1), _a(2000)`) inizializza gli attributi prima del corpo del costruttore; è il modo consigliato, e l'unico per gli attributi costanti e i riferimenti.

Il **distruttore** `~Data()` è chiamato automaticamente quando l'oggetto finisce di esistere: all'uscita dal blocco per un oggetto locale, con `delete` per uno dinamico. Non ha parametri né tipo di ritorno, e ce n'è uno solo. Serve soprattutto a liberare le risorse che l'oggetto possiede, come la memoria dinamica (6.5).

**Oggetti dinamici.** `Data* p = new Data(1, 3, 2027);` alloca un oggetto e chiama il costruttore; si usano i metodi con la freccia, `p->avanza()`; `delete p;` chiama il distruttore e libera. `Data* v = new Data[10];` crea dieci oggetti con il costruttore di default, liberati con `delete[] v;`.

## 6.3 Selettori, modificatori, `const` e `this`

Un **selettore** (*getter*) restituisce il valore di un attributo senza modificarlo; un **modificatore** (*setter*) lo cambia, controllando che il nuovo valore sia valido. I selettori si dichiarano **`const`** (la parola dopo i parametri): un metodo costante promette di non modificare l'oggetto, e il compilatore lo verifica. È necessario per chiamare metodi su oggetti costanti o passati per riferimento costante: su un `const Data& d` si può chiamare solo `d.stampa()` se `stampa` è `const`.

Dentro un metodo, **`this`** è un puntatore all'oggetto su cui il metodo è stato chiamato: `_g` equivale a `this->_g`. Serve per distinguere un attributo da un parametro con lo stesso nome (`this->x = x;`), per confrontare l'oggetto con un altro (`if (this != &v)`) e per restituire l'oggetto stesso (`return *this;`).

## 6.4 Il sovraccarico degli operatori

Per una classe si possono ridefinire gli operatori: `a + b` con `a` oggetto diventa la chiamata `a.operator+(b)`. L'operatore si dichiara come metodo (il primo operando è l'oggetto) oppure come funzione esterna con due parametri; se la funzione esterna deve accedere agli attributi privati la si dichiara **`friend`** della classe. Gli operatori `<<` e `>>` per i flussi devono essere funzioni esterne, perché il primo operando è `cout` (un `ostream`), e restituiscono il flusso per permettere le catene `cout << a << b`.

```cpp
// file: frazione.cpp
#include <iostream>
#include <cstdlib>
using namespace std;

class Frazione {
    int _num, _den;                     // _den > 0, ridotta ai minimi termini
    void semplifica();
public:
    Frazione(int num = 0, int den = 1); // fa anche da costruttore di default
    int getNum() const { return _num; }
    int getDen() const { return _den; }
    Frazione operator+(const Frazione& f) const;
    Frazione operator*(const Frazione& f) const;
    bool operator==(const Frazione& f) const;
    bool operator<(const Frazione& f) const;
    friend ostream& operator<<(ostream& os, const Frazione& f);
};

static int mcd(int a, int b) { return b == 0 ? a : mcd(b, a % b); }

void Frazione::semplifica() {
    if (_den < 0) { _num = -_num; _den = -_den; }
    int m = mcd(abs(_num), _den);
    if (m > 1) { _num /= m; _den /= m; }
}

Frazione::Frazione(int num, int den) : _num(num), _den(den == 0 ? 1 : den) {
    semplifica();
}

Frazione Frazione::operator+(const Frazione& f) const {
    return Frazione(_num * f._den + f._num * _den, _den * f._den);
}

Frazione Frazione::operator*(const Frazione& f) const {
    return Frazione(_num * f._num, _den * f._den);
}

bool Frazione::operator==(const Frazione& f) const {
    return _num == f._num && _den == f._den;    // sono ridotte
}

bool Frazione::operator<(const Frazione& f) const {
    return _num * f._den < f._num * _den;       // denominatori positivi
}

ostream& operator<<(ostream& os, const Frazione& f) {
    os << f._num;
    if (f._den != 1) os << "/" << f._den;
    return os;
}

template <typename T>
T massimo(const T a[], int n) {
    T m = a[0];
    for (int i = 1; i < n; i++)
        if (m < a[i]) m = a[i];
    return m;
}

int main() {
    Frazione a(1, 6), b(-3, -4), c(4, -8);
    cout << a << " " << b << " " << c << endl;
    cout << a + b << " " << a * b << " " << (a + a + a == Frazione(1, 2))
         << " " << b + c + 2 << endl;
    Frazione v[] = {a, b, c, Frazione(5, 7)};
    cout << massimo(v, 4) << endl;
    return 0;
}
```

Alcuni dettagli. Gli argomenti di default (`int num = 0, int den = 1`) vanno nel prototipo e non nella definizione. In `b + c + 2` il 2 viene convertito in `Frazione(2)` dal costruttore con un parametro. Un metodo può accedere agli attributi privati di **un altro oggetto della stessa classe** (`f._den`): il controllo di accesso è per classe, non per oggetto. Il template `massimo` del modulo 5 funziona con le frazioni perché la classe definisce `<`.

## 6.5 Classi con memoria dinamica: la regola dei tre

Se una classe ha un attributo puntatore a memoria allocata con `new`, il costruttore di copia e l'assegnamento generati dal compilatore copiano il **puntatore**, non la memoria puntata (**copia superficiale**): due oggetti condividono lo stesso array, la modifica di uno si vede nell'altro, e quando entrambi vengono distrutti l'array viene liberato due volte. Serve la **copia profonda**, e per averla bisogna scrivere tre metodi insieme (**regola dei tre**):

1. il **distruttore**, che libera la memoria;
2. il **costruttore di copia**, che alloca un nuovo array e copia gli elementi;
3. l'**operatore di assegnamento**, che libera la memoria vecchia, alloca la nuova e copia, controllando l'**autoassegnamento** `a = a` (senza il controllo, liberando la memoria vecchia si perderebbero i dati da copiare).

L'assegnamento restituisce `*this`, così si possono scrivere catene `a = b = c`; le slide lo dichiarano con tipo di ritorno `const Vettore&`.

## 6.6 I template di classe

Come le funzioni, anche le classi possono avere un parametro di tipo. Il vettore dinamico è il caso tipico: lo stesso codice per vettori di interi, di reali, di frazioni.

```cpp
// file: vettore.cpp
#include <iostream>
using namespace std;

template <typename T>
class Vettore {
    int _dim;
    T* _val;
public:
    Vettore();
    Vettore(int dim, const T* pval);
    Vettore(const Vettore<T>& v);                    // copia profonda
    ~Vettore();
    int getDim() const { return _dim; }
    T& operator[](int i) { return _val[i]; }         // lettura e scrittura
    const T& operator[](int i) const { return _val[i]; }
    const Vettore<T>& operator=(const Vettore<T>& v);
    Vettore<T> operator+(const Vettore<T>& v) const; // elemento per elemento
};

template <typename T>
Vettore<T>::Vettore() : _dim(0), _val(nullptr) {}

template <typename T>
Vettore<T>::Vettore(int dim, const T* pval) : _dim(dim), _val(new T[dim]) {
    for (int i = 0; i < _dim; i++) _val[i] = pval[i];
}

template <typename T>
Vettore<T>::Vettore(const Vettore<T>& v) : _dim(v._dim), _val(new T[v._dim]) {
    for (int i = 0; i < _dim; i++) _val[i] = v._val[i];
}

template <typename T>
Vettore<T>::~Vettore() { delete[] _val; }

template <typename T>
const Vettore<T>& Vettore<T>::operator=(const Vettore<T>& v) {
    if (this != &v) {                     // a = a non deve fare nulla
        delete[] _val;
        _dim = v._dim;
        _val = new T[_dim];
        for (int i = 0; i < _dim; i++) _val[i] = v._val[i];
    }
    return *this;
}

template <typename T>
Vettore<T> Vettore<T>::operator+(const Vettore<T>& v) const {
    int n = _dim < v._dim ? _dim : v._dim;  // la parte comune
    Vettore<T> r(n, _val);
    for (int i = 0; i < n; i++) r._val[i] = r._val[i] + v._val[i];
    return r;
}

template <typename T>
void stampa(const Vettore<T>& v) {
    for (int i = 0; i < v.getDim(); i++) cout << v[i] << " ";
    cout << endl;
}

int main() {
    int a[] = {1, 2, 3}, b[] = {10, 20, 30, 40};
    Vettore<int> x(3, a), y(4, b);
    Vettore<int> z(x);                   // costruttore di copia
    z[0] = 100;                          // x non cambia
    Vettore<int> w;
    w = x + y;
    w = w;                               // autoassegnamento
    stampa(x); stampa(z); stampa(w);
    double d[] = {0.5, 1.5};
    Vettore<double> u(2, d);
    stampa(u + u);
    return 0;
}
```

Ogni metodo definito fuori dalla classe ricomincia con `template <typename T>` e usa il nome completo `Vettore<T>::`. Un template di classe si mette tutto in un file di intestazione, perché il compilatore deve vedere il codice per istanziarlo. Si usano due versioni di `operator[]`: quella non costante restituisce un riferimento e permette di scrivere `z[0] = 100`, quella costante serve sugli oggetti costanti, come il parametro di `stampa`.

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove 2016-2020 (esercizi "identificare e correggere gli errori" e prova al calcolatore con una classe); programmi compilati ed eseguiti con `strumenti/verifica.py` (FI-09)

**Esercizio 1. Identificare e correggere gli errori** nella dichiarazione del template di classe.

```text
1   template <typename T>
2   class Coppia
3   public:
4       Coppia(T a, T b);
5       Coppia(Coppia<T> c);
6       ~Coppia(int k);
7       T getPrimo();
8       void setPrimo(const T& a) const;
9       const Coppia<T>& operator=(const Coppia<T>& c);
10      bool operator==(const Coppia<T>& c) const;
11  private:
12      T _primo, _secondo
13  }
```

Riga 2: manca la graffa aperta, `class Coppia {`. Riga 5: il costruttore di copia riceve un riferimento costante, `Coppia(const Coppia<T>& c);`. Riga 6: il distruttore non ha parametri, `~Coppia();`. Riga 7: un selettore va dichiarato costante, `T getPrimo() const;`. Riga 8: un modificatore non può essere `const`, perché modifica l'oggetto. Riga 12: manca il `;`. Riga 13: dopo la graffa che chiude la classe serve `;`.

**Esercizio 2. Quali metodi vengono chiamati?** Per ogni riga, dire quale costruttore o operatore della classe `Vettore<int>` viene chiamato.

| Codice | Chiamata |
|---|---|
| `Vettore<int> a;` | costruttore di default |
| `Vettore<int> b(3, v);` | costruttore con parametri |
| `Vettore<int> c = b;` | costruttore di copia (non l'assegnamento: `c` nasce ora) |
| `a = b;` | operatore di assegnamento |
| `stampa(b);` con parametro `const Vettore<int>&` | nessuno: si passa un riferimento |
| `void f(Vettore<int> x); f(b);` | costruttore di copia per il parametro, distruttore all'uscita |
| `Vettore<int>* p = new Vettore<int>(b);` | costruttore di copia; poi `delete p;` chiama il distruttore |

**Esercizio 3. La classe `Presenze`** (sul modello della prova al calcolatore). Un corso tiene il registro delle presenze di `NS` studenti a `NL` lezioni. Si scriva la classe `Presenze` con: un codice del corso `_codice` (intero), il numero `_fatte` di lezioni già svolte (intero) e una matrice `_P` di `NS` righe e `NL` colonne, con `_P[i][j]` uguale a 1 se lo studente `i` era presente alla lezione `j`, 0 altrimenti. Metodi: costruttore di default (tutto a zero), costruttore con parametri, costruttore di copia, selettori (quello di `_P` riceve gli indici e restituisce −1 se non validi), modificatori, operatore di assegnamento; `presenzeStudente(i)` (somma della riga, −1 se l'indice non è valido); `presentiLezione(j)` (somma della colonna, −1 se non valido); `piuAssiduo()` (indice dello studente con più presenze, il più piccolo in caso di parità); `percentuali(double p[])`, che mette in `p[i]` la percentuale di presenza dello studente `i` sulle lezioni svolte; `leggiDati(nomeFile)`, che legge dalla prima riga codice e lezioni svolte, poi le `NS` righe della matrice. Il programma alloca dinamicamente un oggetto, legge il file, stampa lo studente più assiduo e quanti studenti sono sotto il 70% di presenze, e libera l'oggetto. Qui `NS` = 4 e `NL` = 6 per tenere piccolo il file di prova.

```cpp
// file: presenze.cpp
#include <iostream>
#include <fstream>
using namespace std;

const int NS = 4, NL = 6;

class Presenze {
    int _codice, _fatte;
    int _P[NS][NL];
public:
    Presenze();
    Presenze(int codice, int fatte, const int P[][NL]);
    Presenze(const Presenze& p);
    int getCodice() const { return _codice; }
    int getFatte() const { return _fatte; }
    int getP(int i, int j) const;
    void setCodice(int codice) { _codice = codice; }
    void setFatte(int fatte) { _fatte = fatte; }
    void setP(const int P[][NL]);
    const Presenze& operator=(const Presenze& p);
    int presenzeStudente(int i) const;
    int presentiLezione(int j) const;
    int piuAssiduo() const;
    void percentuali(double p[]) const;
    void leggiDati(const char nomeFile[]);
};

Presenze::Presenze() : _codice(0), _fatte(0) {
    for (int i = 0; i < NS; i++)
        for (int j = 0; j < NL; j++) _P[i][j] = 0;
}

Presenze::Presenze(int codice, int fatte, const int P[][NL])
    : _codice(codice), _fatte(fatte) {
    setP(P);
}

Presenze::Presenze(const Presenze& p)
    : _codice(p._codice), _fatte(p._fatte) {
    setP(p._P);
}

int Presenze::getP(int i, int j) const {
    if (i < 0 || i >= NS || j < 0 || j >= NL) return -1;
    return _P[i][j];
}

void Presenze::setP(const int P[][NL]) {
    for (int i = 0; i < NS; i++)
        for (int j = 0; j < NL; j++) _P[i][j] = P[i][j];
}

const Presenze& Presenze::operator=(const Presenze& p) {
    if (this != &p) {
        _codice = p._codice;
        _fatte = p._fatte;
        setP(p._P);
    }
    return *this;
}
```

```cpp
// segue: presenze.cpp
int Presenze::presenzeStudente(int i) const {
    if (i < 0 || i >= NS) return -1;
    int s = 0;
    for (int j = 0; j < NL; j++) s += _P[i][j];
    return s;
}

int Presenze::presentiLezione(int j) const {
    if (j < 0 || j >= NL) return -1;
    int s = 0;
    for (int i = 0; i < NS; i++) s += _P[i][j];
    return s;
}

int Presenze::piuAssiduo() const {
    int best = 0;
    for (int i = 1; i < NS; i++)              // > stretto: vince il primo
        if (presenzeStudente(i) > presenzeStudente(best)) best = i;
    return best;
}

void Presenze::percentuali(double p[]) const {
    for (int i = 0; i < NS; i++)
        p[i] = _fatte > 0 ? 100.0 * presenzeStudente(i) / _fatte : 0;
}

void Presenze::leggiDati(const char nomeFile[]) {
    ifstream in(nomeFile);
    in >> _codice >> _fatte;
    for (int i = 0; i < NS; i++)
        for (int j = 0; j < NL; j++) in >> _P[i][j];
}

int main() {
    Presenze* pr = new Presenze;
    pr->leggiDati("presenze.txt");
    cout << "corso " << pr->getCodice() << ", piu' assiduo: "
         << pr->piuAssiduo() << endl;
    double perc[NS];
    pr->percentuali(perc);
    int sotto = 0;
    for (int i = 0; i < NS; i++)
        if (perc[i] < 70) sotto++;
    cout << sotto << " sotto il 70%, presenti alla lezione 2: "
         << pr->presentiLezione(2) << ", getP(9, 0) = " << pr->getP(9, 0)
         << endl;
    Presenze copia(*pr);                      // prova del costruttore di copia
    delete pr;
    cout << copia.presenzeStudente(3) << endl;
    return 0;
}
```

Con il file

```text
104 5
1 1 0 1 1 0
1 1 1 1 1 0
0 1 0 0 1 0
1 1 1 1 0 0
```

stampa `corso 104, piu' assiduo: 1`, poi `1 sotto il 70%, presenti alla lezione 2: 2, getP(9, 0) = -1`, e infine `4`. La copia resta valida dopo il `delete`, perché la matrice è un array dentro l'oggetto e il costruttore di copia l'ha duplicata.

**Esercizio 4. Un vettore di frazioni.** Si può usare `Vettore<Frazione>`? Che cosa serve alla classe `Frazione`?

Sì: `Vettore<T>` usa `new T[dim]`, che richiede il costruttore di default (c'è, grazie agli argomenti di default), l'assegnamento `=` (quello generato dal compilatore va bene, perché `Frazione` non ha memoria dinamica) e, per `operator+`, la somma di due `T` (c'è). Per stamparlo con `stampa` serve `<<` (c'è). È il senso dei template: il codice si adatta a ogni tipo che offre le operazioni usate.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; programmi compilati ed eseguiti con `strumenti/verifica.py` (FI-09)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Rifare i conti di `Presenze`.** Con il file dell'esercizio 3, calcolare a mano le uscite.

*Passo 1: le somme delle righe.* Studente 0: 4; studente 1: 5; studente 2: 2; studente 3: 4.

*Passo 2: il più assiduo.* Lo studente 1, con 5.

*Passo 3: le percentuali su 5 lezioni svolte.* 80%, 100%, 40%, 80%: sotto il 70% c'è un solo studente, il 2.

*Passo 4: la colonna 2.* $0 + 1 + 0 + 1 = 2$. `getP(9, 0)` ha un indice non valido: $-1$. Ultima riga: `copia.presenzeStudente(3)` vale 4.

*Passo 5: la morale.* Prima di consegnare un programma d'esame, si prepara un file piccolo di cui si conoscono a mano i risultati e si confronta.

**Guidato 2. La copia superficiale.** Che cosa succede se nella classe `Vettore` si toglie il costruttore di copia scritto a mano?

*Passo 1: quello generato.* Copia `_dim` e il **puntatore** `_val`.

*Passo 2: l'effetto.* In `Vettore<int> z(x); z[0] = 100;` anche `x[0]` diventerebbe 100, perché `x` e `z` condividono l'array.

*Passo 3: la fine.* All'uscita da `main` vengono distrutti sia `z` sia `x`, e lo stesso array viene liberato due volte: errore di esecuzione (AddressSanitizer lo segnala come *double free*). Per questo distruttore, costruttore di copia e assegnamento vanno scritti insieme.

**Guidato 3. Un contatore di oggetti.** Una classe `Contatore` tiene in un attributo `static` il numero di oggetti esistenti. Che cosa stampa il programma?

```cpp
// file: contatore.cpp
#include <iostream>
using namespace std;

class Contatore {
    static int _vivi;                 // uno solo per tutta la classe
public:
    Contatore() { _vivi++; }
    Contatore(const Contatore&) { _vivi++; }
    ~Contatore() { _vivi--; }
    static int vivi() { return _vivi; }
};

int Contatore::_vivi = 0;             // definizione dell'attributo statico

void f(Contatore) { cout << Contatore::vivi() << " "; }   // per valore

int main() {
    Contatore a;
    {
        Contatore b, c;
        cout << Contatore::vivi() << " ";
    }                                 // b e c distrutti qui
    f(a);                             // copia per il parametro
    Contatore* p = new Contatore[3];
    cout << Contatore::vivi() << " ";
    delete[] p;
    cout << Contatore::vivi() << endl;
    return 0;
}
```

*Passo 1: il blocco interno.* `a`, `b`, `c`: stampa 3; all'uscita dal blocco restano solo `a`.

*Passo 2: la chiamata per valore.* Il parametro (senza nome, perché `f` non lo usa) è una copia: dentro `f` gli oggetti sono 2; all'uscita la copia viene distrutta.

*Passo 3: l'array dinamico.* Tre oggetti in più con il costruttore di default: 4. Dopo `delete[]`, di nuovo 1.

*Passo 4: l'uscita.* `3 2 4 1`. Un parametro che non si usa si può lasciare senza nome, come nel costruttore di copia: il compilatore non avvisa e la copia viene fatta lo stesso.

## Riepilogo

Una classe riunisce attributi e metodi; il controllo di accesso (`private`, `public`) realizza l'incapsulamento, e i metodi si definiscono fuori dalla classe con `Classe::`. I costruttori inizializzano gli oggetti (di default, con parametri, di copia con parametro `const T&`), preferibilmente con la lista di inizializzazione; il distruttore li chiude ed è chiamato all'uscita dal blocco o con `delete`. I selettori sono metodi `const`, i modificatori controllano i valori; `this` punta all'oggetto corrente. Gli operatori si ridefiniscono come metodi o come funzioni esterne (`friend` se servono gli attributi privati), e `<<` restituisce il flusso. Una classe con memoria dinamica deve avere distruttore, costruttore di copia e assegnamento con copia profonda e controllo dell'autoassegnamento. I template di classe parametrizzano il tipo degli elementi; ogni metodo esterno ripete `template <typename T>` e `Classe<T>::`.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (FI-09)

### Lo scheletro di una classe d'esame

```text
class C {
    int _a;  T* _p;  int _m[R][K];          // attributi privati
public:
    C();                                     // default
    C(int a, ...);                           // con parametri
    C(const C& c);                           // di copia
    ~C();                                    // distruttore (se c'e' new)
    int getA() const;   void setA(int a);    // selettori, modificatori
    const C& operator=(const C& c);          // assegnamento
    friend ostream& operator<<(ostream& os, const C& c);
};
const C& C::operator=(const C& c) {
    if (this != &c) { /* libera, alloca, copia */ }
    return *this;
}
template <typename T> T Classe<T>::metodo(...) const { ... }
```

| Situazione | Chi viene chiamato |
|---|---|
| `C x;` / `C x(…);` | costruttore di default / con parametri |
| `C y = x;`, `C y(x);`, passaggio o ritorno per valore | costruttore di copia |
| `y = x;` fra oggetti già esistenti | operatore di assegnamento |
| fine del blocco, `delete p` | distruttore |
| `new C[n]` | $n$ volte il costruttore di default |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Incapsulamento | attributi privati, accesso solo con i metodi |
| Interfaccia, implementazione | che cosa fa la classe; come lo fa |
| Costruttore di copia | crea un oggetto copia di un altro |
| Lista di inizializzazione | inizializza gli attributi prima del corpo |
| Metodo `const` | non modifica l'oggetto |
| `this` | puntatore all'oggetto corrente |
| `friend` | funzione esterna con accesso ai membri privati |
| Copia superficiale, profonda | copia del puntatore; della memoria puntata |
| Regola dei tre | distruttore, copia e assegnamento si scrivono insieme |
| Membro `static` | appartiene alla classe, non al singolo oggetto |

### Domande che tornano spesso

- Differenza fra struttura e classe; che cos'è l'incapsulamento?
- Tipi di costruttore; quando viene chiamato il costruttore di copia e quando l'assegnamento?
- Perché il costruttore di copia riceve un riferimento? Perché l'assegnamento controlla `this != &c`?
- Come si ridefinisce `<<`, e perché non può essere un metodo?
- Che cos'è un template di classe e come si definiscono i suoi metodi fuori dalla classe?
