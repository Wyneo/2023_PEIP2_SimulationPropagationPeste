import math
import pygame
import os
from modelisation import *
from fonctions import *
#from CheminPlusCourt import *

pygame.init()

clock = pygame.time.Clock()
info = pygame.display.Info()

longueur = 0.93*info.current_w                                           # taille de la fenêtre de jeu en plein écran
hauteur = 0.93*info.current_h
fact = (783/662)                                                     #rapport dimension ancien plan pour la nouvelle fenêtre
fact2 = hauteur/662
#print(int(hauteur*fact),int(hauteur))
#rapport entre nouvelle et ancienne hauteur pour avoir les bonnes coordonnées
WIN = pygame.display.set_mode((int(hauteur),int(hauteur)))
pygame.display.set_caption("modelisation de la ville")
#print (hauteur, fact*hauteur, fact)

WHITE=(255,255,255)                                            #couleurs RGB
GREEN=(0,255,0)
BLACK=(0,0,0)

plan_polytech = pygame.image.load(os.path.join('planpopovierge.png')) #importe image
plan_polytech = pygame.transform.scale(plan_polytech,(hauteur*fact,hauteur))
busc6 = pygame.image.load(os.path.join('c6.jpg'))               #c6
busc6 = pygame.transform.scale(busc6,(fact*25,fact*22))         #diminution taille
buse5 = pygame.image.load(os.path.join('e5.jpg'))               #e5
buse5 = pygame.transform.scale(buse5,(fact*26,fact*22))
bus75 = pygame.image.load(os.path.join('75.jpg'))               #75
bus75 = pygame.transform.scale(bus75,(fact*24,fact*22))
#p = [(fact2*202,fact2*354), (fact2*259,fact2*153), (fact2*352,fact2*176), (fact2*352,fact2*148), (fact2*368,fact2*150), (fact2*368,fact2*180), (fact2*564,fact2*234), (fact2*545,fact2*245), (fact2*363,fact2*197), (fact2*361,fact2*224), (fact2*344,fact2*224), (fact2*347,fact2*192), (fact2*271,fact2*174),(fact2*221,fact2*347)]
p=[(fact2*197,fact2*353), (fact2*254,fact2*152), (fact2*347,fact2*176), (fact2*347,fact2*153),
    (fact2*377,fact2*153), (fact2*377,fact2*178), (fact2*565,fact2*229),  (fact2*559,fact2*253),
    (fact2*371,fact2*202), (fact2*369 ,fact2*226 ), (fact2*344,fact2*224), (fact2*346,fact2*200),
    (fact2*272,fact2*182),(fact2*227,fact2*340),                                                                        #chemins 1 à 6
    (fact2*552,fact2*414), (fact2*338,fact2*406) ,(fact2*326,fact2*381), (fact2*500,fact2*387),                         #chemin ireste isitem
    (fact2*226,fact2*492),                                                                                              #chemin C6
    (fact2*208,fact2*502),(fact2*22,fact2*363), (fact2*7,fact2*383), (fact2*184,fact2*515),                             #chemin 75
    (fact2*160,fact2*529), (fact2*172,fact2*551), (fact2*236,fact2*515),                                                #chemin C6
    (fact2*636,fact2*635), (fact2*390,fact2*525),(fact2*405,fact2*559), (fact2*626,fact2*658)]                          #chemin e5


# p correspond aux coins des chemins, voir schéma pour correspondances

centreisitem,rayonisitem=(fact2*563, fact2*326),fact2*91  # coordonnées du centre d'isitem et son rayon

