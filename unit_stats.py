import pygame
import numpy as np
import random
import os


unit = np.dtype([
    ('Name', np.object_),
    ('Health', np.uint8),
    ('Maxhealth', np.uint8),
    ('Faction', np.uint8),
    ('Abilities', np.object_),
    ('Speed', np.uint8),
    ('turn', np.uint8)
])

def unit_stats(i):
    global unit_statsss
    return unit_statsss[i]

unit_statsss = np.zeros((100), dtype=unit)
def unit_statss(i, Name, Maxhealth, Abilities, Speed):
    global unit_stats
    unit_statsss[i]['Name'] = Name
    unit_statsss[i]['Health'] = Maxhealth
    unit_statsss[i]['Maxhealth'] = Maxhealth
    unit_statsss[i]['Faction'] = 0
    unit_statsss[i]['Abilities'] = Abilities
    unit_statsss[i]['Speed'] = Speed
    unit_statsss[i]['turn'] = 0

unit_statss(0, "blue_wiz", 80, ["fireball"], 5)
unit_statss(1, "green_wiz", 70, ["fireball", "zap"], 5)
unit_statss(2, "purple_wiz", 60, ["fireball"], 6)
unit_statss(3, "orange_wiz", 90, ["fireball"], 4)

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

ability = np.dtype([
    ('Name', np.object_),
    ('Damage', np.object_),
    ('Type', np.object_),
    ('Purpose', np.object_),
    ('Attributes', np.object_),
    ('Range', np.uint8),
    ('Cooldown', np.uint8),
    ('Cooldown_current', np.uint8)
    ])

damage = np.dtype([
    ('Min', np.uint8),
    ('Max', np.uint8),
    ('Type', np.object_)])


def ability_stats(i):
    global ability_statsss
    return ability_statsss[i]
ability_statsss = np.zeros((100), dtype=ability)
def ability_statss(i, Name, Damage, Range, Cooldown, Purpose, Attributes, Type):
    global ability_statsss
    ability_statsss[i]['Name'] = Name
    ability_statsss[i]['Damage'] = Damage
    ability_statsss[i]['Type'] = Type
    ability_statsss[i]['Range'] = Range
    ability_statsss[i]['Purpose'] = Purpose
    ability_statsss[i]['Cooldown'] = Cooldown
    ability_statsss[i]['Cooldown_current'] = 0
    ability_statsss[i]['Attributes'] = Attributes

ability_statss(0, Name = "fireball", Damage = [4,7, 'fire'], Purpose='attack', Type = 'fire', Range = 4, Cooldown = 2, Attributes = ['exploding_1', 'burn_2'])
ability_statss(1, Name = "zap", Damage = [1,9, 'lightning'], Purpose='attack', Type = 'lightning', Range = 6, Cooldown = 2, Attributes = ['chaining_1'])
ability_statss(1, Name = "tear_assunder", Damage = [6,9, 'blood'], Purpose='attack', Type = 'blood', Range = 1, Cooldown = 1, Attributes = ['bleed_2'])