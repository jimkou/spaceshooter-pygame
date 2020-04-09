import pygame
import time
import random
import pgzrun




#SPACESHIP IMAGE - SIZE - POSITION
spaceship = Actor('spaceship')
spaceship._surf = pygame.transform.scale(spaceship._surf, (50, 50))
spaceship.pos = 200, 370

#SPACE
space = Actor('space2')
space._surf = pygame.transform.scale(space._surf, (350 , 400))

#BULLET
bullet = Actor('bullet3')
bullet.pos = (1000,1000)

#EXPLOSION
explosion = Actor('explosion1')
explosion.pos = (1000 , 1000)


#SIZE of MAP
WIDTH = 350
HEIGHT =  400


a_pressed = False
w_pressed = False
d_pressed = False
s_pressed = False
space_pressed = False

#SHOOTING
first_shoot = False
shoot = False
bullet_finished = True

# K for help initialize shoot 2
k = 1
#SHOOTING2
first_shoot2 = False
shoot2 = False
bullet2_finished = False

hit_count = 0

#TIME SHOOT
start_time_shoot = 0
elapsed_time_shoot = 0

#TIME SHOOT 2
start_time_shoot2 = 0
elapsed_time_shoot2 = 0

#ENEMY INIT
enemy_init = True
enemy_first_init = True

#COLLISION
player_collision = False
collision_counter = 0

#EXPLOSION
explosion_effect = False
start_time_explosion = 0
first_explosion = True
second_explosion = False
third_explosion = False
#SCORE
score = 0
#pygame.mixer.music.load('/home/pi/mu_code/music/metallica.wav')
#pygame.mixer.music.play(-1)
game_over = False

potision = explosion.pos

bullets =  []

enemies = []

explosions = []

planets = []

start_time_bull = 0
bull_counter = 0

class planet_class(object):
    def __init__(self , x, y , img):
        self.x = x
        self.y = y
        #self.height = height
        #self.width = width
        self.actor = Actor(img)
        self.actor.pos = ( self.x, self.y)
        self.vel = 1#random.randint(1 , 5)
        self.hits = 0
        self.img = img
       # self.explosionlist = [pygame.image.load('/home/pi/mu_code/images/explosion1.png'),pygame.image.load('/home/pi/mu_code/images/explosion2.png'),pygame.image.load('/home/pi/mu_code/images/explosion3.png')]
        self.player_collision = False

        self.explode = False
        self.position = (0 , 0)
        self.check = True




    def update(self):
        self.actor.top += self.vel

    def check_bullet_hit(self , sprite1 ):


        halfWidthSprite1 = sprite1.width//4
        halfWidthSprite2 = self.actor.width//4
        halfHeightSprite1 = sprite1.height//4
        halfHeightSprite2 = self.actor.height//4
        distanceX = abs(sprite1.center[0] - self.actor.center[0])
        distanceY = abs(sprite1.center[1] - self.actor.center[1])

        if (distanceX < (halfWidthSprite1 + halfWidthSprite2)) and (distanceY < (halfHeightSprite1 + halfHeightSprite2)):


            self.hits += 1


        if ((self.hits >=3) and (not self.explode)):
            
            self.explode = True
            self.position = self.actor.pos
            self.actor.pos = (10000,10000)

    def check_players_collision(self, sprite1 , sprite2):


        halfWidthSprite1 = sprite1.width//3
        halfWidthSprite2 = sprite2.width//3
        halfHeightSprite1 = sprite1.height//3
        halfHeightSprite2 = sprite2.height//3
        distanceX = abs(sprite1.center[0] - sprite2.center[0])
        distanceY = abs(sprite1.center[1] - sprite2.center[1])

        if (distanceX < (halfWidthSprite1 + halfWidthSprite2)) and (distanceY < (halfHeightSprite1 + halfHeightSprite2)):



            self.position = self.actor.pos
            self.actor.pos = (1000 , 1000)
            self.explode = True


