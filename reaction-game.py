import tkinter as tk
import time
import random as rd

colors = ['red','blue','green']
root = tk.Tk()
#tracked score
score = 0
#variable that is updated for GUI
playerScore = tk.IntVar()
playerScore.set(score)
#color string updated for GUI
curColor = tk.StringVar()

class Window:
    #Constructor for GUI
    def __init__(self, master):
        #Create three frames, frame for top with choice, 
        #frame in middle with buttons, frame in bottom with score
        display_frame = tk.Frame(master)
        display_frame.pack()
        button_frame = tk.Frame(master, height = 24, width = 72)
        button_frame.pack()
        score_frame = tk.Frame(master)
        score_frame.pack()
        #Create color buttons
        self.red_button = tk.Button(button_frame, text="RED", bg="red", command = self.select_color("red"))
        self.blue_button = tk.Button(button_frame, text="BLUE", bg="blue", command = self.select_color("blue"))
        self.green_button = tk.Button(button_frame, text="GREEN", bg="green", command = self.select_color("green"))
        self.red_button.pack(padx = 10, side="left")
        self.blue_button.pack(padx = 10, anchor = "center", side="left")
        self.green_button.pack(padx = 10, side="right")
        #Add selection prompt with changing color and play button
        self.header_label = tk.Label(display_frame, text="Color is:")
        self.color_label = tk.Label(display_frame, textvariable=curColor)
        self.header_label.pack(side="left")
        self.color_label.pack(side="left")
        self.play_button = tk.Button(display_frame, text="Play", command=self.play_game())
        self.play_button.pack()
        #Add score label
        self.bottom_label = tk.Label(score_frame,text="Score:")
        self.score_label = tk.Label(score_frame,textvariable = playerScore)
        self.bottom_label.pack(side="left")
        self.score_label.pack(side="left")

    def select_color(self, color):
        if color == curColor:
            global score
            score += 5

    def play_game(self):
        playerScore.set(score)
        randomNumber = rd.randint(0,2)
        global curColor
        time.sleep(2)
        curColor.set(colors[randomNumber])


app = Window(root)

root.mainloop()