import sys

import pygame


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Platformer')
        self.screen = pygame.display.set_mode((1280, 720))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img_pos = [640, 360]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(640, 360, 360, 60)

    def run(self):
        while True:
            self.screen.fill((14, 180, 245))

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 255, 100), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 100, 100), self.collision_area)

            self.img_pos[1] += 5 * (self.movement[1] - self.movement[0])
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()
