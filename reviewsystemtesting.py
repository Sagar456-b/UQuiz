import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import  filedialog
# from GUI_UPDATED import GUI
# from  os import startfile
# import tempfile
import sqlite3


window = tk.Tk()

class Play_Programming:
    def __init__(self):
        self.q_no = 0
        self.Question_no = 1
        self.data_size = 5
        self.correct = 0
        # self.result_frame = Frame()
        self.display_question()
        # self.mm = StringVar()
        # self.opts = self.radio_buttons()
        # self.display_result()
        # self.check_ans()
        self.Review_no = 1
        self.op = 0
        # self.review()



    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def display_question(self):
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()
        q_frame = Frame(bg="lightblue", width=700, height=1000)
        q_frame.pack(pady=70, padx=30)
        h = 0
        # self.opt_selected = IntVar()

        mm = StringVar()
        mm.set(0)
        c.execute(" SELECT HEADER FROM " + "Programming" + "Questionbank WHERE NO =" + str(self.q_no) + ";")
        question = (c.fetchone()[0])
        w = Label(q_frame, text="Q.No " + str(self.Question_no) + ") " + question,
                  font=('ariel',17, 'bold'), anchor='w', bg="lightblue", width=80)
        w.place(x=50, y=100)
        w.pack(padx=90, pady=20)

        for r in range(len([0, 1, 2, 3])):

            c.execute(
                " SELECT ANSWER" + str(h) + " FROM Answers" + "Programming" + "Questionbank WHERE NO = " + str(
                    self.q_no) + ";")
            answer = (c.fetchone()[0].translate({ord('"'): None}))
            a = Radiobutton(q_frame, text=answer, variable=mm, value=answer, bg="lightblue")
            a.pack(pady=5)
            h = h + 1
            c.execute(" SELECT ANSWER0 FROM Answers" + "Engineering" + "Questionbank WHERE NO = " + str(self.q_no) + ";")
            correct_answer = (c.fetchone()[0]).translate({ord('"'): None})
            # print(list)



        def check_ans():
            if mm.get() == correct_answer:
                return  True
            # am = mm.get()
            # Label(text=am).pack()
            # commit our command
            conn.commit()
            # close our command
            conn.close()




                # Label(text=question).pack()




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
                wrong =wrong_count

                # calcultaes the percentage of correct answers
                score = int(self.correct / self.data_size * 100)
                result = f"Score: {score}%"
                Result_Frame =Frame(bg="crimson", width=900, height=1000)
                Result_Frame.pack(pady=20, padx=30)
                Label(Result_Frame, text="Congratulations ! YOU HAVE COMPLETED QUIZ",bg="crimson",
                      font=("Mochiy Pop P One",20,"bold"),
                      fg="white", width=50, height=5).pack(padx=50,pady=5)
                Label(Result_Frame,text="Quiz Report",bg="crimson").pack(padx=50,pady=5)
                Label(Result_Frame,text="Correct:" + f"{correct}",bg="crimson").pack(padx=30,pady=5)
                Label(Result_Frame,text="Wrong:" + f"{wrong}",bg="crimson").pack(padx=30,pady=5)
                Label(Result_Frame,text="Result:" + f"{result}",bg="crimson").pack(padx=30,pady=5)


                # Button(text="Exit", command=Quit).pack()





                if correct > 2:

                    Label(Result_Frame,text="Wow! you got very good marks ").pack(pady=10, padx=10)
                    Label(text="Keep on").pack()
                    Label(text="You got  " + f"{correct}" + " answer right  out of  " + f"{self.data_size} question", fg="Red",
                    font="helvatica").pack(pady=10,padx=10)
                else:
                    Label(Result_Frame, text="Bad luck! you got very low marks ").pack(pady=10, padx=10)
                    Label(Result_Frame, text="Focus on your study ").pack()
                    Label(Result_Frame, text="You got  " + f"{correct}" + " answer right  out of  " + f"{self.data_size} question",
                          fg="Red",
                          font="helvatica").pack(pady=10, padx=10)

                    # creating file


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
                                f"Quiz \n Paradigm of Programming \n Your Quiz Report: \n Correct answer : {correct} \n Wrong answer : {wrong} \n Your score(Precentage) : {result}")
                        Quiz_Report.close()



                Report_Save = Button(text="save", command=save_file)
                Report_Save.pack()

                def review_result():
                    Report_Save.destroy()
                    Result_Frame.destroy()
                    Review_frame = Frame()
                    Review_frame.pack()
                    Review_title = Label(Review_frame, text="Your Quiz Review ", font=("Helvatica",18,'bold'))
                    Review_title.pack(pady=10)

                    #**************connection
                    conn = sqlite3.connect("question_bank12.db")
                    # create Cursor
                    c = conn.cursor()
                    q_frame = Frame(bg="lightblue", width=700, height=1000)
                    q_frame.pack()
                    # self.op = 0
                    # self.opt_selected = IntVar()


                    c.execute(" SELECT HEADER FROM " + "Programming" + "Questionbank WHERE NO =" +str(self.op) + ";")
                    # a = 0?
                    question = (c.fetchone()[0])
                    w = Label(q_frame, text="Q.No " + str(self.Review_no) + ") " + question,
                              font=('ariel', 15, 'bold'), anchor='w', bg="lightblue", width=80)
                    w.pack(ipady=5)
                    for r in range(len([0, 1, 2, 3])):
                        c.execute(" SELECT ANSWER0 FROM Answers" + "Engineering" + "Questionbank WHERE NO = " + str(
                            self.op) + ";")
                        correct_answer = (c.fetchone()[0]).translate({ord('"'): None})



                    # Label(text=correct_answer).pack()

                    if mm.get == correct_answer:
                        Label(text=mm.get(), bg="lightgreen",width=100).pack(ipady=5)
                        Label(text=correct_answer, bg="lightgreen", width=100).pack(ipady=5)
                    else:
                        Label(text=f"Your answer: {mm.get()}", bg="crimson",width=100).pack(ipady=5)
                        Label(text=f"Correct answer:  {correct_answer}", bg="lightgreen",width=100).pack(ipady=5)

                    # print(correct_answer)
                    conn.commit()
                    # close our command
                    conn.close()

                    def Next():
                        self.op += 1
                        self.Review_no +=1
                        mm.get()
                        if self.op >= 5:
                            mb.showinfo("Review completed","You have completed the Review \n Note:click okay to exit")
                            # self.display_question()
                            window.destroy()
                        else:
                            review_result()
                    Button(text="Show Next", command=Next).pack(pady=5)
                Button(text="Review", command=review_result).pack()


            else:
                q_frame.destroy()
                self.display_question()

        Next_btn = Button(q_frame, text="Next", command=nxt, fg= "green", border=1, highlightbackground="cyan",
                          font=("Helvatic",15,"bold"))
        Next_btn.pack(pady=10, ipadx=5, ipady=5)
Play_Programming()
window.mainloop()