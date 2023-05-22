from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        canvas = Canvas(width=400, height=600, bg=THEME_COLOR, highlightthickness=0)
        canvas.grid(column=0, row=0, columnspan=2, rowspan=4)

        label_score = Label(text="Score : TODO",font=("Arial",12,"bold"),bg=THEME_COLOR,fg="white")
        label_score.grid(column=1,row=0)

        label_question = Label(text="TODO",font=("Arial",40,"italic"),width=10,height=5)
        label_question.grid(column=0,row=1,columnspan=2)

        image_right = PhotoImage(file="images/true.png")
        image_wrong = PhotoImage(file="images/false.png")

        button_right = Button(image=image_right,highlightthickness=0)
        button_right.grid(column=0,row=2)

        button_wrong = Button(image=image_wrong,highlightthickness=0)
        button_wrong.grid(column=1,row=2)

        self.window.mainloop()