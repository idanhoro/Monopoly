
from board import TrainStation, Facilities
from board import PLAYERS, BLOCKS
import random


class Chance():
    def __init__(self):
        self.deck = [AdvanceToGo(), MoveToBoardWalk(), AdvanceToIllinois(), AdvanceToCharlesPlaces(), TakeARide(),
                NearestRailroad(), NearestFacility(), GoBack(), Dividend(), BuildingMatures(), PoorTaxes(), Chairman(),
                GeneralRepairs(), GoToJail(), GetOutOfJail()]

        random.shuffle(self.deck)


class AdvanceToGo:
    def __init__(self):
        self.card_text = 'Advance to go collect 200$'

    def action(self, player):
        player.balance += 200


class MoveToBoardWalk:
    def __init__(self):
        self.card_text = 'Take a walk on the Boardwalk, advance token to Boardwalk'

    def action(self, player):
        blocks = board.BLOCKS
        player.location = board.move_to_location(blocks, player, 39)


class AdvanceToIllinois:
    def __init__(self):
        self.card_text = 'Advance to Illinois Ave.'

    def action(self, player):
        blocks = board.BLOCKS
        player.location = board.move_to_location(blocks, player, 24)


class AdvanceToCharlesPlaces:
    def __init__(self):
        self.card_text = 'Advance to St.Charles Place, if you pass Go collect 200$'

    def action(self, player):
        blocks = board.BLOCKS
        player.location = board.move_to_location(blocks, player, 11)


class TakeARide:
    def __init__(self):
        self.card_text = 'Take a ride on the reading, if you pass GO collect 200$'

    def action(self, player):
        blocks = board.BLOCKS
        player.location = board.move_to_location(blocks, player, 5)


class NearestRailroad:
    def __init__(self):
        self.card_text = 'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. if Railroad is UNOWNED, you may buy it from the bank'

    def action(self, player):
        while not isinstance(BLOCKS[player.location], TrainStation):
            player.location = (player.location + 1) % len(BLOCKS)
            BLOCKS[player.location].path(player)
        if BLOCKS[player.location].owner is None:
            BLOCKS[player.location].buy(player)
        if BLOCKS[player.location].owner != player.owner:
            BLOCKS[player.location].pay_rent(player, BLOCKS)
            BLOCKS[player.location].pay_rent(player, BLOCKS)


class NearestFacility:
    def __init__(self):
        self.card_text = 'Advance token to nearest utility, if unowned you may buy it from the bank. if owned, throw dice and pay owner a total ten times the amount thrown'

    def action(self, player):
        while not isinstance(BLOCKS[player.location], Facilities):
            player.location = (player.location + 1) % len(BLOCKS)
            BLOCKS[player.location].path(player)
        if BLOCKS[player.location].owner is None:
            BLOCKS[player.location].buy(player)
        if BLOCKS[player.location].owner != player.owner:
            player.balance -= player.last_roll * 10
            BLOCKS[player.location].owner.balance += player.last_roll * 10


class GoBack:
    def __init__(self):
        self.card_text = 'Go back 3 spaces'

    def action(self, player):
        blocks = board.BLOCKS
        player.location = board.move_to_location(blocks, player, player.location - 3)


class Dividend:
    def __init__(self):
        self.card_text = 'Bank pays you dividend of 50$'

    def action(self, player):
        player.balance += 50


class BuildingMatures:
    def __init__(self):
        self.card_text = 'Your building and loan matures collect 150'

    def action(self, player):
        player.balance += 150


class PoorTaxes:
    def __init__(self):
        self.card_text = 'Pay poor tax of 15$'

    def action(self, player):
        player.balance -= 15


class Chairman:
    def __init__(self):
        self.card_text = 'You have been elected chairman of the board pay each player 50$'

    def action(self, player):
        for p in PLAYERS:
            p.balance -= 50
            player.balance += 50


class GeneralRepairs:
    def __init__(self):
        self.card_text = 'Make general repairs on all your property for each house pay 25$ for each hotel 100$, 130$ for each sky-scraper'

    def action(self, player):
        total_sum = 0
        for block in BLOCKS:
            if block.house_count <= 4:
                total_sum += block.house_count * 25
            elif block.house_count == 5:
                total_sum += 100
            elif block.house_count == 6:
                total_sum += 130
        player.balance -= total_sum


class GoToJail:
    def __init__(self):
        self.card_text = 'Go directly to jail'

    def action(self, player):
        blocks = board.BLOCKS
        player.is_in_jail = True
        player.location = board.move_to_location(blocks, player, 10)


class GetOutOfJail:
    def __init__(self):
        self.card_ = 'Get out of jail FREE, this card may be kept until needed, or sold.'

    def action(self, player):
        player.is_in_jail = False
