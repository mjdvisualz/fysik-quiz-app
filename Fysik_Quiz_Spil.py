import tkinter as tk
from tkinter import ttk
import random
from abc import ABC

#Liste af SI-enheder
SI_Data = {
    "Hvad er enheden for længde?": "meter",
    "Hvad er enheden for masse?": "kilogram",
    "Hvad er enheden for tid?": "sekund",
    "Hvad er enheden for strøm?": "ampere",
    "Hvad er enheden for temperatur?": "kelvin",
    "Hvad er enheden for stofmængde?": "mol",
    "Hvad er enheden for lysstyrke?": "candela",
    "Hvad er enheden for kraft?": "newton",
    "Hvad er enheden for energi?": "joule",
    "Hvad er enheden for tryk?": "pascal",
    "Hvad er enheden for frekvens?": "hertz",
    "Hvad er enheden for elektrisk spænding?": "volt",
    "Hvad er enheden for elektrisk modstand?": "ohm",
    "Hvad er enheden for elektrisk kapacitans?": "farad",
    "Hvad er enheden for magnetisk flux?": "weber",
    "Hvad er enheden for magnetisk fluxtæthed?": "tesla",
    "Hvad er enheden for induktans?": "henry",
}

#Liste af præfikser
Prefix_Data = {
    "Hvad er præfikset for 10^24?": "yotta",
    "Hvad er præfikset for 10^21?": "zetta",
    "Hvad er præfikset for 10^18?": "exa",
    "Hvad er præfikset for 10^15?": "peta",
    "Hvad er præfikset for 10^12?": "tera",
    "Hvad er præfikset for 10^9?": "giga",
    "Hvad er præfikset for 10^6?": "mega",
    "Hvad er præfikset for 10^3?": "kilo",
    "Hvad er præfikset for 10^2?": "hekto",
    "Hvad er præfikset for 10^1?": "deka",
    "Hvad er præfikset for 10^-1?": "deci",
    "Hvad er præfikset for 10^-2?": "centi",
    "Hvad er præfikset for 10^-3?": "milli",
    "Hvad er præfikset for 10^-6?": "mikro",
    "Hvad er præfikset for 10^-9?": "nano",
    "Hvad er præfikset for 10^-12?": "piko",
    "Hvad er præfikset for 10^-15?": "femto",
    "Hvad er præfikset for 10^-18?": "atto",
    "Hvad er præfikset for 10^-21?": "zepto",
    "Hvad er præfikset for 10^-24?": "yokto",
}

class AppStart:
    def __init__(self, root, data):
     self.root = root
     self.data = data




class QuizAppUnlimited:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.selectedButton = None
        self.correctAnswer = None
        self.frm = ttk.Frame(root, padding=100)
        self.frm.grid()

        # Create a label for the question
        self.ql = ttk.Label(self.frm, text="")
    
        self.ql.grid(column=0, row=0, columnspan=2)
  
        # Create buttons for answers
        self.answer_buttons = [tk.Button(self.frm)  for _ in range(4)]
        for i, button in enumerate(self.answer_buttons):
            button.grid(column=i % 2, row=1 + i // 2)
            button.config(background = 'grey', foreground = 'black')   


        # Create the submit button
        self.bs = tk.Button(self.frm, text="Tjek svar", command=self.checkAnswer)
        self.bs.place(relx=0.5, rely=1.25, anchor='center')

        # Generate the first question and answers
        self.generateQuestionAndAnswers()

    def generateQuestionAndAnswers(self):
        question, self.correctAnswer = random.choice(list(self.data.items()))
        self.ql.config(text=question)  # Update the question label

        # Gather all possible answers and shuffle them
        all_answers = list(self.data.values())
        random.shuffle(all_answers)

        # Ensure three unique random answers different from the correct answer
        random_answers = [answer for answer in all_answers if answer != self.correctAnswer][:3]
        random_answers.append(self.correctAnswer)
        random.shuffle(random_answers)

        # Update button texts with answers
        for button, answer in zip(self.answer_buttons, random_answers):
            button.config(text=answer, command=lambda a=answer: self.onSelected(a))
            
            
            
           

    def onSelected(self, a):
        self.selectedButton = a
        print("you clicked on " + a)
           

    def checkAnswer(self):
        if self.selectedButton == self.correctAnswer:
            print("Congratulations you have the correct answer.")
            self.bs.config(background ='green', foreground='white')  # Change to green on correct answer
            self.generateQuestionAndAnswers()
        else:
            print("Better luck next time, your answer was incorrect.")
            self.bs.config(background ='red', foreground='white')  # Reset to default colors on incorrect answer
            # Generate a new question and answers
            self.generateQuestionAndAnswers()

      

# Create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("Fysik Quiz")

app = QuizAppUnlimited(root, SI_Data)

# Start the application
root.mainloop()