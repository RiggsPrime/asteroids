import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, other_shape):
        r1 = self.radius
        r2 = other_shape.radius

        # if the distance between two circles is less than or equal to the sum of their radii, then they are colliding!

        distance = pygame.math.Vector2.distance_to(self.position, other_shape.position)

        return distance <= r1 + r2

        