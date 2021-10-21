import pygame

# ไฟล์นี้แสดงการตรวจสอบการชนกัน

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Object Collision")

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
FPS = 60
clock = pygame.time.Clock()

VELOCITY = 5

# กำหนด background color
display_surface.fill(BLUE)

# Load Image
ship_image = pygame.image.load("../chapter_12_pygame/images/ship.png")
ship_ract = ship_image.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
ship_ract.left = 0
ship_ract.centery = WINDOW_HEIGHT/2

rock_image = pygame.image.load("../chapter_12_pygame/images/asteroid.png")
rock_ract = rock_image.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
rock_ract.centerx = 500
rock_ract.centery = WINDOW_HEIGHT/2


# game loop ในการสร้างเกม จะมีการทำงานในลักษณะที่ไม่รู้จบ จนกว่าจะสิ้นสุดเกม เรียกว่า game loop
running = True
while running:
    # ในการรับ mouse หรือ keyboard จะเรียกว่า event
    # จะใช้วิธีวนลูปเพื่อรับไปเรื่อยๆ
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    # รับคีย์ต่อเนื่อง
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ship_ract.left > 0:
        ship_ract.x -= VELOCITY
    if keys[pygame.K_RIGHT] and ship_ract.right < WINDOW_WIDTH:
        ship_ract.x += VELOCITY
    if keys[pygame.K_UP] and ship_ract.top > 0:
        ship_ract.y -= VELOCITY
    if keys[pygame.K_DOWN] and ship_ract.bottom < WINDOW_HEIGHT:
        ship_ract.y += VELOCITY

    # ตรวจสอบการชนกัน
    if ship_ract.colliderect(rock_ract):
        print("HIT")

    # เคลียร์ screen เพื่อลบรูปเก่า
    display_surface.fill(BLUE)

    # แสดงขอบเขตของวัตถุ
    pygame.draw.rect(display_surface, RED, ship_ract, 1)
    pygame.draw.rect(display_surface, GREEN, rock_ract, 1)

    display_surface.blit(ship_image, ship_ract)
    display_surface.blit(rock_image, rock_ract)

    # update screen เพื่อให้แสดงผล
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)

# end of the game
pygame.quit()
