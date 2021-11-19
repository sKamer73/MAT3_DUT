#!/usr/bin/env python
# coding: utf-8

# # Cours
# ## Introduction
# 
# 
# Dans ce premier chapitre, nous allons aborder la géométrie dans l'espace. Une introduction aux outils mathématiques utilisés pour décrire les forces, vitesses et positions des différents objets nous environnant est donnée.
# 
# Une vidéo de M. Ouin présentant une version similaire de ce cours est disponible à l'adresse suivante: https://www.youtube.com/watch?v=9LGTMhIp7ig .
# 
# ### Définition
# 
# Dans l'ensemble de ce chapitre on définit un repère orthonormé $\mathcal{E} = (O,\vec{i},\vec{j},\vec{k})$ dans l'espace .
# 
# ## Vecteurs, rappels
# 
# **Définition.** Un vecteur est un objet mathématique, généralement noté à l'aide d'une flèche, caractérisé par sa direction, son sens ainsi que sa norme. 
# 
# Par exemple si $A$ et $B$ sont deux points de l'espace, de coordonnées respectives $\begin{pmatrix} x_A \\ y_A \\ z_A \end{pmatrix}$ et $\begin{pmatrix} x_B \\ y_B \\ z_B \end{pmatrix}$, le vecteur $\vec{AB}$ a pour coordonnées $\begin{pmatrix}x_A-y_A \\ x_B-y_B \\ z_B-z_A \end{pmatrix}$, il a pour direction la droite $(AB)$, pour sens $A$ vers $B$ et pour norme :
# 
# $$
# ||\vec{AB}|| = \sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}
# $$
# 
# La norme du vecteur $\vec{AB}$ est égale à la distance de $A$ à $B$.
# 
# Un vecteur peut être défini sans la donnée a priori de deux points : on peut par exemple se donner le vecteur $\vec{u}$ ayant pour coordonnées $(x_u,y_u,z_u)$. Pour faire l'analogie avec la précédente définition, on comprendra le vecteur $\vec{u}$ comme le vecteur $\vec{O U}$ ou $U$ est le point de coordonnées $(x_u;y_u;z_u)$. Dans ce cas :
# 
# $$
# ||\vec{u}|| = \sqrt{x_u^2+y_u^2 + z_u^2}
# $$ 
# 
# **Exemple.** En mécanique, les vitesses et les forces sont toutes représentées par des vecteurs. Ces derniers contiennent l'information sur la direction et l'ampleur des phénomènes. Les vecteurs sont donc des outils très pratiques dans ce domaine. Il est fréquent d'écrire un vecteur sous la forme: norme $\cdot$ vecteur direction, par exemple: soit $\vec{F}$ une force, il peut être utile d'écrire $\vec{F} = F \vec{u}$ avec $F$ la norme du vecteur $\vec{F}$ ($F=||\vec{F}||$) et $\vec{u}$ le vecteur unitaire indiquant la direction de la force ($\vec{u} = \frac{\vec{F}}{F}$).
# 
# ## Opération sur les vecteurs dans l'espace
# ### Produit scalaire
# 
# Soient $\vec{u}$ et $\vec{v}$ deux vecteurs de coordonnées $\begin{pmatrix} x_u \\ y_u \\ z_u \end{pmatrix}$ et $\begin{pmatrix} x_v \\ y_v \\ z_v \end{pmatrix}$.
# 
# On appelle produit scalaire de deux vecteurs et on note par $\cdot$ la quantité (réelle, ce n'est pas un vecteur !) : 
# $\vec{u} \cdot \vec{v} = x_u x_v + y_u y_v + z_u z_v.$
# On remarquera en particulier que :
# 
# 
# $$||\vec{u}||^2 = x_u^2 + y_u^2 + z_u^2 = \vec{u}\cdot\vec{u}.$$
# 
# 
# Il existe aussi une expression géométrique du produit scalaire de deux vecteurs :
# 
# $$
# \vec{u} \cdot \vec{v} = ||\vec{u}|| \times ||\vec{v}|| \times \cos(\vec{u},\vec{v}),
# $$
# 
# où $(\vec{u},\vec{v})$ est l'angle orienté formé par les vecteurs $\vec{u}$ et $\vec{v}$.\\
# 
# **Exemple.** Un cycliste prenant le vent de face, de côté ou de l'arrière ne ressentira pas du tout les mêmes frottements dûs à l'air. En fait, la composante du vent influant sur la puissance qu'il doit développer est celle projetée dans la direction de son déplacement. Mathématiquement, soit $\vec{v}$ la vitesse du vent dans le référentiel du cycliste et $\vec{u}$ le vecteur unitaire indiquant la direction de déplacement du cycliste. Alors, la composante influente dans son déplacement sera $\vec{v} \cdot \vec{u}$. La même chose s'applique en voiture et donc pour expliquer la consommation d'essence.
# 
# ### Orthogonalité de deux vecteurs
# 
# On déduit aisément de l'expression géométrique du produit scalaire que si $\vec{u}$ et $\vec{v}$ sont deux vecteurs orthogonaux alors leur produit scalaire est nul. On a en fait le résultat plus général suivant :
# 
# **Proposition 1.** On dit que deux vecteurs sont orthogonaux si et seulement si leur produit scalaire est nul, autrement dit :
# $\vec{u} \perp \vec{v} \Leftrightarrow \vec{u} \cdot \vec{v} =0.$
# 
# 
# **Exemple.** Un vent de côté n'influencera pas la demande en puissance du cycliste.
# 
# ### Opération sur les vecteurs
# 
# Soient $\vec{u}$ et $\vec{v}$ deux vecteurs de coordonnées $\begin{pmatrix} x_u \\ y_u \\ z_u \end{pmatrix}$ et $\begin{pmatrix} x_v \\ y_v \\ z_v \end{pmatrix}$, alors :
# 
# * pour tout $\lambda \in \mathbb{R}$, $\lambda\vec{u}$ est le vecteur de coordonnées $\begin{pmatrix} \lambda x_u \\ \lambda y_u \\ \lambda z_u\end{pmatrix}$
# * $\vec{u}+\vec{v}$ est le vecteur de coordonnées $\begin{pmatrix} x_u+x_v\\y_u+y_v\\z_u+z_v \end{pmatrix}$. 
# 
# 
# **Exemple.** La vitesse du cycliste influe sur son ressenti de la vitesse du vent. Soit $\vec{v}_{vent}$ la vitesse du vent lorsque le cycliste est à l'arrêt, et soit $\vec{v}_{cycliste}$ la vitesse du cycliste. La vitesse du vent telle que ressentie par le cycliste sera alors $\vec{v}_{vent}-\vec{v}_{cycliste}$. 
# 
# **Question bonus**: Si un vent provenant de la direction sud-ouest et d'intensité 30 km/h souffle sur le cycliste qui circule vers le nord, quelle vitesse devra-t-il avoir pour que le vent ne lui apporte plus d'aide?
# 
# ### Produit vectoriel
# #### Trièdre direct
# 
# Soit $\vec{u},\vec{v},\vec{w}$  trois vecteurs de l'espace $\mathcal{E}$. On dit que $(\vec{u},\vec{v},\vec{w})$ est un triède direct si :
# 
# * $\vec{u},\vec{v},\vec{w}$ ne sont pas coplanaires
# * $\vec{u},\vec{v},\vec{w}$ vérifient la règle des trois doigts (pouce, index, majeur).
# 
# 
# 
# #### Produit vectoriel
# On peut enfin définir dans l'espace, et uniquement dans l'espace, le produit vectoriel.
# 
# **Définition.**
# 
# Soient $\vec{u}_1$ et $\vec{u}_2$ deux vecteurs de l'espace. On appelle produit vectoriel de $\vec{u}_1$ et $\vec{u}_2$ et on note $\vec{u}_1 \wedge \vec{u}_2$ le vecteur:
# 
# * orthogonal à $\vec{u}_1$ et $\vec{u}_2$
# * de direction telle que le trièdre ($\vec{u}_1,\vec{u}_2,\vec{u}_1 \wedge \vec{u}_2$) soit direct
# * de norme $||\vec{u}_1 \wedge \vec{u}_2|| = ||\vec{u}_1 || \times || \vec{u}_2|| \times |\sin(\vec{u}_1,\vec{u}_2)|$ où $(\vec{u}_1,\vec{u}_2)$ est l'angle orienté formé par les vecteurs $\vec{u}_1$ et $\vec{u}_2$,
# 
# lorsque  $\vec{u}_1$ et $\vec{u}_2$ ne sont pas colinéaires et le vecteur nul $\vec{0_E}$ sinon.
# 
# 
# **Remarque.** La direction est donc donnée par l'orthogonal aux vecteurs $\vec{u}$ et $\vec{v}$, le sens se déduit du trièdre direct.
# 
# 
# D'un point de vue "pratique", on calcule les coordonnées du vecteur produit de la manière suivante. Soient $\vec{u}_1$ et $\vec{u}_2$ deux vecteurs de $\mathcal{E}$ de coordonnées respectives $\begin{pmatrix}x_1 \\ y_1 \\ z_1\end{pmatrix}$ et $\begin{pmatrix}x_2 \\ y_2 \\ z_2\end{pmatrix}$ dans cette base. Le vecteur $\vec{u}_1 \wedge \vec{u}_2$ aura pour coordonnées : 
# 
# $$
# \begin{pmatrix}
# y_1z_2 - z_1y_2\cr
# z_1x_2 - z_2 x_1 \cr
# x_1y_2 - x_2y_1\cr
# \end{pmatrix}
# $$
# 
# Finalement, on a les propriétés suivantes concernant le produit vectoriel:
# 
# **Propriété.**
# Soient $\vec{u},\vec{v}$  deux vecteurs de l'espace $\mathcal{E}$, alors :
# 
# * $\vec{u} \wedge \vec{v}$ est orthogonal à $\vec{u}$ et à $\vec{v}$;
# * $\vec{u}$ et $\vec{v}$ sont colinéaires ssi $\vec{u} \wedge \vec{v} =\vec{0}$.
# * $\vec{u} \wedge \vec{v} =-\vec{v} \wedge \vec{u}$.
# 
# **Exemple.** En mécanique, le moment appliqué par une force se définit au moyen du produit vectoriel: soit O l'axe de référence, P le point d'application d'une force $\vec{F}$, le moment appliqué par cette force s'écrit $M_O = \vec{OP} \wedge \vec{F}$. On peut alors retrouver la notion de bras de levier: Si $\vec{OP}$ et $\vec{F}$ sont perpendiculaires (comme dans le cas d'un poids au bout d'une grue), on a alors $||M_O|| = OP \times F$. 
# 
# ## Equation cartésienne d'un plan dans l'espace
# 
# Soit $A$, $B$ et $C$ trois points non alignés de l'espace, on appelle plan de l'espace $\mathcal{E}$ et on note $\mathcal{P}$ le plan $(ABC)$. Pour rappel,  $\mathcal{P}$ est l'ensemble des points $M$ de $\mathcal{E}$ tels que $\vec{AM} = \lambda_1 \vec{AB} + \lambda_2 \vec{AC}$ quand $\lambda_1$ et $\lambda_2$ parcourent $\mathbb{R}$ : 
# $$
# \mathcal{P} = \{M \in \mathcal{E},\quad \vec{AM} = \lambda_1 \vec{AB}+\lambda_2 \vec{AC},\ \lambda_1, \lambda_2 \in \mathbb{R}\}
# $$ 
# 
# On dira que $\vec{AB}$ et $\vec{AC}$ sont deux vecteurs directeurs de $\mathcal{P}$.
# 
# ### Détermination de l'équation cartésienne.
# 
# Soit $\vec{n}=\begin{pmatrix}a \\ b \\ c \end{pmatrix}$ un vecteur normal au plan $(ABC) = : \mathcal{P}$. Alors, pour tout point $M$ de coordonnées $(x,y,z)$ du plan : 
# $\vec{AM} \cdot \vec{n} = 0.$
# *i.e.*
# $
# (x-x_A)a + b(y-y_A) + c(z-z_A) = 0 \Leftrightarrow ax + by + cz - (x_A.a+y_A.b+z_A.c) = 0.
# $
# On en déduit :
# 
# **Proposition 3.**
# L'ensemble des points de $\mathcal{E}$ de coordonnées $(x,y,z)$ telles que :
# $ax+by + cz + d = 0,$
# où au moins un des réels $a$, $b$ et $c$ est différent de 0, forme un plan affine $\mathcal{P}$ admettant $\vec{n}=\begin{pmatrix}a \\ b \\ c \end{pmatrix}$ comme vecteur normal. On parle d'équation cartésienne du plan $\mathcal{P}$ dans l'espace. 
# 
# 
# **Exemple.** D'après sa définition, le vecteur $\vec{AB} \wedge \vec{AC}$ est normal au plan $\mathcal{P}$.
# 
# 
# 
# ### Distance d'un point à un plan
# 
# Soit $\mathcal{P}$ un plan d'équation cartésienne $ax + by + cz +d =0$ et soit $M$ un point quelconque de l'espace de coordonnées $(x_M,y_M,z_M)$. La distance du point $M$ au plan, notée $d(M,\mathcal{P})$ est donnée par :
#  $d(M,\mathcal{P}) = \frac{|ax_M+ by_M + cz_M + d|}{\sqrt{a^2+b^2+c^2}}.$
# C'est la plus petite distance du point $M$ à n'importe quel point du plan $\mathcal{P}$. Le point du plan $\mathcal{P}$ qui réalise cette distance est appelé \textbf{projeté orthogonal de $M$ sur $\mathcal{P}$}.
# 
# **Question bonus:** Le démontrer !
# 
# ## Equation d'une droite dans l'espace
# 
# Soient $A(x_A;y_A;z_A)$, $B(x_B;y_B;z_A)$ deux points de l'espace. La droite $(AB)$ est l'ensemble des points $M$ de $\mathcal{E}$  tels que $\vec{AM} = \lambda .\vec{AB} $ quand $\lambda$ parcourt $\mathbb{R}$ : 
# $(AB) = \{M \in \mathcal{E},\quad \vec{AM} = \lambda. \vec{AB},\ \lambda \in \mathbb{R}\}.$
# On dira que $\vec{AB}$ est un vecteur directeur de $(AB)$.
# 
# 
# De cette définition, on obtient un système d'équations paramétriques de la droite $(AB)$:
# $$
# \left\lbrace\begin{array}{lll}
# (x-x_A) = \lambda (x_B-x_A)\\
# (y-y_A) = \lambda (y_B-y_A),\quad \lambda \in \mathbb{R}\\
# (z-z_A) = \lambda (z_B-z_A)
# \end{array}\right. \Leftrightarrow \left\lbrace\begin{array}{lll}
# x = \lambda (x_B-x_A) + x_A\\
# y = \lambda (y_B-y_A)+ y_A ,\quad \lambda \in \mathbb{R}\\
# z = \lambda (z_B-z_A)+ z_A
# \end{array}\right. 
# $$
#  
#  
#  
# Par ailleurs, les vecteurs $\vec{AB}$ et $\vec{AM}$ sont colinéaires, en particulier :
# 
# $$
# \vec{AB} \wedge \vec{AM} = \vec{0}
# $$
# 
# L'ensemble des points $M$ de coordonnées $(x,y,z)$ appartenant à $(AB)$ est donc caractérisé par un système d'équations.\
# 
# En effet, étant donné un point $M$ de la droite $(AB)$ et en notant les coordonnées de $\vec{AB} = \begin{pmatrix}\alpha\cr \beta \cr \gamma \end{pmatrix}$ on retrouve le système:
# 
# ```{math}
# :label: eq_1
# \gamma(y-y_A) - \beta(z-z_A) = 0 
# ```
# 
# 
# $$
# \alpha(z-z_A)-\gamma(x-x_A)=0 
# $$ (eq_2)
# 
# $$
# \beta(x-x_A) - \alpha (y-y_A)=0 
# $$ (eq_3)
# 
# On remarque que $\alpha \times$ {eq}`eq_1` $+ \beta \times $ {eq}`eq_2`  $=-\gamma $ {eq}`eq_3` et qu'en conséquence l'équation {eq}`eq_3` est superflue. La droite $(AB)$ est donc caractérisée par le système d'équations:
# 
# $$
# \gamma(y-y_A) - \beta(z-z_A) = 0\\
# \alpha(z-z_A)-\gamma(x-x_A)=0.
# $$
# 
# On l'appelle système d'équation caractéristique de $(AB)$.
# 
# **Remarque.** Il s'agit en fait des équations de deux plan de l'espace $\mathcal{E}$. Dans l'espace, une droite est ainsi caractérisée comme l'intersection de deux plans.
# 
# **Question bonus:** Le démontrer !
# 
# 

# In[ ]:




