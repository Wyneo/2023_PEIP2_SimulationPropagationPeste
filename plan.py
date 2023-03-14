
import pygame
import os

pygame.init()

info = pygame.display.Info()
longueur= 0.93*info.current_w                                           # taille de la fenêtre de jeu en plein écran
hauteur =0.93*info.current_h
fact=(783/662)                                                          #rapport dimension ancien plan pour la nouvelle fenêtre
fact2=hauteur/662                                                       #rapport entre nouvelle et ancienne hauteur pour avoir les bonnes coordonnées
WIN=pygame.display.set_mode((950,803))
pygame.display.set_caption("modelisation de la ville")
print (hauteur, fact*hauteur, fact)

WHITE=(255,255,255)                                                      #couleurs RGB
GREEN=(0,255,0)
BLACK=(0,0,0)


plan_polytech=pygame.image.load(os.path.join('planpopo.png')) #importe image
plan_polytech=pygame.transform.scale(plan_polytech,(hauteur*fact,hauteur))
busc6=pygame.image.load(os.path.join('c6.jpg'))                     #c6
busc6=pygame.transform.scale(busc6,(fact*25,fact*22))                                  #diminution taille
buse5=pygame.image.load(os.path.join('e5.jpg'))                     #e5
buse5=pygame.transform.scale(buse5,(fact*26,fact*22))
bus75=pygame.image.load(os.path.join('75.jpg'))                     #75
bus75=pygame.transform.scale(bus75,(fact*24,fact*22))
p=[(fact2*202,fact2*354), (fact2*259,fact2*153), (fact2*352,fact2*176), (fact2*352,fact2*148), (fact2*368,fact2*150), (fact2*368,fact2*180), (fact2*564,fact2*234), (fact2*545,fact2*245), (fact2*363,fact2*197), (fact2*361,fact2*224), (fact2*344,fact2*224), (fact2*347,fact2*192), (fact2*271,fact2*174),(fact2*221,fact2*347)]



def fonctlin ( x1, y1, x2, y2 ):             #entrée : coordonées de 2 points, sortie : a et b de la fonction y = a*x + b passant par les 2 points
    if (x1 != x2):
        a = (y1-y2)/(x1-x2)
        b = y1 - x1 * a
    else :
        a = x1
        b = 0
    return (a,b)


# fmin = correspond aux lignes fermant les chemins en haut et à gauche (là ou x et y sont les plus bas)
# fmax = correspond aux lignes fermant les chemins en bas et à droite (là ou x et y sont les plus hauts)

def f1xmin(x) :
    (a,b)=fonctlin(p[0][0],p[0][1],p[1][0],p[1][1])
    f= - 3.53 * x + 1066.32 * fact2
    return f
def f1ymax (x):
    f = -0.37 * x + 428.42 * fact2
    return f
def f1xmax (x):
    f = -3.46*x + 1111.66 * fact2
    return f
def f1ymin (x):
    f = 1.75 *x - 300.25 * fact2
    return f
def f2xmin (x):
    f = 0.25 * x + 88.95 * fact2
    return f
def f2xmax (x):
    f = 0.24 * x + 109.82 * fact2
    return f
def f2ymax (x):
    f = -3.2*x + 1302.40 * fact2
    return f
def f2ymin (x):
    f = 1.75*x -300.25 * fact2
    return f
def f3xmax (x):
    f = 0.31*x + 83.56 * fact2
    return f
def f3ymax (x):
    f = -3.40 * x +1431.20 * fact2
    return f
def f3xmin (x):
    f = 0.25 * x + 88 * fact2
    return f
def f3ymin (x):
    f = -3.2 * x + 1302.4 * fact2
    return f
def f4xmax (x):
    f = 0.26 * x + 101.26 * fact2
    return f
def f4ymax (x):
    f = -0.58*x +560.53 * fact2
    return f
def f4xmin (x):
    f = 0.28*x + 78.61 * fact2
    return f
def f4ymin (x):
    f = -3.4*x + 83.56 * fact2
    return f
def f5ymax (x):
    f = 224 * fact2
    return f
def f5xmax (x):
    f = -13.5 *x + 5097.5 * fact2
    return f
def f5xmin (x):
    f = -10.67*x + 3893.33 * fact2
    return f
def f5ymin (x):
    f = 0.31 * x +83.46 * fact2
    return f
def f6xmax (x):
    f= - 25*x + 9355 * fact2
    return f
def f6ymax (x):
    f = 0.25*x + 88 * fact2
    return f
def f6xmin (x):
    f = -23*x + 8249 * fact2
    return f
def f6ymin (x):
    f= 0.13*x + 109 * fact2
    return f




