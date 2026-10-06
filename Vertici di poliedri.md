$\text{Poliedro (in forma generale) }P=\{x|Ax\ge b\}\mskip{24mu} A\text{ matrice }m\times n,\ x\in\mathbb R^n,\ b\in\mathbb R^m$
# Definizione (vertice)
$\overline x\in P$ si dice **vertice** se non esistono $x_1,x_2\in P$ tali che $\overline x\in\text{ segmento }\bigl]x_1,x_2\bigr[$
$I(\overline x)=\bigl\{i\in\{1,\ldots,m\}\ |\ a_i^T\overline x=b_i\bigr\}$
## Teorema
$\overline x\in P$
Allora sono fatti equivalenti:
1) $\overline x$ è un vertice
2) $\operatorname{rank}(A_{I(\overline x)})=n$, dove $A_{I(\overline x)}$ è la matrice ottenuta considerando solo le right dei vincoli attivi
## Proposizione
Sia $P=\{x|Ax\ge b\}\ne\varnothing$
Allora sono equivalenti:
1) $P$ ha almeno un vertic
2) e
3) $P$ non contiene rette


Problema di programmazione lineare:
$\min C^Tx$
$Ax\ge b$

# Teorema fondamentale della programmazione lineare
Sia $P=\{x|Ax\ge b\}\ne\varnothing$ e non contenga rette
Allora, uno dei seguenti casi si verifica per il problema:
1) Il problema è illimitato inferiormente
2) Il problema ammette soluzione ottima, e una delle soluzioni è un vertice di $P$

### Esempio
$f(x)=x{^-1}$
Non ammette minimo ma è limitata dal basso
Questa situazione NON si verifica per i problemi di PL.

