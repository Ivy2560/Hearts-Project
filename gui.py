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
        self.round_points_dict = {p:0 for p in self.players}
        # other
        self.current_player = self.players[0]
        self.round_number = 1
        self.starts_trick = None
        self.can_play_hearts = False

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
        hand_size = len(shuffled_deck) // 4
        shuffle(shuffled_deck)
        for player in self.players:
            self.hands_dict[player] = shuffled_deck[:hand_size]
            shuffled_deck = shuffled_deck[hand_size:]
        #
        # sort hands
        for player in self.players:
            self.sort_hand(player)
        print(self.hands_dict)


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

    def turn_order(self):
        order = []
        first_index = self.players.index(self.starts_trick)
        for n in range(self.num_players):
            player_index = (first_index +n) % self.num_players
            order.append(self.players[player_index])
        return order

    def play_turn(self,player, trick_suit, first_trick=False, first_turn=False):
        force_suit = False
        if trick_suit is not None:
            for card in self.hands_dict[player]:
                if card[1] is trick_suit:
                    force_suit = True
                    break
        #
        self.hand_frame = Frame(self.window)
        card_displays = []
        for card in self.hands_dict[player]:
            # logic for if cards are playable
            if first_trick and first_turn:
                if self.num_players != 5:
                    can_play = card is (2, 'club')
                else: # self.num_players != 5
                    can_play = card is (3, 'club')
            elif force_suit:
                # don't have to check for Q of spades because first
                # trick suit will never be spades
                can_play = card[1] is trick_suit
            elif :
                # if we're not forcing the suit, it could be because
                # they are starting the trick or because they are
                # playing later so we have to check for hearts

            else: # they don't have the suit a
                if first_trick

            new_card = PlayingCard(self.hand_frame, card, can_play)
            card_displays.append(new_card)
            new_card.pack(side='left')
        self.hand_frame.pack(side='bottom')

    def play_trick(self, first_trick=False):
        # a trick won't always start with the same player
        trick_order = self.turn_order()
        trick_suit = self.play_turn(trick_order[0], None, first_trick, True)
        for player in trick_order[0:]:
            self.play_turn(player, trick_suit, first_trick)

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
                self.starts_trick = player
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



