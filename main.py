#all your imports - no touching!
import pygame, sys, os


#classes and functions
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#inits - if it's already here - no touching!
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
os.environ["SDL_VIDEO_CENETERED"] = "1"
pygame.init()
pygame.font.init()

win = pygame.display
    
#define screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

#create game window
d = win.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
win.set_caption("Shooter Game!")

#frame rate
clock = pygame.time.Clock()

#score stuff
score = 0
score_increment = 10

bg = pygame.image.load("img/space.png")

shipIMG = pygame.image.load("img/ship.png")
shipIMG = pygame.transform.scale(shipIMG, (50,50))

alienIMG = pygame.image.load("img/alien.png")
alienIMG = pygame.transform.scale(alienIMG, (40,40))

missleIMG = pygame.image.load("img/missile.png")
missleIMG = pygame.transform.scale(missleIMG, (10, 30))

#objects!
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        #attributes
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 2
        self.image = shipIMG
    def draw(self,d):
        d.blit(self.image,(self.x, self.y))

    def move_left(self):
        self.x -= self.speed
    
    def move_right(self):
        self.x += self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 10

        self.image = pygame.Surface((10,30))
        self.image = missleIMG
        self.rect = pygame.Rect(x,y,10,30)
    
    def update(self):
        self.y -= self.speed
        self.rect =  pygame.Rect(self.x,self.y,10,30)
    def draw(self):
        d.blit(self.image,(self.x, self.y)) 

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((40,40))
        self.rect = pygame.Rect(x,y,40,40)
        self.image = alienIMG
    def draw(self):
        d.blit(self.image,(self.x,self.y))

#main
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
p = Player(60,300,50,50)
bulletGroup = pygame.sprite.Group()
squareTarg = Target(200,100)
badGuy = Target(300, 50)
#allGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
enemyGroup.add(squareTarg)
enemyGroup.add(badGuy)

run = True
while run:
    font = pygame.font.Font(None, 36)
    #nothing here yet
    clock.tick(100)
    #print(pygame.time.get_ticks())
    #if pygame.time.get_ticks() % 750 == 0:
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(p.x + p.width//2, p.y)
                bulletGroup.add(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p.move_left()
    if keys[pygame.K_RIGHT]:
        p.move_right()
    
    collisions = pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, True)


    if len(collisions) == 1:
        score += score_increment


    """if pygame.sprite.spritecollideany(squareTarg,bulletGroup):
        print("hit")
        squareTarg.kill()
        squareTarg.update()
    
        win.update()"""
    
    #update background
    d.blit(bg, (0,0))
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    d.blit(score_text, (10, 10))
    for b in bulletGroup:
        b.update()
        b.draw()
        if b.y < 0:
            b.kill()
      
    for item in enemyGroup:
        item.draw()
    
    p.draw(d)
    #update display
    win.update()