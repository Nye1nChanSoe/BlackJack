import pygame
from src.deck import Deck
from src.deck_renderer import DeckRenderer

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Card Game')

    # Load card back image
    card_back_image = pygame.image.load('assets/cards/cardback.png')

    # Create deck and renderer
    renderer = DeckRenderer(card_back_image=card_back_image, screen=screen)
    deck = Deck(renderer)

    # Main game loop
    running = True
    while running:
        screen.fill((0, 128, 0))  # Green background

        deck.render()  # Render the deck's stack of cards

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    # Shuffle deck and show shuffle animation
                    deck.shuffle()
                elif event.key == pygame.K_d:
                    # Draw a card and show draw animation
                    if not deck.is_empty():
                        deck.draw()

        pygame.display.flip()  # Update display after each frame

    pygame.quit()

if __name__ == '__main__':
    main()
