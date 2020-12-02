# Zodiac
# From 1 to 7 players compete against a dealer

import zodiacs, games

class BJ_Zodiac(zodiacs.Zodiac):

    ARIES_VALUE = 1

    @property
    def value(self):
        if self.asc1:
            v = BJ_Zodiac.SUNS.index(self.sun) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Pile(zodiacs.Pile):
    """ A Blackjack Deck. """
    def populate(self):
        for element in BJ_Zodiac.ELEMENTS:
            for sun in BJ_Zodiac.SUNS:
                self.zodiacs.append(BJ_Zodiac(sun, element))
    

class BJ_Hand(zodiacs.Hand):

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "{" + str(self.total) + "}"
        return rep

    @property     
    def total(self):

        for zodiac in self.zodiacs:
            if not zodiac.value:
                return None
        
        # add up zodiac values, treat each Aries as 1
        t = 0
        for zodiac in self.zodiacs:
              t += zodiac.value

        # determine if hand contains an Aries
        doyouhave_aries = False
        for zodiac in self.zodiacs:
            if zodiac.value == BJ_Zodiac.ARIES_VALUE:
                doyouhave_aries = True
                
        # if hand contains Aries and total is low enough, treat Aries as 11
        if doyouhave_aries and t <= 11:
            # add only 10 since we've already added 1 for the Aries
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a new zodiac? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")


    def push(self):
        print(self.name, "pushes.")

        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def descend_first_zodiac(self):
        first_zodiac = self.zodiacs[0]
        first_zodiac.turn_to_descend()


class BJ_Game(object):

    def __init__(self, names):
        self.players = []

        for name in names:
            player = BJ_Player(name)
            self.players.append(player)



        self.dealer = BJ_Dealer("Dealer")

        self.pile = BJ_Pile()
        self.pile.populate()
        self.pile.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_zodiacs(self, player):
        while not player.is_busted() and player.is_hitting():
            self.pile.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
           
    def play(self):
        # deal initial 2 zodiacs to everyone
        self.pile.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.descend_first_zodiac()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional zodiacs to players
        for player in self.players:
            self.__additional_zodiacs(player)

        self.dealer.descend_first_zodiac()    # reveal dealer's first

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional zodiacs to dealer
            print(self.dealer)
            self.__additional_zodiacs(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()                    
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
        

def main():
    print("\t\tWelcome to Zodiacs!\n")
    
    names = []
    total_bets=0
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()
        
    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")



