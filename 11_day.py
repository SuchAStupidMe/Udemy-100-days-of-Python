# Blackjack capstone project
import random


def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    return sum(hand)


def game():
    print(f"Computer's first card is {dealer_hand[0]}")
    print(f"Your cards are {player_hand} with score of {sum(player_hand)}")

    if calculate_score(dealer_hand) == 0:
        print("Dealer has a blackjack, you lost")
        return False
    elif calculate_score(player_hand) == 0:
        print("You have a blackjack, congrats!")
        return True

    while True:
        if calculate_score(player_hand) == 21:
            return True

        another_card = input('Do you want ot take another card?: ').lower()
        if another_card == "y":
            player_hand.append(random.choice(cards))
            print(f"Your cards are {player_hand} with score of {sum(player_hand)}")
            if calculate_score(player_hand) > 21:
                if 11 in player_hand:
                    player_hand[player_hand.index(11)] = 1
                    if calculate_score(player_hand) > 21:
                        return False

                return False

        elif another_card == "n":
            while calculate_score(dealer_hand) < 17:
                print("Dealer takes another card.")
                dealer_hand.append(random.choice(cards))

            if calculate_score(dealer_hand) > 21:
                print(f"Dealer went above 21 with score of {calculate_score(dealer_hand)}.")
                return True

            if calculate_score(player_hand) == calculate_score(dealer_hand):
                return None
            elif calculate_score(player_hand) > calculate_score(dealer_hand):
                return True
            elif calculate_score(dealer_hand) > calculate_score(player_hand):
                return False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = random.sample(cards, 2)
player_hand = random.sample(cards, 2)

if input("Do you want to play a game of blackjack?: ").lower() == "y":
    result = game()
    print(f"Your hand is {player_hand} and your score is {calculate_score(player_hand)}")
    print(f"Dealers hand is {dealer_hand} and their score is {calculate_score(dealer_hand)}")
    if result is None:
        print("It's a draw!")
    elif result:
        print("Congrats! You win.")
    elif not result:
        print("Dealer wins.")

