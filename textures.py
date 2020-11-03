import pygame

# from textures import (road_2, road_2_90, road_4, road_L,
#                       road_L_90, road_L_180, road_L_270, road_T, road_T_90, road_T_180, road_T_270, grass)

# road with 2 openings
road_2 = pygame.image.load('./textures/road-2.png')
road_2 = pygame.transform.scale(road_2, (100, 100))
road_2_90 = pygame.transform.rotate(road_2, 90)
# road with 4 openings / intersection
road_4 = pygame.image.load('./textures/road-4.png')
road_4 = pygame.transform.scale(road_4, (100, 100))
# road with 3 way openings / T shape
road_T = pygame.image.load('./textures/road-T.png')
road_T = pygame.transform.scale(road_T, (100, 100))
road_T_90 = pygame.transform.rotate(road_T, 90)
road_T_180 = pygame.transform.rotate(road_T, 180)
road_T_270 = pygame.transform.rotate(road_T, 270)
# rooad with 2 openings / L shape
road_L = pygame.image.load('./textures/road-L.png')
road_L = pygame.transform.scale(road_L, (100, 100))
road_L_90 = pygame.transform.rotate(road_L, 90)
road_L_180 = pygame.transform.rotate(road_L, 180)
road_L_270 = pygame.transform.rotate(road_L, 270)

grass = pygame.image.load('./textures/grass.jpg')
grass = pygame.transform.scale(grass, (100, 100))


texture_dict = {
    "-": road_2_90,
    "|": road_2,
    "[0, 0, 0, 0]": road_4,
    "[0, 1, 0, 1]": road_2,
    "[1, 0, 1, 0]": road_2_90,
    "[1, 0, 0, 0]": road_T,
    "[0, 1, 0, 0]": road_T_270,
    "[0, 0, 1, 0]": road_T_180,
    "[0, 0, 0, 1]": road_T_90,
    "[0, 0, 1, 1]": road_L,
    "[1, 0, 0, 1]": road_L_270,
    "[1, 1, 0, 0]": road_L_180,
    "[0, 1, 1, 0]": road_L_90,
    "0": grass
}
