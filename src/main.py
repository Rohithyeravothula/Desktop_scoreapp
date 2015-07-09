import pygame
from score import getdata




pygame.init()

class mainapp():
    def __init__(self,info):
        self.screen = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Cricket Score")
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((26,223,218))
        #self.screen.blit(self.background,(0,0))
        #pygame.display.update()
    def main_screen(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Live Cricket Scores", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)
        info_length = len(info)
        for i in range(0,info_length):
            text = font.render(info[i][1][0]+"-vs-"+info[i][1][1], 1, (10, 10, 10))
            #textpos = text.get_rect()
            #textpos.centerx = self.background.get_rect().centerx
            self.background.blit(text, (10,0+i*15,20+i*10,20+i*10))
        self.screen.blit(self.background,(0,0))
        pygame.display.update()
    def mainloop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.update()



info = getdata()  # will get information about live matches
canvas = mainapp(info)
canvas.main_screen()
canvas.mainloop()