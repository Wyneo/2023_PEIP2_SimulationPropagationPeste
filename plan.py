import math
import pygame
import os
from modelisation import *
from fonctions import *
from CheminPlusCourt import *

pygame.init()

clock = pygame.time.Clock()
info = pygame.display.Info()

longueur = 0.93*info.current_w                                           # taille de la fenêtre de jeu en plein écran
hauteur = 0.93*info.current_h
fact = (783/662)                                                     #rapport dimension ancien plan pour la nouvelle fenêtre
fact2 = hauteur/662
#print(int(hauteur))
#rapport entre nouvelle et ancienne hauteur pour avoir les bonnes coordonnées
WIN = pygame.display.set_mode((int(hauteur),int(hauteur)))
pygame.display.set_caption("modelisation de la ville")
#print (hauteur, fact*hauteur, fact)

WHITE=(255,255,255)                                            #couleurs RGB
GREEN=(0,255,0)
BLACK=(0,0,0)

plan_polytech = pygame.image.load(os.path.join('planpopovierge.png')) #importe image
plan_polytech = pygame.transform.scale(plan_polytech,(int(hauteur),int(hauteur)))
busc6 = pygame.image.load(os.path.join('c6.jpg'))               #c6
busc6 = pygame.transform.scale(busc6,(fact*25,fact*22))         #diminution taille
buse5 = pygame.image.load(os.path.join('e5.jpg'))               #e5
buse5 = pygame.transform.scale(buse5,(fact*26,fact*22))
bus75 = pygame.image.load(os.path.join('75.jpg'))               #75
bus75 = pygame.transform.scale(bus75,(fact*24,fact*22))
#p = [(fact2*202,fact2*354), (fact2*259,fact2*153), (fact2*352,fact2*176), (fact2*352,fact2*148), (fact2*368,fact2*150), (fact2*368,fact2*180), (fact2*564,fact2*234), (fact2*545,fact2*245), (fact2*363,fact2*197), (fact2*361,fact2*224), (fact2*344,fact2*224), (fact2*347,fact2*192), (fact2*271,fact2*174),(fact2*221,fact2*347)]
p=[(fact2*197,fact2*353), (fact2*254,fact2*152), (fact2*347,fact2*176), (fact2*347+1,fact2*153),
    (fact2*377+1,fact2*153), (fact2*377,fact2*178), (fact2*565,fact2*229),  (fact2*559,fact2*253),
    (fact2*371,fact2*202), (fact2*369 ,fact2*226 ), (fact2*344,fact2*224), (fact2*346,fact2*200),
    (fact2*272,fact2*182),(fact2*227,fact2*340),                                                                        #chemins 1 à 6
    (fact2*552,fact2*414), (fact2*338,fact2*406) ,(fact2*326,fact2*381), (fact2*500,fact2*387),                         #chemin ireste isitem
    (fact2*226,fact2*492),                                                                                              #chemin C6
    (fact2*208,fact2*502),(fact2*22,fact2*363), (fact2*7,fact2*383), (fact2*184,fact2*515),                             #chemin 75
    (fact2*160,fact2*529), (fact2*172,fact2*551), (fact2*236,fact2*515),                                                #chemin C6
    (fact2*610,fact2*624), (fact2*390,fact2*525),(fact2*405,fact2*559), (fact2*626,fact2*658),                          #chemin e5
    (fact2*178,fact2*260),(fact2*219,fact2*276),(fact2*212,fact2*300),(fact2*170,fact2*284)]                                    #chemin 11
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
def fruxmin(x,fact2,p):
    a,b = fonctlin(fact2*425,fact2*301,fact2*381,fact2*206)
    f = a*x + b
    pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fruxmax(x,fact2,p):
    a,b = fonctlin(fact2*384,fact2*317,fact2*338,fact2*223)
    f = a*x + b
    pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fruymin(x,fact2,p):
    a,b=fonctlin(fact2*381,fact2*206,fact2*338,fact2*223)
    f = a*x + b
    pygame.draw.line(WIN, BLACK, (0, a * 0 + b), (1000, a * 1000 + b))
    return f
