import pygame, random
from Contents.Constants import Consts

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((Consts.SCREEN_WIDTH / 2), (Consts.SCREEN_HEIGHT / 2))]
        self.direction = random.choice([Consts.DIRECTIONS["UP"], Consts.DIRECTIONS["DOWN"], Consts.DIRECTIONS["LEFT"], Consts.DIRECTIONS["RIGHT"]])
        self.color = Consts.COLORS["GREEN"]

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*Consts.BLOCK_SIZE)) % Consts.SCREEN_WIDTH), (cur[1] + (y*Consts.BLOCK_SIZE)) % Consts.SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((Consts.SCREEN_WIDTH / 2), (Consts.SCREEN_HEIGHT / 2))]
        self.direction = random.choice([Consts.DIRECTIONS["UP"], Consts.DIRECTIONS["DOWN"], Consts.DIRECTIONS["LEFT"], Consts.DIRECTIONS["RIGHT"]])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (Consts.BLOCK_SIZE, Consts.BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, Consts.COLORS["BLACK"], r, 1)

