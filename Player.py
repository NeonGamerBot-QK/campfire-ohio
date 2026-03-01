from WaterBoss import WaterBoss
import pygame
from ProjectileManager import *

class Player:
    def __init__(self, animated_sprite, game):
        self.sprite = animated_sprite
        self.attacking = False
        self.attack_timer = 0
        self.attack_damage = 10
        self.attack_cooldown = 0.5
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.xp_to_next_level = 10
        self.game = game
        self.facing_dir = pygame.math.Vector2(1, 0)
        self.projectile_manager = ProjectileManager("./assets/seapickle.png")

    def update(self):
        self.attack_timer += self.game.dt
        curr_sprite = self.sprite.sprites()[0]

        vx, vy = 0, 0
        if any(k in self.game.pressed_keys for k in [pygame.K_d, pygame.K_RIGHT]):
            vx += 100
        if any(k in self.game.pressed_keys for k in [pygame.K_a, pygame.K_LEFT]):
            vx -= 100
        if any(k in self.game.pressed_keys for k in [pygame.K_w, pygame.K_UP]):
            vy -= 100
        if any(k in self.game.pressed_keys for k in [pygame.K_s, pygame.K_DOWN]):
            vy += 100

        curr_sprite.vx = vx
        curr_sprite.vy = vy

        if vx != 0 or vy != 0:
            self.facing_dir = pygame.math.Vector2(vx, vy).normalize()

        if vx > 0:
            curr_sprite.flip_x = False
        elif vx < 0:
            curr_sprite.flip_x = True

        if vx != 0 or vy != 0:
            curr_sprite.play("Swim2" if abs(vy) > abs(vx) else "Swim")
        else:
            curr_sprite.play("Idle")

        if pygame.K_SPACE in self.game.pressed_keys:
            self.attack(curr_sprite)

        if self.attacking and curr_sprite.frame_index >= len(curr_sprite.animations["Attack"]) - 1:
            self.attacking = False

        # Check if any NPC projectile hit this player
        self.check_hits_from_npcs()

        self.sprite.update(self.game.dt)
        self.projectile_manager.update(self.game.dt)

    def check_hits_from_npcs(self):
        """Player checks itself for collisions with NPC projectiles."""
        if not self.sprite.sprites():
            return
        curr_sprite = self.sprite.sprites()[0]
        for npc in self.game.npcs:
            hits = pygame.sprite.spritecollide(curr_sprite, npc.projectile_manager.projectiles, True)
            if hits:
                self.taking_damage(npc.attack_damage)

    def taking_damage(self, amount=10):
        self.game.healthbar.hp = max(0, self.game.healthbar.hp - amount)

    def attack(self, curr_sprite):
        if self.attack_timer >= self.attack_cooldown:
            self.attacking = True
            self.attack_timer = 0
            curr_sprite.play("Attack", loop=False)
            self.projectile_manager.shoot(
                curr_sprite.rect.centerx,
                curr_sprite.rect.centery,
                self.facing_dir.x,
                self.facing_dir.y
            )

    def gain_xp(self, amount):
        """Add XP and level up when threshold is reached."""
        levels_gained = 0
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level = 10 * self.level
            levels_gained += 1
        self.attack_damage += 2 * levels_gained  # Increase attack damage by 2 per level
        self.game.healthbar.max_hp = max(self.game.healthbar.max_hp, self.game.healthbar.hp + 10 * levels_gained)  # Increase max HP by 20 per level
        self.game.healthbar.hp += 10 * levels_gained  # Increase max HP by 5 per level

        if self.level >= 3 and not self.game.water_boss:
            self.game.water_boss = WaterBoss(pygame.sprite.Group(), "./assets/Water assets/6", x=200, y=200, scale=4.0)
        return levels_gained

    def draw(self, screen):
        self.sprite.draw(screen)
        self.projectile_manager.draw(screen)