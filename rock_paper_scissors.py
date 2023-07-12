import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

rock_paper_scissors = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if rock_paper_scissors >= 3 or rock_paper_scissors < 0:
    print("You typed an invalid number, you lose!")
else:
    computer_chose = random.randint(0, 2)
    print(game_images[rock_paper_scissors])
    print("Computer chose:")
    print(game_images[computer_chose])

    if rock_paper_scissors == 0:
        if rock_paper_scissors == computer_chose:
            print("It's a draw")
        elif rock_paper_scissors == 0 and computer_chose == 2:
            print("You win")
        else:
            print("You lose")

    elif rock_paper_scissors == 1:
        if rock_paper_scissors == computer_chose:
            print("It's a draw")
        elif rock_paper_scissors == 1 and computer_chose == 0:
            print("You win")
        else:
            print("You lose")

    elif rock_paper_scissors == 2:
        if rock_paper_scissors == computer_chose:
            print("It's a draw")
        elif rock_paper_scissors == 2 and computer_chose == 1:
            print("You win")
        else:
            print("You lose")
