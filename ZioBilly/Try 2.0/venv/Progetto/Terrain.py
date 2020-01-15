import pygame as pg
import schedule
import time
from car import Car

class Terrain(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self) 
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

terreno = Terrain('C:/Users/PC/Desktop/traffic-simulator/ZioBilly/Try 2.0/venv/img/terrain.png', [0,0])
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

car = []

def job():
    macchina = Car()
    car.append(macchina)

spawn = pg.USEREVENT + 1

pg.time.set_timer(spawn, 3000)

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == spawn:
            job()

    screen.fill([255, 255, 255])
    screen.blit(terreno.image, terreno.rect) 
    all_cars = pg.sprite.Group(car)
    all_cars.update()
    all_cars.draw(screen)
  

    pg.display.flip()
    clock.tick(120)


pg.quit()

