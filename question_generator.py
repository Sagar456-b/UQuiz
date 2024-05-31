import sqlite3
import Quiz as q
import random

print("-------------------------------\n\n\n\n")

# These two lists represents the data that needs to be read in and transfored into the amount of different variables
Qs_asked = []
num_list = [0, 1, 2, 3, 4]
score = 0
module_selected = None

def anyname():
    """

    :return: Generates
    """
    for r in range(len(num_list)):
        Qs_asked.append(r)

    print("QSA", Qs_asked)
    print("NUM", num_list)


def checker(random_q):
    # print("length is ", 4)
    # print("Random number is ", random_q)
    value1 = False
    for r in range(len(num_list)):
        if random_q == r:
            for j in Qs_asked:
                if j == r:
                    # print("This number has already been added")
                    # print(Qs_asked)
                    return Qs_asked

            # print("YES YOUR NUMBER IS ", random_q)
            Qs_asked.append(random_q)
            value1 = True
            # print(Qs_asked)
            return True

        # elif random_q != r:
        #     print(r, "NO")


modules = ["Mathematics", "Engineering", "Programming", "Communication"]


def play_button():



    # Start/Prompting
    global module_selected
    print("Welcome to the Quiz \n", "Here are the Modules Availabale to study : \n")
    for m in modules:
        print(m)

    x = input("\nPut in the module like to study? : ")
    value = False

    for m in modules:
        if m == x:
            value = True
            module_selected = x
            print("\n\nYou have selected Module : ", m)

    if value == True:
        print("\nModule ", x, " is Correct.\nYou are now inside the *", x, "* Quiz now!")
        Quizzing(module_selected)

    else:
        print("\n\nInvalid Module")


def Quizzing(x):
    score = 0
    # connect to a database
    conn = sqlite3.connect("question_bank12.db")
    # create Cursor
    c = conn.cursor()

    x = module_selected



    while len(Qs_asked) < 5:
        # print(len(Qs_asked))
        a = random.randint(0, 4)

        if checker(a) == True:
            print("\n\n\n !!!!!Question ", "!!!")
            c.execute(" SELECT HEADER FROM " + module_selected + "Questionbank WHERE NO = " + str(a) + ";")
            print(c.fetchone())
            answer = input("Answer")
            c.execute(" SELECT ANSWER0 FROM Answers" + module_selected + "Questionbank WHERE NO = " + str(a) + ";")
            correct_answer = (c.fetchone()[0]).translate({ord('"'): None})
            if str(correct_answer) == answer:
                score += 1
                print("U GOT IT RIGHT")



    # commit our command
    conn.commit()
    # close our command
    conn.close()

    print("Your score was", score, "/5")



def play_button2(y):



    # Start/Prompting
    global module_selected
    print("Welcome to the Quiz \n", "Here are the Modules Availabale to study : \n")
    for m in modules:
        print(m)

    x = input("\nPut in the module like to study? : ")
    value = False

    for m in modules:
        if m == x:
            value = True
            module_selected = x
            print("\n\nYou have selected Module : ", m)

    if value == True:
        print("\nModule ", x, " is Correct.\nYou are now inside the *", x, "* Quiz now!")
        Quizzing(y)

    else:
        print("\n\nInvalid Module")







# Quizzing()
#
# 1179|Mathematics
# 1821|Engineering
# 1811|Programming
# 1765|Communication Systems
# checker(random.randint(0, 4))
# random_number = random.randint(0, 4)


# # play_button()
play_button2("Mathematics")
# play_button2("Engineering")
# play_button2("Programming")
# play_button2("Communication")


