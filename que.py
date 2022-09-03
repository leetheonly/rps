def newGame():
    guesses = []
    correctGuesses = 0
    questionNum = 1
    for key in questions:
        print(".........................................")
        print(key)
        for i in options[questionNum-1]:
            print(i)
        guess = input("A,B,C OR D?; ").upper()
        guesses.append(guess) 
        correctGuesses += checkAnswer(questions.get(key),guess)
        questionNum += 1    
    displayScore(correctGuesses, guesses)    


def checkAnswer(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("DUMBASS!!")
        return 0    
def displayScore(correctGuesses, guesses):
    print('--------------------------')
    print('RESULTS')
    print('--------------------------')
    print("ANSWERS; ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()   
    print("YOUR ANSWERS; ", end="") 
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correctGuesses/len(questions))*100)
    print("your score is: "+str(score))    

     


def playAgain():
    pass


questions = {
    "Who created python?; ":"A",
    "What yeaar was python created?: ":"B",
    "Python is tributed to which coomedy group?: ":"C",
    "Is the earth round?: ":"A"
}

options = [
    ["A.Guido Van Rossum ","B.Elon Musk ","C.Bill Gates ","D.Mark Zuckerburg "],
    ["A.1889 ","B.1991 ","C.2000 ","D.2016 "],
    ["A.Lonely Island ","B.Mosh ","C.Monty python","D.SNL "],
    ["A.True ","B.False ","C.Sometimes ","D.Whats earth "],
]
    
newGame()    