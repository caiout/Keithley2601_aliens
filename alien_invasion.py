import pygame
import sys  #玩家退出时，使用sys中的工具来推出游戏
from settings import *
from ship import *
from bullet import *
from alien import *
from time import *
from game_stats import *
from  button import *
from scoreboad import*

class AlienInvasion:

    def __init__(self):
        pygame.init() #方法__init__中，调用pygame.init()来初始化背景设置
        self.settings=Settings()

        '''
        self.screen=pygame.display.set_mode((0,0) , pygame.FULLSCREEN)   #全屏下运行游戏
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heigh = self.screen.get_rect().height
        '''

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # 1：使用pygame.display.set_mode（）创建一个显示窗口，实参(1200,800)是一个元组
        # 2：赋给self.screende的对象是一个surface，Pygame中，surface是屏幕的一部分，用于显示游戏元素
        # 3：游戏中的所有元素都是一个surface，包括飞船等
        # 4：display.set_mode（）返回的surface代表整个游戏窗口，激活游戏动画循环后，每经过一次循环都将重绘这个surface
        # 将用户输入触发的所有变化都重绘出来
        pygame.display.set_caption("Alien Invasion")


        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()    #创建一个编组，管理有效的子弹
        self.aliens = pygame.sprite.Group()
        self.alien=Alien(self)
        self.stats=GameStats(self)

        self.creat_fleet()
        self.bg_color =(self.settings.bg_color)  #RGB 设置背景颜色
        self.sb = Scoreboard(self)
        self.play_button=Button(self,"play")

    def run_game(self):
        i=1
        #整个游戏由方法 run_game(）控制，包含一个不断运行的while循环
        # 包含一个事件循环以及管理屏幕更新
        while True:
           self._check_events()
           if self.stats.game_active:
               self.ship.update()
               self.bullets.update()
               self._update_aliens()
           self.check_bullet_alien()
           for bullet in self.bullets:
                   #对越过屏幕边界的bullet删除
              if bullet.rect.y<0:
                 self.bullets.remove(bullet)

               #print(len(self.bullets))
               #print(self.ship.rect.x)


           self._update_screen()

    def check_bullet_alien(self):
        colisioms = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        # 将；两个编组进行比较，即第一个和第二个参数
        # True即删除该编组中的元素，False则为保留
        if colisioms:
            for aliens in colisioms.values():

                self.stats.score += ((self.settings.alien_points) * len(aliens))

            self.sb.perp_score()
            self.sb.check_high_score()

        if not self.aliens:  #判断编组是否为空
            self.bullets.empty()  #清空该编组
            self.creat_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.perp_level()


    def _check_events(self):
         for event in pygame.event.get():
                # 1：为了访问pygame检测到的事件，使用函数pygame.event.get()
                # 2：其中包含了在上一次调用后发生的所有事件，可在下面编写相应的循环来相应相关的事件
                # 3：所有的键盘和鼠标都将导致这个for循环运行

             if event.type ==pygame.QUIT:
                 # 若用户点击关闭窗口按钮，将检测到pygame.QUIT进而调用sys.exit()来退出游戏
                sys.exit()
             elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
             elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
             elif event.type== pygame.MOUSEBUTTONDOWN:
                 mous_pos=pygame.mouse.get_pos()          #返回鼠标点击的xy坐标
                 self._check_play_button(mous_pos)

    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
           self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
           self.ship.move_left = True
        elif event.key == pygame.K_q:  #按q退出
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _check_play_button(self,mous_pos):
        button_clicked = self.play_button.rect.collidepoint(mous_pos)
        if button_clicked and not self.stats.game_active:
           self.settings.initialize_dynamic_settings()
           self.stats.reset_stats()
           if self.play_button.rect.collidepoint(mous_pos):  #检查鼠标是否落于开始框内
              pygame.mouse.set_visible(False)  #开启游戏后关闭鼠标光标

              self.stats.game_active=True
              self.sb.perp_score()

              self.aliens.empty()
              self.bullets.empty()

              self.creat_fleet()
              self.ship.center_ship()

    def fire_bullet(self):
        newbullet=Bullet(self)
        if len(self.bullets) < self.settings.bullets_allowed:
           self.bullets.add(newbullet)

    def creat_fleet(self):
        alien=Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

#检查一行可以放多少个alien
        available_space_for_right_leaf=self.settings.screen_width-2*alien_width
        available_numbers=available_space_for_right_leaf//(2*alien_width)-5
        #print('available_numbers is',available_numbers)
# 检查一列可以放多少个alien
        available_space_for_y=self.settings.screen_height-2*alien_height-self.ship.rect.width
        available_numbers_y=available_space_for_y // (2 * alien_height)
       # print(  'aavailable_numbers_y is',available_numbers_y)

        for alien_number in range(available_numbers):
            for alien_number_y in range(available_numbers_y):
                self.creat_alien(alien_number,alien_number_y)

    def creat_alien(self,aliennumber_x,aliennumber_y):
        alien = Alien(self)

        alien.x= alien.rect.width+ 2*alien.rect.width * aliennumber_x
        alien.rect.x = alien.x

        alien.rect.y= alien.rect.height+ 2*alien.rect.height * aliennumber_y


        self.aliens.add(alien)


    def _update_screen(self):

         self.screen.fill(self.bg_color)#调用方法fill（），用这种颜色填充背景屏幕，fill（）用于处理surface
         self.ship.blitme()

         for bullet in self.bullets.sprites():
             bullet.drawbullet()
         self.aliens.draw(self.screen)

         if not self.stats.game_active:
             self.play_button.draw_button()
             #print('self.stats.game_active')
         self.sb.show_score()



         pygame.display.flip()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
         # 命令Pygame让最近绘制的屏幕可见，在这里每次执行while时都绘制一个空屏幕，并擦去旧屏幕，是的只可见新屏幕
        if  pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("ship hit")
            self.ship_hit()
        self.check_aliens_bottom()


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break
                #print('settings.fleet_direction',self.settings.fleet_direction)
       # print('_check_fleet_edges')

    def _change_fleet_direction(self):
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

        #print("self.settings.fleet_direction  is", self.settings.fleet_direction )

    def ship_hit(self):
        self.stats.ships_left -= 1
        if self.stats.ships_left >= 0:

           self.bullets.empty()
           self.aliens.empty()
           self.creat_fleet()
           self.ship.center_ship()
           sleep(2)
           self.sb.perp_ship()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def check_aliens_bottom(self):
        screen_rect=self.screen.get_rect()
        for alien in self.aliens:
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

if __name__ == "__main__":
    #判断是否为主程序
    ai = AlienInvasion()  #创建一个实例，并下下面调用ai.run_game()
    ai.run_game()

