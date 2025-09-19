# Fichier similaire à celui de la première modélisation, avec l'initialisation des variables similaires,
# et avec toute les fonctions de la première modélisation, parfois modifié, et certaines ne sont pas utilisé
# mais toute la partie 'programme' a été enlevé

import pygame
import sys
import pygame.locals as pyl
from math import *
import random
from classes import *

pygame.init()


# plutot en fps mais comme ça le nom est claire, pour plus de visibilté a baisser, sinon on laisse a 60 par convention (60 fps les écrans t'as capter)
vitesse_affichage = 6
simulation_active = True
val_aleatoire = 30 # correspond au déplacement max des points d'un instant à l'autre
rayon_cercle = 1
n = 1
test = 0  # nombre de tours de boucle depuis que la fenêtre est lancée

# nombre d'habitants au départ
nbvert, nbjaune, nbrouge, nbrat, nbmort = 500, 0, 0, 25, 0
nbtot = nbvert+nbjaune+nbrouge+nbrat+nbmort

# facteurs de chance (ex : factjr = facteur de jaune en rouge) compris entre 0 et 1
factjr = 0.35
factjv = 0.8
factjn = 0.55
factrn = 1
factrv = 0.8
factgn = 1
factvr = 0.1
factgvj = 0.25
factru = 0.1
# temps d'attente (ex : tattjr = temps d'attente de jaune en rouge) en tours de boucle
nbTBPJ = 216  # nb de tour de boucle par jour
tattjr = int(3.5*nbTBPJ)
tattjv = int(1.0*nbTBPJ)
tattjn = int(5.0*nbTBPJ)
tattrn = int(2.0*nbTBPJ)
tattrv = int(1.0*nbTBPJ)
tattgn = int(2.4*nbTBPJ)
tattRUinf = int(0.5*nbTBPJ)
tattRUdedans=int(0.2*nbTBPJ)
n2 = 1
n3 = 1

Habitant = []  # liste qui stockera tous les "objets" points
R0 = []  # liste du nombre de gens contaminé par les points lors du passage de vert à rouge
couleur = []  # vaut 'r' si le point est rouge à un moment
couleur2 = []  # vaut 'j' si le point est jaune à un moment
sommeR0 = 0  # somme des contaminations de vert à rouge
nbrougetot = 0  # nb de points rouge qu'il y a eu au total
nbjaunetot = 0  # nb de points jaune qu'il y a eu au total


"""
Fonction qui dessine les cercles de couleurs voulus, sert seulement au moment d'initialiser les points
entrées : couleur voulu, positions x et y du point, le temps à l'instant ou les points sont créé, déplacements x et y, rayon du point, numéro i du point, le fond de la fenêtre, les attributs endroit et preendroit
"""
def hab(color,positionx,positiony,temps,x,y,rayon_cercle,i,screen,endroit,preendroit):
    positionx += x
    positiony += y
    cercle = habitant(color,positionx,positiony,temps,rayon_cercle,screen,endroit,preendroit)
    cercle.dessin() # dessine les points
    Habitant[i] = cercle # ajout des points dans la liste
    return Habitant[i]

"""
Fonction qui déplace les points, à l'initialisation
entrées : la couleur des points à déplacer, leur position x et y, val_aleatoire, rayon_cercle, numéro i du point, nb de , le fond de la fenêtre, les attributs endroit et preendroit
sorties : la liste Habitant, les déplacements x et y
"""
def DéplacementPoints(color,positionx,positiony,val_aleatoire,rayon_cercle,i,test,screen,endroit,preendroit):
    x = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en x) entre -val_aleatoire et val_aleatoire
    y = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en y) entre -val_aleatoire et val_aleatoire
    Habitant[i] = hab(color,positionx,positiony,test,x,y,rayon_cercle,i,screen,endroit,preendroit) # appel la fonction hab
    Habitant[i].posx,Habitant[i].posy = VerifPos(Habitant[i].posx,Habitant[i].posy,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,x,y) # appel la fonction VerifPos
    return Habitant,x,y

"""
Fonctions qui vérifie si le point n'est pas en dehors de l'écran 
entrées : les positions du point i en x et y,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,déplacements x et y
sorties : la nouvelle position 
"""
def VerifPos(positionx,positiony,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,x,y):
    # si dans la zone visible alors on change rien
    if val_aleatoire + rayon_cercle <= positionx <= screen_size_x - ( rayon_cercle):
        positionx += x
    elif val_aleatoire + rayon_cercle > positionx:
        # si on est en dehors du cote des negatifs, on force le nombre x a etre positif pour etre sur d'avancer
        x = random.uniform(0, val_aleatoire)
        positionx += abs(x)
    else:
        # meme chose mais si on est trop loin du cadre
        x = random.uniform(-val_aleatoire, 0)
        positionx -= abs(x)
    # même chose pour y
    if val_aleatoire + rayon_cercle <= positiony <= screen_size_y - ( rayon_cercle):
        positiony += y
    elif val_aleatoire + rayon_cercle > positiony:  # je prends pas 0 en comparaison pour de meilleure collision
        y = random.uniform(0, val_aleatoire)
        positiony += abs(y)
    else:
        y = random.uniform(-val_aleatoire, 0)
        positiony -= abs(y)
    return positionx,positiony


