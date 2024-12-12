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
        self.player_label_positions = [('bottom','center'),
                                       ('left','center'),
                                       ('top','nw'),
                                       ('top','ne'),
                                       ('right','center')]
        self.player_labels = []
        # toggleable by user
        self.num_players = 5
        self.points_till_loss = 100
        self.jack_of_diamonds = False
        self.players = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5']
        # player dicts
        self.points_dict = {p:0 for p in self.players}
        # round update
        self.hands_dict = {p:[] for p in self.players} # list so sortable
        self.round_points_dict = {p:0 for p in self.players}
        self.current_player = self.players[0]
        self.round_number = 0
        self.can_play_hearts = False
        self.selected_card = None
        #
        self.trick_suit = None
        self.first_trick = True
        self.turns_played = 0
        self.cards_on_table = {}

        self.start_screen()

    def start_screen(self):
        self.buttons_frame = Frame(self.window)

        self.start_game = Button(self.buttons_frame, text='START GAME', command=self.play_game)
        self.game_options = Button(self.buttons_frame, text='Options')
        self.game_instructions = Button(self.buttons_frame, text='Instructions')
        self.game_stats = Button(self.buttons_frame, text='Local Stats')
        # back button runs init
        #
        self.start_game.pack(side='top')
        self.game_options.pack(side='top')
        self.game_instructions.pack(side='top')
        self.game_stats.pack(side='top')
        self.buttons_frame.pack(side='bottom',anchor='center')


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
        no_redeal = True
        for hand in self.hands_dict.values():
            has_playable = False
            for card in hand:
                if card != ('queen','spade') or card[1] != 'heart':
                    has_playable = True
                    break
            no_redeal = no_redeal and has_playable
        if not no_redeal:
            self.hands_dict = {p: [] for p in self.players}
            self.deal_cards()

        #
        # sort hands
        for player in self.players:
            self.sort_hand(player)


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

    def change_current_player(self, player):
        self.current_player = player
        order = []
        first_index = self.players.index(self.current_player)
        for n in range(self.num_players):
            player_index = (first_index + n) % self.num_players
            order.append(self.players[player_index])
        #
        for i in range(self.num_players):
            print("got here")
            p = order[i]
            self.player_labels[i].config(text=f'{p}: {self.round_points_dict[p]} points')



    def next_player(self):
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % self.num_players
        next_player = self.players[next_index]
        self.change_current_player(next_player)



    def select_card(self, event):
        card = event.widget
        if card.can_play:
            self.selected_card = card

    def play_card(self):
        if self.selected_card is not None: # checked for playable in select_card
            #
            card_tuple = self.selected_card.get_card()
            #
            if card_tuple == ('queen', 'spade') or card_tuple[1] == 'heart':
                self.can_play_hearts = True
            #
            self.hands_dict[self.current_player].remove(card_tuple)
            self.cards_on_table[card_tuple] = self.current_player
            if self.trick_suit is None:
                self.trick_suit = card_tuple[1]
            #
            self.hand_frame.destroy()
            self.selected_card = None
            self.next_player()
            print(self.turns_played)
            if self.turns_played % self.num_players == 0:
                if len(self.hands_dict[self.players[0]]) == 0:
                    self.finish_round()
                    return
                else:
                    winning_card = highest_hearts(list(self.cards_on_table.keys()), self.trick_suit)
                    winning_player = self.cards_on_table[winning_card]
                    for card in self.cards_on_table:
                        self.round_points_dict[winning_player] += hearts_values[card]
                    #
                    self.change_current_player(winning_player)
                    self.trick_suit = None
                    self.cards_on_table = {}
                    self.first_trick = False
            self.next_turn_button = Button(self.window, text=f'Start next turn({self.current_player})', command=self.play_turn)
            self.next_turn_button.pack(side='bottom')

    def play_turn(self):
        self.next_turn_button.destroy()
        self.turns_played += 1
        ##
        first_of_trick = self.trick_suit is None
        force_suit = False
        if not first_of_trick:
            for card in self.hands_dict[self.current_player]:
                if card[1] == self.trick_suit:
                    force_suit = True
                    break
        #
        self.hand_frame = Frame(self.window)
        #
        self.play_card_button = Button(self.hand_frame,text='Play Selected Card',command=self.play_card)
        self.play_card_button.pack(side='top',anchor='w')
        #
        card_displays = []
        for card in self.hands_dict[self.current_player]:
            # logic for if cards are playable
            if first_of_trick:
                if self.first_trick:
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
                can_play = card[1] == self.trick_suit
            else: # they don't have the suit a
                if self.first_trick:
                    can_play = (card != ('queen', 'spade')) and (card[1] != 'heart')
                else:
                    can_play = True
            #
            new_card = PlayingCard(self.hand_frame, card, can_play)
            new_card.bind('<Button-1>', self.select_card)
            card_displays.append(new_card)
            new_card.pack(side='left')
        self.hand_frame.pack(side='bottom')
        #

    def start_round(self):
        self.deal_cards()
        self.passing_phase()
        ##### passing phase does nothing right now
        starting_card = (2,'club')
        if self.num_players == 5:
            starting_card = (3, 'club')
        for (player,hand) in self.hands_dict.items():
            if starting_card in hand:
                self.change_current_player(player)
                break
        #
        self.play_turn() # first trick when Q of spades can't be played

    def finish_round(self):
        if 26 in self.round_points_dict.values():
            for (player, points) in self.round_points_dict.items():
                if points == 26:
                    continue
                else:
                    self.points_dict[player] += 26
        else:
            for (player, points) in self.round_points_dict.items():
                self.points_dict[player] += points
        #
        self.hands_dict = {p: [] for p in self.players}  # list so sortable
        self.round_points_dict = {p: 0 for p in self.players}
        self.change_current_player(self.players[0])
        self.round_number += 1
        self.can_play_hearts = False
        self.selected_card = None
        #
        self.trick_suit = None
        self.first_trick = True
        self.turns_played = 0
        self.cards_on_table = {}
        self.next_turn_button = Button(self.window, text=f'Start Round({self.current_player})',command=self.start_round)
        self.next_turn_button.pack(side='bottom')




    def play_game(self):
        self.buttons_frame.destroy()
        self.points_dict = {p: 0 for p in self.players}
        self.round_number = 1
        #
        self.next_turn_button = Button(self.window, text=f'Start Round({self.current_player})',command=self.start_round)
        self.next_turn_button.pack(side='bottom')
        #
        self.player_labels = []
        for i in range(self.num_players):
            new_label = Label(self.window,text=f'{self.players[i]}: 0 points')
            side, anchor = self.player_label_positions[i]
            new_label.pack(side=side,anchor=anchor)
            self.player_labels.append(new_label)



