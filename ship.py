"""
Alien Invasion
Willa Rose-Cohen
This module handles the ship class and all it's functions.
08-03-25
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import arsenal and alien_invasion while avoiding circular logic error.
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """A class to manage the ship."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load the ship.
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_width, self.settings.ship_height)
            )
        
        # Get ship's rect.
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self._center_ship()

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        # Store a float for the ship's exact horizontal position. 
        self.x = float(self.rect.x)

        # Set up arsenal.
        self.arsenal = arsenal

    def _center_ship(self):
        """Centers the ship."""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ships position and all active bullets."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()
    
    def _update_ship_movement(self) -> None:
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, ot the rect.
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        elif self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        # Update rect object from self.x.
        self.rect.x = self.x
    

    def draw(self) -> None:
        """Draw the ship at its current location."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Attempt to fire a bullet; returns True if a bullet was fired successfully."""
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        """Check if colliding with any sprite, """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False