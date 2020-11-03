import pygame


def control(car, key):
    press = {
        pygame.K_UP: car.move_up,
        pygame.K_LEFT: car.move_left,
        pygame.K_DOWN: car.move_down,
        pygame.K_RIGHT: car.move_right
    }
    try:
        press[key]()
    except:
        pass
