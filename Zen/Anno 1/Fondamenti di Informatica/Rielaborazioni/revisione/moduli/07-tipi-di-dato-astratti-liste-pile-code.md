---
corso: Fondamenti di Informatica
modulo: 7
titolo: Tipi di dato astratti, liste, pile e code
programma: [FI-10, FI-11]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 7 · Tipi di dato astratti, liste, pile e code

**In questo modulo.** Si usano le classi, i template e la regola dei tre del modulo 6, e i puntatori e la memoria dinamica del modulo 5. È la parte di programmazione modulare con cui si chiude il corso. Si comincia dall'idea di **tipo di dato astratto**: un tipo definito da ciò che si può fare con i suoi valori, non da come è fatto dentro. Poi si studiano tre strutture dati fondamentali come tipi astratti: la **lista concatenata**, con inserimenti, rimozioni e ricerca; la **pila**, in cui l'ultimo elemento entrato è il primo a uscire; la **coda**, in cui esce per primo il primo entrato. Di pile e code si vedono due realizzazioni, con un array e con una lista, e un paio di applicazioni classiche. Alla fine del modulo si sanno scrivere e usare queste classi, disegnare che cosa succede ai puntatori durante un inserimento o una rimozione, e scegliere la realizzazione adatta.

Si seguono le convenzioni delle slide (classe `Node` con `_data` e `_next`, lista con `_head`). I programmi sono stati compilati ed eseguiti con AddressSanitizer, per controllare che tutta la memoria venga liberata.

## 7.1 L'astrazione sui dati

Usando un `int` nessuno pensa al complemento a 2 e ai 32 bit: si usano la somma, il confronto, la stampa. Un **tipo di dato astratto** (ADT, *abstract data type*) generalizza questa idea: è un insieme di valori con un insieme di **operazioni**, descritto solo da che cosa fanno le operazioni. L'ADT "pila", per esempio, è definito da "inserisci in cima", "togli dalla cima", "guarda la cima", "è vuota?", e da una regola: si toglie sempre l'ultimo elemento inserito.

In C++ un ADT si realizza con una classe:

- l'**interfaccia** (la parte pubblica: prototipi dei metodi e loro descrizione) è ciò che conosce chi usa il tipo;
- la **rappresentazione** (gli attributi privati) e l'implementazione dei metodi sono nascoste: è l'**information hiding**.

Il guadagno è l'**indipendenza dalla rappresentazione**: si può cambiare il modo in cui i dati sono memorizzati (un array invece di una lista, un array ordinato invece di uno disordinato) senza cambiare una riga dei programmi che usano la classe, purché l'interfaccia resti la stessa. In 7.4 e 7.5 la stessa interfaccia di pila e di coda viene realizzata in due modi.

## 7.2 Le liste concatenate semplici

Un array ha dimensione fissa e, per inserire un elemento in mezzo, bisogna spostare tutti quelli che seguono. Una **lista concatenata** è una sequenza di **nodi** allocati dinamicamente, ciascuno con un dato e un puntatore al nodo **successivo**; l'ultimo nodo ha il puntatore nullo. La lista è individuata dal **puntatore di testa**, che punta al primo nodo (ed è nullo se la lista è vuota). Si può allungare e accorciare a piacere, e inserire o togliere un nodo è questione di spostare due puntatori; il prezzo è che per arrivare all'elemento $i$-esimo bisogna attraversare i precedenti.

```text
_head -> [ 3 | * ] -> [ 8 | * ] -> [ 5 | 0 ]
```

Come nelle slide, la lista si realizza con due classi: `Node`, il singolo nodo, e `List`, l'intera lista.

```cpp
// file: lista.cpp
#include <iostream>
using namespace std;

class Node {
    int _data;
    Node* _next;
public:
    Node(int data = 0, Node* next = nullptr) : _data(data), _next(next) {}
    int getData() const { return _data; }
    Node* getNext() const { return _next; }
    void setData(int data) { _data = data; }
    void setNext(Node* next) { _next = next; }
};

class List {
    Node* _head;
    void copia(const List& l);            // aiuto per copia e assegnamento
    void svuota();                        // aiuto per distruttore e =
public:
    List() : _head(nullptr) {}
    List(const List& l);
    ~List();
    const List& operator=(const List& l);
    bool empty() const { return _head == nullptr; }
    int size() const;
    void insertFront(int x);
    void insertBack(int x);
    void insertAfter(Node* p, int x);
    void insertOrdered(int x);            // in una lista ordinata
    bool removeFront();
    bool remove(int x);                   // la prima occorrenza
    Node* search(int x) const;
    void print() const;
};
```

