import os
from art import logo


print(logo)
print("Welcome to the secret auction program!")
continue_or_not = False
my_dict = {}
while continue_or_not != True:
    participant_name = input("What's your name? : ")
    bid_price = int(input("What's you bid's price? : $"))
    continue_or_not_inp = input(
        "Are there any other bidders? Type 'yes' or 'no' : ")
    if continue_or_not_inp.lower() == "no":
        continue_or_not = True
    else:
        os.system("cls")
    my_dict[participant_name] = bid_price
winner = 0
winner_participant = ""
for key in my_dict:
    if my_dict[key] > winner:
        winner = my_dict[key]
        winner_participant = key
os.system("cls")
print("The winner is " + winner_participant + f" with ${winner} bid price.")
