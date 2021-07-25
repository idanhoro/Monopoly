import random


class Player:
    def __init__(self, nickname):
        self.location = 0
        self.balance = 1500
        self.is_in_jail = False
        self.nickname = nickname
        self.last_roll = 0
        self.double_counter = 0

    def facilities_count(self, block_list):
        pass

    def roll_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.last_roll = dice1 + dice2
        if dice1 == dice2:
            self.double_counter += 1
        else:
            self.double_counter = 0


