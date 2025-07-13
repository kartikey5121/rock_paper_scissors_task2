import tkinter as tk
import random

def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result_text.set(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        result_text.set(result_text.get() + "\nIt's a Tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result_text.set(result_text.get() + "\nYou Win!")
    else:
        result_text.set(result_text.get() + "\nYou Lose!")

app = tk.Tk()
app.title("Rock-Paper-Scissors Game")
app.geometry("500x300")
app.configure(background="#f4ee45")  

title_label = tk.Label(app, text="Rock-Paper-Scissors", font=("Arial", 26, "bold"), bg="#f4ee45", fg="#000000")
title_label.pack(pady=10)

result_text = tk.StringVar()
result_text.set("Make your choice!")
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 16), bg="#f4ee45", fg="#000000")
result_label.pack(pady=20)

button_frame = tk.Frame(app, bg="#f4ee45")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text=" Rock ", font=("Arial", 12, "bold"), bg="#ed709a", fg="#000000", command=lambda: determine_winner('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text=" Paper ", font=("Arial", 12, "bold"), bg="#61ee5e", fg="#000000", command=lambda: determine_winner('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text=" Scissors ", font=("Arial", 12, "bold"), bg="#9a92e6", fg="#000000", command=lambda: determine_winner('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)
exit_button = tk.Button(app, text=" Exit ", font=("Arial", 12, "bold"), bg="#ffffff", fg="#000000", command=app.quit)
exit_button.pack(pady=20)

app.mainloop()
