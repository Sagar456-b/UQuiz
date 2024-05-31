import Quiz
from tkinter import *
from tkinter import messagebox as mb
import sqlite3


class Add_question:
    def __init__(self, root, module_name):
        self.root = root
        self.module_name = module_name
        self.add(module_name)

    def add(self, module_name):
        # making new window for add question
        New_window = Toplevel(self.root)
        New_window.geometry("300x300")  # screen size of window

        # defining variable types
        question_var = answer_var = StringVar()

        # Defining Frame for Adding Question
        Add_Frame = Frame(New_window)
        Add_Frame.pack()

        # defining title for Interface
        title = Label(Add_Frame, text="ADD QUESTION", font=("helvatica", 15, "bold"), fg="red")
        title.pack(pady=10)

        # Creating user question input box for user
        Question_label = Label(Add_Frame, text="Question")
        Question_label.pack()
        Question_input = Entry(Add_Frame, textvariable=question_var)
        Question_input.pack()

        # Creating user answer input box for user
        Answer_label = Label(Add_Frame, text="Answer")
        Answer_label.pack()
        Answer_input = Entry(Add_Frame, textvariable=answer_var)
        Answer_input.pack()

        # Creating  making a function submit for submit button and joining it to the database
        def submit():
            x = 1
            y = "MCQ"
            z = question_var.get()
            w = answer_var.get()

            #passing argutment to function add_question whici is connected to the database
            Quiz.module_table.add_question(module_name, x, y, z, w)

            #mb display the message box
            mb.showinfo("Added", f"Your question {question_var.get()} has been added succesfully")

        Submit_button = Button(Add_Frame, text="Submit", command=submit, fg="green")
        Submit_button.pack(ipady=5, pady=20)
        New_window.mainloop()  # closing the new window


class Delete_question:
    def __init__(self, root):
        self.delete(root)
        self.root = root

    def delete(self):
        New_window = Toplevel(self.root)
        New_window.geometry("300x300")
        delete_question = IntVar()
        delete_frame = Frame(New_window)
        delete_frame.pack()
        Delete_title = Label(delete_frame, text="Delete Question", font=("helvatica", 15, "bold"), fg="red")
        Delete_title.pack(pady=20)
        Delete_Label = Label(delete_frame, text="Question no")
        Delete_Label.pack()
        Entry(delete_frame, textvariable=delete_question).pack()

        def submit():
            # connect to a database
            conn = sqlite3.connect("question_bank12.db")
            # create Cursor
            c = conn.cursor()

            Quiz.module_table.delete_question(delete_question.get())
            # Quiz.module_table.add_question()

            # commit our command
            conn.commit()
            # close our command
            conn.close()

            mb.showinfo("Delete Module", f" {delete_question.get()} has been added succesfully deleted")
            # GUI.Screen()

        Button(delete_frame, text="Submit", command=submit, fg="green").pack(ipady=5, pady=20)
        New_window.mainloop()

# dlt()
# window.mainloop()
