import pygame

pygame.init()


width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame title")


# Colours
white = (233, 233, 233)
black = (0, 0, 0)


class Game:

    def draw(self): # the draw function
        win.fill(white)

        pygame.display.update()


    def start(self):

        # In game data
        run = True

        clock = pygame.time.Clock()
        fps = 60 # Frame per second

        while run:
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            self.draw()


if __name__ == "__main__":
    game = Game()
    game.start()