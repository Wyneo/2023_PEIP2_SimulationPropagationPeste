import random
from math import *
from modelisation import hab


def fonctlin ( x1, y1, x2, y2 ):             #entrée : coordonées de 2 points, sortie : a et b de la fonction y = a*x + b passant par les 2 points
    if (x1 != x2):
        a = (y1-y2)/(x1-x2)
        b = y1 - x1 * a
    else :
        a = x1
        b = 0
    return a,b

# fmin = correspond aux lignes fermant les chemins en haut et à gauche (là ou x et y sont les plus bas)
# fmax = correspond aux lignes fermant les chemins en bas et à droite (là ou x et y sont les plus hauts)
def f1xmin(x,fact2,p):
    f = -3.53 * x + 1066.32 * fact2
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a* 1000 + b))
    return f
def f1ymax (x,fact2,p):
    #f = -0.37 * x + 428.42 * fact2
    a, b = fonctlin(p[0][0], p[0][1]+20, p[13][0], p[13][1]+20)
    f = a * x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    #pygame.draw.line(WIN, BLACK, (0, -0.37 * 0 + 428.42 * fact2), (1000, -0.37 * 1000 + 428.42 * fact2))
    return f
def f1xmax (x,fact2,p):
    f = -3.46*x + 1111.66 * fact2
    #pygame.draw.line(WIN, BLACK, (0, -3.46 * 0 + 1111.66 * fact2), (1000, -3.46 * 1000 + 1111.66 * fact2))
    return f
def f1ymin (x,fact2,p):
    f = 1.75 *x - 300.25 * fact2
    #a, b = fonctlin(p[0][0], p[0][0] - 20, p[13][0], p[13][0])
    #f = a * x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def f2xmin (x,fact2,p):
    f = 0.25 * x + 88.95 * fact2
    return f
def f2xmax (x,fact2,p):
    f = 0.24 * x + 109.82 * fact2
    return f
def f2ymax (x,fact2,p):
    f = -3.2*x + 1302.40 * fact2
    return f
def f2ymin (x,fact2,p):
    f = 1.75*x -300.25 * fact2
    return f
def f3xmax (x,fact2,p):
    f = 0.31*x + 83.56 * fact2
    return f
def f3ymax (x,fact2,p):
    f = -3.40 * x +1431.20 * fact2
    return f
def f3xmin (x,fact2,p):
    f = 0.25 * x + 88 * fact2
    return f
def f3ymin (x,fact2,p):
    f = -3.2 * x + 1302.4 * fact2
    return f
def f4xmax (x,fact2,p):
    f = 0.26 * x + 101.26 * fact2
    return f
def f4ymax (x,fact2,p):
    f = -0.58*x +560.53 * fact2
    return f
def f4xmin (x,fact2,p):
    f = 0.28*x + 78.61 * fact2
    return f
def f4ymin (x,fact2,p):
    f = -3.4*x + 83.56 * fact2
    return f
def f5ymax (x,fact2,p):
    f = 224 * fact2
    return f
def f5xmax (x,fact2,p):
    f = -13.5 *x + 5097.5 * fact2
    return f
def f5xmin (x,fact2,p):
    f = -10.67*x + 3893.33 * fact2
    return f
def f5ymin (x,fact2,p):
    f = 0.31 * x +83.46 * fact2
    return f
def f6xmax (x,fact2,p):
    f= - 25*x + 9355 * fact2
    return f
def f6ymax (x,fact2,p):
    f = 0.25*x + 88 * fact2
    return f
def f6xmin (x,fact2,p):
    f = -23*x + 8249 * fact2
    return f
def f6ymin (x,fact2,p):
    f = 0.13*x + 109 * fact2
    return f

def f7ymax (x,fact2,p):
    a, b = fonctlin(p[14][0], p[14][1], p[15][0], p[15][1])
    f = a * x + b * fact2
    return f
def f7ymin (x,fact2,p):
    a, b = fonctlin(p[17][0], p[17][1], p[16][0], p[16][1])
    f = a * x + b * fact2
    return f
