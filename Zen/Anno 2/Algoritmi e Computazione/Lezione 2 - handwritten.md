
```c

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

# Interprete:
### 1. ANALISI LESSICALE (LEXER):

##### ha una struttura a lista (o tante boxes sequenziali)

va ad analizzare il codice pezzo per pezzo
	int f(int x) {
dove:
	int --> tipo
	f --> ID
	( --> lp
	int --> tipo
	x --> ID
	) --> rp 
	{ --> lb
con:
	lp = left Parentesis
	rp = right Parentess
	lb = left brace
	rb = right brace
	kw = keyword

Quindi passiamo da un file di testo '.c' --> LEXER --> int, tipo  (che nella sua interezza è detto token, ma è diviso in lessema, in questo caso "int" e tag (etichetta) che in questo caso è tipo)

è il LEXER che:
- Elimina "spazio bianco": spazi, indentazioni, ritorno a capo
- Identifica i token e li mette in linea, o in una lista
### 2. ANALISI SINTATICA (PARSER):

#### ha una struttura ad albero

avendo una lista di *token*
(\*) lista di token
**Nello specifico questa è una lista di token per le prime 4 righe:

	(int, tipo) (f, id) (int, tipo) (x, id) (rp) (lb) 
	(int, tipo) (y, id) (eq) (x, id) (times) (x, id) (col)
	(return, kw) (y, id) (col) 
	(rb)

Trovare (se esiste) la corrispondenza tra lista di token e ***struttura*** sintattica

	<funzione>   := <tipo> <id> lp <param> rp
	<blocco>     := lb <istruzioni> rb
	<istruzioni> := tab <istruzione> <istruzionbi>
	<istruzione> := tab ...

### 3. ANALISI SEMANTICA (EVALUATION):

#### L'evaluator visita l'albero sintattico associando ad ogni nodo la semantica definita per la sintassi del nodo

Passaggio alle slide argomenti preliminari 

