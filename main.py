import pygame
import sys
import random
from collections import deque
pygame.init()

# Constants for the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
TILE_SIZE = SCREEN_WIDTH // 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
SHUFFLE_BUTTON_COLOR = (50, 50, 255)
RESET_BUTTON_COLOR = (255, 50, 50)

def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

def is_mouse_over_button(mouse_pos, button_rect):
    return button_rect.collidepoint(mouse_pos)

shuffle_button_rect = pygame.Rect(20, SCREEN_HEIGHT - 70, BUTTON_WIDTH, BUTTON_HEIGHT)
reset_button_rect = pygame.Rect(140, SCREEN_HEIGHT - 70, BUTTON_WIDTH, BUTTON_HEIGHT)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("15 Puzzle")

goal_board = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,0]]


def generate_board():
    board = [[0] * 4 for _ in range(4)]
    numbers = list(range(1, 16))
    random.shuffle(numbers)
    for row in range(4):
        for col in range(4):
            if(len(numbers)!=0):
                board[row][col] = numbers.pop()
    return board

board = generate_board()

def draw_board(board):
    for row in range(4):
        for col in range(4):
            tile = board[row][col]
            if tile != 0:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text_surface = FONT.render(str(tile), True, BLACK)
                text_rect = text_surface.get_rect(center=(col * TILE_SIZE + TILE_SIZE / 2, row * TILE_SIZE + TILE_SIZE / 2))
                screen.blit(text_surface, text_rect)

def find_empty_space(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return row, col


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    draw_board(board)
    print("hola")


    pygame.display.flip()





