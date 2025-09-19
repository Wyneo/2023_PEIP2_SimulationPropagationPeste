import math
nb_colonnes = 100
nb_lignes = 100


def creation_pixels():  # la on crée l'ensemble des pixels et leur position
    pixels = []
    for i in range(nb_colonnes):
        for j in range(nb_lignes):
            pixels.append([i, j])  # format x,y

    return pixels


liste_pixels = creation_pixels()


def obstacle(pixel):
    # if pixel == [5, 4] or pixel == [5, 3] or pixel == [7, 7]:
    # return False
    return True


def voisins(pixel):
    voisins = []
    # pixel en bas
    if pixel[0] < nb_lignes-1 and obstacle(liste_pixels[liste_pixels.index(pixel)+nb_colonnes]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)+nb_colonnes])
    # pixel a droite
    if pixel[1] < nb_colonnes-1 and obstacle(liste_pixels[liste_pixels.index(pixel)+1]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)+1])
    # pixel a gauche
    if pixel[1] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel)-1]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)-1])
    # pixel en haut
    if pixel[0] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel)-nb_colonnes]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)-nb_colonnes])
    # pixel en haut a gauche
    if pixel[1] > 0 and pixel[0] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel)-1-nb_colonnes]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)-1-nb_colonnes])
    # pixel en haut a droite
    if pixel[0] > 0 and pixel[1] < nb_colonnes-1 and obstacle(liste_pixels[liste_pixels.index(pixel)-nb_colonnes+1]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)-nb_colonnes+1])
    # pixel en bas a droite
    if pixel[0] < nb_lignes-1 and pixel[1] < nb_colonnes-1 and obstacle(liste_pixels[liste_pixels.index(pixel)+nb_colonnes+1]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)+nb_colonnes+1])
    # pixel en bas a gauche
    if pixel[0] < nb_lignes-1 and pixel[1] > 0 and obstacle(liste_pixels[liste_pixels.index(pixel)+nb_colonnes-1]):
        voisins.append(liste_pixels[liste_pixels.index(pixel)+nb_colonnes-1])
    return voisins


def h_scores(pixel1, pixel2):
    x1, y1 = pixel1
    x2, y2 = pixel2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def algo():
    trajet = []
    pixel_arriver = [4, 4]
    pixel_debut = [16, 26]
    trajet.append(pixel_debut)
    while pixel_arriver != pixel_debut:
        score_totals = {}
        # creation de la liste avec les scores de tout les voisins
        for i in voisins(pixel_debut):
            score_totals[tuple(i)] = h_scores(pixel_arriver, i)
        # on trie par ordre décroissant donc la le premier indice = score le plus bas
        score_totals_sorted = dict(
            sorted(score_totals.items(), key=lambda item: item[1]))
        values_totals = list(score_totals_sorted.keys())
        # je converti la liste de tuples en liste de liste
        values_totals_list = [list(t) for t in values_totals]

        # la partie suivante regarde si on a pas déja visité un voisin sinon on prend le prochain
        greedy_base_index = 0
        for i in list(values_totals_list):
            verif = i in trajet
            if not verif:  # si directement on tombe sur un bon voisins alors go
                break
            greedy_base_index += 1
        pixel_debut = list((values_totals[greedy_base_index]))

        trajet.append(pixel_debut)
    return trajet


print(algo())
