# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    # initialize pygame and draw the screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # variables used to redraw the game window
    clock = pygame.time.Clock()
    dt = 0

    # Create groups and assign them to a static field called 'containers' in the Player class.
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    # instantiate Player object at the given coordinates
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    player.timer = 0
    asteroid_field = AsteroidField()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            # add a shot to the screen every time space bar is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player.timer <= 0:
                new_shot = player.shoot()
                shots.add(new_shot)
                updatable.add(new_shot)
                player.timer = PLAYER_SHOOT_COOLDOWN
        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)
        for sprite in updatable:
            sprite.update(dt)
            player.timer -= dt
        for asteroid in asteroids:
            is_colliding_player = asteroid.collision_check(player)
            if is_colliding_player == True:
                print("Game over!")
                return
            for shot in shots:
                is_colliding_shot = asteroid.collision_check(shot)
                if is_colliding_shot == True:
                    asteroid.split()
                    new_shot.kill()
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()

