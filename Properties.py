# File contains all necessary constants used to play a game.
import pygame

# window properties
win_width = 800
win_height = 600
player_width = 53
player_height = 63

# platforms properties:
platform_width = win_width * 0.2
platform_height = win_height * 0.01
platform_x = 95
platform_y = 150

platform2_width = win_width * 0.2
platform2_height = win_height * 0.01
platform2_x = 332
platform2_y = 280

platform3_width = win_width * 0.2
platform3_height = win_height * 0.01
platform3_x = 80
platform3_y = 400

platform4_width = win_width * 0.2
platform4_height = win_height * 0.01
platform4_x = 582
platform4_y = 180

platform5_width = win_width * 0.2
platform5_height = win_height * 0.01
platform5_x = 630
platform5_y = 420

# player properties:
distance_from_bottom = 10
distance_form_sides = 10
distance_from_up = 10

# physics properties:
gravity = 9.81
delta_t = 0.05
jump_velocity = 10
player_velocity_x = 4
bullet_velocity_x = 7

# color properties:
platform_color = (180, 160, 106)
bullet_color = (0, 0, 0)
player_color = (80, 80, 200)

# gameplay properties
FPS = 60
bullet_radius = 3
max_jump_count = 100
bullet_wait_time = 5
Health = 10
platforms = []

# images:
left1 = pygame.image.load('graphics/walkleft1.png')
left2 = pygame.image.load('graphics/walkleft2.png')
right1 = pygame.image.load('graphics/walkright1.png')
right2 = pygame.image.load('graphics/walkright2.png')
left3 = pygame.image.load('graphics/walkleftE1.png')
left4 = pygame.image.load('graphics/walkleftE2.png')
right3 = pygame.image.load('graphics/walkrightE1.png')
right4 = pygame.image.load('graphics/walkrightE2.png')
