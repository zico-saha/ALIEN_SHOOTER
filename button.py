import pygame.font


class Button:
    """Class to handle play button."""

    def __init__(self, ai_game):
        """Initializes the button attributes."""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 160, 40
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.play_button_left = (self.settings.screen_width - self.width) / 2
        self.play_button_top = (
            self.settings.screen_height / 2) - self.height - 5
        self.exit_button_left = (self.settings.screen_width - self.width) / 2
        self.exit_button_top = (self.settings.screen_height / 2) + 5

        self.rect_play = pygame.Rect(
            self.play_button_left, self.play_button_top, self.width, self.height)
        self.rect_exit = pygame.Rect(
            self.exit_button_left, self.exit_button_top, self.width, self.height)

        self.play_message = self.settings.play_message
        self.exit_message = self.settings.exit_message

        self._prep_play_message()
        self._prep_exit_message()

    def _prep_play_message(self):
        """Turns play message into a rendered image and centre text on the button."""
        self.play_msg_image = self.font.render(
            self.play_message, True, self.text_color, self.button_color)
        self.play_msg_image_rect = self.play_msg_image.get_rect()
        self.play_msg_image_rect.center = self.rect_play.center

    def _prep_exit_message(self):
        """Turns exit message into a rendered image and centre text on the button."""
        self.exit_msg_image = self.font.render(
            self.exit_message, True, self.text_color, self.button_color)
        self.exit_msg_image_rect = self.exit_msg_image.get_rect()
        self.exit_msg_image_rect.center = self.rect_exit.center

    def draw_play_button(self):
        """Draw blank button for play and then draw message."""
        self.screen.fill(self.button_color, self.rect_play)
        self.screen.blit(self.play_msg_image, self.play_msg_image_rect)

    def draw_exit_button(self):
        """Draw blank button for exit and then draw message."""
        self.screen.fill(self.button_color, self.rect_exit)
        self.screen.blit(self.exit_msg_image, self.exit_msg_image_rect)
