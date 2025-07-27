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
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height

        fleet_width, fleet_height = self.calculate_fleet_size(alien_width, screen_width, alien_height, screen_height)
        x_offset, y_offset = self.calculate_offsets(alien_width, alien_height, screen_width, fleet_width, fleet_height)

        self._create_rectangle_fleet(alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset):
        """Comment."""
        for row in range(fleet_height):
            for col in range(fleet_width):
                current_x = alien_width * col + x_offset
                current_y = alien_height * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_width, alien_height, screen_width, fleet_width, fleet_height):
        """Comment."""
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_space = fleet_width * alien_width
        fleet_vertical_space = fleet_height * alien_height
        x_offset = int((screen_width - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset,y_offset




    def calculate_fleet_size(self, alien_width, screen_width, alien_height, screen_height):
        """Calculate the fleet size."""
        fleet_width = (screen_width // alien_width)
        fleet_height = ((screen_height / 2) // alien_height)

        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2

        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2
        
        return int(fleet_width), int(fleet_height)
    
    def _create_alien(self, current_x: int, current_y: int):
        """Comment."""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        alien: Alien
        """Delegate down to all the other aliens. If they have an edge, drop down."""
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Comment."""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed


    def update_fleet(self):
        """Comment."""
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Comment."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Comment."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False    




