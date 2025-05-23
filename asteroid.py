import random
from circleshape import *
from constants import *

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    # create two new asteroids when the original is destroyed
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle_1 = random.uniform(20, 50)
            random_angle_2 = random_angle_1 * -1
            old_radius = self.radius

            trajectory_1 = self.velocity.rotate(random_angle_1)
            trajectory_2 = self.velocity.rotate(random_angle_2)

            new_radius = old_radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = trajectory_1 * 1.2
            new_asteroid_2.velocity = trajectory_2 * 1.2
