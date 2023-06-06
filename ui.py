from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label_score = Label(text="Score : 0",bg=THEME_COLOR,fg="white")
        self.label_score.grid(column=1,row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2)

        # self.label_question = Label(text="TODO",font=("Arial",40,"italic"),width=10,height=5)
        # self.label_question.grid(column=0,row=1,columnspan=2)

        image_right = PhotoImage(file="images/true.png")
        image_wrong = PhotoImage(file="images/false.png")

        self.button_true = Button(image=image_right,highlightthickness=0,command=self.true_pressed)
        self.button_true.grid(column=0,row=2)

        self.button_false = Button(image=image_wrong,highlightthickness=0,command=self.false_pressed)
        self.button_false.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback((is_right))

    def give_feedback(self,is_right): #TODO next
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



