import pygame

class Card:
    def __init__(self, rank: str, suit: str, image: pygame.Surface):
        self.rank = rank
        self.suit = suit
        self.image = image
        self.is_hidden = False
        self.card_back = pygame.image.load('assets/cards/cardback.png')

    def flip(self):
        """flip the card"""
        self.is_hidden = not self.is_hidden

    def render(self):
        if self.is_hidden:
            return self.card_back
        return self.image

    def __str__(self):
        return f'Card {self.rank} {self.suit}'