import random
import pygame
import numpy as np
import os

PIECE_SIZE = (75, 75)
players_images = {'Shoe': pygame.transform.scale(pygame.image.load(os.path.join('../images', 'shoe.png')), PIECE_SIZE),
                  'Dog': pygame.transform.scale(pygame.image.load(os.path.join('../images', 'dog.png')), PIECE_SIZE),
                  'Cat': pygame.transform.scale(pygame.image.load(os.path.join('../images', 'cat.png')), PIECE_SIZE),
                  'Iron': pygame.transform.scale(pygame.image.load(os.path.join('../images', 'iron.png')), PIECE_SIZE),
                  'Ship': pygame.transform.scale(pygame.image.load(os.path.join('../images', 'ship.png')), PIECE_SIZE),
                  'wheelbarrow': pygame.transform.scale(pygame.image.load(os.path.join('../images', 'wheelbarrow.png')),
                                                        PIECE_SIZE),
                  'thimble': pygame.transform.scale(pygame.image.load(os.path.join('../images', 'thimble.png')),
                                                    PIECE_SIZE)
                  }


class Player:
    def __init__(self, nickname, image_name):
        self.location = 0
        self.balance = 1500
        self.is_in_jail = False
        self.nickname = nickname
        self.last_roll = 0
        self.double_counter = 0
        self.position = np.array([925, 925])
        self.image = players_images[image_name]

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
