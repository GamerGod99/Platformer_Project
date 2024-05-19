import sys

import pygame

from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Platformer')

        self.screen = pygame.display.set_mode((1280, 720))  # Window surface
        self.display = pygame.Surface((640, 320))  # Render surface, scaled down 2x (for 4x: 320, 180)

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        # asset dictionary
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (100, 100), (6, 16))

    def run(self):
        while True:
            self.display.fill((14, 180, 245))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
