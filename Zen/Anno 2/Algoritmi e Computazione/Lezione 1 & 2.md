
```
---
lezione: 1 e 2
data: 2026-09-24
argomenti: [introduzione al corso, architettura di un interprete, analisi lessicale, analisi sintattica, analisi semantica, alfabeti, stringhe, linguaggi formali, word problem]
---
```

# Introduzione al Corso e Filosofia dell'Ingegneria del Software

Il corso si articola su due moduli principali spalmati su due semestri. Nel primo semestre vengono affrontati i fondamenti dell'informatica teorica (4 CFU) e la programmazione avanzata in C++ (2 CFU). Nel secondo semestre il focus si sposta sulla teoria della complessità (2 CFU) e sull'analisi di algoritmi e strutture dati (4 CFU).

  

Lo scopo ultimo della disciplina non è formare semplici programmatori, ma ingegneri informatici. Un programmatore sta all'ingegnere informatico come un muratore sta all'ingegnere civile: mentre il primo si occupa della stesura materiale del codice, il secondo deve possedere i fondamenti teorico-matematici per garantire la solidità, la correttezza e l'efficienza architetturale del sistema. L'ingegneria del software ha un impatto diretto e "cinetico" sul mondo reale: errori concettuali o di implementazione possono portare a guasti catastrofici. Esempi storici includono il disastro del razzo Ariane 5 nel 1996, causato da un'eccezione software dovuta alla conversione non protetta di un numero in virgola mobile a 64 bit in un intero a 16 bit, o i malfunzionamenti delle macchine per radioterapia Therac-25.

  

Attualmente, l'automazione della stesura del codice tramite Intelligenza Artificiale (come i Large Language Models) solleva ulteriormente la necessità di una profonda comprensione teorica: nessuna macchina, stante gli attuali modelli di computazione, può dimostrare algoritmicamente e in modo assoluto la correttezza formale del software che essa stessa genera. Lo studio dei limiti della computazione serve esattamente a definire i confini di ciò che è calcolabile, ciò che è intrattabile in tempi ragionevoli e ciò che richiede imperativamente la validazione ingegneristica umana.

  

# L'Architettura di un Interprete

L'approccio ingegneristico alla risoluzione di problemi complessi consiste nella scomposizione del problema in sottoproblemi più semplici. La progettazione di un interprete o di un compilatore (un campo di ricerca consolidato da oltre settant'anni) segue esattamente questo principio gerarchico.

  

Per comprendere il processo di interpretazione, consideriamo un semplice programma scritto in un sottoinsieme del linguaggio C++:

  


``` c++
int f(int x){
    int y = x * x;
    return y;
}

void main(){
    int z = f(5);
    printf("Il quadrato di 5 è %d", z);
    return ;
}
```

La trasformazione di questo testo sorgente in un output calcolabile attraversa tre fasi sequenziali e distinte: l'analisi lessicale, l'analisi sintattica e l'analisi semantica (o valutazione).

  



```
graph LR
    A[File Sorgente testuale] -->|Flusso di caratteri| B(Analisi Lessicale<br>Lexer)
    B -->|Lista lineare di Token| C(Analisi Sintattica<br>Parser)
    C -->|Albero Sintattico Astratto| D(Analisi Semantica<br>Evaluator)
    D -->|Esecuzione logica| E[Output]
```

## 1. Analisi Lessicale (Lexer)

La prima fase elabora il codice sorgente trattandolo come una pura sequenza di caratteri. Il modulo responsabile, chiamato _Lexer_ (Lexical Analyzer), ha due compiti fondamentali:

  

- **Rimozione del rumore:** Elimina lo "spazio bianco", ovvero gli spazi, le tabulazioni e i ritorni a capo, che sono utili alla leggibilità umana ma irrilevanti per la logica della macchina.
    
      
    
- **Tokenizzazione:** Raggruppa i caratteri in unità logiche indivisibili chiamate _token_.
    
      
    

Un _token_ è una struttura dati elementare composta tipicamente da due attributi:

  

1. Il **lessema**: la stringa di caratteri effettiva estratta dal codice (es. `int`, `f`, `(`).
    
      
    
2. Il **tag** (o etichetta): la categoria logica a cui il lessema appartiene.
    
      
    

Ad esempio, l'elaborazione della prima riga `int f(int x) {` produce la seguente sequenza logica:

  

- `(int, tipo)`
    
      
    
      
    
- `(f, id)` (dove `id` sta per identificatore)
    
      
    
