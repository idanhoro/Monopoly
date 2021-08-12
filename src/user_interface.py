import pygame
from src.player import Player
from src.board import move_on_board, PLAYERS, BLOCKS
import random

WIDTH = 1000
HEIGHT = 1000
FPS = 7
board_image = pygame.image.load("./images/board_image.jpg")
dice_image = pygame.image.load("./images/dice.png")
dices = {1: dice_image.subsurface((6, 0, 109, 110)), 2: dice_image.subsurface((131, 0, 109, 110)),
         3: dice_image.subsurface((255, 0, 109, 110)), 4: dice_image.subsurface((380, 0, 109, 110)),
         5: dice_image.subsurface((505, 0, 109, 110)), 6: dice_image.subsurface((630, 0, 109, 110))}
board_image = pygame.transform.scale(board_image, (WIDTH, HEIGHT))


def start():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_loop(screen)
    pygame.quit()


def draw_dice(screen, dice1, dice2):
    screen.blit(dices[dice1], (395, 450))
    screen.blit(dices[dice2], (505, 450))


def draw_pieces(screen):
    for player in PLAYERS:
        screen.blit(player.image, player.position)



def game_loop(screen):
    running = True
    PLAYERS.append(Player("player1", 'Dog'))
    PLAYERS.append(Player('player2', 'Shoe'))
    PLAYERS.append(Player('player3', 'wheelbarrow'))
    PLAYERS.append(Player('player4', 'Ship'))
    rolling = False
    turn = 0
    clock = pygame.time.Clock()
    active_player = PLAYERS[turn]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (400 < x < 605) and (460 < y < 560):
                    rolling = not rolling
                    if rolling:
                        turn = (turn+1) % len(PLAYERS)
                        active_player = PLAYERS[turn]
                        active_player.roll_dice()
                    else:
                        active_player.target_location = (active_player.location + active_player.last_roll) % len(BLOCKS)
        screen.blit(board_image, (0, 0))
        draw_pieces(screen)
        if active_player.location != active_player.target_location:
            move_on_board(active_player)
        if rolling:
            draw_dice(screen, random.randint(1, 6), random.randint(1, 6))
        else:
            draw_dice(screen, PLAYERS[turn].dice1, active_player.dice2)
        pygame.display.flip()
        clock.tick(FPS)
