import math
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, image):
        super().__init__()
        # Scale and Rotate
        base_image = pygame.transform.scale(image, (40, 40))
        angle = math.degrees(math.atan2(-direction.y, direction.x))
        self.image = pygame.transform.rotate(base_image, angle)
        
        self.rect = self.image.get_rect(center=(x, y))
        
        self.pos = pygame.math.Vector2(x, y)
        self.vel = direction * speed

    def update(self, dt):
        # Update position vector first
        self.pos += self.vel * dt
        # Update rect to match position
        self.rect.center = self.pos

        # Optional: Kill if off-screen
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()