def f7xmin (x,fact2,p):
    a,b = fonctlin(p[16][0],p[16][1],p[15][0],p[15][1])
    f= a * x + b * fact2
    return f
def f7xmax (x,fact2,p):
    a,b = fonctlin(p[17][0],p[17][1],p[14][0],p[14][1])
    f= a * x + b
    return f

def f8xmin (x,fact2,p):
    a,b = fonctlin(p[23][0],p[23][1],p[18][0],p[18][1])
    f= a * x + b
    return f
def f8xmax (x,fact2,p):
    a,b = fonctlin(p[24][0],p[24][1],p[25][0],p[25][1])
    f= a * x + b
    return f
def f8ymin (x,fact2,p):
    a,b = fonctlin(p[18][0],p[18][1],p[25][0],p[25][1])
    f= a * x + b
    return f
def f8ymax (x,fact2,p):
    a,b = fonctlin(p[23][0],p[23][1],p[24][0],p[24][1])
    f= a * x + b
    return f
def f9xmax (x,fact2,p):
    a,b = fonctlin(p[22][0],p[22][1],p[19][0],p[19][1])
    f= a * x + b
    return f
def f9xmin (x,fact2,p):
    a,b = fonctlin(p[20][0],p[20][1],p[21][0],p[21][1])
    f= a * x + b
    return f
def f9ymin (x,fact2,p):
    a,b = fonctlin(p[21][0],p[21][1],p[22][0],p[22][1])
    f= a * x + b
    return f
def f9ymax (x,fact2,p):
    a,b = fonctlin(p[20][0],p[20][1],p[19][0],p[19][1])
    f= a * x + b
    return f
def f10xmax (x,fact2,p):
    a,b = fonctlin(p[28][0],p[28][1],p[29][0],p[29][1])
    f= a * x + b
    return f
def f10xmin (x,fact2,p):
    a,b = fonctlin(p[27][0],p[27][1],p[26][0],p[26][1])
    f= a * x + b
    return f
def f10ymax (x,fact2,p):
    a,b = fonctlin(p[26][0],p[26][1],p[29][0],p[29][1])
    f= a * x + b
    return f
def f10ymin (x,fact2,p):
    a,b = fonctlin(p[28][0],p[28][1],p[27][0],p[27][1])
    f= a * x + b
    return f
def firestexmax(x,fact2,p):
    a,b = fonctlin(fact2*168,fact2*365,fact2*292,fact2*636)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0,a*0+b),(1000,a*1000+b))
    return f
def firestexmin(x,fact2,p):
    a,b = fonctlin(fact2*295,fact2*309,fact2*416,fact2*584)
    f = a*x+b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def firesteymin(x,fact2,p):
    a,b = fonctlin(fact2*168,fact2*365,fact2*295,fact2*309)
    #print(a, b)
    f = a*x+b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def firesteymax(x,fact2,p):
    a,b= fonctlin(fact2*292,fact2*636,fact2*416,fact2*584)
    #print(a, b)
    f = a*x+b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fruxmin(x,fact2,p):
    a,b = fonctlin(fact2*425,fact2*301,fact2*381,fact2*206)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fruxmax(x,fact2,p):
    a,b = fonctlin(fact2*384,fact2*317,fact2*338,fact2*223)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fruymin(x,fact2,p):
    a,b=fonctlin(fact2*381,fact2*206,fact2*338,fact2*223)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fruymax(x,fact2,p):
    a,b = fonctlin(fact2*384,fact2*317,fact2*425,fact2*301)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fihtxmin(x,fact2,p):
    a,b=fonctlin(fact2*302, fact2*62, fact2*263,fact2*138)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fihtxmax(x,fact2,p):
    a,b = fonctlin(fact2*263, fact2*138, fact2*484, fact2*168)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fihtymin(x,fact2,p):
    a,b = fonctlin(fact2*302,fact2*62,fact2*484,fact2*168)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    #print(a,b)
    return f
def fihtymax(x,fact2,p):
    a,b = fonctlin(fact2*484, fact2*168,fact2*263,fact2*138)
    f = a*x + b
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f

