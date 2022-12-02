import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.ticker import MaxNLocator 
from matplotlib.lines import Line2D 
#Python3 -m pip install -U scikit-learn


#data
point = [[0.,0.],[1.,0.],[2.,0.],[3.,0.],[4.,0.],[0.,1.],[1.,1.],[2.,1.],[3.,1.],[4.,1.],[0.,2.],[1.,2.],[2.,2.],[3.,2.],[4.,2.],[0.,3.],[1.,3.],[2.,3.],[3.,3.],[4.,3.],[0.,4.],[1.,4.],[2.,4.],[3.,4.],[4.,4.]]
cluster = [0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
x_point,y_point=[],[]
for i in range(len(point)):
    x_point.append(point[i][0])
    y_point.append(point[i][1])
x_min=min(x_point)-1.0
x_max=max(x_point)+1.0
y_min=min(y_point)-1.0
y_max=max(y_point)+1.0

#entrainement
#instanciation et définition du k (nb_classe<=k<=sqrt(nb_point entrainement))
k = 9
clf = neighbors.KNeighborsClassifier(k, weights='uniform')
clf.fit(point, cluster)


H = 0.1 # taille de la grille

x_axis_range = np.arange(x_min,x_max, H) #instance de ndarrayavec des valeurs régulièrement espacées 
y_axis_range = np.arange(y_min,y_max, H)
x_grille, y_grille = np.meshgrid(x_axis_range, y_axis_range) #création d'une grille rectangulaire

# Verification de la grille
#print('x_grille.shape:', x_grille.shape)
#print('y_grille.shape:', y_grille.shape)
#plt.scatter(x_grille, y_grille, s=0.5)
#plt.show()

point_grille = np.reshape(np.stack((x_grille.ravel(),y_grille.ravel()),axis=1),(-1,2)) #tableau numpy x y
print('xx.shape:', point_grille.shape)


# prédiction des points de la grille
prédiction_cluster = clf.predict(point_grille) 

# proba pour chaque point de la grille
proba_cluster = clf.predict_proba(point_grille) 
                               
# taille des points suivant proba
yy_size = np.max(proba_cluster, axis=1)

PROB_DOT_SCALE = 40 # modifie la taille suivant probas
PROB_DOT_SCALE_POWER = 3 # coef de décroissance
TRUE_DOT_SIZE = 50 # taille pour les vrais positifs

# figure
plt.style.use('seaborn-whitegrid') 
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,6), dpi=150)

redish = '#d73027'
orangeish = '#fc8d59'
yellowish = '#fee090'
blueish = '#4575b4'
colormap = np.array([blueish,redish,orangeish])


ax.scatter(point_grille[:,0], point_grille[:,1], c=colormap[prédiction_cluster], alpha=0.4, 
           s=PROB_DOT_SCALE*yy_size**PROB_DOT_SCALE_POWER, linewidths=0,)


ax.contour(x_axis_range, y_axis_range, 
           np.reshape(prédiction_cluster,(x_grille.shape[0],-1)), 
           levels=3, linewidths=1, 
           colors=[redish,blueish, blueish,orangeish,])

# Affichage des données d'origine.
ax.scatter(x_point, y_point, c=colormap[cluster], s=TRUE_DOT_SIZE, zorder=3, linewidths=0.7, edgecolor='k')

# Legende
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()

ax.set_ylabel(r"$y$")
ax.set_xlabel(r"$x$")
ax.set_title("Classification k= %i" %(k))

legend_class = []
for flower_class, color in zip(['Bleu', 'Rouge'], [blueish, redish]):
    legend_class.append(Line2D([0], [0], marker='o', label=flower_class,ls='None',
                               markerfacecolor=color, markersize=np.sqrt(TRUE_DOT_SIZE), 
                               markeredgecolor='k', markeredgewidth=0.7))


prob_values = [0.4, 0.6, 0.8, 1.0]
legend_prob = []
for prob in prob_values:
    legend_prob.append(Line2D([0], [0], marker='o', label=prob, ls='None', alpha=0.8,
                              markerfacecolor='grey', 
                              markersize=np.sqrt(PROB_DOT_SCALE*prob**PROB_DOT_SCALE_POWER), 
                              markeredgecolor='k', markeredgewidth=0))

legend1 = ax.legend(handles=legend_class, loc='center', 
                    bbox_to_anchor=(1.10, 0.35),
                    frameon=False, title='Cluster')

legend2 = ax.legend(handles=legend_prob, loc='center', 
                    bbox_to_anchor=(1.08, 0.65),
                    frameon=False, title='Proba', )

ax.add_artist(legend1) # ajoute la légende

ax.set_yticks(np.arange(y_min,y_max, 1)) 
ax.grid(False)


ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))


ax.set_xticks(ax.get_xticks()[1:-1])
ax.set_yticks(np.arange(y_min,y_max, 1)[1:])


ax.set_aspect(1)

# plt.savefig('knn.svg',dpi=300,format='svg', bbox_inches = "tight")
# plt.savefig('knn.png',dpi=300,bbox_inches = "tight")
plt.show()