import random
from Data import data
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
print(logo)


#Generate random number


#Get values for that number from data
def formatdata(account):   
    name=account["name"]
    description=account["description"]
    country=account["country"]
    followers=account["follower_count"]
    return name,description,country,followers


score=0
game=True

while game==True:
    A=random.choice(data)
    B=random.choice(data)
    if A==B:
         B=random.choice(data)
    nameA,descriptionA,countryA,followersA=formatdata(A)
    print(f"Compare A: {nameA}, {descriptionA}, from {countryA}")


    print( """
    _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)
    """)


    nameB,descriptionB,countryB,followersB=formatdata(B)
    print(f"Against B: {nameB}, {descriptionB}, from {countryB}")

    selection=input("Who has more followers? Type A or B\n").upper()
    if selection=="A":
        if followersA>followersB:
            score+=1
            #print(f"You are right! Your score:{score}")
            os.system('cls')
            print(f"You are right! Your score:{score}")
        else:
            os.system('cls')
            print(f"You Lose. Your final score is {score} ")
            game=False

    elif selection=="B":
        if followersB>followersA:
            score+=1
            #print(f"You are right! Your score:{score}")
            os.system('cls')
            print(f"You are right! Your score:{score}")

        else:
            os.system('cls')
            print(f"You Lose. Your final score is {score} ")  
            game=False   
           


