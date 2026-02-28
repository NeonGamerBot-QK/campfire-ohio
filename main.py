from Game import Game
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Water Space Platformer")
clock = pygame.time.Clock()
game = Game(clock)

game.setup(screen)

while game.running:
    for event in pygame.event.get():
        game.handle_event(event)

    game.update()

    game.draw()

pygame.quit()
