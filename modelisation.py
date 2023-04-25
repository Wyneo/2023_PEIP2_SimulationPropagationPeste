import pygame
import sys
import pygame.locals as pyl
from math import *
import random
from classes import *

pygame.init()

""" 
# pas besoin de les définirent ici car fait dans le fichier classes
clock = pygame.time.Clock()
info = pygame.display.Info()
screen_size_x = info.current_w    # taille de la fenêtre de jeu en plein écran
screen_size_y = info.current_h
screen_size_x, screen_size_y = screen_size_x, screen_size_y - 60
# creation de notre fenêtre de dimensions choisis
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
"""

# plutot en fps mais comme ça le nom est claire, pour plus de visibilté a baisser, sinon on laisse a 60 par convention (60 fps les écrans t'as capter)
vitesse_affichage = 6
simulation_active = True
val_aleatoire = 30 # correspond au déplacement max des points d'un instant à l'autre
rayon_cercle = 1
n = 1
test = 0 # nombre de tours de boucle depuis que la fenêtre est lancée

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
factvr = 0.6
factgvj = 0.25
# temps d'attente (ex : tattjr = temps d'attente de jaune en rouge) en tour de boucle int(x*9), x=nbjours
nbTBPJ = 24  # nb de tour de boucle par jour
tattjr = int(3.5*nbTBPJ*9)
tattjv = int(1.0*nbTBPJ*9)
tattjn = int(4.0*nbTBPJ*9)
tattrn = int(2.5*nbTBPJ*9)
tattrv = int(1.0*nbTBPJ*9)
tattgn = int(2.4*nbTBPJ*9) # au lieu de 3.5 pour avoir 60 jours
tattRUinf = int(0.5*nbTBPJ*9)
tattRUsup = int(0.6*nbTBPJ*9)
tattRUdedans=int(0.2*nbTBPJ*9)
n2 = 1
n3 = 1

Habitant = [] # liste qui stockera tous les "objets" points
R0 = [] # liste du nombre de gens contaminé par les points lors du passage de vert à rouge
couleur = [] # vaut 'r' si le point est rouge à un moment
sommeR0 = 0 # somme des contaminations de vert à rouge
nbrougetot = 0 # nb de points rouge qu'il y a eu au total

