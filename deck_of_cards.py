from tkinter import *

suits = ['club','heart','spade','diamond']
numbers = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack','queen','king']

hearts_values = {}
for suit in suits:
    for n in numbers:

class PlayingCard(Canvas):
    def __init__(self,number,suit):
        super().__init__(self)

class DeckOfCards():
    def __init__(self,gameValues):
        pass