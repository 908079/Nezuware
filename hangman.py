import tkinter as tk
import random
from tkinter import messagebox

word_list = ["PYTHON", "JAVASCRIPT", "HANGMAN", "COMPUTER", "PROGRAMMING", "DEVELOPER"]


chosen_word = random.choice(word_list)
word_display = ["_" for _ in chosen_word]
guessed_letters = []
remaining_guesses = 6


BG_COLOR = "#358597"
BUTTON_COLOR = "#F4A896"
TEXT_COLOR = "white"
WRONG_COLOR = "#FF4C4C"


root = tk.Tk()
root.title("Hangman")
root.configure(background=BG_COLOR)


def update_word_display():
    word_label.config(text=" ".join(word_display))


def update_guessed_letters_display():
    guessed_label.config(text="Guessed Letters: " + " ".join(guessed_letters))


def guess_letter(letter):
    global remaining_guesses
    guessed_letters.append(letter)
    if letter in chosen_word:
        for i, l in enumerate(chosen_word):
            if l == letter:
                word_display[i] = letter
    else:
        remaining_guesses -= 1
        remaining_label.config(text=f"Remaining Guesses: {remaining_guesses}", fg=WRONG_COLOR)

    update_word_display()
    update_guessed_letters_display()

    if "_" not in word_display:
        end_game("You Win!")
    elif remaining_guesses == 0:
        end_game(f"You Lose! The word was {chosen_word}")


def end_game(result):
    messagebox.showinfo("Game Over", result)
    root.after(1500, reset_game)  


def reset_game():
    global chosen_word, word_display, guessed_letters, remaining_guesses
    chosen_word = random.choice(word_list)
    word_display = ["_" for _ in chosen_word]
    guessed_letters = []
    remaining_guesses = 6
    update_word_display()
    update_guessed_letters_display()
    remaining_label.config(text=f"Remaining Guesses: {remaining_guesses}", fg=TEXT_COLOR)


word_label = tk.Label(root, text=" ".join(word_display), font=("Helvetica", 24), bg=BG_COLOR, fg=TEXT_COLOR)
word_label.pack(pady=20)

guessed_label = tk.Label(root, text="Guessed Letters: ", font=("Helvetica", 14), bg=BG_COLOR, fg=TEXT_COLOR)
guessed_label.pack(pady=10)

remaining_label = tk.Label(root, text=f"Remaining Guesses: {remaining_guesses}", font=("Helvetica", 14), bg=BG_COLOR, fg=TEXT_COLOR)
remaining_label.pack(pady=10)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
    button = tk.Button(root, text=letter, font=("Helvetica", 14), width=4, height=2,
                       bg=BUTTON_COLOR, fg=TEXT_COLOR,
                       command=lambda letter=letter: guess_letter(letter))
    button.pack(side="left", padx=2, pady=10)



root.mainloop()