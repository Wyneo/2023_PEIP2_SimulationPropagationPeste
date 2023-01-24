import pygame
import sys
from pygame.locals import *
from math import *
import random

pygame.init()
clock = pygame.time.Clock()
info = pygame.display.Info()
# a voir si possible de chopper automatiquement le max de pixel sur un appareil donner, en adaptant en fonction du type (ecran de diff dimension, tel, ipad)
screen_size_x = info.current_w                                                                                                  #Taille fenêtre de jeu
screen_size_y = info.current_h
screen_size_x, screen_size_y = screen_size_x, screen_size_y - 60
# creation de notre fenetre de dimension choisis
screen = pygame.display.set_mode((screen_size_x, screen_size_y))


# plutot en fps mais comme ça le nom est claire, pour plus de visibilté a baisser, sinon on laisse a 60 par convention (60 fps les écrans t'as capter)
vitesse_affichage = 6
val_aleatoire =40
rayon_cercle = 10
simulation_active = True
pos_x1,pos_x2 = (screen_size_x / 2),(screen_size_x / 2)
pos_y1,pos_y2 = (screen_size_y / 2),(screen_size_y / 2)
#pos_x= random.uniform(-val_aleatoire, val_aleatoire)
#pos_x=600
#pos_y=random.uniform(-val_aleatoire, val_aleatoire)
#pos_y=600
habvert=[]
#habverty=[]
habrouge=[]
#habrougey=[]
nbHabitant=10

def habitantvert(pos_x,pos_y):
    x = random.uniform(-val_aleatoire, val_aleatoire)
    y = random.uniform(-val_aleatoire, val_aleatoire)
    pos_x=pos_x+x
    pos_y=pos_y+y
    #habvert.append([pos_x,pos_y])
    Habitantvert= pygame.draw.circle(screen, 'green', (pos_x, pos_y), rayon_cercle)
    return pos_x,pos_y,x,y
def habitantrouge(pos_x,pos_y):
    x = random.uniform(-val_aleatoire, val_aleatoire)
    y = random.uniform(-val_aleatoire, val_aleatoire)
    pos_x=pos_x+x
    pos_y=pos_y+y
    #habrouge.append([pos_x, pos_y])
    Habitantrouge = pygame.draw.circle(screen, 'red', (pos_x, pos_y), rayon_cercle)
    return pos_x,pos_y,x,y

def DéplacementPoints(pos_x1,pos_y1,pos_x2,pos_y2,habitant1,habitant2,hab1,hab2,val_aleatoire,nbHabitant):
    for i in range(nbHabitant):
        pos_x1,pos_y1,x1,y1=habitant1(pos_x1, pos_y1)
        pos_x2,pos_y2,x2,y2=habitant2(pos_x2, pos_y2)  # affichage d'un cercle
        #habitant(pos_x,pos_y,hab)  # affichage d'un cercle
        pos_x1,pos_y1 = VerifPos(pos_x1,pos_y1,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,x1,y1)
        pos_x2,pos_y2 = VerifPos(pos_x2,pos_y2,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,x2,y2)
        hab1.append([pos_x1, pos_y1])
        hab2.append([pos_x2, pos_y2])
    return habvert,habrouge,pos_x1,pos_y1,pos_x2,pos_y2

def VerifPos(pos_x,pos_y,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y,x,y):
    # zone de detection de collision
    # si dans la zone visible alors on change rien
    if val_aleatoire + rayon_cercle <= pos_x <= screen_size_x - ( rayon_cercle):
        pos_x = pos_x + x
    elif val_aleatoire + rayon_cercle > pos_x:
        # si on est en dehors du cote des negatifs, on force le nombre x a etre positif pour etre sur d'avancer
        x = random.uniform(0, val_aleatoire)
        pos_x = pos_x + abs(x)
    else:
        # meme chose mais si on est trop loin du cadre
        x = random.uniform(-val_aleatoire, 0)
        pos_x = pos_x - abs(x)

    if val_aleatoire + rayon_cercle <= pos_y <= screen_size_y - ( rayon_cercle):
        pos_y = pos_y + y
    elif val_aleatoire + rayon_cercle > pos_y:  # je prends pas 0 en comparaison pour de meilleure collision
        y = random.uniform(0, val_aleatoire)
        pos_y = pos_y + abs(y)
    else:
        y = random.uniform(-val_aleatoire, 0)
        pos_y = pos_y - abs(y)

    # fin de zone de detection de collision

    # on prends de nouvelle valeurs aléatoire
    # .uniform c'est des floats pour plus de fluiditer
    #x = random.uniform(-val_aleatoire, val_aleatoire)
    #y = random.uniform(-val_aleatoire, val_aleatoire)
    return pos_x,pos_y

def collision(habvert,habrouge,rayon_cercle):
    col=[]
    for i in range(nbHabitant+1):
        for j in range(nbHabitant+1):
            distance=((habvert[-i][0]-habrouge[-j][0])**2+(habvert[-i][1] - habrouge[-j][1])**2)**(1/2)
        #print(distance)
        #print(not (v in col and r in col))
            if (distance<(4*rayon_cercle)):
                print("collision")
            #print(habvert,habrouge)
            #print(not (v in col and r in col),v,r)
            #print(col)

while True:  # boucle infinie
    for event in pygame.event.get():
        if event.type == QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
            sys.exit()
    if simulation_active:  # si on veut que la simul continue
        screen.fill('black')  # couleur du fond
        habvert,habrouge,pos_x1,pos_y1,pos_x2,pos_y2=DéplacementPoints(pos_x1,pos_y1,pos_x2,pos_y2,habitantvert,habitantrouge,habvert,habrouge,val_aleatoire,nbHabitant)
        #DéplacementPoints(pos_x,pos_y,habitantrouge,habrouge,val_aleatoire,rayon_cercle,screen_size_x,screen_size_y)
        #print(habvert)
        #print(habrouge)
        collision(habvert,habrouge,rayon_cercle)
    clock.tick(vitesse_affichage)  # vitesse

    pygame.display.update()  # truc qui affiche
