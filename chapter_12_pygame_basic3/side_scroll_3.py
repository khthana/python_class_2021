import pygame

pygame.init()

# TODO : Step 1 create blank screen

WIDTH, HEIGHT = 640, 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Side Scroller')


def menu():
    image = pygame.image.load("assets/menu.png")
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    run = True
    while run:

        # TODO : Step 2 create menu function
        screen.blit(image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # TODO : Step 3 check mouse click in arrow
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300, 325) and event.pos[1] in range(200, 228):
                    game()


def game():
    image = pygame.image.load("assets/level1.png")
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    bg_x = 0

    # Load player image
    player = pygame.image.load("assets/boy.png")
    player = pygame.transform.rotozoom(player, 0, 0.2)  # ลดขนาดลงเหลือ 20%
    player_y = 325
    jump = 0
    gravity = 1
    jump_count = 0

    run = True
    while run:
        # ในการสร้าง side scrolling จะต้องสร้าง background image อีก 2 ภาพ
        # โดยให้อยู่ก่อนหน้าและต่อจากภาพ background ปัจจุบัน
        # และเลือกตำแหน่ง x ของการแสดงผลลดลงทีละ 1 ไปเรื่อยๆ
        # TODO : Step 4 สร้าง background เลื่อน

        screen.blit(image, (bg_x - 640, 0))
        screen.blit(image, (bg_x, 0))
        screen.blit(image, (bg_x + 640, 0))

        bg_x -= 1
        if bg_x < -640:
            bg_x = 0

        # TODO : Step 5 show player
        screen.blit(player, (50, player_y))

        # TODO : Step 6 Jump
        # ถ้าอยู่เหนือพื้น จะลดตำแหน่งลงเรื่อยๆ ทุก loop
        if player_y < 325:
            player_y += gravity

        # เมื่อกด jump จะขึ้น loop ละ 4 จำนวน 40 loop
        if jump == 1:
            player_y -= 4
            jump_count += 1
            if jump_count > 40:
                jump_count = 0
                jump = 0

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                jump = 1


menu()
