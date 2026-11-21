---
lezione: 9
data: 2026-10-29
argomenti: [soluzione dell'esercizio sui lavori, factory method, ciclo for su intervallo, iteratori della libreria standard, std::map, std::pair, std::unordered_map, complessità della ricerca, puntatori a funzione, oggetti funzione, operator(), static_cast, eccezioni, try, catch, throw, gerarchia delle eccezioni standard, maschere delle eccezioni degli stream, eccezioni personalizzate, costruttori ereditati, tokenizer]
---

# Lezione 9 — Mappe, oggetti funzione ed eccezioni

La lezione di C++ si apre con la discussione della soluzione dell'esercizio sulla stampa dei lavori, proposto nella [[Lezione 05 - Funzioni virtuali e introduzione a UML#Esercizio: stampare un file di lavori|lezione 5]]. Poi introduce tre strumenti che il docente indica come direttamente utili per l'interprete del progetto: le **mappe**, cioè i contenitori che associano valori a chiavi; gli **oggetti funzione**, che permettono di trattare una funzione come un dato; le **eccezioni**, il meccanismo con cui un programma segnala e gestisce gli errori senza andare in crash. Si chiude con un esercizio che realizza la prima fase dell'interprete, il **tokenizer**. Il docente segue di nuovo il libro di Lischner [@lischner2020]: le slide di questa parte, il pacchetto *04_OOprogramming*, coprono l'Exploration 15 (*The Map Data Structure*), l'Exploration 44 (*Function Objects*) e l'Exploration 48 (*Exceptions*), più il testo dell'esercizio sul tokenizer.

> [!warning] Materiali di questa lezione
> Le slide *04_OOprogramming* sono arrivate dopo la prima stesura di questa nota, insieme ai materiali della [[Lezione 11 - Soluzioni degli esercizi, algoritmi e iteratori|lezione 11]]; la nota è stata riallineata a esse. Il codice degli esempi segue le slide dove le slide riportano il codice, corretto dove le slide contengono errori (segnalati caso per caso), ed è stato verificato compilandolo con g++ in modalità C++20. La soluzione della prima parte (stampa dei lavori) resta invece una ricostruzione dalla trascrizione.

## La soluzione dell'esercizio sulla stampa dei lavori

### La sfida

Il docente si sofferma per la prima volta su una delle soluzioni pubblicate. L'esercizio chiedeva di leggere un file con dati su libri, periodici e film e di stamparlo in modo leggibile. La **sfida** era scrivere codice il più generico possibile: aggiungendo una nuova classe, `report`, accanto a `book`, `periodical` e `movie`, oltre alla definizione della nuova classe si doveva cambiare **una sola riga** del resto del programma. La soluzione pubblicata, dice il docente, raccoglie la sfida e la risolve.

Il `main` è quello che ci si aspetta: chiede all'utente il nome di un file, lo apre e passa il lavoro a due funzioni, una che legge le voci (`read_entries`) e una che le stampa (`print_pretty`). Avrebbe potuto fare tutto nel `main`, ma la divisione rende il programma più chiaro.

### La stampa e il polimorfismo

`print_pretty` è la parte che non si modifica mai, ed è quella che usa davvero il polimorfismo. Riceve per riferimento costante un **vettore di puntatori** a `work`. Per stampare ogni lavoro le basta che l'operatore `<<` sia definito per `work`: non importa quale tipo di lavoro ci sia dietro il puntatore, purché derivi da `work`. Il polimorfismo fa sì che venga chiamata ogni volta la funzione di stampa corretta. Aggiungendo altre sottoclassi di `work` di cui interessa solo la stampa, questo codice funziona senza modifiche per qualsiasi sottoclasse, comportandosi per ciascun oggetto come la sottoclasse ha stabilito.

### Tre modi di scorrere un vettore

Il ciclo di stampa è scritto in una forma che il docente immagina non tutti conoscano:

```cpp
for (auto entry : entries) std::cout << *entry << '\n';
```

È il ciclo `for` su intervallo (*range-based for*), detto in gergo **for each**: dice al C++ di scorrere tutto il vettore `entries`, assegnando a `entry` un elemento alla volta. La parola `auto` chiede al compilatore di **dedurre il tipo** da sé, come già visto nella [[Lezione 07 - Design pattern e classi come tipi#Alias di tipo e value type|lezione 7]]. Non si può usare sempre: il compilatore deve avere da qualche parte l'informazione sul tipo. Qui ce l'ha, perché sa che `entries` è un vettore di puntatori a `work`, e quindi che scorrendolo otterrà puntatori a `work`. In questo caso il risparmio è minimo (`auto` invece di `work*`), ma se gli elementi fossero, per esempio, vettori o altre istanze di template, il risparmio diventerebbe sostanziale. Il codice è più compatto e, secondo il docente, più leggibile.

Chi preferisce può usare le forme classiche. La prima tratta il vettore **come un array**, con un indice e il metodo `size()`, e controlla che il puntatore non sia nullo prima di usarlo:

```cpp
for (std::size_t i{0}; i < entries.size(); ++i)
  if (entries[i] != nullptr) std::cout << *entries[i] << '\n';
```

La seconda usa esplicitamente il **pattern Iterator** della [[Lezione 07 - Design pattern e classi come tipi#Iterator|lezione 7]], incorporato nella libreria standard:

```cpp
for (std::vector<work*>::const_iterator it{entries.begin()}; it != entries.end(); ++it)
  std::cout << **it << '\n';
```

Il metodo `begin()` è il **factory method** che restituisce l'iteratore; si usa un `const_iterator` perché non interessa modificare il contenuto del vettore. Il ciclo continua finché l'iteratore è diverso da `end()`, che indica la fine. Rispetto allo schema astratto del pattern ci sono differenze di sintassi, perché il C++ permette di ridefinire gli operatori: invece di un metodo `next()` c'è l'operatore `++`, e invece di `current()` c'è l'operatore di **dereferenziazione** `*`, come se l'iteratore fosse un puntatore. Qui servono due asterischi: il primo estrae dall'iteratore l'elemento del vettore, che è un puntatore, il secondo accede al lavoro puntato.

Il docente consiglia, con gli iteratori, di preferire l'incremento **prefisso** `++it` a quello postfisso `it++`, perché più efficiente. La ragione è che l'incremento postfisso deve restituire il valore *precedente* dell'iteratore, e quindi farne una copia; il prefisso no. Per i tipi predefiniti il compilatore elimina la differenza, ma per un iteratore, che è un oggetto, la copia può avere un costo.

Le tre forme producono lo stesso risultato, e probabilmente anche lo stesso codice compilato: il docente non vuole fare questioni di efficienza, chiede solo di saperle leggere tutte. La prima, anzi, è un'abbreviazione della terza: il compilatore riconduce il ciclo su intervallo a un ciclo con gli iteratori `begin()` ed `end()` [@cppref-rangefor]. Per chiarezza e compattezza il docente preferisce la prima.

### La lettura e il factory method

`read_entries` controlla che il file sia aperto e poi lo legge **riga per riga**, memorizzando ogni riga in una `std::string` e analizzandola con i metodi delle stringhe: è la modalità di lettura che il docente ritiene più affidabile in C++. Ogni riga corrisponde a un oggetto, e il tipo dell'oggetto dipende dall'**etichetta** (*tag*) all'inizio della riga, che dice se si tratta di un libro, di un periodico, di un film. Il «giochino» è affidato a un **factory method**, `make_work`: riceve la riga, guarda l'etichetta e crea l'oggetto del tipo giusto, restituendolo però come puntatore alla classe base `work`. Da lì in poi l'oggetto viene gestito in modo generico.

Ed ecco lo «spoiler»: la riga da cambiare per aggiungere `report` è in `make_work`, perché il factory method deve saper costruire anche il nuovo tipo di oggetto, riconoscendone l'etichetta nel file. È l'**unica** riga da modificare.

Se il puntatore restituito non è nullo, `read_entries` chiama il metodo `parse` dell'oggetto. Anche questo è un punto importante: dopo aver creato l'oggetto del tipo giusto, il programma non va a estrarre i campi della riga in base al tipo, perché allora a ogni nuovo tipo dovrebbe cambiare molto codice. La **responsabilità di analizzare la riga è affidata all'oggetto**. Aggiungere un nuovo tipo significa quindi dargli anche il modo di leggersi, oltre a quello di stamparsi. Infine l'oggetto viene accodato al vettore, si segnala un eventuale errore sul file, si chiude il file e si restituisce il vettore.

Si potrebbe obiettare che restituire un vettore significa copiarlo. Il compilatore ottimizza molti di questi casi da solo, e chi non si fida può usare `std::move` per forzare la semantica di spostamento vista nella [[Lezione 07 - Design pattern e classi come tipi#Lo spostamento|lezione 7]]. Il docente non l'ha fatto perché era il primo programma svolto insieme, prima di aver visto lo spostamento.

### La classe base e le funzioni di appoggio

La classe `work` definisce alcune **costanti di classe** statiche, come la posizione dell'etichetta e del titolo nella riga del file: ce n'è una sola copia, qualunque sia il numero di oggetti. Ha i costruttori, il costruttore di copia, il distruttore, ovviamente **virtuale** perché è una classe base, e due metodi **virtuali puri**, `print` e `parse`. È quindi una classe **astratta**: non si può istanziare, e dichiara l'interfaccia che ogni sottoclasse deve implementare. È questo che garantisce il funzionamento del codice visto prima, che conta proprio sull'esistenza dei due metodi. Un metodo **protetto** imposta identificativo e titolo: nessun altro può modificarli, se non le classi derivate. L'operatore `<<` riceve il lavoro per riferimento e si appoggia su `print`, quindi il polimorfismo funziona.

Il metodo `parse` di `book` ridefinisce (`override`) quello della base: divide la riga in campi in base al separatore e imposta titolo, autore e anno di pubblicazione. Dentro `book` si sa di leggere un libro, quindi si sa quali campi aspettarsi e dove mettere i dati. Questo, insiste il docente, è il meccanismo tipico della programmazione orientata agli oggetti: l'oggetto sa come leggersi e come stamparsi, il programma generale non lo sa e **delega**. E l'oggetto deve saperlo, perché la classe astratta lo impone come **contratto**. Può sembrare filosofia, ma è la parte interessante del programma: non mettere classi per il gusto di farlo, ma usare i contratti dei metodi astratti per delegare le cose specifiche alle classi, così che ogni aggiunta resti il più possibile circoscritta a ciò che va effettivamente aggiunto.

Alcuni dettagli della soluzione:

- il separatore dei campi è un **parametro con valore di default**, una costante dichiarata in cima al file (il punto e virgola), usata se il chiamante non specifica nulla;
- una funzione di appoggio esegue la **divisione** (*split*) di una stringa in campi: «sorprendentemente», osserva il docente, Python ce l'ha e la classe `std::string` del C++20 no; il codice è un esercizio da Fondamenti di Informatica;
- un'altra funzione converte una stringa in un intero creando uno **string stream** (`std::istringstream`) a partire dalla stringa e leggendo l'intero da esso come lo si leggerebbe dall'input standard;
- i commenti delle funzioni sono scritti nello stile di **Doxygen**, simile a Javadoc, che il libro descrive in una delle Exploration. Con questa sintassi l'ambiente di sviluppo mostra la spiegazione di una funzione passandoci sopra con il mouse, come per le funzioni di libreria. Il docente raccomanda di usarli, anche quando il codice è generato da un'IA, per il codice che passerà ad altri o che si riprenderà dopo sei mesi;
- in testa al file c'è una funzione che stampa un messaggio di errore e termina il programma. Su domanda di uno studente, il docente spiega che è un modo «vecchio» di gestire gli errori: oggi si usano le eccezioni, trattate più avanti nella lezione.

> [!warning] Conversione da stringa a intero
> Il docente ricorda che ora dovrebbe esistere anche una funzione di libreria per convertire direttamente una stringa in un intero. Esiste, ed è disponibile da tempo: `std::stoi`, dichiarata in `<string>`, fa parte dello standard dal **C++11**. Lancia `std::invalid_argument` se la conversione non è possibile e `std::out_of_range` se il valore non è rappresentabile [@cppref-stoi].

Il codice seguente è una ricostruzione ridotta dello schema della soluzione, con le classi `book`, `movie` e la nuova `report`, scritta per mostrare i punti discussi; non è il codice pubblicato dal docente. Per renderla autonoma, legge da uno string stream invece che da un file.

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

const char default_separator{';'};

// Divide una riga in campi in base al separatore
std::vector<std::string> split(std::string const& line, char separator = default_separator) {
  std::vector<std::string> fields;
  std::string field;
  std::istringstream in{line};
  while (std::getline(in, field, separator)) fields.push_back(field);
  return fields;
}

class work {
public:
  work() = default;
  work(work const&) = default;
  work& operator=(work const&) = default;
  virtual ~work() = default;
  virtual void print(std::ostream& out) const = 0;                 // contratto: stampa
  virtual void parse(std::string const& line, char separator) = 0; // contratto: lettura
protected:
  static const int tag_pos{0};      // posizione dei campi comuni nella riga
  static const int title_pos{1};
  void set_title(std::string const& t) { title_ = t; }
  std::string const& title() const { return title_; }
private:
  std::string title_;
};

std::ostream& operator<<(std::ostream& out, work const& w) {
  w.print(out);                     // chiamata polimorfa
  return out;
}

class book : public work {
public:
  void print(std::ostream& out) const override {
    out << title() << ", di " << author_ << " (" << year_ << ")";
  }
  void parse(std::string const& line, char separator) override {
    std::vector<std::string> fields{split(line, separator)};
    set_title(fields.at(title_pos));
    author_ = fields.at(2);
    year_ = std::stoi(fields.at(3));
  }
private:
  std::string author_;
  int year_{0};
};

class movie : public work {
public:
  void print(std::ostream& out) const override {
    out << title() << " (film, " << runtime_ << " minuti)";
  }
  void parse(std::string const& line, char separator) override {
    std::vector<std::string> fields{split(line, separator)};
    set_title(fields.at(title_pos));
    runtime_ = std::stoi(fields.at(2));
  }
private:
  int runtime_{0};
};

class report : public work {      // la classe aggiunta dopo
public:
  void print(std::ostream& out) const override {
    out << title() << " (rapporto tecnico n. " << number_ << ")";
  }
  void parse(std::string const& line, char separator) override {
    std::vector<std::string> fields{split(line, separator)};
    set_title(fields.at(title_pos));
    number_ = fields.at(2);
  }
private:
  std::string number_;
};

// Factory method: dall'etichetta all'oggetto del tipo giusto
work* make_work(std::string const& line, char separator = default_separator) {
  std::string tag{line.substr(0, line.find(separator))};
  if (tag == "book") return new book{};
  if (tag == "movie") return new movie{};
  if (tag == "report") return new report{};   // l'unica riga da aggiungere
  return nullptr;
}

std::vector<work*> read_entries(std::istream& in) {
  std::vector<work*> entries;
  std::string line;
  while (std::getline(in, line)) {
    work* w{make_work(line)};
    if (w != nullptr) {
      w->parse(line, default_separator);   // ogni oggetto sa leggersi
      entries.push_back(w);
    }
  }
  return entries;
}

void print_pretty(std::vector<work*> const& entries) {
  for (auto entry : entries) std::cout << *entry << '\n';
}

int main() {
  std::istringstream file{
      "book;Exploring C++20;Ray Lischner;2020\n"
      "movie;Il cammino degli automi;95\n"
      "report;Tokenizer per un sottoinsieme del C;TR-01\n"};
  std::vector<work*> entries{read_entries(file)};
  print_pretty(entries);
  for (auto entry : entries) delete entry;
}
```

L'output è:

```text
Exploring C++20, di Ray Lischner (2020)
Il cammino degli automi (film, 95 minuti)
Tokenizer per un sottoinsieme del C (rapporto tecnico n. TR-01)
```

Il programma è stato controllato anche con Valgrind, senza perdite di memoria; le due forme alternative del ciclo di stampa viste sopra producono lo stesso output. Chi ha domande sulla soluzione pubblicata, conclude il docente, può scrivergli per email o in un altro momento.

## Le mappe

### Chiavi e valori

Una **mappa** memorizza coppie **chiave-valore**. La chiave, come dice il nome, è la chiave d'accesso al valore: un identificativo sintetico e **univoco** a cui è associato un insieme di valori. Gli esempi del docente vengono dalla vita quotidiana e dalle basi di dati: il numero di matricola è la chiave per accedere al record di uno studente (e non ci sono due matricole uguali, perché sono progressive), il codice fiscale per i dati fiscali e sanitari, la targa per un automezzo. Matematicamente una mappa è una **funzione** dalle chiavi ai valori.

Nell'interprete del progetto, e già negli esercizi, le chiavi saranno per esempio gli **identificatori** delle variabili ed eventualmente delle funzioni: a una variabile è associato un valore, e il suo nome deve essere univoco all'interno di uno **scope**. In un certo scope, quella variabile con quel nome corrisponde a un certo spazio di memoria e a nessun altro. Se il linguaggio permette scope annidati, come il C++ (funzioni dentro classi, e così via), possono esistere variabili con lo stesso nome in scope diversi; a quel punto l'identificativo diventa la coppia scope più nome. Scrivendo `std::cout` si dice che si tratta del `cout` della libreria standard, e l'identificativo torna univoco. Le mappe sono quindi fondamentali per la programmazione in generale e per scrivere interpreti e compilatori in particolare.

### `std::map`

Il C++ offre un tipo di dato parametrico, **`std::map`**, dichiarato in `<map>`: come per `std::vector`, il tipo della chiave e quello del valore si scelgono come parametri del template, per esempio `std::map<std::string, int>`. Come chiave vanno bene tutti i tipi di base: interi, caratteri, numeri in virgola mobile, stringhe della libreria standard. Il valore può essere sostanzialmente qualunque cosa.

La chiave è più critica perché tra le chiavi deve esistere una **relazione d'ordine**. Gli interi, i numeri in virgola mobile e le stringhe ce l'hanno, e quindi vanno bene. Va bene perfino un `std::vector`, per cui è definito l'ordine lessicografico, come per le stringhe. Una classe definita dall'utente, invece, funziona come chiave solo se ne è stato definito l'ordinamento: altrimenti il compilatore segnala un errore. Come si vedrà nel secondo semestre, la struttura dati interna della mappa è organizzata proprio sfruttando l'ordine delle chiavi, ed è la chiave che serve per ritrovare il valore. Per ora il docente chiede di prenderla «a scatola nera».

> [!warning] Quale operatore serve
> Il docente parla di ridefinire l'operatore «minore o uguale». Per default `std::map` ordina le chiavi con `std::less`, cioè con l'operatore **`<`** [@cppref-map]: è quello che una classe usata come chiave deve definire. Lo si è verificato: con una `struct point` priva di operatori, `std::map<point, int>` produce l'errore `no match for 'operator<'`.

### Contare le parole

L'applicazione classica delle mappe è il **conteggio delle frequenze**. Si raccolgono delle stringhe in un vettore, per esempio leggendole da un file, e si vuole sapere quante volte compare ciascuna: se le stringhe sono nomi propri, quante volte compaiono Giulio, Maria, Silvia. Il risultato è una tabella che associa a ogni stringa il numero delle sue occorrenze.

Il modo «brutale» è prendere il primo elemento del vettore e scandire tutti gli altri contando quante volte ricompare, poi fare lo stesso con il secondo, con il terzo, e così via. Anche senza aver ancora studiato la complessità degli algoritmi, osserva il docente, suona costoso: per il primo elemento si scandiscono gli altri $n - 1$, per il secondo $n - 2$, e così via, per un totale di
$$
(n-1) + (n-2) + \cdots + 1 = \frac{n(n-1)}{2}
$$
confronti, un costo **quadratico** nel numero degli elementi.

Con una mappa il procedimento è immediato. La chiave è la parola da contare, il valore il numero di volte che compare. Ogni volta che si incontra una parola nuova si aggiunge una voce con valore 1; se la parola è già presente, si incrementa il valore. E la mappa lo fa in modo efficiente.

```cpp
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

auto count_words(std::vector<std::string> const& pool) {
  std::map<std::string, int> counts{};
  for (auto const& word : pool)
    counts[word] += 1;                    // se la chiave manca, il valore parte da 0

  std::vector<std::pair<std::string, int>> table;
  for (auto const& element : counts)      // ogni elemento è una coppia (chiave, valore)
    table.push_back(element);
  return table;
}

int main() {
  std::vector<std::string> pool{"Maria", "Giulio", "Silvia", "Maria", "Giulio", "Maria"};
  auto result{count_words(pool)};
  for (auto const& element : result)
    std::cout << element.first << ' ' << element.second << '\n';
}
```

L'output è `Giulio 2`, `Maria 3`, `Silvia 1`. Nelle slide il `main` dell'esempio lascia la lettura delle stringhe come compito (un commento `TODO`, «leggere le stringhe nel vettore, per esempio da un file»), e il testo dell'esempio suggerisce di usare la semantica di spostamento esplicita, `std::move`, quando si inseriscono le stringhe lette nel vettore; qui, per avere un programma completo, il vettore è inizializzato direttamente. Ci sono diversi punti da notare.

> [!warning] Refusi nel codice delle slide
> Il codice delle slide sulle mappe non compila così com'è: mancano i punti e virgola dopo `std::map<std::string, int> counts{}`, dopo `std::vector<std::pair<std::string, int>> table{}` e dopo `auto result = count_words(pool)`. Nell'esempio della ricerca, poi, la dichiarazione `std::map counts{};` non specifica i parametri del template e non ha un inizializzatore da cui il compilatore possa dedurli: va scritto `std::map<std::string, int> counts{};`, come nel codice di questa nota. Il ciclo `for (auto word : pool)` delle slide copia ogni stringa; `auto const&`, usato qui, evita la copia.

**L'accesso con le parentesi quadre.** Alla mappa si accede come a un vettore, perché `std::map` ridefinisce l'operatore `[]`. Ma non ci sono indici, perché una mappa non è una struttura sequenziale: al posto dell'indice si usa la chiave. L'istruzione `counts[word] += 1` funziona anche la prima volta che si incontra una parola, perché quando la chiave non è presente l'operatore `[]` inserisce una nuova voce con il valore **inizializzato per default**, cioè 0 per un intero [@cppref-map-at]. Chi non si fida, dice il docente, può prima cercare la parola e poi decidere se inserirla o incrementarla; si vedrà tra poco come.

> [!warning] Un effetto collaterale di `[]`
> Proprio perché inserisce le chiavi mancanti, l'operatore `[]` non va usato per *controllare* se una chiave c'è: anche una semplice lettura come `int x{counts["Paolo"]};` aggiunge alla mappa la voce `Paolo` con valore 0. Lo si è verificato: la dimensione della mappa passa da 3 a 4. Per la sola ricerca si usa `find`, presentato più avanti; per lo stesso motivo `[]` non si può usare su una mappa costante [@cppref-map-at].

**L'iterazione restituisce coppie.** Le mappe si scorrono come i vettori, con il ciclo su intervallo o con gli iteratori, perché sono contenitori. Ma un vettore restituisce direttamente i suoi elementi (anche un vettore, a ben vedere, è una mappa da indici a elementi, ma è chiaro che si vogliono gli elementi), mentre una mappa restituisce delle **coppie**. La libreria standard ha un template apposito, **`std::pair`**, il tipo generico «coppia», usato in molti punti dove servono coppie di valori. Gli elementi di una `std::map<K, V>` sono di tipo `std::pair<const K, V>`: la chiave è costante, perché cambiarla sul posto romperebbe l'ordinamento [@cppref-map].

**I campi `first` e `second`.** `std::pair` è una `struct` con due attributi **pubblici**, `first` e `second`, a cui si accede direttamente, senza metodi. Il docente richiama un consiglio dato in precedenza: per una struttura semplice, priva di un meccanismo interno da proteggere, rendere privati i campi e aggiungere metodi di accesso (*getter* e *setter*) è inutile. La libreria standard fa esattamente così: una coppia è una coppia, e i suoi campi si possono leggere e scrivere liberamente.

**`auto` e tipizzazione statica.** Il tipo di ritorno di `count_words` è `auto`: il compilatore deduce che è `std::vector<std::pair<std::string, int>>`, e si comincia ad apprezzare la comodità di non doverlo scrivere. Da qualche parte, però, il tipo va dichiarato: nella dichiarazione di `table` va scritto per esteso, perché altrimenti il compilatore non avrebbe modo di saperlo. Il C++ non è Python, che è tipizzato dinamicamente: è tipizzato **staticamente**, e `auto` funziona solo se il tipo si può ricavare da informazioni già presenti.

### Quanto costa

Il docente anticipa un ragionamento che sarà centrale nel secondo semestre. Il primo ciclo di `count_words` gira tante volte quante sono le parole del vettore, diciamo $n$. Il secondo gira tante volte quante sono le voci della mappa, diciamo $m$, cioè quante sono le parole **distinte**. Quale relazione c'è tra $m$ ed $n$? Si ha $m \leq n$: se ogni parola compare una sola volta, la mappa ha tante voci quante parole; se c'è almeno una ripetizione, ne ha meno. Il secondo ciclo, quindi, gira **al più** $n$ volte. Ragionamenti di questo tipo, «al più $n$», saranno frequenti nell'analisi della complessità.

Se ogni accesso alla struttura dati richiedesse un tempo indipendente dal numero di voci già presenti, cioè **costante**, il tempo complessivo crescerebbe linearmente con $n$. Per `std::map` non è così: la ricerca, l'inserimento e la rimozione di una chiave hanno costo **logaritmico** nel numero di voci [@cppref-map], e il logaritmo cresce più lentamente della funzione identità. A occhio, quindi, il conteggio con `std::map` costa circa $n \log n$: una funzione che cresce un po' più velocemente di una retta, ma molto più lentamente di una parabola. Quando si troveranno complessità come $n \log n$, osserva il docente, ci si potrà fregare le mani, perché sono i casi fortunati. Il grafico confronta le tre crescite.

```chart
type: line
labels: [2, 4, 8, 16, 32, 64]
series:
  - title: n
    data: [2, 4, 8, 16, 32, 64]
  - title: n log₂ n
    data: [2, 8, 24, 64, 160, 384]
  - title: n²
    data: [4, 16, 64, 256, 1024, 4096]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: true
```

> [!tip] Approfondimento — Come è fatta una `std::map`
> #approfondimento
> La documentazione della libreria standard osserva che le mappe sono di solito realizzate con **alberi rosso-neri** [@cppref-map], una classe di alberi binari di ricerca bilanciati la cui altezza resta logaritmica nel numero di nodi; è da qui che viene il costo logaritmico delle operazioni. Gli alberi rosso-neri sono trattati nel Cormen-Leiserson-Rivest-Stein [@cormen2009], e verranno ripresi nel secondo semestre. L'ordine delle chiavi ha anche un effetto visibile: scorrendo una `std::map` le chiavi escono in ordine crescente, come si vede nell'output del conteggio (Giulio, Maria, Silvia).

### Cercare una chiave

Per cercare una chiave si usa il metodo **`find`**, e qui, osserva il docente, i pattern entrano di nuovo in gioco: `find` restituisce un **iteratore** che «punta» alla coppia chiave-valore, oppure `end()`, il valore che segna la fine dell'iterazione, se la chiave non è presente.

```cpp
std::map<std::string, int> counts;
for (auto const& w : pool) ++counts[w];
for (std::string name : {"Silvia", "Maria", "Paolo"}) {
  auto found{counts.find(name)};
  if (found == counts.end())
    std::cout << name << " non trovato\n";
  else if (found->second == 1)
    std::cout << name << " compare una volta\n";
  else
    std::cout << name << " compare " << (*found).second << " volte\n";
}
```

Con il vettore di prima l'output è `Silvia compare una volta`, `Maria compare 3 volte`, `Paolo non trovato`. L'esempio delle slide è analogo: legge le parole dall'input standard con `while (std::cin >> word) counts[word] += 1;` e poi cerca la parola `"the"`, distinguendo i tre casi (assente, una volta, più volte). Il tipo restituito da `find` sarebbe `std::map<std::string, int>::iterator`: anche qui `auto` fa risparmiare un po' di scrittura. Il docente invita ad abituarsi a questi template, perché la libreria standard fa risparmiare un sacco di tempo: probabilmente tutti gli algoritmi del secondo semestre sono già disponibili, «a gratis o quasi».

L'iteratore si usa **come un puntatore**. Per accedere all'oggetto puntato si scrive `*found`; per accedere ai campi della coppia puntata si usa l'operatore freccia, `found->second`, equivalente a `(*found).second`. È esattamente ciò che si scriverebbe se `found` fosse un puntatore a una `struct` con i campi `first` e `second`. In realtà l'iteratore non è un puntatore ma un oggetto, per il quale sono stati ridefiniti gli operatori `*` e `->`. Nel pattern Iterator visto nella teoria c'era il metodo `current()`; in un linguaggio come Java, che non permette di ridefinire gli operatori, l'iteratore somiglia molto di più allo schema astratto. Il concetto resta valido: ci vuole, dice il docente, un po' di elasticità.

### `std::unordered_map`

`std::map` richiede chiavi ordinabili. Se le chiavi non hanno un ordine, o se l'ordine non interessa, si può usare **`std::unordered_map`**, dichiarata in `<unordered_map>`. È il caso degli identificatori di un programma: sono stringhe, e le stringhe un ordine ce l'hanno, ma non serve a niente; interessa solo sapere se una variabile è stata dichiarata e quale valore le è stato attribuito.

`std::unordered_map` ha la **stessa interfaccia** di `std::map`: sostituendo il nome del tipo, il codice di prima funziona invariato. Può essere ancora più efficiente: per una ricerca ci si aspetta, nel caso medio, un tempo **costante** [@cppref-unorderedmap]. Il conteggio delle frequenze di $n$ parole richiederebbe allora un tempo lineare, invece di $n \log n$. La differenza è che per `std::map` il costo logaritmico è **garantito**, mentre per `std::unordered_map` il tempo costante è un tempo **atteso**: in casi estremi può essere molto peggiore, fino a diventare lineare. Il perché si vedrà nel secondo semestre.

> [!tip] Approfondimento — Che cosa richiede una chiave di `std::unordered_map`
> #approfondimento
> Una `std::unordered_map` non tiene gli elementi in ordine, ma li distribuisce in **bucket** («secchi») in base al valore di una **funzione hash** calcolata sulla chiave; chiavi con lo stesso hash finiscono nello stesso bucket [@cppref-unorderedmap]. Per questo alla chiave non serve l'operatore `<`, ma servono una funzione hash (per default `std::hash<Key>`, definita per i tipi di base e per `std::string`) e il confronto di uguaglianza `==`. Una classe definita dall'utente, per essere usata come chiave, deve fornire entrambi. Il caso pessimo lineare si verifica quando molte chiavi finiscono nello stesso bucket. Il tipo è disponibile dal C++11 [@cppref-unorderedmap].

## Oggetti funzione

### Le funzioni come dati

Il docente ha detto in passato che, tranne che per l'esame di Sistemi operativi, dove si usa il C, si possono dimenticare le stringhe in stile C (`char*`) a favore di `std::string`. Lo stesso vale per un'altra particolarità del C: i **puntatori a funzione**. In C si può definire un puntatore a una funzione, e a quel punto succede una cosa importante: la funzione diventa un **dato**. Non la funzione stessa, ma il puntatore a essa. Si può, per esempio, costruire un array di puntatori a funzione e chiamare tutte le funzioni dell'array; se sono funzioni di un argomento e si ha un array di numeri, si possono applicare tutte le funzioni a tutti i numeri.

```c
#include <stdio.h>

static double twice(double x) { return 2 * x; }
static double square(double x) { return x * x; }

int main(void) {
  double (*ops[])(double) = {twice, square};   /* array di puntatori a funzione */
  double data[] = {1.0, 2.0, 3.0};
  for (int f = 0; f < 2; ++f) {
    for (int i = 0; i < 3; ++i) printf("%g ", ops[f](data[i]));
    printf("\n");
  }
  return 0;
}
```

Il programma stampa `2 4 6` e `1 4 9`. Quando una funzione diventa un dato si possono costruire strutture dati che incorporano funzionalità, da applicare poi a seconda dei casi. L'esempio del docente è un menu di un'interfaccia grafica: associando a ogni voce di menu un elemento di un array di funzioni, cliccando su una voce si chiama la funzione corrispondente, e si possono costruire interfacce in modo del tutto generale a seconda di ciò che si mette nell'array. È l'idea del pattern **Command**, citato nella [[Lezione 07 - Design pattern e classi come tipi#Visitor e gli altri pattern|lezione 7]] ma non approfondito. In Python passare una funzione a un'altra funzione è automatico: essendo tipizzato dinamicamente, Python non pone vincoli, e se poi tutto viene usato correttamente funziona «gratis».

> [!warning] Programmazione di ordine superiore
> Il docente, come le slide (*second-order programming*), chiama questa tecnica «programmazione di secondo ordine». Il termine più diffuso è programmazione con **funzioni di ordine superiore** (*higher-order functions*): funzioni che ricevono altre funzioni come argomenti o le restituiscono come risultato.

### `operator()`

In C++ si può fare lo stesso in modo più elegante, ridefinendo l'**operatore di chiamata** `operator()`. La ridefinizione può prendere tutti i parametri che si vogliono e restituire il tipo che si vuole; a quel punto un oggetto della classe si può **chiamare come una funzione**, e lo si può anche mettere in un vettore o passare come parametro, cioè trattare come un dato. Un oggetto di questo tipo si chiama **oggetto funzione** (*function object*). I puntatori a funzione, conclude il docente, vanno ricordati per Sistemi operativi, dove non c'è alternativa.

L'esempio riprende il generatore di identificativi della [[Lezione 07 - Design pattern e classi come tipi#Variabili automatiche e statiche|lezione 7]]. Là la funzione `generate_id` conservava il contatore in una variabile statica locale, che non sparisce all'uscita dalla funzione: il codice funzionava, ma era «brutto», non rientrante, una variabile globale mascherata. Questa è la versione «bella»: una **classe** con due membri statici, un prefisso e il valore massimo del contatore, che come si è visto hanno senso a livello di classe, e un contatore come attributo dell'oggetto. Ogni volta che si chiama l'oggetto come una funzione, si ottiene un nuovo identificativo univoco. Il docente mostra anche la separazione tra l'header e l'implementazione, e precisa che il dettaglio di come si calcola il valore non è importante.

```cpp
#include <iostream>
#include <string>
#include <vector>

// generate_id.h
class generate_id {
public:
  generate_id() : counter_{0} {}
  long operator()();                     // l'oggetto si chiama come una funzione
private:
  short counter_;                        // stato del singolo generatore
  static short prefix_;                  // dati condivisi dalla classe
  static short constexpr max_counter_{32767};
};

// generate_id.cpp
short generate_id::prefix_{1};

long generate_id::operator()() {
  if (counter_ == max_counter_)
    counter_ = 0;
  else
    ++counter_;
  return static_cast<long>(prefix_) * (max_counter_ + 1) + counter_;
}

struct movie {
  long id;
  std::string title;
  int runtime;
};

// Factory method che riceve il generatore per riferimento non costante:
// chiamarlo ne modifica lo stato interno
movie* make_movie(generate_id& gen) {
  std::string title{};
  int runtime{};
  std::cout << "Movie title: ";
  if (not std::getline(std::cin >> std::ws, title))
    return nullptr;
  std::cout << "Runtime (minutes): ";
  if (not (std::cin >> runtime))
    return nullptr;
  return new movie{gen(), title, runtime};   // "chiamata" dell'oggetto
}

int main() {
  generate_id gen{};
  std::vector<movie*> movie_pool{};
  movie* m{make_movie(gen)};
  while (m != nullptr) {
    movie_pool.push_back(m);
    m = make_movie(gen);
  }
  std::cout << '\n';
  for (movie* p : movie_pool) {
    std::cout << p->id << ' ' << p->title << " (" << p->runtime << " min)\n";
    delete p;
  }
}
```

Con l'input `Primo`, `120`, `Secondo film`, `95` seguito dalla fine dell'input, l'output finale è `32769 Primo (120 min)` e `32770 Secondo film (95 min)`: il prefisso 1 moltiplicato per 32768, più il contatore. La classe `generate_id` è quella delle slide; la struttura `movie`, che le slide non mostrano, è ridotta ai tre campi usati da `make_movie`.

> [!warning] Errori nel codice delle slide
> Il codice delle slide su `generate_id` e `make_movie` va corretto in alcuni punti per compilare e funzionare.
> - Manca il punto e virgola dopo la chiusura della classe `generate_id`.
> - In `make_movie` le variabili `title` e `runtime` non sono dichiarate; qui sono variabili locali. Inoltre `std::getline` letto subito dopo un `std::cin >> runtime` troverebbe il carattere di a capo rimasto nel buffer e leggerebbe una riga vuota: per questo si scrive `std::getline(std::cin >> std::ws, title)`, che salta prima gli spazi bianchi.
> - Nel `main` si dichiara `movie m = make_movie(gen);`, ma `make_movie` restituisce un `movie*`: la variabile deve essere un puntatore.
> - Il ciclo `while (m != nullptr) { movie_pool.push_back(m); }` non aggiorna mai `m`, quindi non termina: dentro il ciclo va chiamato di nuovo `make_movie`.
> - Gli oggetti creati con `new` vanno distrutti; qui lo fa il ciclo finale con `delete`.
>
> C'è poi un'osservazione sul generatore stesso: quando il contatore raggiunge `max_counter_` riparte da 0, ma il prefisso, nel codice delle slide, non cambia mai. Dopo 32768 chiamate, quindi, gli identificativi si ripetono: per garantire l'unicità bisognerebbe incrementare il prefisso a ogni giro del contatore (`++prefix_` insieme a `counter_ = 0`). Per lo stesso motivo due oggetti `generate_id` distinti, che condividono il prefisso statico ma hanno ciascuno il proprio contatore, producono gli stessi identificativi: nel programma va usato un solo generatore, come fa il `main`.

Il factory method `make_movie` riceve il generatore `gen` **per riferimento**, quindi il passaggio costa poco. Il riferimento non può però essere costante, perché chiamare il generatore ne aggiorna il contatore interno. Dentro `make_movie` il generatore si chiama esattamente come una funzione, `gen()`. Il film non ha la responsabilità di generare il proprio identificativo, ma ogni nuovo film ne riceve uno univoco: è la programmazione di ordine superiore all'opera, con una funzione passata come dato.

Il docente chiede poi se gli studenti conoscano la forma di conversione di tipo usata nel codice, `static_cast<long>(prefix_)`, o solo quella con le parentesi, `(long) prefix_`. Tranne che per Sistemi operativi, dice, ci si può dimenticare la conversione con le parentesi e usare questa, che è **più sicura**.

> [!tip] Approfondimento — Perché `static_cast` è più sicuro
> #approfondimento
> `static_cast` converte tra tipi usando conversioni implicite e conversioni definite dall'utente [@cppref-staticcast]. La conversione «alla C» `(T) e`, invece, prova in ordine una serie di conversioni del C++: prima `const_cast`, poi `static_cast` (con alcune estensioni, per esempio verso una classe base inaccessibile), poi `static_cast` seguito da `const_cast`, poi `reinterpret_cast`, infine `reinterpret_cast` seguito da `const_cast`, e sceglie la prima applicabile [@cppref-explicitcast]. Può quindi eliminare un `const` o reinterpretare i bit di un puntatore senza che il programmatore lo abbia chiesto esplicitamente. Con `static_cast` l'intenzione è dichiarata, e il compilatore rifiuta le conversioni pericolose.

> [!tip] Approfondimento — `std::function`
> #approfondimento
> Un vettore di oggetti funzione deve contenere oggetti dello stesso tipo. Per memorizzare insieme funzioni, puntatori a funzione e oggetti funzione di tipi diversi, purché con la stessa firma, la libreria standard offre il template `std::function`, dichiarato in `<functional>` [@cppref-function]: per esempio `std::vector<std::function<double(double)>>` è l'equivalente C++ dell'array di puntatori a funzione dell'esempio in C.

Il docente conclude raccomandando di usare gli oggetti funzione ogni volta che serve trattare le funzioni come dati.

## Le eccezioni

### Perché servono

L'ultimo argomento, importante anche per il progetto, sono le **eccezioni**. Servono a costruire codice più pulito. Chi cerca di individuare tutte le situazioni in cui l'utente può far fallire il programma impazzisce prima, e 99 volte su 100 non ci riesce. La soluzione al problema degli errori non è «blindare» il codice. Non bisogna nemmeno scrivere dei colabrodi, ma, sapendo che non si può prevedere tutto, si lascia che il problema si manifesti e poi lo si **gestisce**, evitando che il programma «esploda».

È esattamente il caso dell'interprete del progetto. L'utente può scrivere un programma sbagliato, in una quantità di modi che non si possono nemmeno immaginare. Ma se l'utente scrive un programma sbagliato, l'interprete non deve andare in crash: deve segnalare l'errore, come fa il compilatore usato finora.

### `at` e l'operatore `[]`

Il primo esempio è un vettore con due soli elementi, 10 e 20, a cui si tenta di accedere in posizione 5, che ovviamente non esiste.

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>

int main() {
  std::vector<int> data{10, 20};
  try {
    std::cout << data.at(5) << '\n';     // controllo dell'indice: lancia un'eccezione
  } catch (std::out_of_range const& ex) {
    std::cout << "errore gestito: " << ex.what() << '\n';
  }
  // std::cout << data[5] << '\n';        // nessun controllo: comportamento indefinito
}
```

Nelle slide i due casi sono due programmi distinti, che scrivono in posizione 5 con `data.at(5) = 0;` e con `data[5] = 0;` e chiedono che cosa succede. Entrambi gli accessi sono errori. Con il metodo **`at`**, il programma genera un'eccezione, che si può gestire; se non la si gestisce, il programma termina con un messaggio di errore. È quella che il docente chiama una **degradazione controllata** (*graceful degradation*): l'errore c'è, ma si manifesta subito e in modo chiaro, non come un comportamento strano che magari emerge molto dopo. Con l'operatore **`[]`**, invece, non c'è alcun controllo, e il comportamento è **indefinito** [@cppref-vector-subscript]: il programma può stampare un valore qualsiasi, andare in crash, o sembrare funzionare. Perché allora esiste `[]`? Perché è il C++: l'operatore è un po' più efficiente, dato che `at` deve controllare l'indice e usa il meccanismo delle eccezioni. Con g++ l'esempio stampa `errore gestito: vector::_M_range_check: __n (which is 5) >= this->size() (which is 2)`; il testo del messaggio dipende dall'implementazione della libreria [@cppref-vector-at].

### `try`, `throw` e `catch`

Gli ingredienti sono tre parole chiave.

- Il blocco **`try`** («prova») contiene il codice che può fallire.
- L'istruzione **`throw`** («lancia») genera un'eccezione.
- I **gestori** (*handler*) che seguono il blocco `try` iniziano con **`catch`** («afferra») e catturano le eccezioni.

L'eccezione, quindi, viene lanciata e poi afferrata; il docente ci vede la metafora del baseball, sport caro agli americani, anche se Stroustrup, il creatore del C++, americano non è. Di norma dentro il `try` non c'è un `throw` diretto, ma la chiamata di una funzione, che in caso di errore lancia l'eccezione. L'errore non viene gestito lì dove avviene: si lascia che avvenga, il programma non va in crash, viene generata un'eccezione che si cattura nel gestore. Lì si può dare un messaggio all'utente, tentare di recuperare l'errore se è recuperabile, oppure uscire, ma senza crash. Nell'interprete, se l'analisi sintattica si blocca perché il programma dell'utente è sbagliato, si lancia un'eccezione, il programma principale la cattura e segnala l'errore.

Le regole principali sono queste.

1. Ogni gestore tratta una specifica eccezione. Quando si verifica un'eccezione si esce dal blocco `try` e si cerca il gestore adatto.
2. Nella maggior parte dei casi il gestore dichiara il parametro come **riferimento costante**, per efficienza e perché di solito l'oggetto eccezione va solo consultato.
3. Un gestore si applica se il suo tipo è **lo stesso** dell'eccezione, oppure se è una sua **classe base**: un gestore per una classe base intercetta anche tutte le classi derivate [@cppref-catch].
4. I gestori vengono provati **nell'ordine** in cui sono scritti, e vince il primo che si applica. I tipi più specifici vanno quindi messi prima: se si mette prima la classe base, intercetta tutto e i gestori successivi non vengono mai eseguiti [@cppref-catch].
5. Quando si entra in un gestore, tutti gli oggetti automatici creati nel blocco `try` sono già stati distrutti. Il meccanismo, detto **srotolamento della pila** (*stack unwinding*), chiama i distruttori degli oggetti automatici costruiti dall'ingresso nel `try`, in ordine inverso rispetto alla costruzione [@cppref-throw].
6. Il gestore **`catch (...)`**, con tre puntini, cattura **qualsiasi** eccezione. Deve essere l'ultimo, e non permette di accedere all'oggetto eccezione: l'unica cosa che si può fare è stampare un messaggio di errore ed eventualmente uscire [@cppref-catch].

Un'eccezione è un **oggetto**, e può quindi trasportare informazioni dal punto in cui avviene l'errore al punto in cui viene gestito. Se, leggendo un file, si trova un errore a una certa riga e a una certa colonna, si inseriscono questi dati nell'eccezione; dove la si gestisce, si sa che cosa è andato storto e dove.

Tutte le eccezioni della libreria standard derivano da **`std::exception`**, dichiarata in `<exception>` [@cppref-exception]. Mettendo un gestore per `std::exception`, tutti i gestori successivi diventano inutili, perché è il tipo più generale; se lo si usa, va messo in fondo, oppure lo si usa per gestire tutte le eccezioni in un colpo solo. La funzione membro virtuale **`what()`**, definita in `std::exception`, restituisce una stringa che descrive l'eccezione; il contenuto esatto dipende dall'implementazione. Tutte le eccezioni standard ricevono nel costruttore una stringa, che poi viene restituita da `what()`.

> [!important] Le principali eccezioni standard
> | Classe | Derivata da | Header | Significato |
> |---|---|---|---|
> | `std::exception` | — | `<exception>` | base di tutte le eccezioni della libreria standard |
> | `std::logic_error` | `std::exception` | `<stdexcept>` | errori nella logica del programma, in teoria evitabili |
> | `std::out_of_range` | `std::logic_error` | `<stdexcept>` | accesso fuori dall'intervallo valido (per esempio `at`) |
> | `std::length_error` | `std::logic_error` | `<stdexcept>` | superamento della dimensione massima consentita |
> | `std::invalid_argument` | `std::logic_error` | `<stdexcept>` | argomento non valido (per esempio `std::stoi("abc")`) |
> | `std::runtime_error` | `std::exception` | `<stdexcept>` | errori rilevabili solo durante l'esecuzione |
> | `std::bad_alloc` | `std::exception` | `<new>` | allocazione di memoria fallita |
>
> Le derivazioni da `std::logic_error` sono quelle indicate dalla documentazione [@cppref-logicerror].

Il docente dice che le eccezioni della libreria sono «predefinite nell'header exception». Più precisamente, `<exception>` dichiara la classe base, mentre le classi derivate più comuni stanno in `<stdexcept>`, come riportato nella tabella.

Le slide spiegano la differenza tra i due rami principali della gerarchia. Gli **errori di runtime** (`std::runtime_error`) nascono da condizioni che si possono prevedere ma non impedire: un file che non esiste, un input malformato. Gli **errori logici** (`std::logic_error`) nascono da condizioni che il codice avrebbe potuto evitare, come un indice fuori dall'intervallo. Le eccezioni standard si possono usare così come sono oppure personalizzare, e secondo le slide personalizzarle è la scelta migliore.

### Un esempio con le stringhe

Il docente mostra un esempio, artificiale ma istruttivo, di codice che manipola una stringa e può generare fino a quattro eccezioni in quattro punti diversi.

```cpp
#include <exception>
#include <iostream>
#include <stdexcept>
#include <string>

int main() {
  std::string line;
  while (std::getline(std::cin, line)) {
    try {
      line.at(10) = ' ';                         // out_of_range se la riga è corta
      if (line.size() < 20)
        line.append(line.max_size(), '*');       // length_error: supera max_size()
      for (std::string::size_type size{line.size()}; size < line.max_size(); size = size * 2)
        line.resize(size);                       // length_error o bad_alloc
      line.resize(line.max_size());              // length_error o bad_alloc
      std::cout << "okay\n";
    } catch (std::out_of_range const& ex) {
      std::cout << "out_of_range: " << ex.what() << '\n';
    } catch (std::length_error const& ex) {
      std::cout << "length_error: " << ex.what() << '\n';
    } catch (std::exception const& ex) {
      std::cout << "eccezione: " << ex.what() << '\n';
    } catch (...) {
      std::cout << "eccezione sconosciuta\n";
    }
  }
}
```

Il programma legge righe dall'input standard. Se una riga ha meno di 11 caratteri, l'accesso alla posizione 10 lancia `std::out_of_range`. Se ha meno di 20 caratteri, il tentativo di aggiungerle in coda tanti asterischi quanta è la dimensione massima possibile di una stringa (`max_size()`) lancia `std::length_error`. Il ciclo successivo raddoppia ripetutamente la dimensione della stringa, e prima o poi può esaurire la memoria. Il punto, osserva il docente, è che non serve controllare prima ogni condizione (per esempio con un `if` sulla lunghezza della riga): si scrive il codice e si gestiscono gli eventuali problemi in un secondo momento. Prevenire ogni errore appesantirebbe molto il codice e la sua lettura.

I gestori sono ordinati dal più specifico al più generale: prima `std::out_of_range` e `std::length_error`, poi `std::exception`, infine il gestore universale. Quest'ultimo, in questo esempio, non dovrebbe mai essere raggiunto, perché tutte le eccezioni della libreria standard derivano da `std::exception`. Nelle slide il codice legge una sola riga, i gestori stampano anche una spiegazione (per esempio la dimensione massima della stringa superata) e il gestore universale termina il programma con `std::abort()`; qui è adattato per elaborare più righe in una sola esecuzione. Con g++ e le tre righe `corta`, `quindici caratt` (15 caratteri) e una riga di 38 caratteri, l'output è:

```text
out_of_range: basic_string::at: __n (which is 10) >= this->size() (which is 5)
length_error: basic_string::_M_replace_aux
eccezione: std::bad_alloc
```

Per la riga lunga il ciclo di raddoppio esaurisce la memoria disponibile e la libreria lancia `std::bad_alloc`, catturata dal gestore per `std::exception`. L'eccezione esatta che si ottiene in quel punto dipende dalla memoria del sistema.

### Lanciare e rilanciare

Quando una funzione incontra un errore che non sa recuperare, esegue un `throw` con un oggetto eccezione, di solito costruito con una stringa descrittiva. Un gestore può anche gestire parzialmente l'eccezione e poi **rilanciarla** con l'istruzione `throw;` senza argomenti, così da costruire gestori a più livelli. L'esempio del docente: si tenta di aprire un file, non ci si riesce, si chiede all'utente un nuovo nome, l'utente sbaglia di nuovo; a quel punto si rilancia l'eccezione, e «se la smazzerà» qualcuno a un livello superiore. Il `throw;` rilancia lo stesso oggetto eccezione, senza crearne uno nuovo [@cppref-throw]; l'esempio più sotto, sui numeri razionali, lo mostra all'opera.

### Gli stream

Gli stream di input e output, per default, **non lanciano eccezioni**. Per sapere se qualcosa è andato storto si controllano i loro bit di stato: per esempio il **badbit** viene impostato quando lo stream non si può più leggere o scrivere, il **failbit** quando un'operazione fallisce, come la lettura di un intero da un testo che non lo contiene. Si può però impostare una **maschera delle eccezioni** con il metodo `exceptions`: da quel momento gli stati di errore indicati nella maschera generano un'eccezione di tipo `std::ios_base::failure` [@cppref-iosexceptions].

L'esempio delle slide imposta la maschera sul solo badbit di `std::cin` e `std::cout`, e legge interi finché può.

```cpp
#include <exception>
#include <iostream>

int main() {
  std::cin.exceptions(std::ios_base::badbit);     // maschere delle eccezioni
  std::cout.exceptions(std::ios_base::badbit);
  int x{};
  try {
    while (std::cin >> x) std::cout << x << '\n';
    if (not std::cin.eof())   // il ciclo è finito senza raggiungere la fine: input non valido
      std::cerr << "Invalid integer input. Program terminated.\n";
  } catch (std::ios_base::failure const& ex) {
    std::cerr << "Major I/O failure! Program terminated.\n" << ex.what() << '\n';
    std::terminate();
  }
}
```

Il programma distingue due situazioni. Un input non valido, per esempio `1 2 x`, non è un guasto dello stream: imposta solo il failbit, che non è nella maschera, quindi non genera eccezioni; il ciclo termina, e poiché non si è arrivati alla fine dell'input (`eof()` è falso) il programma stampa `1`, `2` e il messaggio di input non valido. Un guasto vero dello stream, invece, imposta il badbit e genera un'eccezione `std::ios_base::failure`, gestita stampando un messaggio e terminando con `std::terminate()`.

Se si vuole che anche un input malformato generi un'eccezione, basta aggiungere il failbit alla maschera, come in questa variante su uno stream di stringa.

```cpp
#include <iostream>
#include <sstream>

int main() {
  std::istringstream in{"12 abc"};
  in.exceptions(std::ios_base::failbit | std::ios_base::badbit);
  int a{}, b{};
  try {
    in >> a;
    std::cout << "letto " << a << '\n';     // letto 12
    in >> b;                                 // fallisce: "abc" non è un intero
    std::cout << "letto " << b << '\n';
  } catch (std::ios_base::failure const& ex) {
    std::cout << "errore di lettura\n";
  }
}
```

L'output è `letto 12` seguito da `errore di lettura`. Con il failbit nella maschera, però, anche il normale raggiungimento della fine dell'input durante una lettura imposta il failbit e genera un'eccezione: per questo l'esempio delle slide si limita al badbit.

### Eccezioni personalizzate

Poiché le eccezioni sono oggetti, se ne possono definire di proprie, **derivando** dalle classi della libreria standard. L'esempio, tratto dal libro, è la classe dei numeri razionali. Al suo interno è definita una classe annidata `zero_denominator`, che deriva da `std::logic_error`. Il costruttore del razionale, se il denominatore è zero, lancia un'eccezione di questo tipo con il messaggio `The denominator was set to zero`.

```cpp
#include <iostream>
#include <numeric>
#include <stdexcept>

class rational {
public:
  class zero_denominator : public std::logic_error {   // eccezione annidata
  public:
    using std::logic_error::logic_error;               // eredita i costruttori
  };

  rational(int num, int den) : numerator_{num}, denominator_{den} {
    if (denominator_ == 0)
      throw zero_denominator{"The denominator was set to zero"};
    reduce();
  }
  int numerator() const { return numerator_; }
  int denominator() const { return denominator_; }
private:
  void reduce() {
    if (denominator_ < 0) { denominator_ = -denominator_; numerator_ = -numerator_; }
    int g{std::gcd(numerator_, denominator_)};
    numerator_ /= g;
    denominator_ /= g;
  }
  int numerator_;
  int denominator_;
};

rational read_and_build(int num, int den) {
  try {
    return rational{num, den};
  } catch (rational::zero_denominator const& ex) {
    std::cout << "livello interno: " << ex.what() << ", rilancio\n";
    throw;                                   // rilancia la stessa eccezione
  }
}

int main() {
  try {
    rational r{read_and_build(6, 4)};
    std::cout << r.numerator() << '/' << r.denominator() << '\n';
    rational s{read_and_build(1, 0)};
    std::cout << "non stampato\n";
  } catch (std::logic_error const& ex) {     // cattura anche le classi derivate
    std::cout << "livello esterno: " << ex.what() << '\n';
  }
}
```

L'output è:

```text
3/2
livello interno: The denominator was set to zero, rilancio
livello esterno: The denominator was set to zero
```

> [!warning] La classe `zero_denominator` delle slide
> Nelle slide la classe è dichiarata come `class zero_denominator : public std::logic_error { }`, senza corpo. Così non compila: i costruttori non si ereditano automaticamente, e `std::logic_error` non ha un costruttore di default, quindi `zero_denominator{"The denominator was set to zero"}` non trova un costruttore adatto (g++ segnala `no matching function for call to 'rational::zero_denominator::zero_denominator(...)'`). Le soluzioni sono due: dichiarare un costruttore che inoltra la stringa alla classe base, `zero_denominator(std::string const& what) : std::logic_error{what} {}`, oppure ereditare i costruttori della base con `using std::logic_error::logic_error;`, come nel codice sopra [@cppref-using-decl]. Nelle stesse slide mancano il punto e virgola dopo le due classi e c'è un refuso nell'inizializzazione, `denominator{den}` invece di `denominator_{den}`. Il gestore delle slide stampa semplicemente `zero denominator in rational number` su `std::cerr`.

Il codice che usa i razionali costruisce il numero e, se il denominatore è zero, cattura l'eccezione. Poiché la classe è annidata, il gestore deve nominarla con il nome qualificato `rational::zero_denominator`, altrimenti non funziona. L'esempio mostra anche il rilancio e la cattura tramite la classe base: il gestore esterno per `std::logic_error` intercetta l'eccezione derivata.

Dichiarare l'eccezione **dentro** la classe ha un vantaggio: se un'altra classe avesse anch'essa un'eccezione chiamata `zero_denominator`, non ci sarebbero conflitti di nomi. È una scelta sensata quando i membri di una classe possono generare errori: le eccezioni della classe restano contenute nella classe. E poiché un'eccezione è un oggetto, la si può arricchire a piacere, con dati e metodi.

## Esercizio: un tokenizer per un sottoinsieme del C

Il pacchetto si chiude con un esercizio che, come il precedente, è propedeutico al progetto finale: ne realizza, dice il docente, sostanzialmente il primo terzo. Come anticipato nella [[Lezione 02 - Architettura di un interprete e linguaggi formali|lezione 2]], l'**analisi lessicale** separa le parti significative di un programma dagli spazi bianchi e trasforma il sorgente in una sequenza di **token**. Tecnicamente un token è una **coppia** (*tag*, *parola*): il tag è l'etichetta attaccata al token, la parola è la stringa letta in corrispondenza del token.

Il linguaggio da riconoscere, secondo il testo dell'esercizio nelle slide, è un sottoinsieme del C:

1. le uniche parole chiave sono `int`, `float` e `return`;
2. gli unici separatori sono le parentesi graffe `{` `}`, le parentesi tonde `(` `)`, il punto e virgola e la virgola;
3. gli unici operatori sono `=`, `+`, `-`, `*`, `/`;
4. con questi elementi un programma può contenere dichiarazioni e definizioni di funzioni (compresa la funzione `main`), dichiarazioni e definizioni di variabili, assegnamenti, costanti numeriche ed espressioni aritmetiche.

> [!warning] Trascrizione e slide
> Nella trascrizione le parole chiave risultano «load e return», e il docente cita tra gli operatori «l'uguaglianza». Le slide chiariscono che le parole chiave sono `int`, `float` e `return`, che anche le parentesi graffe sono separatori e che l'operatore in questione è `=`.

Il risultato atteso è una sequenza di token: `int` riceve il tag di parola chiave, `f` quello di identificatore (perché non è una parola chiave), la parentesi aperta il tag `LP` (*left parenthesis*), e così via. Le slide usano i tag `KWORD` (parola chiave), `ID` (identificatore), `LP` e `RP` (parentesi tonde), `LB` e `RB` (parentesi graffe, *braces*), `SC` (punto e virgola, *semicolon*), `OP` (operatore aritmetico), `ISEQ` (il simbolo `=` dell'assegnamento) e `CONST` (costante numerica). L'esempio delle slide è il programma seguente.

```c
int f(int x) {
  return x * x;
}

int main() {
  int y = 10;
  int z;
  z = f(y) + 20;
}
```

La sua tokenizzazione, riga per riga, è:

```text
(KWORD, "int")(ID, "f")(LP, "(")(KWORD, "int")(ID, "x")(RP, ")")(LB, "{")
(KWORD, "return")(ID, "x")(OP, "*")(ID, "x")(SC, ";")
(RB, "}")
(KWORD, "int")(ID, "main")(LP, "(")(RP, ")")(LB, "{")
(KWORD, "int")(ID, "y")(ISEQ, "=")(CONST, "10")(SC, ";")
(KWORD, "int")(ID, "z")(SC, ";")
(ID, "z")(ISEQ, "=")(ID, "f")(LP, "(")(ID, "y")(RP, ")")(OP, "+")(CONST, "20")(SC, ";")
(RB, "}")
```

> [!warning] Un errore nell'esempio delle slide
> Per l'ultima istruzione, `z = f(y) + 20;`, le slide riportano i token `(OP, "*")(CONST, "10")`, che non corrispondono al sorgente: i token corretti sono `(OP, "+")(CONST, "20")`, come sopra e come produce la soluzione più sotto. Le slide, inoltre, non indicano il tag della virgola, che nell'esempio non compare; qui si usa `COMMA`. Infine, il simbolo `=` è elencato tra gli operatori ma riceve un tag proprio, `ISEQ`, distinto da `OP`: è il modo in cui l'analisi sintattica potrà distinguere l'assegnamento dalle operazioni aritmetiche.

Questa sequenza è ciò che servirà poi all'analisi sintattica, su cui il docente tornerà. Il progetto finale potrà riguardare un altro linguaggio, ma la tecnica sarà esattamente la stessa. Le indicazioni, dalla trascrizione e dalle slide, sono:

1. definire una classe `Token` per rappresentare i token;
2. realizzare il tokenizer come **oggetto funzione**, così da ripassare anche quell'argomento;
3. leggere il file **carattere per carattere**, cercando di identificare i token;
4. quando si incontra qualcosa che non è un token, cioè un simbolo non previsto, **lanciare un'eccezione**, definendo una propria classe di eccezioni: il programma non deve andare in crash;
5. restituire il risultato come un **vettore di token**, `std::vector<Token>`, da stampare per controllare il lavoro;
6. provare a scrivere e tokenizzare qualche programma;
7. come possibile miglioramento, fare in modo che l'eccezione riporti la **riga e la colonna** in cui si trova l'errore.

Il docente pubblicherà la sua soluzione, e invita a provarci prima da soli.

> [!example]- Una soluzione possibile (da provare prima da soli)
> La soluzione ufficiale potrebbe differire. Questa versione segue le indicazioni delle slide: una struttura `Token` con il tag e la parola, un oggetto funzione `Tokenizer` e un'eccezione `LexicalError`, derivata da `std::runtime_error`, che riporta riga e colonna del simbolo inatteso. Le costanti numeriche possono avere una parte decimale, dato che il linguaggio prevede il tipo `float`. È stata compilata con g++ in modalità C++20.
>
> ```cpp
> #include <cctype>
> #include <iostream>
> #include <sstream>
> #include <stdexcept>
> #include <string>
> #include <vector>
>
> struct Token {                                   // la coppia (tag, parola)
>   std::string tag;
>   std::string word;
> };
>
> class LexicalError : public std::runtime_error { // eccezione personalizzata
> public:
>   LexicalError(char c, int line, int column)
>       : std::runtime_error{"simbolo inatteso '" + std::string(1, c) + "' alla riga " +
>                            std::to_string(line) + ", colonna " + std::to_string(column)},
>         line_{line}, column_{column} {}
>   int line() const { return line_; }
>   int column() const { return column_; }
> private:
>   int line_, column_;
> };
>
> class Tokenizer {                                // oggetto funzione
> public:
>   std::vector<Token> operator()(std::istream& in) {
>     std::vector<Token> tokens;
>     int line{1}, column{0};
>     char c;
>     while (in.get(c)) {
>       ++column;
>       if (c == '\n') { ++line; column = 0; continue; }
>       if (std::isspace(static_cast<unsigned char>(c))) continue;
>       if (std::isalpha(static_cast<unsigned char>(c)) or c == '_') {
>         std::string word{c};                     // parola chiave o identificatore
>         while (std::isalnum(static_cast<unsigned char>(in.peek())) or in.peek() == '_') {
>           word += static_cast<char>(in.get());
>           ++column;
>         }
>         bool keyword{word == "int" or word == "float" or word == "return"};
>         tokens.push_back({keyword ? "KWORD" : "ID", word});
>       } else if (std::isdigit(static_cast<unsigned char>(c))) {
>         std::string word{c};                     // costante intera o con parte decimale
>         bool point{false};
>         while (std::isdigit(static_cast<unsigned char>(in.peek())) or (in.peek() == '.' and not point)) {
>           if (in.peek() == '.') point = true;
>           word += static_cast<char>(in.get());
>           ++column;
>         }
>         tokens.push_back({"CONST", word});
>       } else {
>         switch (c) {
>           case '(': tokens.push_back({"LP", "("}); break;
>           case ')': tokens.push_back({"RP", ")"}); break;
>           case '{': tokens.push_back({"LB", "{"}); break;
>           case '}': tokens.push_back({"RB", "}"}); break;
>           case ';': tokens.push_back({"SC", ";"}); break;
>           case ',': tokens.push_back({"COMMA", ","}); break;
>           case '=': tokens.push_back({"ISEQ", "="}); break;
>           case '+': case '-': case '*': case '/':
>             tokens.push_back({"OP", std::string(1, c)}); break;
>           default: throw LexicalError{c, line, column};
>         }
>       }
>     }
>     return tokens;
>   }
> };
>
> void run(std::string const& source) {
>   std::istringstream in{source};
>   Tokenizer tokenize;
>   try {
>     for (auto const& t : tokenize(in)) std::cout << '(' << t.tag << ", \"" << t.word << "\")";
>     std::cout << '\n';
>   } catch (LexicalError const& ex) {
>     std::cout << "errore lessicale: " << ex.what() << '\n';
>   }
> }
>
> int main() {
>   run("int f(int x) {\n  return x * x;\n}\nint main() {\n  int y = 10;\n  int z;\n  z = f(y) + 20;\n}\n");
>   run("float g(float a, float b) {\n  return a / 2.5 - b;\n}\n");
>   run("int main() {\n  int y = 10 # 2;\n}\n");
> }
> ```
>
> Per il programma delle slide l'output coincide con la sequenza riportata sopra (stampata su un'unica riga). Per il secondo programma si ottiene `(KWORD, "float")(ID, "g")(LP, "(")(KWORD, "float")(ID, "a")(COMMA, ",")(KWORD, "float")(ID, "b")(RP, ")")(LB, "{")(KWORD, "return")(ID, "a")(OP, "/")(CONST, "2.5")(OP, "-")(ID, "b")(SC, ";")(RB, "}")`. Nel terzo il tokenizer incontra il simbolo `#`, che non appartiene al linguaggio, e l'output è `errore lessicale: simbolo inatteso '#' alla riga 2, colonna 14`.
>
> Il riconoscimento di identificatori e numeri segue la logica di un automa a stati finiti: dal primo carattere si decide quale tipo di token si sta leggendo, e si continua a consumare caratteri finché restano nella classe ammessa. È il legame tra analisi lessicale e linguaggi regolari discusso nella [[Lezione 08 - Dalle espressioni regolari agli automi e ritorno#Specifica e algoritmo|lezione 8]].

## In sintesi

La soluzione dell'esercizio sui lavori mostra il cuore della programmazione orientata agli oggetti: una classe base astratta fissa il contratto (`print` e `parse` virtuali puri), un factory method crea l'oggetto giusto dall'etichetta della riga, e ogni oggetto sa leggersi e stamparsi; aggiungere un tipo richiede di cambiare una sola riga, quella del factory method. Un vettore si scorre con il ciclo su intervallo, con un indice o con gli iteratori, che sono il pattern Iterator della libreria standard.

`std::map` associa valori a chiavi ordinate con l'operatore `<`, con operazioni di costo logaritmico; l'operatore `[]` inserisce le chiavi mancanti con valore di default, `find` restituisce un iteratore o `end()`, e l'iterazione produce coppie `std::pair` con i campi pubblici `first` e `second`. `std::unordered_map` ha la stessa interfaccia, non richiede l'ordine, e ha costo atteso costante ma non garantito. Gli oggetti funzione ridefiniscono `operator()` e permettono di trattare le funzioni come dati, in modo più elegante dei puntatori a funzione del C; `static_cast` è la forma sicura di conversione. Le eccezioni separano la rilevazione dell'errore dalla sua gestione: `throw` lancia un oggetto, i gestori `catch` vengono provati in ordine e catturano anche le classi derivate, `catch (...)` cattura tutto, `throw;` rilancia. Le eccezioni standard derivano da `std::exception`, e se ne possono derivare di proprie. Gli errori di runtime sono prevedibili ma non evitabili, quelli logici evitabili nel codice; gli stream lanciano eccezioni solo per gli stati indicati nella loro maschera. L'esercizio sul tokenizer mette insieme oggetti funzione ed eccezioni per realizzare l'analisi lessicale di un sottoinsieme del C con le parole chiave `int`, `float` e `return`, trasformando il sorgente in una sequenza di coppie (tag, parola) come `(KWORD, "int")` o `(ID, "f")`.
