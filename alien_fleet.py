import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:

    def __init__(self, game: 'AlienInvasion'):
        """A class to manage the Alien's fleet."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Comment."""
        alien_width = self.settings.alien_width
        screen_width = self.settings.screen_width

        fleet_width = self.calculate_fleet_size(alien_width, screen_width)

        # half_screen = self.settings.screen_width
        fleet_horizontal_space = fleet_width * alien_width
        x_offset = int((screen_width - fleet_horizontal_space) // 2)

        for col in range(fleet_width):
            current_x = alien_width * col + x_offset
            self._create_alien(current_x, 10)



    def calculate_fleet_size(self, alien_width, screen_width):
        """Comment."""
        fleet_width = (screen_width // alien_width)

        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2
        
        return fleet_width
    
    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def draw(self):
        """Comment."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()


        




