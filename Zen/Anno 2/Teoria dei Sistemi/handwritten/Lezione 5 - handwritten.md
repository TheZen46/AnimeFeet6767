$F(s) = \frac{s^4}{(s+1)(s+2)(s^{2} +4)}$

impostare il sistema, in latex, senza risolverlo

$$
F(s) = \frac{s^4}{(s+1)(s+2)(s^2+4)} = K + \frac{A}{s+1} + \frac{B}{s+2} + \frac{2\cdot C + D\cdot s}{s^2+4}
$$

Moltiplicando per il denominatore $(s+1)(s+2)(s^2+4) = s^4 + 3s^3 + 6s^2 + 12s + 8$:

$$
s^4 = K\,(s^4 + 3s^3 + 6s^2 + 12s + 8) + A\,(s+2)(s^2+4) + B\,(s+1)(s^2+4) + (2\cdot C + D\cdot s)(s+1)(s+2)
$$

Sviluppando i prodotti:

$$
\begin{aligned}
A\,(s+2)(s^2+4) &= A\,(s^3 + 2s^2 + 4s + 8) \\
B\,(s+1)(s^2+4) &= B\,(s^3 + s^2 + 4s + 4) \\
(Cs + D)(s^2 + 3s + 2) &= C s^3 + (3C + D)\,s^2 + (2C + 3D)\,s + 2D
\end{aligned}
$$

Uguagliando i coefficienti delle potenze di $s$:

$$
\begin{cases}
s^4: & K = 1 \\
s^3: & 3K + A + B + C = 0 \\
s^2: & 6K + 2A + B + 3C + D = 0 \\
s^1: & 12K + 4A + 4B + 2C + 3D = 0 \\
s^0: & 8K + 8A + 4B + 2D = 0
\end{cases}
$$