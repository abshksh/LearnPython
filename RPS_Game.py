import random

def gameWin(c, y):
    if c == "rock" and y == "rock":
        return None
    if c == "rock" and y == "paper":
        return True
    if c == "rock" and y == "scissor":
        return False
    if c == "paper" and y == "rock":
        return False
    if c == "paper" and y == "paper":
        return None
    if c == "paper" and y == "scissor":
        return True
    if c == "scissor" and y == "rock":
        return True
    if c == "scissor" and y == "paper":
        return False
    if c == "scissor" and y == "scissor":
        return None


comp = str()
print(f"Computer's turn: rock, paper, scissor")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "rock"
elif randNo == 2:
    comp = "paper"
elif randNo == 3:
    comp = "scissor"

you = input(f"Your turn: rock, paper, scissor?: ").lower()

if you == "rock" or you == "paper" or you == "scissor":
    result = gameWin(comp, you)
    print(f"""You chose {you} and computer chose {comp}""")
    if result == None:
        print("Game is a tie.")
    elif result:
        print("You win :)")
    else:
        print("You loose :(")
else:
    print("Invalid input. Run the game again.")
