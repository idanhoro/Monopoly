import deck as deck
import numpy as np

WIDTH = 1000
HEIGHT = 1000
BIG_BlOCK = 133
SMALL_BLOCK = 80


class Block:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None
        self.is_mortgage = False
        self.ID = None

    def buy(self, player):
        self.owner = player
        player.balance -= self.price

    def pay_rent(self, player, blocks: list[__init__]):
        pass

    def path(self, player):
        pass

    def mortgage(self, player):
        player.balance += BLOCKS[player.location].mortgage_value
        BLOCKS[player.location].is_mortgage = True


class Street(Block):
    def __init__(self, city, street_name, price, rent: int, rent_one_house, rent_two_house,
                 rent_three_house,
                 rent_four_house, rent_hotel, rent_sky_scraper, house_cost, mortgage_value, ID):
        super().__init__(street_name, price)
        self.rent_price = {0: rent * 2, 1: rent_one_house, 2: rent_two_house, 3: rent_three_house,
                           4: rent_four_house, 5: rent_hotel, 6: rent_sky_scraper}
        self.city = city
        self.price = price
        self.rent = rent
        self.house_cost = house_cost
        self.mortgage_value = mortgage_value
        self.house_count = 0
        self.ID = ID

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

    def buy_house(self, player):
        if player.house_count < 6:
            self.house_count += 1
            player.balance -= self.house_cost

    def sell_house(self, player):
        if player.house_count > 0:
            self.house_count -= 1
            player.balance += self.house_cost


class TrainStation(Block):
    def __init__(self, name, price, mortgage_value, rent, ID):
        super().__init__(name, price)
        self.mortgage_value = mortgage_value
        self.rent = rent
        self.ID = ID

    def pay_rent(self, player, blocks: list[Block]):
        pay_amount = self.rent
        for block in blocks:
            if isinstance(block, TrainStation) and block.owner == self.owner:
                pay_amount *= 2
        self.owner.balance += pay_amount
        player.balance -= pay_amount


class Facilities(Block):
    def __init__(self, name, price, mortgage_value, ID):
        super().__init__(name, price)
        self.mortgage_value = mortgage_value
        self.ID = ID

    def pay_rent(self, player, blocks: list[Block]):
        if self.owner.facilities_count == 1:
            self.owner.balance += player.last_roll * 4
            player.balance -= player.last_roll * 4
        if self.owner.facilities_count == 2:
            self.owner.balance += player.last_roll * 10
            player.balance -= player.last_roll * 10


class FreeParking(Block):
    def __init__(self, ID):
        self.ID = ID
        self.name = "FreeParking"


class Go(Block):
    def __init__(self, ID):
        self.ID = ID
        self.name = 'GO'

    def path(self, player):
        player.balance += 200


class Jail(Block):
    def __init__(self, ID):
        self.name = 'Jail'
        self.ID = ID

    def action(self, player):
        if player.is_in_jail:
            pass


class GoToJail(Block):
    def __init__(self, ID):
        self.name = 'GoToJail'
        self.ID = ID

    def action(self, player):
        player.location = 10


class CommunityChest(Block):
    def __init__(self, deck, ID):
        self.ID = ID


class Chance(Block):
    def __init__(self, deck, ID):
        self.ID = ID


class IncomeTax(Block):
    def __init__(self, ID):
        self.ID = ID

    def pay_tax(self, player):
        self.player.balance -= 200


class LuxuryTax(Block):
    def __init__(self, ID):
        self.ID = ID

    def pay_tax(self, player):
        self.player.balance -= 75


