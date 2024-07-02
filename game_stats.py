class GameStats:
    """Tracks game statistics in Alien Invasion."""

    def __init__(self, ai_game):
        """Initializes statistics."""
        self.settings = ai_game.settings
        self.miss_limit = self.settings.miss_limit
        self.game_active = False
        self.score = 0
        self.high_score = 0

        self.load_high_score()
        self.reset_stats()

    def reset_stats(self):
        """Initializes statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.miss_limit = self.settings.miss_limit
        self.save_high_score()
        self.score = 0

    def load_high_score(self):
        """Loads the highest score earned in the previous games."""
        try:
            with open("high_score.txt", 'r') as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        """Saves the highest score into a file."""
        if self.score >= self.high_score:
            with open("high_score.txt", 'w') as file:
                file.write(str(self.score))
