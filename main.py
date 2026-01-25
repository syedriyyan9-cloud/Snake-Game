import pygame

import sys

from snake import Snake

from setting import Setting

from apple import Apple

from body import Body

class SnakeGame:
    """A class to represent Snake Game"""

    def __init__(self):
        """Initialize attributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting = Setting()
        self.player = Snake(self)
        self.apple = Apple(self)
        self.player_body = pygame.sprite.Group()

    def check_events(self):
        """Check for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_down_event(event)
            self._check_up_event(event)

    def _check_down_event(self, event):
        """check for key presses"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.move_up = True
            if event.key == pygame.K_s:
                self.player.move_down = True
            if event.key == pygame.K_a:
                self.player.move_left = True
            if event.key == pygame.K_d:
                self.player.move_right = True
            if event.key == pygame.K_q:
                sys.exit()

    def _check_up_event(self, event):
        """check for key releases"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.player.move_up = False
            if event.key == pygame.K_s:
                self.player.move_down = False
            if event.key == pygame.K_a:
                self.player.move_left = False
            if event.key == pygame.K_d:
                self.player.move_right = False

    def detect_collision(self):
        """Detect colision"""
        collision = pygame.sprite.collide_rect(self.apple,self.player)
        if collision:
            self.apple.random_position()
            self.add_body()

    def add_body(self):
        """Add player body"""
        body = Body(self)
        self.player_body.add(body)
        print(self.player_body)

    def move_body(self):
        """Move player body"""
        body = self.player.rect.copy()
        for sprite in self.player_body.sprites():
            self.set_body_position(body, sprite)
            # The below line is written by GPT
            body = sprite.rect.copy()

    def set_body_position(self, body, sprite):
        """Change position of body pieces"""
        sprite.rect.x = body.x - 100
        sprite.rect.y = body.y

    def change_body_direction(self):
        """change the direction of body based on user input"""
        pass # to be completed tomorrow

    def update_screen(self):
        """updates the screen"""
        self.screen.fill(self.setting.COLOR_WHITE)
        self.player.built()
        self.player_body.draw(self.screen)
        self.player.change_position()
        self.apple.draw()
        pygame.display.flip()

    def run_game(self):
        """Keep the game window open"""
        while True:
            self.check_events()
            self.detect_collision()
            self.move_body()
            self.update_screen()
            

if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()