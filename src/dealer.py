from .player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__(name="Dealer", is_dealer=True)

    def should_draw(self) -> bool:
        return self.hand_value() < 17

    def __str__(self):
        if len(self.hand) > 1:
            visible_card = f"{self.hand[0].rank} {self.hand[0].suit}"
            return f"Dealer's hand: {visible_card}, [Hidden]"
        return super().__str__()
