import pygame
import Projectile

class Player:
    def __init__(self, animated_sprite):
        self.sprite = animated_sprite
        self.attacking = False
        self.attack_timer = 0
        self.attack_damage = 10
        self.attack_cooldown = 0.5  # seconds
        self.xp = 0
        self.level = 1
        self.xp_to_next_level = 100
        self.projectile_img = pygame.image.load("./assets/seapickle.png").convert_alpha()  # Placeholder for projectile image
        self.projectiles = pygame.sprite.Group()  # Group to hold projectiles

    def update(self, dt, pressed_keys):
        self.attack_timer += dt
        curr_sprite = self.sprite.sprites()[0]  # Assuming single sprite for now

        if pygame.K_SPACE in pressed_keys:
            self.attack()
        
        if self.attacking:
            # Check if animation is finished
            if curr_sprite.frame_index >= len(curr_sprite.animations["Attack"]) - 1:
                self.attacking = False

        vx, vy = 0, 0
        
        if any(k in pressed_keys for k in [pygame.K_d, pygame.K_RIGHT]):
            vx += 100
            curr_sprite.flip_x = False # Face Right
        if any(k in pressed_keys for k in [pygame.K_a, pygame.K_LEFT]):
            vx -= 100
            curr_sprite.flip_x = True  # Face Left

        if any(k in pressed_keys for k in [pygame.K_w, pygame.K_UP]):
            vy -= 100
            curr_sprite.flip_y = False  # Flip upside down (swimming up)
        if any(k in pressed_keys for k in [pygame.K_s, pygame.K_DOWN]):
            vy += 100
            curr_sprite.flip_y = True # Normal orientation (swimming down)

        curr_sprite.vx = vx
        curr_sprite.vy = vy

        if vx != 0 or vy != 0:
            curr_sprite.play("Swim2" if abs(vy) > abs(vx) else "Swim")
        else:
            curr_sprite.play("Idle")
            curr_sprite.flip_y = False # Reset flip when idle
            curr_sprite.vy = 20        # Gravity drift

        self.sprite.update(dt)
        self.projectiles.update(dt)

    def attack(self):
    # Check ONLY the cooldown timer for the ability to fire
        if self.attack_timer >= self.attack_cooldown:
            self.attacking = True
            self.attack_timer = 0  # Reset timer to 0 

            # Create the projectile
            curr_sprite = self.sprite.sprites()[0]
            direction = -200 if curr_sprite.flip_x else 200
            
            self.projectiles.add(Projectile.Projectile(
                x=curr_sprite.rect.centerx,
                y=curr_sprite.rect.centery,
                vx=direction,
                vy=0,
                image=self.projectile_img,
                owner=self
            ))
            
            # Trigger the animation
            curr_sprite.play("Attack", loop=False)
    
    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)  # Increase XP needed for next level

    def draw(self, screen):
        self.sprite.draw(screen)