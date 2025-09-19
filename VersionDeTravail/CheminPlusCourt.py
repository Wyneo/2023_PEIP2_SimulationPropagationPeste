import math
import pygame

def creation_pixels(nb_colonnes,nb_lignes):  # la on crée l'ensemble des pixels et leur position
    pixels = []
    for i in range(nb_colonnes):
        for j in range(nb_lignes):
            pixels.append([i, j])  # format x,y

    return pixels


def obstacle(pixel,Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
    #print(Habitant[i].endroit)
    #print(i)
    if -1 < Habitant[i].endroit < 13:
        #print(i,Habitant[i].endroit)
        if Verif[Habitant[i].endroit](pixel[0],pixel[1],fact2,p):
            return True
    if 13 <= Habitant[i].endroit <18:
        if Verif[9](pixel[0],pixel[1],infocercles,rayon_cercle):
            return True



def voisins(pixel,Verif,Habitant,i,fact2,p, liste_pixels,nb_colonnes,nb_lignes,infocercles,rayon_cercle):
    voisins = []
    # pixel en bas
    if pixel[0] < nb_lignes - 1 and obstacle(liste_pixels[liste_pixels.index(pixel) + nb_colonnes],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) + nb_colonnes])
    # pixel a droite
    if pixel[1] < nb_colonnes - 1 and obstacle(liste_pixels[liste_pixels.index(pixel) + 1],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) + 1])
    # pixel a gauche
    if pixel[1] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel) - 1],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) - 1])
    # pixel en haut
    if pixel[0] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel) - nb_colonnes],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) - nb_colonnes])
    # pixel en haut a gauche
    if pixel[1] > 0 and pixel[0] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel) - 1 - nb_colonnes],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) - 1 - nb_colonnes])
    # pixel en haut a droite
    if pixel[0] > 0 and pixel[1] < nb_colonnes - 1 and obstacle(liste_pixels[liste_pixels.index(pixel) - nb_colonnes + 1],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) - nb_colonnes + 1])
    # pixel en bas a droite
    if pixel[0] < nb_lignes - 1 and pixel[1] < nb_colonnes - 1 and obstacle(liste_pixels[liste_pixels.index(pixel) + nb_colonnes + 1],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) + nb_colonnes + 1])
    # pixel en bas a gauche
    if pixel[0] < nb_lignes - 1 and pixel[1] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel) + nb_colonnes - 1],Verif,Habitant,i,fact2,p,infocercles,rayon_cercle):
        voisins.append(liste_pixels[liste_pixels.index(pixel) + nb_colonnes - 1])
    return voisins

def h_scores(pixel1, pixel2):
    x1, y1 = pixel1
    x2, y2 = pixel2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

"""
def algo(pixel_debut,pixel_arriver,Verif,Habitant,i,fact2,p,nb_colonnes,nb_lignes,centreisitem,rayonisitem,rayon_cercle):
    liste_pixels = creation_pixels(nb_colonnes,nb_lignes)
    trajet = []
    #pixel_arriver = [22, 17]
    #dbpixel_debut = [42, 38]
    trajet.append(pixel_debut)
    while pixel_arriver != pixel_debut:
        score_totals = {}
        #print('bouh')
        for j in voisins(pixel_debut,Verif,Habitant,i,fact2,p,liste_pixels,nb_colonnes,nb_lignes,centreisitem,rayonisitem,rayon_cercle):  # creation de la liste avec les scores
            #print(i)
            score_totals[tuple(j)] = h_scores(pixel_arriver, j)
        # on trie par ordre décroissant donc la le premier indice = score le plus bas
        score_totals_sorted = dict(sorted(score_totals.items(), key=lambda item: item[1]))
        values_totals = list(score_totals_sorted.keys())
        pixel_debut = list(values_totals[0])
        trajet.append(pixel_debut)
        print(trajet)
    return trajet


def algo(pixel_debut,pixel_arriver,Verif,Habitant,i,fact2,p,nb_colonnes,nb_lignes,centreisitem,rayonisitem,rayon_cercle,draw_window):
    trajet = []
    liste_pixels = creation_pixels(nb_colonnes, nb_lignes)
    #pixel_arriver = [22, 17]
    #pixel_debut = [42, 38]
    trajet.append(pixel_debut)
    while pixel_arriver != pixel_debut:
        draw_window(400 * fact2, 200 * fact2)
        score_totals = {}
        # creation de la liste avec les scores de tout les voisins
        for j in voisins(pixel_debut,Verif,Habitant,i,fact2,p,liste_pixels,nb_colonnes,nb_lignes,centreisitem,rayonisitem,rayon_cercle):
            score_totals[tuple(j)] = h_scores(pixel_arriver, j)
        # on trie par ordre décroissant donc la le premier indice = score le plus bas
        score_totals_sorted = dict(sorted(score_totals.items(), key=lambda item: item[1]))
        values_totals = list(score_totals_sorted.keys())
        # je converti la liste de tuples en liste de liste
        values_totals_list = [list(t) for t in values_totals]

        # la partie suivante regarde si on a pas déja visité un voisin sinon on prend le prochain
        greedy_base_index = 0
        for k in list(values_totals_list):
            verif = k in trajet
            if verif:
                greedy_base_index += 1
            break
        pixel_debut = list(values_totals[greedy_base_index])

        trajet.append(pixel_debut)
        #print(trajet)
        Habitant[i].posx=trajet[-1][0]
        Habitant[i].posy = trajet[-1][1]
        Habitant[i].dessin()
        pygame.display.update()
        #return trajet, Habitant[i].posx,Habitant[i].posy
    return trajet 
"""

def algo(pixel_debut,pixel_arriver,Verif,Habitant,i,fact2,p,nb_colonnes,nb_lignes,infocercles,rayon_cercle,draw_window):
    #draw_window(400 * fact2, 200 * fact2)
    trajet = []
    liste_pixels = creation_pixels(nb_colonnes, nb_lignes)
    # pixel_arriver = [22, 17]
    # pixel_debut = [42, 38]
    trajet.append(pixel_debut)
    while pixel_arriver != pixel_debut:
        draw_window(669,669)
        score_totals = {}
        # creation de la liste avec les scores de tout les voisins
        for j in voisins(pixel_debut,Verif,Habitant,i,fact2,p,liste_pixels,nb_colonnes,nb_lignes,infocercles,rayon_cercle):
            score_totals[tuple(j)] = h_scores(pixel_arriver, j)
        # on trie par ordre décroissant donc la le premier indice = score le plus bas
        score_totals_sorted = dict(sorted(score_totals.items(), key=lambda item: item[1]))
        values_totals = list(score_totals_sorted.keys())
        # je converti la liste de tuples en liste de liste
        values_totals_list = [list(t) for t in values_totals]

        # la partie suivante regarde si on a pas déja visité un voisin sinon on prend le prochain
        greedy_base_index = 0
        #print(values_totals_list)
        for k in list(values_totals_list):
            verif = (k in trajet)
            if not verif:  # si directement on tombe sur un bon voisins alors go
                break
            greedy_base_index += 1
        #print(greedy_base_index)
        pixel_debut = list(values_totals[greedy_base_index])

        trajet.append(pixel_debut)
        #print(trajet)
        #Habitant[i].posx = trajet[-1][0]
        #Habitant[i].posy = trajet[-1][1]

        #Habitant[i].dessin()
        #pygame.display.update()
        #return trajet, Habitant[i].posx, Habitant[i].posy
    return trajet

#print(algo())

