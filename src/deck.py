import random
from typing import List
from .card import Card
import pygame


class Deck:
    def __init__(self):
        self.suits_map = {'♠': 's', '♥': 'h', '♦': 'd', '♣': 'c'}
        self.ranks_map = {'A': 'a', 'J': 'j', 'Q': 'q', 'K': 'k'}
        self.cards: List[Card] = []
        self.create_cards()

    def create_cards(self):
        for suit_symbol, suit_suffix in self.suits_map.items():
            # Add numbered cards (2-10)
            for rank in range(2, 11):
                image = pygame.image.load(f'assets/cards/{rank}{suit_suffix}.png')
                card = Card(rank=str(rank), suit=suit_symbol, image=image)
                self.cards.append(card)

            # Add face cards (A, J, Q, K)
            for face, face_letter in self.ranks_map.items():
                image = pygame.image.load(f'assets/cards/{face_letter}{suit_suffix}.png')
                card = Card(rank=face, suit=suit_symbol, image=image)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()

    def reset(self):
        self.cards.clear()
        self.create_cards()
        self.shuffle()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        cards = ' | '.join(str(card) for card in self.cards)
        return cards
