import sqlite3

import Quiz
import Quiz as q

conn = sqlite3.connect("question_bank12.db")
# conn = question_bank12.connect(question_bank12.db)
c = conn.cursor()


def creating_module_tables():
    q.module_table.create_module_table("CommunicationQuestionbank")
    q.module_table.create_module_table("EngineeringQuestionbank")
    q.module_table.create_module_table("MathsQuestionbank")
    q.module_table.create_module_table("PythonQuestionbank")

    q.module_table.create_answer_table("AnswersCommunicationQuestionbank")
    q.module_table.create_answer_table("AnswersEngineeringQuestionbank")
    q.module_table.create_answer_table("AnswersMathsQuestionbank")
    q.module_table.create_answer_table("AnswersPythonQuestionbank")


def add_question_to_database(x):
    questions_path = "questionbanktexts/" + x + ".txt"

    def load_questions(path=questions_path):
        questions = []
        with open(path, 'r') as h:
            for line in h.readlines():
                words = line.split(',')
                module = words[0]
                no = int(words[1])
                typep = words[2].strip('\n').strip('\'')
                text = words[-1].strip('\n').strip('\'')
                q.module_table.add_question(x, module, no, typep,
                                            text)

    load_questions()
    print("Questions added successfully...")


def add_answers_to_database(x):
    answer_path = "answerquestionbanktexts/" + x + ".txt"

    def load_answers(path=answer_path):
        questions = []
        with open(path, 'r') as h:
            for line in h.readlines():
                words = line.split(',')
                module = words[0]
                no = int(words[1])
                typep = words[2].strip('\n').strip('\'')
                answer0 = words[3].strip('\n').strip('\'')
                answer1 = words[4].strip('\n').strip('\'')
                answer2 = words[5].strip('\n').strip('\'')
                answer3 = words[-1].strip('\n').strip('\'')
                q.module_table.add_answer(x, module, no, typep,
                                          answer0, answer1, answer2, answer3)

    load_answers()
    print("Questions added successfully...")



# creating_module_tables()


# Resetting and updating the Database for any changes made - by delteing the table and creating new one and filling it up with the new/updated questions/answersx
q.module_table.delete_table("AnswersCommunicationQuestionbank")
q.module_table.create_answer_table("AnswersCommunicationQuestionbank")
add_answers_to_database("AnswersCommunicationQuestionbank")

# q.module_table.create_answer_table("AnswersPythonQuestionbank")
q.module_table.delete_table("AnswersProgrammingQuestionbank")
q.module_table.create_answer_table("AnswersProgrammingQuestionbank")
add_answers_to_database("AnswersProgrammingQuestionbank")

q.module_table.delete_table("AnswersEngineeringQuestionbank")
q.module_table.create_answer_table("AnswersEngineeringQuestionbank")
add_answers_to_database("AnswersEngineeringQuestionbank")


q.module_table.delete_table("AnswersMathematicsQuestionbank")
q.module_table.create_answer_table("AnswersMathematicsQuestionbank")
add_answers_to_database("AnswersMathematicsQuestionbank")



q.module_table.delete_table("MathematicsQuestionbank")
q.module_table.create_module_table("MathematicsQuestionbank")
add_question_to_database("MathematicsQuestionbank")

q.module_table.delete_table("ProgrammingQuestionbank")
q.module_table.create_module_table("ProgrammingQuestionbank")
add_question_to_database("ProgrammingQuestionbank")

q.module_table.delete_table("CommunicationQuestionbank")
q.module_table.create_module_table("CommunicationQuestionbank")
add_question_to_database("CommunicationQuestionbank")

q.module_table.delete_table("EngineeringQuestionbank")
q.module_table.create_module_table("EngineeringQuestionbank")
add_question_to_database("EngineeringQuestionbank")


