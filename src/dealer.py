from .player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__(name="Dealer", is_dealer=True)

    def should_draw(self) -> bool:
        return self.hand_value() < 17

    def show_hand_value(self) -> int:
        value = 0
        ace_count = 0

        for card in self.hand:
            if card.is_hidden:
                continue
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

    def __str__(self):
        if len(self.hand) > 1:
            visible_card = f"{self.hand[0].rank} {self.hand[0].suit}"
            return f"Dealer's hand: {visible_card}, [Hidden]"
        return super().__str__()
