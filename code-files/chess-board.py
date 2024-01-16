import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 640, 640
SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")

# Create a function to draw the board
def draw_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, pygame.Rect(i * SIZE, j * SIZE, SIZE, SIZE))

# Create a function to convert algebraic notation to row and column numbers
def convert_algebraic_notation(notation):
    if len(notation) != 2:
        raise ValueError("Invalid algebraic notation")
    col = ord(notation[0].lower()) - ord('a')
    row = 8 - int(notation[1])
    return row, col

# Create a function to handle user input
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = pos[1] // SIZE, pos[0] // SIZE
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col * SIZE, row * SIZE, SIZE, SIZE))
            pygame.display.flip()
            user_input = chr(col + ord('a')) + str(8 - row)
            print(f"User input: {user_input}")

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    draw_board()
    handle_input()
    pygame.display.flip()