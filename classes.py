import pygame
import sys
import pygame.locals as pyl
from math import *
import random
"""
pygame.init()

clock = pygame.time.Clock()
info = pygame.display.Info()

screen_size_x = info.current_w    # taille de la fenêtre de jeu en plein écran
screen_size_y = info.current_h
screen_size_x, screen_size_y = screen_size_x, screen_size_y - 60
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
"""
class habitant:

    def __init__(self,color,posx,posy,temps,rayon,screen,endroit,preendroit,objectif):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.rayon = rayon
        self.temps = temps
        self.screen = screen
        self.endroit = endroit
        self.preendroit = preendroit
        self.objectif = objectif

    def dessin(self):
        pygame.draw.circle(self.screen,self.color,(self.posx,self.posy),self.rayon)

    def position(self,verifchemin,fact2,p):
        if verifchemin(self.posx, self.posy,fact2,p):
            return True