class projectile(object):
    def __init__(self, x, y , height , width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.actor = Actor('bullet3')
        self.actor.pos = (self.x  , self.y - 15)
        self.vel = 10
        self.diss = False

    def update(self):
            self.actor.top -= self.vel

    def check_bullet_hit(self , sprite1 ):


        halfWidthSprite1 = sprite1.width//4
        halfWidthSprite2 = self.actor.width//4
        halfHeightSprite1 = sprite1.height//4
        halfHeightSprite2 = self.actor.height//4
        distanceX = abs(sprite1.center[0] - self.actor.center[0])
        distanceY = abs(sprite1.center[1] - self.actor.center[1])

        if (distanceX < (halfWidthSprite1 + halfWidthSprite2)) and (distanceY < (halfHeightSprite1 + halfHeightSprite2)):


            self.diss = True

class explosion_class(object):
    def __init__(self , pos , img):

        self.explosion_effect = False
        self.start_time_explosion = 0
        self.elapsed_time_explosion = 0
        self.first_explosion = True
        self.second_explosion = False
        self.third_explosion = False
        self.fourth_explosion = False
        self.sixth_explosion = False
        self.seventh_explosion = False
        self.explosion_finished = False
        self.pos = pos
        self.actor = Actor('explosion1')
        self.actor_moon = Actor('moon')
        self.img = img
        self.start_time_explosion = time.time()
        if self.img == 'moon':
            self.actor = Actor('moon_explosion1')
        elif self.img == 'enemy1':
            self.actor = Actor('explosion1')


        self.actor.pos = self.pos
        self.player_collision = True
        self.explosion_effect = True


    def explosion_update(self):


            if self.img == 'enemy1':
                self.elapsed_time_explosion = time.time() - self.start_time_explosion
                if self.elapsed_time_explosion > 1.5 :
                    self.actor.pos = (1000 , -1000)
                    self.explosion_effect = False

                else:
                    if self.first_explosion:

                        sounds.enemy1_explosion.play()

                        if self.elapsed_time_explosion > 0.1:

                            self.actor = Actor('explosion1')
                            self.actor.pos = self.pos
                            self.first_explosion = False
                            self.second_explosion = True

                    elif self.second_explosion:
                        if self.elapsed_time_explosion > 0.5:

                            self.actor = Actor('explosion2')
                            self.actor.pos = self.pos
                            self.second_explosion = False
                            self.third_explosion = True
                    elif self.third_explosion:
                        if self.elapsed_time_explosion >=0.7:
                          #  print('third explotion')
                            self.actor = Actor('explosion3')
                            self.actor.pos = self.pos
                            self.third_explosion = False
                            self.fourth_explosion = True
                    elif self.fourth_explosion:
                        if self.elapsed_time_explosion >= 1:
                          #  print('second explotion')
                            self.actor = Actor('explosion4')
                            self.actor.pos = self.pos
                            self.sixth_explosion = True
                            self.fourth_explosion = False
                    elif self.sixth_explosion:
                        if self.elapsed_time_explosion >= 1.3:
                           # print('third explotion')
                            self.actor = Actor('explosion6')
                            self.actor.pos = self.pos
                            self.sixth_explosion = False
                            self.seventh_explosion = True
                    elif self.seventh_explosion:
                        if self.elapsed_time_explosion >= 1.6:
                          #  print('third explotion')
                            self.actor = Actor('explosion7')
                            self.actor.pos = self.pos
                            self.seventh_explosion = False
                            self.explode_finished = True

            elif self.img == 'moon':
                self.elapsed_time_explosion = time.time() - self.start_time_explosion
                if self.elapsed_time_explosion > 1.5 :
                        self.actor.pos = (1000 , 1000)
                        self.explosion_effect = False
                else:

                    if self.first_explosion:

                        if self.elapsed_time_explosion > 0.1:

                            self.actor = Actor('moon_explosion1')
                            self.actor.pos = self.pos
                            self.first_explosion = False
                            self.second_explosion = True
                         #   print('moon first explosion')
                    elif self.second_explosion:
                        if self.elapsed_time_explosion > 0.5:
                          #  print('moon second explotion')
                            self.actor = Actor('moon_explosion2')
                            self.actor.pos = self.pos
                            self.second_explosion = False
                            self.third_explosion = True
                    elif self.third_explosion:
                        if self.elapsed_time_explosion >=0.7:
                          #  print('moon third explotion')
                            self.actor = Actor('moon_explosion3')
                            self.actor.pos = self.pos
                            self.third_explosion = False
                            self.fourth_explosion = True
                    elif self.fourth_explosion:
                        if self.elapsed_time_explosion >= 1:
                           # print('moon 4 explotion')
                            self.actor = Actor('moon_explosion4')
                            self.actor.pos = self.pos
                            self.sixth_explosion = True
                            self.fourth_explosion = False
                    elif self.sixth_explosion:
                        if self.elapsed_time_explosion >= 1.3:
                          #  print('third explotion')
                            self.actor = Actor('moon_explosion5')
                            self.actor.pos = self.pos
                            self.sixth_explosion = False
                            self.seventh_explosion = True
                    elif self.seventh_explosion:
                        if self.elapsed_time_explosion >= 1.6:
                           # print('third explotion')
                            self.actor = Actor('moon_explosion6')
                            self.actor.pos = self.pos
                            self.seventh_explosion = False
                            self.explode_finished = True

class enemy1(object):
    def __init__(self , x, y , height , width , img):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.actor = Actor(img)
        self.actor.pos = ( self.x, self.y)
        self.vel = 1#random.randint(1 , 5)
        self.hits = 0
        self.img = img
       # self.explosionlist = [pygame.image.load('/home/pi/mu_code/images/explosion1.png'),pygame.image.load('/home/pi/mu_code/images/explosion2.png'),pygame.image.load('/home/pi/mu_code/images/explosion3.png')]
        self.player_collision = False
        self.explosion = Actor('explosion1')
        self.explode = False
        self.position = (0 , 0)


#EXPLOSION
        self.explosion_effect = False
        self.start_time_explosion = 0
        self.elapsed_time_explosion = 0
        self.first_explosion = True
        self.second_explosion = False
        self.third_explosion = False

    def update(self):
        self.actor.top += self.vel

    def check_bullet_hit(self , sprite1 ):


        halfWidthSprite1 = sprite1.width//4
        halfWidthSprite2 = self.actor.width//4
        halfHeightSprite1 = sprite1.height//4
        halfHeightSprite2 = self.actor.height//4
        distanceX = abs(sprite1.center[0] - self.actor.center[0])
        distanceY = abs(sprite1.center[1] - self.actor.center[1])

        if (distanceX < (halfWidthSprite1 + halfWidthSprite2)) and (distanceY < (halfHeightSprite1 + halfHeightSprite2)):


            self.hits += 1



              #  self.actor.pos = (10000,10000)

    def check_players_collision(self, sprite1 , sprite2):
        global game_over

        halfWidthSprite1 = sprite1.width//3
        halfWidthSprite2 = sprite2.width//3
        halfHeightSprite1 = sprite1.height//3
        halfHeightSprite2 = sprite2.height//3
        distanceX = abs(sprite1.center[0] - sprite2.center[0])
        distanceY = abs(sprite1.center[1] - sprite2.center[1])

        if (distanceX < (halfWidthSprite1 + halfWidthSprite2)) and (distanceY < (halfHeightSprite1 + halfHeightSprite2)):
            print('COLLIDE')


            self.position = self.actor.pos
            self.actor.pos = (1000 , 1000)
            self.explode = True
            game_over = True





for i in range(10):
    a = random.randint(30 , 400)
    b = random.randint(-300 , 0)
    enemies.append(enemy1(a ,b , 36 , 36 , 'enemy1'))

for i in range(10):

    planets.append(planet_class(100 ,0 , 'moon'))






def draw():
    
    global score
    global planets
    global enemies
    global explosions
    global bullet
    screen.clear()
    space.draw()
    screen.draw.text("Score: " +str(score) ,(10, 10))
   # spaceship.draw()



    if len(enemies) < 1:
         for i in range(10):
            a = random.randint(30 , 300)
            b = random.randint(-300 , 0)
            enemies.append(enemy1(a ,b , 36 , 36 , 'enemy1'))
    if len(planets) <= 1:

            a = random.randint(30 , 300)
            b = random.randint(-300 , 0)
            planets.append(planet_class(a ,b , 'moon'))

    for planet in planets:
        #print(len(planets))
        planet.check_players_collision(planet.actor , spaceship)
        for bullet in bullets:
           bullet.check_bullet_hit(planet.actor)
           planet.check_bullet_hit(bullet.actor)
            
        #explosion_class(enemy.actor.pos , enemy.img)
        if planet.explode:
            explosions.append(explosion_class(planet.position , planet.img))
            planets.pop(planets.index(planet))

        if planet.y > 400:
            planets.pop(planets.index(planet))
        planet.update()
        planet.actor.draw()

    for explosion in explosions:
            if explosion.explosion_finished:
                #print('g=finito')
                explosions.pop(explosions.index(explosion))
            else:
                explosion.explosion_update()
            explosion.actor.draw()



    for enemy in enemies:
        #enemy.update()
       # enemy.actor.draw()
        enemy.check_players_collision(enemy.actor , spaceship)
        if enemy.explode:
            sounds.enemy1_explosion.play()
            explosions.append(explosion_class(enemy.position , enemy.img))
        #if enemy.explode :
           # print('appended')
           # explosions.append(explosion_class(enemy.position))
          #  enemy.explode = False


        if enemy.actor.y > 500:
            #print('popped enemy')
            enemies.pop(enemies.index(enemy))
            continue;

        if enemy.hits >=3:

            score += 1
            a=enemy.actor.pos
            b = enemy.position
            explosions.append(explosion_class(enemy.actor.pos , enemy.img))
            if len(enemies) >= 1:
                enemies.pop(enemies.index(enemy))



       # for explosion in explosions:
         #   if explosion.explosion_finished:
           #     print('g=finito')
            #    explosions.pop(explosions.index(explosion))
          #  else:
          #      explosion.explosion_update()
         #   explosion.actor.draw()
       # check_players_collision(spaceship, enemy.actor)
        for bullet in bullets:
            bullet.check_bullet_hit(enemy.actor)
            enemy.check_bullet_hit(bullet.actor)
            if bullet.diss:
               bullets.pop(bullets.index(bullet))
           # if enemy.hits == 3 :
            #d  game_over = True
        enemy.update()
        enemy.actor.draw()

    for bullet in bullets:
        if bullet.actor.y <= 0:

           bullets.pop(bullets.index(bullet))
        bullet.update()

        bullet.actor.draw()

    spaceship.draw()

    if  game_over:
        screen.clear()
        screen.draw.text("Score: " +str(score) ,(WIDTH/2, HEIGHT/2))
        


    



def check_borders():
    if spaceship.left >= WIDTH - 45:
        spaceship.left = WIDTH - 45

    if spaceship.right <= 50:
        spaceship.right =  + 50
    if spaceship.bottom <= 50:
        spaceship.bottom = 50
    if spaceship.top >= 350:
        spaceship.top = 350


def make_explosion(sprite):
    explosion.pos = sprite.pos
    sprite.pos = (1000 , 1000)


def check_players_collision(sprite1 , sprite2):
    global player_collision
    global explosion_effect
    global start_time_explosion
    global first_explosion
    global second_explosion
    global third_explosion
    global explosion
    global position

    halfWidthSprite1 = sprite1.width//3
    halfWidthSprite2 = sprite2.width//3
    halfHeightSprite1 = sprite1.height//3
    halfHeightSprite2 = sprite2.height//3
    distanceX = abs(sprite1.center[0] - sprite2.center[0])
    distanceY = abs(sprite1.center[1] - sprite2.center[1])

    if (distanceX < (halfWidthSprite1 + halfWidthSprite2)) and (distanceY < (halfHeightSprite1 + halfHeightSprite2)):
        print('collision1')

        start_time_explosion = time.time()
        position = sprite2.pos
        sprite2.pos = (1000 , 1000)
        player_collision = True
        explosion_effect = True
        first_explosion = True

    if explosion_effect:
        elapsed_time_explosion = time.time() - start_time_explosion
        if elapsed_time_explosion > 1.5 :
            explosion.pos = (1000 , 1000)
            explosion_effect = False

        else:
            if first_explosion:
                if elapsed_time_explosion > 0.2:

                    explosion = Actor('explosion1')
                    explosion.pos = position
                    first_explosion = False
                    second_explosion = True

            elif second_explosion:
                if elapsed_time_explosion > 1:

                    explosion = Actor('explosion2')
                    explosion.pos = position
                    second_explosion = False
                    third_explosion = True
            elif third_explosion:
                if elapsed_time_explosion <= 1.5:

                    explosion = Actor('explosion3')
                    explosion.pos = position
                    third_explosion = False










def check_bullet_hit(sprite1 , sprite2):
    global score
    global hit_count
    global potision_en
    halfWidthSprite1 = sprite1.width//4
    halfWidthSprite2 = sprite2.width//4
    halfHeightSprite1 = sprite1.height//4
    halfHeightSprite2 = sprite2.height//4
    distanceX = abs(sprite1.center[0] - sprite2.center[0])
    distanceY = abs(sprite1.center[1] - sprite2.center[1])

    if (distanceX < (halfWidthSprite1 + halfWidthSprite2)) and (distanceY < (halfHeightSprite1 + halfHeightSprite2)):


        sprite2.hits += 1
        sprite1.pos = (1000 , 1000)
        if sprite2.hits == 3:
            score += 1

            sprite2.hits = 0

            sprite2.pos = (10000,10000)




def update():
    global first_shoot
    global shoot
    global start_time_shoot
    global elapsed_time_shoot
    global bullet_finished
    global first_shoot2
    global shoot2
    global start_time_shoot2
    global elapsed_time_shoot2
    global bullet2_finished
    global k
    global enemy_init
    global score
    global check_collision
    global collision_counter
    global player_collision
    global game_over
    global start_time_bull
    global bull_counter
    #bullet2.top = spaceship.top



   # for enemy in enemies:
      #  check_players_collision(spaceship, enemy.actor)
      #  for bullet in bullets:
      #     enemy.check_bullet_hit(bullet.actor)
          # print(enemies.index(enemy))
        #   if enemy.hits == 3 :
              # enemies.pop(enemies.index(enemy))
          #    print('yes')

    if player_collision:
        collision_counter += 1
        player_collision = False
        if collision_counter >= 3:
                game_over = False


    #check_collision()
    check_borders()

    if a_pressed :
        spaceship.left -= 2
    if d_pressed :
        spaceship.left += 2
    if s_pressed :
        spaceship.top += 2
    if w_pressed:
        spaceship.top -= 2
    if space_pressed and bull_counter < 1:
        sounds.gun.play()
        bullets.append(projectile (spaceship.x , spaceship.y , 36 ,36))
        bull_counter += 1
        start_time_bull = time.time()

    else:
        elapsed_time_bull = time.time() - start_time_bull
        if elapsed_time_bull > 0.1:
            bull_counter = 0





       # if bullet_finished:

      #     first_shoot = True
        #   bullet_finished = False

       #    bullet.pos= spaceship.pos
           #bullet2.bottomleft = spaceship.center



 #   if first_shoot:
  #      start_time_shoot = time.time()
   #     first_shoot = False
  #      shoot = True

 #   if shoot :
 #       elapsed_time_shoot = time.time() - start_time_shoot
  #      if elapsed_time_shoot < 0.3:
   #         bullet.top -= 20
            #bullet2.top -= 4
   #     else:
     #       shoot = False
      #      bullet.pos = (1000 , 1000)
      #      bullet_finished = True





def on_key_down(key):
    global w_pressed
    global a_pressed
    global d_pressed
    global s_pressed
    global space_pressed

    if key == keys.A:
        a_pressed = True
    if key == keys.D:
        d_pressed = True
    if key == keys.W:
        w_pressed = True
    if key == keys.S :
        s_pressed = True
    if key == keys.SPACE :

        space_pressed = True

def on_key_up(key):
    global w_pressed
    global a_pressed
    global d_pressed
    global s_pressed
    global space_pressed

    if key == keys.A:
        a_pressed = False
    if key == keys.D:
        d_pressed = False
    if key == keys.W:
        w_pressed = False
    if key == keys.S:
        s_pressed = False
    if key == keys.SPACE:
        space_pressed = False
pgzrun.go()