def fruymax(x,fact2,p):
    a,b = fonctlin(fact2*384,fact2*317,fact2*425,fact2*301)
    f = a*x + b
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
    pygame.draw.circle(WIN,BLACK,(infocercles[15][0][0],infocercles[15][0][1]),infocercles[15][1]) #C6
    pygame.draw.circle(WIN, BLACK, (infocercles[16][0][0], infocercles[16][0][1]), infocercles[16][1]) #parking
    pygame.draw.circle(WIN, BLACK, (infocercles[17][0][0], infocercles[17][0][1]), infocercles[17][1]) #E5
    pygame.draw.circle(WIN, BLACK, (infocercles[18][0][0], infocercles[18][0][1]), infocercles[18][1]) #75
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
        if i!=3 and i!=6 and i!=9 and i!=13 and i!=15 and i!= 17 and i!=20 and i!=23 and i!=25 and i!=27 and i!=29:
            pygame.draw.line(WIN,(0,0,200),p[i],p[i+1],3)



X = 400*fact2  # taille de la fenêtre pygame
Y = 200*fact2
nbsurface = 19
d = 1  # utilisé dans VerifPos2 fonction non utilisé actuellement
#chemin1 = False
test = 0  # correspond au nombre de tour de boucle
Verif = [verifchemin1,verifchemin2,verifchemin3,verifchemin4,verifchemin5,verifchemin6,verifchemin7,verifchemin8,verifchemin9,verifchemin10,verifchemin11,verifireste,verifru,verifiht,verifisitem,verifC6,verifparking,verifE5,verif75]  # tableau contenant les fonctions de vérification
fxmax = [f1xmax,f2xmax,f3xmax,f4xmax,f5xmax,f6xmax,f7xmax,f8xmax,f9xmax,f10xmax,f11xmax,firestexmax,fruxmax,fihtxmax]
fxmin = [f1xmin,f2xmin,f3xmin,f4xmin,f5xmin,f6xmin,f7xmin,f8xmin,f9xmin,f10xmin,f11xmin,firestexmin,fruxmin,fihtxmin]
fymax = [f1ymax,f2ymax,f3ymax,f4ymax,f5ymax,f6ymax,f7ymax,f8ymax,f9ymax,f10ymax,f11ymax,firesteymax,fruymax,fihtymax]
fymin = [f1ymin,f2ymin,f3ymin,f4ymin,f5ymin,f6ymin,f7ymin,f8ymin,f9ymin,f10ymin,f11ymin,firesteymin,fruymin,fihtymin]
infocercles=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,[(fact2*563, fact2*326),fact2*91],[(fact2*153,fact2*530+fact*22/2),40],[(fact2*156,fact2*264),40],[(fact2*618+fact*26/2,fact2*634+fact*22/2),40],[(fact2*6,fact2*364),40]]  # [[(centreisitemx,centreisitemy),rayonisitem],[C6],[Parking],[E5],[75]]
# ATTENTION CENTRE SUR LES COINS POUR L'INSTANT


#Verif = [verifchemin1,verifchemin2,verifchemin3,verifchemin4,verifchemin5,verifchemin6,verifireste,verifru,verifiht,verifisitem]  # tableau contenant les fonctions de vérification
#fxmax = [f1xmax,f2xmax,f3xmax,f4xmax,f5xmax,f6xmax,firestexmax,fruxmax,fihtxmax]
#fxmin = [f1xmin,f2xmin,f3xmin,f4xmin,f5xmin,f6xmin,firestexmin,fruxmin,fihtxmin]
#fymax = [f1ymax,f2ymax,f3ymax,f4ymax,f5ymax,f6ymax,firesteymax,fruymax,fihtymax]
#fymin = [f2xmin,f1xmax,f3ymin,f4ymin,f5ymin,f6ymin,firesteymin,fruymin,fihtymin]

chemin = [[[- 3.53,1066.32 * fact2],[-3.46,1111.66 * fact2]],
          [[0.25,88.95 * fact2],[0.24,109.82 * fact2]],
          [[0.25,88 * fact2],[0.31,83.56 * fact2]],
          [[0.28,78.61 * fact2],[0.26,101.26 * fact2]],
          [[-10.67,3893.33 * fact2],[-13.5,5097.5 * fact2]],
          [[-23,8249 * fact2],[-25,9355 * fact2]]] #[[[chemin1 xmin a,b],[chemin1 xmax a,b]],[]]  Utilisé dans VerifPos2, inutilisé pour l'instant
