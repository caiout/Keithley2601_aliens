import pygame
from pygame.sprite import *
class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings  # 这里只是建立实例，并没有实际引用

        self.image=pygame.image.load( 'C:/Users/12/PycharmProjects/Keithley 2601/alien.bmp' )
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x) #精确控制  X  position

    def update(self):
        self.x +=(self.settings.alien_speed* self.settings.fleet_direction)
        self.rect.x=self.x

    def check_edge(self):
        #检查alien是否碰到了屏幕边缘
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0 :
            return True
            print("hello 1")