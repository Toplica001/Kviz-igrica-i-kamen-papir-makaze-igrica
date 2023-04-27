def newGame():
    guesses = []
    correctGuesses = 0
    questNumber = 1

    for i in questions:
        print(i)
        for j in options[questNumber-1]:
            print(j)

        guess = input("Enter (A,B,C or D): ").upper()
        guesses.append(guess)

        correctGuesses += check(questions.get(i),guess)
        questNumber += 1

    displayScore(correctGuesses, guesses)

    
def check(answer, guess):
    
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def displayScore(correctGuesses, guesses):
    
    print("##########################")
    print("RESULTS")
    print("Answers: ", end =" ")
    for i in questions:
        print(questions.get(i), end = " ")
        print()

    print("Guesses: ", end =" ")
    for i in guesses:
        print(i, end = " ")
        print()

    score = int((correctGuesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def playAgain():
    
    response = input("Do you want to play again? (yes/no): ").lower()

    if response == "yes":
        return True
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C"
    }
options = [["A. Guido van Rossum","B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburn"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"]]

newGame()

while playAgain():
    print()
    newGame()
   

print()
print("Thank you for playing!")

