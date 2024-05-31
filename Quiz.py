import sqlite3


class Module:
    def __init__(self, module_code, module_name):
        self.module_code = module_code
        self.module_name = module_name

    def setting_up(self):
        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        # self.create_table()
        self.add_module("1179", "Mathematics")
        self.add_module("1821", "Engineering")
        self.add_module("1811", "Programming")
        self.add_module("1765", "Communication Systems")

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def create_main_table(self, main_table_name):
        """create the table to hold modules
        input:table_name
        output:modules.db"""
        self.main_table_name = main_table_name
        table_name = (main_table_name,)

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("""CREATE TABLE modules(
                        module_code text,
                        module_name text
                )""")

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def create_module_table(self, md_table_name):
        """create the table to hold modules
        input:md_table_name
        output: a table created inside question_bank12.db"""

        self.md_table_name = md_table_name
        print(type(md_table_name))
        print(type(self.md_table_name))

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        # c.execute("CREATE TABLE " + md_table_name + "(moduldffe_code text, module_naggfme text)")
        c.execute("""CREATE TABLE """ + self.md_table_name + """(
                        MODULE text ,
                        NO integer,
                        TYPE text,
                        HEADER text
                )""")
        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def create_answer_table(self, md_table_name):
        """create the table to hold modules
        input:md_table_name
        output: a table created inside question_bank12.db"""

        self.md_table_name = md_table_name
        print(type(md_table_name))
        print(type(self.md_table_name))

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        # c.execute("CREATE TABLE " + md_table_name + "(moduldffe_code text, module_naggfme text)")
        c.execute("""CREATE TABLE """ + self.md_table_name + """(
                        MODULE text ,
                        NO integer,
                        TYPE text,
                        ANSWER0 text,
                        ANSWER1 text,
                        ANSWER2 text,
                        ANSWER3 text
                )""")
        # commit our command
        conn.commit()
        # close our command
        conn.close()


    def add_module(self, x, y):
        """A function that will add a module/ modules"""
        self.x = x
        self.y = y

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("INSERT INTO modules VALUES (?,?)", (x, y))

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def add_answer(self, module_name, x, y, z, w, a, b, d):
        """A function that will add a module/ modules"""
        self.module_name = module_name
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.a = a
        self.b = b
        self.d = d


        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("INSERT INTO " + module_name + " VALUES (?,?,?,?,?,?,?)", (x, y, z, w, a, b, d))
        print("ANSWERS ADDED SUCCESSFULLY to..." + module_name)

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def add_question(self, module_name, x, y, z, w, ):
        """A function that will add a module/ modules
        module_name = module name
        x = question number
        y = type of question
        z = Question
        w = Answer"""
        self.module_name = module_name
        self.x = x
        self.y = y
        self.z = z
        self.w = w

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("INSERT INTO " + module_name + " VALUES (?,?,?,?)", (x, y, z, w))
        print("ADDED SUCCESFULLY")

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def delete_question(self, x):
        """A function that will add a module/ modules"""
        self.x = x

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()
        # SELECT rowid, * FROM CommunicationQuestionBank WHERE rowid = 1 ;

        c.execute("DELETE FROM MathematicsQuestionBank WHERE rowid =  " + str(x))
        print("DELETED SUCCESFULLY")

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def print_modules(self):
        """rowid shows the ID number of the row
        this function prints modules
        input:none
        output:item"""

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM modules")
        print("ROW ID", "\tMODULES NAME", "\t COURSE NUMBER")
        items = c.fetchall()
        for item in items:
            print(item)
        print(c.fetchall())

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def find_module(self, x):
        """Finding a module
    You can also use LIKE for less accurate
    input: name of the module
    output: data of the module"""
        self.x = x

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()
        c.execute("SELECT * FROM modules WHERE module_name = '" + x + "'")
        print(c.fetchall())

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def update_module(self, x, y):
        """X = module you want to update
           Y = new module name"""
        self.x = x
        self.y = y

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("UPDATE modules SET module_name = '" + y + "' " \
                                                             "WHERE module_name = '" + x + "'")

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def delete_module(self, x):
        """deleting a module
        input:modula name in string
        output: deleted module - NONE"""
        self.x = x
        print("DELETING")


        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()


        c.execute("DELETE from modules WHERE module_name LIKE '" + x + "%';")

        # commit our command
        conn.commit()
        # close our command
        conn.close()

        print("DELETING")

    def delete_table(self, delete_table_name):
        self.delete_table_name = delete_table_name

        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("DROP TABLE " + delete_table_name)
        conn.commit()
        # close our command
        conn.close()


# 1) It is inside a Class. first create an Instance of a class
module_table = Module("0", "0")

# 2) Then create a Table & add modules
# module_table.setting_up()

# 3) Print modules
# module_table.print_modules()
#
# # 4) other functions are here
# module_table.add_module("1234", "A new module added")
# module_table.find_module("Programming")
# module_table.update_module("Programming", "NEW MODULE UPDATED FROM Programming" )
module_table.print_modules()

# If module TABLE already exists delete and create a new one using this sequence
# module_table.delete_table()
# module_table.setting_up()




