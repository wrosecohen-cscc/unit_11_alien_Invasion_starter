"""
Alien Invasion
Willa Rose-Cohen
This module handles the HUD class and all it's functions.
08-03-25
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error. 
    from alien_invasion import AlienInvasion

class HUD:
    """A class to manage and render the game's heads-up display (HUD)."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize HUD elements and references."""
        # References to game, settings, screen, and statistics
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats

        # Font for text rendering
        self.font = pygame.font.Font(
            self.settings.font_file, self.settings.HUD_font_size
        )
        self.padding = 20

        # Initialize score, life image, and level display
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def update_scores(self):
        """Refresh the current, max, hi-score, and level displays."""
        self._update_max_score()
        self.update_score()
        self._update_hi_score()
        self.update_level()

    def _setup_life_image(self):
        """Prepare the ship image to be used as life icons."""
        # Load and scale ship image for life indicators
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image, (self.settings.ship_width / 2, self.settings.ship_height / 2)
        )
        self.life_rect = self.life_image.get_rect()

    def update_score(self):
        """Update current score display and position."""
        # Update current score text and position
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.font.render(
            score_str, True, self.settings.text_color, None
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        """Update session max score display and position."""
        # Update max score text and position
        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(
            max_score_str, True, self.settings.text_color, None
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        """Update all-time high score display and position."""
        # Update hi-score text and position (all-time best)
        hi_score_str = f"Hi-Score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.font.render(
            hi_score_str, True, self.settings.text_color, None
        )
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def _draw_lives(self):
        """Draw remaining lives using ship icons in the bottom-left corner."""
        # Draw remaining ships as life icons in the bottom-left corner
        current_x = self.padding
        current_y = self.boundaries.bottom - self.life_rect.height - self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def update_level(self):
        """Update level display and position in top-left."""
        # Update level text and position (moved to top-left)
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(
            level_str, True, self.settings.text_color, None
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.padding

    def draw(self):
        """Draw all HUD elements to the screen."""
        # Draw all HUD elements
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()