import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mprimg
from math import sqrt

'''
Pour cette mission j'ai décidé de faire plusieurs transformations sur une photo d'origine j'ai utilisé matplotlib ayant trouver plus d'info à son sujet:
1ère modification:
- je fais un dot product entre une matrice représentant un ton de gris et l'image du tigre pour "griser" celle-ci et crée un nouvelle image

2ème modification:
- On ne va afficher que les pixels qui dépassent une certaine valeur de 0 à 255, en fonction de la valeur l'image paraitra clair ou sombre

3ème modification:
-L'image négative de la photo original, pour avoir une photo négative il suffit d'inverser les valeurs des pilxels

4ème modification:
-On va afficher les pixels qui sont en dehors d'une fonction donnée ici un cercle
-On va crée une matrice aux dimensions de l'image grâce à ogrid
-distance: va englober tous les pixels à l'intérieur d'un cercle centrer au centre de l'image
-On va ensuite leurs données une valeur égal à zéro pour observer le cercle

5ème modification:
-on crée un drapeau belge à partir d'une matrice
-il suffit de déterminer les couleurs des pixels voulue ainsi que l'endroit ou ils se trouvent trouve dans la matrice
'''

img = imageio.imread('tiger.jpg')


#greyscale
img_copy2=img
rgb_weight=[0.2989,0.5870,0.1140]
gray_scale_image=np.dot(img_copy2[...], rgb_weight)
imageio.imwrite('tiger_transformeds.jpg',gray_scale_image)


#limiter les couleurs afficher
img_grise = imageio.imread('tiger_transformeds.jpg')
img_grises=(img_grise>=75)
plt.imshow(img_grises)
plt.show()

#Négatif
img_copy=img
img_negatif= 1-img_copy
plt.imshow(img_negatif)
plt.show()

##Cercle
total_rows, total_cols, layers= img.shape
x, y=np.ogrid[:total_rows, :total_cols]
distance=np.sqrt((x-(total_rows/2))**2 + (y-(total_cols/2))**2)
img_cercle= distance < total_rows/2
img[img_cercle]=0
plt.imshow(img)
plt.show()

#creat picture from numpy
rouge=[0.807, 0.066, 0.149]
jaune=[1,1,0]
noir=[0,0,0]

hauteur = 100
largeur= 2*hauteur

img_depart= np.zeros((hauteur, largeur,3))
img_depart[:,0:largeur//3]=noir
img_depart[:, largeur//3: 2*largeur//3]=jaune
img_depart[:, 2*largeur//3:largeur]=rouge
plt.imshow(img_depart)
plt.show()

imageio.imwrite('Belgium_Flag.png', img_depart)