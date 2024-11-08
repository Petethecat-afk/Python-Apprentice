from tkinter import messagebox, simpledialog, Tk

# Make a new window variable, window = Tk()
window = Tk()  # ;

# Hide the window using the window's .withdraw() method
window.withdraw()  # ;

# 1. Create a variable to hold the user's score. Set it equal to zero.
score = 0  # ;

response = simpledialog.askstring(None, "Who is better mickey or pelayo")  # ;

if response.lower() == "pelayo":  # ;
    score += 1  # ;
    print("Correct! Your score is " + str(score))  # ;
else:  # ;
    score -= 1  # ;
    messagebox.showerror(message="WRONG! its pelayo!")  # ;

messagebox.showinfo(message="Your final score is " + str(score))  # ;
# ASK A QUESTION AND CHECK THE ANSWER

# // 2. Ask the user a question


# // 3. Use an if statement to check if their answer is correct

# // 4. if the user's answer was correct, add one to their score

# MAKE MORE QUESTIONS. Ask more questions by repeating the above
# // Option: Subtract a point from their score for a wrong answer

# After all the questions have been asked, tell the user their final score
# remember to convert your score variable to a string using the str() function


score = 0  # ;

questions = [  # ;
    "Why is Micky so cute?",  # ;,  # ;
    "do you like touchy the rat",  # ;
    "is touchy the gonna touch you :3",  # ;
    "do you think that touchy the rat is mickey?",  # ;
    "how did you know",  # ;
    "do you think peter is touchy the rat", # ;
    "great job you completed the fist part of the test", # ;
    "what is 2 + 2", # ;
    "what is 10 to the pwer of 11"
]  # ;

answers = ["he has that pedifile rizz", "Yes :3", "of course i am bucko", "yes", "Peter", "...yes i am", "yippe", "4",  "10,000,000,    000"]  # ;

# Loop through each question in the questions list and ask the user for their response to each one using the simpledialog.askstring() method and an if statement to check if their response is correct or not and change the score accordingly using the score variable you created earlier.  # ;
for i in range(len(questions)):  # ;
    response = simpledialog.askstring(None, questions[i])  # ;

    if response.lower() == answers[i]:  # ;
        score += 1  # ;
        print("Correct! Your score is " + str(score))  # ;
    else:  # ;
        score -= 999  # ;
        messagebox.showerror(message="WRONG! It's " + answers[i] + " of course!")  # ;

messagebox.showinfo(message="Your final score is " + str(score))  # ;

# Run the window's .mainloop() method
window.mainloop()  # ;




