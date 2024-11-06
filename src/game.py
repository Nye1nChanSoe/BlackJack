from .card import Card
from .deck import Deck
from .player import Player
from .dealer import Dealer
from .button import Button
import pygame


"""
include all the game logic as well as rendering objects
"""
class Game:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font, debug: bool):
        self.screen = screen
        self.font = font
        self.deck = Deck()
        self.player = Player('Nyein Chan')
        self.dealer = Dealer()
        self.debug_mode = debug

        self.hit_button = Button((560, 500), (80, 40), "Hit", self.font)
        self.stand_button = Button((660, 500), (80, 40), "Stand", self.font)

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

        self.hit_button.draw(self.screen)
        self.stand_button.draw(self.screen)

    def update_player(self):
        if self.debug_mode:
            print(self.player)

    def update_dealer(self):
        if self.debug_mode:
            print(self.dealer)

    def render_player_hands(self):
        card_offset = 60
        x, y = 100, 400

        player_caption = self.font.render(self.player.name, True, (255, 255, 255))

        for i, card in enumerate(self.player.hand):
            card_position = (x + i * card_offset, y)
            self.screen.blit(card.get_image(), card_position)

        text = f'Hand: {str(self.player.hand_value())}'
        text_surface = self.font.render(text, True, (255, 255, 255))

        self.screen.blit(player_caption, (x, y - 40))
        self.screen.blit(text_surface, (x + 10, y + 150))

    def render_dealer_hands(self):
        card_offset = 60
        x, y = 100, 60

        dealer_caption = self.font.render("Dealer", True, (255, 255, 255))

        for i, card in enumerate(self.dealer.hand):
            card_position = (x + i * card_offset, y)
            self.screen.blit(card.get_image(), card_position)

        text = f'Hand: {str(self.dealer.show_hand_value())}'
        text_surface = self.font.render(text, True, (255, 255, 255))

        self.screen.blit(dealer_caption, (x, y - 40))
        self.screen.blit(text_surface, (x + 10, y + 150))