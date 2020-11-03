import pygame
from random import randint

X_OFFSET = 25
Y_OFFSET = 10
MAX_SPEED = 2
REVERSE_SPEED = 1


class Car(pygame.sprite.Sprite):

    def turn_up(self):
        if self.direction != "S":
            self.direction = "N"
            self.reverse = False
        else:
            self.reverse = True

    def turn_down(self):
        if self.direction != "N":
            self.direction = "S"
            self.reverse = False
        else:
            self.reverse = True

    def turn_left(self):
        if self.direction != "E":
            self.direction = "W"
            self.reverse = False
        else:
            self.reverse = True

    def turn_right(self):
        if self.direction != "W":
            self.direction = "E"
            self.reverse = False
        else:
            self.reverse = True

    def move_up(self):
        self.turn_up()
        self.velX = 0
        self.velY = -1

    def move_down(self):
        self.turn_down()
        self.velX = 0
        self.velY = 1

    def move_left(self):
        self.turn_left()
        self.velX = -1
        self.velY = 0

    def move_right(self):
        self.turn_right()
        self.velX = 1
        self.velY = 0

    move_dict = {
        "N": move_up,
        "S": move_down,
        "W": move_left,
        "E": move_right
    }

    car_texture = {}

    def load_car_texture(self):
        self.car_texture = {
            "car": self.image,
            "car90": pygame.transform.rotate(self.image, 90),
            "car180": pygame.transform.rotate(self.image, 180),
            "car270": pygame.transform.rotate(self.image, 270),
            "N": "car",
            "S": "car180",
            "W": "car90",
            "E": "car270",
            "trans": self.trans,
            "trans90": pygame.transform.rotate(self.trans, 90),
            "trans180": pygame.transform.rotate(self.trans, 180),
            "trans270": pygame.transform.rotate(self.trans, 270),
            "NT": "trans",
            "ST": "trans180",
            "WT": "trans90",
            "ET": "trans270",
        }

    def __init__(self, X, Y):
        super().__init__()

        # self.posX = X
        # self.posY = Y
        self.velX = 0
        self.velY = 0
        self.direction = "N"
        self.reverse = False
        self.accelerating = False
        self.colliding = False
        self.color = "COLOR" + str(randint(1, 5))

        self.image = pygame.image.load('./cars/'+self.color+'.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.trans = pygame.image.load('./cars/TRANS.png')
        self.trans = pygame.transform.scale(self.trans, (45, 45))
        self.load_car_texture()
        self.image = self.car_texture[self.car_texture[self.direction]]
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y

    def move(self, dir):
        self.move_dict[dir](self)

    def update(self):
        # update direction
        self.image = self.car_texture[self.car_texture[self.direction]]
        # update velocity if accelerating or decelerating
        if self.accelerating:
            if self.velocity_axis[self.direction] == 0 and abs(self.velX) < 1:
                self.velX += self.velocity_polarity[self.direction]*abs(
                    self.velX)
                print('velx', self.velX)
            elif self.velocity_axis[self.direction] == 1 and abs(self.velY) < 1:
                self.velY += self.velocity_polarity[self.direction]*abs(
                    self.velY)
                print('vely', self.velY)
            else:
                print("reached max speed")
                self.accelerating = False
        # limit velocity to 1
        if abs(self.velX) > 1:
            self.velX = self.velocity_polarity[self.direction]
        elif abs(self.velY) > 1:
            self.velY = self.velocity_polarity[self.direction]

        # update position
        if self.reverse:
            self.rect.x += self.velX * REVERSE_SPEED
            self.rect.y += self.velY * REVERSE_SPEED
        else:
            self.rect.x += self.velX * MAX_SPEED
            self.rect.y += self.velY * MAX_SPEED

        if self.colliding:
            # print("collide", self.color)
            self.image = self.car_texture[self.car_texture[self.direction+"T"]]

    velocity_polarity = {
        "N": -1,
        "W": -1,
        "S": 1,
        "E": 1
    }
    velocity_axis = {
        "N": 1,
        "W": 0,
        "S": 1,
        "E": 0
    }

    def accelerate(self):
        if self.velocity_axis[self.direction] == 0 and self.velX == 0:
            self.velX = 0.1 * self.velocity_polarity[self.direction]
            self.accelerating = True
        elif self.velocity_axis[self.direction] == 1 and self.velX == 0:
            self.velY = 0.1 * self.velocity_polarity[self.direction]
            self.accelerating = True

    # def accelerate(self):
    #     if self.velocity_axis[self.direction] == 0:
    #         self.velX = 0.1
    #         while round(self.velX) < 1:
    #             self.velX += self.velocity_polarity[self.direction]*self.velX
    #     elif self.velocity_axis[self.direction] == 1:
    #         self.velY = 0.1
    #         while round(self.velY) < 1:
    #             self.velY += self.velocity_polarity[self.direction]*self.velY

    def decelerate(self):
        while round(self.velX) > 0 or round(self.velY) > 0:
            if self.velX == 0:
                self.velY -= self.velY/10
            elif self.velY == 0:
                self.velX -= self.velX/10

    def stop(self):
        # self.decelerate()
        self.velX = 0
        self.velY = 0
