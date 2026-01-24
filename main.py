import pygame

import sys

from snake import Snake

from setting import Setting

class SnakeGame:
    """A class to represent Snake Game"""

    def __init__(self):
        """Initialize attributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting = Setting()
        self.player = Snake(self)

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

    def update_screen(self):
        """updates the screen"""
        self.screen.fill(self.setting.COLOR_WHITE)
        self.player.built()
        self.player.change_position()
        pygame.display.flip()

    def run_game(self):
        """Keep the game window open"""
        while True:
            self.check_events()
            self.update_screen()
            

if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()