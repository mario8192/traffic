import pygame
from car import Car
from road import Road
from keys import control
from params import CELLS_X, CELLS_Y
from collision import check_collisions

pygame.init()
flags = pygame.HWSURFACE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((CELLS_X*100, CELLS_Y*100), flags)
clock = pygame.time.Clock()
pygame.display.set_caption("Traffic")

grid = [["0", "0", "0", "0", "0", "0", "|", "0"],
        ["0", "0", "0", "0", "0", "|", "|", "0"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["0", "|", "0", "|", "0", "|", "|", "0"],
        ["0", "|", "-", "-", "0", "|", "|", "0"],
        ["0", "|", "0", "0", "0", "|", "|", "0"]
        ]

if __name__ == "__main__":
    running = True

    road = Road(grid)
    road.build()
    car = Car(300, 400)
    car2 = Car(300, 200)
    car3 = Car(500, 200)
    cars = [car, car2, car3]

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(car)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                car.stop()
            elif event.type == pygame.KEYDOWN:
                control(car, event.key)

        check_collisions(cars, grid)
        road.draw(screen)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        # update screen
        pygame.display.flip()
        clock.tick(60)
        # end of game loop
