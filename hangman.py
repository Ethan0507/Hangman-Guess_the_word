# Necessary imports for the program to execute
from os import system
from turtle import *
import turtle

# Function to clear the console
def clear_screen():
    _ = system('cls')


# This function prints all the wrong guesses made and the remaining attempts
def printWrongGuesses(wrong_guesses, my_turt2):
    
    ''' To redraw the necessary changes '''
    my_turt2.clear() 
    my_turt2.color("red")
    my_turt2.penup()
    my_turt2.hideturtle()
    
    ''' Checking if any wrong guesses have been made '''
    if len(wrong_guesses) > 0:
        my_turt2.goto(-350, -200)
        my_turt2.write("Wrong Guesses:", font=('Comic Sans MS', 25, 'italic'), align='left')
        my_turt2.goto(-300, -230)
        my_turt2.write(" ".join(wrong_guesses), font=('Comic Sans MS', 25, 'italic'), align='left')
    my_turt2.goto(-150, -300)
    my_turt2.color('yellow')
    
    ''' Printing the number of remaining attempts '''
    my_turt2.write("You have " + str(8 - len(wrong_guesses)) + " attempts left.", font=('Comic Sans MS', 15, 'italic'), align='left') 


# This function prints the word to be guessed
def printWord(word_dup, break_index, my_turtle):
    
    ''' Redrawing the necessary changes in the word on screen '''
    my_turtle.clear() 
    global word
    my_turtle.penup()
    my_turtle.goto(-250, 230)    
    my_turtle.color("white")
    my_turtle.pendown()
    
    ''' To check if the word had a seperator '''
    if break_index == -1: 
        my_turtle.write(' '.join([word[i] if word_dup[i] == '*' else '*' for i in range(len(word_dup))]), font=('Comic Sans MS', 30, 'italic'), align='left')
    else:
        temp_op = [word[i] if word_dup[i] == '*' else '*' for i in range(len(word))]
        ''' Printing the seperator between the word '''
        my_turtle.write(' '.join(temp_op[:break_index] + ["-"] +temp_op[break_index:]), font=('Comic Sans MS', 30, 'italic'), align='left') 

# This function takes a number between 1 - 8 and draws the respective ambulance part
def drawAmbulance(step):
    my_turt3 = turtle.Turtle()
    my_turt3.pensize(5)
    my_turt3.hideturtle()
    my_turt3.pencolor('blue')
    
    ''' Wrong Guess 1'''
    if step == 1:
        my_turt3.penup()
        my_turt3.goto(50, 100)
        my_turt3.fillcolor('white')
        my_turt3.begin_fill()
        my_turt3.pendown()
        my_turt3.right(90)
        my_turt3.forward(150)
        my_turt3.right(90)
        my_turt3.forward(200)
        my_turt3.right(90)
        my_turt3.forward(150)
        my_turt3.right(90)
        my_turt3.forward(200)
        my_turt3.end_fill()
        return

    ''' Wrong guess 2 '''
    if step == 2:
        my_turt3.penup()
        my_turt3.goto(50, 100)
        my_turt3.fillcolor('white')
        my_turt3.pendown()
        my_turt3.begin_fill()
        my_turt3.goto(135, 50)
        my_turt3.right(90)
        my_turt3.forward(100)
        my_turt3.right(90)
        my_turt3.forward(85)
        my_turt3.end_fill()
        return

    ''' Wrong Guess 3 '''
    if step == 3:
        my_turt3.penup()
        my_turt3.goto(50, 80)
        my_turt3.pendown()
        my_turt3.begin_fill()
        my_turt3.goto(115, 45)
        my_turt3.right(90)
        my_turt3.forward(25)
        my_turt3.right(90)
        my_turt3.forward(65)
        my_turt3.right(90)
        my_turt3.goto(50,80)
        my_turt3.end_fill()
        return

    ''' Wrong Guess 4 '''  
    if step == 4:
        my_turt3.penup()
        my_turt3.pencolor('red')
        my_turt3.fillcolor('red')
        my_turt3.goto(0, 100)
        my_turt3.pendown()
        my_turt3.begin_fill()
        my_turt3.left(90)
        my_turt3.forward(25)
        my_turt3.right(90)
        my_turt3.forward(20)
        my_turt3.right(90)
        my_turt3.forward(25)
        my_turt3.end_fill()
        return

    ''' Wrong Guess 5 '''
    if step == 5:
        my_turt3.penup()
        my_turt3.goto(-85, 35)
        my_turt3.pendown()
        my_turt3.pencolor('red')
        my_turt3.fillcolor('red')
        my_turt3.begin_fill()
        my_turt3.forward(75)
        my_turt3.right(90)
        my_turt3.forward(10)
        my_turt3.right(90)
        my_turt3.forward(75)
        my_turt3.right(90)
        my_turt3.forward(10)
        my_turt3.right(90)
        my_turt3.end_fill()
        return

    ''' Wrong Guess 6 '''
    if step == 6:
        my_turt3.penup()
        my_turt3.goto(-85, 35)
        my_turt3.pencolor('red')
        my_turt3.fillcolor('red')
        my_turt3.forward(32)
        my_turt3.pendown()
        my_turt3.begin_fill()
        my_turt3.left(90)
        my_turt3.forward(32)
        my_turt3.right(90)
        my_turt3.forward(10)
        my_turt3.right(90)
        my_turt3.forward(75)
        my_turt3.right(90)
        my_turt3.forward(10)
        my_turt3.right(90)
        my_turt3.forward(75)
        my_turt3.right(90)
        my_turt3.end_fill()
        return

    ''' Wrong Guess 7 '''
    if step == 7:
        my_turt3.penup()
        my_turt3.goto(-150, -50)
        my_turt3.forward(30)
        my_turt3.right(90)
        my_turt3.forward(15)
        my_turt3.pendown()
        my_turt3.pencolor('gray')
        my_turt3.fillcolor('gray')
        my_turt3.begin_fill()
        my_turt3.circle(30)
        my_turt3.end_fill()
        return

    ''' Wrong Guess 8 '''
    my_turt3.penup()
    my_turt3.goto(20, -50)
    my_turt3.right(90)
    my_turt3.forward(15)
    my_turt3.pendown()
    my_turt3.pencolor('gray')
    my_turt3.fillcolor('gray')
    my_turt3.begin_fill()
    my_turt3.circle(30)
    my_turt3.end_fill()



