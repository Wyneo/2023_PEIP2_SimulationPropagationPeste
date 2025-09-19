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
val_aleatoire = 10
rayon_cercle = 50
simulation_active = True
x = random.randint(-val_aleatoire, val_aleatoire)
y = random.randint(-val_aleatoire, val_aleatoire)
# x = random.uniform(-val_aleatoire, val_aleatoire)
# y = random.uniform(-val_aleatoire, val_aleatoire)
pos_x = (screen_size_x/2)
pos_y = (screen_size_y/2)


def collision():
    global pos_y  # on note global pour que ces diffs variable soit utilisable partout et pas que localement
    global pos_x
    global x
    global y

    if val_aleatoire+rayon_cercle <= pos_x <= screen_size_x-(val_aleatoire+rayon_cercle):
        pos_x = pos_x + x
    elif val_aleatoire+rayon_cercle > pos_x:
        # si on est en dehors du cote des negatifs, on force le nombre x a etre positif pour etre sur d'avancer
        x = random.uniform(0, val_aleatoire)
        pos_x = pos_x+abs(x)
    else:
        # meme chose mais si on est trop loin du cadre
        x = random.uniform(-val_aleatoire, 0)
        pos_x = pos_x-abs(x)

    if val_aleatoire+rayon_cercle <= pos_y <= screen_size_y-(val_aleatoire+rayon_cercle):
        pos_y = pos_y + y
    elif val_aleatoire+rayon_cercle > pos_y:  # je prends pas 0 en comparaison pour de meilleure collision
        y = random.uniform(0, val_aleatoire)
        pos_y = pos_y+abs(y)
    else:
        y = random.uniform(-val_aleatoire, 0)
        pos_y = pos_y-abs(y)
    pos_x = round(pos_x+x)
    pos_y = round(pos_y+y)


def habitant():
    pygame.draw.circle(screen, 'green', (pos_x+x, pos_y+y), rayon_cercle)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
                sys.exit()  # on peut faire avec une var a la place du True qu'on assigne a false ici
        if simulation_active:  # si on veut que la simul continue
            screen.fill('black')  # couleur du fond
            habitant()
            collision()
            print(pos_x)

        clock.tick(vitesse_affichage)  # vitesse

        # truc qui affiche tres important a pas enlever sinon ça nous montre pas les changements
        pygame.display.update()


if __name__ == "__main__":
    main()
