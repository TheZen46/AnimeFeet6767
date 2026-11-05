# Analisi Matematica 1A · notazione comune

Notazione proposta per tutti i moduli. Dove gli appunti usano due forme per la stessa cosa, la tabella indica quale si tiene.

## Insiemi e logica

| Oggetto | Notazione | Note |
|---|---|---|
| Naturali | $\mathbb{N} = \{0, 1, 2, \dots\}$, $\mathbb{N}_0 = \mathbb{N} \setminus \{0\}$ | Come negli appunti (L02). Da dire una volta nel modulo 1, perché alcuni testi escludono lo 0 |
| Intervalli | $[a, b]$, $(a, b)$, $[a, b)$, $(a, b]$, $[a, +\infty)$ | Parentesi tonde per gli estremi esclusi (L02) |
| Intorni | $I_r(x_0)$, $I_a(+\infty)$, $I_b(-\infty)$ | Negli appunti $I_K(-\infty)$ è usato con estremo $-K$: si scrive $I_{-K}(-\infty)$ |
| "tale che" | ":" negli insiemi, "tale che" per esteso nel testo | Niente "t.c." |
| Implicazioni | $\Rightarrow$, $\iff$ | – |

## Funzioni

| Oggetto | Notazione | Note |
|---|---|---|
| Funzione | $f : X \to Y$, $x \mapsto f(x)$ | – |
| Dominio, immagine, grafico | $\operatorname{dom}(f)$, $\operatorname{im}(f)$, $\Gamma(f)$ | Negli appunti compare anche "dominio(f)": si usa $\operatorname{dom}$ |
| Controimmagine e inversa | $f^{-1}(B)$ per la controimmagine, $f^{-1}$ per l'inversa | Stessa scrittura per due oggetti diversi: va spiegato alla prima occorrenza (modulo 1) |
| Restrizione | $f|_A$ | – |
| Potenze | $x^\alpha$ | Negli appunti $(\cdot)^\alpha$ indica la funzione: si tiene solo nella definizione |
| Logaritmo naturale | $\ln x$ | Il formulario usa $\log$: si uniforma a $\ln$, con $\log_a$ per le altre basi |
| Esponenziale | $e^x$, $\exp$ solo quando serve la funzione come oggetto (inversa del logaritmo) | – |
| Trigonometriche | $\sin x$, $\cos x$, $\tan x$, $\cot x$, $\arcsin x$, $\arccos x$, $\arctan x$, $\operatorname{arccot} x$ | Parentesi solo con argomenti composti: $\sin(2x)$, $\sin x$ |

## Limiti e confronto

| Oggetto | Notazione | Note |
|---|---|---|
| Limite | $\lim_{x \to x_0} f(x) = l$; $\lim_{n \to +\infty} a_n$ | Si scrive sempre $+\infty$, non $\infty$, per le successioni |
| Limiti unilaterali | $x \to x_0^+$, $x \to x_0^-$ | – |
| Landau | $f = o(g)$, $f = O(g)$, $f \sim g$ per $x \to c$ | Indicare sempre "per $x \to c$" |
| Parte principale | $p(x) = l\,\varphi(x)^\alpha$ | – |

## Derivate e Taylor

| Oggetto | Notazione | Note |
|---|---|---|
| Rapporto incrementale | $R_{f,x_0}(x)$ | Come negli appunti |
| Derivata | $f'(x_0)$, $\frac{df}{dx}(x_0)$; derivate successive $f''$, $f^{(k)}$ | – |
| Derivata destra e sinistra | $f'_+(x_0)$, $f'_-(x_0)$ | – |
| Classi | $C^k(I)$, $C^\infty(I)$ | – |
| Polinomio di Taylor | $T_{n,x_0}f(x)$ | Gli appunti scrivono $Tf_{n,x_0}$ e $T\ln(1+x)_{n,0}$: propongo $T_{n,x_0}f$, che si legge meglio con funzioni lunghe (ad esempio $T_{n,0}[\ln(1+x)]$). Se preferisci la tua, la tengo |

## Teoremi e abbreviazioni

| Negli appunti | Nel testo finale |
|---|---|
| Th, Dim, Oss, Def, Prop, Cor | Callout `[!teorema]` e `[!definizione]` con il nome per esteso; "Dimostrazione", "Osservazione" |
| Th $\exists_0$ | "teorema di esistenza degli zeri" |
| B-W | "teorema di Bolzano-Weierstrass" |
| H sopra l'uguale | "per il teorema di de l'Hôpital" nel testo, oppure $\overset{H}{=}$ spiegato alla prima occorrenza |
| p.to, p.ti | "punto", "punti" |

## Incoerenze trovate

- $\ln$ e $\log$ per il logaritmo naturale (lezioni e formulario).
- $f^{-1}$ usato senza distinguere controimmagine e inversa.
- $Tf_{n,x_0}$ e $T\ln(1+x)_{n,x_0}$: per $\ln(1+x)$ negli appunti il pedice dice $x_0$, ma lo sviluppo è in 0.
- "monotona crescente (non decrescente)": si sceglie "crescente" per $\le$ e "strettamente crescente" per $<$, come negli appunti, dicendolo una volta.
