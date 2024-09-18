import pygame
from pyfiglet import figlet_format
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable )
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
    score = 0
    f = open("high_score.txt", "r")
    high_score = int(f.read().strip())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.is_colliding(player):
                if score > high_score:
                    high_score = str(score)
                    f = open("high_score.txt", "w")
                    f.write(high_score)
                    print(figlet_format("\nNEW HIGH SCORE"))

                print("\n\n\n--- GAME OVER !! ---\n\n")

                print("--- SCORE --- \n")
                print(figlet_format(str(score)))

                print("--- HIGH SCORE --- \n")
                print(figlet_format(str(high_score)))

                return
            for s in shots:
                if a.is_colliding(s):
                    s.kill()
                    a.split()
                    score += 1

        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(0) / 1000
     
if __name__ == "__main__":
    main()
