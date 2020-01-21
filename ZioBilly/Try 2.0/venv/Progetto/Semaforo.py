import random
import numpy
import pygame
from pygame.math import *

class Semaforo(pygame.sprite.Sprite):
    def __init__(self, surface, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.rect = pygame.draw.rect(surface, [169, 169, 169], [x, y, 100, 50])