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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

random_computer = random.randint(0,2)
print(random_computer)

Human_score = 0
Computer_score = 0
opt_out = "n"

while opt_out != "y":

    if choice == 0:
        print(f"{rock}")
        print("computer chose:")
        if random_computer == 0:
            print(f"{rock}")
        if random_computer == 1:
            print(f"{paper}")
            Computer_score +=1
        elif random_computer == 2:
            print(f"{scissors}")
            Human_score += 1

    elif choice == 1:
        print(f"{paper}")
        print("computer chose:")
        if random_computer == 0:
            Human_score +=1
            print(f"{rock}")
        elif random_computer == 1:
            print(f"{paper}")
        elif random_computer == 2:
            print(f"{scissors}")
            Computer_score +=1


    elif choice == 2:
        print(f"{scissors}")
        print("computer chose:")
        if random_computer == 0:
            print(f"{rock}")
            Computer_score +=1
        elif random_computer == 1:
            print(f"{paper}")
            Human_score +=1
        elif random_computer == 2:
            print(f"{scissors}")

    # elif choice == "cancel":
    #     break

    else:
        print("Incorrect selection.")

    opt_out = input("Do you wanna opt out? '(y or n)'")

    if opt_out != "y":
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
        random_computer = random.randint(0, 2)
        print(random_computer)


print(f"Human_score :  {Human_score}")
print(f"Computer_score:  {Computer_score}")


print()