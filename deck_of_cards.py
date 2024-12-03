from tkinter import *
from card_values import card_suits, card_numbers, deck_list, hearts_values, hearts_values_jack

class PlayingCard(Canvas):
    def __init__(self,number,suit, value=False):
        if number not in card_numbers:
            raise ValueError('Invalid card number')
        if suit not in card_suits:
            raise ValueError('Invalid card suit')
        super().__init__(self)
        self.number = number
        self.suit = suit
        if not value:
            if type(self.number, int):
                self.value = value
            elif self.number == 'ace':
                self.value = 1
            elif self.number == 'ace':
                self.value = 1
            elif self.number == 'ace':
                self.value = 1

    def __str__(self):
        return f'{self.number} of {self.suit}s'




class DeckOfCards():
    def __init__(self,gameValues):
        pass