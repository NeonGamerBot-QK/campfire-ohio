import pygame

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Platform levels: each entry is a list of (x, y, width, height) tuples + speeds
PLATFORM_LEVELS = [
    {
        "platforms": [(0, 550, 800, 50), (150, 400, 100, 20), (400, 300, 150, 20)],
        "speeds": [0, 2, 2],
    },
    {
        "platforms": [(0, 550, 800, 50), (100, 450, 120, 20), (300, 350, 100, 20), (550, 250, 130, 20)],
        "speeds": [0, -2, 3, -2],
    },
    {
        "platforms": [(0, 550, 800, 50), (50, 420, 80, 20), (250, 330, 80, 20), (450, 240, 80, 20), (650, 150, 80, 20)],
        "speeds": [0, 3, -3, 3, -3],
    },
]

current_platform_level = 0

# List of rect objects (initialized to first level)
platforms = [pygame.Rect(data) for data in PLATFORM_LEVELS[0]["platforms"]]
platform_speeds = list(PLATFORM_LEVELS[0]["speeds"])


def switch_platform_level(level_index):
    """Switch to a new platform layout by index (wraps around)."""
    global platforms, platform_speeds, current_platform_level
    current_platform_level = level_index % len(PLATFORM_LEVELS)
    level_data = PLATFORM_LEVELS[current_platform_level]
    platforms = [pygame.Rect(data) for data in level_data["platforms"]]
    platform_speeds = list(level_data["speeds"])
    if _game:
        _game.platforms = platforms

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

    # Handle player-platform collisions
    if not _game.player or not _game.player.sprite.sprites():
        return
    sprite = _game.player.sprite.sprites()[0]

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

