from pygame import *  

init()

win_width = 700
win_height = 700
window = display.set_mode((win_width,win_height))
display.set_caption('Ping_Pong') 
window.fill((255,255,255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 70:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 70:
            self.rect.y += self.speed


ball = Player('pngwing.com (1).png', 250,250,10)
speed_x = 3
speed_y = 3
Ploika_1 = Player('pngwing.com.png',0,0,10)
Ploika_2 = Player('pngwing.com.png',630,0,10)

clock = time.Clock()
FPS = 60
game = True
finish = False

font.init()
font1 = font.Font(None, 36)

win_text = font1.render('Победил кидала-1!', None, (255,255,255))
lose_text = font1.render('Победил кидала-2!', None, (255,0,0))

while game:
    for e in event.get():
       if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill((255,255,255))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if sprite.collide_rect(Ploika_1, ball) or sprite.collide_rect(Ploika_2, ball):
            speed_x *= -1
        
        if ball.rect.y >= 650 or ball.rect.y <= 1:
            speed_y *= -1
        
        if ball.rect.x >= 650:
            speed_x *= 0
            lose_text.reset()
            lose_text.update()
        if ball.rect.x <= 1:
            speed_x *= 0
            win_text.reset()
            win_text.update()

        ball.reset()
        Ploika_1.reset()  
        Ploika_2.reset()
    display.update()
    Ploika_1.update2()
    Ploika_2.update1()
    clock.tick(FPS)
    

  