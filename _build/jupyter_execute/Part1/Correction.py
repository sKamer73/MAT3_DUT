#!/usr/bin/env python
# coding: utf-8

# # Correction du TD

# ```{note}
# Dans tout le TD, on se place dans un repère orthonormé $\mathcal{E} = (O,\vec{i},\vec{j},\vec{k})$.
# ```
# 
# 
# **Exercice 1.** On souhaite exprimer l'aire S d'un triangle à l'aide d'un produit vectoriel. On considère le triangle $ABC$ et on note les coordonnées des points $A(1;-2;7)$, $B(2;2;1)$ et $C(1;1;5)$.
# 
# Dans le plan $(ABC)$, les formules de trigonométrie donnent la relation suivante:
# 
# $$
# S=\frac{1}{2}\begin{Vmatrix}\vec{AB}\end{Vmatrix} \times \begin{Vmatrix}\vec{AC}\end{Vmatrix} \times \begin{vmatrix}sin\alpha\end{vmatrix}
# $$
# 
# où $\alpha$ est l'angle orienté $(\vec{AB},\vec{AC})$.
# 
# * Exprimer l'aire $S$ à l'aide d'un produit vectoriel.
# * Calculer l'aire $S$.
# 
# **Corrigé.** 
# 
# 1. On remarque via la formule du cours que $S=\frac{1}{2} ||\vec{AB} \wedge \vec{AC}||$
# 2. On fait le calcul: $\vec{AB} = \begin{pmatrix} 1 \\ 4 \\ -6 \end{pmatrix}$ et $\vec{AC} = \begin{pmatrix} 0 \\ 3 \\ -2 \end{pmatrix}$
# 
# On en déduit: $\vec{AB} \wedge \vec{AC} = \begin{pmatrix} 10 \\ 2 \\ 3 \end{pmatrix}$
# D'où $S = \frac{1}{2} \sqrt{100+4+9} = 5.31$ (l'unité de S est alors l'unité que l'on choisit pour les coordonnées des points A,B,C: si les points sont en m, la surface est en m², cm => cm², etc.)

# In[4]:


from math import sqrt
sqrt (100+4+9)/2


