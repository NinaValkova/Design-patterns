from question import Question


class JavaQuestions(Question):
    def __init__(self):
        self.questions = [
            "What is class?",
            "What is interface?",
            "What is abstraction?",
            "How multiple polymorphism is achieved in Java?",
            "How many types of exception handling are there in Java?",
            "Define the keyword final for variables, method, and class in Java?",
            "What is abstract class?",
            "What is multi-threading?",
        ]
        self.current = 0

    def next_question(self):
        if self.current < len(self.questions) - 1:
            self.current += 1

    def previous_question(self):
        if self.current > 0:
            self.current -= 1

    def new_question(self, question: str):
        self.questions.append(question)

    def delete_question(self, question: str):
        size = len(self.questions)
        
        i=0
        while i < len(self.questions):
            if self.questions[i] == question:
                # pop() returns the removed element.
                self.questions.pop(i)  # removes element at i
            else:
                i += 1

    def display_question(self):
        print(self.questions[self.current])

    def display_all_questions(self):
        for q in self.questions:
            print(q)
