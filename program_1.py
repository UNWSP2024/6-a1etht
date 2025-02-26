#Programmer: Alethea Lo
#Date: 2/25/25
#Title: Random Dice

import random

def randDice():
    """Simulates rolling two six-sided dice and returns their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def main():
    rolls = [randDice() for _ in range(100)]  # Roll dice 100 times
    average_roll = sum(rolls) / len(rolls)  # Calculate average
    print(f"Average roll: {round(average_roll, 2)}")  # Print rounded result

if __name__ == "__main__":
    main()
