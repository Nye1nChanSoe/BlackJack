from typing import List
from .card import Card

class Player:
    def __init__(self, name: str, is_dealer: bool = False):
        self.name = name
        self.is_dealer = is_dealer
        self.hand: List[Card] = []

    def hit(self, card: Card):
        self.hand.append(card)

    def hand_value(self) -> int:
        value = 0
        ace_count = 0

        for card in self.hand:
            if card.rank.isdigit():
                value += int(card.rank)
            elif card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                ace_count += 1
                value += 11

        # adjust the ace value accordingly
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1

        return value

    def is_busted(self) -> bool:
        return self.hand_value() > 21

    def reset_hand(self):
        self.hand.clear()

    def __str__(self):
        hand_str = ' | '.join([f"{card.rank} {card.suit}" for card in self.hand])
        return f"{self.name}'s hand: {hand_str} (Value: {self.hand_value()})"
