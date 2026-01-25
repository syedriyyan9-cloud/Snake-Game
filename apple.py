import pygame

import random

class Apple:
    """Represents an apple"""

    def __init__(self, game):
        """Initialize attributes"""
        self.screen = game.screen
        self.setting = game.setting
        self.screen_rect = game.screen.get_rect()
        self.y_axis = self.screen_rect.height//2
        self.x_axis = self.screen_rect.width//2
        self.rect = pygame.Rect(self.x_axis,self.y_axis,10,10)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def random_position(self):
        """Draws apple at random position on screen"""
        self.x = random.randint(0,self.screen_rect.width)
        self.y = random.randint(0,self.screen_rect.height)
        self.rect.x, self.rect.y = self.x, self.y

    def draw(self):
        """Draw apple on screen"""
        pygame.draw.rect(self.screen, self.setting.COLOR_RED,self.rect)