import pygame
import neon
import mathew
import grant

class Game:
    def __init__(self):
        self.screen = None
        self.clock = None
        self.running = True
        self.player = None  # Placeholder for player sprite or group
        self.space_boss = None  # Placeholder for space boss sprite or group
        self.water_boss = None  # Placeholder for enemies group
        self.platforms = None  # Placeholder for platforms group

        self.modules = [neon, mathew, grant]

    def setup(self, screen, clock):
        self.screen = screen
        self.clock = clock

        for mod in self.modules:
            if hasattr(mod, "setup"):
                mod.setup(self)


    def handle_event(self, event):
        for mod in self.modules:
            if hasattr(mod, "handle_event"):
                mod.handle_event(event)

    def update(self, dt):
        for mod in self.modules:
            if hasattr(mod, "update"):
                mod.update(dt)

    def draw(self):
        for mod in self.modules:
            if hasattr(mod, "draw"):
                mod.draw(self.screen)