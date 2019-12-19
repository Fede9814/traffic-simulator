import pygame

pygame.init()

adesso = pygame.time.get_ticks()

sicuroCheSiaAdesso = adesso

tempo = pygame.time.Clock()

tempoScorre = True

i = 0

class clockGlobal(object):
    # TODO: Aggingere variazione di tempo a seconda del semaforo 
    stato = 0    
    def __init__(self):
        while tempoScorre:
            if(self.stato < 4):
                self.stato = self.stato + 1 
            else:
                self.stato = 1
            tempo.tick(0.5)   
            print(self.stato)
                
m = clockGlobal()