# renvoie true si dans la surface
def verifchemin1(x,y,fact2,p):
    if (p[0][0] <= x <= p[12][0] and ((f1xmin(x,fact2,p) <= y <= f1xmax(x,fact2,p) and f2xmin(x,fact2,p) <= y <= f1ymax(x,fact2,p)))):
        #print("chemin 1")
        return True
def verifchemin2(x, y,fact2,p):
    if (p[1][0] <= x <= p[2][0] and ((f2xmin(x,fact2,p) <= y <= f2xmax(x,fact2,p)) and (f1xmax(x,fact2,p) <= y <= f2ymax(x,fact2,p)))):  #POURQUOI??
        #print("chemin 2")
        return True
def verifchemin3(x, y,fact2,p):
    if (p[11][0] <= x <= p[5][0] and (f3xmin(x,fact2,p) <= y <= f3xmax(x,fact2,p)) and (f6ymax(x,fact2,p) <= y <= f5ymin(x,fact2,p))):
        #print("chemin 3")
        return True
def verifchemin4(x, y,fact2,p):
    if (p[8][0] <= x <= p[6][0] and f4xmin(x,fact2,p) <= y <= f4xmax(x,fact2,p) and f4ymin(x,fact2,p) <= y <= f4ymax(x,fact2,p)):
        #print("chemin 4")
        return True
def verifchemin5(x, y,fact2,p):
    if (p[11][0] <= x <= p[8][0] and f5xmin(x,fact2,p) <= y <= f5xmax(x,fact2,p) and f5ymin(x,fact2,p) <= y <= f5ymax(x,fact2,p)):
        #print("chemin 5")
        return True
def verifchemin6(x, y,fact2,p):
    if (p[3][0] <= x <= p[5][0] and f6xmin(x,fact2,p) <= y <= f6xmax(x,fact2,p) and fihtymax(x,fact2,p) <= y <=f6ymax(x,fact2,p)):  # pbl ihtymax
        #print("chemin 6")
        return True
def verifchemin7(x, y,fact2,p):
    if (p[16][0] <= x <= p[17][0] and f7xmin(x,fact2,p) <= y <= f7xmax(x,fact2,p) and f7ymin(x,fact2,p) <= y <= f7ymax(x,fact2,p)):
        return True

def verifchemin8(x, y,fact2,p):
    if (p[23][0] <= x <= p[25][0] and f8xmin(x,fact2,p) <= y <= f8xmax(x,fact2,p) and f8ymin(x,fact2,p) <= y <= f8ymax(x,fact2,p)):
        return True

def verifchemin9(x, y,fact2,p):
    if (p[21][0] <= x <= p[19][0] and f9xmin(x,fact2,p) <= y <= f9xmax(x,fact2,p) and f9ymin(x,fact2,p) <= y <= f9ymax(x,fact2,p)):
        return True

def verifchemin10(x, y,fact2,p):
    if (p[27][0] <= x <= p[26][0] and f10xmin(x,fact2,p) <= y <= f10xmax(x,fact2,p) and f10ymin(x,fact2,p) <= y <= f10ymax(x,fact2,p)):
        return True
def verifireste(x,y,fact2,p):
    if (fact2*168 <= x <= fact2*416 and (firestexmin(x,fact2,p) <= y <= firestexmax(x,fact2,p)) and (f1ymax(x,fact2,p) <= y <= firesteymax(x,fact2,p))):
        return True
def verifru(x,y,fact2,p):
    if fact2*338 <= x <= fact2*425 and fruxmin(x,fact2,p) <= y <= fruxmax(x,fact2,p) and f5ymax(x,fact2,p) <= y <= fruymax(x,fact2,p):
        return True
def verifiht(x,y,fact2,p):
    if fact2*263 <= x <= fact2*484 and fihtxmin(x,fact2,p) <= y <= fihtxmax(x,fact2,p) and fihtymin(x,fact2,p) <= y <= fihtymax(x,fact2,p):
        return True
