import pygame
import asyncio
import sys
from Game import Game
from menu import SimpleMenu

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Water Space Platformer")
clock = pygame.time.Clock()

game = Game(clock)
game_started = False


def start_game():
    global game_started
    game.setup(screen)
    game_started = True
    main_menu.disable()


main_menu = SimpleMenu(screen, start_game)


async def main():
    global game_started

    while True:
        await asyncio.sleep(0)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if main_menu.is_enabled():
            main_menu.update(events)
            main_menu.draw()
        else:
            # Game runs once menu is disabled
            for event in events:
                game.handle_event(event)

            if game.running:
                game.update()
                game.draw()
            else:
                # Don't break in browser
                game.running = True

        pygame.display.flip()
        clock.tick(60)


asyncio.run(main())
