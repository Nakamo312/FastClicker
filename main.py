import pygame
from random import randint
from time import time
max_frame = 30       
frame = max_frame-1

WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
LIGHT_BLUE = (200, 255, 255) 
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)




pygame.init()

window = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

finish = True

Font = pygame.font.SysFont('Verdana',25)
Font1 = pygame.font.SysFont('Comic sans',50)


class Area():
    def __init__(self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill = color
    def fill_area(self):
        pygame.draw.rect(window,self.fill,self.rect)    

    def color(self,color):
        self.fill = color
    def outline(self,border_color,thick):
        pygame.draw.rect(window, border_color, self.rect, thick)  
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
        
class Label(Area):
    def __init__(self,x,y,width,height,color,text):
        super().__init__(x,y,width,height,color)
        self.font = pygame.font.SysFont('Verdana',15)
        self.text = self.font.render(text, True, BLACK)
    def draw(self):
        self.fill_area()
        self.outline(BLUE,5)
    def draw_label(self,shift_x,shift_y):
        self.fill_area()
        self.outline(BLUE,5)
        window.blit(self.text,(self.rect.x + shift_x,self.rect.y +shift_y))
    


cards = []
for i in range(4):
    cards.append(Label(112*i+50,200,75,115,YELLOW,'CLICK'))


start_time = time()
cur_time = start_time
total_time = 10
score = 0
text_timer = Font.render('Время: ' + str(int(cur_time)), True, BLUE)

text_score = Font.render('Счет: ' + str(score), True, BLUE)

text_win = Font1.render('ВЫ ВЫИГРАЛИ!', True, BLACK)
text_lose = Font1.render('ВЫ ПРОИГРАЛИ', True, BLACK)
run = True
while finish:
    if run: 
        window.fill(LIGHT_BLUE)
        frame+=1
        if frame // 6 == 0:
            if cur_time != 0:
                cur_time = 10 - int(time() - start_time )
                text_timer = Font.render('Время: ' + str(int(cur_time)), True, BLUE)
            else:
                run = False    
        if frame == max_frame:         
            rand_num = randint(0,3)
            frame = 0
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                finish = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    x,y = e.pos
                    for i in range(len(cards)):
                        if cards[i].collidepoint(x,y):
                            if i == rand_num:
                                cards[i].color(GREEN)
                                score += 1
                            else:
                                cards[i].color(RED) 
                                score -= 1  
                            text_score = Font.render('Счет: ' + str(min(max(0,score),10)), True, BLUE)          
        pygame.display.set_caption('FPS: '+str(int(clock.get_fps())))  
        for i in range(len(cards)):
            cards[i].draw()
            if (frame // 2) == 0:
                cards[i].color(YELLOW)
            if i == rand_num:
                cards[i].draw_label(15,45)       
        clock.tick(60)
        window.blit(text_timer,(25,25))
        window.blit(text_score,(375,25))
        pygame.display.update()
    else:
        if score == 10:
            window.fill(GREEN)
            window.blit(text_win,(125,150))
        else:
            window.fill(RED)
            window.blit(text_lose,(125,150))
        pygame.display.update()    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                finish = False            
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    start_time = time()
                    cur_time = start_time
                    total_time = 10
                    score = 0
                    text_timer = Font.render('Время: ' + str(int(cur_time)), True, BLUE)
                    text_score = Font.render('Счет: ' + str(score), True, BLUE)
                    run = True  
