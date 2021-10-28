# สร้างภาพเคลื่อนไหว
import pygame

# load image
walkRight = [pygame.image.load('image/R1.png'),
             pygame.image.load('image/R2.png'),
             pygame.image.load('image/R3.png'),
             pygame.image.load('image/R4.png'),
             pygame.image.load('image/R5.png'),
             pygame.image.load('image/R6.png'),
             pygame.image.load('image/R7.png'),
             pygame.image.load('image/R8.png'),
             pygame.image.load('image/R9.png')]

walkLeft = [pygame.image.load('image/L1.png'),
            pygame.image.load('image/L2.png'),
            pygame.image.load('image/L3.png'),
            pygame.image.load('image/L4.png'),
            pygame.image.load('image/L5.png'),
            pygame.image.load('image/L6.png'),
            pygame.image.load('image/L7.png'),
            pygame.image.load('image/L8.png'),
            pygame.image.load('image/L9.png')]

background = pygame.image.load('image/bg.jpg')
character = pygame.image.load('image/standing.png')

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Character Animation")

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(character, (self.x, self.y))


def redrawGameWindow():
    screen.blit(background, (0, 0))
    man.draw(screen)

    pygame.display.update()


# mainloop
man = Player(200, 410, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:
        man.x += man.velocity
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()