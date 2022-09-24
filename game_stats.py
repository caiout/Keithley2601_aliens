import pygame.mouse


class GameStats():
    def __init__(self,ai_game):

        self.settings=ai_game.settings
        self.reset_stats()
        self.game_active=False
        self.high_score=0


    def reset_stats(self):
        self.ships_left=self.settings.ship_limit
        print(self.ships_left)
        self.score=0
        print(self.score)
        self.level=1