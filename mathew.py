# Mathew's code goes here
import pygame

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Platform data: (x, y, width, height)
platforms_data = [
    (0, 550, 800, 50),  # Ground platform
    (150, 400, 100, 20),
    (400, 300, 150, 20)
]

# List of rect objects
platforms = [pygame.Rect(data) for data in platforms_data]

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
    pass


def draw(screen):
    """Draw Mathew's visuals to the screen."""
    for platform in platforms:
        pygame.draw.rect(screen, (225,255,0), platform)
