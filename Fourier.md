# Teorema (Fourier)
$\text{Sia }f:\R\to\R\ 2\pi\text{-periodica e di classe }C^1\text{ a tratti su tutti i periodi.}\\\text{Allora la serie di Fourier }\frac12 a_0+\suml_{k=1}^{+\infty}\bigl(a_k\cos(kx)+b_k\sin(kx\bigr)\text{ dove }\array{a_k=\frac1\pi\int_{-\pi}^\pi f(t)\cos(kt)dt&a_0=\frac1\pi\int_{-\pi}^\pi f(t)dt\\b_k=\frac1\pi\int_{-\pi}^\pi f(t)\sin(kt)dt&\bigl(k\in\mathcal{Z}_{>0}\bigr)}\text{,converge per ogni }x\in\R\text{ a }\frac12\bigl(f(x_+)+f(x_-)\bigr)\text{, ovvero alle medie tra i limiti monotoni }f(x_\pm)\coloneqq\lim\limits_{y\to x^\pm}f(y)\text{ in }x\text.$
## Osservazione
$\text{Se }f\text{ è continua in }x\text{, allora la serie di Fourier converge proprio a }f(x)\text.\\\text{Se invece }f\text{ ha un salto in }x\text{, la serie converge al punto medio del salto.}$

(Un onda quadra ha valore $0.5$ nel cambio di polarità, altrimenti $0/1$)

## Dimostrazione
Obiettivo: Mostrare che la successione delle somme parziali $s_n(x)=\frac12a_o+\suml_{k=1}^{a_k}\bigl(\cos(kx)+b_k\sin(kx)\bigr)$