import pygame
from pygame.sprite import *
class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()

        self.settings = ai_game.settings

        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect() #get_rect()访问屏幕的属性rect

        self.image=pygame.image.load('C:/Users/12/PycharmProjects/Keithley 2601/ship.bmp')
        self.rect=self.image.get_rect()

        ship_width=self.rect.width
        ship_width = self.rect.height
        #加载飞船图像并获取其外接矩形

        self.rect.midbottom=self.screen_rect.midbottom
        #对于加载的每艘飞船，都将其放在屏幕底部中央

        self.move_right = False
        self.move_left = False


        self.x=float(self.rect.x)  #用float函数将self.rect.x转化为小数

    def update(self):

        if self.move_right:
            if self.move_right and self.rect.right < self.screen_rect.right:  #对飞船的移动范围进行限制，self.move_right这里重复表达，注意上一个if
               self.x += self.settings.ship_speed
        elif self.move_left:
            if self.move_left and self.rect.left>0:
               self.x += -self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):
         # 在指定的位置绘制飞船
        self.screen.blit(self.image,self.rect)  #surface.blit方法将一个图像(Surface实例)绘制到另一个图像(Surface实例)上

    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x = float(self.rect.x)