#points = [[[p[0],p[1]],[p[13],p[12]]],
 #         [[p[1],p[2]],[p[12],p[11]]],
  #        [[p[2],p[5]],[p[11],p[8]]],
   #       [[p[5],p[6]],[p[8],p[7]]],
    #      [[p[10],p[11]],[p[9],p[8]]],
     #     [[p[2],p[3]],[p[5],p[4]]],
      #    [[(fact2*416,fact2*584),(fact2*295,fact2*309)],[(fact2*292,fact2*636),(fact2*168,fact2*365)]],
       #   [[(fact2*425,fact2*301),(fact2*381,fact2*206)],[(fact2*384,fact2*317),(fact2*338,fact2*223)]],
        #  [[(fact2*263,fact2*138),(fact2*302,fact2*62)],[(fact2*484,fact2*168),(fact2*302,fact2*62)]]] #[[[chemin1 fxmin],[chemin1 fxmax]],]  Points répertoriés par surface, d'abord ceux correspondant à fxmin puis ceux fxmax

points = [[[p[0],p[1]],[p[13],p[12]]],
          [[p[1],p[2]],[p[12],p[11]]],
          [[p[2],p[5]],[p[11],p[8]]],
          [[p[5],p[6]],[p[8],p[7]]],
          [[p[10],p[11]],[p[9],p[8]]],
          [[p[2],p[3]],[p[5],p[4]]],
          [[p[15],p[16]],[p[14],p[17]]],
          [[p[24],p[23]],[p[25],p[18]]],
          [[p[22],p[21]],[p[19],p[20]]],
          [[p[26],p[29]],[p[28],p[27]]],
          [[p[30],p[33]],[p[31],p[32]]],
          [[(fact2*416,fact2*584),(fact2*295,fact2*309)],[(fact2*292,fact2*636),(fact2*168,fact2*365)]],
          [[(fact2*425,fact2*301),(fact2*381,fact2*206)],[(fact2*384,fact2*317),(fact2*338,fact2*223)]],
          [[(fact2*263,fact2*138),(fact2*302,fact2*62)],[(fact2*484,fact2*168),(fact2*302,fact2*62)]]]

stop = [False for i in range(nbsurface)]  # tableau contenant des booléens, false tant qu'il n'y a pas trop de d'hab dans la surface
autorisation = [50/100*(nbtot-nbrat-nbmort) if i == 11 else 30/100*(nbtot-nbrat-nbmort) if i == 14 else 0 if i == 12 else 20/100*(nbtot-nbrat-nbmort) if i == 13 else nbtot+1 for i in range(nbsurface)]  # nombre d'hab autorisés dans chaque surface
#autorisation = [1000 for i in range(nbsurface)]  # nombre d'hab autorisés dans chaque surface

#print(autorisation)
#depart = [[300,450] if i < 100 else [400,290] if 100 <= i < 200 else [350,130] if 200 <= i < 300 else [centreisitem[0],centreisitem[1]] for i in range(nbtot)] # coordonées des points de départ
depart = [[fact2*618,fact2*634] if i < 17/100*(nbtot-nbrat-nbmort) else [fact2*156,fact2*264] if 17/100*(nbtot-nbrat-nbmort) <= i < (17+39)/100*(nbtot-nbrat-nbmort) else [fact2*153,fact2*530] if (17+39)/100*(nbtot-nbrat-nbmort) <= i < (17+39+42)/100*(nbtot-nbrat-nbmort) else [fact2*6,fact2*364] if (17+39+42)/100*(nbtot-nbrat-nbmort) <= i < (nbtot-nbrat-nbmort) else [hauteur/2,hauteur/2] for i in range(nbtot)] # coordonées des points de départ E5,parking,C6,75
#departrat=[[300,450] if i < nbvert + nbjaune + 5 else [450,210] if nbvert + nbjaune + 5<= i < nbvert + nbjaune+10 else [600,400] if nbvert + nbjaune+10<= i < nbvert + nbjaune+15 else [310,180] if nbvert + nbjaune+15<= i < nbvert + nbjaune+20 else [350,140] for i in range(nbvert + nbjaune, nbvert + nbjaune + nbrat)]
objct = [[168,366] for i in range(nbtot)]  # coordonnés des objectifs de chaque hab
verifru = False

#print(tattRUinf,tattRUsup)



#initialisation

for i in range(nbtot):
    preendroit1 = -1
    endroit1 = -1
    cercle = habitant('white', depart[i][0],depart[i][1], test, rayon_cercle, WIN, endroit1, preendroit1, objct[i])
    #cercle = habitant('white',360,170, test, rayon_cercle, WIN, endroit1, preendroit1, objct[i])
    Habitant.append(cercle)
    R0.append(0)  # initialisation de la liste
    couleur.append(0)  # initialisation de la liste


