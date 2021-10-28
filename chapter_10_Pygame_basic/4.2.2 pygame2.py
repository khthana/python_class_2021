# วาดรูปทรง
import pygame

pygame.init()

# สร้าง display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# กรณีที่ต้องการ caption
pygame.display.set_caption("Draw Shape")

# กำหนดค่าคงที่ของสี เป็น Tuple ของ RGB
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

# การวาดเส้นรูปทรงต่างๆ
# line(surface, color, start, stop, thickness)
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)

# circle
# circle(surface, color, center, radius, thickness)
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 100, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 95, 0)

# rectangle(surface, color, (top-left-x, top-left-y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
