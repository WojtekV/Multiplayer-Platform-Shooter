from Network import Network
from Platform import Platform
from Properties import *


class Game:
    """Game launch class, which exchanges data with server and draws all required graphics in game window"""

    win = pygame.display.set_mode((win_width, win_height))
    wait_for_player2 = True
    run = True
    bg = pygame.image.load('graphics/background2.png')

    @staticmethod
    def _init_platforms(p):
        p.append(Platform(platform_x, platform_y, platform_width, platform_height))
        p.append(Platform(platform2_x, platform2_y, platform2_width, platform2_height))
        p.append(Platform(platform3_x, platform3_y, platform3_width, platform3_height))
        p.append(Platform(platform4_x, platform4_y, platform4_width, platform4_height))
        p.append(Platform(platform5_x, platform5_y, platform5_width, platform5_height))

    def play(self):
        """Method runs game: :
            - connects to server
            - gets player instance
            - sends and receives information from server until one of players wins

        """

        pygame.init()
        clock = pygame.time.Clock()
        self._init_platforms(platforms)
        n = Network()
        p = n.get_p()
        pygame.display.set_caption("First Game")

        while self.wait_for_player2:
            p2 = n.send(p)
            font = pygame.font.SysFont("consolas", 50)
            self.win.blit(self.bg, (0, 0))
            text = font.render("Waiting for player 2...", 1, (0, 50, 200))
            self.win.blit(text, (win_width / 2 - text.get_width() / 2, win_height / 2 - text.get_height() / 2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.wait_for_player2 = False
            pygame.display.update()
            if p2.num_of_players == 2 or p.num_of_players == 2:
                print('Running!')
                while self.run:
                    clock.tick(FPS)
                    p2 = n.send(p)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.run = False
                            self.wait_for_player2 = False
                    self._redraw_game_window(p, p2)
        pygame.quit()

    def _redraw_game_window(self, player, player2):
        # redraws window

        self.win.blit(self.bg, (0, 0))
        for pl in platforms:
            pl.draw(self.win)
        player.collision(player2)
        player.move()
        player.draw(self.win, player2)
        player2.draw(self.win, player)
        if player.is_dead:
            self._you_lost()
        if player2.is_dead:
            self._you_win()

        pygame.display.update()

    def _you_win(self):
        # displays winner status

        font = pygame.font.SysFont("consolas", 120)
        text = font.render("You Win!", 1, (0, 255, 0))
        self.win.blit(text, (win_width / 2 - text.get_width() / 2, win_height / 2 - text.get_height() / 2))

    def _you_lost(self):
        # displays loser status

        font = pygame.font.SysFont("consolas", 120)
        text = font.render("You Lost!", 1, (255, 0, 0))
        self.win.blit(text, (win_width / 2 - text.get_width() / 2, win_height / 2 - text.get_height() / 2))


if __name__ == "__main__":
    Game().play()
