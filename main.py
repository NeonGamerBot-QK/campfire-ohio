from Game import Game
import pygame
import menu

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Water Space Platformer")
clock = pygame.time.Clock()
game = Game(clock)

# Track whether the game has started
game_started = False


def start_game():
    """Callback for the menu Play button."""
    global game_started
    game.setup(screen)
    game_started = True
    main_menu.disable()


main_menu = menu.create_menu(screen, start_game)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if main_menu.is_enabled():
        main_menu.update(events)
        if main_menu.is_enabled():
            main_menu.draw(screen)
            pygame.display.flip()
    elif game_started:
        if not game.running:
            break
        for event in events:
            game.handle_event(event)
        game.update()
        game.draw()

pygame.quit()