**Inserimento in testa.** Si crea un nodo che punta alla vecchia testa, e la testa diventa il nuovo nodo; funziona anche con la lista vuota. Costo costante.

**Inserimento in coda.** Se la lista è vuota è un inserimento in testa; altrimenti si scorre fino all'ultimo nodo (quello con `getNext()` nullo) e lo si fa puntare al nuovo nodo. Costo proporzionale alla lunghezza.

**Inserimento dopo un nodo `p`.** Il nuovo nodo punta al successivo di `p`, e `p` punta al nuovo nodo, **in quest'ordine**: facendo prima `p->setNext(nuovo)` si perderebbe il resto della lista.

```cpp
// segue: lista.cpp
void List::insertFront(int x) { _head = new Node(x, _head); }

void List::insertBack(int x) {
    if (empty()) { insertFront(x); return; }
    Node* p = _head;
    while (p->getNext() != nullptr) p = p->getNext();
    p->setNext(new Node(x));
}

void List::insertAfter(Node* p, int x) {
    if (p == nullptr) return;
    p->setNext(new Node(x, p->getNext()));
}

void List::insertOrdered(int x) {
    if (empty() || x <= _head->getData()) { insertFront(x); return; }
    Node* p = _head;                     // p: ultimo nodo con dato < x
    while (p->getNext() != nullptr && p->getNext()->getData() < x)
        p = p->getNext();
    insertAfter(p, x);
}

bool List::removeFront() {
    if (empty()) return false;
    Node* q = _head;
    _head = _head->getNext();
    delete q;                            // prima si sposta la testa
    return true;
}

bool List::remove(int x) {
    if (empty()) return false;
    if (_head->getData() == x) return removeFront();
    Node* q = _head;                     // q: il nodo PRECEDENTE
    while (q->getNext() != nullptr && q->getNext()->getData() != x)
        q = q->getNext();
    if (q->getNext() == nullptr) return false;   // non c'e'
    Node* r = q->getNext();
    q->setNext(r->getNext());            // si "salta" r
    delete r;
    return true;
}
```

**Rimozione.** Per togliere un nodo bisogna modificare il puntatore del nodo **precedente**: per questo la ricerca si ferma un nodo prima, guardando `q->getNext()`. Il caso della testa è a parte, perché non ha un precedente e va modificato `_head`. In ogni caso si salva l'indirizzo del nodo da togliere, si sistemano i puntatori e solo dopo si fa `delete`.

```cpp
// segue: lista.cpp
Node* List::search(int x) const {
    for (Node* p = _head; p != nullptr; p = p->getNext())
        if (p->getData() == x) return p;
    return nullptr;
}

int List::size() const {
    int n = 0;
    for (Node* p = _head; p != nullptr; p = p->getNext()) n++;
    return n;
}

void List::print() const {
    for (Node* p = _head; p != nullptr; p = p->getNext())
        cout << p->getData() << " ";
    cout << endl;
}

void List::svuota() { while (removeFront()) {} }

void List::copia(const List& l) {        // copia profonda, stesso ordine
    _head = nullptr;
    Node* ultimo = nullptr;
    for (Node* p = l._head; p != nullptr; p = p->getNext()) {
        Node* n = new Node(p->getData());
        if (ultimo == nullptr) _head = n;
        else ultimo->setNext(n);
        ultimo = n;
    }
}

List::List(const List& l) { copia(l); }
List::~List() { svuota(); }

const List& List::operator=(const List& l) {
    if (this != &l) { svuota(); copia(l); }
    return *this;
}

int main() {
    List l;
    l.insertBack(8); l.insertFront(3); l.insertBack(5);
    l.insertAfter(l.search(8), 6);
    l.print();                                   // 3 8 6 5
    List m(l);
    l.remove(8); l.remove(5); l.remove(42);
    l.print(); m.print();                        // m non cambia
    List o;
    int v[] = {7, 2, 9, 2, 4};
    for (int x : v) o.insertOrdered(x);
    o.print();
    m = o;
    cout << m.size() << " " << (m.search(9) != nullptr) << endl;
    return 0;
}
```

Il distruttore deve liberare **tutti** i nodi: con `delete _head` se ne libererebbe solo uno, e gli altri resterebbero allocati e irraggiungibili. Per la stessa ragione della classe `Vettore`, una lista ha bisogno di costruttore di copia e assegnamento con copia profonda. Il ciclo `for (Node* p = _head; p != nullptr; p = p->getNext())` è lo schema di **scansione** di una lista, l'analogo di `for (i = 0; i < n; i++)` per gli array. In `main`, `for (int x : v)` è il ciclo "per ogni elemento" del C++11 su un array.

