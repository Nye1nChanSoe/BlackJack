import pygame
from typing import List
from .card import Card

class DeckRenderer:
    def __init__(self, card_back_image, screen: pygame.Surface, shuffle_duration: float = 1.0):
        self.card_back_image = card_back_image
        self.screen = screen
        self.shuffle_duration = shuffle_duration
        self.card_x = 570  # Constant for card x-position
        self.card_y = 100   # Constant for card y-position
        self.steps = 20     # Total animation steps for shuffle
        self.stack_size_multiplier = 0.25  # Multiplier for card stacking

    def render_stack(self, total_cards: int = 52):
        for i in range(total_cards):
            self.screen.blit(self.card_back_image, (self.card_x, self.card_y + i * self.stack_size_multiplier))
        pygame.display.flip()

    def render_shuffle(self):
        self.shuffled_positions = []  # Clear previous shuffle positions
        for step in range(self.steps):
            progress = step / self.steps
            self.screen.fill((0, 128, 0))  # Clear screen
            for i in range(5):
                offset_x = int(20 * (i + 1) * progress)
                offset_y = int(5 * (i + 1) * progress)
                new_x = self.card_x + offset_x if i % 2 == 0 else self.card_x - offset_x
                new_y = self.card_y + offset_y
                self.screen.blit(self.card_back_image, (new_x, new_y))
                if step == self.steps - 1:
                    self.shuffled_positions.append((new_x, new_y))
            pygame.display.flip()
            pygame.time.wait(30)
        self._return_cards_to_deck()

    def _return_cards_to_deck(self):
        for step in range(self.steps):
            progress = step / self.steps
            self.screen.fill((0, 128, 0))
            for i, start_pos in enumerate(self.shuffled_positions):
                x = int(start_pos[0] * (1 - progress) + self.card_x * progress)
                y = int(start_pos[1] * (1 - progress) + self.card_y * progress)
                self.screen.blit(self.card_back_image, (x, y))
            pygame.display.flip()
            pygame.time.wait(30)

    def render_draw(self, card: Card, position=(400, 300)):
        """Render the draw animation for a card."""
        start_pos = (self.card_x, self.card_y)  # Start drawing from the deck's position
        end_pos = position  # Where the card will be placed after drawing

        for step in range(20):
            t = step / 20  # Animation progress (from 0 to 1)
            x = int(start_pos[0] * (1 - t) + end_pos[0] * t)
            y = int(start_pos[1] * (1 - t) + end_pos[1] * t)

            self.screen.fill((0, 128, 0))  # Clear the screen
            self.screen.blit(self.card_back_image, (x, y))  # Draw the card at interpolated position
            pygame.display.flip()
            pygame.time.wait(50)  # Slow down the animation for visual effect

    def render_reset(self, cards: List[Card]):
        """Render deck reset by stacking the cards back on the deck."""
        self.screen.fill((0, 128, 0))  # Green background
        self.render_stack(len(cards))  # Re-render the full stack
        pygame.display.flip()