"""
def draw_window(x,y):
    WIN.fill(WHITE)                                                         #fond blanc
    #WIN.blit(super_uu,(300,100))
    WIN.blit(plan_polytech,(0,0))
    pygame.draw.polygon(WIN, (0,150,0), [(fact2*202,fact2*354), (fact2*259,fact2*153), (fact2*271,fact2*174),(fact2*221,fact2*347)])        # chemin 1 = chemin sortant d'Ireste
    pygame.draw.polygon(WIN, (0,65,200), [(fact2*259,fact2*153), (fact2*352,fact2*176), (fact2*347,fact2*192), (fact2*271,fact2*174)])       # chemin 2 = chemin entre le chemin 1 (la ou le chemin fait un coude) et l'intersection au niveau de IHT et le RU (chemin 3)
    pygame.draw.polygon(WIN, (255, 165, 100), [(fact2*352,fact2*176), (fact2*368,fact2*180), (fact2*363,fact2*197), (fact2*347,fact2*192)])   # chemin 3 = intersection au niveau de IHT et le RU
    pygame.draw.polygon(WIN, (100, 65, 200), [(fact2*368,fact2*180), (fact2*564,fact2*234), (fact2*545,fact2*245), (fact2*363,fact2*197)])   # chemin 4 = chemin entre intersection (chemin 3) et Isitem
    pygame.draw.polygon(WIN, (255, 119, 165), [(fact2*363,fact2*197), (fact2*361,fact2*224), (fact2*344,fact2*224), (fact2*347,fact2*192)])   # chemin 5 = chemin entre intersection (chemin 3) et le RU
    pygame.draw.polygon(WIN, (255, 105, 30), [(fact2*352,fact2*176), (fact2*352,fact2*148), (fact2*368,fact2*150), (fact2*368,fact2*180)])     # chemin 6 = chemin entre intersection (chemin 3) et IHT

    for i in range(len(p)-1):                                                          #chemins
        if i!=3 and i!=6 and i!=9:
            pygame.draw.line(WIN,BLACK,p[i],p[i+1])
    pygame.draw.polygon(WIN,BLACK,[(fact2*295,fact2*310),(fact2*416,fact2*584),(fact2*292,fact2*636),(fact2*168,fact2*366)])           #ireste
    pygame.draw.polygon(WIN, BLACK, [(fact2*484, fact2*168), (fact2*302, fact2*62), (fact2*263,fact2*138)])               #IHT
    pygame.draw.circle(WIN, BLACK, centreisitem, rayonisitem)                                     #isitem
    pygame.draw.polygon(WIN, BLACK, [(fact2*381,fact2*206),(fact2*425,fact2*301),(fact2*384,fact2*317),(fact2*338,fact2*223)])         #RU

    WIN.blit(busc6,(fact2*153,fact2*530))                                                          #c6
    WIN.blit(bus75,(fact2*6,fact2*364))                                                            #75
    WIN.blit(buse5,(fact2*618,fact2*634))                                                          #e5
"""
"""
def f7xmax (x,fact2,p):
    a, b = fonctlin(p[14][0], p[14][1], p[15][0], p[15][1])
    f = a * x + b * fact2
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def f7xmin (x,fact2,p):
    a, b = fonctlin(p[17][0], p[17][1], p[16][0], p[16][1])
    f = a * x + b * fact2
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def f7ymin (x,fact2,p):
    a,b = fonctlin(p[16][0],p[16][1],p[15][0],p[15][1])
    f= a * x + b * fact2
    #pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def f7ymax (x,fact2,p):
    a,b = fonctlin(p[17][0],p[17][1],p[14][0],p[14][1])
    f= a * x + b
    pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
"""
def draw_window(x,y):
    WIN.fill(WHITE)                                                         #fond blanc
    WIN.blit(plan_polytech,(0,0))
    pygame.draw.polygon(WIN, BLACK,
        [(fact2 * 174, fact2 * 385), (fact2 * 220, fact2 * 365), (fact2 * 248, fact2 * 421),
         (fact2 * 260, fact2 * 415), (fact2 * 223, fact2 * 340), (fact2 * 295, fact2 * 309),
         (fact2 * 381, fact2 * 502), (fact2 * 353, fact2 * 516), (fact2 * 364, fact2 * 544),
         (fact2 * 373, fact2 * 540), (fact2 * 400, fact2 * 595), (fact2 * 349, fact2 * 617),
         (fact2 * 338, fact2 * 594), (fact2 * 327, fact2 * 599), (fact2 * 333, fact2 * 611),
         (fact2 * 288, fact2 * 632), (fact2 * 238, fact2 * 527), (fact2 * 252, fact2 * 479),
         (fact2 * 222, fact2 * 492)])          #ireste
    pygame.draw.polygon(WIN, BLACK,
                            [(fact2 * 266, fact2 * 140), (fact2 * 283, fact2 * 113), (fact2 * 272, fact2 * 95),
                             (fact2 * 283, fact2 * 96), (fact2 * 300, fact2 * 62), (fact2 * 382, fact2 * 104),
                             (fact2 * 371, fact2 * 109), (fact2 * 469, fact2 * 160), (fact2 * 463, fact2 * 170),
                             (fact2 * 389, fact2 * 158), (fact2 * 357, fact2 * 128), (fact2 * 346, fact2 * 155)])               #IHT
    pygame.draw.circle(WIN, BLACK, (fact2*563, fact2*326), fact2*91)                                     #isitem
    pygame.draw.polygon(WIN, BLACK, [(fact2 * 384, fact2 * 318), (fact2 * 359, fact2 * 263), (fact2 * 355, fact2 * 264),
                                    (fact2 * 337, fact2 * 223), (fact2 * 354, fact2 * 215), (fact2 * 360, fact2 * 222),
                                    (fact2 * 384, fact2 * 211), (fact2 * 424, fact2 * 299)])        #RU
    WIN.blit(busc6,(fact2*153,fact2*530))                                                          #c6
    WIN.blit(bus75,(fact2*6,fact2*364))                                                            #75
    WIN.blit(buse5,(fact2*618,fact2*634))                                                          #e5

    #pygame.draw.line(WIN, (200,0,0), (fact2 * 330, fact2 * 386), (fact2 * 552, fact2 * 414))  # chemin ireste isitem
    #pygame.draw.line(WIN, (0, 0, 200), p[14], p[15])
    #pygame.draw.line(WIN, (0,0,200), (fact2* 377,fact2* 176),(fact2* 377,fact2* 153), 5)
    #pygame.draw.line(WIN, (200, 0, 0), (fact2* 347, fact2* 176), (fact2* 347, fact2* 153), 5)
    #pygame.draw.line(WIN, (0, 00, 0), (fact2* 364, fact2* 226), (fact2* 367, fact2* 194), 5)
    #pygame.draw.line(WIN, (200, 0, 0), (fact2 * 334, fact2 * 223), (fact2 * 337, fact2 * 191), 5)

    #pygame.draw.line(WIN, BLACK, (fact2 * 160, fact2 * 539), (fact2 * 250, fact2 * 489))  # chemin C6
    #pygame.draw.line(WIN, BLACK, (fact2 * 13, fact2 * 375), (fact2 * 222, fact2 * 505))  # chemin 75
    #pygame.draw.line(WIN, BLACK, (fact2 * 630, fact2 * 649), (fact2 * 354, fact2 * 525))  # chemin E5



    for i in range(len(p)-1):                                                          #chemins
        if i!=3 and i!=6 and i!=9 and i!=13 and i!=15 and i!= 17 and i!=20 and i!=23 and i!=25 and i!=27 :
            pygame.draw.line(WIN,(0,0,200),p[i],p[i+1],3)



