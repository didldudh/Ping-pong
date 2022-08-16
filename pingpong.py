from pygame import *
from random import randint
win_width = 600
win_height = 500
w = display.set_mode((win_width, win_height))
bg = transform.scale(image.load("blue.png"), (win_width, win_height))

clock = time.Clock()
FPS = 60
speed_x = 5
speed_y = 5
font.init()
win1 = font.SysFont('Roboto', 40, 'bold').render('Player_2 win!', True, (100, 0 ,255))
win2 = font.SysFont('Roboto', 40, 'bold').render('Player_1 win!', True, (100, 0 ,255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        w.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect. y < 400:
         self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y < win_width - 80:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        


racket1 = Player('racket.png', 5, 200, 30, 60, 10)
racket2 = Player('racket.png', 1150, 300, 30, 60, 10)
ball = GameSprite('ball.png', 100, 300, 50, 50, 10)
run = True
finish = False
while run:
    if finish != True:
        w.blit(bg, (0, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            speed_x *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            w.blit(win1, win_width/2 - 50, win_width/2)
            run = False
        if ball.rect.x > win_width:
            finish = True
            w.blit(win2, win_width/2 - 50, win_width/2)
            run = False

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
