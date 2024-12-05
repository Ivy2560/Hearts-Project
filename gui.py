from tkinter import *
from card_values import *
from deck_of_cards import PlayingCard

class Gui:
    def __init__(self,window):
        self.window = window

        # game play attributes
        # toggleable by user
        self.num_players = 4
        self.points_till_loss = 100
        self.jack_of_diamonds = False
        self.players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
        # player dicts
        self.points_dict = {p:0 for p in self.players}
        self.hands_dict = {p:[] for p in self.players} # list so sortable
        self.cards_taken = {p:set() for p in self.players}
        # other
        self.current_player = self.players[0]
        self.round_number = 1
        self.starts_trick = None

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

    def deal_cards(self):
        shuffled_deck = deck_list.copy()
        if self.num_players != 4:
            shuffled_deck.remove((2,'diamond'))
            if self.num_players == 5:
                shuffled_deck.remove((2,'club'))
        # DOUBLE CHECK LATER
        hand_size = len(shuffled_deck) // 4
        shuffle(shuffled_deck)
        for player in self.players:
            self.hands_dict[player] = shuffled_deck[:hand_size]
            shuffled_deck = shuffled_deck[hand_size:]


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

    def play_turn(self):
        pass

    def play_trick(self):
        # a trick won't always start with the same player
        for player in range(self.num_players):
            self.play_turn()

    def play_round(self):
        self.deal_cards()
        self.passing_phase()
        ##### passing phase does nothing right now
        starting_card = (2,'club')
        if self.num_players == 5:
            starting_card = (3, 'club')
        for (player,hand) in self.hands_dict.items()
            if starting_card in hand:
                self.starts_trick = player

        pass


    def play_game(self):
        self.buttons_frame.destroy()
        self.points_dict = {p: 0 for p in self.players}
        self.round_number = 1
        while self.max_points() < self.points_till_loss:
            self.play_round()
            break


