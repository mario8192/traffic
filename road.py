import pygame
import copy
from textures import texture_dict
from params import CELLS_X, CELLS_Y


class Road(pygame.sprite.Sprite):

    def __init__(self, grid):
        self.grid = grid
        # self.grid_textures = copy.deepcopy(grid)
        # self.rects = copy.deepcopy(grid)

    def road_texture(self, grid, i, j):
        # getting trbl elem beforehand because dict error later
        top_elem = i > 0 and self.grid[i-1][j]
        right_elem = j < CELLS_X-1 and self.grid[i][j+1]
        bott_elem = i < CELLS_Y-1 and self.grid[i+1][j]
        left_elem = j > 0 and self.grid[i][j-1]

        texture = texture_dict[self.grid[i][j]["value"]]
        if self.grid[i][j]["value"] != "0":
            # checked which sides of road should be blocked
            blocked_trbl = [0, 0, 0, 0]
            blocked_trbl[0] = int(i > 0 and top_elem["value"] == "0")
            blocked_trbl[1] = int(j < CELLS_X-1 and right_elem == "0")
            blocked_trbl[2] = int(i < CELLS_Y-1 and bott_elem == "0")
            blocked_trbl[3] = int(j > 0 and left_elem["value"] == "0")
            # load texture based on sides blocked
            texture = texture_dict[str(blocked_trbl)]
        return texture

    def build(self):
        for i in range(0, CELLS_Y):
            for j in range(0, CELLS_X):
                self.grid[i][j] = {
                    "value": self.grid[i][j],
                    "texture": None,
                    "rect": None
                }
                self.grid[i][j]["texture"] = self.road_texture(self.grid, i, j)
                self.grid[i][j]["rect"] = self.grid[i][j]["texture"].get_rect()
                self.grid[i][j]["rect"].x = j*100
                self.grid[i][j]["rect"].y = i*100
                # print(self.grid[i][j]["rect"])

    def draw(self, screen):
        for i in range(0, CELLS_Y):
            for j in range(0, CELLS_X):
                screen.blit(self.grid[i][j]["texture"], (j*100, i*100))
                # print(self.grid[i][j]["rect"])
