import random

class Deck:
    def __init__(self):
        self.cards = [f"{rank} of {suit}" for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]
        self.current_card = 0

    def shuffle(self):
        random.shuffle(self.cards)
        self.current_card = 0

    def draw_card(self):
        card = self.cards[self.current_card]
        self.current_card += 1
        return card
