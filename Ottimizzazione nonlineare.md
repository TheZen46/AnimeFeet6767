# Problema
$\min\limits_{x\in\R^d}f(x)$
$f:\R^d\to\R$

## Obiettivo
Approssimare $\min\limits_{x\in\R^d}f(x)$ con degli algoritmi



Supponiamo $d=1$
$f:\R\to\R$
$f'(x)=0\rightarrow\text{soluzioni di questa equazione sono i candidati minimi}$

### Osservazione
$\min\limits_{x\in\R}f(x)\qquad\text{intendo minimo globale}$

$\text{Cioè }m\text{ tale che }m\le f(x)\quad \forall\ x\in\R\\\text{e }m=f(\overline x),\text{ con }\overline x\in\R$



# Algoritmi del primo ordine
Usano solo $f'(x)\bigl(\text{eventualmente }f(x)\bigr)$

## Algoritmo di discesa del gradiente
### Problema
$\min\limits_{x\in\R}f(x)\qquad f:\R\to\R$

### Supposizione
$f$ sia derivabile, con derivata prima continua: $f\in C^1(\R)$

### Teorema
Se $f\in C^1(\R)$ allora $\forall\ x\in\R\quad f(x+h)=f(x)+f'(x))h+o\bigl(|h|\bigr)\qquad\forall\ h\in\R$
.\underbrace{}_{}