# Grant's code goes here
import os
from AnimatedSprite import AnimatedSprite
import pygame
import sys
import random

game = None

def setup(game_obj):
    """Initialize Grant's module with the game object."""
    global game
    game = game_obj
    game.player = pygame.sprite.Group()

    initiate_sprite("./Sprites/Character Animations/", game.player)

    
def initiate_sprite(path, sprite_group):
    FRAME_WIDTH = 48
    FRAME_HEIGHT = 48

    animation_frames = {}

    for file_name in os.listdir(path):
        image = pygame.image.load(os.path.join(path, file_name)).convert_alpha()

        N_FRAMES = image.get_width() // FRAME_WIDTH

        animation_name = file_name.replace(".png", "")
        frames = []

        for i in range(N_FRAMES):
            frame = image.subsurface((i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT))
            frames.append(frame)
        animation_frames[animation_name] = frames
    
    sprite_group.add(AnimatedSprite(0, 0, animation_frames, default_animation="Idle", animation_speed=7))

def handle_event(event):
    global game
    if event.type == pygame.KEYDOWN:
        game.pressed_keys.add(event.key)
    elif event.type == pygame.KEYUP:
        game.pressed_keys.discard(event.key)

def update(dt):
    global game
    if not game.player.sprites(): return
    
    sprite = game.player.sprites()[0]
    vx, vy = 0, 0
    
    if any(k in game.pressed_keys for k in [pygame.K_d, pygame.K_RIGHT]):
        vx += 150
        sprite.flip_x = False # Face Right
    if any(k in game.pressed_keys for k in [pygame.K_a, pygame.K_LEFT]):
        vx -= 150
        sprite.flip_x = True  # Face Left

    if any(k in game.pressed_keys for k in [pygame.K_w, pygame.K_UP]):
        vy -= 150
        sprite.flip_y = False  # Flip upside down (swimming up)
    if any(k in game.pressed_keys for k in [pygame.K_s, pygame.K_DOWN]):
        vy += 150
        sprite.flip_y = True # Normal orientation (swimming down)

    sprite.vx, sprite.vy = vx, vy

    if vx != 0 or vy != 0:
        sprite.play("Swim2" if abs(vy) > abs(vx) else "Swim")
    else:
        sprite.play("Idle")
        sprite.flip_y = False # Reset flip when idle
        sprite.vy = 20        # Gravity drift

    game.player.update(dt)

def draw(screen):
    """Draw Grant's visuals to the screen."""
    game.player.draw(screen)