BLOCKS = [Go(ID=0),
          Street(city='purple', street_name='Mediterranean AVE.', price=60, rent=2, rent_one_house=10,
                 rent_two_house=30, rent_three_house=90, rent_four_house=160, rent_hotel=250,
                 rent_sky_scraper=750, house_cost=50, mortgage_value=30, ID=1),
          CommunityChest(deck, ID=2),
          Street(city='purple', street_name='Baltic Avenue', price=60, rent=4, rent_one_house=20,
                 rent_two_house=60, rent_three_house=180, rent_four_house=320, rent_hotel=450,
                 rent_sky_scraper=950, house_cost=50, mortgage_value=30, ID=3),
          IncomeTax(ID=4),
          TrainStation(name='Reading Railroad', price=200, mortgage_value=100, rent=25, ID=5),
          Street(city='light blue', street_name='Oriental Avenue', price=100, rent=6, rent_one_house=30,
                 rent_two_house=90, rent_three_house=270, rent_four_house=400, rent_hotel=550,
                 rent_sky_scraper=1050, house_cost=50, mortgage_value=50, ID=6),
          Chance(deck, ID=7),
          Street('light blue', street_name='Vermont Avenue', price=100, rent=6, rent_one_house=30,
                 rent_two_house=90, rent_three_house=270, rent_four_house=400, rent_hotel=550,
                 rent_sky_scraper=1050, house_cost=50, mortgage_value=50, ID=8),
          Street('light blue', street_name='Connecticut Avenue', price=120, rent=8, rent_one_house=40,
                 rent_two_house=100, rent_three_house=300, rent_four_house=450, rent_hotel=600,
                 rent_sky_scraper=1100, house_cost=50, mortgage_value=60, ID=9),
          Jail(ID=10),
          Street(city='pink', street_name='St. Charles Place', price=140, rent=10, rent_one_house=50,
                 rent_two_house=150, rent_three_house=450, rent_four_house=625, rent_hotel=750,
                 rent_sky_scraper=1250, house_cost=100, mortgage_value=70, ID=11),
          Facilities(name=' Electric Company', price=150, mortgage_value=75, ID=12),
          Street(city='pink', street_name='States Avenue', price=140, rent=10, rent_one_house=50,
                 rent_two_house=150, rent_three_house=450, rent_four_house=625, rent_hotel=750,
                 rent_sky_scraper=1250, house_cost=100, mortgage_value=70, ID=13),
          Street(city='pink', street_name='Virginia Avenue', price=160, rent=12, rent_one_house=60,
                 rent_two_house=180, rent_three_house=500, rent_four_house=700, rent_hotel=900,
                 rent_sky_scraper=1400, house_cost=100, mortgage_value=80, ID=14),
          TrainStation(name='Pennsylvania Railroad', price=200, mortgage_value=100, rent=25, ID=15),
          Street(city='orange', street_name='St.James Place', price=180, rent=14, rent_one_house=70,
                 rent_two_house=200, rent_three_house=550, rent_four_house=750, rent_hotel=950,
                 rent_sky_scraper=1450, house_cost=100, mortgage_value=90, ID=16),
          CommunityChest(deck, ID=17),
          Street(city='orange', street_name='Tennessee Avenue', price=180, rent=14, rent_one_house=70,
                 rent_two_house=200, rent_three_house=550, rent_four_house=750, rent_hotel=950,
                 rent_sky_scraper=1450, house_cost=100, mortgage_value=90, ID=18),
          Street(city='orange', street_name='New York Avenue', price=200, rent=16, rent_one_house=80,
                 rent_two_house=220, rent_three_house=600, rent_four_house=800, rent_hotel=1000,
                 rent_sky_scraper=1500, house_cost=100, mortgage_value=100, ID=19),
          FreeParking(ID=20),
          Street(city='red', street_name='Kentucky Avenue', price=220, rent=18, rent_one_house=90,
                 rent_two_house=250, rent_three_house=700, rent_four_house=875, rent_hotel=1050,
                 rent_sky_scraper=2050, house_cost=150, mortgage_value=110, ID=21),
          Chance(deck, ID=22),
          Street(city='red', street_name='Indiana Avenue', price=220, rent=18, rent_one_house=90,
                 rent_two_house=250, rent_three_house=700, rent_four_house=875, rent_hotel=1050,
                 rent_sky_scraper=2050, house_cost=150, mortgage_value=110, ID=23),
          Street(city='red', street_name='Illinois Avenue', price=240, rent=20, rent_one_house=100,
                 rent_two_house=300, rent_three_house=750, rent_four_house=925, rent_hotel=1100,
                 rent_sky_scraper=2100, house_cost=150, mortgage_value=120, ID=24),
          TrainStation(name='B.& O. Railroad', price=200, mortgage_value=100, rent=25, ID=25),
          Street(city='yellow', street_name='Atlantic Avenue', price=260, rent=22, rent_one_house=110,
                 rent_two_house=330, rent_three_house=800, rent_four_house=975, rent_hotel=1150,
                 rent_sky_scraper=2150, house_cost=150, mortgage_value=130, ID=26),
          Street(city='yellow', street_name='Ventnor Avenue', price=260, rent=22, rent_one_house=110,
                 rent_two_house=330, rent_three_house=800, rent_four_house=975, rent_hotel=1150,
                 rent_sky_scraper=2150, house_cost=150, mortgage_value=130, ID=27),
          Facilities(name='Water Works', price=150, mortgage_value=75, ID=28),
          Street(city='yellow', street_name='Marvin Gardens', price=280, rent=24, rent_one_house=120,
                 rent_two_house=360, rent_three_house=850, rent_four_house=1025, rent_hotel=1200,
                 rent_sky_scraper=2200, house_cost=150, mortgage_value=140, ID=29),
          GoToJail(ID=30),
          Street(city='green', street_name='Pacific Avenue', price=300, rent=26, rent_one_house=130,
                 rent_two_house=390, rent_three_house=900, rent_four_house=1100, rent_hotel=1275,
                 rent_sky_scraper=2275, house_cost=200, mortgage_value=150, ID=31),
          Street(city='green', street_name='North Carolina Avenue', price=300, rent=26, rent_one_house=130,
                 rent_two_house=390, rent_three_house=900, rent_four_house=1100, rent_hotel=1275,
                 rent_sky_scraper=2275, house_cost=200, mortgage_value=150, ID=32),
          CommunityChest(deck, ID=33),
          Street(city='green', street_name='Pennsylvania Avenue', price=320, rent=28, rent_one_house=150,
                 rent_two_house=450, rent_three_house=1000, rent_four_house=1200, rent_hotel=1400,
                 rent_sky_scraper=2400, house_cost=200, mortgage_value=160, ID=34),
          TrainStation(name='Short Line', price=200, mortgage_value=100, rent=25, ID=35),
          Chance(deck, ID=36),
          Street(city='blue', street_name='Park Place', price=350, rent=35, rent_one_house=175,
                 rent_two_house=500, rent_three_house=1100, rent_four_house=1300, rent_hotel=1500,
                 rent_sky_scraper=2500, house_cost=200, mortgage_value=175, ID=37),
          LuxuryTax(ID=38),
          Street(city='blue', street_name='Boardwalk', price=400, rent=50, rent_one_house=200,
                 rent_two_house=600, rent_three_house=1400, rent_four_house=1700, rent_hotel=2000,
                 rent_sky_scraper=3000, house_cost=200, mortgage_value=200, ID=39)]

