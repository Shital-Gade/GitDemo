
import random
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,'Jack':11, 'Queen': 12, 'Ace': 13,'King':14}
suits =('Heart', 'Diamond', 'Club', 'Square')
ranks =('Two', 'Three', 'Four', 'Five', 'Six', 'Jack', 'Queen', 'Ace', 'King')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.allCards =[]
        for suit in suits:
            for rank in ranks:
                #Create cards
                created_card=Card(suit,rank)
                self.allCards.append(created_card)

    def shuffle(self):
        random.shuffle(self.allCards)
    def dealOne(self):
        return self.allCards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

