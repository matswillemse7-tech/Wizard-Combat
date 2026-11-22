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
unit_statss(1, "green_wiz", 70, ["fireball", "lightning"], 5)
unit_statss(2, "purple_wiz", 60, ["fireball"], 6)
unit_statss(3, "orange_wiz", 90, ["fireball"], 4)



ability = np.dtype([
    ('Name', np.object_),
    ('Damage', np.object_),
    ('Type', np.object_),
    ('Purpose', np.object_),
    ('Range', np.uint8),
    ('Cooldown', np.uint8)])

damage = np.dtype([
    ('Min', np.uint8),
    ('Max', np.uint8),
    ('Type', np.object_)])


def ability_stats(i):
    global ability_statsss
    return ability_statsss[i]
ability_statsss = np.zeros((100), dtype=ability)
def ability_statss(i, Name, Damage, Range, Cooldown):
    global ability_statsss
    ability_statsss[i]['Name'] = Name
    ability_statsss[i]['Damage'] = Damage
    ability_statsss[i]['Range'] = Range
    ability_statsss[i]['Cooldown'] = Cooldown

ability_statss(0, "fireball", [(1,8)], 5, 2)
