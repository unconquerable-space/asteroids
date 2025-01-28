import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    ## initialization ##

    # game engine #
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # define groups #
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # assign groups #
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    # instantiate player #
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # instantiate asteroid field #
    asteroid_field = AsteroidField()

    ## main loop ##
    while True:

        # event loop #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update game state #
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

        # update screen #
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # update game clock #
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
