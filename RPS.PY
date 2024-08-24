from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("ROCK PAPER SCISSORS")
root.configure(background='#1c1c1c')  # Dark background

# Resize and load images
rock_userimg = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100), Image.LANCZOS))
paper_userimg = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100), Image.LANCZOS))
scissor_userimg = ImageTk.PhotoImage(Image.open("scissor.png").resize((100, 100), Image.LANCZOS))
rock_compimg = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100), Image.LANCZOS))
paper_compimg = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100), Image.LANCZOS))
scissor_compimg = ImageTk.PhotoImage(Image.open("scissor.png").resize((100, 100), Image.LANCZOS))

# Labels and their placements
user_lab = Label(root, image=scissor_userimg, bg='#1c1c1c')
comp_lab = Label(root, image=scissor_compimg, bg='#1c1c1c')
comp_lab.grid(row=1, column=0, padx=20, pady=20)
user_lab.grid(row=1, column=4, padx=20, pady=20)

# Score Labels
playerScore = Label(root, text=0, font=("Helvetica", 24), bg='#1c1c1c', fg='#00BFFF')
compScore = Label(root, text=0, font=("Helvetica", 24), bg='#1c1c1c', fg='#00BFFF')
compScore.grid(row=1, column=1, padx=20)
playerScore.grid(row=1, column=3, padx=20)

# Indicators
user_indicator = Label(root, font=("Helvetica", 18), text='USER', bg='#1c1c1c', fg='#FF1493')
comp_indicator = Label(root, font=("Helvetica", 18), text='COMPUTER', bg='#1c1c1c', fg='#FFD700')
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Message Label
msg = Label(root, font=("Helvetica", 18), bg='#1c1c1c', fg='#FFD700', width=24)
msg.grid(row=3, column=2, pady=20)

# Update Message
def updatemes(x):
    msg['text'] = x

# Score Updaters
def updateuserscore():
    score = int(playerScore['text'])
    score += 1
    playerScore["text"] = str(score)

def updatecompscore():
    score = int(compScore['text'])
    score += 1
    compScore["text"] = str(score)

# Reset
def reset():
    playerScore["text"] = "0"
    compScore["text"] = "0"
    updatemes("Game Reset! Let's Play Again!")

# Win Conditions
def win(player, computer):
    if player == computer:
        updatemes("It's a Tie!")
    elif player == 'rock':
        if computer == "paper":
            updatemes("You Lose!")
            updatecompscore()
        else:
            updatemes("You Win!")
            updateuserscore()
    elif player == 'paper':
        if computer == "scissor":
            updatemes("You Lose!")
            updatecompscore()
        else:
            updatemes("You Win!")
            updateuserscore()
    elif player == 'scissor':
        if computer == "rock":
            updatemes("You Lose!")
            updatecompscore()
        else:
            updatemes("You Win!")
            updateuserscore()
    else:
        pass

choices = ["rock", "paper", "scissor"]

def update(n):
    computer = choices[randint(0, 2)]
    if computer == "rock":
        comp_lab.configure(image=rock_compimg)
    elif computer == 'paper':
        comp_lab.configure(image=paper_compimg)
    else:
        comp_lab.configure(image=scissor_compimg)

    if n == "rock":
        user_lab.configure(image=rock_userimg)
    elif n == 'paper':
        user_lab.configure(image=paper_userimg)
    else:
        user_lab.configure(image=scissor_userimg)

    win(n, computer)

# Buttons with Neon Colors
rock = Button(root, width=20, height=2, text="ROCK", bg='#FF1493', fg='white', command=lambda: update("rock"))
paper = Button(root, width=20, height=2, text="PAPER", bg='#00BFFF', fg='white', command=lambda: update("paper"))
scissor = Button(root, width=20, height=2, text="SCISSORS", bg='#FFD700', fg='white', command=lambda: update("scissor"))
reset_button = Button(root, width=20, height=2, text="RESET", bg='#4B0082', fg='white', command=reset)

# Place buttons
rock.grid(row=2, column=1, pady=20)
paper.grid(row=2, column=2, pady=20)
scissor.grid(row=2, column=3, pady=20)
reset_button.grid(row=4, column=2, pady=20)

root.mainloop()
