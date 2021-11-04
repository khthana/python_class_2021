import random
import pygame

pygame.init()


WIDTH, HEIGHT = 640, 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Side Scroller')


def menu():
    image = pygame.image.load("assets/menu.png")
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    run = True
    while run:

        screen.blit(image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300, 325) and event.pos[1] in range(200, 228):
                    game()

def game():
    image = pygame.image.load("assets/level1.png")
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    bg_x = 0

    # Load player image
    player = pygame.image.load("assets/boy.png")
    player = pygame.transform.rotozoom(player, 0, 0.2)  # ลดขนาดลง 20%
    player_y = 325
    jump = 0
    gravity = 1
    jump_count = 0

    # TODO : โหลดกล่อง
    box = pygame.image.load("assets/crate.png")
    box = pygame.transform.rotozoom(box, 0, 0.8)  # ลดขนาดลง 20%

    box_x = 700
    box_speed = 2

    run = True
    while run:

        screen.blit(image, (bg_x - 640, 0))
        screen.blit(image, (bg_x, 0))
        screen.blit(image, (bg_x + 640, 0))

        bg_x -= 1
        if bg_x < -640:
            bg_x = 0

        p_rect = screen.blit(player, (50, player_y))
        if player_y < 325:
            player_y += gravity
        if jump == 1:
            player_y -= 4
            jump_count += 1
            if jump_count > 40:
                jump_count = 0
                jump = 0

        # TODO : แสดงกล่อง และให้เลื่อนเร็วกว่าฉาก ถ้าถึงต้นจอ ให้ สุ่มตำแหน่ง และ ความเร็ว
        b_rect = screen.blit(box, (box_x, 360))
        box_x -= box_speed
        if box_x < -50:
            box_x = random.randint(700, 800)
            box_speed = random.randint(2, 5)

        # TODO : ตรวจสอบการชนกัน
        if p_rect.colliderect(b_rect):
            return

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                jump = 1


menu()
