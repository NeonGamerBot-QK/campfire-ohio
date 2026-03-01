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
    game.player = Player.Player(pygame.sprite.Group(), game)  # Pass the game instance to the player
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
    
    player.sprite.add(AnimatedSprite(400, 250, animation_frames, default_animation="Idle", animation_speed=7))

def handle_event(event):
    global game
    if event.type == pygame.KEYDOWN:
        game.pressed_keys.add(event.key)
    elif event.type == pygame.KEYUP:
        game.pressed_keys.discard(event.key)

def update(dt):
    global game
    if game.game_over:
        game.water_boss = None
        game.player = Player.Player(pygame.sprite.Group(), game)
        initiate_sprite("./Sprites/Character Animations/", game.player)
        return
    if game.water_boss:
        game.water_boss.update(dt, player=game.player, healthbar=game.healthbar)
        if game.water_boss.removable:
            game.player.gain_xp(50)
            game.water_boss = None
    game.player.update()

def draw(screen):
    """Draw Grant's visuals to the screen."""
    if game.game_over:
        return
    
    game.water_boss.draw(screen) if game.water_boss else None
    game.player.draw(screen)