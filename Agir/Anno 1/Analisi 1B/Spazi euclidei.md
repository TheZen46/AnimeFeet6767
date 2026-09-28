$\mathbb R^n=\{(x_1,\ldots,x_n)|x_1,\ldots,x_n\in\mathbb R\}$
$\mathbb R^2=\{(x,y)|x,y\in\mathbb R\}$
$\mathbb R^3=\{(x,y,z)|x,y,z\in\mathbb R\}$

$\mathbb R^n$ si può identificare in 2 modi:
- come spazio affine (ossia come insieme di punti)
- come spazio vettoriale (insieme di vettori)

Pensando $\mathbb R^n$ come spazio vettoriale possiamo definire le operazioni:
- Somma$\quad(x_1,\ldots,x_n)+(y_1,\ldots,y_n)=(x_1+y_1,\ldots,x_n+y_n)$
- Prodotto per uno scalare$\quad\alpha(x_1,\ldots,x_n)=(\alpha x_1,\ldots,\alpha x_n)\quad (\alpha\in\mathbb R)$

$\mathbb R^n$ con queste operazioni è uno spazio vettoriale. Una sua base è $\vec{e_1}=(1,0,\ldots,0),\ \vec{e_2}=(0,1,\ldots,0),\ldots,\ \vec{e_n}=(0,0,\ldots,1)$
$(x_1,\ldots,x_n)=x_1 e_1+\ldots+x_n e_n$

Altri due operazioni
- Norma$\quad\vec x=(x_1,\ldots,x_n)\Rightarrow ||\vec x||=\sqrt{{x_1}^2+\ldots+{x_n}^2}$
	È la distanza di $\vec x$ dall'origine $\vec O$ (equivalentemente, la lunghezza del vettore corrispondente)
	Segue che se $\vec P,\vec Q\in\mathbb R^n$, allora $||\vec P-\vec Q||$ è la distanza di $\vec P$ da $\vec Q$
	Abbiamo: $\begin{array}{l}||\vec x||=0&\iff&\vec x=\vec O\\||\vec x+\vec Y||&\le& ||\vec x||+||\vec y||&\forall\ \vec x,\vec y\in\mathbb R^n\\||\alpha\vec x&=& |\alpha|\cdot||\vec x||+||\vec y||&\forall\ \alpha\in\mathbb R,\ \forall\ \vec x\in\mathbb R^n\end{array}$

- Prodotto scalare$\quad(x_1,\ldots,x_n)\cdot(y_1,\ldots,y_n)=(x_1y_1,\ldots,x_ny_n)$

Abbiamo:
- $\vec x\cdot\vec x=||\vec x||^2$
- $\vec x\cdot \vec y=||\vec x||\cdot||\vec y||\cos(\theta)$, dove $\theta$ è l'angolo tra $\vec x$ e $\vec y\quad\displaystyle\left(\Rightarrow\theta=\arccos\left(\frac{\vec x\cdot \vec y}{||x||\cdot||y||}\right)\right)$

In particolare $|\vec x\cdot\vec y|\le||\vec x||\cdot||\vec y||$ (disuguaglianza di Cauchy-Schwarz)

