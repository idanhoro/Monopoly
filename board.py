from block import *


class Board:
    def __init__(self):
        blocks = [Go(),
                  Street(city='purple', street_name='Mediterranean AVE.', price=60, rent=2, rent_one_house=10,
                         rent_two_house=30, rent_three_house=90, rent_four_house=160, rent_hotel=250,
                         rent_sky_scraper=750, house_cost=50, mortgage_value=30),
                  ]
