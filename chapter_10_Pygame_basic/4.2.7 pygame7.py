# ไฟล์นี้แสดงการรับคีย์บอร์ดแบบต่อเนื่อง กระโดด และ ตรวจสอบขอบเขต
import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Keyboard Continuous Movement")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
DARK_GREEN = (10, 50, 10)

# Set FPS and clock
# FPS = 60
# clock = pygame.time.Clock()

VELOCITY = 5

# กำหนด background color
display_surface.fill(BLUE)

# Load Image
original_ship_image = pygame.image.load("../chapter_13_pygame/images/ship.png")
ship_image = pygame.transform.rotate(original_ship_image,90)
ship_ract = ship_image.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
ship_ract.centerx = WINDOW_WIDTH/2
ship_ract.bottom = WINDOW_HEIGHT

# game loop ในการสร้างเกม จะมีการทำงานในลักษณะที่ไม่รู้จบ จนกว่าจะสิ้นสุดเกม เรียกว่า game loop
running = True
isJump = False
jumpCount = 10

while running:
    # ในการรับ mouse หรือ keyboard จะเรียกว่า event
    # จะใช้วิธีวนลูปเพื่อรับไปเรื่อยๆ
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    # รับคีย์ต่อเนื่อง
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
          ship_ract.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
          ship_ract.x += VELOCITY

    # ตรวจสอบขอบเขตของการเคลื่อนที่
    if keys[pygame.K_LEFT] and ship_ract.left > 0:
        ship_ract.x -= VELOCITY

    if keys[pygame.K_RIGHT] and ship_ract.right < WINDOW_WIDTH:
        ship_ract.x += VELOCITY

    # กระโดด
    # if not isJump:  # Checks is user is not jumping
    #     if keys[pygame.K_UP] and ship_ract.y > VELOCITY:  # Same principles apply for the y coordinate
    #         ship_ract.y -= VELOCITY
    #
    #     if keys[pygame.K_DOWN] and ship_ract.y < 500 - WINDOW_HEIGHT - VELOCITY:
    #         ship_ract.y += VELOCITY
    #
    #     if keys[pygame.K_SPACE]:
    #         isJump = True
    # else:
    #     # This is what will happen if we are jumping
    #     if jumpCount >= -10:
    #         ship_ract.y -= (jumpCount * abs(jumpCount)) * 0.5
    #         # print(ship_ract.y,jumpCount)
    #         jumpCount -= 1
    #     else:  # This will execute if our jump is finished
    #         jumpCount = 10
    #         isJump = False

    # เคลียร์ screen เพื่อลบรูปเก่า
    display_surface.fill(BLUE)

    display_surface.blit(ship_image, ship_ract)

    # update screen เพื่อให้แสดงผล
    pygame.display.update()

    # tick the clock
#    clock.tick(FPS)

# end of the game
pygame.quit()
