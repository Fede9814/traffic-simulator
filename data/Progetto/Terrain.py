import pygame as pg
from car import Car

class Terrain(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self) 
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Semaforo(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


terreno = Terrain('S:/TrafficSim/img/terrain.png', [0,0])
semaforo_nord = Semaforo('S:/TrafficSim/img/luce_rossaN.png', [279, 138])
semaforo_sud = Semaforo('S:/TrafficSim/img/luce_rossa.png', [501, 402])
semaforo_est = Semaforo('S:/TrafficSim/img/luce_rossaE.png', [501,178])
semaforo_ovest = Semaforo('S:/TrafficSim/img/luce_rossaO.png', [239,402])

screen = pg.display.set_mode((800, 600), pg.FULLSCREEN)
clock = pg.time.Clock()

passa_N = True
passa_S = False
passa_E = False
passa_O = False

t_passa_N = False
t_passa_S = False
t_passa_E = False
t_passa_O = False

def ifgiallo(passa_N, passa_S, passa_E, passa_O):

    t_passa_N = passa_N
    t_passa_S = passa_S
    t_passa_E = passa_E
    t_passa_O = passa_O
    if (t_passa_N == True):
        semaforo_nord.image = pg.image.load('S:/TrafficSim/img/luce_gialla.png')
    if (t_passa_S == True):
        semaforo_sud.image = pg.image.load('S:/TrafficSim/img/luce_gialla.png')
    if (t_passa_E == True):
        semaforo_est.image = pg.image.load('S:/TrafficSim/img/luce_giallaE.png')
    if (t_passa_O == True):
        semaforo_ovest.image = pg.image.load('S:/TrafficSim/img/luce_giallaO.png')
        
    passa_N = False
    passa_S = False
    passa_E = False
    passa_O = False

    return passa_N, passa_S, passa_E, passa_O, t_passa_N, t_passa_S, t_passa_E, t_passa_O


def ifsemaforo(passa_N, passa_S, passa_E, passa_O):
    if(passa_N == True):
        passa_N = False
        passa_S = False
        passa_E = True
        semaforo_est.image = pg.image.load('S:/TrafficSim/img/luce_verdeE.png')
        semaforo_nord.image = pg.image.load('S:/TrafficSim/img/luce_rossaN.png')
        passa_O = False

    elif(passa_S == True):
        passa_N = False
        passa_S = False
        passa_E = False
        passa_O = True
        semaforo_ovest.image = pg.image.load('S:/TrafficSim/img/luce_verdeO.png')
        semaforo_sud.image = pg.image.load('S:/TrafficSim/img/luce_rossa.png')


    elif(passa_E == True):
        passa_N = False
        passa_S = True
        semaforo_sud.image = pg.image.load('S:/TrafficSim/img/luce_verde.png')
        semaforo_est.image = pg.image.load('S:/TrafficSim/img/luce_rossaE.png')
        passa_E = False
        passa_O = False

    elif(passa_O == True):
        passa_N = True
        semaforo_nord.image = pg.image.load('S:/TrafficSim/img/luce_verdeN.png')
        semaforo_ovest.image = pg.image.load('S:/TrafficSim/img/luce_rossaO.png')
        passa_S = False
        passa_E = False
        passa_O = False
    return passa_N, passa_S, passa_E, passa_O


spawn = pg.USEREVENT + 1
semaforo = pg.USEREVENT + 2
giallo = pg.USEREVENT + 3
hour = pg.USEREVENT + 4
t2 = 6
t = 6000



def t_spawn(t2):

    t = 0
    if t2 == 24:
        t2 = 0
    t2 += 1
    if t2 == 1 or t2 == 2 or t2 == 3 or t2 == 4 or t2 == 5 or t2 == 6:
        t = 6000
    if t2 == 7 or t2 == 8 or t2 == 9 or t2 == 14 or t2 == 15 or t2 == 16 or t2 == 23 or t2 == 24:
        t = 2500
    if t2 == 10 or t2 == 11 or t2 == 17 or t2 == 18 or t2 == 21 or t2 == 22:
        t = 1000
    if t2 == 12 or t2 == 13 or t2 == 19 or t2 == 20:
        t = 500

    return t2, t

pg.time.set_timer(hour, 10000)
pg.time.set_timer(spawn, t)
pg.time.set_timer(giallo, 1000)

macchina = Car()
all_cars = pg.sprite.Group(macchina)

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == hour:
            pg.time.set_timer(spawn, 0)
            t2, t = t_spawn(t2)
            print("ORA: ", t2, "\n\rSPAWN: ", t)
            pg.time.set_timer(spawn, t)
        elif event.type == spawn:
            print("creata")
            macchina = Car()
            all_cars.add(macchina)
        elif event.type == giallo:
            pg.time.set_timer(giallo, 0)
            passa_N, passa_S, passa_E, passa_O, t_passa_N, t_passa_S, t_passa_E, t_passa_O = ifgiallo(passa_N, passa_S, passa_E, passa_O)
            pg.time.set_timer(semaforo, 2000)
        elif event.type == semaforo:
            pg.time.set_timer(semaforo, 0)
            passa_N, passa_S, passa_E, passa_O = ifsemaforo(t_passa_N, t_passa_S, t_passa_E, t_passa_O)
            pg.time.set_timer(giallo, 7000)

    screen.set_alpha(None)
    screen.fill([255, 255, 255])
    screen.blit(terreno.image, terreno.rect)

    screen.blit(semaforo_nord.image, semaforo_nord)
    screen.blit(semaforo_sud.image, semaforo_sud.rect)
    screen.blit(semaforo_est.image, semaforo_est.rect)
    screen.blit(semaforo_ovest.image, semaforo_ovest.rect)

    macchine = all_cars.sprites()
#    for i in macchine:
#       pg.draw.rect(screen, (0, 0, 255), i.vision)
#       pg.draw.rect(screen, (0, 255, 0), i.rect)
    
    all_cars.update(passa_N, passa_S, passa_E, passa_O, macchine)
    all_cars.draw(screen)
    pg.display.flip()
    clock.tick(80)


pg.quit()

