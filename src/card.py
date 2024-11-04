from pygame import Surface
from .card_renderer import CardRenderer

class Card:
    def __init__(self, rank: str, suit: str, renderer: CardRenderer, face_up: bool = True):
        self.rank: str = rank
        self.suit: str = suit
        self.renderer = renderer
        self.face_up: bool = face_up

    def val(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            # Ace's value can be 1 or 11 depending on the game logic later
            return 11
        else:
            return int(self.rank)

    def is_face_up(self) -> bool:
        return self.face_up

    def render(self, screen: Surface, x: int, y: int) -> None:
        self.renderer.render(screen, x, y, self.face_up)

    def flip(self, screen: Surface, x: int, y: int) -> None:
        self.face_up = not self.face_up
        self.renderer.render_flip_animation(screen, x, y, self.face_up)

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}" if self.face_up else "Card is face down"

    def __repr__(self) -> str:
        return f"Card(rank={self.rank}, suit={self.suit}, value={self.value}, face_up={self.face_up})"