def draw_window(x,y):
   WIN.fill(WHITE)                                                         #fond blanc
   #WIN.blit(super_uu,(300,100))
   WIN.blit(plan_polytech,(0,0))
   pygame.draw.polygon(WIN, (0,150,0), [(fact2*202,fact2*354), (fact2*259,fact2*153), (fact2*271,fact2*174),(fact2*221,fact2*347)])        # chemin 1 = chemin sortant d'Ireste
   pygame.draw.polygon(WIN, (255,65,200), [(fact2*259,fact2*153), (fact2*352,fact2*176), (fact2*347,fact2*192), (fact2*271,fact2*174)])       # chemin 2 = chemin entre le chemin 1 (la ou le chemin fait un coude) et l'intersection au niveau de IHT et le RU (chemin 3)
   pygame.draw.polygon(WIN, (255, 165, 100), [(fact2*352,fact2*176), (fact2*368,fact2*180), (fact2*363,fact2*197), (fact2*347,fact2*192)])   # chemin 3 = intersection au niveau de IHT et le RU
   pygame.draw.polygon(WIN, (255, 65, 200), [(fact2*368,fact2*180), (fact2*564,fact2*234), (fact2*545,fact2*245), (fact2*363,fact2*197)])   # chemin 4 = chemin entre intersection (chemin 3) et Isitem
   pygame.draw.polygon(WIN, (255, 119, 165), [(fact2*363,fact2*197), (fact2*361,fact2*224), (fact2*344,fact2*224), (fact2*347,fact2*192)])   # chemin 5 = chemin entre intersection (chemin 3) et le RU
   pygame.draw.polygon(WIN, (255, 105, 30), [(fact2*352,fact2*176), (fact2*352,fact2*148), (fact2*368,fact2*150), (fact2*368,fact2*180)])     # chemin 6 = chemin entre intersection (chemin 3) et IHT

   for i in range(len(p)-1):                                                          #chemins
        if i!=3 and i!=6 and i!=9:
            pygame.draw.line(WIN,BLACK,p[i],p[i+1])
   pygame.draw.polygon(WIN,BLACK,[(fact2*295,fact2*310),(fact2*416,fact2*584),(fact2*292,fact2*636),(fact2*168,fact2*366)])           #ireste
   pygame.draw.polygon(WIN, BLACK, [(fact2*484, fact2*168), (fact2*302, fact2*62), (fact2*263,fact2*138)])               #IHT
   pygame.draw.circle(WIN, BLACK, (fact2*563, fact2*326), fact2*91)                                     #isitem
   pygame.draw.polygon(WIN, BLACK, [(fact2*381,fact2*206),(fact2*425,fact2*301),(fact2*384,fact2*317),(fact2*338,fact2*223)])         #RU
   WIN.blit(busc6,(fact2*153,fact2*530))                                                          #c6
   WIN.blit(bus75,(fact2*6,fact2*364))                                                            #75
   WIN.blit(buse5,(fact2*618,fact2*634))                                                          #e5

   pygame.draw.circle(WIN, (90,150,200),(x,y), 5)

   pygame.display.update()



def verifchemin1(x,y,o):
    if (202 <= x <= 271 and ((f1xmin(x) <= y <= f1xmax(x) and y >= 174) or (y < 174 and y > f1ymin(x))) and o):
        print("chemin 1")
        o = False
    return o

def verifchemin2(x, y, o):
    if (p[1][0] <= x <= p[2][0] and ((f2xmin(x) <= y <= f2xmax(x)) and y <= f2ymin(x) and (y <= f2ymax(x))) and o):
        print("chemin 2")
        o = False
    return o

def verifchemin3(x, y, o):
    if (p[11][0] <= x <= p[5][0] and f3xmin(x) <= y <= f3xmax(x) and f3ymin(x) <= y <= f3ymax(x) and o):
        print("chemin 3")
        o = False
    return o

def verifchemin4(x, y, o):
    if (p[8][0] <= x <= p[6][0] and f4xmin(x) <= y <= f4xmax(x) and f4ymin(x) <= y <= f4ymax(x) and o):
        print("chemin 4")
        o = False
    return o

def verifchemin5(x, y, o):
    if (p[11][0] <= x <= p[8][0] and f5xmin(x) <= y <= f5xmax(x) and f5ymin(x) <= y <= f5ymax(x) and o):
        print("chemin 5")
        o = False
    return o

def verifchemin6(x, y, o):
    if (p[3][0] <= x <= p[5][0] and f6xmin(x) <= y <= f6xmax(x) and f6ymin(x) <= y <= f6ymax(x) and o):
        print("chemin 6")
        o = False
    return o


x=400*fact2
y=200*fact2

def main():                                                                 #fonction principale
   run=True
   o = True
   v=True
   while run:
       for event in pygame.event.get():
           if event.type==pygame.QUIT:                 #ferme la fenêtre quand l'utilisateur fait la croix
               run=False
       draw_window(x,y)
       if (v):
           print(f2xmin(x))
           print(f2xmax(x))
           print(f2ymin(x))
           print(f2ymax(x))
           print(y)
           print("")
           print(p[11][0])
           print(p[5][0])
           print(x)
           v = False
       o = verifchemin1(x, y, o)
       o = verifchemin2(x, y, o)
       o = verifchemin3(x, y, o)
       o = verifchemin4(x, y, o)
       o = verifchemin5(x, y, o)
       o = verifchemin6(x, y, o)

   pygame.quit()


if __name__=="__main__":                                 #pour appeler la fonction dans  un autre code
   main()
