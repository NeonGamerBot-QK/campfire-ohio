# Grant's code goes here
import os
from AnimatedSprite import AnimatedSprite
import pygame
import sys
import random

_screen = None
player = pygame.sprite.Group()
pressed_keys = set()


def setup(screen):
    """Initialize Grant's module with the display surface."""
    global _screen
    _screen = screen

    initiate_sprites()

    
def initiate_sprites():
    global player

    FRAME_WIDTH = 48
    FRAME_HEIGHT = 48

    animation_frames = {}

    path = "./Sprites/Character Animations/"

    for file_name in os.listdir(path):
        image = pygame.image.load(os.path.join(path, file_name)).convert_alpha()

        sheet_width = image.get_width()
        sheet_height = image.get_height()

        N_FRAMES = sheet_width // FRAME_WIDTH

        animation_name = file_name.replace(".png", "")
        frames = []

        for i in range(N_FRAMES):
            frame = image.subsurface((i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT))
            frames.append(frame)
        animation_frames[animation_name] = frames
    
    player.add(AnimatedSprite(0, 0, animation_frames, default_animation="Idle", animation_speed=7))

def handle_event(event):
    global pressed_keys
    if event.type == pygame.KEYDOWN:
        pressed_keys.add(event.key)
    elif event.type == pygame.KEYUP:
        pressed_keys.discard(event.key)

def update(dt):
    global player, pressed_keys
    if not player.sprites(): return
    
    sprite = player.sprites()[0]
    vx, vy = 0, 0
    
    if any(k in pressed_keys for k in [pygame.K_d, pygame.K_RIGHT]):
        vx += 150
        sprite.flip_x = False # Face Right
    if any(k in pressed_keys for k in [pygame.K_a, pygame.K_LEFT]):
        vx -= 150
        sprite.flip_x = True  # Face Left

    if any(k in pressed_keys for k in [pygame.K_w, pygame.K_UP]):
        vy -= 150
        sprite.flip_y = False  # Flip upside down (swimming up)
    if any(k in pressed_keys for k in [pygame.K_s, pygame.K_DOWN]):
        vy += 150
        sprite.flip_y = True # Normal orientation (swimming down)

    sprite.vx, sprite.vy = vx, vy

    if vx != 0 or vy != 0:
        sprite.play("Swim2" if abs(vy) > abs(vx) else "Swim")
    else:
        sprite.play("Idle")
        sprite.flip_y = False # Reset flip when idle
        sprite.vy = 20        # Gravity drift

    player.update(dt)

def draw(screen):
    """Draw Grant's visuals to the screen."""
    player.draw(screen)