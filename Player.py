import pygame
from ProjectileManager import *

class Player:
    def __init__(self, animated_sprite):
        self.sprite = animated_sprite
        self.attacking = False
        self.attack_timer = 0
        self.attack_damage = 10
        self.attack_cooldown = 0.5  
        self.xp = 0
        self.level = 1
        self.xp_to_next_level = 10
        # Store the direction the player is facing (Default to Right)
        self.facing_dir = pygame.math.Vector2(1, 0) 
        self.projectile_manager = ProjectileManager("./assets/seapickle.png")

    def update(self, dt, pressed_keys):
        self.attack_timer += dt
        curr_sprite = self.sprite.sprites()[0]

        vx, vy = 0, 0
        if any(k in pressed_keys for k in [pygame.K_d, pygame.K_RIGHT]):
            vx += 100
        if any(k in pressed_keys for k in [pygame.K_a, pygame.K_LEFT]):
            vx -= 100
        if any(k in pressed_keys for k in [pygame.K_w, pygame.K_UP]):
            vy -= 100
        if any(k in pressed_keys for k in [pygame.K_s, pygame.K_DOWN]):
            vy += 100

        curr_sprite.vx = vx
        curr_sprite.vy = vy

        # Update facing direction if moving
        if vx != 0 or vy != 0:
            self.facing_dir = pygame.math.Vector2(vx, vy).normalize()

        # Handle Sprite Flipping and Animations
        if vx > 0:
            curr_sprite.flip_x = False  
        elif vx < 0:
            curr_sprite.flip_x = True   

        if vx != 0 or vy != 0:
            # Use Swim2 for vertical-heavy movement, Swim for horizontal
            curr_sprite.play("Swim2" if abs(vy) > abs(vx) else "Swim")
        else:
            curr_sprite.play("Idle")
            
        # Attack input
        if pygame.K_SPACE in pressed_keys:
            self.attack(curr_sprite)

        # End attack when animation is done
        if self.attacking and curr_sprite.frame_index >= len(curr_sprite.animations["Attack"]) - 1:
            self.attacking = False

        self.sprite.update(dt)
        self.projectile_manager.update(dt)
    
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_to_next_level:
            self.level += 1
            self.xp -= self.xp_to_next_level
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)  # Increase XP needed for next level

    def attack(self, curr_sprite):
        if self.attack_timer >= self.attack_cooldown:
            self.attacking = True
            self.attack_timer = 0
            curr_sprite.play("Attack", loop=False)
            
            # PASS THE FACING DIRECTION TO THE MANAGER
            self.projectile_manager.shoot(
                curr_sprite.rect.centerx, 
                curr_sprite.rect.centery, 
                self.facing_dir.x, 
                self.facing_dir.y
            )
    def gain_xp(self, amount):
        """
        Add XP and level up when threshold is reached (10 * level to level up).

        Returns:
            Number of levels gained.
        """
        levels_gained = 0
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level = 10 * self.level
            levels_gained += 1
        return levels_gained

    def draw(self, screen):
        self.sprite.draw(screen)
        self.projectile_manager.draw(screen)