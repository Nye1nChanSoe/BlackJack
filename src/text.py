import pygame

class Text:
    def __init__(self, screen, font_size=30, color=(255, 255, 255)):
        self.screen = screen
        self.font = pygame.font.SysFont(None, font_size)
        self.color = color

    def text(self, text):
        return self.font.render(text, True, self.color)
