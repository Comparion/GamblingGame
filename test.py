import sys
import datetime
import os
import random

name = input("Welcome, enter your name!\n")
print(name,"are you ready for an adventure in the gambling world?")
date_of_brith = int(input("Enter your birth year to confirm.\n"))
today = datetime.datetime.now()
if today.year - date_of_brith < 18 :
        print("You are underage!")
        sys.exit(0)
    
print("You are over 18, so here we go! You get 1000 tokens!")

game = "1"
tokens = 1000

while game != "0":
    os.system("cls")
    print("You have", tokens, "tokens")
    print("Choose 1 to play the Lotto (50 tokens)")
    print("Choose 2 to play Jackpot")
    print("Choose 3 to view instructions")
    print("Choose 0 to exit game")
    game = input()
    if game == "1":
        ex = True
        if tokens < 50:
            print("You don't have enough tokens!!")
            input()
            continue
        number = input("Enter 4 numbers separated by spaces, between 1 and 12\n")
        numbers = number.split()
        if len(numbers) > 4 or len(numbers) < 4:
            print("You need to enter 4 numbers!")
            input()
            continue
        for i in range(len(numbers)-1):
            if not numbers[i].isdigit():
                print("You entered characters instead of numbers!")
                ex = False
                break
        if ex == False:
            input()
            continue
        for i in range(len(numbers)-1):
            if int(numbers[i]) < 1 or int(numbers[i]) > 12:
                print("Enter correct numbers!")
                ex = False
                break
        if ex == False:
            input()
            continue
        for i in range(4):
            if numbers.count(numbers[i]) > 1 :
                print("Enter different numbers!")
                ex = False
                break
        if ex == False:
            input()
            continue
        tokens -= 50
        score = [random.randint(1, 12) for x in range(4)]
        search = True
        while search == True:
            for i in range(12):
                if score.count(i) > 1:
                    score[score.index(i)] = random.randint(1, 12)
                    break
                search = False
        print("Your drawn numbers are:",score)
        win = 0
        for i in range (len(score)):
            for j in range (len(numbers)):
               if score[i] == int(numbers[j]):
                   win += 1
        if win == 2 :
            tokens = tokens + 200
            print("You win 200!")  
        elif win == 3 :
            tokens = tokens + 600
            print("You win 600!!")  
        elif win == 4 :
            tokens = tokens + 50**2
            print("You win 2500!!!")
        elif win == 0:
            print("You lose!")          
        input()
    elif game == "2":
        tok = int(input("How many tokens you want to bet?\n"))
        tokens = tokens - tok
        tab=[[e for e in range(3)] for e in range(3)]
        for i in range(3):
            for j in range(3):
                tab[i][j] = random.randint(1, 3)
        for i in range(len(tab)):
            print(tab[i])
        win = 0
        if tab[0][0] == tab[0][1] == tab[0][2]:
            win+=1
        if tab[1][0] == tab[1][1] == tab[1][2]:
            win+=1
        if tab[2][0] == tab[2][1] == tab[2][2]:
            win+=1
        if tab[0][0] == tab[1][0] == tab[2][0]:
            win+=1
        if tab[0][1] == tab[1][1] == tab[2][1]:
            win+=1 
        if tab[0][2] == tab[1][2] == tab[2][2]:
            win+=1 
        if tab[0][0] == tab[1][1] == tab[2][2]:
            win+=1  
        if tab[0][2] == tab[1][1] == tab[2][0]:
            win+=1
        if win == 0:
            print("You Lose!")
        elif win == 1:
            tokens = tokens + tok * 1.5
            print("You Win",tok *1.5,"tokens!")
        elif win == 2:
            tokens = tokens + tok * 2
            print("You Win",tok *2,"tokens!")
        elif win == 3:
            tokens = tokens + tok * 3
            print("You Win",tok *3,"tokens!")
        elif win == 4:
            tokens = tokens + tok * 4
            print("You Win",tok *4,"tokens!")
        elif win == 5:
            tokens = tokens + tok * 5
            print("You Win",tok *5,"tokens!")
        elif win == 6:
            tokens = tokens + tok * 6
            print("You Win",tok *6,"tokens!")
        elif win == 7:
            tokens = tokens + tok * 7
            print("You Win",tok *7,"tokens!")
        elif win == 8:
            tokens = tokens + tok * 10
            print("You Win",tok *10,"tokens!")
        input()
    elif game == "3":
        print("Lotto game is to enter 4 numbers, 4 numbers will be drawn from the pool from 1 to 12 if you hit 2 numbers you win 200,"
        " if 3 you win 600, and if 4 you win 2500 tokens!")
        print("The Jackpot game is that you deposit any amount of tokens, if you hit three of the same numbers vertically,"
        " horizontally or diagonally you win, the number of points you can get is from 1 to 8."
        "1 is a multiplier of 1.5, 2 is 2, 3 is 3, etc. then 8 is a multiplier of 10 !!")
        input()
