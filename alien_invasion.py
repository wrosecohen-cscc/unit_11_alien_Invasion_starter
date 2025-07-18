import sys
import pygame

class AlienInvasion:
    """Comment"""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.running = True
    
    def run_game(self) -> None:
        # Game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            pygame.display.flip()


if __name__ == "__main__":
    """Test comment"""
    ai = AlienInvasion()
    ai.run_game()
