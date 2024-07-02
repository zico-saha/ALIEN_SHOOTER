import pygame


class Ship:
    """Class to manage the ship's properties and action."""

    def __init__(self, ai_game):
        """Initialization of ship and setting its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()
        self.ship_size = self.settings.ship_res

        self.image = pygame.image.load("images\_space_ship.bmp")
        self.image = pygame.transform.scale(self.image, self.ship_size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on movement flag."""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >= 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draws the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centre the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