## 7.3 La lista come template

La lista delle slide ha anche una versione generica, con `template <typename T> class Node` e `template <typename T> class List`: il codice è lo stesso, con `T` al posto di `int` per il dato e `Node<T>*` per i puntatori. I tipi astratti dei paragrafi seguenti sono scritti direttamente come template.

## 7.4 La pila

Una **pila** (*stack*) è una sequenza in cui si inserisce e si toglie sempre dallo stesso estremo, la **cima**: l'ultimo elemento inserito è il primo a uscire (**LIFO**, *last in, first out*), come una pila di piatti. Le operazioni sono `push` (inserisci in cima), `pop` (togli dalla cima), `top` (guarda la cima), `empty`. Le pile sono ovunque in informatica: lo stack delle chiamate di funzione del modulo 5, l'annulla degli editor, il controllo delle parentesi, la valutazione delle espressioni.

**Con un array.** Un array di capacità fissata e un indice `_top` del primo posto libero: `push` scrive in `_v[_top]` e incrementa, `pop` decrementa. Tutte le operazioni hanno costo costante; il limite è la capacità.

```cpp
// file: pila.cpp
#include <iostream>
using namespace std;

template <typename T>
class Pila {                       // realizzazione con un array dinamico
    T* _v;
    int _cap, _top;                // _top = numero di elementi
public:
    Pila(int cap = 100) : _v(new T[cap]), _cap(cap), _top(0) {}
    Pila(const Pila<T>& p) : _v(new T[p._cap]), _cap(p._cap), _top(p._top) {
        for (int i = 0; i < _top; i++) _v[i] = p._v[i];
    }
    ~Pila() { delete[] _v; }
    const Pila<T>& operator=(const Pila<T>& p);
    bool empty() const { return _top == 0; }
    bool full() const { return _top == _cap; }
    bool push(const T& x) {
        if (full()) return false;
        _v[_top++] = x;
        return true;
    }
    bool pop() {
        if (empty()) return false;
        _top--;
        return true;
    }
    T top() const { return _v[_top - 1]; }   // solo se non vuota
};

template <typename T>
const Pila<T>& Pila<T>::operator=(const Pila<T>& p) {
    if (this != &p) {
        delete[] _v;
        _cap = p._cap; _top = p._top;
        _v = new T[_cap];
        for (int i = 0; i < _top; i++) _v[i] = p._v[i];
    }
    return *this;
}
```

**Applicazione: le parentesi bilanciate.** Si scorre la stringa: una parentesi aperta va sulla pila; una chiusa deve corrispondere a quella in cima, che si toglie. Alla fine la pila deve essere vuota.

```cpp
// segue: pila.cpp
bool bilanciata(const char s[]) {
    Pila<char> p;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') p.push(c);
        else if (c == ')' || c == ']' || c == '}') {
            if (p.empty()) return false;             // chiusa di troppo
            char a = p.top();
            p.pop();
            if ((c == ')' && a != '(') || (c == ']' && a != '[') ||
                (c == '}' && a != '{')) return false;
        }
    }
    return p.empty();                                // aperte rimaste?
}

int valutaPostfissa(const char s[]) {   // cifre singole e + - *
    Pila<int> p;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c >= '0' && c <= '9') p.push(c - '0');
        else if (c == '+' || c == '-' || c == '*') {
            int b = p.top(); p.pop();               // l'ordine conta
            int a = p.top(); p.pop();
            p.push(c == '+' ? a + b : c == '-' ? a - b : a * b);
        }
    }
    return p.top();
}

int main() {
    cout << bilanciata("v[(i+1)*2] = {f(x)};") << " "
         << bilanciata("(a[0)]") << " " << bilanciata("((x)") << endl;
    cout << valutaPostfissa("3 4 + 2 *") << " "
         << valutaPostfissa("9 5 3 - -") << endl;
    Pila<int> a(3), b;
    a.push(1); a.push(2); a.push(3);
    cout << a.push(4) << " ";                       // piena
    b = a;
    b.pop();
    cout << a.top() << " " << b.top() << endl;
    return 0;
}
```

Nella **notazione postfissa** l'operatore segue gli operandi: `3 4 + 2 *` è $(3 + 4) \cdot 2 = 14$, e non servono parentesi. La pila la valuta da sinistra a destra: i numeri si impilano, un operatore toglie due operandi e impila il risultato. Attenzione all'ordine: il primo tolto è il secondo operando, e `9 5 3 - -` vale $9 - (5 - 3) = 7$.

**Con una lista.** La cima è la testa della lista: `push` è un inserimento in testa, `pop` una rimozione in testa, entrambi a costo costante, e la pila non ha capacità massima (esercizio 2).

