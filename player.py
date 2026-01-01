import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Facing upwards initially
        # in the Player class
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), LINE_WIDTH)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

        
    def rotate_right(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def rotate_left(self, dt):
        self.rotation -= PLAYER_TURN_SPEED * dt

    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity = direction * PLAYER_SPEED * dt
        self.position += self.velocity
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate_left(dt)
        if keys[pygame.K_d]:
            self.rotate_right(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    