def verifisitem(x, y,centreisitem,rayonisitem,rayon_cercle):
    if sqrt((x - centreisitem[0]) ** 2 + (y - centreisitem[1]) ** 2) < rayonisitem - rayon_cercle:
        return True

# inutiliser pour l'instant
def VerifPos2(Habitant,i,d,sens,verifchemin):
    #print(Habitant[i].posy, f1ymin(Habitant[i].posx),Habitant[i].posx)
    for j in range(0, nbsurface):
        if Habitant[i].position(Verif[j]):
            Habitant[i].endroit = j
            verifchemin = True
            #print("dans chemin")
    if Habitant[i].endroit != -1 and verifchemin:
        # print(verifchemin)
        # print(Habitant[i].endroit)
        Habitant[i].posx += sens
        if Habitant[i].preendroit != Habitant[i].endroit :
            d = chemin[Habitant[i].endroit][0][1] + fxmax[Habitant[i].endroit](Habitant[i].posx) - Habitant[i].posy
            Habitant[i].preendroit = Habitant[i].endroit
        #positionx += x
        #y = random.uniform(f1xmin(positionx),f1xmax(positionx))

        Habitant[i].posy = chemin[Habitant[i].endroit][0][0]*Habitant[i].posx + d
        #print(chemin[Habitant[i].endroit][0][1],Habitant[i].posx,d)
    return Habitant[i].posx, Habitant[i].posy, Habitant[i].endroit, Habitant[i].preendroit, d, verifchemin

# attribut un numéro aux hab selon la où ils sont, et la où ils étaients avant
def endroit(Habitant, i, nbsurface,Verif,fact2,p,centreisitem,rayonisitem,rayon_cercle):
    for j in range(nbsurface):
        if j != nbsurface-1:  # exclu isitem
            if Habitant[i].position(Verif[j],fact2,p):  # vérifi la position
                if j != Habitant[i].endroit:  # si l'hab était pas déjà la
                    Habitant[i].preendroit = Habitant[i].endroit  # l'ancienne position devient la nouvelle précédente
                    Habitant[i].endroit = j  # mise à jour de la position
                else:
                    Habitant[i].endroit = j  # simple mise à jour de la position
        else:  # pareil mais avec isitem
            if verifisitem(Habitant[i].posx,Habitant[i].posy, centreisitem,rayonisitem,rayon_cercle):
                if j != Habitant[i].endroit:
                    Habitant[i].preendroit = Habitant[i].endroit
                    Habitant[i].endroit = j
                else:
                    Habitant[i].endroit = j
    return Habitant[i].endroit, Habitant[i].preendroit

# vérifie les positions afin que les hab restent dans les surfaces
def collmur(Habitant, i,fact2,points,fxmax,fxmin,fymax,fymin,p,stop):
    rayon = 1
    if not(stop[Habitant[i].endroit]):  # vérifier d'abord qu'il est dedans
        if Habitant[i].posx + rayon > max(points[Habitant[i].endroit][0][0][0], points[Habitant[i].endroit][0][1][0],points[Habitant[i].endroit][1][0][0], points[Habitant[i].endroit][1][1][0]):
            Habitant[i].posx = max(points[Habitant[i].endroit][0][0][0], points[Habitant[i].endroit][0][1][0],points[Habitant[i].endroit][1][0][0], points[Habitant[i].endroit][1][1][0])
        elif Habitant[i].posx + rayon < min(points[Habitant[i].endroit][0][0][0], points[Habitant[i].endroit][0][1][0],points[Habitant[i].endroit][1][0][0], points[Habitant[i].endroit][1][1][0]):
            Habitant[i].posx = min(points[Habitant[i].endroit][0][0][0], points[Habitant[i].endroit][0][1][0],points[Habitant[i].endroit][1][0][0], points[Habitant[i].endroit][1][1][0])
        if Habitant[i].posy + rayon > fxmax[Habitant[i].endroit](Habitant[i].posx,fact2,p):
            # print('sup')
            Habitant[i].posy = fxmax[Habitant[i].endroit](Habitant[i].posx,fact2,p)
        elif Habitant[i].posy + rayon < fxmin[Habitant[i].endroit](Habitant[i].posx,fact2,p):
            # print('inf')
            Habitant[i].posy = fxmin[Habitant[i].endroit](Habitant[i].posx,fact2,p)
        elif Habitant[i].posy < fymin[Habitant[i].endroit](Habitant[i].posx,fact2,p):
            # print('gauche')
            Habitant[i].posy = fymin[Habitant[i].endroit](Habitant[i].posx,fact2,p)
        elif Habitant[i].posy > fymax[Habitant[i].endroit](Habitant[i].posx,fact2,p):
            # print('droite')
            Habitant[i].posy = fymax[Habitant[i].endroit](Habitant[i].posx,fact2,p)
    return Habitant[i].posx, Habitant[i].posy

