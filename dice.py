import random


#function for  dice rolling

def roll_dice():

    #dictionary for dice images
    dice_image = {1:('+-------+',
                     '|       |',
                     '|   O   |',
                     '|       |',
                     '+-------+')
                  ,2:('+-------+',
                      '| O     |',
                      '|       |',
                      '|     O |',
                      '+-------+')
                  ,3:('+-------+',
                      '| O     |',
                      '|   O   |',
                      '|     O |',
                      '+-------+')
                  ,4:('+-------+',
                     '| O   O |',
                     '|       |',
                     '| O   O |',
                     '+-------+')
                  ,5:('+-------+',
                     '| O   O |',
                     '|   O   |',
                     '| O   O |',
                     '+-------+')
                  ,6:('+-------+',
                      '| O   O |',
                      '| O   O |',
                      '| O   O |',
                      '+-------+')}

    #input for dice rolling
    roll = input("Roll the dice? (Yes/No) : ")
    print("----------------------------------------------------  \n")

    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print(f"dice rolled {dice1} and {dice2} \n \n")
        print("user1 : ")
        print("\n".join(dice_image[dice1]),"\n")
        print("user2 : ")
        print("\n".join(dice_image[dice2]),"\n")

        
        print("---------------------------------------------------- \n")

        #input to continue dice rolling
        roll = input("Roll again? (Yes/No): ")


#calling roll_dice funtion
roll_dice()
