import tkinter as tk
from tkinter import ttk
import random
from abc import ABC, abstractmethod

# Klasse til at repræsentere et datasæt
class DataSet:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    # Metode til at hente et tilfældigt spørgsmål og svar
    def get_question_and_answer(self):
        question, answer = random.choice(list(self.data.items()))
        return question, answer

    # Metode til at hente 3 forkerte svar og et korrekt svar
    def get_random_answers(self, correct_answer, n=3):
        all_answers = list(set(self.data.values()))  # Ensure uniqueness
        random_answers = random.sample(
            [ans for ans in all_answers if ans != correct_answer], n
        )
        random_answers.append(correct_answer)
        random.shuffle(random_answers)
        return random_answers


# Datasæt for SI-enheder
SI_Data = DataSet(
    "SI-enheder",
    {
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
        "Hvad er enheden for bølgelængde?": "meter",
        "Hvad er enheden for areal?": "kvadratmeter",
        "Hvad er enheden for volumen?": "kubikmeter",
        "Hvad er enheden for vinkelhastighed?": "radianer pr. sekund",
        "Hvad er enheden for acceleration?": "meter pr. sekund kvadreret",
        "Hvad er enheden for elektrisk ladning?": "coulomb",
        "Hvad er enheden for elektrisk feltstyrke?": "volt pr. meter",
        "Hvad er enheden for lydintensitet?": "decibel",
        "Hvad er enheden for lysflux?": "lumen",
        "Hvad er enheden for belysningsstyrke?": "lux",
    },
)

# Datasæt for præfikser
Prefix_Data = DataSet(
    "Præfikser",
    {
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
    },
)

# Liste af datasæt
Data = [SI_Data, Prefix_Data]

# Abstrakt klasse til at repræsentere en kommando
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Klasse til at repræsentere en kommando til at vælge et svar
class SelectAnswerCommand(Command):
    def __init__(self, app, answer):
        self.app = app
        self.answer = answer
    
    def execute(self):
        self.app.select_answer(self.answer)

# Klasse til at repræsentere en kommando til at tjekke et svar
class CheckAnswerCommand(Command):
    def __init__(self, app):
        self.app = app

    def execute(self):
        self.app.check_answer()

