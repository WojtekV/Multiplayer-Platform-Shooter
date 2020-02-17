import pygame
from Properties import *


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.velocity_x = bullet_velocity_x
        self.velocity_y = 0
        self.radius = bullet_radius
        self.color = bullet_color
        self.direction = direction

    def move(self):
        self.x += self.direction * self.velocity_x
        self.velocity_y += gravity*delta_t/18
        self.y += self.velocity_y

    def draw(self, win):
        self.move()
        pygame.draw.rect(win, bullet_color, (self.x, self.y, 5, 5))