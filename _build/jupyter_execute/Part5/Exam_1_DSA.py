#!/usr/bin/env python
# coding: utf-8

# # Sujet Contrôle DSA 1

# **Exercice 1**.   **(5 Points)**
# 
# Soient $A=\begin{pmatrix}
# 1&1&0\\ 0&1&1\\ 0&0&1
# \end{pmatrix}$ et
# $B = \begin{pmatrix} 0&1&0 \\ 0&0&1 \\ 0&0&0 \end{pmatrix}$
# 
# 1.  Calculer $(2I_3+A)$, ($2I_3+A - ~^tB)\times B$ (avec $~^tB$ la
#     transposée de $B$), $B^2$ et $B^3$ .
# 
# 2.  Donner une relation entre $I_3$, A et B. En déduire que A et B
#     commutent (i.e., $AB=BA$).
# 
# 3.  Soit $n \in \mathbb{N}$. Calculer $B^n$ selon les valeurs de n. En
#     utilisant la formule de Newton et les éléments donnée à la fin de ce
#     document, donnez une expression pour $A^n$.
# 
# **Exercice 2**.   **(8 Points)**
# 
# Soient $\vec{n} =\begin{pmatrix} 1 \\ 2 \\3 \end{pmatrix}$ et
# $\vec{d} =\begin{pmatrix} 2 \\ 0 \\-2 \end{pmatrix}$.
# 
# Soient $A(2,0,-2)$, $B(2,3,-1)$ et $C(0,2,-1)$.
# 
# 1.  Calculer $\vec{n} \cdot \vec{d}$, $\vec{n} \wedge \vec{AC}$ et
#     $||\vec{AB}||$
# 
# 2.  Calculer l’équation cartésienne du plan $(P)$ passant par les
#     points A,B et C.
# 
# 3.  Calculer le système cartésien de la droite $\mathcal{D}$, de
#     vecteur directeur $\vec{d}$ et telle que B appartienne à cette
#     droite.
# 
# 4.  Ecrire le système permettant de trouver l’intersection de la droite
#     et du plan, puis l’écrire sous forme matricielle $AX = Y$
# 
# 5.  Soit $D(1,-2,5)$. On cherche un point $M(x,y,z)$ tel que la droite
#     $(DM)$ soit perpendiculaire à la droite $\mathcal{D}$
# 
#     1.  On suppose que $M \in \mathcal{D}$. Ecrire la condition de
#         perpendicularité entre $(DM)$ et $\mathcal{D}$.
# 
#     2.  On prend un point $M(x,y,z)$ sur la droite $\mathcal{D}$.
#         Ecrire les conditions d’appartenance de $M$ à $\mathcal{D}$,
#         puis écrire et résoudre le système associé à l’appartenance de
#         $M$ à $\mathcal{D}$ et la perpendicularité de $(DM)$ et
#         $\mathcal{D}$. Conclure.
# 
# **Exercice 3**.   **(7 Points)**
# 
# Soit $$A=\begin{pmatrix}
# 1&-2&6\\ 0&1&0\\ 1&0&1
# \end{pmatrix}$$
# 
# 1.  Montrer que $A$ est inversible.
# 
# 2.  Trouver $A^{-1}$.
# 
# 3.  Soit $\displaystyle{Y=\begin{pmatrix}-10\\ 3\\1 \end{pmatrix}}$.
#     Résoudre le système $AX=Y$, avec ou sans calculs, et en justifiant.
# 
# **BONUS**   **(2 Points)** Soient a et b deux réels non-nuls, on pose
# $A=\begin{pmatrix} a & b \\ 0&a \end{pmatrix}$. En posant une matrice
# $B=\begin{pmatrix} c &d \\ e&f \end{pmatrix}$, donner l’ensemble des
# matrices qui commutent avec $A$, c’est-à-dire telles que $AB=BA$.
# 
# **Formule de Newton** **Q.1.c.** Soient 2 matrices $M$ et $N$ qui
# commutent, alors:
# $(M+N)^n = \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix} M^k N^{n-k} = \begin{pmatrix} n \\ 0 \end{pmatrix}M^0N^n + \begin{pmatrix} n \\ 1 \end{pmatrix}M^1N^{n-1} + \begin{pmatrix} n \\ 2 \end{pmatrix}M^2N^{n-2} + \dots + \begin{pmatrix} n \\ n-1 \end{pmatrix}M^{n-1}N^{1} + \begin{pmatrix} n \\ n \end{pmatrix}M^{n}N^{0}$.
# On donne $\begin{pmatrix} n \\ 0 \end{pmatrix} = 1$,
# $\begin{pmatrix} n \\ 1 \end{pmatrix} = n$,
# $\begin{pmatrix} n \\ 2 \end{pmatrix} = \frac{n(n-1)}{2}$ et $B^0=I_3$.
# Pour information,
# $\begin{pmatrix} n \\ k \end{pmatrix} = \frac{n!}{k!(n-k)!}$, avec
# $k \leq n$ des entiers et
# $n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1$.
# 
# **EX1:=(0.5+1+0.5+0.5)+(0.5+0.5)+(0.75+0.75)    EX2:=2+2+1+1+1+1    EX3:=1.5+4+1.5**
