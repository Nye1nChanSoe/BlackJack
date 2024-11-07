import pygame

class Card:
    def __init__(self, rank: str, suit: str, image: pygame.Surface):
        self.rank = rank
        self.suit = suit
        self.image = image
        self.is_hidden = False
        self.card_back = pygame.image.load('assets/cards/cardback.png')

        self.is_flipping = False
        self.flip_progress = 0.0
        self.flip_duration = 1.0

    def flip(self) -> 'Card':
        """flip the card"""
        self.is_hidden = not self.is_hidden
        return self

    def render(self):
        if self.is_hidden:
            return self.card_back
        return self.image

    def get_image(self):
        if self.is_hidden:
            return self.card_back
        return self.image

    def __str__(self):
        if self.is_hidden:
            return 'Hidden'
        return f'Card {self.rank} {self.suit}'