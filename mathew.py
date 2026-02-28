import pygame
import Game  # Assuming grant has a rect and velocity (vx, vy)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Platform data: (x, y, width, height)
platforms_data = [
    (0, 550, 800, 50),# Ground platform
    (150, 400, 100, 20),(400, 300, 150, 20)
]

# List of rect objects
platforms = [pygame.Rect(data) for data in platforms_data]
platform_speeds = [0, 2, 2]  # Speed for each platform (0 for ground)

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
    # 1. Move platforms based on speed
    for i, platform in enumerate(platforms):
        platform.x += platform_speeds[i]
        # Simple bounce back logic for moving platforms
        if platform.left < 0 or platform.right > 800:
            platform_speeds[i] *= -1

    # 2. Handle Player-Platform Collisions (Assuming player is imported)
    # Horizontal Movement & Collision
    Game.self.rect.x += Game.player.vx
    hits = pygame.Rect.collidelistall(Game.player.rect, platforms)
    for index in hits:
        platform = platforms[index]
        if Game.self.vx > 0:  # Moving right
            Game.self.rect.right = platform.left
        elif Game.self.vx < 0:  # Moving left
            Game.self.rect.left = platform.right

    # Vertical Movement & Collision
    Game.self.rect.y += Game.self.vy
    hits = pygame.Rect.collidelistall(Game.self.rect, platforms)
    for index in hits:
        platform = platforms[index]
        if Game.self.vy > 0:  # Falling down
            Game.self.rect.bottom = platform.top
            Game.self.vy = 0  # Stop falling
            Game.self.on_ground = True
        elif Game.self.vy < 0:  # Jumping up
            Game.self.rect.top = platform.bottom
            Game.self.vy = 0  # Stop upward movement

def draw(screen):
    """Draw Mathew's visuals to the screen."""
    for platform in platforms:
        # Corrected: Use pygame.draw.rect correctly
        pygame.draw.rect(screen, GREEN, platform)
