# Easy python game
#Game is called 100
#Objective of the game is 2 people to pick numbers from 1 to 10 and on each turn they add the sum of the values up
#The perosn who losses is the person who cannot use the last turn to reach 100

from random import Random, randint
import tkinter as tk


#The basic algorithem that will let the AI always win


root = tk.Tk()

root.title("EMPORIO GAME 100")

#root.geometry("800x600")

root.configure(background="red")

frame_1 = tk.Frame(root, borderwidth=30, relief="raised", bg = "dark red")
frame_1.pack(pady=10)


label_1 = tk.Label(frame_1, text = "GAME 100", font = ("Bodoni MT", 30))
label_1.grid()


frame_2 = tk.Frame(root, bg = "dark red", relief = "sunken", borderwidth=30)
frame_2.pack(pady=10)

objective_label = tk.Label(frame_2, text = ("""Game is called 100 \n
Objective of the game is 2 people to pick numbers from 1 to 10 \n on each turn they add the sum of the values up \n
The perosn who losses is the person who cannot use the last turn to reach 100"""), font = 1)
objective_label.grid()


frame_3 = tk.Frame(root, borderwidth=30, relief="raised", bg = "red")
frame_3.pack()

name_label = tk.Label(frame_3, text = ("Enter You number "), font = ("Bodoni MT", 15), fg = "black")
name_label.grid(column=1,row=1)


name_entry = tk.Entry(frame_3, bg = "white")
name_entry.grid(row=1, column=2)



submit_button = tk.Button(frame_3, text= "Submit", bg = "green")
submit_button.grid(row = 3, column=2)

value_label = tk.Label(frame_3, text = "Current Number: 1", font = ("Ariel", 20), bg = "red")
value_label.grid()


def check_length(x):

    return (11 - int(x))



def game_fun():
    counter = 0
    counter += 1
    print("AI Number:  1")
    #For the algorithm to work the ai must have the first pick of 1
    while counter < 100:
           

        user_input = input("Choose a number: ")
        if int(user_input) > 10:
            print("Sorry incorect number")
            break
            #ensure that the user choice is within bound

        print("User Pick:" + str(user_input))
        counter += int(user_input)
        print(counter)
        counter += check_length(user_input)
        #Ai will use the users input to get the correct pick

        ai_pick = check_length(user_input)
        print("Ai Number: ", ai_pick)
        print((counter))

game_fun()

#List of possible end game statements can easily be added
statements = ["HAHA YOU LOST", "YOU ARE TRASH DELETE YOURSELF", "UNLUCKY BOI", "FIND ANOTHER GAME", "CLOSE GAME", "BETTER LUCK NEXT TIME", "STOP EMBARRASING YOURSELF"]

random_number = randint(0, len(statements) - 1)

##this funtion will randomly pick a statment to display

def show_end(ran, stat):
    return stat[ran]



text_to_show = (show_end(random_number, statements))

greeting = tk.Label(text=text_to_show)

greeting.pack()

root.mainloop()