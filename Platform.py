from Properties import *


class Platform:
    """Platforms for players. Players can jump on them."""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.platform_color = platform_color

    def draw(self, win):
        """Draws platforms in window.

        Parameters:
            win (pygame.display): game window

        """

        pygame.draw.rect(win, platform_color, (self.x, self.y, self.width, self.height))
