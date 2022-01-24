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

# **Correction:** la correction et disponible dans la feuille de cours supplémentaire présentant les calculs d'espérance et de variance des lois usuels.

# **Exercice 2**. (\*\*) Soit $X$ une variable aléatoire. Calculer la
# fonction de répartition de $X$ lorsque :
# 
# 1.  $X \sim \mathcal{U}([a,b])$
# 
# 2.  $X\sim \mathcal{E}(\lambda)$  

# **Correction:**
# 
# 1. $F_X(x) = \int_a^x \frac{dt}{b-a} =  \frac{x-a}{b-a}$
# 2. $F_X(x) = \int_0^x \lambda e^{-\lambda t}dt = [-e^{-\lambda t}]_0^x = 1-e^{-\lambda x}$

# **Exercice 3**. (\*) Madame Michel et Monsieur Boulanger vont chaque
# semaine au marché hebdomadaire. Madame Michel arrive à une heure
# aléatoire entre 8h et 12h et elle reste 30 minutes ; on suppose que son
# heure d’arrivée suit une loi uniforme. Monsieur Boulanger arrive à 10h
# pile et reste également 30 minutes. Quelle est la probabilité pour
# qu’ils se trouvent ensemble au marché à un certain moment ?

# $M$ la v.a. de l'arrivée de Mme Michel. On cherche $P(9.5<M<10.5)$. On a alors:
# $P(9.5<M<10.5)=\int_{9.5}^{10.5} \frac{dt}{4} = 0.25$

# **Exercice 4**. (\*) Max a un rendez-vous avec une amie. Ils vont au
# restaurant, puis au cinéma. Le temps passé au restaurant est une
# variable aléatoire suivant une loi exponentielle de paramètre
# $\lambda = 1$. (temps compté en heures)
# 
# 1.  Le film commence 1 heure après leur entrée au restaurant. On néglige
#     les temps d’attente et de déplacement, quelle est alors la
#     probabilité pour qu’ils ratent le début du film ?
# 
# 2.  Le film dure 1h30. Quelle est la probabilité qu’ils ne voient qu’une
#     partie du film seulement ?
# 
# 3.  Le temps passé au cinéma est une variable aléatoire de loi
#     exponentielle de paramètre $\lambda = \frac{1}{2}$. Combien de temps
#     Max peut-il espérer passer avec son amie ce soir ?

# **Correction**:
# 
# soit T la v.a. du temps passé au restaurant.
# 
# 1. $P(T>1)=\int_1^{+\infty} \lambda e^{-\lambda t} dt = [-e^{-\lambda t}]_1^{+\infty}=e^{-\lambda}=e^{-1}$
# 2. $P(1<T<2.5)=\int_1^{2.5} \lambda e^{-\lambda t} dt = [-e^{-t}]_1^{2.5}= e^{-1}-e^{-2.5}$
# 3. Soit $C$ la v.a. du temps passé au cinéma Alors: $E(T+C) = E(T)+E(C) = \frac{1}{1}+\frac{1}{\frac{1}{2}}=3$

# **Exercice 5**. (\*)
# 
# 1.  Soit $X$ une variable aléatoire suivant une loi normale
#     $N(m,\sigma)$. Quelle est la probabilité que $X$ soit supérieure à
#     $m$ ?
# 
# 2.  Soit $Y$ une variable aléatoire suivant une loi normale $N(0,1)$.
#     Quelle est la loi de $-Y$ ? la loi de $\sigma Y+m$ ?
# 
# 3.  En utilisant la table de $\mathcal{N}(0,1)$, déterminer
#     $P(0\leqslant Y\leqslant 0,8)$, $P(-0,6\leqslant Y\leqslant 0)$ et
#     $P(Y\leqslant 0,8)$.

# **Correction:**
# 
# 1. Montrer avec le changement de variable et avec le dessin que c'est 1/2. Invoquer la symétrie de la fonction carré.
# 2. -Y suit la loi $N(0,1)$, par symétrie en 0. D'après le cours, $\sigma Y+m \sim N(m,\sigma)$ 
# 3. voir table. Précisément: $P(0<=Y<=0.8)=0.7881-0.5=0.2881$,$P(-0,6\leqslant Y\leqslant 0)=0.7257-0.5=0.2257$, $P(Y<=0.8)=0.7881$

# **Exercice 6**. (\*) La variable aléatoire $X$ suit la loi normale
# $N(12,4)$. Calculer:
# $$P(X\leqslant 15), \qquad P(X\geqslant 18), \qquad P(X\geqslant 7), \qquad P(X\leqslant 9), \qquad P(8\leqslant X\leqslant 17).$$

# Soit $Y=\frac{X-12}{4}$ la variable centrée réduite correspondante, on cherche les probas:
# 
# $$P(Y\leqslant 0.75)=0.7734, \qquad P(Y\geqslant 1.5)=1-0.9332=, \qquad P(Y\geqslant -1.25) = P(Y \leqslant 1.25) = 0.8944, \qquad P(Y \leqslant -0.75)=0.5 - (0.7734-0.5), \qquad P(-1\leqslant Y\leqslant 1.25).$$

# **Exercice 7**. (\*) Une machine produit des rondelles métalliques en
# grande série. Une rondelle est acceptée si son diamètre extérieur est
# compris entre 21,9 et 22,1 mm. On suppose que sur l’ensemble de la
# production le diamètre extérieur des rondelles est une variable
# aléatoire X suivant la loi normale de moyenne $m$ = 22 mm et
# d’écart-type $\sigma$ = 0,05 mm. Quelle est la probabilité qu’une pièce
# soit refusée ?

