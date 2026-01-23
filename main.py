import pygame

import sys

class SnakeGame:
    """A class to represent Snake Game"""

    def __init__(self):
        """Initialize attributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))

    def check_events(self):
        """Check for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        """Keep the game window open"""
        while True:
            self.check_events()
            pygame.display.flip()

if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()