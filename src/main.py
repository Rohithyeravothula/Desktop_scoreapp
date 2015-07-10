import pygame
import time
from score import getdata




pygame.init()

class mainapp():
    def __init__(self):
        self.screen = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Cricket Score")
        #self.screen.blit(self.background,(0,0))
        #pygame.display.update()
    def main_screen(self,info):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((26,223,218))
        font = pygame.font.Font(None, 36)
        text = font.render("Live Cricket Scores", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)
        info_length = len(info)
        for i in range(0,info_length):
            text = font.render(info[i][1][0]+"-vs-"+info[i][1][1]+" "+info[i][2], 1, (10, 10, 10))
            #textpos = text.get_rect()
            #textpos.centerx = self.background.get_rect().centerx
            self.background.blit(text, (10,20+i*25,20+i*10,20+i*10))
        self.screen.blit(self.background,(0,0))
        pygame.display.update()





def mainloop(time_last):
    done = False
    while not done:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        time_now = pygame.time.get_ticks()
        wait_time = 1000
        if time_now-time_last>=wait_time:
            info=getdata()
            canvas.main_screen(info)
            pygame.display.update()
            time_last=time_now


canvas = mainapp()
time_last=pygame.time.get_ticks()
mainloop(time_last)





