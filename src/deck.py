import random
from typing import List
from .card import Card
import pygame


class Deck:
    def __init__(self):
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards: List[Card] = []
        self.create_cards()

    def create_cards(self):
        suits_map = {'♠': 's', '♥': 'h', '♦': 'd', '♣': 'c'}
        ranks_map = {'A': 'a', 'J': 'j', 'Q': 'q', 'K': 'k'}

        for suit_symbol, suit_suffix in suits_map.items():
            for rank in range(2, 11):
                image = pygame.image.load(f'assets/cards/{rank}{suit_suffix}.png')
                card = Card(rank=str(rank), suit=suit_symbol, image=image)
                self.cards.append(card)

        for suit_symbol, suit_suffix in suits_map.items():
            for face, face_letter in ranks_map.items():
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
