import pygame
import time
from score import getdata

# colours used

White = (255,255,255)
Cream = (226,223,218)

# colours used

# def and classes space starts


def game_screen(info):
    background = pygame.Surface(screen.get_size())
    print screen.get_size()
    background = background.convert()
    background.fill(White)
    font = pygame.font.Font(None, 36)
    text = font.render("Live Cricket Scores", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    info_length = len(info)
    for i in range(0,info_length):
        text = font.render(info[i][1][0].upper()+"-vs-"+info[i][1][1].upper()+" "+info[i][2], 1, (10, 10, 10))
        background.blit(text, (10,50+i*25,20+i*10,20+i*10))
        screen.blit(background,(0,0))
        pygame.display.update()




class Button():
    def __init__(self,size,name,pos):  # name will be displayed on button, size is (x,y), position is(x,y,w,h)
        self.button = pygame.Surface(size)
        self.button = self.button.convert()
        self.button.fill((100,100,100))
        buttonfont = pygame.font.Font(None, 36)
        buttontext = buttonfont.render(name,1,(10, 10, 10))
        self.button.blit(buttontext,pos)




# definition and classes space ends

pygame.init()
screen = pygame.display.set_mode((280, 350))

pygame.display.set_caption("Cricket Score")
initialbackground = pygame.Surface(screen.get_size())
initialbackground = initialbackground.convert()
initialbackground.fill(Cream)
screen.blit(initialbackground, (0,0))
button = Button((20,50),"hello",(10,10,50,50))
screen.blit(button.button,(20,20))

#font = pygame.font.Font(None, 40)
#initialtext = font.render("Loading", 1, (10, 10, 10))
#initialbackground.blit(initialtext,[100,110])





pygame.display.update()

















# main pygame code



time_last=pygame.time.get_ticks()
position = "game screen"

done = False
while not done:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        if position == "main screen":
            position = "in main screen"

        elif position == "game screen":
            time_now = pygame.time.get_ticks()
            wait_time = 10
            if time_now-time_last>=wait_time:
                info=getdata()
                game_screen(info)
                pygame.display.update()
                time_last=time_now


pygame.quit()






