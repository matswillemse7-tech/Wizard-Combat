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
pixel_font = pygame.font.Font("graphics/Retro Gaming.ttf", 24)
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

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(5 * 40, 0 * 40, 20 * 40+1, 20 * 40), 1)  # Outer border

def draw_units():
    global keys, see_faction
    for y in range(20):
        for x in range(20):
            unit_name = str(map[x, y]["Name"])
            if unit_name and unit_name in IMAGES:
                draw_image(IMAGES[map[x,y]['Name']], (x+5) * 40 + 20, (y) * 40 + 20, 0, 32)
            if (map[x,y]['Faction'] != 1) & (map[x,y]['Faction'] != 0) & see_faction:
                draw_image(IMAGES['enemy'], (x+5) * 40 + 28, (y) * 40 + 12, 0, 32)
            if (map[x,y]['Faction'] == 1 ) & see_faction:
                draw_image(IMAGES['friend'], (x+5) * 40 + 28, (y) * 40 + 12, 0, 32)
                

def def_collermaps():
    global color_map_main, color_map_second
    color_map_main = {
        'physical': (130, 130, 130),        # gray
        'water': (100, 130, 220),        # blue
        'fire': (220, 170, 0),        # red
        'plant': (156, 220, 156),        # green
        'lightning': (220, 220, 0),      # yellow
        'ice': (200, 200, 255),        # blue
        'earth': (150, 144, 133),        # brown
        'blood': (160, 100, 100),        # red
        'holy': (255, 255, 180),      # yellow
        'dark': (50, 30, 60), #deep purple
        'air': (200, 220, 228), #light cyanblue
        'technology': (130, 118, 110) #brown
        }


    color_map_second = {
        'physical': (115, 115, 115),        # gray
        'water': (90, 120, 200),        # blue
        'fire': (200, 155, 0),        # red
        'plant': (140, 200, 140),        # green
        'lightning': (200, 200, 0),      # yellow
        'ice': (180, 180, 233),        # blue
        'earth': (137, 131, 121),        # brown
        'blood': (146, 90, 90),        # red
        'holy': (245, 245, 170),      # yellow
        'dark': (40, 20, 50), #deep purple
        'air': (180, 200, 208), #light cyanblue
        'technology': (120, 110, 103) #brown
        }
  

def draw_turn_stuff(x, y):
    global map, turn_order, turn, full_turn, color_map_main, color_map_secondary
    pygame.draw.rect(screen, (80, 80, 100), pygame.Rect(1000, 0, 200, 140)) 
    pygame.draw.rect(screen, (40, 40, 50), pygame.Rect(1065, 38, 68, 68))
    name = str(map[x, y]["Name"])
    name = name.replace("_", " ")
    draw_text(name, pixel_font, (255, 255, 255), 1100, 20)
    draw_image(IMAGES[map[x,y]['Name']], 1100, 70, 0, 64)
    pygame.draw.rect(screen, (50, 30, 40), pygame.Rect(1002, 138, 198, 32),4) 
    pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(1004, 142, 194*(map[x,y]['Health']/map[x,y]['Maxhealth']), 24)) 
    draw_text(f'{map[x,y]['Health']}/{map[x,y]['Maxhealth']}', pixel_font,(255, 200, 200), 1100, 154)
    if map[x,y]['Abilities'] != 0:
        for i, ability in enumerate(map[x,y]['Abilities']):
            pygame.draw.rect(screen, (80, 80, 100), pygame.Rect(1004, 175+(i*124), 192, 120))
            pygame.draw.rect(screen, (60, 60, 100), pygame.Rect(1004, 175+(i*124), 192, 120), 4)
            name = str(ability["Name"].item()); name = name.replace("_", " ")
            draw_text(name, pixel_font, (color_map_main[str(ability['Type'].item())]),1100, 190+(i*124))  




                
def Next_full_turn():
    global map, turn_order, turn, full_turn, round_number
    full_turn = 0
    round_number +=1
    turn= 0
    speed_list = []
    for y in range(20):
        for x in range(20):
            if map[x, y]['Name'] != '':
                speed_list.append((map[x, y]['Speed'], x, y))
    random.shuffle(speed_list)
    turn_order = sorted(speed_list, reverse=True)
        

def unit_turn():
    global map, turn_order, turn, full_turn
    if turn < len(turn_order):
        x, y = turn_order[turn][1], turn_order[turn][2]
    
    draw_turn_stuff(x, y)

def key_toggles():
    global keys, see_faction, key_pressed
    
    if keys[pygame.K_LALT]:
        if key_pressed[0] == 0:
            key_pressed[0] = 1
            if see_faction == True:
                see_faction = False
            elif see_faction == False:
                see_faction = True
    else:
        key_pressed[0] = 0
    


    
    
    


def game_loop():
    global running, full_turn, round_number, mouse_buttons, keys,see_faction, key_pressed
    key_pressed = [0]
    # Main loop
    running = True
    see_faction = True
    full_turn = 1; round_number = 0
    
    define_background()
    def_collermaps()
    create_unit(1, 2, 5, 5)
    create_unit(0, 1, 2, 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        mouse_buttons = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        key_toggles()



        if full_turn == 1:
            Next_full_turn()
            

        screen.fill((20,20,20)) 
        draw_background()
        draw_units()
        unit_turn()
            
        

        


        
        if(pygame.key.get_pressed()[pygame.K_p]):
            draw_text(f"FPS: {clock.get_fps():.1f}", text_font, (255, 255, 255), 10, 10, center=False)
        pygame.display.flip()
        clock.tick(60)





#gameloop start

game_loop()



pygame.quit()