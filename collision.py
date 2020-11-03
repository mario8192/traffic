import pygame
import copy


def check_collisions(cars, grid):
    # carsd = copy.deepcopy(cars)
    for car in cars:
        car.colliding = False
        for car2 in cars:
            car.colliding = car2 != car and bool(
                car2.rect.colliderect(car.rect))
            if car.colliding:
                break
        if not car.colliding:
            # print(grid)
            for row in grid:
                for tile in row:
                    car.colliding = (tile["value"] == '0') and bool(tile["rect"].colliderect(
                        car.rect))
                    if car.colliding:
                        break
                if car.colliding:
                    break
                    # print(tile["rect"], car.rect, bool(
                    #     tile["rect"].colliderect(car.rect)), tile["value"] == '0')
                    # print(car.colliding)
