# Secret Auction program
from replit import clear


def find_highest_bid(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of {highest_bid}$!")


print("Welcome to the secret auction program.")

bidders = {}

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    other = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if other == "yes":
        clear()
        continue
    elif other == "no":
        find_highest_bid(bidders)
        bidding_finished = True

