import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import *
from shot import Shot

def main():
    pygame.init()
    updatetable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    Asteroid.containers = (asteroids, updatetable, drawable)
    AsteroidField.containers = (updatetable)
    Shot.containers = (shots, updatetable, drawable)
    Player.containers = (updatetable, drawable)

    asteroid_field = AsteroidField()
    player_1 = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    print("Starting Asteroids!")

    while pygame.get_init():
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatetable.update(dt)

        for i in drawable:
            i.draw(screen)

        for a in asteroids:
            if a.is_colliding(player_1):
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.is_colliding(s):
                    a.split()
                    s.kill()
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":  
    main()
