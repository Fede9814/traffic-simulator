import pygame
import sys

color_line = (255,255,255)
filler_color = (0,0,0)
width = 2000
heigth = 2000
x, y = 1000, 1000


class Terrain(object):
    
    def __init__(self):
        terrain = pygame.display.set_mode((2000,2000), pygame.RESIZABLE)
        terrain.blit(terrain, (x - terrain.get_width() // 2, y - terrain.get_height() // 2 ))
        
        terrain.fill(filler_color)

        pygame.draw.line(terrain, color_line, (800,0), (800,800), 3)
        pygame.draw.line(terrain, color_line, (895,0), (895,800), 3)
        pygame.draw.line(terrain, color_line, (990,0), (990,800), 3)
        pygame.draw.line(terrain, color_line, (1010,0), (1010,800), 3)
        pygame.draw.line(terrain, color_line, (1105,0), (1105,800), 3)
        pygame.draw.line(terrain, color_line, (1200,0), (1200,800), 3)
        pygame.draw.line(terrain, color_line, (1200,0), (1200,800), 3)
        
        pygame.draw.line(terrain, color_line, (0,800), (800,800), 3)
        pygame.draw.line(terrain, color_line, (0,895), (800,895), 3)
        pygame.draw.line(terrain, color_line, (0,990), (800,990), 3)
        pygame.draw.line(terrain, color_line, (0,1010), (800,1010), 3)
        pygame.draw.line(terrain, color_line, (0,1105), (800,1105), 3)
        pygame.draw.line(terrain, color_line, (0,1200), (800,1200), 3)
        pygame.draw.line(terrain, color_line, (0,1200), (800,1200), 3)
        
        pygame.display.toggle_fullscreen
        pygame.display.flip()
        
while True:
    Terrain()