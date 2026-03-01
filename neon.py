# Neon's code goes here
import os
import random
import pygame
from healthbar import *
from Npc import Npc
import mathew
_screen = None
_game = None
hb = None

max_health = 100
health = 100
ratio = health / max_health
NPC_COUNT = 2
VARIANTS = [str(v) for v in range(1, 7)]


def spawn_npc():
    """Spawn a single NPC at a random position with a random water asset variant."""
    screen_width, screen_height = _screen.get_size()
    variant = random.choice(VARIANTS)
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 150)
    return Npc(pygame.sprite.Group(), f"./assets/Water assets/{variant}", x=x, y=y,
               patrol_speed=random.randint(40, 120))

def setup(game):
    """Initialize Neon's module with the Game instance."""
    global _screen, _game, hb
    _game = game
    _screen = game.screen
    hb = HealthBar(10, 10, 200, 20, max_health)
    game.healthbar = hb
    hb.hp = health
    # Spawn initial NPCs
    for _ in range(NPC_COUNT):
        _game.npcs.append(spawn_npc())


def handle_event(event):
    """Handle pygame events for Neon's module."""
    if event.type == pygame.KEYDOWN:
        # Press P to take 10 damage (temp, requires SELF_DAMADGE_CODE env var)
        if event.key == pygame.K_p and hb and os.environ.get("SELF_DAMADGE_CODE"):
            hb.hp = max(0, hb.hp - 10)
        # Press R to restart after game over
        if event.key == pygame.K_r and _game.game_over:
            _game.game_over = False
            hb.hp = max_health


def update(dt):
    """Update Neon's game logic each frame."""
    if _game.game_over:
        return
    # Trigger game over when health runs out
    if hb and hb.hp <= 0:
        _game.game_over = True
        return
    if not _game.player or not _game.player.sprite.sprites():
        return
    sprite = _game.player.sprite.sprites()[0]
    screen_width, screen_height = _screen.get_size()
    # Clamp player position to screen bounds
    sprite.rect.clamp_ip(pygame.Rect(0, 0, screen_width, screen_height))
    # Update NPCs with player proximity and shock damage
    for npc in _game.npcs:
        npc.update(dt, player=_game.player, healthbar=hb)
    # Remove dead NPCs, award XP, and respawn replacements
    respawn_count = 0
    previous_level = _game.player.level
    for npc in _game.npcs:
        if npc.removable:
            levels = _game.player.gain_xp(2)
            # Increase max HP by 1 and heal 10% per level gained
            if levels > 0 and hb:
                hb.max_hp += levels
                hb.hp = min(hb.max_hp, hb.hp + int(hb.max_hp * 0.1) * levels)
            respawn_count += 1
    # Switch platform level every 3 player levels
    new_level = _game.player.level
    if new_level // 3 > previous_level // 3:
        mathew.switch_platform_level(new_level // 3)
    _game.npcs[:] = [npc for npc in _game.npcs if not npc.removable]
    for _ in range(respawn_count):
        _game.npcs.append(spawn_npc())

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
    if _game.game_over:
        # Semi-transparent black overlay (20% opacity) over the background
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 51))
        screen.blit(overlay, (0, 0))
        font = pygame.font.SysFont(None, 72)
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
        # Restart prompt
        small_font = pygame.font.SysFont(None, 36)
        restart_text = small_font.render("Press R to restart", True, (255, 255, 255))
        screen.blit(restart_text, restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50)))
        return
    gradient_surface = vertical(screen.get_size(), (0, 255, 255, 255),(0, 0, 255, 255))
    screen.blit(gradient_surface, (0, 0))
    for npc in _game.npcs:
        npc.draw(screen)
    if hb:
        hb.draw(screen)
    # Draw level and XP below the health bar
    if _game.player:
        font = pygame.font.SysFont(None, 24)
        level_text = font.render(f"Lv {_game.player.level}  XP {_game.player.xp}/{_game.player.xp_to_next_level}", True, (255, 255, 255))
        screen.blit(level_text, (10, 35))
