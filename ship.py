import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    """A class to manage the ship."""

    def __init__(self, game: 'AlienInvasion') -> None:
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
        self.rect.midbottom = self.boundaries.midbottom

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        # Store a float for the ship's exact horizontal position. 
        self.x = float(self.rect.x)


    def update(self) -> None:
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, ot the rect.
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        elif self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        # Update rect onject from self.x.
        self.rect.x = self.x
    

    def draw(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)