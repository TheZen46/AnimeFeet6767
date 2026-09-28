```c++
int f(int x){
    int y = x*x;
    return y;
}

int main(){
    int z = f(5);
    printf("5^2=%d", z);
    return 0;
}
```

$\fbox{C++}\to\fbox{Compiler}\to\boxed{5\mskip{3mu} \text{\^{}}\mskip{3mu} 2=25}$

# Compiler
$\fbox{lexer}-\star\to\fbox{parser}-\boxed\star\to\fbox{eval}$
1) Analisi lessicale (**lexer**)
	Divide `int` (tipo), `f` (id), `(` (LP), `)` (RB), `{` (LB), `=` (eq), `*` (times), `;` (colon)
	Ogni token è composto da un **lessema** ed un **tag** \[int, tipo]
	Elimina il whitespace

Token list $\star$ per `f`
(int,tipo)(f,id)(lp)(int,tipo)(x,id)(rp)(lb)
(int,tipo)(y,id)(eq)(x,id)(times)(x,id)(colon)
(return,kw),(y,id)(colon)(rb)

2) Analisi sintattica (**parser**)
	Trova (se esiste) la corrispondenza tra la lista di token e **struttura sintattica** specificata da una grammatica
		\<funzione> = \<tipo>\<id>LP\<param>RP\<blocco>
		\<blocco> = LB\<istruzioni>RB
		\<istruzioni> = ␣ | \<istruzione>\<istruzioni>
		\<istruzione> = ...
	Genera un albero/grafo

Albero sintattico $\boxed\star$

3) Analisi semantica (**evaluator**)
	Genera un albero sintattico (albero con gerarchia delle istruzioni)
	L'evaluator **visita** l'albero sintattico associato ad ogni nodo la semantica definita per sintassi del nodo