## 7.5 La coda

Una **coda** (*queue*) è una sequenza in cui si inserisce da un estremo (il **fondo**) e si toglie dall'altro (la **testa**): esce per primo il primo entrato (**FIFO**, *first in, first out*), come la fila a uno sportello. Le operazioni sono `enqueue` (accoda), `dequeue` (togli dalla testa), `front` (guarda la testa), `empty`. Si usano per tutto ciò che va servito in ordine di arrivo: le stampe in attesa, i processi pronti di un sistema operativo, i pacchetti di rete.

**Con una lista.** Per avere entrambe le operazioni a costo costante si tengono **due puntatori**, alla testa e all'ultimo nodo: si accoda dopo l'ultimo, si toglie dalla testa. Bisogna curare i casi limite: accodando in una coda vuota il nuovo nodo è sia testa sia fondo; togliendo l'ultimo elemento anche il puntatore al fondo torna nullo.

```cpp
// file: coda.cpp
#include <iostream>
using namespace std;

template <typename T>
class Coda {                          // realizzazione con una lista
    struct Nodo { T dato; Nodo* next; };
    Nodo *_head, *_tail;
    int _n;
public:
    Coda() : _head(nullptr), _tail(nullptr), _n(0) {}
    Coda(const Coda<T>& c) : _head(nullptr), _tail(nullptr), _n(0) {
        for (Nodo* p = c._head; p != nullptr; p = p->next) enqueue(p->dato);
    }
    ~Coda() { while (dequeue()) {} }
    const Coda<T>& operator=(const Coda<T>& c) {
        if (this != &c) {
            while (dequeue()) {}
            for (Nodo* p = c._head; p != nullptr; p = p->next)
                enqueue(p->dato);
        }
        return *this;
    }
    bool empty() const { return _head == nullptr; }
    int size() const { return _n; }
    void enqueue(const T& x) {
        Nodo* nuovo = new Nodo{x, nullptr};
        if (empty()) _head = nuovo;
        else _tail->next = nuovo;
        _tail = nuovo;
        _n++;
    }
    bool dequeue() {
        if (empty()) return false;
        Nodo* q = _head;
        _head = _head->next;
        if (_head == nullptr) _tail = nullptr;   // era l'ultimo
        delete q;
        _n--;
        return true;
    }
    T front() const { return _head->dato; }      // solo se non vuota
};

int main() {
    Coda<int> c;                // giro "a turno": ogni lavoro ha 3 unita'
    int resto[] = {5, 2, 7};    // di lavoro residuo per i lavori 0, 1, 2
    for (int i = 0; i < 3; i++) c.enqueue(i);
    while (!c.empty()) {
        int j = c.front();
        c.dequeue();
        resto[j] -= 3;
        cout << j;
        if (resto[j] > 0) c.enqueue(j);          // non finito: in fondo
        else cout << "*";                        // finito
        cout << " ";
    }
    cout << endl;
    Coda<char> a, b;
    for (char x = 'a'; x <= 'e'; x++) a.enqueue(x);
    b = a;
    b.dequeue(); b.dequeue();
    cout << a.size() << a.front() << " " << b.size() << b.front() << endl;
    return 0;
}
```

