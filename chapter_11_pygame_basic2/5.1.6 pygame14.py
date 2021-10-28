# ตรวจสอบการชน
import pygame

# load image
walkRight = [pygame.image.load('image/R1.png'), pygame.image.load('image/R2.png'),
             pygame.image.load('image/R3.png'), pygame.image.load('image/R4.png'),
             pygame.image.load('image/R5.png'), pygame.image.load('image/R6.png'),
             pygame.image.load('image/R7.png'), pygame.image.load('image/R8.png'),
             pygame.image.load('image/R9.png')]

walkLeft = [pygame.image.load('image/L1.png'), pygame.image.load('image/L2.png'),
            pygame.image.load('image/L3.png'), pygame.image.load('image/L4.png'),
            pygame.image.load('image/L5.png'), pygame.image.load('image/L6.png'),
            pygame.image.load('image/L7.png'), pygame.image.load('image/L8.png'),
            pygame.image.load('image/L9.png')]

background = pygame.image.load('image/bg.jpg')
character = pygame.image.load('image/standing.png')

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Collision")

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
        self.standing = True  # NEW
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)  # NEW

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)    # NEW
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # To draw the hit box around the player


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


class Enemy(object):
    walkRight = [pygame.image.load('image/R1E.png'), pygame.image.load('image/R2E.png'),
                 pygame.image.load('image/R3E.png'), pygame.image.load('image/R4E.png'),
                 pygame.image.load('image/R5E.png'), pygame.image.load('image/R6E.png'),
                 pygame.image.load('image/R7E.png'), pygame.image.load('image/R8E.png'),
                 pygame.image.load('image/R9E.png'), pygame.image.load('image/R10E.png'),
                 pygame.image.load('image/R11E.png')]
    walkLeft = [pygame.image.load('image/L1E.png'), pygame.image.load('image/L2E.png'),
                pygame.image.load('image/L3E.png'), pygame.image.load('image/L4E.png'),
                pygame.image.load('image/L5E.png'), pygame.image.load('image/L6E.png'),
                pygame.image.load('image/L7E.png'), pygame.image.load('image/L8E.png'),
                pygame.image.load('image/L9E.png'), pygame.image.load('image/L10E.png'),
                pygame.image.load('image/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)  # NEW

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)  # NEW
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # Draws the hit box around the enemy

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    # NEW METHOD
    def hit(self):  # This will display when the enemy is hit
        print('hit')


def redraw_game_window():
    screen.blit(background, (0, 0))
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.update()


# mainloop
man = Player(200, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 300)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # NEW
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] \
                and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] \
                    and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))

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
