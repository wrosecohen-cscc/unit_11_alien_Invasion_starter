from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        self.name: str = 'Alien Invasion'
        self.difficulty_scale = 1.1

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Ship settings.
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width = 40
        self.ship_height = 60

        # Bullet settings.
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
       
        # Alien settings.
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_width = 40
        self.alien_height = 40

        # Fleet settings.
        self.fleet_direction = 1
        
        # Button settings.
        self.button_width = 200
        self.button_height = 50
        self.button_color = (76, 41, 0)

        # Font settings.
        self.text_color = (255, 255, 255)
        self.button_font_size = 40
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        """Initialize the game's dynamic settings."""
        # Ship settings.
        self.ship_speed = 5
        self.starting_ship_count = 3

        # Bullet settings.
        self.bullet_speed = 7
        self.bullet_amount = 5
        self.bullet_width = 25
        self.bullet_height = 88

        # Fleet settings.
        self.fleet_speed = 2
        self.fleet_drop_speed = 40

        # Scoring settings. 
        self.alien_points = 50 


    def increase_difficulty(self):
        """Increase the difficulty of the game."""
        # Ship settings.
        self.ship_speed *= self.difficulty_scale

        # Bullet settings. 
        self.bullet_speed *= self.difficulty_scale

        # Fleet settings.
        self.fleet_speed *- self.difficulty_scale


       
