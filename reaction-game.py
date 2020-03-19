import tkinter as tk
from timer import Timer
from datetime import datetime
import random as rd
import pyodbc

# --Connect to SQL Server
#conn = pyodbc.connect('Driver={SQL Server};'
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
# Leaderboard name
firstName = ""
lastName = ""
# timer object
timer = Timer()
# tracks time passed
timePassed = 0


class Window:
    # Constructor for GUI
    def __init__(self, master):
        # allows first and last name to be updated
        global firstName, lastName
        # Create four frames: frame for game info, frame for top with choice,
        # frame in middle with buttons, frame in bottom with score
        info_frame = tk.Frame(master)
        info_frame.pack()
        display_frame = tk.Frame(master)
        display_frame.pack()
        button_frame = tk.Frame(master, height=24, width=72)
        button_frame.pack()
        score_frame = tk.Frame(master)
        score_frame.pack()
        # Create color buttons to add to button_frame, use lambda functions for command
        # If you don't make the command an anonymous function, then it will only execute at runtime (so the buttons won't work)
        self.red_button = tk.Button(
            button_frame, text="RED", bg="red", command=lambda: selectColor(colors[0]))
        self.blue_button = tk.Button(
            button_frame, text="BLUE", bg="blue", command=lambda: selectColor(colors[1]))
        self.green_button = tk.Button(
            button_frame, text="GREEN", bg="green", command=lambda: selectColor(colors[2]))
        self.red_button.pack(padx=50, pady=20, side="left")
        self.blue_button.pack(padx=50, pady=20, anchor="center", side="left")
        self.green_button.pack(padx=50, pady=20, side="right")
        # Add selection prompt with changing color and play button to display_frame
        self.header_label = tk.Label(display_frame, textvariable=headerText)
        self.color_label = tk.Label(display_frame, textvariable=GUIColor)
        self.header_label.pack(side="left")
        self.color_label.pack(side="left")
        self.play_button = tk.Button(
            display_frame, text="Play", command=play_game)
        self.play_button.pack()
        # Add score label for score_frame
        self.bottom_label = tk.Label(score_frame, text="Score:")
        self.score_label = tk.Label(score_frame, textvariable=playerScore)
        self.bottom_label.pack(side="left")
        self.score_label.pack(side="left")
        # Add game instructions and name entry in info_frame
        self.game_info = tk.Message(info_frame, text="Welcome to the reaction game. Input your name below. You must choose five correct colors in a row to win. You have two seconds to select each color. Good luck!", width=300, justify = "center")
        self.fname_input = tk.Entry(info_frame)
        self.fname_input.insert(0, "First name")
        self.lname_input = tk.Entry(info_frame)
        self.lname_input.insert(0, "Last name")
        self.submit_button = tk.Button(info_frame, text = "SUBMIT", command=lambda: setLeaderboard(self.fname_input.get(), self.lname_input.get()))
        self.game_info.pack(side="top")
        self.fname_input.pack()
        self.lname_input.pack()
        self.submit_button.pack(side="bottom")
        
# saves text from entry so that they can be added to the leaderboard
def setLeaderboard(fname, lname):
    global firstName, lastName
    firstName = fname
    lastName = lname

# Function to see if chosen color is correct
def selectColor(color):
    global score, playerScore, timePassed
    timePassed = timer.stop()
    if color is thisColor:
        #if it takes longer than two seconds for someone to click, they lose
        if timePassed <= 2:
            continue_game()
        else:
            end_game()
    else:
        end_game()

# Increments score
def continue_game():
    global score
    score += 5
    playerScore.set(str(score))
    # If player gets five in a row, they win
    if score >= 25:
        win_game()
    else:
        play_game()

# Win condition
def win_game():
    timestamp = datetime.now()
    # cursor.execute(
    #    'INSERT INTO LeaderboardDB (lname, fname, score, timestamp) VALUES ({lastName}, {firstName}, {score}, {timestamp});')
    # conn.commit()
    global score
    score = 0
    GUIColor.set("")
    headerText.set("You got 5 in a row correct! You win!")

#loss condition
def end_game():
    timestamp = datetime.now()
    # cursor.execute(
    #    'INSERT INTO LeaderboardDB (lname, fname, score, timestamp) VALUES ({lastName}, {firstName}, {score}, {timestamp});')
    # conn.commit()
    global score
    score = 0
    playerScore.set(str(score))
    if timePassed > 2:
        headerText.set("Out of time! GAME OVER!")
        
    else:
        headerText.set("Wrong! GAME OVER!")
    GUIColor.set("")

# launches game
def play_game():
    timer.start()
    playerScore.set(str(score))
    randomNumber = rd.randint(0, 2)
    global GUIColor, thisColor
    GUIColor.set(colors[randomNumber])
    thisColor = colors[randomNumber]
    headerText.set("Your color is:")

#opens and runs GUI
app = Window(root)
root.mainloop()