X = 400*fact2  # taille de la fenêtre pygame
Y = 200*fact2
nbsurface = 10
d = 1  # utilisé dans VerifPos2 fonction non utilisé actuellement
#chemin1 = False
test = 0  # correspond au nombre de tour de boucle
#Verif = [verifchemin1,verifchemin2,verifchemin3,verifchemin4,verifchemin5,verifchemin6,verifchemin7,verifchemin8,verifchemin9,verifchemin10,verifireste,verifru,verifiht,verifisitem]  # tableau contenant les fonctions de vérification
#fxmax = [f1xmax,f2xmax,f3xmax,f4xmax,f5xmax,f6xmax,f7xmax,f8xmax,f9xmax,f10xmax,firestexmax,fruxmax,fihtxmax]
#fxmin = [f1xmin,f2xmin,f3xmin,f4xmin,f5xmin,f6xmin,f7xmin,f8xmin,f9xmin,f10xmin,firestexmin,fruxmin,fihtxmin]
#fymax = [f1ymax,f2ymax,f3ymax,f4ymax,f5ymax,f6ymax,f7ymax,f8ymax,f9ymax,f10ymax,firesteymax,fruymax,fihtymax]
#fymin = [f2xmin,f1xmax,f3ymin,f4ymin,f5ymin,f6ymin,f7ymin,f8ymin,f9ymin,f10ymin,firesteymin,fruymin,fihtymin]

