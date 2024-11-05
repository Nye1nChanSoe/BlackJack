from .card import Card
from .deck import Deck
import pygame


"""
include all the game logic as well as rendering objects
"""
class Game:
    def __init__(self):
        self.card = Card('a', 'd', pygame.image.load('assets/cards/as.png'))
        self.deck = Deck()

    def update(self):
        if not self.card.is_hidden:
            self.card.flip()

    def render(self):
        print(f'is card hidden: {self.card.is_hidden}')
        pass