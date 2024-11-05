import random
from typing import List
from .card import Card
from .card_renderer import CardRenderer
from .deck_renderer import DeckRenderer
import pygame

class Deck:
    def __init__(self, renderer: DeckRenderer):
        self.renderer = renderer
        self.cards: List[Card] = []
        self.initialize_cards()

    def initialize_cards(self) -> None:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Load card images
        face_up_image = pygame.image.load('assets/cards/ad.png')
        face_down_image = pygame.image.load('assets/cards/cardback.png')
        card_renderer = CardRenderer(face_up_image, face_down_image)

        # Initialize the deck of cards
        self.cards = [Card(rank, suit, card_renderer, face_up=False) for suit in suits for rank in ranks]

    def shuffle(self) -> None:
        random.shuffle(self.cards)
        for _ in range(3):
            self.renderer.render_shuffle()
            pygame.time.wait(100)

    def draw(self) -> Card:
        if not self.cards:
            raise ValueError("The deck is empty.")
        card = self.cards.pop()
        self.renderer.render_draw(card)
        return card

    def render(self) -> None:
        self.renderer.render_stack(len(self.cards))

    def is_empty(self) -> bool:
        return len(self.cards) == 0
