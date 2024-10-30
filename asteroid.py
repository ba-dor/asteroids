from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position[0],self.position[1],new_radius).velocity = vector_1*1.2
        Asteroid(self.position[0],self.position[1],new_radius).velocity = vector_2*1.2