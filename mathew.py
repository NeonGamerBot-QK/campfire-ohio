# Mathew's code goes here

pygame.init()
pygame.display.set_caption("Platform Example")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Platform data: (x, y, width, height)
platforms_data = [
    (0, 550, 800, 50), # Ground platform
    (150, 400, 100, 20),
    (400, 300, 150, 20)
]

# List of rect objects
platforms = []
for platform_rect_data in platforms_data:
    platforms.append(pygame.Rect(platform_rect_data))

# Global variables for screen and clock
_screen = None
clock = pygame.time.Clock()

def setup(width, height):
    """Initialize Neon's module with the display surface."""
    global _screen
    _screen = pygame.display.set_mode((width, height))

def handle_event(event):
    """Handle pygame events for Neon's module."""
    # pass
    pass

def update(dt):
    """Update Neon's game logic each frame."""
    # pass
    pass

def draw():
    """Draw Neon's visuals to the screen."""
    global _screen
    if _screen:
        _screen.fill(BLACK) # Clear screen with black each frame
        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(_screen, BLUE, platform)
        
        # Update the display
        pygame.display.flip() # or pygame.display.update()
        clock.tick(60)

# Example main loop structure to run the code
if __name__ == '__main__':
    setup(800, 600) # Set screen dimensions
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_event(event)
        
        # Update game state (delta time handling can be added)
        update(1) 
        
        # Draw everything
        draw()
        
    pygame.quit() # Uninitialize pygame when loop finishes
