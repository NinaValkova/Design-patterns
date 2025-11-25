class QuestionManager:
    def __init__(self, catalog, question):
        self.catalog = catalog
        self.question = question

    def next(self):
        self.question.next_question()

    def previous(self):
        self.question.previous_question()

    def new_one(self, quest):
        self.question.new_question(quest)

    def delete(self, quest):
        self.question.delete_question(quest)

    def display_quest(self):
        self.question.display_question()

    def display(self):
        print(f"Question paper: {self.catalog}")   
        self.question.display_all_questions()