# pareil que collmur mais pour isitem
def dansisitem(Habitant, i,centreisitem,rayonisitem,stop):
    r = sqrt(abs(Habitant[i].posx-centreisitem[0])**2+abs(Habitant[i].posy-centreisitem[1])**2)
    if not (stop[Habitant[i].endroit]):
        if r**2 > rayonisitem**2:
            if Habitant[i].posx > centreisitem[0] and Habitant[i].posy < centreisitem[1]:
                Habitant[i].posx = centreisitem[0] + rayonisitem * cos(pi/4)
                Habitant[i].posy = centreisitem[1] - rayonisitem * sin(pi/4)
            elif Habitant[i].posx > centreisitem[0] and Habitant[i].posy > centreisitem[1]:
                Habitant[i].posx = centreisitem[0] + rayonisitem * cos(7*pi / 4)
                Habitant[i].posy = centreisitem[1] - rayonisitem * sin(7*pi / 4)
            elif Habitant[i].posx < centreisitem[0] and Habitant[i].posy < centreisitem[1]:
                Habitant[i].posx = centreisitem[0] + rayonisitem * cos(3 * pi / 4)
                Habitant[i].posy = centreisitem[1] - rayonisitem * sin(3 * pi / 4)
            elif Habitant[i].posx < centreisitem[0] and Habitant[i].posy > centreisitem[1]:
                Habitant[i].posx = centreisitem[0] + rayonisitem * cos(5 * pi / 4)
                Habitant[i].posy = centreisitem[1] - rayonisitem * sin(5 * pi / 4)
    return Habitant[i].posx, Habitant[i].posy

def DéplacementPoints2(color, positionx, positiony, val_aleatoire, rayon_cercle, i, test, screen,Habitant,centreisitem,rayonisitem,fact2,points,fxmax,fxmin,fymax,fymin,stop,objectif):
    x = random.uniform(-val_aleatoire,val_aleatoire)  # génère une valeur aléatoire (correspondra au déplacement en x) entre -val_aleatoire et val_aleatoire
    y = random.uniform(-val_aleatoire,val_aleatoire)  # génère une valeur aléatoire (correspondra au déplacement en y) entre -val_aleatoire et val_aleatoire
    #x,y=0,0
    Habitant[i] = hab(color, positionx, positiony, test, x, y, rayon_cercle, i, screen, Habitant[i].endroit,Habitant[i].preendroit,objectif)  # appel la fonction hab
    if -1 < Habitant[i].endroit < 9:
        Habitant[i].posx, Habitant[i].posy = collmur(Habitant, i,fact2,points,fxmax,fxmin,fymax,fymin,p,stop)  # appel la fonction VerifPos
    if Habitant[i].endroit == 9:
        Habitant[i].posx, Habitant[i].posy = dansisitem(Habitant, i,centreisitem,rayonisitem,stop)
    return Habitant, x, y

