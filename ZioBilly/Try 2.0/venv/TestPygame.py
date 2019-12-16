import pygame

pygame.init()

adesso = pygame.time.get_ticks()

sicuroCheSiaAdesso = adesso

tempo = pygame.time.Clock()

tempoScorre = True

stato = bool

while tempoScorre:

    for i in range(10):
        if stato == True:
            stato = False
        else:
            stato = True
            tempo.tick(100)
        print(stato)
