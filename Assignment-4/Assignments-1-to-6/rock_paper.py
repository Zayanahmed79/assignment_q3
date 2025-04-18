import random

def play():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer}")

    if user_choice == computer:
        return "It's a tie!"

    if is_win(user_choice, computer):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    if (player == "rock" and opponent == "scissors") or \
       (player == "paper" and opponent == "rock") or \
       (player == "scissors" and opponent == "paper"):
        return True

print(play())