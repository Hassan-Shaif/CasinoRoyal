import random
import sys

# List of possible numbers to guess
list = list(range(1, 101))
correctnumber = random.choice(list)


def instructions():
    global capital

    print(f"Welcome to Casino Royal++ game")
    print("""" In this game you have to guess a number between 1 and 100
    -If you guess correctly in the first or second trying, your capital will be 10 times doubled 
    -If not, you will get three more chances, each chance you can ask one question to help you guess correctly")
    -With each chance the prize will be reduced 20%""")
    capital = int(input("Enter the amount of money you want to play with in the game: "))
    print(f"Your capital is {capital}")
    checknumber()


def checknumber():
    global list
    global useerguess
    global trying
    trying = 0
    while trying < 2:
        useerguess = int(input("Enter a number between 1 and 100:"))
        if useerguess == correctnumber:
            print(f"Wow, true guess! Your money is 10 times doubled, you have won {10 * capital}.")
            sys.exit(0)
        elif useerguess != correctnumber:
            print("wrong guess")
            print("try again")
        trying += 1
    if trying == 2:
        round2()
    print(f" the correct number was {correctnumber}, You was very close, try again")
    sys.exit(0)


def checknumber_round2():
    global chances
    if correctnumber == useerguess and chances == 3:
        print(f"Wow, true guess! Your money is 8 times doubled, you have won {8 * capital}.")
        sys.exit(0)
    elif correctnumber == useerguess and chances == 2:
        print(f"Wow, true guess! Your money is 6 times doubled, you have won {6 * capital}.")
        sys.exit(0)
    elif correctnumber == useerguess and chances == 1:
        print(f"Wow, true guess! Your money is 4 times doubled, you have won {4 * capital}.")
        sys.exit(0)

    else:
        print("unfortunatlly you guessed uncorrectly")


def round2():
    global ques
    global chances
    print(
        "now, you have 3 chances, with each chance you have one question to ask about the number and you lose 20% from"
        " the prize  every trying")
    chances = 3
    while chances > 0:
        print(f"You still have {chances} trying")
        print("choose one of the following questions to know more about the number ")
        print("""
        1  : is the number even or odd?;
        2  : is the number bigger than 50 or not?
        3  : is the number smaller than 25 or not?
        4  : is the number bigger than 75 or not?
        5  : is the number between 1 and 15?
        6  : is the number between 15 and 30?
        7  : is the number between 30 and 45?
        8  : is the number between 45 and 60?
        9  : is the number between 60 and 75?
        10 : is the number between 75 and 90?
        11 : is the number between 90 and 100?""")

        questions()
        chances -= 1

    print("Game over, see you soon")


def questions():
    global chances
    global correctnumber
    global useerguess
    ques = int(input("Enter the number of the question"))

    if ques == 1:
        if correctnumber % 2 == 0:
            print("is even")

        else:
            print("is odd")
    if ques == 2:
        if correctnumber > 50:
            print("it is bigger then 50")
        else:
            print("no it's not bigger then 50")
    if ques == 3:
        if correctnumber < 25:
            print("yes it is smaller the 25")
        else:
            print("no it is not smaller the 25")
    if ques == 4:
        if correctnumber > 75:
            print("yes it is bigger then 75")
        else:
            print("no it is not bigger then 75")
    if ques == 5:
        if correctnumber < 15:
            print("yes, it is  between 1 and 15? ")
        else:
            print("no it is not between 1 and 15?")
    if ques == 6:
        if correctnumber > 15 and correctnumber < 30:
            print("yes, it is  between 15 and 30? ")
        else:
            print("no it is not between 15 and 30?")
    if ques == 7:
        if correctnumber > 30 and correctnumber < 45:
            print("yes, it is  between 30 and 45? ")
        else:
            print("no it is not between 30 and 45?")
    if ques == 8:
        if correctnumber > 45 and correctnumber < 60:
            print("yes, it is  between 45 and 60? ")
        else:
            print("no it is not between 45 and 60?")
    if ques == 9:
        if correctnumber > 60 and correctnumber < 75:
            print("yes, it is  between 60 and 75? ")
        else:
            print("no it is not between 60 and 75?")
    if ques == 10:
        if correctnumber > 75 and correctnumber < 90:
            print("yes, it is  between 75 and 90? ")
        else:
            print("no it is not between 75 and 90?")
    if ques == 11:
        if correctnumber > 90:
            print("yes, it is  between 90 and 100? ")
        else:
            print("no it is not between 90 and 100?")
    useerguess = int(input("Enter a number between 1 and 100:"))
    checknumber_round2()
