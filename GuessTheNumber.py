import tkinter as tk
import random
import sys

form = tk.Tk()
form.title("Guess the Number")
form.state("normal")
form.geometry("450x400+300+300")
form.resizable(0, 0)


def initialization():
    global number, score, attempts

    number = random.randint(1, 100)
    score = 100
    attempts = 10


initialization()

title = tk.Label(form, text="Guess the Number!", font="roman 18 bold")
p = tk.Label(
    form, text="Guess a number between 1 and 100.\nYou have 10 attempts.")
attempt_label = tk.Label(form, text="Attempts:", font="roman 17 bold")
attempt_label2 = tk.Label(form, text=attempts, font="roman 17")
guess_label = tk.Label(form, text="Guess:", font="roman 17 bold")
guess_entry = tk.Entry(form)
label = tk.Label(form, text="", font="roman 15")


title.pack()
p.pack()
attempt_label.place(x=135, y=70)
attempt_label2.place(x=270, y=70)
guess_label.place(x=120, y=100)
guess_entry.place(x=214, y=105, width=90)
label.place(x=60, y=175)


def exit_game(): 
  sys.exit()

def restart_game():
    initialization()
    guess_entry.delete(0, tk.END)
    label.config(text="")
    attempt_label.config(state="normal")
    attempt_label2.config(state="normal", text=attempts)
    guess_label.config(state="normal")
    guess_entry.config(state="normal")
    button1.config(state="normal")
    yes.destroy()
    no.destroy()
    label2.destroy()


def game_over(s):
    global label2, yes, no

    attempt_label.config(state="disabled")
    attempt_label2.config(state="disabled")
    guess_label.config(state="disabled")
    guess_entry.config(state="disabled")
    button1.config(state="disabled")

    label2 = tk.Label(
        form, text="Do you want to play again?", font="roman 15")
    yes = tk.Button(form, text="Yes", fg="white", bg="green", command=restart_game)
    no = tk.Button(form, text="No", fg="white", bg="red", command=exit_game)

    label2.place(x=80, y=215+s)
    yes.place(x=150, y=246+s)
    no.place(x=220, y=246+s)


def check_guess():
    global guess, attempts, score
    if (guess_entry.get()).isdigit() and (not guess_entry.get() == "") and 0 < int(guess_entry.get()) <= 100:
        guess = int(guess_entry.get())
        if guess == number:
            label.config(
                text=f"                Correct!\n                Your Score: {score}")
            game_over(20)
        elif guess < number:
            attempts -= 1
            score -= 10
            label.config(text="                     Higher")
        elif guess > number:
            attempts -= 1
            score -= 10
            label.config(text=("                     Lower"))
        else:
            label.config(text="An unknown error occurred.")
    else:
        label.config(text="                     Error")
        
    if attempts == 0:
        label.config(text=f"You lost the game. Correct number: {number}")
        game_over(1)
    attempt_label2.config(text=attempts)


button1 = tk.Button(form, text="Guess", command=check_guess)
button1.place(x=180, y=140)

form.mainloop()
