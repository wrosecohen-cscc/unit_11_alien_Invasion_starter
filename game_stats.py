#from pathlib import Path
from typing import TYPE_CHECKING
import json

if TYPE_CHECKING:
    # Import alien_invasion while avoiding circular logic error. 
    from alien_invasion import AlienInvasion

class GameStats():
    """Tracks game statistics for Alien Invasion including lives, scores and levels."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize stats and load persistent highscore."""
        # Reference to settings and game.
        self.game = game
        self.settings = game.settings

        # Highest score across any session (Non-resettable)
        self.max_score = 0

        # Load saved high score or create new file.
        self.init_saved_score = 0

        # Statistics that reset after each session.
        self.remaining_ships = self.settings.starting_ship_count

    def init_saved_scores(self):
        """Read saved high score from disk or initialize it."""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 80:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get("high_score", 0)
        else:
            self.high_score = 0
            self.save_scores()

    def save_scores(self):
        """Write high score to file."""
        scores = {
            'high_score': self.high_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def reset_stats(self):
        """Reset dynamic stats for new session."""
        self.remaining_ships = self.settings.starting_ship_count
        self.score = 0 
        self.level = 1

    def update(self, collisions):
        """Update score and high score after collisions."""
        self._update_score(collisions)
        self._update_max_score()
        self._update_high_score()

    def _update_max_score(self):
        """Update session's max score."""
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')
        
    def _update_high_score(self):
        """Update and save hi-score if current score exceeds it."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_scores()

    def _update_score(self, collisions):
        """Increase score based on number of collisions."""
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        """Advance to next level."""
        self.level += 1