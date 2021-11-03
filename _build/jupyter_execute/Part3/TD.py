#!/usr/bin/env python
# coding: utf-8

# # Travaux Dirigés
# 
# ## Partie 1
# 
# **Exercice 1**. (\*) L’ancien système d’immatriculation français était
# le suivant: chaque plaque avait 4 chiffres suivis de 2 lettres, puis des
# deux numéros du département. Les nouvelles plaques françaises sont
# formées de la façon suivante: elles comportent deux lettres, puis 3
# chiffres, puis 2 lettres. Il n’y a plus d’indication de département, le
# nouveau système étant national.  
# 
# 1.  Combien un département pouvait-il immatriculer de véhicules dans
#     l’ancien système ?
# 
# 2.  En supposant que la France a 101 départements, combien pouvait-on
#     immatriculer de véhicules ?
# 
# 3.  Combien le nouveau système permet-il d’immatriculer de véhicules ?
# 
# 4.  Proposer une explication au fait que le nouveau système reste
#     avantageux malgré tout.
# 
# 5.  En réalité dans le nouveau système comme dans l’ancien, certaines
#     combinaisons sont interdites pour éviter une confusion dans les
#     procès-verbaux: les I, O et U du fait de leur trop proche
#     ressemblance avec le 1, le 0 et le V, ainsi que les séries SS et WW
#     du bloc de gauche et la série SS du bloc de droite. Par ailleurs les
#     séries de chiffrent ne commencent pas à 000 mais démarrent à 001.  
#     Quel est, en procédant à ces ajustements, le nouveau nombre de
#     plaques réalisables en France avant que le nombre de combinaisons de
#     plaques soit épuisé ?  
# 
# 6.  Proposer une estimation (grossière) de la durée de vie de ce nouveau
#     système.  
# 
# **Exercice 2**. (\*) Quatre personnes participent à une course. Combien
# peut-il y avoir de classements possibles, en admettant qu’il puisse y
# avoir des ex-aequo ?
# 
# **Exercice 3**. (\*) Si $30$ personnes sont présentes à un réveillon et
# si, à minuit, chaque personne fait une bise à chacune des autres
# personnes, combien de bises se sont échangées en tout ?
# 
# **Exercice 4**. (\*) Un QCM comporte $10$ questions, pour chacune
# desquelles $4$ réponses sont proposées, une seule est exacte. Combien y
# a-t-il de grilles-réponses possibles? Quelle est la probabilité de
# répondre au hasard au moins à $6$ questions correctement?
# 
# **Exercice 5**. (\*) Amédée, Barnabé, Charles tirent sur un oiseau; si
# les probabilités de succès sont pour Amédée : $70$%, Barnabé : $50$%,
# Charles : $90$%, quelle est la probabilité que l’oiseau soit touché ?
# 
# **Exercice 6**. (\*\*\*) On se pose la question suivante: "Combien de
# personnes doit-on réunir pour que la probabilité que deux d’entre elles
# au moins possèdent la même date d’anniversaire dépasse 50 % ?" On
# négligera les années bissextiles.
# 
# 1.  Donner la réponse qui vous vient naturellement à l’esprit sans
#     calcul.
# 
# 2.  Soit $n$ le nombre de personnes présentes, qu’on suppose inférieur
#     à 365. Dénombrer le nombre de cas possibles de répartition des dates
#     d’anniversaires dans toute l’assemblée.
# 
# 3.  Dénombrer maintenant le nombre de cas de figures où toutes les
#     personnes présentes ont une date d’anniversaire différente.
# 
# 4.  Conclure en répondant à la question initiale.  
#       
#     *Indication: Il est probable que la calculatrice ne puisse pas
#     effectuer tel quel le calcul. Un tableur en revanche le fait bien
#     jusqu’à $n=100$ environ, à condition d’utiliser les bonnes
#     formules.*  
# 
# **Quelques formules sous Excel** Soit un ensemble à $n$ éléments.  
# 
# $$\begin{array}{|l|c|l|}
# \hline
# & \text{Formule}&\text{Formule Excel}\\
# \hline
# &&\\
# \text{Le nombre de permutations de ces élements} & n! & \text{=FACT(n)}\\
# &&\\
# \hline
# &&\\
# \text{Le nombre d'arrangements de k éléments parmi n} & A_n^k=\dfrac{n!}{(n-k)!} & \text{=PERMUTATION(n;k)}\\
# &&\\\hline
# &&\\
# \text{Le nombre de combinaisons de k éléments parmi n} & C_n^k=\dfrac{n!}{k!(n-k)!} & \text{=COMBIN(n;k)}\\
# &&\\
# \hline
# \end{array}$$
# 
# ## Partie 2
# 
# 
# **Exercice 1**. (\*) Un quart d’une population a été vaccinée. Si on est
# vacciné, on tombe malade avec une probabilité de $\frac{1}{20}$. Parmi
# les malades, il y a 4-non vaccinés pour 1 vacciné.  
# Quelle est la probabilité pour un non-vacciné de tomber malade ?  
# 
# **Exercice 2**. (\*) On considère une maladie dont est atteinte 1% de la
# population.  
# Si on est malade, on a une chance sur deux de mourir. Il existe un
# traitement contre la maladie, qui fait qu’un individu malade et traité
# n’a plus que 10% de chances de mourir.  
# Le test de dépistage permet de détecter 80% des malades, mais désigne
# aussi à tort 3% de personnes saines. Or si une personne saine est
# traitée, elle meurt dans 2% des cas.  
# 
# 1.  Si on n’effectue aucun test de dépistage, quelle est la probabilité
#     de mourir de cette maladie ?
# 
# 2.  On décide de procéder à un dépistage généralisé et à un traitement
#     des individus désignés comme malades.  
#     Quelle est la probabilité de mourir dans ce cas ? (que ce soit à
#     cause de la maladie ou du traitement)  
# 
# **Exercice 3**. (\*\*\*) Une source d’informations émet un message sous
# forme de "0" ou de "1" avec des probabilités respectives $p_{0}=0,3$ et
# $p_{1}=0,7$.  
# On souhaite transmettre ce message vers le récepteur par une liaison
# $A$. Cette liaison, à cause de défauts, transmet le contraire du message
# avec une probabilité d’erreur $q_{A}=10^{-7}$.  
# Pour diminuer cette probabilité d’erreur, on considère alors le système
# suivant:  
# Les messages sont maintenant tranmis vers un récepteur par 2 canaux
# distincts $A$ et $B$. On suppose que les deux liaisons sont
# indépendantes et que les probabilités d’erreur sur chacune de ces
# liaisons sont respectivement $q_{A}=10^{-7}$ et $q_{B}=2.10^{-7}$ (quel
# que soit le message émis).  
# 
# 1.  A un instant donné, le récepteur reçoit "0" sur le premier canal et
#     "1" sur le second. On demande de **décider** quel était le message
#     émis, en choisissant celui dont la probabilité d’émission sachant le
#     résultat à la réception (sur les 2 canaux) est maximale. (C’est la
#     méthode dit du *maximum a posteriori*.)
# 
# 2.  Etablir une règle de décision par la méthode du maximum a posteriori
#     pour toutes les configurations possibles en réception: autrement
#     dit, que décider dans les cas suivants ?
# 
#     -   0 reçu sur $A$, 0 reçu sur $B$.
# 
#     -   0 reçu sur $A$, 1 reçu sur $B$.
# 
#     -   1 reçu sur $A$, 1 reçu sur $B$.
# 
#     -   1 reçu sur $A$, 0 reçu sur $B$.
# 
# 3.  Calculer approximativement la probabilité d’erreur globale de cette
#     règle de décision. Quelle conclusion en tirer ?
#     
# ## Partie 3
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
#     
# ## Partie 4
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
# **Exercice 2**. (\*\*) Soit $X$ une variable aléatoire. Calculer la
# fonction de répartition de $X$ lorsque :
# 
# 1.  $X \sim \mathcal{U}([a,b])$
# 
# 2.  $X\sim \mathcal{E}(\lambda)$  
# 
# **Exercice 3**. (\*) Madame Michel et Monsieur Boulanger vont chaque
# semaine au marché hebdomadaire. Madame Michel arrive à une heure
# aléatoire entre 8h et 12h et elle reste 30 minutes ; on suppose que son
# heure d’arrivée suit une loi uniforme. Monsieur Boulanger arrive à 10h
# pile et reste également 30 minutes. Quelle est la probabilité pour
# qu’ils se trouvent ensemble au marché à un certain moment ?
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
