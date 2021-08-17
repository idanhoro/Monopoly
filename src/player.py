import random
import pygame
import numpy as np
import os
import sys
from board import get_pos

print(sys.path)
PIECE_SIZE = (65, 65)
players_images = {'Shoe': pygame.transform.scale(pygame.image.load(os.path.join('./images', 'shoe.png')), PIECE_SIZE),
                  'Dog': pygame.transform.scale(pygame.image.load(os.path.join('./images', 'dog.png')), PIECE_SIZE),
                  'Cat': pygame.transform.scale(pygame.image.load(os.path.join('./images', 'cat.png')), PIECE_SIZE),
                  'Iron': pygame.transform.scale(pygame.image.load(os.path.join('./images', 'iron.png')), PIECE_SIZE),
                  'Ship': pygame.transform.scale(pygame.image.load(os.path.join('./images', 'ship.png')), PIECE_SIZE),
                  'wheelbarrow': pygame.transform.scale(pygame.image.load(os.path.join('./images', 'wheelbarrow.png')),
                                                        PIECE_SIZE),
                  'thimble': pygame.transform.scale(pygame.image.load(os.path.join('./images', 'thimble.png')),
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
        self.position = get_pos(0)
        self.image = players_images[image_name]
        self.dice1 = 1
        self.dice2 = 1
        self.target_location = 0

    def facilities_count(self, block_list):
        pass

    def roll_dice(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.last_roll = self.dice1 + self.dice2
        if self.dice1 == self.dice2:
            self.double_counter += 1
        else:
            self.double_counter = 0