PLAYERS = []


def move_player(player):
    player.location = (player.location + 1) % len(BLOCKS)
    BLOCKS[player.location].path(player)
    player.position = get_pos(player.location)
    print(player.location)


def move_to_location(blocks: list[Block], player, location):
    while player.location != location:
        player.location = (player.location + 1) % len(BLOCKS)
        blocks[player.location].path(player)


def get_pos(loc):
    if loc // 10 == 0:
        if loc % 10 == 0:
            return WIDTH - (BIG_BlOCK // 2), HEIGHT - (BIG_BlOCK // 2)
        return WIDTH - BIG_BlOCK - (SMALL_BLOCK * (loc % 10)) + (SMALL_BLOCK // 2), HEIGHT - (BIG_BlOCK // 2)

    if loc // 10 == 1:
        if loc % 10 == 0:
            return (BIG_BlOCK // 2), HEIGHT - (BIG_BlOCK // 2)
        return (BIG_BlOCK // 2), HEIGHT - BIG_BlOCK - (SMALL_BLOCK * (loc % 10)) + (SMALL_BLOCK // 2)

    if loc // 10 == 2:
        if loc % 10 == 0:
            return (BIG_BlOCK // 2), (BIG_BlOCK // 2)
        return BIG_BlOCK + (SMALL_BLOCK * (loc % 10)) - (SMALL_BLOCK // 2), (BIG_BlOCK // 2)

    if loc // 10 == 3:
        if loc % 10 == 0:
            return WIDTH - (BIG_BlOCK // 2), (BIG_BlOCK // 2)
        return WIDTH - (BIG_BlOCK // 2), BIG_BlOCK + (SMALL_BLOCK * (loc % 10)) - (SMALL_BLOCK // 2)
