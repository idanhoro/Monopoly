import deck as deck

from block import *

BLOCKS = [Go(),
          Street(city='purple', street_name='Mediterranean AVE.', price=60, rent=2, rent_one_house=10,
                 rent_two_house=30, rent_three_house=90, rent_four_house=160, rent_hotel=250,
                 rent_sky_scraper=750, house_cost=50, mortgage_value=30),
          CommunityChest(deck),
          Street(city='purple', street_name='Baltic Avenue', price=60, rent=4, rent_one_house=20,
                 rent_two_house=60, rent_three_house=180, rent_four_house=320, rent_hotel=450,
                 rent_sky_scraper=950, house_cost=50, mortgage_value=30),
          IncomeTax(),
          TrainStation(name='Reading Railroad', price=200, mortgage_value=100, rent=25),
          Street(city='light blue', street_name='Oriental Avenue', price=100, rent=6, rent_one_house=30,
                 rent_two_house=90, rent_three_house=270, rent_four_house=400, rent_hotel=550,
                 rent_sky_scraper=1050, house_cost=50, mortgage_value=50),
          Chance(deck),
          Street('light blue', street_name='Vermont Avenue', price=100, rent=6, rent_one_house=30,
                 rent_two_house=90, rent_three_house=270, rent_four_house=400, rent_hotel=550,
                 rent_sky_scraper=1050, house_cost=50, mortgage_value=50),
          Street('light blue', street_name='Connecticut Avenue', price=120, rent=8, rent_one_house=40,
                 rent_two_house=100, rent_three_house=300, rent_four_house=450, rent_hotel=600,
                 rent_sky_scraper=1100, house_cost=50, mortgage_value=60),
          Jail(),
          Street(city='pink', street_name='St. Charles Place', price=140, rent=10, rent_one_house=50,
                 rent_two_house=150, rent_three_house=450, rent_four_house=625, rent_hotel=750,
                 rent_sky_scraper=1250, house_cost=100, mortgage_value=70),
          Facilities(name=' Electric Company', price=150, mortgage_value=75),
          Street(city='pink', street_name='States Avenue', price=140, rent=10, rent_one_house=50,
                 rent_two_house=150, rent_three_house=450, rent_four_house=625, rent_hotel=750,
                 rent_sky_scraper=1250, house_cost=100, mortgage_value=70),
          Street(city='pink', street_name='Virginia Avenue', price=160, rent=12, rent_one_house=60,
                 rent_two_house=180, rent_three_house=500, rent_four_house=700, rent_hotel=900,
                 rent_sky_scraper=1400, house_cost=100, mortgage_value=80),
          TrainStation(name='Pennsylvania Railroad', price=200, mortgage_value=100, rent=25),
          Street(city='orange', street_name='St.James Place', price=180, rent=14, rent_one_house=70,
                 rent_two_house=200, rent_three_house=550, rent_four_house=750, rent_hotel=950,
                 rent_sky_scraper=1450, house_cost=100, mortgage_value=90),
          CommunityChest(deck),
          Street(city='orange', street_name='Tennessee Avenue', price=180, rent=14, rent_one_house=70,
                 rent_two_house=200, rent_three_house=550, rent_four_house=750, rent_hotel=950,
                 rent_sky_scraper=1450, house_cost=100, mortgage_value=90),
          Street(city='orange', street_name='New York Avenue', price=200, rent=16, rent_one_house=80,
                 rent_two_house=220, rent_three_house=600, rent_four_house=800, rent_hotel=1000,
                 rent_sky_scraper=1500, house_cost=100, mortgage_value=100),
          FreeParking(),
          Street(city='red', street_name='Kentucky Avenue', price=220, rent=18, rent_one_house=90,
                 rent_two_house=250, rent_three_house=700, rent_four_house=875, rent_hotel=1050,
                 rent_sky_scraper=2050, house_cost=150, mortgage_value=110),
          Chance(deck),
          Street(city='red', street_name='Indiana Avenue', price=220, rent=18, rent_one_house=90,
                 rent_two_house=250, rent_three_house=700, rent_four_house=875, rent_hotel=1050,
                 rent_sky_scraper=2050, house_cost=150, mortgage_value=110),
          Street(city='red', street_name='Illinois Avenue', price=240, rent=20, rent_one_house=100,
                 rent_two_house=300, rent_three_house=750, rent_four_house=925, rent_hotel=1100,
                 rent_sky_scraper=2100, house_cost=150, mortgage_value=120),
          TrainStation(name='B.& O. Railroad', price=200, mortgage_value=100, rent=25),
          Street(city='yellow', street_name='Atlantic Avenue', price=260, rent=22, rent_one_house=110,
                 rent_two_house=330, rent_three_house=800, rent_four_house=975, rent_hotel=1150,
                 rent_sky_scraper=2150, house_cost=150, mortgage_value=130),
          Street(city='yellow', street_name='Ventnor Avenue', price=260, rent=22, rent_one_house=110,
                 rent_two_house=330, rent_three_house=800, rent_four_house=975, rent_hotel=1150,
                 rent_sky_scraper=2150, house_cost=150, mortgage_value=130),
          Facilities(name='Water Works', price=150, mortgage_value=75),
          Street(city='yellow', street_name='Marvin Gardens', price=280, rent=24, rent_one_house=120,
                 rent_two_house=360, rent_three_house=850, rent_four_house=1025, rent_hotel=1200,
                 rent_sky_scraper=2200, house_cost=150, mortgage_value=140),
          GoToJail(),
          Street(city='green', street_name='Pacific Avenue', price=300, rent=26, rent_one_house=130,
                 rent_two_house=390, rent_three_house=900, rent_four_house=1100, rent_hotel=1275,
                 rent_sky_scraper=2275, house_cost=200, mortgage_value=150),
          Street(city='green', street_name='North Carolina Avenue', price=300, rent=26, rent_one_house=130,
                 rent_two_house=390, rent_three_house=900, rent_four_house=1100, rent_hotel=1275,
                 rent_sky_scraper=2275, house_cost=200, mortgage_value=150),
          CommunityChest(deck),
          Street(city='green', street_name='Pennsylvania Avenue', price=320, rent=28, rent_one_house=150,
                 rent_two_house=450, rent_three_house=1000, rent_four_house=1200, rent_hotel=1400,
                 rent_sky_scraper=2400, house_cost=200, mortgage_value=160),
          TrainStation(name='Short Line', price=200, mortgage_value=100, rent=25),
          Chance(deck),
          Street(city='blue', street_name='Park Place', price=350, rent=35, rent_one_house=175,
                 rent_two_house=500, rent_three_house=1100, rent_four_house=1300, rent_hotel=1500,
                 rent_sky_scraper=2500, house_cost=200, mortgage_value=175),
          LuxuryTax(),
          Street(city='blue', street_name='Boardwalk', price=400, rent=50, rent_one_house=200,
                 rent_two_house=600, rent_three_house=1400, rent_four_house=1700, rent_hotel=2000,
                 rent_sky_scraper=3000, house_cost=200, mortgage_value=200)]


#
# class Board:
#     def __init__(self):
#         self.blocks =

def move_player(blocks: list[Block], player):
    player.roll_dice()
    for i in range(player.last_roll):
        player.location += 1
        blocks[player.location].path(player)


def move_to_location(blocks: list[Block], player, location):
    while player.location != location:
        player.location += 1
        blocks[player.location].path(player)
