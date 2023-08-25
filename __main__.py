from table import Table
from player import Player
from helper import input_integer

def main():

    print("Welcome to the King BlackJack Casino!")

    """offers the player the option of how many decks of cards in the shoe they would like to play with"""
    num_decks = input_integer("How many decks of cards would you like in the shoe? (1-6) ", 1, 6)

    """asks the player what their starting balance is"""
    balance = input_integer("What is your starting balance? (1-100) ", 1, 100)

    player = Player(balance)

    table = Table(num_decks, player)
    table.play()

    print("Thank you for playing with me.")

if __name__ == "__main__":
    main()
