import random
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Class to manage the stars in the game."""

    def __init__(self, ai_game):
        """Initializes a star object"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.star_color

        self.rect = pygame.Rect(
            0, 0, self.settings.star_width, self.settings.star_height)

        self.rect.x = random.randint(
            0, ai_game.screen.get_width() - self.rect.width)
        self.rect.y = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Updates the star's position."""
        self.y += self.settings.star_speed
        self.rect.y = self.y

    def draw_star(self):
        """Draws the star to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
