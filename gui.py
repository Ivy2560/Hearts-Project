from tkinter import *
from card_values import *
from deck_of_cards import PlayingCard

class Gui:
    def __init__(self,window):
        """

        :param window:
        """
        self.window = window

        # game play attributes
        # toggleable by user
        self.num_players = 3
        self.points_till_loss = 100
        self.jack_of_diamonds = False
        self.players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
        # player dicts
        self.points_dict = {p:0 for p in self.players}
        self.hands_dict = {p:[] for p in self.players} # list so sortable
        self.cards_taken = {p:set() for p in self.players}
        self.round_points_dict = {p:0 for p in self.players}
        # other
        self.current_player = self.players[0]
        self.round_number = 1
        self.can_play_hearts = False
        self.selected_card = None

        self.start_screen()

    def start_screen(self):
        self.buttons_frame = Frame(self.window)

        self.start_game = Button(self.buttons_frame, text='START GAME', command=self.play_game)
        self.game_options = Button(self.buttons_frame, text='Options')
        self.game_instructions = Button(self.buttons_frame, text='Instructions')
        self.game_stats = Button(self.buttons_frame, text='Local Stats')
        #
        self.start_game.pack(side='top')
        self.game_options.pack(side='top')
        self.game_instructions.pack(side='top')
        self.game_stats.pack(side='top')
        self.buttons_frame.grid(row=100, column=100)


    def max_points(self):
        return max(self.points_dict.values())

    def sort_hand(self, player):
        hand = self.hands_dict[player]
        for num_passes in range(len(hand)-1):
            has_swapped = False
            for i in range(len(hand)-1-num_passes):
                card_1 = hearts_card_order[hand[i]]
                card_2 = hearts_card_order[hand[i+1]]
                if card_1 > card_2:
                    has_swapped = True
                    hand = hand[:i] + [hand[i+1], hand[i]] + hand[i+2:]
            if not has_swapped:
                break
        self.hands_dict[player] = hand

    def deal_cards(self):
        shuffled_deck = deck_list.copy()
        if self.num_players != 4:
            shuffled_deck.remove((2,'diamond'))
            if self.num_players == 5:
                shuffled_deck.remove((2,'club'))
        # DOUBLE CHECK LATER
        hand_size = len(shuffled_deck) // self.num_players
        shuffle(shuffled_deck)
        for player in self.players:
            self.hands_dict[player] = shuffled_deck[:hand_size]
            shuffled_deck = shuffled_deck[hand_size:]
        #
        # sort hands
        for player in self.players:
            self.sort_hand(player)
        print(self.hands_dict)
        print('VERY IMPORTANT! We need a redeal feature after the passing phase for if delt only point cards for 5 player hearts ')


    def passing_phase(self):
        pass_indicator = self.round_number % 4
        if pass_indicator == 1:  # pass to right
            pass
        elif pass_indicator == 2:  # pass to left
            pass
        elif pass_indicator == 3:  # pass across
            pass
        else:  # pass_indicator == 0: # no pass
            pass

    def next_player(self):
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % self.num_players
        next_player = self.players[next_index]
        return next_player

    def select_card(self, event):
        card = event.widget
        print(card)
        if card.can_play:
            self.selected_card = card
            print(self.selected_card)

    def play_card(self):
        if self.selected_card is not None and self.selected_card.get_can_play():
            card_value = self.selected_card.get_value()
            card_tuple = self.selected_card.get_card()
            self.hands_dict[self.current_player].remove(card_tuple)
            self.points_dict[self.current_player] += card_value
            #
            self.selected_card.destroy()
            self.selected_card = None
            self.current_player = self.next_player()
            self.next_turn_button = Button(self.window)

    def play_turn(self, trick_suit, first_trick=False):
        ##
        # add logic for show hand button
        ##
        first_of_trick = trick_suit is None
        force_suit = False
        if not first_of_trick:
            for card in self.hands_dict[self.current_player]:
                if card[1] == trick_suit:
                    force_suit = True
                    break
        #
        self.hand_frame = Frame(self.window)
        card_displays = []
        for card in self.hands_dict[self.current_player]:
            # logic for if cards are playable
            if first_of_trick:
                if first_trick:
                    if self.num_players != 5:
                        can_play = card == (2, 'club')
                    else: # self.num_players != 5
                        can_play = card == (3, 'club')
                else: # first of trick but not first trick
                    # we have to check if hearts are playable, but not
                    # if queen of spades is cus its not the first trick
                    if not self.can_play_hearts:
                        can_play = card[1] != 'heart'
                    else:
                        can_play = True
            elif force_suit:
                # don't have to check for Q of spades because first
                # trick suit will never be spades
                can_play = card[1] == trick_suit
            else: # they don't have the suit a
                if first_trick:
                    can_play = (card != ('queen', 'spades')) and (card[1] != 'heart')
                else:
                    can_play = True
            #
            #
            value = hearts_values[card]
            new_card = PlayingCard(self.hand_frame, card, can_play, value)
            new_card.bind('<Button-1>', self.select_card)
            card_displays.append(new_card)
            new_card.pack(side='left')
        self.hand_frame.pack(side='bottom')
        #
        self.play_card_button = Button(self.hand_frame,text='Play Selected Card',command=self.play_card)
        self.pack


    def play_trick(self, first_trick=False):
        # a trick won't always start with the same player
        self.play_turn(None, first_trick)

    def play_round(self):
        self.round_points_dict = {p: 0 for p in self.players}
        self.can_play_hearts = False
        #
        self.deal_cards()
        self.passing_phase()
        ##### passing phase does nothing right now
        starting_card = (2,'club')
        if self.num_players == 5:
            starting_card = (3, 'club')
        for (player,hand) in self.hands_dict.items():
            if starting_card in hand:
                self.current_player = player
                break
        #
        self.play_trick(True) # first trick when Q of spades can't be played
        while len(self.hands_dict[self.players[0]]) > 0:
            self.play_trick()
        #
        if 26 in self.round_points_dict.values():
            for (player, points) in self.round_points_dict.items():
                if points == 26:
                    continue
                else:
                    self.points_dict[player] += 26
        else:
            for (player, points) in self.round_points_dict.items():
                self.points_dict[player] += points



    def play_game(self):
        self.buttons_frame.destroy()
        self.points_dict = {p: 0 for p in self.players}
        self.round_number = 1
        while self.max_points() < self.points_till_loss:
            self.play_round()
            break



