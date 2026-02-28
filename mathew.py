import pygame

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Platform data: (x, y, width, height)
platforms_data = [
    (0, 550, 800, 50),# Ground platform
    (150, 400, 100, 20),
    (400, 300, 150, 20)
]

# List of rect objects
platforms = [pygame.Rect(data) for data in platforms_data]
platform_speeds = [0, 2, 2] # Speed for each platform (0 for ground)

_screen = None

def setup(screen):
    """Initialize Mathew's module with the display surface."""
    global _screen
    _screen = screen

def handle_event(event):
    """Handle pygame events for Mathew's module."""
    pass

def update(dt):
    """Update Mathew's game logic each frame."""
    # Move platforms based on speed
    for i, platform in enumerate(platforms):
        platform.x += platform_speeds[i]
        # Simple bounce back logic for moving platforms
        if platform.left < 0 or platform.right > 800:
            platform_speeds[i] *= -1 # Corrected: string "-1" to number -1

def draw(screen):
    """Draw Mathew's visuals to the screen."""
    for platform in platforms:
        # Change screen(...) to a valid color tuple and use pygame.draw.rect correctly
        pygame.draw.rect(screen, GREEN, platform)
