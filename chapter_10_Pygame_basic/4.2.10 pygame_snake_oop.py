import pygame
import random

pygame.init()
w = 500
h = 500
screen_size = [w, h]
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (211, 211, 211)
x_speed = 1
y_speed = 0


class Square:

    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw_it(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width), 0)


class Grid:

    def __init__(self, size, distance, color):
        self.size = size
        self.distance = distance
        self.color = color
        self.square = []
        x = 0
        y = 0
        for i in range(self.size ** 2):
            self.square.append(Square(x, y, self.color, self.size))
            x += self.size + self.distance
            if x >= w:
                x = 0
                y += self.size + self.distance

    def draw_gird(self, color):
        for i in range(self.size ** 2):
            self.square[i].color = color
            self.square[i].draw_it()


class Snake:
    def __init__(self, length, color):
        self.square = []
        self.color = color
        self.length = length
        self.points = length
        x = 0
        y = 0
        for i in range(length):
            self.square.append(Square(x, y, color, grid.size))
            x -= grid.size + grid.distance

    def draw_it(self):
        for i in range(len(self.square)):
            self.square[i].draw_it()

    def move_it(self):
        for i in range(len(self.square) - 1, 0, -1):
            self.square[i].x = self.square[i - 1].x
            self.square[i].y = self.square[i - 1].y
        self.square[0].x += (grid.size + grid.distance) * x_speed
        self.square[0].y += (grid.size + grid.distance) * y_speed
        if self.square[0].x >= w:
            self.square[0].x = 0
        if self.square[0].y >= h:
            self.square[0].y = 0
        if self.square[0].x < 0:
            self.square[0].x = w - (grid.size + grid.distance)
        if self.square[0].y < 0:
            self.square[0].y = w - (grid.size + grid.distance)

    def check_food(self):
        if self.square[0].x == apple.x and self.square[0].y == apple.y:
            apple_xy()
            self.points += 1
            self.square.append(Square(-100, -100, self.color, grid.size))

    def check_die(self):
        for i in range(1, len(self.square), 1):
            if self.square[0].x == self.square[i].x and self.square[0].y == self.square[i].y:
                for j in range(len(self.square) - 1, self.length - 1, -1):
                    del self.square[j]
                    self.points = self.length
                apple_xy()
                break


def movement():
    global x_speed
    global y_speed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_speed != 1:
                    x_speed = 0
                    y_speed = 0
                    y_speed = -1
                    break
            if event.key == pygame.K_DOWN:
                if y_speed != -1:
                    x_speed = 0
                    y_speed = 0
                    y_speed = 1
                    break
            if event.key == pygame.K_RIGHT:
                if x_speed != -1:
                    x_speed = 0
                    y_speed = 0
                    x_speed = 1
                    break
            if event.key == pygame.K_LEFT:
                if x_speed != 1:
                    x_speed = 0
                    y_speed = 0
                    x_speed = -1
                    break


def apple_xy():
    apple.x = random.randint(0, (w / (grid.size + grid.distance)) - 1) * (grid.size + grid.distance)
    apple.y = random.randint(0, (h / (grid.size + grid.distance)) - 1) * (grid.size + grid.distance)
    for i in range(len(snake.square)):
        if snake.square[i].x == apple.x and snake.square[i].y == apple.y:
            apple_xy()


grid = Grid(22, 3, GREY)
snake = Snake(4, GREEN)
apple = Square(-100, -100, RED, grid.size)
font = pygame.font.SysFont("courier new", 20)
apple_xy()

while True:
    pygame.draw.rect(screen, BLACK, (0, 0, w, h), 0)
    grid.draw_gird(GREY)
    movement()
    snake.move_it()
    snake.check_die()
    snake.check_food()
    snake.draw_it()
    apple.draw_it()
    text = font.render(str(snake.points), True, (0, 0, 0))
    screen.blit(text, (0, 0))
    pygame.display.update()
    clock.tick(10)