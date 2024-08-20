import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    # initialize pygame
    pygame.init()
    # initialize fps lock
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.is_colliding(player):
                print("Game over!")
                return
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(0) / 1000



        


if __name__ == "__main__":
    main()