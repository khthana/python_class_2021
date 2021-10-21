import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Image")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# กำหนด background color
display_surface.fill(BLUE)

# load picture from www.iconarchive.com
# ต้องใช้วิธีสร้างรูปสี่เหลี่ยมขนาดเท่ารูปและเอารูปไปไว้บนนั้น
dragon_left_image = pygame.image.load("asset/dragon_left.png")
dragon_left_ract = dragon_left_image.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
dragon_left_ract.topleft = (0,0)

dragon_right_image = pygame.image.load("asset/dragon_right.png")
dragon_right_ract = dragon_right_image.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
dragon_right_ract.topright = (WINDOW_WIDTH,0)

# game loop ในการสร้างเกม จะมีการทำงานในลักษณะที่ไม่รู้จบ จนกว่าจะสิ้นสุดเกม เรียกว่า game loop
running = True
while running:
    # 1) pass
    # ในการรับ mouse หรือ keyboard จะเรียกว่า event
    # จะใช้วิธีวนลูปเพื่อรับไปเรื่อยๆ
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # Blit : copy a surface object to display
    display_surface.blit(dragon_left_image, dragon_left_ract)
    display_surface.blit(dragon_right_image, dragon_right_ract)

    pygame.draw.line(display_surface, WHITE, (0, 75), (WINDOW_WIDTH, 75), 4)

    # update screen เพื่อให้แสดงผล
    pygame.display.update()
# end of the game
pygame.quit()
