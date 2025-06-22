import random


computer = random.choice([0,-1,1])
youstr=input("Enter your choice :")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a tie!")
else:
    if(computer == -1 and you == 1):
        print("You Win !")
    elif(computer== 1 and you ==0):
        print("You Win !")
    elif(computer== 0 and you ==-1):
        print("You Win !") 
    elif(computer== 1 and you ==-1):
        print("You Lose !")
    elif(computer== -1 and you ==0):
        print("You Lose !")    
    elif(computer== 0 and you ==1):
        print("You Lose !")         
    else:
        print("Invalid Input")
 