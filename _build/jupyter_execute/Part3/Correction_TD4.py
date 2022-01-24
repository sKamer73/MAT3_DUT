#!/usr/bin/env python
# coding: utf-8

# # Correction du TD4

# **Exercice 1**. (\* à \*\*\*) En utilisant les définitions du cours,
# montrer que :
# 
# 1.  si $X \sim \mathcal{B}(p)$ alors $\mathbb{E}[X] = p$ et
#     ${\rm Var}[X]=p(1-p)$
# 
# 2.  si $X \sim \mathcal{U}([1,2])$ alors $\mathbb{E}[X] = \dfrac{3}{2}$
#     et ${\rm Var}[X] = \dfrac{1}{12}$
# 
# 3.  si $X \sim \mathcal{E}(\lambda)$ alors
#     $\mathbb{E}[X] = \dfrac{1}{\lambda}$ et
#     ${\rm Var}(X) = \dfrac{1}{\lambda^2}$.  
#       
#     Ce dernier cas est plus difficile.  
#     Indication: Utiliser une intégration par parties.  

# Cet exercice est traité dans la feuille de cours supplémentaire.

# **Exercice 2**. (\*\*) Soit $X$ une variable aléatoire. Calculer la
# fonction de répartition de $X$ lorsque :
# 
# 1.  $X \sim \mathcal{U}([a,b])$
# 
# 2.  $X\sim \mathcal{E}(\lambda)$  

# 1. $F_X(x) = \int_a^x \frac{dt}{b-a} =  \frac{x-a}{b-a}$
# 2. $F_X(x) = \int_0^x \lambda e^{-\lambda t}dt = [-e^{-\lambda t}]_0^x = 1-e^{-\lambda x}$

# 
