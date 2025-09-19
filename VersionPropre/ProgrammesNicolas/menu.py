import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
# Titre de la fenetre
pygame.display.set_caption("Menu")
# type d'ecriture
# l'int correspond a la taille de l'écriture, le None c'est la calligraphie de base car flemme
font = pygame.font.Font(None, 30)

# Option du menu
habitants = ["Population de campagne", "Population de petite ville",
             "Population de Nantes", "Population de Tokyo"]
type_virus = ["Covid-19", "Ebola", "SIDA", "l'optique"]
nb_habitants = 0
virus_selectionner = 0

# Main loop
running = True
while running:
    # partie ou ça gere les appuis de touche (fleche directionnelle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # ici python rend un modulo positif voir stack overflow pk
                nb_habitants = (nb_habitants - 1) % len(habitants)
            elif event.key == pygame.K_DOWN:
                # le modulo permet de pas dépasser l'index de habitants
                nb_habitants = (nb_habitants + 1) % len(habitants)
            elif event.key == pygame.K_LEFT:
                virus_selectionner = (
                    virus_selectionner - 1) % len(type_virus)
            elif event.key == pygame.K_RIGHT:
                virus_selectionner = (
                    virus_selectionner + 1) % len(type_virus)
            elif event.key == pygame.K_RETURN:
                print("Tu as sélectionné ce type de densité de population: ",
                      habitants[nb_habitants])
                print("Tu as prit ce virus: ",
                      type_virus[virus_selectionner])

    screen.fill('white')

    # draw du menu
    # enumerate renvoie l'index et la valeur, on associe l'index a i et t'as capter
    for i, option in enumerate(habitants):
        # creation d'un texte sur une nouvelle surface, faut ensuite utiliser blit pour l'associer au bon bail, le True c'est pour l'anti-aliasing
        text = font.render(option, True, (0, 0, 0))
        text_rect = text.get_rect()  # transforme en un rectangle le texte crée avant
        # on fout le text a cette endroit la, le i*50 c'est l'espacement de 50 pixel entre les textes
        text_rect.center = (400, 300 + i * 50)
        # prend le texte 'text' le fout sur 'screen' a la position 'text_rect'
        screen.blit(text, text_rect)
    for i, virus_option in enumerate(type_virus):
        text = font.render(virus_option, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (600, 300 + i * 50)
        screen.blit(text, text_rect)

    # on surligne la partie qu'on selectionne
    # partit habitants
    selected_text = font.render(habitants[nb_habitants], True, (255, 0, 0))
    selected_text_rect = selected_text.get_rect()
    selected_text_rect.center = (400, 300 + nb_habitants * 50)
    screen.blit(selected_text, selected_text_rect)

    # partit viurs
    selected_text_virus = font.render(
        type_virus[virus_selectionner], True, (255, 0, 0))
    selected_text_rect_virus = selected_text_virus.get_rect()
    selected_text_rect_virus.center = (600, 300 + virus_selectionner * 50)
    screen.blit(selected_text_virus, selected_text_rect_virus)
    pygame.display.update()
