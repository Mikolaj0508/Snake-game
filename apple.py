import random
import pygame
from pygame.locals import *


SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('resources/Image.png').convert()
        self.parent_screen = parent_screen
        self.x = SIZE*2
        self.y = SIZE*2

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 24)*SIZE
        self.y = random.randint(0, 19)*SIZE