# inutiliser pour l'instant
def DéplacementPoints3(Habitant,i,val_aleatoire,fact2,points,fxmax,fxmin,fymax,fymin,p,stop,centreisitem,rayonisitem):
    x = random.uniform(-val_aleatoire,val_aleatoire)
    #x=0
    y = random.uniform(-val_aleatoire,val_aleatoire)
    #y=5
    #if not stop[Habitant[i].endroit]:
    Habitant[i].posx += x
    Habitant[i].posy += y
    #Habitant[i].endroit=endroit(Habitant,i,nbsurface,Verif,fact2,p,centreisitem,rayonisitem,rayon_cercle)
    if -1 < Habitant[i].endroit <= 8:
        Habitant[i].posx, Habitant[i].posy = collmur(Habitant, i, fact2, points, fxmax, fxmin, fymax, fymin, p,stop)  # appel la fonction VerifPos
    if Habitant[i].endroit == 9:
        Habitant[i].posx, Habitant[i].posy = dansisitem(Habitant, i, centreisitem, rayonisitem,stop)
    Habitant[i].dessin()  # dessine les points
    return Habitant[i].posx,Habitant[i].posy

# calcul la quantité d'hab par surface
def calculprop(Habitant,i,prop,Verif,fact2,p,centreisitem,rayonisitem,rayon_cercle):
    if -1 < Habitant[i].endroit < 9:
        if Habitant[i].position(Verif[Habitant[i].endroit],fact2,p):
            prop[Habitant[i].endroit] += 1
    if Habitant[i].endroit == 9:
        if verifisitem(Habitant[i].posx,Habitant[i].posy,centreisitem,rayonisitem,rayon_cercle):
            prop[Habitant[i].endroit] += 1
    return prop

# vérifie qu'il n'y a pas trop d'hab dans les surfaces, et les envoies à leur surface d'avant si trop
def verifprop(Habitant,i,prop,pourcent,stop,nbtot,nbsurface,fact2, points, fxmax, fxmin, fymax, fymin, p,centreisitem, rayonisitem,Verif,rayon_cercle):
    for i in range(nbtot):  # stop[surface] = True si trop d'hab dans la surface
        if prop[Habitant[i].endroit] >= pourcent[Habitant[i].endroit]:
            stop[Habitant[i].endroit] = True
    for i in range(nbtot):
        prop = [0 for i in range(nbsurface)]
        if stop[Habitant[i].endroit]:  # si trop d'hab
            Habitant[i].preendroit, Habitant[i].endroit = Habitant[i].endroit,Habitant[i].preendroit # inverse endroit et preendroit
            if Habitant[i].endroit == -1:
                Habitant[i].posx,Habitant[i].posy = 0,0
            elif -1 < Habitant[i].endroit < 9:
                Habitant[i].posx, Habitant[i].posy = collmur(Habitant, i, fact2, points, fxmax, fxmin, fymax, fymin, p,stop)  # appel la fonction VerifPos
            elif Habitant[i].endroit == 9:
                Habitant[i].posx, Habitant[i].posy = dansisitem(Habitant, i, centreisitem, rayonisitem,stop)
            for j in range(nbtot):  # recalcul du nombre d'hab par surface
                prop = calculprop(Habitant, j, prop,Verif,fact2,p,centreisitem,rayonisitem,rayon_cercle)
            if prop[Habitant[i].preendroit] < pourcent[Habitant[i].preendroit]:  # si passé sous la barre du nombre max, alors stop[surface]=False
                stop[Habitant[i].preendroit] = False
    return stop

# inutiliser pour l'instant
def xyobjectif(Habitant,i,val_aleatoire):
    x, y = 0, 0
    alea = random.randint(0, 100)
    if Habitant[i].objectif[0] - Habitant[i].posx < 0 and alea < 50:
        # print(Habitant[i].objectif[0], Habitant[i].posx, Habitant[i].objectif[0] - Habitant[i].posx)
        x = random.uniform(-val_aleatoire, 0)
    elif Habitant[i].objectif[0] - Habitant[i].posx > 0 and alea < 50:
        x = random.uniform(0, val_aleatoire)
    if Habitant[i].objectif[1] - Habitant[i].posy < 0 and alea > 50:
        y = random.uniform(-val_aleatoire, 0)
    elif Habitant[i].objectif[1] - Habitant[i].posy > 0 and alea > 50:
        y = random.uniform(0, val_aleatoire)
    return x,y