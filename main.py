import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #grouping entities
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #initializing objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score = Score()
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #updating
        for obj in updatable:
            obj.update(dt)

        #checking collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                print(f"Score: {score.get_score()}")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    score.update_score(asteroid.get_score_value())
                    shot.kill()
                    asteroid.split()

        #rendering
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        score.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()