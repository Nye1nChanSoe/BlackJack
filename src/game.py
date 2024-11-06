from .card import Card
from .deck import Deck
import pygame


"""
include all the game logic as well as rendering objects
"""
class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.deck = Deck()
        self.card = self.deck.draw()

    def update(self):
        print(self.card)

    def render(self):
        self.screen.blit(self.card.image, (100, 100))