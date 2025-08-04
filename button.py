"""
Alien Invasion
Willa Rose-Cohen
This module handles the button class and all it's functions.
08-03-25
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error. 
    from alien_invasion import AlienInvasion

class Button:
    """A class to build buttons for the game."""

    def __init__(self, game: 'AlienInvasion', msg):
        """Initialize button attributes."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Set the dimensions and properties of the button.
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0,0, self.settings.button_width, 
            self.settings.button_height)
        self.rect.center = self.boundaries.center

        # The button only needs to be prepped once. 
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, 
            self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw a blank button then draw message."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_position):
        """Check if the button's been clicked."""
        return self.rect.collidepoint(mouse_position)
