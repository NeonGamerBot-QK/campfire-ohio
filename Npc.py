import os
import pygame
from AnimatedSprite import AnimatedSprite


def load_water_animations(variant_path):
    """
    Load animation frames from a Water assets variant folder.
    Auto-detects frame dimensions per sprite sheet since they vary
    (e.g., Idle is 100x100, Death is 64x72).

    Args:
        variant_path: Path to a variant folder (e.g., "assets/Water assets/1")

    Returns:
        Dictionary mapping animation names to lists of frame surfaces.
    """
    animation_frames = {}

    for file_name in sorted(os.listdir(variant_path)):
        if not file_name.endswith(".png"):
            continue

        image = pygame.image.load(os.path.join(variant_path, file_name)).convert_alpha()
        animation_name = file_name.replace(".png", "")

        img_width = image.get_width()
        img_height = image.get_height()

        # Try square frames first (frame_width = frame_height)
        frame_width = img_height
        if img_width % frame_width != 0:
            # Find the divisor of img_width closest to img_height
            best_width = img_width
            best_diff = abs(img_width - img_height)
            for num_frames in range(1, 11):
                candidate = img_width // num_frames
                if img_width % num_frames == 0 and abs(candidate - img_height) < best_diff:
                    best_width = candidate
                    best_diff = abs(candidate - img_height)
            frame_width = best_width

        num_frames = img_width // frame_width
        frames = []
        for i in range(num_frames):
            frame = image.subsurface((i * frame_width, 0, frame_width, img_height))
            frames.append(frame)
        animation_frames[animation_name] = frames

    return animation_frames


class Npc:
    # Detection range in pixels for triggering attack
    AGGRO_RANGE = 150
    # Range at which the NPC deals damage to the player
    SHOCK_RANGE = 60

    def __init__(self, sprite_group, variant_path, x=0, y=0, patrol_speed=80):
        """
        Create an NPC using Water assets.

        Args:
            sprite_group: pygame.sprite.Group to add the animated sprite to.
            variant_path: Path to a Water assets variant folder.
            x: Starting x position.
            y: Starting y position.
            patrol_speed: Horizontal movement speed in pixels/sec.
        """
        animation_frames = load_water_animations(variant_path)
        self.animated_sprite = sprite_group
        self.sprite = AnimatedSprite(x, y, animation_frames, default_animation="Idle", animation_speed=7)
        self.animated_sprite.add(self.sprite)
        self.variant_path = variant_path

        # Combat attributes
        self.attacking = False
        self.attack_timer = 0
        self.attack_damage = 10
        self.attack_cooldown = 0.5
        self.attack_every = 2.0
        self.shock_timer = 0
        self.shock_interval = 1.0  # Damage the player every 1 second while in range
        self.alive = True

        # Patrol attributes
        self.patrol_speed = patrol_speed
        self.direction = 1  # 1 = right, -1 = left
        self.patrol_min_x = x - 100
        self.patrol_max_x = x + 100

    def _distance_to_player(self, player_rect):
        """Calculate distance between NPC center and player center."""
        npc_center = pygame.math.Vector2(self.sprite.rect.center)
        player_center = pygame.math.Vector2(player_rect.center)
        return npc_center.distance_to(player_center)

    def update(self, dt, player=None, healthbar=None):
        """
        Update NPC behavior based on proximity to the player.

        Args:
            dt: Delta time in seconds.
            player: The Player object (optional, for aggro/shock behavior).
            healthbar: The HealthBar object (optional, for shocking the player).
        """
        if not self.alive:
            return

        player_nearby = False
        player_in_shock_range = False

        # Check player proximity if player exists
        if player and player.animated_sprite.sprites():
            player_rect = player.animated_sprite.sprites()[0].rect
            distance = self._distance_to_player(player_rect)
            player_nearby = distance <= self.AGGRO_RANGE
            player_in_shock_range = distance <= self.SHOCK_RANGE

        if player_nearby:
            # Chase toward the player instead of patrolling
            player_center_x = player.animated_sprite.sprites()[0].rect.centerx
            if player_center_x > self.sprite.rect.centerx:
                self.direction = 1
            else:
                self.direction = -1

            # Enter attack mode
            if not self.attacking:
                self.attacking = True
                self.sprite.play("Attack")

            # Shock the player on a timer (variant 1 = jellyfish shock)
            if player_in_shock_range and healthbar and "1" in self.variant_path:
                self.shock_timer += dt
                if self.shock_timer >= self.shock_interval:
                    self.shock_timer = 0
                    healthbar.hp = max(0, healthbar.hp - self.attack_damage)
        else:
            # No player nearby — patrol normally
            if self.attacking:
                self.attacking = False
                self.attack_timer = 0
            self.shock_timer = 0

            # Reverse direction at patrol bounds
            if self.sprite.rect.x <= self.patrol_min_x:
                self.direction = 1
            elif self.sprite.rect.x >= self.patrol_max_x:
                self.direction = -1

            if not self.attacking:
                self.sprite.play("Walk")

        # Move in current direction
        self.sprite.vx = self.patrol_speed * self.direction
        self.sprite.flip_x = self.direction < 0

        self.animated_sprite.update(dt)

    def take_damage(self):
        """Play the Hurt animation when the NPC takes damage."""
        if self.alive:
            self.sprite.play("Hurt")

    def die(self):
        """Play the Death animation and mark NPC as dead."""
        if self.alive:
            self.alive = False
            self.sprite.vx = 0
            self.sprite.vy = 0
            self.sprite.play("Death", loop=False)

    def draw(self, screen):
        """Draw the NPC to the screen."""
        self.animated_sprite.draw(screen)
