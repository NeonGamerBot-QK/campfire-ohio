import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, image, owner=None):
        super().__init__()
        self.image = pygame.transform.scale(image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = vx
        self.vy = vy
        self.owner = owner

    def update(self, dt):
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt