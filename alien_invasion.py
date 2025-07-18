import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        "Initialize the game and create game resources."
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_width, self.settings.screen_height)
            )
        
        self.running = True
        self.clock = pygame.time.Clock()

        # Create ship
        self.ship =Ship(self)


    
    def run_game(self) -> None:
        """Start the main loop for the game."""
        while self.running:
            self._check_events()

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    """Make a game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()