Il programma simula la politica **round robin** di un sistema operativo: ogni lavoro riceve a turno 3 unità di tempo e, se non ha finito, torna in fondo alla coda. Stampa `0 1* 2 0* 2 2*` (l'asterisco segna un lavoro finito), poi `5a 3c`. Il nodo qui è una `struct` dentro la classe: è un dettaglio della rappresentazione, invisibile a chi usa la coda.

**Con un array circolare.** Un array di capacità $N$, l'indice della testa e il numero di elementi; il fondo è in posizione $(testa + n) \bmod N$. Quando un indice arriva in fondo all'array ricomincia da 0, così lo spazio liberato in testa viene riusato. Tutte le operazioni hanno costo costante (guidato 2).

| Struttura | Inserimento | Rimozione | Accesso all'elemento $i$ | Limite |
|---|---|---|---|---|
| array | in fondo costante, in mezzo proporzionale a $n$ | idem | costante | capacità fissa |
| lista semplice | in testa costante, in coda proporzionale a $n$ | in testa costante | proporzionale a $i$ | memoria per i puntatori |
| pila (array o lista) | `push` costante | `pop` costante | solo la cima | capacità (con l'array) |
| coda (lista con due puntatori, array circolare) | `enqueue` costante | `dequeue` costante | solo la testa | capacità (con l'array) |

## Esempi ed esercizi svolti

**Esercizio 1. Completare le affermazioni** (sul modello della prova di teoria, su tutto il corso).

| Affermazione | Completamento |
|---|---|
| Il puntatore di testa di una lista semplice punta al … della lista | primo nodo |
| In una pila si estrae per primo l'elemento inserito … | per ultimo (LIFO) |
| Un … identifica un insieme di oggetti e un insieme di operazioni su di essi | tipo di dato astratto |
| Un oggetto allocato … va esplicitamente deallocato | dinamicamente (con `new`) |
| L'istruzione … termina la funzione in esecuzione | `return` |
| Dato un puntatore a un oggetto, si accede ai membri con l'operatore … | `->` |
| Il numero di relazioni fra gli insiemi finiti $A$ e $B$ vale … | $2^{\lvert A \rvert \lvert B \rvert}$ |
| Nei cicli definiti il numero di ripetizioni è controllato da un … | contatore |
| Un elemento $v$ confrontabile con ogni $x \in X$ e minore o uguale di ognuno è un … di $X$ | minorante |
| In una coda realizzata con una lista, l'inserimento avviene in … | fondo (dopo l'ultimo nodo) |

**Esercizio 2. La pila con una lista.** Realizzare l'interfaccia della pila del paragrafo 7.4 con nodi collegati, senza limite di capacità.

```cpp
// file: pila_lista.cpp
#include <iostream>
using namespace std;

template <typename T>
class PilaL {
    struct Nodo { T dato; Nodo* next; };
    Nodo* _cima;
public:
    PilaL() : _cima(nullptr) {}
    PilaL(const PilaL<T>& p) : _cima(nullptr) { copia(p._cima); }
    ~PilaL() { while (pop()) {} }
    const PilaL<T>& operator=(const PilaL<T>& p) {
        if (this != &p) { while (pop()) {} copia(p._cima); }
        return *this;
    }
    bool empty() const { return _cima == nullptr; }
    void push(const T& x) { _cima = new Nodo{x, _cima}; }   // in testa
    bool pop() {
        if (empty()) return false;
        Nodo* q = _cima;
        _cima = _cima->next;
        delete q;
        return true;
    }
    T top() const { return _cima->dato; }
private:
    void copia(Nodo* p) {          // ricorsiva: copia dal fondo alla cima
        if (p == nullptr) return;
        copia(p->next);
        push(p->dato);
    }
};

int main() {
    PilaL<int> p;
    for (int i = 1; i <= 5; i++) p.push(i * i);
    PilaL<int> q(p);
    p.pop(); p.pop();
    cout << p.top() << " " << q.top() << " ";
    while (!q.empty()) { cout << q.top() << " "; q.pop(); }
    cout << endl;
    return 0;
}
```

Stampa `9 25 25 16 9 4 1`: gli elementi escono in ordine inverso di inserimento. La copia è delicata: scorrendo la pila originale dalla cima e facendo `push`, la copia verrebbe rovesciata; la funzione ricorsiva `copia` arriva prima in fondo e inserisce risalendo. L'interfaccia è la stessa di `Pila` (salvo `full`, che qui non serve): chi usa la pila non si accorge del cambio di rappresentazione.

**Esercizio 3. Metodi nuovi per la lista.** Aggiungere alla lista di interi due funzioni: la somma degli elementi e il rovesciamento della lista sul posto, senza allocare nodi.

```cpp
// file: lista_rovescia.cpp
#include <iostream>
using namespace std;

struct Nodo { int dato; Nodo* next; };

void inserisciTesta(Nodo*& testa, int x) { testa = new Nodo{x, testa}; }

int somma(const Nodo* p) {      // ricorsiva
    return p == nullptr ? 0 : p->dato + somma(p->next);
}

void rovescia(Nodo*& testa) {
    Nodo* prec = nullptr;
    Nodo* p = testa;
    while (p != nullptr) {
        Nodo* succ = p->next;     // si salva il resto
        p->next = prec;           // si gira la freccia
        prec = p;
        p = succ;
    }
    testa = prec;
}

void stampa(const Nodo* p) {
    for (; p != nullptr; p = p->next) cout << p->dato << " ";
    cout << endl;
}

void distruggi(Nodo*& testa) {
    while (testa != nullptr) {
        Nodo* q = testa;
        testa = testa->next;
        delete q;
    }
}

int main() {
    Nodo* l = nullptr;
    for (int i = 1; i <= 5; i++) inserisciTesta(l, 10 * i);
    stampa(l);
    rovescia(l);
    stampa(l);
    cout << somma(l) << endl;
    distruggi(l);
    return 0;
}
```

Stampa `50 40 30 20 10`, poi `10 20 30 40 50` e `150`. Qui la lista è scritta "alla C", con una `struct` e funzioni esterne, come in alcune esercitazioni: il puntatore di testa si passa **per riferimento** (`Nodo*&`) alle funzioni che lo devono cambiare. Il rovesciamento usa tre puntatori: se si girasse la freccia di `p` senza aver salvato `p->next`, il resto della lista andrebbe perso.

**Esercizio 4. Disegnare i puntatori.** Una lista contiene `3 8 6 5`; si esegue `remove(6)`. Descrivere i passi.

`q` parte dalla testa (3); `q->getNext()` è 8, diverso da 6: `q` avanza a 8. Ora `q->getNext()` è 6: ci si ferma. `r` = nodo 6; `q->setNext(r->getNext())` fa puntare 8 a 5; `delete r`. Lista: `3 8 5`. Se si facesse `delete r` prima di leggere `r->getNext()`, si leggerebbe memoria già liberata.

### Esercizi più impegnativi

**Esercizio 5. Fondere due liste ordinate senza creare nodi.** Date due liste ordinate (nodi "alla C" come nell'esercizio 3), costruire la lista ordinata che le contiene tutte e due **riusando i nodi**, solo spostando i puntatori.

```cpp
// file: fondi_liste.cpp
#include <iostream>
using namespace std;

struct Nodo { int dato; Nodo* next; };

Nodo* daArray(const int v[], int n) {          // costruisce nello stesso ordine
    Nodo* testa = nullptr;
    for (int i = n - 1; i >= 0; i--) testa = new Nodo{v[i], testa};
    return testa;
}

Nodo* fondi(Nodo* a, Nodo* b) {
    Nodo finto{0, nullptr};                    // nodo sentinella sullo stack
    Nodo* coda = &finto;
    while (a != nullptr && b != nullptr) {
        if (a->dato <= b->dato) { coda->next = a; a = a->next; }
        else { coda->next = b; b = b->next; }
        coda = coda->next;
    }
    coda->next = (a != nullptr) ? a : b;       // il resto, gia' ordinato
    return finto.next;
}

int main() {
    int x[] = {1, 4, 9, 12}, y[] = {2, 3, 10};
    Nodo* l = fondi(daArray(x, 4), daArray(y, 3));
    for (Nodo* p = l; p != nullptr; p = p->next) cout << p->dato << " ";
    cout << endl;
    while (l != nullptr) { Nodo* q = l; l = l->next; delete q; }
    return 0;
}
```

Stampa `1 2 3 4 9 10 12`, come la fusione di array del modulo 4 ma senza memoria in più. Il **nodo sentinella** `finto` evita di trattare a parte il primo nodo della lista risultato: si aggancia sempre a `coda->next`, e alla fine la vera testa è `finto.next`. Il resto della lista che non è finita si attacca in un colpo solo.

**Esercizio 6. Una coda fatta con due pile.** Realizzare la coda con due pile `dentro` e `fuori`: `enqueue` fa `push` su `dentro`; `dequeue` toglie da `fuori` e, se è vuota, prima ci travasa tutta `dentro`.

```cpp
// file: coda_due_pile.cpp
#include <iostream>
using namespace std;

template <typename T>
class Pila {                                    // pila minima su lista
    struct Nodo { T dato; Nodo* next; };
    Nodo* _cima = nullptr;
public:
    Pila() = default;
    Pila(const Pila&) = delete;                 // copia vietata: non serve
    Pila& operator=(const Pila&) = delete;
    ~Pila() { while (pop()) {} }
    bool empty() const { return _cima == nullptr; }
    void push(const T& x) { _cima = new Nodo{x, _cima}; }
    T top() const { return _cima->dato; }
    bool pop() {
        if (empty()) return false;
        Nodo* q = _cima; _cima = q->next; delete q;
        return true;
    }
};

template <typename T>
class CodaP {
    Pila<T> dentro, fuori;
    int travasi = 0;
    void travasa() {
        if (!fuori.empty()) return;
        while (!dentro.empty()) { fuori.push(dentro.top()); dentro.pop(); }
        travasi++;
    }
public:
    void enqueue(const T& x) { dentro.push(x); }
    bool empty() const { return dentro.empty() && fuori.empty(); }
    T front() { travasa(); return fuori.top(); }
    bool dequeue() { travasa(); return fuori.pop(); }
    int getTravasi() const { return travasi; }
};

int main() {
    CodaP<int> c;
    for (int i = 1; i <= 3; i++) c.enqueue(i);
    cout << c.front() << " ";
    c.dequeue();
    c.enqueue(4);
    while (!c.empty()) { cout << c.front() << " "; c.dequeue(); }
    cout << "(" << c.getTravasi() << " travasi)" << endl;
    return 0;
}
```

Stampa `1 2 3 4 (2 travasi)`: l'ordine FIFO è giusto anche se 4 entra mentre 2 e 3 sono già in `fuori`. Il travaso rovescia la pila, quindi rimette in testa il primo entrato; ogni elemento viene travasato una sola volta, perciò in media ogni operazione costa poco anche se un singolo `dequeue` può spostare molti elementi. `= delete` vieta copia e assegnamento: è il modo esplicito di dire che la classe non li supporta, invece di lasciare quelli superficiali generati dal compilatore.

**Esercizio 7. Una lista è palindroma?** Usare una pila per dire se la sequenza di una lista si legge uguale nei due versi.

```cpp
// file: lista_palindroma.cpp
#include <iostream>
using namespace std;

struct Nodo { char dato; Nodo* next; };

bool palindroma(const Nodo* l) {
    const int MAX = 100;
    char pila[MAX];
    int top = 0;
    for (const Nodo* p = l; p != nullptr && top < MAX; p = p->next)
        pila[top++] = p->dato;                  // prima passata: impila
    for (const Nodo* p = l; p != nullptr; p = p->next)
        if (p->dato != pila[--top]) return false;   // la pila esce al contrario
    return true;
}

Nodo* daStringa(const char s[]) {
    Nodo* testa = nullptr;
    Nodo** fine = &testa;                       // dove attaccare il prossimo
    for (int i = 0; s[i] != '\0'; i++) {
        *fine = new Nodo{s[i], nullptr};
        fine = &(*fine)->next;
    }
    return testa;
}

void distruggi(Nodo* l) {
    while (l != nullptr) { Nodo* q = l; l = l->next; delete q; }
}

int main() {
    const char* prove[] = {"radar", "abba", "lista", "x"};
    for (const char* s : prove) {
        Nodo* l = daStringa(s);
        cout << s << ":" << palindroma(l) << " ";
        distruggi(l);
    }
    cout << endl;
    return 0;
}
```

Stampa `radar:1 abba:1 lista:0 x:1`. La pila rovescia la sequenza: confrontando la lista dall'inizio con gli elementi tolti dalla pila si confronta il primo con l'ultimo, il secondo con il penultimo, e così via. In `daStringa` il puntatore a puntatore `fine` indica il campo da riempire (prima `testa`, poi il `next` dell'ultimo nodo): si costruisce la lista nell'ordine giusto senza casi particolari per il primo nodo.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Pila e coda a confronto.** Si inseriscono nell'ordine 1, 2, 3, 4 in una pila e in una coda, poi si tolgono due elementi, si inserisce 5 e si tolgono tutti. In che ordine escono?

*Passo 1: la pila.* Dopo gli inserimenti la cima è 4: escono 4 e 3; resta `1 2` (cima 2); entra 5; escono 5, 2, 1. Ordine: `4 3 5 2 1`.

*Passo 2: la coda.* Escono 1 e 2; resta `3 4`; 5 va in fondo: escono 3, 4, 5. Ordine: `1 2 3 4 5`.

*Passo 3: la regola.* La coda conserva l'ordine di arrivo, la pila lo rovescia: per rovesciare una sequenza basta farla passare da una pila.

**Guidato 2. La coda con un array circolare.**

*Passo 1: la rappresentazione.* Array `_v` di capacità `_cap`, indice `_testa` del primo elemento, numero di elementi `_n`.

*Passo 2: le operazioni.* `enqueue` scrive in `(_testa + _n) % _cap` e incrementa `_n`; `dequeue` porta `_testa` a `(_testa + 1) % _cap` e decrementa `_n`. Vuota se `_n == 0`, piena se `_n == _cap`.

```cpp
// file: coda_circolare.cpp
#include <iostream>
using namespace std;

const int CAP = 4;

class CodaC {
    int _v[CAP];
    int _testa, _n;
public:
    CodaC() : _testa(0), _n(0) {}
    bool empty() const { return _n == 0; }
    bool full() const { return _n == CAP; }
    bool enqueue(int x) {
        if (full()) return false;
        _v[(_testa + _n) % CAP] = x;
        _n++;
        return true;
    }
    bool dequeue() {
        if (empty()) return false;
        _testa = (_testa + 1) % CAP;
        _n--;
        return true;
    }
    int front() const { return _v[_testa]; }
    int posTesta() const { return _testa; }
};

int main() {
    CodaC c;
    for (int x = 1; x <= 5; x++) cout << c.enqueue(x);   // il 5 non entra
    cout << endl;
    c.dequeue(); c.dequeue();
    c.enqueue(6); c.enqueue(7);                          // girano in testa
    cout << c.posTesta() << ":";
    while (!c.empty()) { cout << " " << c.front(); c.dequeue(); }
    cout << endl;
    return 0;
}
```

*Passo 3: la prova.* La prima riga è `11110`: il quinto inserimento fallisce. Dopo due `dequeue` la testa è in posizione 2; 6 e 7 vanno nelle posizioni 0 e 1, liberate. Escono `3 4 6 7`. Senza il modulo, dopo quattro inserimenti la coda non potrebbe più accettare elementi anche con l'array mezzo vuoto.

**Guidato 3. Un ADT con due rappresentazioni.** L'ADT "insieme di interi fra 0 e 99" ha le operazioni `aggiungi`, `togli`, `contiene`, `cardinalita`. Confrontare due rappresentazioni.

*Passo 1: array di booleani.* `bool _c[100]`, con `_c[x]` vero se `x` è nell'insieme: `aggiungi`, `togli` e `contiene` costano un accesso; `cardinalita` richiede di contare (o un contatore in più).

*Passo 2: array ordinato degli elementi.* `int _e[100]` più il numero di elementi: `contiene` con la ricerca binaria del modulo 4 (circa $\log_2 n$ confronti), `aggiungi` e `togli` devono spostare gli elementi per mantenere l'ordine; occupa meno memoria se gli elementi sono pochi e l'intervallo è grande.

*Passo 3: l'interfaccia.* In entrambi i casi la parte pubblica della classe è la stessa (i quattro metodi con gli stessi prototipi): un programma che usa l'insieme non cambia se si passa da una rappresentazione all'altra. È l'indipendenza dalla rappresentazione, il motivo per cui gli attributi sono privati.

## Riepilogo

Un tipo di dato astratto è definito dalle sue operazioni; in C++ è una classe con interfaccia pubblica e rappresentazione privata (information hiding), che si può cambiare senza toccare il codice che la usa. Una lista concatenata semplice è una catena di nodi con dato e puntatore al successivo, a partire dal puntatore di testa: inserimenti e rimozioni spostano puntatori, nell'ordine giusto, e la rimozione richiede il nodo precedente; la scansione segue i puntatori fino a quello nullo; il distruttore libera tutti i nodi, e servono copia e assegnamento profondi. La pila (LIFO) inserisce e toglie dalla cima, con un array o in testa a una lista, e serve per le chiamate, le parentesi e la notazione postfissa. La coda (FIFO) accoda in fondo e toglie dalla testa, con una lista con due puntatori o un array circolare, e serve per servire in ordine di arrivo.

## Formulario

### Schemi sulle liste

```text
scansione:      for (Node* p = _head; p != nullptr; p = p->getNext())
in testa:       _head = new Node(x, _head);
dopo p:         p->setNext(new Node(x, p->getNext()));
togli la testa: Node* q = _head; _head = _head->getNext(); delete q;
togli dopo q:   Node* r = q->getNext(); q->setNext(r->getNext()); delete r;
coda, accoda:   if (vuota) _head = n; else _tail->next = n; _tail = n;
coda, togli:    ... if (_head == nullptr) _tail = nullptr;
circolare:      fondo = (testa + n) % CAP;   testa = (testa + 1) % CAP;
```

| ADT | Regola | Operazioni |
|---|---|---|
| pila | LIFO | `push`, `pop`, `top`, `empty` |
| coda | FIFO | `enqueue`, `dequeue`, `front`, `empty` |
| lista | sequenza con accesso per scansione | inserimenti, rimozioni, ricerca, scansione |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Tipo di dato astratto | valori più operazioni, indipendente dalla rappresentazione |
| Information hiding | rappresentazione nascosta dietro l'interfaccia |
| Nodo | dato più puntatore al successivo |
| Puntatore di testa | punta al primo nodo; nullo se la lista è vuota |
| LIFO, FIFO | l'ultimo entrato esce per primo; il primo entrato esce per primo |
| Array circolare | gli indici ripartono da 0 con il modulo |
| Notazione postfissa | operatore dopo gli operandi, valutata con una pila |

### Domande che tornano spesso

- Che cos'è un tipo di dato astratto; che cosa vuol dire indipendenza dalla rappresentazione?
- Differenze fra array e lista; costo delle operazioni.
- Come si inserisce e si toglie un nodo; perché l'ordine delle istruzioni conta?
- Pila e coda: definizione, operazioni, realizzazione con array e con lista, applicazioni.
- Perché una classe lista ha bisogno di distruttore, costruttore di copia e assegnamento?
