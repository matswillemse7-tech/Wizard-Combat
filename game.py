import pygame
import numpy as np
import random
import os
from unit_stats import unit_stats
from collections import deque


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()
running = True


Massive_font = pygame.font.Font(None, 200)
title_font = pygame.font.Font(None, 74)
text_font = pygame.font.Font(None, 36)
bold_font = pygame.font.Font(None, 44)
messages = []

Screen_width = 1200
Screen_height = 800

GRAPHICS_DIR = "graphics"; IMAGES = {}

for filename in os.listdir(GRAPHICS_DIR):
    if filename.endswith(".png"):
        name = os.path.splitext(filename)[0]
        path = os.path.join(GRAPHICS_DIR, filename)
        IMAGES[name] = pygame.image.load(path).convert_alpha()






def draw_image(surface, x, y, angle=0, size=0):
    if size > 0:
        scale_factor = size / max(surface.get_width(), surface.get_height())
        new_size = (int(surface.get_width() * scale_factor), int(surface.get_height() * scale_factor))
        scaled_surface = pygame.transform.scale(surface, new_size)
    else:
        scaled_surface = surface
            


    if angle != 0:
        rotated_surface = pygame.transform.rotate(scaled_surface, angle)
        rect = rotated_surface.get_rect(center=(x, y))
        screen.blit(rotated_surface, rect)
    else:
        rect = scaled_surface.get_rect(center=(x, y))
        screen.blit(scaled_surface, rect)

    




def draw_text(text, font, color, x, y, center=True):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)


unit = np.dtype([
    ('Name', np.object_),
    ('Health', np.uint8),
    ('Maxhealth', np.uint8),
    ('Faction', np.uint8),
    ('Abilities', np.object_),
    ('Speed', np.uint8),
    ('turn', np.uint8)
])

map = np.zeros((20, 20), dtype=unit)




def create_unit(i, faction, x, y):
    map[x, y] = unit_stats(i)
    map[x, y]['Faction'] = faction



def define_background():
    global background
    background = np.zeros((20, 20))
    for i in range(20):
        for j in range(20):
            background[i, j] = random.randint(0, 10)  # Randomly assign 0 or 1
    return background

def draw_background():
    global background
    for y in range(20):
        for x in range(20):
            if background[x, y] == 0:
                draw_image(IMAGES["ground"], (x+5) * 40 + 20, (y) * 40 + 20, 0, 40)
            if background[x, y] == 1:
                draw_image(IMAGES["grass"], (x+5) * 40 + 20, (y) * 40 + 20, 0, 40)


            #pygame.draw.rect(screen, (50, 50, 50), rect)  # Dark gray for empty cells
            #pygame.draw.rect(screen, (100, 100, 100), rect, 1)  # Grid lines
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(5 * 40, 0 * 40, 20 * 40+1, 20 * 40), 1)  # Outer border

def draw_units():
    for y in range(20):
        for x in range(20):
            unit_name = str(map[x, y]["Name"])
            if unit_name and unit_name in IMAGES:
                draw_image(IMAGES[map[x,y]['Name']], (x+5) * 40 + 20, (y) * 40 + 20, 0, 32)
                
def Next_turn():
    global map
    speed_list = []
    for y in range(20):
        for x in range(20):
            if map[x, y]['Name'] != '':
                speed_list.append((map[x, y]['Speed'], x, y))
    for speed, x, y in sorted(speed_list, reverse=True):
        turn(x, y)

def turn(x, y):
    global map
    #if enemy not in range move towards enemy
    move(x, y, map[x, y]['Speed'], map[x,y]['abilities'], map[x, y]['Faction'])
    #attack if enemy in range
    use_abilties(x, y, map[x, y]['Abilities'], map[x, y]['Faction'])

def move(x, y, speed, abilities, faction):
    global map
    distance_map = np.full((20, 20), np.inf)
    distance_map[x, y] = 0
    for i in range(x):
        for j in range(y):
            if map[i, j]['Name'] != '':
                distance_map[i, j] = -1
    
    
    


def game_loop():

    # Main loop
    running = True
    turn= 0

    define_background()
    create_unit(1, 0, 5, 5)
    create_unit(0, 1, 2, 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    turn += 1
                    Next_turn()



        screen.fill((20,20,20)) 
        draw_background()
        draw_units()
        
            
        

        


        
        if(pygame.key.get_pressed()[pygame.K_p]):
            draw_text(f"FPS: {clock.get_fps():.1f}", text_font, (255, 255, 255), 10, 10, center=False)
        pygame.display.flip()
        clock.tick(60)





#gameloop start

game_loop()



pygame.quit()