"""
Fonction qui dessine les cercles de couleurs voulus, sert seulement au moment d'initialiser les points
entrées : couleur voulu, positions x et y du point, le temps à l'instant ou les points sont créé, déplacements x et y, numéro i du point
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
entrées : la couleur des points à déplacer, leur position x et y, val_aleatoire, rayon_cercle, numéro i du point, nb de tours 
sorties : la liste Habitant, les déplacements x et y
"""
def DéplacementPoints(color,positionx,positiony,val_aleatoire,rayon_cercle,i,test,screen,endroit,preendroit):
    x = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en x) entre -val_aleatoire et val_aleatoire
    y = random.uniform(-val_aleatoire, val_aleatoire) # génère une valeur aléatoire (correspondra au déplacement en y) entre -val_aleatoire et val_aleatoire
    Habitant[i]=hab(color,positionx,positiony,test,x,y,rayon_cercle,i,screen,endroit,preendroit) # appel la fonction hab
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
entrées : couleur1,couleur2,nombre d'habitants de la couleur c1 et c2,rayon_cercle, facteur de réussite de la collision, nb de tours
sorties : nombre d'habitants de la couleur c1 et c2
"""
def collision(c1,c2,nb1,nb2,nbtot,rayon_cercle,facteur,test):
    for i in range(nbtot):
        col =False
        if Habitant[i].color == c1:  # si le point est bien de la couleur c1
            for j in range(nbtot):
                if Habitant[j].color == c2:  # si le point est bien de la couleur c2
                    distance = ((Habitant[i].posx - Habitant[j].posx)**2+(Habitant[i].posy - Habitant[j].posy)**2)**(1/2)
                    if (distance<(rayon_cercle)):
                        col = True
                        pourcent = random.uniform(0,1)  # nombre aléatoire correspond au pourcentage de chance de changer de couleur
                        if pourcent < facteur:
                            R0[j] += 1  # s'il y a eu contamination on ajoute un à lan case du point
            if col and pourcent < facteur:  # s'il y a eu collision et que le nb aleatoire est inférieur au facteur définit
                Habitant[i].color = c2  # changement de couleur
                Habitant[i].temps = test # nouveau temps : temps au moment de la "création" du "nouveau" point
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
                    if (distance < (rayon_cercle)):
                        pourcent = random.uniform(0,1) # pourcentage de chance de changer de couleur
                        if pourcent < facteur:
                            Habitant[j].color = c3 # changement de couleur
                            Habitant[j].temps = test # nouveau temps : temps au moment de la "création" du "nouveau" point
                            nb2 -= 1 # enlève 1 au nombre d'habitants vert
                            nb3 += 1 # ajoute 1 au nombre d'habitants jaune
    return nb2,nb3

"""
Fonction qui calcul le temps qui s'est écoulé depuis que le point est de la couleur c1, si ce temps est inf au temps d'attente alors c1 > c2
entrées : couleur c1 et c2, nombre d'habitants de la couleur c1 et c2, temps de départ de la simulation, temps d'attente, facteur de réussite du changement de couleur, numéro i du point, nb de tours
sorties : nombre d'habitants de la couleur c1 et c2
"""
def verifTempsSup(c1,c2,nb1,nb2,tattente,facteur,i,test):
    if Habitant[i].color == c1:
        pourcent = random.uniform(0,1) # pourcentage de chance de changer de couleur
        #print(Habitant[i].temps)
        if test - Habitant[i].temps > tattente and pourcent < facteur: # si le temps est supérieur au temps d'attente et que le nb aleatoire est inférieur au facteur définit
            Habitant[i].color = c2 # changement de couleur
            Habitant[i].temps = test # nouveau temps : temps au moment de la "création" du "nouveau" point
            nb1 -= 1
            nb2 += 1
            if c2 == 'black':
                Habitant[i].posx, Habitant[i].posy = -10000, -10000
                Habitant[i].endroit, Habitant[i].preendroit = -1, -1
    return nb1,nb2

"""
Fonction comme verifTempsSup mais pour quand on veut que ce soit possible seulement avant un temps max
"""
def verifTempsInf(c1,c2,nb1,nb2,tattente,facteur,i,test):
    if Habitant[i].color == c1:
        pourcent = random.uniform(0,1) # pourcentage de chance de changer de couleur
        if test - Habitant[i].temps == tattente and pourcent < facteur: # si le temps est supérieur au temps d'attente et que le nb aleatoire est inférieur au facteur définit
            Habitant[i].color = c2 # changement de couleur
            Habitant[i].temps = test # nouveau temps : temps au moment de la "création" du "nouveau" point
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
            Habitant[i].posx,Habitant[i].posy = -10000, -10000
            Habitant[i].endroit, Habitant[i].preendroit = -1,-1
            #print('rat', nb1)
    return n,nb1,nb2

"""
# initialisation

# d'abord en points blanc à des endroits aléatoire
for i in range(nbtot):
    cercle = habitant('white', random.uniform(0,screen_size_x-10), random.uniform(0,screen_size_y-10), test,rayon_cercle)
    Habitant.append(cercle)
    R0.append(0)  # initialisation de la liste
    couleur.append(0)  # initialisation de la liste
# puis on créer les "bons" points au couleur voulu
for i in range(nbvert):
    Habitant, x1, y1 = DéplacementPoints('green', Habitant[i].posx, Habitant[i].posy, val_aleatoire, rayon_cercle, i,test)  # appel la fonction DéplacementPoints
for j in range(nbvert, nbvert + nbjaune):
    Habitant, x3, y3 = DéplacementPoints('yellow', Habitant[j].posx, Habitant[j].posy, val_aleatoire, rayon_cercle, j,test)
for k in range(nbvert + nbjaune, nbvert + nbjaune + nbrat):
    Habitant, x4, y4 = DéplacementPoints('gray', Habitant[k].posx, Habitant[k].posy, val_aleatoire, rayon_cercle, k,test)
for m in range(nbvert + nbjaune + nbrat, nbvert + nbjaune + nbrat + nbrouge):
    Habitant, x2, y2 = DéplacementPoints('red', Habitant[m].posx, Habitant[m].posy, val_aleatoire, rayon_cercle,m,test)


#simulation

