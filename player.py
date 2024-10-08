class Player:
    def __init__(self, name, is_dealer=False):
        self.name = name
        self.hand = []
        self.is_dealer = is_dealer

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def calculate_total(self):
        total = 0
        aces = 0
        for card in self.hand:
            rank = card.split(' ')[0]
            if rank in ['Jack', 'Queen', 'King']:
                total += 10
            elif rank == 'Ace':
                aces += 1
                total += 11  # initially count Ace as 11
            else:
                total += int(rank)

        # Adjust for Aces
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total
