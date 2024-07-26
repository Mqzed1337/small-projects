import os
import pygame


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screenWidth = 900
screenHeight = 600
fps = 60

if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


# functions to create our resources
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pygame.image.load(fullname)
    image = image.convert()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pygame.mixer.Sound(fullname)

    return sound


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        pass

    def update(self):
        pass

    pass


class Obstacle:
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.SCALED)
    pygame.display.set_caption("Platformer")
    pygame.mouse.set_visible(False)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((BLACK))

    screen.blit(background, (0, 0))
    pygame.display.flip()
    going = True
    clock = pygame.time.Clock()
    player = Player()
    while going:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False

        screen.blit(player.image, (100, 100))
        pygame.display.flip()

    pass


if __name__ == "__main__":
    main()