# **Exercice 2.** On considère le point $A(-2;0;5)$ et le vecteur $\vec{n}\begin{pmatrix}
# 2\\-6\\4
# \end{pmatrix}$.
# 
# Déterminer une équation cartésienne du plan $\mathcal{P}$ passant par $A$ et de vecteur normal $\vec{n}$.
# 
# **Corrigé.**
# 
# On utilise la démonstration du cours (plus facile à retenir que la formule): soit M$(x,y,z)$ un point du plan $\mathcal{P}$, alors M vérifie l'équation: $\vec{AM} \cdot \vec{n} = 0$. Cela s'écrie: $\begin{pmatrix} x+2 \\ y \\ x-5 \end{pmatrix} \cdot \begin{pmatrix} 2\\-6\\4 \end{pmatrix} = 0 \leftrightarrow 2(x+2)-6y+4(z-5) = 0 \leftrightarrow x-3y+2z-8=0$.
# 
# **Exercice 3.** Soient les points $A(1;-2;7)$, $B(2;2;1)$ et $C(1;1;5)$. En utilisant un produit vectoriel, déterminer une équation cartésienne du plan $(ABC)$.
# 
# **Corrigé.** Le produit vectoriel va nous permettre d'obtenir une normale au plan (ABC). Prenons donc deux vecteurs du plan : $\vec{AB}$ et $\vec{AC}$. Le vecteur $\vec{n} = \vec{AB} \wedge \vec{AC} $ est alors normal au plan. 
# 
# $\vec{AB} = \begin{pmatrix} 1 \\ 4 \\ -6 \end{pmatrix}$ et $\vec{AC} = \begin{pmatrix} 0 \\ 3 \\ -2 \end{pmatrix}$
# 
# On en déduit: $\vec{n} = \begin{pmatrix} 10 \\ 2 \\ 3 \end{pmatrix}$. On reprend alors la procédure de l'exercice 2:
# 
# On utilise la démonstration du cours (plus facile à retenir que la formule): soit M$(x,y,z)$ un point du plan (ABC), alors M vérifie l'équation: $\vec{AM} \cdot \vec{n} = 0$. Cela s'écrie: $\begin{pmatrix} x-1 \\ y+2 \\ x-7 \end{pmatrix} \cdot \begin{pmatrix} 10 \\ 2 \\ 3 \end{pmatrix} = 0 \leftrightarrow 10(x-1)+2(y+2)+3(x-7)= 0 \leftrightarrow 10x+2y+3x-28=0$.
# 
# 
# **Exercice 4.** On considère la droite $(AB)$ avec $A(1;2;-1)$ et $B(0;1;3)$, ainsi que le plan $\mathcal{P}$ d'équation : $x+y+z-1=0$.
# 
# * Montrer que $(AB)$ et $\mathcal{P}$ sont sécants.
# * Déterminer les coordonnées de leur point d'intersection $I$. On commencera par déterminer une représentation paramétrique de $(AB)$.
# 
# **Corrigé.** Dans cet exercice, le plus simple est de faire les deux en même temps. Deux techniques sont possibles: soit par une représentation paramétrique de la droite, soit par une représentation en système. L'énoncé indique d'utiliser une forme paramétrique, ce qui s'écrit:
# Soit I un point de (AB) et de $\mathcal{P}$, alors:
# * **Appartenance de I à la droite (AB):** $\vec{AI} = \lambda \vec{AB}$, ce qui s'écrit: $\begin{pmatrix}x_I-1 \\ y_I - 2 \\ z_I +1 \end{pmatrix} = \lambda \begin{pmatrix} -1 \\ -1 \\ 4 \end{pmatrix}$, ce qui s'écrit sous la forme d'un système comme: 
# 
# $$
# \left\{ \begin{array}{l}x_I=1-\lambda \\ y_I=2-\lambda \\ z_I = -1+4\lambda \end{array} \right. \quad
# $$
# * **Appartenance de I au plan** $\mathcal{P}$: En réinjectant les coordonnées de I dans l'équation du plan $\mathcal{P}$, on obtient: $1-\lambda + 2- \lambda -1 + 4 \lambda -1 = 0$, ce qui done alors: $1 + 2\lambda = 0$, d'où: $ \lambda = - \frac{1}{2}$. 
# 
# On en déduit les coordonnées de $I(\frac{3}{2},\frac{5}{2},-3$) en réinjectant $\lambda$ dans le système ci-dessus. Si l'on n'avait pas trouvé de solution pour I, cela aurait démontré que les droites ne s'intersectionnent pas.
# 
# **Exercice 5.** Montrer que les représentations paramétriques suivantes définissent le même plan :
# 
# $$
# \left\{ \begin{array}{l}x=2+s+2t \\ y=2+2s+t \\ z=1-s-t \end{array} \right.
# \quad \text{ et } \quad  \left\{ \begin{array}{l} x=1+3s'-t'\\ y=3+3s'+t'\\ z=1-2s' \end{array} \right.
# $$
# 
# **Correction.**
# On  est ici face à une représentation paramétrique du plan, càd la première définition du cours: soit trois points (A,B,C) du plan d'intérêt, alors tout vecteur $\vec{AM}$ avec M un point du plan peut s'écrire comme une combinaison linéaire de deux vecteurs non colinéaires du plans tels que $\vec{AB}$ et $\vec{BC}$ (par exemple). Cela s'écrit formellement: $\exists (s,t) \in \mathbb{R}², t.q. \ \vec{AM} = s \vec{AB} + t \vec{BC}$. 
# 
# Pour montrer que ces deux représentations se confondent, il faut soit montrer:
# 1. Un point est partagé, les deux normales sont colinéaires.
# 2. Trois points sont partagés.
# 3. Les deux équations cartésiennes sont proportionelles.
# 
# Nous allons traiter la méthode 1. On détermine tout d'abord, pour chacun des deux plans: 2 vecteurs directeurs du plan, on fait le produit vectoriel pour obtenir une normale. Ensuite, on prend un point dans l'une des deux représentations, et on vérifie que ce point appartient à l'autre représentation.
# 
# * Représentation 1. Vecteur $\vec{u}_1=\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$ (valeurs devant le $s$) et $\vec{v}_1 = \begin{pmatrix}2 \\ 1 \\ -1 \end{pmatrix}$ (valeurs devant le $t$). On obtient $\vec{n}_1 = \vec{u}_1 \wedge \vec{v}_1 = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \wedge \begin{pmatrix}2 \\ 1 \\ -1 \end{pmatrix} = \begin{pmatrix} -1 \\ -1 \\ -3 \end{pmatrix}$
# * Représentation 2. Vecteur $\vec{u}_2=\begin{pmatrix} 3 \\ 3 \\ -2 \end{pmatrix}$ (valeurs devant le $s'$) et $\vec{v}_2 = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}$ (valeurs devant le $t'$). On obtient $\vec{n}_2 = \vec{u}_2 \wedge \vec{v}_2 = \begin{pmatrix} 3 \\ 3 \\ -2 \end{pmatrix} \wedge \begin{pmatrix}-1 \\ 1 \\ 0\end{pmatrix} = \begin{pmatrix} 2 \\ 2 \\ 6 \end{pmatrix}$
# 
# On a donc que les deux normales sont colinéaires: $\vec{n}_1 = -\frac{1}{2} \vec{n}_2$.
# On vérifie ensuite qu'un point de la représentation 1 appartient bien à la représentation2. En prenant le point s=t=0, on trouve que le point A(2,2,1) appartient à la représentation 1. On résoud alors le système en s' et t' pour vérifier que le point A vérifie la deuxième représentation. 
# 
# $$
# \left\{ \begin{array}{l}x_A=1+3s'-t'\\ y_A=3+3s'+t'\\ z_A=1-2s' \end{array} \right.
# \quad \text{ d'où } \quad  \left\{ \begin{array}{l} 2=1+3s'-t'\\ 2=3+3s'+t'\\ 1=1-2s' \end{array} \right.
# $$
# 
# On déduit de la troisième équation que s'=0. On déduit de la deuxième équation que $t'=-1$. On réinjecte alors s' et t' dans la première équation pour vérifier que A vérifie la représentation paramétrique n°2. On trouve bien: $ 2=2$. Les deux représentations sont donc bien identiques.
# 
# 
# **Exercice 6.**
# 
# &nbsp; 1. Déterminer la distance du point $A$ au plan $(P)$
# 
# * $A(1,0,2)$ et $(P): 2x+y+z+4=0$.
# * $A(3,2,1)$ et $(P): -x+5y-4z=5$.
# 
# &nbsp; 2. (** Un peu plus difficile) Calculer la distance du point $A(1,2,3)$ à la droite 
# $(D):  \left\{ \begin{array}{l}
# -2x+y-3z=1\\ x+z=1  \end{array} \right.$
# 
# **Correction.** 
# 
# &nbsp; 1.
# 
# On applique la formule du cours: 
# * $d(A,\mathcal{P}) = \frac{|2x_A+y_A+z_A+4|}{\sqrt{2²+1²+1²}} = 4.08$
# 
# * $d(A,\mathcal{P}) = \frac{|-x_A+5 y_A-4z_A-5|}{\sqrt{1²+5²+4²}} = 0.308$
# 
# La formule du cours est bien expliqué [ici](https://fr.wikipedia.org/wiki/Distance_d%27un_point_%C3%A0_un_plan)
# 
# &nbsp; 2.
# 
# La formule nécessaire est [ici](https://fr.wikipedia.org/wiki/Distance_d%27un_point_%C3%A0_une_droite#Dans_l'espace).
# Comment la trouver seul.e? En faisant un dessin, et en appliquant SOHCAHTOA.
# 
# On trouve un vecteur directeur $\vec{u}$ avec deux points; par exemple, en prenant x=0 dans la représentation paramétrique de la droite, on trouve le point B(0,4,1) et en prenant z=0 on trouve le point C(1,3,0), ce qui donne $\vec{u} = \vec{BC} = \begin{pmatrix} 1 \\ -1 \\ -1 \end{pmatrix}$.
# 
# On trouve alors $ d(A,\mathcal{D}) = \frac{||\vec{AB}\wedge \vec{u}||}{||\vec{u}||} = \frac{||\begin{pmatrix} -4 \\ -3 \\ -1 \end{pmatrix}||}{\sqrt{1²+1²+1²}} = 2.94$

# In[4]:


from math import sqrt
print((2*2+2+4)/sqrt(6))
print(abs(-3+5*2-4-5)/sqrt(1+5*5+4*4))
print(sqrt(4*4+3*3+1)/sqrt(3))

