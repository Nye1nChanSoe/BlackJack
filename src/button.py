import pygame
from pygame import Surface, Rect
from typing import Tuple

class Button:
    def __init__(self, text: str, position: Tuple[float, float], width: float, height: float, color: Tuple[float, float, float], text_color: Tuple[float, float, float]):
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)  # Default font
        self.rect = Rect(position, (width, height))

    def draw(self, screen: Surface) -> None:
        # Draw the button
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos: tuple) -> bool:
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered(pygame.mouse.get_pos()):
                return True
        return False
