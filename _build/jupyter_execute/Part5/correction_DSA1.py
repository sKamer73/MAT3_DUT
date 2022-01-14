#!/usr/bin/env python
# coding: utf-8

# # Correction rapide - DSA1

# ## Exercice 1

# **Question 1:** 0.5 +1 +0.5 +0.5

# In[2]:


import numpy as np
A = np.array([[1,1,0],[0,1,1],[0,0,1]])
rez1 = 2*np.identity(3)+A
print("A+2I_3 = ",rez1)
B=A-np.identity(3)
rez2 = rez1-np.transpose(B)
print( "(A+2I_3-transpose(B))*B = ", rez2.dot(B))
print("B² = ", B.dot(B))
print("B^3 = ", B.dot(B.dot(B)))


# **Question 2:** 0.5+0.5

# $B=A-I_3$. Donc: $AB = A(A-I_3) = A²-A = (A-I_3)*A = BA$

# **Question 3:**
# 
# On a vu que $B^3=0$. On en déuit que $B^n = 0$ pour tout n>=3. De plus, on connaît $B$ et $B^2$ de la question 1. En développant avec le binôme de Newton, comme on sait que $B$ et $I_3$ commutent, on a : $A^n = (B+I_3)^n = \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix} B^k \times I_3^{n-k} = \begin{pmatrix} n \\ 0 \end{pmatrix} I_3 + \begin{pmatrix} n \\ 1 \end{pmatrix} B + \begin{pmatrix} n \\ 2 \end{pmatrix}B^2$. Ce qui donne: $A^n = \begin{pmatrix} 1 & n & \frac{n(n-1)}{2} \\ 0&1&n \\ 0&0&1 \end{pmatrix} $

# ## Exercice 2:

# **Question a:**

# In[3]:


from math import sqrt
n = np.array([1,2,3])
d = np.array([2,0,-2])
AC = np.array([0-2,2-0,-1-(-2)])
AB = np.array([2-2,3-0,-1-(-2)])
print("n.d = ", n.dot(d) )
print(" n vectorielle AC = ", np.cross(n,AC) ) 
print(" Norme de AB = ", np.linalg.norm(AB), " = sqrt(10) = ", sqrt(10))


# **Question b:**

# In[4]:


normalP = np.cross(AB,AC)
print("Normal à P:", normalP)


# On en déduit l'équation du plan: $\vec{AM} \cdot \vec{n} = 0 \implies \begin{pmatrix} x-2 \\ y \\ z+2 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ -2 \\ 6 \end{pmatrix} = 0 \implies (x-2)-2y+6(z+2) = 0 \implies x-2y+6z = -10$ 

# **Question c:**
# 
# On prend un point M(x,y,z) sur la droite, alors ce point vérifie: $\vec{BM} \wedge \vec{d} = \vec{0}$, ce qui donne: $\begin{pmatrix} -2(y-3) \\ 2(x-2)+2(z+1) \\ -2(y-3) \end{pmatrix} = \vec{0}$. On voit que la première et la dernière coordonnée nous donnent la même équation. Le système cartésien s'écrit alors: 
# $\left\lbrace\begin{array}{lll}
# y = 3\\
# x+z = 1
# \end{array}\right.$

# **Question d:**
# 
# On unit alors les deux systèmes, ce qui donne: 
# $\left\lbrace\begin{array}{lll}
# x-2y+6z = -10\\
# y = 3 \\
# x+z = 1
# \end{array}\right.$

# La matrice associée A s'écrit alors: $A = \begin{pmatrix} 1&-2&6 \\ 0&1&0 \\ 1&0&1 \end{pmatrix}$ et la matrice $Y = \begin{pmatrix} -10 \\ 3 \\ 1 \end{pmatrix}$

# **Question e:**
# i. Cela s'écrit: $\vec{DM} \cdot \vec{d} = 0 \implies \begin{pmatrix} x-1 \\ y+2 \\ z-5 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ 0 \\ -2 \end{pmatrix} = 0 \implies 2(x-1)-2(z-5) = 0 \implies x-z = -4$

# ii. On utilise la condition d'appartenance à la droite par le système cartésien et on y ajoute l'équation correspondant à la condition de perpendicularité. Cela donne:
# 
# $\left\lbrace\begin{array}{lll}
# x-z = -4\\
# y = 3 \\
# x+z = 1
# \end{array}\right.$
# 
# Ce qui se résout en $\left\lbrace\begin{array}{lll}
# x = -\frac{2}{3}\\
# y = 3 \\
# z = \frac{5}{3}
# \end{array}\right.$
# 
# On en déduit que le point de coordonnées $M(-\frac{2}{3},3,\frac{5}{3})$ donne une droite $(DM)$ perpendiculaire à $\mathcal{D}$.

# ## Exercice 3

# **Question a:**

# $det(A) = -5$ (développement en ligne sur la ligne du milieu)
# 
# **Question b:**
# 
# $A^{-1} = \frac{1}{7} \begin{pmatrix} 1 & -2 & 6 \\ 0 & 5 & 0 \\ 1 & 2 & -1 \end{pmatrix} $

# In[ ]:





# In[6]:


A = np.array([[1,-2,6],[0,1,0],[1,0,1]])
Am1 = np.array([[-1,-2,6],[0,5,0],[1,2,-1]])/5
print(np.linalg.inv(A))


# **Question c:**
# 
# C'est la matrice de l'exercice 2, par conséquent le point d'interception est le point B. D'où: $Y = \begin{pmatrix} 2 \\ 3 \\ -1 \end{pmatrix} $

# **Bonus**:
# 
# On écrit le système donné par $AB=BA$, et on résoud. Cela donne:
# 
# $AB = \begin{pmatrix} ac +be & ad+bf \\ ae & af \end{pmatrix} = BA = \begin{pmatrix} ac & bc+ad \\ bc+ad & be+af \end{pmatrix}$

# De la coordonnée en (1,1) on déduit que $be = 0 \implies e = 0$ car $b$ est non nul et de la coordonnée en (1,2) on déduit que $f=c$. D'où la matrice $B = \begin{pmatrix} c & d \\ 0 & c \end{pmatrix}$
