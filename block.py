import block as block


class Block:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None

    def buy(self, player):
        self.owner = player

    def sell(self):
        pass

    def pay_rent(self, player, blocks: list[__init__]):
        pass

    def path(self, player):
        pass


class Street(Block):
    def __init__(self, city, street_name, price, rent: int, rent_one_house, rent_two_house,
                 rent_three_house,
                 rent_four_house, rent_hotel, rent_sky_scraper, house_cost, mortgage_value):
        super().__init__(street_name, price)
        self.rent_price = {0: rent * 2, 1: rent_one_house, 2: rent_two_house, 3: rent_three_house,
                           4: rent_four_house, 5: rent_hotel, 6: rent_sky_scraper}
        self.city = city
        self.price = price
        self.rent = rent
        self.house_cost = house_cost
        self.mortgage_value = mortgage_value
        self.house_count = 0

    def pay_rent(self, player, blocks: list[Block]):
        pay_amount = self.rent
        if self.check_full_set(blocks):
            pay_amount = self.rent_price[self.house_count]

        self.owner.balance += pay_amount
        player.balance -= pay_amount

    def check_full_set(self, blocks: list[Block]):
        for block in blocks:
            if isinstance(block, Street) and block.city == self.city and block.owner != self.owner:
                return False
        return True


class TrainStation(Block):
    def __init__(self, name, price, mortgage_value, rent):
        super().__init__(name, price)
        self.mortgage_value = mortgage_value
        self.rent = rent

    def pay_rent(self, player, blocks: list[Block]):
        pay_amount = self.rent
        for block in blocks:
            if isinstance(block, TrainStation) and block.owner == self.owner:
                pay_amount *= 2
        self.owner.balance += pay_amount
        player.balance -= pay_amount


class Facilities(Block):
    def __init__(self, name, price, mortgage_value):
        super().__init__(name, price)
        self.mortgage_value = mortgage_value

    def pay_rent(self, player, blocks: list[Block]):
        if self.owner.facilities_count == 1:
            self.owner.balance += player.last_roll * 4
            player.balance -= player.last_roll * 4
        if self.owner.facilities_count == 2:
            self.owner.balance += player.last_roll * 10
            player.balance -= player.last_roll * 10


class FreeParking(Block):
    def __init__(self, name):
        self.name = "FreeParking"


class Go(Block):
    def __init__(self):
        self.name = 'GO'

    def path(self, player):
        player.balance += 200


class Jail(Block):
    def __init__(self):
        self.name = 'Jail'

    def action(self, player):
        if player.is_in_jail:
            pass  # TODO:out of jail function


class GoToJail(Block):
    def __init__(self):
        self.name = 'GoToJail'

    def action(self, player):
        player.location = 10


class CommunityChest(block):
    def __init__(self, deck, player):
        pass


class Chance(block):
    def __init__(self, deck):
        pass


class IncomeTax(block):
    def __init__(self, player):
        self.player = player

    def pay_tax(self, player):
        self.player.balance -= 200


class LuxuryTax(block):
    def __init__(self, player):
        self.player = player

    def pay_tax(self, player):
        self.player.balance -= 75
