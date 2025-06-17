from pygame import *  

init()

win_width = 700
win_height = 500
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
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 70:
            self.rect.y += self.speed





clock = time.Clock()
FPS = 60
game = True


font.init()
font1 = font.Font(None, 36)

win_text = font1.render('Победил кидала-1!', True, (255,255,255))
lose_text = font1.render('Победил кидала-2!', True, (255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
      
           

    
   

   
    
 
    

    
    
    display.update()
    clock.tick(FPS)
    

  