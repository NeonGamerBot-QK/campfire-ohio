import pygame

class SimpleMenu:
    def __init__(self, screen, on_play):
        self.screen = screen
        self.on_play = on_play
        self.enabled = True
        self.font = pygame.font.SysFont(None, 60)

    def is_enabled(self):
        return self.enabled

    def disable(self):
        self.enabled = False

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.on_play()

    def draw(self):
        self.screen.fill((0, 0, 0))
        title = self.font.render("Pickl Power", True, (255, 255, 255))
        start = self.font.render("Press SPACE to Play", True, (255, 255, 255))

        self.screen.blit(title, (150, 200))
        self.screen.blit(start, (200, 300))