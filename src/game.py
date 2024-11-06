from .deck import Deck
from .player import Player
from .dealer import Dealer
from .button import Button
from typing import List
import pygame
import random

class Game:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font, debug: bool):
        self.screen = screen
        self.font = font
        self.deck = Deck()
        self.player = Player('Nyein Chan')
        self.dealer = Dealer()
        self.debug_mode = debug

        self.player_turn = True
        self.dealer_turn = False
        self.game_over = False
        self.player_won = False

        self.game_result = ''

        self.hit_button = Button((560, 500), (80, 40), "Hit", self.font)
        self.stand_button = Button((660, 500), (80, 40), "Stand", self.font)

        self.random_no_of_cards = random.randint(10, 14)
        self.random_offsets_x = [random.randint(-5, 5) for _ in range(self.random_no_of_cards)]
        self.random_offsets_y = [random.randint(-5, 5) for _ in range(self.random_no_of_cards)]
        self.random_rotates = [random.randint(-12, 12) for _ in range(self.random_no_of_cards)]

        self.init_deck()
        self.init_player()
        self.init_dealer()

        self.check_initial_blackjack()

    def init_deck(self):
        self.deck.shuffle()

    def init_player(self):
        self.player.hit(self.deck.draw())
        self.player.hit(self.deck.draw())

    def init_dealer(self):
        self.dealer.hit(self.deck.draw())
        self.dealer.hit(self.deck.draw().flip())

    def check_initial_blackjack(self):
        if self.player.hand_value() == 21:
            self.game_over = True
            self.player_won = True
            self.game_result = "Blackjack!"

    def update(self, events: List[pygame.event.Event]):
        for event in events:
            if self.debug_mode:
                print(event)

            if event.type == pygame.KEYDOWN:
                # Restart the game when 'R' is pressed
                if event.key == pygame.K_r and self.game_over:
                    self.reset()

            if not self.game_over:
                self.update_player(event)
                self.update_dealer(event)

    def render(self):
        self.render_player_hands()
        self.render_dealer_hands()

        if self.player_turn:
            self.hit_button.draw(self.screen)
            self.stand_button.draw(self.screen)

        self.render_deck_stack()

        if self.game_over:
            if self.player_won:
                result_color = (0, 255, 0)
            elif "Tie" in self.game_result:
                result_color = (255, 255, 0)
            else:
                result_color = (255, 0, 0)

            result_surface = self.font.render(self.game_result, True, result_color)
            text_width = result_surface.get_width()
            screen_center_x = self.screen.get_width() // 2
            centered_x = screen_center_x - (text_width // 2)
            self.screen.blit(result_surface, (centered_x, self.screen.get_height() // 2 - 20))

            # Display message to restart
            restart_message = self.font.render("Press 'R' to restart", True, (255, 255, 255))
            restart_message_width = restart_message.get_width()
            self.screen.blit(restart_message, (screen_center_x - (restart_message_width // 2), self.screen.get_height() // 2 + 20))

    def update_player(self, event: pygame.event.Event):
        if self.player_turn and not self.game_over:
            if self.debug_mode:
                print(self.player)

            if self.hit_button.is_clicked(event):
                if len(self.player.hand) < 5:
                    self.player.hit(self.deck.draw())
                    if self.player.hand_value() > 21:
                        self.game_over = True
                        self.player_won = False
                        self.game_result = "Busted!"
                    elif len(self.player.hand) == 5 and self.player.hand_value() <= 21:
                        # Player has 5 cards and didn't bust
                        self.game_over = True
                        self.player_won = True
                        self.game_result = "5-Card Charlie!"
            # Player stands
            if self.stand_button.is_clicked(event):
                self.player_turn = False
                self.dealer_turn = True

    def update_dealer(self, event: pygame.event.Event):
        if self.dealer_turn and not self.game_over:
            if self.debug_mode:
                print(self.dealer)

            if len(self.dealer.hand) < 5 and self.dealer.should_draw():
                self.dealer.hit(self.deck.draw().flip())
            elif len(self.dealer.hand) == 5 and self.dealer.hand_value() <= 21:
                self.game_over = True
                self.player_won = False
                self.game_result = "You Lose!"

            if not self.dealer.should_draw():
                self.dealer_turn = False
                self.compare_hands()

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
            if self.game_over and card.is_hidden:
                card.flip()
            card_position = (x + i * card_offset, y)
            self.screen.blit(card.get_image(), card_position)

        text = f'Hand: {str(self.dealer.show_hand_value())}'
        text_surface = self.font.render(text, True, (255, 255, 255))

        self.screen.blit(dealer_caption, (x, y - 40))
        self.screen.blit(text_surface, (x + 10, y + 150))

    def render_deck_stack(self):
        x, y = 660, 140
        image = pygame.image.load('assets/cards/cardback.png').convert_alpha()
        deck_caption = self.font.render(f"Deck: {len(self.deck)}", True, (255, 255, 255))
        for i in range(self.random_no_of_cards):
            random_offset_x = self.random_offsets_x[i]
            random_offset_y = self.random_offsets_y[i]
            random_rotations = self.random_rotates[i]
            rotated_image = pygame.transform.rotozoom(image, random_rotations, 1)
            rotated_rect = rotated_image.get_rect(center=(x + random_offset_x, y + random_offset_y + i * 2))
            self.screen.blit(rotated_image, rotated_rect.topleft)
        self.screen.blit(deck_caption, (x - 40, y - 114))

    # compare dealer and player's hand
    def compare_hands(self):
        player_hand_value = self.player.hand_value()
        dealer_hand_value = self.dealer.hand_value()

        if dealer_hand_value > 21:
            self.game_over = True
            self.player_won = True
            self.game_result = "Dealer Busted! You Win!"
        elif player_hand_value > dealer_hand_value:
            self.game_over = True
            self.player_won = True
            self.game_result = "You Win!"
        elif player_hand_value < dealer_hand_value:
            self.game_over = True
            self.player_won = False
            self.game_result = "You Lose!"
        else:
            self.game_over = True
            self.game_result = "It's a Tie!"

    def reset(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.player_turn = True
        self.dealer_turn = False
        self.game_over = False
        self.player_won = False
        self.random_no_of_cards = random.randint(10, 14)
        self.random_offsets_x = [random.randint(-5, 5) for _ in range(self.random_no_of_cards)]
        self.random_offsets_y = [random.randint(-5, 5) for _ in range(self.random_no_of_cards)]
        self.random_rotates = [random.randint(-12, 12) for _ in range(self.random_no_of_cards)]
        self.game_result = ''
        self.deck.reset()
        self.init_deck()
        self.init_player()
        self.init_dealer()
