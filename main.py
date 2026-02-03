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
        self.clock = pygame.time.Clock()
        self.move_delay = 50   # milliseconds
        self.last_move_time = pygame.time.get_ticks()


    def check_events(self):
        """Check for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_down_event(event)
            # self._check_up_event(event)

    def _check_down_event(self, event):
        """check for key presses"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.move_up = True
                self.player.move_down = False
                self.player.move_left = False
                self.player.move_right = False
            elif event.key == pygame.K_s:
                self.player.move_down = True
                self.player.move_up = False
                # self.player.move_down = False
                self.player.move_left = False
                self.player.move_right = False
            elif event.key == pygame.K_a:
                self.player.move_left = True
                self.player.move_up = False
                self.player.move_down = False
                # self.player.move_left = False
                self.player.move_right = False
            elif event.key == pygame.K_d:
                self.player.move_right = True
                self.player.move_up = False
                self.player.move_down = False
                self.player.move_left = False
                # self.player.move_right = False
            elif event.key == pygame.K_q:
                sys.exit()

    # def _check_up_event(self, event):
    #     """check for key releases"""
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_w:
    #             self.player.move_up = False
    #         if event.key == pygame.K_s:
    #             self.player.move_down = False
    #         if event.key == pygame.K_a:
    #             self.player.move_left = False
    #         if event.key == pygame.K_d:
    #             self.player.move_right = False

    def detect_collision(self):
        """Detect colision"""
        if(collision := pygame.sprite.collide_rect(self.apple,self.player)):
            self.apple.random_position()
            self.add_body()

    def add_body(self):
        """Add player body"""
        body = Body(self)
        self.player_body.add(body)

    def move_body(self):
        """Move player body"""
        head = self.player.rect.copy()
        for sprite in self.player_body.sprites():
            tail =  head
            head = sprite.rect.copy()
            # self.change_body_direction(sprite, tail)
            sprite.rect = tail

    def update_screen(self):
        """updates the screen"""
        self.screen.fill(self.setting.COLOR_WHITE)
        self.player.built()
        self.player_body.draw(self.screen)
        self.apple.draw()
        pygame.display.flip()

    def run_game(self):
        """Keep the game window open"""
        while True:
            self.clock.tick(60)
            current_time = pygame.time.get_ticks()
            if current_time - self.last_move_time >= self.move_delay:
                self.last_move_time = current_time
                self.check_events()
                self.detect_collision()
                self.player.change_position()
                self.move_body()
            self.update_screen()
            
if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()