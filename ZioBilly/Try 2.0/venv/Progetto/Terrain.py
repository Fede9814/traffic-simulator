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

passa_NS_DX = True
passa_EO_DX = False
passa_EO_SX = False
passa_NS_SX = False

t_passa_NS_DX = False
t_passa_EO_DX = False
t_passa_EO_SX = False
t_passa_NS_SX = False

def ifgiallo(passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX):
    t_passa_NS_DX = passa_NS_DX
    t_passa_EO_DX = passa_EO_DX
    t_passa_EO_SX = passa_EO_SX
    t_passa_NS_SX = passa_NS_SX

    passa_NS_DX = False
    passa_EO_DX = False
    passa_EO_SX = False
    passa_NS_SX = False
    print("Giallo")

    return passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX, t_passa_NS_DX, t_passa_EO_DX, t_passa_EO_SX, t_passa_NS_SX


def ifsemaforo(passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX):
    if(passa_NS_DX == True):
        passa_NS_DX = False
        passa_EO_DX = True
        passa_EO_SX = False
        passa_NS_SX = False
    elif(passa_EO_DX == True):
        passa_NS_DX = False
        passa_EO_DX = False
        passa_EO_SX = True
        passa_NS_SX = False
    elif(passa_EO_SX == True):
        passa_NS_DX = False
        passa_EO_DX = False
        passa_EO_SX = False
        passa_NS_SX = True
    elif(passa_NS_SX == True):
        passa_NS_DX = True
        passa_EO_DX = False
        passa_EO_SX = False
        passa_NS_SX = False

    print("Nord/Sud DX ", passa_NS_DX,"\n\rEst/Ovest DX ", passa_EO_DX, "\n\rEst/Ovest SX ", passa_EO_SX,"\n\rNord/Sud SX ", passa_NS_SX, "\n\r")
    return passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX

spawn = pg.USEREVENT + 1
semaforo = pg.USEREVENT + 2
giallo = pg.USEREVENT + 3

pg.time.set_timer(spawn, 3000)
pg.time.set_timer(giallo, 1000)

macchina = Car()
all_cars = pg.sprite.Group(macchina)

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == spawn:
            print("creata")
            macchina = Car()
            all_cars.add(macchina)
        elif event.type == giallo:
            pg.time.set_timer(giallo, 0)
            passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX, t_passa_NS_DX, t_passa_EO_DX, t_passa_EO_SX, t_passa_NS_SX = ifgiallo(passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX)
            pg.time.set_timer(semaforo, 2000)
        elif event.type == semaforo:
            pg.time.set_timer(semaforo, 0)
            passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX = ifsemaforo(t_passa_NS_DX, t_passa_EO_DX, t_passa_EO_SX, t_passa_NS_SX)
            pg.time.set_timer(giallo, 7000)
        
    
    screen.fill([255, 255, 255])
    screen.blit(terreno.image, terreno.rect) 
    macchine = all_cars.sprites()
    for i in macchine:
        pg.draw.rect(screen, (0, 0, 255), i.vision)
        pg.draw.rect(screen, (0, 255, 0), i.rect)
    
    all_cars.update(passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX, macchine)
    all_cars.draw(screen)
    

    pg.display.flip()
    clock.tick(200)


pg.quit()

