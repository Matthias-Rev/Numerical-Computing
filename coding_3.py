import matplotlib.pyplot as plt
import numpy as np
import csv
liste_data=[]
liste_label=[]
jour=0
x=0

'''
Dans cet exo:
y-axis -> Nombre de personnne sous aide respiratoire
x-axis -> Nombre de jour passée depuis le début de l'épidemie
Je l'ai dessiné en "nuage de point", sa forme est proche d'une courbe donc j'ai décidé d'utiliser polyfit
Qui va représenter une fonction polynomial, j'ai lu sur mathworks que il est idéal de prendre un ordre égal à n-1
donc un polynome d'ordre 84
'''

with open('COVID19BE_HOSP.csv') as file:
    csv_file=csv.DictReader(file)
    for row in csv_file:
        dictionnary=dict(row)
        if dictionnary['REGION']=='Brussels':
            jour+=1
            x+=1
            liste_label.append(x)
            liste_data.append(int(dictionnary['TOTAL_IN_RESP']))
            

#Draw the scatterplot
plt.style.use('seaborn')
plt.scatter(liste_label, liste_data, edgecolors='black')
plt.title('Nombre de personne sous aide-respiratoire à Bruxelles durant la crise du Covid19')
plt.xlabel("Jour de l'épidemie")
plt.ylabel('Nombre de personnne sous aide respiratoire')

#Polyfit
p = np.polyfit(np.array(liste_label), np.array(liste_data), 84)
polit=np.poly1d(p)
plt.plot(np.array(liste_label), polit(np.array(liste_label)), color='red')
print(np.poly1d(p))


#All screen
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.tight_layout()
plt.show()
plt.close()