# Klasse til at repræsentere hovedmenuen
class QuizAppMenu:
    def __init__(self, root):
        self.root = root

        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid(sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Start knap
        self.bs = tk.Button(self.frm, text="Start", command=self.startQuizTopicSelection)
        self.bs.grid(sticky="ew")

        # Quit knap
        self.bq = tk.Button(self.frm, text="Quit", command=root.destroy)
        self.bq.grid(sticky="ew")

        self.frm.grid_columnconfigure(0, weight=1)

    # Metode til at starte valg af emne
    def startQuizTopicSelection(self):
        self.bs.destroy()
        self.bq.destroy()
        self.frm.destroy()
        self.app = QuizAppTopicSelect(self.root)

# Klasse til at repræsentere valg af emne
class QuizAppTopicSelect:
    def __init__(self, root):
        self.root = root

        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid(sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Opret knapper for hvert datasæt
        self.buttons = [tk.Button(self.frm, text=data.name, command=lambda d=data: self.selectMode(d)) for data in Data]
        for i, button in enumerate(self.buttons):
            button.grid(sticky="ew")

        # Tilbage knap
        self.bb = tk.Button(self.frm, text="Tilbage", command=self.backToMenu)
        self.bb.grid(sticky="ew")

        self.frm.grid_columnconfigure(0, weight=1)
        for i in range(len(self.buttons) + 2):
            self.frm.grid_rowconfigure(i, weight=1)

    # Metode til at starte valg af spil mode
    def selectMode(self, selected_data):
        for button in self.buttons:
            button.destroy()
        self.bb.destroy()
        self.frm.destroy()

        self.app = QuizAppSelectMode(self.root, selected_data)

    # Metode til at gå tilbage til hovedmenuen
    def backToMenu(self):
        for button in self.buttons:
            button.destroy()
        self.bb.destroy()
        self.frm.destroy()

        # Gå tilbage til hovedmenuen
        self.app = QuizAppMenu(self.root)

    # Metode til at afslutte programmet
    def quitApp(self):
        self.root.quit()

# Klasse til at repræsentere valg af spil mode
class QuizAppSelectMode:
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid(sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Uendelig knap
        self.bi = tk.Button(self.frm, text="Uendelig", command=lambda: self.startQuiz("Infinite"))
        self.bi.grid(sticky="ew")

        # Hardcore knap
        self.bh = tk.Button(self.frm, text="Hardcore", command=lambda: self.startQuiz("Hardcore"))
        self.bh.grid(sticky="ew")

        # Tilbage knap
        self.bb = tk.Button(self.frm, text="Tilbage", command=self.backToTopicSelection)
        self.bb.grid(sticky="ew")

        self.frm.grid_columnconfigure(0, weight=1)
        for i in range(3):
            self.frm.grid_rowconfigure(i, weight=1)

    # Metode til at starte spillet
    def startQuiz(self, mode):
        self.bi.destroy()
        self.bh.destroy()
        self.bb.destroy()
        self.frm.destroy()
        self.app = QuizApp(self.root, self.data, mode)

    # Metode til at gå tilbage til valg af emne
    def backToTopicSelection(self):
        self.bi.destroy()
        self.bh.destroy()
        self.bb.destroy()
        self.frm.destroy()
        self.app = QuizAppTopicSelect(self.root)

# Klasse til at repræsentere spillet
class QuizApp:
    def __init__(self, root, data, mode):
        self.root = root
        self.data = data
        self.mode = mode
        self.score = 0
        self.incorrect_answers = 0

        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid(sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Label til spørgsmål
        self.ql = tk.Label(self.frm, text="")
        self.ql.grid(row=0, column=0, columnspan=2, sticky="ew")

        # 4 Knapper til svar muligheder
        self.answer_buttons = [ttk.Button(self.frm) for _ in range(4)]
        for i, button in enumerate(self.answer_buttons):
            button.grid(row=1 + i // 2, column=i % 2, sticky="ew")

        self.check_answer_command = CheckAnswerCommand(self)

        # Tjek svar knap
        self.bs = tk.Button(self.frm, text="Tjek svar", command=self.check_answer_command.execute)
        self.bs.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Tjek svar på enter
        self.root.bind("<Return>", lambda event: self.check_answer_command.execute())

        # Score label
        self.score_label = tk.Label(self.frm, text="Score: 0")
        self.score_label.grid(row=4, column=0, columnspan=2, sticky="ew")

        # Hvis der spilles i uendelig mode, tilføj stop knap
        if self.mode == "Infinite":
            self.stop_button = tk.Button(self.frm, text="Afslut quiz", command=self.stopQuiz)
            self.stop_button.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.generateQuestionAndAnswers()

        self.frm.grid_columnconfigure(0, weight=1)
        self.frm.grid_columnconfigure(1, weight=1)
        for i in range(6):
            self.frm.grid_rowconfigure(i, weight=1)

    # Metode til at generere spørgsmål og svar
    def generateQuestionAndAnswers(self):
        question, self.correctAnswer = self.data.get_question_and_answer()
        self.ql.config(text=question)
        
        random_answers = self.data.get_random_answers(self.correctAnswer, 3)
        for button, answer in zip(self.answer_buttons, random_answers):
            select_answer_command = SelectAnswerCommand(self, answer)
            button.config(text=answer, command=select_answer_command.execute)

        self.frm.grid_columnconfigure(0, weight=1)
        self.frm.grid_columnconfigure(1, weight=1)
        for i in range(6):
            self.frm.grid_rowconfigure(i, weight=1)

    # Metode til at stoppe spillet
    def stopQuiz(self):
        if self.mode == "Infinite":
            self.endQuiz(f"Quiz afsluttet. Din score: {self.score}, Ukorrekte svar: {self.incorrect_answers}")

    # Metode til at afslutte spillet
    def endQuiz(self, message):
        for widget in self.frm.winfo_children():
            widget.destroy()
        
        tk.Label(self.frm, text=message, font=("Arial", 14)).grid()
        tk.Button(self.frm, text="Tilbage til menu", command=self.backToMenu).grid()

    # Metode til at gå tilbage til hovedmenuen
    def backToMenu(self):
        self.frm.destroy()
        QuizAppMenu(self.root)

    # Metode til at vælge et svar
    def select_answer(self, answer):
        self.selectedAnswer = answer

    # Metode til at tjekke et svar
    def check_answer(self):
        if self.selectedAnswer == self.correctAnswer:
            self.score += 1
            self.bs.config(background ='green', foreground='white')
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.bs.config(background ='red', foreground='white')
            self.incorrect_answers += 1
            if self.mode == "Hardcore":
                self.root.after(1000, lambda: self.endQuiz(f"Game over! Din score: {self.score}"))
                return
        self.generateQuestionAndAnswers()

# Opret root vindue
root = tk.Tk()
root.geometry("500x500")
root.title("Fysik Quiz")

# Start hovedmenuen
app = QuizAppMenu(root)

# Start mainloop
root.mainloop()
