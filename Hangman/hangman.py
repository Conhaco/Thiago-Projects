"""
to create a hangman game using python
1. to create a loop less than 6 steps as 

"""

guessword = ["f","r","y"]

count =0 # (2 legs + body = 3)

answerlist = []

correctanswercount = 0

wronganswercount =0

while count < 3:
    answer = input("please guess a letter: ")
    if answer in guessword:
        correctanswercount = correctanswercount + 1 
        print("Bingo, you got " + str(correctanswercount)+" letter(s) correctly -" + answer)
        answerlist.append(answer)
        print(answerlist)
    else:
        print("you have lost one leg")
        count = count + 1
