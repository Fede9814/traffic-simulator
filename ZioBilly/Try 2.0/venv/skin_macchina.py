import numpy
import pygame
import sys

# genera il canvas
pygame.display.init()

# setta le dimensioni
terrain = pygame.display.set_mode(size = (800, 600))

# aggiorna costantemente il canvas
pygame.display.flip()

car = pygame.image.load('img/macchinina_brum_brum.png')
x=10
y=50

# carica la macchina
veicolo_skin = pygame.image.load('D:/traffic-simulator/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum.png')

while True:
    
    terrain.blit(veicolo_skin, (x,y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('Vai su')
                y-=5
            elif event.key == pygame.K_DOWN:
                print('Vai giù')
                y+=5
            elif event.key == pygame.K_LEFT:
               print('Vai a sinistra')
               x-=5
            elif event.key == pygame.K_RIGHT:
                print('Vai a destra')
                x+=5
        pygame.display.update()