continuer = True
while continuer: # boucle infinie
    for event in pygame.event.get():
        if event.type == pyl.QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
            continuer = False
    if simulation_active:  # si on veut que la simul continue
        screen.fill('black')  # couleur du fond
        font = pygame.font.Font(None, int(screen_size_x/30))
        time1 = pygame.time.get_ticks() # temps de départ
        time2 = int(time1/ 1000) # transforme time1 en seconde
        text = font.render(str(time2), True, 'white') # transforme en texte time2
        nbboucle= font.render(str(test),True,'white')
        for i in range(nbtot):
            x = random.uniform(-val_aleatoire,val_aleatoire)  # génère une valeur aléatoire (correspondra au déplacement en x) entre -val_aleatoire et val_aleatoire
            y = random.uniform(-val_aleatoire,val_aleatoire)  # génère une valeur aléatoire (correspondra au déplacement en y) entre -val_aleatoire et val_aleatoire
            Habitant[i].posx += x # change la position des points
            Habitant[i].posy += y
            Habitant[i].posx, Habitant[i].posy = VerifPos(Habitant[i].posx, Habitant[i].posy, val_aleatoire,rayon_cercle, screen_size_x, screen_size_y, x,y)  # appel la fonction VerifPos
            Habitant[i].dessin() # dessine les points
            nbjaune,nbrouge = verifTempsSup('yellow','red',nbjaune,nbrouge,tattjr,factjr,i,test) # les points jaunes deviennent rouges au bout d'un moment
            nbrouge,nbmort = verifTempsSup('red','black',nbrouge,nbmort,tattrn,factrn,i,test) # les points rouges deviennent noirs (meurent) au bout d'un moment
            nbjaune,nbvert = verifTempsInf('yellow','green',nbjaune,nbvert,tattjv,factjv,i,test) # les points jaunes deviennent verts (guérissent) tant que le temps est pas dépassé
            nbjaune,nbmort = verifTempsSup('yellow','black',nbjaune,nbmort,tattjn,factjn,i,test) # les points jaunes deviennent noirs (meurent) au bout d'un moment
            n,nbrat,nbmort = rat('gray','black',nbrat,nbmort,test,tattgn,n,i) # les points gris (rats) deviennent noirs (meurent) au bout d'un moment
            nbrouge,nbvert = verifTempsInf('red','green',nbrouge,nbvert,tattrv,factrv,i,test) # les points rouges deviennent verts (guérissent) tant que le temps est pas dépassé
            if Habitant[i].color == 'red': # si le point est rouge on met 'r' dans le tableau afin de savoir à la fin qui a été rouge à un momen t
                couleur[i] = 'r'
        nbvert,nbrouge = collision('green', 'red', nbvert, nbrouge,nbtot,rayon_cercle,factvr,test) # appel la fonction collision : les points verts sont contaminés par les rouges
        nbvert,nbjaune = collision2('gray','green','yellow',nbrat,nbvert,nbjaune,nbtot,rayon_cercle,factgvj,test) # appel la fonction collision2 : les points gris (rats) contaminent les verts  qui deviennent jaunes
        screen.blit(text, (screen_size_x / 100, screen_size_y / 100))  # affiche le texte sur le fond
        screen.blit(nbboucle, (300, 10)) # affiche le nombre de tours
    clock.tick(vitesse_affichage)  # vitesse
    pygame.display.update()  # truc qui affiche tout
    test+=1 # on compte le nombre de tours


#On regarde si le point a été rouge à un moment
#Si oui on ajoute son nombre de contamination, et on compte le nombre de point rouge
#Ensuite on divise la somme des contaminations par le nombre de rouge

for i in range(nbtot):
    if couleur[i] == 'r':
        sommeR0 += R0[i]
        nbrougetot += 1
print(test)
print("nbvert restant : ", nbvert)
print("nb de contaminations : ", sommeR0)
print("nb de rouge total : ", nbrougetot)
print("R0 : ", sommeR0/nbrougetot) # affiche le nombre de vert restant, le nombre total de contamination, le nombre de rouge qu'il y a eu au total, le R0

# ajout dans un tableur des nouvels stats, à commenter si vous avez pas le tableur
with open("stat modélisation conf peip - Feuille 1.csv", "a") as fichier:
    fichier.write("\n")
    fichier.write("\t")
    fichier.write("\t")

    fichier.write(str(tattgn/1000))
    fichier.write("\t")
    fichier.write(str(nbvert))
    fichier.write("\t")
    fichier.write(str(sommeR0))
    fichier.write("\t")
    fichier.write(str(nbrougetot))
    fichier.write("\t")
    fichier.write(str(sommeR0/nbrougetot))
"""