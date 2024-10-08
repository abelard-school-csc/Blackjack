from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(input("Enter your name: "))
        self.dealer = Player("Dealer", is_dealer=True)

    def start_game(self):
        while True:
            self.deck.shuffle()
            self.player.clear_hand()
            self.dealer.clear_hand()

            self.deal_initial_cards()
            self.player_turn()
            self.dealer_turn()
            self.determine_winner()

            if input("Play again? (y/n): ").lower() != 'y':
                break

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

    def player_turn(self):
        while True:
            print(f"\n{self.player.name}'s hand: {self.player.hand} (Total: {self.player.calculate_total()})")
            if self.player.calculate_total() > 21:
                print("You bust! Dealer wins.")
                return
            choice = input("Do you want to (h)it or (s)tand? ").lower()
            if choice == 'h':
                self.player.add_card(self.deck.draw_card())
            elif choice == 's':
                break

    def dealer_turn(self):
        while self.dealer.calculate_total() < 17:
            self.dealer.add_card(self.deck.draw_card())
        print(f"\nDealer's hand: {self.dealer.hand} (Total: {self.dealer.calculate_total()})")

    def determine_winner(self):
        player_total = self.player.calculate_total()
        dealer_total = self.dealer.calculate_total()

        if player_total > 21:
            print("You bust! Dealer wins.")
        elif dealer_total > 21 or player_total > dealer_total:
            print("You win!")
        elif player_total < dealer_total:
            print("Dealer wins!")
        else:
            print("It's a tie!")
