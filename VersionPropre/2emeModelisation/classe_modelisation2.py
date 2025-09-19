import pygame

class habitant:
    def __init__(self,color,posx,posy,temps,rayon,screen,endroit,preendroit):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.rayon = rayon
        self.temps = temps
        self.screen = screen
        self.endroit = endroit
        self.preendroit = preendroit
        self.ru = False

    def dessin(self):
        pygame.draw.circle(self.screen,self.color,(self.posx,self.posy),self.rayon)
