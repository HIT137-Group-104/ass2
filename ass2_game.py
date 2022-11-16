import pygame as pg
import sys
import random
from pygame.locals import *

pg.init()                                                   #initialising all pygame modules

''' SOUND '''

shoot_sound = pg.mixer.Sound('sound/shoot.wav')
start_sound = pg.mixer.Sound('sound/start.wav')
collision_sound = pg.mixer.Sound('sound/hit.wav')
end_sound = pg.mixer.Sound('sound/died.wav')                #inserting sound effects and background music then store it on its own variables
start_music = pg.mixer.Sound('sound/start.menu.mp3')        #pygame.mixer is a pygame module to load and play sound
end_music = pg.mixer.Sound('sound/gameover.menu.mp3')
bg_music = pg.mixer.music.load('sound/bg.music.mp3')

pg.mixer.init()                                             #initialising the mixer in the game


''' IMAGES '''

player = 'assets/space_ship.png'
small_enemy = 'assets/small_enemy.png'
big_enemy = 'assets/big_enemy.png'                          #inserting different shapes of the game then store it on its own variables
player_bullet = 'assets/player_bullet.png'
small_enemy_bullet = 'assets/small_bullet.png'
big_enemy_bullet = 'assets/big_bullet.png'
player_lives = 'assets/heart.png'


screen = pg.display.set_mode((800, 600))                    #set the screen to be its following resolution then store it to "screen"
s_width, s_height = screen.get_size()                       #creating width and height variable and store the "screen" variable into it
caption = pg.display.set_caption("Group 104")               #changing the title of the tab to be "Group 104"
pygame_icon = pg.image.load(player)                         #store "player" picture into its variable
bg_img = pg.image.load('assets/crash.jpg').convert()
bg_img2 = pg.image.load('assets/background.gif').convert()      #load pictures then store it
bg_img = pg.transform.smoothscale(bg_img, screen.get_size())
bg_img2 = pg.transform.smoothscale(bg_img2, screen.get_size())  #call the variables to be able to load the pictures
pg.display.set_icon(pygame_icon)                            #changing the icon of the game

clock = pg.time.Clock()
FPS = 60                                                    #set the frame rate per second to make the game play normal (not too slow and fast) 

bg_grp = pg.sprite.Group()
player_grp = pg.sprite.Group()
small_enemy_grp = pg.sprite.Group()
big_enemy_grp = pg.sprite.Group()
player_bullet_grp = pg.sprite.Group()                       #create variables for pygame sprite group to hold and manage multiple Sprite objects
small_bullet_grp = pg.sprite.Group()
big_bullet_grp = pg.sprite.Group()
spots_grp = pg.sprite.Group()

sprite_group = pg.sprite.Group()
pg.mouse.set_visible(False)                                 #make the cursor invisible when play the game


class Background(pg.sprite.Sprite):                         #make a background class and hold multiple Sprite objects
    def __init__(self, x, y):                               
        super().__init__()                                  #to return an object to the parent class which is "Background"

        self.image = pg.Surface([x, y])                     #to represent any image
        self.image.fill('white')                            #make the surface colour to be white (this is for spots(stars) elements on the black background)
        self.image.set_colorkey('black')                    #to make the image transparent
        self.rect = self.image.get_rect()                   #a variable to store x and y values

    def update(self):
        self.rect.y += 1
        self.rect.x += 1                                    #to make the spots(stars) moving with a speed of 1
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)          #if the spots(starts) going beyond the height, it will reset to  any y value randomly
            self.rect.x = random.randrange(-400, s_width)   #if the spots(starts) going beyond the height, it will reset to  any x value randomly


class Spots(Background):                                  
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rect.x = random.randrange(0, s_width) #from the random range of x and y axis, the spots will appear randomly, whole width and height of the screen
        self.rect.y = random.randrange(0, s_height) 
        self.image.fill('grey')             #changing the spots(stars) colour to grey
        self.vel = random.randint(3, 8)     #the amount of spaces it will randomly move from top to bottom, i.e the speed of spots going downwards

    def update(self):
        self.rect.y += self.vel     #the spots will keep going downwards
        if self.rect.y > s_height:  #if the spots increase in y axis until it reaches the bottom
            self.rect.x = random.randrange(0, s_width)  #more spots will appear randomly based on this x and y axis random range, from the whole width and height of the screen
            self.rect.y = random.randrange(0, s_height)


