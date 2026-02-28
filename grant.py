# Grant's code goes here
import os
from AnimatedSprite import AnimatedSprite
import pygame
import Player
import sys
import random

game = None

def setup(game_obj):
    """Initialize Grant's module with the game object."""
    global game
    game = game_obj
    game.player = Player.Player(pygame.sprite.Group())
    initiate_sprite("./Sprites/Character Animations/", game.player)

    
def initiate_sprite(path, player):
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
    
    player.animated_sprite.add(AnimatedSprite(0, 0, animation_frames, default_animation="Idle", animation_speed=7))

def handle_event(event):
    global game
    if event.type == pygame.KEYDOWN:
        game.pressed_keys.add(event.key)
    elif event.type == pygame.KEYUP:
        game.pressed_keys.discard(event.key)

def update(dt):
    global game

    game.player.update(game.dt, game.pressed_keys)

def draw(screen):
    """Draw Grant's visuals to the screen."""
    game.player.draw(screen)