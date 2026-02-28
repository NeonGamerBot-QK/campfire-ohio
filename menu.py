import pygame
import pygame_menu


def create_menu(screen, on_play):
    """
    Create and return the main menu.

    Args:
        screen: The pygame display surface.
        on_play: Callback function to run when 'Play' is pressed.

    Returns:
        The pygame_menu.Menu instance.
    """
    width, height = screen.get_size()
    main_menu = pygame_menu.Menu(
        'Water Space Platformer', width, height,
        theme=pygame_menu.themes.THEME_BLUE
    )
    main_menu.add.button('Play', on_play)
    main_menu.add.button('Exit', pygame_menu.events.EXIT)
    return main_menu
