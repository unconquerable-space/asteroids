import pygame
from circleshape import *
from shot import *
from constants import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return

        shot = Shot(self.position.x, self.position.y) 
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):

        ## key events ##
        keys = pygame.key.get_pressed()

        # [A] was pressed #
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        # [D] was pressed #
        if keys[pygame.K_d]:
            self.rotate(dt)

        # [W] was pressed #
        if keys[pygame.K_w]:
            self.move(dt)

        # [S] was pressed #
        if keys[pygame.K_s]:
            self.move(dt * -1)

        # [SPACE] was pressed #
        if keys[pygame.K_SPACE]:
            self.shoot()

        ## cooldown ##
        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)


    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2) 

