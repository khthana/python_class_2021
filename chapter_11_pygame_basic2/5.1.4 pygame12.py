# สร้างกระสุน
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
pygame.display.set_caption("Bullet")

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


class Fire(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redraw_game_window():
    screen.blit(background, (0, 0))
    man.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.update()


# mainloop
man = Player(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                Fire(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:
        man.x += man.velocity
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
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

    redraw_game_window()

pygame.quit()
