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
    print(f"Dealer's first card is {p1cards[0][0]}")
    # dealer's first card is 8
    # your cards : A + 9 = 20 or 10
    # calc_score()
    pass


def deal_cards(deck):
    random.shuffle(deck)
    # player1 = [shuffled_deck.pop() for _ in range(2)] this will pop the cards,
    # player2 = [shuffled_deck.pop() for _ in range(2)] but not alternate like it should.
    player1, player2 = deck[-4::2], deck[-3::2]
    # slicing is a little harder to read, but will alternate.
    # essentially remove every second card from the last 4
    # and then the second slice is the cards in between
    # p1score = [rank_values[card[0]] if card[0] in rank_values else int(card[0]) for card in player1]
    # p2score = [rank_values[card[0]] if card[0] in rank_values else int(card[0]) for card in player2]
    # maybe just return cards here instead of calculating everything?
    return player1, player2

    def calc_score(cards, rank_values):
        pass


if __name__ == "__main__":
    main()

