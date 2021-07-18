class Street:
    def __init__(self, city, street_name, price, rent, rent_city_set, rent_one_house, rent_two_house, rent_three_house,
                 rent_four_house, rent_hotel, house_cost, mortgage_value):
        self.rent_price = {0: rent_city_set, 1: rent_one_house, 2: rent_two_house, 3: rent_three_house,
                           4: rent_four_house, 5: rent_hotel}
        self.street_name = street_name
        self.city = city
        self.price = price
        self.rent = rent
        self.house_cost = house_cost
        self.mortgage_value = mortgage_value
        self.house_count = 0
        self.owner = None


class TrainStation:
    def __init__(self, name, price, mortgage_value):
        self.name = name
        self.price = price
        self.owner = None
        self.mortgage_value = mortgage_value


class Facilities:
    def __init__(self, name, price, mortgage_value):
        self.name = name
        self.price = price
        self.mortgage_value = mortgage_value
        self.owner = None


class