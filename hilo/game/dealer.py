from game.card import Card

class Dealer:

    def __init__(self):
        self.is_playing = True
        self.starting_points = 300
        self.card_guess = ""
        self.next_card = ""
        self.card = Card()
        self.current_card = self.card.draw()

    def start_game(self):
        while self.is_playing and self.starting_points > 0:
            self.get_input()
            self.do_updates()
            self.do_outputs()

    def get_input(self):
        print(f"The card is: {self.current_card}")
        self.card_guess = input("Higher or Lower? [h/l]: ")

        while (self.card_guess != "h") and (self.card_guess != "l"):
            print("You can only type 'h' or 'l'")
            self.card_guess = input("Higher or Lower? [h/l]: ")

    def do_updates(self):
        self.next_card = self.card.draw()
        while self.next_card == self.current_card:
            self.next_card = self.card.draw()

        if self.current_card < self.next_card:
            answer = "h"
        elif self.current_card > self.next_card:
            answer = "l"

        if self.card_guess == answer:
            self.starting_points += 100
        else:
            self.starting_points -= 75

    def do_outputs(self):
        print(f"Next card was: {self.next_card}")
        print(f"Your score is: {self.starting_points}")


        if self.starting_points > 0:
            keep_playing = input("Play again? [y/n]: ")

            while (keep_playing != "y") and (keep_playing != "n"):
                print("You can only type 'y' or 'n'.")
                keep_playing = input("Play again? [y/n]: ")

            self.is_playing = (keep_playing == "y")
        print()
        self.current_card = self.next_card  