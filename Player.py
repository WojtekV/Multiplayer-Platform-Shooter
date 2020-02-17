from Properties import *
from Bullet import Bullet


class Player:
    """Class contains all variables describing the player instance."""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_y = 0
        self.velocity_x = player_velocity_x
        self.prev_space_state = False
        self.jump_count = 0
        self.player_color = player_color
        self.direction = 1  # 1 is right, -1 is left
        self.cd = 0
        self.cd_bool = False
        self.my_bullets = []
        self.health = Health
        self.is_dead = False
        self.counter = 0
        self.num_of_players = 0
        self.which_blit = False

    def _move_horizontally(self):
        # updates player horizontal position

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.x < win_width - player_width - self.velocity_x - distance_form_sides:
                self.x += self.velocity_x
                self.direction = 1
                self.counter += 1

        elif keys[pygame.K_LEFT]:
            if self.x > self.velocity_x + distance_form_sides:
                self.x -= self.velocity_x
                self.direction = -1
                self.counter += 1

    def _move_vertically(self):
        # updates player vertical position

        self.velocity_y -= gravity*delta_t
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] != self.prev_space_state and not self.prev_space_state\
                and self.jump_count < max_jump_count:
            self.velocity_y = jump_velocity
            self.jump_count += 1
        self.prev_space_state = keys[pygame.K_SPACE]

        # is_jumping
        if self.velocity_y > 0:
            # if in borders
            if self.y - self.velocity_y - distance_from_up > 0:
                self.y -= self.velocity_y
            # if jumped off screen
            else:
                self.y = distance_from_up
                self.velocity_y = 0
        # is_falling
        elif self.velocity_y < 0:
            # if is falling on platform
            for p in platforms:
                if self.x + self.width > p.x and self.x < p.x + p.width:
                    if self.y + self.height <= p.y < self.y + self.height - self.velocity_y:
                        self.y = p.y - self.height
                        self.velocity_y = 0
                # if is on platform
                if self.x + self.width > p.x and self.x < p.x + p.width and self.y == p.y - self.height:
                    self.velocity_y = 0
            # if in borders
            if self.y < win_height - player_height + self.velocity_y - distance_from_bottom:
                self.y -= self.velocity_y
            # if fall off the screen
            else:
                self.y = win_height - player_height - distance_from_bottom
                self.velocity_y = 0
                self.jump_count = 0

    def _shoot(self):
        # shoots an bullet (creates Bullet object and adds it to the player bullet list)

        if self.cd == 0:
            bullet = Bullet(self.x + self.width / 2, self.y + self.height / 2 + 9, self.direction)
            self.my_bullets.append(bullet)

    def _is_shooting(self):
        # checks if player wants to shoot (if shot key is pressed)

        if not self.cd_bool:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self._shoot()
                self.cd = bullet_wait_time
                self.cd_bool = True
        else:
            if self.cd > 0:
                self.cd -= 0.5
            else:
                self.cd_bool = False
                pass

    def move(self):
        """Moves player (if he is not dead)"""

        if not self.is_dead:
            self._move_vertically()
            self._move_horizontally()
            self._is_shooting()

    def draw(self, win, enemy):
        """Draws players and bullets in window

        Arguments:
            win (pygame.display): game window
            enemy (Player): second player instance

        """
        for b in self.my_bullets:
            if enemy.x < b.x < enemy.x + enemy.width and enemy.y < b.y < enemy.y + enemy.height:
                self.my_bullets.remove(b)
            elif 0 < b.x < win_width:
                b.draw(win)
            else:
                self.my_bullets.remove(b)

        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 10, 50, 3))
        if self.health > 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - 10, 5 * self.health, 3))

        pygame.draw.rect(win, self.player_color, (self.x, self.y, self.width, self.height))
        if self.counter > 5:
            self.counter = 0
            self.which_blit = not self.which_blit
        if self.num_of_players == 1:
            if self.direction == -1:    #left
                if self.which_blit:
                    win.blit(left1, (self.x, self.y))
                else:
                    win.blit(left2, (self.x, self.y))
            else: # pygame.draw.rect(win, self.player_color, (self.x, self.y, self.width, self.height))
                if self.which_blit:
                    win.blit(right1, (self.x, self.y))
                else:
                    win.blit(right2, (self.x, self.y))
        else:
            if self.direction == -1:    #left
                if self.which_blit:
                    win.blit(left3, (self.x, self.y))
                else:
                    win.blit(left4, (self.x, self.y))
            else: # pygame.draw.rect(win, self.player_color, (self.x, self.y, self.width, self.height))
                if self.which_blit:
                    win.blit(right3, (self.x, self.y))
                else:
                    win.blit(right4, (self.x, self.y))

    def collision(self, enemy):
        """Checks if the bullet has hit an enemy player

        Arguments:
            enemy (class): second player instance

        """
        for b in enemy.my_bullets:
            if self.x < b.x < self.x + self.width and self.y < b.y < self.y + self.height:
                enemy.my_bullets.remove(b)
                self.health -= 1
                if self.health < 0:
                    self.is_dead = True
                    self.player_color = (0, 100, 150)
