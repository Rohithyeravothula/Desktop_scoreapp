
from main import mainapp
import pygame

class main_screen(mainapp):
    def __init__(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Live Cricket Scores", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)
        self.screen.blit(self.background,(0,0))
        pygame.display.update()