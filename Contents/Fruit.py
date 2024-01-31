from Contents.Constants import Consts
import pygame, random

class Fruit:
    def __init__(self):
        self.position = (0, 0)
        self.color = Consts.COLORS["RED"]
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (Consts.SCREEN_WIDTH-Consts.BLOCK_SIZE)//Consts.BLOCK_SIZE) * Consts.BLOCK_SIZE, random.randint(0, (Consts.SCREEN_HEIGHT-Consts.BLOCK_SIZE)//Consts.BLOCK_SIZE) * Consts.BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect((self.position[0], self.position[1]), (Consts.BLOCK_SIZE, Consts.BLOCK_SIZE)))
        pygame.draw.rect(surface, Consts.COLORS["BLACK"], pygame.Rect((self.position[0], self.position[1]), (Consts.BLOCK_SIZE, Consts.BLOCK_SIZE)), 1)

