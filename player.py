from circleshape import *
from constants import *
from shot import Shot

# create Player class that inherits from CircleShape and extends 'rotation'

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    # create the player sprite as a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # draw the player to the screen. This should be ran inside the game loop in order to update every frame in main.py.
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # rotate() method to rotate the player. Called upon in the update() method below.
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # update the player's rotation when a key is pressed/held using the rotate() method. Called every frame in main.py.
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    # move() method to move the player forward. Creates a vector, rotates it to the player's rotation, then increases the vector resulting in speed.
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot (self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED
        return new_shot
