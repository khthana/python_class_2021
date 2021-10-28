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

# Global Variable
pos_x = 50
pos_y = 400
WIDTH = 40
HEIGHT = 60
VELOCITY = 5

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redraw_game_screen():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount

    screen.blit(background, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:  # If we are facing left
        screen.blit(walkLeft[walkCount // 3], (pos_x, pos_y))   # We integer divide walkCount by 3 to ensure each
        walkCount += 1                                          # image is shown 3 times every animation
    elif right:
        screen.blit(walkRight[walkCount // 3], (pos_x, pos_y))
        walkCount += 1
    else:
        screen.blit(character, (pos_x, pos_y))  # If the character is standing still

    pygame.display.update()


run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and pos_x > VELOCITY:
        pos_x -= VELOCITY
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and pos_x < 480 - VELOCITY - WIDTH:
        pos_x += VELOCITY
        left = False
        right = True

    else:  # If the character is not moving we will set both left and right false
           # and reset the animation counter (walkCount)
        left = False
        right = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            pos_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redraw_game_screen()

pygame.quit()
