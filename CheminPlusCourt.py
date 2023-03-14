nb_colonnes = 50
nb_lignes = 50


def creation_pixels():  # la on crée l'ensemble des pixels et leur position
    pixels = []
    for i in range(nb_colonnes):
        for j in range(nb_lignes):
            pixels.append([i, j])  # format x,y

    return pixels


liste_pixels = creation_pixels()


def obstacle(pixel):
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
    return voisins


def h_scores(pixel1, pixel2):
    x1, y1 = pixel1
    x2, y2 = pixel2
    return abs(x1 - x2) + abs(y1 - y2)


def algo():
    trajet = []
    pixel_arriver = [22, 17]
    pixel_debut = [42, 38]
    trajet.append(pixel_debut)
    while pixel_arriver != pixel_debut:
        score_totals = {}
        for i in voisins(pixel_debut):  # creation de la liste avec les scores
            score_totals[tuple(i)] = h_scores(pixel_arriver, i)
        # on trie par ordre décroissant donc la le premier indice = score le plus bas
        score_totals_sorted = dict(
            sorted(score_totals.items(), key=lambda item: item[1]))
        values_totals = list(score_totals_sorted.keys())
        pixel_debut = list(values_totals[0])
        trajet.append(pixel_debut)
    return trajet


print(algo())
