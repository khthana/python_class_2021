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

            # TODO : check mouse click in arrow
            if event.type == pygame.MOUSEBUTTONDOWN:
               if event.pos[0] in range(300,325) and event.pos[1] in range(200,228):
                   print("play")

menu()
