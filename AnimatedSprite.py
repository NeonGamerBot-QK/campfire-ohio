import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, animations, default_animation="Idle", animation_speed=8):
        super().__init__()
        self.vx = 0
        self.vy = 0
        # Tracking both axes
        self.flip_x = False
        self.flip_y = False 
        
        self.animations = animations
        self.current_animation = default_animation
        self.animation_speed = animation_speed
        
        self.frame_index = 0
        self.image = self.animations[self.current_animation][0]
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.loop = True

    def play(self, animation_name, loop=True):
        if animation_name != self.current_animation:
            self.current_animation = animation_name
            self.frame_index = 0
            self.loop = loop

    def update(self, dt):
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt

        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.animations[self.current_animation]):
            if self.loop:
                self.frame_index = 0
            else:
                self.frame_index = len(self.animations[self.current_animation]) - 1
        
        raw_image = self.animations[self.current_animation][int(self.frame_index)]
        
        # Apply both horizontal and vertical flips
        self.image = pygame.transform.flip(raw_image, self.flip_x, self.flip_y)