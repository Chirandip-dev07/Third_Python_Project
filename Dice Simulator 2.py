import random
print("WELCOME TO DICE SIMULATOR")
print("JUST ENTER 'Y' FOR ROLLING THE DICE OR 'N' FOR VICE VERSA")
choice = input("DO YOU WANT TO ROLL THE DICE? (Y/N) : ")

def dice(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    space = [[a1,a2,a3],
             [a4,a5,a6],
             [a7,a8,a9]]
    print("-"*12)
    print("|",space[0][0],space[0][1],space[0][2],"|")
    print("|",space[1][0],space[1][1],space[1][2],"|")
    print("|",space[2][0],space[2][1],space[2][2],"|")
    print("-"*12)




def roll_dice():
    a1 = "  "
    a2 = "  "
    a3 = "  "
    a4 = "  "
    a5 = "  "
    a6 = "  "
    a7 = "  "
    a8 = "  "
    a9 = "  "
    print("ROLLING DICE...........")
    print(" ")
    dc = random.randint(1,6)
    if dc==1:
        a5 = u"\u26AA"
        dice(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    elif dc==2:
        a1 = u"\u26AA"
        a9 = u"\u26AA"
        dice(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    elif dc==3:
        a1 = u"\u26AA"
        a5 = u"\u26AA"
        a9 = u"\u26AA"
        dice(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    elif dc==4:
        a1 = u"\u26AA"
        a3 = u"\u26AA"
        a7 = u"\u26AA"
        a9 = u"\u26AA"
        dice(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    elif dc==5:
        a1 = u"\u26AA"
        a3 = u"\u26AA"
        a5 = u"\u26AA"
        a7 = u"\u26AA"
        a9 = u"\u26AA"
        dice(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    else:
        a1 = u"\u26AA"
        a3 = u"\u26AA"
        a4 = u"\u26AA"
        a6 = u"\u26AA"
        a7 = u"\u26AA"
        a9 = u"\u26AA"
        dice(a1,a2,a3,a4,a5,a6,a7,a8,a9)

while choice=="Y":
    roll_dice()
    choice = input("DO YOU WANT TO ROLL THE DICE? (Y/N) : ")

print("\n")
print("THANKS FOR USING DICE SIMULATOR")