# **Correction:**
# 
# $P(21.9<=X<=22.1)=P(-0.1/0.05<Y<0.1/0.05)=P(-2<Y<2)=2*(0.9772-0.5)=0.95439$
# La réponse à la question est alors $-> 1-P(21.9<=X<=22.1)=0.0456$

# In[2]:


1-2*(0.9772-0.5)


# **Exercice 8**. (\*) Le nombre de clients d’un magasin suit chaque
# samedi une loi normale $N(365,30)$. Quelle est la probabilité pour qu’il
# y ait un samedi donné:
# 
# 1.  plus de 400 clients ?
# 
# 2.  moins de 300 clients ?
# 
# 3.  entre 320 et 380 clients ?

# 1.$P(N>400)=P(N_{adim}>1.17)=1-0.9554$
# 
# 2. $P(N<300)=P(N_{adim}<-2.16)=0.5-(0.9846-0.5)=0.0153$
# 
# 3. $P(320<N<380)=P( -1.5 < N_{adim}<0.5 )=0.6915-(1-P(N_{adim}<-1.5))=0.6915-1+(0.9332-0.5)=0.124$

# **Exercice 9**. (\*\*) Dans une population, le poids des individus est
# une variable aléatoire suivant une loi normale de moyenne égale à 60 kg
# et un écart-type égal à 15 kg. Un ascenseur a une capacité égale à 2200
# kg. Calculer :
# 
# 1.  La probabilité que 20 individus pèsent ensemble plus de 2200 kg.
# 
# 2.  Le nombre maximum de personnes pouvant rentrer dans l’ascenseur de
#     sorte que celui-ci ne soit en surcharge qu’avec une probabilité
#     inférieure à 0,01.

# $M=\sum_i M_i$, M suit la loi $N(20*60,\sqrt{20*\sigma²})=N(1200,67.08)$
# 1. $P(M>2200)=P(M_{a}>14.9)=0$
# 2. M suit la loi $N(n*60,\sqrt{n}*15)$, et on veut $P(N>2200)=0.01$ (99ème centile), d'où: $P(N_{a}>\frac{2200-n*60}{\sqrt{n}*15})$, le deuxième doit être égal à 2.326, on doit résoudre (en passant au carré):
# $(2200²-120*2200*n+60²*n²)/(n*15²)=2.326²$ équivalent à $60²*n²-(120*2200+2.326²*15²)*n+2200²=0$

# In[25]:


sqrt(20)*15


# In[21]:


delta = (120*2200+15**2*2.326**2)**2-4*(60**2)*2200**2


# In[22]:


x1=(-(120*2200+15**2*2.326**2)+sqrt(delta))/(2*60**2)


# In[23]:


x1


# **Exercice 10**. (\*\*) Une machine est conçue pour confectionner des
# paquets d’un poids de 500g, mais ils n’ont pas exactement tous le même
# poids. On a constaté que la distribution des poids autour de la valeur
# moyenne de 500g avait un écart-type de 25g.
# 
# 1.  Par quelle loi est-il raisonnable de modéliser le poids des paquets
#     ?
# 
# 2.  Sur 1000 paquets, quel est le nombre moyen de paquets pesant entre
#     480g et 520g ? (*utiliser la table de $\mathcal{N}(0,1)$*)
# 
# 3.  Combien de paquets pèsent entre 480g et 490g ?
# 
# 4.  Sur 1000 paquets, quel est le nombre moyen de paquets pesant plus de
#     450g ?
# 
# 5.  Trouver $a$ tel que les 9/10 de cette production aient un poids
#     compris entre $500-a$ et $500+a$.

# **Exercice 11**. (\*\*\*) Une entreprise d’édition a retenu la technique
# du placard publicitaire vantant quelques articles sans en donner le
# prix, invitant le lecture à recevoir à domicile gratuitement et san
# engagement de sa part des documents le renseignant de façon détaillée.
# L’expérience montre que le client qui se manifeste a une chance sur cinq
# de passer commande. En utilisant une approximation appropriée, calculer
# la probabilité d’observer lorsque l’on envoie 500 articles de
# renseignement :
# 
# 1.  exactement 110 commandes
# 
# 2.  plus de 110 commandes

# Manque la donnée: quelle proba que le client se manifeste

# **Exercice 12**. (\*\*\*) La demande de fabrication d’une pièce X à une
# entreprise suit une loi normale. Elle a une probabilité 0,1 d’être
# inférieure à 15.000, et une probabilité 0,1 d’être supérieure à 25.000.
# 
# 1.  Déterminer les paramètres de la loi normale.
# 
# 2.  La marge sur une pièce est de 10 euros, les charges fixes mensuelles
#     de l’entreprise sont de 175.000 euros. Déterminer la loi de
#     probabilité suivie par le résultat mensuel de l’entreprise.
# 
# 3.  En déduire la probabilité que le seuil de rentabilité mensuel soit
#     atteint.
# 
# 4.  Quelle est la probabilité que le seuil de rentabilité trimestriel
#     soit atteint ?

# P(N_a<x)=0.1 -> x1 = -1.282=(15000-m)/s, 1.282 = (25000-m)/s -> m = 20000, s

# In[ ]:




