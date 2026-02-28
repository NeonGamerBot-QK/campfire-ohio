import pygame
import neon
import mathew
import grant

class Game:
    def __init__(self, clock):
        self.screen = None
        self.clock = clock
        self.running = True
        self.pressed_keys = set()
        self.dt = self.clock.tick(60) / 1000.0

        self.game_over = False
        self.player_object = None
        self.npcs = []  # List of active NPCs

        # Modules for setup, input, update, draw
        self.modules = [neon, mathew, grant]

    def setup(self, screen):
        self.screen = screen
        for mod in self.modules:
            if hasattr(mod, "setup"):
                mod.setup(self)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        for mod in self.modules:
            if hasattr(mod, "handle_event"):
                mod.handle_event(event)

    def update(self):
        self.dt = self.clock.tick(60) / 1000.0

        # Update modules (e.g., player, NPCs)
        for mod in self.modules:
            if hasattr(mod, "update"):
                mod.update(self.dt)

        # Check collisions: NPCs detect player projectiles
        if self.player_object:
            for npc in self.npcs:
                npc.check_projectile_hit(self.player_object.projectile_manager.projectiles)

        # Player detects NPC projectiles
        if self.player_object:
            for npc in self.npcs:
                self.player_object.check_projectile_hit(npc.projectile_manager.projectiles)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for mod in self.modules:
            if hasattr(mod, "draw"):
                mod.draw(self.screen)
        pygame.display.flip()