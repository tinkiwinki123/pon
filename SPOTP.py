import pygame
from random import randint
from time import sleep
pygame.init()
# Створення вікон гри
lose_image = pygame.image.load('lose.png')
background_image = pygame.image.load('bg.png') # Колір фону ігрової сцени
prewiew_image = pygame.image.load('prewiew.png')
size = (800, 800) # Розмір ігрової сцени
mw = pygame.display.set_mode(size) # Створюємо вікно для ігрової сцени
prewiew = pygame.display.set_mode(size)
clock = pygame.time.Clock() # Створюємо твймер
FPS = 60 # Змінна для збереженн FPS
font1=pygame.font.Font(None, 70)
font2=pygame.font.Font(None, 40)
#Кольори
DARK_BLUE=(0,0,55)
WHITE = ((255,255,255))
DARK_GREEN = (1,50,32)
RED = (255,0,0)
#Рахунок та сердечки
score=0
live=3

# Класи для гри
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = background_image
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Клас для створення області зображення
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
#Ігрові змінні
plane = Picture('plane.png', 250, 700, 60, 50)
monster = Picture('monster.png',randint(0,750) , 0, 50, 50)
monster2 = Picture('monster.png',randint(0,750) , 0, 50, 50)
monster3 = Picture('monster.png',randint(0,750) , 0, 50, 50)
people = Picture('people.png', randint(0,750), 0, 50, 50)
heart = Picture('heart.png', 0, 0, 50, 50)
heart2 = Picture('heart.png', 50, 0, 50, 50)
heart3 = Picture('heart.png', 100, 0, 50, 50)
exit= Label(0,750,80,60, RED)
exit.set_text('ВИЙТИ', 23, WHITE)
restart= Label(200,400,410,70, DARK_GREEN)
restart.set_text('ПОЧАТИ ЗНОВУ', 50, WHITE)
step = 50
move_RIGHT = False
move_LEFT = False
running = 1
move= 4
#Цикл гри
while running == 1: #Стартове вікно
    prewiew.blit(prewiew_image, (0,0))
    exit.draw(0,10)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if exit.collidepoint(x, y):
                running=False
            else:
                running = 2    
    pygame.display.update()
    clock.tick(FPS)
while running == 2: #Основна гра

    move_RIGHT = False
    move_LEFT = False
    move_UP =False
    move_DOWN = False
    mw.blit(background_image, (0, 0))
    plane.draw()
    monster.draw()
    monster2.draw()
    monster3.draw()
    people.draw()
    exit.draw(0,10)
    score_text=font2.render('Рахунок:'+str(score),True, DARK_BLUE)
    mw.blit(score_text, (650,0))
    if live==3:
        heart.draw()
        heart2.draw()
        heart3.draw() 
    if live==2:
        heart.draw()
        heart2.draw()
        
    if live==1:
        heart.draw()
    
    if live<=0:
        running=3
        pygame.display.update()
        clock.tick(FPS)
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_RIGHT = True
            if event.key == pygame.K_LEFT:
                move_LEFT = True
            if event.key == pygame.K_UP:
                move_UP = True
            if event.key == pygame.K_DOWN:
                move_DOWN = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if exit.collidepoint(x, y):
                    running=False  # як
    monster.rect.y += move
    monster2.rect.y += move
    monster3.rect.y += move
    people.rect.y += move
    if move_RIGHT:
        plane.rect.x += step

    if move_LEFT:
        plane.rect.x -= step
    
    if move_UP:
        plane.rect.y -= step

    if move_DOWN:
        plane.rect.y += step

    if monster2.rect.y > 800:
        monster2 = Picture('monster.png', randint(0,750), 0, 60, 50)

    if monster.rect.y > 800:
        monster = Picture('monster.png', randint(0,750), 0, 60, 50)

    if monster3.rect.y > 800:
        monster3 = Picture('monster.png', randint(0,750), 0, 50, 50)

    if people.rect.y > 800:
        people = Picture('people.png', randint(0,750), 0, 50, 50)
        live -=1
    if people.rect.colliderect(plane.rect):
        people = Picture('people.png', randint(0,750), 0, 50, 50)
        score+=1
    
    if monster.rect.colliderect(plane.rect):
        monster = Picture('monster.png', randint(0,750), 0, 50, 50)
        live-=1
    
    if monster2.rect.colliderect(plane.rect):
        monster2 = Picture('monster.png', randint(0,750), 0, 50, 50)
        live-=1
    
    if monster3.rect.colliderect(plane.rect):
        monster3 = Picture('monster.png', randint(0,750), 0, 50, 50)
        live-=1
        pygame.display.update()
        clock.tick(FPS)
    pygame.display.update()
    clock.tick(FPS)

while running == 3: #Вікно поразки
    mw.blit(lose_image, (0,0))
    exit.draw(0,10)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if exit.collidepoint(x,y):
                running = False
    pygame.display.update()
    clock.tick(FPS)
