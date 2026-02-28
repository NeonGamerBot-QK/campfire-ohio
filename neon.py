# Neon's code goes here
import pygame
import grant
from healthbar import *
_screen = None
hb = None

max_health = 100
health = 20
ratio = health / max_health

def setup(game):
    """Initialize Neon's module with the Game instance."""
    global _screen, hb
    _screen = game.screen
    hb = HealthBar(10, 10, 200, 20, max_health)
    hb.hp = health


def handle_event(event):
    """Handle pygame events for Neon's module."""
    pass


def update(dt):
    """Update Neon's game logic each frame."""
    if not grant.player.sprites():
        return
    sprite = grant.player.sprites()[0]
    screen_width, screen_height = _screen.get_size()
    # Clamp player position to screen bounds
    sprite.rect.clamp_ip(pygame.Rect(0, 0, screen_width, screen_height))

"""
@source https://stackoverflow.com/questions/52045413/setting-screen-fill-as-a-gradient-in-pygame
"""
def vertical(size, startcolor, endcolor):
    """
    Draws a vertical linear gradient filling the entire surface. Returns a
    surface filled with the gradient (numeric is only 2-3 times faster).
    """
    height = size[1]
    bigSurf = pygame.Surface((1,height)).convert_alpha()
    dd = 1.0/height
    sr, sg, sb, sa = startcolor
    er, eg, eb, ea = endcolor
    rm = (er-sr)*dd
    gm = (eg-sg)*dd
    bm = (eb-sb)*dd
    am = (ea-sa)*dd
    for y in range(height):
        bigSurf.set_at((0,y),
                        (int(sr + rm*y),
                         int(sg + gm*y),
                         int(sb + bm*y),
                         int(sa + am*y))
                      )
    return pygame.transform.scale(bigSurf, size)


def draw(screen):
    """Draw Neon's visuals to the screen."""
    gradient_surface = vertical(screen.get_size(), (0, 255, 255, 255),(0, 0, 255, 255))
    screen.blit(gradient_surface, (0, 0))
    if hb:
        hb.draw(screen)
