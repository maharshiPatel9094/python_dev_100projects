def bid_compare(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidders_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



# should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
bidders_dict = {}
continue_bidding = True
while continue_bidding:
    user_name = input("What is your name?: ").lower()
    user_bid = int(input("What is your bid?: $ "))
    bidders_dict[user_name] = user_bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        bid_compare(bidders_dict)
    elif should_continue == "yes":
        # clearing out the screen
        print("\n" * 100)