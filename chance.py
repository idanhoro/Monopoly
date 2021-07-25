import board


class Chance():
    def __init__(self):
        deck = [AdvanceToGo(), MoveToBoardWalk(), AdvanceToIllinois(), AdvanceToCharlesPlaces(), TakeARide(),
                NearestRailroad(), NearestFacility(), GoBack(), Dividend(), BuildingMatures(), PoorTaxes(), Chairman(),
                GeneralRepairs(), GoToJail(), GetOutOfJail()]


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

    pass  # TODO: function to find nearest Railroad


class NearestFacility:
    def __init__(self):
        self.card_text = 'Advance token to nearest utility, if unowned you may buy it from the bank. if owned, throw dice and pay owner a total ten times the amount thrown'

    pass  # TODO: function to find nearest facility


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
        pass  # TODO: function to pay all the players from the current player


class GeneralRepairs:
    def __init__(self):
        self.card_text = 'Make general repairs on all your property for each house pay 25$ for each hotel 100$'

    def action(self, player):
        pass  # TODO: function to calculate the repairs costs


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
