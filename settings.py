class Settings:
    """Class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialization of game's settings."""

        # Window settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 70)
        self.game_caption = "Alien Invasion"

        # Button Settings
        self.play_message = "Play"
        self.exit_message = "Exit"

        # Star settings
        self.star_width = 4
        self.star_height = 4
        self.star_color = (255, 255, 255)
        self.star_speed = 0.1
        self.star_timer = 400
        self.star_counter = 0

        # Ship Settings
        self.ship_res = (50, 50)
        self.ship_speed = 0.6
        self.ship_limit = 2

        # Bullet Settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_speed = 0.75
        self.bullet_color = (255, 165, 0)
        self.bullet_allowed = 5

        # Alien Settings
        self.alien_res = (55, 55)
        self.alien_speed = 0.1
        self.spawn_timer = 2000
        self.spawn_counter = 0
        self.miss_limit = 3
        self.alien_points = 10