# attribution de la couleur de chaque hab, et positionnement

# ATTENTION dans DéplacementPoints2 x,y=0,0


for i in range(nbvert):
    Habitant, x1, y1 = DéplacementPoints2('green', Habitant[i].posx, Habitant[i].posy, val_aleatoire, rayon_cercle, i, test,WIN,Habitant,infocercles,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif,p,nbsurface,Verif)  # appel la fonction DéplacementPoints
for j in range(nbvert, nbvert + nbjaune):
    Habitant, x3, y3 = DéplacementPoints2('yellow', Habitant[j].posx, Habitant[j].posy, val_aleatoire, rayon_cercle, j, test,WIN,Habitant,infocercles,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif,p,nbsurface,Verif)
for k in range(nbvert + nbjaune, nbvert + nbjaune + nbrat):  # positionnement des premiers rats
    Habitant, x4, y4 = DéplacementPoints2('gray', hauteur/2,hauteur/2, val_aleatoire, rayon_cercle, k,test,WIN,Habitant,infocercles,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif,p,nbsurface,Verif)
"""
for k1 in range(nbvert + nbjaune, nbvert + nbjaune + int(nbrat/3)):  # positionnement des premiers rats
    Habitant, x4, y4 = DéplacementPoints2('gray', 238,270, val_aleatoire, rayon_cercle, k1,test,WIN,Habitant,infocercles,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif,p,nbsurface,Verif)
for k2 in range(nbvert + nbjaune + int(nbrat/3),nbvert + nbjaune + int(2*nbrat/3)):  # positionnement des autres rats
    Habitant, x4, y4 = DéplacementPoints2('gray', 470,217, val_aleatoire, rayon_cercle, k2, test, WIN, Habitant, infocercles,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif,p,nbsurface,Verif)
for k3 in range(nbvert + nbjaune + int(2*nbrat/3),nbvert + nbjaune + nbrat):  # positionnement des autres rats
    Habitant, x4, y4 = DéplacementPoints2('gray', 300,177, val_aleatoire, rayon_cercle, k3, test, WIN, Habitant, infocercles,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif,p,nbsurface,Verif)
"""
for m in range(nbvert + nbjaune + nbrat, nbvert + nbjaune + nbrat + nbrouge):
    Habitant, x2, y2 = DéplacementPoints2('red', Habitant[m].posx, Habitant[m].posy, val_aleatoire, rayon_cercle,m,test,WIN,Habitant,infocercles,fact2,points,fxmax,fxmin,fymax,fymin,stop,Habitant[i].objectif,p,nbsurface,Verif)

#nb_colonnes = int(hauteur)
#nb_lignes = int(hauteur)
#tab = algo([int(Habitant[i].posx), int(Habitant[i].posy)], [300, 350], Verif, Habitant, i, fact2, p, nb_colonnes,nb_lignes, infocercles, rayon_cercle, draw_window)

#fonction principale

