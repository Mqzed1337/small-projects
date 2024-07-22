import pygame

pygame.init()

ScreenWidth = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Pygame Revision")

x = 50
y = 425
width = 60
height = 80
velocity = 0

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

clock = pygame.time.Clock()

"""
class player:
    def __init__(self, x, y, xvel, gravity, width, height, drag, change):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.gravity = gravity
        self.yvel = 0
        self.width = width
        self.height = height
        self.drag = drag
        self.change = change

    def draw(self, canvas):
        pygame.draw.rect(canvas, (255, 0, 0), self.x, self.y, self.width, self.height)

    def tick(self):
        self.x += self.xvel
        self.x *= self.drag
        if self.collidelist(obstacles):
            xvel = 0
       
        self.y += self.yvel
        self.y -= self.gravity
        if self.collidelist(obstacles):
            yvel = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.xvel -= self.change
   
        if keys[pygame.K_RIGHT]:
            self.xvel += self.change


obstacles = [pygame.rect(300, 450, 50, 50), pygame.rect(0, 500, 500, 1)]
player1 = player(50, 425, 0, 1, 60, 80, 0.8, 2)
"""


run = True
while run:
    x += velocity
    velocity *= 0.8

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        velocity -= 2

    if keys[pygame.K_RIGHT] and x < 500 - width - velocity:
        velocity += 2

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.3 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    ScreenWidth.fill((0, 0, 0))
    pygame.draw.rect(ScreenWidth, (255, 0, 0), (x, y, width, height))

    pygame.draw.rect(ScreenWidth, (0, 255, 0), (300, 450, 50, 50))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
