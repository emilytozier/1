# Zodiac Module
# Basic classes for a game with zodiacs

class Zodiac(object):
    """ A playing zodiac. """
    SUNS = ["Aries ", "Tau ", "Gem ", "Cancer ", "Leo ", "Virgo ", "Libra ",
             "Saggit ", "Scorpio ","Capric ", "Aquarius ", "Pisces ", "Jocker "]
    ELEMENTS = ["water", "earth", "air", "fire"]

    def __init__(self, sun, element, asc = True):
        self.sun = sun
        self.element = element
        self.asc1 = asc

    def __str__(self):
        if self.asc1:
            rep = self.sun + self.element
        else:
            rep = "XX"
        return rep

    def turn_to_descend(self):
        self.asc1 = not self.asc1
      
class Hand(object):
    """ A hand of zodiac """
    def __init__(self):
        self.zodiacs = []

    def __str__(self):
        if self.zodiacs:
           rep = ""
           for zodiac in self.zodiacs:
               rep += str(zodiac) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.zodiacs = []

    def add(self, zodiac):
        self.zodiacs.append(zodiac)

    def give(self, zodiac, other_hand):
        self.zodiacs.remove(zodiac)
        other_hand.add(zodiac)

class Pile(Hand):
    """ A deck of playing zodiacs. """
    def populate(self):
        for element in Zodiac.ELEMENTS:
            for sun in Zodiac.SUNS:
                self.add(Zodiac(sun, element))

    def shuffle(self):
        import random
        random.shuffle(self.zodiacs)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.zodiacs:
                    top_zodiac = self.zodiacs[0]
                    self.give(top_zodiac, hand)
                else:
                    print("Can't continue deal. Zodiacs are running out!")



if __name__ == "__main__":
    print("This is a module with classes for playing cards.")
    input("\n\nPress the enter key to exit.")
