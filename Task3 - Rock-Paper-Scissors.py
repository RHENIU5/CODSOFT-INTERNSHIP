import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices list
choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        outcome = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        outcome = "You Win!"
        user_score += 1
    else:
        outcome = "You Lose!"
        computer_score += 1

    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{outcome}")
    score_text.set(f"Score → You: {user_score} | Computer: {computer_score}")

# Reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("Make your move!")
    score_text.set("Score → You: 0 | Computer: 0")

# Main GUI window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.resizable(False, False)

# Heading
tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16, "bold")).pack(pady=10)

# Result display
result_text = tk.StringVar()
result_text.set("Make your move!")
tk.Label(root, textvariable=result_text, font=("Arial", 12), wraplength=350, justify="center").pack(pady=10)

# Score display
score_text = tk.StringVar()
score_text.set("Score → You: 0 | Computer: 0")
tk.Label(root, textvariable=score_text, font=("Arial", 12, "italic")).pack(pady=5)

# Buttons for user choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Reset Button
tk.Button(root, text="Reset Game", command=reset_game, bg="#f2f2f2").pack(pady=10)

# Run the app
root.mainloop()
