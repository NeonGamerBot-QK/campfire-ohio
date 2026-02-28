from Game import Game
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Water Space Platformer")
clock = pygame.time.Clock()
game = Game()

game.setup(screen, clock)

while game.running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        game.handle_event(event)

    game.update(dt)

    game.draw()

    pygame.display.flip()

pygame.quit()
