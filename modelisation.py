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

simulation_active = True
val_aleatoire = 20 # correspond au déplacement max des points d'un instant à l'autre
rayon_cercle = 9
nbvert = 50 # nombre d'habitants vert au départ
nbrouge = 1 # nombre d'habitants rouge au départ
nbjaune = 0 # nombre d'habitants jaune au départ
nbrat = 1 # nombre de rats contaminés au départ
vert = [[screen_size_x/2,screen_size_y/2] for i in range(nbvert)] # liste qui contiendra les positions des points verts, à initialiser aux positions de départs
rouge = [[0,0] for i in range(nbrouge)] # liste qui contiendra les positions des points rouges, à initialiser aux positions de départs
jaune = [[600,600] for i in range(nbjaune)]
rat = [[700,0] for i in range(nbrat)]
Habitantvert = [0 for i in range(nbvert)] # liste qui contiendra les cercles verts
Habitantrouge = [0 for i in range(nbrouge)] # liste qui contiendra les cercles rouges
Habitantjaune = [0 for i in range(nbjaune)]
Habitantrat = [0 for i in range(nbrat)]

"""
Fonction qui dessine les cercles verts
entrées : listes des positions de la couleur voulu, chaine de caractère contenant la couleur voulu en anglais,liste des cercles, taille du cercle voulu, fond d'écran, déplacements x et y, numéro i du point
"""
def habitant(couleur,color,Habitant,rayon_cercle,screen,x,y,i):
    couleur[0] += x # déplace le point en x
    couleur[1] += y # déplace le point en y
    Habitant[i] = pygame.draw.circle(screen, color, (couleur[0],couleur[1]), rayon_cercle) # met dans la liste des cercles le cercle dessiné
    return couleur


"""
Fonction qui déplace les points 
entrées : la liste vert ou rouge selon les points à déplacer, la fonction pour dessiner cercle, val_aleatoire, rayon_cercle, screen, numéro i du point 
sorties : déplacements x et y
"""
def DéplacementPoints(couleur,color,Habitant,val_aleatoire,rayon_cercle,screen,i):
    x = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en x) entre -val_aleatoire et val_aleatoire
    y = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en y) entre -val_aleatoire et val_aleatoire
    couleur[i] = habitant(couleur[i],color,Habitant,rayon_cercle,screen,x,y,i) # appel la fonction habitant
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
Fonctions qui calcule la distance entre 2 points, si proche alors collisions, donc change de couleur (c1 rencontre c2 > c1 devient c2)
entrées : vert,rouge,Habitantvert,Habitantrouge,nbvert,nbrouge,rayon_cercle
sorties : nbvert,nbrouge
"""
def collision(c1,c2,Habitant1,Habitant2,nb1,nb2,color,rayon_cercle,facteur):
    i = 0
    while i != nb1:
        col = False
        for j in range(nb2):
            distance = ((c1[i][0] - c2[j][0])**2+(c1[i][1] - c2[j][1])**2)**(1/2)
            if (distance<(4*rayon_cercle)):
                #print('collision')
                col = True
                pourcent=random.uniform(0,1) # pourcentage de chance de devenir malade
        if col and pourcent<facteur:
            c2.insert(j,c1[i]) # ajoute nouvelle position du point rouge dans la liste
            Habitant2.insert(j, pygame.draw.circle(screen, color, (c1[i][0],c1[i][1]), rayon_cercle)) # dessine nouveau point rouge
            Habitant1.pop(i) # supprime ancien point vert
            c1.pop(i) # enlève position ancien point vert de la liste
            nb1 -= 1 # enlève 1 au nombre d'habitants vert
            nb2 += 1 # ajoute 1 au nombre d'habitants rouge
        else:
            i +=1 # si pas de collision on passe à l'indice d'après
    return nb1,nb2

"""
Fonction comme collision sauf que quand c1 rencontre c2, c2 devient c3 et c1 reste
"""
def collision2(c1,c2,c3,Habitant1,Habitant2,Habitant3,nb1,nb2,nb3,color,rayon_cercle,facteur):
    i = 0
    while i != nb1:
        col = False
        for j in range(nb2):
            distance = ((c1[i][0] - c2[j][0])**2+(c1[i][1] - c2[j][1])**2)**(1/2)
            if (distance<(4*rayon_cercle)):
                #print('collision')
                col = True
                pourcent=random.uniform(0,1) # pourcentage de chance de devenir malade
        if col and pourcent<facteur:
            c3.insert(j,c1[i]) # ajoute nouvelle position du point jaune dans la liste
            Habitant3.insert(j, pygame.draw.circle(screen, color, (c1[i][0],c1[i][1]), rayon_cercle)) # dessine nouveau point jaune
            Habitant2.pop(i) # supprime ancien point vert
            c2.pop(i) # enlève position ancien point vert de la liste
            nb2 -= 1 # enlève 1 au nombre d'habitants vert
            nb3 += 1 # ajoute 1 au nombre d'habitants jaune
        else:
            i +=1 # si pas de collision on passe à l'indice d'après
    return nb2,nb3


while True: # boucle infinie
    for event in pygame.event.get():
        if event.type == QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
            sys.exit()
    if simulation_active:  # si on veut que la simul continue
        screen.fill('black')  # couleur du fond
        for i in range(nbvert):
            vert,x1,y1=DéplacementPoints(vert,'green',Habitantvert,val_aleatoire,rayon_cercle,screen,i) #appel la fonction DéplacementPoints
        for i in range(nbrouge):
            rouge,x2,y2=DéplacementPoints(rouge,'red',Habitantrouge,val_aleatoire,rayon_cercle,screen,i) #appel la fonction DéplacementPoints
        for i in range(nbjaune):
            jaune,x3,y3=DéplacementPoints(jaune,'yellow',Habitantjaune,val_aleatoire,rayon_cercle,screen,i)
        for i in range(nbrat):
            rat,x4,y4=DéplacementPoints(rat,'gray',Habitantrat,val_aleatoire,rayon_cercle,screen,i)
        nbvert,nbjaune=collision(vert,jaune,Habitantvert,Habitantjaune,nbvert,nbjaune,'yellow',rayon_cercle,0.5) #appel la fonction collision
        nbjaune,nbrouge=collision(jaune,rouge,Habitantjaune,Habitantrouge,nbjaune,nbrouge,'red',rayon_cercle,0.3)
        nbvert,nbjaune=collision2(rat,vert,jaune,Habitantrat,Habitantvert,Habitantjaune,nbrat,nbvert,nbjaune,'yellow',rayon_cercle,0.05)

    clock.tick(vitesse_affichage)  # vitesse
    pygame.display.update()  # truc qui affiche tout
