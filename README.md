# BlackJack


# Intro
In Python, we coded the popular casino game Blackjack. We stuck with the same rules as the
game, including all of the actions the player can use against the dealer. This game is meant for
only one player, so it becomes the dealer versus the player. The player has the opportunity to
create their initial balance and bet money with the game ending as soon as the player runs out
of money or enters a bet of 0.

# Features
1. The dealer - hitting until their hand value is 17 or greater
2. Player actions - stand, hit, double down or split
3. Betting - maintaining a player balance, asking how much they want to bet, calculating how much they won or lost

# Complexity and Abstraction
This project managed the complexity of implementing all the features by using OOP and
creating classes for the table, player, dealer, card, shoe, hand, and actions. Inheritance was
used to create enumerated constants for the card ranks, suits, and possible player actions.
List comprehensions were frequently used in the methods of the Hand class. Formatted string
literals and class __str__ methods were used to construct output text.