- `(lp)` (left parenthesis - parentesi tonda aperta)
    
      
    
- `(int, tipo)`
    
      
    
      
    
- `(x, id)`
    
      
    
      
    
- `(rp)` (right parenthesis)
    
      
    
- `(lb)` (left brace - parentesi graffa aperta)
    
      
    

L'output del Lexer è una lista lineare e sequenziale (o un vettore) di token immagazzinata in memoria. Se il codice sorgente contiene stringhe che non appartengono al vocabolario del linguaggio, l'analisi lessicale fallisce, sollevando un errore.

  

## 2. Analisi Sintattica (Parser)

La lista lineare di token, pur essendo composta da "parole" corrette, non garantisce che la frase abbia un senso strutturale. Ad esempio, la sequenza di token derivata da `void x } ; int (` è lessicalmente valida ma non forma un costrutto C++ ammissibile.

  

L'Analisi Sintattica, delegata a un modulo chiamato _Parser_, ha il compito di verificare se la sequenza di token rispetta le regole grammaticali del linguaggio. Tali regole definiscono una struttura fortemente gerarchica:

  

- Un programma è composto da funzioni.
    
      
    
- Una funzione è definita da un'intestazione e da un blocco.
    
      
    
- Un blocco contiene una sequenza di istruzioni.
    
      
    

Formalmente, si stabilisce una grammatica, ad esempio:

  

- `<funzione> := <tipo> <id> lp <param> rp <blocco>`
    
      
    
      
    
- `<blocco> := lb <istruzioni> rb`
    
      
    
      
    

Se l'analisi ha successo, il Parser abbandona la struttura lineare della lista per costruire una struttura dati ramificata: l'**Albero Sintattico** (o Grafo Sintattico).

  

Snippet di codice

```
graph TD
    Prog[Programma] --> F[Funzione: f]
    Prog --> M[Funzione: main]
    F --> Param[Parametri: int x]
    F --> CorpoF[Corpo]
    CorpoF --> Ass1[Assegnamento]
    Ass1 --> Esp1[Espressione: x * x]
    CorpoF --> Ret1[Return: y]
    M --> ParamM[Parametri: vuoti]
    M --> CorpoM[Corpo]
    CorpoM --> Ass2[Assegnamento]
    Ass2 --> Esp2[Chiamata: f 5]
    CorpoM --> Pr[Print]
```

## 3. Analisi Semantica e Valutazione (Evaluator)

L'ultima fase è l'interpretazione del significato (semantica) e la conseguente esecuzione logica. Il modulo di valutazione (_Evaluator_) opera visitando (ovvero percorrendo sistematicamente) l'albero sintattico. Ad ogni nodo dell'albero viene associata l'azione semantica definita per quel particolare costrutto.

  

Durante questa traversata, l'Evaluator si avvale di una fondamentale struttura dati mantenuta in memoria, denominata **Symbol Table** (Tabella dei Simboli). Quando l'Evaluator visita la definizione della funzione `f`, non ne esegue immediatamente il corpo, ma registra nella Symbol Table il suo nome, i parametri richiesti (`int`) e il tipo di ritorno (`int`).

  

Successivamente, visitando la funzione `main`, incontra l'assegnamento alla variabile `z` tramite la chiamata `f(5)`. L'Evaluator interroga la Symbol Table per recuperare la definizione di `f`, assegna il valore `5` al parametro formale `x`, calcola il risultato del blocco (`5 * 5 = 25`), e infine salva il risultato per stamparlo.

  

> [!important] Definizione: Lexer, Parser ed Evaluator
> 
>   
> 
> - **Lexer:** converte i caratteri in unità logiche minimali (token). Lavora su strutture lineari.
>     
>       
>     
> - **Parser:** converte la lista di token in una gerarchia strutturale (albero sintattico) basata su regole grammaticali.
>     
>       
>     
> - **Evaluator:** esegue il codice percorrendo l'albero sintattico e gestendo lo stato in memoria tramite la Symbol Table.
>     
>       
>     

# Fondamenti Teorici: Alfabeti, Stringhe e Linguaggi

La tecnologia dei compilatori è supportata da una rigorosa modellizzazione matematica. Per capire come un Lexer discrimina un identificatore valido o come un Parser riconosce un costrutto lecito, si ricorre alla teoria dei linguaggi formali.

  

## Alfabeti e Stringhe

- **Alfabeto ($\Sigma$):** Un insieme finito e strettamente non vuoto di simboli.
    
      
    - Esempi: L'alfabeto binario $\Sigma = \{0, 1\}$; l'insieme di tutti i caratteri ASCII.
        
          
        
