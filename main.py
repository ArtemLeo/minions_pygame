import pygame
import os
import random

# Initialize Pygame and its mixer for sound
pygame.init()
pygame.mixer.init()

# Load and set up sounds
collect_sounds = [
    pygame.mixer.Sound("assets/sounds/collect1.mp3"),
    pygame.mixer.Sound("assets/sounds/collect2.mp3"),
    pygame.mixer.Sound("assets/sounds/collect3.mp3"),
    pygame.mixer.Sound("assets/sounds/collect4.mp3"),
    pygame.mixer.Sound("assets/sounds/collect5.mp3"),
    pygame.mixer.Sound("assets/sounds/collect6.mp3")
]

# Set volume for each sound
for sound in collect_sounds:
    sound.set_volume(1.0)

# Load background music and set it to play indefinitely
background_music = "assets/sounds/background.mp3"
pygame.mixer.music.load(background_music)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My PyGame Project: Minions")

# Colors
background_color = (0, 0, 0)
wall_color = (255, 255, 255)

# Cell size for the maze
cell_size = 40

# Load and scale images
player_img = pygame.image.load(os.path.join("assets", "images", "player.png"))
player_img = pygame.transform.scale(player_img, (cell_size, cell_size))

key_img = pygame.image.load(os.path.join("assets", "images", "banana.png"))
key_img = pygame.transform.scale(key_img, (cell_size, cell_size))

door_img = pygame.image.load(os.path.join("assets", "images", "door.jpg"))
door_img = pygame.transform.scale(door_img, (cell_size, cell_size))

wall_img = pygame.image.load(os.path.join("assets", "images", "wall.png")).convert_alpha()
wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))

# Load and scale background images
background_img_start = pygame.image.load(os.path.join("assets", "images", "background_start.jpg"))
background_img_start = pygame.transform.scale(background_img_start, (screen_width, screen_height))

background_img_game = pygame.image.load(os.path.join("assets", "images", "background_game.png"))
background_img_game = pygame.transform.scale(background_img_game, (screen_width, screen_height))

background_img_finish = pygame.image.load(os.path.join("assets", "images", "background_finish.jpg"))
background_img_finish = pygame.transform.scale(background_img_finish, (screen_width, screen_height))

# Load button images
start_button_img = pygame.image.load(os.path.join("assets", "images", "start_button.png"))
play_again_button_img = pygame.image.load(os.path.join("assets", "images", "play_again_button.png"))
exit_button_img = pygame.image.load(os.path.join("assets", "images", "exit_button.png"))

# Define the maze layout
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Initial player and exit positions
player_x, player_y = 1, 1
exit_x, exit_y = 17, 9

# Initialize keys with one fixed position and 14 random positions
keys = [(6, 1)]
for _ in range(14):
    x, y = random.randint(1, len(maze[0]) - 2), random.randint(1, len(maze) - 2)
    while maze[y][x] != 0 or (x, y) in keys:
        x, y = random.randint(1, len(maze[0]) - 2), random.randint(1, len(maze) - 2)
    keys.append((x, y))

# Initialize variables
has_key = False
collected_keys = 0

# Game loop control
running = True
clock = pygame.time.Clock()
fps = 60

# Font for text rendering
font = pygame.font.SysFont(None, 36)

# Sound index for cycling through collect sounds
sound_index = 0

def main_menu():
    """Display the main menu and wait for user interaction."""
    menu = True
    start_button_rect = pygame.Rect(150, 50, start_button_img.get_width(),
                                    start_button_img.get_height())  # Clickable area for "START NOW" button
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    menu = False

        screen.blit(background_img_start, (0, 0))
        screen.blit(start_button_img, (150, 50))
        pygame.display.flip()

def finish_screen():
    """Display the finish screen and wait for user interaction."""
    finish = True
    play_again_button_rect = pygame.Rect(25, 35, play_again_button_img.get_width(),
                                         play_again_button_img.get_height())  # Clickable area for "Play Again" button
    exit_button_rect = pygame.Rect(635, 295, exit_button_img.get_width(),
                                   exit_button_img.get_height())  # Clickable area for "Exit" button
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if play_again_button_rect.collidepoint(mouse_x, mouse_y):
                    main_menu()
                    return True
                elif exit_button_rect.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        screen.blit(background_img_finish, (0, 0))
        screen.blit(play_again_button_img, (25, 35))
        screen.blit(exit_button_img, (635, 295))
        pygame.display.flip()

# Display the main menu
main_menu()

# Movement flags
move_left = move_right = move_up = move_down = False

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_x > 0 and maze[player_y][player_x - 1] == 0:
                move_left = True
            if event.key == pygame.K_RIGHT and player_x < len(maze[0]) - 1 and maze[player_y][player_x + 1] == 0:
                move_right = True
            if event.key == pygame.K_UP and player_y > 0 and maze[player_y - 1][player_x] == 0:
                move_up = True
            if event.key == pygame.K_DOWN and player_y < len(maze) - 1 and maze[player_y + 1][player_x] == 0:
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    # Update player position based on movement flags
    if move_left:
        player_x -= 1
        move_left = False
    if move_right:
        player_x += 1
        move_right = False
    if move_up:
        player_y -= 1
        move_up = False
    if move_down:
        player_y += 1
        move_down = False

    # Check for key collection
    for key_x, key_y in keys:
        if player_x == key_x and player_y == key_y:
            keys.remove((key_x, key_y))
            collected_keys += 1
            collect_sounds[sound_index].play()
            sound_index = (sound_index + 1) % len(collect_sounds)
            break

    # Check if the player has reached the exit with all keys collected
    if player_x == exit_x and player_y == exit_y and collected_keys == 15:
        if finish_screen():
            # Reset game state
            player_x, player_y = 1, 1
            keys = [(6, 1)]
            for _ in range(14):
                x, y = random.randint(1, len(maze[0]) - 2), random.randint(1, len(maze) - 2)
                while maze[y][x] != 0 or (x, y) in keys:
                    x, y = random.randint(1, len(maze[0]) - 2), random.randint(1, len(maze) - 2)
                keys.append((x, y))
            collected_keys = 0
        else:
            running = False

    # Draw everything
    screen.blit(background_img_game, (0, 0))
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                screen.blit(wall_img, (x * cell_size, y * cell_size))

    screen.blit(player_img, (player_x * cell_size, player_y * cell_size))

    for key_x, key_y in keys:
        screen.blit(key_img, (key_x * cell_size, key_y * cell_size))

    screen.blit(door_img, (exit_x * cell_size, exit_y * cell_size))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