# Thcdpsvsis function is used to print the final output of the game
def GameStatus(status):
    my_turt4 = turtle.Turtle()
    my_turt4.hideturtle()
    my_turt4.penup()
    my_turt4.pensize(5)
    my_turt4.pencolor('dark gray')
    my_turt4.goto(-300, 0)
    
    '''Setting the background color of the output card to green or red depending on result '''
    if status == 'win' :
        my_turt4.pendown()
        my_turt4.fillcolor('green')
    else:
        my_turt4.pendown()
        my_turt4.fillcolor('red')
    my_turt4.begin_fill()
    my_turt4.left(90)
    my_turt4.forward(100)
    my_turt4.right(90)
    my_turt4.forward(600)
    my_turt4.right(90)
    my_turt4.forward(200)
    my_turt4.right(90)
    my_turt4.forward(600)
    my_turt4.right(90)
    my_turt4.forward(100)
    my_turt4.end_fill()
    my_turt4.penup()
    my_turt4.goto(-250, -50)
    my_turt4.pendown()
    my_turt4.color('white')
    
    '''Printing the result 'You win' or 'You lose' depending on the result passed to this function'''
    if status == 'win':
        my_turt4.write('You Win!', font=('Comic Sans MS', 75, 'bold'), align='left')
    else:
        my_turt4.write('You Lose!', font=('Comic Sans MS', 75, 'bold'), align='left')


# A welcome screen to the user before player 1 enters a letter
def welcome_screen():
    wn = turtle.Screen()
    wn.bgcolor("Black")
    wn.title("Hangman2.0")
    turtle.color('gray')
    turtle.hideturtle()
    turtle.write('Welcome!', font=('Comic Sans MS', 90, 'bold'), align='center')


# This is the main function that control the flow of the game
def start_game():
    welcome_screen()
    global word
    print("------------------Player 1's turn-----------------------")
    
    ''' Taking input from player 1'''
    word = list(input("Please enter your word (seperate two words using '-', eg: ice-cream):").lower())
    break_index = -1
    
    '''Checking if word entered contains a seperator '''
    if '-' in word:
        break_index = word.index('-')
        word = word[:break_index] + word[break_index + 1:]
    
    '''A duplicate array to keep track of unguessed characters'''
    word_dup = [word[i] for i in range(len(word))]

    '''Calling the clear screen function to clear the console'''
    clear_screen()

    '''Clearing the welcome screen '''
    turtle.clear()

    my_turt = turtle.Turtle()
    my_turt.color("white")
    my_turt.penup()
    my_turt.hideturtle()
    my_turt.goto(-380,270)
    my_turt.pendown()
    
    my_turt.write("Guess the word: ", font=('Comic Sans MS', 30, 'italic'),align='left')
    my_turt1 = turtle.Turtle()
    my_turt2 = turtle.Turtle()
    my_turt1.hideturtle()
    my_turt2.hideturtle()
    
    ''' Printing the appropriate *'s on the screen for the word to be guessed '''
    printWord(word_dup, break_index, my_turt1)    
    
    '''An array to maintain the number of wrong guesses'''
    wrong_guesses = []

    '''Asking the player 2 to take over the console and try to win!'''
    print('-----------------Player 2 take over---------------------')

    '''The loop will run until no attempts are remaining or the player guesses all the characters in the word'''
    while len(wrong_guesses) < 8 and word_dup.count('*') < len(word):
        printWord(word_dup, break_index, my_turt1)

        '''Calling the function to print the wrong guesses and remaining attempts on the screen '''
        printWrongGuesses(wrong_guesses, my_turt2)

        '''Taking the input from player 2'''
        p2_in = input("Enter a letter:").lower()

        ''' Getting all the occurrences of entered character '''
        char_matches = [i for i in range(len(word)) if word_dup[i] == p2_in]
        if char_matches:

            ''' Marking all the matching characters '''
            for i in char_matches:
                word_dup[i] = '*'
        else:

            ''' Adding the character to wrong_guesses array '''
            wrong_guesses.append(p2_in)

            ''' Calling the raw ambulance function with appropriate step number '''
            drawAmbulance(len(wrong_guesses))

    ''' Checking if the loop broke because user guessed all charcters or because he ran out of guesses'''        
    if word_dup.count('*') == len(word):
        printWord(word_dup, break_index, my_turt1)
        ''' Printing the win output for player 2'''
        GameStatus('win')
    else:
        ''' Printing the word entered by player 1'''
        printWord(['*' for i in word], break_index, my_turt1)
        ''' Printing the 'You lose' output for player 2'''
        GameStatus('lose')
    

''' The array that will store the word entered by player 1'''
word = []

while 1:
    start_game()
    clear_screen()
    ''' To restart the game '''
    x = input('Enter any character to restart: ')
    ''' Clearing the screen of the previous game's output '''
    turtle.clearscreen()