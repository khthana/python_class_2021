# แสดงตัวอักษร
import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Text")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
DARK_GREEN = (10, 50, 10)

# กำหนด background color
display_surface.fill(BLUE)

# การแสดง Text
# เราจะดู fonts ทั้งหมดได้จาก
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

# สามารถโหลด font ได้จาก https://www.fontspace.com/
# define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('AttackGraffiti.ttf', 32)

# define text
system_text = system_font.render("Hello", True, GREEN, DARK_GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("KMITL", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80)

# game loop ในการสร้างเกม จะมีการทำงานในลักษณะที่ไม่รู้จบ จนกว่าจะสิ้นสุดเกม เรียกว่า game loop
running = True
while running:
    # 1) pass
    # ในการรับ mouse หรือ keyboard จะเรียกว่า event
    # จะใช้วิธีวนลูปเพื่อรับไปเรื่อยๆ
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    # Blis (copy) text surface to display serface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    # update screen เพื่อให้แสดงผล
    pygame.display.update()
# end of the game
pygame.quit()
