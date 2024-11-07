from .deck import Deck
from .player import Player
from .dealer import Dealer
from .button import Button
from typing import List
import pygame
import random

# TODO: separate rendering logic to renderer class (optional)
# TODO: card flip animation at the game end
# TODO: card draw animation for player and dealer
class Game:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font, debug: bool):
        self.screen = screen
        self.font = font
        self.deck = Deck()
        self.player = Player('Player')
        self.dealer = Dealer()
        self.debug_mode = debug

        self.player_turn = True
        self.dealer_turn = False
        self.game_over = False
        self.player_won = False

        self.game_result = ''
        self.win = 0
        self.lose = 0

        self.hit_button = Button((340, 550), (80, 36), "Hit", self.font)
        self.stand_button = Button((440, 550), (80, 36), "Stand", self.font)

        self.init_deck()
        self.init_player()
        self.init_dealer()

        self.check_initial_blackjack()

        self.is_shuffled = False
        self.shuffle_frames = 10
        self.shuffle_frame_counter = 0
        self.random_no_of_cards = 10
        self.random_offsets_x = [0] * self.random_no_of_cards
        self.random_offsets_y = [0] * self.random_no_of_cards
        self.random_rotates = [0] * self.random_no_of_cards


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
            self.win += 1

    def update(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.reset()
            if not self.game_over and self.player_turn:
                self.update_player(event)
            else:
                self.update_dealer(event)

    def render(self):
        if not self.is_shuffled:
            self.render_shuffle()
        else:
            self.render_deck_stack()
            self.render_player_hands()
            self.render_dealer_hands()
            if self.player_turn and not self.game_over:
                self.hit_button.draw(self.screen)
                self.stand_button.draw(self.screen)
        if self.game_over:
            self.render_game_result()
        self.render_score()

    def update_player(self, event: pygame.event.Event):
        if self.hit_button.is_clicked(event) and len(self.player.hand) < 5:
            self.player.hit(self.deck.draw())
            player_value = self.player.hand_value()

            if player_value == 21:
                self.end_game("Blackjack!", True)
            elif player_value > 21:
                self.end_game("Busted!", False)
            elif len(self.player.hand) == 5 and player_value <= 21:
                self.end_game("5-Card Charlie!", True)

        if self.stand_button.is_clicked(event):
            self.player_turn = False
            self.dealer_turn = True

    def update_dealer(self, event: pygame.event.Event):
        if self.dealer_turn and not self.game_over:
            if self.debug_mode:
                print(self.dealer)
            dealer_value = self.dealer.hand_value()
            if len(self.dealer.hand) < 5 and self.dealer.should_draw():
                self.dealer.hit(self.deck.draw().flip())
            elif len(self.dealer.hand) == 5 and dealer_value <= 21:
                self.end_game("You Lose!", False)
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

    def render_shuffle(self):
        x, y = 660, 140
        image = pygame.image.load('assets/cards/cardback.png').convert_alpha()
        if self.shuffle_frame_counter < self.shuffle_frames:
            for i in range(self.random_no_of_cards):
                self.random_offsets_x[i] = random.randint(-30, 30)
                self.random_offsets_y[i] = random.randint(-10, 30)
                self.random_rotates[i] = random.randint(-20, 20)
                rotated_image = pygame.transform.rotozoom(image, self.random_rotates[i], 1)
                rotated_rect = rotated_image.get_rect(center=(x + self.random_offsets_x[i], y + self.random_offsets_y[i] + i * 2))
                self.screen.blit(rotated_image, rotated_rect.topleft)
            deck_caption = self.font.render(f"Shuffling...", True, (255, 255, 255))
            self.screen.blit(deck_caption, (x - 40, y - 114))
            self.shuffle_frame_counter += 1
        else:
            self.is_shuffled = True

    def render_deck_stack(self):
        x, y = 660, 140
        image = pygame.image.load('assets/cards/cardback.png').convert_alpha()
        deck_caption = self.font.render(f"Deck: {len(self.deck)}", True, (255, 255, 255))

        # Use the final shuffled positions and rotations
        for i in range(self.random_no_of_cards):
            random_offset_x = self.random_offsets_x[i]
            random_offset_y = self.random_offsets_y[i]
            random_rotation = self.random_rotates[i]
            rotated_image = pygame.transform.rotozoom(image, random_rotation, 1)
            rotated_rect = rotated_image.get_rect(center=(x + random_offset_x, y + random_offset_y + i * 2))
            self.screen.blit(rotated_image, rotated_rect.topleft)

        self.screen.blit(deck_caption, (x - 40, y - 114))

    def render_game_result(self):
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

    def render_score(self):
        # Render the win and lose tally in the bottom-right corner
        score_text = f"Wins: {self.win}  |  Losses: {self.lose}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        score_rect = score_surface.get_rect(bottomright=(self.screen.get_width() - 30, self.screen.get_height() - 20))
        self.screen.blit(score_surface, score_rect)

    # compare dealer and player's hand
    def compare_hands(self):
        player_hand_value = self.player.hand_value()
        dealer_hand_value = self.dealer.hand_value()

        if dealer_hand_value > 21:
            self.game_over = True
            self.player_won = True
            self.game_result = "Dealer Busted! You Win!"
            self.win += 1
        elif player_hand_value > dealer_hand_value:
            self.game_over = True
            self.player_won = True
            self.game_result = "You Win!"
            self.win += 1
        elif player_hand_value < dealer_hand_value:
            self.game_over = True
            self.player_won = False
            self.game_result = "You Lose!"
            self.lose += 1
        else:
            self.game_over = True
            self.game_result = "It's a Tie!"

    def end_game(self, result: str, player_won: bool):
        self.game_over = True
        self.player_won = player_won
        self.game_result = result
        if player_won:
            self.win += 1
        else:
            self.lose += 1

    def reset(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.player_turn = True
        self.dealer_turn = False
        self.game_over = False
        self.player_won = False
        self.game_result = ''
        self.deck.reset()
        self.init_deck()
        self.init_player()
        self.init_dealer()

        self.is_shuffled = False
        self.shuffle_frames = 10
        self.shuffle_frame_counter = 0
        self.random_no_of_cards = 10
        self.random_offsets_x = [0] * self.random_no_of_cards
        self.random_offsets_y = [0] * self.random_no_of_cards
        self.random_rotates = [0] * self.random_no_of_cards

