$$
% The identity itself
\frac{1}{2} + \sum_{k=1}^{n} \cos(ky) = \frac{\sin\bigl((n + \frac{1}{2})y\bigr)}{2\sin(\frac{1}{2}y)}\\\\\\

% 3-line telescoping proof
\begin{aligned}
2\sin\Bigl(\frac{y}{2}\Bigr) \left(\frac{1}{2} + \sum_{k=1}^{n} \cos(ky)\right) 
&= \sin\Bigl(\frac{y}{2}\Bigr) + \sum_{k=1}^{n} 2\cos(ky)\sin\Bigl(\frac{y}{2}\Bigr) \\
&= \sin\Bigl(\frac{y}{2}\Bigr) + \sum_{k=1}^{n} \biggl[\sin\Bigl(\Bigl(k+\frac{1}{2}\Bigr)y\Bigr) - \sin\Bigl(\Bigl(k-\frac{1}{2}\Bigr)y\Bigr)\biggr] \\
&= \sin\Bigl(\Bigl(n+\frac{1}{2}\Bigr)y\Bigr)
\end{aligned}$$