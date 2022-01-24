#!/usr/bin/env python
# coding: utf-8

# IUT de Chambéry - 2 année GCCD 2017-2018  
#   
# 
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
# 
# *Corrigé 1*.
# 
# 1.  Dans ce cas, la variable aléatoire $X$ est discrète à valeur dans
#     l’ensemble fini $\{0,1\}$. D’après la définition du cours,
#     $$\mathbb{E}[X] = 0\times \mathbb{P}(X=0) + 1\times \mathbb{P}(X=1),$$
#     et on déduit du fait que $X$ suive une loi de Bernoulli de paramètre
#     $p$ que : $$\mathbb{E}[X] = 0\times (1-p) + 1\times p =p.$$ Par les
#     même arguments on obtient que : $$\begin{aligned}
#     {\rm Var}[X] &=& (0-\mathbb{E}[X])^2\times \mathbb{P}(X=0) + (1-\mathbb{E}[X])^2 \times \mathbb{P}(X=1)\\
#     &=& p^2 (1-p) + (1-p)^2 p\\
#     &=& p^2-p^3 + p - 2p^2 +p^3\\
#     &=& p-p^2\\
#     &=& p(1-p).\end{aligned}$$
# 
# 2.  Dans ce cas, la variable aléatoire $X$ est continue et a pour
#     densité la fonction $$f_X(x)  = \left\lbrace\begin{array}{ll}
#     1/(2-1)=1\text{ si }x \text{ est dans l'intervalle }[0,1],\\
#     0 \text{ sinon.}
#     \end{array}\right.$$ Ainsi, d’après la définition du cours :
#     $$\begin{aligned}
#     \mathbb{E}[X] = \int_{-\infty}^{+\infty}xf_X(x){\rm d}x &=& \int_{1}^{2} x {\rm d}x\\
#     &=& \frac{1}{2}[x^2]_1^2 = \frac{4}{2} - \frac{1}{2} = \frac{3}{2}. \end{aligned}$$
#     Pour la variance, on applique la formule : $$\begin{aligned}
#     {\rm Var}[X] &=& \int_{-\infty}^{+\infty}(x-\mathbb{E}[X])^2f_X(x){\rm d}x\\
#     &=& \int_{1}^{2} \left(x-\frac{3}{2}\right)^2  {\rm d}x\\
#     &=& \int_{1}^{2} x^2-3x+\frac{9}{4} {\rm d}x\\
#     &=& \left[\frac{1}{3}x^3 - \frac{3}{2}x^2 + \frac{9}{4}x\right]_1^2\\
#     &=& \frac{1}{12} \end{aligned}$$
# 
# **Exercice 2**. (\*\*) Soit $X$ une variable aléatoire. Calculer la
# fonction de répartition de $X$ lorsque :
# 
# 1.  $X \sim \mathcal{U}([a,b])$
# 
# 2.  $X\sim \mathcal{E}(\lambda)$  
# 
# *Corrigé 2*. D’après la définition du cours, on sait que la fonction de
# répartition de $X$ est la fonction $F_X$ donnée par :
# $$F_X(x) = \mathbb{P}(X\leqslant x),$$ pour tout $x$ appartenant à
# $\mathbb{R}$.
# 
# 1.  Par définition, puisque $X$ est une v.a. continue :
#     $$F_X(x) = \mathbb{P}(X\leqslant x)=\int_{-\infty}^x f_X(y) {\rm d}y,$$
#     ou $f_X$ est la densité de $X$. Et puisque $X$ suit une loi uniforme
#     sur $[a,b]$
#     $$\int_{-\infty}^x f_X(y) {\rm d}y = \left\lbrace\begin{array}{lll}
#     0, \text{ si } x\leqslant a\\
#     \int_{a}^x f_X(y) {\rm d}y = (x-a)(b-a)\text{ si } a<x<b\\
#     1 \text{ sinon.}
#     \end{array}
#     \right.$$
# 
# 2.  Par définition de la fonction de répartition et puisque $X$ suit une
#     loi exponentielle de paramètre $\lambda$ :
#     $$F_X(x) = \int_{-\infty}^x f_X(y) {\rm d}y = \lim_{a\to -\infty} \int_a^x \lambda e^{-\lambda y} {\rm d}y = 1-e^{-\lambda x}.$$
# 
# **Exercice 3**. (\*) Madame Michel et Monsieur Boulanger vont chaque
# semaine au marché hebdomadaire. Madame Michel arrive à une heure
# aléatoire entre 8h et 12h et elle reste 30 minutes ; on suppose que son
# heure d’arrivée suit une loi uniforme. Monsieur Boulanger arrive à 10h
# pile et reste également 30 minutes. Quelle est la probabilité pour
# qu’ils se trouvent ensemble au marché à un certain moment ?
# 
# *Corrigé 3*. Il faut que Mme Michel arrive entre 9h30 et 10h30.
# Intervalle de temps d’1h sur 4h, donc proba = 1/4.
# 
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
# 
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
# 
# **Exercice 6**. (\*) La variable aléatoire $X$ suit la loi normale
# $N(12,4)$. Calculer:
# $$P(X\leqslant 15), \qquad P(X\geqslant 18), \qquad P(X\geqslant 7), \qquad P(X\leqslant 9), \qquad P(8\leqslant X\leqslant 17).$$
# 
# **Exercice 7**. (\*) Une machine produit des rondelles métalliques en
# grande série. Une rondelle est acceptée si son diamètre extérieur est
# compris entre 21,9 et 22,1 mm. On suppose que sur l’ensemble de la
# production le diamètre extérieur des rondelles est une variable
# aléatoire X suivant la loi normale de moyenne $m$ = 22 mm et
# d’écart-type $\sigma$ = 0,05 mm. Quelle est la probabilité qu’une pièce
# soit refusée ?
# 
# **Exercice 8**. (\*) Le nombre de clients d’un magasin suit chaque
# samedi une loi normale $N(365,30)$. Quelle est la probabilité pour qu’il
# y ait un samedi donné:
# 
# 1.  plus de 400 clients ?
# 
# 2.  moins de 300 clients ?
# 
# 3.  entre 320 et 380 clients ?
# 
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
# 
# *Corrigé 4*.
# 
# 1.  On désigne par.
# 
#     Dans cet exercice on considère $n=20$ individus. On les numérote de
#     $1$ à $n$ et on note $X_i$ la variable aléatoire représentant le
#     poids de la $i$ème personne. Par hypothèse, cette v.a. suit une loi
#     normale de paramètre $\mu =60$ et $\sigma=15$. On cherche à calculer
#     la probabilité que le poids de ces 20 individus soit supérieur à
#     2200kg, i.e. on considère la variable aléatoire
#     $X = \sum_{i=1}^{20} X_i$ et on cherche la probabilité que $X$ soit
#     supérieur à 2200kg :
#     $$\mathbb{P}\left(\sum_{i=1}^{20} X_i \geqslant 2200 \right).$$
# 
#     Puisque les $X_i$, $1\leqslant i \leqslant 20$ sont i.i.d., on sait
#     que $\sum_{i=1}^{20} X_i$ suit une loi normale d’espérance $60n$ et
#     de variance,$15^2n$. Ainsi, si $Z$ désigne une v.a de loi normale
#     centrée réduite $$\begin{aligned}
#     \mathbb{P}\left(\sum_{i=1}^{20} X_i \geqslant 2200 \right) &=& \mathbb{P}\left(15\sqrt{n}Z+60n \geqslant 2200 \right) \\
#     &=& \mathbb{P}\left(Z \geqslant(2200-60n)/(15\sqrt{n}) \right)\\
#     &=& \mathbb{P}\left( Z \geqslant 14.9 \right) = 1-\mathbb{P}\left( \mathcal{N}(0,1) < 14.9 \right).\end{aligned}$$
# 
# 2.  Notons $N$ le nombre maximum de personne pouvant rentrer dans
#     l’ascenseur de sorte que celui-ci ne soit en surcharge qu’avec une
#     probabilité inférieure à $\alpha = 0,01$. En suivant le même
#     raisonnement qu’à la question précédente, on en déduit que $N$ est
#     tel que:
# 
#     $$\mathbb{P}\left(\sum_{i=1}^N X_i \geqslant 2200 \right) \leqslant\alpha. \quad (1)$$
#     L’idée est à nouveaux de faire apparaître la loi normale centrée
#     réduite. On sait que si $$X \sim \mathcal{N}(m,\sigma^2)$$ alors
#     $$\sum_{i=1}^N X_i \sim \mathcal{N}(Nm,N\sigma^2).$$ Par conséquent,
#     $$\frac{\sum_{i=1}^N X_i - Nm}{\sqrt{N}\sigma} \sim \mathcal{N}(0,1).$$
#     En remplaçant dans $(1)$, on en déduit que $N$ est solution de:
# 
#     $$\begin{aligned}
#     &&\mathbb{P}\left(\frac{\sum_{i=1}^N X_i - Nm}{\sqrt{N}\sigma} \geqslant(2200-Nm)/\sqrt{N}\sigma \right) \leqslant\alpha \\
#     &&\Leftrightarrow \mathbb{P}\left( \mathcal{N}(0,1) \geqslant(2200-Nm)/\sqrt{N}\sigma \right) \leqslant\alpha.\end{aligned}$$
# 
#     Notons $t(\alpha,N):= (2200-Nm)/\sqrt{N}\sigma$. $t(\alpha,N)$ est
#     donc tel que:
# 
#     $$\mathbb{P}\left( \mathcal{N}(0,1) \geqslant t(\alpha,N) \right) \leqslant\alpha \Leftrightarrow \mathbb{P}\left( \mathcal{N}(0,1) \leqslant t(\alpha,N) \right) \geqslant 1-\alpha.$$
#     Cette valeur ($x$), peut être lue dans la table de la loi normale
#     $(t(\alpha,N)=x)$. $N$ est donc la partie entière inférieure (on
#     cherche le nombre maximum de personnes) de la solution “$x$” de
#     l’équation: $$(2200-xm) =\sqrt{x}\sigma.$$ En posant $m=60$,
#     $\sigma^2 =15$, on en déduit $N$.
# 
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
# 
# *Corrigé 5*.
# 
# 1.  L’énoncé suggère que le poids en grammes des paquets est une
#     variable aléatoire qui suit une loi normale d’espérance 500 et
#     d’écart-type 25. Soit $X$ la variable aléatoire correspondante, et
#     $Y=(X-500)/25$.
# 
# 2.  $P(480\leqslant X\leqslant 520)=P(|Y|\leqslant 0,8)=0,576.$ On
#     s’attend donc à ce que, sur 1000 paquets, il y en ait 576 dont le
#     poids est compris entre 480g et 520g.
# 
# 3.  $$\begin{aligned}
#     P(480\leqslant X\leqslant 490)&=&P(-0,8\leqslant Y\leqslant-0,4)\\
#     &=&P(0,4\leqslant Y\leqslant 0,8)\\
#     &=&p(Y\leqslant 0,8)-p(Y\leqslant 0,4)=0,1327.\end{aligned}$$ On
#     s’attend donc à ce que, sur 1000 paquets, il y en ait 132 dont le
#     poids est compris entre 480g et 490g.
# 
# 4.  $P(450\leqslant X)=0,5+P(0\leqslant Y\leqslant 2)=0,5+\frac 12 P(-2\leqslant Y\leqslant 2)=0,5+0,4772=0,9772.$
#     On s’attend donc à ce que, sur 1000 paquets, il y en ait 977 dont le
#     poids est supérieur à 450g.
# 
# 5.  Il faut trouver $t$ tel que $p(|Y|<t)=0,9$. La table donne
#     $t=1,645$, puis $a=25t=41$. Par conséquent, environ 90% de la
#     production a un poids compris entre $500-41=459$g et $500+41=541$g.
# 
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
# 
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
