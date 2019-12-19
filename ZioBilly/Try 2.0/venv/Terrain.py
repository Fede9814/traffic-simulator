import pygame
import sys

color_line = (255,255,255)
filler_color = (0,0,0)
width = 2000
heigth = 2000

class Terrain(object):
    
    def __init__(self):
        surface = pygame.Surface((1900, 800), flags=0)
        terrain = pygame.display.set_mode((2000,2000))
        pygame.transform.scale(surface, (1900,800))
        terrain.center(1000,1000)
        
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