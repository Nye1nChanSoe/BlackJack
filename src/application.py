import pygame
from src.game import Game
from typing import List

class Application:
    def __init__(self, width: float, height: float, fps: float, caption: str, debug: bool = True):
        self.screen = pygame.display.set_mode((width, height))
        self.fps = fps
        self.caption = caption
        self.icon = pygame.image.load("assets/icon.png")
        self.running = True
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.font = pygame.font.SysFont('timesnewroman', 20)
        self.game = Game(self.screen, self.font, debug)

    def init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.update(events)
            self.render()
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.exit()
            self.clock.tick(self.fps)

    def update(self, events: List[pygame.event.Event]):
        self.game.update(events)

    def render(self):
        self.screen.fill((0, 100, 0))
        # self.screen.fill((0, 0, 0))
        self.game.render()
        pygame.display.flip()

    def exit(self):
        self.running = False
        pygame.display.quit()