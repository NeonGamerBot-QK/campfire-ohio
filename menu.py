import pygame
import pygame_menu
import Game

pygame.init()
surface = pygame.display.set_mode((600, 400))

clock = pygame.time.Clock()
game = Game(clock)

def start_the_game():
    # This function is called when the "Play" button is clicked
    print("Game Started!")
    game.setup(screen)
    # Add your game logic here
    pass

# Create the menu
menu = pygame_menu.Menu('Welcome', 600, 400, theme=pygame_menu.themes.THEME_BLUE)

# Add a button that calls the 'start_the_game' function
menu.add.button('Play', start_the_game)

# Add a button to exit the application
menu.add.button('Exit', pygame_menu.events.EXIT)

# Main game loop
while True:
    # Handle events for the menu
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # If the menu is enabled, update and draw it
    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)

    # Update the display
    pygame.display.update()
