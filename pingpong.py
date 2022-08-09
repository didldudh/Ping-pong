from pygame import *
from random import randint

win = display.set_mode((700, 700))
backgroud = transform.scale(image.load('blue.png'), (700, 700))

FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        if keys[K_W] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.x < 695:
            self.rect.x += self.speed

    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 695:
            self.rect.y += self.speed

racket1 = Player('racket.png', 5, 200, 30, 60, 10)
racket2 = Player('racket.png', 650, 300, 30, 60, 10)
ball = GameSprite('ball.png', 100, 300, 50, 50, 10)

run = True
finish = False
while run:
    win.blit(background, (0, 0))
    racket1.reset()
    racket2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
