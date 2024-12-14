from tkinter import *
from card_values import card_suits, card_numbers, deck_list
from typing import Union

class PlayingCard(Canvas):
    def __init__(self, master: Tk, card: tuple, can_play: bool=True, value: Union[int,str,None]=None):
        """
        Creates an instance of a Playing card canvas
        :param master: Tk
        :param card: tuple
        :param can_play: bool
        :param value:
        """
        (number, suit) = card
        if number not in card_numbers:
            raise ValueError('Invalid card number')
        if suit not in card_suits:
            raise ValueError('Invalid card suit')
        #
        if can_play:
            card_color = 'white'
        else: # not can_play
            card_color = 'grey'
        super().__init__(master, width=5*10,height=7*10,
                         bg=card_color,bd=3, relief='sunken')
        self.number = number
        self.suit = suit
        #
        self.can_play = can_play
        #
        if value is None:
            if type(self.number) == int or self.number in ['2','3','4','5','6','7','8','9','10']:
                self.value = int(self.number)
            elif self.number == 'ace':
                self.value = 1
            elif self.number in ['jack','queen','king']:
                self.value = 10
        else:
            self.value = value

        self.draw_card()

    #
    def draw_diamond (self,x: int,y: int, color: str) -> None:
        """
        Draws a diamond centered at x,y on the canvas
        :param x: int
        :param y: int
        :param color: str
        :return: None
        """
        coordinates = [x,y-14, x+7,y, x,y+14, x-7,y]
        self.create_polygon(coordinates, fill=color)

    def draw_heart(self,x: int,y: int,color: str) -> None:
        """
        Draws a heart centered at x,y on the canvas
        :param x: int
        :param y: int
        :param color: str
        :return: None
        """
        coordinates_1 = [x,y+10, x+10,y-1, x-9,y-1]
        self.create_polygon(coordinates_1, fill=color)
        coordinates_2 = [x,y+12, x+8,y-2, x-8,y-2]
        self.create_polygon(coordinates_2, fill=color)
        #
        coordinates_3 = [x-10,y, x,y-10]
        self.create_oval(coordinates_3, fill=color, outline=color)
        coordinates_4 = [x,y, x+10,y-10]
        self.create_oval(coordinates_4, fill=color, outline=color)

    def draw_club(self,x: int, y: int, color: str) -> None:
        """
        Draws a club centered at x,y on the canvas
        :param x: int
        :param y: int
        :param color: str
        :return: None
        """
        coordinates_1 = [x-5,y-13, x+5,y-3]
        self.create_oval(coordinates_1, fill=color, outline=color)
        coordinates_2 = [x-10,y-4, x,y+6]
        self.create_oval(coordinates_2, fill=color, outline=color)
        coordinates_3 = [x,y-4, x+10,y+6]
        self.create_oval(coordinates_3, fill=color, outline=color)
        #
        coordinates_4 = [x,y-9, x+4,y+1, x-4,y+1]
        self.create_polygon(coordinates_4, fill=color)
        coordinates_5 = [x,y, x+4,y+12, x-4,y+12]
        self.create_polygon(coordinates_5, fill=color)

    def draw_spade(self, x: int, y: int, color: str) -> None:
        """
        Draws a spade centered at x,y on the canvas
        :param x: int
        :param y: int
        :param color: str
        :return: None
        """
        coordinates_1 = [x,y-9, x+9,y-2, x-9,y-2]
        self.create_polygon(coordinates_1, fill=color)
        coordinates_2 = [x,y-12, x+7,y, x-7,y]
        self.create_polygon(coordinates_2, fill=color)
        #
        coordinates_3 = [x-10,y-3, x,y+7]
        self.create_oval(coordinates_3, fill=color, outline=color)
        coordinates_4 = [x,y-3, x+10,y+7]
        self.create_oval(coordinates_4, fill=color, outline=color)
        #
        coordinates_5 = [x,y+1, x+4,y+11, x-4,y+11]
        self.create_polygon(coordinates_5, fill=color)

    def draw_char(self,x: int, y: int, char: str, color: str) -> None:
        """
        Draws a character centered at x,y on the canvas
        :param x: int
        :param y: int
        :param char: str
        :param color: str
        :return: None
        """
        self.create_text([x,y], text=str(char), fill=color, font=('Helvetica 28'))

    #
    def draw_card(self) -> None:
        """
        Draws the card suit and number
        :return: None
        """
        if self.suit == 'club':
            color = 'black'
            self.draw_club(20, 55, color)
        elif self.suit == 'heart':
            color = 'red'
            self.draw_heart(20, 55, color)
        elif self.suit == 'spade':
            color = 'black'
            self.draw_spade(20, 55, color)
        else: # self.suit == 'diamond':
            color = 'red'
            self.draw_diamond(20, 55, color)

        if type(self.number) == str: # A, J, Q, K
            char = self.number[0].upper()
        else:
            char = str(self.number)
        self.draw_char(20,25,char, color)

    def get_value(self) -> int:
        """
        Returns the cards numeric value
        :return: int
        """
        return self.value

    def get_card(self) -> tuple:
        """
        returns the cards number and suit as a tuple
        :return: tuple
        """
        return (self.number, self.suit)

    def get_can_play(self) -> bool:
        """
        returns whether or not a card can be played
        :return: bool
        """
        return self.can_play

    def __str__(self) -> str:
        """
        Overrides default __str__ function
        :return: str
        """
        return f'{self.number} of {self.suit}s'

"""
window = Tk()
window.title('Hearts')
window.geometry('1000x700')

def show_cards(start_card):
    for c in range(6):
        for r in range(3):
            i = c+1 + 6*r - 1 + start_card-1
            if i >= 52:
                break
            my_card = PlayingCard(window,(deck_list[i]))
            my_card.grid(row=r,column=c)

show_cards(1)

window.mainloop()
"""
