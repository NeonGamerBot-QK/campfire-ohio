import pygame
from src.modules import neon
from src.modules import mathew
from src.modules import grant

class Game:
    def __init__(self, clock):
        self.screen = None
        self.clock = clock
        self.running = True
        self.pressed_keys = set()

        self.dt = self.clock.tick(60) / 1000.0

        self.game_over = False
        self.player = None  # Placeholder for player sprite or group
        self.space_boss = None  # Placeholder for space boss sprite or group
        self.water_boss = None  # Placeholder for enemies group
        self.platforms = None  # Placeholder for platforms group
        self.npcs = []  # List of active NPCs
        self.healthbar = None  # Placeholder for healthbar instance
        self.skip_to_boss = False

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

        for mod in self.modules:
            if hasattr(mod, "update"):
                mod.update(self.dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for mod in self.modules:
            if hasattr(mod, "draw"):
                mod.draw(self.screen) 