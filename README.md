# Conférence PEIP : Simulation de la propagation de la peste

### Mots-clés : Simulation, Épidémies, Peste, Python

### Projet : Simuler la propagation de la peste au sein du campus universitaire de la Chantrerie (Nantes) en utilisant les déplacements semi-aléatoires des étudiants.

Deux modélisations ont été effectuées. La première, plus simpliste, est constituée de points de différentes couleurs, avec des déplacements aléatoires. Les points verts sont les habitants sains, les jaunes sont atteints de la peste bubonique (moins mortelle), les rouges sont atteints de la peste pulmonaire (plus mortelle), les points gris représentent les rats (qui transmettent la peste), et les habitants morts sont représentés par des points noirs, donc invisibles sur le fond noir de la fenêtre graphique pygame.
Lorsque deux points entrent en collision, ils peuvent changer d'états. Ces changements d'états sont régis par des paramètres représentant la probabilité d'occurrence de l'évènement. Une évolution temporelle de la peste est aussi implémentée.

La deuxième modélisation reprend les mêmes principes que la première mais cette fois-ci les habitants ne se déplacent plus de manières aléatoires dans un rectangle mais au sein d'un campus universitaire, représenté par des bâtiments et des chemins. Les déplacements ne sont plus aléatoires mais probabilistes, selon un sondage effectué sur les bâtiments les plus fréquentés et selon les moments de la journée (le midi les étudiants vont au restaurant universitaire). 

Pour exécuter les modélisations il faut lancer le fichier "modelisationi.py" (i=1,2). L'interface graphique s'ouvrira alors. Les librairies pygame, math, os, random sont utilisées.

Les résultats ainsi que plus de détails sont disponibles dans le rapport du projet.

Projet réalisé avec Mm. Ndiaye, Mm. Tremier, Mm. Bachelier, Mm. Perrot, Mm. Racineau, Mm. Picart, M. Liégard. Codes programmés par Mm. Renoud Hallereau (moi-même) et M. Liégard.
Remerciements à M. Martinod pour son aide.
