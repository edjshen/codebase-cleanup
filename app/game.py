



from random import choice




#
# DETERMINATION OF WINNER
#

def validate(u,c):
    winner = -1
    possible = {"rock":"rock","paper":"paper","scissors":"scissors","rock":"scissors","paper":"rock","scissors":"paper"}
    if u == c:
        print("It's a tie")
    elif possible[u] == c:   
        print("You win")
    elif possible[c] == u:        
        print("You lose")
    else:
        print("You broke the game \n")

if __name__ == "__main__":
    
#
# USER SELECTION
#
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in ["rock", "paper", "scissors"]:
        print("OOPS, TRY AGAIN")
        exit()
        
#
# COMPUTER SELECTION
#
    c = choice(["rock", "paper", "scissors"])
    print("COMPUTER CHOICE:", c)
    validate(u,c)

