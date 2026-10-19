
$\text{git clone} \rightarrow \text{git pull}$
$^\omega_bR$
$\{\text{a}\} = (O_a, ^ai_a, ^aj_a, ^ak_a)$
$\text{a }x\text{ b} \mskip{25mu} \left|| \text{ a }x\text{ b } \right|| = \left|\left|a\right|\right|\cdot\left|\left|b\right|\right|sin\theta$
$^a_bR = \left[^ai_b, ^aj_b, ^ak_b\right]$
$^av = ^a_bR^bv$
$\text{SO(3)} = \left\{R\in \mathbb{R}^{3x3} : R^TR = I, det(R)=1\right\}$

$R_x : i \rightarrow \pmatrix{1 \\ 0 \\ 0} \mskip{15mu} , \mskip{15mu} j \rightarrow \pmatrix{0 \\ cos\phi \\ sin\phi} \mskip{15mu} , \mskip{15mu} k \rightarrow\pmatrix{0 \\ -sin\phi \\ cos\phi}$

$R_x = \pmatrix{1 \ &0 \ &0 \\ 0 \ &cos\phi \ &-sin\phi \\ 0 \ &sin\phi \ &cos\phi} \mskip{15mu} ; \mskip{15mu} R_y = \pmatrix{cos\theta \ &0 \ &0 \\ 0 \ &1 \ &0 \\ -sin\theta \ &0 \ &cos\theta} \mskip{15mu} ; \mskip{15mu} R_z = \pmatrix{cos\psi \ &-sin\psi \ &0 \\ sin\psi \ &cos\psi \ &0 \\ 0 \ &0 \ &1}$

 $R(0)= I \mskip{15mu},R(\alpha)^{-1}=R(-\alpha) = R(\alpha)^T$
 $\{b\} \text{prima della rotazione } ^\omega v=^\omega_bR^bv$
 $\{b'\} \text{dopo una rotazione } ^bv = ^{b'}v'$
 
 
 $\underline{Assi \ fissi \ \{w\}} \mskip{15mu} ^\omega Q \mskip{10mu} \{b\} \rightarrow \{b'\}$
 $^\omega v' = ^\omega Q ^\omega v = ^\omega Q(^\omega_bR^bv) \rightarrow ^\omega_{b'}R = ^\omega Q^\omega_bR$
 ---
 $\underline{Assi \ mobili \ \{b\}} \mskip{15mu} ^b Q \mskip{10mu} \{b\} \rightarrow \{b'\}$
 $^\omega v' = ^\omega R ^\omega v = ^\omega_bR(^bQ^bv) \rightarrow ^\omega_{b'}R = ^\omega_bR^\omega_bQ$


$^a_bT = \pmatrix{ ^a_bR \ &^aO_b \\ \varnothing_{1x3} \ &1} \mskip{15mu} , \mskip{15mu} \overline{P}=\pmatrix{x_{p,a} \\ y_{p,a} \\ z{p,a} \\ 1}$

$\text{SE(3)} = \left\{ ^a_bT:^a_bR\in SO(3),^aO_b\in \mathbb{R}^3 \right\}$

$^a_cT = ^a_bT^b_cT = \pmatrix{^a_bR^b_cR \ &^aO_b+^a_bT^bO_c \\ 0_{3x1} \ &1}$

$^b_a T = \,^a_b T^{-1} = \pmatrix{ ^a_b R^T & -\,^a_b R^T \,^a O_b \cr 0 & 1 }$

---

$\underline{ESEMPIO } \text{ :Posa 3D sensore}$
$\omega_bR = R_z(\frac{\pi}{2}) , \mskip{15mu} ^\omega O_b = \pmatrix{1 \\ 2 \\ 0}$

$^b_sR = R_x(\frac{\pi}{2}), \mskip{15mu} ^bO_s = \pmatrix{0.2 \\ 0 \\ 0.5}$
$^sP = \pmatrix{0 \\ 1 \\ 0}$

$^\omega_b T = \pmatrix{ 0 \ &-1 \ &0 \ &1 \\ 1 \ &0 \ &0 \ &2 \\ 0 \ &0 \ &1 \ &0 \\ 0 \ &0 \ &0 \ &1}$

$^b_s T = \pmatrix{ 1 \ &0 \ &0 \ &0.2 \\ 0 \ &0 \ &-1 \ &0 \\ 0 \ &1 \ &0 \ &0.5 \\ 0 \ &0 \ &0 \ &1}$

$^\omega_sT = ^\omega_bT^b_sT = \pmatrix{ 0 \ &0 \ &1 \ &1 \\ 1 \ &0 \ &0 \ &2.2 \\ 0 \ &1 \ &0 \ &0.5 \\ 0 \ &0 \ &0 \ &1}$


$^\omega\overline{P} = ^\omega_sT^s\overline{P} = \pmatrix{ 0 \ &0 \ &1 \ &1 \\ 1 \ &0 \ &0 \ &2.2 \\ 0 \ &1 \ &0 \ &0.5 \\ 0 \ &0 \ &0 \ &1}\pmatrix{0\\ 1 \\ 0 \\ 1} = \pmatrix{1 \\ 2.2 \\ 1.5 \\ 1}$
