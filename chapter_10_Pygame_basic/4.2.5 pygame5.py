# สร้างเสียง
import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Sound")

# กำหนด background color
BLUE = (0, 0, 255)
display_surface.fill(BLUE)

# สามารถสร้าง sound effect ได้ที่ https://www.leshylabs.com/apps/sfMaker/
# load soft effects
sound_1 = pygame.mixer.Sound('asset/sound_1.wav')
sound_2 = pygame.mixer.Sound('asset/sound_2.wav')

# play sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

# ปรับเสียงดัง ค่อย
sound_2.set_volume(.1)
sound_2.play()

# background music
pygame.mixer.music.load('asset/music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(10000)
pygame.mixer.music.stop()

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

    # update screen เพื่อให้แสดงผล
    pygame.display.update()
# end of the game
pygame.quit()
