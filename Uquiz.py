"""""""""

                      QUIZ GENERATOR SYSTEM

DEVELOPED BY:
     BOM BAHADUR THAPA
     Student is :: 001196411
     SEBASTRIAN Martinez Zuleta 
     Student id :: 006222220
     
"""""""""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from Play_Frame import Play
from Module_Edit import Add_Module, Delete_module
from Question_Edit import Delete_question, Add_question


# ************************************************Defining the user interface for system*******************************
# creating the main class GUI
class GUI:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.Screen()

    def Screen(self):  # defininig the function screen which contain the widgets for our first interfgace
        # ***************************************** First Interface of software ***************************************
        First_page = ttk.Frame(self.root)  # this define first frame for GUI, which contain button and label
        First_page.pack(padx=20, pady=20)

        # Displaying welcome message in interface
        Welcome_msg = Label(First_page, text="WELCOME  TO  UQUIZ", font=('Ariel bold', 30), fg='Red')
        Welcome_msg.pack(padx=40, pady=40)

        # function for onclick on button Start
        def Start_btn():
            First_page.destroy()
            self.Main_menu()

        # --------FIRST BUTTON START------------------------------------
        Start_button = Button(First_page, text="START", command=Start_btn, font="helvetica, 30", fg="Green", width=10,
                              highlightbackground="lightblue")
        Start_button.pack(pady=90, padx=90, ipady=10, ipadx=5)

    # ********************************************DEFINING SECOND INTERFACE  FOR APP ****************************
    def Main_menu(self):  # defining menu function

        # ****************************--MAKING INTERFACE FOR MODULE FOR PRINCIPLE OF SOFTWARE ENGINEERING
        def Onclick_Software():
            # making the sub item for sub_btn2
            Main_interface.destroy()  # DESTROY THE MAIN INTERFACE FRAME

            # *********************APPLYING CONDITION TO DISPLAY CERTAIN MODULE IN SELECT TOP MENU
            if Select_menu.delete(0) == "Principle of Software Engineering":
                Select_menu.delete("Principle of Software Engineering")
            else:
                pass

            # ***********--- CREATING FRAME CALLED NEW MENU WHICH DEFINE GUI FOR PRINCIPLE OF SOFTWARE ENGINEERING

            new_menu = ttk.Frame()
            new_menu.pack(padx=10, pady=10)

            frame = Label(new_menu, text="PRINCIPLE OF SOFTWARE ENGINEERING", fg="green", font="Helvetica, 20")
            frame.pack(padx=10, pady=50)

            def Play_button():  # ---------DEFINING THE FUNCTION PLAY BUTTON

                new_menu.destroy()
                Play_frame = ttk.Frame()
                Play_frame.pack()
                Main_title = Label(Play_frame,
                                   text="QUIZ",
                                   font=("EB Garamond", 30, "bold"),
                                   fg="Green")
                Main_title.pack()

                Subject_title = Label(Play_frame,
                                      text="Principle of Software Engineering",
                                      font=("EB Garamond", 20, "bold"),
                                      fg="crimson")
                Subject_title.pack(pady=10)

                # ******************* PLAY GUI******************************
                Play_class = Play('Engineering')  # generating play class
                # # ********************* GUI END PLAY ***************************************

            def Sub_btn2CLick():
                # Defining the function for button Cancel
                # :: this button work as back button which will back to the Sub button
                def Add():
                    Add_question(self.root, "EngineeringQuestionBank")

                def delete():
                    Delete_question(self.root)

                def Cancel():
                    Edit_menu.destroy()
                    Onclick_Software()

                # this will destroy the new_menu and open edit menu
                new_menu.destroy()
                Edit_menu = ttk.Frame()
                Edit_menu.pack(pady=40)

                # button for edit menu
                Edit_Button = Frame(Edit_menu)
                Edit_header = Label(Edit_Button, text="EDIT", fg="Green", font="Aerial, 25")
                Edit_header.pack(side=TOP, pady=20)
                Add_button = Button(Edit_Button, text="Add Question", width=10, fg="Red", command=Add)
                Add_button.pack(pady=10)
                Delete_Button = Button(Edit_Button, text="Delete Question", width=10, fg="Red", command=delete)
                Delete_Button.pack(pady=10)
                Cancel_Button = Button(Edit_Button, text="Cancel", width=10, fg="Red", command=Cancel)
                Cancel_Button.pack(pady=10)
                Edit_Button.pack()

            def QUit_cmd():
                new_menu.destroy()
                self.Main_menu()

            Sub_button = ttk.Frame(new_menu)
            sub_btn1 = Button(Sub_button, text="Play", width=5, fg='red', command=Play_button)
            sub_btn1.pack(pady=10)
            sub_btn2 = Button(Sub_button, text="Edit", width=5, fg='red', command=Sub_btn2CLick)
            sub_btn2.pack(pady=10)
            sub_btn3 = Button(Sub_button, text="Quit", width=5, fg='red', command=QUit_cmd)
            sub_btn3.pack(pady=10)
            Sub_button.pack()

        # -------------------------------------------------------
        # *********************** Programming ***************************************** #######################

        def Onclick_Programming():
            # making the sub item for sub_btn2
            Main_interface.destroy()

            # ***********--- CREATING FRAME CALLED NEW MENU WHICH DEFINE GUI FOR PARADIGM OF PROGRAMMING

            new_menu = ttk.Frame()
            new_menu.pack(padx=10, pady=10)

            frame = Label(new_menu, text="PARADIGM OF PROGRAMMING", fg="green", font="Helvetica, 20")
            frame.pack(padx=10, pady=50)

            def Play_button():  # ---------DEFINING THE FUNCTION PLAY BUTTON
                new_menu.destroy()

                Play_frame = ttk.Frame()
                Play_frame.pack(pady=40)

                Main_title = Label(Play_frame, text="QUIZ", font=("EB Garamond", 35, "bold", "roman",), fg="Green")
                Main_title.pack(pady=10, padx=10)

                Subject_title = Label(Play_frame, text="Paradigm of Programming", font=("EB Garamond", 20, "bold"),
                                      fg="crimson")
                Subject_title.pack(pady=10)
                # ******************* MAKE GUI FOR PLAY HERE ******************************
                Play_class = Play('Programming')

                # ***** GUI END PLAY ***************************************

            def Sub_btn2CLick():
                # Defining the function for button Cancel
                # defining the function for the button add question
                def Add():
                    Add_question(self.root, "EngineeringQuestionBank")

                def delete():
                    Delete_question(self.root)

                # :: this button work as back button which will back to the Sub button

                def Cancel():
                    Edit_menu.destroy()
                    Onclick_Programming()

                # this will destroy the new_menu and open edit menu
                new_menu.destroy()
                Edit_menu = ttk.Frame()
                Edit_menu.pack()

                # button for edit menu
                Edit_Button = Frame(Edit_menu)
                Edit_header = Label(Edit_Button, text="EDIT", fg="Green", font="Aerial, 25")
                Edit_header.pack(side=TOP, pady=20)
                Add_button = Button(Edit_Button, text="Add Question", width=10, fg="Red", command=Add)
                Add_button.pack(pady=10)
                Delete_Button = Button(Edit_Button, text="Delete Question", width=10, fg="Red", command=delete)
                Delete_Button.pack(pady=10)
                Cancel_Button = Button(Edit_Button, text="Cancel", width=10, fg="Red", command=Cancel)
                Cancel_Button.pack(pady=10)
                Edit_Button.pack()

            def QUit_cmd():
                new_menu.destroy()
                self.Main_menu()

            Sub_button = ttk.Frame(new_menu)
            sub_btn1 = Button(Sub_button, text="Play", width=5, fg='red', command=Play_button)
            sub_btn1.pack(pady=10)
            sub_btn2 = Button(Sub_button, text="Edit", width=5, fg='red', command=Sub_btn2CLick)
            sub_btn2.pack(pady=10)
            sub_btn3 = Button(Sub_button, text="Quit", width=5, fg='red', command=QUit_cmd)
            sub_btn3.pack(pady=10)
            Sub_button.pack()

        def Onclick_Computer():
            # making the sub item for sub_btn2
            Main_interface.destroy()

            # ***********--- CREATING FRAME CALLED NEW MENU WHICH DEFINE GUI FOR COMPUTER AND COMMUNICATION SYSTEM

            new_menu = ttk.Frame()
            new_menu.pack(padx=10, pady=10)

            frame = Label(new_menu, text="COMPUTER AND COMMUNICATION SYSTEM", fg="green", font="Helvetica, 20")
            frame.pack(padx=10, pady=50)

            def Play_button():  # ---------DEFINING THE FUNCTION PLAY BUTTON

                new_menu.destroy()

                Play_frame = ttk.Frame()
                Play_frame.pack(pady=40)

                Main_title = Label(Play_frame, text="QUIZ", font=("EB Garamond", 30, "bold"), fg="Green")
                Main_title.pack()

                Subject_title = Label(Play_frame, text="Computer and Communication System",
                                      font=("EB Garamond", 20, "bold"),
                                      fg="crimson")
                Subject_title.pack(pady=10)
                # ******************* MAKE GUI FOR PLAY HERE ******************************
                Play_class = Play('Communication')

                # # ********************* GUI END PLAY ***************************************

            def Sub_btn2CLick():
                # Defining the function for button Cancel
                # :: this button work as back button which will back to the Sub button
                def Add():
                    Add_question(self.root, "EngineeringQuestionBank")

                def delete():
                    Delete_question(self.root)

                def Cancel():
                    Edit_menu.destroy()
                    Onclick_Computer()

                # this will destroy the new_menu and open edit menu
                new_menu.destroy()
                Edit_menu = ttk.Frame()
                Edit_menu.pack()

                # button for edit menu
                Edit_Button = Frame(Edit_menu)
                Edit_header = Label(Edit_Button, text="EDIT", fg="Green", font="Aerial, 25")
                Edit_header.pack(side=TOP, pady=20)
                Add_button = Button(Edit_Button, text="Add Question", width=10, fg="Red", command=Add)
                Add_button.pack(pady=10)
                Delete_Button = Button(Edit_Button, text="Delete Question", width=10, fg="Red", command=delete)
                Delete_Button.pack(pady=10)
                Cancel_Button = Button(Edit_Button, text="Cancel", width=10, fg="Red", command=Cancel)
                Cancel_Button.pack(pady=10)
                Edit_Button.pack()

            def QUit_cmd():
                new_menu.destroy()
                self.Main_menu()

            Sub_button = ttk.Frame(new_menu)
            sub_btn1 = Button(Sub_button, text="Play", width=5, fg='red', command=Play_button)
            sub_btn1.pack(pady=10)
            sub_btn2 = Button(Sub_button, text="Edit", width=5, fg='red')
            sub_btn2.bind("<Button-1>", Sub_btn2CLick)
            sub_btn2.pack(pady=10)
            sub_btn3 = Button(Sub_button, text="Quit", width=5, fg='red', command=QUit_cmd)
            sub_btn3.pack(pady=10)
            Sub_button.pack()

        def Onclick_Maths():
            # making the sub item for sub_btn2
            Main_interface.destroy()

            # ***********--- CREATING FRAME CALLED NEW MENU WHICH DEFINE GUI FOR MATHMATICS FOR COMPUTER SCIENCE

            new_menu = ttk.Frame(window)
            new_menu.pack(padx=10, pady=10)

            frame = Label(new_menu, text="MATHMATICS FOR COMPUTER SCIENCE", fg="green", font="Helvetica, 20")
            frame.pack(padx=10, pady=40)

            def Play_button():  # ---------DEFINING THE FUNCTION PLAY BUTTON

                new_menu.destroy()

                Play_frame = ttk.Frame()
                Play_frame.pack()

                Main_title = Label(Play_frame, text="QUIZ", font=("EB Garamond", 30, "bold"), fg="Green")
                Main_title.pack()

                Subject_title = Label(Play_frame, text="Mathmatics For Computer Science",
                                      font=("EB Garamond", 20, "bold"),
                                      fg="crimson")
                Subject_title.pack(pady=10)
                # ******************* MAKE GUI FOR PLAY HERE ******************************
                Play_class = Play('Mathematics')
                # # ********************* GUI END PLAY ***************************************

            def Sub_btn2CLick():
                # Defining the function for button Cancel
                # :: this button work as back button which will back to the Sub button
                def Add():
                    Add_question(self.root, "EngineeringQuestionBank")

                def delete():
                    Delete_question(self.root)

                def Cancel():
                    Edit_menu.destroy()
                    Onclick_Maths()

                # this will destroy the new_menu and open edit menu
                new_menu.destroy()
                Edit_menu = ttk.Frame()
                Edit_menu.pack()

                # button for edit menu
                Edit_Button = Frame(Edit_menu)
                Edit_header = Label(Edit_Button, text="EDIT", fg="Green", font="Aerial, 25")
                Edit_header.pack(side=TOP, pady=20)
                Add_button = Button(Edit_Button, text="Add Question", width=10, fg="Red", command=Add)
                Add_button.pack(pady=10)
                Delete_Button = Button(Edit_Button, text="Delete Question", width=10, fg="Red", command=delete)
                Delete_Button.pack(pady=10)
                Cancel_Button = Button(Edit_Button, text="Cancel", width=10, fg="Red", command=Cancel)
                Cancel_Button.pack(pady=10)
                Edit_Button.pack()

            def QUit_cmd():
                new_menu.destroy()
                self.Main_menu()

            Sub_button = ttk.Frame(new_menu)
            sub_btn1 = Button(Sub_button, text="Play", width=5, fg='red', command=Play_button)
            sub_btn1.pack(pady=10)
            sub_btn2 = Button(Sub_button, text="Edit", width=5, fg='red')
            sub_btn2.bind("<Button-1>", Sub_btn2CLick)
            sub_btn2.pack(pady=10)
            sub_btn3 = Button(Sub_button, text="Quit", width=5, fg='red', command=QUit_cmd)
            sub_btn3.pack(pady=10)
            Sub_button.pack()

        # Top bar menu
        def SE_select():
            Main_interface.destroy()
            Onclick_Software()

        def Programming_Select():
            Main_interface.destroy()
            Onclick_Programming()

        def Communication_Select():
            Main_interface.destroy()
            Onclick_Computer()

        def Mathmatics_Select():
            Main_interface.destroy()
            Onclick_Maths()

        Top_menu = Menu(self.root)
        # first menu Select
        Select_menu = Menu(Top_menu)
        Top_menu.add_cascade(label="Select", menu=Select_menu)
        Select_menu.add_command(label="Principle of Software Engineering", command=SE_select)
        Select_menu.add_command(label="Paradigm of Programming", command=Programming_Select)
        Select_menu.add_command(label="Computer and Communication System", command=Communication_Select)
        Select_menu.add_command(label="Mathmatics for Computer Science", command=Mathmatics_Select)

        # Second menu Read
        def Software():
            Read_window = Toplevel(window)
            a = open("Principle of Software Engineering.txt", 'r')
            # a.read()
            Label(Read_window, text=a.read()).pack()
            a.close()
            Read_window.mainloop()

        def programming():
            Read_window = Toplevel(window)
            a = open("Principle of Software Engineering.txt", 'r')
            # a.read()
            Label(Read_window, text=a.read()).pack()
            a.close()
            Read_window.mainloop()

        def computer():
            Read_window = Toplevel(window)
            a = open("Principle of Software Engineering.txt", 'r')
            # a.read()
            Label(Read_window, text=a.read()).pack()
            a.close()
            Read_window.mainloop()

        def maths():
            Read_window = Toplevel(window)
            a = open("Principle of Software Engineering.txt", 'r')
            # a.read()
            Label(Read_window, text=a.read()).pack()
            a.close()
            Read_window.mainloop()

        Read_menu = Menu(Top_menu)
        Top_menu.add_cascade(label="Read", menu=Read_menu)
        Read_menu.add_command(label="Principles of Software Engineering", command=Software)
        # Read_menu.add_separator()
        Read_menu.add_command(label="Paradigm of Programming", command=programming)
        Read_menu.add_command(label="Computer and Communication System", command=computer)
        Read_menu.add_command(label="Mathmatics for Computer Science", command=maths)

        def add_module():
            Add_Module(window)

        def delete_module():
            Delete_module(window)

        Edit_menu = Menu(Top_menu)
        Top_menu.add_cascade(label="Edit", menu=Edit_menu)
        Edit_menu.add_cascade(label="Add Module", command=add_module)
        Edit_menu.add_cascade(label="Delete Module", command=delete_module)

        self.root.config(menu=Top_menu)
        # ******************************** -- SECOND INTERFACE SOFTWARE -- ************************************

        # THIS IS THE MAIN INTERFACE WHICH CONTAIN ALL THE MAIN MENUS.

        # Making GUI for Main_Menu

        # --------------------- First defining the Frame for main_menu

        Main_interface = ttk.Frame(window)
        Main_interface.pack(pady=40)
        # Heading
        welcome_message = Label(Main_interface, text="HOME", font=('Ariel bold', 30), fg='Red')
        welcome_message.pack(side=TOP, padx=10, pady=10)
        # message for menu
        menu_message = Label(Main_interface, text="Choose the subject to take quiz", fg="green")
        menu_message.pack(side=TOP)

        # creating the menu
        menu = ttk.Frame(Main_interface)
        btn1 = Button(
            menu, text="Software Engineering", fg="black", width=30, height=2, highlightbackground="light green",
            command=Onclick_Software
        )
        btn1.pack(pady=15)
        btn2 = Button(menu, text="Paradigm of Programming", fg="black", width=30, highlightbackground="light green",
                      height=2,
                      command=Onclick_Programming
                      )
        btn2.pack(pady=15)
        btn3 = Button(menu, text="Computer and Communication system", fg="black", width=30,
                      highlightbackground="light green",
                      command=Onclick_Computer,
                      height=2)

        btn3.pack(pady=15)
        btn4 = Button(menu, text="Mathmatics for computer science", fg="black", highlightbackground="light green",
                      width=30, height=2, command=Onclick_Maths)
        btn4.pack(pady=15)
        menu.pack(pady=20)


window = tk.Tk()
my_gui = GUI(window, "UQuiz")
window.geometry("800x800")
window.mainloop()
