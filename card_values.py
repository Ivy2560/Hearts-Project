from random import shuffle
from typing import Optional

card_suits: list = ['club','heart','spade','diamond']
card_numbers: list = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack','queen','king']

def make_deck_list() -> list:
    """
    Takes no variables. Returns a list where each element is a tuple
    representing a playing card. Tuples are of the form (number, suit)
    :return: list
    """
    output: list = []
    for suit in card_suits:
        for n in card_numbers:
            output.append((n,suit))
    return output

deck_list: list = [('ace', 'club'), (2, 'club'), (3, 'club'), (4, 'club'),
             (5, 'club'), (6, 'club'), (7, 'club'), (8, 'club'),
             (9, 'club'), (10, 'club'), ('jack', 'club'), ('queen', 'club'),
             ('king', 'club'), ('ace', 'heart'), (2, 'heart'), (3, 'heart'),
             (4, 'heart'), (5, 'heart'), (6, 'heart'), (7, 'heart'),
             (8, 'heart'), (9, 'heart'), (10, 'heart'), ('jack', 'heart'),
             ('queen', 'heart'), ('king', 'heart'), ('ace', 'spade'), (2, 'spade'),
             (3, 'spade'), (4, 'spade'), (5, 'spade'), (6, 'spade'),
             (7, 'spade'), (8, 'spade'), (9, 'spade'), (10, 'spade'),
             ('jack', 'spade'), ('queen', 'spade'), ('king', 'spade'), ('ace', 'diamond'),
             (2, 'diamond'), (3, 'diamond'), (4, 'diamond'), (5, 'diamond'),
             (6, 'diamond'), (7, 'diamond'), (8, 'diamond'), (9, 'diamond'),
             (10, 'diamond'), ('jack', 'diamond'), ('queen', 'diamond'), ('king', 'diamond')]



def make_hearts_values(jack_of_diamonds=False) -> dict:
    """
    Returns a dictionary where each key is a card and each value is the
    point number that card takes on in the card game hearts. If
    jack_of_diamonds is set to True, the jack of diamonds will be worth
    -10 points rather than 0 - as it is in a popular variation of the
    game.
    :param jack_of_diamonds: bool
    :return: dict
    """
    output: dict = {}
    for card in deck_list:
        if card[1] == 'heart':
            value: int = 1
        elif card == ('queen', 'spade'):
            value: int = 13
        else:
            value: int = 0
            if jack_of_diamonds and card == ('jack', 'diamond'):
                value: int = -10
        output[card] = value
    return output


hearts_values: dict = {('ace', 'club'): 0, (2, 'club'): 0, (3, 'club'): 0, (4, 'club'): 0,
                 (5, 'club'): 0, (6, 'club'): 0, (7, 'club'): 0, (8, 'club'): 0,
                 (9, 'club'): 0, (10, 'club'): 0, ('jack', 'club'): 0, ('queen', 'club'): 0,
                 ('king', 'club'): 0, ('ace', 'heart'): 1, (2, 'heart'): 1, (3, 'heart'): 1,
                 (4, 'heart'): 1, (5, 'heart'): 1, (6, 'heart'): 1, (7, 'heart'): 1,
                 (8, 'heart'): 1, (9, 'heart'): 1, (10, 'heart'): 1, ('jack', 'heart'): 1,
                 ('queen', 'heart'): 1, ('king', 'heart'): 1, ('ace', 'spade'): 0, (2, 'spade'): 0,
                 (3, 'spade'): 0, (4, 'spade'): 0, (5, 'spade'): 0, (6, 'spade'): 0,
                 (7, 'spade'): 0, (8, 'spade'): 0, (9, 'spade'): 0, (10, 'spade'): 0,
                 ('jack', 'spade'): 0, ('queen', 'spade'): 13, ('king', 'spade'): 0, ('ace', 'diamond'): 0,
                 (2, 'diamond'): 0, (3, 'diamond'): 0, (4, 'diamond'): 0, (5, 'diamond'): 0,
                 (6, 'diamond'): 0, (7, 'diamond'): 0, (8, 'diamond'): 0, (9, 'diamond'): 0,
                 (10, 'diamond'): 0, ('jack', 'diamond'): 0, ('queen', 'diamond'): 0, ('king', 'diamond'): 0}

