import pygame
import sys
from pygame.locals import *
from math import *
import random

pygame.init()

clock = pygame.time.Clock()
info = pygame.display.Info()

screen_size_x = info.current_w    # taille de la fenêtre de jeu en plein écran
screen_size_y = info.current_h
screen_size_x, screen_size_y = screen_size_x, screen_size_y - 60
# creation de notre fenêtre de dimensions choisis
screen = pygame.display.set_mode((screen_size_x, screen_size_y))


# plutot en fps mais comme ça le nom est claire, pour plus de visibilté a baisser, sinon on laisse a 60 par convention (60 fps les écrans t'as capter)
vitesse_affichage = 10

val_aleatoire = 20 # correspond au déplacement max des points d'un instant à l'autre
rayon_cercle = 10
nbvert = 50 # nombre d'habitants vert au départ
nbrouge = 50 # nombre d'habitants rouge au départ
simulation_active = True
vert = [[screen_size_x/2,screen_size_y/2] for i in range(nbvert)] # liste qui contiendra les positions des points verts, à initialiser aux positions de départs
rouge = [[0,0] for i in range(nbrouge)] # liste qui contiendra les positions des points rouges, à initialiser aux positions de départs
Habitantvert = [0 for i in range(nbvert)] # liste qui contiendra les cercles verts
Habitantrouge = [0 for i in range(nbrouge)] # liste qui contiendra les cercles rouges

"""
Fonction qui dessine les cercles verts
entrées : listes des positions verts, taille du cercle voulu, fond d'écran, déplacements x et y, numéro i du point
"""
def habitantvert(vert,rayon_cercle,screen,x,y,i):
    vert[0] += x # déplace le point en x
    vert[1] += y # déplace le point en y
    Habitantvert[i] = pygame.draw.circle(screen, 'green', (vert[0],vert[1]), rayon_cercle) # met dans la liste des cercles le cercle dessiné
    return vert

"""
Fonction qui dessine les cercles rouges
entrées : listes des positions rouges, taille du cercle voulu, fond d'écran, déplacements x et y, numéro i du point
"""
def habitantrouge(rouge,rayon_cercle,screen,x,y,i):
    rouge[0] += x # déplace le point en x
    rouge[1] += y # déplace le point en y
    Habitantrouge[i]=pygame.draw.circle(screen, 'red', (rouge[0],rouge[1]), rayon_cercle) # met dans la liste des cercles le cercle dessiné
    return rouge

"""
Fonction qui déplace les points 
entrées : la liste vert ou rouge selon les points à déplacer, la fonction pour dessiner cercle, val_aleatoire, rayon_cercle, screen, numéro i du point 
sorties : déplacements x et y
"""
def DéplacementPoints(couleur,habitant1,val_aleatoire,rayon_cercle,screen,i):
    x = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en x) entre -val_aleatoire et val_aleatoire
    y = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en y) entre -val_aleatoire et val_aleatoire
    couleur[i]=habitant1(couleur[i],rayon_cercle,screen,x,y,i) # appel la fonction habitantvert ou habitantrouuge
    couleur[i] = VerifPos(couleur[i],val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,x,y) # appel la fonction VerifPos
    return couleur,x,y

"""
Fonctions qui vérifie si le point n'est pas en dehors de l'écran 
entrées : la position du point i vert ou rouge,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,déplacements x et y
sorties : la nouvelle position 
"""
def VerifPos(pos,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,x,y):
    # si dans la zone visible alors on change rien
    if val_aleatoire + rayon_cercle <= pos[0] <= screen_size_x - ( rayon_cercle):
        pos[0] = pos[0] + x
    elif val_aleatoire + rayon_cercle > pos[0]:
        # si on est en dehors du cote des negatifs, on force le nombre x a etre positif pour etre sur d'avancer
        x = random.uniform(0, val_aleatoire)
        pos[0] = pos[0] + abs(x)
    else:
        # meme chose mais si on est trop loin du cadre
        x = random.uniform(-val_aleatoire, 0)
        pos[0] = pos[0] - abs(x)
    # même chose pour y
    if val_aleatoire + rayon_cercle <= pos[1] <= screen_size_y - ( rayon_cercle):
        pos[1] = pos[1] + y
    elif val_aleatoire + rayon_cercle > pos[1]:  # je prends pas 0 en comparaison pour de meilleure collision
        y = random.uniform(0, val_aleatoire)
        pos[1] = pos[1] + abs(y)
    else:
        y = random.uniform(-val_aleatoire, 0)
        pos[1] = pos[1] - abs(y)
    return pos


"""
Fonctions qui calcule la distance entre 2 points, si proche alors collisions, donc change de couleur
entrées : vert,rouge,Habitantvert,Habitantrouge,nbvert,nbrouge,rayon_cercle
sorties : nbvert,nbrouge
"""
def collision(vert,rouge,Habitantvert,Habitantrouge,nbvert,nbrouge,rayon_cercle):
    i = 0
    while i != nbvert:
        col = False
        for j in range(nbrouge-2):
            distance = ((vert[i][0] - rouge[j][0])**2+(vert[i][1] - rouge[j][1])**2)**(1/2)
            if (distance<(4*rayon_cercle)):
                #print('collision')
                col = True
                pourcent=random.uniform(0,1) # pourcentage de chance de devenir malade
        if col and pourcent>0.5:
            rouge.insert(j,vert[i]) # ajoute nouvelle position du point rouge dans la liste
            Habitantrouge.insert(j, pygame.draw.circle(screen, 'red', (vert[i][0],vert[i][1]), rayon_cercle)) # dessine nouveau point rouge
            Habitantvert.pop(i) # supprime ancien point vert
            vert.pop(i) # enlève position ancien point vert de la liste
            nbvert -= 1 # enlève 1 au nombre d'habitants vert
            nbrouge += 1 # ajoute 1 au nombre d'habitants rouge
        else:
            i +=1 # si pas de collision on passe à l'indice d'après
    return nbvert,nbrouge



while True: # boucle infinie
    for event in pygame.event.get():
        if event.type == QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
            sys.exit()
    if simulation_active:  # si on veut que la simul continue
        screen.fill('black')  # couleur du fond
        for i in range(nbvert):
            vert,x1,y1=DéplacementPoints(vert,habitantvert,val_aleatoire,rayon_cercle,screen,i) #appel la fonction DéplacementPoints
        for i in range(nbrouge):
            rouge,x2,y2=DéplacementPoints(rouge,habitantrouge,val_aleatoire,rayon_cercle,screen,i) #appel la fonction DéplacementPoints
        nbvert,nbrouge=collision(vert,rouge,Habitantvert,Habitantrouge,nbvert,nbrouge,rayon_cercle) #appel la fonction collision

    clock.tick(vitesse_affichage)  # vitesse
    pygame.display.update()  # truc qui affiche tout
