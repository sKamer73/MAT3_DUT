#!/usr/bin/env python
# coding: utf-8

# IUT de Chambéry - 2 année GCCD 2017-2018  
#   
# 
# **Exercice 1**. (\*) A chaque expérience aléatoire proposée, déterminer
# son ensemble des évènements élémentaires possibles $\Omega$, ainsi la
# variable aléatoire choisie.
# 
# 1.  On tire deux dés et on observe leur somme.
# 
# 2.  On répond au hasard à un QCM où chaque question donne 4 choix, dont
#     un seul est bon, et on observe, pour une question, le résultat du
#     nombre de points obtenus, en sachant que:
# 
#     1.  Une réponse juste rapporte 1 point
# 
#     2.  Une réponse fausse enlève 0,5 point
# 
# 3.  On observe maintenant le résultat du test QCM présenté plus haut,
#     sachant qu’il y a 20 questions.  
# 
# **Exercice 2**. (\*\*) Reprendre l’exercice précédent en calculant cette
# fois-ci la loi de probabilité de la variable aléatoire, ainsi que son
# espérance.  
# 
# **Exercice 3**. (\* à \*\*\*) En utilisant les définitions du cours,
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
# **Exercice 4**. (\*\*) Soit $X$ une variable aléatoire. Calculer la
# fonction de répartition de $X$ lorsque :
# 
# 1.  $X \sim \mathcal{U}([a,b])$
# 
# 2.  $X\sim \mathcal{E}(\lambda)$  
# 
# **Exercice 5**. (\*) On lance 7 fois une pièce équilibré. On note
# modélise par la variable aléatoire $X_i$ le résultat du $i$-ème lancé.
# 
# 1.  Donner la loi de la variable aléatoire $X_i$.
# 
# 2.  Donner la loi de la variable aléatoire $X_1+\ldots+X_7$.
# 
# 3.  En déduire la probabilité qu’il y ait plus de pile que de face.  
# 
# **Exercice 6**. (\*) Une entreprise fabrique des pièces pour l’industrie
# automobile. Après une réorganisation de l’atelier, le taux de pièces
# défectueuses est tombé à 1%. Calculer la probabilité d’avoir moins de 15
# pièces défectueuses sur un lot de 1000.  
# 
# **Exercice 7**. (\*) Dans une usine de fabrication d’emballage, on
# considère que 3% sont défectueux. Le fabricant doit livrer une série de
# 60 pièces à un de ses particulièrement pointilleux : dès que le nombre
# de produits défectueux livrés est supérieur à 2, il doit donner une
# indemnité forfaitaire de $x$ euros.
# 
# 1.  En utilisant une modélisation de type succès-échec, donner la
#     probabilité que la série contienne plus de deux pièces
#     défectueuses<span id="q1" label="q1">\[q1\]</span>
# 
# 2.  Sachant qu’il doit vendre la série 1000 euros, calculer l’espérance
#     du gain du fabricant
# 
# 3.  En faisant effectuer une manipulation par un technicien spécialisé,
#     le fabricant sait qu’il peut à coup sûr produire une série de 100
#     pièces en bon état. Sachant que l’intervention lui coûte 200 euros,
#     à partir de quelle pénalité $x$ a-t-il intérêt à faire se déplacer
#     le technicien ?
# 
# 4.  On note $Y$ la variable aléatoire qui, à chaque lot de 60 pièces,
#     associe le nombre d’emballage défectueux. Reprendre la question
#     <a href="#q1" data-reference-type="eqref" data-reference="q1">[q1]</a>
#     en supposant que $Y\sim \mathcal{P}(60\times 0.03)$ et commenter.  
# 
# **Exercice 8**. (\*) Un standard téléphonique reçoit en moyenne 2 appels
# par minute. Les appels sont répartis au hasard dans le temps.
# 
# 1.  Quelle est la loi de probabilité régissant le nombre d’appels reçus
#     en 3 minutes ? Quelle est la probabilité qu’il n’y ait aucun appel
#     en 3 minutes ?
# 
# 2.  Quelle est la probabilité que le nombre d’appels en 2 minutes soit
#     supérieur ou égal à 5 ?
# 
#   
# 
# **Exercice 9**. (\*) Dans une population, le poids des individus est une
# variable aléatoire suivant une loi normale de moyenne égale à 60 kg et
# un écart-type égal à 15 kg. Un ascenseur a une capacité égale à 2200 kg.
# Calculer :
# 
# 1.  La probabilité que 20 individus pèsent ensemble plus de 2200 kg.
# 
# 2.  Le nombre maximum de personnes pouvant rentrer dans l’ascenseur de
#     sorte que celui-ci ne soit en surcharge qu’avec une probabilité
#     inférieure à 0,01.