Verif = [verifchemin1,verifchemin2,verifchemin3,verifchemin4,verifchemin5,verifchemin6,verifireste,verifru,verifiht,verifisitem]  # tableau contenant les fonctions de vérification
fxmax = [f1xmax,f2xmax,f3xmax,f4xmax,f5xmax,f6xmax,firestexmax,fruxmax,fihtxmax]
fxmin = [f1xmin,f2xmin,f3xmin,f4xmin,f5xmin,f6xmin,firestexmin,fruxmin,fihtxmin]
fymax = [f1ymax,f2ymax,f3ymax,f4ymax,f5ymax,f6ymax,firesteymax,fruymax,fihtymax]
fymin = [f2xmin,f1xmax,f3ymin,f4ymin,f5ymin,f6ymin,firesteymin,fruymin,fihtymin]

chemin = [[[- 3.53,1066.32 * fact2],[-3.46,1111.66 * fact2]],
          [[0.25,88.95 * fact2],[0.24,109.82 * fact2]],
          [[0.25,88 * fact2],[0.31,83.56 * fact2]],
          [[0.28,78.61 * fact2],[0.26,101.26 * fact2]],
          [[-10.67,3893.33 * fact2],[-13.5,5097.5 * fact2]],
          [[-23,8249 * fact2],[-25,9355 * fact2]]] #[[[chemin1 xmin a,b],[chemin1 xmax a,b]],[]]  Utilisé dans VerifPos2
points = [[[p[0],p[1]],[p[13],p[12]]],
          [[p[1],p[2]],[p[12],p[11]]],
          [[p[2],p[5]],[p[11],p[8]]],
          [[p[5],p[6]],[p[8],p[7]]],
          [[p[10],p[11]],[p[9],p[8]]],
          [[p[2],p[3]],[p[5],p[4]]],
          [[(fact2*416,fact2*584),(fact2*295,fact2*309)],[(fact2*292,fact2*636),(fact2*168,fact2*365)]],
          [[(fact2*425,fact2*301),(fact2*381,fact2*206)],[(fact2*384,fact2*317),(fact2*338,fact2*223)]],
          [[(fact2*263,fact2*138),(fact2*302,fact2*62)],[(fact2*484,fact2*168),(fact2*302,fact2*62)]]] #[[[chemin1 fxmin],[chemin1 fxmax]],]  Points répertoriés par surface, d'abord ceux correspondant à fxmin puis ceux fxmax

#points = [[[p[0],p[1]],[p[13],p[12]]],
#          [[p[1],p[2]],[p[12],p[11]]],
 #         [[p[2],p[5]],[p[11],p[8]]],
  #        [[p[5],p[6]],[p[8],p[7]]],
   #       [[p[10],p[11]],[p[9],p[8]]],
     #     [[p[2],p[3]],[p[5],p[4]]],
      #    [[p[15],p[16]],[p[14],p[17]]],
       #   [[p[24],p[23]],[p[25],p[18]]],
        #  [[p[22],p[21]],[p[19],p[20]]],
         # [[p[28],p[27]],[p[29],p[26]]],
          #[[(fact2*416,fact2*584),(fact2*295,fact2*309)],[(fact2*292,fact2*636),(fact2*168,fact2*365)]],
          #[[(fact2*425,fact2*301),(fact2*381,fact2*206)],[(fact2*384,fact2*317),(fact2*338,fact2*223)]],
          #[[(fact2*263,fact2*138),(fact2*302,fact2*62)],[(fact2*484,fact2*168),(fact2*302,fact2*62)]]]

stop = [False for i in range(nbsurface)]  # tableau contenant des booléens, false tant qu'il n'y a pas trop de d'hab dans la surface
pourcent = [1000 for i in range(nbsurface)]  # nombre d'hab autorisés dans chaque surface
depart = [[300,450] if i < 100 else [400,290] if 100 <= i < 200 else [350,130] if 200 <= i < 300 else [centreisitem[0],centreisitem[1]] for i in range(nbtot)] # coordonées des points de départ
#departrat=[[300,450] if i < nbvert + nbjaune + 5 else [450,210] if nbvert + nbjaune + 5<= i < nbvert + nbjaune+10 else [600,400] if nbvert + nbjaune+10<= i < nbvert + nbjaune+15 else [310,180] if nbvert + nbjaune+15<= i < nbvert + nbjaune+20 else [350,140] for i in range(nbvert + nbjaune, nbvert + nbjaune + nbrat)]
objct = [[168,366] for i in range(nbtot)]  # coordonnés des objectifs de chaque hab




