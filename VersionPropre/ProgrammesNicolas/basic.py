import pygame
import sys
from pygame.locals import *
import math
import random

clock = pygame.time.Clock()
# a voir si possible de chopper automatiquement le max de pixel sur un appareil donner, en adaptant en fonction du type (ecran de diff dimension, tel, ipad)
screen_size_x = 800
screen_size_y = 800
pygame.init()
# creation de notre fenetre de dimension choisis
screen = pygame.display.set_mode((screen_size_x, screen_size_y))


# plutot en fps mais comme ça le nom est claire, pour plus de visibilté a baisser, sinon on laisse a 60 par convention (60 fps les écrans t'as capter)
vitesse_affichage = 60
val_aleatoire = 40
rayon_cercle = 50
simulation_active = True
x = random.uniform(-val_aleatoire, val_aleatoire)
y = random.uniform(-val_aleatoire, val_aleatoire)
pos_x = (screen_size_x/2)
pos_y = (screen_size_y/2)


while True:  # boucle infinie
    for event in pygame.event.get():
        if event.type == QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
            sys.exit()
    if simulation_active:  # si on veut que la simul continue
        screen.fill('black')  # couleur du fond
        habitant = pygame.draw.circle(
            screen, 'green', (pos_x+x, pos_y+y), rayon_cercle)  # affichage d'un cercle

        pos_x = pos_x+x
        pos_y = pos_y+y

        # zone de detection de collision
        # si dans la zone visible alors on change rien
        if val_aleatoire+rayon_cercle <= pos_x <= screen_size_x-(val_aleatoire+rayon_cercle):
            pos_x = pos_x + x
        elif val_aleatoire+rayon_cercle > pos_x:
            # si on est en dehors du cote des negatifs, on force le nombre x a etre positif pour etre sur d'avancer
            pos_x = pos_x+abs(x)
        else:
            # meme chose mais si on est trop loin du cadre
            pos_x = pos_x-abs(x)

        if val_aleatoire+rayon_cercle <= pos_y <= screen_size_y-(val_aleatoire+rayon_cercle):
            pos_y = pos_y + y
        elif val_aleatoire+rayon_cercle > pos_y:  # je prends pas 0 en comparaison pour de meilleure collision
            pos_y = pos_y+abs(y)
        else:
            pos_y = pos_y-abs(y)

        # fin de zone de detection de collision

        # on prends de nouvelle valeurs aléatoire
        # .uniform c'est des floats pour plus de fluiditer
        x = random.uniform(-val_aleatoire, val_aleatoire)
        y = random.uniform(-val_aleatoire, val_aleatoire)

    clock.tick(vitesse_affichage)  # vitesse

    pygame.display.update()  # truc qui affiche