"""
Fonctions qui calcule la distance entre 2 points, si proche alors collisions, donc change de couleur (c1 rencontre c2 > c1 devient c2)
entrées : couleur1,couleur2, nombre d'habitants de la couleur c1 et c2, nb d'hab tot, rayon_cercle, facteur de réussite de la collision, nb de tours
sorties : nombre d'habitants de la couleur c1 et c2
"""
def collision(c1,c2,nb1,nb2,nbtot,rayon_cercle,facteur,test):
    for i in range(nbtot):
        col = False
        if Habitant[i].color == c1:  # si le point est bien de la couleur c1
            for j in range(nbtot):
                if Habitant[j].color == c2:  # si le point est bien de la couleur c2
                    distance = ((Habitant[i].posx - Habitant[j].posx)**2+(Habitant[i].posy - Habitant[j].posy)**2)**(1/2)
                    if (distance<(rayon_cercle)):
                        col = True
                        pourcent = random.uniform(0,1)  # nombre aléatoire correspond au pourcentage de chance de changer de couleur
                        if pourcent < facteur:
                            R0[j] += 1  # s'il y a eu contamination on ajoute un à la case du point
            if col and pourcent < facteur:  # s'il y a eu collision et que le nb aleatoire est inférieur au facteur définit
                Habitant[i].color = c2  # changement de couleur
                Habitant[i].temps = test  # nouveau temps : temps au moment de la "création" du "nouveau" point
                nb1 -= 1  # enlève 1 au nombre d'habitants de la couleur c1
                nb2 += 1  # ajoute 1 au nombre d'habitants de la couleur c2
    return nb1,nb2

"""
Fonction comme collision sauf que quand c1 rencontre c2, c2 devient c3 et c1 reste
"""
def collision2(c1,c2,c3,nb1,nb2,nb3,nbtot,rayon_cercle,facteur,test):
    for i in range(nbtot):
        if Habitant[i].color == c1:
            for j in range(nbtot):
                if Habitant[j].color == c2:
                    distance = ((Habitant[i].posx - Habitant[j].posx)**2+(Habitant[i].posy - Habitant[j].posy)**2)**(1/2)
                    if distance < (rayon_cercle):
                        pourcent = random.uniform(0,1) # pourcentage de chance de changer de couleur
                        if pourcent < facteur:
                            Habitant[j].color = c3 # changement de couleur
                            Habitant[j].temps = test # nouveau temps : temps au moment de la "création" du "nouveau" point
                            nb2 -= 1 # enlève 1 au nombre d'habitants vert
                            nb3 += 1 # ajoute 1 au nombre d'habitants jaune
    return nb2,nb3

"""
Fonction qui calcul le temps qui s'est écoulé depuis que le point est de la couleur c1, si ce temps est sup au temps d'attente alors c1 devient c2
entrées : couleur c1 et c2, nombre d'habitants de la couleur c1 et c2, temps d'attente, facteur de réussite du changement de couleur, numéro i du point, nb de tours
sorties : nombre d'habitants de la couleur c1 et c2
"""
def verifTempsSup(c1,c2,nb1,nb2,tattente,facteur,i,test):
    if Habitant[i].color == c1:
        pourcent = random.uniform(0,1)  # pourcentage de chance de changer de couleur
        if test - Habitant[i].temps > tattente and pourcent < facteur:  # si le temps est supérieur au temps d'attente et que le nb aleatoire est inférieur au facteur définit
            Habitant[i].color = c2  # changement de couleur
            Habitant[i].temps = test  # nouveau temps : temps au moment de la "création" du "nouveau" point
            nb1 -= 1
            nb2 += 1
            if c2 == 'black':  # si l'habitant est mort on l'envoie très loin
                Habitant[i].posx, Habitant[i].posy = -10000, -10000
                Habitant[i].endroit, Habitant[i].preendroit = -1, -1
    return nb1,nb2

"""
Fonction comme verifTempsSup mais pour quand on veut que ce soit possible seulement à un temps donné
"""
def verifTempsInf(c1,c2,nb1,nb2,tattente,facteur,i,test):
    if Habitant[i].color == c1:
        pourcent = random.uniform(0,1)  # pourcentage de chance de changer de couleur
        if test - Habitant[i].temps == tattente and pourcent < facteur: # si le temps est égal au temps d'attente et que le nb aleatoire est inférieur au facteur définit
            Habitant[i].color = c2  # changement de couleur
            Habitant[i].temps = test  # nouveau temps : temps au moment de la "création" du "nouveau" point
            nb1 -= 1
            nb2 += 1
    return nb1,nb2

"""
Fonction qui fait disparaitre les rats un par un 
entrée: couleur 1(rat), couleur2(mort), nb1,nb2, nb de tours, tous les combiens ils meurent, variable entière pour passer au tour suivant, numéro i du point
sorties : n, nb1,nb2
"""
def rat(c1,c2,nb1,nb2,test,tattente,n,i):
    if Habitant[i].color == c1:
        if test - Habitant[i].temps > n*tattente:
            Habitant[i].color = c2
            n += 1
            nb1 -= 1
            nb2 += 1
            Habitant[i].posx,Habitant[i].posy = -10000, -10000  # l'habitant est mort, on l'envoie très loin
            Habitant[i].endroit, Habitant[i].preendroit = -1,-1
    return n,nb1,nb2
