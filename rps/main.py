import tkinter as tk
import customtkinter as ctk
import random

# Initialize the main window
root = ctk.CTk()
root.title("Rock Paper Scissors")

# Initialize scores
player_score = 0
computer_score = 0
total_games = 0


# Function to update the scores and win percentage
def update_scores():
    player_score_label.configure(text=f"Player Score: {player_score}")
    computer_score_label.configure(text=f"Computer Score: {computer_score}")
    win_percentage = (player_score / total_games) * 100 if total_games > 0 else 0
    win_percentage_label.configure(text=f"Win Percentage: {win_percentage:.2f}%")


# Function to handle player's choice
def play(player_choice):
    global player_score, computer_score, total_games
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result_label.configure(text=f"Draw! Both chose {player_choice}")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        player_score += 1
        result_label.configure(text=f"You Win! {player_choice} beats {computer_choice}")
    else:
        computer_score += 1
        result_label.configure(
            text=f"You Lose! {computer_choice} beats {player_choice}"
        )

    total_games += 1
    update_scores()


# Create buttons for Rock, Paper, and Scissors
rock_button = ctk.CTkButton(root, text="Rock", command=lambda: play("Rock"))
paper_button = ctk.CTkButton(root, text="Paper", command=lambda: play("Paper"))
scissors_button = ctk.CTkButton(root, text="Scissors", command=lambda: play("Scissors"))

# Create labels for scores and result
player_score_label = ctk.CTkLabel(root, text=f"Player Score: {player_score}")
computer_score_label = ctk.CTkLabel(root, text=f"Computer Score: {computer_score}")
result_label = ctk.CTkLabel(root, text="")
win_percentage_label = ctk.CTkLabel(root, text="Win Percentage: 0.00%")

# Place widgets on the window
player_score_label.pack(pady=10)
computer_score_label.pack(pady=10)
result_label.pack(pady=10)
win_percentage_label.pack(pady=10)
rock_button.pack(side=tk.LEFT, padx=20, pady=20)
paper_button.pack(side=tk.LEFT, padx=20, pady=20)
scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

# Run the main loop
root.mainloop()
