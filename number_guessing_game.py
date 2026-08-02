import random
#So while true is to loop the game repeatedly if user says yes 

while True:
    print("Welcome to number guessing game!!")
    print("You will get 7 chances, Now for the range please:")

    # lb and ub are the range of numbers between which random integer will be generated
    lb = int(input("Enter the lower bounded number: "))
    ub = int(input("Enter the upper bounded number: "))

    num = random.randint(lb,ub)

    #Its the number of chance that user will get to guess the number
    chances = 7

    #Initially the guess is zero for the sake of iteration
    user_guess = 0

    #Loop
    while(user_guess<chances):
        user_guess+=1 
        guess = int(input("Guess the number: "))
        if(guess==num):
            print("Horayyy! You guessed it right ....")
            break  
        elif(user_guess>=chances and guess!= num ):
            print("Oooo! Better luck next time the number was", num)
        elif(guess > num and user_guess< chances):
            print("The number is bit lesser...")
        elif(guess < num and user_guess< chances):
            print("The number is greater...")

    #If the user wants to restart
    play_again = input("Wanna go for another round mate: Y for yes / N for no: ")
    if(play_again.lower() == "n"):
        break

    



