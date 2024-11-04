import pygame
from pygame import Surface
import time

class CardRenderer:
    def __init__(self, face_up_image: Surface, face_down_image: Surface, flip_duration: float = 0.65):
        self.face_up_image = face_up_image
        self.face_down_image = face_down_image
        self.flip_duration = flip_duration


    def render(self, screen: Surface, x: int, y: int, face_up: bool) -> None:
        image = self.face_up_image if face_up else self.face_down_image
        screen.blit(image, (x, y))


    def render_flip_animation(self, screen: Surface, x: int, y: int, face_up: bool) -> None:
        start_time = time.time()
        end_time = start_time + self.flip_duration
        original_width = self.face_up_image.get_width()
        original_height = self.face_up_image.get_height()

        while time.time() < end_time:
            elapsed_time = time.time() - start_time
            progress = elapsed_time / self.flip_duration
            scale_factor = 1 - abs(progress - 0.5) * 2  # Scale from 1 to 0 and back to 1

            # Calculate the current width of the card during the flip
            current_width = int(original_width * scale_factor)
            if current_width == 0:
                current_width = 1

            scaled_image = pygame.transform.scale(
                self.face_up_image if face_up else self.face_down_image,
                (current_width, original_height)
            )

            screen.fill((0, 128, 0), pygame.Rect(x, y, original_width, original_height))
            screen.blit(scaled_image, (x + (original_width - current_width) // 2, y))
            pygame.display.flip()

