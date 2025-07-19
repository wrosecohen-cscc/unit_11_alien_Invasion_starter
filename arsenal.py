import pygame

from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error. 
    from alien_invasion import AlienInvasion

class Arsenal:
    """A class to manage the ship's arsenal of bullets."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the Arsenal with game settings and create a group to store bullets."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update the position of all active bullets and remove any that are offscreen."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Remove bullets once they leave the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets currently in the arsenal to the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self):
        """Fire a bullet if under the limit; return True if successful."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    