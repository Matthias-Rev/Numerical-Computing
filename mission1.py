#Matrice de changement de base
import numpy as np
from scipy import linalg

'''
Enoncé:
• NC101 – Understand what is numerical computing (+1)
• PP401 – Numpy to represent multidimensional arrays and perform operations with them
(+1)

1. Install SciPy on your computer.
2. Write your own variant of the Hello World program, compile it and run it.
3. Explain to the teacher how you compiled and run your program and how it is working.
-----------------------------------------------------------------------------------------------

Fonction Hello World, est une matrice de changement de base qui utilise l'équation apprise en outil math
s étant la matrice de changement de coordonnées
On effectue son inverse qu'on multiplie par la matrice utilisé en paramètre
ce qui nous return la matrice dans la nouvelle base
'''

def HelloWorld(matrix):
    s=np.matrix([[1,1,1],[2,-1,-1],[1,2,-1]])
    s_prime=linalg.inv(s)
    return s_prime*matrix

print(HelloWorld([[3],[0],[2]]))