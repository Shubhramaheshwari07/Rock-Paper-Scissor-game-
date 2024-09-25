import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For loading images
import random
import os

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def user_choice(choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(choice, computer_choice)

    # Update the labels with computer choice and result
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=f"Result: {result}")

    # Update result color dynamically
    if "win" in result:
        result_label.config(fg="green")
    elif "lose" in result:
        result_label.config(fg="red")
    else:
        result_label.config(fg="orange")

# Function to quit the game
def quit_game():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Set window size
root.geometry("600x400")

# Load background image
background_img = Image.open("background.jpg")
background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(background_img)

# Create a label to hold the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Set the image to cover the entire window

# Create a frame to hold the game elements
game_frame = tk.Frame(root, bg="white", bd=5)
game_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = tk.Label(game_frame, text="Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), bg="white")
title_label.grid(row=0, column=1, pady=10)

# Load images for Rock, Paper, Scissors buttons
rock_img = Image.open("rock.png").resize((80, 80), Image.Resampling.LANCZOS)
rock_photo = ImageTk.PhotoImage(rock_img)

paper_img = Image.open("paper.png").resize((80, 80), Image.Resampling.LANCZOS)
paper_photo = ImageTk.PhotoImage(paper_img)

scissors_img = Image.open("scissors.png").resize((80, 80), Image.Resampling.LANCZOS)
scissors_photo = ImageTk.PhotoImage(scissors_img)

# Create buttons for Rock, Paper, Scissors
rock_button = tk.Button(game_frame, image=rock_photo, command=lambda: user_choice('rock'), borderwidth=0)
rock_button.grid(row=1, column=0, padx=10)

paper_button = tk.Button(game_frame, image=paper_photo, command=lambda: user_choice('paper'), borderwidth=0)
paper_button.grid(row=1, column=1, padx=10)

scissors_button = tk.Button(game_frame, image=scissors_photo, command=lambda: user_choice('scissors'), borderwidth=0)
scissors_button.grid(row=1, column=2, padx=10)

# Create a label for computer's choice
computer_label = tk.Label(game_frame, text="Computer chose: ", font=("Helvetica", 14), bg="white")
computer_label.grid(row=2, column=1, pady=10)

# Create a label for displaying the result
result_label = tk.Label(game_frame, text="Result: ", font=("Helvetica", 16, "bold"), bg="white")
result_label.grid(row=3, column=1, pady=20)

# Create a Quit button
quit_button = tk.Button(root, text="Quit", command=quit_game, font=("Helvetica", 12, "bold"), bg="red", fg="white")
quit_button.pack(pady=20)

# Start the GUI main loop
root.mainloop()
