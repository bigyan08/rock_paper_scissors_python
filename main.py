import random
com_score=0
usr_score=0
opts=["rock","paper","scissors"]

while True:
    usr_input=input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
    if(usr_input=="q"):
        print("\n!!!Score!!!")
        print("You:",usr_score)
        print("Com:",com_score)
        quit()
    elif(usr_input in opts):
        com_input=opts[random.randint(0,2)]
        print("YOU: "+usr_input)
        print("COM: "+com_input)
        if usr_input=="rock" and com_input=="scissors":
            print("You Win!")
            usr_score += 1
        elif usr_input=="paper" and com_input=="rock":
            print("You Win!")
            usr_score += 1
        elif usr_input=="scissors" and com_input=="paper":
            print("You Win!")
            usr_score +=1
        elif usr_input==com_input:
            print("Draw")
        else:
            print("You Lose!")
            com_score+=1
    else:
        print("invalid input! Please try again!")

