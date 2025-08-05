"""
Alien Invasion
Willa Rose-Cohen
This program is a modified version of the Alien Invasion game.
08-03-25
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship  # If you want to draw icons for lives
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error.
    from alien_invasion import AlienInvasion

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize scorekeeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.game_stats

        # Font settings for score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score image
        self.prep_score()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Position score in top-right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.remaining_ships):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw score and ships to screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)