- **Stringa:** Una sequenza finita di simboli prelevati da un alfabeto $\Sigma$. Nonostante i simboli appartengano a un set finito, la costruzione della stringa implica un numero finito di occorrenze. Un codice sorgente C++ è, nella sua interezza, una singola, lunga stringa.
    
      
    
- **Stringa vuota ($\epsilon$):** La stringa definita con zero occorrenze di simboli.
    
      
    
- **Lunghezza ($\vert{}w\vert{}$):** Il numero di posizioni occupate dai simboli all'interno della stringa $w$. Ad esempio, per la stringa "0110", la lunghezza è $\vert{}0110\vert{} = 4$; per la stringa vuota è $\vert{}\epsilon\vert{} = 0$.
    
      
    

## Potenze di un Alfabeto e Chiusure

Per descrivere insiemi di stringhe, l'informatica teorica introduce l'operatore di potenza:

  

- $\Sigma^k$ denota l'insieme (finito) di tutte le stringhe di esatta lunghezza $k$ componibili con i simboli di $\Sigma$.
    
      
    
- Esempio: Se $\Sigma = \{0, 1\}$, allora $\Sigma^2 = \{00, 01, 10, 11\}$. La cardinalità in questo caso è $\vert{}\Sigma^2\vert{} = 4$.
    
      
    
- Per convenzione fondamentale, $\Sigma^0 = \{\epsilon\}$.
    
      
    

Da questo deriviamo due insiemi infiniti cruciali:

  

- La **Chiusura di Kleene (Stella di Kleene):** $\Sigma^*$ è l'insieme (infinito) di _tutte_ le possibili stringhe generabili sull'alfabeto $\Sigma$, inclusa la stringa vuota. $\Sigma^* = \bigcup_{k=0}^{\infty} \Sigma^k$.
    
      
    
- **Chiusura Positiva:** $\Sigma^+$ è l'insieme di tutte le stringhe generabili escludendo (salvo che non vi rientri in altre forme) la componente nulla isolata. $\Sigma^+ = \bigcup_{k=1}^{\infty} \Sigma^k$. Ne deriva che $\Sigma^* = \Sigma^+ \cup \{\epsilon\}$.
    
      
    

> [!warning] Sezione ricostruita — inizio
> 
> (Chiarimento matematico sulla differenza tra chiusura positiva e stella di Kleene).
> 
> La relazione $\Sigma^* = \Sigma^+ \cup \{\epsilon\}$ è una delle uguaglianze più fondamentali dell'informatica teorica. Si noti che $\Sigma^+$ non esclude a priori l'utilizzo di un simbolo di stringa vuota _se_ questo facesse parte dell'alfabeto originale, ma la definizione rigorosa impone che l'alfabeto contenga "simboli", mentre $\epsilon$ rappresenta l'assenza di simboli. Dunque $\Sigma^+$ garantisce la presenza di almeno un simbolo formale nella stringa.
> 
> [!warning] Sezione ricostruita — fine
> 
>   

## I Linguaggi Formali

Un **Linguaggio** $L$, dato un alfabeto $\Sigma$, è un qualsiasi sottoinsieme dell'insieme di tutte le stringhe possibili: $L \subseteq \Sigma^*$. Un linguaggio può essere un set infinito di elementi nonostante l'alfabeto da cui attinge sia strettamente finito. I programmi C++ sintatticamente corretti sono infiniti, ma scaturiscono da un insieme finito di caratteri ASCII e da un set ristretto di regole.

  

Esempi notevoli di linguaggi:

  

- $L_p = \{10, 11, 101, \dots\}$, ovvero l'insieme dei numeri binari il cui valore decimale associato è un numero primo.
    
      
    
- L'insieme di stringhe costituite da un numero uguale di zero e di uno.
    
      
    
- $L_\emptyset = \emptyset$: il linguaggio vuoto (non contiene alcuna stringa).
    
      
    
- $L_\epsilon = \{\epsilon\}$: il linguaggio che contiene esclusivamente la stringa vuota.
    
      
    
- _Nota Bene:_ Il linguaggio vuoto è strutturalmente diverso dal linguaggio contenente la stringa vuota ($L_\emptyset \neq L_\epsilon$).
    
      
    

### Operazioni sui Linguaggi e Leggi Algebriche

Sui linguaggi è possibile applicare operatori insiemistici e specifici dell'informatica teorica:

  