class Player(pg.sprite.Sprite):   
    def __init__(self, img):
        super().__init__()
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')    #so the player image does not look like a rectangle
        self.alive = True
        self.count_to_live = 0
        self.activate_bullet = True
        self.alpha_duration = 0

    def update(self):
        if self.alive:
            self.image.set_alpha(80)
            self.alpha_duration += 1
            if self.alpha_duration > 170:
                self.image.set_alpha(255)
        mouse = pg.mouse.get_pos()                  #Player will follow the mouse cursor
        self.rect.x = mouse[0] - 20                 #To center the player bullet
        self.rect.y = mouse[1] + 40
        if self.count_to_live > 100:
            self.alive = True
            self.count_to_live = 0
            self.activate_bullet = True

    def shoot(self):
        bullet = PlayerBullet(player_bullet)
        mouse = pg.mouse.get_pos()
        bullet.rect.x = mouse[0]
        bullet.rect.y = mouse[1]
        player_bullet_grp.add(bullet)
        sprite_group.add(bullet)

    def dead(self):
        pg.mixer.Sound.play(collision_sound)
        self.alive = False
        self.activate_bullet = False


class Small(Player):
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = random.randrange(0, s_width-80)   #to place the small enemies randomly within the screen
        self.rect.y = random.randrange(-500, 0)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += 1
        if self.rect.y > s_height:     #how the small enemies will move in a direction that we want, in this case downwards
            self.rect.x = random.randrange(80, s_width-50)
            self.rect.y = random.randrange(-2000, 0)
        self.shoot()

    def shoot(self):
        if self.rect.y in (0, 30, 70, 300, 700):
            enemybullet = EnemyBullet(small_enemy_bullet)
            enemybullet.rect.x = self.rect.x + 20
            enemybullet.rect.y = self.rect.y + 50
            small_bullet_grp.add(enemybullet)
            sprite_group.add(enemybullet)


class Big(Small):
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = -200  #we want the big enemy to move from the middle left. if it is not killed it will then move back from the middle right.
        self.rect.y = 200   #if it is killed, a new big enemy will spawn from the left again
        self.move = 1

    def update(self):
        self.rect.x += self.move
        if self.rect.x > s_width + 200:
            self.move *= -1
        elif self.rect.x < -200:
            self.move *= -1
        self.shoot()

    def shoot(self):
        if self.rect.x % 50 == 0:
            bigbullet = EnemyBullet(big_enemy_bullet)
            bigbullet.rect.x = self.rect.x + 50 #this is to ensure that the bullets are shot from the middle
            bigbullet.rect.y = self.rect.y + 70
            big_bullet_grp.add(bigbullet)
            sprite_group.add(bigbullet)


