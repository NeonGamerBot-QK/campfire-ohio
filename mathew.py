# Mathew's code goes here

_screen = None


def setup(screen):
    """Initialize Neon's module with the display surface."""
    global _screen
    _screen = screen


def handle_event(event):
    """Handle pygame events for Neon's module."""
    pass


def update(dt):
    """Update Neon's game logic each frame."""
    pass


def draw(screen):
    """Draw Neon's visuals to the screen."""
    screen.fill((255, 0, 255))  # Neon pink background
