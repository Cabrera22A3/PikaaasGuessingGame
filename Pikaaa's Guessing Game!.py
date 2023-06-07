# Developer: Pikaaa
# Game Title: Guessing Game!
# Developed: 06-07-2023 , 10:40PM (UTC+8)
# Language Used: Python
import random
print()

Choice = "Y"
User = ""
while Choice == "Y" or Choice == "N":
    if Choice != "N":
        RanNum = random.randint(1,10)
        attempt = 3
        print()
        print("*********************************************************")
        for x in range(1, 4):
            print()
            print("     Attempt(s) Remaining:", attempt)
            print()
            MissNum = int(input("     Guess the Random number (1-10): "))
            print()
            if MissNum == RanNum:
                print("*********************************************************")
                print("||                                                     ||")
                print("||                     OK! you won!                    ||")
                print("||                                                     ||")
                print("*********************************************************")
                break
            elif MissNum == 123456:
                print("*********************************************************")
                print("||                                                     ||")
                print("||                  Greetings Admin!!                  ||")
                print("||                                                     ||")
                print("*********************************************************")
                User = "Admin"
                break
            elif MissNum < RanNum:
                print("*********************************************************")
                print("||                                                     ||")
                print("||          Close Enough! But you're too Low!          ||")
                print("||                                                     ||")
                print("*********************************************************")
            elif MissNum > RanNum:
                print("*********************************************************")
                print("||                                                     ||")
                print("||          Close Enough! But you're too High!         ||")
                print("||                                                     ||")
                print("*********************************************************")
            attempt = attempt - 1
        print()
        if attempt == 0:
            print("     You are out of Attempt(s) Remaining:", attempt)
        elif User == "Admin":
            print("     Bobo you still have Attempt(s) Remaining:", attempt)
        else:
            print("     Yet you still have Attempt(s) Remaining:", attempt)
        print()
        Choice = str.upper(input("     Would you like to Try again? (Y) Yes or (N) No: "))
        
    
