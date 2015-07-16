import pygame
import time
from score import getdata

# colours used

White = (255,255,255)
Cream = (226,223,218)

# colours used

# def and classes space starts


def main_screen(info):
    background = pygame.Surface(screen.get_size())
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
    def __init__(self,size,name):
        self.button = pygame.Surface(size)
        self.button = self.button.convert()
        self.button.fill((100,100,100))
        buttonfont = pygame.font.Font(None, 36)
        buttontext = buttonfont.render(name,1,(10, 10, 10))
        buttontextpos = self.button.get_rect()
        self.button.blit(buttontext,buttontextpos)




# definition and classes space ends

pygame.init()
screen = pygame.display.set_mode((280, 350))

pygame.display.set_caption("Cricket Score")
initialbackground = pygame.Surface(screen.get_size())
initialbackground = initialbackground.convert()
initialbackground.fill(Cream)
button = Button((10,10),"hello")
screen.blit(button.button,(20,20))

#font = pygame.font.Font(None, 40)
#initialtext = font.render("Loading", 1, (10, 10, 10))
#initialbackground.blit(initialtext,[100,110])





screen.blit(initialbackground, (0,0))
pygame.display.update()





def mainloop(time_last):
    while True:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        time_now = pygame.time.get_ticks()
        wait_time = 10
        if time_now-time_last>=wait_time:
            info=getdata()
            main_screen(info)
            pygame.display.update()
            time_last=time_now


time_last=pygame.time.get_ticks()
mainloop(time_last)