continuer = True
simulation_active = True
while continuer:  # boucle infinie
    for event in pygame.event.get():
        if event.type == pyl.QUIT:  # quiter le prog et que ça fasse pas une boucle infinie
            continuer = False
    if nbrat == 0:  # la simulation s'arrête s'il n'y a plus de rats
        continuer = False
    if simulation_active:  # si on veut que la simul continue
        draw_window(X,Y)
        fruxmax(Habitant[i].posx, fact2, p)
        fruxmin(Habitant[i].posx, fact2, p)
        fruymax(Habitant[i].posx, fact2, p)
        fruymin(Habitant[i].posx, fact2, p)
        #print(verifchemin10(Habitant[i].posx,Habitant[i].posy,fact2,p))
        #verifchemin = False
        font = pygame.font.Font(None, int(hauteur*fact / 30))
        time1 = pygame.time.get_ticks()  # temps de départ
        time2 = int(time1 / 1000)  # transforme time1 en seconde
        text = font.render('Seconde : '+str(time2), True, 'black')  # transforme en texte time2
        nbboucle = font.render('Tour de boucle : ' + str(test), True, 'black')  # transforme en texte test, correspond au nombre de boucle
        nbjour = font.render('Jour : ' + str(n3-1), True, 'black')
        prop = [0 for i in range(nbsurface)]  # table contenant le nombre d'hab dans chaque surface
        #verifru = False

        for i in range(nbtot):
            #print(Habitant[i].objectif[0])
            #if -1<Habitant[i].endroit <=3:
                #x,y=xyobjectif(Habitant,i)
            #else:
            x = random.uniform(-val_aleatoire, val_aleatoire)
            y = random.uniform(-val_aleatoire, val_aleatoire)
            #x,y=0,0

            #verifchemin1(Habitant[i].posx,Habitant[i].posy,fact2,p)
            #print(i,test,Habitant[i].temps)

            if n2 * tattRUinf < test < (n2 * tattRUinf) + tattRUdedans:  # PAS LE M ECART
                #print('dedans',i,test,Habitant[i].temps,n2 * tattRUinf, test - Habitant[i].temps, n2 * tattRUsup,Habitant[i].color)
                #print(n2*tattRUinf,test,n2*tattRUinf+tattRUdedans)
                #n2bis=n2
                autorisation[12] = 1/2*nbtot
                pourcent = random.uniform(0, 1)
                if pourcent < 0.1 and not(Habitant[i].ru) and Habitant[i].ru != 'black' and Habitant[i].color != 'gray':
                    Habitant[i].posx, Habitant[i].posy = 400, 290
                    #Habitant[i].endroit = 12
                    Habitant[i].ru = True
                    verifru = True
                    #print('ru')
                    #Habitant[i].posx, Habitant[i].posy = collmur(Habitant, i, fact2, points, fxmax, fxmin, fymax, fymin,p, stop)  # appel la fonction collmur
            #else:
                #autorisation[12] = 0  # renvoie à 0,0
                #verifru=False
                #Habitant[i].ru=False
            #print(test,(n2 * tattRUinf) + tattRUdedans)
            if test >= (n2 * tattRUinf) + tattRUdedans:
                # print(test)
                autorisation[12] = 0
                # Habitant[i].ru = False
                # verifru = False
                # Habitant[i].endroit=Habitant[i].preendroit
            if test == n3*int(nbTBPJ*9):  # nouveau jour
                if Habitant[i].color != 'black' and Habitant[i].color != 'gray':
                    #Habitant[i] = habitant('green', depart[i][0],depart[i][1], test, rayon_cercle, WIN, endroit1, preendroit1, objct[i])
                    Habitant[i].posx, Habitant[i].posy = depart[i][0], depart[i][1]
                    #Habitant[i].endroit, Habitant[i].preendroit = -1,-1  ATTENTION
                    Habitant[i].ru = False
                    #print(Habitant[i].ru)
                    #print('JOUR')
            #print(firestexmax(Habitant[i].posx,fact2,p),f10xmin(Habitant[i].posx,fact2,p),f10xmax(Habitant[i].posx,fact2,p), Habitant[i].posy)  # pbl chemin10: pas d'inversions des vals si inversions des min et max, ym et xm inverser ?
            else:
                Habitant[i].posx += x
                Habitant[i].posy += y

            Habitant[i].endroit, Habitant[i].preendroit = endroit(Habitant, i, nbsurface, Verif, fact2, p, infocercles,rayon_cercle)  # attribut un numéro aux hab selon la où ils sont

            #print(Habitant[i].endroit,Habitant[i].preendroit,Habitant[i].ru)
            #print(test,Habitant[i].posx,Habitant[i].posy)
            #print(tab)
            #Habitant[i].posx = tab[2*test][0]
            #Habitant[i].posy = tab[2*test][1]


            if -1 < Habitant[i].endroit < 14 and Habitant[i].color != 'gray':  # si pas nul part et pas dans isitem
                Habitant[i].posx, Habitant[i].posy = collmur(Habitant, i, fact2, points, fxmax, fxmin, fymax, fymin, p,stop)  # appel la fonction collmur
            if 14 <= Habitant[i].endroit < 19 and Habitant[i].color != 'gray':  # si dans isitem
                Habitant[i].posx, Habitant[i].posy = dansisitem(Habitant, i, infocercles,stop)  # appel la fonction dans isitem
            #print(verifC6(Habitant[i].posx,Habitant[i].posy,infocercles,rayon_cercle))
            #print(Habitant[i].endroit,Habitant[i].preendroit)

            nbjaune, nbrouge = verifTempsSup('yellow', 'red', nbjaune, nbrouge, tattjr, factjr, i,test)  # les points jaunes deviennent rouges au bout d'un moment
            nbrouge, nbmort = verifTempsSup('red', 'black', nbrouge, nbmort, tattrn, factrn, i,test)  # les points rouges deviennent noirs (meurent) au bout d'un moment
            nbjaune, nbvert = verifTempsInf('yellow', 'green', nbjaune, nbvert, tattjv, factjv, i,test)  # les points jaunes deviennent verts (guérissent) tant que le temps est pas dépassé
            nbjaune, nbmort = verifTempsSup('yellow', 'black', nbjaune, nbmort, tattjn, factjn, i,test)  # les points jaunes deviennent noirs (meurent) au bout d'un moment
            n, nbrat, nbmort = rat('gray', 'black', nbrat, nbmort, test, tattgn, n,i)  # les points gris (rats) deviennent noirs (meurent) au bout d'un moment
            nbrouge, nbvert = verifTempsInf('red', 'green', nbrouge, nbvert, tattrv, factrv, i,test)  # les points rouges deviennent verts (guérissent) tant que le temps est pas dépassé
            if Habitant[i].color == 'red':  # si le point est rouge on met 'r' dans le tableau afin de savoir à la fin qui a été rouge à un momen t
                couleur[i] = 'r'
            prop = calculprop(Habitant,i,prop,Verif,fact2,p,infocercles,rayon_cercle)  # calcule le nombre d'hab dans les surfaces
            #print(prop)
            #print(i,test,Habitant[i].temps,n2 * tattRUinf, test - Habitant[i].temps, n2 * tattRUsup)


            Habitant[i].dessin()  # dessine les points


        stop = verifprop(Habitant,i,prop,autorisation,stop,nbtot,nbsurface,fact2, points, fxmax, fxmin, fymax, fymin, p,infocercles,Verif,rayon_cercle)  # vérifie qu'il n'y a pas trop d'hab dans les surfaces, et les envoies à leur surface d'avant si trop
        nbvert, nbrouge = collision('green', 'red', nbvert, nbrouge, nbtot, rayon_cercle, factvr,test)  # appel la fonction collision : les points verts sont contaminés par les rouges
        nbvert, nbjaune = collision2('gray', 'green', 'yellow', nbrat, nbvert, nbjaune, nbtot, rayon_cercle, factgvj,test)  # appel la fonction collision2 : les points gris (rats) contaminent les verts  qui deviennent jaunes
        WIN.blit(text, (10, 10))  # affiche le texte sur le fond
        WIN.blit(nbboucle, (160, 10))  # affiche le nombre de tours
        WIN.blit(nbjour,(400,10))
    #print(test,(n2 * tattRUinf) + tattRUdedans,verifru)
    if verifru and test > (n2 * tattRUinf) + tattRUdedans:
        #print(test)
        autorisation[12] = 0
        verifru = False
        n2 += 2  # ou n2 += 2, n2 = n3+1, n2=n3+2
        print('ru',n2)
    if test == n3 * int(nbTBPJ*9):
        n3 += 1
        print('jour',n3)

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



with open("stat modelisation polytech.csv", "a") as fichier:
    fichier.write("\n")
    fichier.write("\t")
    fichier.write("\t")

    fichier.write(str(tattgn/9))
    fichier.write("\t")
    fichier.write(str(nbvert))
    fichier.write("\t")
    fichier.write(str(sommeR0))
    fichier.write("\t")
    fichier.write(str(nbrougetot))
    fichier.write("\t")
    fichier.write(str(sommeR0/nbrougetot))
    fichier.write("\t")
    fichier.write(str(test))
    fichier.write("\t")
    fichier.write(str(nbTBPJ))



pygame.quit()

#Habitant[i].ru = False à la fin de la journée, gérer la fin de la journée     FAIT
# diminuer le temps de vie des rats pour arriver à une modélisation de 2 mois    FAIT : 2.4
#augmenter le déplacement car pas le temps d'arriver en isitem     FAIT : 30
# chemin6      FAIT
# chemin E5

# dimminuer collision : diminuer rayon (*4), ou facteur      FAIT : *2
# taille de fenêtre propre
# rat partout    FAIT : quand appelle de collmur ou dans isitem rajouter "and Habitant[i].color != 'gray'"

# calculer l'incrémentation de n2, points qui sortent      FAIT: n2+=2