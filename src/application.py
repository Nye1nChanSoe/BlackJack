import pygame
from src.game import Game

class Application:
    def __init__(self, width: float, height: float, fps: float, caption: str):
        self.screen = pygame.display.set_mode((width, height))
        self.fps = fps
        self.caption = caption
        self.icon = pygame.image.load("assets/icon.png")
        self.running = True
        self.clock = pygame.time.Clock()
        self.game = Game()

    def init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)

    def run(self):
        while self.running:
            self.update()
            self.render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.exit()
            self.clock.tick(self.fps)

    def update(self):
        self.game.update()

    def render(self):
        self.game.render()
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def exit(self):
        self.running = False
        pygame.display.quit()