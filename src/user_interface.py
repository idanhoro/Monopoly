import pygame
from src.player import Player
from src.board import move_on_board, PLAYERS, BLOCKS

WIDTH = 1000
HEIGHT = 1000
board_image = pygame.image.load("../images/board_image.jpg")
board_image = pygame.transform.scale(board_image, (WIDTH, HEIGHT))


def start():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_loop(screen)
    pygame.quit()


def game_loop(screen):
    running = True
    PLAYERS.append(Player("player1", 'Dog'))
    PLAYERS.append(Player('player2', 'Shoe'))
    PLAYERS.append(Player('player3', 'wheelbarrow'))
    PLAYERS.append(Player('player4', 'Ship'))

    for _ in range(0):
        move_on_board(PLAYERS[1])

    def draw():
        screen.blit(board_image, (0, 0))
        for block in BLOCKS:
            block_players = filter(lambda player: player.location == block.ID, PLAYERS)
            for player, position in zip(block_players, block.positions):
                screen.blit(player.image, position)
            break

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        draw()
        pygame.display.flip()
