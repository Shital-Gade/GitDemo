from Card_Game import Card, Deck, Player

two_hearts = Card("Heart", "Two")
new_deck = Deck()
new_player = Player('Shital')
first_card = new_deck.allCards[0]
print(first_card)
print(new_player)

new_deck.shuffle()
mycard = new_deck.dealOne()
print(new_player.add_cards([mycard]))

# print(two_hearts)
