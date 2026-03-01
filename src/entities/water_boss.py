from src.entities.npc import Npc
from src.components.projectile_manager import ProjectileManager
from src.ui.healthbar import HealthBar

class WaterBoss(Npc):
    def __init__(self, sprite_group, variant_path, x=0, y=0, scale=4.0):
        super().__init__(sprite_group, variant_path, x, y, scale=scale)
        self.healthbar = HealthBar(x, y - 20, 100, 10, max_hp=250)
        self.hp = 250
        self.attack_damage = 18
        self.shock_damage = 5
        self.attack_cooldown = 0.2
        self.attack_every = 1.0
        self.shoot_interval = 0.8
        self.shock_interval = 0.5
        self.projectile_manager = ProjectileManager("./assets/seapickle.png", speed=150)
        self.AGGRO_RANGE = 10000
    
    def update(self, dt, player=None, healthbar=None):
        # Call the base Npc update
        super().update(dt, player, healthbar)

        # Update health bar position above boss
        self.healthbar.x = self.sprite.rect.centerx - self.healthbar.w // 2
        self.healthbar.y = self.sprite.rect.top - 20

        # Sync health bar value
        self.healthbar.hp = max(0, self.hp)

    def draw(self, screen):
        # Draw NPC and projectiles
        super().draw(screen)
        # Draw the health bar
        if self.alive:
            self.healthbar.draw(screen)
