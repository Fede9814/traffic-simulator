import pygame as pg
from pygame.math import *

class Entity(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        # carica la macchinina
        self.background_image = pg.image.load('C:/Users/PC/Desktop/traffic-simulator/ZioBilly/Try 2.0/venv/img/terrain.jpg')
        self.image = pg.image.load('C:/Users/PC/Desktop/traffic-simulator/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum.png')

        self.rect = self.image.get_rect(center=pos)

        self.pos = Vector2(pos)

    def update(self):

        self.pos.y -= 1

        self.rect = self.image.get_rect(center=self.pos)

        if(self.pos.y == 0):
            self.kill()

terreno = Entity((475, 600))
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
all_sprites = pg.sprite.Group(terreno)

done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.blit(terreno.background_image, [0, 0])
    all_sprites.update()
    all_sprites.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.init()
pg.quit()
