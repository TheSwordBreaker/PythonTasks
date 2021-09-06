import random
import time

def main():
    start = random.randint(0, 2)
    data = {"rock" : 0, "paper" : 1, "scissors" : 2}
    resultData = [
                    [0,-1,1],
                    [1,0,-1],
                    [-1,1,0],
                 ]
    # resultData = [
    # """ rock """        [0,-1,1],
    # """ paper """       [1,0,-1],
    # """ scissors """    [-1,1,0],
    #              ]
    print("Game Starts Now. Does Are The Options")           

    while True:
        print("\n\t",end="\t")
        print(" ".join(list(data.keys())))  
        print()  
         
        user = input("Pleas Enter the Your Choice : ")
        computer = random.choice(list(data.keys()))
        # print(list(data.keys()))
        if user == "c" or user == "C":
            exit()

        if user in list(data.keys()):
            print(f"You Have Selected # {user} #")
        elif user in ["1","2","3"]:
            user = int(user)
            user = list(data.keys())[user-1]
            print(f"You Have Selected # {user} #")
        else:
            print("You Have Selected Non-Game Item !!! ")
            print("Game Item Are Only:")
            print("\t 1 \t rock")
            print("\t 2 \t paper")
            print("\t 3 \t scissors")
            print("\t C \t c")
            print("Other Inputs are Non-Game Items")
            continue

        print("\nThe Computer is Selecting !!! \n")
        time.sleep(1)
        print(f"\nComputer Have Selected  # {computer} #")
        time.sleep(1)
        print(f"\nYou Have Selected # {user} # and Computer Have Selected  # {computer} #")
        print("\nCalauating Result !!! \n")

        result = resultData[data[user]][data[computer]]

        time.sleep(1)

        if result == 0:
            print("Result Is Draw.")
            print("Better Luck Next Time !")
        elif result == 1:
            print("You Have Won The Game.")
            print("See How Far you Can Go !")
        else:
            print("Ohhh You Lost This One")
            print("There is always a next Time")

        time.sleep(3)

        print("\nWant to Try Again !!!\nTo Quit Enter C/c")


if __name__ == '__main__':
    main()
