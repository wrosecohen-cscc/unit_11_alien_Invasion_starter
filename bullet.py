"""
Alien Invasion
Willa Rose-Cohen
This module handles the bullet class and all it's functions.
08-03-25
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error.
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet.
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_width, self.settings.bullet_height)    
        )

        # Create a bullet rect at (0,0) and then set correct position. 
        self.rect = self.image.get_rect()
        self.rect.midtop = self.game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up on the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y 

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)