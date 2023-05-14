import pygame
import time

# Initialisation de Pygame
pygame.init()

# Définition de la police d'écriture
font = pygame.font.SysFont('Calibri', 50)
font_2 = pygame.font.SysFont('Calibri', 30)

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (123, 140, 222)
RED = (255, 0, 0)
GREEN=(0,255,0)
YELLOW=(255,255, 0)
# Ouverture de la fenêtre
screen = pygame.display.set_mode((400, 150))
pygame.display.set_caption("Horloge_V.2")

# Demande du temps de départ
while True:
    try:
        Timer = (int(input("Temps de départ (minutes) : ")))*60
        Timer_2 = Timer
        break
    except ValueError:
        print("Ceci n'est pas un entier.")

# Boucle principale
Lancement = False
Le_timer_tourne = False
Temps_restant = Timer
Dépassement = 0
Demande_de_reset=False
Reset=False

text_3 = font.render(str(Temps_restant), True, WHITE)

while True:
    
    # Gestion de l'événement de fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        #Gestion du clic
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            Lancement = True
            Début = time.time()
            Le_timer_tourne=True
        else:
            Lancement=False
            print('Pas de clic')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame  .K_r:
                Demande_de_reset=True

    if Le_timer_tourne==False and Demande_de_reset:
        Reset=True

    if Reset:
        try:
            Timer = (int(input("Temps de départ (minutes) : ")))*60
            Timer_2 = Timer
            
        except ValueError:
                print("Ceci n'est pas un entier.")
        Reset=False
        Demande_de_reset=False

    if Lancement==False and Le_timer_tourne:
        Le_timer_tourne=True
        print('Le timer fonctionne')

    if Lancement==True and Le_timer_tourne:
        Le_timer_tourne = False
        Dépassement=0
        print('Le timer a été reset')
    
    # Affichage
    screen.fill(BLACK)

    # Temps Unix actuel
    temps_unix = time.time()

    # Conversion du temps Unix en temps local
    temps_local = time.localtime(temps_unix)

    # Formatage du temps local en chaîne de caractères
    temps_formate_date = time.strftime("%d/%m/%y", temps_local)
    temps_formate_hour = time.strftime("%H:%M:%S", temps_local)

    # Calcul du temps écoulé
    if Le_timer_tourne:
        Temps_restant = Timer - int(temps_unix - Début)
        Le_timer_tourne =True
        if Temps_restant <= 0:
            Dépassement = -(Temps_restant)
    else:
        Temps_restant=Timer
        text_3=font.render(str(Temps_restant),True, BLACK)
    
    try:
        Avancement=Timer/Temps_restant
    
        if Avancement<=2:
            GRADENDE=GREEN
        elif Avancement>=2:
            GRADENDE=YELLOW
            if Avancement>=4:
                GRADENDE=RED

    except  ZeroDivisionError:
        GRADENDE=RED
    
    # Création de l'affichage
    text = font_2.render(temps_formate_date, True, BLUE)
    text_2 = font.render(temps_formate_hour, True, WHITE)
    text_3 = font.render(str(Temps_restant), True, GRADENDE)

    if Dépassement!=0:
        text_4 = font.render(str(Dépassement), True, RED)
        text_3 = font.render(str(Temps_restant), True, BLACK)
    else:
        text_4 = font.render("", True, WHITE)

    screen.blit(text, (10, 10))
    screen.blit(text_2, (10, 40))
    screen.blit(text_3, (10, 90))
    screen.blit(text_4, (150, 90))

    # Rafraîchissement de l'affichage
    pygame.display.flip()

    # Attente d'une seconde
    time.sleep(1)
