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

        # Combat attributes
        self.attacking = False
        self.attack_timer = 0
        self.attack_damage = 10
        self.attack_cooldown = 0.5
        self.attack_every = 2.0
        self.alive = True

        # Patrol attributes
        self.patrol_speed = patrol_speed
        self.direction = 1  # 1 = right, -1 = left
        self.patrol_min_x = x - 100
        self.patrol_max_x = x + 100

    def update(self, dt):
        """Update NPC patrol movement and attack timer."""
        if not self.alive:
            return

        # Patrol back and forth
        self.sprite.vx = self.patrol_speed * self.direction
        self.sprite.flip_x = self.direction < 0

        # Reverse direction at patrol bounds
        if self.sprite.rect.x <= self.patrol_min_x:
            self.direction = 1
        elif self.sprite.rect.x >= self.patrol_max_x:
            self.direction = -1

        # Attack timer
        self.attack_timer += dt
        if self.attack_timer >= self.attack_every and not self.attacking:
            self.attacking = True
            self.attack_timer = 0
            self.sprite.play("Attack")

        # Return to Walk after attack cooldown
        if self.attacking:
            self.attack_timer += dt
            if self.attack_timer >= self.attack_cooldown:
                self.attacking = False
                self.attack_timer = 0

        # Play Walk animation when not attacking
        if not self.attacking:
            self.sprite.play("Walk")

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
