#Matrice de changement de base
import numpy as np
from scipy import linalg

'''
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