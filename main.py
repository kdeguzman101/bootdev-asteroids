import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # This code block implements our time-keeping functionality
    game_clock: Clock = pygame.time.Clock()
    dt: float = 0.0

    # Creating the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    # Initializing the ship that the player will control
    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    new_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updatable.update(dt)
        for _ in drawable:
            _.draw(screen)
        pygame.display.flip()
        dt = (game_clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
