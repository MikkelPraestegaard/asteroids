from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius)
        return 
    
    def update(self, dt):
        self.position += self.velocity * dt 
        return 
    
    def split(self):
        
        old_radius = self.radius

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)

        vec1 = self.velocity.rotate(new_angle)
        vec2 = self.velocity.rotate(-new_angle)

        new_radius = old_radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        
        
        asteroid1.velocity = vec1 * 1.2
        asteroid2.velocity = vec2 * 1.2

        