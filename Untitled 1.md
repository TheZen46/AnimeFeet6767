```tikz
\begin{tikzpicture}
  % x, y, z axes (z points up, x points out, y points right)
  \draw[->] (0,0,0) -- (2,0,0) node[below left] {$x$};
  \draw[->] (0,0,0) -- (0,2,0) node[right] {$y$};
  \draw[->] (0,0,0) -- (0,0,2) node[above] {$z$};
  \draw[thick, red, ->] (0,0,0) -- (1,1.5,1.5) node[above right] {$\vec{v}$};
\end{tikzpicture}
```
Iniettività
