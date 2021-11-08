#!/usr/bin/env python
# coding: utf-8

# # Analyse Rapide des notes - DSC1

# In[1]:


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


df=pd.read_csv("Notes_DSC1.csv", encoding="latin-1")


# In[8]:


df.describe()


# In[9]:


df['Note']=df["Note"]*100/20


# In[10]:


df['Exo1'] = df['Exo1']*100/5
df['Exo2'] = df['Exo2']*100/8
df['Exo 3'] = df['Exo 3']*100/7


# In[11]:


df["Note"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes",xTitle='Notes sur 100', yTitle='Quantité')


# In[12]:


df["Exo1"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exercice 1 - Calculs matriciel",xTitle='Notes sur 100', yTitle='Quantité')


# In[13]:


df["Exo2"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 2 - Géométrie",xTitle='Notes sur 100', yTitle='Quantité')


# In[14]:


df["Exo 3"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 3 - Matrices, inversion",xTitle='Notes sur 100', yTitle='Quantité')

