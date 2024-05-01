import random
user_wins=0
computer_wins=0
options=["Paper","Scissors","Rock"]

while True:
    user_input=input("Type Rock/Paper/Scissors").lower()

    random_number=random.randint(0,2)

    comsputer_pick=options[random_number]

    if user_input=="rock" and comsputer_pick=="scissors":
            print("You won!")
            user_wins +=1
    elif user_input=="paper" and comsputer_pick=="rock":
            print("You won!")
            user_wins +=1
    elif user_input=="scissors" and comsputer_pick=="paper":
            print("You won!")
            user_wins +=1
    else:
            print("You lost!")
            computer_wins +=1


            print("you won",user_wins, "times")

            print("you lost",computer_wins, "times")

