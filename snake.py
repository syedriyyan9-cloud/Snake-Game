import pygame

class Snake:
    """represents snake"""

    def __init__(self, game):
        """Initialize attributes"""
        self.screen = game.screen
        self.setting = game.setting
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('image/snake_right.png')
        self.rect = self.image.get_rect()
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def change_position(self):
        """Change player's position"""
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.y -= self.setting.player_speed
            self.rotate_image('up')
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.player_speed
            self.rotate_image('down')
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.x -= self.setting.player_speed
            self.rotate_image('left')
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.player_speed
            self.rotate_image('right')
        self.rect.x, self.rect.y = self.x, self.y

    def rotate_image(self,direction):
        """Rotate image by given degrees"""
        if direction == 'up':
            self.image = pygame.image.load('image/snake_up.png')
        if direction == 'down':
            self.image = pygame.image.load('image/snake_down.png')
        if direction == 'left':
            self.image = pygame.image.load('image/snake_left.png')
        if direction == 'right':
            self.image = pygame.image.load('image/snake_right.png')

    def built(self):
        """Put image onto screen"""
        self.screen.blit(self.image, self.rect)