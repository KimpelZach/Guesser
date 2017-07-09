def main():
    print("Guess a number between 1 and 100.")
    randomNumber = 35
    found = False

    if (not found):
         userGuess = input("Your guess ")
         while (userGuess == randomNumber):
            print("You got it!")
            found = True
         else:
            print("That's not it, please try again.")



    if __name__ == '__main__':
        main()
