  #Создай собственный Шутер!

from pygame import *
from random import randint                                                                                                   


win_width = 1090 
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Шутер')
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


FPS = 60


lost = 0
window.blit(background,(0, 500 ))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')
fire.play()
clock = time.Clock()
game = True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]:
            self.rect.x += self.speed 
   
    def shoot(self):
        bullet = Bullet("laser.png", self.rect.centerx, self.rect.top, 10  )
        bullets.add(bullet)
           

class Monster(GameSprite):
    direction = "down"
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
        
        if self.rect.y == 500:
            self.rect.y == 0
            
       

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()

rocket = Player('rocketa-removebg-preview.png',700,650,7)
monsters = sprite.Group()
for i in range(6):
    monster = Monster("DFG.png", randint(80, win_width - 80),0,randint(1, 3))
    monsters.add(monster)



bullets = sprite.Group()


score = 0

while game:
    window.blit(background,(0,0))
    rocket.update()
    monsters.update()
    bullets.update()
    rocket.reset()
    monsters.draw(window)
    bullets.draw(window)
    for e in event.get():
        if e.type == QUIT:
            game = False 
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.shoot()
    collides = sprite.groupcollide(monsters,bullets,True, True)
    for c in collides:
        score = score + 1
        monster = Monster("DFG.png", randint(80, win_width - 80),0,randint(1, 3))
        monsters.add(monster)
    if sprite.spritecollide(rocket,monsters, False) or lost >=3 :
        finish = False

    if score >=30 :
        game = False 
    clock.tick(FPS)
    display.update()
 