#.....................................................................
#Kohen Johnston
#Simple py game
#2024-05-13
#.....................................................................

import pygame
from qddq import Player

# starts up Pygame
pygame.init()

# makes the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame OOP Example")

# Colors
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)

# FPS 
FPS = 60
clock = pygame.time.Clock()

def main():
    # Create player size and look
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input
        keys = pygame.key.get_pressed()
        player.handle_input(keys)

        # Updates the players position 
        player.update()

        # Draws the map
        screen.fill(WHITE)
        player.draw(screen)
        pygame.display.flip()

        # Caps the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
