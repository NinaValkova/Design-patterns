from java_question import JavaQuestions
from question_format import QuestionFormat

if __name__ == "__main__":
    question = JavaQuestions()
    question_format = QuestionFormat("Java Programming Lnguage", question)

    question_format.next()
    question_format.display_quest()

    question_format.delete("What is class?")

    question_format.new_one("What is inheritance?")
    question_format.new_one("How many types of inheritance are there in Java?")

    question_format.display_all()
