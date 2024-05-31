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

        self.create_table()
        self.add_module("1179", "Mathematics for Computer Scicence")
        self.add_module("1821", "Principles of Software Engineering")
        self.add_module("1811", "Paradigms of Programming")
        self.add_module("1765", "Computer and Communication Systems")

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def create_table(self):
        """create a table
        input:none
        output:modules.db"""

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

        # connect to a database
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()

        c.execute("DELETE from modules WHERE rowid = (?)", str(x))

        # commit our command
        conn.commit()
        # close our command
        conn.close()

    def delete_table(self):
        conn = sqlite3.connect("question_bank12.db")
        # create Cursor
        c = conn.cursor()
        c.execute("DROP TABLE modules")
        conn.commit()
        # close our command
        conn.close()


# 1) It is inside a Class. first create an Instance of a class
module_table = Module("0", "0")

# 2) Then create a Table & add modules
# module_table.setting_up()

# 3) Print modules
module_table.print_modules()



# # 4) other functions are here
# module_table.add_module("1234", "A new module added")
# module_table.find_module("Programming")
# module_table.update_module("Programming", "NEW MODULE UPDATED FROM Programming" )
# module_table.print_modules()

# If module TABLE already exists delete and create a new one using this sequence
# module_table.delete_table()
# module_table.setting_up()


class questions(Module):
    def __init__(self, module_name, question_bank):
        super().__init__(self, module_name)
        self.module_name = module_name
        self.question_bank = question_bank

    def setting_up(self):
        # connecting to database
        conn = sqlite3.connect("question_bank12.db")
        # creating cursor
        c = conn.cursor()

