import pygame
from projectile import Projectile

class ProjectileManager:
    def __init__(self, projectile_image_path, speed=400): # Increased speed for feel
        self.projectile_img = pygame.image.load(projectile_image_path).convert_alpha()
        self.projectiles = pygame.sprite.Group()
        self.last_facing = pygame.math.Vector2(1, 0)
        self.speed = speed

    def shoot(self, x, y, vx=0, vy=0):
        # Update internal facing memory if we have movement
        if vx != 0 or vy != 0:
            self.last_facing = pygame.math.Vector2(vx, vy).normalize()

        # Create projectile with the normalized direction
        projectile = Projectile(x, y, self.last_facing, self.speed, self.projectile_img)
        self.projectiles.add(projectile)

    def update(self, dt):
        self.projectiles.update(dt)
        for projectile in self.projectiles:
            if not pygame.display.get_surface().get_rect().colliderect(projectile.rect):
                projectile.kill()

    def draw(self, screen):
        self.projectiles.draw(screen)