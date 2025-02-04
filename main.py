import random


def main():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank_values = {'K': 10,
                   'Q': 10,
                   'J': 10,
                   'A': 11}
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    p1cards, p2cards = deal_cards(deck)
    print(p1cards, p2cards)
    print(f"Dealer's first card is {p1cards[0][0]}")
    print(f"Your cards are {p2cards[0][0]} + {p2cards[1][0]} = {calc_score(p2cards, rank_values)}")
    list_cards(p2cards, rank_values)
    if p1cards[0][0] == 'A':
        c = input("Insurance? 'y' or 'n': ").strip().lower()
        if c == 'y' or '':
            print("Good luck!")
            if p1cards[1][0] == rank_values or '10':
                print(f"Dealer BlackJack!: {p1cards}")
                return
    dealer_score = calc_score(p1cards, rank_values)
    hit(deck, p2cards, rank_values)
    print(p2cards)
    player_score = calc_score(p2cards, rank_values)
    print(f"Scores: Dealer - {dealer_score} Player - {player_score}")
    if dealer_score > player_score:
        print("Dealer Wins!")
    elif player_score > dealer_score:
        print("You Win!!")
    else:
        print("Push!")


def deal_cards(deck):
    random.shuffle(deck)
    # player1, player2 = deck[-4::2], deck[-3::2] slicing doesn't remove them from the deck.
    player1 = [deck.pop()]
    player2 = [deck.pop()]  # we are initializing a list and then popping the first card
    player1.append(deck.pop())  # then we append in order by popping the second card
    player2.append(deck.pop())
    return player1, player2


def calc_score(player, rank_values):
    score = 0
    aces = 0

    for card in player:
        rank = card[0]
        if rank == 'A':
            aces += 1
            score += 11
        elif rank in rank_values:
            score += rank_values[rank]
        else:
            score += int(rank)
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def hit(deck, player, rank_values):
    while True:
        h = input("Would you like to hit? Y or n: ").strip().lower()

        if h == 'y' or h == '':  # Corrected condition
            new_card = deck.pop()
            print(f"New card: {new_card[0]}")
            player.append(new_card)
            list_cards(player, rank_values)

            # Check for bust AFTER adding the new card
            player_score = calc_score(player, rank_values)
            ranks = [card[0] for card in player]  # Extract ranks
            print(f"Your cards are now: {', '.join(ranks)} = {player_score}")
            if player_score > 21:
                print("Bust!")
                exit()  # Ends the game immediately when busted
        elif h == 'n':
            return  # Ends hitting if the player chooses 'n'
        else:
            print("Invalid input, please use 'y' or 'n'.")


def split():
    pass


def list_cards(player, rank_values):
    t = []
    for card in player:
        rank = card[0]
        if rank in rank_values:
            value = rank_values[rank]
        else:
            value = int(rank)
        t.append(value)
    return t


if __name__ == "__main__":
    main()
