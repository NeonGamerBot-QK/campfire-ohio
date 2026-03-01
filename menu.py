import pygame
import sys
import Game

class SimpleMenu:
    def __init__(self, screen, on_play, Game):
        
        self.game = game
        self.screen = screen
        self.on_play = on_play
        self.enabled = True
        self.font = pygame.font.SysFont(None, 60)
        self.x_start = 100
        self.x_title = 150
        self.x_skip = 200
        self.speed = 5
    
    def is_enabled(self):
        return self.enabled

    def disable(self):
        self.enabled = False

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.on_play()
                if event.key == pygame.K_j:
                    self.Dame.skip_to_boss = True
                    self.on_play()


        self.x_start += self.speed
        self.x_title += self.speed
        self.x_skip += self.speed
        
        if self.x_start > 800:
            self.x_start = -200
        if self.x_title > 800:
            self.x_title = -400
        if self.x_skip > 800:
            self.x_skip = -600
    
    def draw(self):
        self.screen.fill((0, 0, 255))
        
        title = self.font.render("Water Space Platformer", True, (255, 0, 0))
        start = self.font.render("Press SPACE to Play", True, (255, 0, 0))
        skip = self.font.render("press j to skip to boss", True, (255, 0, 0))
        
        self.screen.blit(title, (self.x_title, 200))
        self.screen.blit(start, (self.x_start, 300))
