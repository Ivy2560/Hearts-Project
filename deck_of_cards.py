from tkinter import *
from card_values import card_suits, card_numbers, deck_list, hearts_values, hearts_values_jack


class PlayingCard(Canvas):
    def __init__(self, master, number, suit, can_play=True, value=False):
        if number not in card_numbers:
            raise ValueError('Invalid card number')
        if suit not in card_suits:
            raise ValueError('Invalid card suit')
        #
        super().__init__(master, width=5*30,height=7*30,
                         bg='white',bd=3, relief='sunken')
        self.number = number
        self.suit = suit
        #
        self.can_play = can_play
        #
        if value == False:
            if type(self.number) == int:
                self.value = value
            elif self.number == 'ace':
                self.value = 1
            elif self.number in ['jack','queen','king']:
                self.value = 10
        else:
            self.value = value

        self.draw_card()
        self.bind('Button-1',self.card_selected)

    def card_selected(self,event):
        if self.can_play:
            return_value = self.value
            self.delete()
            return return_value

    def draw_card(self):


    def __str__(self):
        return f'{self.number} of {self.suit}s'


class DeckOfCards():
    def __init__(self,gameValues):
        pass


window = Tk()
window.title('Hearts')
window.geometry('1000x700')
my_card = PlayingCard(window,'ace','spade')
my_card.grid(row=0,column=0)


window.mainloop()