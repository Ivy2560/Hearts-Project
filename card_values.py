from random import shuffle

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



# may or may not end up included
hearts_values_jack: dict = {('ace', 'club'): 0, (2, 'club'): 0, (3, 'club'): 0, (4, 'club'): 0,
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
                      (10, 'diamond'): 0, ('jack', 'diamond'): -10, ('queen', 'diamond'): 0, ('king', 'diamond'): 0}

