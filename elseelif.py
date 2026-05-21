rangos = ["Challenger", "Grand Master", "Master", "Diamond", "Platinum", "Gold", "Silver", "Bronze", "Unranked"]
def rank_to_index(rank):
    if rank in rangos:
        return rangos.index(rank)
    else:
        return -1
rank = rank_to_index(input("Enter your rank: "))
challenger_idx = rank_to_index("Challenger")
master_idx = rank_to_index("Master")
diamond_idx = rank_to_index("Diamond")
platinum_idx = rank_to_index("Platinum")
gold_idx = rank_to_index("Gold")

if rank == -1:
    print("Invalid rank entered.")
else:
    Winrate = int(input("Enter your winrate: "))
    
    # Check from highest rank to lowest
    if rank <= master_idx:  # Challenger (0), Grand Master (1), Master (2)
        if Winrate >= 60:
            if rank == challenger_idx:
                print("Go pro")
            else:
                print("Just a bit more games and you'll be there")
        else:
            print("Boosted")  # Or customize for low winrate in high ranks
    elif rank == diamond_idx:  # Diamond (3)
        if Winrate >= 50:
            print("You are decent")
        else:
            print("Either you don't rank or you are just bad")
    elif rank == platinum_idx:  # Platinum (4)
        if Winrate >= 50:
            print("Okay for a casual")
        else:
            print("Game spammer")
    elif rank == gold_idx:  # Gold (5)
        if Winrate >= 50:
            print("Guess you just started")
        else:
            print("pretty bad")
    else:  # Silver, Bronze, Unranked, or any unhandled ranks
        print("Either you don't rank or you are just bad")
Games=int(input("Enter the number of games played: "))
Winrate=int(input("Enter your winrate: "))
if Games < 100 and rank <= master_idx:
    print("You are a good smurf")
elif rank <= diamond_idx and Games < 100 and Winrate >= 60:
    print("You are a good smurf") 
    