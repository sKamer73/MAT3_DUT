#!/usr/bin/env python
# coding: utf-8

# # Correction du sujet de contrôle 2020

# Ici, l'énoncé est donné, sa correction étant donné en dessous. Du code Python a été utilisé pour faciliter les calculs, bien que calculable à la main, afin de donner des idées d'outils possibles et/ou de méthodes algorithmiques.

# **Exercice 1: 7 points**
# 
# | Charge Maximale | Nombre de câbles |
# |:---------------:|:---------------:|
# |[9,3 ;9,7]|2| 
#  |[9,8 ;10,2]|5| 
#  |[10,3 ;10,7]|12| 
#  |[10,8 ;11,2]|17| 
#  |[11,3 ;11,7]|14| 
#  |[11,8 ;12,2]|6| 
#  |[12,3 ;12,7]|3| 
#  |[12,8 ;13,2]|1|
# 
# Calculer la moyenne, la médiane, l'écart type et les quartiles de cette distribution.

# ```{admonition} Cliquez pour voir la solution!
# :class: dropdown
# 
# **Correction:**
# 
# Dans cet exercice, il est d'abord nécessaire de donner une valeur unique aux intervalles. On prend de manière classique la valeur moyenne, par exemple: [9.3;9.7] -> 9.5.
# 
# Pour le calcul de la moyenne, la formule $\bar{x}=\frac{1}{N} \sum_{i=1}^n x_i*n_i$ est utilisée et donne:
# $\bar{x}=11.09 \ t$
# Pour le calcul de la variance (puis de l'écart-type), la formule $Var(x)=\frac{1}{N} \sum_{i=1}^n (x_i-\bar{x})²*n_i$ est utilisée et donne:
# $Var(x) = 0.546 \ t²$ et donc $\sigma = \sqrt{Var(x)} = 0.7392 \ t$
# 
# Pour le calcul des médianes et des quartiles, ce genre d'exercice se fait bien en ajoutant les fréquences dans le tableau:
# ```

# Ci-dessous, code pour calcul rapide. Applicable à de nombreuses séries, lisibles facilement via pandas.read_csv(chemin au fichier). Voir la correction du TD de stat en Python pour plus de fonctions.

# In[2]:


#importation standards des librairies pour plotter et calculer
import pandas as pd
from ipywidgets import interact, interactive, fixed, interact_manual, IntSlider
# Standard plotly imports
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
# Using plotly + cufflinks in offline mode
import cufflinks as cf
cf.go_offline(connected=False)
init_notebook_mode(connected=False)


# In[7]:


#Méthode de calcul des moyennes et écarts-types rapide
valeurs = [9.5,10,10.5,11,11.5,12,12.5,13]
nombres = [2,5,12,17,14,6,3,1]
dataForFrame = [[valeurs[k] for i in range(nombres[k])] for k in range(len(nombres))] #il est plus simple de créer une liste avec la charge répétée son nombre de fois
dataForFrame=sum(dataForFrame,[])
df=pd.DataFrame(data=[dataForFrame]).T #création d'un dataframe
df.columns=["Charge"] #on nomme les colonnes
df.describe() #décrire le dataframe donne accès à toutes les informations
#mean:moyenne
#std: standard deviation = écart-type


# Le tableau nécessaire est ci-dessous (avec du code pour son affichage).

# In[12]:


df2=pd.DataFrame(data=[valeurs,nombres]).T
df2.columns=["charge","nombres"]
df2["Fréquence (%)"]=df2["nombres"]/60*100
df2["Fréquence Cumulée (%)"]=df2["Fréquence (%)"]
for k in range(1,len(df2["Fréquence (%)"])):
    df2["Fréquence Cumulée (%)"][k]+=df2["Fréquence Cumulée (%)"][k-1]
df2


# ```{admonition} Cliquez pour voir la fin de la solution!
# :class: dropdown
# Par lecture du tableau ci-dessus, on voit alors que la médiane (où la barre des 50% de fréquence cumulée est dépassé) est de 11, et que les quartiles sont atteints en 10.5 (1er quartile) et en 11.5 (3ème quartile).
# ```

# **Exercice 2: (4 points)**
# 
# Soit X $\sim$ $\mathcal{U}([1,2])$. Montrer que $\mathbb{E}[X]=\dfrac{3}{2}$ puis calculer $V[X]$. 

# ```{admonition} Cliquez pour voir la solution!
# :class: dropdown
# 
# **Correction:** 
# 
# Traité en TD. Le calcul de l'espérance se fait en nommant la densité de probabilité $f_X(x)=\frac{1}{2-1} \mathbb{1}_{[1;2]}(x)$, puis en intégrant sur $\mathbb{R}$ la fonction $x -> x*f_X(x)$.
# 
# Cela s'écrit:
# 
# $E(X) = \int_{-\infty}^{+\infty} x*f_X(x) dx = \int_1^2 xdx = [\frac{x²}{2}]_1^2 = \frac{3}{2}$
# 
# Et le calcul de la variance se fait en utilisant la formule $Var(X)=E(X²)-E(X)²$, il suffit donc de calculer $E(X²)$. Cela s'écrit:
# 
# $E(X²)=\int_{-\infty}^{+\infty} x²*f_X(x) dx = \int_1^2 x²dx = [\frac{x^3}{3}]_1^2 = \frac{7}{12}$
# 
# On trouve alors: $Var(X) = \frac{7}{12}-(\frac{3}{2})² = \frac{1}{12}$
# ```

