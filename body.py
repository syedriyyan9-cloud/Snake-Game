import pygame

from pygame.sprite import Sprite

class Body(Sprite):
    """A class to add body to snake"""

    def __init__(self, game):
        """Initialize variables"""
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.player = game.player
        self.image = pygame.image.load('image/body.png')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x = self.player.rect.x - 100
        self.align_body()

    def align_body(self):
        """aligns snake body behind its head"""
        self.x = self.player.rect.x - 100
        self.y = self.player.rect.y
        self.rect.x = self.x
        self.rect.y = self.y