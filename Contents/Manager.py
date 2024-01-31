# Constants
from Contents.Constants import Consts

# Models (Classes)
from Contents.Fruit import Fruit
from Contents.Snake import Snake

#Libraries
import pygame

class Manager():
    def run():
        pygame.init()
        screen = pygame.display.set_mode((Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        clock = pygame.time.Clock()
        snake = Snake()
        fruit = Fruit()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.turn(Consts.DIRECTIONS["UP"])
                    elif event.key == pygame.K_DOWN:
                        snake.turn(Consts.DIRECTIONS["DOWN"])
                    elif event.key == pygame.K_LEFT:
                        snake.turn(Consts.DIRECTIONS["LEFT"])
                    elif event.key == pygame.K_RIGHT:
                        snake.turn(Consts.DIRECTIONS["RIGHT"])

            snake.move()
            if snake.get_head_position() == fruit.position:
                snake.length += 1
                fruit.randomize_position()

            screen.fill(Consts.COLORS["WHITE"])
            snake.draw(screen)
            fruit.draw(screen)
            pygame.display.update()
            clock.tick(10)