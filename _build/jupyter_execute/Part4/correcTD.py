#!/usr/bin/env python
# coding: utf-8

# # Correction du TD de statistique via Python

# Définir un DataFrame (tableau 2D, bibliothèques Pandas) et le plotter avec CuffLinks permet de faire différents tracés statistiques très rapides, ainsi que leur analyse. Dans ce NoteBook, nous allons utiliser ces outils afin de répondre aux questions.

# In[1]:


#importation standars des librairies
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


# **Exercice 1:**
# 
# Il faut commencer par donner une valeur moyenne des intervalles de charge maximale. Cela est fait directement dans l'entrée des données ci-dessous.

# In[45]:


valeurs = [9.5,10,10.5,11,11.5,12,12.5,13]
nombres = [2,5,12,17,14,6,3,1]
dataForFrame = [[valeurs[k] for i in range(nombres[k])] for k in range(len(nombres))] #il est plus simple de créer une liste avec la charge répétée son nombre de fois
dataForFrame=sum(dataForFrame,[])
df=pd.DataFrame(data=[dataForFrame]).T #création d'un dataframe
df.columns=["Charge"] #on nomme les colonnes


# In[46]:


df.describe() #décrire le dataframe donne accès à toutes les informations
#mean:moyenne
#std: standard deviation = écart-type


# In[47]:


df2=pd.DataFrame(data=[valeurs,nombres]).T
df2.columns=["charge","nombres"]
df2["freq"]=df2["nombres"]/60*100
df2["freqCumul"]=df2["freq"]
for k in range(1,len(df2["freq"])):
    df2["freqCumul"][k]+=df2["freqCumul"][k-1]


# In[48]:


df2


# In[49]:


N = 60
print("Nombres de cables: ",N)


# On peut en déduire les déciles: le premier décile est pour la sixème valeur (10), le 9ème pour la 54ème valeur (12).

# 2. $C_v = \sigma/m = 0.74/11.09*100 = 6.67\%$

# In[50]:


fig=df.iplot(kind="histogram",xTitle="Charge",yTitle="Quantité",title="Histogramme",asFigure=True)
fig.update_layout(plot_bgcolor='White',paper_bgcolor="White")
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.show()


# In[51]:


fig=df.iplot(kind="box",yTitle="Charge",title="Diagramme Moustache",asFigure=True)
fig.update_layout(plot_bgcolor='White',paper_bgcolor="White")
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.show()


# **Exercice 2**:

# In[2]:


valeurs = [71.5,74.5,77.5,80.5,83.5,86.5,89.5,92.5,95.5]
nombres = [17,33,80,114,107,76,28,31,1]
dataForFrame = [[valeurs[k] for i in range(nombres[k])] for k in range(len(nombres))] #il est plus simple de créer une liste avec la charge répétée son nombre de fois
dataForFrame=sum(dataForFrame,[])
df=pd.DataFrame(data=[dataForFrame]).T #création d'un dataframe
df.columns=["Charge"] #on nomme les colonnes


# In[3]:


df.describe()


# In[5]:


5.08**2


# 1. La moyenne est de 82.09 MPa, et l'écart-type est de 5.32 MPa.

# In[54]:


fig=df.iplot(kind="histogram", title="Histogramme", xTitle = "Classe de résistance", yTitle = "Occurences", bins = 9,asFigure=True)
fig.update_layout(plot_bgcolor='White',paper_bgcolor="White")
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.show()


# 3. Cela ressemble à une loi gaussienne. On peut l'identifier à une loi gaussienne avec la même moyenne et écart-type, d'où: $B \sim N(82.08,5.32)$ avec $B$ la v.a. de la résistance du béton.

# 4. La résistance caractéristique doit être la moyenne (82.08), pour la classe de résistance je ne comprends pas.

# 5. On cherche: $P(B < 70)$. On adimensionnalise la v.a.: $B_a = \frac{B-82.08}{5.32}$, et on cherche donc: $P(B_a < -2.27) = 1-0.9884=0.0116$.
# 
# On cherche ensuite $P(B>90)=P(B_a>1.488)=1-0.9319=0.068$
# 
# Pour vérifier la cohérence, on multiplie la probabilité par le nombre d'éprouvettes totales, et l'on vérifie si l'on obtient des chiffres similaires au tableau: il y a 487 éprouvettes, on vérifie: $P(B<70)*487 = 5.6$, $P(B>90)*487 = 33$. 
# On voit que la loi n'est pas totalement adaptée: il y a plus d'éprouvettes en dessous de 70 que prévue par la loi de probabilité.

# **Exercie 3:**
# 
# Le signe donne la valeur montante ou descendante du nuage de points, alors que la proximité avec 1 de la valeur donne le degré de corrélation.

# On en déduit donc:
# 1. Signe positif: a,b. Plus forte corrélation en a donc 0.87 est associé à a, 0.73 à b. 
# 2. Signe négatif: c,d. Plus forte corrélation en c donc -0.7 est associé à c, -0.4 à d.

# **Exercice 4:**

# In[55]:


temps = [100,200,300,400,500,600,750,1000,1500]
R=[0.8,0.64,0.52,0.4,0.32,0.28,0.2,0.12,0.04]
df = pd.DataFrame(data=[temps,R]).T
df.columns=["t_i","R"]
fig=df.iplot(x="t_i",kind="scatter",mode="markers",title = "Question 1. Tracé du nuage de points",xTitle="$t_i$",yTitle="$R(t_i)$",asFigure=True)
fig.update_layout(plot_bgcolor='White',paper_bgcolor="White")
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.show()


# In[56]:


from math import log
df["y_i"]= list(map(log,df["R"]))
fig=df.iplot(x="t_i",y="y_i",mode="markers",title = "Question 2. Tracé du nuage de points avec logarithme",xTitle = "$t_i$",yTitle = "$ln(R(t_i))$",asFigure=True)
fig.update_layout(plot_bgcolor='White',paper_bgcolor="White")
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
fig.show()


# In[57]:


from scipy.stats import linregress
a, b, r, p_value, std_err = linregress(list(df["t_i"]), list(df["y_i"]))


# In[58]:


print("y(x) = ",a,"x",b)


# In[59]:


print("Coefficient de corrélation r = ",r)


# On en déduit que l'on peut bien approximer $ln(R(t))=y(t) = a*t+b$, d'où en passant à l'exponentielle: $R(t)=e^b*e^{at}=0.9709*e^{-0.002119*t}$

# 4. On calcule $R(900)$ à l'aide de la formule ci-dessus: $R(900)=0.144$
