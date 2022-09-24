import pygame.font
from pygame.sprite import *
from ship import *
class Scoreboard:

    def __init__(self,ai_game):
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        self.perp_score()
        self.perp_high_score()
        self.perp_level()
        self.perp_ship()

    def perp_score(self):
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def perp_high_score(self):

        high_score=round(self.stats.high_score,-1) #取10位整数，参考round函数
        high_score_str='{:,}'.format(high_score)  #用逗号分隔数字 1000，000，000
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
        self.high_score_rect=self.score_image.get_rect()
        self.high_score_rect.right=self.screen_rect.centerx
        self.score_rect.top=20

    def perp_level(self):

        high_level=self.stats.level #取10位整数，参考round函数
        high_level_str=str(self.stats.level)  #用逗号分隔数字 1000，000，000
        self.level_image=self.font.render( high_level_str,True,self.text_color,self.settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right
        self.score_rect.top=40+self.level_rect.height

    def perp_ship(self):

        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_game)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    def check_high_score(self):
        if self.stats.score >self.stats.high_score:
           self.stats.high_score = self.stats.score
           self.perp_high_score()