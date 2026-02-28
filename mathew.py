# Mathew's code goes here
_screen = None

def setup(screen):
    """Initialize Neon's module with the display surface."""
    import pygame

    pygame.init()

    pygame.display.set_caption("Platform Example")

    #Colors
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    #Platform sizea:
    platforms_data = [
        (0, 550, 800, 50),  #Ground platform
        (150, 400, 100, 20),
        (400, 300, 150, 20)
    ]

    #List of rect objects
    platforms = []
    for platform_rect_data in platforms_data:
        platforms.append(pygame.Rect(platform_rect_data))

def handle_event(event):
    """Handle pygame events for Neon's module."""
        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(screen, BLUE, platform) #

    pass

def update(dt):
    """Update Neon's game logic each frame."""
        # Update the display
    pygame.display.flip()
    clock.tick(60)
    pass


def draw(screen):
    """Draw Neon's visuals to the screen."""
    pass