# **Exercice 3: (4 points)**
# 
# Une route contient 6 feux tricolores alignés, dont les fonctionnements sont indépendants les uns des autres. On estime que chaque feu est vert les 3/4 du temps. Lorsqu'une voiture arrive, quelle est la probabilité: 
# 
# 1. qu'elle ait tous les feux verts?
# 2. qu'elle doive s'arrêter une fois?
# 3. qu'elle doive s'arrêter au moins deux fois?

# **Correction:**
# ```{admonition} Cliquez pour voir la solution!
# :class: dropdown
# 
# On est dans le cas classique d'une loi binomiale: en effet, on répète 6 fois d'affilé une expérience de type Succès-Echec. Par conséquent, on peut poser une variable aléatoire $V_i$, telle que $V_i$ vale 0 si le feu est rouge (échec) et 1 si le feu est vert (succès). Dans ce cas, $V_i \sim \mathcal{B}(3/4)$. Posons alors X=$\sum_{i=1}^6 V_i$, alors X suit une loi binomiale: $X \sim \mathcal{B}(6,3/4)$.
# 
# On nous demande donc:
# 1. $P(X=6) = \begin{pmatrix} 6 \\ 6 \end{pmatrix} (\frac{3}{4})^6 (\frac{1}{4})^0 = \frac{6!}{6! 0!} * (\frac{3}{4})^6 = (\frac{3}{4})^6 = 0.177$
# 
# 2.$P(X=5) = \begin{pmatrix} 6 \\ 5 \end{pmatrix} (\frac{3}{4})^5 (\frac{1}{4})^1 = \frac{6!}{5! 1!} * (\frac{3}{4})^5 * \frac{1}{4} = 6*(\frac{3}{4})^5*\frac{1}{4} = 0.356$
# 
# 3.$P(X \leq 4) = 1-P(X > 4)$. Or $P(X > 4) = P(X \ge 5) = P(X=5)+P(X=6) = 0.534$. d'où: $P(X \leq 4) = 0.466$
# ```

# **Exercice 4: (5 points)**
# 
# Des machines fabriques des plaques de tôle destinées à être empilées. 
# 1. Soit $X$ la variable aléatoire "épaisseur de la plaque en mm"; on suppose que $X$ suit une loi normale de paramètres $m=0,3 \ mm$ et $\sigma=0,1 \ mm$. Calculez la probabilité pour que $X$ soit inférieur à $0,36$ mm et la probabilité pour que $X$ soit compris entre $0.25$ et $0,35$ mm. (**Indication**: En supposant que $P(Y\leq 0,6)=0.726$ où $Y\sim \mathcal{N}(0,1)$ et que $F(0,5)=0.6915$ où $F$ est la fonction de répartition d'une loi normale centré réduite).
# 2. L'utilisation de ces plaques consiste à en empiler $n$, numérotées de $1$ à $n$ les prenant au hazard: soit $X_i$ la variable aléatoire "épaisseur de la plaque numéro $i$ en mm" et $Z$ la variable aléatoire "épaisseur des $n$ plaques en mm". Pour $n=20$, quelle est la loi de $Z$, son espérance et sa variance? 
# 

# ```{admonition} Cliquez pour voir la solution!
# :class: dropdown
# 
# **Correction:**
# 
# 1. Soit $Y=\frac{X-m}{\sigma}$, alors $Y \sim \mathcal(N)(0,1)$. On doit calculer $P(X \leq 0.36) = P(Y \leq \frac{0.36-m}{\sigma}) = P(Y \leq 0.6) = 0.726$ (d'après l'énoncé, surprise). On doit maintenant calculer $P(0.25 \leq X \leq 0.35) = P(\frac{0.25-m}{\sigma} \leq Y \leq \frac{0.35-m}{\sigma} = P(-0.5 \leq Y \leq 0.5)$. Dans l'énoncé, on nous donne $P(Y \leq 0.5) = F(0.5)$. En traçant la courbe et en utilisant ses propriétés de symétrie, on voit facilement les relations suivantes: $P(-0.5 \leq Y \leq 0.5) = 2*P(0 \leq Y \leq 0.5) = 2*(F(0.5)-0.5) = 0.383$
# 2. Comme cela a été vu en TD: $Z=\sum_{i=1}^n X_i$, alors d'après les propriétés d'additions de Gaussienne, si $X_i \sim \mathcal{N}(m,\sigma)$, alors $Z \sim \mathcal{N}(n*m,\sqrt{n*\sigma²})$. Par conséquent, avec $n=20$, on sait que $Z \sim \mathcal{N}(6,0.44)$.
# ```

# In[19]:


from math import sqrt
print(20*0.3,",",sqrt(20)*0.1)

