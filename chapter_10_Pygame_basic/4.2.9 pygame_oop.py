import pygame
import sys


MAX_FPS = 30
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
WHITE = (255, 255, 255)
BLUE = (90, 90, 255)
RED = (255, 50, 50)


def main():
    # Initialization
    pygame.init()
    size = width, height = 640, 360
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Game objects
    widget = Widget([290, 40], [60, 40])
    blue_button = Button(BLUE, [60, 210], [90, 40], widget.change_color)
    red_button = Button(RED, [490, 210], [90, 40], widget.change_color)
    white_button = Button(WHITE, [275, 210], [90, 40], widget.change_color)

    game_objects = [
        widget,
        blue_button,
        red_button,
        white_button,
    ]

    while True:
        # Handle events
        for event in pygame.event.get():
            # Let game objects handle events they care about
            for obj in game_objects:
                obj.handle_event(event)

            # Handle global events
            if event.type == pygame.QUIT:
                print("Got quit event!")
                quit()

        # Clear the screen
        screen.fill(GRAY)

        # Render game objects
        for obj in game_objects:
            obj.render(screen)

        # Complete the frame
        pygame.display.update()
        clock.tick(MAX_FPS)


class Widget(object):
    def __init__(self, pos, size):
        self._color = WHITE
        self._pos = pos
        self._size = size
        return

    def render(self, surface):
        pygame.draw.rect(surface, self._color, (self._pos + self._size))
        return

    def change_color(self, new_color):
        self._color = new_color
        return

    def handle_event(self, event):
        pass


class Button(object):
    def __init__(self, color, pos, size, callback):
        self._pos = pos
        self._size = size
        self._color = color
        self._callback = callback

        self._hover_surface = pygame.Surface(self._size)
        self._hover_surface.fill(BLACK)
        self._hover_surface.set_alpha(0)
        return

    def render(self, surface):
        pygame.draw.rect(surface, self._color, (self._pos + self._size))
        if self._is_hovered():
            self._hover_surface.set_alpha(100)
        else:
            self._hover_surface.set_alpha(0)
        surface.blit(self._hover_surface, self._pos)
        return

    def _is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        m_x = mouse_pos[0]
        m_y = mouse_pos[1]

        b_w = self._size[0]  # button width
        b_h = self._size[1]  # button height
        b_x1 = self._pos[0]  # button x1
        b_x2 = b_x1 + b_w    # button x2
        b_y1 = self._pos[1]  # button y1
        b_y2 = b_y1 + b_h    # button y2

        in_x_bound = (b_x1 <= m_x <= b_x2)
        in_y_bound = (b_y1 <= m_y <= b_y2)

        return in_x_bound and in_y_bound

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self._is_hovered():
            self._callback(self._color)


def quit(status=0):
    print("Quitting!")
    pygame.quit()
    sys.exit(status)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()