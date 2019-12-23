import pygame as pg

class Terrain(object):

    def __init__(self):
        super().__init__()

        # carica il path della foto di background
        self.background_image = pg.image.load('A:/DAM/Traffico/traffic-simulator/ZioBilly/Try 2.0/venv/img/terrain.jpg')

# dimensioni del canvas
window = pg.display.set_mode((800, 600))
# aggiorna lo schermo (temporalmente, è il tick dei frame)
clock = pg.time.Clock()
# richiama la classe
terrain = Terrain()
# centra l'immagine
window.blit(terrain.background_image, [0, 0])
# aggiorna lo schermo
pg.display.flip()