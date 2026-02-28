import pygame
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, image, owner=None):
        super().__init__()
        base_image = pygame.transform.scale(image, (40, 40))
        angle = math.degrees(math.atan2(-direction.y, direction.x))
        self.image = pygame.transform.rotate(base_image, angle)
        self.rect = self.image.get_rect(center=(x, y))

        self.vx = direction.x * speed
        self.vy = direction.y * speed
        self.owner = owner

    def update(self, dt):
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt