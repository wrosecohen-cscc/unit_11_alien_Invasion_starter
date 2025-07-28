from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error. 
    from alien_invasion import AlienInvasion

class GameStats():
    """Track Statistics for Alien Invasion."""

    def __init__(self, game: 'AlienInvasion'):
        """Initial game stats."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.remaining_ships = self.settings.starting_ship_count

    def reset_stats(self):
        """Comment."""
        self.remaining_ships = self.settings.starting_ship_count
        self.score = 0 
        self.level = 1

    def update(self, collisions):
        """Comment."""
        # Update score.
        self._update_score(collisions)

        # Update max_score.
        self._update_max_score()

        # Update high_score.


    def _update_max_score(self):
        """Comment."""
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')
        

    def _update_score(self, collisions):
        """Comment."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Basic: {self.score}')

    def update_level(self):
        """Comment."""
        self.level += 1
        #print(self.level)




