from tkinter import *
from card_values import card_suits, card_numbers, deck_list, hearts_values, hearts_values_jack

#class DrawShapes:
#    @staticmethod
#    def draw_diamond():

class PlayingCard(Canvas):
    def __init__(self, master, number, suit, can_play=True, value=False):
        if number not in card_numbers:
            raise ValueError('Invalid card number')
        if suit not in card_suits:
            raise ValueError('Invalid card suit')
        #
        if can_play:
            card_color = 'white'
        else: # not can_play
            card_color = 'grey'
        super().__init__(master, width=5*30,height=7*30,
                         bg=card_color,bd=3, relief='sunken')
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
    #
    def draw_diamond (self,x,y, color):
        coordinates = [x,y-14, x+7,y, x,y+14, x-7,y]
        self.create_polygon(coordinates, fill=color)

    def draw_heart(self,x,y,color):
        coordinates_1 = [x-8,y-14, x,y] # bounding box is for the circle
        self.create_arc(coordinates_1,start=0,extent=185,fill=color, outline=color)
        coordinates_2 = [x,y-14, x+8,y]
        self.create_arc(coordinates_2, start=-5, extent=185, fill=color, outline=color)
        coordinates_3 = [x-8,y-9, x+9,y-9, x,y+13]
        self.create_polygon(coordinates_3, fill=color)

    def draw_club(self,x, y, color):
        coordinates_1 = [x-5,y-13, x+5,y-3]
        self.create_oval(coordinates_1, fill=color)
        coordinates_2 = [x-10,y-4, x,y+6]
        self.create_oval(coordinates_2, fill=color)
        coordinates_3 = [x,y-4, x+10,y+6]
        self.create_oval(coordinates_3, fill=color)
        #
        coordinates_4 = [x,y-9, x+4,y+1, x-4,y+1]
        self.create_polygon(coordinates_4, fill=color)
        coordinates_5 = [x,y, x+4,y+12, x-4,y+12]
        self.create_polygon(coordinates_5, fill=color)

    def draw_A(self,x,y, color):
        coordinates_1 = [x,y+25, x+3,y+25, x+5,y+16, x+9,y+16, x+11,y+25,x+14,y+25,
                       x+9,y, x+5,y]
        self.create_polygon(coordinates_1, fill=color)
        coordinates_2 = [x+5,y+12, x+9,y+12, x+7,y+4]
        self.create_polygon(coordinates_2, fill= self['background'])

    #
    def draw_card(self):
        pass


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

my_card.draw_A(12,12, 'black')
#my_card.draw_diamond(19,57, 'red')
my_card.draw_club(19,57, 'black')
#my_card.draw_heart(80,30)




window.mainloop()