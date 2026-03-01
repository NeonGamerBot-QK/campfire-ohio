from Npc import Npc
from ProjectileManager import ProjectileManager

class WaterBoss(Npc):
    def __init__(self, sprite_group, variant_path, x=0, y=0, scale=4.0):
        super().__init__(sprite_group, variant_path, x, y, scale)
        self.hp = 300
        self.attack_damage = 25
        self.shock_damage = 5
        self.attack_cooldown = 0.2
        self.attack_every = 1.0
        self.shoot_interval = 0.8
        self.shock_interval = 0.5
        self.projectile_manager = ProjectileManager("./assets/seapickle.png", speed=150)
        self.hp = 300
        self.AGGRO_RANGE = 10000
