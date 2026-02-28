import pygame
from Projectile import Projectile

class ProjectileManager:
    def __init__(self, projectile_image_path, speed=200):
        self.projectile_img = pygame.image.load(projectile_image_path).convert_alpha()
        self.projectiles = pygame.sprite.Group()
        self.last_facing = pygame.math.Vector2(1, 0)  # Default right
        self.speed = speed

    def shoot(self, x, y, vx=0, vy=0):
        # Update facing if velocity is provided
        if vx != 0 or vy != 0:
            self.last_facing = pygame.math.Vector2(vx, vy).normalize()

        # Create projectile
        projectile = Projectile(x, y, self.last_facing, self.speed, self.projectile_img, owner=self)
        self.projectiles.add(projectile)

    def update(self, dt):
        self.projectiles.update(dt)

    def draw(self, screen):
        self.projectiles.draw(screen)