import pygame
from constants import *
from player import *

def main():

    # initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(player.position)

    while True:

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update game state
        player.update(dt)

        # draw and update game clock
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