hearts_card_order_list: list = [(2, 'club'), (3, 'club'), (4, 'club'), (5, 'club'),
                                (6, 'club'), (7, 'club'), (8, 'club'), (9, 'club'),
                                (10, 'club'), ('jack', 'club'), ('queen', 'club'), ('king', 'club'),
                                ('ace', 'club'),
                                (2, 'diamond'), (3, 'diamond'), (4, 'diamond'), (5, 'diamond'),
                                (6, 'diamond'), (7, 'diamond'), (8, 'diamond'), (9, 'diamond'),
                                (10, 'diamond'), ('jack', 'diamond'), ('queen', 'diamond'), ('king', 'diamond'),
                                ('ace', 'diamond'),
                                (2, 'spade'), (3, 'spade'), (4, 'spade'), (5, 'spade'),
                                (6, 'spade'), (7, 'spade'), (8, 'spade'), (9, 'spade'),
                                (10, 'spade'), ('jack', 'spade'), ('queen', 'spade'), ('king', 'spade'),
                                ('ace', 'spade'),
                                (2, 'heart'), (3, 'heart'), (4, 'heart'), (5, 'heart'),
                                (6, 'heart'), (7, 'heart'), (8, 'heart'), (9, 'heart'),
                                (10, 'heart'), ('jack', 'heart'), ('queen', 'heart'), ('king', 'heart'),
                                ('ace', 'heart')]

def make_hearts_order_dict():
    """
    Creates a dictionary consisting of the order cards should
    be shown in a player's hand in the card game hearts
    :return: dict
    """
    output: dict = {}
    for n in range(1,53):
        card: tuple = hearts_card_order_list[n-1]
        output[card] = n
    return output


hearts_card_order: dict = {(2, 'club'): 1, (3, 'club'): 2, (4, 'club'): 3, (5, 'club'): 4,
                           (6, 'club'): 5, (7, 'club'): 6, (8, 'club'): 7, (9, 'club'): 8,
                           (10, 'club'): 9, ('jack', 'club'): 10, ('queen', 'club'): 11, ('king', 'club'): 12,
                           ('ace', 'club'): 13,
                           (2, 'diamond'): 14, (3, 'diamond'): 15, (4, 'diamond'): 16, (5, 'diamond'): 17,
                           (6, 'diamond'): 18, (7, 'diamond'): 19, (8, 'diamond'): 20, (9, 'diamond'): 21,
                           (10, 'diamond'): 22, ('jack', 'diamond'): 23, ('queen', 'diamond'): 24, ('king', 'diamond'): 25,
                           ('ace', 'diamond'): 26,
                           (2, 'spade'): 27, (3, 'spade'): 28, (4, 'spade'): 29, (5, 'spade'): 30,
                           (6, 'spade'): 31, (7, 'spade'): 32, (8, 'spade'): 33, (9, 'spade'): 34,
                           (10, 'spade'): 35, ('jack', 'spade'): 36, ('queen', 'spade'): 37, ('king', 'spade'): 38,
                           ('ace', 'spade'): 39,
                           (2, 'heart'): 40, (3, 'heart'): 41, (4, 'heart'): 42, (5, 'heart'): 43,
                           (6, 'heart'): 44, (7, 'heart'): 45, (8, 'heart'): 46, (9, 'heart'): 47,
                           (10, 'heart'): 48, ('jack', 'heart'): 49, ('queen', 'heart'): 50, ('king', 'heart'): 51,
                           ('ace', 'heart'): 52}



### BELOW DOESNT HAVE DOC STRING OR TYPE HINTING



def highest_hearts(cards: list, suit: str) -> tuple:
    """
    Returns the highest ranking card in the game hearts in
    the list cards of the provided suit. Returns None if
    there are no cards in list cards of the provided suit
    :param cards: list
    :param suit: str
    :return: tuple
    """
    highest: Optional[tuple] = None
    for card in cards:
        if card[1] != suit:
            continue
        elif highest is None:  # and card[1] == suit
            highest = card
        else:  # we need to compare
            if hearts_card_order[highest] < hearts_card_order[card]:
                highest = card
    return highest
