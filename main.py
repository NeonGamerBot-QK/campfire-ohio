import pygame
import neon
import mathew
import grant

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Water Space Platformer")
clock = pygame.time.Clock()

# List of all player modules for easy iteration
modules = [neon, mathew, grant]

# Call each module's setup() if it exists
for mod in modules:
    if hasattr(mod, "setup"):
        mod.setup(screen)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pass events to each module
        for mod in modules:
            if hasattr(mod, "handle_event"):
                mod.handle_event(event)

    # Call each module's update()
    for mod in modules:
        if hasattr(mod, "update"):
            mod.update(dt)

    screen.fill((0, 0, 0))

    # Call each module's draw()
    for mod in modules:
        if hasattr(mod, "draw"):
            mod.draw(screen)

    pygame.display.flip()

pygame.quit()
