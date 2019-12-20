import pygame as pg
from pygame.math import Vector2


class Entity(pg.sprite.Sprite):

    def __init__(self, pos, waypoints):
        super().__init__()
        # carica la macchinina
        self.image = pg.image.load('D:/traffic-simulator/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum.png')
        
        # centro di massa della macchina
        self.rect = self.image.get_rect(center=pos)
        
        # vettore velocità
        self.vel_max = Vector2(0, 0)
        
        # velocità effettiva
        self.max_speed = 4
        
        # locka il vettore sul centro di massa
        self.pos = Vector2(pos)
        
        #sai cos'è un waypoint vero? bon dai te lo dico io, è approssimabile ad un "checkpoint" dei videogiochi.
        self.waypoints = waypoints
        
        # indice dei waypoint, sono punti? si, e cominceranno pure da qualche parte
        self.waypoint_index = 0
        
        # setta al waypoint il valore dell'indice...(questo non so cosa voglia dire...)
        self.target = self.waypoints[self.waypoint_index]
        
        # raggio al di sotto il quale la macchinina brum brum comincia a rallentare
        self.target_radius = 50

    def update(self):
        # un vettore che va da se stesso (la macchinina brum brum) al waypoint
        heading = self.target - self.pos
        
        # distanza con il prossimo waypoint (o macchina, o semaforo eccetera)
        distance = heading.length()
        
        # inizializza il vettore e lo porta a valore 1
        heading.normalize_ip()
        
        # se la distanza è minore di n pixel
        if distance <= 2:  # We're closer than 2 pixels.

                
            # aumenta l'indice dei waypoint e scambia la direzione verso la quale mi muovo
            self.waypoint_index = (self.waypoint_index + 1) % len(self.waypoints)
            
            # se il modulo (quindi il valore della velocità) è uguale alla distanza porta l'indice a 0
            self.target = self.waypoints[self.waypoint_index]
            
        # se la distanza è minore (quindi sei vicino) del raggio dal centro di massa    
        if distance <= self.target_radius:
            
            # tony frena che nden in tel foss
            self.vel = heading * (distance / self.target_radius * self.max_speed)
            
        # cori goldon che fen tardi
        else:  
            self.vel = heading * self.max_speed

        # la posizione si aggiorna in base alla velocità
        self.pos += self.vel
        
        # il cnetro di massa diventa costantemente la posizione
        self.rect.center = self.pos


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    waypoints = [(200, 100), (500, 400), (100, 300), (200, 300), (100, 80)]
    all_sprites = pg.sprite.Group(Entity((100, 300), waypoints))

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        all_sprites.update()
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        
        #il for che proietta i waypoint, cioè i punti del percorso
        for point in waypoints:
            pg.draw.rect(screen, (90, 200, 40), (point, (0, 0)))

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()