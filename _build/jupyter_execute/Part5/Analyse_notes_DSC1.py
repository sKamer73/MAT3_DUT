#!/usr/bin/env python
# coding: utf-8

# # Analyse Rapide des notes

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


# ## Continus

# ### DS 1

# In[2]:


df=pd.read_csv("Notes_DSC1.csv", encoding="latin-1")


# In[3]:


df.describe()


# In[4]:


df['Note']=df["Note"]*100/20


# In[5]:


df['Exo1'] = df['Exo1']*100/5
df['Exo2'] = df['Exo2']*100/8
df['Exo 3'] = df['Exo 3']*100/7


# In[6]:


df["Note"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes",xTitle='Notes sur 100', yTitle='Quantité')


# In[7]:


df["Exo1"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exercice 1 - Calculs matriciel",xTitle='Notes sur 100', yTitle='Quantité')


# In[8]:


df["Exo2"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 2 - Géométrie",xTitle='Notes sur 100', yTitle='Quantité')


# In[9]:


df["Exo 3"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 3 - Matrices, inversion",xTitle='Notes sur 100', yTitle='Quantité')


# ### DS 2

# In[43]:


df=pd.read_csv("Notes_DSC2.csv", encoding="latin-1")


# In[44]:


df.describe()


# In[45]:


df['Note']=df["Note"]*100/20


# In[46]:


df['Exo1'] = df['Exo1']*100/7
df['Exo2'] = df['Exo2']*100/4
df['Exo 3'] = df['Exo 3']*100/4
df['Exo 4'] = df['Exo 4']*100/5


# In[47]:


df["Note"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes",xTitle='Notes sur 100', yTitle='Quantité')


# In[48]:


df["Exo1"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exercice 1 - Statistiques",xTitle='Notes sur 100', yTitle='Quantité')


# In[49]:


df["Exo2"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 2 - Dénombrement et probabilités conditionnelles",xTitle='Notes sur 100', yTitle='Quantité')


# In[50]:


df["Exo 3"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 3 - Loi binomiale",xTitle='Notes sur 100', yTitle='Quantité')


# In[51]:


df["Exo 4"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 4 - Loi normale",xTitle='Notes sur 100', yTitle='Quantité')


# ## Alternants

# ### DS 1

# In[14]:


df=pd.read_csv("Notes_DSA1.csv", encoding="latin-1")


# In[15]:


df.describe()


# In[16]:


df['Note']=df["Note"]*100/20


# In[17]:


df['Exo1'] = df['Exo1']*100/5
df['Exo2'] = df['Exo2']*100/8
df['Exo 3'] = df['Exo 3']*100/7


# In[18]:


df["Note"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes",xTitle='Notes sur 100', yTitle='Quantité')


# In[19]:


df["Exo1"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exercice 1 - Calculs matriciel",xTitle='Notes sur 100', yTitle='Quantité')


# In[20]:


df["Exo2"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 2 - Géométrie",xTitle='Notes sur 100', yTitle='Quantité')


# In[21]:


df["Exo 3"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 3 - Matrices, inversion",xTitle='Notes sur 100', yTitle='Quantité')


# ### DS 2

# In[53]:


df=pd.read_csv("Notes_DSA2.csv", encoding="latin-1")


# In[54]:


df.describe()


# In[55]:


df['Note']=df["Note"]*100/20


# In[56]:


df['Exo1'] = df['Exo1']*100/7
df['Exo2'] = df['Exo2']*100/4
df['Exo 3'] = df['Exo 3']*100/4
df['Exo 4'] = df['Exo 4']*100/5


# In[57]:


df["Note"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes",xTitle='Notes sur 100', yTitle='Quantité')


# In[58]:


df["Exo1"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exercice 1 - Statistiques",xTitle='Notes sur 100', yTitle='Quantité')


# In[59]:


df["Exo2"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 2 - Dénombrement et proba conditionnelles",xTitle='Notes sur 100', yTitle='Quantité')


# In[60]:


df["Exo 3"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 3 - Loi binomiale",xTitle='Notes sur 100', yTitle='Quantité')


# In[61]:


df["Exo 4"].iplot(kind="histogram", bins=20, theme="white", title="Répartition des notes - Exo 4 - Loi normale",xTitle='Notes sur 100', yTitle='Quantité')

