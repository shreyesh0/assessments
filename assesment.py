import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = [rank + " of " + suit for rank in ranks for suit in suits]
random.shuffle(deck)

num_players = 0
while True:
    try:
        num_players = int(input("Enter number of players: "))
        if num_players <= 0:
            print("Number of players must be positive.")
            continue
        if num_players > 52:
            print("Too many players for a 52 card deck.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

cards_per_player = len(deck) // num_players

players = []
index = 0
for p in range(num_players):
    hand = deck[index:index + cards_per_player]
    players.append(hand)
    index = index + cards_per_player

scores = [0] * num_players

total_rounds = cards_per_player

for round_number in range(1, total_rounds + 1):
    print("\nRound " + str(round_number))
    played_cards = []
    for p in range(num_players):
        chosen_card = random.choice(players[p])
        players[p].remove(chosen_card)
        played_cards.append(chosen_card)
        print("Player " + str(p + 1) + " played: " + chosen_card)

    winner = 0
    while True:
        try:
            winner = int(input("Enter the winner of this round (player number): "))
            if winner < 1 or winner > num_players:
                print("Invalid player number. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    scores[winner - 1] = scores[winner - 1] + 1

print("\nFinal Scores")
for p in range(num_players):
    print("Player " + str(p + 1) + ": " + str(scores[p]) + " rounds won")

highest_score = max(scores)
winners = []
for p in range(num_players):
    if scores[p] == highest_score:
        winners.append(p + 1)

if len(winners) == 1:
    print("\nPlayer " + str(winners[0]) + " wins the game!")
else:
    print("\nIt's a tie between players: " + str(winners))