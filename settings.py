class Settings:
    "存储游戏中所有设置的类"
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        self.ship_speed = 1
        self.ship_limit=3

        self.fleet_direction=1 #1表示向右，-1表示向左


        #bullet property

        self.bullet_speed= 1.0
        self.bullet_width=3
        self.bullet_heigh=50
        self.bullet_color=(60,60,60)

        self.bullets_allowed = 311111111

        # Alien settings
        self.alien_speed =1
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
       # print("self.alien_points", self.alien_points)

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 5
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        #print('self.ship_speed',self.ship_speed)
        self.alien_points=int(self.alien_points * self.score_scale)
        #print(' self.alien_points', self.alien_points * self.score_scale)
