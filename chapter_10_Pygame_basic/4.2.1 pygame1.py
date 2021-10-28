# game loop
# ต้อง import pygame

import pygame

# Initialize
pygame.init()

# สร้าง display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# กรณีที่ต้องการ caption
pygame.display.set_caption("Test")

# game loop ในการสร้างเกม จะมีการทำงานในลักษณะที่ไม่รู้จบ จนกว่าจะสิ้นสุดเกม เรียกว่า game loop
running = True
while running:
    # 1) pass
    # ในการรับ mouse หรือ keyboard จะเรียกว่า event
    # จะใช้วิธีวนลูปเพื่อรับไปเรื่อยๆ
    # TODO: ให้รัน 2 บรรทัดนี้ แล้วดูการแสดงผลที่เกิดขึ้น
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

# end of the game
pygame.quit()







