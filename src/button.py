import pygame
from typing import Tuple

class Button:
    def __init__(
            self, 
            pos: Tuple[float, float], 
            size: Tuple[float, float], 
            text: str, 
            font: pygame.font.Font,
            color: Tuple[int, int, int] = (255, 255, 255), 
            hover_color: Tuple[int, int, int] = (200, 200, 200),
            border_radius: int = 4
        ):
        self.rect = pygame.Rect(*pos, *size)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.border_radius = border_radius
        self.text_surface = self.font.render(text, True, (0, 0, 0))

    def draw(self, screen: pygame.Surface):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_x, mouse_y) else self.color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=self.border_radius)

        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def is_clicked(self) -> bool:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse_x, mouse_y) and mouse_click[0] == 1