1. **Unione:** $L \cup M = \{w \mid w \in L \lor w \in M\}$. L'unione è commutativa e associativa.
    
      
    
2. **Concatenazione:** $L \cdot M = \{w \mid w = xy, x \in L, y \in M\}$. Date le stringhe $x$ e $y$, la concatenazione $xy$ giustappone una copia di $y$ immediatamente dopo $x$.
    
      
    - La concatenazione è associativa, ma **non** commutativa ($L \cdot M \neq M \cdot L$).
        
          
        
    - È distributiva a destra e a sinistra rispetto all'unione.
        
          
        
    - L'identità (elemento neutro) della concatenazione è il linguaggio $L_\epsilon = \{\epsilon\}$.
        
          
        
    - L'elemento assorbente della concatenazione è il linguaggio vuoto $\emptyset$ ($L \cdot \emptyset = \emptyset \cdot L = \emptyset$).
        
          
        
3. **Potenza di un linguaggio:** $L^0 = \{\epsilon\}$, $L^1 = L$, e ricorsivamente $L^{k+1} = L \cdot L^k$.
    
      
    
4. **Chiusura di Kleene su linguaggi:** $L^* = \bigcup_{i=0}^{\infty} L^i$. La chiusura è un operatore idempotente, per cui $(L^*)^* = L^*$.
    
      
    - Applicando la chiusura all'insieme vuoto o all'insieme della stringa vuota si ottiene lo stesso risultato: $\emptyset^* = \{\epsilon\}$ e $\{\epsilon\}^* = \{\epsilon\}$.
        
          
        

> [!tip] Approfondimento: Elemento assorbente della concatenazione
> 
> Perché $L \cdot \emptyset = \emptyset$? #approfondimento
> 
> Per definizione formale di concatenazione, una stringa $w$ appartiene a $L \cdot M$ se e solo se esiste una porzione $x \in L$ e una porzione $y \in M$ tali che $w = xy$. Se $M = \emptyset$, non esiste alcun $y$ prelevabile da $M$. Poiché la proposizione richiede la congiunzione logica (AND) di entrambe le esistenze, l'intera proposizione risulta falsa. Di conseguenza, non si può formare alcuna stringa valida, risultando nell'insieme vuoto. L'approccio deduttivo alla teoria degli insiemi è alla base di queste dimostrazioni (Sipser, _Introduction to the Theory of Computation_).
> 
>   

# Il Problema della Parola (Word Problem)

La definizione dei linguaggi introduce il problema centrale dell'informatica teorica: il **Problema della Parola** (Word Problem).

  

**Definizione:** Dato un alfabeto $\Sigma$ e un linguaggio formalmente descritto $L \subseteq \Sigma^*$, verificare se una stringa data $w \in \Sigma^*$ è un elemento appartenente a $L$.

  

Decidere se una stringa appartiene o meno a un linguaggio equivale a processare computazionalmente il problema soggiacente. Se il linguaggio $L_p$ è l'insieme delle stringhe binarie indicanti numeri primi, decidere se la stringa $w \in L_p$ è l'esatto equivalente logico e computazionale di testare se il numero codificato in $w$ è primo. Analogamente per decidere se un numero è pari nel linguaggio delle stringhe binarie a valore pari ($L_e$).

  

La correlazione con le fasi del compilatore studiate precedentemente è diretta e assoluta:

  

- Verificare se una sequenza di caratteri ASCII compone un nome di variabile ammissibile in C++ (linguaggio $L_{id}$) è la soluzione di un Word Problem eseguita dal Lexer.
    
      
    
- Verificare se una sequenza di token costituisce un programma gerarchicamente conforme alle regole sintattiche del C++ è la soluzione di un Word Problem eseguita dal Parser (dove in questo caso l'alfabeto di partenza è costituito dall'insieme dei token e non dai singoli caratteri).
    
      
    
- Verificare che una variabile sia stata precedentemente dichiarata prima di essere usata è un'ulteriore iterazione del Word Problem processata nell'Analisi Semantica.
    
      
    

Ogni fase risolve la sua istanza del Word Problem facendo affidamento su specifici modelli di automi computazionali (es. Automi a Stati Finiti per l'analisi lessicale, sistemi computazionali più complessi come la Macchina di Turing per l'analisi semantica) a seconda della potenza espressiva richiesta dal linguaggio che modella il problema. L'intera impalcatura concettuale dell'Informatica risiede nella composizione di questi modelli per risolvere i problemi di appartenenza associati.