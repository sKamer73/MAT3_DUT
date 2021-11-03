#!/usr/bin/env python
# coding: utf-8

# # Travaux Dirigés
#   
# ## Partie I - Premiers calculs
# 
# **Exercice 1**. Soit $A$ et $B$ deux matrices. Effectuer les produits
# matriciels $A$x$B$ et $B$x$A$, quand cela est possible.
# 
# 1.  $A=\begin{pmatrix}
#     1&-2&3\\
#     2&1&0\\
#     -1&2&5
#     \end{pmatrix}$ et $B=\begin{pmatrix}
#     1&0&0\\
#     0&2&0\\
#     0&0&3
#     \end{pmatrix}$
# 
# 2.  $A=\begin{pmatrix}
#     1&-2&3\\
#     2&1&0\\
#     -1&2&5
#     \end{pmatrix}$ et $B=\begin{pmatrix}
#     1&2&-1\\
#     -2&2&1\\
#     1&0&1
#     \end{pmatrix}$
# 
# 3.  $A=\begin{pmatrix}
#     1&-2&3\\
#     2&1&0\\
#     -1&2&5\\
#     \end{pmatrix}$ et $B=\begin{pmatrix}
#     2\\-1\\5
#     \end{pmatrix}$
# 
# **Exercice 2**. Soit $A=\begin{pmatrix}
# 3&9&-9\\
# 2&0&0\\
# 3&3&-3
# \end{pmatrix}$. Calculer $A^{3}$.
# 
# **Exercice 3**. Dans chaque cas, trouver une matrice $M$ et une
# multiplication (soit $A$x$M$ soit $M$x$A$) qui permette d’obtenir la
# matrice indiquée:
# 
# 1.  Décaler toutes les colonnes vers la droite:  
#     $A=\begin{pmatrix}
#     a&a'&a"\\
#     b&b'&b"\\
#     c&c'&c"
#     \end{pmatrix} \longrightarrow \begin{pmatrix}
#     0&a&a'\\
#     0&b&b'\\
#     0&c&c'
#     \end{pmatrix}$
# 
# 2.  Décaler toutes les colonnes vers la gauche:  
#     $A=\begin{pmatrix}
#     a&a'&a"\\
#     b&b'&b"\\
#     c&c'&c"
#     \end{pmatrix} \longrightarrow \begin{pmatrix}
#     a'&a"&0\\
#     b'&b"&0\\
#     c'&c"&0
#     \end{pmatrix}$
# 
# 3.  Décaler toutes les lignes vers le haut:  
#     $A=\begin{pmatrix}
#     a&a'&a"\\
#     b&b'&b"\\
#     c&c'&c"
#     \end{pmatrix} \longrightarrow \begin{pmatrix}
#     b&b'&b"\\
#     c&c'&c"\\
#     0&0&0
#     \end{pmatrix}$
# 
# 4.  Décaler toutes les lignes vers le bas:  
#     $A=\begin{pmatrix}
#     a&a'&a"\\
#     b&b'&b"\\
#     c&c'&c"
#     \end{pmatrix} \longrightarrow \begin{pmatrix}
#     0&0&0\\
#     a&a'&a"\\
#     b&b'&b"
#     \end{pmatrix}$
# 
# ## Partie 2 - Déterminant et inversion
# 
# 
# Nous allons dans cette partie réaliser différents calculs de
# déterminants et d’inverses de matrices, et nous étudierons la résolution
# de systèmes à l’aide de matrices.
# 
# **Exercice 1**. Calculer les déterminants des matrices suivantes et,
# lorsque cela est possible, calculer leur inverse. 
# 
# $$\begin{array}{lcl}
# A=\begin{pmatrix}
# -1&2\\
# 2&3\\
# \end{pmatrix}
# & \qquad \qquad
# &
# B=\begin{pmatrix}
# 2&1\\
# 3&-1
# \end{pmatrix}\\
# \\
# C=\begin{pmatrix}
# 1&-1&2\\
# -1&2&-3\\
# -1&1&-1
# \end{pmatrix}
# &
# &
# D=\begin{pmatrix}
# 3&-1&2\\
# 1&2&-3\\
# 4&1&-1\\
# \end{pmatrix}
# \\
# \end{array}$$ 
# 
# $$N=\begin{pmatrix}
# 1&0&0&1\\
# 0&1&0&0\\
# 1&0&1&1\\
# 2&3&1&1
# \end{pmatrix}$$
# 
# *Indication 1*. Calcul de déterminant  
# Chercher la technique de calcul la plus avantageuse parmi celles que
# vous connaissez, notamment pour les déterminants d’ordre 3: règle de
# Sarrus, développement par ligne ou par colonne, ou opérations sur les
# lignes ou les colonnes.
# 
# *Indication 2*. Calcul de d’inverse de matrice  
# De même il existe plusieurs façons de calculer l’inverse d’une matrice:
# grâce à la formule du cours (faisant intervenir la comatrice), mais
# aussi la technique dite du "Pivot de Gauss" qui sera étudiée un peu plus
# tard (exercice 5).  
# 
# **Exercice 2**. Soit $A$ une matrice de $M_{3}(\mathbb{R})$ définie par
# $A=\begin{pmatrix}
# 1&0&2\\
# 0&-1&1\\
# 1&-2&0
# \end{pmatrix}$.
# 
# 1.  Calculer $A^{3}-A$.
# 
# 2.  En déduire que $A$ est inversible puis déterminer son inverse
#     $A^{-1}$.
# 
# **Exercice 3**. On considère le système d’équations suivants
# 
# $$\left\lbrace
# \begin{array}{ll}
# 3x+2y =1\\
# x + 4y =2
# \end{array}\right.$$
# 
# 1.  Montrer que le système s’écrit sous la forme $A\begin{pmatrix}
#     x\\y
#     \end{pmatrix}=\begin{pmatrix}
#     1\\2
#     \end{pmatrix}$, et déterminer $A$.
# 
# 2.  La matrice $A$ est-elle inversible ? Si oui donner son inverse.
# 
# 3.  En déduire une solution au système précédent.
# 
# 4.  Reproduire la démarche avec le système suivant: 
# 
# $$\left\lbrace
#     \begin{array}{ll}
#     x-y =1\\
#     x + y + 3z =2\\
#     x-z=4
#     \end{array}\right.$$
# 
# Dans cet exercice le déterminant de la matrice associé est non nul, donc
# cette matrice est inversible et le système admet une unique solution: on
# appelle un tel système un "système de Cramer".  
# 
# **Exercice 4**. Nous avons vu précédemment comment résoudre un système
# dont le déterminant associé est non nul. Dans cet exercice nous allons
# étudier le cas où ce déterminant est nul.  
#   
# Soit le système à étudier dans $\mathbb{R}^{2}$: 
# 
# $$\left\lbrace
# \begin{array}{ll}
# 3x-7y =2\\
# -1,5x + 3,5y =-1
# \end{array}\right.$$
# 
# 1.  Ecrire le système sous forme matricielle et calculer le déterminant
#     de la matrice associée au système. Peut-on trouver une solution au
#     système grâce à la forme matricielle ?
# 
# 2.  Résoudre de façon "classique" le système.
# 
# 3.  Etudier maintenant le système proche suivant. Que peut-on en dire ?
#     Quelles sont ses solutions ?
#     
#     $$\left\lbrace
#     \begin{array}{ll}
#     3x-7y =2\\
#     -1,5x + 3,5y =0
#     \end{array}\right.$$
# 
# 4.  Conclure sur la résolution d’un système de deux équations à deux
#     inconnues dont le déterminant de la matrice associée est nul.
# 
# 5.  Que se passe-t-il en dimension 3 ? (C’est-à-dire avec un système de
#     trois équations à trois inconnues dont le déterminant associé est
#     nul.)  
#     Enumérer les cas de figure possibles: à quoi correspondent-ils
#     géométriquement ?
# 
# *Indication 3*. Des schémas de ces différents cas de figure sont
# disponibles sur Moodle.
# 
# **Exercice 5**. Pivot de Gauss Nous allons voir dans cet exercice une
# autre méthode pour résoudre un système ou inverser une matrice.
# Reprenons la matrice $A$ de l’exercice 1.
# 
# $$A=\begin{pmatrix}
# -1&2\\
# 2&3\\
# \end{pmatrix}$$
# 
# Nous savons d’après l’exercice 1 que cette matrice est inversible. Nous
# allons calculer son inverse grâce à la méthode dite du "Pivot de Gauss".
# 
# 1.  Ecrire côte à côte la matrice $A$ et la matrice identité $I_{2}$:  
# 
#     $$\left(
#      \begin{array}{cc|cc}
#     -1&2&1&0\\
#     2&3&0&1
#      \end{array}\right)$$
# 
#     Notre but est d’obtenir la matrice identité à gauche grâce à une
#     série d’opérations élémentaires sur les lignes. On aura alors à
#     droite la matrice inverse $A^{-1}$.
# 
#     $$\left(
#      \begin{array}{cc|cc}
#     -1&2&1&0\\
#     2&3&0&1
#      \end{array}\right)
#      \longrightarrow \left(
#      \begin{array}{cc|c}
#     1&0&\\
#     0&1&
#      \end{array} A^{-1}\right)$$
# 
#     Pour cela commencer par effectuer une opération sur la deuxième
#     ligne pour obtenir un $0$ en $a_{2,1}$.
# 
#     On obtient alors en faisant $L_{2}\leftarrow L_{2}+2.L_{1}$ :
# 
#     $$\left(
#      \begin{array}{cc|cc}
#     -1&2&1&0\\
#     2&3&0&1
#      \end{array}\right)
#      \Leftrightarrow \left(
#      \begin{array}{cc|cc}
#     -1&2&1&0\\
#     0&7&2&1
#      \end{array}\right)$$  
# 
# 2.  Réaliser sur le même modèle une opération sur la ligne 1 pour
#     obtenir $a_{1,2}=0$. On aura alors une matrice diagonale à gauche.
# 
# 3.  Terminer en réalisant une opération sur chaque ligne pour nous
#     ramener à la matrice identité.
# 
# 4.  Comparer le résultat obtenu avec celui obtenu dans l’exercice 1.
# 
# 5.  Reproduire la démarche avec les matrices $C$ et $N$ de l’exercice
#     1.  
# 
# *Indication 4*. Pour des exemples de la méthode du Pivot de Gauss, voir
# la video explicative disponible sur Moodle, issue du site Exo7.
# 
# ## Partie 3 - applications
# 
# 
# Dans ce dernier TD, nous allons étudier quelques applications du produit
# matriciel, de façon un peu plus visuelle.
# 
# **Exercice 1**. On se place dans un repère orthonormé
# $(\mathcal{O},\vec{i},\vec{j})$.
# 
# On étudiera le vecteur $\vec{u}_{1}= \begin{pmatrix}
# 3\\1
# \end{pmatrix}$. et $\vec{u}_{2}= \begin{pmatrix}
# 2\\2
# \end{pmatrix}$ On notera $U_{1}$ et $U_{2}$ les matrices colonnes
# contenant leurs coordonnées respectives dans la suite de l’énoncé. Soit
# $R(\theta)=\begin{pmatrix}
# cos(\theta)&-sin(\theta)\\
# sin(\theta)&cos(\theta)
# \end{pmatrix}$
# 
# 1.  $\theta=\frac{\pi}{2}$
# 
#     1.  Calculer $R(\frac{\pi}{2})$.
# 
#     2.  Calculer $V_{1}=R(\frac{\pi}{2}).U_{1}$ et
#         $V_{2}=R(\frac{\pi}{2}).U_{2}$.
# 
#     3.  Soit $\vec{v}_{1}$ le vecteur donc les coordonnées sont
#         représentées par la matrice colonne $V_{1}$ et $\vec{v}_{2}$ par
#         la matrice colonne $V_{2}$. Dessiner les vecteurs $\vec{u}_{1}$,
#         $\vec{u}_{2}$, $\vec{v}_{1}$ et $\vec{v}_{2}$ dans le repère
#         orthonormé $(\mathcal{O},\vec{i},\vec{j})$ en faisant partir
#         tous les vecteurs de l’origine du repère.
# 
# 2.  $\theta=\frac{\pi}{3}$
# 
#     1.  Calculer $R(\frac{\pi}{3})$.
# 
#     2.  Calculer $V'_{1}=R(\frac{\pi}{3}).U_{1}$ et
#         $V'_{2}=R(\frac{\pi}{3}).U_{2}$.
# 
#     3.  De la même façon dans un second repère aux mêmes dimensions
#         représenter $\vec{u}_{1}$, $\vec{u}_{2}$, $\vec{v}'_{1}$ et
#         $\vec{v}'_{2}$ en partant toujours de l’origine du repère.
# 
# 3.  Que remarque-t-on ?
# 
# 4.  Dans un troisième repère observer maintenant ce que devient le
#     vecteur $\vec{u}_{1}$ par les matrices $P_{x}=\begin{pmatrix}
#     1&0\\
#     0&0
#     \end{pmatrix}$ et $P_{y}=\begin{pmatrix}
#     0&0\\
#     0&1
#     \end{pmatrix}$
# 
# 5.  Même question dans un dernier repère avec
#     $M(\lambda)=\begin{pmatrix}
#     \lambda&0\\
#     0&\lambda
#     \end{pmatrix}$ et prenant plusieurs valeurs de $\lambda$.  
#     (On pourra par exemple prendre $\lambda=\frac{1}{2}$ et $\lambda=2$)
# 
# 6.  Que pouvez-vous en déduire sur l’utilité géométrique des matrices ?
# 
# *Indications 1*. On pourra aussi, pour les curieux, regarder l’effet des
# matrices $\begin{pmatrix}
# 1&0\\
# 0&-1
# \end{pmatrix}$, $\begin{pmatrix}
# -1&0\\
# 0&1
# \end{pmatrix}$, et $\begin{pmatrix}
# 1&0\\
# 0&\lambda
# \end{pmatrix}$

# In[2]:


from random import randint
randint(1,29)


# In[4]:


3.14159*(0.03**2)*45*1000/470


# In[ ]:




