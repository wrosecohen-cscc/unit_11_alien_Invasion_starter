"""
Alien Invasion
Willa Rose-Cohen
This program is a modified version of the Alien Invasion game.
08-03-25
"""

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from HUD import HUD


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        "Initialize the game, and create game resources."
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_width, self.settings.screen_height)
            )

        # Start screen image
        self.start_screen = pygame.image.load(self.settings.start_page_file)
        self.start_screen = pygame.transform.scale(self.start_screen, (self.settings.screen_width, self.settings.screen_height))


        # Define clickable play button area (match this to the real button location inside the image)
        self.play_button_rect = pygame.Rect(481, 551, 239, 52)
        
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.HUD = HUD(self)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        self.play_button = Button(self, 'Play')
        self.game_active = False

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """Check for all in-game collisions and apply effects."""
        # Check ship-alien collisions.
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

            # Subtact one life.

        # Check collisions for aliens and bottom of screen.
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        # Check collisions of projectiles and aliens.
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        # If all aliens are destroyed, begin next level.
        if self.alien_fleet.check_destroyed_status():
            self._next_level()

    def _next_level(self):
        """Advance to the next level by resetting and increasing difficulty."""
        self.settings.increase_difficulty()
        self._reset_level()
        self.game_stats.update_level()
        self.HUD.update_scores()

    def _check_game_status(self):
        """Update game status after a collision or end of level."""
        self.game_stats.remaining_ships -= 1
        if self.game_stats.remaining_ships > 0:
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self):
        """Clear bullets and aliens, then create new fleet."""
        # Reset arsenal and alien fleet.
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        
        # Recreate alien fleet.
        self.alien_fleet.create_random_fleet()

    def restart_game(self):
        """Reset all dynamic settings and stats to start a new game."""
        # Initialize dynamic settings.
        self.settings.initialize_dynamic_settings()

        # Reset Game stats.
        self.game_stats.reset_stats()

        # Update HUD scores.
        self.HUD.update_scores()

        # Reset level.
        self._reset_level()

        # Recenter the ship.
        self.ship._center_ship()

        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Draw background and all elements.
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()

        # Draw HUD.
        self.HUD.draw()

        # Draw start screen and play button if game is inactive.
        if not self.game_active:
            self.screen.blit(self.start_screen, (0, 0))
            pygame.mouse.set_visible(True)
        pygame.display.flip()

    def _check_events(self):
        """Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """When play button is clicked, start a new game."""
        mouse_position = pygame.mouse.get_pos()
        if self.play_button_rect.collidepoint(mouse_position):
            self.restart_game()

    def _check_keydown_events(self, event) -> None:
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
    
    def _check_keyup_events(self, event) -> None:
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        

if __name__ == "__main__":
    """Make a game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()