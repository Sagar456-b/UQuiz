import random
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
import sqlite3


class Play:
    def __init__(self, module):
        self.module = module
        self.q_no = 0
        self.Question_no = 1
        self.data_size = 5
        self.correct = 0
        self.Review_q_no = 0
        self.Review_no = 1
        self.display_question(module)

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = self.correct
        wrong = wrong_count

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result =score

        # Shows a message box to display the result
        mb.showinfo("Result", f"Score:{result}%\nCorrect:{correct}\nWrong:{wrong}")

    def display_question(self, Module_name):
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()
        q_frame = Frame(bg="lightblue", width=700, height=1000)
        q_frame.pack(pady=70, padx=30)
        h = 0
        # self.opt_selected = IntVar()

        mm = StringVar()
        mm.set(0)
        c.execute(" SELECT HEADER FROM " + Module_name + "Questionbank WHERE NO =" + str(self.q_no) + ";")
        question = (c.fetchone()[0])
        w = Label(q_frame, text="Q.No " + str(self.Question_no) + ") " + question,
                  font=('ariel', 15, 'bold'), anchor='w', bg="lightblue", width=100)
        w.place(x=50, y=100)
        w.pack(padx=10, pady=20)

        for r in range(len([0, 1, 2, 3])):
            c.execute(
                " SELECT ANSWER" + str(h) + " FROM Answers" + Module_name + "Questionbank WHERE NO = " + str(
                    self.q_no) + ";")
            answer = (c.fetchone()[0].translate({ord('"'): None}))
            a = Radiobutton(q_frame, text=answer, variable=mm, value=answer, bg="lightblue")
            a.pack(pady=5)
            h = h + 1
            c.execute(
                " SELECT ANSWER0 FROM Answers" + Module_name + "Questionbank WHERE NO = " + str(self.q_no) + ";")
            correct_answer = (c.fetchone()[0]).translate({ord('"'): None})
        def check_ans():
            if mm.get() == correct_answer:
                return True
            # commit our command
            conn.commit()
            # close our command
            conn.close()

        def nxt():

            # q_frame.destroy()
            if check_ans():
                self.correct += 1

            self.q_no += 1
            self.Question_no += 1
            if self.q_no == 5:
                q_frame.destroy()
                self.display_result()

                wrong_count = self.data_size - self.correct
                correct = self.correct
                wrong = wrong_count

                # calcultaes the percentage of correct answers
                score = int(self.correct / self.data_size * 100)
                result = score
                Result_Frame = Frame(bg="crimson", width=900, height=1000)
                Result_Frame.pack(pady=20, padx=30)
                Label(Result_Frame, text="Congratulations ! YOU HAVE COMPLETED QUIZ", bg="crimson",
                      font=("Mochiy Pop P One", 20, "bold"),
                      fg="white", width=50, height=5).pack(padx=50, pady=5)
                Label(Result_Frame, text="Quiz Report", bg="crimson", fg="cyan", font=("EB Garamond", 20, "bold")).pack(padx=50, pady=5)
                Label(Result_Frame, text="Correct: " + f"{correct}", bg="crimson",fg="whitesmoke", font=("EB Garamond", 15, "bold")).pack()
                Label(Result_Frame, text="Wrong: " + f"{wrong}", bg="crimson",fg="whitesmoke", font=("EB Garamond", 15, "bold")).pack()
                Label(Result_Frame, text="Result: " + f"{result}%", bg="crimson",fg="whitesmoke", font=("EB Garamond", 15, "bold")).pack()

                # Button(text="Exit", command=Quit).pack()

                Feedback_Frame = Frame(Result_Frame, background="Lightblue")
                Feedback_Frame.pack(pady=20, padx=10)
                Feedback_title = Label(Feedback_Frame, text="Overall  Feedback:", fg="Green")
                Feedback_title.pack(side=TOP)
                Button_Frame = Frame()
                Button_Frame.pack()

                if correct > 2:

                    Label(Feedback_Frame, text="Wow! you got very good marks ",background="Lightblue", fg="Red").pack(pady=10, padx=10)
                    Label(Feedback_Frame, text="Keep on",background="Lightblue",fg="Red").pack()
                    Label(Feedback_Frame,
                          text="You got  " + f"{correct}" + " answer right  out of  " + f"{self.data_size} question",
                          fg="Red",
                          font="helvatica",background="Lightblue").pack(pady=10, padx=10)
                else:
                    Label(Feedback_Frame, text="Bad luck! you got very low marks ",background="Lightblue",fg="Red").pack(pady=10, padx=10)
                    Label(Feedback_Frame, text="Focus on your study ",background="Lightblue",fg="Red").pack()
                    Label(Feedback_Frame,
                          text="You got  " + f"{correct}" + " answer right  out of  " + f"{self.data_size} question",
                          fg="Red",background="Lightblue",
                          font="helvatica").pack(pady=10, padx=10)

                def save_file():
                    t_f = filedialog.asksaveasfilename(initialdir="/", title="Save file",
                                                       filetypes=[('All Files', '*.*'),
                                                                  ('Word Document', '*.docx'),
                                                                  ('Python Files', '*.py'),
                                                                  ('Text Document', '*.txt'), ('PDF', '*.pdf')])
                    if t_f:
                        if t_f.endswith(".dat"):
                            pass
                        else:
                            t_f = f'{t_f}'
                        Quiz_Report = open(t_f, "w")
                        Quiz_Report.write(
                            f"Quiz \n Paradigm of Programming \n Your Quiz Report: \n Correct answer : {correct} \n Wrong answer : {wrong} \n Your score(Precentage) : {result}%")
                        Quiz_Report.close()

                Report_Save = Button(Button_Frame, text="save", fg="Green", command=save_file)
                Report_Save.pack()
                def review_result():
                    Report_Save.destroy()
                    Result_Frame.destroy()
                    Review_frame = Frame()
                    Review_frame.pack()
                    Review_title = Label(Review_frame, text="Your Quiz Review ", font=("Helvatica",18,'bold'))
                    Review_title.pack(pady=10)

                    #**************connection
                    def review_loop():
                        conn = sqlite3.connect("question_bank12.db")
                        # create Cursor
                        c = conn.cursor()
                        q_frame = Frame(bg="lightblue", width=700, height=1000)
                        q_frame.pack()
                        # self.op = 0
                        # self.opt_selected = IntVar()

                        c.execute(" SELECT HEADER FROM " + self.module + "Questionbank WHERE NO =" + str(
                            self.Review_q_no) + ";")
                        # a = 0?
                        question = (c.fetchone()[0])
                        w = Label(q_frame, text="Q.No " + str(self.Review_no) + ") " + question,
                                  font=('ariel', 12, 'bold'), anchor='w', bg="lightblue", width=80)
                        w.pack(ipady=5)
                        for r in range(len([0, 1, 2, 3])):
                            a = mm.get()
                            c.execute(" SELECT ANSWER0 FROM Answers" + self.module + "Questionbank WHERE NO = " + str(
                                self.Review_q_no) + ";")
                            correct_answer = (c.fetchone()[0]).translate({ord('"'): None})

                        # Label(text=correct_answer).pack()

                        if a == correct_answer:
                            Label(text=a, bg="lightgreen", font=('ariel', 10), width=100).pack(ipady=5)
                            Label(text=correct_answer, bg="lightgreen", font=('ariel', 10), width=100).pack(ipady=5)
                        else:
                            Label(text=f"Your answer: {a}", bg="crimson", font=('ariel', 12), width=100).pack(ipady=5)
                            Label(text=f"Correct answer:  {correct_answer}", bg="lightgreen", font=('ariel', 12),
                                  width=100).pack(ipady=5)

                        # print(correct_answer)
                        conn.commit()
                        # close our command
                        conn.close()
                    #
                    def Next():
                        self.Review_q_no += 1
                        self.Review_no +=1
                        mm.get()
                        if self.Review_q_no >= 5:
                            mb.showinfo("Review completed","You have completed the Review \n Note:click okay to exit")


                        else:
                            review_loop()

                    Button(text="Show Next", command=Next).pack(pady=50, side=BOTTOM)
                    review_loop()

                Review_button = Button(Button_Frame, text="Review",fg = "Green", command=review_result)
                Review_button.pack()




            else:
                q_frame.destroy()
                self.display_question(self.module)

        Next_btn = Button(q_frame, text="Next", command=nxt, fg="green", border=1, highlightbackground="cyan",
                          font=("Helvatic", 15, "bold"))
        Next_btn.pack(pady=10, ipadx=5, ipady=5)
