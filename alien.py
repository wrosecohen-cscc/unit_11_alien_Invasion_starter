import pygame

from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error.
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """A class to manage aliens."""

    def __init__(self, game: 'AlienInvasion', x: float , y: float):
        """Create an alien object at the _____ position."""
        super().__init__()

        self.game = game
        self.screen = game.screen
        self.boundries = game.screen.get_rect()
        self.settings = game.settings

        # Load the bullet.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_width, self.settings.alien_height)    
        )

        # Create an alien rect at (0,0) and then set correct position. 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

        # Store the alien's position as a float.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.y += self.settings.fleet_drop_speed

        self.x += temp_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self) -> bool:
        "Switch direction when edge is hit."
        return(self.rect.right >= self.boundries.right or self.rect.left <= self.boundries.left)
    

    def draw_alien(self):
        """Draw the alien to the screen."""
        self.screen.blit(self.image, self.rect)