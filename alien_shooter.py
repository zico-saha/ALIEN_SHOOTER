import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from stars import Star
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Class to do overall management of game assets and behavior."""

    def __init__(self):
        """Initialization of game and creating game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_caption)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.button = Button(self)
        self.scoreboard = Scoreboard(self)

    def run_game(self):
        """Starts the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()

                self._update_bullet()
                self._remove_bullet()

                self._create_alien_fleet()
                self._upadte_aliens()
                self._remove_alien()

                self._create_stars()
                self._update_stars()
                self._remove_stars()

            self._update_screen()

    def _check_events(self):
        """Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_exit_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Responds to key presses."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            self._game_exit()

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """Starts a new game when player clicks play."""
        button_clicked = self.button.rect_play.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)

            self.stats.reset_stats()
            self.stats.game_active = True
            self._reset()

    def _check_exit_button(self, mouse_pos):
        """Exits from the game when player clicks exit."""
        if self.button.rect_exit.collidepoint(mouse_pos):
            self._game_exit()

    def _fire_bullet(self):
        """Creates a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """Updates the bullets position."""
        for bullet in self.bullets.sprites():
            bullet.update()

        self._check_bullet_alien_collision()

    def _remove_bullet(self):
        """Removes the bullets from the list that have gone out of top-edge."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_alien_fleet(self):
        """Creates the fleet of aliens."""
        if self.settings.spawn_counter == 0:
            new_alien = Alien(self)
            self.aliens.add(new_alien)
            self.settings.spawn_counter += 1

        elif self.settings.spawn_counter == self.settings.spawn_timer:
            self.settings.spawn_counter = 0
        else:
            self.settings.spawn_counter += 1

    def _upadte_aliens(self):
        for alien in self.aliens.sprites():
            alien.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _remove_alien(self):
        """Removes the aliens from the list that have gone out of bottom-edge"""
        for alien in self.aliens.copy():
            if alien.rect.top >= self.settings.screen_height:
                self.aliens.remove(alien)
                self.stats.miss_limit -= 1

            if self.stats.miss_limit <= 0:
                self._ship_hit()
                return

    def _create_stars(self):
        """Creates stars in the game."""
        if self.settings.star_counter == 0:
            new_star = Star(self)
            self.stars.add(new_star)
            self.settings.star_counter += 1

        elif self.settings.star_counter == self.settings.star_timer:
            self.settings.star_counter = 0
        else:
            self.settings.star_counter += 1

    def _update_stars(self):
        """Updates each star's position(Moves downward)."""
        for star in self.stars.sprites():
            star.update()

    def _remove_stars(self):
        """Removes stars in the list that have gone off the edge."""
        for star in self.stars.copy():
            if star.rect.top >= self.settings.screen_height:
                self.stars.remove(star)

    def _check_bullet_alien_collision(self):
        """Checks for bullet & alien collison, removes them and updates score."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            self.stats.score += self.settings.alien_points
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

    def _ship_hit(self):
        """Responds to ship hit by alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self._reset()
            self.stats.miss_limit = self.settings.miss_limit
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Updates images on the screen, and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        for star in self.stars.sprites():
            star.draw_star()

        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.button.draw_play_button()
            self.button.draw_exit_button()

        pygame.display.flip()

    def _reset(self):
        """Resets the game screen."""
        self.aliens.empty()
        self.bullets.empty()

        self.ship.center_ship()
        self._create_alien_fleet()
        self.scoreboard.prep_score()

    def _game_exit(self):
        """Save the high score and exits from game."""
        self.stats.save_high_score()
        sys.exit()