class PlayerBullet(pg.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')

    def update(self):
        self.rect.y -= 20       #this code is to adjust the speed of the bullet going upwards from the player ship
        if self.rect.y < 0:     #if it reaches to y axis = 0, it will disappear
            self.kill()


class EnemyBullet(PlayerBullet):
    def __init__(self, img):
        super().__init__(img)
        self.image.set_colorkey('white')    #to remove the background around the enemy bullet image

    def update(self):
        self.rect.y += 3    #the enemy bullet will go downwards in increments of 3 in y axis
        if self.rect.y > s_height:  #it will disappear when it reaches to the bottom of the screen
            self.kill()


class Game:                                 #making a class for game
    def __init__(self):                     #to call an object that is created from a class. 
        self.init_create = True
        self.count_hit = 0
        self.count_hit2 = 0
        self.lives = 3
        self.score = 0
        self.count_enemy = 0
        self.count_ufo = 0
        
        self.start_screen()

    def start_text(self):
        font = pg.font.SysFont('Verandah', 70)
        text = font.render('Space Defender', True, 'aqua')
        text_rect = text.get_rect(center=(s_width/2, s_height/2-200))
        screen.blit(text, text_rect)

        font2 = pg.font.SysFont('Verandah', 40)
        text2 = font2.render('Press Space to Start', True, 'white')
        text2_rect = text2.get_rect(center=(s_width/2, s_height/2))
        screen.blit(text2, text2_rect)
        
        font3 = pg.font.SysFont('Verandah', 30)
        text3 = font3.render('Instructions: Press S key to shoot bullets and use mouse to move', True, 'white')
        text3_rect = text3.get_rect(center=(s_width/2, s_height/2+100))
        screen.blit(text3, text3_rect)
        
        font4 = pg.font.SysFont('Verandah', 30)
        text4 = font4.render('Destroy small spaceship = 1 bullet', True, 'white')
        text4_rect = text4.get_rect(center=(s_width/2, s_height/2+150))
        screen.blit(text4, text4_rect)
        
        font5 = pg.font.SysFont('Verandah', 30)
        text5 = font5.render('Destroy big spaceship = 10 bullets', True, 'white')
        text5_rect = text5.get_rect(center=(s_width/2, s_height/2+180))
        screen.blit(text5, text5_rect)

    def start_screen(self):
        pg.mixer.Sound.stop(end_music)
        pg.mixer.Sound.play(start_music)
        self.lives = 3
        sprite_group.empty()
        
        while True:
            screen.blit(bg_img2, (0,0))
            self.start_text()
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        self.run_game()

            pg.display.update()

    def screen_end_text(self):
        font = pg.font.SysFont('Verandah', 50)
        text = font.render('GAME OVER', True, 'black')
        text_rect = text.get_rect(center=(s_width/2, s_height/2-150))
        screen.blit(text, text_rect)
        
        font1 = pg.font.SysFont('Verandah', 50)
        text1 = font1.render('Press Esc to return to Main Menu', True, 'black')
        text1_rect = text1.get_rect(center=(s_width/2, s_height/2-50))
        screen.blit(text1, text1_rect)
        
        font2 = pg.font.SysFont('Verandah', 50)
        text2 = font2.render('Press R key to restart game', True, 'black')
        text2_rect = text2.get_rect(center=(s_width/2, s_height/2))
        screen.blit(text2, text2_rect)
        
        font3 = pg.font.SysFont('Verandah', 50)
        text3 = font3.render("Points: " + str(round(self.score, 1)), True, 'black')
        text3_rect = text3.get_rect(center=(s_width/2, s_height/2-100))
        screen.blit(text3, text3_rect)

    def screen_end(self):
        pg.mixer.music.stop()
        pg.mixer.Sound.play(end_sound)
        pg.mixer.Sound.play(end_music)
        while True:
            screen.blit(bg_img,(0,0))
            self.screen_end_text()

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.score = 0
                        self.start_screen()

                    if event.key == K_r:
                        self.score = 0
                        self.restart_game()
                        

            pg.display.update()

    def create_bg(self):            #define a function for "create_bg) 
        for i in range(20):         #create the amount of spots in this case 20, going diagonally in the background 
            x = random.randint(1, 6)        #change the size between 1-6px randomly
            bg_img = Background(x, x)
            bg_img.rect.x = random.randrange(0, s_width)
            bg_img.rect.y = random.randrange(0, s_height)
            bg_grp.add(bg_img)
            sprite_group.add(bg_img)

    def create_spots(self):
        for i in range(70): #create the amount of spots going downwards
            x = 1
            y = random.randint(1, 7)
            stars = Spots(x, y)
            spots_grp.add(stars)
            sprite_group.add(stars)

    def create_player(self):
        self.player = Player(player)
        player_grp.add(self.player)
        sprite_group.add(self.player)

    def create_small_enemy(self):
        for i in range(6):      #how many small enemies we want to spawn
            self.enemy = Small(small_enemy) 
            small_enemy_grp.add(self.enemy)
            sprite_group.add(self.enemy)
                
    def create_big_enemy(self):
        for i in range(1):      # 1 big enemy to spawn
            self.ufo = Big(big_enemy)   
            big_enemy_grp.add(self.ufo)
            sprite_group.add(self.ufo)
                

    def playerbullet_shoot_small(self):
        hits = pg.sprite.groupcollide(small_enemy_grp, player_bullet_grp, False, True)
        for i in hits:
            self.count_hit += 1  #everytime a bullet from the player hits the small enemy, the count from self.count_hit will increase by 1
            if self.count_hit == 1: #if the bullet from player hits the small enemy twice,
                self.score += 10    #player will receive 10 points
                i.rect.x = random.randrange(0, s_width) #when the small enemy gets destroyed, it will be spawned again randomly based on these x and y coordinates
                i.rect.y = random.randrange(-3000, -100)
                self.count_hit = 0  #then the small enemies will reset their counts back to 0
                pg.mixer.Sound.play(collision_sound) #sound when the player bullet hits the small enemy

    def playerbullet_shoot_big(self):
        hits = pg.sprite.groupcollide(big_enemy_grp, player_bullet_grp, False, True)
        for i in hits:
            self.count_hit2 += 1 #similar for the small enemy, the count from self.count_hit2 will increase by 1 everytime the big enemy gets hit by the player buller
            if self.count_hit2 == 10: #it will get destroyed when it gets hit by the player bullet 10 times
                self.score += 50 #player will score 50 points when the big enemy gets destroyed
                i.rect.x = -199 #it will then be spawned from the x coordinate since we want it to move horizontally
                self.count_hit2 = 0 #this will return the self.count for the big enemy to 0
                pg.mixer.Sound.play(collision_sound) #sound when the player bullet hits the big enemy

    def smallbullet_shoot_player(self):
        if self.player.image.get_alpha() == 255:
            hits = pg.sprite.spritecollide(self.player, small_bullet_grp, True) #when the following condition which is when the small enemy bullet hits the player is true,
            if hits:                                                            #the if statements will run
                self.lives -= 1               #in this case, everytime the player gets hit by the small enemy bullet, the player life will reduce by 1
                self.player.dead()            #the player will die
                if self.lives < 0:            #if the player lives has less than 0 lives
                    self.screen_end()         #it will go to the end screen which is game over

    def bigbullet_shoot_player(self):
        if self.player.image.get_alpha() == 255:
            hits = pg.sprite.spritecollide(self.player, big_bullet_grp, True) #when the following condition which is when the big enemy bullet hits the player is true,
            if hits:                                                          #the if statements will run
                self.lives -= 1                #similar to smallbullet, everytime the player gets hit by the big enemy bullet, the player life will reduce by 1
                self.player.dead()             #the player will die
                if self.lives < 0:             #if the player lives has less than 0 lives
                    self.screen_end()          #it will go to the end screen which is game over
                    
    def player_small_crash(self):
        if self.player.image.get_alpha() == 255:
            hits = pg.sprite.spritecollide(self.player, small_enemy_grp, False)
            if hits:
                for i in hits:
                    i.rect.x = random.randrange(0, s_width)
                    i.rect.y = random.randrange(-3000, -100)
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        self.screen_end()
 
    def player_big_crash(self):
        if self.player.image.get_alpha() == 255:
            hits = pg.sprite.spritecollide(self.player, big_enemy_grp, False)
            if hits:
                for i in hits:
                    i.rect.x = -199
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        self.screen_end()

    def create_lives(self):             
        self.live_img = pg.image.load(player_lives) #the image of the player lives
        self.live_img = pg.transform.scale(self.live_img, (30, 30)) #this is the size of the player lives image
        n = 0 #count for n
        for i in range(self.lives):
            screen.blit(self.live_img, (0+n, s_height-50)) #this coordinates is where we want the player lives image to be positioned in the run_game
            n += 40 #the gap between the player lives

    def create_score(self):
        score = self.score
        font = pg.font.SysFont('Verandah', 30)  #the font for the score text
        text = font.render("Point: "+str(score), True, 'white') #the score will be a string
        text_rect = text.get_rect(center=(s_width-100, s_height-585)) #these coordinated is to position the text
        screen.blit(text, text_rect) #this is to put the text and text_rect to the screen

    def run_update(self):
        sprite_group.draw(screen)  #draw the screen 
        sprite_group.update() #this will update any changes made

    def run_game(self):                     #define a function for run_game so the game will properly play
        pg.mixer.Sound.stop(start_music)    #stop the music from the start screen
        pg.mixer.Sound.play(start_sound)    #play the start sound
        pg.mixer.music.play(-1)             #play the background music when playing continuously
        if self.init_create:
            self.create_bg()
            self.create_spots()
            self.create_player()
            self.create_small_enemy()
            self.create_big_enemy()
        while True:                         #the game will play when the while loop is true
            screen.fill('black')
            self.playerbullet_shoot_small()
            self.playerbullet_shoot_big()
            self.smallbullet_shoot_player()         #the game will play if all these instance of the classes is running properly
            self.bigbullet_shoot_player()
            self.player_small_crash()
            self.player_big_crash()
            self.run_update()
            pg.draw.rect(screen, 'black', (0, 0, s_width, 30))
            self.create_lives()
            self.create_score()
            

            for event in pg.event.get():
                if event.type == QUIT:       
                    pg.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:       #the game will quit or move to start screen when players press escape
                        pg.quit()
                        sys.exit()

                    if event.key == K_s:                        #the player will shoot if they press "s" key
                        pg.mixer.Sound.play(shoot_sound)        #sound effect when shooting
                        self.player.shoot()

            pg.display.update()
            clock.tick(FPS)

    def restart_game(self):
        pg.mixer.Sound.stop(end_music)
        pg.mixer.music.play(-1)
        self.lives = 3
        sprite_group.empty()
        
        if self.init_create:
            self.create_bg()
            self.create_spots()
            self.create_player()
            self.create_small_enemy()
            self.create_big_enemy()
            
        while True:
            screen.fill('black')
            self.playerbullet_shoot_small()
            self.playerbullet_shoot_big()
            self.smallbullet_shoot_player()
            self.bigbullet_shoot_player()
            self.player_small_crash()
            self.player_big_crash()
            self.run_update()
            pg.draw.rect(screen, 'black', (0, 0, s_width, 30)) #to draw a rect for the below codes to reside in
            self.create_lives()
            self.create_score()
          
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pg.quit()
                        sys.exit()

                    if event.key == K_s:
                        pg.mixer.Sound.play(shoot_sound)
                        self.player.shoot()

            pg.display.update()
            clock.tick(FPS)


def main():             
    game = Game()      #make an instance "game" inside the main 


if __name__ == '__main__':
    main()             #act as a starting point of execution for the game (without this, game will not run)