#initialisation

for i in range(nbtot):
    preendroit1 = -1
    endroit1 = -1
    cercle = habitant('white', depart[i][0],depart[i][1], test, rayon_cercle, WIN, endroit1, preendroit1, objct[i])
    #cercle = habitant('white', 300,450, test, rayon_cercle, WIN, endroit1, preendroit1, objct[i])
    Habitant.append(cercle)
    R0.append(0)  # initialisation de la liste
    couleur.append(0)  # initialisation de la liste

# attribution de la couleur de chaque hab, et positionnement

# ATTENTION dans DéplacementPoints2 x,y=0,0


for i in range(nbvert):
    Habitant, x1, y1 = DéplacementPoints2('green', Habitant[i].posx, Habitant[i].posy, val_aleatoire, rayon_cercle, i,test,WIN,Habitant,centreisitem,rayonisitem,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif)  # appel la fonction DéplacementPoints
for j in range(nbvert, nbvert + nbjaune):
    Habitant, x3, y3 = DéplacementPoints2('yellow', Habitant[j].posx, Habitant[j].posy, val_aleatoire, rayon_cercle, j,test,WIN,Habitant,centreisitem,rayonisitem,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif)
for k1 in range(nbvert + nbjaune, nbvert + nbjaune + int(nbrat/2)):  # positionnement des premiers rats
    Habitant, x4, y4 = DéplacementPoints2('gray', 245,270, val_aleatoire, rayon_cercle, k1,test,WIN,Habitant,centreisitem,rayonisitem,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif)
for k2 in range(nbvert + nbjaune + int(nbrat/2),nbvert + nbjaune + nbrat):  # positionnement des autres rats
    Habitant, x4, y4 = DéplacementPoints2('gray', 450,210, val_aleatoire, rayon_cercle, k2, test, WIN, Habitant,centreisitem,rayonisitem,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif)
for m in range(nbvert + nbjaune + nbrat, nbvert + nbjaune + nbrat + nbrouge):
    Habitant, x2, y2 = DéplacementPoints2('red', Habitant[m].posx, Habitant[m].posy, val_aleatoire, rayon_cercle,m,test,WIN,Habitant,centreisitem,rayonisitem,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif)


#fonction principale

