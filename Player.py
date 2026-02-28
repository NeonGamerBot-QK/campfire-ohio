import pygame

class Player:
    def __init__(self, player_sprite):
        self.animated_sprite = player_sprite
        self.attacking = False
        self.attack_timer = 0
        self.attack_damage = 10
        self.attack_cooldown = 0.5  # seconds
    
    def update(self, dt, pressed_keys):
        curr_sprite = self.animated_sprite.sprites()[0]  # Assuming single sprite for now
        vx, vy = 0, 0
        
        if any(k in pressed_keys for k in [pygame.K_d, pygame.K_RIGHT]):
            vx += 150
            curr_sprite.flip_x = False # Face Right
        if any(k in pressed_keys for k in [pygame.K_a, pygame.K_LEFT]):
            vx -= 150
            curr_sprite.flip_x = True  # Face Left

        if any(k in pressed_keys for k in [pygame.K_w, pygame.K_UP]):
            vy -= 150
            curr_sprite.flip_y = False  # Flip upside down (swimming up)
        if any(k in pressed_keys for k in [pygame.K_s, pygame.K_DOWN]):
            vy += 150
            curr_sprite.flip_y = True # Normal orientation (swimming down)

        curr_sprite.vx = vx
        curr_sprite.vy = vy

        if vx != 0 or vy != 0:
            curr_sprite.play("Swim2" if abs(vy) > abs(vx) else "Swim")
        else:
            curr_sprite.play("Idle")
            curr_sprite.flip_y = False # Reset flip when idle
            curr_sprite.vy = 20        # Gravity drift
        

        self.animated_sprite.update(dt)
    def draw(self, screen):
        self.animated_sprite.draw(screen)