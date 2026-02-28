# Grant's code goes here
import os
from AnimatedSprite import AnimatedSprite
import pygame
import sys
import random

_screen = None
player = pygame.sprite.Group()


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
    
    player.add(AnimatedSprite(0, 0, animation_frames, default_animation="Idle"))




def handle_event(event):
    """Handle pygame events for Grant's module."""
    pass


def update(dt):
    """Update Grant's game logic each frame."""
    player.update(dt)


def draw(screen):
    """Draw Grant's visuals to the screen."""
    screen.fill((255, 0, 255))  # Neon pink background
    player.draw(screen)