continuer = True
simulation_active=True
while continuer:  # boucle infinie
    for event in pygame.event.get():
        if event.type == pyl.QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
            continuer = False
    #if nbrat == 0:  # la simulation s'arrête s'il n'y a plus de rats
     #   continuer = False
    if simulation_active:  # si on veut que la simul continue
        draw_window(X,Y)
        #f7xmax(Habitant[i].posx, fact2, p)
       # f7xmin(Habitant[i].posx, fact2, p)
        #f7ymax(Habitant[i].posx, fact2, p)
        #f7ymin(Habitant[i].posx, fact2, p)
        #verifchemin = False
        font = pygame.font.Font(None, int(hauteur*fact / 30))
        time1 = pygame.time.get_ticks()  # temps de départ
        time2 = int(time1 / 1000)  # transforme time1 en seconde
        text = font.render(str(time2), True, 'black')  # transforme en texte time2
        nbboucle = font.render(str(test), True, 'black')  # transforme en texte test, correspond au nombre de boucle
        prop = [0 for i in range(nbsurface)]  # table contenant le nombre d'hab dans chaque surface
        #nb_colonnes = int(hauteur)
        #nb_lignes = int(hauteur)
        for i in range(nbtot):
            #print(Habitant[i].objectif[0])
            #if -1<Habitant[i].endroit <=3:
                #x,y=xyobjectif(Habitant,i)
            #else:
            x = random.uniform(-val_aleatoire, val_aleatoire)
            y = random.uniform(-val_aleatoire, val_aleatoire)
            Habitant[i].posx += x
            Habitant[i].posy += y

            Habitant[i].endroit, Habitant[i].preendroit = endroit(Habitant, i, nbsurface, Verif, fact2, p, centreisitem,rayonisitem,rayon_cercle)  # attribut un numéro aux hab selon la où ils sont

            #print(Habitant[i].endroit)
            #tab, Habitant[i].posx,Habitant[i].posy = algo([int(Habitant[i].posx), int(Habitant[i].posy)], [600, 400],Verif,Habitant,i,fact2,p,nb_colonnes,nb_lignes,centreisitem,rayonisitem,rayon_cercle,draw_window)
            #print(test,Habitant[i].posx,Habitant[i].posy)
            #Habitant[i].posx += tab[test][0]
            #Habitant[i].posy += tab[test][1]


            if -1 < Habitant[i].endroit < nbsurface-1:  # si pas nul part et pas dans isitem
                Habitant[i].posx, Habitant[i].posy = collmur(Habitant, i, fact2, points, fxmax, fxmin, fymax, fymin, p,stop)  # appel la fonction collmur
            if Habitant[i].endroit == nbsurface-1:  # si dans isitem
                Habitant[i].posx, Habitant[i].posy = dansisitem(Habitant, i, centreisitem, rayonisitem,stop)  # appel la fonction dans isitem
            Habitant[i].dessin()  # dessine les points
            nbjaune, nbrouge = verifTempsSup('yellow', 'red', nbjaune, nbrouge, tattjr, factjr, i,test)  # les points jaunes deviennent rouges au bout d'un moment
            nbrouge, nbmort = verifTempsSup('red', 'black', nbrouge, nbmort, tattrn, factrn, i,test)  # les points rouges deviennent noirs (meurent) au bout d'un moment
            nbjaune, nbvert = verifTempsInf('yellow', 'green', nbjaune, nbvert, tattjv, factjv, i,test)  # les points jaunes deviennent verts (guérissent) tant que le temps est pas dépassé
            nbjaune, nbmort = verifTempsSup('yellow', 'black', nbjaune, nbmort, tattjn, factjn, i,test)  # les points jaunes deviennent noirs (meurent) au bout d'un moment
            n, nbrat, nbmort = rat('gray', 'black', nbrat, nbmort, test, tattgn, n,i)  # les points gris (rats) deviennent noirs (meurent) au bout d'un moment
            nbrouge, nbvert = verifTempsInf('red', 'green', nbrouge, nbvert, tattrv, factrv, i,test)  # les points rouges deviennent verts (guérissent) tant que le temps est pas dépassé
            if Habitant[i].color == 'red':  # si le point est rouge on met 'r' dans le tableau afin de savoir à la fin qui a été rouge à un momen t
                couleur[i] = 'r'
            prop = calculprop(Habitant,i,prop,Verif,fact2,p,centreisitem,rayonisitem,rayon_cercle)  # calcule le nombre d'hab dans les surfaces

        stop = verifprop(Habitant,i,prop,pourcent,stop,nbtot,nbsurface,fact2, points, fxmax, fxmin, fymax, fymin, p,centreisitem, rayonisitem,Verif,rayon_cercle)  # vérifie qu'il n'y a pas trop d'hab dans les surfaces, et les envoies à leur surface d'avant si trop
        nbvert, nbrouge = collision('green', 'red', nbvert, nbrouge, nbtot, rayon_cercle, factvr,test)  # appel la fonction collision : les points verts sont contaminés par les rouges
        nbvert, nbjaune = collision2('gray', 'green', 'yellow', nbrat, nbvert, nbjaune, nbtot, rayon_cercle, factgvj,test)  # appel la fonction collision2 : les points gris (rats) contaminent les verts  qui deviennent jaunes
        WIN.blit(text, (hauteur*fact / 100, hauteur / 100))  # affiche le texte sur le fond
        WIN.blit(nbboucle, (300, 10))  # affiche le nombre de tours
    clock.tick(vitesse_affichage)
    pygame.display.update()
    test += 1  # on compte le nombre de tours

for i in range(nbtot):
    if couleur[i] == 'r':
        sommeR0 += R0[i]
        nbrougetot += 1
print(test)
print("nbvert restant : ", nbvert)
print("nb de contaminations : ", sommeR0)
print("nb de rouge total : ", nbrougetot)
print("R0 : ", sommeR0/nbrougetot)




pygame.quit()