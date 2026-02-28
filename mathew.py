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
platform_speeds = [0, 2, 2]  # Speed for each platform (0 for ground)

_screen = None
_game = None


def setup(game):
    """Initialize Mathew's module with the Game instance."""
    global _screen, _game
    _game = game
    _screen = game.screen
    game.platforms = platforms


def handle_event(event):
    """Handle pygame events for Mathew's module."""
    pass


def update(dt):
    """Update Mathew's game logic each frame."""
    if _game.game_over:
        return

    # Move platforms based on speed
    for i, platform in enumerate(platforms):
        platform.x += platform_speeds[i]
        if platform.left < 0 or platform.right > 800:
            platform_speeds[i] *= -1

    if not _game.player or not _game.player.animated_sprite.sprites():
        return
    sprite = _game.player.animated_sprite.sprites()[0]

    # --- FIXED COLLISION LOGIC ---
    
    # 1. Horizontal Movement and Collision
    sprite.rect.x += sprite.vx * dt
    for platform in platforms:
        if sprite.rect.colliderect(platform):
            if sprite.vx > 0:
                sprite.rect.right = platform.left
            elif sprite.vx < 0:
                sprite.rect.left = platform.right

    # 2. Vertical Movement and Collision
    sprite.rect.y += sprite.vy * dt
    for platform in platforms:
        if sprite.rect.colliderect(platform):
            if sprite.vy > 0:
                sprite.rect.bottom = platform.top
                sprite.vy = 0 # Landed
            elif sprite.vy < 0:
                sprite.rect.top = platform.bottom
                sprite.vy = 0 # Hit ceiling


def draw(screen):
    """Draw Mathew's visuals to the screen."""
    if _game.game_over:
        return
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

