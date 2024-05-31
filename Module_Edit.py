
from tkinter import *
from tkinter import messagebox as mb
import Quiz
import sqlite3


class Add_Module:
    def __init__(self,root):
        self.root = root
        self.Add()

    def Add(self):
        New_window = Toplevel(self.root)
        New_window.geometry("300x300")
        module_var = StringVar()
        code_var = IntVar()
        add_Frame = Frame(New_window)
        add_Frame.pack()
        Label(add_Frame, text="Module name").pack()
        Entry(add_Frame, textvariable=module_var).pack()
        Label(add_Frame, text="Module code").pack()
        Entry(add_Frame, textvariable=code_var).pack()

        # Creating submit button and joining it to the database
        def submit():
            # connect to a database
            conn = sqlite3.connect("question_bank12.db")
            # create Cursor
            c = conn.cursor()

            Quiz.module_table.add_module(code_var.get(), module_var.get())

            # commit our command
            conn.commit()
            # close our command
            conn.close()

            mb.showinfo("Added", f"{code_var}{module_var.get()} has been added succesfully")

            New_window.destroy()

        Button(New_window, text="Submit", command=submit).pack()
        New_window.mainloop()

class Delete_module():
    def __init__(self,root):
        self.root = root
        self.delete()

    def delete(self):
        New_window = Toplevel(self.root)
        New_window.geometry("300x300")
        delete_var = StringVar()
        delete_frame = Frame(New_window)
        delete_frame.pack()
        Delete_title = Label(delete_frame, text="Delete Module", font=("helvatica", 15, "bold"))
        Delete_title.pack()
        Delete_Module = Label(delete_frame, text="Module name")
        Delete_Module.pack()
        Entry(delete_frame, textvariable=delete_var).pack()

        def submit():
            # connect to a database
            conn = sqlite3.connect("question_bank12.db")
            # create Cursor
            c = conn.cursor()

            Quiz.module_table.delete_module(delete_var.get())

            # commit our command
            conn.commit()
            # close our command
            conn.close()

            mb.showinfo("Delete Module", f" {delete_var.get()} has been added succesfully deleted")
            # window.destroy()

        Button(delete_frame, text="Submit", command=submit).pack()
        New_window.mainloop()
