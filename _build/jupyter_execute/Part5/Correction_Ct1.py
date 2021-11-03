#!/usr/bin/env python
# coding: utf-8

# # Brève Correction - DSC1

# **Exercice 1:**

# In[1]:


import numpy as np
M=np.array([[2,1,0],[-3,-1,1],[1,0,-1]])
print("M²=",M.dot(M))
print("M^3=",M.dot(M.dot(M)))


# $ det(M^3) = det(M)^3 = 0 \implies det(M) = 0$

# In[2]:


I3=np.identity(3)
print(I3+M+M.dot(M))


# 3. $(I_3-M)*(I_3+M+M²)=I_3+M+M²-M*I_3-M*M-M*M² = I_3+M-M+M²-M²-M^3 = I_3$

# **Exercice 2:**

# a.1. $\vec{n}_1 \cdot \vec{n}_2 = 3*2+2*(-2)=2$
# 
# a.2. $ \vec{n}_1 \wedge \vec{AB} = \begin{pmatrix} 2 \\ -7 \\ -3 \end{pmatrix}$
# 
# a.3. $ ||\vec{AB}|| = ||  \begin{pmatrix} -2 \\ -1 \\ 1 \end{pmatrix} || = \sqrt{2²+1²+1²} = \sqrt{6}$

# b. $ \vec{n_1} \cdot \vec{AM} = 0 \implies 3*(x-1)+2*(z-2)=0 \implies 3x +2z = 7 $
# 
# $ \vec{n}_2 \cdot \vec{AM} = 0 \implies 2*(x-1) -2 * (z-2) = 0 \implies 2x-2z = -2 $ 

# c. $ \vec{n} = \vec{AB} \wedge \vec{AC} = \begin{pmatrix} 0 \\ -7 \\ -7 \end{pmatrix} $ 
# 
# $\vec{n} \cdot \vec{AM} = -7*(y+1)-7*(z-2) = 0 \implies y+1+z-2 = 0 \implies y+z = 1 $

# d. $(S) : \left\{ \begin{array}{l}  3x + 0y +2z = 7 \\  2x + 0y -2z =-2 \\  0x + y+z=1  \end{array} \right.$  
# En prenant: $A=\begin{pmatrix}
#     3&0&2\\
#     2&0&-2\\
#     0&1&1
#     \end{pmatrix}$  et $X = \begin{pmatrix} x \\ y \\ z \end{pmatrix} $ et $ Y = \begin{pmatrix} 7 \\ -2 \\ 1 \end{pmatrix}$

# e.i. L'équation paramètrique de la droite (BD) s'écrit sous forme vectoriel (et le système paramétrique sous forme d'un système). 
# Cela s'écrit de la manière suivante: $(BD) = \{ \text{points M tels que:}\vec{BM} = \lambda \vec{BD}, \lambda \in \mathbb{R} \}$
# 
# On peut préciser $\vec{BD} = \begin{pmatrix} a+1 \\ 0 \\ 2 \end{pmatrix}$, ce qui donne le système paramètrique suivante: soit $M(x,y,z)$ un point de (BD), alors le système suivant est vérifié:
# $(S) : \left\{ \begin{array}{l}  x = -1 + \lambda*(a+1) \\  y =-2 \\  z= 3 + 2*\lambda  \end{array} \right.$  

# e.ii. Il faut et il suffit que le vecteur directeur de la droite (BD) soit proportionelle au vecteur normale de $(P_1)$. Cela s'écrit alors: $\vec{BD} = \lambda \vec{n}_1$, $\lambda \in \mathbb{R}$. Cela donne le système suivant:
# 
# $(S) : \left\{ \begin{array}{l}  a+1 = 3 \lambda \\  0 = 0 \\  2=2 \lambda  \end{array} \right.$  
# 
# On obtient de la dernière équation que $\lambda = 1$ et de la première, on obtient que $a=2$.

# **Exercice 3**:
# 
# a. On peut soit calculer le déterminant, soit inverser la matrice et montrer qu'elle est inversible. Les résultats sont donnés ici directement (se référer au cours pour la méthode de calcul).

# In[6]:


import numpy as np
A=np.array([[3,0,2],[2,0,-2],[0,1,1]])
print("det(A)=",np.linalg.det(A))
print("A^(-1) = ", np.linalg.inv(A))


# c. On peut remarquer que les matrices correspondent par rapport à l'exercice 2. Or le point d'intersection des trois plans est forcément le point A (commun aux trois plans). Par conséquent, la solution du système est le point A.
