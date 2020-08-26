import csv
import matplotlib.pyplot as plt
import numpy as np

'''
Enoncé:
• NC101 – Understand what is numerical computing (+1)
• PP401 – Use Numpy to represent multidimensional arrays and perform operations with them
(+1)
• PP411 – Draw a simple plot representing data with Matplotlib

1. Select a dataset and imagine the visualisation you want to build from it (line plot, scatter,
histogram, etc.)
2. Write and test a program that reads the dataset and create the plot with Matplotlib.
3. Explain to the teacher how you designed your code and make a demonstration.

In this coding assessment, you have to use the Matplotlib module to draw a plot to visualise data. You
have to use a dataset from the The Belgian Open Data Initiative portal (https://data.gov.be/en). For
example, you may want to plot the evolution of the number of accidents in 2018 1 with time.

--------------------------------------------------------------------------------------------------

Pour cette mission j'ai décidé de représenter un graphique lié avec notre triste situation sanitaire
L'axe des y représentant les semaines depuis le début de la pandémie
L'axe des x , le Nombre de personne sous aide-respiratoire
'''


liste_data=[]
liste_label=[]
fig, ax=plt.subplots()
moyenne=0
jour=0
x=0

with open('COVID19BE_HOSP.csv') as file:
    csv_file=csv.DictReader(file)
    for row in csv_file:
        dictionnary=dict(row)
        if dictionnary['REGION']=='Brussels':
            moyenne+=int(dictionnary['TOTAL_IN_RESP'])
            jour+=1
            if jour ==7:
                x+=1
                jour=0
                liste_data.append(round(moyenne/7, 2))
                liste_label.append('Semaine{}'.format(x))


ax.set_title("Nombre de personne sous aide-respiratoire à Bruxelles durant la crise du Covid19")
ax.set_xlabel("Nombre de personne sous aide respiratoire", fontsize=10)
index=np.arange(len(liste_label))
plt.tight_layout()

ax.barh(index, liste_data, align='center', color='green')
ax.set_yticks(index)
ax.set_yticklabels(liste_label)

#All screen
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()
plt.close()