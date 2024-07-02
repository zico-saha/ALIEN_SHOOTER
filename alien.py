import random
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialization of the alien and setting its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.alien_size = self.settings.alien_res

        self.image = pygame.image.load("images\_alien_ship.bmp")
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, self.alien_size)
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(
            0, ai_game.screen.get_width() - self.rect.width)
        self.rect.y = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update's the alien-ship's position(moves downward)."""
        self.y += self.settings.alien_speed
        self.rect.y = self.y
