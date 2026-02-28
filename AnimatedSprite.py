import pygame

class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, x, y, animations, default_animation="Idle", animation_speed=0.15):
            super().__init__()
            
            self.animations = animations
            self.current_animation = default_animation
            self.animation_speed = animation_speed
            
            self.frame_index = 0
            
            self.image = self.animations[self.current_animation][0]
            self.rect = self.image.get_rect(topleft=(x, y))
            
            self.loop = True
            self.finished = False

        def play(self, animation_name, loop=True):
            if animation_name != self.current_animation:
                self.current_animation = animation_name
                self.frame_index = 0
                self.loop = loop
                self.finished = False

        def update(self, dt):
            self.frame_index += self.animation_speed * dt
            
            if self.frame_index >= len(self.animations[self.current_animation]):
                if self.loop:
                    self.frame_index = 0
                else:
                    self.frame_index = len(self.animations[self.current_animation]) - 1
                    self.finished = True

            self.image = self.animations[self.current_animation][int(self.frame_index)]
