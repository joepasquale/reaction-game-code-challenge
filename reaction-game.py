import tkinter as tk
import time
import random as rd
import pyodbc

# --Connect to SQL Server
# conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=jpasquale\SQLEXPRESS;'
#                      'Database=LeaderboardDB;'
#                      'Trusted_Connection=yes;')
#cursor = conn.cursor()
# create tkinter object
root = tk.Tk()
# dynamically updated header label
headerText = tk.StringVar()
headerText.set("Press 'Play' to begin")
# tracked score in program
score = 0
# variable that is updated for GUI
playerScore = tk.IntVar()
playerScore.set(score)
# color string updated for GUI
GUIColor = tk.StringVar()
# current color used for comparison
thisColor = ""
# color options
colors = ["red", "blue", "green"]
#Leaderboard name
firstName = "Joe"
lastName = "Pasquale"


class Window:
    # Constructor for GUI
    def __init__(self, master):
        # Create three frames, frame for top with choice,
        # frame in middle with buttons, frame in bottom with score
        display_frame = tk.Frame(master)
        display_frame.pack()
        button_frame = tk.Frame(master, height=24, width=72)
        button_frame.pack()
        score_frame = tk.Frame(master)
        score_frame.pack()
        # Create color buttons, use lambda functions for command
        # If you don't make the command an anonymous function, then it will only execute at runtime (so the buttons won't work)
        self.red_button = tk.Button(
            button_frame, text="RED", bg="red", command= lambda: select_color(colors[0]))
        self.blue_button = tk.Button(
            button_frame, text="BLUE", bg="blue", command= lambda: select_color(colors[1]))
        self.green_button = tk.Button(
            button_frame, text="GREEN", bg="green", command= lambda: select_color(colors[2]))
        self.red_button.pack(padx=10, side="left")
        self.blue_button.pack(padx=10, anchor="center", side="left")
        self.green_button.pack(padx=10, side="right")
        # Add selection prompt with changing color and play button
        self.header_label = tk.Label(display_frame, textvariable=headerText)
        self.color_label = tk.Label(display_frame, textvariable=GUIColor)
        self.header_label.pack(side="left")
        self.color_label.pack(side="left")
        self.play_button = tk.Button(
            display_frame, text="Play", command=play_game)
        self.play_button.pack()
        # Add score label
        self.bottom_label = tk.Label(score_frame, text="Score:")
        self.score_label = tk.Label(score_frame, textvariable=playerScore)
        self.bottom_label.pack(side="left")
        self.score_label.pack(side="left")

#Function to see if chosen color is correct
def select_color(color):
    print(color)
    global score, playerScore
    if color is thisColor:
        print("continue")
        continue_game()
    else:
        print("end")
        end_game()

#Increments score, runs play_game again
#Needs to reset timer
def continue_game():
    global score
    score += 5
    playerScore.set(str(score))
    play_game()


def end_game():
    # cursor.execute(
    #    'INSERT INTO LeaderboardDB (lname, fname, score) VALUES ({lastName}, {firstName}, {score});')
    # conn.commit()
    global score
    score = 0
    playerScore.set(str(score))



def play_game():
    #timer = time.perf_counter()
    playerScore.set(str(score))
    print(score)
    randomNumber = rd.randint(0, 2)
    global GUIColor, thisColor
    GUIColor.set(colors[randomNumber])
    thisColor = colors[randomNumber]
    headerText.set("Your color is:")


app = Window(root)

root.mainloop()
