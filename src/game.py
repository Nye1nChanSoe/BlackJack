from .card import Card
from .deck import Deck
from .player import Player
from .dealer import Dealer
import pygame


"""
include all the game logic as well as rendering objects
"""
class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.deck = Deck()
        self.player = Player('Nyein Chan')
        self.dealer = Dealer()
        self.init_deck()
        self.init_player()
        self.init_dealer()

    def init_deck(self):
        self.deck.shuffle()

    def init_player(self):
        self.player.hit(self.deck.draw())
        self.player.hit(self.deck.draw())

    def init_dealer(self):
        self.dealer.hit(self.deck.draw())
        self.dealer.hit(self.deck.draw().flip())

    def update(self):
        self.update_player()
        self.update_dealer()

    def render(self):
        self.render_player_hands()
        self.render_dealer_hands()

    def update_player(self):
        print(self.player)

    def update_dealer(self):
        print(self.dealer)

    def render_player_hands(self):
        card_offset = 60
        x,y = 100, 400
        for i, card in enumerate(self.player.hand):
            card_position = (x + i * card_offset, y)
            self.screen.blit(card.image, card_position)

    def render_dealer_hands(self):
        card_offset = 60
        x,y = 100, 100
        for i, card in enumerate(self.dealer.hand):
            card_position = (x + i * card_offset, y)
            if not card.is_hidden:
                self.screen.blit(card.image, card_position)
            else:
                self.screen.blit(card.card_back, card_position)
