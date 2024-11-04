import pygame
import sys
from src.card import Card
from src.card_renderer import CardRenderer
from src.button import Button

pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Card with Renderer and Flip Animation")

face_up_image = pygame.image.load('assets/cards/ad.png')
face_down_image = pygame.image.load('assets/cards/cardback.png')

card = Card(
    rank="Ace", 
    suit="Diamond", 
    renderer=CardRenderer(face_up_image, face_down_image),
    face_up=True
)

# Create Buttons
hit_button = Button("Hit", (600, 400), 100, 50, (0, 255, 0), (0, 0, 0))
stand_button = Button("Stand", (600, 470), 100, 50, (255, 0, 0), (255, 255, 255))

running = True
x, y = 350, 225  # Position of the card
while running:
    screen.fill((0, 128, 0))  # Green background (like a card table)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                card.flip(screen, x, y)
        # Handle button events
        if hit_button.is_clicked(event):
            print("Hit button pressed!")  # Placeholder for future logic
        if stand_button.is_clicked(event):
            print("Stand button pressed!")  # Placeholder for future logic

    card.render(screen, x, y)  # Render the card
    hit_button.draw(screen)  # Draw the hit button
    stand_button.draw(screen)  # Draw the stand button
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()