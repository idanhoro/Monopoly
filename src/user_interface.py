import pygame
from src.player import Player, players_images
from src.board import move_player, PLAYERS, BLOCKS, WIDTH, HEIGHT
import random
import menu
import os

FPS = 7
board_image = pygame.image.load("./images/board_image.jpg")
dice_image = pygame.image.load("./images/dice.png")
dices = {1: dice_image.subsurface((6, 0, 109, 110)), 2: dice_image.subsurface((131, 0, 109, 110)),
         3: dice_image.subsurface((255, 0, 109, 110)), 4: dice_image.subsurface((380, 0, 109, 110)),
         5: dice_image.subsurface((505, 0, 109, 110)), 6: dice_image.subsurface((630, 0, 109, 110))}
board_image = pygame.transform.scale(board_image, (WIDTH, HEIGHT))
BLUE = (0, 0, 255)


def start():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_loop(screen)
    pygame.quit()


def draw_dice(screen, dice1, dice2):
    screen.blit(dices[dice1], (395, 450))
    screen.blit(dices[dice2], (505, 450))


def draw_pieces(screen,turn):
    for index,player in enumerate(PLAYERS):
        rect = player.image.get_rect()
        rect.center = player.position
        if index == turn:
            effect = menu.effects.blit_outline((1, 1, 1))
            effect.apply(screen,player.image, rect)
        screen.blit(player.image, rect)


def players_menu(screen):
    bump = menu.effects.bump((1, 1, 1), 3)
    font_path = os.path.join('fonts', 'SNAP____.TTF')
    gap = (100, 100)
    offset = (500, 150)

    class NumPlayers:
        def __init__(self):
            self.num = 0

        def set(self, num):
            self.num = num

    num_players = NumPlayers()
    # Player selection menu
    h1 = menu.Header(menu.Font("Monopoly", font_size=100, font_color=(0, 0, 0), font_path=font_path))
    h2 = menu.Header(menu.Font("Select number of players:", font_size=50, font_color=(0, 0, 0), font_path=font_path))
    b1 = menu.RadioButton(
        menu.Font("Two players", highlight_color=BLUE, effects=bump, font_path=font_path, font_size=40),
        num_players.set, {"num": 2})
    b2 = menu.RadioButton(
        menu.Font("Three players", highlight_color=BLUE, effects=bump, font_path=font_path, font_size=40),
        num_players.set, {"num": 3})
    b3 = menu.RadioButton(
        menu.Font("Four players", highlight_color=BLUE, effects=bump, font_path=font_path, font_size=40),
        num_players.set, {"num": 4})
    b4 = menu.RadioButton(
        menu.Font("Five players", highlight_color=BLUE, effects=bump, font_path=font_path, font_size=40),
        num_players.set, {"num": 5})
    b5 = menu.RadioButton(
        menu.Font("Six players", highlight_color=BLUE, effects=bump, font_path=font_path, font_size=40),
        num_players.set, {"num": 6})
    b6 = menu.BackButton(
        menu.Font("Confirm", highlight_color=BLUE, effects=bump, font_path=font_path, font_size=40))

    player_selection_buttons = [[h1], [h2], [b1], [b2], [b3], [b4], [b5], [b6]]

    player_selection = menu.Menu(screen, player_selection_buttons, offset, gap,
                                 background_image="./images/players_menu.png")
    player_selection.render()

    # Pieces selection menu

    gap = (150, 150)
    bump = menu.effects.blit_outline((1, 1, 1), 5)
    image_selected = []
    for _ in range(num_players.num):

        player = Player('Idan', 'Shoe')

        t1 = menu.InputBox(
            menu.Font('Nickname: ', highlight_color=BLUE, effects=bump, font_path=font_path, font_size=40),
            player.set_nickname, ['nickname'], default='Type here')

        pieces_selection_buttons = [[h1], [t1], [], [], [b6]]
        for index, name in enumerate(players_images):
            pieces_selection_buttons[(index % 2) + 2].append(
                menu.Image(pygame.transform.scale(players_images[name], (120, 120)), player.set_image,
                           {'image_name': name}, effect=bump, disable_effect=menu.effects.shadow((125, 125, 125), 1),
                           disable=name in image_selected))

        pieces_selection = menu.Menu(screen, pieces_selection_buttons, offset, gap,
                                     background_image='./images/pieces_selection_menu.png')

        pieces_selection.render()
        image_selected.append(player.image_name)
        PLAYERS.append(player)


def game_loop(screen):
    running = True
    players_menu(screen)
    # PLAYERS.append(Player("player1", 'Dog'))
    # PLAYERS.append(Player('player2', 'Shoe'))
    # PLAYERS.append(Player('player3', 'Iron'))
    # PLAYERS.append(Player('player4', 'Ship'))
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
                        turn = (turn + 1) % len(PLAYERS)
                        active_player = PLAYERS[turn]
                        active_player.roll_dice()
                    else:
                        active_player.target_location = (active_player.location + active_player.last_roll) % len(
                            BLOCKS)
        screen.blit(board_image, (0, 0))
        draw_pieces(screen, turn)
        if active_player.location != active_player.target_location:
            move_player(active_player)
        if rolling:
            draw_dice(screen, random.randint(1, 6), random.randint(1, 6))
        else:
            draw_dice(screen, PLAYERS[turn].dice1, active_player.dice2)
        pygame.display.flip()
        clock.tick(FPS)
