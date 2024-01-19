# Import necessary libraries
import random  # to choose a number randomly from the list
import sys  # we need it to exit the program when it should be exited
import csv
import game2

# List of possible numbers to guess
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Counter for the number of rounds played
trying = 1

# List to store the amount gained or lost in each round
amount_of_loss_gain = []


def chosegame():
    global game
    print("We have two guessing number games for you")
    game = int(input("choose 1 for game1 or 2 for game2  ..."))
    if game == 2:
        game2.instructions()
    elif game == 1:
        instructions()
    else:
        print("choose 1 or 2")


# Function to display instructions and set the initial capital
def instructions():
    global capital
    print("""Thank you for choosing this game.
            -In this game you have to guess a number between 1 and 9.
            - Every round you can chose the money you want to play with.
            -Pay attention, In this game the correct number that you have to guess, change every round.
            -You can try 20 times or until you have 0 coin , and you can stop after any round you want.
            -If you guess correctly, the amount of coins you play with will be doubled 10 times.
            -If you guess incorrectly, you will only lose the amount of money you play with.
            -Fair enough, isn't it? Let's start.""")
    capital = int(input("Enter the amount of money you want to play with in the game: "))
    print(f"Welcome again, your capital is {capital}.")
    start_game()


# Function to start a new game round
def start_game():
    global list
    global number
    global money
    money = 0
    number = None
    # while loop to make sure that the program can only start if the money that entered < the capital
    # and the number is in the list and capital != zero
    while (money > capital or number not in list) and capital != 0:
        money = int(input("Enter how much money you want to play with in this round:"))
        number = int(input("Enter a number between 1 and 9:"))
        if money > capital:
            print(f"The maximum you can play with is {capital}.")
        elif capital == 0:
            print("You lost all of your money.")
        elif money < capital and number not in list:
            print("Please enter a number between 1 and 9.")
        elif number not in list:
            print("Please enter a number between 1 and 9.")
        elif money <= capital and number in list:
            check_number()
        else:
            print(f"Please try again, you can't play with more than {capital}. ")
            exit_program()


# Function to check if the guess is correct
def check_number():
    global money
    global capital
    global amount_of_loss_gain
    # choose a number randomly from the list and compare it with the number that entered by the player.
    correct_number = random.choice(list)
    if correct_number == number:
        money *= 10
        capital += money

        # if the player guessed correctly, it should be added in negative into the list
        amount_of_loss_gain.append(-money)

        print(f"Wow, true guess! Your money is doubled, you have won {money}.")
        print(f"Your total amount in coins is {capital}.")
        new_round()

        # if the player guessed incorrectly and has no more money in capital, than the program should stop.
    elif correct_number != number and capital == 0:
        print("We are very sorry to tell you that, but you lost all of your money!")
        print("Hope to see you soon to try again and win.")
        exit_program()  # function to exit the program

        # if the player guessed incorrectly but has more money in capital the program should start new round.
    elif correct_number != number:
        capital -= money
        amount_of_loss_gain.append(money)
        print(f"Wrong guess! The amount you lost in coins is {money}.")
        print(f"You have {capital}.")
        print(f"the correct number was {correct_number}")
        new_round()  # function so start new round


# Function to start a new rond or exit
def new_round():
    global money
    global trying
    global capital
    new_trying = None

    # while loop to make sure that the answer of continue playing question is yes or no
    # and to check again before each rond that the capital is not zero
    # and The player did not exceed the permitted number of rounds which is 20 rounds'''
    while new_trying != 'n' and new_trying != 'y' and capital != 0 and trying < 20:
        new_trying = input("Would you like to try again? 'y' or 'n'? ")
        if new_trying == 'n':
            exit_program()
        elif new_trying == 'y':
            trying += 1
            start_game()
            check_number()
        else:
            print("Please enter 'y' to continue or 'n' to stop.")
    exit_program()


# Function to exit the program and write data to a CSV file
def exit_program():
    global money
    global capital
    global trying
    global amount_of_loss_gain
    print(f"You have {capital}.")
    print(f"You have tried {trying} times.")
    print('Thank you, see you soon.')
    print("Exiting the program...")
    schrijfnaarcsv(amount_of_loss_gain)
    uitlezencsv()
    sys.exit(0)


# Function to write data to a CSV file
def schrijfnaarcsv(coins):
    filename = 'gegevens.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(coins)  # "coins" is a list that has the history of losses and gains
        x = "the casino has gained"
        summary_of_gain_and_lost = sum(amount_of_loss_gain)
        summary_str = str(summary_of_gain_and_lost)
        writer.writerow([x, summary_str])


# Function to read and print data from a CSV file
def uitlezencsv():
    filename = 'gegevens.csv'
    row_index = 0
    row_values = []
    # Open the CSV file
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if index == row_index:
                row_values = row
                break
    row_values = [int(item) for item in row_values]
    print(row_values)


chosegame()
